from pathlib import Path


def test_codex_runtime_plugin_migration_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/codex_runtime_plugin_migration.py")
    text = path.read_text(encoding="utf-8")

    required = [
        "# managed by doppel-agent — `doppel codex-runtime migrate` regenerates this section",
        "# end doppel-agent managed section",
        "No MCP servers found in Doppel config.",
        "``~/.doppel`` symlink that happens to live under ``/private/var/folders``",
        "so a doppel installed under /opt/, /usr/local/, or a venv all work.",
        "PYTHONPATH passes through so a worktree-launched doppel finds the",
        "Translate Doppel mcp_servers config + Codex curated plugins into",
        "hermes_config: full ~/.doppel/config.yaml dict",
        "register Doppel's own",
        "call back into Doppel for tools",
        "mcp_servers in Doppel config is not a dict; cannot migrate.",
    ]
    forbidden = [
        "# managed by hermes-agent — `hermes codex-runtime migrate` regenerates this section",
        "# end hermes-agent managed section",
        "No MCP servers found in Hermes config.",
        "``~/.hermes`` symlink that happens to live under ``/private/var/folders``",
        "so a hermes installed under /opt/, /usr/local/, or a venv all work.",
        "PYTHONPATH passes through so a worktree-launched hermes finds the",
        "Translate Hermes mcp_servers config + Codex curated plugins into",
        "hermes_config: full ~/.hermes/config.yaml dict",
        "register Hermes' own",
        "call back into Hermes for tools",
        "mcp_servers in Hermes config is not a dict; cannot migrate.",
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
