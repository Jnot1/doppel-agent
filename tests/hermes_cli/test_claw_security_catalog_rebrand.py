from pathlib import Path


def test_claw_security_and_catalog_surfaces_prefer_doppel() -> None:
    expectations = {
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/claw.py": {
            "required": [
                "Doppel may try to use the same token, causing disconnects.",
                '"""Check if a Doppel gateway is running with connected platforms.',
                "Doppel gateway is running with active connections: ",
                "Recommendation: stop the gateway first with 'doppel stop'.",
                "│          ⚕ Doppel — OpenClaw Migration                │",
                "Each conflict is an item whose target already exists in ~/.doppel/. ",
                "restorable with `doppel import`.",
                "free up disk space under the Doppel home.",
                "'doppel claw cleanup' separately.",
                "│          ⚕ Doppel — OpenClaw Cleanup                  │",
            ],
            "forbidden": [
                "Hermes may try to use the same token, causing disconnects.",
                '"""Check if a Hermes gateway is running with connected platforms.',
                "Hermes gateway is running with active connections: ",
                "Recommendation: stop the gateway first with 'hermes stop'.",
                "│          ⚕ Hermes — OpenClaw Migration                 │",
                "Each conflict is an item whose target already exists in ~/.hermes/. ",
                "restorable with `hermes import`.",
                "free up disk space under the Hermes home.",
                "'hermes claw cleanup' separately.",
                "│          ⚕ Hermes — OpenClaw Cleanup                   │",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/security_audit.py": {
            "required": [
                '"""On-demand supply-chain audit for Doppel Agent installs.',
                "Scans three surfaces a Doppel user actually controls and we can map to",
                "1. The Doppel venv (every PyPI dist via ``importlib.metadata``).",
                "2. Python deps declared by user-installed plugins under ``~/.doppel/plugins``",
                '"""Python deps declared by plugins under ``~/.doppel/plugins``.',
                '"""Implementation of `doppel security audit`."""',
            ],
            "forbidden": [
                '"""On-demand supply-chain audit for Hermes Agent installs.',
                "Scans three surfaces a Hermes user actually controls and we can map to",
                "1. The Hermes venv (every PyPI dist via ``importlib.metadata``).",
                "2. Python deps declared by user-installed plugins under ``~/.hermes/plugins``",
                '"""Python deps declared by plugins under ``~/.hermes/plugins``.',
                '"""Implementation of `hermes security audit`."""',
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/model_catalog.py": {
            "required": [
                "Reads disk cache at ``~/.doppel/cache/model_catalog.json``.",
                '"""Clear the in-process cache. Used by tests and ``doppel model --refresh``."""',
            ],
            "forbidden": [
                "Reads disk cache at ``~/.hermes/cache/model_catalog.json``.",
                '"""Clear the in-process cache. Used by tests and ``hermes model --refresh``."""',
            ],
        },
    }

    for path_str, expected in expectations.items():
        text = Path(path_str).read_text(encoding="utf-8")
        for snippet in expected["required"]:
            assert snippet in text, f"{path_str}: missing {snippet!r}"
        for snippet in expected["forbidden"]:
            assert snippet not in text, f"{path_str}: forbidden {snippet!r}"
