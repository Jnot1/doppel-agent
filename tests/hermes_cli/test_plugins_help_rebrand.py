from __future__ import annotations

import subprocess
import sys

from hermes_cli.main import PROJECT_ROOT


def test_plugins_install_no_enable_help_is_doppel_first():
    result = subprocess.run(
        [sys.executable, "-m", "hermes_cli.main", "plugins", "install", "--help"],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=15,
    )

    assert result.returncode == 0
    assert "doppel plugins enable <name>" in result.stdout
    assert "hermes plugins enable <name>" not in result.stdout
