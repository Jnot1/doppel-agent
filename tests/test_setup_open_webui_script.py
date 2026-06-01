"""Regression tests for Open WebUI bootstrap naming and home resolution."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SETUP_OPEN_WEBUI_SH = REPO_ROOT / "scripts" / "setup_open_webui.sh"


def _extract_function_body(name: str) -> str:
    text = SETUP_OPEN_WEBUI_SH.read_text(encoding="utf-8")
    match = re.search(
        rf"^{name}\(\)\s*\{{\s*\n(?P<body>.*?)^\}}",
        text,
        re.MULTILINE | re.DOTALL,
    )
    assert match is not None, f"Could not locate {name}() in scripts/setup_open_webui.sh"
    return match["body"]


def _run_resolve_agent_env_file(
    tmp_path: Path,
    *,
    precreate_doppel: bool = False,
    precreate_legacy: bool = False,
    extra_env_lines: list[str] | None = None,
) -> subprocess.CompletedProcess[str]:
    home = tmp_path / "home"
    home.mkdir()
    if precreate_doppel:
        (home / ".doppel").mkdir()
    if precreate_legacy:
        (home / ".hermes").mkdir()

    env_lines = extra_env_lines or []
    script = "\n".join(
        [
            "set -e",
            f'HOME="{home}"',
            "unset DOPPEL_ENV_FILE",
            "unset HERMES_ENV_FILE",
            "unset DOPPEL_HOME",
            "unset HERMES_HOME",
            *env_lines,
            'HERMES_ENV_FILE=""',
            'AGENT_HOME_DIR=""',
            'LOG_DIR=""',
            "resolve_agent_env_file() {",
            _extract_function_body("resolve_agent_env_file"),
            "}",
            "resolve_agent_env_file",
            'printf "ENV=%s\\nHOME_DIR=%s\\nLOG_DIR=%s\\n" "$HERMES_ENV_FILE" "$AGENT_HOME_DIR" "$LOG_DIR"',
        ]
    )
    return subprocess.run(
        ["bash", "-c", script],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )


def test_resolve_agent_env_file_defaults_to_doppel_home_on_fresh_install(tmp_path: Path) -> None:
    result = _run_resolve_agent_env_file(tmp_path)

    expected_home = tmp_path / "home"
    assert result.returncode == 0, result.stderr
    assert f"ENV={expected_home / '.doppel' / '.env'}" in result.stdout
    assert f"HOME_DIR={expected_home / '.doppel'}" in result.stdout
    assert f"LOG_DIR={expected_home / '.doppel' / 'logs'}" in result.stdout


def test_resolve_agent_env_file_preserves_existing_legacy_home(tmp_path: Path) -> None:
    result = _run_resolve_agent_env_file(tmp_path, precreate_legacy=True)

    expected_home = tmp_path / "home"
    assert result.returncode == 0, result.stderr
    assert f"ENV={expected_home / '.hermes' / '.env'}" in result.stdout
    assert f"HOME_DIR={expected_home / '.hermes'}" in result.stdout
    assert f"LOG_DIR={expected_home / '.hermes' / 'logs'}" in result.stdout


def test_resolve_agent_env_file_prefers_explicit_doppel_env_file(tmp_path: Path) -> None:
    custom_env = tmp_path / "custom-home" / ".env"
    result = _run_resolve_agent_env_file(
        tmp_path,
        precreate_legacy=True,
        extra_env_lines=[f'DOPPEL_ENV_FILE="{custom_env}"'],
    )

    assert result.returncode == 0, result.stderr
    assert f"ENV={custom_env}" in result.stdout
    assert f"HOME_DIR={custom_env.parent}" in result.stdout
    assert f"LOG_DIR={custom_env.parent / 'logs'}" in result.stdout


def test_write_legacy_launcher_shim_forwards_to_doppel_launcher(tmp_path: Path) -> None:
    shell_quote_body = _extract_function_body("shell_quote")
    shim_body = _extract_function_body("write_legacy_launcher_shim")
    launcher_dir = tmp_path / "bin dir"
    current_launcher = launcher_dir / "start-open-webui-doppel.sh"
    legacy_launcher = launcher_dir / "start-open-webui-hermes.sh"

    script = "\n".join(
        [
            "set -e",
            f'LAUNCHER_PATH="{current_launcher}"',
            f'LEGACY_LAUNCHER_PATH="{legacy_launcher}"',
            "shell_quote() {",
            shell_quote_body,
            "}",
            "write_legacy_launcher_shim() {",
            shim_body,
            "}",
            "write_legacy_launcher_shim",
        ]
    )
    result = subprocess.run(
        ["bash", "-c", script],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    shim = legacy_launcher.read_text(encoding="utf-8")
    assert f"exec '{current_launcher}' \"$@\"" in shim
