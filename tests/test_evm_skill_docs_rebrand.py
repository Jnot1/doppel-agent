from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL = REPO_ROOT / "optional-skills" / "blockchain" / "evm" / "SKILL.md"
DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "blockchain"
    / "blockchain-evm.md"
)


def test_evm_skill_docs_prefer_doppel_for_customer_facing_copy():
    combined = SKILL.read_text(encoding="utf-8") + "\n" + DOC.read_text(encoding="utf-8")

    expected = (
        "author: Mibayy (@Mibayy), youssefea (@youssefea), ethernet8023 (@ethernet8023), Doppel Agent",
        "Helper script path: `~/.doppel/skills/blockchain/evm/scripts/evm_client.py`",
        "SCRIPT=~/.doppel/skills/blockchain/evm/scripts/evm_client.py",
        "python3 ~/.doppel/skills/blockchain/evm/scripts/evm_client.py stats",
        "python3 ~/.doppel/skills/blockchain/evm/scripts/evm_client.py ens vitalik.eth",
    )
    stale = (
        "author: Mibayy (@Mibayy), youssefea (@youssefea), ethernet8023 (@ethernet8023), Hermes Agent",
        "Helper script path: `~/.hermes/skills/blockchain/evm/scripts/evm_client.py`",
        "SCRIPT=~/.hermes/skills/blockchain/evm/scripts/evm_client.py",
        "python3 ~/.hermes/skills/blockchain/evm/scripts/evm_client.py stats",
        "python3 ~/.hermes/skills/blockchain/evm/scripts/evm_client.py ens vitalik.eth",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
