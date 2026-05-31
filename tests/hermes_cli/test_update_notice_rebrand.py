from __future__ import annotations

import subprocess
from types import SimpleNamespace

import pytest


def test_refresh_active_lazy_features_retry_hint_is_doppel_first(monkeypatch, capsys):
    from hermes_cli import main as hermes_main
    from tools import lazy_deps

    monkeypatch.setattr(lazy_deps, "active_features", lambda: ["webui"])
    monkeypatch.setattr(
        lazy_deps,
        "refresh_active_features",
        lambda prompt=False: {"webui": "failed: upstream resolver error"},
    )

    hermes_main._refresh_active_lazy_features()

    out = capsys.readouterr().out
    assert "`doppel update` once the upstream issue is resolved." in out


def test_cmd_update_syntax_guard_retry_hint_is_doppel_first(monkeypatch, capsys):
    from hermes_cli import main as hermes_main

    args = SimpleNamespace(
        check=False,
        branch=None,
        yes=False,
        force=False,
        gateway=False,
        backup=False,
        no_backup=False,
    )

    monkeypatch.setattr(hermes_main, "_install_hangup_protection", lambda gateway_mode=False: None)
    monkeypatch.setattr(hermes_main, "_finalize_update_output", lambda _state: None)
    monkeypatch.setattr(hermes_main, "_run_pre_update_backup", lambda _args: None)
    monkeypatch.setattr(hermes_main, "_get_origin_url", lambda git_cmd, cwd: None)
    monkeypatch.setattr(hermes_main, "_is_fork", lambda origin_url: False)
    monkeypatch.setattr(hermes_main, "_stash_local_changes_if_needed", lambda *a, **k: None)
    monkeypatch.setattr(hermes_main, "_invalidate_update_cache", lambda: None)
    monkeypatch.setattr(hermes_main, "_clear_bytecode_cache", lambda *_a, **_k: 0)
    monkeypatch.setattr(hermes_main, "_capture_head_sha", lambda *a, **k: "deadbeefcafe")
    monkeypatch.setattr(
        hermes_main,
        "_validate_critical_files_syntax",
        lambda *_a, **_k: (False, "hermes_cli/config.py", SyntaxError("bad syntax")),
    )

    def fake_run(cmd, **kwargs):
        joined = " ".join(str(c) for c in cmd)
        if "fetch" in joined:
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
        if "rev-parse" in joined and "--abbrev-ref" in joined:
            return subprocess.CompletedProcess(cmd, 0, stdout="main\n", stderr="")
        if "rev-list" in joined:
            return subprocess.CompletedProcess(cmd, 0, stdout="1\n", stderr="")
        if "pull" in joined:
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
        if "reset" in joined and "--hard" in joined:
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    monkeypatch.setattr(hermes_main.subprocess, "run", fake_run)

    with pytest.raises(SystemExit) as excinfo:
        hermes_main.cmd_update(args)

    assert excinfo.value.code == 1
    out = capsys.readouterr().out
    assert "Try ``doppel update`` again later once a fix lands." in out
