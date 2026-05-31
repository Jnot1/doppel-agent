from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

DEV_GUIDE_CATEGORY = REPO_ROOT / "website" / "docs" / "developer-guide" / "_category_.json"
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
EN_ADDING_TOOLS_DOC = EN_DEV_GUIDE_DIR / "adding-tools.md"
EN_CONTRIBUTING_DOC = EN_DEV_GUIDE_DIR / "contributing.md"
EN_GATEWAY_INTERNALS_DOC = EN_DEV_GUIDE_DIR / "gateway-internals.md"
EN_CONTEXT_COMPRESSION_DOC = EN_DEV_GUIDE_DIR / "context-compression-and-caching.md"
EN_ADDING_PLATFORM_ADAPTERS_DOC = EN_DEV_GUIDE_DIR / "adding-platform-adapters.md"
EN_CREATING_SKILLS_DOC = EN_DEV_GUIDE_DIR / "creating-skills.md"
EN_ACP_INTERNALS_DOC = EN_DEV_GUIDE_DIR / "acp-internals.md"
EN_EXTENDING_CLI_DOC = EN_DEV_GUIDE_DIR / "extending-the-cli.md"
EN_ARCHITECTURE_DOC = EN_DEV_GUIDE_DIR / "architecture.md"
EN_PROMPT_ASSEMBLY_DOC = EN_DEV_GUIDE_DIR / "prompt-assembly.md"
EN_SESSION_STORAGE_DOC = EN_DEV_GUIDE_DIR / "session-storage.md"
EN_TRAJECTORY_DOC = EN_DEV_GUIDE_DIR / "trajectory-format.md"
EN_CONTEXT_FILES_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "context-files.md"
EN_PERSONALITY_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "personality.md"
EN_GOALS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "goals.md"
EN_PROVIDER_ROUTING_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "provider-routing.md"
)
EN_CONTEXT_REFERENCES_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "context-references.md"
)
EN_TOOL_GATEWAY_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "tool-gateway.md"
)
EN_SUBSCRIPTION_PROXY_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "subscription-proxy.md"
)
EN_TOOLS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "tools.md"
EN_FALLBACK_PROVIDERS_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "fallback-providers.md"
)
EN_CREDENTIAL_POOLS_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "credential-pools.md"
)
EN_CRON_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "cron.md"
EN_BROWSER_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "browser.md"
EN_CODEX_RUNTIME_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "codex-app-server-runtime.md"
)
EN_MCP_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "mcp.md"
EN_KANBAN_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "kanban.md"
EN_HOOKS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "hooks.md"
EN_USE_SOUL_DOC = REPO_ROOT / "website" / "docs" / "guides" / "use-soul-with-hermes.md"
ZH_ADDING_PROVIDERS_DOC = ZH_DEV_GUIDE_DIR / "adding-providers.md"
ZH_PROVIDER_RUNTIME_DOC = ZH_DEV_GUIDE_DIR / "provider-runtime.md"
ZH_ADDING_TOOLS_DOC = ZH_DEV_GUIDE_DIR / "adding-tools.md"
ZH_CONTRIBUTING_DOC = ZH_DEV_GUIDE_DIR / "contributing.md"
ZH_GATEWAY_INTERNALS_DOC = ZH_DEV_GUIDE_DIR / "gateway-internals.md"
ZH_CONTEXT_COMPRESSION_DOC = ZH_DEV_GUIDE_DIR / "context-compression-and-caching.md"
ZH_ADDING_PLATFORM_ADAPTERS_DOC = ZH_DEV_GUIDE_DIR / "adding-platform-adapters.md"
ZH_CREATING_SKILLS_DOC = ZH_DEV_GUIDE_DIR / "creating-skills.md"
ZH_ACP_INTERNALS_DOC = ZH_DEV_GUIDE_DIR / "acp-internals.md"
ZH_EXTENDING_CLI_DOC = ZH_DEV_GUIDE_DIR / "extending-the-cli.md"
ZH_ARCHITECTURE_DOC = ZH_DEV_GUIDE_DIR / "architecture.md"
ZH_PROMPT_ASSEMBLY_DOC = ZH_DEV_GUIDE_DIR / "prompt-assembly.md"
ZH_SESSION_STORAGE_DOC = ZH_DEV_GUIDE_DIR / "session-storage.md"
ZH_TRAJECTORY_DOC = ZH_DEV_GUIDE_DIR / "trajectory-format.md"
ZH_CONTEXT_FILES_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "context-files.md"
)
ZH_PERSONALITY_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "personality.md"
)
ZH_GOALS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "goals.md"
)
ZH_PROVIDER_ROUTING_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "provider-routing.md"
)
ZH_CONTEXT_REFERENCES_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "context-references.md"
)
ZH_TOOL_GATEWAY_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "tool-gateway.md"
)
ZH_SUBSCRIPTION_PROXY_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "subscription-proxy.md"
)
ZH_TOOLS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "tools.md"
)
ZH_FALLBACK_PROVIDERS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "fallback-providers.md"
)
ZH_CREDENTIAL_POOLS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "credential-pools.md"
)
ZH_CRON_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "cron.md"
)
ZH_BROWSER_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "browser.md"
)
ZH_CODEX_RUNTIME_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "codex-app-server-runtime.md"
)
ZH_MCP_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "mcp.md"
)
ZH_KANBAN_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "kanban.md"
)
ZH_HOOKS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "hooks.md"
)
ZH_USE_SOUL_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "guides"
    / "use-soul-with-hermes.md"
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


def test_tooling_and_contributing_docs_prefer_doppel_surfaces():
    en_tools = EN_ADDING_TOOLS_DOC.read_text(encoding="utf-8")
    en_contributing = EN_CONTRIBUTING_DOC.read_text(encoding="utf-8")
    zh_tools = ZH_ADDING_TOOLS_DOC.read_text(encoding="utf-8")
    zh_contributing = ZH_CONTRIBUTING_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent" in en_tools
    assert "built-in Doppel tool" in en_tools
    assert "Build a Doppel Plugin" in en_tools
    assert 'doppel chat -q "Use the weather tool for London"' in en_tools
    assert "Build a Hermes Plugin" not in en_tools
    assert 'hermes chat -q "Use the weather tool for London"' not in en_tools
    assert "_HERMES_CORE_TOOLS" in en_tools
    assert "hermes_cli/config.py" in en_tools

    assert "Doppel Agent" in en_contributing
    assert "https://github.com/Jnot1/doppel-agent.git" in en_contributing
    assert "cd doppel-agent" in en_contributing
    assert "~/.doppel" in en_contributing
    assert "doppel doctor" in en_contributing
    assert 'doppel chat -q "Hello"' in en_contributing
    assert "doppel version" in en_contributing
    assert "https://github.com/Jnot1/doppel-agent/issues" in en_contributing
    assert "https://github.com/Jnot1/doppel-agent/blob/main/LICENSE" in en_contributing
    assert "https://github.com/NousResearch/hermes-agent.git" not in en_contributing
    assert "hermes doctor" not in en_contributing
    assert 'hermes chat -q "Hello"' not in en_contributing
    assert "get_hermes_home()" in en_contributing
    assert "display_hermes_home()" in en_contributing

    assert "Doppel Agent" in zh_tools
    assert "Doppel 内置工具" in zh_tools
    assert "构建 Doppel 插件" in zh_tools
    assert 'doppel chat -q "Use the weather tool for London"' in zh_tools
    assert "构建 Hermes 插件" not in zh_tools
    assert 'hermes chat -q "Use the weather tool for London"' not in zh_tools
    assert "_HERMES_CORE_TOOLS" in zh_tools
    assert "hermes_cli/config.py" in zh_tools

    assert "Doppel Agent" in zh_contributing
    assert "https://github.com/Jnot1/doppel-agent.git" in zh_contributing
    assert "cd doppel-agent" in zh_contributing
    assert "~/.doppel" in zh_contributing
    assert "doppel doctor" in zh_contributing
    assert 'doppel chat -q "Hello"' in zh_contributing
    assert "doppel version" in zh_contributing
    assert "https://github.com/Jnot1/doppel-agent/issues" in zh_contributing
    assert "https://github.com/Jnot1/doppel-agent/blob/main/LICENSE" in zh_contributing
    assert "https://github.com/NousResearch/hermes-agent.git" not in zh_contributing
    assert "hermes doctor" not in zh_contributing
    assert 'hermes chat -q "Hello"' not in zh_contributing
    assert "get_hermes_home()" in zh_contributing
    assert "display_hermes_home()" in zh_contributing


