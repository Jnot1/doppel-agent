from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
CANVAS_SKILL = REPO_ROOT / "optional-skills" / "productivity" / "canvas" / "SKILL.md"
CANVAS_DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "productivity"
    / "productivity-canvas.md"
)
CANVAS_SCRIPT = (
    REPO_ROOT
    / "optional-skills"
    / "productivity"
    / "canvas"
    / "scripts"
    / "canvas_api.py"
)
SHOPIFY_SKILL = REPO_ROOT / "optional-skills" / "productivity" / "shopify" / "SKILL.md"
SHOPIFY_DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "productivity"
    / "productivity-shopify.md"
)
SIYUAN_SKILL = REPO_ROOT / "optional-skills" / "productivity" / "siyuan" / "SKILL.md"
SIYUAN_DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "productivity"
    / "productivity-siyuan.md"
)


def test_productivity_skill_docs_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            CANVAS_SKILL,
            CANVAS_DOC,
            CANVAS_SCRIPT,
            SHOPIFY_SKILL,
            SHOPIFY_DOC,
            SIYUAN_SKILL,
            SIYUAN_DOC,
        )
    )

    expected = (
        'Name the token (e.g., "Doppel Agent"), set an optional expiry',
        "Copy the token and add to `~/.doppel/.env`:",
        'CANVAS="python $DOPPEL_HOME/skills/productivity/canvas/scripts/canvas_api.py"',
        '"""Canvas LMS API CLI for Doppel Agent.',
        "Set them in ~/.doppel/.env or export them in your shell.",
        'description="Canvas LMS API CLI for Doppel Agent"',
        "Save to `~/.doppel/.env`:",
        '"vendor":"Doppel"',
        "Store it in `~/.doppel/.env`:",
        "# In ~/.doppel/config.yaml under mcp_servers:",
    )
    stale = (
        'Name the token (e.g., "Hermes Agent"), set an optional expiry',
        "Copy the token and add to `~/.hermes/.env`:",
        'CANVAS="python $HERMES_HOME/skills/productivity/canvas/scripts/canvas_api.py"',
        '"""Canvas LMS API CLI for Hermes Agent.',
        "Set them in ~/.hermes/.env or export them in your shell.",
        'description="Canvas LMS API CLI for Hermes Agent"',
        "Save to `~/.hermes/.env`:",
        '"vendor":"Hermes"',
        "Store it in `~/.hermes/.env`:",
        "# In ~/.hermes/config.yaml under mcp_servers:",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
