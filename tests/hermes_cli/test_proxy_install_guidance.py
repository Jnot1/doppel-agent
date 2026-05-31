from __future__ import annotations

import io
from contextlib import redirect_stderr

import pytest

from hermes_cli.proxy import cli as proxy_cli
from hermes_cli.proxy import server as proxy_server


def test_proxy_cli_missing_aiohttp_guidance_is_doppel_first():
    stream = io.StringIO()
    with redirect_stderr(stream):
        proxy_cli._print_aiohttp_missing()

    output = stream.getvalue()
    assert "cd ~/.doppel/doppel-agent && uv pip install -e '.[messaging]'" in output
    assert "hermes-agent[messaging]" not in output


def test_proxy_server_missing_aiohttp_guidance_is_doppel_first(monkeypatch):
    monkeypatch.setattr(proxy_server, "AIOHTTP_AVAILABLE", False)

    with pytest.raises(RuntimeError) as excinfo:
        proxy_server.create_app(adapter=None)  # type: ignore[arg-type]

    message = str(excinfo.value)
    assert "cd ~/.doppel/doppel-agent && uv pip install -e '.[messaging]'" in message
    assert "hermes-agent[messaging]" not in message
