from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL = REPO_ROOT / "skills" / "devops" / "webhook-subscriptions" / "SKILL.md"
DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "bundled"
    / "devops"
    / "devops-webhook-subscriptions.md"
)


def test_webhook_skill_and_docs_prefer_doppel_for_customer_facing_copy():
    combined = SKILL.read_text(encoding="utf-8") + "\n" + DOC.read_text(encoding="utf-8")

    expected = (
        "trigger Doppel agent runs",
        "doppel webhook list",
        "doppel gateway setup",
        "`~/.doppel/config.yaml`",
        "`~/.doppel/.env`",
        "doppel gateway run",
        "`doppel webhook` CLI command",
        "doppel webhook subscribe <name>",
        "doppel webhook remove <name>",
        "doppel webhook test <name>",
        "doppel webhook subscribe github-issues",
        "doppel webhook subscribe github-prs",
        "doppel webhook subscribe stripe-payments",
        "doppel webhook subscribe ci-builds",
        "doppel webhook subscribe alerts",
        "doppel webhook subscribe antenna-matches",
        "`~/.doppel/webhook_subscriptions.json`",
        "doppel webhook subscribe` writes to `~/.doppel/webhook_subscriptions.json",
        "`grep webhook ~/.doppel/logs/gateway.log | tail -20`",
        "the one from `doppel webhook list`",
    )
    stale = (
        "trigger Hermes agent runs",
        "hermes webhook list",
        "hermes gateway setup",
        "`~/.hermes/config.yaml`",
        "`~/.hermes/.env`",
        "hermes gateway run",
        "`hermes webhook` CLI command",
        "hermes webhook subscribe <name>",
        "hermes webhook remove <name>",
        "hermes webhook test <name>",
        "hermes webhook subscribe github-issues",
        "hermes webhook subscribe github-prs",
        "hermes webhook subscribe stripe-payments",
        "hermes webhook subscribe ci-builds",
        "hermes webhook subscribe alerts",
        "hermes webhook subscribe antenna-matches",
        "`~/.hermes/webhook_subscriptions.json`",
        "hermes webhook subscribe` writes to `~/.hermes/webhook_subscriptions.json",
        "`grep webhook ~/.hermes/logs/gateway.log | tail -20`",
        "the one from `hermes webhook list`",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
