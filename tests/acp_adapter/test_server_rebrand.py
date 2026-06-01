from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_acp_server_customer_surfaces_prefer_doppel() -> None:
    server = _read("acp_adapter/server.py")

    assert '"""Convert ACP prompt blocks into a Hermes/OpenAI-compatible user content payload."""' not in server
    assert '"""Convert ACP prompt blocks into a Doppel/OpenAI-compatible user content payload."""' in server
    assert '"""ACP Agent implementation wrapping Hermes AIAgent."""' not in server
    assert '"""ACP Agent implementation wrapping Doppel AIAgent."""' in server
    assert '"version": "Show Hermes version"' not in server
    assert '"version": "Show Doppel version"' in server
    assert '"description": "Show Hermes version"' not in server
    assert '"description": "Show Doppel version"' in server
    assert "so Hermes maps edit approval" not in server
    assert "so Doppel maps edit approval" in server
    assert "Hermes estimates ``used``" not in server
    assert "Doppel Agent estimates ``used``" in server
    assert '"""Send ACP native session metadata after Hermes changes it."""' not in server
    assert '"""Send ACP native session metadata after Doppel changes it."""' in server
    assert "harmless under Hermes' threat model" not in server
    assert "Doppel's threat model (ACP is stdio-only, local-trust)" in server
    assert "Terminal auth launches Hermes setup/model selection out-of-band." not in server
    assert "Terminal auth launches Doppel setup/model selection out-of-band." in server
    assert "Merely restoring server-side state makes Hermes" not in server
    assert "Merely restoring server-side state makes Doppel" in server
    assert '"""Run Hermes on the user\'s prompt and stream events back to the editor."""' not in server
    assert '"""Run Doppel on the user\'s prompt and stream events back to the editor."""' in server
    assert "ACP thought panes should not receive Hermes' local kawaii waiting/status" not in server
    assert "ACP thought panes should not receive Doppel's local kawaii waiting/status" in server
    assert '"""Accept ACP config option updates even when Hermes has no typed ACP config surface yet."""' not in server
    assert '"""Accept ACP config option updates even when Doppel has no typed ACP config surface yet."""' in server
