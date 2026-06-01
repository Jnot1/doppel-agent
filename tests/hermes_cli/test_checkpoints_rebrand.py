"""Focused rebrand guards for the checkpoints CLI help surface."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_checkpoints_cli_module_prefers_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "checkpoints.py").read_text(encoding="utf-8")

    expected = [
        '"""`doppel checkpoints` CLI subcommand.',
        "store at ``~/.doppel/checkpoints/``.  Actions:",
        "    doppel checkpoints               # same as `status`",
        "    doppel checkpoints status        # total size, project count, breakdown",
        "    doppel checkpoints list          # per-project checkpoint counts + workdir",
        "    doppel checkpoints prune [opts]  # force a sweep (ignores the 24h marker)",
        "    doppel checkpoints clear [-f]    # nuke the entire base (asks first)",
        "    doppel checkpoints clear-legacy  # delete just the legacy-* archives",
        "    doppel checkpoints",
        "    doppel checkpoints prune --retention-days 3 --max-size-mb 200",
        "    doppel checkpoints clear -f",
        'print("Clear with: doppel checkpoints clear-legacy")',
        '"""Wire subcommands onto the ``doppel checkpoints`` parser."""',
        "# bare `doppel checkpoints` → status",
    ]
    forbidden = [
        '"""`hermes checkpoints` CLI subcommand.',
        "store at ``~/.hermes/checkpoints/``.  Actions:",
        "    hermes checkpoints               # same as `status`",
        "    hermes checkpoints status        # total size, project count, breakdown",
        "    hermes checkpoints list          # per-project checkpoint counts + workdir",
        "    hermes checkpoints prune [opts]  # force a sweep (ignores the 24h marker)",
        "    hermes checkpoints clear [-f]    # nuke the entire base (asks first)",
        "    hermes checkpoints clear-legacy  # delete just the legacy-* archives",
        "    hermes checkpoints",
        "    hermes checkpoints prune --retention-days 3 --max-size-mb 200",
        "    hermes checkpoints clear -f",
        'print("Clear with: hermes checkpoints clear-legacy")',
        '"""Wire subcommands onto the ``hermes checkpoints`` parser."""',
        "# bare `hermes checkpoints` → status",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text
