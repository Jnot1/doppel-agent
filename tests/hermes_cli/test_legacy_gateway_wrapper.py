from pathlib import Path
import subprocess
import shutil
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]
LEGACY_GATEWAY_SCRIPT = REPO_ROOT / "scripts" / "hermes-gateway"


def test_legacy_gateway_wrapper_help_redirects_to_doppel_gateway():
    python = shutil.which("python3") or sys.executable
    result = subprocess.run(
        [python, str(LEGACY_GATEWAY_SCRIPT), "--help"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    combined = f"{result.stdout}\n{result.stderr}"
    assert "deprecated" in combined.lower()
    assert "doppel gateway" in combined


def test_legacy_gateway_wrapper_checks_project_virtualenvs():
    content = LEGACY_GATEWAY_SCRIPT.read_text(encoding="utf-8")

    assert 'PROJECT_DIR / ".venv" / "bin" / "python"' in content
    assert 'PROJECT_DIR / "venv" / "bin" / "python"' in content
