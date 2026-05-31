from __future__ import annotations

import re
import subprocess
import sys

from hermes_cli.main import PROJECT_ROOT


def test_backup_help_prefers_doppel_archive_name():
    result = subprocess.run(
        [sys.executable, "-m", "hermes_cli.main", "backup", "--help"],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=15,
    )

    assert result.returncode == 0
    normalized = " ".join(result.stdout.split())
    normalized = re.sub(r"(?<=-)\s+(?=[A-Za-z])", "", normalized)
    assert "~/doppel-backup-<timestamp>.zip" in normalized
    assert "~/hermes-backup-<timestamp>.zip" not in normalized
