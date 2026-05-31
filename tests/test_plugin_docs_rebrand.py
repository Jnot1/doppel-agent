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
EN_INTEGRATIONS_PROVIDERS_DOC = REPO_ROOT / "website" / "docs" / "integrations" / "providers.md"
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
ZH_INTEGRATIONS_PROVIDERS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "integrations"
    / "providers.md"
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
EN_SECURITY_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "security.md"
EN_ENVIRONMENT_VARIABLES_DOC = (
    REPO_ROOT / "website" / "docs" / "reference" / "environment-variables.md"
)
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
EN_TOOLS_REFERENCE_DOC = (
    REPO_ROOT / "website" / "docs" / "reference" / "tools-reference.md"
)
EN_FALLBACK_PROVIDERS_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "fallback-providers.md"
)
EN_CREDENTIAL_POOLS_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "credential-pools.md"
)
EN_CURATOR_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "curator.md"
EN_CRON_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "cron.md"
EN_BROWSER_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "browser.md"
EN_CODEX_RUNTIME_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "codex-app-server-runtime.md"
)
EN_MCP_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "mcp.md"
EN_KANBAN_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "kanban.md"
EN_FEATURE_SKILLS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "skills.md"
EN_FEATURE_ACP_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "acp.md"
EN_TTS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "tts.md"
EN_SPOTIFY_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "spotify.md"
EN_WEB_SEARCH_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "web-search.md"
EN_VOICE_MODE_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "voice-mode.md"
EN_HONCHO_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "honcho.md"
EN_MEMORY_PROVIDERS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "memory-providers.md"
EN_LSP_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "lsp.md"
EN_CODE_EXECUTION_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "code-execution.md"
EN_KANBAN_WORKER_LANES_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "kanban-worker-lanes.md"
EN_COMPUTER_USE_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "computer-use.md"
EN_EXTENDING_DASHBOARD_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "extending-the-dashboard.md"
)
EN_WEB_DASHBOARD_DOC = (
    REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "web-dashboard.md"
)
EN_SKINS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "skins.md"
EN_HOOKS_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "hooks.md"
EN_USE_SOUL_DOC = REPO_ROOT / "website" / "docs" / "guides" / "use-soul-with-hermes.md"
EN_LOCAL_OLLAMA_GUIDE = REPO_ROOT / "website" / "docs" / "guides" / "local-ollama-setup.md"
EN_CONFIGURATION_DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "configuration.md"
EN_MICROSOFT_GRAPH_APP_REG_DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "guides"
    / "microsoft-graph-app-registration.md"
)
EN_MCP_CONFIG_REFERENCE_DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "reference"
    / "mcp-config-reference.md"
)
EN_REFERENCE_FAQ_DOC = REPO_ROOT / "website" / "docs" / "reference" / "faq.md"
EN_REFERENCE_SLASH_COMMANDS_DOC = (
    REPO_ROOT / "website" / "docs" / "reference" / "slash-commands.md"
)
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
ZH_SECURITY_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "security.md"
)
ZH_REFERENCE_FAQ_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "reference"
    / "faq.md"
)
ZH_REFERENCE_SLASH_COMMANDS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "reference"
    / "slash-commands.md"
)
ZH_ENVIRONMENT_VARIABLES_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "reference"
    / "environment-variables.md"
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
ZH_TOOLS_REFERENCE_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "reference"
    / "tools-reference.md"
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
ZH_CURATOR_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "curator.md"
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
ZH_FEATURE_SKILLS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "skills.md"
)
ZH_FEATURE_ACP_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "acp.md"
)
ZH_TTS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "tts.md"
)
ZH_SPOTIFY_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "spotify.md"
)
ZH_WEB_SEARCH_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "web-search.md"
)
ZH_VOICE_MODE_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "voice-mode.md"
)
ZH_HONCHO_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "honcho.md"
)
ZH_MEMORY_PROVIDERS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "memory-providers.md"
)
ZH_LSP_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "lsp.md"
)
ZH_CODE_EXECUTION_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "code-execution.md"
)
ZH_KANBAN_WORKER_LANES_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "kanban-worker-lanes.md"
)
ZH_COMPUTER_USE_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "computer-use.md"
)
ZH_EXTENDING_DASHBOARD_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "extending-the-dashboard.md"
)
ZH_WEB_DASHBOARD_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "web-dashboard.md"
)
ZH_SKINS_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "features"
    / "skins.md"
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
ZH_LOCAL_OLLAMA_GUIDE = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "guides"
    / "local-ollama-setup.md"
)
ZH_CONFIGURATION_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "configuration.md"
)
ZH_MICROSOFT_GRAPH_APP_REG_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "guides"
    / "microsoft-graph-app-registration.md"
)
ZH_MCP_CONFIG_REFERENCE_DOC = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "reference"
    / "mcp-config-reference.md"
)


def _extract_configuration_top_cluster(text: str, heading: str) -> str:
    start = text.index(heading)
    end_markers = (
        "### SSH Backend",
        "### SSH 后端",
        "### Modal 后端",
        "### Modal Backend",
    )
    for marker in end_markers:
        end = text.find(marker, start)
        if end != -1:
            return text[start:end]
    return text[start:]


def _extract_configuration_backend_cluster(
    text: str, start_heading: str, end_heading: str
) -> str:
    start = text.index(start_heading)
    end = text.index(end_heading, start)
    return text[start:end]


def _extract_configuration_middle_cluster(
    text: str, start_heading: str, end_heading: str
) -> str:
    start = text.index(start_heading)
    end = text.index(end_heading, start)
    return text[start:end]


def _extract_configuration_display_to_working_directory_cluster(
    text: str,
    start_heading: str,
    working_heading: str,
) -> str:
    start = text.index(start_heading)
    working_start = text.index(working_heading, start)
    end = text.find("\n## ", working_start + 1)
    if end == -1:
        end = len(text)
    return text[start:end]


def _assert_prefer_doppel_terminology(
    text: str,
    doppel_phrase: str,
    hermes_phrase: str,
) -> None:
    if doppel_phrase in text:
        assert hermes_phrase not in text


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


def test_local_ollama_guides_prefer_doppel_branding_and_keep_runtime_literals():
    en = EN_LOCAL_OLLAMA_GUIDE.read_text(encoding="utf-8")
    zh = ZH_LOCAL_OLLAMA_GUIDE.read_text(encoding="utf-8")

    en_title = next(line for line in en.splitlines() if line.startswith("title:"))
    zh_title = next(line for line in zh.splitlines() if line.startswith("title:"))
    en_h1 = next(line for line in en.splitlines() if line.startswith("# "))
    zh_h1 = next(line for line in zh.splitlines() if line.startswith("# "))

    assert "Doppel" in en_title and "Hermes" not in en_title
    assert "Doppel" in zh_title and "Hermes" not in zh_title
    assert "Doppel" in en_h1
    assert "Doppel" in zh_h1

    assert "Run Doppel Agent Locally with Ollama" in en
    assert "使用 Ollama 在本地运行 Doppel Agent" in zh
    assert "Doppel Agent connected to Ollama as a custom endpoint" in en
    assert "Doppel Agent 通过自定义端点连接到 Ollama" in zh
    assert "Doppel Agent works exactly like it does with OpenRouter or Anthropic" in en
    assert "Doppel Agent 的使用体验与 OpenRouter 或 Anthropic 完全一致" in zh
    assert "Doppel Agent is an **agentic** assistant" in en
    assert "Doppel Agent 是一个**agentic（智能体）**助手" in zh
    assert "inside Doppel Agent with `/model`" in en
    assert "在 Doppel Agent 中使用 `/model` 切换" in zh
    assert "Run the Doppel setup wizard:" in en
    assert "运行 Doppel 设置向导：" in zh
    assert "`~/.doppel/.env` on fresh installs; legacy `~/.hermes/.env` still works" in en
    assert "默认路径为 `~/.doppel/.env`" in zh
    assert "`~/.doppel/config.yaml` on fresh installs; legacy `~/.hermes/config.yaml` still works" in en
    assert "默认路径为 `~/.doppel/config.yaml`" in zh
    assert "doppel setup" in en
    assert "doppel setup" in zh
    assert "\ndoppel\n```" in en
    assert "\ndoppel\n```" in zh
    assert "doppel gateway" in en
    assert "doppel gateway" in zh
    assert "64,000 tokens" in en
    assert "64,000 token" in zh
    assert "gemma4-64k" in en
    assert "gemma4-64k" in zh
    assert "Doppel Agent has auto-repair" in en
    assert "Doppel Agent 具备自动修复功能" in zh
    assert "Doppel Agent falls back to a cloud provider" in en
    assert "Doppel Agent 将回退到云端提供商" in zh
    assert "Doppel Agent wraps the command, runs it, and reads output" in en
    assert "Doppel Agent 封装命令、执行并读取输出" in zh
    assert "below Doppel Agent's 64K minimum" in en
    assert "低于 Doppel Agent 所需的 64K 最低值" in zh

    assert "Run Hermes Locally with Ollama" not in en
    assert "使用 Ollama 在本地运行 Hermes" not in zh
    assert "Hermes Agent entirely on your own machine" not in en
    assert "在本机完整运行 Hermes Agent" not in zh
    assert "Hermes connected to Ollama as a custom endpoint" not in en
    assert "Hermes 通过自定义端点连接到 Ollama" not in zh
    assert "Hermes is an **agentic** assistant" not in en
    assert "Hermes 是一个**agentic（智能体）**助手" not in zh
    assert "inside Hermes with `/model`" not in en
    assert "在 Hermes 中使用 `/model` 切换" not in zh
    assert "hermes setup" not in en
    assert "hermes setup" not in zh
    assert "hermes gateway" not in en
    assert "hermes gateway" not in zh
    assert "Hermes has auto-repair" not in en
    assert "Hermes 具备自动修复功能" not in zh
    assert "Hermes falls back to a cloud provider" not in en
    assert "Hermes 将回退到云端提供商" not in zh
    assert "Hermes wraps the command, runs it, reads output" not in en
    assert "Hermes 封装命令、执行并读取输出" not in zh
    assert "below Hermes' 64K minimum" not in en
    assert "16384" not in zh
    assert "gemma4-16k" not in zh

    for literal in (
        "DOPPEL_API_TIMEOUT",
        "~/.hermes/.env",
        "~/.hermes/config.yaml",
        "ollama",
        "http://localhost:11434/v1",
        "gemma4:31b",
        "gemma2:27b",
        "gemma2:9b",
        "llama3.2:3b",
        "OLLAMA_KEEP_ALIVE",
        "openrouter",
        "anthropic/claude-sonnet-4",
    ):
        assert literal in en
        assert literal in zh


def test_microsoft_graph_app_registration_guides_prefer_doppel_branding_and_keep_runtime_literals():
    en = EN_MICROSOFT_GRAPH_APP_REG_DOC.read_text(encoding="utf-8")
    zh = ZH_MICROSOFT_GRAPH_APP_REG_DOC.read_text(encoding="utf-8")

    assert "Doppel Teams Meeting Pipeline" in en
    assert "Doppel Teams Meeting Pipeline" in zh
    assert "doppel-graph-secret" in en
    assert "doppel-graph-secret" in zh
    assert "# Create a policy scoped to the Doppel app" in en
    assert "# Create a policy scoped to the Doppel app" in zh
    assert 'Identity "Doppel-Meeting-Pipeline-Policy"' in en
    assert 'Identity "Doppel-Meeting-Pipeline-Policy"' in zh
    assert "Restrict Doppel meeting pipeline to allow-listed users" in en
    assert "Restrict Doppel meeting pipeline to allow-listed users" in zh
    assert "Doppel Agent ships a Graph auth smoke-test. From your Doppel Agent install:" in en
    assert "Doppel Agent 内置了 Graph 身份验证冒烟测试" in zh
    assert "`~/.doppel/.env` on fresh installs; legacy `~/.hermes/.env` still works" in en
    assert "默认路径为 `~/.doppel/.env`" in zh
    assert "chmod 600 ~/.doppel/.env" in en
    assert "chmod 600 ~/.doppel/.env" in zh
    assert "doppel gateway restart" in en
    assert "doppel gateway restart" in zh

    assert "Hermes Teams Meeting Pipeline" not in en
    assert "Hermes Teams Meeting Pipeline" not in zh
    assert "hermes-graph-secret" not in en
    assert "hermes-graph-secret" not in zh
    assert "# Create a policy scoped to the Hermes app" not in en
    assert "# Create a policy scoped to the Hermes app" not in zh
    assert 'Identity "Hermes-Meeting-Pipeline-Policy"' not in en
    assert 'Identity "Hermes-Meeting-Pipeline-Policy"' not in zh
    assert "Hermes ships a Graph auth smoke-test. From your Hermes install:" not in en
    assert "Hermes 内置了 Graph 身份验证冒烟测试" not in zh
    assert "hermes gateway restart" not in en
    assert "hermes gateway restart" not in zh

    for fixed in (
        "MSGRAPH_CLIENT_ID",
        "MSGRAPH_CLIENT_SECRET",
        "MSGRAPH_TENANT_ID",
        "platforms.teams.extra.delivery_mode",
        "incoming_webhook",
        "MicrosoftGraphTokenProvider",
        "MicrosoftGraphTokenError",
        "~/.hermes/.env",
    ):
        assert fixed in en
        assert fixed in zh


def test_configuration_top_cluster_prefer_doppel_customer_facing_and_keep_runtime_literals():
    en = EN_CONFIGURATION_DOC.read_text(encoding="utf-8")
    zh = ZH_CONFIGURATION_DOC.read_text(encoding="utf-8")

    en_cluster = _extract_configuration_top_cluster(en, "# Configuration")
    zh_cluster = _extract_configuration_top_cluster(zh, "# 配置")

    assert "doppel setup --portal" in en_cluster
    assert "doppel setup --portal" in zh_cluster
    assert "doppel config" in en_cluster
    assert "doppel config" in zh_cluster
    assert "doppel config set" in en_cluster
    assert "doppel config set" in zh_cluster
    assert "hermes config set" not in en_cluster
    assert "hermes config set" not in zh_cluster
    assert "`~/.doppel/config.yaml`" in en_cluster
    assert "`~/.doppel/config.yaml`" in zh_cluster
    assert "~/.hermes/" in en_cluster
    assert "~/.hermes/" in zh_cluster

    assert "`doppel chat --model anthropic/claude-sonnet-4`" in en_cluster
    assert "`doppel chat --model anthropic/claude-sonnet-4`" in zh_cluster
    assert "hermes chat --model anthropic/claude-sonnet-4" not in en_cluster
    assert "hermes chat --model anthropic/claude-sonnet-4" not in zh_cluster

    assert "supports six terminal backends" in en_cluster
    assert "Doppel" in en_cluster
    assert "六种终端后端" in zh_cluster
    assert "Doppel" in zh_cluster
    assert "Hermes supports six terminal backends." not in en_cluster
    assert "Hermes 支持六种终端后端" not in zh_cluster
    assert "doppel tools" in en_cluster
    assert "doppel tools" in zh_cluster

    assert "providers.<id>.request_timeout_seconds" in en_cluster
    assert "providers.<id>.request_timeout_seconds" in zh_cluster
    assert "DOPPEL_API_TIMEOUT" in en_cluster
    assert "DOPPEL_API_TIMEOUT" in zh_cluster
    assert "DOPPEL_API_CALL_STALE_TIMEOUT" in en_cluster
    assert "DOPPEL_API_CALL_STALE_TIMEOUT" in zh_cluster
    assert "DOPPEL_DOCKER_BINARY" in en_cluster
    assert "DOPPEL_DOCKER_BINARY" in zh_cluster
    assert "~/.hermes/.env" in en_cluster
    assert "~/.hermes/.env" in zh_cluster
    assert "~/.hermes/config.yaml" in en_cluster
    assert "~/.hermes/config.yaml" in zh_cluster
    assert "~/.doppel/.env" in en_cluster
    assert "~/.doppel/.env" in zh_cluster
    assert "~/.doppel/" in en_cluster
    assert "~/.doppel/" in zh_cluster


