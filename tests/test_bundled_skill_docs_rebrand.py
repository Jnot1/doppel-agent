from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
EN_LINEAR = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "bundled"
    / "productivity"
    / "productivity-linear.md"
)
EN_SPOTIFY = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "bundled"
    / "media"
    / "media-spotify.md"
)
EN_GIF = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "bundled"
    / "media"
    / "media-gif-search.md"
)
ZH_LINEAR = (
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
    / "productivity-linear.md"
)
ZH_SPOTIFY = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "skills"
    / "bundled"
    / "media"
    / "media-spotify.md"
)
ZH_GIF = (
    REPO_ROOT
    / "website"
    / "i18n"
    / "zh-Hans"
    / "docusaurus-plugin-content-docs"
    / "current"
    / "user-guide"
    / "skills"
    / "bundled"
    / "media"
    / "media-gif-search.md"
)


def test_bundled_skill_docs_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (EN_LINEAR, EN_SPOTIFY, EN_GIF, ZH_LINEAR, ZH_SPOTIFY, ZH_GIF)
    )

    expected = (
        "Set `LINEAR_API_KEY` in your environment (via `doppel setup` or your env config)",
        'SCRIPT="${DOPPEL_HOME:-$HOME/.doppel}/skills/productivity/linear/scripts/linear_api.py"',
        "Control the user's Spotify account via the Doppel Spotify toolset (7 tools).",
        "Tell the user to run `doppel auth spotify` again.",
        "Set your Tenor API key in your environment (add to `~/.doppel/.env`):",
        "| 作者 | Doppel Agent |",
        "以下是 Doppel 在触发此 skill 时加载的完整 skill 定义。",
        "以下是 Doppel 在触发该 skill 时加载的完整 skill 定义。",
        "在环境中设置 `LINEAR_API_KEY`（通过 `doppel setup` 或你的环境配置）",
        "通过 Doppel Spotify 工具集（7 个工具）控制用户的 Spotify 账户。",
        "告知用户重新运行 `doppel auth spotify`。",
        "在环境中设置 Tenor API 密钥（添加到 `~/.doppel/.env`）：",
        "- GIF URL 可直接用于 markdown：`![alt](url)`",
    )
    stale = (
        "Set `LINEAR_API_KEY` in your environment (via `hermes setup` or your env config)",
        "find ~/.hermes -path '*skills/productivity/linear/scripts/linear_api.py'",
        "Control the user's Spotify account via the Hermes Spotify toolset (7 tools).",
        "Tell the user to run `hermes auth spotify` again.",
        "Set your Tenor API key in your environment (add to `~/.hermes/.env`):",
        "| 作者 | Hermes Agent |",
        "以下是 Hermes 在触发此 skill 时加载的完整 skill 定义。",
        "以下是 Hermes 在触发该 skill 时加载的完整 skill 定义。",
        "在环境中设置 `LINEAR_API_KEY`（通过 `hermes setup` 或你的环境配置）",
        "通过 Hermes Spotify 工具集（7 个工具）控制用户的 Spotify 账户。",
        "告知用户重新运行 `hermes auth spotify`。",
        "在环境中设置 Tenor API 密钥（添加到 `~/.hermes/.env`）：",
        "https://github.com/NousResearch/hermes-agent/blob/main/skills/media/gif-search/url",
        "https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
