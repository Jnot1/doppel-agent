from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_dashboard_runtime_frontend_surfaces_prefer_doppel() -> None:
    api = _read("web/src/lib/api.ts")
    flags = _read("web/src/lib/dashboard-flags.ts")
    gateway_client = _read("web/src/lib/gatewayClient.ts")
    chat_page = _read("web/src/pages/ChatPage.tsx")

    required = [
        "window.__DOPPEL_BASE_PATH__",
        "__DOPPEL_SESSION_TOKEN__",
        "__DOPPEL_AUTH_REQUIRED__",
        '__DOPPEL_DASHBOARD_EMBEDDED_CHAT__',
        'const SESSION_HEADER = "X-Doppel-Session-Token";',
        'sessionStorage.setItem("doppel.lastLocation"',
        'sessionStorage.getItem("doppel.tokenReloadAttempted")',
        'sessionStorage.setItem("doppel.tokenReloadAttempted", "1")',
        'sessionStorage.removeItem("doppel.tokenReloadAttempted")',
        "page must be served by the Doppel dashboard server",
        "`doppel dashboard --tui`",
        "window.__DOPPEL_SESSION_TOKEN__",
        "window.__DOPPEL_AUTH_REQUIRED__",
        "__DOPPEL_DASHBOARD_TUI__",
    ]
    forbidden = [
        "window.__HERMES_BASE_PATH__",
        "__HERMES_SESSION_TOKEN__",
        "__HERMES_AUTH_REQUIRED__",
        '__HERMES_DASHBOARD_EMBEDDED_CHAT__',
        'const SESSION_HEADER = "X-Hermes-Session-Token";',
        'sessionStorage.setItem("hermes.lastLocation"',
        'sessionStorage.getItem("hermes.tokenReloadAttempted")',
        'sessionStorage.setItem("hermes.tokenReloadAttempted", "1")',
        'sessionStorage.removeItem("hermes.tokenReloadAttempted")',
        "page must be served by the Hermes dashboard server",
        "`hermes dashboard --tui`",
        "window.__HERMES_SESSION_TOKEN__",
        "window.__HERMES_AUTH_REQUIRED__",
        "__HERMES_DASHBOARD_TUI__",
    ]

    combined = "\n".join([api, flags, gateway_client, chat_page])
    for text in required:
        assert text in combined, text
    for text in forbidden:
        assert text not in combined, text
