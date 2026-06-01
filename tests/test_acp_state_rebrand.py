from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_acp_session_and_state_surfaces_prefer_doppel() -> None:
    session = _read("acp_adapter/session.py")
    entry = _read("acp_adapter/entry.py")
    state = _read("hermes_state.py")

    assert "maps ACP sessions to Hermes AIAgent instances." not in session
    assert "maps ACP sessions to Doppel AIAgent instances." in session
    assert "shared SessionDB (``~/.hermes/state.db``)" not in session
    assert "shared SessionDB (``~/.doppel/state.db``)" in session
    assert "when Hermes itself is running in WSL." not in session
    assert "when Doppel itself is running in WSL." in session
    assert "launch ``hermes acp`` inside WSL" not in session
    assert "launch ``doppel acp`` inside WSL" in session
    assert "Zed can launch Hermes from a Windows workspace" not in session
    assert "Zed can launch Doppel from a Windows workspace" in session
    assert "ACP-managed Hermes agent" not in session
    assert "ACP-managed Doppel agent" in session
    assert "backed by Hermes AIAgent instances." not in session
    assert "backed by Doppel AIAgent instances." in session
    assert "current Hermes runtime provider configuration." not in session
    assert "current Doppel runtime provider configuration." in session
    assert "SessionDB (``~/.hermes/state.db``) is lazily created." not in session
    assert "SessionDB (``~/.doppel/state.db``) is lazily created." in session

    assert "    hermes acp" not in entry
    assert "    doppel acp" in entry
    assert "partial ``hermes update``" not in entry
    assert "partial ``doppel update``" in entry

    assert "SQLite State Store for Hermes Agent." not in state
    assert "SQLite State Store for Doppel Agent." in state
    assert "This usually means Hermes is running on an " not in state
    assert "This usually means Doppel Agent is running on an " in state
    assert "upgrade Hermes, keep the old" not in state
    assert "upgrade Doppel Agent, keep the old" in state
    assert "Bind one Telegram DM topic thread to one Hermes session." not in state
    assert "Bind one Telegram DM topic thread to one Doppel session." in state
    assert "A Hermes session may only be linked to one Telegram topic in MVP." not in state
    assert "A Doppel session may only be linked to one Telegram topic in MVP." in state
    assert "Return True if a Hermes session is already bound to any Telegram DM topic." not in state
    assert "Return True if a Doppel session is already bound to any Telegram DM topic." in state