def test_gateway_and_context_docs_prefer_doppel_surfaces():
    en_gateway = EN_GATEWAY_INTERNALS_DOC.read_text(encoding="utf-8")
    en_context = EN_CONTEXT_COMPRESSION_DOC.read_text(encoding="utf-8")
    zh_gateway = ZH_GATEWAY_INTERNALS_DOC.read_text(encoding="utf-8")
    zh_context = ZH_CONTEXT_COMPRESSION_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent" in en_gateway
    assert "doppel send" in en_gateway
    assert "doppel gateway start" in en_gateway
    assert "doppel gateway stop" in en_gateway
    assert "doppel gateway stop --all" in en_gateway
    assert "`hermes send`" not in en_gateway
    assert "`hermes gateway start`" not in en_gateway
    assert "`hermes gateway stop`" not in en_gateway
    assert "`hermes gateway stop --all`" not in en_gateway
    assert "~/.hermes/.env" in en_gateway
    assert "~/.hermes/config.yaml" in en_gateway
    assert "~/.hermes/gateway.pid" in en_gateway
    assert "~/.hermes/hooks/" in en_gateway
    assert "TELEGRAM_ALLOW_ALL_USERS" in en_gateway
    assert "GATEWAY_ALLOW_ALL_USERS" in en_gateway
    assert "build_session_key()" in en_gateway
    assert "GATEWAY_KNOWN_COMMANDS" in en_gateway
    assert "start_gateway()" in en_gateway
    assert "telegram:-1001234567890" in en_gateway
    assert "/approve" in en_gateway
    assert "/stop" in en_gateway
    assert "send_message" in en_gateway
    assert "agent:main:{platform}:{chat_type}:{chat_id}" in en_gateway

    assert "Doppel Agent" in zh_gateway
    assert "doppel send" in zh_gateway
    assert "doppel gateway start" in zh_gateway
    assert "doppel gateway stop" in zh_gateway
    assert "doppel gateway stop --all" in zh_gateway
    assert "`hermes send`" not in zh_gateway
    assert "`hermes gateway start`" not in zh_gateway
    assert "`hermes gateway stop`" not in zh_gateway
    assert "`hermes gateway stop --all`" not in zh_gateway
    assert "~/.hermes/.env" in zh_gateway
    assert "~/.hermes/config.yaml" in zh_gateway
    assert "~/.hermes/gateway.pid" in zh_gateway
    assert "~/.hermes/hooks/" in zh_gateway
    assert "TELEGRAM_ALLOW_ALL_USERS" in zh_gateway
    assert "GATEWAY_ALLOW_ALL_USERS" in zh_gateway
    assert "build_session_key()" in zh_gateway
    assert "GATEWAY_KNOWN_COMMANDS" in zh_gateway
    assert "start_gateway()" in zh_gateway
    assert "telegram:-1001234567890" in zh_gateway
    assert "/approve" in zh_gateway
    assert "/stop" in zh_gateway
    assert "send_message" in zh_gateway
    assert "agent:main:{platform}:{chat_type}:{chat_id}" in zh_gateway

    assert "Doppel Agent" in en_context
    assert "doppel plugins" in en_context
    assert "Doppel Agent has two separate compression layers" in en_context
    assert "Doppel Agent\nuses the \"system_and_3\" strategy:" in en_context
    assert "Hermes Agent uses a dual compression system" not in en_context
    assert "`hermes plugins`" not in en_context
    assert "agent/context_engine.py" in en_context
    assert "apply_anthropic_cache_control()" in en_context
    assert "compression.threshold" in en_context
    assert "run_agent.py" in en_context
    assert "cache_control" in en_context
    assert "No intermediate pressure warnings — they caused models to 'give up' prematurely on complex tasks" in en_context

    assert "Doppel Agent" in zh_context
    assert "doppel plugins" in zh_context
    assert "Doppel Agent 有两个独立运行的压缩层" in zh_context
    assert 'Doppel Agent 使用"system_and_3"策略：' in zh_context
    assert "Hermes Agent 使用双重压缩系统" not in zh_context
    assert "`hermes plugins`" not in zh_context
    assert "agent/context_engine.py" in zh_context
    assert "apply_anthropic_cache_control()" in zh_context
    assert "compression.threshold" in zh_context
    assert "run_agent.py" in zh_context
    assert "cache_control" in zh_context
    assert "No intermediate pressure warnings — they caused models to 'give up' prematurely on complex tasks" in zh_context


