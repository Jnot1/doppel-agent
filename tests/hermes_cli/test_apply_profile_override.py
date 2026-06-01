"""Regression tests for _apply_profile_override home-env guard (issue #22502).

When DOPPEL_HOME or HERMES_HOME is set to the root directory (for example a
service unit hardcodes ``DOPPEL_HOME=/root/.doppel``), _apply_profile_override
must still read ``active_profile`` and redirect both env vars to the named
profile directory.

When either env var already points to ``.../profiles/<name>``,
_apply_profile_override must trust it and return without re-reading
``active_profile`` (child-process inheritance contract).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _capture_home_env() -> tuple[str | None, str | None]:
    return os.environ.get("DOPPEL_HOME"), os.environ.get("HERMES_HOME")


def _restore_home_env(doppel_home: str | None, hermes_home: str | None) -> None:
    if doppel_home is None:
        os.environ.pop("DOPPEL_HOME", None)
    else:
        os.environ["DOPPEL_HOME"] = doppel_home

    if hermes_home is None:
        os.environ.pop("HERMES_HOME", None)
    else:
        os.environ["HERMES_HOME"] = hermes_home


def _run_apply_profile_override(
    tmp_path,
    monkeypatch,
    *,
    root_dir_name: str = ".hermes",
    doppel_home: str | None = None,
    hermes_home: str | None,
    active_profile: str | None,
    argv: list[str] | None = None,
):
    """Run _apply_profile_override in isolation.

    Returns ``(DOPPEL_HOME, HERMES_HOME)`` after the call.
    """
    hermes_root = tmp_path / root_dir_name
    hermes_root.mkdir(parents=True, exist_ok=True)

    if active_profile is not None:
        (hermes_root / "active_profile").write_text(active_profile)

    if active_profile and active_profile != "default":
        (hermes_root / "profiles" / active_profile).mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    if doppel_home is not None:
        monkeypatch.setenv("DOPPEL_HOME", doppel_home)
    else:
        monkeypatch.delenv("DOPPEL_HOME", raising=False)
    if hermes_home is not None:
        monkeypatch.setenv("HERMES_HOME", hermes_home)
    else:
        monkeypatch.delenv("HERMES_HOME", raising=False)

    original_doppel_home, original_hermes_home = _capture_home_env()
    try:
        monkeypatch.setattr(sys, "argv", argv or ["hermes", "gateway", "start"])

        from hermes_cli.main import _apply_profile_override
        _apply_profile_override()
        return os.environ.get("DOPPEL_HOME"), os.environ.get("HERMES_HOME")
    finally:
        _restore_home_env(original_doppel_home, original_hermes_home)


class TestApplyProfileOverrideHermesHomeGuard:
    """Regression guard for issue #22502.

    Verifies that HERMES_HOME pointing to the hermes root does NOT suppress
    the active_profile check, while HERMES_HOME already pointing to a
    profile directory IS trusted as-is.
    """

    def test_hermes_home_at_root_with_active_profile_is_redirected(
        self, tmp_path, monkeypatch
    ):
        """HERMES_HOME=/root/.hermes + active_profile=coder must redirect
        HERMES_HOME to .../profiles/coder.

        Bug scenario from #22502: systemd sets HERMES_HOME to the hermes root
        and the user switches to a profile via `hermes profile use`.
        Before the fix, the guard returned early and active_profile was ignored.
        """
        hermes_root = tmp_path / ".hermes"
        hermes_root.mkdir(parents=True, exist_ok=True)

        doppel_result, hermes_result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            hermes_home=str(hermes_root),
            active_profile="coder",
        )

        assert hermes_result is not None, "HERMES_HOME must be set after profile redirect"
        assert doppel_result == hermes_result
        assert "profiles" in hermes_result, (
            f"Expected HERMES_HOME to point into profiles/ dir, got: {hermes_result!r}"
        )
        assert hermes_result.endswith("coder"), (
            f"Expected HERMES_HOME to end with 'coder', got: {hermes_result!r}"
        )

    def test_hermes_home_already_profile_dir_is_trusted(self, tmp_path, monkeypatch):
        """HERMES_HOME=.../profiles/coder must not be overridden even when
        active_profile says something different.

        Preserves the child-process inheritance contract: a subprocess spawned
        with HERMES_HOME already set to a specific profile must stay in that
        profile.
        """
        hermes_root = tmp_path / ".hermes"
        profile_dir = hermes_root / "profiles" / "coder"
        profile_dir.mkdir(parents=True, exist_ok=True)

        doppel_result, hermes_result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            hermes_home=str(profile_dir),
            active_profile="other",
        )

        assert doppel_result == str(profile_dir)
        assert hermes_result == str(profile_dir), (
            "HERMES_HOME must remain unchanged when already pointing to a profile dir"
        )

    def test_hermes_home_unset_reads_active_profile(self, tmp_path, monkeypatch):
        """Classic case: HERMES_HOME unset + active_profile=coder must set
        HERMES_HOME to the profile directory (existing behaviour must not regress).
        """
        doppel_result, hermes_result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            root_dir_name=".doppel",
            hermes_home=None,
            active_profile="coder",
        )

        assert hermes_result is not None
        assert "coder" in hermes_result
        assert doppel_result == hermes_result

    def test_hermes_home_unset_default_profile_no_redirect(self, tmp_path, monkeypatch):
        """active_profile=default must not redirect HERMES_HOME."""
        doppel_result, hermes_result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            root_dir_name=".doppel",
            hermes_home=None,
            active_profile="default",
        )

        assert doppel_result is None
        assert hermes_result is None

    def test_doppel_home_at_root_with_active_profile_is_redirected(
        self, tmp_path, monkeypatch
    ):
        doppel_root = tmp_path / ".doppel"
        doppel_root.mkdir(parents=True, exist_ok=True)

        doppel_result, hermes_result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            root_dir_name=".doppel",
            doppel_home=str(doppel_root),
            hermes_home=None,
            active_profile="coder",
        )

        assert doppel_result is not None
        assert hermes_result == doppel_result
        assert doppel_result.endswith("coder")

    def test_doppel_home_already_profile_dir_is_trusted(self, tmp_path, monkeypatch):
        doppel_root = tmp_path / ".doppel"
        profile_dir = doppel_root / "profiles" / "coder"
        profile_dir.mkdir(parents=True, exist_ok=True)

        doppel_result, hermes_result = _run_apply_profile_override(
            tmp_path,
            monkeypatch,
            root_dir_name=".doppel",
            doppel_home=str(profile_dir),
            hermes_home=None,
            active_profile="other",
            argv=["doppel", "gateway", "start"],
        )

        assert doppel_result == str(profile_dir)
        assert hermes_result == str(profile_dir)
