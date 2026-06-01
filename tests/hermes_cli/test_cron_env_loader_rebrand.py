from pathlib import Path


def test_cron_and_env_loader_surfaces_prefer_doppel() -> None:
    expectations = {
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/cron.py": {
            "required": [
                "Cron subcommand for doppel CLI.",
                "Usage: doppel cron [list|create|edit|pause|resume|run|remove|status|tick]",
            ],
            "forbidden": [
                "Cron subcommand for hermes CLI.",
                "Usage: hermes cron [list|create|edit|pause|resume|run|remove|status|tick]",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/env_loader.py": {
            "required": [
                "Helpers for loading Doppel .env files consistently across entrypoints.",
                "Used by setup / `doppel model` flows to label detected credentials so",
                "already knows all valid Doppel env-var names and can split",
                "Load Doppel environment files with user config taking precedence.",
                "- `~/.doppel/.env` overrides stale shell-exported values when present.",
                "locate the access token) but BEFORE the rest of Doppel reads",
                "(tests, future ``doppel secrets bitwarden sync`` from a long-running",
                "Remember where these came from so the setup / `doppel model`",
            ],
            "forbidden": [
                "Helpers for loading Hermes .env files consistently across entrypoints.",
                "Used by setup / `hermes model` flows to label detected credentials so",
                "already knows all valid Hermes env-var names and can split",
                "Load Hermes environment files with user config taking precedence.",
                "- `~/.hermes/.env` overrides stale shell-exported values when present.",
                "locate the access token) but BEFORE the rest of Hermes reads",
                "(tests, future ``hermes secrets bitwarden sync`` from a long-running",
                "Remember where these came from so the setup / `hermes model`",
            ],
        },
    }

    for path_str, expected in expectations.items():
        text = Path(path_str).read_text(encoding="utf-8")
        for snippet in expected["required"]:
            assert snippet in text, f"{path_str}: missing {snippet!r}"
        for snippet in expected["forbidden"]:
            assert snippet not in text, f"{path_str}: forbidden {snippet!r}"
