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
