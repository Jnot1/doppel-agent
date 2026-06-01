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


def test_auth_cli_setup_and_provider_guidance_prefers_doppel() -> None:
    auth_text = AUTH_PY.read_text(encoding="utf-8")

    expected = [
        "Check 'doppel model' for available providers, or run 'doppel doctor' to diagnose config issues.",
        "Config issue detected — run 'doppel doctor' for full diagnostics:",
        "No inference provider configured. Run 'doppel model' to choose a ",
        "OPENAI_API_KEY, etc.) in ~/.doppel/.env.",
        "Spotify client_id is required. Set a Spotify client ID in your agent-home .env or pass --client-id.",
        "<code>doppel auth add xai-oauth</code> to retry.",
        "pip install azure-identity  (or rely on Doppel's ",
        "Run `doppel doctor` to verify token acquisition.",
        "The 'doppel login' command has been removed.",
        "Use 'doppel auth' to manage credentials,",
        "'doppel model' to select a provider, or 'doppel setup' for full setup.",
        "Saved Spotify client ID to ~/.doppel/.env",
    ]
    forbidden = [
        "Check 'hermes model' for available providers, or run 'hermes doctor' to diagnose config issues.",
        "Config issue detected — run 'hermes doctor' for full diagnostics:",
        "No inference provider configured. Run 'hermes model' to choose a ",
        "OPENAI_API_KEY, etc.) in ~/.hermes/.env.",
        "Spotify client_id is required. Set HERMES_SPOTIFY_CLIENT_ID or pass --client-id.",
        "<code>hermes auth add xai-oauth</code> to retry.",
        "pip install azure-identity  (or rely on Hermes' ",
        "Run `hermes doctor` to verify token acquisition.",
        "The 'hermes login' command has been removed.",
        "Use 'hermes auth' to manage credentials,",
        "'hermes model' to select a provider, or 'hermes setup' for full setup.",
        "Saved HERMES_SPOTIFY_CLIENT_ID to ~/.hermes/.env",
    ]

    for needle in expected:
        assert needle in auth_text
    for needle in forbidden:
        assert needle not in auth_text


def test_auth_store_and_status_docstrings_prefer_doppel_customer_facing_copy() -> None:
    auth_text = AUTH_PY.read_text(encoding="utf-8")
    commands_text = AUTH_COMMANDS_PY.read_text(encoding="utf-8")

    expected = [
        "Multi-provider authentication system for Doppel Agent.",
        "is persisted in ~/.doppel/auth.json with cross-process file locking.",
        "instead of prompting the operator to run ``doppel auth``.",
        "# Auth Store — persistence layer for ~/.doppel/auth.json",
        "Once the user runs ``doppel auth login <provider>`` inside",
        "Once the user runs ``doppel auth add <provider>`` inside the profile",
        "and `doppel model` walks users into a broken Qwen setup flow.",
        "Tokens live in ~/.doppel/auth/google_oauth.json",
        '"""Return a status dict for `doppel auth list` / `doppel status`."""',
        "# Spotify auth — PKCE tokens stored in ~/.doppel/auth.json",
        "resulting client_id to ~/.doppel/.env, and return it.",
        "subsequent `doppel auth spotify` runs skip the wizard.",
        "Read Codex OAuth tokens from Doppel auth store (~/.doppel/auth.json).",
        "Saves the new tokens to Doppel auth store automatically.",
        "OAuth flow when the user logged in via ``doppel setup`` / the model",
        "* ``manual:device_code`` — entries created by ``doppel auth add openai-codex``",
        "``doppel auth add`` workaround for #33000",
        '"""Save Codex OAuth tokens to Doppel auth store (~/.doppel/auth.json)."""',
        '"""OpenAI Codex login via device code flow. Tokens stored in ~/.doppel/auth.json."""',
        '"""Persist MiniMax OAuth state to Doppel auth store (~/.doppel/auth.json)."""',
        "output is cached in ``~/.doppel/auth.json``.",
        "re-run `doppel model` to refetch.",
        "Re-running ``doppel model``",
        "`doppel auth` stores credentials",
        "`doppel model` store device_code tokens.",
        "``doppel doctor`` runs the live",
        "``doppel status`` that just want to know",
        "so a new `doppel --profile <name> auth add nous --type oauth` can one-tap",
        "``<doppel-root>/shared/nous_auth.json`` where ``<doppel-root>`` is what",
        "``~/.doppel`` on Linux/macOS,",
        "Linux/macOS classic installs land at ``~/.doppel/shared/``",
        "``doppel auth add nous --label <name>``).  It gets embedded in the",
        "via `doppel auth add nous --type oauth`. Best-",
        "so a re-link after `doppel auth",
    ]
    forbidden = [
        "Multi-provider authentication system for Hermes Agent.",
        "is persisted in ~/.hermes/auth.json with cross-process file locking.",
        "instead of prompting the operator to run ``hermes auth``.",
        "# Auth Store — persistence layer for ~/.hermes/auth.json",
        "Once the user runs ``hermes auth login <provider>`` inside",
        "Once the user runs ``hermes auth add <provider>`` inside the profile",
        "and `hermes model` walks users into a broken Qwen setup flow.",
        "Tokens live in ~/.hermes/auth/google_oauth.json",
        '"""Return a status dict for `hermes auth list` / `hermes status`."""',
        "# Spotify auth — PKCE tokens stored in ~/.hermes/auth.json",
        "resulting client_id to ~/.hermes/.env, and return it.",
        "subsequent `hermes auth spotify` runs skip the wizard.",
        "Read Codex OAuth tokens from Hermes auth store (~/.hermes/auth.json).",
        "Saves the new tokens to Hermes auth store automatically.",
        "OAuth flow when the user logged in via ``hermes setup`` / the model",
        "* ``manual:device_code`` — entries created by ``hermes auth add openai-codex``",
        "``hermes auth add`` workaround for #33000",
        '"""Save Codex OAuth tokens to Hermes auth store (~/.hermes/auth.json)."""',
        '"""OpenAI Codex login via device code flow. Tokens stored in ~/.hermes/auth.json."""',
        '"""Persist MiniMax OAuth state to Hermes auth store (~/.hermes/auth.json)."""',
        "output is cached in ``~/.hermes/auth.json``.",
        "re-run `hermes model` to refetch.",
        "Re-running ``hermes model``",
        "`hermes auth` stores credentials",
        "`hermes model` store device_code tokens.",
        "``hermes doctor`` runs the live",
        "``hermes status`` that just want to know",
        "so a new `hermes --profile <name> auth add nous --type oauth` can one-tap",
        "``<hermes-root>/shared/nous_auth.json`` where ``<hermes-root>`` is what",
        "``~/.hermes`` on Linux/macOS,",
        "Linux/macOS classic installs land at ``~/.hermes/shared/``",
        "``hermes auth add nous --label <name>``).  It gets embedded in the",
        "via `hermes auth add nous --type oauth`. Best-",
        "so a re-link after `hermes auth",
    ]

    for needle in expected:
        assert needle in auth_text or needle in commands_text
    for needle in forbidden:
        assert needle not in auth_text
        assert needle not in commands_text
