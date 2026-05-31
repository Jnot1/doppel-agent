"""Source-level guards for bounded gateway runtime help copy seams."""

from pathlib import Path


def test_gateway_runtime_kanban_recovery_hints_are_doppel_first():
    runtime = Path("gateway/run.py").read_text(encoding="utf-8")

    assert "doppel kanban init" in runtime
    assert "doppel kanban list --status ready" in runtime
    assert "hermes kanban init" not in runtime
    assert "hermes kanban list --status ready" not in runtime
