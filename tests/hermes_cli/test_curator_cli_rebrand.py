from pathlib import Path


def test_curator_cli_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/curator.py")
    text = path.read_text(encoding="utf-8")

    required = [
        '"""CLI subcommand: `doppel curator <subcommand>`.',
        "curator: snapshot created at ~/.doppel/skills/.curator_backups/",
        "This will replace the current ~/.doppel/skills/ tree",
        "Take a manual tar.gz snapshot of ~/.doppel/skills/",
        "Restore ~/.doppel/skills/ from a curator snapshot",
    ]
    forbidden = [
        '"""CLI subcommand: `hermes curator <subcommand>`.',
        "curator: snapshot created at ~/.hermes/skills/.curator_backups/",
        "This will replace the current ~/.hermes/skills/ tree",
        "Take a manual tar.gz snapshot of ~/.hermes/skills/",
        "Restore ~/.hermes/skills/ from a curator snapshot",
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
