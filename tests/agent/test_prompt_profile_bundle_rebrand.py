from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_prompt_profile_and_bundle_surfaces_prefer_doppel() -> None:
    system_prompt = _read("agent/system_prompt.py")
    prompt_builder = _read("agent/prompt_builder.py")
    skill_bundles = _read("agent/skill_bundles.py")

    assert "Active Hermes profile: default." not in system_prompt
    assert "Active Doppel profile: default." in system_prompt
    assert "under ~/.hermes/profiles/<name>/." not in system_prompt
    assert "under ~/.doppel/profiles/<name>/." in system_prompt
    assert "Active Hermes profile: {active_profile}." not in system_prompt
    assert "Active Doppel profile: {active_profile}." in system_prompt
    assert "~/.hermes/profiles/{active_profile}/." not in system_prompt
    assert "~/.doppel/profiles/{active_profile}/." in system_prompt
    assert "~/.hermes/skills/, ~/.hermes/plugins/," not in system_prompt
    assert "~/.doppel/skills/, ~/.doppel/plugins/," in system_prompt
    assert "~/.hermes/cron/, ~/.hermes/memories/" not in system_prompt
    assert "~/.doppel/cron/, ~/.doppel/memories/" in system_prompt

    assert "the shared board at `~/.hermes/kanban.db`." not in prompt_builder
    assert "the shared board at `~/.doppel/kanban.db`." in prompt_builder
    assert "- Do not shell out to `hermes kanban <verb>` for board operations." not in prompt_builder
    assert "- Do not shell out to `doppel kanban <verb>` for board operations." in prompt_builder
    assert "scanned alongside the local ``~/.hermes/skills/`` directory." not in prompt_builder
    assert "scanned alongside the local ``~/.doppel/skills/`` directory." in prompt_builder

    assert "Bundles live in ``~/.hermes/skill-bundles/*.yaml``" not in skill_bundles
    assert "Bundles live in ``~/.doppel/skill-bundles/*.yaml``" in skill_bundles
    assert "return rich info for display (``hermes bundles``)" not in skill_bundles
    assert "return rich info for display (``doppel bundles``)" in skill_bundles
    assert "Return the canonical bundles directory under HERMES_HOME." not in skill_bundles
    assert "Return the canonical bundles directory under DOPPEL_HOME." in skill_bundles
    assert "``<HERMES_HOME>/skill-bundles``." not in skill_bundles
    assert "``<DOPPEL_HOME>/skill-bundles``." in skill_bundles
    assert "used by `hermes bundles` CLI subcommand." not in skill_bundles
    assert "used by `doppel bundles` CLI subcommand." in skill_bundles
