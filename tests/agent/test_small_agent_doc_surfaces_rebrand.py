from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_small_agent_doc_surfaces_prefer_doppel() -> None:
    plugin_llm = _read("agent/plugin_llm.py")
    bedrock = _read("agent/bedrock_adapter.py")
    lsp_init = _read("agent/lsp/__init__.py")
    auxiliary = _read("agent/auxiliary_client.py")
    models_dev = _read("agent/models_dev.py")

    assert "Plugins built on Hermes Agent often need" not in plugin_llm
    assert "Plugins built on Doppel Agent often need" in plugin_llm
    assert "extend an existing Hermes" not in plugin_llm
    assert "extend an existing Doppel Agent" in plugin_llm
    assert "This mirrors Hermes' main config" not in plugin_llm
    assert "This mirrors Doppel Agent's main config" in plugin_llm
    assert "override Hermes\nsupports." not in plugin_llm
    assert "override Doppel Agent\nsupports." in plugin_llm

    assert '"""AWS Bedrock Converse API adapter for Hermes Agent.' not in bedrock
    assert '"""AWS Bedrock Converse API adapter for Doppel Agent.' in bedrock
    assert "Or install Hermes with Bedrock support" not in bedrock
    assert "Or install Doppel Agent with Bedrock support" in bedrock

    assert '"""Language Server Protocol (LSP) integration for Hermes Agent.' not in lsp_init
    assert '"""Language Server Protocol (LSP) integration for Doppel Agent.' in lsp_init
    assert "Hermes runs full language servers" not in lsp_init
    assert "Doppel Agent runs full language servers" in lsp_init
    assert "``hermes chat`` exit would leak pyright processes" not in lsp_init
    assert "``doppel chat`` exit would leak pyright processes" in lsp_init

    assert "from Hermes auth store." not in auxiliary
    assert "from Doppel Agent auth store." in auxiliary
    assert "``hermes config aux reset``" not in auxiliary
    assert "``doppel config aux reset``" in auxiliary

    assert "used by ``hermes config refresh``" not in models_dev
    assert "used by ``doppel config refresh``" in models_dev
