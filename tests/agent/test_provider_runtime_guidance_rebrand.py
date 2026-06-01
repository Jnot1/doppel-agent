from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_auxiliary_client_runtime_guidance_prefers_doppel():
    text = _read("agent/auxiliary_client.py")

    assert '"X-Title": "Hermes Agent"' not in text
    assert '"X-Title": "Doppel Agent"' in text
    assert '"User-Agent": "codex_cli_rs/0.0.0 (Hermes Agent)"' not in text
    assert '"User-Agent": "codex_cli_rs/0.0.0 (Doppel Agent)"' in text

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
    assert "(run: hermes auth)." not in text
    assert "(run: doppel auth)." in text
    assert "(run: hermes auth add nous)." not in text
    assert "(run: doppel auth add nous)." in text
    assert "but Nous Portal not configured (run: hermes auth)" not in text
    assert "but Nous Portal not configured (run: doppel auth)" in text


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


def test_compression_and_acp_runtime_guidance_prefers_doppel():
    conversation_compression = _read("agent/conversation_compression.py")
    copilot_acp_client = _read("agent/copilot_acp_client.py")

    assert "Run `hermes setup` or set OPENROUTER_API_KEY." not in conversation_compression
    assert "Run `doppel setup` or set OPENROUTER_API_KEY." in conversation_compression

    assert '"title": "Hermes Agent"' not in copilot_acp_client
    assert '"title": "Doppel Agent"' in copilot_acp_client


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


def test_conversation_loop_and_gemini_runtime_guidance_prefers_doppel():
    conversation_loop = _read("agent/conversation_loop.py")
    gemini_native = _read("agent/gemini_native_adapter.py")

    assert "Ollama runtime context too small for Hermes tool use" not in conversation_loop
    assert "Ollama runtime context too small for Doppel tool use" in conversation_loop
    assert "context, but Hermes needs at least" not in conversation_loop
    assert "context, but Doppel needs at least" in conversation_loop
    assert "tokens. In Hermes config, set `model.ollama_num_ctx: 65536`" not in conversation_loop
    assert "tokens. In Doppel config, set `model.ollama_num_ctx: 65536`" in conversation_loop
    assert "❌ Ollama runtime context is too small for Hermes tool use" not in conversation_loop
    assert "❌ Ollama runtime context is too small for Doppel tool use" in conversation_loop
    assert "request at ~8K tokens. Hermes' system prompt + tool schemas baseline" not in conversation_loop
    assert "request at ~8K tokens. Doppel's system prompt + tool schemas baseline" in conversation_loop
    assert "Use the `copilot` provider with a Copilot subscription token (`hermes" not in conversation_loop
    assert "Use the `copilot` provider with a Copilot subscription token (`doppel" in conversation_loop
    assert "      setup` → GitHub Copilot), or pick any other provider." in conversation_loop

    assert "Re-authenticate: hermes auth add nous" not in conversation_loop
    assert "Re-authenticate: doppel auth add nous" in conversation_loop
    assert "Run `hermes doctor` for credential-chain diagnostics" not in conversation_loop
    assert "Run `doppel doctor` for credential-chain diagnostics" in conversation_loop
    assert "Then run `hermes auth` to re-authenticate." not in conversation_loop
    assert "Then run `doppel auth` to re-authenticate." in conversation_loop
    assert "from `hermes model`." not in conversation_loop
    assert "from `doppel model`." in conversation_loop
    assert "Re-authenticate: hermes auth add nous --type oauth" not in conversation_loop
    assert "Re-authenticate: doppel auth add nous --type oauth" in conversation_loop
    assert "• Is the key valid? Run: hermes setup" not in conversation_loop
    assert "• Is the key valid? Run: doppel setup" in conversation_loop
    assert "hermes fallback add   (interactive picker — same as `hermes model`)" not in conversation_loop
    assert "doppel fallback add   (interactive picker — same as `doppel model`)" in conversation_loop
    assert 'Legacy cleanup: hermes config set ANTHROPIC_TOKEN \\"\\"' not in conversation_loop
    assert 'Legacy cleanup: doppel config set ANTHROPIC_TOKEN \\"\\"' in conversation_loop
    assert 'Clear stale keys: hermes config set ANTHROPIC_API_KEY \\"\\"' not in conversation_loop
    assert 'Clear stale keys: doppel config set ANTHROPIC_API_KEY \\"\\"' in conversation_loop
    assert "(not a Hermes/gateway failure)." not in conversation_loop
    assert "(not a Doppel/gateway failure)." in conversation_loop
    assert "adding a fallback provider with `hermes fallback add`." not in conversation_loop
    assert "adding a fallback provider with `doppel fallback add`." in conversation_loop

    assert "~/.hermes/.env" not in gemini_native
    assert "~/.doppel/.env" in gemini_native
    assert "run `hermes setup`" not in gemini_native
    assert "run `doppel setup`" in gemini_native


def test_google_oauth_runtime_guidance_prefers_doppel():
    google_oauth = _read("agent/google_oauth.py")

    assert "Run `hermes auth add google-gemini-cli` first." not in google_oauth
    assert "Run `doppel auth add google-gemini-cli` first." in google_oauth
