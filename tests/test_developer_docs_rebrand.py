from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
GATEWAY_DOC = REPO_ROOT / "website" / "docs" / "developer-guide" / "gateway-internals.md"
MODEL_PROVIDER_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "model-provider-plugin.md"
)
VIDEO_GEN_DOC = (
    REPO_ROOT / "website" / "docs" / "developer-guide" / "video-gen-provider-plugin.md"
)


def test_developer_docs_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (GATEWAY_DOC, MODEL_PROVIDER_DOC, VIDEO_GEN_DOC)
    )

    expected = (
        "| `~/.doppel/.env` | API keys, bot tokens, platform credentials |",
        "| `~/.doppel/config.yaml` | Model settings, tool configuration, display options |",
        "and `~/.doppel/hooks/` (user-installed).",
        "PID file at `~/.doppel/gateway.pid` — profile-scoped process tracking",
        "Create `~/.doppel/plugins/model-providers/gmi/__init__.py`:",
        "2. **User** — `~/.doppel/plugins/video_gen/<name>/` (opt-in via `plugins.enabled`)",
    )
    stale = (
        "| `~/.hermes/.env` | API keys, bot tokens, platform credentials |",
        "| `~/.hermes/config.yaml` | Model settings, tool configuration, display options |",
        "and `~/.hermes/hooks/` (user-installed).",
        "PID file at `~/.hermes/gateway.pid` — profile-scoped process tracking",
        "Create `~/.hermes/plugins/model-providers/gmi/__init__.py`:",
        "2. **User** — `~/.hermes/plugins/video_gen/<name>/` (opt-in via `plugins.enabled`)",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
