from types import SimpleNamespace

from hermes_cli import portal_cli


class _FeatureList:
    def __init__(self, items):
        self._items = items

    def items(self):
        return list(self._items)


def test_portal_status_shows_shared_docs_and_signup_urls(monkeypatch, capsys):
    monkeypatch.setattr("hermes_cli.portal_cli.load_config", lambda: {})
    monkeypatch.setattr("hermes_cli.auth.get_nous_auth_status", lambda: {})
    monkeypatch.setattr(
        "hermes_cli.nous_subscription.get_nous_subscription_features",
        lambda _cfg: _FeatureList([
            SimpleNamespace(
                label="Web search",
                managed_by_nous=False,
                active=False,
                current_provider=None,
            )
        ]),
    )

    assert portal_cli._cmd_status(SimpleNamespace()) == 0
    out = capsys.readouterr().out
    assert portal_cli.DOCS_URL in out
    assert portal_cli.SUBSCRIPTION_URL in out
    assert "Login:   doppel auth add nous --type oauth" in out


def test_portal_status_uses_doppel_model_hint(monkeypatch, capsys):
    monkeypatch.setattr("hermes_cli.portal_cli.load_config", lambda: {"model": {"provider": "openrouter"}})
    monkeypatch.setattr("hermes_cli.auth.get_nous_auth_status", lambda: {"logged_in": True})
    monkeypatch.setattr(
        "hermes_cli.nous_subscription.get_nous_subscription_features",
        lambda _cfg: _FeatureList([
            SimpleNamespace(
                label="Web search",
                managed_by_nous=False,
                active=False,
                current_provider=None,
            )
        ]),
    )

    assert portal_cli._cmd_status(SimpleNamespace()) == 0
    out = capsys.readouterr().out
    assert "currently openrouter (switch with `doppel model`)" in out
