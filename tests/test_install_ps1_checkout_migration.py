"""Structural regression tests for install.ps1 checkout migration parity.

`pwsh` is not available in this environment, so these tests pin the intended
PowerShell migration seam directly in the script source:

- a dedicated helper exists to migrate `hermes-agent` -> `doppel-agent`
- the repository stage invokes that helper before touching git/update logic
"""

from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_PS1 = REPO_ROOT / "scripts" / "install.ps1"


def _extract_function_body(name: str) -> str:
    text = INSTALL_PS1.read_text(encoding="utf-8")
    match = re.search(
        rf"^function\s+{re.escape(name)}\s*\{{\s*\n(?P<body>.*?)^\}}",
        text,
        re.MULTILINE | re.DOTALL,
    )
    assert match is not None, f"Could not locate {name} in scripts/install.ps1"
    return match["body"]


def test_install_ps1_defines_managed_checkout_migration_helper() -> None:
    body = _extract_function_body("Migrate-ManagedCheckoutDir")

    assert "$preferredCheckoutDir = Join-Path $HermesHome $ManagedCheckoutName" in body
    assert "$legacyCheckoutDir = Join-Path $HermesHome $LegacyManagedCheckoutName" in body
    assert "Move-Item $legacyCheckoutDir $preferredCheckoutDir -Force" in body
    assert "$InstallDir = $preferredCheckoutDir" in body


def test_install_repository_calls_checkout_migration_before_repo_access() -> None:
    body = _extract_function_body("Install-Repository")

    migrate_idx = body.find("Migrate-ManagedCheckoutDir")
    test_path_idx = body.find("if (Test-Path $InstallDir)")

    assert migrate_idx != -1, "Install-Repository must call Migrate-ManagedCheckoutDir"
    assert test_path_idx != -1, "Install-Repository must still probe the target repo path"
    assert migrate_idx < test_path_idx, (
        "Checkout migration must run before repo validation/update logic touches "
        "$InstallDir"
    )
