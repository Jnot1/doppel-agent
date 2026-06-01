from pathlib import Path


def test_plugins_cmd_customer_facing_copy_prefers_doppel() -> None:
    plugins_cmd = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/plugins_cmd.py"
    ).read_text(encoding="utf-8")

    required = [
        '"""``doppel plugins`` CLI subcommand — install, update, remove, and list plugins.',
        "Plugins are installed from Git repositories into ``~/.doppel/plugins/``.",
        "``~/.doppel/plugins/<name>/``.",
        '"""Return declared ``requires_env`` names that are unset in ``~/.doppel/.env``."""',
        '"""Clone Git plugin into ``~/.doppel/plugins``.',
        "Run {recommended_update_command()} to update Doppel.",
        "or run `doppel plugins update {plugin_name}`.",
        "It may not be a valid Doppel plugin.",
        "Run `doppel plugins enable {installed_name}` to activate.",
        "[dim]  doppel gateway restart[/dim]",
        "user types into ``doppel plugins enable <key>``. For category-namespaced",
        '"""Apply ``doppel plugins list`` CLI filters."""',
        '"""Resolved path under ``~/.doppel/plugins/<name>`` if it exists."""',
        '"""``git pull`` inside ``~/.doppel/plugins/<name>``."""',
        '"""Delete a plugin tree under ``~/.doppel/plugins/`` only."""',
    ]
    forbidden = [
        '"""``hermes plugins`` CLI subcommand — install, update, remove, and list plugins.',
        "Plugins are installed from Git repositories into ``~/.hermes/plugins/``.",
        "``~/.hermes/plugins/<name>/``.",
        '"""Return declared ``requires_env`` names that are unset in ``~/.hermes/.env``."""',
        '"""Clone Git plugin into ``~/.hermes/plugins``.',
        "or run `hermes plugins update {plugin_name}`.",
        "It may not be a valid Hermes plugin.",
        "Run `hermes plugins enable {installed_name}` to activate.",
        "[dim]  hermes gateway restart[/dim]",
        "user types into ``hermes plugins enable <key>``. For category-namespaced",
        '"""Apply ``hermes plugins list`` CLI filters."""',
        '"""Resolved path under ``~/.hermes/plugins/<name>`` if it exists."""',
        '"""``git pull`` inside ``~/.hermes/plugins/<name>``."""',
        '"""Delete a plugin tree under ``~/.hermes/plugins/`` only."""',
    ]

    for text in required:
        assert text in plugins_cmd, text
    for text in forbidden:
        assert text not in plugins_cmd, text
