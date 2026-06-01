from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_prompt_and_runtime_misc_surfaces_prefer_doppel() -> None:
    prompt_builder = _read("agent/prompt_builder.py")
    gemini = _read("agent/gemini_native_adapter.py")
    credential_pool = _read("agent/credential_pool.py")

    assert "of the Hermes process are irrelevant" not in prompt_builder
    assert "of the Doppel Agent process are irrelevant" in prompt_builder

    assert "Hermes keeps ``api_mode='chat_completions'``" not in gemini
    assert "Doppel Agent keeps ``api_mode='chat_completions'``" in gemini
    assert "brittle for Hermes's multi-turn" not in gemini
    assert "brittle for Doppel Agent's multi-turn" in gemini

    assert "``hermes auth status``" not in credential_pool
    assert "``doppel auth status``" in credential_pool
    assert "another Hermes process" not in credential_pool
    assert "another Doppel Agent process" in credential_pool
    assert "`hermes auth add nous --label <name>`" not in credential_pool
    assert "`doppel auth add nous --label <name>`" in credential_pool
    assert "`hermes auth remove openai-codex`" not in credential_pool
    assert "`doppel auth remove openai-codex`" in credential_pool
    assert "Hermes owns its own Codex auth state" not in credential_pool
    assert "Doppel Agent owns its own Codex auth state" in credential_pool
