from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_skill_and_hook_surfaces_prefer_doppel() -> None:
    skill_commands = _read("agent/skill_commands.py")
    skill_utils = _read("agent/skill_utils.py")
    shell_hooks = _read("agent/shell_hooks.py")

    assert "find a skill via ~/.hermes/skills/<name>" not in skill_commands
    assert "find a skill via ~/.doppel/skills/<name>" in skill_commands
    assert '"""Scan ~/.hermes/skills/ and return a mapping of /command -> skill info.' not in skill_commands
    assert '"""Scan ~/.doppel/skills/ and return a mapping of /command -> skill info.' in skill_commands
    assert "Rescans ``~/.hermes/skills/`` and any ``skills.external_dirs``" not in skill_commands
    assert "Rescans ``~/.doppel/skills/`` and any ``skills.external_dirs``" in skill_commands

    assert "paths that resolve to the local ``~/.hermes/skills/`` are silently skipped." not in skill_utils
    assert "paths that resolve to the local ``~/.doppel/skills/`` are silently skipped." in skill_utils
    assert "Return all skill directories: local ``~/.hermes/skills/`` first, then external." not in skill_utils
    assert "Return all skill directories: local ``~/.doppel/skills/`` first, then external." in skill_utils

    assert "``~/.hermes/shell-hooks-allowlist.json``." not in shell_hooks
    assert "``~/.doppel/shell-hooks-allowlist.json``." in shell_hooks
    assert "Used by ``hermes hooks list`` and ``doctor``." not in shell_hooks
    assert "Used by ``doppel hooks list`` and ``doctor``." in shell_hooks
    assert "used by `hermes hooks` CLI" not in shell_hooks
    assert "used by `doppel hooks` CLI" in shell_hooks
    assert "Used by ``hermes hooks test`` and ``hermes hooks doctor``." not in shell_hooks
    assert "Used by ``doppel hooks test`` and ``doppel hooks doctor``." in shell_hooks
    assert "scripts tested via ``hermes hooks test`` could" not in shell_hooks
    assert "scripts tested via ``doppel hooks test`` could" in shell_hooks
