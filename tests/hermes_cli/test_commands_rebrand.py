from pathlib import Path


def test_commands_doc_surfaces_prefer_doppel() -> None:
    text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/commands.py"
    ).read_text(encoding="utf-8")

    required = [
        "``doppel skills list`` and the agent's ``/skill-name`` dispatch but",
        "Skills disabled for the ``\"telegram\"`` platform (via ``doppel skills",
        "parity, external-dir skills are visible via ``doppel skills list`` and",
        '"""Return subcommand -> /command mapping for Slack /doppel handler.',
        "Maps both canonical names and aliases so /doppel bg do stuff works",
        "the same as /doppel background do stuff.",
        "Plugin-registered slash commands are included so ``/doppel <plugin-cmd>``",
        "in Slack's ``/doppel`` subcommand mapping, and",
    ]
    forbidden = [
        "``hermes skills list`` and the agent's ``/skill-name`` dispatch but",
        "Skills disabled for the ``\"telegram\"`` platform (via ``hermes skills",
        "parity, external-dir skills are visible via ``hermes skills list`` and",
        '"""Return subcommand -> /command mapping for Slack /hermes handler.',
        "Maps both canonical names and aliases so /hermes bg do stuff works",
        "the same as /hermes background do stuff.",
        "Plugin-registered slash commands are included so ``/hermes <plugin-cmd>``",
        "in Slack's ``/hermes`` subcommand mapping, and",
    ]

    for needle in required:
        assert needle in text, needle
    for needle in forbidden:
        assert needle not in text, needle
