from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_runtime_bridge_and_dashboard_surfaces_prefer_doppel() -> None:
    mcp_serve = _read("mcp_serve.py")
    chat_page = _read("web/src/pages/ChatPage.tsx")
    gateway_base = _read("gateway/platforms/base.py")
    acp_entry = _read("acp_adapter/entry.py")

    assert "Hermes MCP Server — expose messaging conversations as MCP tools." not in mcp_serve
    assert "Doppel MCP Server — expose messaging conversations as MCP tools." in mcp_serve
    assert "Plus: channels_list (Hermes-specific extra)" not in mcp_serve
    assert "Plus: channels_list (Doppel-specific extra)" in mcp_serve
    assert "    hermes mcp serve" not in mcp_serve
    assert "    doppel mcp serve" in mcp_serve
    assert '"hermes": {' not in mcp_serve
    assert '"doppel": {' in mcp_serve
    assert '"command": "hermes"' not in mcp_serve
    assert '"command": "doppel"' in mcp_serve
    assert "This is the Hermes equivalent of OpenClaw's WebSocket gateway bridge." not in mcp_serve
    assert "This is the Doppel equivalent of OpenClaw's WebSocket gateway bridge." in mcp_serve
    assert "Create and return the Hermes MCP server with all tools registered." not in mcp_serve
    assert "Create and return the Doppel MCP server with all tools registered." in mcp_serve
    assert "Start the Hermes MCP server on stdio." not in mcp_serve
    assert "Start the Doppel MCP server on stdio." in mcp_serve
    assert 'os.environ.get("HERMES_HOME", Path.home() / ".hermes")' not in mcp_serve
    assert 'Path.home() / ".doppel"' in mcp_serve

    assert "Open this page through `hermes dashboard`, not directly." not in chat_page
    assert "Open this page through `doppel dashboard`, not directly." in chat_page
    assert "ChatPage — embeds `hermes --tui` inside the dashboard." not in chat_page
    assert "ChatPage — embeds `doppel --tui` inside the dashboard." in chat_page
    assert "even when the inner Hermes TUI has enabled xterm mouse-events" not in chat_page
    assert "even when the inner Doppel TUI has enabled xterm mouse-events" in chat_page
    assert "`hermes --tui`." not in chat_page
    assert "`doppel --tui`." in chat_page
    assert "forwarding them into Hermes." not in chat_page
    assert "forwarding them into Doppel." in chat_page

    assert "add the key to ~/.hermes/.env manually." not in gateway_base
    assert "add the key to ~/.doppel/.env manually." in gateway_base
    assert "Audio file extensions Hermes recognizes for native audio delivery." not in gateway_base
    assert "Audio file extensions Doppel recognizes for native audio delivery." in gateway_base
    assert "Telegram private-chat topics created through Hermes' DM-topic helper" not in gateway_base
    assert "Telegram private-chat topics created through Doppel's DM-topic helper" in gateway_base
    assert "replying to the triggering message. Hermes-created Telegram private-chat" not in gateway_base
    assert "replying to the triggering message. Doppel-created Telegram private-chat" in gateway_base
    assert '"User-Agent": "Mozilla/5.0 (compatible; HermesAgent/1.0)"' not in gateway_base
    assert '"User-Agent": "Mozilla/5.0 (compatible; DoppelAgent/1.0)"' in gateway_base
    assert "The Hermes home itself contains credentials" not in gateway_base
    assert "The Doppel home itself contains credentials" in gateway_base
    assert "Hermes-managed cache, under an operator-allowlisted root" not in gateway_base
    assert "Doppel-managed cache, under an operator-allowlisted root" in gateway_base
    assert "~/.hermes/.env," not in gateway_base
    assert "~/.doppel/.env," in gateway_base
    assert "~/.hermes/auth.json, etc." not in gateway_base
    assert "~/.doppel/auth.json, etc." in gateway_base

    assert "Install agent-browser + Playwright Chromium into ~/.hermes/node/" not in acp_entry
    assert "Install agent-browser + Playwright Chromium into ~/.doppel/node/" in acp_entry
    assert "with ``hermes postinstall`` and the runtime lazy installer." not in acp_entry
    assert "with ``doppel postinstall`` and the runtime lazy installer." in acp_entry
