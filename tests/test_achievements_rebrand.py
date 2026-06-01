from pathlib import Path


ROOT = Path("/Users/macshelton/Documents/DoppelFork-repair2")


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    marker = f"### {heading}"
    start = text.index(marker)
    remainder = text[start:]
    next_heading = remainder.find("\n### ", len(marker))
    if next_heading == -1:
        return remainder
    return remainder[:next_heading]


def test_achievements_customer_surfaces_prefer_doppel() -> None:
    manifest = _read("plugins/hermes-achievements/dashboard/manifest.json")
    plugin_api = _read("plugins/hermes-achievements/dashboard/plugin_api.py")
    dist = _read("plugins/hermes-achievements/dashboard/dist/index.js")
    readme = _read("plugins/hermes-achievements/README.md")
    en_doc = _section(
        _read("website/docs/user-guide/features/built-in-plugins.md"),
        "doppel-achievements",
    )
    zh_doc = _section(
        _read(
            "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/built-in-plugins.md"
        ),
        "doppel-achievements",
    )

    docs_combined = "\n".join([readme, en_doc, zh_doc])
    required_docs = [
        "doppel-achievements",
        "Doppel Achievements",
        "Doppel Agent",
        "~/.doppel/state.db",
        "$DOPPEL_HOME/plugins/doppel-achievements/state.json",
        "/api/plugins/doppel-achievements/",
        "doppel dashboard",
        "~/.doppel/plugins/doppel-achievements/",
    ]
    forbidden_docs = [
        "Hermes Achievements",
        "Hermes Agent",
        "~/.hermes/state.db",
        "$HERMES_HOME/plugins/hermes-achievements/state.json",
        "/api/plugins/hermes-achievements/",
        "`hermes dashboard`",
        "~/.hermes/plugins/hermes-achievements/",
    ]
    for text in required_docs:
        assert text in docs_combined, text
    for text in forbidden_docs:
        assert text not in docs_combined, text

    required_manifest = [
        '"name": "doppel-achievements"',
        "agentic Doppel workflows",
    ]
    forbidden_manifest = [
        '"name": "hermes-achievements"',
        "agentic Hermes workflows",
    ]
    for text in required_manifest:
        assert text in manifest, text
    for text in forbidden_manifest:
        assert text not in manifest, text

    required_runtime = [
        "Doppel Achievements dashboard plugin backend.",
        "/api/plugins/doppel-achievements/",
        '"X-Doppel-Session-Token"',
        "__DOPPEL_PLUGIN_SDK__",
        "__DOPPEL_PLUGINS__",
        'register("doppel-achievements", AchievementsPage)',
        "Doppel Achievements",
        "Doppel Agent",
        '"category": "Doppel Native"',
        'PLUGIN_SLUG = "doppel-achievements"',
        "doppel-achievement-",
    ]
    for text in required_runtime:
        combined = "\n".join([plugin_api, dist])
        assert text in combined, text
