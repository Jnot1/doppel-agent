from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_provider_plugin_surfaces_prefer_doppel() -> None:
    browser_provider = _read("agent/browser_provider.py")
    web_search_provider = _read("agent/web_search_provider.py")
    image_gen_provider = _read("agent/image_gen_provider.py")
    video_gen_provider = _read("agent/video_gen_provider.py")
    tts_provider = _read("agent/tts_provider.py")
    transcription_provider = _read("agent/transcription_provider.py")
    web_search_registry = _read("agent/web_search_registry.py")
    image_gen_registry = _read("agent/image_gen_registry.py")
    video_gen_registry = _read("agent/video_gen_registry.py")
    browser_registry = _read("agent/browser_registry.py")

    assert "``~/.hermes/plugins/browser/<name>/``" not in browser_provider
    assert "``~/.doppel/plugins/browser/<name>/``" in browser_provider
    assert "``hermes tools``" not in browser_provider
    assert "``doppel tools``" in browser_provider

    assert "``~/.hermes/plugins/web/<name>/``" not in web_search_provider
    assert "``~/.doppel/plugins/web/<name>/``" in web_search_provider
    assert "``hermes tools``" not in web_search_provider
    assert "``doppel tools``" in web_search_provider

    assert "``~/.hermes/plugins/image_gen/<name>/``" not in image_gen_provider
    assert "``~/.doppel/plugins/image_gen/<name>/``" in image_gen_provider
    assert "``hermes tools``" not in image_gen_provider
    assert "``doppel tools``" in image_gen_provider
    assert "``$HERMES_HOME/cache/images/``" not in image_gen_provider
    assert "``$DOPPEL_HOME/cache/images/``" in image_gen_provider

    assert "``~/.hermes/plugins/video_gen/<name>/``" not in video_gen_provider
    assert "``~/.doppel/plugins/video_gen/<name>/``" in video_gen_provider
    assert "``hermes tools``" not in video_gen_provider
    assert "``doppel tools``" in video_gen_provider
    assert "``$HERMES_HOME/cache/videos/``" not in video_gen_provider
    assert "``$DOPPEL_HOME/cache/videos/``" in video_gen_provider

    assert "CLI into Hermes with shell-template placeholders." not in tts_provider
    assert "CLI into Doppel with shell-template placeholders." in tts_provider
    assert "``~/.hermes/plugins/tts/<name>/``" not in tts_provider
    assert "``~/.doppel/plugins/tts/<name>/``" in tts_provider
    assert "``hermes tools``" not in tts_provider
    assert "``doppel tools``" in tts_provider
    assert "``hermes setup``" not in tts_provider
    assert "``doppel setup``" in tts_provider
    assert "the rest of Hermes" not in tts_provider
    assert "the rest of Doppel" in tts_provider

    assert "``~/.hermes/plugins/transcription/<name>/``" not in transcription_provider
    assert "``~/.doppel/plugins/transcription/<name>/``" in transcription_provider
    assert "``hermes tools``" not in transcription_provider
    assert "``doppel tools``" in transcription_provider
    assert "``hermes setup``" not in transcription_provider
    assert "``doppel setup``" in transcription_provider

    assert "``hermes tools``" not in web_search_registry
    assert "``doppel tools``" in web_search_registry
    assert "``hermes tools``" not in image_gen_registry
    assert "``doppel tools``" in image_gen_registry
    assert "``hermes tools``" not in video_gen_registry
    assert "``doppel tools``" in video_gen_registry

    assert "``~/.hermes/plugins/browser/<vendor>/``" not in browser_registry
    assert "``~/.doppel/plugins/browser/<vendor>/``" in browser_registry
