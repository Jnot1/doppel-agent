"""Focused rebrand guards for the Slack CLI helper surface."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_slack_cli_module_prefers_doppel_customer_facing_examples():
    text = (REPO_ROOT / "hermes_cli" / "slack_cli.py").read_text(encoding="utf-8")

    assert '"""``doppel slack ...`` CLI subcommands.' in text
    assert "Today only ``doppel slack manifest`` is implemented" in text
    assert "$ doppel slack manifest > slack-manifest.json" in text
    assert "$ doppel slack manifest --write" in text

    for stale in (
        '"""``hermes slack ...`` CLI subcommands.',
        "Today only ``hermes slack manifest`` is implemented",
        "$ hermes slack manifest > slack-manifest.json",
        "$ hermes slack manifest --write",
    ):
        assert stale not in text


def test_cmd_slack_usage_hint_is_doppel_first_in_source():
    text = (REPO_ROOT / "hermes_cli" / "main.py").read_text(encoding="utf-8")

    assert "Dispatches ``doppel slack <subcommand>``." in text
    assert '"usage: doppel slack <subcommand>\\n"' in text
    assert '"Run `doppel slack manifest -h` for details."' in text

    for stale in (
        "Dispatches ``hermes slack <subcommand>``.",
        '"usage: hermes slack <subcommand>\\n"',
        '"Run `hermes slack manifest -h` for details."',
    ):
        assert stale not in text
