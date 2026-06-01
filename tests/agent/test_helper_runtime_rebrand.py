from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_helper_runtime_surfaces_prefer_doppel() -> None:
    anthropic = _read("agent/anthropic_adapter.py")
    azure = _read("agent/azure_identity_adapter.py")
    memory = _read("agent/memory_provider.py")
    lsp_manager = _read("agent/lsp/manager.py")
    lsp_eventlog = _read("agent/lsp/eventlog.py")
    stream_diag = _read("agent/stream_diag.py")

    assert '"""Anthropic Messages API adapter for Hermes Agent.' not in anthropic
    assert '"""Anthropic Messages API adapter for Doppel Agent.' in anthropic
    assert "Stores credentials in ~/.hermes/.anthropic_oauth.json" not in anthropic
    assert "Stores credentials in ~/.doppel/.anthropic_oauth.json" in anthropic
    assert '"""Run Hermes-native OAuth PKCE flow and return credential state."""' not in anthropic
    assert '"""Run Doppel-native OAuth PKCE flow and return credential state."""' in anthropic
    assert 'print("Authorize Hermes with your Claude Pro/Max subscription.")' not in anthropic
    assert 'print("Authorize Doppel with your Claude Pro/Max subscription.")' in anthropic
    assert '"""Read Hermes-managed OAuth credentials from ~/.hermes/.anthropic_oauth.json."""' not in anthropic
    assert '"""Read Doppel-managed OAuth credentials from ~/.doppel/.anthropic_oauth.json."""' in anthropic
    assert 'text = text.replace("Doppel Agent", "Claude Code")' in anthropic
    assert 'text = text.replace("doppel-agent", "claude-code")' in anthropic

    assert "``~/.hermes/.env`` or the deployment environment." not in azure
    assert "``~/.doppel/.env`` or the deployment environment." in azure
    assert "Use for ``doppel doctor`` /\n    ``hermes auth status`` / wizard preflight." not in azure
    assert "Use for ``doppel doctor`` /\n    ``doppel auth status`` / wizard preflight." in azure

    assert "for profile-scoped storage instead of hardcoding ``~/.hermes``." not in memory
    assert "for profile-scoped storage instead of hardcoding ``~/.doppel``." in memory
    assert "Used by 'hermes memory setup' to walk the user through configuration." not in memory
    assert "Used by 'doppel memory setup' to walk the user through configuration." in memory
    assert "Called by 'hermes memory setup' after collecting user inputs." not in memory
    assert "Called by 'doppel memory setup' after collecting user inputs." in memory

    assert "until the service is restarted (``hermes lsp" not in lsp_manager
    assert "until the service is restarted (``doppel lsp" in lsp_manager
    assert "used by ``hermes lsp status``" not in lsp_manager
    assert "used by ``doppel lsp status``" in lsp_manager

    assert "tail -f ~/.hermes/logs/agent.log | rg 'lsp\\\\['" not in lsp_eventlog
    assert "tail -f ~/.doppel/logs/agent.log | rg 'lsp\\\\['" in lsp_eventlog

    assert "``hermes logs --level WARNING | grep \"Stream drop\"`` to inspect." not in stream_diag
    assert "``doppel logs --level WARNING | grep \"Stream drop\"`` to inspect." in stream_diag
