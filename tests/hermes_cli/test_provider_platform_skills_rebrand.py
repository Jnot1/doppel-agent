from pathlib import Path


def test_provider_platform_and_skills_config_surfaces_prefer_doppel() -> None:
    expectations = {
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/providers.py": {
            "required": [
                "Single source of truth for provider identity in Doppel Agent.",
                "Combine env vars: models.dev env + doppel extra",
            ],
            "forbidden": [
                "Single source of truth for provider identity in Hermes Agent.",
                "Combine env vars: models.dev env + hermes extra",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/platforms.py": {
            "required": [
                "Shared platform registry for Doppel Agent.",
            ],
            "forbidden": [
                "Shared platform registry for Hermes Agent.",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/skills_config.py": {
            "required": [
                "Skills configuration for Doppel Agent.",
                "`doppel skills` enters this module.",
                "Config stored in ~/.doppel/config.yaml under:",
                '"""Entry point for `doppel skills`."""',
            ],
            "forbidden": [
                "Skills configuration for Hermes Agent.",
                "`hermes skills` enters this module.",
                "Config stored in ~/.hermes/config.yaml under:",
                '"""Entry point for `hermes skills`."""',
            ],
        },
    }

    for path_str, expected in expectations.items():
        text = Path(path_str).read_text(encoding="utf-8")
        for snippet in expected["required"]:
            assert snippet in text, f"{path_str}: missing {snippet!r}"
        for snippet in expected["forbidden"]:
            assert snippet not in text, f"{path_str}: forbidden {snippet!r}"
