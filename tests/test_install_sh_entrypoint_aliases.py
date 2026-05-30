"""Migration-focused tests for install.sh command shim generation.

These tests pin the compatibility behavior before we rename managed install
paths or remove legacy aliases:

- fresh installs keep a primary ``doppel`` launcher
- the legacy ``hermes`` alias is still emitted alongside it
- both shims export the same home-dir compatibility env vars
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_SH = REPO_ROOT / "scripts" / "install.sh"


def _extract_setup_path_body() -> str:
    text = INSTALL_SH.read_text(encoding="utf-8")
    match = re.search(
        r"^setup_path\(\)\s*\{\s*\n(?P<body>.*?)^\}",
        text,
        re.MULTILINE | re.DOTALL,
    )
    assert match is not None, "Could not locate setup_path() in scripts/install.sh"
    return match["body"]


def _extract_shim_generation_block() -> str:
    body = _extract_setup_path_body()
    match = re.search(
        r"(?P<block>mkdir -p \"\$command_link_dir\".*?log_info \"Legacy alias kept at \$command_link_display_dir/hermes\")",
        body,
        re.DOTALL,
    )
    assert match is not None, "Could not locate shim generation block in setup_path()"
    return match["block"]


def _run_shim_generation(tmp_path: Path) -> tuple[Path, str]:
    command_link_dir = tmp_path / "bin"
    install_dir = tmp_path / "install"
    hermes_bin = install_dir / "venv" / "bin" / "doppel"
    hermes_home = tmp_path / ".doppel"
    hermes_bin.parent.mkdir(parents=True)
    hermes_bin.write_text("#!/usr/bin/env bash\nexit 0\n", encoding="utf-8")
    hermes_bin.chmod(0o755)

    script = "\n".join(
        [
            "set -e",
            'log_success() { :; }',
            'log_info() { :; }',
            'log_warn() { :; }',
            "run_block() {",
            f'command_link_dir="{command_link_dir}"',
            'command_link_display_dir="$command_link_dir"',
            f'HERMES_HOME="{hermes_home}"',
            f'HERMES_BIN="{hermes_bin}"',
            _extract_shim_generation_block(),
            "}",
            "run_block",
        ]
    )
    result = subprocess.run(
        ["bash", "-c", script],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    return command_link_dir, str(hermes_bin), str(hermes_home)


def test_install_sh_explicitly_generates_doppel_and_hermes_shims() -> None:
    text = INSTALL_SH.read_text(encoding="utf-8")
    assert "for shim_name in doppel hermes; do" in text


def test_install_sh_generates_both_launcher_shims(tmp_path: Path) -> None:
    command_link_dir, hermes_bin, hermes_home = _run_shim_generation(tmp_path)

    for shim_name in ("doppel", "hermes"):
        shim = command_link_dir / shim_name
        assert shim.exists()
        assert shim.is_file()
        assert shim.stat().st_mode & 0o111
        body = shim.read_text(encoding="utf-8")
        assert 'unset PYTHONPATH' in body
        assert 'unset PYTHONHOME' in body
        assert f'export DOPPEL_HOME="{hermes_home}"' in body
        assert f'export HERMES_HOME="{hermes_home}"' in body
        assert f'exec "{hermes_bin}" "$@"' in body