def test_configuration_terminal_backend_cluster_prefer_doppel_and_preserve_runtime_terms():
    en = EN_CONFIGURATION_DOC.read_text(encoding="utf-8")
    zh = ZH_CONFIGURATION_DOC.read_text(encoding="utf-8")

    en_cluster = _extract_configuration_backend_cluster(
        en, "### SSH Backend", "### Remote-to-Host File Sync on Teardown"
    )
    zh_cluster = _extract_configuration_backend_cluster(
        zh, "### SSH 后端", "### 拆卸时远程到宿主文件同步"
    )

    assert "### Common Terminal Backend Issues" in en_cluster
    assert "### 常见终端后端问题" in zh_cluster
    assert "### Remote-to-Host File Sync on Teardown" not in en_cluster
    assert "### 拆卸时远程到宿主文件同步" not in zh_cluster
    assert "Doppel Agent logs a clear error" in en_cluster
    assert "Doppel Agent 会记录清晰的错误" in zh_cluster
    assert "Run `doppel doctor` to check." in en_cluster
    assert "运行 `doppel doctor` 检查。" in zh_cluster
    assert "Run `hermes doctor` to check." not in en_cluster
    assert "运行 `hermes doctor`" not in zh_cluster
    assert "hermes doctor" not in en_cluster
    assert "`hermes doctor`" not in zh_cluster
    assert "doppel doctor" in en_cluster
    assert "doppel doctor" in zh_cluster
    assert "doppel config set terminal.backend local" in en_cluster
    assert "doppel config set terminal.backend local" in zh_cluster
    assert "`~/.doppel/modal_snapshots.json`" in en_cluster
    assert "`~/.doppel/modal_snapshots.json`" in zh_cluster
    assert "`~/.doppel/`" in en_cluster
    assert "`~/.doppel/`" in zh_cluster
    assert "Hermes logs a clear error" not in en_cluster
    assert "Hermes 会记录清晰的错误" not in zh_cluster

    for literal in (
        "TERMINAL_SSH_HOST",
        "TERMINAL_SSH_USER",
        "hermes-{task_id}",
        "/scratch/$USER/hermes-agent",
        "~/.hermes/sandboxes/singularity",
        "BatchMode=yes",
        "StrictHostKeyChecking=accept-new",
        "bash -l",
    ):
        assert literal in en_cluster
        assert literal in zh_cluster

    assert "~/.hermes/modal_snapshots.json" in zh_cluster


def test_configuration_remote_sync_and_persistent_shell_cluster_prefer_doppel_and_keep_runtime_terms():
    en = EN_CONFIGURATION_DOC.read_text(encoding="utf-8")
    zh = ZH_CONFIGURATION_DOC.read_text(encoding="utf-8")

    en_cluster = _extract_configuration_backend_cluster(
        en, "### Remote-to-Host File Sync on Teardown", "## Skill Settings"
    )
    zh_cluster = _extract_configuration_backend_cluster(
        zh, "### 拆卸时远程到宿主文件同步", "## 技能设置"
    )

    assert "Doppel Agent syncs a tracked set of agent-home inputs" in en_cluster
    assert "Doppel Agent 会先把一组受跟踪的 agent-home 输入同步到远程" in zh_cluster
    assert "remote `.hermes/` tree" in en_cluster
    assert "远程 `.hermes/` 树" in zh_cluster
    assert "`~/.doppel/` on fresh installs" in en_cluster
    assert "`~/.doppel/`" in zh_cluster
    assert "matching host paths in your agent home" in en_cluster
    assert "同步回宿主上对应的路径" in zh_cluster
    assert "does **not** create a per-session agent-worktree snapshot directory" in en_cluster
    assert "不会**创建按会话目录划分的 agent 工作树快照" in zh_cluster
    assert "/home/user/.doppel/cache/documents:/output" in en_cluster
    assert "/home/user/.doppel/cache/documents:/output" in zh_cluster
    assert "MEDIA:/home/user/.doppel/cache/documents/report.txt" in en_cluster
    assert "MEDIA:/home/user/.doppel/cache/documents/report.txt" in zh_cluster
    assert "Doppel resolves each listed variable" in en_cluster
    assert "Doppel Agent 首先从您当前的 shell 解析每个列出的变量" in zh_cluster
    assert "Doppel Agent appends `--user $(id -u):$(id -g)`" in en_cluster
    assert "Doppel Agent 将 `--user $(id -u):$(id -g)` 附加到 `docker run` 命令" in zh_cluster
    assert "Doppel Agent does **not** pass your current host working directory" in en_cluster
    assert "Doppel Agent **不会**将您当前的宿主工作目录传入容器" in zh_cluster
    assert "launch Doppel Agent from `~/projects/my-app`" in en_cluster
    assert "启动 Doppel Agent" in zh_cluster
    assert "directory you launched Doppel Agent from" in en_cluster
    assert "启动 Doppel Agent 的目录" in zh_cluster
    assert "doppel config set terminal.persistent_shell false" in en_cluster
    assert "doppel config set terminal.persistent_shell false" in zh_cluster
    assert "HERMES_FORCE_FILE_SYNC=1" in en_cluster
    assert "HERMES_FORCE_FILE_SYNC=1" in zh_cluster

    assert "/home/user/.hermes/cache/documents:/output" not in en_cluster
    assert "/home/user/.hermes/cache/documents:/output" not in zh_cluster
    assert "Hermes appends `--user $(id -u):$(id -g)`" not in en_cluster
    assert "Hermes 将 `--user $(id -u):$(id -g)`" not in zh_cluster
    assert "launch Hermes from `~/projects/my-app`" not in en_cluster
    assert "启动 Hermes" not in zh_cluster
    assert "hermes config set terminal.persistent_shell false" not in en_cluster
    assert "hermes config set terminal.persistent_shell false" not in zh_cluster
    assert "`~/.doppel/cache/remote-syncs/<session-id>/`" not in en_cluster
    assert "`~/.doppel/cache/remote-syncs/<session-id>/`" not in zh_cluster
    assert "file_sync_max_mb" not in en_cluster
    assert "file_sync_max_mb" not in zh_cluster
    assert "file_sync_enabled" not in en_cluster
    assert "file_sync_enabled" not in zh_cluster

    for literal in (
        "MEDIA:/",
        "TERMINAL_DOCKER_VOLUMES",
        "docker_forward_env",
        "GITHUB_TOKEN",
        "NPM_TOKEN",
        "--user $(id -u):$(id -g)",
        "/workspace",
        "/root",
        "TERMINAL_SSH_PERSISTENT",
        "TERMINAL_LOCAL_PERSISTENT",
        "stdin_data",
        "sudo",
    ):
        assert literal in en_cluster
        assert literal in zh_cluster

    assert "~/.hermes/" in en_cluster
    assert "~/.hermes/" in zh_cluster
    assert "~/.hermes/.env" in zh_cluster


def test_configuration_display_to_working_directory_cluster_prefer_doppel_wording_and_runtime_terms():
    en = EN_CONFIGURATION_DOC.read_text(encoding="utf-8")
    zh = ZH_CONFIGURATION_DOC.read_text(encoding="utf-8")

    en_cluster = _extract_configuration_display_to_working_directory_cluster(
        en,
        "## Display Settings",
        "## Working Directory",
    )
    zh_cluster = _extract_configuration_display_to_working_directory_cluster(
        zh,
        "## 显示设置",
        "## 工作目录",
    )

    assert "## Display Settings" in en_cluster
    assert "## 显示设置" in zh_cluster
    assert "## Working Directory" in en_cluster
    assert "## 工作目录" in zh_cluster
    _assert_prefer_doppel_terminology(
        en_cluster,
        "Doppel Agent appends",
        "Hermes appends",
    )
    _assert_prefer_doppel_terminology(
        en_cluster,
        "Doppel Agent falls back automatically",
        "Hermes falls back automatically",
    )
    _assert_prefer_doppel_terminology(
        en_cluster,
        "Control what Doppel Agent does when an unknown user sends a direct message",
        "Control what Hermes does when an unknown user sends a direct message",
    )
    _assert_prefer_doppel_terminology(
        zh_cluster,
        "控制当未知用户发送私信时 Doppel Agent 的行为",
        "控制当未知用户发送私信时 Hermes 的行为",
    )
    _assert_prefer_doppel_terminology(
        en_cluster,
        "doppel status",
        "hermes status",
    )
    _assert_prefer_doppel_terminology(
        en_cluster,
        "doppel update",
        "hermes update",
    )
    _assert_prefer_doppel_terminology(
        zh_cluster,
        "doppel status",
        "hermes status",
    )
    _assert_prefer_doppel_terminology(
        zh_cluster,
        "doppel update",
        "hermes update",
    )
    assert "HERMES_FILE_MUTATION_VERIFIER" in en_cluster
    assert "HERMES_FILE_MUTATION_VERIFIER" in zh_cluster
    assert "HERMES_LANGUAGE" in en_cluster
    assert "HERMES_LANGUAGE" in zh_cluster
    assert "HERMES_YOLO_MODE" in en_cluster
    assert "HERMES_YOLO_MODE" in zh_cluster
    assert ".hermes.md" in en_cluster
    assert "HERMES.md" in en_cluster
    assert ".hermes.md" in zh_cluster
    assert "HERMES.md" in zh_cluster
    assert "MESSAGING_CWD" in en_cluster
    assert "TERMINAL_CWD" in en_cluster
    assert "MESSAGING_CWD" in zh_cluster
    assert "TERMINAL_CWD" in zh_cluster

    assert "~/.doppel/browser_recordings/" in en_cluster
    assert "~/.doppel/browser_recordings/" in zh_cluster
    assert "~/.doppel/SOUL.md" in en_cluster
    assert "$DOPPEL_HOME/SOUL.md" in en_cluster
    assert "~/.doppel/SOUL.md" in zh_cluster
    assert "$DOPPEL_HOME/SOUL.md" in zh_cluster
    assert "~/.hermes/.env" in en_cluster or "~/.hermes/.env" in zh_cluster
    assert "/etc/doppel/blocked-sites.txt" in en_cluster
    assert "/etc/doppel/blocked-sites.txt" in zh_cluster

    _assert_prefer_doppel_terminology(
        en_cluster,
        "CLI (`doppel`)",
        "CLI (`hermes`)",
    )
    _assert_prefer_doppel_terminology(
        zh_cluster,
        "CLI（`doppel`）",
        "CLI（`hermes`）",
    )
    if "doppel tools" in en_cluster:
        assert "hermes tools" not in en_cluster
    if "doppel tools" in zh_cluster:
        assert "hermes tools" not in zh_cluster


def test_configuration_skill_and_compression_cluster_prefer_doppel_and_keep_runtime_terms():
    en = EN_CONFIGURATION_DOC.read_text(encoding="utf-8")
    zh = ZH_CONFIGURATION_DOC.read_text(encoding="utf-8")

    en_cluster = _extract_configuration_middle_cluster(
        en, "## Skill Settings", "## Context Engine"
    )
    zh_cluster = _extract_configuration_middle_cluster(
        zh, "## 技能设置", "## 上下文引擎"
    )

    assert "doppel config migrate" in en_cluster
    assert "doppel config migrate" in zh_cluster
    assert "doppel config show" in en_cluster
    assert "doppel config show" in zh_cluster
    assert "doppel config set skills.config.myplugin.path ~/myplugin-data" in en_cluster
    assert "doppel config set skills.config.myplugin.path ~/myplugin-data" in zh_cluster
    assert "Doppel Agent can optionally scan" in en_cluster
    assert "Doppel Agent 可以选择扫描" in zh_cluster
    assert "before Doppel Agent truncates it" in en_cluster
    assert "在 Doppel Agent 截断之前" in zh_cluster
    assert "`doppel tools`" in en_cluster
    assert "`doppel tools`" in zh_cluster
    assert "same as doppel -w" in en_cluster
    assert "与 doppel -w 相同" in zh_cluster
    assert "Doppel Agent automatically compresses long conversations" in en_cluster
    assert "Doppel Agent 自动压缩长对话" in zh_cluster
    assert "Doppel Agent forces compression" in en_cluster
    assert "Doppel Agent 会强制压缩" in zh_cluster
    assert "protect_first_n: 3" in en_cluster
    assert "protect_first_n: 3" in zh_cluster
    assert "`protect_first_n` controls how many **non-system** head messages" in en_cluster
    assert "`protect_first_n` 控制每次压缩时要固定保留多少条**非系统**开头消息" in zh_cluster

    assert "hermes config migrate" not in en_cluster
    assert "hermes config migrate" not in zh_cluster
    assert "hermes config show" not in en_cluster
    assert "hermes config show" not in zh_cluster
    assert "hermes config set skills.config.myplugin.path" not in en_cluster
    assert "hermes config set skills.config.myplugin.path" not in zh_cluster
    assert "Hermes can optionally scan" not in en_cluster
    assert "Hermes 可以选择扫描" not in zh_cluster
    assert "before Hermes truncates it" not in en_cluster
    assert "在 Hermes 截断之前" not in zh_cluster
    assert "`hermes tools`" not in en_cluster
    assert "`hermes tools`" not in zh_cluster
    assert "same as hermes -w" not in en_cluster
    assert "与 hermes -w 相同" not in zh_cluster
    assert "Hermes automatically compresses long conversations" not in en_cluster
    assert "Hermes 自动压缩长对话" not in zh_cluster

    for literal in (
        "skills.config",
        "guard_agent_created",
        "~/.ssh/",
        "$OPENAI_API_KEY",
        "file_read_max_chars",
        "tool_output:",
        "max_bytes",
        "max_lines",
        "max_line_length",
        "agent.disabled_toolsets",
        ".worktrees/",
        "threshold",
        "target_ratio",
        "protect_last_n",
        "hygiene_hard_message_limit",
        "auxiliary.compression.provider",
        "auxiliary.compression.base_url",
    ):
        assert literal in en_cluster
        assert literal in zh_cluster


