from __future__ import annotations

import re
import subprocess
import sys

from hermes_cli.main import PROJECT_ROOT


def test_model_help_keeps_registered_oauth_client_id_contract():
    result = subprocess.run(
        [sys.executable, "-m", "hermes_cli.main", "model", "--help"],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=15,
    )

    assert result.returncode == 0
    normalized = " ".join(result.stdout.split())
    normalized = re.sub(r"(?<=-)\s+(?=[A-Za-z])", "", normalized)
    assert "Registered OAuth client id to use for Nous login" in normalized
    assert "(default: hermes-cli)" in normalized
    assert "doppel-cli" not in normalized


def test_login_help_keeps_registered_oauth_client_id_contract():
    result = subprocess.run(
        [sys.executable, "-m", "hermes_cli.main", "login", "--help"],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=15,
    )

    assert result.returncode == 0
    normalized = " ".join(result.stdout.split())
    normalized = re.sub(r"(?<=-)\s+(?=[A-Za-z])", "", normalized)
    assert "Registered OAuth client id to use" in normalized
    assert "(default: hermes-cli)" in normalized
    assert "doppel-cli" not in normalized
