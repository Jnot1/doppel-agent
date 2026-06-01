from pathlib import Path

import hermes_cli.uninstall as uninstall


def test_remove_path_from_shell_configs_removes_doppel_managed_block(tmp_path, monkeypatch):
    home = tmp_path / "home"
    home.mkdir()
    shell_config = home / ".zshrc"
    shell_config.write_text(
        '# Doppel Agent — ensure ~/.local/bin is on PATH\n'
        'export PATH="$HOME/.local/bin:$PATH"\n'
        'export KEEP_ME=1\n'
    )
    monkeypatch.setattr(Path, "home", classmethod(lambda cls: home))

    removed = uninstall.remove_path_from_shell_configs()

    assert removed == [shell_config]
    assert shell_config.read_text() == 'export KEEP_ME=1\n'


def test_remove_wrapper_script_removes_doppel_and_hermes_wrappers(tmp_path, monkeypatch):
    home = tmp_path / "home"
    bin_dir = home / ".local" / "bin"
    bin_dir.mkdir(parents=True)
    doppel = bin_dir / "doppel"
    hermes = bin_dir / "hermes"
    doppel.write_text(
        "#!/bin/sh\n"
        'export DOPPEL_HOME="$HOME/.doppel"\n'
        'exec "$HOME/.doppel/doppel-agent/venv/bin/doppel" "$@"\n'
    )
    hermes.write_text(
        "#!/bin/sh\n"
        'exec "$HOME/.doppel/doppel-agent/venv/bin/hermes" "$@"\n'
    )
    monkeypatch.setattr(Path, "home", classmethod(lambda cls: home))

    removed = uninstall.remove_wrapper_script()

    assert sorted(path.name for path in removed) == ["doppel", "hermes"]
    assert not doppel.exists()
    assert not hermes.exists()


def test_windows_path_markers_cover_current_and_legacy_checkout_names(tmp_path):
    markers = uninstall._hermes_path_markers(tmp_path / ".doppel")

    assert any(marker.endswith("\\doppel-agent") for marker in markers)
    assert any(marker.endswith("\\hermes-agent") for marker in markers)