def test_configuration_context_engine_and_auxiliary_cluster_prefer_doppel_and_keep_runtime_terms():
    en = EN_CONFIGURATION_DOC.read_text(encoding="utf-8")
    zh = ZH_CONFIGURATION_DOC.read_text(encoding="utf-8")

    en_cluster = _extract_configuration_middle_cluster(
        en, "## Context Engine", "## Reasoning Effort"
    )
    zh_cluster = _extract_configuration_middle_cluster(
        zh, "## 上下文引擎", "## 推理努力程度"
    )

    assert "doppel plugins" in en_cluster
    assert "doppel plugins" in zh_cluster
    assert "Doppel Agent retries a provider API call" in en_cluster
    assert "Doppel Agent 在回退 provider 切换启动" in zh_cluster
    assert "Doppel Agent has separate timeout layers" in en_cluster
    assert "Doppel Agent 对流式传输有单独的超时层" in zh_cluster
    assert "Doppel Agent turns on cross-session prompt caching automatically" in en_cluster
    assert "Doppel Agent 自动开启跨会话 prompt 缓存" in zh_cluster
    assert "across Doppel sessions" in en_cluster
    assert "跨 Doppel 会话" in zh_cluster
    assert 'Doppel Agent uses "auxiliary" models' in en_cluster
    assert 'Doppel Agent 使用"辅助"模型' in zh_cluster
    assert "doppel model" in en_cluster
    assert "doppel model" in zh_cluster
    assert "doppel auth" in en_cluster
    assert "doppel auth" in zh_cluster
    assert "doppel config" in en_cluster
    assert "doppel config" in zh_cluster
    assert "doppel kanban specify <id>" in en_cluster
    assert "doppel kanban specify <id>" in zh_cluster
    assert "doppel kanban decompose <id>" in en_cluster
    assert "doppel kanban decompose <id>" in zh_cluster
    assert "### Auxiliary config reference {#auxiliary-config-reference}" in en_cluster
    assert "### 辅助配置参考 {#auxiliary-config-reference}" in zh_cluster
    assert "OpenRouter → Nous → custom → Codex → API-key providers" in en_cluster
    assert "OpenRouter → Nous → custom → Codex → API 密钥 providers" in zh_cluster
    assert "Or via environment variable (in `~/.doppel/.env`; legacy `~/.hermes/.env` also works):" in en_cluster
    assert "或通过环境变量（在 `~/.doppel/.env` 中；旧版 `~/.hermes/.env` 也可用）：" in zh_cluster
    assert "# In ~/.doppel/.env (legacy ~/.hermes/.env also works):" in en_cluster
    assert "# 在 ~/.doppel/.env 中（旧版 ~/.hermes/.env 也可用）：" in zh_cluster
    assert "AUXILIARY_APPROVAL_PROVIDER" in en_cluster
    assert "AUXILIARY_APPROVAL_PROVIDER" in zh_cluster
    assert "AUXILIARY_APPROVAL_MODEL" in en_cluster
    assert "AUXILIARY_APPROVAL_MODEL" in zh_cluster
    assert "AUXILIARY_APPROVAL_BASE_URL" in en_cluster
    assert "AUXILIARY_APPROVAL_BASE_URL" in zh_cluster
    assert "AUXILIARY_APPROVAL_API_KEY" in en_cluster
    assert "AUXILIARY_APPROVAL_API_KEY" in zh_cluster
    assert "title_generation:" in en_cluster
    assert "title_generation:" in zh_cluster
    assert "kanban_decomposer:" in en_cluster
    assert "kanban_decomposer:" in zh_cluster
    assert "profile_describer:" in en_cluster
    assert "profile_describer:" in zh_cluster
    assert "curator:" in en_cluster
    assert "curator:" in zh_cluster

    assert "hermes plugins" not in en_cluster
    assert "hermes plugins" not in zh_cluster
    assert "hermes auth" not in en_cluster
    assert "hermes auth" not in zh_cluster
    assert "hermes config" not in en_cluster
    assert "hermes config" not in zh_cluster
    assert "hermes kanban specify <id>" not in en_cluster
    assert "hermes kanban specify <id>" not in zh_cluster
    assert "hermes kanban decompose <id>" not in en_cluster
    assert "hermes kanban decompose <id>" not in zh_cluster
    assert "Full auxiliary config reference" not in en_cluster
    assert "完整辅助配置参考" not in zh_cluster

    for literal in (
        "DOPPEL_STREAM_READ_TIMEOUT",
        "DOPPEL_STREAM_STALE_TIMEOUT",
        "DOPPEL_API_CALL_STALE_TIMEOUT",
        "DOPPEL_API_TIMEOUT",
        "cache_control",
        'ttl: "1h"',
        "OPENROUTER_API_KEY",
        "OPENAI_BASE_URL",
        "OPENAI_API_KEY",
        "fallback_providers:",
        "fallback_model:",
        "gpt-5.3-codex",
    ):
        assert literal in en_cluster
        assert literal in zh_cluster


def test_mcp_config_reference_docs_prefer_doppel_branding_and_keep_runtime_literals():
    en = EN_MCP_CONFIG_REFERENCE_DOC.read_text(encoding="utf-8")
    zh = ZH_MCP_CONFIG_REFERENCE_DOC.read_text(encoding="utf-8")

    assert 'description: "Reference for Doppel Agent MCP configuration keys, filtering semantics, and utility-tool policy"' in en
    assert 'description: "Doppel Agent MCP 配置键、过滤语义及工具策略参考"' in zh
    assert "[Use MCP with Doppel Agent](/guides/use-mcp-with-hermes)" in en
    assert "[在 Doppel Agent 中使用 MCP](/guides/use-mcp-with-hermes)" in zh
    assert "Doppel Agent may register these utility wrappers per MCP server" in en
    assert "Doppel Agent 可为每个 MCP 服务器注册以下工具包装器" in zh
    assert "Doppel Agent only registers those utility tools" in en
    assert "Doppel Agent 也只在 MCP 会话实际暴露对应能力时才注册相应工具" in zh
    assert "Doppel Agent does not create an empty MCP runtime toolset" in en
    assert "Doppel Agent 不会为该服务器创建空的 MCP 运行时工具集" in zh
    assert "## TLS client certificate (mTLS)" in en
    assert "## TLS 客户端证书（mTLS）" in zh
    assert "client_cert: \"~/secrets/mcp-client.pem\"" in en
    assert "client_cert: \"~/secrets/mcp-client.pem\"" in zh
    assert "client_key: \"~/secrets/client.key\"" in en
    assert "client_key: \"~/secrets/client.key\"" in zh
    assert "Doppel Agent uses the MCP SDK's OAuth 2.1 PKCE flow" in en
    assert "Doppel Agent 使用 MCP SDK 的 OAuth 2.1 PKCE 流程" in zh
    assert "`~/.doppel/mcp-tokens/<server>.json`" in en
    assert "`~/.doppel/mcp-tokens/<server>.json`" in zh

    assert "Use MCP with Doppel](/guides/use-mcp-with-hermes)" not in en
    assert "在 Hermes 中使用 MCP" not in zh
    assert 'description: "Hermes Agent MCP 配置键、过滤语义及工具策略参考"' not in zh
    assert "Hermes 可为每个 MCP 服务器注册以下工具包装器" not in zh
    assert "Hermes 也只在 MCP 会话实际暴露对应能力时才注册相应工具" not in zh
    assert "Hermes 不会为该服务器创建空的 MCP 运行时工具集" not in zh
    assert "Hermes 使用 MCP SDK 的 OAuth 2.1 PKCE 流程" not in zh

    for fixed in (
        "/reload-mcp",
        "mcp_<server>_<tool>",
        "mcp_<server>_list_resources",
        "mcp_<server>_read_resource",
        "mcp_<server>_list_prompts",
        "mcp_<server>_get_prompt",
        "auth: oauth",
        "ssl_verify",
        "client_cert",
        "client_key",
        "~/.hermes/",
    ):
        assert fixed in en
        assert fixed in zh


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


def test_integrations_providers_docs_prefer_doppel_customer_facing_wording_and_preserve_runtime_literals():
    en = EN_INTEGRATIONS_PROVIDERS_DOC.read_text(encoding="utf-8")
    zh = ZH_INTEGRATIONS_PROVIDERS_DOC.read_text(encoding="utf-8")
    en_preview = "\n".join(en.splitlines()[:220])
    zh_preview = "\n".join(zh.splitlines()[:220])

    assert "AI Providers" in en_preview
    assert "AI 提供商" in zh_preview
    assert "Doppel Agent" in en
    assert "Doppel Agent" in zh
    assert "recommended way to run Doppel Agent" in en_preview
    assert "运行 Doppel Agent 的推荐方式" in zh_preview
    assert "`doppel setup --portal`" in en_preview
    assert "`doppel setup --portal`" in zh_preview
    assert "`doppel model`" in en_preview
    assert "`doppel model`" in zh_preview
    assert "hermes model" not in en_preview
    assert "hermes model" not in zh_preview
    assert "doppel chat --provider" in en_preview
    assert "doppel chat --provider" in zh_preview
    assert "doppel auth add" in en_preview
    assert "doppel auth add" in zh_preview

    for literal in (
        "client=hermes-client-v<version>",
        "DOPPEL_COPILOT_ACP_COMMAND",
        "DOPPEL_COPILOT_ACP_ARGS",
        "DOPPEL_QWEN_BASE_URL",
        "DOPPEL_GEMINI_PROJECT_ID",
        "--tool-call-parser hermes",
    ):
        assert literal in en
        assert literal in zh

    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/auth.json" in en
    assert "~/.doppel/auth.json" in zh


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


def test_tools_reference_docs_prefer_doppel_customer_facing_wording_and_keep_runtime_literals():
    en = EN_TOOLS_REFERENCE_DOC.read_text(encoding="utf-8")
    zh = ZH_TOOLS_REFERENCE_DOC.read_text(encoding="utf-8")
    en_intro = "\n".join(en.splitlines()[:20])
    zh_intro = "\n".join(zh.splitlines()[:20])

    assert 'description: "Authoritative reference for Doppel Agent built-in tools, grouped by toolset"' in en
    assert "This page documents Doppel Agent's built-in tools" in en
    assert "In addition to built-in tools, Doppel Agent can load tools dynamically from MCP servers." in en
    assert "Doppel Agent tools programmatically" in en
    assert "Hermes" not in en_intro

    assert 'title: "' in zh and "内置工具参考" in zh
    assert "本页记录" in zh
    assert "Doppel" in zh
    assert "Doppel Agent" in zh
    assert "Hermes" not in zh_intro

    assert "Hermes 内置工具权威参考，按工具集分组" not in zh
    assert "本页记录 Hermes 的内置工具" not in zh
    assert "除内置工具外，Hermes 还可从 MCP 服务器动态加载工具" not in zh
    assert "运行可以编程方式调用 Hermes 工具的 Python 脚本" not in zh
    assert "通过 `doppel tools` → 🐦 X (Twitter) Search 选择启用" in zh
    assert "运行一次 `doppel spotify setup` 进行授权" in zh

    for fixed in (
        "`hermes-cli`",
        "`hermes-discord`",
        "`hermes-yuanbao`",
        "HERMES_KANBAN_TASK",
        "~/.hermes/skills/",
    ):
        assert fixed in en or fixed in zh

    assert "legacy `~/.hermes/skills/`" in en
    assert "旧版 `~/.hermes/skills/` 目录树仍可用" in zh
    assert "HERMES_KANBAN_TASK" in en
    assert "HERMES_KANBAN_TASK" in zh

    assert "hermes-cli" in en or "hermes-cli" in zh
    assert "`doppel tools`" in en
    assert "`doppel tools`" in zh
    assert "doppel spotify setup" in en
    assert "doppel spotify setup" in zh


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

    for fixed in ("DOPPEL_GEMINI_PROJECT_ID", "DOPPEL_QWEN_BASE_URL", "Auxiliary <task>"):
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

    for fixed in ("HERMES_HOME", "DOPPEL_CRON_SCRIPT_TIMEOUT", "cronjob", "wakeAgent"):
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


def test_feature_skills_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_FEATURE_SKILLS_DOC.read_text(encoding="utf-8")
    zh = ZH_FEATURE_SKILLS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent currently integrates with these skills ecosystems" in en
    assert "Doppel Agent 目前与以下 skills 生态系统和发现来源集成" in zh
    assert "~/.doppel/skills/" in en
    assert "~/.doppel/skills/" in zh
    assert "doppel chat --toolsets skills -q \"What skills do you have?\"" in en
    assert "doppel chat --toolsets skills -q \"What skills do you have?\"" in zh
    assert "doppel bundles create backend-dev" in en
    assert "doppel bundles create backend-dev" in zh
    assert "doppel skills browse --source official" in en
    assert "doppel skills browse --source official" in zh
    assert "doppel skills install official/security/1password" in en
    assert "doppel skills install official/security/1password" in zh
    assert "doppel skills tap add my-org/doppel-skills" in en
    assert "doppel skills tap add my-org/doppel-skills" in zh
    assert "doppel skills install my-org/doppel-skills/deploy-runbook" in en
    assert "doppel skills install my-org/doppel-skills/deploy-runbook" in zh
    assert "doppel skills reset google-workspace" in en
    assert "doppel skills reset google-workspace" in zh

    for fixed in (
        ".hermes/plans/",
        "  hermes:",
        "HERMES_HOME",
        "TRUSTED_REPOS",
    ):
        assert fixed in en
        assert fixed in zh

    assert "hermes-agent.nousresearch.com/docs" in en

    assert "Hermes currently integrates with these skills ecosystems" not in en
    assert "Hermes 目前与以下 skills 生态系统和发现来源集成" not in zh
    assert "hermes chat --toolsets skills" not in en
    assert "hermes chat --toolsets skills" not in zh
    assert "hermes bundles create" not in en
    assert "hermes bundles create" not in zh
    assert "hermes skills browse" not in en
    assert "hermes skills browse" not in zh
    assert "hermes skills install" not in en
    assert "hermes skills install" not in zh
    assert "my-org/hermes-skills" not in en
    assert "my-org/hermes-skills" not in zh


def test_zh_reference_skill_docs_mirror_doppel_skill_commands():
    zh_skills_catalog = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "skills-catalog.md"
    ).read_text(encoding="utf-8")
    zh_optional_skills_catalog = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "optional-skills-catalog.md"
    ).read_text(encoding="utf-8")
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    assert "`doppel update`" in zh_skills_catalog
    assert "`doppel skills reset <name> --restore`" in zh_skills_catalog
    assert "`hermes update`" not in zh_skills_catalog
    assert "`hermes skills reset <name> --restore`" not in zh_skills_catalog

    assert "doppel skills install official/<category>/<skill>" in zh_optional_skills_catalog
    assert "doppel skills uninstall <skill-name>" in zh_optional_skills_catalog
    assert "hermes skills install official/<category>/<skill>" not in zh_optional_skills_catalog
    assert "hermes skills uninstall <skill-name>" not in zh_optional_skills_catalog

    assert "doppel skills install official/migration/openclaw-migration" in zh_cli_commands
    assert "doppel skills reset google-workspace" in zh_cli_commands
    assert "hermes skills install official/migration/openclaw-migration" not in zh_cli_commands
    assert "hermes skills reset google-workspace" not in zh_cli_commands