def test_platform_adapter_and_skill_docs_prefer_doppel_surfaces():
    en_adapters = EN_ADDING_PLATFORM_ADAPTERS_DOC.read_text(encoding="utf-8")
    en_skills = EN_CREATING_SKILLS_DOC.read_text(encoding="utf-8")
    zh_adapters = ZH_ADDING_PLATFORM_ADAPTERS_DOC.read_text(encoding="utf-8")
    zh_skills = ZH_CREATING_SKILLS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent" in en_adapters
    assert "Doppel gateway" in en_adapters
    assert "Doppel plugin system" in en_adapters
    assert "doppel config" in en_adapters
    assert "doppel status" in en_adapters
    assert "doppel gateway setup" in en_adapters
    assert "doppel tools" in en_adapters
    assert "doppel skills" in en_adapters
    assert "doppel gateway status" in en_adapters
    assert "doppel cron run" in en_adapters
    assert "`hermes config`" not in en_adapters
    assert "`hermes status`" not in en_adapters
    assert "`hermes gateway setup`" not in en_adapters
    assert "`hermes tools`" not in en_adapters
    assert "`hermes skills`" not in en_adapters
    assert "`hermes cron run`" not in en_adapters
    assert "Hermes core codebase" not in en_adapters
    assert "~/.hermes/plugins/" in en_adapters
    assert "hermes_cli/config.py" in en_adapters
    assert "hermes-newplat" in en_adapters
    assert "MY_PLATFORM_CHANNEL" in en_adapters
    assert "NEWPLAT_TOKEN" in en_adapters

    assert "Doppel Agent" in zh_adapters
    assert "Doppel gateway" in zh_adapters
    assert "Doppel plugin 系统" in zh_adapters
    assert "doppel config" in zh_adapters
    assert "doppel status" in zh_adapters
    assert "doppel gateway setup" in zh_adapters
    assert "doppel tools" in zh_adapters
    assert "doppel skills" in zh_adapters
    assert "doppel gateway status" in zh_adapters
    assert "doppel cron run" in zh_adapters
    assert "`hermes config`" not in zh_adapters
    assert "`hermes status`" not in zh_adapters
    assert "`hermes gateway setup`" not in zh_adapters
    assert "`hermes tools`" not in zh_adapters
    assert "`hermes skills`" not in zh_adapters
    assert "`hermes cron run`" not in zh_adapters
    assert "Hermes 核心代码库" not in zh_adapters
    assert "~/.hermes/plugins/" in zh_adapters
    assert "hermes_cli/config.py" in zh_adapters
    assert "hermes-newplat" in zh_adapters
    assert "MY_PLATFORM_CHANNEL" in zh_adapters
    assert "NEWPLAT_TOKEN" in zh_adapters

    assert "Doppel Agent" in en_skills
    assert "doppel config migrate" in en_skills
    assert "doppel config show" in en_skills
    assert "doppel config set" in en_skills
    assert 'doppel chat --toolsets skills -q "Use the X skill to do Y"' in en_skills
    assert "doppel skills browse" in en_skills
    assert "doppel skills install" in en_skills
    assert "doppel skills publish" in en_skills
    assert "doppel skills tap add" in en_skills
    assert "Doppel Agent can now consume third-party skills" in en_skills
    assert "hermes config migrate" not in en_skills
    assert "hermes config show" not in en_skills
    assert "hermes config set" not in en_skills
    assert "hermes skills browse" not in en_skills
    assert "hermes skills install" not in en_skills
    assert "hermes skills publish" not in en_skills
    assert "hermes skills tap add" not in en_skills
    assert "Hermes Agent" not in en_skills
    assert "hermes:" in en_skills
    assert "${HERMES_SKILL_DIR}" in en_skills
    assert "${HERMES_SESSION_ID}" in en_skills
    assert "~/.hermes/.env" in en_skills
    assert "~/.hermes/config.yaml" in en_skills

    assert "Doppel Agent" in zh_skills
    assert "doppel config migrate" in zh_skills
    assert "doppel config show" in zh_skills
    assert "doppel config set" in zh_skills
    assert 'doppel chat --toolsets skills -q "Use the X skill to do Y"' in zh_skills
    assert "doppel skills browse" in zh_skills
    assert "doppel skills install" in zh_skills
    assert "doppel skills publish" in zh_skills
    assert "doppel skills tap add" in zh_skills
    assert "Doppel Agent 现在可以通过多种外部发现模型使用第三方 skill" in zh_skills
    assert "hermes config migrate" not in zh_skills
    assert "hermes config show" not in zh_skills
    assert "hermes config set" not in zh_skills
    assert "hermes skills browse" not in zh_skills
    assert "hermes skills install" not in zh_skills
    assert "hermes skills publish" not in zh_skills
    assert "hermes skills tap add" not in zh_skills
    assert "Hermes Agent" not in zh_skills
    assert "hermes:" in zh_skills
    assert "${HERMES_SKILL_DIR}" in zh_skills
    assert "${HERMES_SESSION_ID}" in zh_skills
    assert "~/.hermes/.env" in zh_skills
    assert "~/.hermes/config.yaml" in zh_skills


def test_acp_and_cli_extension_docs_prefer_doppel_surfaces():
    en_acp = EN_ACP_INTERNALS_DOC.read_text(encoding="utf-8")
    en_cli = EN_EXTENDING_CLI_DOC.read_text(encoding="utf-8")
    zh_acp = ZH_ACP_INTERNALS_DOC.read_text(encoding="utf-8")
    zh_cli = ZH_EXTENDING_CLI_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent" in en_acp
    assert "Doppel ACP adapter" in en_acp
    assert "Doppel `once`" in en_acp
    assert "Doppel `always`" in en_acp
    assert "Doppel `deny`" in en_acp
    assert "Doppel Agent tools" in en_acp
    assert "Doppel Agent's runtime resolver" in en_acp
    assert "Doppel Agent's interactive model/provider configuration" in en_acp
    assert "hermes-acp" in en_acp
    assert "`hermes-setup`" in en_acp
    assert "~/.hermes/.env" in en_acp
    assert "~/.hermes/state.db" in en_acp
    assert "hermes_cli/runtime_provider.py" in en_acp
    assert "hermes_cli/main.py" in en_acp

    assert "Doppel Agent" in zh_acp
    assert "Doppel ACP 适配器" in zh_acp
    assert "Doppel `once`" in zh_acp
    assert "Doppel `always`" in zh_acp
    assert "Doppel `deny`" in zh_acp
    assert "Doppel Agent 工具" in zh_acp
    assert "Doppel Agent 的运行时解析器" in zh_acp
    assert "Doppel Agent 的交互式模型/provider 配置" in zh_acp
    assert "hermes-acp" in zh_acp
    assert "`hermes-setup`" in zh_acp
    assert "~/.hermes/.env" in zh_acp
    assert "~/.hermes/state.db" in zh_acp
    assert "hermes_cli/runtime_provider.py" in zh_acp
    assert "hermes_cli/main.py" in zh_acp

    assert "Doppel TUI" in en_cli
    assert "Doppel Agent exposes protected extension hooks" in en_cli
    assert "extends Doppel" in en_cli
    assert "Doppel Agent registers its own keybindings" in en_cli
    assert "HermesCLI" in en_cli
    assert "cd ~/.hermes/hermes-agent" in en_cli
    assert "Hermes TUI" not in en_cli

    assert "Doppel TUI" in zh_cli
    assert "Doppel Agent 在 `HermesCLI` 上暴露了受保护的扩展 hook" in zh_cli
    assert "extends Doppel" in zh_cli
    assert "在 Doppel Agent 注册自身快捷键之后" in zh_cli
    assert "HermesCLI" in zh_cli
    assert "cd ~/.hermes/hermes-agent" in zh_cli
    assert "Hermes TUI" not in zh_cli


def test_architecture_and_trajectory_docs_prefer_doppel_surfaces():
    en_arch = EN_ARCHITECTURE_DOC.read_text(encoding="utf-8")
    zh_arch = ZH_ARCHITECTURE_DOC.read_text(encoding="utf-8")
    en_traj = EN_TRAJECTORY_DOC.read_text(encoding="utf-8")
    zh_traj = ZH_TRAJECTORY_DOC.read_text(encoding="utf-8")

    assert "Hermes Agent internals" not in en_arch
    assert "Hermes Agent 内部结构" not in zh_arch
    assert "Doppel Agent internals" in en_arch
    assert "Doppel Agent 内部结构" in zh_arch
    assert "all `doppel` subcommands" in en_arch
    assert "所有 `doppel` 子命令" in zh_arch
    assert "doppel plugins" in en_arch
    assert "doppel plugins" in zh_arch
    assert "Build a Doppel Plugin" in en_arch
    assert "构建 Doppel 插件" in zh_arch
    assert "Exposes Doppel Agent as an editor-native agent" in en_arch
    assert "将 Doppel Agent 作为编辑器原生 agent 暴露给" in zh_arch
    assert "`doppel -p <name>`" in en_arch
    assert "`doppel -p <name>`" in zh_arch
    assert "AIAgent" in en_arch
    assert "AIAgent" in zh_arch
    assert "HermesCLI" in en_arch
    assert "HermesCLI" in zh_arch
    assert "run_agent.py" in en_arch
    assert "run_agent.py" in zh_arch
    assert "HERMES_HOME" in en_arch
    assert "HERMES_HOME" in zh_arch
    assert "~/.hermes/plugins/" in en_arch
    assert "~/.hermes/plugins/" in zh_arch

    assert "Hermes Agent saves conversation trajectories" not in en_traj
    assert "Hermes Agent 以 ShareGPT 兼容的 JSONL 格式保存对话轨迹" not in zh_traj
    assert "Doppel Agent saves conversation trajectories" in en_traj
    assert "Doppel Agent 以 ShareGPT 兼容的 JSONL 格式保存对话轨迹" in zh_traj
    assert "Doppel Agent function-calling prompt template" in en_traj
    assert "Doppel Agent 函数调用 prompt 模板" in zh_traj
    assert "FunctionCall" in en_traj
    assert "FunctionCall" in zh_traj
    assert "_save_trajectory" in en_traj
    assert "_save_trajectory" in zh_traj
    assert "model_tools.TOOL_TO_TOOLSET_MAP" in en_traj
    assert "model_tools.TOOL_TO_TOOLSET_MAP" in zh_traj
    assert "trajectory_samples.jsonl" in en_traj
    assert "trajectory_samples.jsonl" in zh_traj
    assert "failed_trajectories.jsonl" in en_traj
    assert "failed_trajectories.jsonl" in zh_traj
    assert '"tool_call_id"' in en_traj
    assert '"tool_call_id"' in zh_traj
    assert '"gpt"' in en_traj
    assert '"gpt"' in zh_traj


