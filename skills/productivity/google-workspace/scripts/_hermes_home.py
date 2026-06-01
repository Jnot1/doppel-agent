"""Resolve the active agent home for standalone skill scripts.

Skill scripts may run outside the Doppel process (e.g. system Python,
nix env, CI) where ``hermes_constants`` is not importable.  This module
provides the same ``get_hermes_home()`` and ``display_hermes_home()``
contracts as ``hermes_constants`` without requiring it on ``sys.path``.

When ``hermes_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``hermes_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``DOPPEL_HOME`` / ``HERMES_HOME`` lookup pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from hermes_constants import display_hermes_home as display_hermes_home
    from hermes_constants import get_hermes_home as get_hermes_home
except (ModuleNotFoundError, ImportError):

    def _select_native_home_root() -> Path:
        preferred = Path.home() / ".doppel"
        legacy = Path.home() / ".hermes"
        if preferred.exists():
            return preferred
        if legacy.exists():
            return legacy
        return preferred

    def get_hermes_home() -> Path:
        """Return the active agent home directory (default: ~/.doppel).

        Mirrors ``hermes_constants.get_hermes_home()``."""
        preferred = os.environ.get("DOPPEL_HOME", "").strip()
        legacy = os.environ.get("HERMES_HOME", "").strip()
        if preferred:
            return Path(preferred)
        if legacy:
            return Path(legacy)
        return _select_native_home_root()

    def display_hermes_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``hermes_constants.display_hermes_home()``."""
        home = get_hermes_home()
        try:
            return "~/" + str(home.relative_to(Path.home()))
        except ValueError:
            return str(home)
