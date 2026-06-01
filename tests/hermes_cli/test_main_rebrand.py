from pathlib import Path


def test_main_customer_facing_copy_prefers_doppel() -> None:
    main_py = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/main.py"
    ).read_text(encoding="utf-8")

    required = [
        "When the user upgrades code via ``git pull`` (or ``doppel update``",
        "``doppel update`` to recover.  Missing the bootstrap means UTF-8 stdio",
        "installed via ``doppel tools`` or",
        "Skip when stdout is redirected (`doppel --tui … >log`, CI capture):",
        '"""Handle ``doppel --version`` before config/logging imports on Termux."""',
        "Interactive TUI commands (doppel tools, doppel setup, doppel model) use",
        "`doppel profile use` and the gateway should honour that choice.",
        "Load .env from ~/.doppel/.env first, then project root as dev fallback.",
        "a plain `doppel --tui` try to",
        "Relaunch as `doppel update` so",
        "(``doppel kanban …``) resolve the board on different paths: the env-pin if",
        "``doppel kanban boards switch`` from another session can flip the file",
        "user's ~/.doppel/config.yaml and return built-in defaults. Set BEFORE",
        "Shared by ``cmd_model`` (``doppel model``) and the setup wizard",
        "a leftover OPENAI_BASE_URL in ~/.doppel/.env can poison auxiliary",
        '"""Remove OPENAI_BASE_URL from ~/.doppel/.env if the active provider is not \'custom\'.',
        "Doppel uses lightweight \"auxiliary\" models for side tasks (vision analysis,",
        "`doppel model` provider picker. It does NOT re-run credential setup",
        "configure new providers through the normal `doppel model` flow first.",
        "``doppel model`` flow, then route aux tasks to them here.",
        "edit ~/.doppel/.env by hand. The",
        "re-running `doppel setup` from scratch. OpenRouter",
        "Prefer credential pool (where `doppel auth` stores device_code tokens),",
        "Forward CLI flags from ``doppel model --manual-paste``",
        "can't reach the manual-paste path via ``doppel model``.",
        "live only in the pool (e.g. after ``doppel auth add xai-oauth``).  Fall",
        "Save to ~/.doppel/config.yaml.",
        '"""Shared API-key entry point for ``doppel setup`` / ``doppel model``.',
        "recover from a malformed paste without editing ``~/.doppel/.env`` by hand.",
    ]
    forbidden = [
        "When the user upgrades code via ``git pull`` (or ``hermes update``",
        "``hermes update`` to recover.  Missing the bootstrap means UTF-8 stdio",
        "installed via ``hermes tools`` or",
        "Skip when stdout is redirected (`hermes --tui … >log`, CI capture):",
        '"""Handle ``hermes --version`` before config/logging imports on Termux."""',
        "Interactive TUI commands (hermes tools, hermes setup, hermes model) use",
        "`hermes profile use` and the gateway should honour that choice.",
        "Load .env from ~/.hermes/.env first, then project root as dev fallback.",
        "a plain `hermes --tui` try to",
        "Relaunch as `hermes update` so",
        "(``hermes kanban …``) resolve the board on different paths: the env-pin if",
        "``hermes kanban boards switch`` from another session can flip the file",
        "user's ~/.hermes/config.yaml and return built-in defaults. Set BEFORE",
        "Shared by ``cmd_model`` (``hermes model``) and the setup wizard",
        "a leftover OPENAI_BASE_URL in ~/.hermes/.env can poison auxiliary",
        '"""Remove OPENAI_BASE_URL from ~/.hermes/.env if the active provider is not \'custom\'.',
        "Hermes uses lightweight \"auxiliary\" models for side tasks (vision analysis,",
        "`hermes model` provider picker. It does NOT re-run credential setup",
        "configure new providers through the normal `hermes model` flow first.",
        "``hermes model`` flow, then route aux tasks to them here.",
        "edit ~/.hermes/.env by hand. The",
        "re-running `hermes setup` from scratch. OpenRouter",
        "Prefer credential pool (where `hermes auth` stores device_code tokens),",
        "Forward CLI flags from ``hermes model --manual-paste``",
        "can't reach the manual-paste path via ``hermes model``.",
        "live only in the pool (e.g. after ``hermes auth add xai-oauth``).  Fall",
        "Save to ~/.hermes/config.yaml.",
        '"""Shared API-key entry point for ``hermes setup`` / ``hermes model``.',
        "recover from a malformed paste without editing ``~/.hermes/.env`` by hand.",
    ]

    for text in required:
        assert text in main_py, text
    for text in forbidden:
        assert text not in main_py, text