def test_session_storage_and_dev_guide_category_prefer_doppel_surfaces():
    en_session = EN_SESSION_STORAGE_DOC.read_text(encoding="utf-8")
    zh_session = ZH_SESSION_STORAGE_DOC.read_text(encoding="utf-8")
    dev_category = DEV_GUIDE_CATEGORY.read_text(encoding="utf-8")

    assert "Doppel Agent uses a SQLite database" in en_session
    assert "Doppel Agent 使用 SQLite 数据库" in zh_session
    assert "Hermes Agent uses a SQLite database" not in en_session
    assert "Hermes Agent 使用 SQLite 数据库" not in zh_session
    assert "Multiple Doppel processes" in en_session
    assert "多个 Doppel 进程" in zh_session
    assert "Preferred default path: `~/.doppel/state.db`" in en_session
    assert "首选默认路径：`~/.doppel/state.db`" in zh_session
    assert "~/.hermes/state.db" in en_session
    assert "~/.hermes/state.db" in zh_session
    assert "DOPPEL_HOME" in en_session
    assert "DOPPEL_HOME" in zh_session
    assert "hermes_state.py" in en_session
    assert "hermes_state.py" in zh_session
    assert "hermes_constants.get_hermes_home()" in en_session
    assert "hermes_constants.get_hermes_home()" in zh_session
    assert "HERMES_HOME" in en_session
    assert "HERMES_HOME" in zh_session

    assert "Contribute to Doppel Agent" in dev_category
    assert "Contribute to Hermes Agent" not in dev_category


def test_prompt_assembly_docs_prefer_doppel_surfaces_but_keep_runtime_literals():
    en_prompt = EN_PROMPT_ASSEMBLY_DOC.read_text(encoding="utf-8")
    zh_prompt = ZH_PROMPT_ASSEMBLY_DOC.read_text(encoding="utf-8")

    assert "How Doppel Agent builds the system prompt" in en_prompt
    assert "Doppel Agent deliberately separates" in en_prompt
    assert "How Hermes builds the system prompt" not in en_prompt
    assert "Hermes deliberately separates" not in en_prompt
    assert "Doppel-native project config" in en_prompt
    assert "Hermes-native project config" not in en_prompt
    assert "Doppel Agent already loads" in en_prompt
    assert "without forking Doppel Agent" in en_prompt
    assert "~/.doppel/SOUL.md" in en_prompt
    assert "~/.doppel/MEMORY.md" in en_prompt
    assert "change how Doppel Agent assembles prompts for everyone" in en_prompt

    assert "Doppel Agent 如何构建系统 prompt" in zh_prompt
    assert "Doppel Agent 刻意将以下内容分离" in zh_prompt
    assert "Hermes 如何构建系统 prompt" not in zh_prompt
    assert "Hermes 刻意将以下内容分离" not in zh_prompt
    assert "Doppel 原生项目配置" in zh_prompt
    assert "Hermes 原生项目配置" not in zh_prompt
    assert "Doppel Agent 已加载的 prompt 输入" in zh_prompt
    assert "无需 fork Doppel Agent" in zh_prompt
    assert "~/.doppel/SOUL.md" in zh_prompt
    assert "~/.doppel/MEMORY.md" in zh_prompt
    assert "Doppel Agent 为所有人组装 prompt 的方式" in zh_prompt

    assert "You are Hermes, an AI assistant created by Nous Research." in en_prompt
    assert "You are Hermes Agent, an intelligent AI assistant created by Nous Research." in en_prompt
    assert "You are Hermes, an AI assistant created by Nous Research." in zh_prompt
    assert "You are Hermes Agent, an intelligent AI assistant created by Nous Research." in zh_prompt
    assert "HERMES.md" in en_prompt and "HERMES_HOME" in en_prompt
    assert "HERMES_EPHEMERAL_SYSTEM_PROMPT" in en_prompt
    assert "HERMES.md" in zh_prompt and "HERMES_HOME" in zh_prompt
    assert "HERMES_EPHEMERAL_SYSTEM_PROMPT" in zh_prompt
    assert "DEFAULT_AGENT_IDENTITY" in en_prompt
    assert "DEFAULT_AGENT_IDENTITY" in zh_prompt
    assert "~/.hermes/" in en_prompt and "~/.hermes/" in zh_prompt
    assert "build_context_files_prompt(skip_soul=True)" in en_prompt
    assert "build_context_files_prompt(skip_soul=True)" in zh_prompt


