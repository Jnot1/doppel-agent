from pathlib import Path


def test_small_cli_modules_prefer_doppel_customer_facing_copy() -> None:
    hooks = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/hooks.py"
    ).read_text(encoding="utf-8")
    bundles = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/bundles.py"
    ).read_text(encoding="utf-8")
    prompt_size = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/prompt_size.py"
    ).read_text(encoding="utf-8")

    hooks_required = [
        '"""doppel hooks — inspect and manage shell-script hooks.',
        "    doppel hooks list",
        "    doppel hooks test <event> [--for-tool X] [--payload-file F]",
        "    doppel hooks revoke <command>",
        "    doppel hooks doctor",
        "Consent records live under ``~/.doppel/shell-hooks-allowlist.json`` and",
        "hook definitions come from the ``hooks:`` block in ``~/.doppel/config.yaml``",
        '"""Entry point for ``doppel hooks`` — dispatches to the requested action."""',
        "Usage: doppel hooks {list|test|revoke|doctor}",
        "Run 'doppel hooks --help' for details.",
        "No shell hooks configured in ~/.doppel/config.yaml.",
        "See `doppel hooks --help` or",
        "run `doppel hooks doctor` to re-validate",
        "stdin a script sees under `doppel hooks test` and `doppel hooks doctor`",
        "parsed (Doppel wire shape):",
        "then `doppel hooks revoke` + re-approve to refresh",
        "is already allowlisted.  Otherwise `doppel hooks doctor` would execute",
        "then re-run `doppel hooks doctor`.",
    ]
    hooks_forbidden = [
        '"""hermes hooks — inspect and manage shell-script hooks.',
        "    hermes hooks list",
        "    hermes hooks test <event> [--for-tool X] [--payload-file F]",
        "    hermes hooks revoke <command>",
        "    hermes hooks doctor",
        "Consent records live under ``~/.hermes/shell-hooks-allowlist.json`` and",
        "hook definitions come from the ``hooks:`` block in ``~/.hermes/config.yaml``",
        '"""Entry point for ``hermes hooks`` — dispatches to the requested action."""',
        "Usage: hermes hooks {list|test|revoke|doctor}",
        "Run 'hermes hooks --help' for details.",
        "No shell hooks configured in ~/.hermes/config.yaml.",
        "See `hermes hooks --help` or",
        "run `hermes hooks doctor` to re-validate",
        "stdin a script sees under `hermes hooks test` and `hermes hooks doctor`",
        "parsed (Hermes wire shape):",
        "then `hermes hooks revoke` + re-approve to refresh",
        "is already allowlisted.  Otherwise `hermes hooks doctor` would execute",
        "then re-run `hermes hooks doctor`.",
    ]

    bundles_required = [
        '"""Implementation of the ``doppel bundles`` CLI subcommand.',
        "# Bind to stderr so piping `doppel bundles list | grep …` doesn't",
        '"""Build the ``doppel bundles`` argparse tree.',
        '"""Dispatch ``doppel bundles <subcommand>`` to the right handler."""',
    ]
    bundles_forbidden = [
        '"""Implementation of the ``hermes bundles`` CLI subcommand.',
        "# Bind to stderr so piping `hermes bundles list | grep …` doesn't",
        '"""Build the ``hermes bundles`` argparse tree.',
        '"""Dispatch ``hermes bundles <subcommand>`` to the right handler."""',
    ]

    prompt_required = [
        '"""Prompt-size diagnostic: ``doppel prompt-size``.',
        '"""Entry point for ``doppel prompt-size``."""',
    ]
    prompt_forbidden = [
        '"""Prompt-size diagnostic: ``hermes prompt-size``.',
        '"""Entry point for ``hermes prompt-size``."""',
    ]

    for text in hooks_required:
        assert text in hooks, text
    for text in hooks_forbidden:
        assert text not in hooks, text
    for text in bundles_required:
        assert text in bundles, text
    for text in bundles_forbidden:
        assert text not in bundles, text
    for text in prompt_required:
        assert text in prompt_size, text
    for text in prompt_forbidden:
        assert text not in prompt_size, text
