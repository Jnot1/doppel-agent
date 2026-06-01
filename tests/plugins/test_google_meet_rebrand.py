from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_google_meet_customer_surfaces_prefer_doppel() -> None:
    cli_text = (REPO_ROOT / "plugins/google_meet/cli.py").read_text(encoding="utf-8")
    tools_text = (REPO_ROOT / "plugins/google_meet/tools.py").read_text(encoding="utf-8")
    skill_text = (REPO_ROOT / "plugins/google_meet/SKILL.md").read_text(encoding="utf-8")
    readme_text = (REPO_ROOT / "plugins/google_meet/README.md").read_text(encoding="utf-8")

    required = (
        "doppel meet setup",
        "doppel meet join",
        "doppel meet node approve",
        "Doppel Agent",
        "DOPPEL_MEET_REALTIME_KEY",
        "~/.doppel/.env",
        "$DOPPEL_HOME/workspace/meetings",
        "doppel_meet_src",
    )
    for needle in required:
        corpus = "\n".join((cli_text, tools_text, skill_text, readme_text))
        assert needle in corpus, f"missing Doppel surface: {needle}"

    forbidden = (
        "hermes meet ",
        "Hermes Agent",
        "~/.hermes/.env",
        "$HERMES_HOME/workspace/meetings",
        "hermes_meet_src",
        "hermes_meet_sink",
    )
    for needle in forbidden:
        assert needle not in cli_text
        assert needle not in tools_text
        assert needle not in skill_text
        assert needle not in readme_text


def test_google_meet_runtime_config_prefers_doppel_alias() -> None:
    from plugins.google_meet.meet_bot import _read_runtime_config

    keys = (
        "DOPPEL_MEET_URL",
        "HERMES_MEET_URL",
        "DOPPEL_MEET_OUT_DIR",
        "HERMES_MEET_OUT_DIR",
        "DOPPEL_MEET_GUEST_NAME",
        "HERMES_MEET_GUEST_NAME",
        "DOPPEL_MEET_MODE",
        "HERMES_MEET_MODE",
        "DOPPEL_MEET_REALTIME_KEY",
        "HERMES_MEET_REALTIME_KEY",
        "OPENAI_API_KEY",
        "DOPPEL_MEET_LOBBY_TIMEOUT",
        "HERMES_MEET_LOBBY_TIMEOUT",
    )
    old = {key: os.environ.get(key) for key in keys}
    try:
        os.environ["DOPPEL_MEET_URL"] = "https://meet.google.com/dop-pel-test"
        os.environ["HERMES_MEET_URL"] = "https://meet.google.com/her-mes-test"
        os.environ["DOPPEL_MEET_OUT_DIR"] = "/tmp/doppel-meet"
        os.environ["HERMES_MEET_OUT_DIR"] = "/tmp/hermes-meet"
        os.environ["DOPPEL_MEET_GUEST_NAME"] = "Doppel Agent"
        os.environ["HERMES_MEET_GUEST_NAME"] = "Hermes Agent"
        os.environ["DOPPEL_MEET_MODE"] = "realtime"
        os.environ["HERMES_MEET_MODE"] = "transcribe"
        os.environ["DOPPEL_MEET_REALTIME_KEY"] = "sk-doppel"
        os.environ["HERMES_MEET_REALTIME_KEY"] = "sk-hermes"
        os.environ["DOPPEL_MEET_LOBBY_TIMEOUT"] = "90"
        os.environ["HERMES_MEET_LOBBY_TIMEOUT"] = "300"

        config = _read_runtime_config()
        assert config["url"] == "https://meet.google.com/dop-pel-test"
        assert config["out_dir"] == "/tmp/doppel-meet"
        assert config["guest_name"] == "Doppel Agent"
        assert config["mode"] == "realtime"
        assert config["realtime_api_key"] == "sk-doppel"
        assert config["lobby_timeout"] == "90"
    finally:
        for key, value in old.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
