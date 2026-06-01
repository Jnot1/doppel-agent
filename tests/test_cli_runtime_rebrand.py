from pathlib import Path


def test_cli_runtime_surfaces_prefer_doppel() -> None:
    cli = Path("/Users/macshelton/Documents/DoppelFork-repair2/cli.py").read_text(
        encoding="utf-8"
    )

    required = [
        "Load .env from ~/.doppel/.env first, then project root as dev fallback.",
        "Relative paths are resolved from ~/.doppel/.",
        "1. ~/.doppel/config.yaml (user config - preferred)",
        "the user config at ``~/.doppel/config.yaml`` is skipped entirely and only the",
        "Initialize centralized logging early — agent.log + errors.log in ~/.doppel/logs/.",
        "Interactive CLI for Doppel Agent.",
        "Saves the image to ~/.doppel/images/ and appends the path to",
        '"""Save the current conversation to a JSON snapshot under ~/.doppel/sessions/saved/.',
        "DB, so the live session remains resumable via ``doppel --resume <id>``",
        "``doppel update`` so the user sees update output directly and gets",
        '"""Reload skills: rescan ~/.doppel/skills/ and queue a note for the',
    ]
    forbidden = [
        "Load .env from ~/.hermes/.env first, then project root as dev fallback.",
        "Relative paths are resolved from ~/.hermes/.",
        "1. ~/.hermes/config.yaml (user config - preferred)",
        "the user config at ``~/.hermes/config.yaml`` is skipped entirely and only the",
        "Initialize centralized logging early — agent.log + errors.log in ~/.hermes/logs/.",
        "Interactive CLI for the Hermes Agent.",
        "Saves the image to ~/.hermes/images/ and appends the path to",
        '"""Save the current conversation to a JSON snapshot under ~/.hermes/sessions/saved/.',
        "DB, so the live session remains resumable via ``hermes --resume <id>``",
        "``hermes update`` so the user sees update output directly and gets",
        '"""Reload skills: rescan ~/.hermes/skills/ and queue a note for the',
    ]

    for text in required:
        assert text in cli, text
    for text in forbidden:
        assert text not in cli, text
