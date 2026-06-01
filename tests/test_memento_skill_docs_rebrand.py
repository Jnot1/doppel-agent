from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL = REPO_ROOT / "optional-skills" / "productivity" / "memento-flashcards" / "SKILL.md"
DOC = (
    REPO_ROOT
    / "website"
    / "docs"
    / "user-guide"
    / "skills"
    / "optional"
    / "productivity"
    / "productivity-memento-flashcards.md"
)


def test_memento_skill_docs_prefer_doppel_for_customer_facing_copy():
    combined = SKILL.read_text(encoding="utf-8") + "\n" + DOC.read_text(encoding="utf-8")

    expected = (
        "~/.doppel/skills/productivity/memento-flashcards/data/cards.json",
        "python3 ~/.doppel/skills/productivity/memento-flashcards/scripts/memento_cards.py add",
        "python3 ~/.doppel/skills/productivity/memento-flashcards/scripts/memento_cards.py due",
        "python3 ~/.doppel/skills/productivity/memento-flashcards/scripts/memento_cards.py rate",
        "python3 ~/.doppel/skills/productivity/memento-flashcards/scripts/youtube_quiz.py fetch VIDEO_ID",
        "python3 ~/.doppel/skills/productivity/memento-flashcards/scripts/memento_cards.py export",
        "python3 ~/.doppel/skills/productivity/memento-flashcards/scripts/memento_cards.py import",
        "python3 ~/.doppel/skills/productivity/memento-flashcards/scripts/memento_cards.py stats",
    )
    stale = (
        "~/.hermes/skills/productivity/memento-flashcards/data/cards.json",
        "python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py add",
        "python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py due",
        "python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py rate",
        "python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/youtube_quiz.py fetch VIDEO_ID",
        "python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py export",
        "python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py import",
        "python3 ~/.hermes/skills/productivity/memento-flashcards/scripts/memento_cards.py stats",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
