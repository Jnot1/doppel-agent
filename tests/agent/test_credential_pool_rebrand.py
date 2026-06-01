from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_credential_pool_guidance_prefers_doppel() -> None:
    source = _read("agent/credential_pool.py")

    assert "via ``hermes auth add``." not in source
    assert "via ``doppel auth add``." in source
    assert "Meanwhile the user may run ``hermes model`` / ``hermes auth``" not in source
    assert "Meanwhile the user may run ``doppel model`` / ``doppel auth``" in source
    assert "When another Hermes process" not in source
    assert "When another Doppel Agent process" in source
    assert "re-authed via `hermes model` / `hermes auth`" not in source
    assert "re-authed via `doppel model` / `doppel auth`" in source
    assert "a fresh `hermes model` ->" not in source
    assert "a fresh `doppel model` ->" in source
    assert "re-add via `hermes auth add %s`" not in source
    assert "re-add via `doppel auth add %s`" in source

    assert "`hermes auth remove <provider> <N>` is stable across all source types." not in source
    assert "`doppel auth remove <provider> <N>` is stable across all source types." in source
    assert "Only auto-discover external credentials (Claude Code, Hermes PKCE)" not in source
    assert "Only auto-discover external credentials (Claude Code, the legacy hermes_pkce source)" in source
    assert "`hermes setup`" not in source
    assert "`doppel setup`" in source
    assert "Prefer ~/.hermes/.env over os.environ" not in source
    assert "Prefer ~/.doppel/.env over os.environ" in source
    assert "that `hermes setup` writes." not in source
    assert "that `doppel setup` writes." in source

    assert "MiniMax OAuth tokens live in ~/.hermes/auth.json providers.minimax-oauth." not in source
    assert "MiniMax OAuth tokens live in ~/.doppel/auth.json providers.minimax-oauth." in source
    assert "standard `hermes auth remove minimax-oauth <N>` flow works." not in source
    assert "standard `doppel auth remove minimax-oauth <N>` flow works." in source
    assert "the Hermes auth store.  Without this gate" not in source
    assert "the Doppel auth store.  Without this gate" in source
    assert "via `hermes auth openai-codex`." not in source
    assert "via `doppel auth openai-codex`." in source
    assert "When the user logs in via ``hermes model`` -> xAI Grok OAuth," not in source
    assert "When the user logs in via ``doppel model`` -> xAI Grok OAuth," in source
    assert "``hermes auth list`` reflects the logged-in state" not in source
    assert "``doppel auth list`` reflects the logged-in state" in source
    assert "authoritative source for Hermes credentials." not in source
    assert "authoritative source for Doppel Agent credentials." in source
    assert "won't be re-seeded from the user's shell environment or ~/.hermes/.env." not in source
    assert "won't be re-seeded from the user's shell environment or ~/.doppel/.env." in source