def test_main_update_and_dashboard_copy_prefers_doppel() -> None:
    main_py = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/main.py"
    ).read_text(encoding="utf-8")

    required = [
        '"""Return PIDs of ``doppel dashboard`` processes other than ourselves.',
        "``doppel dashboard`` is a long-lived server process commonly started and",
        "forgotten.  When ``doppel update`` replaces files on disk, the running",
        '"""Print a short heads-up about the skill curator after `doppel update`.',
        "rename. ``doppel update`` is a high-attention surface — surface the",
        "Subsequent ``doppel update`` invocations skip the block until a newer",
        '"""Kill running ``doppel dashboard`` processes.',
        "Called at the end of ``doppel update`` (default ``reason``) and also",
        "from ``doppel dashboard --stop`` (which overrides ``reason``).  The",
        '"""Update Doppel Agent by downloading a ZIP archive.',
        "streamed output to ``~/.doppel/logs/update.log`` so nothing is lost.",
        '"""Stream wrapper used during ``doppel update`` to survive terminal loss.',
        "(``~/.doppel/logs/update.log``) that users can inspect after the",
        "this makes ``doppel update`` safe to",
        "Users commonly run ``doppel update`` in an SSH session or a terminal",
        "``~/.doppel/logs/update.log`` and to silently absorb",
        "In gateway mode (``doppel update --gateway``) the update is already",
        '"""Implement ``doppel update --check``: fetch and report without installing.',
        "same long-form ``docker pull`` guidance ``doppel update``",
        '# Doppel Agent — ensure /usr/local/bin is on PATH ',
        "The ``--backup`` flag on ``doppel update``",
        "Render path using display_hermes_home so the user sees ~/.doppel/...",
        '"""Update Doppel Agent to the latest version.',
    ]
    forbidden = [
        '"""Return PIDs of ``hermes dashboard`` processes other than ourselves.',
        "``hermes dashboard`` is a long-lived server process commonly started and",
        "forgotten.  When ``hermes update`` replaces files on disk, the running",
        '"""Print a short heads-up about the skill curator after `hermes update`.',
        "rename. ``hermes update`` is a high-attention surface — surface the",
        "Subsequent ``hermes update`` invocations skip the block until a newer",
        '"""Kill running ``hermes dashboard`` processes.',
        "Called at the end of ``hermes update`` (default ``reason``) and also",
        "from ``hermes dashboard --stop`` (which overrides ``reason``).  The",
        '"""Update Hermes Agent by downloading a ZIP archive.',
        "streamed output to ``~/.hermes/logs/update.log`` so nothing is lost.",
        '"""Stream wrapper used during ``hermes update`` to survive terminal loss.',
        "(``~/.hermes/logs/update.log``) that users can inspect after the",
        "this makes ``hermes update`` safe to",
        "Users commonly run ``hermes update`` in an SSH session or a terminal",
        "``~/.hermes/logs/update.log`` and to silently absorb",
        "In gateway mode (``hermes update --gateway``) the update is already",
        '"""Implement ``hermes update --check``: fetch and report without installing.',
        "same long-form ``docker pull`` guidance ``hermes update``",
        '# Hermes Agent — ensure /usr/local/bin is on PATH ',
        "The ``--backup`` flag on ``hermes update``",
        "Render path using display_hermes_home so the user sees ~/.hermes/...",
        '"""Update Hermes Agent to the latest version.',
    ]

    for text in required:
        assert text in main_py, text
    for text in forbidden:
        assert text not in main_py, text


def test_main_parser_and_help_examples_prefer_doppel() -> None:
    main_py = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/main.py"
    ).read_text(encoding="utf-8")

    required = [
        '"""Dispatch `doppel security <subcmd>`."""',
        "When a user types ``doppel -c Pokemon Agent Dev`` without quoting the",
        "# so that in ``doppel -m gpt5 chat``, ``gpt5`` is correctly skipped as a",
        "``doppel -m gpt5 --provider openai chat \"msg\"`` by skipping the",
        "# subcommand — ``doppel --help``, ``doppel version``, ``doppel logs``,",
        "# doppel tools list [--platform cli]",
        "# doppel tools disable <name...> [--platform cli]",
        "# doppel tools enable <name...> [--platform cli]",
        "# flag is omitted, causing `doppel mcp add ...` to fall through to",
        '"""Launch Doppel Agent as an ACP server."""',
        "# e.g. ``doppel -c Pokemon Agent Dev`` → ``doppel -c 'Pokemon Agent Dev'``",
    ]
    forbidden = [
        '"""Dispatch `hermes security <subcmd>`."""',
        "When a user types ``hermes -c Pokemon Agent Dev`` without quoting the",
        "# so that in ``hermes -m gpt5 chat``, ``gpt5`` is correctly skipped as a",
        "``hermes -m gpt5 --provider openai chat \"msg\"`` by skipping the",
        "# subcommand — ``hermes --help``, ``hermes version``, ``hermes logs``,",
        "# hermes tools list [--platform cli]",
        "# hermes tools disable <name...> [--platform cli]",
        "# hermes tools enable <name...> [--platform cli]",
        "# flag is omitted, causing `hermes mcp add ...` to fall through to",
        '"""Launch Hermes Agent as an ACP server."""',
        "# e.g. ``hermes -c Pokemon Agent Dev`` → ``hermes -c 'Pokemon Agent Dev'``",
    ]

    for text in required:
        assert text in main_py, text
    for text in forbidden:
        assert text not in main_py, text


