"""Focused rebrand guards for the callback prompt help surface."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_callbacks_module_prefers_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "callbacks.py").read_text(encoding="utf-8")

    expected = [
        "Each function takes the DoppelCLI instance",
        "The secret is stored in ~/.doppel/.env and never exposed to the model.",
    ]
    forbidden = [
        "Each function takes the HermesCLI instance",
        "The secret is stored in ~/.hermes/.env and never exposed to the model.",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text