def test_zh_reference_cli_commands_rebrand_top_level_model_support_and_update_sections():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    top = zh_cli_commands.split("## `doppel chat`", 1)[0]
    pre_model = zh_cli_commands.split("## `doppel model`", 1)[0]
    model = zh_cli_commands.split("## `doppel model`", 1)[1].split("## `doppel gateway`", 1)[0]
    support = zh_cli_commands.split("## `doppel dump`", 1)[1].split("## `doppel checkpoints`", 1)[0]
    update = zh_cli_commands.split("## `doppel update`", 1)[1].split("## 维护命令", 1)[0]

    assert "doppel [global-options] <command> [subcommand/options]" in top
    assert "~/.doppel/config.yaml" in top
    assert "`doppel send`" in top
    assert "`doppel backup`" in top
    assert "`doppel update`" in top
    assert "hermes [global-options] <command> [subcommand/options]" not in top
    assert "| `hermes chat` |" not in top
    assert "| `hermes model` |" not in top

    assert "doppel -z " in pre_model
    assert "`doppel chat -q`" in pre_model
    assert "`doppel model`" in model
    assert "活跃的 Doppel 聊天会话" in model
    assert "hermes -z " not in pre_model
    assert "`hermes chat -q`" not in pre_model
    assert "`hermes model`" not in model

    assert "--- doppel dump ---" in support
    assert "DOPPEL_HOME 路径" in support
    assert "`doppel doctor`" in support
    assert "doppel debug share" in support
    assert "doppel backup" in support
    assert "`~/doppel-backup-<timestamp>.zip`" in support
    assert "`hermes-backup-*`" not in support
    assert "--- hermes dump ---" not in support
    assert "hermes debug share" not in support
    assert "## `hermes backup`" not in support

    assert "doppel update [--gateway] [--check] [--no-backup] [--backup] [--yes]" in update
    assert "`pip install --upgrade hermes-agent`" in update
    assert "`hermes.service`" in update
    assert "`doppel backup restore --state pre-update`" in update
    assert "## `hermes update`" not in zh_cli_commands
    assert "hermes update [--check] [--backup] [--restart-gateway]" not in update


def test_zh_reference_cli_commands_rebrand_checkpoints_promptsize_and_skills_cluster():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    section = zh_cli_commands.split("## `doppel checkpoints`", 1)[1].split("## `hermes hooks`", 1)[0]

    assert "doppel checkpoints [COMMAND]" in section
    assert "~/.doppel/checkpoints/" in section
    assert "doppel import ~/doppel-backup-20260423.zip" in section
    assert "doppel logs [log_name] [options]" in section
    assert "~/.doppel/logs/" in section
    assert "## `doppel prompt-size`" in section
    assert "doppel prompt-size --platform telegram" in section
    assert "`doppel tools`" in section
    assert "doppel config <subcommand>" in section
    assert "doppel pairing <list|approve|revoke|clear-pending>" in section
    assert "doppel skills browse" in section
    assert "doppel bundles create backend-dev" in section
    assert "~/.doppel/skill-bundles/<slug>.yaml" in section
    assert "doppel curator run --dry-run" in section
    assert "从快照恢复 `~/.doppel/skills/`" in section
    assert "与 `doppel model` 相同的选择器" in section
    assert "## `hermes checkpoints`" not in section
    assert "hermes import ~/doppel-backup-20260423.zip" not in section
    assert "hermes logs [log_name] [options]" not in section
    assert "## `hermes config`" not in section
    assert "hermes skills browse" not in section
    assert "## `hermes bundles`" not in section
    assert "hermes curator run --dry-run" not in section
    assert "与 `hermes model` 相同的选择器" not in section


def test_zh_reference_cli_commands_rebrand_hooks_mcp_and_sessions_cluster():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    section = zh_cli_commands.split("## `doppel hooks`", 1)[1].split("## `hermes insights`", 1)[0]

    assert "doppel hooks <subcommand>" in section
    assert "~/.doppel/config.yaml" in section
    assert "~/.doppel/shell-hooks-allowlist.json" in section
    assert "doppel memory <subcommand>" in section
    assert "`doppel honcho`" in section
    assert "运行 `doppel --help`" in section
    assert "doppel acp" in section
    assert "将 Doppel 作为 ACP" in section
    assert "hermes-acp" in section
    assert "doppel mcp <subcommand>" in section
    assert "doppel mcp install n8n" in section
    assert "[在 Doppel 中使用 MCP](../guides/use-mcp-with-hermes.md)" in section
    assert "doppel plugins [subcommand]" in section
    assert "[构建 Doppel Plugin](../guides/build-a-hermes-plugin.md)" in section
    assert "doppel tools [--summary]" in section
    assert "doppel computer-use <subcommand>" in section
    assert "`doppel computer-use install`" in section
    assert "`doppel tools`" in section
    assert "`doppel update`" in section
    assert "doppel sessions <subcommand>" in section
    assert "`rename <session-id> <title>`" in section
    assert "## `hermes hooks`" not in section
    assert "## `hermes memory`" not in section
    assert "## `hermes acp`" not in section
    assert "## `hermes mcp`" not in section
    assert "## `hermes plugins`" not in section
    assert "## `hermes tools`" not in section
    assert "## `hermes computer-use`" not in section
    assert "## `hermes sessions`" not in section
    assert "运行 `hermes --help`" not in section


def test_zh_reference_cli_commands_rebrand_insights_claw_dashboard_and_profile_cluster():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    section = zh_cli_commands.split("## `doppel insights`", 1)[1].split("## `doppel completion`", 1)[0]

    assert "doppel insights [--days N] [--source platform]" in section
    assert "## `doppel claw`" in section
    assert "将 OpenClaw 设置迁移到 Doppel" in section
    assert "~/.doppel/backups/pre-migration-*.zip" in section
    assert "doppel import" in section
    assert "直接导入**到 Doppel 等效项" in section
    assert "doppel claw migrate --preset full" in section
    assert "## `doppel dashboard`" in section
    assert "`doppel --tui`" in section
    assert "`doppel dashboard`" in section
    assert "## `doppel profile`" in section
    assert "多个隔离的 Doppel 实例" in section
    assert "doppel profile list" in section
    assert 'doppel -p work chat -q "Hello from work profile"' in section
    assert "## `hermes insights`" not in section
    assert "## `hermes claw`" not in section
    assert "现有 Hermes 文件" not in section
    assert "~/.hermes/backups/pre-migration-*.zip" not in section
    assert "hermes claw migrate --dry-run" not in section
    assert "## `hermes dashboard`" not in section
    assert "`hermes --tui`" not in section
    assert "## `hermes profile`" not in section
    assert "多个隔离的 Hermes 实例" not in section
    assert "hermes profile list" not in section
    assert 'hermes -p work chat -q "Hello from work profile"' not in section


def test_zh_reference_cli_commands_rebrand_completion_block():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    section = zh_cli_commands.split("## `doppel completion`", 1)[1].split("## `doppel update`", 1)[0]

    assert "doppel completion [bash|zsh|fish]" in section
    assert "对 Doppel 命令、子命令和 profile 名称进行 Tab 补全" in section
    assert "doppel completion bash >> ~/.bashrc" in section
    assert "doppel completion zsh >> ~/.zshrc" in section
    assert "doppel completion fish > ~/.config/fish/completions/doppel.fish" in section
    assert "## `hermes completion`" not in section
    assert "对 Hermes 命令、子命令和 profile 名称进行 Tab 补全" not in section
    assert "hermes completion bash >> ~/.bashrc" not in section
    assert "hermes completion zsh >> ~/.zshrc" not in section
    assert "hermes completion fish > ~/.config/fish/completions/hermes.fish" not in section


def test_zh_reference_cli_commands_rebrand_gateway_setup_and_portal_cluster():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    section = zh_cli_commands.split("## `doppel gateway`", 1)[1].split("## `doppel whatsapp`", 1)[0]

    assert "doppel gateway <subcommand>" in section
    assert "而不仅限于当前智能体主目录" in section
    assert "在 `doppel update` 后全部重启" in section
    assert "使用 `doppel gateway run` 而非 `doppel gateway start`" in section
    assert "tmux new -s doppel 'doppel gateway run'" in section
    assert "doppel lsp <subcommand>" in section
    assert "## `doppel setup`" in section
    assert "**最简单路径：** `doppel setup --portal`" in section
    assert "运行 `doppel setup` 现在默认执行此操作" in section
    assert "## `doppel portal`" in section
    assert "上方的 `doppel setup --portal`" in section
    assert "## `hermes gateway`" not in section
    assert "在 `hermes update` 后全部重启" not in section
    assert "使用 `hermes gateway run` 而非 `hermes gateway start`" not in section
    assert "tmux new -s hermes 'hermes gateway run'" not in section
    assert "doppel lsp <subcommand>" in section
    assert "## `hermes lsp`" not in section
    assert "## `hermes setup`" not in section
    assert "运行 `hermes setup` 现在默认执行此操作" not in section
    assert "## `hermes portal`" not in section
    assert "上方的 `hermes setup --portal`" not in section


def test_zh_reference_cli_commands_rebrand_whatsapp_auth_and_cron_cluster():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    section = zh_cli_commands.split("## `doppel whatsapp`", 1)[1].split("## `doppel kanban`", 1)[0]

    assert "```bash\ndoppel whatsapp\n```" in section
    assert "## `doppel slack`" in section
    assert "doppel slack manifest --write" in section
    assert "~/.doppel/slack-manifest.json" in section
    assert "$DOPPEL_HOME/slack-manifest.json" in section
    assert "| `--name NAME` | `Doppel` |" in section
    assert "`doppel update` 后重新运行 `doppel slack manifest --write`" in section
    assert "## `doppel login` / `doppel logout` *（已弃用）*" in section
    assert "`doppel auth` 管理 OAuth 凭据" in section
    assert "## `doppel auth`" in section
    assert "doppel auth spotify                                      # 通过 PKCE 将 Doppel 与 Spotify 认证" in section
    assert "## `doppel status`" in section
    assert "doppel status [--all] [--deep]" in section
    assert "## `doppel cron`" in section
    assert "doppel cron <list|create|edit|pause|resume|run|remove|status|tick>" in section
    assert "## `hermes whatsapp`" not in section
    assert "## `hermes slack`" not in section
    assert "~/.hermes/slack-manifest.json" not in section
    assert "| `--name NAME` | `Hermes` |" not in section
    assert "`hermes update` 后重新运行 `hermes slack manifest --write`" not in section
    assert "## `hermes login` / `hermes logout` *（已弃用）*" not in section
    assert "`hermes auth` 管理 OAuth 凭据" not in section
    assert "## `hermes auth`" not in section
    assert "通过 PKCE 将 Hermes 与 Spotify 认证" not in section
    assert "## `hermes status`" not in section
    assert "hermes status [--all] [--deep]" not in section
    assert "## `hermes cron`" not in section
    assert "hermes cron <list|create|edit|pause|resume|run|remove|status|tick>" not in section


def test_zh_reference_cli_commands_rebrand_kanban_webhook_and_doctor_cluster():
    zh_cli_commands = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    section = zh_cli_commands.split("## `doppel kanban`", 1)[1].split("## `doppel dump`", 1)[0]

    assert "doppel kanban [--board <slug>] <action> [options]" in section
    assert "~/.doppel/kanban.db" in section
    assert "通过 `doppel kanban boards switch`" in section
    assert "而非调用 `doppel kanban`" in section
    assert "写入 `~/.doppel/kanban/current`" in section
    assert "doppel kanban boards create atm10-server" in section
    assert "doppel kanban boards rm atm10-server --delete" in section
    assert "→ `~/.doppel/kanban/current` 文件" in section
    assert "## `doppel webhook`" in section
    assert "doppel webhook <subscribe|list|remove|test>" in section
    assert "### `doppel webhook subscribe`" in section
    assert "doppel webhook subscribe <name> [options]" in section
    assert "~/.doppel/webhook_subscriptions.json" in section
    assert "## `doppel doctor`" in section
    assert "doppel doctor [--fix]" in section
    assert "## `hermes kanban`" not in section
    assert "~/.hermes/kanban.db" not in section
    assert "通过 `hermes kanban boards switch`" not in section
    assert "而非调用 `hermes kanban`" not in section
    assert "写入 `~/.hermes/kanban/current`" not in section
    assert "hermes kanban boards create atm10-server" not in section
    assert "## `hermes webhook`" not in section
    assert "### `hermes webhook subscribe`" not in section
    assert "~/.hermes/webhook_subscriptions.json" not in section
    assert "## `hermes doctor`" not in section
    assert "hermes doctor [--fix]" not in section


def test_feature_acp_docs_prefer_doppel_surfaces_and_keep_registry_literals():
    en = EN_FEATURE_ACP_DOC.read_text(encoding="utf-8")
    zh = ZH_FEATURE_ACP_DOC.read_text(encoding="utf-8")

    assert "Use Doppel Agent inside ACP-compatible editors" in en
    assert "在 VS Code、Zed 和 JetBrains 等兼容 ACP 的编辑器中使用 Doppel Agent" in zh
    assert "Doppel Agent can run as an ACP server" in en
    assert "Doppel Agent 可作为 ACP 服务器运行" in zh
    assert "What Doppel Agent exposes in ACP mode" in en
    assert "Doppel Agent 在 ACP 模式下暴露的内容" in zh
    assert "doppel acp" in en
    assert "doppel acp" in zh
    assert "doppel model" in en
    assert "doppel model" in zh
    assert "doppel doctor" in en
    assert "doppel doctor" in zh
    assert "doppel status" in en
    assert "doppel status" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/node/" in en
    assert "~/.doppel/node/" in zh
    assert '"Doppel Agent": {' in en
    assert '"doppel-agent": {' in en
    assert '"Doppel Agent": {' in zh
    assert '"doppel-agent": {' in zh

    for fixed in (
        "hermes-acp",
        "hermes-agent[acp]",
        "acp_registry/agent.json",
        "agentclientprotocol/registry",
        "~/.hermes/",
        "Hermes Agent",
    ):
        assert fixed in en
        assert fixed in zh

    assert "Use Hermes Agent inside ACP-compatible editors" not in en
    assert "在 VS Code、Zed 和 JetBrains 等兼容 ACP 的编辑器中使用 Hermes Agent" not in zh
    assert "Hermes Agent can run as an ACP server" not in en
    assert "Hermes Agent 可作为 ACP 服务器运行" not in zh
    assert "What Hermes exposes in ACP mode" not in en
    assert "Hermes 在 ACP 模式下暴露的内容" not in zh
    assert "hermes acp --version" not in en
    assert "hermes acp --version" not in zh
    assert "hermes acp --check" not in en
    assert "hermes acp --check" not in zh
    assert "hermes model" not in en
    assert "hermes model" not in zh
    assert "hermes doctor" not in en
    assert "hermes doctor" not in zh
    assert "hermes status" not in en
    assert "hermes status" not in zh
    assert '"command": "hermes"' not in en
    assert '"command": "hermes"' not in zh


