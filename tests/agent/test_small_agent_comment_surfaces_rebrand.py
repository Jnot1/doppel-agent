from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_small_agent_comment_and_doc_surfaces_prefer_doppel() -> None:
    display = _read("agent/display.py")
    model_metadata = _read("agent/model_metadata.py")
    conversation_loop = _read("agent/conversation_loop.py")

    assert "Render unified diff lines in Hermes' inline transcript style." not in display
    assert "Render unified diff lines in Doppel Agent's inline transcript style." in display

    assert "Minimum context length required to run Hermes Agent." not in model_metadata
    assert "Minimum context length required to run Doppel Agent." in model_metadata
    assert "unusable for Hermes' system prompt" not in model_metadata
    assert "unusable for Doppel Agent's system prompt" in model_metadata

    assert "``hermes logs --session <id>`` can filter a single conversation." not in conversation_loop
    assert "``doppel logs --session <id>`` can filter a single conversation." in conversation_loop
    assert "The system prompt is Hermes's territory" not in conversation_loop
    assert "The system prompt is Doppel Agent's territory" in conversation_loop
    assert "which Hermes' system prompt + tool schemas alone exceed." not in conversation_loop
    assert "which Doppel Agent's system prompt + tool schemas alone exceed." in conversation_loop
