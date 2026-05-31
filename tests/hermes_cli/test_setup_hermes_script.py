from pathlib import Path
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[2]
SETUP_SCRIPT = REPO_ROOT / "setup-hermes.sh"


def test_setup_hermes_script_is_valid_shell():
    result = subprocess.run(["bash", "-n", str(SETUP_SCRIPT)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_setup_hermes_script_has_termux_path():
    content = SETUP_SCRIPT.read_text(encoding="utf-8")

    assert "is_termux()" in content
    assert ".[termux]" in content
    assert "constraints-termux.txt" in content
    assert "$PREFIX/bin" in content


def test_setup_hermes_script_exposes_doppel_and_legacy_launchers():
    content = SETUP_SCRIPT.read_text(encoding="utf-8")

    assert 'venv/bin/doppel' in content
    assert 'ln -sf "$DOPPEL_BIN" "$COMMAND_LINK_DIR/doppel"' in content
    assert 'ln -sf "$HERMES_BIN" "$COMMAND_LINK_DIR/hermes"' in content


def test_setup_hermes_script_next_steps_are_doppel_first():
    content = SETUP_SCRIPT.read_text(encoding="utf-8")

    assert 'Setting up doppel command' in content
    assert 'doppel setup' in content
    assert 'doppel status' in content
    assert 'doppel gateway install' in content
