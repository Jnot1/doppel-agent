from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL = REPO_ROOT / "skills" / "productivity" / "google-workspace" / "SKILL.md"
DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "skills" / "google-workspace.md"


def test_google_workspace_skill_prefers_doppel_for_customer_facing_copy():
    text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (SKILL, DOC)
    )

    expected = (
        "through Doppel-managed OAuth and a thin CLI wrapper.",
        "while preserving Doppel's existing JSON output contract.",
        'GSETUP="python ${DOPPEL_HOME:-$HOME/.doppel}/skills/productivity/google-workspace/scripts/setup.py"',
        "Important Doppel CLI note",
        "~/Downloads/doppel-google-client-secret.json",
        "`~/.doppel/google_oauth_last_url.txt`.",
        "Token is stored at `~/.doppel/google_token.json` and auto-refreshes.",
        "Pending OAuth session state/verifier are stored temporarily at `~/.doppel/google_oauth_pending.json` until exchange completes.",
        "points it at the same `~/.doppel/google_token.json` credentials file.",
        'GAPI="python ${DOPPEL_HOME:-$HOME/.doppel}/skills/productivity/google-workspace/scripts/google_api.py"',
        "Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration for Doppel.",
        "The setup is fully agent-driven — ask Doppel to set up Google Workspace and it walks you through each step.",
        "Doppel generates an auth URL, you approve in the browser, paste back the redirect URL",
        "| `NOT_AUTHENTICATED` | Run setup (ask Doppel to set up Google Workspace) |",
    )
    stale = (
        "through Hermes-managed OAuth and a thin CLI wrapper.",
        "while preserving Hermes' existing JSON output contract.",
        'GSETUP="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/setup.py"',
        "Important Hermes CLI note",
        "~/Downloads/hermes-google-client-secret.json",
        "`~/.hermes/google_oauth_last_url.txt`.",
        "Token is stored at `~/.hermes/google_token.json` and auto-refreshes.",
        "Pending OAuth session state/verifier are stored temporarily at `~/.hermes/google_oauth_pending.json` until exchange completes.",
        "points it at the same `~/.hermes/google_token.json` credentials file.",
        'GAPI="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/google_api.py"',
        "Gmail, Calendar, Drive, Contacts, Sheets, and Docs integration for Hermes.",
        "The setup is fully agent-driven — ask Hermes to set up Google Workspace and it walks you through each step.",
        "Hermes generates an auth URL, you approve in the browser, paste back the redirect URL",
        "| `NOT_AUTHENTICATED` | Run setup (ask Hermes to set up Google Workspace) |",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