def test_context_files_and_soul_guide_prefer_doppel_surfaces_but_keep_literals():
    en_context = EN_CONTEXT_FILES_DOC.read_text(encoding="utf-8")
    zh_context = ZH_CONTEXT_FILES_DOC.read_text(encoding="utf-8")
    en_soul = EN_USE_SOUL_DOC.read_text(encoding="utf-8")
    zh_soul = ZH_USE_SOUL_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent automatically discovers and loads context files" in en_context
    assert "Doppel Agent 会自动发现并加载上下文文件" in zh_context
    assert "Hermes Agent automatically discovers and loads context files" not in en_context
    assert "Hermes Agent 会自动发现并加载上下文文件" not in zh_context
    assert "current Doppel Agent instance" in en_context
    assert "当前 Doppel Agent 实例" in zh_context
    assert "Doppel Agent loads the `AGENTS.md`" in en_context
    assert "Doppel Agent 将工作目录中的 `AGENTS.md`" in zh_context
    assert "Doppel Agent is compatible with Cursor IDE" in en_context
    assert "Doppel Agent 兼容 Cursor IDE" in zh_context
    assert "~/.doppel/SOUL.md" in en_context
    assert "~/.doppel/SOUL.md" in zh_context
    assert "DOPPEL_HOME" in en_context
    assert "DOPPEL_HOME" in zh_context
    assert "HERMES_HOME" in en_context
    assert "HERMES_HOME" in zh_context
    assert ".hermes.md" in en_context
    assert ".hermes.md" in zh_context
    assert "HERMES.md" in en_context
    assert "HERMES.md" in zh_context
    assert "build_context_files_prompt()" in en_context
    assert "SubdirectoryHintTracker" in en_context
    assert "agent/subdirectory_hints.py" in en_context

    assert 'title: "Use SOUL.md with Doppel Agent"' in en_soul
    assert "# Use SOUL.md with Doppel Agent" in en_soul
    assert 'title: "在 Doppel Agent 中使用 SOUL.md"' in zh_soul
    assert "# 在 Doppel Agent 中使用 SOUL.md" in zh_soul
    assert "**primary identity** for your Doppel Agent instance" in en_soul
    assert "你的 Doppel Agent 实例的**主要身份标识**" in zh_soul
    assert "replace the built-in default persona entirely with your own" in en_soul
    assert "完全替换内置默认人设" in zh_soul
    assert "Doppel Agent now uses only the global SOUL file" in en_soul
    assert "Doppel Agent 目前仅使用当前实例的全局 SOUL 文件" in zh_soul
    assert "~/.doppel/SOUL.md" in en_soul
    assert "~/.doppel/SOUL.md" in zh_soul
    assert "$DOPPEL_HOME/SOUL.md" in en_soul
    assert "$DOPPEL_HOME/SOUL.md" in zh_soul
    assert "$HERMES_HOME/SOUL.md" in en_soul
    assert "$HERMES_HOME/SOUL.md" in zh_soul
    assert "Doppel Agent automatically seeds a starter `SOUL.md`" in en_soul
    assert "Doppel Agent 会自动为你生成一个初始文件" in zh_soul
    assert "When Doppel Agent starts a session" in en_soul
    assert "Doppel Agent 启动会话时" in zh_soul
    assert "Doppel Agent already tries to be helpful and clear" in en_soul
    assert "Doppel Agent 本身已经尽力做到有帮助且清晰" in zh_soul
    assert "Who Doppel Agent is." in en_soul
    assert "Who Doppel Agent is." in zh_soul
    assert "How Doppel Agent should sound." in en_soul
    assert "How Doppel Agent should sound." in zh_soul
    assert "nano ~/.doppel/SOUL.md" in en_soul
    assert "nano ~/.doppel/SOUL.md" in zh_soul
    assert "restart Doppel Agent or start a new session" in en_soul
    assert "重启 Doppel Agent 或开启新会话" in zh_soul
    assert "Talk to Doppel Agent for a while" in en_soul
    assert "与 Doppel Agent 交谈一段时间" in zh_soul
    assert "I edited SOUL.md but Doppel Agent still sounds the same" in en_soul
    assert "我编辑了 SOUL.md，但 Doppel Agent 听起来还是一样" in zh_soul
    assert "Doppel Agent is ignoring parts of my SOUL.md" in en_soul
    assert "Doppel Agent 忽略了我 SOUL.md 中的部分内容" in zh_soul
    assert "/personality" in en_soul
    assert "/personality" in zh_soul
    assert "~/.hermes/SOUL.md" in en_soul
    assert "~/.hermes/SOUL.md" in zh_soul


def test_personality_feature_docs_prefer_doppel_surfaces_and_keep_literals():
    en = EN_PERSONALITY_DOC.read_text(encoding="utf-8")
    zh = ZH_PERSONALITY_DOC.read_text(encoding="utf-8")

    assert "Customize Doppel Agent's personality" in en
    assert "自定义 Doppel Agent 的个性" in zh
    assert "Doppel Agent's personality is fully customizable" in en
    assert "Doppel Agent 的个性完全可自定义" in zh
    assert "~/.doppel/SOUL.md" in en
    assert "~/.doppel/SOUL.md" in zh
    assert "$DOPPEL_HOME/SOUL.md" in en
    assert "$DOPPEL_HOME/SOUL.md" in zh
    assert "Doppel Agent ships with built-in personalities" in en
    assert "Doppel Agent 内置了多种个性" in zh
    assert "Captain Doppel" in en
    assert "Doppel 船长" in zh
    assert "Use SOUL.md with Doppel Agent" in en
    assert "在 Doppel Agent 中使用 SOUL.md" in zh
    assert "affect how Doppel Agent speaks" in en
    assert "影响 Doppel Agent 的说话方式" in zh

    assert "HERMES_HOME" in en and "HERMES_HOME" in zh
    assert "~/.hermes/SOUL.md" in en and "~/.hermes/SOUL.md" in zh
    assert "$HERMES_HOME/SOUL.md" in en and "$HERMES_HOME/SOUL.md" in zh
    assert "/personality" in en and "/personality" in zh
    assert "You are Hermes Agent, an intelligent AI assistant created by Nous Research..." in en
    assert "You are Hermes Agent, an intelligent AI assistant created by Nous Research..." in zh
    assert "~/.hermes/config.yaml" in en
    assert "~/.hermes/config.yaml" in zh

    assert "Customize Hermes Agent's personality" not in en
    assert "自定义 Hermes Agent 的个性" not in zh
    assert "Hermes Agent's personality is fully customizable" not in en
    assert "Hermes Agent 的个性完全可自定义" not in zh


def test_goals_feature_docs_prefer_doppel_surfaces_and_keep_goal_literals():
    en = EN_GOALS_DOC.read_text(encoding="utf-8")
    zh = ZH_GOALS_DOC.read_text(encoding="utf-8")

    assert "let Doppel Agent keep working across turns" in en
    assert "让 Doppel Agent 跨轮次持续工作直到完成" in zh
    assert "`/goal` gives Doppel Agent a standing objective" in en
    assert "`/goal` 为 Doppel Agent 设置一个跨轮次持续存在的目标" in zh
    assert "adapted to Doppel Agent's architecture" in en
    assert "已适配 Doppel Agent 的架构" in zh
    assert "Use `/goal` for tasks where you want Doppel Agent to iterate" in en
    assert "当你希望 Doppel Agent 自主迭代" in zh
    assert "Doppel Agent starts working as if you'd sent the goal as a normal message." in en
    assert "Doppel Agent 开始工作，就像你发送了一条普通消息一样。" in zh
    assert "Add to `~/.doppel/config.yaml`" in en
    assert "在 `~/.doppel/config.yaml` 中添加" in zh
    assert "Legacy installs may still keep this under `~/.hermes/config.yaml`." in en
    assert "legacy 安装仍可能将这段配置保留在 `~/.hermes/config.yaml` 中。" in zh
    assert "Doppel: Creating /tmp/note_1.txt now." in en
    assert "Doppel: Creating /tmp/note_1.txt now." in zh
    assert "`/goal` is Doppel Agent's take on the **Ralph loop** pattern." in en
    assert "`/goal` 是 Doppel Agent 对 **Ralph loop** 模式的实现。" in zh

    assert "/goal" in en and "/goal" in zh
    assert "Codex CLI 0.128.0" in en and "Codex CLI 0.128.0" in zh
    assert "Ralph loop" in en and "Ralph loop" in zh
    assert "tests/hermes_cli/" in en and "tests/hermes_cli/" in zh
    assert "~/.hermes/config.yaml" in en and "~/.hermes/config.yaml" in zh
    assert "SessionDB.state_meta" in en and "SessionDB.state_meta" in zh

    assert "let Hermes keep working across turns" not in en
    assert "让 Hermes 跨轮次持续工作直到完成" not in zh
    assert "`/goal` gives Hermes a standing objective" not in en
    assert "`/goal` 为 Hermes 设置一个跨轮次持续存在的目标" not in zh


def test_provider_routing_docs_prefer_doppel_surfaces_and_keep_legacy_config_note():
    en = EN_PROVIDER_ROUTING_DOC.read_text(encoding="utf-8")
    zh = ZH_PROVIDER_ROUTING_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent supports **provider routing**" in en
    assert "Doppel Agent 支持 **provider routing**" in zh
    assert "`~/.doppel/config.yaml`" in en
    assert "`~/.doppel/config.yaml`" in zh
    assert "Legacy installs may still keep this in `~/.hermes/config.yaml`." in en
    assert "legacy 安装仍可能将这段配置保留在 `~/.hermes/config.yaml` 中。" in zh
    assert "loaded at startup (legacy installs may still use `~/.hermes/config.yaml`)" in en
    assert "启动时加载（legacy 安装仍可能使用 `~/.hermes/config.yaml`）" in zh
    assert "~/.hermes/config.yaml" in en
    assert "~/.hermes/config.yaml" in zh

    assert "Hermes Agent supports **provider routing**" not in en
    assert "Hermes Agent 支持 **provider routing**" not in zh


