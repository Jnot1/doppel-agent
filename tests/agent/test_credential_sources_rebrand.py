from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_credential_source_surfaces_prefer_doppel() -> None:
    source = _read("agent/credential_sources.py")

    assert '"""Unified removal contract for every credential source Hermes reads from.' not in source
    assert '"""Unified removal contract for every credential source Doppel Agent reads from.' in source

    assert "env:<VAR>     — os.environ / ~/.hermes/.env" not in source
    assert "env:<VAR>     — os.environ / ~/.doppel/.env" in source
    assert "hermes_pkce   — ~/.hermes/.anthropic_oauth.json" not in source
    assert "hermes_pkce   — ~/.doppel/.anthropic_oauth.json" in source
    assert "manual        — user ran `hermes auth add`" not in source
    assert "manual        — user ran `doppel auth add`" in source
    assert "``hermes auth remove <provider> <N>`` must make the pool entry stay gone." not in source
    assert "``doppel auth remove <provider> <N>`` must make the pool entry stay gone." in source

    assert "1. Var lives only in ~/.hermes/.env  → clear it" not in source
    assert "1. Var lives only in ~/.doppel/.env  → clear it" in source
    assert "We just suppress it so Hermes stops reading it." not in source
    assert "We just suppress it so Doppel Agent stops reading it." in source

    assert '"""~/.hermes/.anthropic_oauth.json is ours — delete it outright."""' not in source
    assert '"""~/.doppel/.anthropic_oauth.json is ours — delete it outright."""' in source
    assert "Cleared Hermes Anthropic OAuth credentials" not in source
    assert "Cleared Doppel Anthropic OAuth credentials" in source

    assert "`hermes auth add nous`" not in source
    assert "`doppel auth add nous`" in source
    assert "``hermes auth remove xai-oauth <N>`` silently undoes" not in source
    assert "``doppel auth remove xai-oauth <N>`` silently undoes" in source
    assert "``hermes auth add openai-codex``" not in source
    assert "``doppel auth add openai-codex``" in source
    assert "the Hermes auth store is not enough" not in source
    assert "the Doppel auth store is not enough" in source

    assert "just suppress so\n    Hermes stops picking the token up." not in source
    assert "just suppress so\n    Doppel Agent stops picking the token up." in source
    assert 'description="~/.hermes/.anthropic_oauth.json"' not in source
    assert 'description="~/.doppel/.anthropic_oauth.json"' in source
