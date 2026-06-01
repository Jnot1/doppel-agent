from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
GIF_SEARCH = REPO_ROOT / "skills" / "media" / "gif-search" / "SKILL.md"
SPOTIFY = REPO_ROOT / "skills" / "media" / "spotify" / "SKILL.md"
OCR_DOCS = REPO_ROOT / "skills" / "productivity" / "ocr-and-documents" / "SKILL.md"


def test_small_skills_prefer_doppel_for_customer_facing_copy():
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (GIF_SEARCH, SPOTIFY, OCR_DOCS)
    )

    expected = (
        "author: Doppel Agent",
        "add to `~/.doppel/.env`",
        "Control the user's Spotify account via the Doppel Spotify toolset (7 tools).",
        "Tell the user to run `doppel auth spotify` again.",
    )
    stale = (
        "author: Hermes Agent",
        "add to `~/.hermes/.env`",
        "Control the user's Spotify account via the Hermes Spotify toolset (7 tools).",
        "Tell the user to run `hermes auth spotify` again.",
        "https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify",
    )

    for needle in expected:
        assert needle in combined
    for needle in stale:
        assert needle not in combined