def test_context_references_docs_prefer_doppel_prose_and_keep_blocked_literals():
    en = EN_CONTEXT_REFERENCES_DOC.read_text(encoding="utf-8")
    zh = ZH_CONTEXT_REFERENCES_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent expands the reference inline" in en
    assert "Doppel Agent 会将引用内联展开" in zh
    assert "Doppel env: `$HERMES_HOME/.env`" in en
    assert "Doppel 环境文件：`$HERMES_HOME/.env`" in zh
    assert "$HERMES_HOME/.env" in en and "$HERMES_HOME/.env" in zh
    assert "$HERMES_HOME/skills/.hub/" in en and "$HERMES_HOME/skills/.hub/" in zh
    assert "`@file:`" in en and "`@file:`" in zh
    assert "`@folder:`" in en and "`@folder:`" in zh
    assert "`@url:`" in en and "`@url:`" in zh

    assert "Hermes expands the reference inline" not in en
    assert "Hermes 会将引用内联展开" not in zh
    assert "Hermes env: `$HERMES_HOME/.env`" not in en
    assert "Hermes 环境文件：`$HERMES_HOME/.env`" not in zh


def test_tool_gateway_docs_prefer_doppel_surfaces_and_keep_gateway_literals():
    en = EN_TOOL_GATEWAY_DOC.read_text(encoding="utf-8")
    zh = ZH_TOOL_GATEWAY_DOC.read_text(encoding="utf-8")

    assert "routes Doppel Agent's tool calls" in en
    assert "let Doppel Agent default to FLUX 2 Klein" in en
    assert "doppel setup --portal" in en
    assert "doppel model" in en
    assert "doppel portal status" in en
    assert "doppel portal tools" in en
    assert "doppel status" in en
    assert "doppel tools" in en
    assert "doppel setup terminal" in en
    assert "~/.doppel/.env" in en
    assert "Legacy installs may still keep these overrides in `~/.hermes/.env`." in en
    assert "Doppel Agent shows a clear error pointing at the portal." in en

    assert "运行 `doppel model` 并选择 Nous Portal 作为提供商时，Doppel Agent 会主动询问是否启用 Tool Gateway：" in zh
    assert "### 通过 `doppel tools`" in zh
    assert "doppel tools" in zh
    assert "doppel status" in zh
    assert "`~/.doppel/config.yaml`" in zh
    assert "`~/.doppel/auth.json`" in zh
    assert "`~/.doppel/.env`" in zh
    assert "legacy 安装仍可能使用 `~/.hermes/auth.json`" in zh
    assert "legacy 安装仍可能将这些覆盖项保留在 `~/.hermes/.env` 中。" in zh
    assert "doppel setup terminal" in zh

    for fixed in (
        "~/.hermes/.env",
        "~/.hermes/auth.json",
        "use_gateway",
        "TOOL_GATEWAY_DOMAIN",
        "TOOL_GATEWAY_SCHEME",
        "TOOL_GATEWAY_USER_TOKEN",
        "FIRECRAWL_GATEWAY_URL",
        "image_generate",
        "text_to_speech",
        "browser_navigate",
    ):
        assert fixed in en or fixed in zh

    assert "hermes setup --portal" not in en
    assert "hermes model" not in en
    assert "hermes portal status" not in en
    assert "hermes portal tools" not in en
    assert "hermes tools" not in en
    assert "hermes setup terminal" not in en
    assert "运行 `hermes model`" not in zh
    assert "### 通过 `hermes tools`" not in zh


def test_subscription_proxy_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_SUBSCRIPTION_PROXY_DOC.read_text(encoding="utf-8")
    zh = ZH_SUBSCRIPTION_PROXY_DOC.read_text(encoding="utf-8")

    assert "use your Doppel-managed provider subscription" in en
    assert "将你的 Doppel 托管提供商订阅用作其 LLM 端点" in zh
    assert '"Use Doppel Agent as a chat backend"' in en
    assert '"将 Doppel Agent 用作聊天后端"' in zh
    assert "doppel auth add nous" in en
    assert "doppel auth add nous" in zh
    assert "doppel proxy start" in en
    assert "doppel proxy start" in zh
    assert "doppel proxy providers" in en
    assert "doppel proxy providers" in zh
    assert "doppel proxy status" in en
    assert "doppel proxy status" in zh
    assert "Starting Doppel proxy for Nous Portal" in en
    assert "Starting Doppel proxy for Nous Portal" in zh
    assert "Doppel proxy upstream adapters" in en
    assert "Doppel proxy upstream adapters" in zh
    assert "~/.doppel/auth.json" in en
    assert "~/.doppel/auth.json" in zh
    assert "~/.hermes/auth.json" in en
    assert "~/.hermes/auth.json" in zh
    assert "Hermes-4-70B" in en
    assert "Hermes-4-70B" in zh
    assert "hermes_cli/proxy/adapters/" in en
    assert "hermes_cli/proxy/adapters/" in zh
    assert "UpstreamAdapter" in en
    assert "UpstreamAdapter" in zh

    assert "use your Hermes-managed provider subscription" not in en
    assert "将你的 Hermes 托管提供商订阅用作其 LLM 端点" not in zh
    assert "hermes auth add nous" not in en
    assert "hermes proxy start" not in en
    assert "Hermes proxy upstream adapters" not in en


def test_tools_feature_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_TOOLS_DOC.read_text(encoding="utf-8")
    zh = ZH_TOOLS_DOC.read_text(encoding="utf-8")

    assert "Overview of Doppel Agent's tools" in en
    assert "Doppel Agent ships with a broad built-in tool registry" in en
    assert "doppel model" in en
    assert "doppel tools" in en
    assert 'doppel chat --toolsets "web,terminal"' in en
    assert "doppel config set terminal.backend singularity" in en
    assert "doppel config set terminal.backend modal" in en
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/.env" in en
    assert "~/.hermes/config.yaml" in en
    assert "~/.hermes/.env" in en

    assert "Doppel Agent 工具概览" in zh
    assert "Doppel Agent 内置了丰富的工具注册表" in zh
    assert "doppel model" in zh
    assert "doppel tools" in zh
    assert 'doppel chat --toolsets "web,terminal"' in zh
    assert "doppel config set terminal.backend singularity" in zh
    assert "doppel config set terminal.backend modal" in zh
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/.env" in zh
    assert "~/.hermes/config.yaml" in zh
    assert "~/.hermes/.env" in zh

    for fixed in (
        "hermes-cli",
        "hermes-telegram",
        "XAI_API_KEY",
        "TERMINAL_SSH_HOST",
        "TERMINAL_SSH_USER",
        "TERMINAL_SSH_KEY",
        "SUDO_PASSWORD",
        "container_persistent",
    ):
        assert fixed in en
        assert fixed in zh

    assert "Overview of Hermes Agent's tools" not in en
    assert "Hermes ships with a broad built-in tool registry" not in en
    assert 'hermes chat --toolsets "web,terminal"' not in en
    assert "hermes tools" not in en
    assert "hermes model" not in en
    assert "Hermes Agent 工具概览" not in zh
    assert "Hermes 内置了丰富的工具注册表" not in zh
    assert 'hermes chat --toolsets "web,terminal"' not in zh
    assert "hermes tools" not in zh
    assert "hermes model" not in zh


