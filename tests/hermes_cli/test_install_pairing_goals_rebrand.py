from pathlib import Path


def test_install_pairing_and_goals_surfaces_prefer_doppel_copy() -> None:
    install_sh = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/scripts/install.sh"
    ).read_text(encoding="utf-8")
    pairing = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/pairing.py"
    ).read_text(encoding="utf-8")
    goals = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/goals.py"
    ).read_text(encoding="utf-8")

    required = [
        '        echo "~/.doppel"',
        "~/.doppel/platforms/pairing/_rate_limits.json\\n",
        "model in ~/.doppel/config.yaml:\\n",
    ]
    forbidden = [
        '        echo "~/.hermes"',
        "~/.hermes/platforms/pairing/_rate_limits.json\\n",
        "model in ~/.hermes/config.yaml:\\n",
    ]

    combined = "\n".join([install_sh, pairing, goals])
    for text in required:
        assert text in combined, text
    for text in forbidden:
        assert text not in combined, text
