from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def test_lsp_customer_surfaces_prefer_doppel() -> None:
    cli_text = (ROOT / "agent" / "lsp" / "cli.py").read_text(encoding="utf-8")
    eventlog_text = (ROOT / "agent" / "lsp" / "eventlog.py").read_text(encoding="utf-8")
    install_text = (ROOT / "agent" / "lsp" / "install.py").read_text(encoding="utf-8")

    required = [
        '"""``doppel lsp`` CLI subcommand.',
        '"""Wire the ``doppel lsp`` subcommand tree into the main argparse."""',
        '"""Top-level dispatcher for ``doppel lsp <subcommand>``."""',
        "(install via `doppel lsp install <id>` or set lsp.servers.<id>.command)",
        "All installs go to a Doppel-owned bin staging dir,",
        "silently skipped and the user is told about it via ``doppel lsp",
        '"""Return the Doppel-owned bin staging dir for LSP servers."""',
        "Used by the ``doppel lsp status`` CLI to give users a quick",
    ]
    forbidden = [
        '"""``hermes lsp`` CLI subcommand.',
        '"""Wire the ``hermes lsp`` subcommand tree into the main argparse."""',
        '"""Top-level dispatcher for ``hermes lsp <subcommand>``."""',
        "(install via `hermes lsp install <id>` or set lsp.servers.<id>.command)",
        "All installs go to a Hermes-owned bin staging dir,",
        "silently skipped and the user is told about it via ``hermes lsp",
        '"""Return the Hermes-owned bin staging dir for LSP servers."""',
        "Used by the ``hermes lsp status`` CLI to give users a quick",
    ]

    joined = "\n".join((cli_text, eventlog_text, install_text))
    for needle in required:
        assert needle in joined, needle
    for needle in forbidden:
        assert needle not in joined, needle


def test_lsp_bin_dir_prefers_doppel_home(monkeypatch, tmp_path) -> None:
    from agent.lsp.install import hermes_lsp_bin_dir

    monkeypatch.delenv("DOPPEL_HOME", raising=False)
    monkeypatch.delenv("HERMES_HOME", raising=False)

    monkeypatch.setenv("DOPPEL_HOME", str(tmp_path / "doppel-home"))
    path = hermes_lsp_bin_dir()
    assert path == (tmp_path / "doppel-home" / "lsp" / "bin")

    monkeypatch.delenv("DOPPEL_HOME", raising=False)
    monkeypatch.setenv("HERMES_HOME", str(tmp_path / "legacy-home"))
    path = hermes_lsp_bin_dir()
    assert path == (tmp_path / "legacy-home" / "lsp" / "bin")
