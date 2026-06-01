from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from hermes_cli import main as main_mod
from hermes_cli import profile_distribution as dist_mod
from hermes_cli import profiles as profiles_mod
import hermes_constants


@pytest.fixture
def isolated_home(tmp_path, monkeypatch):
    monkeypatch.setenv("DOPPEL_HOME", str(tmp_path / ".doppel"))
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / ".doppel"))
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    return tmp_path


def _dist_plan(name: str, version: str, target_dir: Path, *, has_cron: bool) -> SimpleNamespace:
    return SimpleNamespace(
        manifest=SimpleNamespace(name=name, version=version, env_requires=[]),
        target_dir=target_dir,
        has_cron=has_cron,
    )


def test_cmd_profile_status_alias_hint_uses_doppel_flag(monkeypatch, capsys, isolated_home):
    row = SimpleNamespace(
        name="coder",
        is_default=False,
        model="opus",
        provider="openai",
        gateway_running=True,
        skill_count=3,
        alias_path=Path("/tmp/coder"),
    )
    monkeypatch.setattr(profiles_mod, "get_active_profile_name", lambda: "coder")
    monkeypatch.setattr(profiles_mod, "list_profiles", lambda: [row])
    monkeypatch.setattr(
        hermes_constants,
        "display_hermes_home",
        lambda: "~/.doppel/profiles/coder",
    )

    main_mod.cmd_profile(SimpleNamespace(profile_action=None))

    out = capsys.readouterr().out
    assert "Alias:          coder → doppel -p coder" in out


def test_cmd_profile_use_default_shows_current_root(monkeypatch, capsys, isolated_home):
    monkeypatch.setattr(profiles_mod, "set_active_profile", lambda name: None)
    monkeypatch.setattr(hermes_constants, "display_hermes_home", lambda: "~/.hermes")

    main_mod.cmd_profile(SimpleNamespace(profile_action="use", profile_name="default"))

    out = capsys.readouterr().out
    assert "Switched to: default (~/.hermes)" in out


def test_cmd_profile_create_collision_guidance_uses_doppel_commands(
    monkeypatch, capsys, isolated_home
):
    profile_dir = isolated_home / ".doppel" / "profiles" / "coder"
    monkeypatch.setattr(profiles_mod, "create_profile", lambda **kwargs: profile_dir)
    monkeypatch.setattr(profiles_mod, "seed_profile_skills", lambda _p: {"copied": []})
    monkeypatch.setattr(profiles_mod, "check_alias_collision", lambda name: "already on PATH")

    args = SimpleNamespace(
        profile_action="create",
        profile_name="coder",
        clone=False,
        clone_all=False,
        clone_from=None,
        no_alias=False,
        no_skills=False,
        description=None,
    )
    main_mod.cmd_profile(args)

    out = capsys.readouterr().out
    assert "doppel profile alias coder --name <custom>" in out
    assert "doppel -p coder chat" in out


def test_cmd_profile_show_distribution_hint_uses_doppel_profile_info(
    monkeypatch, capsys, isolated_home
):
    profile_dir = isolated_home / ".doppel" / "profiles" / "coder"
    monkeypatch.setattr(profiles_mod, "profile_exists", lambda name: True)
    monkeypatch.setattr(profiles_mod, "get_profile_dir", lambda name: profile_dir)
    monkeypatch.setattr(profiles_mod, "_read_config_model", lambda _p: (None, None))
    monkeypatch.setattr(profiles_mod, "_check_gateway_running", lambda _p: False)
    monkeypatch.setattr(profiles_mod, "_count_skills", lambda _p: 0)
    monkeypatch.setattr(
        profiles_mod,
        "_read_distribution_meta",
        lambda _p: ("demo", "1.2.3", "git+https://example.com/demo.git"),
    )
    monkeypatch.setattr(profiles_mod, "_get_wrapper_dir", lambda: isolated_home / ".local" / "bin")

    main_mod.cmd_profile(SimpleNamespace(profile_action="show", profile_name="coder"))

    out = capsys.readouterr().out
    assert "`doppel profile info coder`" in out


def test_cmd_profile_install_distribution_guidance_uses_doppel_profile_flag(
    monkeypatch, capsys, isolated_home
):
    plan = _dist_plan("demo", "1.0.0", isolated_home / ".doppel" / "profiles" / "demo", has_cron=True)
    monkeypatch.setattr(dist_mod, "plan_install", lambda *args, **kwargs: plan)
    monkeypatch.setattr(dist_mod, "install_distribution", lambda *args, **kwargs: plan)
    monkeypatch.setattr(main_mod, "_render_distribution_plan", lambda _plan: None)

    args = SimpleNamespace(
        profile_action="install",
        source="https://example.com/demo.git",
        install_name=None,
        yes=True,
        force=False,
        alias=False,
    )
    main_mod.cmd_profile(args)

    out = capsys.readouterr().out
    assert "doppel -p demo cron list" in out
    assert "doppel -p demo chat" in out


def test_cmd_profile_update_non_distribution_error_uses_doppel_install_hint(
    monkeypatch, capsys, isolated_home
):
    monkeypatch.setattr(profiles_mod, "normalize_profile_name", lambda name: name)
    monkeypatch.setattr(profiles_mod, "get_profile_dir", lambda name: isolated_home / ".doppel" / "profiles" / name)
    monkeypatch.setattr(dist_mod, "read_manifest", lambda _p: None)

    with pytest.raises(SystemExit) as excinfo:
        main_mod.cmd_profile(
            SimpleNamespace(
                profile_action="update",
                profile_name="demo",
                yes=True,
                force_config=False,
            )
        )
    assert excinfo.value.code == 1
    out = capsys.readouterr().out
    assert "doppel profile install" in out


def test_cmd_profile_update_distribution_guidance_uses_doppel_profile_flag(
    monkeypatch, capsys, isolated_home
):
    current = SimpleNamespace(source="https://example.com/demo.git", version="1.0.0")
    plan = _dist_plan("demo", "1.1.0", isolated_home / ".doppel" / "profiles" / "demo", has_cron=True)
    monkeypatch.setattr(profiles_mod, "normalize_profile_name", lambda name: name)
    monkeypatch.setattr(profiles_mod, "get_profile_dir", lambda name: isolated_home / ".doppel" / "profiles" / name)
    monkeypatch.setattr(dist_mod, "read_manifest", lambda _p: current)
    monkeypatch.setattr(dist_mod, "update_distribution", lambda *args, **kwargs: plan)

    main_mod.cmd_profile(
        SimpleNamespace(
            profile_action="update",
            profile_name="demo",
            yes=True,
            force_config=False,
        )
    )

    out = capsys.readouterr().out
    assert "doppel -p demo cron list" in out
