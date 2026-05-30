"""Regression tests for explicit managed-checkout migration in install.sh.

This phase no longer accepts "reuse the old path forever" as the end state.
When an existing managed checkout still lives at ``$HERMES_HOME/hermes-agent``
and the preferred ``$HERMES_HOME/doppel-agent`` path is absent, the installer
should migrate the checkout forward before updating it in place.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_SH = REPO_ROOT / "scripts" / "install.sh"


def _extract_migrate_checkout_body() -> str:
    text = INSTALL_SH.read_text(encoding="utf-8")
    match = re.search(
        r"^migrate_managed_checkout_dir\(\)\s*\{\s*\n(?P<body>.*?)^\}",
        text,
        re.MULTILINE | re.DOTALL,
    )
    assert match is not None, "Could not locate migrate_managed_checkout_dir() in scripts/install.sh"
    return match["body"]


def _run_checkout_migration(tmp_path: Path) -> tuple[Path, Path, str]:
    hermes_home = tmp_path / "home" / ".hermes"
    legacy_checkout = hermes_home / "hermes-agent"
    current_checkout = hermes_home / "doppel-agent"
    (legacy_checkout / ".git").mkdir(parents=True)
    (legacy_checkout / "README.md").write_text("legacy checkout\n", encoding="utf-8")

    script = "\n".join(
        [
            "set -e",
            'log_info() { :; }',
            'log_warn() { :; }',
            'log_error() { printf "%s\\n" "$*" >&2; }',
            f'HERMES_HOME="{hermes_home}"',
            'MANAGED_CHECKOUT_DIR_NAME="doppel-agent"',
            'LEGACY_MANAGED_CHECKOUT_DIR_NAME="hermes-agent"',
            'INSTALL_DIR="$HERMES_HOME/$LEGACY_MANAGED_CHECKOUT_DIR_NAME"',
            "migrate_managed_checkout_dir() {",
            _extract_migrate_checkout_body(),
            "}",
            "migrate_managed_checkout_dir",
            'printf "INSTALL_DIR=%s\\n" "$INSTALL_DIR"',
        ]
    )
    result = subprocess.run(
        ["bash", "-c", script],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    return legacy_checkout, current_checkout, result


def test_install_sh_migrates_legacy_checkout_dir_to_doppel_name(tmp_path: Path) -> None:
    legacy_checkout, current_checkout, result = _run_checkout_migration(tmp_path)

    assert result.returncode == 0, result.stderr
    assert not legacy_checkout.exists()
    assert (current_checkout / ".git").exists()
    assert (current_checkout / "README.md").read_text(encoding="utf-8") == "legacy checkout\n"
    assert f"INSTALL_DIR={current_checkout}" in result.stdout
