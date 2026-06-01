"""Focused rebrand guards for the customer-facing models surface."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_models_module_prefers_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "models.py").read_text(encoding="utf-8")

    expected = [
        "Add, remove, or reorder entries here — both `doppel setup` and",
        "`doppel` provider-selection will pick up the change automatically.",
        "This keeps the gateway /model picker in sync with the CLI `doppel model`",
        "this list:  doppel model, /model, list_authenticated_providers.",
        "tui_desc    — longer description for the `doppel model` interactive picker",
        "detailed description for `doppel model` TUI",
        "slug as a top-level row in the interactive `doppel model` / setup wizard /",
        "DISPLAY ONLY. Used by every interactive picker (``doppel model``, the",
        "model a user would be offered first in the ``doppel model`` picker.",
        "selected a model (e.g. ``doppel auth add openai-codex`` without",
        "``doppel model``).",
        "source of truth shared with ``doppel model``, ``/model``, etc.).",
        "populated by ``doppel auth add copilot`` and by ``_seed_from_env``",
        "when the env var is set in ``~/.doppel/.env``.",
        "``doppel model --refresh``.",
        "Doppel Agent will still save `{requested}`, but the endpoint should expose `/models` for verification.",
        "MiniMax does not expose a /models endpoint, so Doppel Agent cannot verify the model name.",
    ]
    forbidden = [
        "Add, remove, or reorder entries here — both `hermes setup` and",
        "`hermes` provider-selection will pick up the change automatically.",
        "This keeps the gateway /model picker in sync with the CLI `hermes model`",
        "this list:  hermes model, /model, list_authenticated_providers.",
        "tui_desc    — longer description for the `hermes model` interactive picker",
        "detailed description for `hermes model` TUI",
        "slug as a top-level row in the interactive `hermes model` / setup wizard /",
        "DISPLAY ONLY. Used by every interactive picker (``hermes model``, the",
        "model a user would be offered first in the ``hermes model`` picker.",
        "selected a model (e.g. ``hermes auth add openai-codex`` without",
        "``hermes model``).",
        "source of truth shared with ``hermes model``, ``/model``, etc.).",
        "populated by ``hermes auth add copilot`` and by ``_seed_from_env``",
        "when the env var is set in ``~/.hermes/.env``.",
        "``hermes model --refresh``.",
        "Hermes will still save `{requested}`, but the endpoint should expose `/models` for verification.",
        "MiniMax does not expose a /models endpoint, so Hermes cannot verify the model name.",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text
