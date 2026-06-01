"""Tests for agent.i18n -- catalog parity, fallback, language resolution."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from agent import i18n


LOCALES_DIR = Path(__file__).resolve().parents[2] / "locales"


def _load_raw(lang: str) -> dict:
    with (LOCALES_DIR / f"{lang}.yaml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _flatten(d, prefix="") -> dict:
    flat = {}
    for k, v in (d or {}).items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            flat.update(_flatten(v, key))
        else:
            flat[key] = v
    return flat


# ---------------------------------------------------------------------------
# Catalog completeness -- this is the key invariant test.  If someone adds a
# new key to en.yaml they MUST add it to every other locale, else runtime
# falls back to English for those users and defeats the feature.
# ---------------------------------------------------------------------------

def test_all_locales_exist():
    """Every supported language must have a catalog file on disk."""
    for lang in i18n.SUPPORTED_LANGUAGES:
        assert (LOCALES_DIR / f"{lang}.yaml").is_file(), f"missing locales/{lang}.yaml"


@pytest.mark.parametrize("lang", [l for l in i18n.SUPPORTED_LANGUAGES if l != "en"])
def test_catalog_keys_match_english(lang: str):
    """Every non-English catalog must have exactly the same key set as English."""
    en_keys = set(_flatten(_load_raw("en")).keys())
    lang_keys = set(_flatten(_load_raw(lang)).keys())
    missing = en_keys - lang_keys
    extra = lang_keys - en_keys
    assert not missing, f"{lang}.yaml missing keys: {sorted(missing)}"
    assert not extra, f"{lang}.yaml has keys not in en.yaml: {sorted(extra)}"


@pytest.mark.parametrize("lang", list(i18n.SUPPORTED_LANGUAGES))
def test_catalog_placeholders_match_english(lang: str):
    """Every translated value must use the same {placeholder} tokens as English.

    A mistranslated placeholder (e.g. ``{description}`` typoed as ``{descricao}``)
    would either raise KeyError at runtime or silently drop the interpolated
    value.  Pin parity at the test layer.
    """
    import re
    placeholder_re = re.compile(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}")
    en_flat = _flatten(_load_raw("en"))
    lang_flat = _flatten(_load_raw(lang))
    for key, en_value in en_flat.items():
        en_placeholders = set(placeholder_re.findall(en_value))
        lang_value = lang_flat.get(key, "")
        lang_placeholders = set(placeholder_re.findall(lang_value))
        assert en_placeholders == lang_placeholders, (
            f"{lang}.yaml key={key!r}: placeholders {lang_placeholders} "
            f"don't match English {en_placeholders}"
        )


# ---------------------------------------------------------------------------
# Language resolution
# ---------------------------------------------------------------------------

def test_normalize_lang_accepts_supported():
    assert i18n._normalize_lang("zh") == "zh"
    assert i18n._normalize_lang("EN") == "en"


def test_normalize_lang_accepts_aliases():
    assert i18n._normalize_lang("chinese") == "zh"
    assert i18n._normalize_lang("zh-CN") == "zh"
    assert i18n._normalize_lang("Deutsch") == "de"
    assert i18n._normalize_lang("español") == "es"
    assert i18n._normalize_lang("jp") == "ja"
    assert i18n._normalize_lang("Ukrainian") == "uk"
    assert i18n._normalize_lang("uk-UA") == "uk"
    assert i18n._normalize_lang("ua") == "uk"
    assert i18n._normalize_lang("Turkish") == "tr"
    assert i18n._normalize_lang("tr-TR") == "tr"
    assert i18n._normalize_lang("türkçe") == "tr"


def test_normalize_lang_unknown_falls_back():
    assert i18n._normalize_lang("klingon") == "en"
    assert i18n._normalize_lang("") == "en"
    assert i18n._normalize_lang(None) == "en"


def test_env_var_override(monkeypatch):
    """HERMES_LANGUAGE wins over config."""
    i18n.reset_language_cache()
    monkeypatch.setenv("HERMES_LANGUAGE", "ja")
    assert i18n.get_language() == "ja"


def test_env_var_normalized(monkeypatch):
    i18n.reset_language_cache()
    monkeypatch.setenv("HERMES_LANGUAGE", "Chinese")
    assert i18n.get_language() == "zh"


def test_default_when_nothing_set(monkeypatch):
    """With no env var and no config override, falls back to English."""
    monkeypatch.delenv("HERMES_LANGUAGE", raising=False)
    # Force config lookup to return None -- patch the cached reader.
    i18n.reset_language_cache()
    monkeypatch.setattr(i18n, "_config_language_cached", lambda: None)
    assert i18n.get_language() == "en"


# ---------------------------------------------------------------------------
# t() semantics
# ---------------------------------------------------------------------------

def test_t_explicit_lang():
    assert i18n.t("approval.denied", lang="en").endswith("Denied")
    assert i18n.t("approval.denied", lang="zh").endswith("已拒绝")
    assert i18n.t("approval.denied", lang="uk").endswith("Відхилено")
    assert i18n.t("approval.denied", lang="tr").endswith("Reddedildi")


def test_t_formats_placeholders():
    msg = i18n.t("gateway.draining", lang="en", count=3)
    assert "3" in msg


def test_t_missing_key_returns_key():
    """A missing key returns its own path -- ugly but never crashes."""
    result = i18n.t("nonexistent.key.path", lang="en")
    assert result == "nonexistent.key.path"


def test_t_missing_key_in_non_english_falls_back_to_english(tmp_path, monkeypatch):
    """If a key exists in English but not in the target locale, fall back."""
    # Stand up a fake incomplete locale under a temp locales dir.
    fake_locales = tmp_path / "locales"
    fake_locales.mkdir()
    (fake_locales / "en.yaml").write_text("foo: English Foo\n", encoding="utf-8")
    (fake_locales / "zh.yaml").write_text("# intentionally empty\n", encoding="utf-8")
    monkeypatch.setattr(i18n, "_locales_dir", lambda: fake_locales)
    i18n.reset_language_cache()
    try:
        assert i18n.t("foo", lang="zh") == "English Foo"
    finally:
        # Clear the cache on teardown so subsequent tests don't see the
        # fake "foo: English Foo" catalog instead of the real locales/*.yaml.
        i18n.reset_language_cache()


def test_t_unknown_language_uses_english():
    """Unknown lang codes normalize to English, not to a key-path fallback."""
    assert i18n.t("approval.denied", lang="klingon") == i18n.t("approval.denied", lang="en")


@pytest.mark.parametrize(
    "lang",
    ["en", "af", "zh-hant", "es", "ga", "fr", "de", "hu", "it", "ja", "ko", "pt", "ru", "tr", "uk", "zh"],
)
def test_gateway_customer_facing_locale_slice_prefers_doppel(lang: str):
    help_header = i18n.t("gateway.help.header", lang=lang)
    assert "Doppel" in help_header
    assert "Hermes" not in help_header

    debug_hint = i18n.t("gateway.debug.full_logs_hint", lang=lang)
    assert "`doppel debug share`" in debug_hint
    assert "`hermes debug share`" not in debug_hint

    share_hint = i18n.t("gateway.debug.share_hint", lang=lang)
    assert "Doppel" in share_hint
    assert "Hermes" not in share_hint

    status_header = i18n.t("gateway.status.header", lang=lang)
    assert "Doppel" in status_header
    assert "Hermes" not in status_header

    thread_ready = i18n.t("gateway.topic.thread_ready", lang=lang)
    assert "Doppel" in thread_ready
    assert "Hermes" not in thread_ready

    restart_notice = i18n.t("gateway.restart.restarting", lang=lang)
    assert "`doppel gateway restart`" in restart_notice
    assert "`hermes gateway restart`" not in restart_notice

    kanban_suffix = i18n.t("gateway.kanban.truncated_suffix", lang=lang)
    assert "`doppel kanban" in kanban_suffix
    assert "`hermes kanban" not in kanban_suffix

    update_platform = i18n.t("gateway.update.platform_not_messaging", lang=lang)
    assert "`doppel update`" in update_platform
    assert "`hermes update`" not in update_platform

    update_missing = i18n.t("gateway.update.hermes_cmd_not_found", lang=lang)
    assert "`doppel`" in update_missing
    assert "`hermes`" not in update_missing
    assert "Doppel" in update_missing
    assert "Hermes" not in update_missing

    update_starting = i18n.t("gateway.update.starting", lang=lang)
    assert "Doppel" in update_starting
    assert "Hermes" not in update_starting
