from pathlib import Path


def test_migrate_and_install_surfaces_prefer_doppel() -> None:
    migrate_text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/migrate.py"
    ).read_text(encoding="utf-8")
    install_text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/scripts/install.sh"
    ).read_text(encoding="utf-8")

    required_migrate = [
        '"""CLI handlers for ``doppel migrate ...``.',
        "Currently exposes only ``doppel migrate xai``",
        '"""Dispatcher for ``doppel migrate <subtype>``."""',
        'print("usage: doppel migrate xai [--apply] [--no-backup]", file=sys.stderr)',
        "Re-run with `doppel migrate xai --apply` to rewrite ",
        "Run `doppel doctor` to confirm no retired xAI models remain.",
    ]
    forbidden_migrate = [
        '"""CLI handlers for ``hermes migrate ...``.',
        "Currently exposes only ``hermes migrate xai``",
        '"""Dispatcher for ``hermes migrate <subtype>``."""',
        'print("usage: hermes migrate xai [--apply] [--no-backup]", file=sys.stderr)',
        "Re-run with `hermes migrate xai --apply` to rewrite ",
        "Run `hermes doctor` to confirm no retired xAI models remain.",
    ]

    required_install = [
        'log_warn "No Doppel entry point found on PATH after install"',
    ]
    forbidden_install = [
        'log_warn "No Doppel/Hermes entry point found on PATH after install"',
    ]

    for needle in required_migrate:
        assert needle in migrate_text, needle
    for needle in forbidden_migrate:
        assert needle not in migrate_text, needle

    for needle in required_install:
        assert needle in install_text, needle
    for needle in forbidden_install:
        assert needle not in install_text, needle
