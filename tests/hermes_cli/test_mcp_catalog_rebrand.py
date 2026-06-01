"""Focused rebrand guards for the MCP catalog customer-facing surface."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_mcp_catalog_prefers_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "mcp_catalog.py").read_text(encoding="utf-8")

    expected = [
        "entries via ``doppel mcp catalog`` or the interactive ``doppel mcp picker``,",
        "and install them with ``doppel mcp install <name>``",
        "auto-updated; users explicitly re-run ``doppel mcp install <name>`` to",
        "Secrets prompted at install time go to ``~/.doppel/.env``",
        "Clone the entry's repo into ``~/.doppel/mcp-installs/<name>`` and run",
        "non-secrets alike to ~/.doppel/.env via save_env_value().",
        "Either way, point the user at ``doppel mcp configure <name>``.",
        "Run `doppel mcp configure {entry.name}` after the server ",
        "Run `doppel mcp configure {entry.name}` after first ",
        "No tools selected. Run `doppel mcp configure {entry.name}` ",
        "the user can re-run `doppel mcp configure <name>` and unselect a",
        "the existing `doppel auth <provider>` flow. Surface guidance",
        "`doppel auth {entry.auth.provider}` if you have not ",
        "Entries are added only by merging a PR into doppel-agent.",
        "Return the optional-mcps/ directory shipped with this Doppel Agent install.",
        "this Doppel Agent understands version",
    ]
    forbidden = [
        "entries via ``hermes mcp catalog`` or the interactive ``hermes mcp picker``,",
        "and install them with ``hermes mcp install <name>``",
        "auto-updated; users explicitly re-run ``hermes mcp install <name>`` to",
        "Secrets prompted at install time go to ``~/.hermes/.env``",
        "Clone the entry's repo into ``~/.hermes/mcp-installs/<name>`` and run",
        "non-secrets alike to ~/.hermes/.env via save_env_value().",
        "Either way, point the user at ``hermes mcp configure <name>``.",
        "Run `hermes mcp configure {entry.name}` after the server ",
        "Run `hermes mcp configure {entry.name}` after first ",
        "No tools selected. Run `hermes mcp configure {entry.name}` ",
        "the user can re-run `hermes mcp configure <name>` and unselect a",
        "the existing `hermes auth <provider>` flow. Surface guidance",
        "`hermes auth {entry.auth.provider}` if you have not ",
        "Entries are added only by merging a PR into hermes-agent.",
        "Return the optional-mcps/ directory shipped with this Hermes install.",
        "this Hermes understands version",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text
