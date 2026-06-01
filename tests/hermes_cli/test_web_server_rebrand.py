from pathlib import Path


def test_web_server_customer_facing_copy_prefers_doppel() -> None:
    web_server = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/web_server.py"
    ).read_text(encoding="utf-8")

    required = [
        "Doppel Agent — Web UI server.",
        "running `doppel dashboard` needs fastapi+uvicorn; lazy install keeps",
        "Off unless ``doppel dashboard --tui``",
        "streamed to a per-action log file under ``~/.doppel/logs/<action>.log`` so",
        '"""Spawn ``doppel <subcommand>`` detached and record the Popen handle.',
        '"""Kick off a ``doppel gateway restart`` in the background."""',
        '"""Kick off ``doppel update`` in the background."""',
        '_log.exception("Failed to spawn doppel update")',
        "Writes to ``~/.doppel/config.yaml`` — applies to **new** sessions only.",
        "the canonical ``doppel auth add <provider>`` command so the dashboard",
        "1. ``~/.doppel/.anthropic_oauth.json`` — Doppel-managed PKCE flow",
        "Claude Code subscription tokens are actively flowing into Doppel",
        "when they also have a separate Doppel-managed PKCE login.",
        "→ persists to ~/.doppel/.anthropic_oauth.json AND credential pool",
        "the system in the same state as ``doppel auth add anthropic``.",
        "``doppel auth add minimax-oauth``.",
        'return "doppel setup" if name == "default" else f"{name} setup"',
        "The endpoint spawns the same ``doppel --tui`` binary the CLI uses, behind",
        "Default: whatever ``doppel --tui`` would run.",
        "YAML in ~/.doppel/, same trust level as the config file itself.",
        '"""Scan ~/.doppel/dashboard-themes/*.yaml for user-created themes.',
        "from `~/.doppel/dashboard-themes/*.yaml` ship with their full",
        "1. User plugins:    ~/.doppel/plugins/<name>/dashboard/manifest.json",
        "~/.doppel/plugins/ if you trust it)",
        "Each provider plugin that ships with Doppel Agent exposes a",
    ]
    forbidden = [
        "Hermes Agent — Web UI server.",
        "running `hermes dashboard` needs fastapi+uvicorn; lazy install keeps",
        "Off unless ``hermes dashboard --tui``",
        "streamed to a per-action log file under ``~/.hermes/logs/<action>.log`` so",
        '"""Spawn ``hermes <subcommand>`` detached and record the Popen handle.',
        '"""Kick off a ``hermes gateway restart`` in the background."""',
        '"""Kick off ``hermes update`` in the background."""',
        '_log.exception("Failed to spawn hermes update")',
        "Writes to ``~/.hermes/config.yaml`` — applies to **new** sessions only.",
        "the canonical ``hermes auth add <provider>`` command so the dashboard",
        "1. ``~/.hermes/.anthropic_oauth.json`` — Hermes-managed PKCE flow",
        "Claude Code subscription tokens are actively flowing into Hermes",
        "when they also have a separate Hermes-managed PKCE login.",
        "→ persists to ~/.hermes/.anthropic_oauth.json AND credential pool",
        "the system in the same state as ``hermes auth add anthropic``.",
        "``hermes auth add minimax-oauth``.",
        'return "hermes setup" if name == "default" else f"{name} setup"',
        "The endpoint spawns the same ``hermes --tui`` binary the CLI uses, behind",
        "Default: whatever ``hermes --tui`` would run.",
        "YAML in ~/.hermes/, same trust level as the config file itself.",
        '"""Scan ~/.hermes/dashboard-themes/*.yaml for user-created themes.',
        "from `~/.hermes/dashboard-themes/*.yaml` ship with their full",
        "1. User plugins:    ~/.hermes/plugins/<name>/dashboard/manifest.json",
        "~/.hermes/plugins/ if you trust it)",
        "Each provider plugin that ships with Hermes Agent exposes a",
    ]

    for text in required:
        assert text in web_server, text
    for text in forbidden:
        assert text not in web_server, text
