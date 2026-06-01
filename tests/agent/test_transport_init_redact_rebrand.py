from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_transport_init_and_redact_surfaces_prefer_doppel() -> None:
    transport = _read("agent/transports/hermes_tools_mcp_server.py")
    agent_init = _read("agent/agent_init.py")
    redact = _read("agent/redact.py")

    assert "write ~/.hermes/kanban.db" not in transport
    assert "write ~/.doppel/kanban.db" in transport
    assert "Hermes' skill library" not in transport
    assert "Doppel's skill library" in transport
    assert 'description = spec.get("description") or f"Hermes {name} tool"' not in transport
    assert 'description = spec.get("description") or f"Doppel {name} tool"' in transport

    assert "still use ~/.hermes/SOUL.md as the primary" not in agent_init
    assert "still use ~/.doppel/SOUL.md as the primary" in agent_init
    assert "both live under ~/.hermes/logs/." not in agent_init
    assert "both live under ~/.doppel/logs/." in agent_init
    assert "Session logs go into ~/.hermes/sessions/" not in agent_init
    assert "Session logs go into ~/.doppel/sessions/" in agent_init
    assert "Per-session JSON snapshot writer (~/.hermes/sessions/session_{sid}.json)" not in agent_init
    assert "Per-session JSON snapshot writer (~/.doppel/sessions/session_{sid}.json)" in agent_init

    assert "`HERMES_REDACT_SECRETS=false` in ~/.hermes/.env." not in redact
    assert "`HERMES_REDACT_SECRETS=false` in ~/.doppel/.env." in redact
    assert "Canonical helper for display-time redaction across Hermes" not in redact
    assert "Canonical helper for display-time redaction across Doppel Agent" in redact
    assert "``hermes config``, ``hermes status``, ``hermes dump``" not in redact
    assert "``doppel config``, ``doppel status``, ``doppel dump``" in redact
