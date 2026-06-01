"""Focused rebrand guards for small Hermes CLI helper modules."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_small_cli_helper_modules_prefer_doppel_customer_facing_copy() -> None:
    build_info = (REPO_ROOT / "hermes_cli" / "build_info.py").read_text(encoding="utf-8")
    cli_output = (REPO_ROOT / "hermes_cli" / "cli_output.py").read_text(encoding="utf-8")
    colors = (REPO_ROOT / "hermes_cli" / "colors.py").read_text(encoding="utf-8")

    assert "Baked-in build metadata for Doppel Agent." in build_info
    assert "To make ``doppel dump`` and the startup banner identify the exact commit the" in build_info
    assert "Baked-in build metadata for Hermes Agent." not in build_info
    assert "To make ``hermes dump`` and the startup banner identify the exact commit the" not in build_info

    assert '"""Shared CLI output helpers for Doppel CLI modules.' in cli_output
    assert '"""Shared ANSI color utilities for Doppel CLI modules."""' in colors
    assert '"""Shared CLI output helpers for Hermes CLI modules.' not in cli_output
    assert '"""Shared ANSI color utilities for Hermes CLI modules."""' not in colors
