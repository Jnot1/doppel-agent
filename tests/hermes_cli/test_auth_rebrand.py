from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from hermes_cli.auth import AuthError, format_auth_error
from hermes_cli.auth_commands import auth_status_command


ROOT = Path(__file__).resolve().parents[2]
AUTH_PY = ROOT / "hermes_cli" / "auth.py"
AUTH_COMMANDS_PY = ROOT / "hermes_cli" / "auth_commands.py"


def test_format_auth_error_relogin_hint_prefers_doppel_model() -> None:
    rendered = format_auth_error(
        AuthError("Session expired.", provider="openai-codex", relogin_required=True)
    )
    assert "`doppel model`" in rendered
    assert "`hermes model`" not in rendered


def test_auth_status_missing_provider_prefers_doppel_example() -> None:
    with pytest.raises(SystemExit) as exc_info:
        auth_status_command(SimpleNamespace(provider=""))

    message = str(exc_info.value)
    assert "`doppel auth status spotify`" in message
    assert "`hermes auth status spotify`" not in message


def test_auth_runtime_copy_prefers_doppel_customer_surfaces() -> None:
    auth_text = AUTH_PY.read_text(encoding="utf-8")
    commands_text = AUTH_COMMANDS_PY.read_text(encoding="utf-8")

    expected_auth = [
        "Run `doppel auth spotify` again.",
        "Run `doppel auth spotify` first.",
        "Run `doppel auth` to authenticate.",
        "Run `doppel auth` to re-authenticate.",
        "Select xAI Grok OAuth (SuperGrok / Premium+) in `doppel model`.",
        "Re-authenticate with `doppel model`.",
        "After subscribing, run `doppel model` again to finish setup.",
        "Run `doppel model` again to switch to Nous Portal.",
        "Doppel will use OpenRouter for inference.",
        "Run `doppel model` or configure an API key to use Doppel.",
        "For health checks, use `doppel auth status`",
        "Re-authenticate with: doppel auth add nous",
    ]
    forbidden_auth = [
        "Run `hermes auth spotify`",
        "Run `hermes auth` to authenticate.",
        "Run `hermes auth` to re-authenticate.",
        "Select xAI Grok OAuth (SuperGrok / Premium+) in `hermes model`.",
        "Re-authenticate with `hermes model`.",
        "After subscribing, run `hermes model` again to finish setup.",
        "Run `hermes model` again to switch to Nous Portal.",
        "Hermes will use OpenRouter for inference.",
        "Run `hermes model` or configure an API key to use Hermes.",
        "For health checks, use `hermes auth status`",
        "Re-authenticate with: hermes auth add nous",
    ]

    for needle in expected_auth:
        assert needle in auth_text
    for needle in forbidden_auth:
        assert needle not in auth_text

    assert "Run `doppel model` and select " in auth_text
    assert "MiniMax (OAuth)." in auth_text
    assert "Run `hermes model` and select " not in auth_text

    assert "`doppel auth add {provider}` is not implemented" in commands_text
    assert "`hermes auth add {provider}` is not implemented" not in commands_text
    assert "`doppel auth status spotify`" in commands_text
    assert "`hermes auth status spotify`" not in commands_text
    assert "when `doppel auth` is called bare." in commands_text
    assert "when `hermes auth` is called bare." not in commands_text
