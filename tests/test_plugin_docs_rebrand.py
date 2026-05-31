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
EN_DEV_GUIDE_DIR = REPO_ROOT / "website" / "docs" / "developer-guide"
ZH_DEV_GUIDE_DIR = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "developer-guide"
)
EN_ADDING_PROVIDERS_DOC = EN_DEV_GUIDE_DIR / "adding-providers.md"
EN_PROVIDER_RUNTIME_DOC = EN_DEV_GUIDE_DIR / "provider-runtime.md"
ZH_ADDING_PROVIDERS_DOC = ZH_DEV_GUIDE_DIR / "adding-providers.md"
ZH_PROVIDER_RUNTIME_DOC = ZH_DEV_GUIDE_DIR / "provider-runtime.md"


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


def test_provider_plugin_developer_guides_prefer_doppel_surfaces():
    en_context = (EN_DEV_GUIDE_DIR / "context-engine-plugin.md").read_text(encoding="utf-8")
    en_image = (EN_DEV_GUIDE_DIR / "image-gen-provider-plugin.md").read_text(encoding="utf-8")
    en_memory = (EN_DEV_GUIDE_DIR / "memory-provider-plugin.md").read_text(encoding="utf-8")
    en_model = (EN_DEV_GUIDE_DIR / "model-provider-plugin.md").read_text(encoding="utf-8")
    en_video = (EN_DEV_GUIDE_DIR / "video-gen-provider-plugin.md").read_text(encoding="utf-8")
    en_web = (EN_DEV_GUIDE_DIR / "web-search-provider-plugin.md").read_text(encoding="utf-8")

    zh_context = (ZH_DEV_GUIDE_DIR / "context-engine-plugin.md").read_text(encoding="utf-8")
    zh_image = (ZH_DEV_GUIDE_DIR / "image-gen-provider-plugin.md").read_text(encoding="utf-8")
    zh_memory = (ZH_DEV_GUIDE_DIR / "memory-provider-plugin.md").read_text(encoding="utf-8")
    zh_model = (ZH_DEV_GUIDE_DIR / "model-provider-plugin.md").read_text(encoding="utf-8")
    zh_video = (ZH_DEV_GUIDE_DIR / "video-gen-provider-plugin.md").read_text(encoding="utf-8")
    zh_web = (ZH_DEV_GUIDE_DIR / "web-search-provider-plugin.md").read_text(encoding="utf-8")

    assert "doppel plugins" in en_context
    assert "hermes plugins" not in en_context
    assert "doppel tools" in en_image
    assert "Build a Doppel Plugin" in en_image
    assert 'doppel -z "Generate an image of a corgi in a spacesuit"' in en_image
    assert "How to build an image-generation backend plugin for Hermes Agent" not in en_image
    assert "hermes plugins enable my-backend" not in en_image
    assert "doppel memory setup" in en_memory
    assert "Usage: doppel my-provider <status|config>" in en_memory
    assert "How to build a memory provider plugin for Hermes Agent" not in en_memory
    assert "hermes my-provider status" not in en_memory
    assert "doppel doctor" in en_model
    assert "Building a Doppel Plugin" in en_model
    assert 'doppel -z "hello" --provider my-provider -m some-model' in en_model
    assert "How to build a model provider (inference backend) plugin for Hermes Agent" not in en_model
    assert "hermes doctor" not in en_model
    assert "doppel tools" in en_video
    assert "How to build a video-generation backend plugin for Hermes Agent" not in en_video
    assert "hermes tools" not in en_video
    assert "doppel tools" in en_web
    assert "Build a Doppel Plugin" in en_web
    assert "How to build a web-search/extract/crawl backend plugin for Hermes Agent" not in en_web
    assert "hermes plugins enable <name>" not in en_web

    assert "doppel plugins" in zh_context
    assert "hermes plugins" not in zh_context
    assert "构建 Doppel 插件" in zh_image
    assert "doppel tools" in zh_image
    assert "如何为 Hermes Agent 构建图像生成后端插件" not in zh_image
    assert "hermes plugins enable my-backend" not in zh_image
    assert "doppel memory setup" in zh_memory
    assert "Usage: doppel my-provider <status|config>" in zh_memory
    assert "如何为 Hermes Agent 构建 memory provider 插件" not in zh_memory
    assert "hermes my-provider status" not in zh_memory
    assert "构建 Doppel 插件" in zh_model
    assert "doppel doctor" in zh_model
    assert 'doppel -z "hello" --provider my-provider -m some-model' in zh_model
    assert "如何为 Hermes Agent 构建模型提供商（推理后端）插件" not in zh_model
    assert "hermes doctor" not in zh_model
    assert "doppel tools" in zh_video
    assert "如何为 Hermes Agent 构建视频生成后端插件" not in zh_video
    assert "hermes tools" not in zh_video
    assert "构建 Doppel 插件" in zh_web
    assert "doppel tools" in zh_web
    assert "如何为 Hermes Agent 构建网页搜索/提取/爬取后端插件" not in zh_web
    assert "hermes plugins enable <name>" not in zh_web


def test_provider_onboarding_docs_prefer_doppel_surfaces():
    en_adding = EN_ADDING_PROVIDERS_DOC.read_text(encoding="utf-8")
    en_runtime = EN_PROVIDER_RUNTIME_DOC.read_text(encoding="utf-8")
    zh_adding = ZH_ADDING_PROVIDERS_DOC.read_text(encoding="utf-8")
    zh_runtime = ZH_PROVIDER_RUNTIME_DOC.read_text(encoding="utf-8")

    assert "Doppel" in en_adding
    assert "Doppel" in en_runtime
    assert "Doppel" in zh_adding
    assert "Doppel" in zh_runtime

    assert "`doppel model`" in en_adding
    assert "`doppel setup`" in en_adding
    assert "`hermes model`" not in en_adding
    assert "`hermes setup`" not in en_adding
    assert "Hermes Agent" not in en_adding
    assert "hermes_cli/main.py" in en_adding
    assert "hermes_cli/setup.py" in en_adding
    assert (
        'python -m hermes_cli.main chat -q "Say hello" --provider your-provider --model your-model'
        in en_adding
    )
    assert "tests/hermes_cli/test_runtime_provider_resolution.py" in en_adding

    assert "`doppel model`" in zh_adding
    assert "`doppel setup`" in zh_adding
    assert "`hermes model`" not in zh_adding
    assert "`hermes setup`" not in zh_adding
    assert "Hermes Agent" not in zh_adding
    assert "hermes_cli/main.py" in zh_adding
    assert "hermes_cli/setup.py" in zh_adding

    assert "`doppel chat`" in en_runtime
    assert "`hermes chat`" not in en_runtime
    assert "Hermes Agent" not in en_runtime
    assert "OPENROUTER_API_KEY" in en_runtime

    assert "`doppel chat`" in zh_runtime
    assert "`hermes chat`" not in zh_runtime
    assert "Hermes Agent" not in zh_runtime
    assert "OPENROUTER_API_KEY" in zh_runtime