def test_tts_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_TTS_DOC.read_text(encoding="utf-8")
    zh = ZH_TTS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent supports both text-to-speech output" in en
    assert "Doppel Agent 支持跨所有消息平台的文字转语音" in zh
    assert "doppel setup --portal" in en
    assert "doppel setup --portal" in zh
    assert "doppel model" in en
    assert "doppel model" in zh
    assert "doppel tools" in en
    assert "doppel tools" in zh
    assert "doppel plugins enable my-tts" in en
    assert "doppel plugins enable my-tts" in zh
    assert "~/.doppel/audio_cache/" in en
    assert "~/.doppel/audio_cache/" in zh
    assert "~/.doppel/cache/piper-voices/" in en
    assert "~/.doppel/cache/piper-voices/" in zh
    assert "# In ~/.doppel/config.yaml" in en
    assert "# In ~/.doppel/config.yaml" in zh

    for fixed in (
        "DOPPEL_LOCAL_STT_COMMAND",
        "~/.hermes/plugins/my-tts/",
        "pip install hermes-agent[mistral]",
        "tts.providers.<name>",
    ):
        assert fixed in en
        assert fixed in zh

    assert "HERMES_LOCAL_STT_COMMAND" in en
    assert "HERMES_LOCAL_STT_COMMAND" in zh

    assert "doppel plugins enable my-stt" in en
    assert "stt.providers.<name>" in en

    assert "Hermes Agent supports both text-to-speech output" not in en
    assert "Hermes Agent 支持跨所有消息平台的文字转语音" not in zh
    assert "hermes setup --portal" not in en
    assert "hermes setup --portal" not in zh
    assert "hermes model" not in en
    assert "hermes model" not in zh
    assert "hermes tools" not in en
    assert "hermes tools" not in zh
    assert "hermes plugins enable my-tts" not in en
    assert "hermes plugins enable my-tts" not in zh
    assert "~/.hermes/audio_cache/" not in en
    assert "~/.hermes/audio_cache/" not in zh
    assert "~/.hermes/cache/piper-voices/" not in en
    assert "~/.hermes/cache/piper-voices/" not in zh
    assert "# In ~/.hermes/config.yaml" not in en
    assert "# In ~/.hermes/config.yaml" not in zh


def test_spotify_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_SPOTIFY_DOC.read_text(encoding="utf-8")
    zh = ZH_SPOTIFY_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent can control Spotify directly" in en
    assert "Doppel Agent 可以直接控制 Spotify" in zh
    assert "`doppel auth spotify`" in en
    assert "`doppel auth spotify`" in zh
    assert "`doppel tools`" in en
    assert "`doppel tools`" in zh
    assert "`doppel setup` / `doppel setup tools`" in en
    assert "`doppel setup` / `doppel setup tools`" in zh
    assert "doppel cron add" in en
    assert "doppel cron add" in zh
    assert "~/.doppel/auth.json" in en
    assert "~/.doppel/auth.json" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "App name | anything (e.g. `doppel-agent`)" in en
    assert "App name | 任意（例如 `doppel-agent`）" in zh
    assert "personal Doppel integration" in en
    assert "personal Doppel integration" in zh

    for fixed in (
        "HERMES_SPOTIFY_CLIENT_ID",
        "HERMES_SPOTIFY_REDIRECT_URI",
        "providers.spotify",
        "/guides/oauth-over-ssh",
    ):
        assert fixed in en
        assert fixed in zh

    assert "Legacy installs may still keep the same auth files under `~/.hermes`." in en
    assert "旧安装仍可能把相同的认证文件保存在 `~/.hermes` 下。" in zh

    assert "Hermes can control Spotify directly" not in en
    assert "Hermes 可以直接控制 Spotify" not in zh
    assert "`hermes auth spotify`" not in en
    assert "`hermes auth spotify`" not in zh
    assert "`hermes tools`" not in en
    assert "`hermes tools`" not in zh
    assert "`hermes setup` / `hermes setup tools`" not in en
    assert "`hermes setup` / `hermes setup tools`" not in zh
    assert "hermes cron add" not in en
    assert "hermes cron add" not in zh
    assert "~/.hermes/auth.json" not in en
    assert "~/.hermes/auth.json" not in zh
    assert "~/.hermes/.env" not in en
    assert "~/.hermes/.env" not in zh


def test_web_search_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_WEB_SEARCH_DOC.read_text(encoding="utf-8")
    zh = ZH_WEB_SEARCH_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent includes two model-callable web tools" in en
    assert "Doppel Agent 内置两个可供模型调用的网页工具" in zh
    assert "`doppel tools`" in en
    assert "`doppel tools`" in zh
    assert "`doppel setup --portal`" in en
    assert "`doppel setup --portal`" in zh
    assert "`doppel model`" in en
    assert "`doppel model`" in zh
    assert "`doppel setup`" in en
    assert "`doppel setup`" in zh
    assert "doppel auth add xai-oauth --type oauth" in en
    assert "doppel auth add xai-oauth --type oauth" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "source ~/.doppel/doppel-agent/.venv/bin/activate" in en
    assert "source ~/.doppel/doppel-agent/.venv/bin/activate" in zh
    assert "doppel skills install official/research/searxng-search" in en
    assert "doppel skills install official/research/searxng-search" in zh

    for fixed in (
        "web_extract",
        "web_search",
        "FIRECRAWL_API_KEY",
        "SEARXNG_URL",
        "XAI_API_KEY",
        "Tool Gateway",
        "Nous Portal",
        "Legacy installs may still keep the same config and env files under `~/.hermes`.",
        "旧安装仍可能将相同的配置和环境变量文件保存在 `~/.hermes` 下。",
    ):
        assert fixed in en or fixed in zh

    assert "Hermes Agent includes two model-callable web tools" not in en
    assert "Hermes Agent 内置两个可供模型调用的网页工具" not in zh
    assert "`hermes tools`" not in en
    assert "`hermes tools`" not in zh
    assert "`hermes setup --portal`" not in en
    assert "`hermes setup --portal`" not in zh
    assert "`hermes model`" not in en
    assert "`hermes model`" not in zh
    assert "`hermes setup`" not in en
    assert "`hermes setup`" not in zh
    assert "hermes auth login xai-oauth" not in en
    assert "hermes auth login xai-oauth" not in zh
    assert "~/.hermes/config.yaml" not in en
    assert "~/.hermes/config.yaml" not in zh
    assert "~/.hermes/.env" not in en
    assert "~/.hermes/.env" not in zh
    assert "source ~/.hermes/hermes-agent/.venv/bin/activate" not in en
    assert "source ~/.hermes/hermes-agent/.venv/bin/activate" not in zh
    assert "hermes skills install official/research/searxng-search" not in en
    assert "hermes skills install official/research/searxng-search" not in zh


def test_voice_mode_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_VOICE_MODE_DOC.read_text(encoding="utf-8")
    zh = ZH_VOICE_MODE_DOC.read_text(encoding="utf-8")

    assert "Real-time voice conversations with Doppel Agent" in en
    assert "与 Doppel Agent 进行实时语音对话" in zh
    assert "Doppel Agent supports full voice interaction" in en
    assert "Doppel Agent 支持在 CLI 和消息平台上进行完整的语音交互" in zh
    assert "[Use Voice Mode with Doppel Agent](/guides/use-voice-mode-with-hermes)" in en
    assert "[在 Doppel Agent 中使用语音模式](/guides/use-voice-mode-with-hermes)" in zh
    assert "`doppel model`" in en
    assert "`doppel model`" in zh
    assert "`doppel setup --portal`" in en
    assert "`doppel setup --portal`" in zh
    assert "`doppel chat`" in en
    assert "`doppel chat`" in zh
    assert "`doppel --tui`" in en
    assert "`doppel --tui`" in zh
    assert "doppel gateway" in en
    assert "doppel gateway" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/logs/" in en
    assert "~/.doppel/logs/" in zh
    assert "@your-bot-name hello" in en
    assert "@your-bot-name 你好" in zh

    for fixed in (
        'uv pip install -e ".[voice]"',
        'uv pip install -e ".[messaging]"',
        'uv pip install -e ".[tts-premium]"',
        'uv pip install -e ".[all]"',
        "~/.doppel/doppel-agent",
        "~/.hermes/.env",
        "~/.hermes/config.yaml",
        "~/.hermes/logs/",
        "DISCORD_REQUIRE_MENTION",
        "DISCORD_FREE_RESPONSE_CHANNELS",
        "GROQ_API_KEY",
        "VOICE_TOOLS_OPENAI_KEY",
        "ELEVENLABS_API_KEY",
        'find_library("opus")',
        "/opt/homebrew/lib/libopus.dylib",
        "/usr/local/lib/libopus.dylib",
        "libopus.so.0",
    ):
        assert fixed in en or fixed in zh

    assert "Real-time voice conversations with Hermes Agent" not in en
    assert "与 Hermes Agent 进行实时语音对话" not in zh
    assert "Hermes Agent supports full voice interaction" not in en
    assert "Hermes Agent 支持在 CLI 和消息平台上进行完整的语音交互" not in zh
    assert "[Use Voice Mode with Hermes](/guides/use-voice-mode-with-hermes)" not in en
    assert "[使用 Hermes 的语音模式](/guides/use-voice-mode-with-hermes)" not in zh
    assert "`hermes model`" not in en
    assert "`hermes model`" not in zh
    assert "`hermes setup --portal`" not in en
    assert "`hermes setup --portal`" not in zh
    assert "`hermes chat`" not in en
    assert "`hermes chat`" not in zh
    assert "`hermes --tui`" not in en
    assert "`hermes --tui`" not in zh
    assert "@hermesbyt4 hello" not in en
    assert "@hermesbyt4 你好" not in zh
    assert "hermes-agent[voice]" not in en
    assert "hermes-agent[voice]" not in zh
    assert "hermes-agent[messaging]" not in en
    assert "hermes-agent[messaging]" not in zh
    assert "hermes-agent[tts-premium]" not in en
    assert "hermes-agent[tts-premium]" not in zh
    assert "hermes-agent[all]" not in en
    assert "hermes-agent[all]" not in zh


def test_voice_and_weixin_guides_use_doppel_checkout_install_commands():
    en_voice_guide = (
        REPO_ROOT / "website" / "docs" / "guides" / "use-voice-mode-with-hermes.md"
    ).read_text(encoding="utf-8")
    zh_voice_guide = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "guides"
        / "use-voice-mode-with-hermes.md"
    ).read_text(encoding="utf-8")
    en_weixin = (
        REPO_ROOT / "website" / "docs" / "user-guide" / "messaging" / "weixin.md"
    ).read_text(encoding="utf-8")
    zh_weixin = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "user-guide"
        / "messaging"
        / "weixin.md"
    ).read_text(encoding="utf-8")

    for doc in (en_voice_guide, zh_voice_guide, en_weixin, zh_weixin):
        assert 'cd ~/.doppel/doppel-agent && uv pip install -e ".[messaging]"' in doc
        assert "hermes-agent[messaging]" not in doc

    for doc in (en_voice_guide, zh_voice_guide):
        assert 'cd ~/.doppel/doppel-agent && uv pip install -e ".[voice]"' in doc
        assert 'cd ~/.doppel/doppel-agent && uv pip install -e ".[tts-premium]"' in doc
        assert 'cd ~/.doppel/doppel-agent && uv pip install -e ".[all]"' in doc
        assert "hermes-agent[voice]" not in doc
        assert "hermes-agent[tts-premium]" not in doc
        assert "hermes-agent[all]" not in doc


def test_honcho_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_HONCHO_DOC.read_text(encoding="utf-8")
    zh = ZH_HONCHO_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent's built-in memory system" in en
    assert "Doppel Agent 内置记忆系统" in zh
    assert "multiple Doppel Agent instances" in en
    assert "多个 Doppel Agent 实例" in zh
    assert "`doppel memory setup`" in en
    assert "`doppel memory setup`" in zh
    assert "`doppel honcho`" in en
    assert "`doppel honcho`" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "$DOPPEL_HOME/honcho.json" in en
    assert "$DOPPEL_HOME/honcho.json" in zh
    assert "When pointing Doppel Agent at a self-hosted Honcho server" in en
    assert "当你将 Doppel Agent 指向自托管 Honcho 服务器时" in zh

    for fixed in (
        "~/.honcho/config.json",
        "$HERMES_HOME/honcho.json",
        "HONCHO_API_KEY",
        "AUTH_JWT_SECRET",
        "AUTH_USE_AUTH=false",
        "openclaw-honcho",
        "honcho_reasoning",
        "honcho_search",
        "doppel honcho migrate",
        "Migrating from `hermes honcho`",
        "从 `hermes honcho` 迁移",
        "~/.hermes/config.yaml",
        "~/.hermes/.env",
    ):
        assert fixed in en or fixed in zh

    assert "Hermes's built-in memory system" not in en
    assert "Hermes 内置记忆系统" not in zh
    assert "multiple Hermes instances" not in en
    assert "多个 Hermes 实例" not in zh
    assert "hermes memory setup    # select \"honcho\" from the provider list" not in en
    assert "hermes memory setup    # 从 provider 列表中选择 \"honcho\"" not in zh
    assert "When pointing Hermes at a self-hosted Honcho server" not in en
    assert "`hermes honcho status`" not in en
    assert "`hermes honcho status`" not in zh


