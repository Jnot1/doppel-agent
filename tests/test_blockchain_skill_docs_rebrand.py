from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
HYPERLIQUID_SKILL = REPO_ROOT / "optional-skills" / "blockchain" / "hyperliquid" / "SKILL.md"
HYPERLIQUID_DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "blockchain"
    / "blockchain-hyperliquid.md"
)
SOLANA_SKILL = REPO_ROOT / "optional-skills" / "blockchain" / "solana" / "SKILL.md"
SOLANA_DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "blockchain"
    / "blockchain-solana.md"
)


def test_blockchain_skill_docs_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (HYPERLIQUID_SKILL, HYPERLIQUID_DOC, SOLANA_SKILL, SOLANA_DOC)
    )

    expected = (
        "author: Hugo Sequier (Hugo-SEQUIER), Doppel Agent",
        "author: Deniz Alagoz (gizdusum), enhanced by Doppel Agent",
        "`~/.doppel/.env`",
        "Helper script: `~/.doppel/skills/blockchain/hyperliquid/scripts/hyperliquid_client.py`",
        "python3 ~/.doppel/skills/blockchain/hyperliquid/scripts/hyperliquid_client.py <command> [args]",
        "set in `~/.doppel/.env`",
        "Helper script path: ~/.doppel/skills/blockchain/solana/scripts/solana_client.py",
        "python3 ~/.doppel/skills/blockchain/solana/scripts/solana_client.py stats",
        "python3 ~/.doppel/skills/blockchain/solana/scripts/solana_client.py price SOL",
    )
    stale = (
        "author: Hugo Sequier (Hugo-SEQUIER), Hermes Agent",
        "author: Deniz Alagoz (gizdusum), enhanced by Hermes Agent",
        "`~/.hermes/.env`",
        "Helper script: `~/.hermes/skills/blockchain/hyperliquid/scripts/hyperliquid_client.py`",
        "python3 ~/.hermes/skills/blockchain/hyperliquid/scripts/hyperliquid_client.py <command> [args]",
        "set in `~/.hermes/.env`",
        "Helper script path: ~/.hermes/skills/blockchain/solana/scripts/solana_client.py",
        "python3 ~/.hermes/skills/blockchain/solana/scripts/solana_client.py stats",
        "python3 ~/.hermes/skills/blockchain/solana/scripts/solana_client.py price SOL",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
