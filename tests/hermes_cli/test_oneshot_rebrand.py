from pathlib import Path


def test_oneshot_surfaces_prefer_doppel() -> None:
    text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/oneshot.py"
    ).read_text(encoding="utf-8")

    required = [
        'configured for "cli" in `doppel tools`.',
        "Model / provider selection mirrors `doppel chat`:",
        'return None, f"doppel -z: failed to validate --toolsets: {exc}\\n"',
        '"doppel -z: --toolsets all enables every toolset; "',
        'f"doppel -z: ignoring unknown --toolsets entries: {\', \'.join(unknown)}\\n"',
        '"doppel -z: ignoring disabled MCP servers (set enabled: true in config.yaml to use): "',
        'return None, "doppel -z: --toolsets did not contain any valid toolsets.\\n"',
        '"doppel -z: --provider requires --model (or DOPPEL_INFERENCE_MODEL). "',
        'real_stderr.write(f"doppel -z: agent failed: {failure}\\n")',
        'real_stderr.write("doppel -z: no final response was produced; treating the run as failed.\\n")',
        '"""Best-effort SessionDB for ``doppel -z`` / oneshot mode.',
        "Oneshot bypasses ``DoppelCLI._init_agent()``",
    ]
    forbidden = [
        'configured for "cli" in `hermes tools`.',
        "Model / provider selection mirrors `hermes chat`:",
        'return None, f"hermes -z: failed to validate --toolsets: {exc}\\n"',
        '"hermes -z: --toolsets all enables every toolset; "',
        'f"hermes -z: ignoring unknown --toolsets entries: {\', \'.join(unknown)}\\n"',
        '"hermes -z: ignoring disabled MCP servers (set enabled: true in config.yaml to use): "',
        'return None, "hermes -z: --toolsets did not contain any valid toolsets.\\n"',
        '"hermes -z: --provider requires --model (or DOPPEL_INFERENCE_MODEL). "',
        'real_stderr.write(f"hermes -z: agent failed: {failure}\\n")',
        'real_stderr.write("hermes -z: no final response was produced; treating the run as failed.\\n")',
        '"""Best-effort SessionDB for ``hermes -z`` / oneshot mode.',
        "Oneshot bypasses ``HermesCLI._init_agent()``",
    ]

    for needle in required:
        assert needle in text, needle
    for needle in forbidden:
        assert needle not in text, needle