def test_memory_provider_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_MEMORY_PROVIDERS_DOC.read_text(encoding="utf-8")
    zh = ZH_MEMORY_PROVIDERS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent supports 9 external memory provider integrations" in en
    assert "Doppel Agent 支持 9 个外部记忆提供者集成" in zh
    assert "doppel memory setup` only lists the providers whose dependencies are currently installed" in en
    assert "`doppel memory setup` 只会列出当前环境中已安装依赖的提供者" in zh
    assert "doppel memory setup" in en
    assert "doppel memory setup" in zh
    assert "doppel memory status" in en
    assert "doppel memory status" in zh
    assert "doppel memory off" in en
    assert "doppel memory off" in zh
    assert "`doppel plugins`" in en
    assert "`doppel plugins`" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "$DOPPEL_HOME/honcho.json" in en
    assert "$DOPPEL_HOME/honcho.json" in zh
    assert "$DOPPEL_HOME/mem0.json" in en
    assert "$DOPPEL_HOME/mem0.json" in zh
    assert "$DOPPEL_HOME/hindsight/config.json" in en
    assert "$DOPPEL_HOME/hindsight/config.json" in zh
    assert "$DOPPEL_HOME/memory_store.db" in en
    assert "$DOPPEL_HOME/memory_store.db" in zh
    assert "$DOPPEL_HOME/byterover/" in en
    assert "$DOPPEL_HOME/byterover/" in zh
    assert "$DOPPEL_HOME/supermemory.json" in en
    assert "$DOPPEL_HOME/supermemory.json" in zh
    assert "doppel honcho sync" in en
    assert "doppel honcho sync" in zh
    assert "doppel profile create coder --clone" in en
    assert "doppel profile create coder --clone" in zh
    assert "### Memori" in en
    assert "### Memori" in zh
    assert "doppel config set memory.provider memori" in en
    assert "doppel config set memory.provider memori" in zh

    for fixed in (
        "hermes honcho setup",
        "~/.hermes/honcho.json",
        "$HERMES_HOME/honcho.json",
        "$HERMES_HOME/mem0.json",
        "$HERMES_HOME/hindsight/config.json",
        "$HERMES_HOME/supermemory.json",
        "~/.honcho/config.json",
        "OPENVIKING_ENDPOINT",
        "MEM0_API_KEY",
        "HINDSIGHT_API_KEY",
        "RETAINDB_API_KEY",
        "SUPERMEMORY_API_KEY",
        "SUPERMEMORY_CONTAINER_TAG",
        "hermes.coder",
        "hermes.writer",
        '"workspace": "hermes"',
        "hindsight-embed -p hermes ui start",
        "hermes-user",
        "| `bank_id` | `hermes` |",
        "conversation between Hermes Agent and the User",
        '| `container_tag` | `hermes` |',
        "`hermes-memori install`",
    ):
        assert fixed in en or fixed in zh

    assert "Hermes Agent ships with 8 external memory provider plugins" not in en
    assert "Hermes Agent 内置 8 个外部记忆提供者插件" not in zh
    assert "hermes memory setup      # interactive picker + configuration" not in en
    assert "hermes memory setup      # 交互式选择器 + 配置" not in zh
    assert "hermes memory status     # check what's active" not in en
    assert "hermes memory status     # 查看当前激活状态" not in zh
    assert "hermes memory off        # disable external provider" not in en
    assert "hermes memory off        # 禁用外部提供者" not in zh
    assert "`hermes plugins`" not in en
    assert "`hermes plugins`" not in zh


def test_lsp_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_LSP_DOC.read_text(encoding="utf-8")
    zh = ZH_LSP_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent runs full language servers" in en
    assert "Doppel Agent 以后台子进程方式运行完整的语言服务器" in zh
    assert "Doppel Agent ships it self-contained" in en.replace("\n", " ")
    assert "Doppel Agent 将其作为自包含组件提供" in zh
    assert "`<DOPPEL_HOME>/lsp/bin/`" in en
    assert "`<DOPPEL_HOME>/lsp/bin/`" in zh
    assert "`<DOPPEL_HOME>/lsp/node_modules/`" in en
    assert "`<DOPPEL_HOME>/lsp/node_modules/`" in zh
    assert "`doppel lsp status`" in en
    assert "`doppel lsp status`" in zh
    assert "`doppel lsp install typescript`" in en
    assert "`doppel lsp install typescript`" in zh
    assert "doppel lsp restart" in en
    assert "doppel lsp restart" in zh
    assert "~/.doppel/logs/agent.log" in en
    assert "~/.doppel/logs/agent.log" in zh
    assert "`dockerfile-ls` (`dockerfile-language-server-nodejs`)" in en
    assert "`dockerfile-ls`（`dockerfile-language-server-nodejs`）" in zh
    assert "`gleam` (`gleam lsp`)" in en
    assert "`gleam`（`gleam lsp`）" in zh
    assert "off     — same as manual today; reserved for a stricter future mode" in en
    assert "off     — 当前与 manual 相同；为未来更严格的关闭模式预留" in zh

    for fixed in (
        "pyright-langserver",
        "typescript-language-server",
        "rust-analyzer",
        "bash-language-server",
        "shellcheck",
        "write_file",
        "patch",
        "`<HERMES_HOME>/lsp/bin/`",
        "~/.hermes/logs/agent.log",
        "[agent.lsp.client]",
        "ast.parse",
        "json.loads",
    ):
        assert fixed in en or fixed in zh

    assert "Hermes runs full language servers" not in en
    assert "Hermes 以后台子进程方式运行完整的语言服务器" not in zh
    assert "`hermes lsp status`" not in en
    assert "`hermes lsp status`" not in zh
    assert "`hermes lsp install typescript`" not in en
    assert "`hermes lsp install typescript`" not in zh
    assert "`<HERMES_HOME>/lsp/node_modules/`" not in en
    assert "`<HERMES_HOME>/lsp/node_modules/`" not in zh


def test_code_execution_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_CODE_EXECUTION_DOC.read_text(encoding="utf-8")
    zh = ZH_CODE_EXECUTION_DOC.read_text(encoding="utf-8")

    assert "call Doppel Agent tools programmatically" in en
    assert "调用 Doppel Agent 工具的 Python 脚本" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/logs/agent.log" in en
    assert "~/.doppel/logs/agent.log" in zh
    assert "`doppel logs --level DEBUG`" in en
    assert "`doppel logs --level DEBUG`" in zh
    assert "loopback TCP on **Windows**" in en
    assert "在 **Windows** 上使用回环 TCP" in zh
    assert "file-based RPC" in en
    assert "基于文件的 RPC" in zh
    assert "`background`, `pty`, `notify_on_complete`, and `watch_patterns`" in en
    assert "`background`、`pty`、`notify_on_complete` 和 `watch_patterns`" in zh
    assert "[OUTPUT TRUNCATED - X chars omitted out of Y total]" in en
    assert "[OUTPUT TRUNCATED - X chars omitted out of Y total]" in zh

    for fixed in (
        "execute_code",
        "terminal()",
        "from hermes_tools import",
        "hermes_tools.py",
        "handle_function_call",
        "HERMES_HOME",
        "HERMES_PROFILE",
        "HERMES_CONFIG",
        "HERMES_ENV",
        "HERMES_RPC_DIR",
        "HERMES_RPC_SOCKET",
        "HERMES_KANBAN_DB",
        "HERMES_BASE_URL",
        "~/.hermes/config.yaml",
        "~/.hermes/logs/agent.log",
    ):
        assert fixed in en or fixed in zh

    assert "call Hermes tools programmatically" not in en
    assert "调用 Hermes 工具的 Python 脚本" not in zh
    assert "Hermes generates a `hermes_tools.py` stub module" not in en
    assert "Hermes 生成带有 RPC 函数的 `hermes_tools.py` 存根模块" not in zh
    assert "Hermes always writes the script" not in en
    assert "Hermes 始终将脚本和自动生成的 `hermes_tools.py` RPC 存根写入临时暂存目录" not in zh
    assert "`hermes logs --level\nDEBUG`" not in en
    assert "`hermes logs --level DEBUG`" not in en
    assert "`hermes logs --level DEBUG`" not in zh
    assert "Unix domain sockets and is available on **Linux and macOS only**" not in en
    assert "仅在 **Linux 和 macOS** 上可用。在 Windows 上会自动禁用" not in zh
    assert "[output truncated at 50KB]" not in en
    assert "[output truncated at 50KB]" not in zh


def test_kanban_worker_lane_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_KANBAN_WORKER_LANES_DOC.read_text(encoding="utf-8")
    zh = ZH_KANBAN_WORKER_LANES_DOC.read_text(encoding="utf-8")

    assert "non-Doppel service that pulls tasks via the API" in en
    assert "非 Doppel 服务" in zh
    assert "Doppel Kanban =  canonical task lifecycle + audit trail" in en
    assert "Doppel Kanban =  规范的任务生命周期 + 审计追踪" in zh
    assert "`doppel kanban show`" in en
    assert "`doppel kanban show`" in zh
    assert "`doppel kanban tail <task_id>`" in en
    assert "`doppel kanban tail <task_id>`" in zh
    assert "`doppel kanban runs <task_id>`" in en
    assert "`doppel kanban runs <task_id>`" in zh
    assert "### Doppel profile lane (default)" in en
    assert "### Doppel profile 通道（默认）" in zh
    assert "`doppel -p <profile>`" in en
    assert "`doppel -p <profile>`" in zh
    assert "`doppel -p <assignee> chat -q <prompt>`" in en
    assert "`doppel -p <assignee> chat -q <prompt>`" in zh
    assert "`doppel profile list`" in en
    assert "`doppel profile list`" in zh
    assert "`doppel kanban diagnostics`" in en
    assert "`doppel kanban diagnostics`" in zh

    for fixed in (
        "HERMES_KANBAN_TASK",
        "HERMES_KANBAN_DB",
        "HERMES_KANBAN_BOARD",
        "HERMES_KANBAN_WORKSPACES_ROOT",
        "HERMES_KANBAN_WORKSPACE",
        "HERMES_KANBAN_RUN_ID",
        "HERMES_KANBAN_CLAIM_LOCK",
        "HERMES_PROFILE",
        "HERMES_TENANT",
        "kanban_complete",
        "kanban_block",
        "kanban_unblock",
        "kanban_show",
        "KANBAN_GUIDANCE",
        "review-required",
        "dispatch_once",
        "DEFAULT_CLAIM_TTL_SECONDS",
        "[#19931]",
        "PR [#19924]",
    ):
        assert fixed in en or fixed in zh

    assert "non-Hermes service that pulls tasks via the API" not in en
    assert "非 Hermes 服务" not in zh
    assert "Hermes Kanban  =  canonical task lifecycle + audit trail" not in en
    assert "Hermes Kanban  =  规范的任务生命周期 + 审计追踪" not in zh
    assert "`hermes kanban show`" not in en
    assert "`hermes kanban show`" not in zh
    assert "`hermes kanban tail <task_id>`" not in en
    assert "`hermes kanban tail <task_id>`" not in zh
    assert "`hermes kanban runs <task_id>`" not in en
    assert "`hermes kanban runs <task_id>`" not in zh
    assert "### Hermes profile lane (default)" not in en
    assert "### Hermes profile 通道（默认）" not in zh
    assert "`hermes -p <profile>`" not in en
    assert "`hermes -p <profile>`" not in zh
    assert "`hermes -p <assignee> chat -q <prompt>`" not in en
    assert "`hermes -p <assignee> chat -q <prompt>`" not in zh
    assert "`hermes profile list`" not in en
    assert "`hermes profile list`" not in zh
    assert "`hermes kanban diagnostics`" not in en
    assert "`hermes kanban diagnostics`" not in zh


def test_computer_use_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_COMPUTER_USE_DOC.read_text(encoding="utf-8")
    zh = ZH_COMPUTER_USE_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent can drive your Mac's desktop" in en
    assert "Doppel Agent 可以在**后台**驱动你的 Mac 桌面" in zh
    assert "`doppel computer-use install`" in en
    assert "`doppel computer-use install`" in zh
    assert "`doppel computer-use status`" in en
    assert "`doppel computer-use status`" in zh
    assert "`doppel tools`" in en
    assert "`doppel tools`" in zh
    assert "doppel -t computer_use chat" in en
    assert "doppel -t computer_use chat" in zh
    assert "`~/.doppel/config.yaml`" in en
    assert "`~/.doppel/config.yaml`" in zh
    assert "`~/.hermes/config.yaml`" in en
    assert "`~/.hermes/config.yaml`" in zh
    assert "Doppel Agent applies three layers of optimisation" in en
    assert "Doppel Agent 应用三层优化措施" in zh

    for fixed in (
        "`computer_use`",
        "cua-driver",
        "`image_url`",
        "`tool_result`",
        "HERMES_CUA_DRIVER_CMD",
        "HERMES_CUA_DRIVER_VERSION",
        "HERMES_COMPUTER_USE_BACKEND",
        "SLEventPostToPid",
        "_AXObserverAddNotificationAndCheckRemote",
    ):
        assert fixed in en or fixed in zh

    assert "Hermes Agent can drive your Mac's desktop" not in en
    assert "Hermes Agent 可以在**后台**驱动你的 Mac 桌面" not in zh
    assert "`hermes computer-use install`" not in en
    assert "`hermes computer-use install`" not in zh
    assert "`hermes computer-use status`" not in en
    assert "`hermes computer-use status`" not in zh
    assert "`hermes tools`" not in en
    assert "`hermes tools`" not in zh
    assert "hermes -t computer_use chat" not in en
    assert "hermes -t computer_use chat" not in zh
    assert "`hermes update`" not in en
    assert "`hermes update`" not in zh
    assert "context_management" not in en
    assert "context_management" not in zh
    assert "clear_tool_uses_20250919" not in en
    assert "clear_tool_uses_20250919" not in zh


def test_extending_dashboard_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_EXTENDING_DASHBOARD_DOC.read_text(encoding="utf-8")
    zh = ZH_EXTENDING_DASHBOARD_DOC.read_text(encoding="utf-8")

    assert "Build themes and plugins for the Doppel web dashboard" in en
    assert "为 Doppel Web Dashboard 构建主题和插件" in zh
    assert "Doppel Agent's web dashboard (`doppel dashboard`)" in en
    assert "Doppel Agent Web Dashboard（`doppel dashboard`）" in zh
    assert "~/.doppel/dashboard-themes/" in en
    assert "~/.doppel/dashboard-themes/" in zh
    assert "~/.doppel/plugins/my-plugin/" in en
    assert "~/.doppel/plugins/my-plugin/" in zh
    assert "Before the Doppel brand in the top bar." in en
    assert "顶栏 Doppel 品牌之前。" in zh
    assert "restart `doppel dashboard`" in en
    assert "重启 `doppel dashboard`" in zh
    assert "~/.doppel/logs/errors.log" in en
    assert "~/.doppel/logs/errors.log" in zh

    for fixed in (
        "Hermes Teal",
        "data-hermes-theme-css",
        "__HERMES_PLUGIN_SDK__",
        "__HERMES_PLUGINS__",
        "hermes-example-plugins",
        "strike-freedom-cockpit",
        "HERMES_ENABLE_PROJECT_PLUGINS",
        "Legacy installs may still keep the same dashboard themes, plugins, and logs under `~/.hermes`.",
        "旧安装仍可能将相同的 dashboard 主题、插件和日志保存在 `~/.hermes` 下。",
    ):
        assert fixed in en or fixed in zh

    assert "Build themes and plugins for the Hermes web dashboard" not in en
    assert "为 Hermes Web Dashboard 构建主题和插件" not in zh
    assert "The Hermes web dashboard (`hermes dashboard`)" not in en
    assert "Hermes Web Dashboard（`hermes dashboard`）" not in zh
    assert "~/.hermes/dashboard-themes/" not in en
    assert "~/.hermes/dashboard-themes/" not in zh
    assert "~/.hermes/plugins/my-plugin/" not in en
    assert "~/.hermes/plugins/my-plugin/" not in zh
    assert "Before the Hermes brand in the top bar." not in en
    assert "顶栏 Hermes 品牌之前。" not in zh
    assert "restart `hermes dashboard`" not in en
    assert "重启 `hermes dashboard`" not in zh
    assert "~/.hermes/logs/errors.log" not in en
    assert "~/.hermes/logs/errors.log" not in zh