def test_main_product_wording_prefers_doppel() -> None:
    main_py = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/main.py"
    ).read_text(encoding="utf-8")

    required = [
        "Determine whether Doppel itself has been explicitly configured",
        "Only count these if Doppel has been explicitly configured",
        "Doppel will still save it.",
        "Use Doppel URL heuristics; best for standard OpenAI-compatible endpoints.",
        "Doppel typically makes 3-10 API calls per user turn",
        "To use Gemini with Doppel, enable billing on your",
        "Doppel will use Claude's credential store directly instead of copying a setup-token into",
        '"""Authenticate Doppel CLI with a provider."""',
        '"""Back up Doppel home directory to a zip file."""',
        '"""Restore a Doppel backup from a zip file."""',
        "Close Doppel Desktop, exit other `doppel` REPLs, stop the ",
        '"""Update Doppel via pip (for PyPI installs)."""',
        '"""Main entry point for doppel CLI."""',
    ]
    forbidden = [
        "Determine whether Hermes itself has been explicitly configured",
        "Only count these if Hermes has been explicitly configured",
        "Hermes will still save it.",
        "Use Hermes URL heuristics; best for standard OpenAI-compatible endpoints.",
        "Hermes typically makes 3-10 API calls per user turn",
        "To use Gemini with Hermes, enable billing on your",
        "Hermes will use Claude's credential store directly instead of copying a setup-token into",
        '"""Authenticate Hermes CLI with a provider."""',
        '"""Back up Hermes home directory to a zip file."""',
        '"""Restore a Hermes backup from a zip file."""',
        "Close Hermes Desktop, exit other `hermes` REPLs, stop the ",
        '"""Update Hermes via pip (for PyPI installs)."""',
        '"""Main entry point for hermes CLI."""',
    ]

    for text in required:
        assert text in main_py, text
    for text in forbidden:
        assert text not in main_py, text


def test_main_runtime_update_guidance_prefers_doppel() -> None:
    main_py = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/main.py"
    ).read_text(encoding="utf-8")

    required = [
        "Every subsequent `doppel gateway` then paid a 30s",
        "`doppel gateway` skips it cleanly instead of paying a 30s",
        "fast paths like `doppel --version` and slash-command dispatch",
        "providers if the user switches without running 'doppel model'.",
        "even run ``doppel update`` again to roll forward.",
        "Used by ``doppel update --gateway`` so interactive prompts",
        "the next ``doppel update`` to stash the",
        "instead of a soft warning (used by ``doppel web``).",
        "# Fork detection and upstream management for `doppel update`",
        "``doppel update``, every profile is now current.",
        "know ``doppel update`` is still progressing even if pip/uv itself is silent.",
        "path in `doppel gateway restart`",
        "every `doppel update` surfaces the issue until the user migrates.",
        "check `doppel curator status`. Self-stamps after printing so it",
        "Tying the refresh to ``doppel update`` gives users a predictable",
        "When running as ``doppel update --gateway``",
        "Reuse the same SIGTERM-grace-SIGKILL path used after `doppel update`.",
        "`doppel --tui` is the hot path on phones.",
        "# ``doppel update`` runs on Windows. Silent no-op on non-Windows or when",
    ]
    forbidden = [
        "Every subsequent `hermes gateway` then paid a 30s",
        "`hermes gateway` skips it cleanly instead of paying a 30s",
        "fast paths like `hermes --version` and slash-command dispatch",
        "providers if the user switches without running 'hermes model'.",
        "even run ``hermes update`` again to roll forward.",
        "Used by ``hermes update --gateway`` so interactive prompts",
        "the next ``hermes update`` to stash the",
        "instead of a soft warning (used by ``hermes web``).",
        "# Fork detection and upstream management for `hermes update`",
        "``hermes update``, every profile is now current.",
        "know ``hermes update`` is still progressing even if pip/uv itself is silent.",
        "path in `hermes gateway restart`",
        "every `hermes update` surfaces the issue until the user migrates.",
        "check `hermes curator status`. Self-stamps after printing so it",
        "Tying the refresh to ``hermes update`` gives users a predictable",
        "When running as ``hermes update --gateway``",
        "Reuse the same SIGTERM-grace-SIGKILL path used after `hermes update`.",
        "`hermes --tui` is the hot path on phones.",
        "# ``hermes update`` runs on Windows. Silent no-op on non-Windows or when",
    ]

    for text in required:
        assert text in main_py, text
    for text in forbidden:
        assert text not in main_py, text
