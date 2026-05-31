"""Tests for website/scripts/extract-skills.py."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
EXTRACTOR = REPO_ROOT / "website" / "scripts" / "extract-skills.py"


@pytest.fixture(scope="module")
def extract_module():
    spec = importlib.util.spec_from_file_location("extract_skills", EXTRACTOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_docs_page_path_uses_doppel_alias_for_legacy_hermes_skill_docs(extract_module):
    path = extract_module._docs_page_path(
        "autonomous-ai-agents/hermes-agent",
        "built-in",
    )
    assert path == "bundled/autonomous-ai-agents/autonomous-ai-agents-doppel-agent"


def test_install_command_is_doppel_first(extract_module):
    cmd = extract_module._install_command("clawhub", "runcomfy-cli", "runcomfy-cli")
    assert cmd == "doppel skills install clawhub/runcomfy-cli"


def test_display_name_prefers_docs_override(extract_module):
    frontmatter = {
        "name": "hermes-agent",
        "metadata": {"hermes": {"docs_display_name": "Doppel Agent"}},
    }
    assert extract_module._display_name(frontmatter, "hermes-agent") == "Doppel Agent"
