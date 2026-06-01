from pathlib import Path


ROOT = Path("/Users/macshelton/Documents/DoppelFork-repair2")


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_project_plugin_docs_and_runtime_prefer_doppel_aliases() -> None:
    en = _read("website/docs/user-guide/features/plugins.md")
    zh = _read(
        "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/plugins.md"
    )
    plugins_py = _read("hermes_cli/plugins.py")
    web_server = _read("hermes_cli/web_server.py")
    tips = _read("hermes_cli/tips.py")

    combined_docs = "\n".join([en, zh])
    combined_runtime = "\n".join([plugins_py, web_server, tips])

    required_docs = [
        "~/.doppel/plugins/",
        "./.doppel/plugins/",
        "DOPPEL_ENABLE_PROJECT_PLUGINS",
        '[project.entry-points."doppel_agent.plugins"]',
    ]
    forbidden_docs = [
        "~/.hermes/plugins/",
        "./.hermes/plugins/",
        "HERMES_ENABLE_PROJECT_PLUGINS",
        '[project.entry-points."hermes_agent.plugins"]',
    ]
    required_runtime = [
        "DOPPEL_ENABLE_PROJECT_PLUGINS",
        ".doppel",
        "doppel_agent.plugins",
    ]

    for text in required_docs:
        assert text in combined_docs, text
    for text in forbidden_docs:
        assert text not in combined_docs, text
    for text in required_runtime:
        assert text in combined_runtime, text
