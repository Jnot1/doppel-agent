from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
AIRTABLE = REPO_ROOT / "skills" / "productivity" / "airtable" / "SKILL.md"
LINEAR = REPO_ROOT / "skills" / "productivity" / "linear" / "SKILL.md"
NOTION = REPO_ROOT / "skills" / "productivity" / "notion" / "SKILL.md"
MAPS = REPO_ROOT / "skills" / "productivity" / "maps" / "SKILL.md"


def test_productivity_core_skills_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (AIRTABLE, LINEAR, NOTION, MAPS)
    )

    expected = (
        "Store the token in `~/.doppel/.env` (or via `doppel setup`):",
        "the tool output stays clean for Doppel.",
        "## Typical Doppel Workflow",
        "## Important Notes for Doppel",
        "**`AIRTABLE_API_KEY` flows from `~/.doppel/.env` into the subprocess automatically**",
        "author: Doppel Agent",
        "Set `LINEAR_API_KEY` in your environment (via `doppel setup` or your env config)",
        'SCRIPT="${DOPPEL_HOME:-$HOME/.doppel}/skills/productivity/linear/scripts/linear_api.py"',
        "Store in `~/.doppel/.env`:",
        "Add those exports to your shell profile (or to `~/.doppel/.env`) so every session inherits them.",
        '"Hello from Doppel!"',
        "wire it via Doppel's MCP support",
        'Script path: `${DOPPEL_HOME:-$HOME/.doppel}/skills/maps/scripts/maps_client.py`',
        'MAPS="${DOPPEL_HOME:-$HOME/.doppel}/skills/maps/scripts/maps_client.py"',
        'python3 "${DOPPEL_HOME:-$HOME/.doppel}/skills/maps/scripts/maps_client.py" search "Statue of Liberty"',
    )
    stale = (
        "Store the token in `~/.hermes/.env` (or via `hermes setup`):",
        "the tool output stays clean for Hermes.",
        "## Typical Hermes Workflow",
        "## Important Notes for Hermes",
        "**`AIRTABLE_API_KEY` flows from `~/.hermes/.env` into the subprocess automatically**",
        "author: Hermes Agent",
        "Set `LINEAR_API_KEY` in your environment (via `hermes setup` or your env config)",
        "find ~/.hermes -path '*skills/productivity/linear/scripts/linear_api.py'",
        "Store in `~/.hermes/.env`:",
        "Add those exports to your shell profile (or to `~/.hermes/.env`) so every session inherits them.",
        '"Hello from Hermes!"',
        "wire it via Hermes' MCP support",
        "Script path: `~/.hermes/skills/maps/scripts/maps_client.py`",
        "MAPS=~/.hermes/skills/maps/scripts/maps_client.py",
        'python3 ~/.hermes/skills/maps/scripts/maps_client.py search "Statue of Liberty"',
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
