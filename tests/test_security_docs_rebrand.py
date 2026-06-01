from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "security.md"


def test_security_docs_prefer_doppel_for_customer_facing_copy():
    text = DOC.read_text(encoding="utf-8")

    expected = (
        "configured via `approvals.mode` in your agent-home `config.yaml` (`~/.doppel/config.yaml`):",
        "Configure the timeout in your agent-home `config.yaml` (`~/.doppel/config.yaml`):",
        "| `tee` to `/etc/`, `~/.ssh/`, or your agent-home `.env` (`~/.doppel/.env`) | Overwrite sensitive file via tee |",
        "| `>` / `>>` to `/etc/`, `~/.ssh/`, or your agent-home `.env` (`~/.doppel/.env`) | Overwrite sensitive file via redirection |",
        "Set allowed user IDs as comma-separated values in your agent-home `.env` file (`~/.doppel/.env`):",
        "**Storage:** Pairing data is stored in `~/.doppel/pairing/` with per-platform JSON files:",
        "Container resources are configurable in your agent-home `config.yaml` (`~/.doppel/config.yaml`):",
        "Bind-mounts `/workspace` and `/root` from the profile-scoped Docker sandbox directory under your agent home",
        "Google Workspace stores OAuth tokens as `google_token.json` under the active profile's agent home.",
        "When loaded, Doppel checks if these files exist in the active profile's agent home and registers them for mounting:",
        "Paths are relative to the active agent-home root. Files are mounted under the container's agent-home directory.",
        "keep API keys in your agent-home `.env` file (`~/.doppel/.env`) with proper file permissions",
        "check `~/.doppel/logs/` for unauthorized access attempts",
    )
    stale = (
        "legacy `~/.hermes/config.yaml` still works",
        "legacy `~/.hermes/.env` still works",
        "legacy `~/.hermes/pairing/` still works",
        "legacy `~/.hermes/logs/` still works",
        "`container_persistent: true`): Bind-mounts `/workspace` and `/root` from `~/.hermes/sandboxes/docker/<task_id>/`",
        "active profile's `HERMES_HOME`",
        "Paths are relative to `~/.hermes/`. Files are mounted to `/root/.hermes/` inside the container.",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
