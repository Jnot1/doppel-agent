from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "sessions.md"


def test_sessions_doc_prefers_doppel_for_customer_facing_copy():
    text = DOC.read_text(encoding="utf-8")

    expected = (
        "Doppel Agent automatically saves every conversation as a session.",
        "`~/.doppel/state.db`",
        "Doppel stores session history so it can resume conversations",
        "asks Doppel to make a meme from it",
        "`doppel sessions prune`",
        "Interactive CLI (`doppel` or `doppel chat`)",
        "doppel --continue",
        "doppel chat --continue",
        "doppel --resume 20250305_091523_a1b2c3d4",
        "`doppel sessions list`",
        "shown when resuming a Doppel session",
        "`~/.doppel/config.yaml`",
        '(or `doppel -r "<title>"` from the shell)',
        "Doppel automatically generates a short descriptive title",
        "`doppel sessions browse`",
        "Doppel provides a full set of session management commands via `doppel sessions`",
        "doppel sessions list",
        "doppel sessions export backup.jsonl",
        "doppel sessions delete 20250305_091523_a1b2c3d4",
        "doppel sessions rename 20250305_091523_a1b2c3d4",
        "doppel sessions prune --older-than 30",
        "doppel sessions stats",
        "[`doppel insights`](/reference/cli-commands#doppel-insights)",
        "When Doppel cannot get a participant identifier",
        "By default, Doppel uses `group_sessions_per_user: true`",
        "Alice and Bob can both talk to Doppel",
        "| SQLite database | `~/.doppel/state.db` |",
        "| Gateway routing index | `~/.doppel/sessions/sessions.json` |",
        "`*.jsonl` files in `~/.doppel/sessions/`.",
        "read by Doppel.",
        "same `DOPPEL_HOME`",
    )

    stale = (
        "Hermes Agent automatically saves every conversation as a session.",
        "`~/.hermes/state.db`",
        "Hermes stores session history so it can resume conversations",
        "asks Hermes to make a meme from it",
        "`hermes sessions prune`",
        "Interactive CLI (`hermes` or `hermes chat`)",
        "hermes --continue",
        "hermes chat --continue",
        "hermes --resume 20250305_091523_a1b2c3d4",
        "`hermes sessions list`",
        "shown when resuming a Hermes session",
        "`~/.hermes/config.yaml`",
        '(or `hermes -r "<title>"` from the shell)',
        "Hermes automatically generates a short descriptive title",
        "`hermes sessions browse`",
        "Hermes provides a full set of session management commands via `hermes sessions`",
        "hermes sessions list",
        "hermes sessions export backup.jsonl",
        "hermes sessions delete 20250305_091523_a1b2c3d4",
        "hermes sessions rename 20250305_091523_a1b2c3d4",
        "hermes sessions prune --older-than 30",
        "hermes sessions stats",
        "[`hermes insights`](/reference/cli-commands#hermes-insights)",
        "When Hermes cannot get a participant identifier",
        "By default, Hermes uses `group_sessions_per_user: true`",
        "Alice and Bob can both talk to Hermes",
        "| SQLite database | `~/.hermes/state.db` |",
        "| Gateway routing index | `~/.hermes/sessions/sessions.json` |",
        "`*.jsonl` files in `~/.hermes/sessions/`.",
        "read by Hermes.",
        "same `HERMES_HOME`",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
