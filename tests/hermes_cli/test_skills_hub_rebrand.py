"""Focused rebrand guards for the skills hub customer-facing surface."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_skills_hub_prefers_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "skills_hub.py").read_text(encoding="utf-8")

    expected = [
        "Skills Hub CLI — Unified interface for the Doppel Skills Hub.",
        "- `doppel skills <subcommand>` (CLI argparse entry point)",
        "so users can copy it for `doppel skills install`.",
        'Return sorted subdirectory names under ``~/.doppel/skills/`` that look',
        "[bold]Category[/] [dim](optional — press Enter to install flat at ~/.doppel/skills/<name>/)[/]",
        "into `doppel skills install` fail.",
        "[dim]Use: doppel skills inspect <identifier> to preview, ",
        "[dim]Tip: 'doppel skills search <query>' searches deeper across all registries[/]",
        "[bold]doppel skills install {url} --name <your-name>[/]",
        'subtitle="doppel skills install <id> to install"',
        "config — ``doppel -p <profile> skills list`` reads that profile's",
        "Usage: doppel skills tap add owner/repo",
        "Usage: doppel skills tap remove owner/repo",
        "Usage: doppel skills publish <path> --to github --repo owner/repo",
        "Submitting the `{skill_name}` skill via Doppel Skills Hub.",
        "This skill was scanned by the Doppel Skills Guard before submission.",
        "Router for `doppel skills <subcommand>` — called from hermes_cli/main.py.",
        "Usage: doppel skills snapshot [export|import]",
        "Usage: doppel skills tap [list|add|remove]",
        "Usage: doppel skills [browse|search|install|inspect|list|check|update|audit|uninstall|reset|publish|snapshot|tap]",
        "Run 'doppel skills <command> --help' for details.",
    ]
    forbidden = [
        "Skills Hub CLI — Unified interface for the Hermes Skills Hub.",
        "- `hermes skills <subcommand>` (CLI argparse entry point)",
        "so users can copy it for `hermes skills install`.",
        'Return sorted subdirectory names under ``~/.hermes/skills/`` that look',
        "[bold]Category[/] [dim](optional — press Enter to install flat at ~/.hermes/skills/<name>/)[/]",
        "into `hermes skills install` fail.",
        "[dim]Use: hermes skills inspect <identifier> to preview, ",
        "[dim]Tip: 'hermes skills search <query>' searches deeper across all registries[/]",
        "[bold]hermes skills install {url} --name <your-name>[/]",
        'subtitle="hermes skills install <id> to install"',
        "config — ``hermes -p <profile> skills list`` reads that profile's",
        "Usage: hermes skills tap add owner/repo",
        "Usage: hermes skills tap remove owner/repo",
        "Usage: hermes skills publish <path> --to github --repo owner/repo",
        "Submitting the `{skill_name}` skill via Hermes Skills Hub.",
        "This skill was scanned by the Hermes Skills Guard before submission.",
        "Router for `hermes skills <subcommand>` — called from hermes_cli/main.py.",
        "Usage: hermes skills snapshot [export|import]",
        "Usage: hermes skills tap [list|add|remove]",
        "Usage: hermes skills [browse|search|install|inspect|list|check|update|audit|uninstall|reset|publish|snapshot|tap]",
        "Run 'hermes skills <command> --help' for details.",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text
