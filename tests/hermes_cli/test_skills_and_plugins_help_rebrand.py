from __future__ import annotations

import re
import subprocess
import sys

from hermes_cli.main import PROJECT_ROOT


def test_skills_reset_help_is_doppel_first():
    result = subprocess.run(
        [sys.executable, "-m", "hermes_cli.main", "skills", "reset", "--help"],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=15,
    )

    assert result.returncode == 0
    normalized = " ".join(result.stdout.split())
    normalized = re.sub(r"(?<=-)\s+(?=[A-Za-z])", "", normalized)
    assert "future 'doppel update' runs stop marking it as user-modified" in normalized
    assert "future 'hermes update' runs stop marking it as user-modified" not in normalized


def test_plugins_install_help_uses_doppel_example_repo():
    result = subprocess.run(
        [sys.executable, "-m", "hermes_cli.main", "plugins", "install", "--help"],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=15,
    )

    assert result.returncode == 0
    normalized = " ".join(result.stdout.split())
    normalized = re.sub(r"(?<=-)\s+(?=[A-Za-z])", "", normalized)
    assert "my-org/doppel-plugin-chrome-profiles" in normalized
    assert "anpicasso/hermes-plugin-chrome-profiles" not in normalized
