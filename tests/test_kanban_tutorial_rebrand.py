from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "features" / "kanban-tutorial.md"


def test_kanban_tutorial_prefers_doppel_for_customer_facing_copy():
    text = DOC.read_text(encoding="utf-8")

    expected = (
        "A walkthrough of the four use-cases the Doppel Kanban system was designed for",
        "doppel kanban init",
        "doppel dashboard",
        "`~/.doppel/kanban.db`",
        "`~/.doppel/kanban/boards/<slug>/kanban.db`",
        "run `doppel kanban decompose <id>`",
        "SCHEMA=$(doppel kanban create",
        "API=$(doppel kanban create",
        "doppel kanban create \"Write auth integration tests\"",
        "doppel kanban show $SCHEMA",
        "doppel kanban runs $SCHEMA",
        "doppel gateway start",
        "doppel kanban unblock $IMPL",
        "doppel kanban create \"Deploy to staging (missing creds)\"",
        "doppel kanban runs t_ef5d",
        "`doppel kanban complete a b c --summary X`",
        "`doppel kanban --help`",
        "`doppel kanban watch --kinds completed,gave_up,timed_out`",
        "`doppel kanban notify-subscribe <task> --platform telegram --chat-id <id>`",
    )
    stale = (
        "A walkthrough of the four use-cases the Hermes Kanban system was designed for",
        "hermes kanban init",
        "hermes dashboard",
        "`~/.hermes/kanban.db`",
        "`~/.hermes/kanban/boards/<slug>/kanban.db`",
        "run `hermes kanban decompose <id>`",
        "SCHEMA=$(hermes kanban create",
        "API=$(hermes kanban create",
        "hermes kanban create \"Write auth integration tests\"",
        "hermes kanban show $SCHEMA",
        "hermes kanban runs $SCHEMA",
        "hermes gateway start",
        "hermes kanban unblock $IMPL",
        "hermes kanban create \"Deploy to staging (missing creds)\"",
        "hermes kanban runs t_ef5d",
        "`hermes kanban complete a b c --summary X`",
        "`hermes kanban --help`",
        "`hermes kanban watch --kinds completed,gave_up,timed_out`",
        "`hermes kanban notify-subscribe <task> --platform telegram --chat-id <id>`",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