def test_web_dashboard_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_WEB_DASHBOARD_DOC.read_text(encoding="utf-8")
    zh = ZH_WEB_DASHBOARD_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent installation" in en
    assert "Doppel Agent 安装" in zh
    assert "`doppel setup --portal`" in en
    assert "doppel dashboard" in en
    assert "doppel dashboard" in zh
    assert "doppel --tui" in en
    assert "doppel --tui" in zh
    assert "`doppel config set`" in en
    assert "`doppel config set`" in zh
    assert "~/.doppel/skills/" in en
    assert "~/.doppel/skills/" in zh
    assert "~/.doppel/.env" in en
    assert "~/.doppel/.env" in zh
    assert "Doppel Teal" in en
    assert "Doppel Teal" in zh

    for fixed in (
        "hermes-agent[web,pty]",
        "hermes-agent[all]",
        "HERMES_DASHBOARD_TUI",
        "HERMES_DASHBOARD_OAUTH_CLIENT_ID",
        "HERMES_DASHBOARD_PORTAL_URL",
        "HERMES_DASHBOARD_PUBLIC_URL",
        "https://portal.nousresearch.com",
        "hermes_session_at",
        "hermes_session_pkce",
        "hermes_session_rt",
        "hermes_cli/web_dist/",
        "~/.hermes/skills/",
        "~/.hermes/.env",
    ):
        assert fixed in en or fixed in zh

    assert "Hermes Agent installation" not in en
    assert "Hermes Agent 安装" not in zh
    assert "`hermes setup --portal`" not in en
    assert "hermes dashboard --host 0.0.0.0" not in en
    assert "hermes dashboard --host 0.0.0.0" not in zh
    assert "Hermes Teal" not in en
    assert "Hermes Teal" not in zh


def test_skins_docs_prefer_doppel_surfaces_and_match_runtime_defaults():
    en = EN_SKINS_DOC.read_text(encoding="utf-8")
    zh = ZH_SKINS_DOC.read_text(encoding="utf-8")

    assert "Customize the Doppel CLI with built-in and user-defined skins" in en
    assert "使用内置和用户自定义皮肤定制 Doppel CLI 的外观" in zh
    assert "Skins control the **visual presentation** of the Doppel CLI" in en
    assert "皮肤控制 Doppel CLI 的**视觉呈现**" in zh
    assert "~/.doppel/skins/mytheme.yaml" in en
    assert "~/.doppel/skins/mytheme.yaml" in zh
    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/config.yaml" in zh
    assert "| `default` | Classic Doppel — gold and kawaii | `Doppel Agent` |" in en
    assert "| `default` | 经典 Doppel — 金色与 kawaii 风格 | `Doppel Agent` |" in zh
    assert "| `mono` | Monochrome — clean grayscale | `Doppel Agent` |" in en
    assert "| `mono` | 单色 — 简洁灰度 | `Doppel Agent` |" in zh
    assert "| `agent_name` | Name shown in banner title and status display | `Doppel Agent` |" in en
    assert "| `agent_name` | 横幅标题和状态显示中的名称 | `Doppel Agent` |" in zh
    assert "`Welcome to Doppel Agent! Type your message or /help for commands.`" in en
    assert "`Welcome to Doppel Agent! Type your message or /help for commands.`" in zh
    assert "` ⚕ Doppel `" in en
    assert "` ⚕ Doppel `" in zh
    assert "Hermes Mod" in en
    assert "Hermes Mod" in zh
    assert "npx -y hermes-mod" in en
    assert "npx -y hermes-mod" in zh
    assert "HERMES_HOME" in en
    assert "HERMES_HOME" in zh

    assert "Customize the Hermes CLI with built-in and user-defined skins" not in en
    assert "使用内置和用户自定义皮肤定制 Hermes CLI 的外观" not in zh
    assert "| `default` | Classic Hermes — gold and kawaii | `Hermes Agent` |" not in en
    assert "| `default` | 经典 Hermes — 金色与 kawaii 风格 | `Hermes Agent` |" not in zh
    assert "| `agent_name` | Name shown in banner title and status display | `Hermes Agent` |" not in en
    assert "| `agent_name` | 横幅标题和状态显示中的名称 | `Hermes Agent` |" not in zh
    assert "` ⚕ Hermes `" not in en
    assert "` ⚕ Hermes `" not in zh


def test_curator_docs_prefer_doppel_surfaces_and_keep_runtime_literals():
    en = EN_CURATOR_DOC.read_text(encoding="utf-8")
    zh = ZH_CURATOR_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent" in en
    assert "Doppel Agent" in zh
    assert "~/.doppel/skills/" in en
    assert "~/.doppel/skills/" in zh
    assert "~/.doppel/skills/.archive/" in en
    assert "~/.doppel/skills/.archive/" in zh
    assert "~/.doppel/skills/.curator_backups/<utc-iso>/skills.tar.gz" in en
    assert "~/.doppel/skills/.curator_backups/<utc-iso>/skills.tar.gz" in zh
    assert "~/.doppel/skills/.usage.json" in en
    assert "~/.doppel/skills/.usage.json" in zh
    assert "~/.doppel/logs/curator/" in en
    assert "~/.doppel/logs/curator/" in zh
    assert "`doppel update`" in en
    assert "`doppel update`" in zh
    assert "`doppel curator run --dry-run`" in en
    assert "`doppel curator run --dry-run`" in zh
    assert "`doppel model`" in en
    assert "`doppel model`" in zh
    assert "doppel curator status" in en
    assert "doppel curator status" in zh
    assert "doppel curator backup" in en
    assert "doppel curator backup" in zh
    assert "doppel curator rollback" in en
    assert "doppel curator rollback" in zh
    assert "doppel curator pin <name>" in en
    assert "doppel curator pin <name>" in zh
    assert "doppel curator restore <name>" in en
    assert "doppel curator restore <name>" in zh
    assert "Legacy installs may still keep the same tree under `~/.hermes/skills/`." in en
    assert "旧安装仍可能将同样的目录树保留在 `~/.hermes/skills/` 下。" in zh

    for fixed in (
        "AIAgent",
        "skill_view",
        "skill_manage",
        "curator.auxiliary.{provider,model}",
        "agentskills.io",
        "Issue #7816",
        "NousResearch/hermes-agent/issues/7816",
    ):
        assert fixed in en or fixed in zh

    assert "`hermes update`" not in en
    assert "`hermes update`" not in zh
    assert "`hermes curator run --dry-run`" not in en
    assert "`hermes curator run --dry-run`" not in zh
    assert "`hermes model`" not in en
    assert "`hermes model`" not in zh
    assert "hermes curator status" not in en
    assert "hermes curator status" not in zh
    assert "hermes curator backup" not in en
    assert "hermes curator backup" not in zh
    assert "hermes curator rollback" not in en
    assert "hermes curator rollback" not in zh
    assert "hermes curator pin <name>" not in en
    assert "hermes curator pin <name>" not in zh
    assert "hermes curator restore <name>" not in en
    assert "hermes curator restore <name>" not in zh


def test_security_docs_prefer_doppel_customer_facing_wording_and_preserve_runtime_literals():
    en = EN_SECURITY_DOC.read_text(encoding="utf-8")
    zh = ZH_SECURITY_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent is designed with a defense-in-depth security model." in en
    assert "Doppel Agent 采用纵深防御安全模型" in zh
    assert "Hermes Agent 采用纵深防御安全模型" not in zh

    assert "doppel --yolo" in en
    assert "doppel --yolo" in zh
    assert "doppel pairing approve" in en
    assert "doppel pairing approve" in zh
    assert "doppel doctor" in en
    assert "doppel doctor" in zh
    assert "doppel update" in en
    assert "doppel update" in zh

    assert "hermes --yolo" not in en
    assert "hermes --yolo" not in zh
    assert "hermes pairing approve" not in en
    assert "hermes pairing approve" not in zh
    assert "hermes doctor" not in en
    assert "hermes doctor" not in zh
    assert "hermes update" not in en
    assert "hermes update" not in zh

    for fixed in (
        "approvals.mode",
        "HERMES_YOLO_MODE=1",
        "HERMES_EXEC_ASK=1",
        "HERMES_HOME",
        "tools/approval.py::UNRECOVERABLE_BLOCKLIST",
        "tools/credential_files.py",
        "/etc/hermes/blocked-sites.txt",
        "hermes_cli/security_advisories.py",
        "tools/lazy_deps.py",
        "config.security.acked_advisories",
        "~/.hermes/.env",
        "~/.hermes/config.yaml",
    ):
        assert fixed in en
        assert fixed in zh

    assert "~/.doppel/config.yaml" in en
    assert "~/.doppel/.env" in en
    assert "legacy `~/.hermes/config.yaml`" in en
    assert "legacy `~/.hermes/.env`" in en

    assert "~/.doppel/config.yaml" in zh
    assert "~/.doppel/.env" in zh
    assert "~/.doppel/pairing/" in zh
    assert "~/.doppel/logs/" in zh
    assert "doppel config edit" in zh


def test_environment_variable_reference_prefers_doppel_aliases_for_core_cli_surface():
    en = EN_ENVIRONMENT_VARIABLES_DOC.read_text(encoding="utf-8")
    zh = ZH_ENVIRONMENT_VARIABLES_DOC.read_text(encoding="utf-8")

    assert "All variables go in `~/.doppel/.env`." in en
    assert "You can also set them with `doppel config set VAR value`." in en
    assert "所有变量均写入 `~/.doppel/.env`。" in zh
    assert "也可以使用 `doppel config set VAR value` 进行设置。" in zh

    en_provider = en.split("## LLM Providers", 1)[1].split("## Provider Auth (OAuth)", 1)[0]
    zh_provider = zh.split("## LLM 提供商", 1)[1].split("## 提供商认证（OAuth）", 1)[0]
    en_agent = en.split("## Agent Behavior", 1)[1].split("## Interface", 1)[0]
    zh_agent = zh.split("## Agent 行为", 1)[1].split("## 界面", 1)[0]
    en_interface = en.split("## Interface", 1)[1].split("## Session Settings", 1)[0]
    zh_interface = zh.split("## 界面", 1)[1].split("## 会话设置", 1)[0]

    assert "`DOPPEL_MODEL`" in en_provider
    assert "`DOPPEL_MODEL`" in zh_provider
    assert "`DOPPEL_HOME`" in en_provider
    assert "`DOPPEL_HOME`" in zh_provider
    for preferred in (
        "`DOPPEL_OPENROUTER_CACHE`",
        "`DOPPEL_OPENROUTER_CACHE_TTL`",
        "`DOPPEL_COPILOT_ACP_COMMAND`",
        "`DOPPEL_COPILOT_ACP_ARGS`",
        "`DOPPEL_GEMINI_CLIENT_ID`",
        "`DOPPEL_GEMINI_CLIENT_SECRET`",
        "`DOPPEL_GEMINI_PROJECT_ID`",
        "`DOPPEL_QWEN_BASE_URL`",
    ):
        assert preferred in en_provider
        assert preferred in zh_provider
    assert "| `HERMES_MODEL` |" not in en_provider
    assert "| `HERMES_MODEL` |" not in zh_provider
    assert "| `HERMES_HOME` |" not in en_provider
    assert "| `HERMES_HOME` |" not in zh_provider
    for legacy in (
        "| `HERMES_OPENROUTER_CACHE` |",
        "| `HERMES_OPENROUTER_CACHE_TTL` |",
        "| `HERMES_COPILOT_ACP_COMMAND` |",
        "| `HERMES_COPILOT_ACP_ARGS` |",
        "| `HERMES_GEMINI_CLIENT_ID` |",
        "| `HERMES_GEMINI_CLIENT_SECRET` |",
        "| `HERMES_GEMINI_PROJECT_ID` |",
        "| `HERMES_QWEN_BASE_URL` |",
    ):
        assert legacy not in en_provider
        assert legacy not in zh_provider

    for preferred in (
        "`DOPPEL_MAX_ITERATIONS`",
        "`DOPPEL_INFERENCE_MODEL`",
        "`DOPPEL_YOLO_MODE`",
        "`DOPPEL_ACCEPT_HOOKS`",
        "`DOPPEL_IGNORE_USER_CONFIG`",
        "`DOPPEL_IGNORE_RULES`",
        "`DOPPEL_QUIET`",
        "`DOPPEL_EPHEMERAL_SYSTEM_PROMPT`",
        "`DOPPEL_REDACT_SECRETS`",
    ):
        assert preferred in en_agent
        assert preferred in zh_agent

    for legacy_row in (
        "| `HERMES_MAX_ITERATIONS` |",
        "| `HERMES_INFERENCE_MODEL` |",
        "| `HERMES_YOLO_MODE` |",
        "| `HERMES_ACCEPT_HOOKS` |",
        "| `HERMES_IGNORE_USER_CONFIG` |",
        "| `HERMES_IGNORE_RULES` |",
        "| `HERMES_QUIET` |",
        "| `HERMES_EPHEMERAL_SYSTEM_PROMPT` |",
        "| `HERMES_REDACT_SECRETS` |",
    ):
        assert legacy_row not in en_agent
        assert legacy_row not in zh_agent

    for preferred in (
        "`DOPPEL_TUI`",
        "`DOPPEL_TUI_DIR`",
        "`DOPPEL_TUI_RESUME`",
        "`DOPPEL_TUI_THEME`",
    ):
        assert preferred in en_interface
        assert preferred in zh_interface

    assert "legacy `HERMES_" not in en_agent
    assert "Legacy `HERMES_" not in en_interface
    assert "旧版 `HERMES_" not in zh_agent
    assert "旧版 `HERMES_" not in zh_interface

    for legacy_row in (
        "| `HERMES_TUI` |",
        "| `HERMES_TUI_DIR` |",
        "| `HERMES_TUI_RESUME` |",
        "| `HERMES_TUI_THEME` |",
    ):
        assert legacy_row not in en_interface
        assert legacy_row not in zh_interface


def test_reference_faq_uses_doppel_model_name_only():
    en = EN_REFERENCE_FAQ_DOC.read_text(encoding="utf-8")
    zh = ZH_REFERENCE_FAQ_DOC.read_text(encoding="utf-8")

    assert "doppel config set DOPPEL_MODEL anthropic/claude-opus-4.7" in en
    assert "doppel config set DOPPEL_MODEL anthropic/claude-opus-4.7" in zh
    assert "HERMES_MODEL" not in en
    assert "HERMES_MODEL" not in zh


