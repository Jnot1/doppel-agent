from pathlib import Path


ROOT = Path("/Users/macshelton/Documents/DoppelFork-repair2")


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_dashboard_docs_surfaces_prefer_doppel() -> None:
    en = _read("website/docs/user-guide/features/extending-the-dashboard.md")
    zh = _read(
        "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/extending-the-dashboard.md"
    )

    required = [
        "Doppel Teal",
        "window.__DOPPEL_PLUGIN_SDK__",
        "window.__DOPPEL_PLUGINS__.register(",
        "window.__DOPPEL_PLUGINS__.registerSlot(",
        "`plugins/example-dashboard`",
        "single scoped `<style>` tag",
    ]
    forbidden = [
        "~/.hermes",
        "Hermes Teal",
        "__HERMES_PLUGIN_SDK__",
        "__HERMES_PLUGINS__",
        "hermes-example-plugins",
        "data-hermes-theme-css",
        "hermes-agent codebase",
        "./.hermes/plugins",
        "HERMES_ENABLE_PROJECT_PLUGINS",
    ]

    combined = "\n".join([en, zh])

    for text in required:
        assert text in combined, text
    for text in forbidden:
        assert text not in combined, text
