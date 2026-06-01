from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "secrets" / "bitwarden.md"


def test_bitwarden_docs_prefer_doppel_for_customer_facing_copy():
    text = DOC.read_text(encoding="utf-8")

    expected = (
        "inside `~/.doppel/.env`",
        "Doppel stores that single token in `~/.doppel/.env`",
        "Every time `doppel`",
        "after `~/.doppel/.env` has loaded, Doppel calls",
        "every Doppel process picks it up on next start",
        "auto-downloaded into `~/.doppel/bin/`",
        'Create or pick a **Project** (e.g. "Doppel keys").',
        "**Machine accounts → New machine account → My Doppel machine**",
        "doppel secrets bitwarden setup",
        "`~/.doppel/bin/bws`",
        "`~/.doppel/.env` as `BWS_ACCESS_TOKEN`",
        "doppel secrets bitwarden status",
        "every `doppel` invocation pulls fresh secrets at startup",
        "| `doppel secrets bitwarden setup` |",
        "Defaults in `~/.doppel/config.yaml`",
        "new `doppel` invocations start fresh",
        "Re-run `doppel secrets bitwarden setup`",
        "Bitwarden never blocks Doppel startup.",
        "updated through PRs to this repo — Doppel does not auto-upgrade `bws`",
        "**Single-machine personal setups** where `~/.doppel/.env` is fine.",
        "multiple Doppel installations",
    )
    stale = (
        "inside `~/.hermes/.env`",
        "Hermes stores that single token in `~/.hermes/.env`",
        "Every time `hermes`",
        "after `~/.hermes/.env` has loaded, Hermes calls",
        "every Hermes process picks it up on next start",
        "auto-downloaded into `~/.hermes/bin/`",
        'Create or pick a **Project** (e.g. "Hermes keys").',
        "**Machine accounts → New machine account → My Hermes machine**",
        "hermes secrets bitwarden setup",
        "`~/.hermes/bin/bws`",
        "`~/.hermes/.env` as `BWS_ACCESS_TOKEN`",
        "hermes secrets bitwarden status",
        "every `hermes` invocation pulls fresh secrets at startup",
        "| `hermes secrets bitwarden setup` |",
        "Defaults in `~/.hermes/config.yaml`",
        "new `hermes` invocations start fresh",
        "Re-run `hermes secrets bitwarden setup`",
        "Bitwarden never blocks Hermes startup.",
        "updated through PRs to this repo — Hermes does not auto-upgrade `bws`",
        "**Single-machine personal setups** where `~/.hermes/.env` is fine.",
        "multiple Hermes installations",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
