from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


DOC_PATHS = (
    REPO_ROOT / "website/docs/getting-started/installation.md",
    REPO_ROOT / "website/docs/getting-started/updating.md",
    REPO_ROOT / "website/docs/integrations/nous-portal.md",
    REPO_ROOT / "website/docs/guides/run-hermes-with-nous-portal.md",
    REPO_ROOT / "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/installation.md",
    REPO_ROOT / "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/getting-started/updating.md",
    REPO_ROOT / "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/integrations/nous-portal.md",
    REPO_ROOT / "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/guides/run-hermes-with-nous-portal.md",
)


def test_install_and_portal_docs_prefer_doppel_surfaces() -> None:
    corpus = "\n".join(path.read_text(encoding="utf-8") for path in DOC_PATHS)

    required = (
        "DOPPEL_DISABLE_WINDOWS_UTF8=1",
        "~/.doppel/auth.json",
        "~/.doppel/config.yaml",
        "https://github.com/Jnot1/doppel-agent/issues",
        "legacy compatibility",
    )
    for needle in required:
        assert needle in corpus, f"missing expected Doppel-first surface: {needle}"

    forbidden = (
        "HERMES_DISABLE_WINDOWS_UTF8=1",
        "~/.hermes/auth.json",
        "~/.hermes/config.yaml",
        "~/.hermes",
        "$HERMES_HOME",
        "HERMES_HOME",
        "hermes-agent/issues",
        "brew upgrade hermes-agent",
        "pip uninstall hermes-agent",
        "%LOCALAPPDATA%\\hermes",
    )
    for needle in forbidden:
        assert needle not in corpus, f"unexpected legacy customer-facing surface: {needle}"


def test_windows_stdio_disable_flag_prefers_doppel_alias() -> None:
    from hermes_cli import stdio

    original = {k: os.environ.get(k) for k in ("DOPPEL_DISABLE_WINDOWS_UTF8", "HERMES_DISABLE_WINDOWS_UTF8")}
    original_is_windows = stdio.is_windows
    original_configured = stdio._CONFIGURED
    try:
        stdio.is_windows = lambda: True
        stdio._CONFIGURED = False
        os.environ["DOPPEL_DISABLE_WINDOWS_UTF8"] = "1"
        os.environ.pop("HERMES_DISABLE_WINDOWS_UTF8", None)
        changed = stdio.configure_windows_stdio()
        assert changed is False
        assert stdio._CONFIGURED is True

        stdio._CONFIGURED = False
        os.environ.pop("DOPPEL_DISABLE_WINDOWS_UTF8", None)
        os.environ["HERMES_DISABLE_WINDOWS_UTF8"] = "1"
        changed = stdio.configure_windows_stdio()
        assert changed is False
        assert stdio._CONFIGURED is True
    finally:
        stdio.is_windows = original_is_windows
        stdio._CONFIGURED = original_configured
        for key, value in original.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def test_windows_stdio_known_tools_prefer_doppel_paths_and_keep_legacy_fallback(tmp_path: Path) -> None:
    from hermes_cli import stdio

    doppel_git_bin = tmp_path / "doppel" / "git" / "bin"
    doppel_scripts = tmp_path / "doppel" / "doppel-agent" / "venv" / "Scripts"
    legacy_git_bin = tmp_path / "hermes" / "git" / "bin"
    for path in (doppel_git_bin, doppel_scripts, legacy_git_bin):
        path.mkdir(parents=True)

    original_local_appdata = os.environ.get("LOCALAPPDATA")
    original_path = os.environ.get("PATH")
    original_is_windows = stdio.is_windows
    try:
        stdio.is_windows = lambda: True
        os.environ["LOCALAPPDATA"] = str(tmp_path)
        os.environ["PATH"] = "C:\\Windows\\System32"
        stdio._augment_path_with_known_tools()
        path_parts = os.environ["PATH"].split(os.pathsep)
        assert str(doppel_git_bin) in path_parts
        assert str(doppel_scripts) in path_parts
        assert str(legacy_git_bin) in path_parts
        assert path_parts.index(str(doppel_git_bin)) < path_parts.index(str(legacy_git_bin))
        assert path_parts.index(str(doppel_scripts)) < path_parts.index(str(legacy_git_bin))
    finally:
        stdio.is_windows = original_is_windows
        if original_local_appdata is None:
            os.environ.pop("LOCALAPPDATA", None)
        else:
            os.environ["LOCALAPPDATA"] = original_local_appdata
        if original_path is None:
            os.environ.pop("PATH", None)
        else:
            os.environ["PATH"] = original_path
