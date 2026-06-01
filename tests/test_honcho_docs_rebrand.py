from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL = REPO_ROOT / "optional-skills" / "autonomous-ai-agents" / "honcho" / "SKILL.md"
DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "autonomous-ai-agents"
    / "autonomous-ai-agents-honcho.md"
)


def test_honcho_skill_and_docs_prefer_doppel_for_customer_facing_copy():
    skill = SKILL.read_text(encoding="utf-8")
    doc = DOC.read_text(encoding="utf-8")

    expected = (
        "Configure and use Honcho memory with Doppel",
        "author: Doppel Agent",
        "# Honcho Memory for Doppel",
        "Doppel creates two peers per session",
        "Each Doppel profile gets its own Honcho AI peer",
        "doppel memory setup honcho",
        "doppel honcho status",
        "Manual override: `doppel honcho map my-project-name`",
        "doppel profile create coder --clone",
        "doppel honcho sync",
        "`~/.doppel/config.yaml`",
        "| `doppel honcho setup` |",
        "| `doppel honcho status` |",
        "| `doppel honcho migrate` | Step-by-step migration guide from OpenClaw native memory to Doppel + Honcho |",
        "| `doppel memory setup` |",
        "| `doppel memory off` |",
        "| Related skills | [`doppel-agent`]",
    )
    stale = (
        "Configure and use Honcho memory with Hermes",
        "author: Hermes Agent",
        "# Honcho Memory for Hermes",
        "Hermes creates two peers per session",
        "Each Hermes profile gets its own Honcho AI peer",
        "hermes memory setup honcho",
        "hermes honcho status",
        "Manual override: `hermes honcho map my-project-name`",
        "hermes profile create coder --clone",
        "hermes honcho sync",
        "`~/.hermes/config.yaml`",
        "| `hermes honcho setup` |",
        "| `hermes honcho status` |",
        "| `hermes honcho migrate` | Step-by-step migration guide from OpenClaw native memory to Hermes + Honcho |",
        "| `hermes memory setup` |",
        "| `hermes memory off` |",
        "| Related skills | [`hermes-agent`]",
    )

    combined = skill + "\n" + doc
    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
