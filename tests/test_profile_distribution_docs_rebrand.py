from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DOC = REPO_ROOT / "website" / "docs" / "user-guide" / "profile-distributions.md"


def test_profile_distribution_docs_prefer_doppel_for_customer_facing_copy():
    text = DOC.read_text(encoding="utf-8")

    expected = (
        "packages a complete Doppel agent",
        "sharing a Doppel agent meant sending someone",
        "running Doppel in 2026",
        "[`doppel profile export` / `import`](../reference/profile-commands.md#doppel-profile-export)",
        "doppel profile create research-bot",
        "# Edit ~/.doppel/profiles/research-bot/SOUL.md",
        "Create `~/.doppel/profiles/research-bot/distribution.yaml`",
        "cd ~/.doppel/profiles/research-bot",
        "doppel profile update research-bot",
        "doppel profile install github.com/you/research-bot --alias",
        "Copies distribution-owned files into `~/.doppel/profiles/research-bot/`",
        "# Environment variables required by this Doppel distribution.",
        "cp ~/.doppel/profiles/research-bot/.env.EXAMPLE ~/.doppel/profiles/research-bot/.env",
        "doppel profile info research-bot",
        "Requires:     Doppel >=0.12.0",
        "`doppel profile list` also shows a `Distribution` column",
        "doppel profile delete research-bot",
        "Path:    ~/.doppel/profiles/research-bot",
        "You built Doppel-on-top",
        "github.com/you/doppel-polymarket-trader",
        "doppel profile install git@github.com:your-org/incident-2026-q2.git --alias",
        "Track your installed version via `doppel profile info <name>`",
        "# ~/.doppel/profiles/research-bot/local/my-overrides.yaml",
        "doppel profile update research-bot --force-config --yes",
        "# Iterate locally in ~/.doppel/profiles/forked-research-bot/",
        "doppel profile install ~/.doppel/profiles/research-bot --name research-bot-test --alias",
        "`doppel -p <name> cron list`",
        "`install`, `update`, `info` live inside `doppel profile`",
    )

    stale = (
        "packages a complete Hermes agent",
        "sharing a Hermes agent meant sending someone",
        "running Hermes in 2026",
        "[`hermes profile export` / `import`](../reference/profile-commands.md#hermes-profile-export)",
        "hermes profile create research-bot",
        "# Edit ~/.hermes/profiles/research-bot/SOUL.md",
        "Create `~/.hermes/profiles/research-bot/distribution.yaml`",
        "cd ~/.hermes/profiles/research-bot",
        "hermes profile update research-bot",
        "hermes profile install github.com/you/research-bot --alias",
        "Copies distribution-owned files into `~/.hermes/profiles/research-bot/`",
        "# Environment variables required by this Hermes distribution.",
        "cp ~/.hermes/profiles/research-bot/.env.EXAMPLE ~/.hermes/profiles/research-bot/.env",
        "hermes profile info research-bot",
        "Requires:     Hermes >=0.12.0",
        "`hermes profile list` also shows a `Distribution` column",
        "hermes profile delete research-bot",
        "Path:    ~/.hermes/profiles/research-bot",
        "You built Hermes-on-top",
        "github.com/you/hermes-polymarket-trader",
        "hermes profile install git@github.com:your-org/incident-2026-q2.git --alias",
        "Track your installed version via `hermes profile info <name>`",
        "# ~/.hermes/profiles/research-bot/local/my-overrides.yaml",
        "hermes profile update research-bot --force-config --yes",
        "# Iterate locally in ~/.hermes/profiles/forked-research-bot/",
        "hermes profile install ~/.hermes/profiles/research-bot --name research-bot-test --alias",
        "`hermes -p <name> cron list`",
        "`install`, `update`, `info` live inside `hermes profile`",
    )

    for needle in expected:
        assert needle in text
    for needle in stale:
        assert needle not in text
