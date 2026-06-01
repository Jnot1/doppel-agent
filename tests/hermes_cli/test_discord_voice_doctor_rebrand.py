from pathlib import Path


ROOT = Path("/Users/macshelton/Documents/DoppelFork-repair2")


def test_discord_voice_doctor_surfaces_prefer_doppel() -> None:
    text = (ROOT / "scripts" / "discord-voice-doctor.py").read_text(encoding="utf-8")

    required = [
        'DOPPEL_HOME = Path(os.getenv("DOPPEL_HOME") or os.getenv("HERMES_HOME") or Path.home() / ".doppel")',
        'ENV_FILE = DOPPEL_HOME / ".env"',
        '"""Check Doppel config.yaml."""',
        'config_path = DOPPEL_HOME / "config.yaml"',
        'voice_mode_path = DOPPEL_HOME / "gateway_voice_mode.json"',
    ]
    forbidden = [
        'HERMES_HOME = Path(os.getenv("HERMES_HOME", Path.home() / ".hermes"))',
        'ENV_FILE = HERMES_HOME / ".env"',
        '"""Check hermes config.yaml."""',
        'config_path = HERMES_HOME / "config.yaml"',
        'voice_mode_path = HERMES_HOME / "gateway_voice_mode.json"',
    ]

    for needle in required:
        assert needle in text, needle
    for needle in forbidden:
        assert needle not in text, needle
