from pathlib import Path


def test_pairing_cli_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/pairing.py")
    text = path.read_text(encoding="utf-8")

    required = [
        "doppel pairing list",
        "doppel pairing approve <platform> <code>",
        "doppel pairing revoke <platform> <user_id>",
        "doppel pairing clear-pending",
        '"""Handle doppel pairing subcommands."""',
        "Usage: doppel pairing {list|approve|revoke|clear-pending}",
        "Run 'doppel pairing --help' for details.",
        "Run 'doppel pairing list' to see pending codes.",
    ]
    forbidden = [
        "hermes pairing list",
        "hermes pairing approve <platform> <code>",
        "hermes pairing revoke <platform> <user_id>",
        "hermes pairing clear-pending",
        '"""Handle hermes pairing subcommands."""',
        "Usage: hermes pairing {list|approve|revoke|clear-pending}",
        "Run 'hermes pairing --help' for details.",
        "Run 'hermes pairing list' to see pending codes.",
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
