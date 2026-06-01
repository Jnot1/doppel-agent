from pathlib import Path


def test_tools_mcp_curses_and_doctor_surfaces_prefer_doppel() -> None:
    expectations = {
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/curses_ui.py": {
            "required": [
                '"""Shared curses-based UI components for Doppel CLI.',
                "Used by `doppel tools` and `doppel skills` for interactive checklists.",
            ],
            "forbidden": [
                '"""Shared curses-based UI components for Hermes CLI.',
                "Used by `hermes tools` and `hermes skills` for interactive checklists.",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/mcp_config.py": {
            "required": [
                "MCP Server Management CLI — ``doppel mcp`` subcommand.",
                "Implements ``doppel mcp add/remove/list/test/configure`` for interactive",
                "configuration in ~/.doppel/config.yaml under the ``mcp_servers`` key.",
                "_info('  doppel mcp add ink --url \"https://mcp.ml.ink/mcp\"')",
                "_info('  doppel mcp add github --command npx --args @modelcontextprotocol/server-github')",
                "_info('  doppel mcp add myserver --preset mypreset')",
                '_info("Fix the issue, then: doppel mcp test " + name)',
                "_info('  doppel mcp add <name> --url <endpoint>')",
                "_info('  doppel mcp add <name> --command <cmd> --args <args...>')",
                '_info("Use `doppel mcp remove` + `doppel mcp add` to reconfigure auth.")',
                '_info("Then re-run `doppel mcp login " + name + "`.")',
                'print("Error: \'doppel mcp configure\' requires an interactive terminal.", file=_sys.stderr)',
                '"""Main dispatcher for ``doppel mcp`` subcommands."""',
                '_info("doppel mcp                                    Open the catalog picker (default)")',
                '_info("doppel mcp login <name>                       Re-authenticate OAuth")',
            ],
            "forbidden": [
                "MCP Server Management CLI — ``hermes mcp`` subcommand.",
                "Implements ``hermes mcp add/remove/list/test/configure`` for interactive",
                "configuration in ~/.hermes/config.yaml under the ``mcp_servers`` key.",
                "_info('  hermes mcp add ink --url \"https://mcp.ml.ink/mcp\"')",
                "_info('  hermes mcp add github --command npx --args @modelcontextprotocol/server-github')",
                "_info('  hermes mcp add myserver --preset mypreset')",
                '_info("Fix the issue, then: hermes mcp test " + name)',
                "_info('  hermes mcp add <name> --url <endpoint>')",
                "_info('  hermes mcp add <name> --command <cmd> --args <args...>')",
                '_info("Use `hermes mcp remove` + `hermes mcp add` to reconfigure auth.")',
                '_info("Then re-run `hermes mcp login " + name + "`.")',
                'print("Error: \'hermes mcp configure\' requires an interactive terminal.", file=_sys.stderr)',
                '"""Main dispatcher for ``hermes mcp`` subcommands."""',
                '_info("hermes mcp                                    Open the catalog picker (default)")',
                '_info("hermes mcp login <name>                       Re-authenticate OAuth")',
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/tools_config.py": {
            "required": [
                "Saves per-platform tool configuration to ~/.doppel/config.yaml under the",
                "Changes take effect on next 'doppel' or gateway restart.",
            ],
            "forbidden": [
                "Saves per-platform tool configuration to ~/.hermes/config.yaml on fresh",
                "Changes take effect on next 'hermes' or gateway restart.",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/doctor.py": {
            "required": [
                'Doctor command for doppel CLI.',
                "_DHH = display_hermes_home()  # user-facing display path (e.g. ~/.doppel or ~/.doppel/profiles/coder)",
                "# Load environment variables from ~/.doppel/.env so API key checks work",
                '"""Return True when ~/.doppel/.env contains provider auth/base URL settings."""',
                "other, leaving ``doppel --version`` reporting a stale version while",
                "\"Re-sync version files (e.g. run 'doppel update', or set \"",
                'check_info("No per-profile gateways registered yet — create one with `doppel profile create <name>`")',
                "Fix: run 'doppel config set model.provider <valid_provider>'",
                "Fix: run 'doppel config set model.provider <provider>' ",
                "or switch providers with 'doppel config set model.provider <name>'",
                'check_warn("Skills Hub directory not initialized", "(run: doppel skills list)")',
                "check_warn(",
                "\"(doppel not in venv/bin/ or .venv/bin/ — reinstall with pip install -e '.[all]')\"",
                "Broken symlink at {_cmd_link_display}/doppel — run 'doppel doctor --fix'",
                "Missing {_cmd_link_display}/doppel symlink — run 'doppel doctor --fix'",
                "check_ok(f\"{_cmd_link_display}/doppel → correct target\")",
                "check_fail(",
                "f\"{_cmd_link_display}/doppel not found\"",
                "\"(doppel command may not work outside the venv)\"",
            ],
            "forbidden": [
                'Doctor command for hermes CLI.',
                "_DHH = display_hermes_home()  # user-facing display path (e.g. ~/.hermes or ~/.hermes/profiles/coder)",
                "# Load environment variables from ~/.hermes/.env so API key checks work",
                '"""Return True when ~/.hermes/.env contains provider auth/base URL settings."""',
                "other, leaving ``hermes --version`` reporting a stale version while",
                "\"Re-sync version files (e.g. run 'hermes update', or set \"",
                'check_info("No per-profile gateways registered yet — create one with `hermes profile create <name>`")',
                "Fix: run 'hermes config set model.provider <valid_provider>'",
                "Fix: run 'hermes config set model.provider <provider>' ",
                "or switch providers with 'hermes config set model.provider <name>'",
                'check_warn("Skills Hub directory not initialized", "(run: hermes skills list)")',
                "\"(hermes not in venv/bin/ or .venv/bin/ — reinstall with pip install -e '.[all]')\"",
                "Broken symlink at {_cmd_link_display}/hermes — run 'doppel doctor --fix'",
                "Missing {_cmd_link_display}/hermes symlink — run 'doppel doctor --fix'",
                "check_ok(f\"{_cmd_link_display}/hermes → correct target\")",
                "f\"{_cmd_link_display}/hermes not found\"",
                "\"(hermes command may not work outside the venv)\"",
            ],
        },
    }

    for path_str, expected in expectations.items():
        text = Path(path_str).read_text(encoding="utf-8")
        for snippet in expected["required"]:
            assert snippet in text, f"{path_str}: missing {snippet!r}"
        for snippet in expected["forbidden"]:
            assert snippet not in text, f"{path_str}: forbidden {snippet!r}"