def test_fallback_provider_docs_prefer_doppel_surfaces_and_keep_legacy_literals():
    en = EN_FALLBACK_PROVIDERS_DOC.read_text(encoding="utf-8")
    zh = ZH_FALLBACK_PROVIDERS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent has three layers of resilience" in en
    assert "Doppel Agent 具备三层弹性机制" in zh
    assert "doppel fallback" in en
    assert "doppel fallback" in zh
    assert "doppel model" in en
    assert "doppel model" in zh
    assert "doppel auth add nous" in en
    assert "doppel auth add nous" in zh
    assert "doppel setup --portal" in en
    assert "doppel setup --portal" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.hermes/config.yaml" in en
    assert "~/.hermes/config.yaml" in zh
    assert "fallback_providers" in en
    assert "fallback_providers" in zh
    assert "fallback_model" in en
    assert "fallback_model" in zh

    for fixed in ("HERMES_GEMINI_PROJECT_ID", "HERMES_QWEN_BASE_URL", "Auxiliary <task>"):
        assert fixed in en
        assert fixed in zh

    assert "Hermes Agent has three layers of resilience" not in en
    assert "Hermes Agent 具备三层弹性机制" not in zh
    assert "hermes fallback" not in en
    assert "hermes setup --portal" not in en
    assert "hermes auth add nous" not in en
    assert "hermes model" not in en
    assert "hermes fallback" not in zh
    assert "hermes setup --portal" not in zh
    assert "hermes auth add nous" not in zh
    assert "hermes model" not in zh


def test_credential_pool_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_CREDENTIAL_POOLS_DOC.read_text(encoding="utf-8")
    zh = ZH_CREDENTIAL_POOLS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent automatically rotates" in en
    assert "Doppel Agent 会自动轮换到下一个健康密钥" in zh
    assert "doppel auth add openrouter --api-key" in en
    assert "doppel auth add openrouter --api-key" in zh
    assert "doppel auth list" in en
    assert "doppel auth list" in zh
    assert "doppel auth" in en
    assert "doppel auth" in zh
    assert "doppel model" in en
    assert "doppel model" in zh
    assert "~/.doppel/auth.json" in en
    assert "~/.doppel/auth.json" in zh
    assert "~/.hermes/auth.json" in en
    assert "~/.hermes/auth.json" in zh
    assert "fallback_providers" in en
    assert "fallback_providers" in zh
    assert "Doppel PKCE OAuth" in en
    assert "Doppel PKCE OAuth" in zh

    for fixed in ("hermes_pkce", "OPENROUTER_API_KEY", "ANTHROPIC_API_KEY", "credential_pool"):
        assert fixed in en
        assert fixed in zh

    assert "Hermes automatically rotates" not in en
    assert "Hermes 会自动轮换到下一个健康密钥" not in zh
    assert "hermes auth add openrouter" not in en
    assert "hermes auth list" not in en
    assert "hermes model" not in en
    assert "hermes auth add openrouter" not in zh
    assert "hermes auth list" not in zh
    assert "hermes model" not in zh


def test_cron_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_CRON_DOC.read_text(encoding="utf-8")
    zh = ZH_CRON_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent exposes cron management" in en
    assert "Doppel Agent 通过单一 `cronjob` 工具暴露 cron 管理能力" in zh
    assert "doppel model" in en
    assert "doppel model" in zh
    assert "doppel setup --portal" in en
    assert "doppel setup --portal" in zh
    assert "doppel cron create" in en
    assert "doppel cron create" in zh
    assert "doppel cron list" in en
    assert "doppel cron list" in zh
    assert "doppel gateway install" in en
    assert "doppel gateway install" in zh
    assert "doppel tools" in en
    assert "doppel tools" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/cron/jobs.json" in en
    assert "~/.doppel/cron/jobs.json" in zh
    assert "~/.doppel/scripts/" in en
    assert "~/.doppel/scripts/" in zh
    assert "~/.hermes/cron/" in en
    assert "~/.hermes/cron/" in zh
    assert "~/.hermes/state.db" in en
    assert "~/.hermes/state.db" in zh

    for fixed in ("HERMES_HOME", "HERMES_CRON_SCRIPT_TIMEOUT", "cronjob", "wakeAgent"):
        assert fixed in en
        assert fixed in zh

    assert "Hermes exposes cron management" not in en
    assert "Hermes 通过单一 `cronjob` 工具暴露 cron 管理能力" not in zh
    assert "hermes cron" not in en
    assert "hermes cron" not in zh
    assert "hermes gateway install" not in en
    assert "hermes gateway install" not in zh
    assert "hermes setup --portal" not in en
    assert "hermes setup --portal" not in zh
    assert "hermes tools" not in en
    assert "hermes tools" not in zh


def test_browser_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_BROWSER_DOC.read_text(encoding="utf-8")
    zh = ZH_BROWSER_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent includes a full browser automation toolset" in en
    assert "Doppel Agent 内置完整的浏览器自动化工具集" in zh
    assert "doppel setup --portal" in en
    assert "doppel setup --portal" in zh
    assert "doppel setup tools" in en
    assert "doppel setup tools" in zh
    assert "doppel model" in en
    assert "doppel model" in zh
    assert "doppel tools" in en
    assert "doppel tools" in zh
    assert "doppel chat" in en
    assert "doppel chat" in zh
    assert "doppel config set toolsets '[\"hermes-cli\", \"browser\"]'" in en
    assert "doppel config set toolsets '[\"hermes-cli\", \"browser\"]'" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/browser_auth/camofox/" in en
    assert "~/.doppel/browser_auth/camofox/" in zh
    assert "~/.doppel/browser_recordings/" in en
    assert "~/.doppel/browser_recordings/" in zh
    assert "~/.doppel/cache/screenshots/" in en
    assert "~/.doppel/cache/screenshots/" in zh
    assert "$HOME/.doppel/chrome-debug" in en
    assert "$HOME/.doppel/chrome-debug" in zh
    assert "Use MCP with Doppel Agent" in en
    assert "在 Doppel Agent 中使用 MCP" in zh

    for fixed in (
        "HERMES_HOME",
        "CAMOFOX_USER_ID",
        "CAMOFOX_SESSION_KEY",
        "CAMOFOX_ADOPT_EXISTING_TAB",
        "CAMOFOX_URL",
        "/browser connect",
        "browser_navigate",
        "browser_snapshot",
        "browser_click",
        "browser_type",
        "browser_cdp",
        "browser_dialog",
        "GET /tabs?userId=<user_id>",
        "DELETE /sessions/<user_id>",
        "REQUEST_RELEASE",
        "MEDIA:",
        "~/.hermes/browser_auth/camofox/",
        "~/.hermes/browser_recordings/",
        "~/.hermes/cache/screenshots/",
        "hermes-cli",
    ):
        assert fixed in en
        assert fixed in zh

    assert "Hermes Agent includes a full browser automation toolset" not in en
    assert "Hermes Agent 内置完整的浏览器自动化工具集" not in zh
    assert "hermes setup --portal" not in en
    assert "hermes setup --portal" not in zh
    assert "hermes setup tools" not in en
    assert "hermes setup tools" not in zh
    assert "hermes model" not in en
    assert "hermes model" not in zh
    assert "hermes tools" not in en
    assert "hermes tools" not in zh
    assert "hermes chat" not in en
    assert "hermes chat" not in zh
    assert "hermes config set toolsets" not in en
    assert "hermes config set toolsets" not in zh
    assert 'Type "hermes agent" into the search field @e3' not in en
    assert 'Type "hermes agent" into the search field @e3' not in zh


