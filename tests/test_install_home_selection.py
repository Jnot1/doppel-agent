"""Migration-focused tests for installer home selection.

These pin the compatibility window before we touch installer layout/name
changes:

- Fresh installs default to the new ``~/.doppel`` home.
- Existing ``~/.hermes`` installs are preserved in place.
- Explicit env overrides still win over legacy auto-detection.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_SH = REPO_ROOT / "scripts" / "install.sh"
INSTALL_PS1 = REPO_ROOT / "scripts" / "install.ps1"


def _extract_install_sh_home_selection_block() -> str:
    text = INSTALL_SH.read_text(encoding="utf-8")
    match = re.search(
        r'(?P<block>DEFAULT_DOPPEL_HOME="\$HOME/\.doppel".*?export HERMES_HOME)',
        text,
        re.DOTALL,
    )
    assert match is not None, "Could not locate install.sh home-selection block"
    return match["block"]


def _run_install_sh_home_selection(
    tmp_path: Path,
    *,
    doppel_home: str | None = None,
    hermes_home: str | None = None,
    legacy_repo: bool = False,
    legacy_config: bool = False,
    legacy_env_file: bool = False,
) -> tuple[str, str]:
    home = tmp_path / "home"
    home.mkdir()
    legacy_root = home / ".hermes"
    if legacy_repo:
        (legacy_root / "hermes-agent" / ".git").mkdir(parents=True)
    if legacy_config:
        legacy_root.mkdir(parents=True, exist_ok=True)
        (legacy_root / "config.yaml").write_text("model: test\n", encoding="utf-8")
    if legacy_env_file:
        legacy_root.mkdir(parents=True, exist_ok=True)
        (legacy_root / ".env").write_text("OPENAI_API_KEY=test\n", encoding="utf-8")

    env_lines = [
        "unset DOPPEL_HOME",
        "unset HERMES_HOME",
    ]
    if doppel_home is not None:
        env_lines.append(f'export DOPPEL_HOME="{doppel_home}"')
    if hermes_home is not None:
        env_lines.append(f'export HERMES_HOME="{hermes_home}"')

    script = "\n".join(
        [
            "set -e",
            f'export HOME="{home}"',
            'PACKAGE_DISTRIBUTION_NAME="hermes-agent"',
            'MANAGED_CHECKOUT_DIR_NAME="$PACKAGE_DISTRIBUTION_NAME"',
            *env_lines,
            _extract_install_sh_home_selection_block(),
            'printf "HERMES_HOME=%s\\n" "$HERMES_HOME"',
            'printf "DOPPEL_HOME=%s\\n" "$DOPPEL_HOME"',
        ]
    )
    result = subprocess.run(
        ["bash", "-c", script],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    values: dict[str, str] = {}
    for line in result.stdout.splitlines():
        key, _, value = line.partition("=")
        values[key] = value
    return values["HERMES_HOME"], values["DOPPEL_HOME"]


def test_install_sh_fresh_install_defaults_to_doppel_home(tmp_path: Path) -> None:
    hermes_home, doppel_home = _run_install_sh_home_selection(tmp_path)

    expected = str(tmp_path / "home" / ".doppel")
    assert hermes_home == expected
    assert doppel_home == expected


def test_install_sh_preserves_legacy_repo_home(tmp_path: Path) -> None:
    hermes_home, doppel_home = _run_install_sh_home_selection(
        tmp_path,
        legacy_repo=True,
    )

    expected = str(tmp_path / "home" / ".hermes")
    assert hermes_home == expected
    assert doppel_home == expected


def test_install_sh_preserves_legacy_config_home(tmp_path: Path) -> None:
    hermes_home, doppel_home = _run_install_sh_home_selection(
        tmp_path,
        legacy_config=True,
    )

    expected = str(tmp_path / "home" / ".hermes")
    assert hermes_home == expected
    assert doppel_home == expected


def test_install_sh_doppel_home_override_beats_legacy_auto_detection(tmp_path: Path) -> None:
    custom = tmp_path / "custom-doppel-home"
    hermes_home, doppel_home = _run_install_sh_home_selection(
        tmp_path,
        doppel_home=str(custom),
        legacy_repo=True,
        legacy_config=True,
        legacy_env_file=True,
    )

    assert hermes_home == str(custom)
    assert doppel_home == str(custom)


def test_install_ps1_prefers_doppel_home_then_legacy_then_default() -> None:
    text = INSTALL_PS1.read_text(encoding="utf-8")

    doppel_idx = text.find("if ($env:DOPPEL_HOME)")
    hermes_idx = text.find("} elseif ($env:HERMES_HOME) {")
    legacy_idx = text.find('} elseif ((Test-Path (Join-Path $LegacyHermesHome $ManagedCheckoutName))')
    default_idx = text.find("} else {\n        $HermesHome = $DefaultDoppelHome")

    assert -1 not in {doppel_idx, hermes_idx, legacy_idx, default_idx}
    assert doppel_idx < hermes_idx < legacy_idx < default_idx


def test_install_ps1_keeps_legacy_checkout_dir_name_for_in_place_upgrade() -> None:
    text = INSTALL_PS1.read_text(encoding="utf-8")

    assert '$PackageDistributionName = "hermes-agent"' in text
    assert '$ManagedCheckoutName = $PackageDistributionName' in text
    assert '$InstallDir = Join-Path $HermesHome $ManagedCheckoutName' in text


def test_install_ps1_exports_both_home_env_vars() -> None:
    text = INSTALL_PS1.read_text(encoding="utf-8")

    assert '$env:DOPPEL_HOME = $HermesHome' in text
    assert '$env:HERMES_HOME = $HermesHome' in text


def test_install_ps1_prefers_doppel_exe_before_hermes_exe_fallback() -> None:
    text = INSTALL_PS1.read_text(encoding="utf-8")

    doppel_idx = text.find('$hermesCmd = "$InstallDir\\venv\\Scripts\\doppel.exe"')
    hermes_idx = text.find('$hermesCmd = "$InstallDir\\venv\\Scripts\\hermes.exe"')
    fallback_idx = text.find('$hermesCmd = "doppel"')

    assert -1 not in {doppel_idx, hermes_idx, fallback_idx}
    assert doppel_idx < hermes_idx < fallback_idx
