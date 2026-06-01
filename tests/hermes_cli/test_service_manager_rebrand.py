from pathlib import Path


def test_service_manager_command_surfaces_prefer_doppel() -> None:
    text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/service_manager.py"
    ).read_text(encoding="utf-8")

    required = [
        "``doppel gateway start/stop/restart`` when running inside a container.",
        "in ``doppel gateway start/stop/restart``).",
        "``doppel -p <profile>`` flag before the call).",
        "``doppel -p <profile> gateway run`` (or just ``doppel",
        "Special case: ``profile == \"default\"`` emits ``doppel gateway",
        'lines.append("exec s6-setuidgid hermes doppel gateway run")',
        'f"exec s6-setuidgid hermes doppel -p {shlex.quote(profile)} gateway run"',
        "This is what ``doppel logs`` reads and what",
    ]
    forbidden = [
        "``hermes gateway start/stop/restart`` when running inside a container.",
        "in ``hermes gateway start/stop/restart``).",
        "``hermes -p <profile>`` flag before the call).",
        "``hermes -p <profile> gateway run`` (or just ``hermes",
        "Special case: ``profile == \"default\"`` emits ``hermes gateway",
        'lines.append("exec s6-setuidgid hermes hermes gateway run")',
        'f"exec s6-setuidgid hermes hermes -p {shlex.quote(profile)} gateway run"',
        "This is what ``hermes logs`` reads and what",
    ]

    for needle in required:
        assert needle in text, needle
    for needle in forbidden:
        assert needle not in text, needle
