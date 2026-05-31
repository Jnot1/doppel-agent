from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

EN_PLUGINS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "plugins.md"
EN_BUILD_GUIDE = REPO_ROOT / "website" / "docs" / "guides" / "build-a-hermes-plugin.md"
ZH_PLUGINS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "plugins.md"
)
ZH_BUILD_GUIDE = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "guides"
    / "build-a-hermes-plugin.md"
)
EN_BUILTIN_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "built-in-plugins.md"
EN_INTEGRATIONS_DOC = REPO_ROOT / "website" / "docs" / "integrations" / "index.md"
ZH_BUILTIN_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "built-in-plugins.md"
)
ZH_INTEGRATIONS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "integrations"
    / "index.md"
)


def test_english_plugin_docs_prefer_doppel_branding_and_commands():
    plugins = EN_PLUGINS_DOC.read_text(encoding="utf-8")
    guide = EN_BUILD_GUIDE.read_text(encoding="utf-8")

    assert "Build a Doppel Plugin" in plugins
    assert "Doppel Agent has a plugin system" in plugins
    assert "doppel plugins install user/repo" in plugins
    assert "doppel plugins enable my-plugin" in plugins
    assert "doppel skills tap add <repo>" in plugins
    assert "doppel plugins list" in plugins
    assert "Build a Hermes Plugin" not in plugins
    assert "hermes plugins install user/repo" not in plugins
    assert "hermes plugins enable my-plugin" not in plugins
    assert "hermes skills tap add <repo>" not in plugins

    assert 'title: "Build a Doppel Plugin"' in guide
    assert "# Build a Doppel Plugin" in guide
    assert "Start Doppel:" in guide
    assert "\ndoppel\n```" in guide
    assert "doppel plugins install" in guide
    assert "doppel plugins enable <name>" in guide
    assert "doppel my-plugin <subcommand>" in guide
    assert "doppel my-plugin status" in guide
    assert "doppel skills tap add myorg/skills-repo" in guide
    assert "doppel logs --level WARNING | grep -i plugin" in guide
    assert "Build a Hermes Plugin" not in guide
    assert "hermes my-plugin <subcommand>" not in guide
    assert "hermes plugins install" not in guide
    assert "hermes plugins enable <name>" not in guide
    assert "hermes skills tap add myorg/skills-repo" not in guide


def test_zh_plugin_docs_prefer_doppel_branding_and_commands():
    plugins = ZH_PLUGINS_DOC.read_text(encoding="utf-8")
    guide = ZH_BUILD_GUIDE.read_text(encoding="utf-8")

    assert "构建 Doppel 插件" in plugins
    assert "Doppel Agent 提供了一套插件系统" in plugins
    assert "doppel plugins install user/repo" in plugins
    assert "doppel plugins enable my-plugin" in plugins
    assert "doppel skills tap add <repo>" in plugins
    assert "doppel plugins list" in plugins
    assert "构建 Hermes 插件" not in plugins
    assert "hermes plugins install user/repo" not in plugins
    assert "hermes plugins enable my-plugin" not in plugins
    assert "hermes skills tap add <repo>" not in plugins

    assert 'title: "构建 Doppel 插件"' in guide
    assert "# 构建 Doppel 插件" in guide
    assert "启动 Doppel：" in guide
    assert "\ndoppel\n```" in guide
    assert "doppel plugins install" in guide
    assert "doppel plugins enable <name>" in guide
    assert "doppel my-plugin <subcommand>" in guide
    assert "doppel my-plugin status" in guide
    assert "doppel skills tap add myorg/skills-repo" in guide
    assert "doppel logs --level WARNING | grep -i plugin" in guide
    assert "构建 Hermes 插件" not in guide
    assert "hermes my-plugin <subcommand>" not in guide
    assert "hermes plugins install" not in guide
    assert "hermes plugins enable <name>" not in guide
    assert "hermes skills tap add myorg/skills-repo" not in guide


def test_built_in_and_integration_plugin_docs_prefer_doppel_surfaces():
    en_builtin = EN_BUILTIN_DOC.read_text(encoding="utf-8")
    en_integrations = EN_INTEGRATIONS_DOC.read_text(encoding="utf-8")
    zh_builtin = ZH_BUILTIN_DOC.read_text(encoding="utf-8")
    zh_integrations = ZH_INTEGRATIONS_DOC.read_text(encoding="utf-8")

    assert "Plugins shipped with Doppel Agent" in en_builtin
    assert "Build a Doppel Plugin" in en_builtin
    assert "doppel plugins enable disk-cleanup" in en_builtin
    assert "doppel plugins disable disk-cleanup" in en_builtin
    assert "doppel plugins enable observability/langfuse" in en_builtin
    assert "doppel chat -q \"hello\"" in en_builtin
    assert "doppel dashboard" in en_builtin
    assert "Build a Hermes Plugin" not in en_builtin
    assert "hermes plugins enable disk-cleanup" not in en_builtin
    assert "hermes plugins disable observability/langfuse" not in en_builtin
    assert "hermes dashboard" not in en_builtin

    assert "Extend Doppel Agent with custom tools" in en_integrations
    assert "creating Doppel plugins" in en_integrations
    assert "Extend Hermes with custom tools" not in en_integrations
    assert "creating Hermes plugins" not in en_integrations

    assert "随 Doppel Agent 附带" in zh_builtin
    assert "构建 Doppel 插件" in zh_builtin
    assert "doppel plugins enable disk-cleanup" in zh_builtin
    assert "doppel plugins disable observability/langfuse" in zh_builtin
    assert "doppel dashboard" in zh_builtin
    assert "构建 Hermes 插件" not in zh_builtin
    assert "hermes plugins enable google_meet" not in zh_builtin
    assert "hermes dashboard" not in zh_builtin

    assert "扩展 Doppel Agent" in zh_integrations
    assert "Doppel 插件的分步指南" in zh_integrations
    assert "扩展 Hermes" not in zh_integrations
    assert "Hermes 插件的分步指南" not in zh_integrations
