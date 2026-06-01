"""Source-level guards for bounded gateway runtime help copy seams."""

from pathlib import Path


def test_gateway_runtime_kanban_recovery_hints_are_doppel_first():
    runtime = Path("gateway/run.py").read_text(encoding="utf-8")

    assert "doppel kanban init" in runtime
    assert "doppel kanban list --status ready" in runtime
    assert "hermes kanban init" not in runtime
    assert "hermes kanban list --status ready" not in runtime


def test_gateway_runtime_lifecycle_copy_is_doppel_first():
    runtime = Path("gateway/run.py").read_text(encoding="utf-8")

    assert "to retry, or `doppel gateway restart` to restart the gateway." in runtime
    assert "Could not locate doppel binary for detached /restart" in runtime
    assert 'logger.info("Starting Doppel Gateway...")' in runtime
    assert 'thread_name = f"Doppel — {cli_title}"' in runtime
    assert "DOPPEL_HOME=%s" in runtime
    assert "Use 'doppel gateway restart' to replace it, or 'doppel gateway stop' first." in runtime
    assert "Or use 'doppel gateway run --replace' to auto-replace." in runtime

    assert "to retry, or `hermes gateway restart` to restart the gateway." not in runtime
    assert "Could not locate hermes binary for detached /restart" not in runtime
    assert 'logger.info("Starting Hermes Gateway...")' not in runtime
    assert 'thread_name = f"Hermes — {cli_title}"' not in runtime
    assert "HERMES_HOME=%s" not in runtime
    assert "Use 'hermes gateway restart' to replace it, or 'hermes gateway stop' first." not in runtime
    assert "Or use 'hermes gateway run --replace' to auto-replace." not in runtime


def test_platform_runtime_matrix_and_telegram_copy_is_doppel_first():
    matrix = Path("gateway/platforms/matrix.py").read_text(encoding="utf-8")
    telegram = Path("gateway/platforms/telegram.py").read_text(encoding="utf-8")
    web_server = Path("hermes_cli/web_server.py").read_text(encoding="utf-8")

    assert 'device_name="Doppel Agent"' in matrix
    assert 'device_name="Hermes Agent"' not in matrix

    assert "with this token, then restart the gateway with 'doppel gateway restart'." in telegram
    assert "with this token, then restart the gateway with 'hermes gateway restart'." not in telegram

    assert 'app = FastAPI(title="Doppel Agent", version=__version__)' in web_server
    assert 'app = FastAPI(title="Hermes Agent", version=__version__)' not in web_server


def test_platform_runtime_whatsapp_copy_is_doppel_first():
    whatsapp = Path("gateway/platforms/whatsapp.py").read_text(encoding="utf-8")

    assert "install Node.js and re-run `doppel gateway`." in whatsapp
    assert "Run `doppel whatsapp` to pair, or remove WHATSAPP_ENABLED from " in whatsapp
    assert "WhatsApp enabled but not paired — run `doppel whatsapp` to pair." in whatsapp
    assert "If session expired, re-pair: doppel whatsapp" in whatsapp

    assert "install Node.js and re-run `hermes gateway`." not in whatsapp
    assert "Run `hermes whatsapp` to pair, or remove WHATSAPP_ENABLED from " not in whatsapp
    assert "WhatsApp enabled but not paired — run `hermes whatsapp` to pair." not in whatsapp
    assert "If session expired, re-pair: hermes whatsapp" not in whatsapp


def test_gateway_runtime_paths_update_and_stop_help_are_doppel_first():
    runtime = Path("gateway/run.py").read_text(encoding="utf-8")

    expected = [
        "Load environment variables from ~/.doppel/.env first.",
        "Gateway processes are long-lived, so per-turn code reloads ~/.doppel/.env to",
        '"""Load and parse ~/.doppel/config.yaml, returning {} on any error.',
        "checkpoint repos under ~/.doppel/checkpoints/.",
        "the prefill_messages_file key in ~/.doppel/config.yaml.",
        "Relative paths are resolved from ~/.doppel/.",
        "agent.system_prompt in ~/.doppel/config.yaml.",
        "Set GATEWAY_ALLOW_ALL_USERS=true in ~/.doppel/.env to allow open access, ",
        "Spawn `doppel update --gateway` detached so it survives gateway restart.",
        "Windows: no bash/setsid chain.  Run `doppel update --gateway`",
        '"""Watch ``doppel update --gateway``, streaming output + forwarding prompts.',
        "Planned stop check: service managers and `doppel gateway stop`",
        "on Windows, so `doppel gateway stop`'s SIGTERM",
        "The fix is a marker-polling thread: `doppel gateway stop` writes the",
        "- doppel update killing the gateway mid-work",
        "`doppel gateway stop` and interactive Ctrl+C are handled above as",
    ]
    forbidden = [
        "Load environment variables from ~/.hermes/.env first.",
        "Gateway processes are long-lived, so per-turn code reloads ~/.hermes/.env to",
        '"""Load and parse ~/.hermes/config.yaml, returning {} on any error.',
        "checkpoint repos under ~/.hermes/checkpoints/.",
        "the prefill_messages_file key in ~/.hermes/config.yaml.",
        "Relative paths are resolved from ~/.hermes/.",
        "agent.system_prompt in ~/.hermes/config.yaml.",
        "Set GATEWAY_ALLOW_ALL_USERS=true in ~/.hermes/.env to allow open access, ",
        "Spawn `hermes update --gateway` detached so it survives gateway restart.",
        "Windows: no bash/setsid chain.  Run `hermes update --gateway`",
        '"""Watch ``hermes update --gateway``, streaming output + forwarding prompts.',
        "Planned stop check: service managers and `hermes gateway stop`",
        "on Windows, so `hermes gateway stop`'s SIGTERM",
        "The fix is a marker-polling thread: `hermes gateway stop` writes the",
        "- hermes update killing the gateway mid-work",
        "`hermes gateway stop` and interactive Ctrl+C are handled above as",
    ]

    for needle in expected:
        assert needle in runtime
    for needle in forbidden:
        assert needle not in runtime


def test_gateway_runtime_remaining_operator_guidance_is_doppel_first():
    runtime = Path("gateway/run.py").read_text(encoding="utf-8")

    expected = [
        "`doppel setup` run) silently shadow the user's current config.",
        "(e.g. user ran `doppel auth add openai-codex` without `doppel model`),",
        "``doppel setup``, their unit file may still encode the old",
        "This prevents unwanted auto-resets after `doppel update`,",
        "`doppel gateway restart`, or `/restart`.",
        "never runs when ``doppel gateway stop`` signals the gateway. The",
    ]
    forbidden = [
        "`hermes setup` run) silently shadow the user's current config.",
        "(e.g. user ran `hermes auth add openai-codex` without `hermes model`),",
        "``hermes setup``, their unit file may still encode the old",
        "This prevents unwanted auto-resets after `hermes update`,",
        "`hermes gateway restart`, or `/restart`.",
        "never runs when ``hermes gateway stop`` signals the gateway. The",
    ]

    for needle in expected:
        assert needle in runtime
    for needle in forbidden:
        assert needle not in runtime