def test_reference_faq_profiles_section_prefers_doppel_home_wording():
    en = EN_REFERENCE_FAQ_DOC.read_text(encoding="utf-8")
    zh = ZH_REFERENCE_FAQ_DOC.read_text(encoding="utf-8")

    en_profiles = en.split("## Profiles", 1)[1].split("## Workflows & Patterns", 1)[0]
    zh_profiles = zh.split("## Profiles（配置文件）", 1)[1].split("## 工作流与模式", 1)[0]

    assert "How do profiles differ from just setting `DOPPEL_HOME`?" in en_profiles
    assert "You *could* manually set `DOPPEL_HOME=/some/path` before every command" in en_profiles
    assert "older installs may still use the legacy home layout" in en_profiles
    assert "How do profiles differ from just setting `DOPPEL_HOME` or `HERMES_HOME`?" not in en_profiles
    assert "legacy `HERMES_HOME`" not in en_profiles
    assert "~/.hermes/active_profile" not in en_profiles

    assert "Profiles 与直接设置 `DOPPEL_HOME` 有何不同？" in zh_profiles
    assert "您*可以*在每次命令前手动设置 `DOPPEL_HOME=/some/path`" in zh_profiles
    assert "旧安装仍可能使用旧版主目录布局" in zh_profiles
    assert "Profiles 与直接设置 `DOPPEL_HOME` 或 `HERMES_HOME` 有何不同？" not in zh_profiles
    assert "旧版兼容的 `HERMES_HOME`" not in zh_profiles
    assert "~/.hermes/active_profile" not in zh_profiles


def test_reference_faq_prefers_doppel_timeout_and_home_paths():
    en = EN_REFERENCE_FAQ_DOC.read_text(encoding="utf-8")
    zh = ZH_REFERENCE_FAQ_DOC.read_text(encoding="utf-8")

    en_cluster = en.split("### What LLM providers work with Doppel?", 1)[1].split(
        "### How much does it cost?", 1
    )[0]
    zh_cluster = zh.split("### Doppel 支持哪些 LLM 提供商？", 1)[1].split(
        "### 费用是多少？", 1
    )[0]
    en_troubleshooting = en.split("### Installation Issues", 1)[1].split(
        "### Provider & Model Issues", 1
    )[0]
    zh_troubleshooting = zh.split("### 安装问题", 1)[1].split(
        "### 提供商与模型问题", 1
    )[0]
    en_export = en.split("### Exporting Doppel to another machine", 1)[1].split(
        "### Moving a single profile to another machine", 1
    )[0]
    zh_export = zh.split("### 将 Doppel 迁移到另一台机器", 1)[1].split(
        "### 将单个 profile 迁移到另一台机器", 1
    )[0]

    assert "older installs may still keep the legacy home layout" in en_cluster
    assert "旧安装仍可能保留旧版主目录布局" in zh_cluster
    assert "DOPPEL_STREAM_READ_TIMEOUT=1800" in en_cluster
    assert "DOPPEL_STREAM_READ_TIMEOUT=1800" in zh_cluster
    assert "~/.hermes" not in en_cluster
    assert "~/.hermes" not in zh_cluster
    assert "HERMES_STREAM_READ_TIMEOUT" not in en_cluster
    assert "HERMES_STREAM_READ_TIMEOUT" not in zh_cluster

    assert "usually `~/.doppel/config.yaml`" in en_troubleshooting
    assert "`~/.doppel/config.yaml` 中列出需要额外 source 的文件" in zh_troubleshooting
    assert "~/.hermes/config.yaml" not in en_troubleshooting
    assert "~/.hermes/config.yaml" not in zh_troubleshooting

    assert "older installs keeping their legacy home layout in place" in en_export
    assert "旧安装则可能继续保留旧版主目录布局" in zh_export
    assert "~/doppel-backup-<timestamp>.zip" in en_export
    assert "~/doppel-backup-<timestamp>.zip" in zh_export
    assert "cd ~/.doppel/doppel-agent && uv pip install -e \".[messaging]\"" in en
    assert "cd ~/.doppel/doppel-agent && uv pip install -e \".[messaging]\"" in zh
    assert "~/.hermes/" not in en_export
    assert "~/.hermes/" not in zh_export
    assert "~/hermes-backup-<timestamp>.zip" not in en_export
    assert "~/hermes-backup-<timestamp>.zip" not in zh_export


def test_reference_cli_commands_active_home_examples_stay_doppel_first():
    en = (REPO_ROOT / "website" / "docs" / "reference" / "cli-commands.md").read_text(
        encoding="utf-8"
    )
    zh = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "reference"
        / "cli-commands.md"
    ).read_text(encoding="utf-8")

    en_top = en.split("## `doppel chat`", 1)[0]
    zh_top = zh.split("## `doppel chat`", 1)[0]
    en_gateway = en.split("## `doppel gateway`", 1)[1].split("## `doppel lsp`", 1)[0]
    zh_gateway = zh.split("## `doppel gateway`", 1)[1].split("## `doppel lsp`", 1)[0]
    en_slack = en.split("## `doppel slack`", 1)[1].split("## `doppel login`", 1)[0]
    zh_slack = zh.split("## `doppel slack`", 1)[1].split("## `doppel login`", 1)[0]
    en_update = en.split("## `doppel update`", 1)[1].split("## Maintenance commands", 1)[0]
    zh_update = zh.split("## `doppel update`", 1)[1].split("## 维护命令", 1)[0]

    assert "takes a pre-pull snapshot of the active agent home" in en_top
    assert "为当前智能体主目录创建快照" in zh_top
    assert "legacy `HERMES_HOME`" not in en_top
    assert "旧版 `HERMES_HOME`" not in zh_top

    assert "not just the active agent home" in en_gateway
    assert "而不仅限于当前智能体主目录" in zh_gateway
    assert "legacy `HERMES_HOME` still works" not in en_gateway
    assert "兼容旧版 `HERMES_HOME`" not in zh_gateway

    assert "Bare `--write` writes `$DOPPEL_HOME/slack-manifest.json`." in en_slack
    assert "裸 `--write` 写入 `$DOPPEL_HOME/slack-manifest.json`。" in zh_slack
    assert "legacy `$HERMES_HOME`" not in en_slack
    assert "旧版 `$HERMES_HOME`" not in zh_slack

    assert "Create a labeled pre-update snapshot of the active agent home before pulling." in en_update
    assert "在拉取前为当前智能体主目录创建带标签的预更新快照" in zh_update
    assert "with legacy `HERMES_HOME` still honored" not in en_update
    assert "兼容旧版 `HERMES_HOME`" not in zh_update


def test_reference_slash_commands_prefer_doppel_customer_wording():
    en = EN_REFERENCE_SLASH_COMMANDS_DOC.read_text(encoding="utf-8")
    zh = ZH_REFERENCE_SLASH_COMMANDS_DOC.read_text(encoding="utf-8")

    assert "Doppel Agent has two slash-command surfaces" in en
    assert "Doppel Agent acknowledges the ping silently" in en
    assert "Doppel Agent works toward across turns" in en
    assert "Create or restore state snapshots of Doppel config/state." in en
    assert "run `doppel model` from your terminal" in en
    assert "The full `doppel kanban` surface is available" in en
    assert "Re-scan `~/.doppel/skills/`" in en
    assert "your agent-home `config.yaml` (usually `~/.doppel/config.yaml`)" in en
    assert "doppel config set model.aliases.fav anthropic/claude-opus-4.6" in en
    assert "Update Doppel Agent to the latest version." in en
    assert "`doppel --tui --resume <id-or-title>`" in en
    assert "command: doppel gateway status" in en

    assert "Hermes has two slash-command surfaces" not in en
    assert "Hermes config/state" not in en
    assert "run `hermes model` from your terminal" not in en
    assert "Full `hermes kanban` surface is available" not in en
    assert "Re-scan `~/.hermes/skills/`" not in en
    assert "Configure them in `~/.hermes/config.yaml`" not in en
    assert "hermes config set model.aliases.fav anthropic/claude-opus-4.6" not in en
    assert "Update Hermes Agent to the latest version." not in en
    assert "`hermes --tui --resume <id-or-title>`" not in en
    assert "command: systemctl status hermes-agent" not in en

    assert "Doppel Agent 有两个斜杠命令入口" in zh
    assert "创建或恢复 Doppel 配置/状态的快照" in zh
    assert "Doppel Agent 将跨轮次持续推进" in zh
    assert "在终端运行 `doppel model`" in zh
    assert "完整的 `doppel kanban` 命令面均可用" in zh
    assert "重新扫描 `~/.doppel/skills/`" in zh
    assert "agent-home 的 `config.yaml`（通常是 `~/.doppel/config.yaml`）" in zh
    assert "doppel config set model.aliases.fav anthropic/claude-opus-4.6" in zh
    assert "将 Doppel Agent 更新到最新版本" in zh
    assert "command: doppel gateway status" in zh

    assert "Hermes 有两个斜杠命令入口" not in zh
    assert "创建或恢复 Hermes 配置/状态的快照" not in zh
    assert "Hermes 将跨轮次持续推进" not in zh
    assert "在终端运行 `hermes model`" not in zh
    assert "完整的 `hermes kanban` 命令面均可用" not in zh
    assert "重新扫描 `~/.hermes/skills/`" not in zh
    assert "在 `~/.hermes/config.yaml` 中配置" not in zh
    assert "hermes config set model.aliases.fav anthropic/claude-opus-4.6" not in zh
    assert "将 Hermes Agent 更新到最新版本" not in zh
    assert "command: systemctl status hermes-agent" not in zh


def test_environment_variable_reference_prefers_doppel_stream_timeout_alias():
    en = EN_ENVIRONMENT_VARIABLES_DOC.read_text(encoding="utf-8")
    zh = ZH_ENVIRONMENT_VARIABLES_DOC.read_text(encoding="utf-8")

    assert "| `DOPPEL_STREAM_READ_TIMEOUT` |" in en
    assert "| `DOPPEL_STREAM_READ_TIMEOUT` |" in zh
    assert "| `HERMES_STREAM_READ_TIMEOUT` |" not in en
    assert "| `HERMES_STREAM_READ_TIMEOUT` |" not in zh
    for preferred in (
        "DOPPEL_NOUS_TIMEOUT_SECONDS",
        "DOPPEL_TELEGRAM_HTTP_CONNECT_TIMEOUT",
        "DOPPEL_VISION_DOWNLOAD_TIMEOUT",
        "DOPPEL_RESTART_DRAIN_TIMEOUT",
        "DOPPEL_GATEWAY_PLATFORM_CONNECT_TIMEOUT",
        "DOPPEL_CRON_TIMEOUT",
        "DOPPEL_CRON_SCRIPT_TIMEOUT",
        "DOPPEL_API_TIMEOUT",
        "DOPPEL_API_CALL_STALE_TIMEOUT",
        "DOPPEL_STREAM_STALE_TIMEOUT",
        "DOPPEL_AGENT_TIMEOUT",
        "DOPPEL_AGENT_TIMEOUT_WARNING",
        "DOPPEL_CHECKPOINT_TIMEOUT",
    ):
        assert preferred in en
        assert preferred in zh

    for preferred in (
        "DOPPEL_OPENROUTER_CACHE",
        "DOPPEL_OPENROUTER_CACHE_TTL",
        "DOPPEL_COPILOT_ACP_COMMAND",
        "DOPPEL_COPILOT_ACP_ARGS",
        "DOPPEL_GEMINI_CLIENT_ID",
        "DOPPEL_GEMINI_CLIENT_SECRET",
        "DOPPEL_GEMINI_PROJECT_ID",
        "DOPPEL_QWEN_BASE_URL",
        "DOPPEL_PORTAL_BASE_URL",
        "DOPPEL_NOUS_MIN_KEY_TTL_SECONDS",
        "DOPPEL_LOCAL_STT_COMMAND",
        "DOPPEL_LOCAL_STT_LANGUAGE",
        "DOPPEL_TIMEZONE",
        "DOPPEL_DOCKER_BINARY",
    ):
        assert preferred in en
        assert preferred in zh

    for legacy in (
        "| `HERMES_OPENROUTER_CACHE` |",
        "| `HERMES_OPENROUTER_CACHE_TTL` |",
        "| `HERMES_COPILOT_ACP_COMMAND` |",
        "| `HERMES_COPILOT_ACP_ARGS` |",
        "| `HERMES_GEMINI_CLIENT_ID` |",
        "| `HERMES_GEMINI_CLIENT_SECRET` |",
        "| `HERMES_GEMINI_PROJECT_ID` |",
        "| `HERMES_QWEN_BASE_URL` |",
        "| `HERMES_PORTAL_BASE_URL` |",
        "| `HERMES_NOUS_MIN_KEY_TTL_SECONDS` |",
        "| `HERMES_LOCAL_STT_COMMAND` |",
        "| `HERMES_LOCAL_STT_LANGUAGE` |",
        "| `HERMES_TIMEZONE` |",
        "| `HERMES_DOCKER_BINARY` |",
    ):
        assert legacy not in en
        assert legacy not in zh


def test_zh_environment_variable_reference_rebrands_remaining_doppel_prose():
    zh = ZH_ENVIRONMENT_VARIABLES_DOC.read_text(encoding="utf-8")

    for updated in (
        "Doppel 使用 MiniMax 的 Anthropic Messages 兼容端点",
        "共享 Doppel 根目录",
        "Doppel 在 Claude Code 自身凭证文件存在时优先使用",
        "Doppel 自动注入 `--no-sandbox,--disable-dev-shm-usage`",
        "在 `~/.doppel/.env` 中设置",
        "`doppel plugins enable observability/langfuse`",
        "`doppel model` 或 `doppel tools`",
        "覆盖 Doppel 调用的容器二进制",
        "控制 Doppel 何时清理空闲终端会话",
        "`~/.doppel/sandboxes/`",
        "远程 Doppel API 服务器 URL",
        "存储在 `~/.doppel/.env` 中并设置 `chmod 600`",
        "运行 `doppel gateway run` 时跳过 s6 自动监管",
        "Doppel 附加一个建议列表",
        "Doppel 的迁移将托管块写入 `<CODEX_HOME>/config.toml`",
        "自动导出到 Doppel 生成的每个工具子进程",
        "对于特定任务的直接端点，Doppel 使用",
        "这些配置写入 `~/.doppel/config.yaml` 的 `provider_routing` 部分",
    ):
        assert updated in zh

    for stale in (
        "Hermes 使用 MiniMax 的 Anthropic Messages 兼容端点",
        "共享 Hermes 根目录",
        "Hermes 在 Claude Code 自身凭证文件存在时优先使用",
        "Hermes 自动注入 `--no-sandbox,--disable-dev-shm-usage`",
        "hermes plugins enable observability/langfuse",
        "`hermes model` 或 `hermes tools`",
        "覆盖 Hermes 调用的容器二进制",
        "控制 Hermes 何时清理空闲终端会话",
        "`~/.hermes/sandboxes/`",
        "远程 Hermes API 服务器 URL",
        "运行 `hermes gateway run` 时跳过 s6 自动监管",
        "Hermes 附加一个建议列表",
        "Hermes 的迁移将托管块写入 `<CODEX_HOME>/config.toml`",
        "自动导出到 Hermes 生成的每个工具子进程",
        "对于特定任务的直接端点，Hermes 使用",
        "这些配置写入 `~/.hermes/config.yaml` 的 `provider_routing` 部分",
    ):
        assert stale not in zh
