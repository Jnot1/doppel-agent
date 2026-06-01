from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOC = REPO_ROOT / "website" / "docs" / "developer-guide" / "cron-internals.md"


def test_cron_internals_doc_prefers_doppel_for_customer_facing_copy():
    text = DOC.read_text(encoding="utf-8")

    expected = (
        'description: "How Doppel stores, schedules, edits, pauses, skill-loads, and delivers cron jobs"',
        "| `hermes_cli/cron.py` | CLI `doppel cron` subcommands |",
        "`~/.doppel/cron/jobs.json`",
        "only fire when `doppel cron` commands are run",
        "# ~/.doppel/scripts/check_competitors.py",
        "Save to `~/.doppel/cron/output/`",
        "a standalone `doppel cron` / manual `tick()` call",
        "The `doppel cron` CLI provides direct job management:",
        "doppel cron list",
        "doppel cron create",
        "doppel cron edit <job_id>",
        "doppel cron pause <job_id>",
        "doppel cron resume <job_id>",
        "doppel cron run <job_id>",
        "doppel cron remove <job_id>",
    )
    stale = (
        'description: "How Hermes stores, schedules, edits, pauses, skill-loads, and delivers cron jobs"',
        "| `hermes_cli/cron.py` | CLI `hermes cron` subcommands |",
        "`~/.hermes/cron/jobs.json`",
        "only fire when `hermes cron` commands are run",
        "# ~/.hermes/scripts/check_competitors.py",
        "Save to `~/.hermes/cron/output/`",
        "a standalone `hermes cron` / manual `tick()` call",
        "The `hermes cron` CLI provides direct job management:",
        "hermes cron list",
        "hermes cron create",
        "hermes cron edit <job_id>",
        "hermes cron pause <job_id>",
        "hermes cron resume <job_id>",
        "hermes cron run <job_id>",
        "hermes cron remove <job_id>",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
