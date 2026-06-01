from pathlib import Path


def test_dump_customer_facing_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/dump.py")
    text = path.read_text(encoding="utf-8")

    required = [
        '"""',
        "Dump command for doppel CLI.",
        "Outputs a compact, plain-text summary of the user's Doppel setup",
        "``doppel dump`` formats empty values as blank",
        "to ``<project_root>/.doppel_build_sha``",
        "lines.append(\"--- doppel dump ---\")",
        'lines.append(f"doppel_home:      {display_hermes_home()}")',
    ]
    forbidden = [
        "Dump command for hermes CLI.",
        "Outputs a compact, plain-text summary of the user's Hermes setup",
        "``hermes dump`` formats empty values as blank",
        "to ``<project_root>/.hermes_build_sha``",
        "lines.append(\"--- hermes dump ---\")",
        'lines.append(f"hermes_home:      {display_hermes_home()}")',
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
