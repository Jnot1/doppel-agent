from pathlib import Path


def test_setup_openclaw_migration_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/setup.py")
    text = path.read_text(encoding="utf-8")

    required = [
        "Would overwrite (conflicts with existing Doppel config):",
        "OpenClaw config values may have different semantics in Doppel.",
        'OpenClaw\'s tool_call_execution: \\"auto\\" ≠ Doppel\'s yolo mode.',
        "overwrite=False so existing Doppel configs are",
        "preserve existing Doppel config",
    ]
    forbidden = [
        "Would overwrite (conflicts with existing Hermes config):",
        "OpenClaw config values may have different semantics in Hermes.",
        'OpenClaw\'s tool_call_execution: \\"auto\\" ≠ Hermes\'s yolo mode.',
        "overwrite=False so existing Hermes configs are",
        "preserve existing Hermes config",
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
