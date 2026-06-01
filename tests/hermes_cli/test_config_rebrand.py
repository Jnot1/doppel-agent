"""Focused rebrand guards for the customer-facing config/help surface."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_config_module_prefers_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "config.py").read_text(encoding="utf-8")

    expected = [
        "⚠️  doppel config:",
        "Run 'doppel doctor' for fix suggestions.",
        "Use `doppel plugins enable <name>` to activate.",
        "│              ⚕ Doppel Configuration                   │",
        "URL of a remote Doppel Agent API server to forward messages to (proxy mode).",
        "Remote Doppel Agent API server URL (e.g. http://192.168.1.100:8642)",
        "Bearer token for authenticating with the remote Doppel Agent API server (proxy mode).",
        "Read ~/.doppel/config.yaml as-is, without merging defaults or migrating.",
        "Load configuration from ~/.doppel/config.yaml.",
        "Save configuration to ~/.doppel/config.yaml.",
        "Load environment variables from ~/.doppel/.env.",
        "Read, sanitize, and rewrite ~/.doppel/.env in place.",
        "Save or update a value in ~/.doppel/.env.",
        "Remove a key from ~/.doppel/.env and os.environ.",
        "Re-read ~/.doppel/.env into os.environ. Returns count of vars updated.",
        "Get a value from ~/.doppel/.env or environment.",
        "openai-codex (OAuth — doppel auth) — OpenAI Codex",
        "nous         (OAuth — doppel auth) — Nous Portal",
        "interactive menu render (`doppel tools`, `doppel setup`, status",
        "same file on every call was burning ~300ms of CPU per `doppel tools`",
        "Opt in via ``doppel chat --checkpoints`` or set enabled=True here.",
        "Azure Foundry base URL (set via 'doppel model' for endpoint-specific config)",
        "Explicit Nous Subscriber access token for tool-gateway requests (optional; otherwise read from the Doppel auth store)",
        "~/.doppel/logs/curator/",
        "in ``doppel config`` UI so users",
    ]
    forbidden = [
        "⚠️  hermes config:",
        "Run 'hermes doctor' for fix suggestions.",
        "Use `hermes plugins enable <name>` to activate.",
        "│              ⚕ Hermes Configuration                    │",
        "URL of a remote Hermes API server to forward messages to (proxy mode).",
        "Remote Hermes API server URL (e.g. http://192.168.1.100:8642)",
        "Bearer token for authenticating with the remote Hermes API server (proxy mode).",
        "Read ~/.hermes/config.yaml as-is, without merging defaults or migrating.",
        "Load configuration from ~/.hermes/config.yaml.",
        "Save configuration to ~/.hermes/config.yaml.",
        "Load environment variables from ~/.hermes/.env.",
        "Read, sanitize, and rewrite ~/.hermes/.env in place.",
        "Save or update a value in ~/.hermes/.env.",
        "Remove a key from ~/.hermes/.env and os.environ.",
        "Re-read ~/.hermes/.env into os.environ. Returns count of vars updated.",
        "Get a value from ~/.hermes/.env or environment.",
        "openai-codex (OAuth — hermes auth) — OpenAI Codex",
        "nous         (OAuth — hermes auth) — Nous Portal",
        "interactive menu render (`hermes tools`, `hermes setup`, status",
        "same file on every call was burning ~300ms of CPU per `hermes tools`",
        "Opt in via ``hermes chat --checkpoints`` or set enabled=True here.",
        "Azure Foundry base URL (set via 'hermes model' for endpoint-specific config)",
        "Explicit Nous Subscriber access token for tool-gateway requests (optional; otherwise read from the Hermes auth store)",
        "~/.hermes/logs/curator/",
        "in ``hermes config`` UI so users",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text
