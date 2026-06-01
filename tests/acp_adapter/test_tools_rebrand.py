from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_acp_tools_customer_surfaces_prefer_doppel() -> None:
    tools = _read("acp_adapter/tools.py")

    assert (
        '"""ACP tool-call helpers for mapping hermes tools to ACP ToolKind and building content."""'
        not in tools
    )
    assert (
        '"""ACP tool-call helpers for mapping doppel tools to ACP ToolKind and building content."""'
        in tools
    )
    assert "# Map hermes tool names -> ACP ToolKind" not in tools
    assert "# Map doppel tool names -> ACP ToolKind" in tools
