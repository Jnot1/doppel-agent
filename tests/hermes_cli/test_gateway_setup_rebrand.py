"""Focused rebrand guards for gateway and setup CLI help surfaces."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_cli_module_docstring_prefers_doppel_customer_facing_commands() -> None:
    text = (REPO_ROOT / "hermes_cli" / "__init__.py").read_text(encoding="utf-8")

    expected = [
        "Doppel CLI - Unified command-line interface for Doppel Agent.",
        "- doppel gateway       - Run gateway in foreground",
        "- doppel gateway start - Start gateway service",
        "- doppel gateway stop  - Stop gateway service",
        "- doppel setup         - Interactive setup wizard",
        "- doppel status        - Show status of all components",
        "- doppel cron          - Manage cron jobs",
    ]
    forbidden = [
        "Hermes CLI - Unified command-line interface for Hermes Agent.",
        "- hermes gateway       - Run gateway in foreground",
        "- hermes gateway start - Start gateway service",
        "- hermes gateway stop  - Stop gateway service",
        "- hermes setup         - Interactive setup wizard",
        "- hermes status        - Show status of all components",
        "- hermes cron          - Manage cron jobs",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text


def test_gateway_module_help_docstrings_prefer_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "gateway.py").read_text(encoding="utf-8")

    expected = [
        "Gateway subcommand for Doppel CLI.",
        "Handles: doppel gateway [run|start|stop|restart|status|install|uninstall|setup]",
        "``doppel gateway status`` output",
        "Foreground ``doppel gateway run`` must remain interruptible",
        "For ``~/.doppel/profiles/<name>``, returns ``\"--profile <name>\"``.",
        "Default ``~/.doppel`` returns ``doppel-gateway``.",
        "Profile ``~/.doppel/profiles/coder`` returns ``doppel-gateway-coder``.",
        "Default ``~/.doppel`` → ``ai.doppel.gateway.plist``.",
        "Profile ``~/.doppel/profiles/coder`` → ``ai.doppel.gateway-coder.plist``.",
        "/opt/hermes/docker/entrypoint.sh before the Doppel command.",
        "``doppel setup gateway`` without needing the gateway to be running.",
        "Users who want Matrix on Windows can run Doppel under",
    ]
    forbidden = [
        "Gateway subcommand for hermes CLI.",
        "Handles: hermes gateway [run|start|stop|restart|status|install|uninstall|setup]",
        "``hermes gateway status`` output",
        "Foreground ``hermes gateway run`` must remain interruptible",
        "For ``~/.hermes/profiles/<name>``, returns ``\"--profile <name>\"``.",
        "Default ``~/.hermes`` returns ``doppel-gateway``.",
        "Profile ``~/.hermes/profiles/coder`` returns ``doppel-gateway-coder``.",
        "Default ``~/.hermes`` → ``ai.doppel.gateway.plist``.",
        "Profile ``~/.hermes/profiles/coder`` → ``ai.doppel.gateway-coder.plist``.",
        "/opt/hermes/docker/entrypoint.sh before the Hermes command.",
        "``hermes setup gateway`` without needing the gateway to be running.",
        "Users who want Matrix on Windows can run hermes under",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text


def test_setup_module_help_and_warnings_prefer_doppel_customer_facing_copy() -> None:
    text = (REPO_ROOT / "hermes_cli" / "setup.py").read_text(encoding="utf-8")

    expected = [
        "Config files are stored in ~/.doppel/ for easy access.",
        "Video generation — opt-in via `doppel tools` → Video Generation.",
        "Delegates to ``cmd_model()`` (the same flow used by ``doppel model``)",
        "provider added to ``doppel model`` is automatically available here.",
        "through ``doppel model`` -> xAI Grok OAuth (SuperGrok / Premium+).",
        "Direct OpenAI credentials are still configured and may take precedence until removed from ~/.doppel/.env.",
        "Both `doppel setup tools` and `doppel tools` use the same flow:",
        "that gets a brand-new user from zero to a fully working Doppel session",
        "the user can customize later via ``doppel setup <section>``.",
    ]
    forbidden = [
        "Config files are stored in ~/.hermes/ for easy access.",
        "Video generation — opt-in via `hermes tools` → Video Generation.",
        "Delegates to ``cmd_model()`` (the same flow used by ``hermes model``)",
        "provider added to ``hermes model`` is automatically available here.",
        "through ``hermes model`` -> xAI Grok OAuth (SuperGrok / Premium+).",
        "Direct OpenAI credentials are still configured and may take precedence until removed from ~/.hermes/.env.",
        "Both `hermes setup tools` and `hermes tools` use the same flow:",
        "that gets a brand-new user from zero to a fully working Hermes session",
        "the user can customize later via ``hermes setup <section>``.",
    ]

    for needle in expected:
        assert needle in text
    for needle in forbidden:
        assert needle not in text
