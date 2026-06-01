from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_runtime_bridge_and_dashboard_surfaces_prefer_doppel() -> None:
    mcp_serve = _read("mcp_serve.py")
    chat_page = _read("web/src/pages/ChatPage.tsx")
    gateway_base = _read("gateway/platforms/base.py")
    acp_entry = _read("acp_adapter/entry.py")

    assert "Hermes Agent messaging bridge." not in mcp_serve
    assert "Doppel Agent messaging bridge." in mcp_serve

    assert "Open this page through `hermes dashboard`, not directly." not in chat_page
    assert "Open this page through `doppel dashboard`, not directly." in chat_page

    assert "add the key to ~/.hermes/.env manually." not in gateway_base
    assert "add the key to ~/.doppel/.env manually." in gateway_base

    assert "Install agent-browser + Playwright Chromium into ~/.hermes/node/" not in acp_entry
    assert "Install agent-browser + Playwright Chromium into ~/.doppel/node/" in acp_entry
    assert "with ``hermes postinstall`` and the runtime lazy installer." not in acp_entry
    assert "with ``doppel postinstall`` and the runtime lazy installer." in acp_entry
