from pathlib import Path


def test_shell_script_surfaces_prefer_doppel() -> None:
    root = Path("/Users/macshelton/Documents/DoppelFork-repair2")
    install_text = (root / "scripts" / "install.sh").read_text(encoding="utf-8")
    open_webui_text = (root / "scripts" / "setup_open_webui.sh").read_text(encoding="utf-8")
    node_bootstrap_text = (
        root / "scripts" / "lib" / "node-bootstrap.sh"
    ).read_text(encoding="utf-8")

    required = [
        'log_info "Legacy compatibility alias kept alongside the Doppel launcher"',
        'echo "Missing required command: doppel" >&2',
        '_nb_ok "Node $(node --version) found (Doppel-managed)"',
    ]
    forbidden = [
        'log_info "Legacy alias kept at $command_link_display_dir/hermes"',
        'echo "Missing required command: doppel (legacy hermes also accepted)" >&2',
        '_nb_ok "Node $(node --version) found (Hermes-managed)"',
    ]

    haystacks = [install_text, open_webui_text, node_bootstrap_text]
    joined = "\n".join(haystacks)
    for needle in required:
        assert needle in joined, needle
    for needle in forbidden:
        assert needle not in joined, needle