def test_hooks_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_HOOKS_DOC.read_text(encoding="utf-8")
    zh = ZH_HOOKS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent has three hook systems" in en
    assert "Doppel Agent 有三套 hook 系统" in zh
    assert "~/.doppel/hooks/" in en
    assert "~/.doppel/hooks/" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/BOOT.md" in en
    assert "~/.doppel/BOOT.md" in zh
    assert "doppel cron list" in en
    assert "doppel cron list" in zh
    assert "doppel gateway restart" in en
    assert "doppel gateway restart" in zh
    assert "doppel logs --follow --level INFO | grep boot-md" in en
    assert "doppel logs --follow --level INFO | grep boot-md" in zh
    assert "doppel --accept-hooks chat" in en
    assert "doppel --accept-hooks chat" in zh
    assert "doppel hooks list" in en
    assert "doppel hooks list" in zh
    assert "doppel hooks doctor" in en
    assert "doppel hooks doctor" in zh
    assert "Doppel Agent needs approval" in en
    assert "Doppel Agent needs approval" in zh
    assert "~/.hermes" in en
    assert "~/.hermes" in zh

    for fixed in (
        "HERMES_ACCEPT_HOOKS",
        "HookRegistry.discover_and_load()",
        "hooks.emit()",
        "agent.shell_hooks.register_from_config(cfg)",
        "run_agent.py",
        "gateway/run.py",
        "AIAgent",
        "pre_tool_call",
        "command:*",
    ):
        assert fixed in en
        assert fixed in zh

    assert "Hermes has three hook systems" not in en
    assert "Hermes 有三套 hook 系统" not in zh
    assert "Hermes needs approval" not in en
    assert "Hermes needs approval" not in zh
    assert "Hermes does not ship a built-in BOOT.md hook" not in en
    assert "Hermes 不内置 BOOT.md hook" not in zh
    assert "hermes cron list" not in en
    assert "hermes cron list" not in zh
    assert "hermes gateway restart" not in en
    assert "hermes gateway restart" not in zh
    assert "hermes logs --follow --level INFO | grep boot-md" not in en
    assert "hermes logs --follow --level INFO | grep boot-md" not in zh
    assert "hermes hooks list" not in en
    assert "hermes hooks list" not in zh


def test_codex_runtime_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_CODEX_RUNTIME_DOC.read_text(encoding="utf-8")
    zh = ZH_CODEX_RUNTIME_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent can optionally hand" in en
    assert "Doppel Agent 可以选择将" in zh
    assert "Default Doppel Agent behavior is unchanged" in en
    assert "否则 Doppel Agent 的默认行为不变" in zh
    assert "doppel setup --portal" in en
    assert "doppel auth login codex" in en
    assert "doppel auth login codex" in zh
    assert "doppel logs --since 5m" in en
    assert "doppel logs --since 5m" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/auth.json" in en
    assert "~/.doppel/auth.json" in zh
    assert "Doppel Agent shell" in en
    assert "Doppel Agent shell" in zh

    assert "Nous Portal" in en

    for fixed in (
        "HERMES_KANBAN_TASK",
        "HERMES_KANBAN_WORKSPACES_ROOT",
        "HERMES_HOME",
        "~/.hermes/config.yaml",
        "~/.hermes/auth.json",
        "hermes_tools_mcp_server",
        "hermes-tools",
        "# managed by hermes-agent",
        "model_tools.handle_function_call()",
        "_import_codex_cli_tokens",
        "https://github.com/NousResearch/hermes-agent/issues",
        "https://github.com/NousResearch/hermes-agent/pull/24182",
    ):
        assert fixed in en
        assert fixed in zh

    assert "hermes setup --portal" not in en
    assert "hermes auth login codex" not in en
    assert "hermes auth login codex" not in zh
    assert "hermes logs --since 5m" not in en
    assert "hermes logs --since 5m" not in zh
    assert "Hermes Agent 2026.5" not in en
    assert "Hermes Agent 2026.5" not in zh


def test_mcp_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_MCP_DOC.read_text(encoding="utf-8")
    zh = ZH_MCP_DOC.read_text(encoding="utf-8")

    assert "Connect Doppel Agent to external tool servers via MCP" in en
    assert "通过 MCP 将 Doppel Agent 连接到外部工具服务器" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/doppel-agent" in en
    assert "~/.doppel/doppel-agent" in zh
    assert "doppel chat" in en
    assert "doppel chat" in zh
    assert "doppel mcp add codex --preset codex" in en
    assert "doppel mcp add codex --preset codex" in zh
    assert "doppel mcp serve" in en
    assert "doppel mcp serve" in zh
    assert "Use MCP with Doppel" in en
    assert "在 Doppel 中使用 MCP" in zh

    for fixed in (
        "~/.hermes/config.yaml",
        "mcp_servers",
        "notifications/tools/list_changed",
        "sampling/createMessage",
        "codex mcp-server",
    ):
        assert fixed in en
        assert fixed in zh

    assert "Connect Hermes Agent to external tool servers via MCP" not in en
    assert "MCP lets Hermes Agent connect to external tool servers" not in en
    assert "hermes chat" not in en
    assert "hermes chat" not in zh
    assert "hermes mcp add" not in en
    assert "hermes mcp add" not in zh
    assert "hermes mcp serve" not in en
    assert "hermes mcp serve" not in zh
    assert "Use MCP with Hermes" not in en
    assert "在 Hermes 中使用 MCP" not in zh


def test_kanban_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_KANBAN_DOC.read_text(encoding="utf-8")
    zh = ZH_KANBAN_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent Kanban is a durable task board" in en
    assert "Doppel Agent Kanban 是一个持久化任务看板" in zh
    assert "multiple Doppel Agent profiles" in en
    assert "多个 Doppel Agent 配置文件" in zh
    assert "~/.doppel/kanban.db" in en
    assert "~/.doppel/kanban.db" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "doppel kanban create" in en
    assert "doppel kanban create" in zh
    assert "doppel gateway start" in en
    assert "doppel gateway start" in zh
    assert "doppel dashboard" in en
    assert "doppel dashboard" in zh
    assert "doppel chat" in en
    assert "doppel chat" in zh
    assert "doppel profile describe" in en
    assert "doppel profile describe" in zh
    assert "doppel skills list" in en
    assert "doppel skills list" in zh

    for fixed in (
        "~/.hermes",
        "docs/hermes-kanban-v1-spec.pdf",
        "HERMES_KANBAN_BOARD",
        "HERMES_KANBAN_TASK",
        "HERMES_KANBAN_WORKSPACE",
        "HERMES_TENANT",
        "kanban_db",
        "hermes_cli.kanban.run_slash()",
    ):
        assert fixed in en
        assert fixed in zh

    assert "HERMES_KANBAN_ATTACHMENTS_ROOT" in en

    assert "multiple Hermes profiles" not in en
    assert "多个 Hermes 配置文件" not in zh
    assert "all your Hermes profiles" not in en
    assert "所有 Hermes 配置文件" not in zh
    assert "hermes kanban create" not in en
    assert "hermes kanban create" not in zh
    assert "hermes gateway start" not in en
    assert "hermes gateway start" not in zh
    assert "hermes dashboard" not in en
    assert "hermes dashboard" not in zh
    assert "hermes chat" not in en
    assert "hermes chat" not in zh
    assert "hermes profile describe" not in en
    assert "hermes profile describe" not in zh
    assert "hermes skills list" not in en
    assert "hermes skills list" not in zh
