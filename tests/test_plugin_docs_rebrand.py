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
EN_ADDING_TOOLS_DOC = EN_DEV_GUIDE_DIR / "adding-tools.md"
EN_CONTRIBUTING_DOC = EN_DEV_GUIDE_DIR / "contributing.md"
EN_GATEWAY_INTERNALS_DOC = EN_DEV_GUIDE_DIR / "gateway-internals.md"
EN_CONTEXT_COMPRESSION_DOC = EN_DEV_GUIDE_DIR / "context-compression-and-caching.md"
EN_ADDING_PLATFORM_ADAPTERS_DOC = EN_DEV_GUIDE_DIR / "adding-platform-adapters.md"
EN_CREATING_SKILLS_DOC = EN_DEV_GUIDE_DIR / "creating-skills.md"
ZH_ADDING_PROVIDERS_DOC = ZH_DEV_GUIDE_DIR / "adding-providers.md"
ZH_PROVIDER_RUNTIME_DOC = ZH_DEV_GUIDE_DIR / "provider-runtime.md"
ZH_ADDING_TOOLS_DOC = ZH_DEV_GUIDE_DIR / "adding-tools.md"
ZH_CONTRIBUTING_DOC = ZH_DEV_GUIDE_DIR / "contributing.md"
ZH_GATEWAY_INTERNALS_DOC = ZH_DEV_GUIDE_DIR / "gateway-internals.md"
ZH_CONTEXT_COMPRESSION_DOC = ZH_DEV_GUIDE_DIR / "context-compression-and-caching.md"
ZH_ADDING_PLATFORM_ADAPTERS_DOC = ZH_DEV_GUIDE_DIR / "adding-platform-adapters.md"
ZH_CREATING_SKILLS_DOC = ZH_DEV_GUIDE_DIR / "creating-skills.md"


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
