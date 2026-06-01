from pathlib import Path


def test_kanban_prompt_surfaces_prefer_doppel() -> None:
    expectations = {
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/kanban_decompose.py": {
            "required": [
                "Invoked by ``doppel kanban decompose [task_id | --all]``",
                "You are the Kanban decomposer for the Doppel Agent board.",
            ],
            "forbidden": [
                "Invoked by ``hermes kanban decompose [task_id | --all]``",
                "You are the Kanban decomposer for the Hermes Agent board.",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/kanban_specify.py": {
            "required": [
                "Used by ``doppel kanban specify [task_id | --all]``.",
                "You are the Kanban triage specifier for the Doppel Agent board.",
            ],
            "forbidden": [
                "Used by ``hermes kanban specify [task_id | --all]``.",
                "You are the Kanban triage specifier for the Hermes Agent board.",
            ],
        },
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/profile_describer.py": {
            "required": [
                "Used by ``doppel profile describe <name> --auto``",
                "You are a profile-describer for the Doppel Agent kanban board.",
                'Never write "Doppel Agent profile" or other meta-narration.',
            ],
            "forbidden": [
                "Used by ``hermes profile describe <name> --auto``",
                "You are a profile-describer for the Hermes Agent kanban board.",
                'Never write "Hermes Agent profile" or other meta-narration.',
            ],
        },
    }

    for path_str, expected in expectations.items():
        text = Path(path_str).read_text(encoding="utf-8")
        for snippet in expected["required"]:
            assert snippet in text, f"{path_str}: missing {snippet!r}"
        for snippet in expected["forbidden"]:
            assert snippet not in text, f"{path_str}: forbidden {snippet!r}"
