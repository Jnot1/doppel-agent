from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_auxiliary_client_runtime_guidance_prefers_doppel():
    text = _read("agent/auxiliary_client.py")

    assert "Run `hermes setup` or `hermes model` and enter a valid http(s) base URL." not in text
    assert "Run `doppel setup` or `doppel model` and enter a valid http(s) base URL." in text
    assert "Run: hermes model to reconfigure" not in text
    assert "Run: doppel model to reconfigure" in text
    assert "but no Codex OAuth token found (run: hermes model)" not in text
    assert "but no Codex OAuth token found (run: doppel model)" in text
    assert "run: hermes model -> xAI Grok OAuth — SuperGrok / Premium+" not in text
    assert "run: doppel model -> xAI Grok OAuth — SuperGrok / Premium+" in text
    assert "switch to a different provider with `hermes model`." not in text
    assert "switch to a different provider with `doppel model`." in text
    assert "Run: hermes setup" not in text
    assert "Run: doppel setup" in text


def test_agent_init_and_backend_helper_guidance_prefers_doppel():
    agent_init = _read("agent/agent_init.py")
    backend_helpers = _read("tools/tool_backend_helpers.py")

    assert "switch to a different provider with `hermes model`." not in agent_init
    assert "switch to a different provider with `doppel model`." in agent_init
    assert "No LLM provider configured. Run `hermes model`" not in agent_init
    assert "No LLM provider configured. Run `doppel model`" in agent_init
    assert "run `hermes setup` for first-time " not in agent_init
    assert "run `doppel setup` for first-time " in agent_init

    assert "Run `hermes model` to refresh your " not in backend_helpers
    assert "Run `doppel model` to refresh your " in backend_helpers
    assert "Nous Portal login and billing status." in backend_helpers


def test_xai_and_tts_runtime_guidance_prefers_doppel():
    x_search = _read("tools/x_search_tool.py")
    transcription = _read("tools/transcription_tools.py")
    tts = _read("tools/tts_tool.py")

    assert "Run `hermes auth add xai-oauth`" not in x_search
    assert "Run `doppel auth add xai-oauth`" in x_search

    assert "Configure xAI OAuth in `hermes model` or set XAI_API_KEY" not in transcription
    assert "Configure xAI OAuth in `doppel model` or set XAI_API_KEY" in transcription

    assert "Configure xAI OAuth in `hermes model` or set XAI_API_KEY." not in tts
    assert "Configure xAI OAuth in `doppel model` or set XAI_API_KEY." in tts
    assert "Run hermes setup and choose NeuTTS" not in tts
    assert "Run doppel setup and choose NeuTTS" in tts
    assert "Run 'hermes setup tts' and choose KittenTTS" not in tts
    assert "Run 'doppel setup tts' and choose KittenTTS" in tts
    assert "Run 'hermes tools' and select Piper under TTS" not in tts
    assert "Run 'doppel tools' and select Piper under TTS" in tts
