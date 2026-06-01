from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "multi-profile-gateways.md"


def test_multi_profile_gateway_docs_prefer_doppel_for_user_facing_examples():
    text = DOC.read_text(encoding="utf-8")

    expected = (
        "If you only run one Doppel agent",
        "You want this setup when you have two or more Doppel agents",
        "doppel profile create coder",
        "`~/.local/bin/doppel-gateways`",
        'echo "Usage: doppel-gateways {start|stop|restart|status|list}"',
        'doppel gateway "$action"',
        'doppel -p "$profile" gateway "$action"',
        "doppel-gateways start",
        "`doppel gateway list`",
        "These are equivalent to `doppel -p coder gateway <action>`",
        "tail -f ~/.doppel/logs/gateway.log",
        "tail -f ~/.doppel/profiles/<name>/logs/gateway.log",
        "doppel logs --tail",
        "doppel profile list",
        "~/.doppel/profiles/<name>/",
        "The default profile uses `~/.doppel/` directly",
        "doppel config set model.model anthropic/claude-sonnet-4",
        "caffeinate -i -w $(cat ~/.doppel/gateway.pid) &",
        '--who=doppel --why="gateways running"',
        "~/.doppel/.env ~/.doppel/profiles/*/.env",
        "`doppel update` pulls the latest code once",
        "You ran `doppel gateway start` after a previous `doppel gateway stop`.",
        "doppel doctor",
        "doppel -p <profile> doctor",
    )

    stale = (
        "If you only run one Hermes agent",
        "You want this setup when you have two or more Hermes agents",
        "hermes profile create coder",
        "`~/.local/bin/hermes-gateways`",
        'echo "Usage: hermes-gateways {start|stop|restart|status|list}"',
        'hermes gateway "$action"',
        'hermes -p "$profile" gateway "$action"',
        "hermes-gateways start",
        "`hermes gateway list`",
        "These are equivalent to `hermes -p coder gateway <action>`",
        "tail -f ~/.hermes/logs/gateway.log",
        "tail -f ~/.hermes/profiles/<name>/logs/gateway.log",
        "hermes logs --tail",
        "hermes profile list",
        "~/.hermes/profiles/<name>/",
        "The default profile uses `~/.hermes/` directly",
        "hermes config set model.model anthropic/claude-sonnet-4",
        "caffeinate -i -w $(cat ~/.hermes/gateway.pid) &",
        '--who=hermes --why="gateways running"',
        "~/.hermes/.env ~/.hermes/profiles/*/.env",
        "`hermes update` pulls the latest code once",
        "You ran `hermes gateway start` after a previous `hermes gateway stop`.",
        "hermes doctor",
        "hermes -p <profile> doctor",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
