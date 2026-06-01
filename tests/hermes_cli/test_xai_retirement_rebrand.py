from pathlib import Path


def test_xai_retirement_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/xai_retirement.py")
    text = path.read_text(encoding="utf-8")

    required = [
        "Pure logic: walks a Doppel config dict, returns issues for any reference",
        "and reusable from both `doppel doctor` and a future `doppel migrate xai`.",
        "A reference to a retired xAI model found in a Doppel config.",
        "Walk all model slots in a Doppel config and return retirement issues.",
    ]
    forbidden = [
        "Pure logic: walks a Hermes config dict, returns issues for any reference",
        "and reusable from both `hermes doctor` and a future `hermes migrate xai`.",
        "A reference to a retired xAI model found in a Hermes config.",
        "Walk all model slots in a Hermes config and return retirement issues.",
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
