from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
README_EN = REPO_ROOT / "README.md"
README_ZH = REPO_ROOT / "README.zh-CN.md"
MCP_CONFIG_REFERENCE = (
    REPO_ROOT / "website" / "docs" / "reference" / "mcp-config-reference.md"
)
TOOLS_REFERENCE = REPO_ROOT / "website" / "docs" / "reference" / "tools-reference.md"
MODEL_CATALOG_REFERENCE = (
    REPO_ROOT / "website" / "docs" / "reference" / "model-catalog.md"
)


def test_frontdoor_readmes_and_reference_docs_prefer_doppel():
    readme_en = README_EN.read_text(encoding="utf-8")
    readme_zh = README_ZH.read_text(encoding="utf-8")
    mcp_config = MCP_CONFIG_REFERENCE.read_text(encoding="utf-8")
    tools_reference = TOOLS_REFERENCE.read_text(encoding="utf-8")
    model_catalog = MODEL_CATALOG_REFERENCE.read_text(encoding="utf-8")

    assert "Original upstream attribution is preserved in [NOTICE.md]." in readme_en
    assert "原始上游署名保留在 [NOTICE.md]。" in readme_zh
    assert "legacy home-dir installs still work" in mcp_config
    assert "legacy skill trees still work" in tools_reference
    assert "legacy cache paths still work" in model_catalog

    stale_en = (
        "It is a modified fork of Hermes Agent by Nous Research",
        "Notice-Hermes%20fork",
        "distributed as a modified fork of Hermes Agent by Nous Research",
    )
    stale_zh = (
        "它是基于 Nous Research 的 Hermes Agent 修改而来的分叉版本",
        "Notice-Hermes%20fork",
        "并作为 Nous Research 的 Hermes Agent 修改分叉发布",
    )
    stale_reference = (
        "legacy `~/.hermes/` installs still work",
        "legacy `~/.hermes/skills/` trees still work",
        "legacy `~/.hermes/cache/model_catalog.json` still works",
    )

    for stale in stale_en:
        assert stale not in readme_en
    for stale in stale_zh:
        assert stale not in readme_zh
    for stale in stale_reference:
        assert stale not in mcp_config
        assert stale not in tools_reference
        assert stale not in model_catalog
