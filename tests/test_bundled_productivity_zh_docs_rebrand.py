from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
AIRTABLE = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "skills"
    / "bundled"
    / "productivity"
    / "productivity-airtable.md"
)
GOOGLE_WORKSPACE = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "skills"
    / "bundled"
    / "productivity"
    / "productivity-google-workspace.md"
)
NOTION = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "skills"
    / "bundled"
    / "productivity"
    / "productivity-notion.md"
)


def test_bundled_productivity_zh_docs_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (AIRTABLE, GOOGLE_WORKSPACE, NOTION)
    )

    expected = (
        "以下是 Doppel 在触发此 skill 时加载的完整 skill 定义。",
        "将令牌存储在 `~/.doppel/.env` 中（或通过 `doppel setup` 配置）：",
        "以确保工具输出对 Doppel 保持整洁。",
        "## Doppel 典型工作流",
        "## Doppel 重要说明",
        "自动从 `~/.doppel/.env` 注入到子进程环境中",
        "通过 Doppel 管理的 OAuth（开放授权）和轻量 CLI 封装器实现。",
        "同时保留 Doppel 现有的 JSON 输出契约。",
        'GSETUP="python ${DOPPEL_HOME:-$HOME/.doppel}/skills/productivity/google-workspace/scripts/setup.py"',
        "> Doppel CLI 重要提示：",
        "~/Downloads/doppel-google-client-secret.json",
        "保存至 `~/.doppel/google_oauth_last_url.txt`",
        "Token 存储于 `~/.doppel/google_token.json`",
        "临时存储于 `~/.doppel/google_oauth_pending.json`",
        "`~/.doppel/google_token.json` 凭据文件",
        'GAPI="python ${DOPPEL_HOME:-$HOME/.doppel}/skills/productivity/google-workspace/scripts/google_api.py"',
        "3. 存储到 `~/.doppel/.env`：",
        "将上述 export 添加到你的 shell 配置文件（或 `~/.doppel/.env`）",
        '"Hello from Doppel!"',
        "可通过 Doppel 的 MCP 支持接入",
    )
    stale = (
        "以下是 Hermes 在触发此 skill 时加载的完整 skill 定义。",
        "将令牌存储在 `~/.hermes/.env` 中（或通过 `hermes setup` 配置）：",
        "以确保工具输出对 Hermes 保持整洁。",
        "## Hermes 典型工作流",
        "## Hermes 重要说明",
        "自动从 `~/.hermes/.env` 注入到子进程环境中",
        "通过 Hermes 管理的 OAuth（开放授权）和轻量 CLI 封装器实现。",
        "同时保留 Hermes 现有的 JSON 输出契约。",
        'GSETUP="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/setup.py"',
        "> Hermes CLI 重要提示：",
        "~/Downloads/hermes-google-client-secret.json",
        "保存至 `~/.hermes/google_oauth_last_url.txt`",
        "Token 存储于 `~/.hermes/google_token.json`",
        "临时存储于 `~/.hermes/google_oauth_pending.json`",
        "`~/.hermes/google_token.json` 凭据文件",
        'GAPI="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/google_api.py"',
        "3. 存储到 `~/.hermes/.env`：",
        "将上述 export 添加到你的 shell 配置文件（或 `~/.hermes/.env`）",
        '"Hello from Hermes!"',
        "可通过 Hermes 的 MCP 支持接入",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
