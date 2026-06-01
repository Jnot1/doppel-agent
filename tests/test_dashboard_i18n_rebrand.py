from pathlib import Path


def test_dashboard_i18n_surfaces_prefer_doppel() -> None:
    en = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/web/src/i18n/en.ts"
    ).read_text(encoding="utf-8")

    required = [
        "Only user-installed plugins under ~/.doppel/plugins can be removed.",
        "No skills found. Skills are loaded from ~/.doppel/skills/.",
    ]
    forbidden = [
        "Only user-installed plugins under ~/.doppel/plugins can be removed. Legacy ~/.hermes/plugins installs still work.",
        "No skills found. Skills are loaded from ~/.doppel/skills/ on fresh installs; legacy ~/.hermes/skills/ trees still work.",
        "~/.hermes/plugins",
        "~/.hermes/skills",
    ]

    for text in required:
        assert text in en, text
    for text in forbidden:
        assert text not in en, text
