import sys
from enum import Enum
from types import SimpleNamespace

from cli import HermesCLI


def _make_cli():
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj._attached_images = []
    cli_obj._should_exit = False
    cli_obj._agent_running = False
    cli_obj.session_id = "sess_abc12345"
    cli_obj._session_db = None
    return cli_obj


def test_rollback_disabled_checkpoint_hint_is_doppel_first(capsys):
    cli_obj = _make_cli()
    cli_obj.agent = SimpleNamespace(
        _checkpoint_mgr=SimpleNamespace(enabled=False),
    )

    cli_obj._handle_rollback_command("/rollback")

    out = capsys.readouterr().out
    assert "Enable with: doppel --checkpoints" in out


def test_tool_availability_warning_uses_doppel_setup(monkeypatch):
    cli_obj = _make_cli()
    rendered = []
    cli_obj._console_print = lambda *args, **kwargs: rendered.append(
        " ".join(str(arg) for arg in args)
    )

    monkeypatch.setitem(
        sys.modules,
        "model_tools",
        SimpleNamespace(
            check_tool_availability=lambda: (
                [],
                [
                    {
                        "name": "OpenRouter",
                        "missing_vars": ["OPENROUTER_API_KEY"],
                        "tools": ["web_search"],
                    }
                ],
            )
        ),
    )

    cli_obj._show_tool_availability_warnings()

    assert any("Run 'doppel setup' to configure" in line for line in rendered)


def test_handoff_timeout_hint_uses_doppel_gateway(monkeypatch):
    cli_obj = _make_cli()
    rendered = []
    monkeypatch.setattr("cli._cprint", lambda *args, **kwargs: rendered.append(
        " ".join(str(arg) for arg in args)
    ))

    class FakePlatform(Enum):
        TELEGRAM = "telegram"

    class FakeGatewayConfig:
        def __init__(self):
            self.platforms = {
                FakePlatform.TELEGRAM: SimpleNamespace(enabled=True),
            }

        def get_home_channel(self, platform):
            if platform is FakePlatform.TELEGRAM:
                return SimpleNamespace(name="home", chat_id="123")
            return None

    class FakeSessionDB:
        def get_session(self, _session_id):
            return {"title": "demo-session"}

        def set_session_title(self, _session_id, _title):
            return None

        def request_handoff(self, _session_id, _platform_name):
            return True

        def get_handoff_state(self, _session_id):
            return {"state": "pending"}

        def fail_handoff(self, _session_id, _reason):
            return None

    cli_obj._session_db = FakeSessionDB()

    monkeypatch.setitem(
        sys.modules,
        "hermes_state",
        SimpleNamespace(format_session_db_unavailable=lambda: "db unavailable"),
    )
    monkeypatch.setitem(
        sys.modules,
        "gateway.config",
        SimpleNamespace(
            load_gateway_config=lambda: FakeGatewayConfig(),
            Platform=FakePlatform,
        ),
    )

    times = iter([0.0, 61.0])
    monkeypatch.setattr("time.time", lambda: next(times))
    monkeypatch.setattr("time.sleep", lambda _seconds: None)

    assert cli_obj._handle_handoff_command("/handoff telegram") is True
    assert any("doppel gateway" in line for line in rendered)


def test_gateway_status_start_hint_is_doppel_first(monkeypatch, capsys):
    cli_obj = _make_cli()

    class FakePlatform(Enum):
        TELEGRAM = "telegram"
        DISCORD = "discord"
        SLACK = "slack"
        WHATSAPP = "whatsapp"

    class FakeGatewayConfig:
        def __init__(self):
            self.platforms = {
                FakePlatform.TELEGRAM: SimpleNamespace(enabled=True),
                FakePlatform.DISCORD: SimpleNamespace(enabled=False),
                FakePlatform.SLACK: SimpleNamespace(enabled=False),
                FakePlatform.WHATSAPP: SimpleNamespace(enabled=False),
            }
            self.default_reset_policy = SimpleNamespace(
                mode="daily",
                at_hour=3,
                idle_minutes=60,
            )

        def get_home_channel(self, platform):
            if platform is FakePlatform.TELEGRAM:
                return SimpleNamespace(name="alerts")
            return None

    monkeypatch.setitem(
        sys.modules,
        "gateway.config",
        SimpleNamespace(
            load_gateway_config=lambda: FakeGatewayConfig(),
            Platform=FakePlatform,
        ),
    )

    cli_obj._show_gateway_status()

    out = capsys.readouterr().out
    assert "doppel gateway start" in out


def test_bundles_empty_hint_is_doppel_first(monkeypatch):
    cli_obj = _make_cli()
    rendered = []
    monkeypatch.setattr("cli._cprint", lambda *args, **kwargs: rendered.append(
        " ".join(str(arg) for arg in args)
    ))

    monkeypatch.setitem(
        sys.modules,
        "agent.skill_bundles",
        SimpleNamespace(
            list_bundles=lambda: [],
            _bundles_dir=lambda: "/tmp/bundles",
        ),
    )

    cli_obj._handle_bundles_command("/bundles")

    assert any("doppel bundles create" in line for line in rendered)


def test_bundles_manage_hint_is_doppel_first(monkeypatch):
    cli_obj = _make_cli()
    rendered = []
    monkeypatch.setattr("cli._cprint", lambda *args, **kwargs: rendered.append(
        " ".join(str(arg) for arg in args)
    ))
    monkeypatch.setattr("cli._accent_hex", lambda: "ffffff")

    class DummyConsole:
        def print(self, *args, **kwargs):
            return None

    monkeypatch.setattr("cli.ChatConsole", DummyConsole)
    monkeypatch.setitem(
        sys.modules,
        "agent.skill_bundles",
        SimpleNamespace(
            list_bundles=lambda: [{"slug": "backend-dev", "skills": ["a", "b"], "description": "desc"}],
            _bundles_dir=lambda: "/tmp/bundles",
        ),
    )

    cli_obj._handle_bundles_command("/bundles")

    assert any("Manage with `doppel bundles`" in line for line in rendered)
