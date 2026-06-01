from pathlib import Path


def test_misc_runtime_and_help_surfaces_prefer_doppel() -> None:
    expectations = {
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/copilot_auth.py": {
            "required": [
                "  → `copilot login` or `doppel model` to authenticate via OAuth",
            ],
            "forbidden": [
                "  → `copilot login` or `hermes model` to authenticate via OAuth",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/portal_cli.py": {
            "required": [
                '"""``doppel portal`` — small CLI surface for Nous Portal users.',
                "already in ``doppel auth`` or ``doppel tools``.",
                '"""Top-level dispatch for `doppel portal <subcommand>`."""',
                "Run `doppel portal -h` for usage.",
                '"""Register `doppel portal` on the given argparse subparsers object."""',
            ],
            "forbidden": [
                '"""``hermes portal`` — small CLI surface for Nous Portal users.',
                "already in ``hermes auth`` or ``hermes tools``.",
                '"""Top-level dispatch for `hermes portal <subcommand>`."""',
                "Run `hermes portal -h` for usage.",
                '"""Register `hermes portal` on the given argparse subparsers object."""',
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/debug.py": {
            "required": [
                '"""``doppel debug`` debug tools for Doppel Agent.',
                "doppel debug share    Upload debug report",
                "``~/.doppel/logs/*.log`` are not leaked into",
                "Path to ``~/.doppel/pastes/pending.json``.",
                "ran ``doppel debug share`` repeatedly.",
                "the user has to run ``doppel debug delete``",
                "Doppel version, provider, which API keys",
                "Full logs are NOT included from the gateway — use `doppel debug share` ",
            ],
            "forbidden": [
                '"""``hermes debug`` debug tools for Hermes Agent.',
                "hermes debug share    Upload debug report",
                "``~/.hermes/logs/*.log`` are not leaked into",
                "Path to ``~/.hermes/pastes/pending.json``.",
                "ran ``hermes debug share`` repeatedly.",
                "the user has to run ``hermes debug delete``",
                "Hermes version, provider, which API keys",
                "Full logs are NOT included from the gateway — use `hermes debug share` ",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/pty_bridge.py": {
            "required": [
                '"""PTY bridge for `doppel dashboard` chat tab.',
                "to the same ``doppel --tui`` binary it would launch from the CLI, so",
                "Doppel Agent supports Windows only via WSL.",
            ],
            "forbidden": [
                '"""PTY bridge for `hermes dashboard` chat tab.',
                "to the same ``hermes --tui`` binary it would launch from the CLI, so",
                "Hermes Agent supports Windows only via WSL.",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/model_switch.py": {
            "required": [
                "for use with Doppel Agent. They lack the tool-calling capabilities ",
                "Check 'doppel model' for available providers, or define it ",
                "the SAME list `doppel model` would build, with",
                "with `doppel model`).",
            ],
            "forbidden": [
                "for use with Hermes Agent. They lack the tool-calling capabilities ",
                "Check 'hermes model' for available providers, or define it ",
                "the SAME list `hermes model` would build, with",
                "with `hermes model`).",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/memory_setup.py": {
            "required": [
                "# Curses-based interactive picker (same pattern as doppel tools)",
            ],
            "forbidden": [
                "# Curses-based interactive picker (same pattern as hermes tools)",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/profile_distribution.py": {
            "required": [
                '"""Profile distributions — shareable, packaged Doppel profiles via git.',
                "A distribution is a Doppel profile published as a git repository",
                "* ``doppel profile export/import`` — local backup / restore for a profile",
                "* ``doppel skills install <url>`` — the URL install pattern we're mirroring,",
                "Subcommands (all live under ``doppel profile``, not a parallel tree):",
                "    doppel profile install <source> [--name N] [--alias] [--force] [--yes]",
                "    doppel profile update  <name>  [--force-config] [--yes]",
                "    doppel profile info    <name>",
                "installed manifest's ``source:`` field so ``doppel profile update`` can",
                "This repository is not a Doppel profile distribution.",
                "Use `doppel profile update` to upgrade in place, ",
                "Only profiles installed via `doppel profile install` can be updated.",
                "`doppel profile install <source> --name {canon} --force`.",
            ],
            "forbidden": [
                '"""Profile distributions — shareable, packaged Hermes profiles via git.',
                "A distribution is a Hermes profile published as a git repository",
                "* ``hermes profile export/import`` — local backup / restore for a profile",
                "* ``hermes skills install <url>`` — the URL install pattern we're mirroring,",
                "Subcommands (all live under ``hermes profile``, not a parallel tree):",
                "    hermes profile install <source> [--name N] [--alias] [--force] [--yes]",
                "    hermes profile update  <name>  [--force-config] [--yes]",
                "    hermes profile info    <name>",
                "installed manifest's ``source:`` field so ``hermes profile update`` can",
                "This repository is not a Hermes profile distribution.",
                "Use `hermes profile update` to upgrade in place, ",
                "Only profiles installed via `hermes profile install` can be updated.",
                "`hermes profile install <source> --name {canon} --force`.",
            ],
        },
    }

    for path_str, expected in expectations.items():
        text = Path(path_str).read_text(encoding="utf-8")
        for snippet in expected["required"]:
            assert snippet in text, f"{path_str}: missing {snippet!r}"
        for snippet in expected["forbidden"]:
            assert snippet not in text, f"{path_str}: forbidden {snippet!r}"
