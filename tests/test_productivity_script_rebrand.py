from __future__ import annotations

import builtins
import os
import tempfile
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parent.parent
LINEAR_SCRIPT = REPO_ROOT / "skills" / "productivity" / "linear" / "scripts" / "linear_api.py"
GWS_SETUP = REPO_ROOT / "skills" / "productivity" / "google-workspace" / "scripts" / "setup.py"
GWS_API = REPO_ROOT / "skills" / "productivity" / "google-workspace" / "scripts" / "google_api.py"
GWS_BRIDGE = REPO_ROOT / "skills" / "productivity" / "google-workspace" / "scripts" / "gws_bridge.py"
GWS_HOME = REPO_ROOT / "skills" / "productivity" / "google-workspace" / "scripts" / "_hermes_home.py"


def test_productivity_scripts_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (LINEAR_SCRIPT, GWS_SETUP, GWS_API, GWS_BRIDGE, GWS_HOME)
    )

    expected = (
        '"""Google Workspace OAuth2 setup for Doppel Agent.',
        "Run the Google Workspace setup again from this same Doppel profile to refresh consent.",
        "  pip install 'doppel-agent[google]'",
        '"""Copy and validate client_secret.json to the active agent home.',
        'description="Google Workspace OAuth setup for Doppel"',
        '"""Google Workspace API CLI for Doppel Agent.',
        "existing Doppel-facing JSON contract",
        'description="Google Workspace API for Doppel Agent"',
        '"""Bridge between Doppel OAuth token and gws CLI.',
        "Resolve the active agent home for standalone skill scripts.",
        "default: ~/.doppel",
        "or add `LINEAR_API_KEY=lin_api_...` to ~/.doppel/.env",
    )
    stale = (
        '"""Google Workspace OAuth2 setup for Hermes Agent.',
        "Run the Google Workspace setup again from this same Hermes profile to refresh consent.",
        "  pip install 'hermes-agent[google]'",
        '"""Copy and validate client_secret.json to Hermes home.',
        'description="Google Workspace OAuth setup for Hermes"',
        '"""Google Workspace API CLI for Hermes Agent.',
        "existing Hermes-facing JSON contract",
        'description="Google Workspace API for Hermes Agent"',
        '"""Bridge between Hermes OAuth token and gws CLI.',
        "Skill scripts may run outside the Hermes process",
        "default: ~/.hermes",
        "or add `LINEAR_API_KEY=lin_api_...` to ~/.hermes/.env",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined


def test_google_workspace_home_helper_prefers_doppel_with_legacy_fallback():
    source = GWS_HOME.read_text(encoding="utf-8")
    namespace: dict[str, object] = {"__name__": "_test_google_workspace_home"}
    real_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "hermes_constants":
            raise ModuleNotFoundError("forced fallback for test")
        return real_import(name, globals, locals, fromlist, level)

    with patch("builtins.__import__", side_effect=fake_import):
        exec(compile(source, str(GWS_HOME), "exec"), namespace)

    get_hermes_home = namespace["get_hermes_home"]

    with tempfile.TemporaryDirectory() as tmpdir:
        home = Path(tmpdir)
        with patch.object(Path, "home", return_value=home):
            with patch.dict(os.environ, {"DOPPEL_HOME": str(home / "custom-doppel")}, clear=True):
                assert get_hermes_home() == home / "custom-doppel"

            with patch.dict(os.environ, {"HERMES_HOME": str(home / "legacy-hermes")}, clear=True):
                assert get_hermes_home() == home / "legacy-hermes"

            with patch.dict(os.environ, {}, clear=True):
                assert get_hermes_home() == home / ".doppel"

            (home / ".hermes").mkdir()
            with patch.dict(os.environ, {}, clear=True):
                assert get_hermes_home() == home / ".hermes"

            (home / ".doppel").mkdir()
            with patch.dict(os.environ, {}, clear=True):
                assert get_hermes_home() == home / ".doppel"
