from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
GATEWAY_DOC = REPO_ROOT / "website" / "docs" / "developer-guide" / "gateway-internals.md"
MODEL_PROVIDER_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "model-provider-plugin.md"
)
VIDEO_GEN_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "video-gen-provider-plugin.md"
)
WEB_SEARCH_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "web-search-provider-plugin.md"
)
PLATFORM_ADAPTERS_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "adding-platform-adapters.md"
)
ARCHITECTURE_DOC = REPO_ROOT / "website" / "docs" / "developer-guide" / "architecture.md"
IMAGE_GEN_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "image-gen-provider-plugin.md"
)
CREATING_SKILLS_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "creating-skills.md"
)
PLUGIN_LLM_ACCESS_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "plugin-llm-access.md"
)
EXTENDING_CLI_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "extending-the-cli.md"
)
AGENT_LOOP_DOC = REPO_ROOT / "website" / "docs" / "developer-guide" / "agent-loop.md"


def test_developer_docs_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            GATEWAY_DOC,
            MODEL_PROVIDER_DOC,
            VIDEO_GEN_DOC,
            WEB_SEARCH_DOC,
            PLATFORM_ADAPTERS_DOC,
            ARCHITECTURE_DOC,
            IMAGE_GEN_DOC,
            CREATING_SKILLS_DOC,
            PLUGIN_LLM_ACCESS_DOC,
            EXTENDING_CLI_DOC,
            AGENT_LOOP_DOC,
        )
    )

    expected = (
        "| `~/.doppel/.env` | API keys, bot tokens, platform credentials |",
        "| `~/.doppel/config.yaml` | Model settings, tool configuration, display options |",
        "and `~/.doppel/hooks/` (user-installed).",
        "PID file at `~/.doppel/gateway.pid` — profile-scoped process tracking",
        "Create `~/.doppel/plugins/model-providers/gmi/__init__.py`:",
        "2. **User** — `~/.doppel/plugins/video_gen/<name>/` (opt-in via `plugins.enabled`)",
        "2. **User** — `~/.doppel/plugins/web/<name>/` (opt-in via `plugins.enabled` or `doppel plugins enable <name>`)",
        "# ~/.doppel/config.yaml",
        "Drop a plugin directory into `~/.doppel/plugins/`",
        "~/.doppel/plugins/my-platform/",
        "dropping env vars into `~/.doppel/.env` rather than editing `config.yaml`",
        "Three discovery sources: `~/.doppel/plugins/` (user), `.doppel/plugins/` (project), and pip entry points.",
        "2. **User** — `~/.doppel/plugins/image_gen/<name>/` (opt-in via `plugins.enabled`)",
        "User plugins at `~/.doppel/plugins/image_gen/<name>/`",
        "save under $DOPPEL_HOME/cache/images/ via save_b64_image()",
        "it writes to `$DOPPEL_HOME/cache/images/<prefix>_<timestamp>_<uuid>.<ext>`",
        "export DOPPEL_HOME=/tmp/doppel-imggen-test",
        "mkdir -p $DOPPEL_HOME/plugins/image_gen/my-backend",
        'echo "image_gen:" >> $DOPPEL_HOME/config.yaml',
        "[Skill config (from ~/.doppel/config.yaml):",
        "stored in `~/.doppel/.env`, never shown to the model",
        "file path relative to `~/.doppel/`",
        "strings stored in `~/.doppel/.env`",
        "`doppel model` and config.yaml model.provider).",
        "`~/.doppel/auth.json` / env, including the credential pool when",
        "cd ~/doppel-agent",
        "The session can be resumed later via `/resume` or `doppel chat --resume`",
    )
    stale = (
        "| `~/.hermes/.env` | API keys, bot tokens, platform credentials |",
        "| `~/.hermes/config.yaml` | Model settings, tool configuration, display options |",
        "and `~/.hermes/hooks/` (user-installed).",
        "PID file at `~/.hermes/gateway.pid` — profile-scoped process tracking",
        "Create `~/.hermes/plugins/model-providers/gmi/__init__.py`:",
        "2. **User** — `~/.hermes/plugins/video_gen/<name>/` (opt-in via `plugins.enabled`)",
        "2. **User** — `~/.hermes/plugins/web/<name>/` (opt-in via `plugins.enabled` or `doppel plugins enable <name>`)",
        "# ~/.hermes/config.yaml",
        "Drop a plugin directory into `~/.hermes/plugins/`",
        "~/.hermes/plugins/my-platform/",
        "dropping env vars into `~/.hermes/.env` rather than editing `config.yaml`",
        "Three discovery sources: `~/.hermes/plugins/` (user), `.hermes/plugins/` (project), and pip entry points.",
        "2. **User** — `~/.hermes/plugins/image_gen/<name>/` (opt-in via `plugins.enabled`)",
        "User plugins at `~/.hermes/plugins/image_gen/<name>/`",
        "save under $HERMES_HOME/cache/images/ via save_b64_image()",
        "it writes to `$HERMES_HOME/cache/images/<prefix>_<timestamp>_<uuid>.<ext>`",
        "export HERMES_HOME=/tmp/hermes-imggen-test",
        "mkdir -p $HERMES_HOME/plugins/image_gen/my-backend",
        'echo "image_gen:" >> $HERMES_HOME/config.yaml',
        "[Skill config (from ~/.hermes/config.yaml):",
        "stored in `~/.hermes/.env`, never shown to the model",
        "file path relative to `~/.hermes/`",
        "strings stored in `~/.hermes/.env`",
        "`hermes model` and config.yaml model.provider).",
        "`~/.hermes/auth.json` / env, including the credential pool when",
        "cd ~/.hermes/hermes-agent",
        "The session can be resumed later via `/resume` or `hermes chat --resume`",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
