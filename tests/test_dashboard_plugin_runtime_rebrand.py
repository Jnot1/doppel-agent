from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_dashboard_plugin_runtime_surfaces_prefer_doppel() -> None:
    app = _read("web/src/App.tsx")
    vite = _read("web/vite.config.ts")
    theme_switcher = _read("web/src/components/ThemeSwitcher.tsx")
    slots = _read("web/src/plugins/slots.ts")
    registry = _read("web/src/plugins/registry.ts")

    combined = "\n".join([app, vite, theme_switcher, slots, registry])

    required = [
        "Doppel",
        "Agent",
        "`window.__DOPPEL_PLUGINS__.registerSlot(pluginName, slotName, Component)`",
        "`window.__DOPPEL_PLUGINS__.registerSlot(...)`",
        "injected before the Doppel brand in the top bar",
        "Plugins call window.__DOPPEL_PLUGINS__.register(name, Component)",
        "__DOPPEL_PLUGIN_SDK__",
        "__DOPPEL_PLUGINS__",
        "`doppel dashboard`",
        "window.__DOPPEL_SESSION_TOKEN__",
        "window.__DOPPEL_DASHBOARD_EMBEDDED_CHAT__",
        "window.__DOPPEL_DASHBOARD_TUI__",
        "[doppel] Could not find session token",
        "is \\`doppel dashboard\\` running? /api calls will 401.",
        "[doppel] Dashboard at ${BACKEND} unreachable",
        "start it with \\`doppel dashboard\\` or set DOPPEL_DASHBOARD_URL.",
        "`~/.doppel/dashboard-themes/*.yaml`",
    ]
    forbidden = [
        "Hermes\n                  <br />\n                  Agent",
        "`window.__HERMES_PLUGINS__.registerSlot(pluginName, slotName, Component)`",
        "`window.__HERMES_PLUGINS__.registerSlot(...)`",
        "injected before the Hermes brand in the top bar",
        "Plugins call window.__HERMES_PLUGINS__.register(name, Component)",
        "__HERMES_PLUGIN_SDK__",
        "__HERMES_PLUGINS__",
        "`hermes dashboard`",
        "window.__HERMES_SESSION_TOKEN__",
        "window.__HERMES_DASHBOARD_EMBEDDED_CHAT__",
        "window.__HERMES_DASHBOARD_TUI__",
        "[hermes] Could not find session token",
        "is \\`hermes dashboard\\` running? /api calls will 401.",
        "[hermes] Dashboard at ${BACKEND} unreachable",
        "start it with `hermes dashboard` or set HERMES_DASHBOARD_URL.",
        "start it with \\`doppel dashboard\\` or set HERMES_DASHBOARD_URL.",
        "`~/.hermes/dashboard-themes/*.yaml`",
    ]

    for text in required:
        assert text in combined, text
    for text in forbidden:
        assert text not in combined, text
