from pathlib import Path


def test_background_review_and_azure_guidance_prefer_doppel() -> None:
    root = Path("/Users/macshelton/Documents/DoppelFork-repair2")
    background_text = (root / "agent" / "background_review.py").read_text(encoding="utf-8")
    azure_text = (root / "agent" / "azure_identity_adapter.py").read_text(encoding="utf-8")

    required_background = [
        "Bundled skills (shipped with Doppel).",
        "Hub-installed skills (installed via 'doppel skills install').",
        "Pinned skills (marked via 'doppel curator pin') CAN be improved — ",
    ]
    forbidden_background = [
        "Bundled skills (shipped with Hermes, e.g. 'hermes-agent').",
        "Hub-installed skills (installed via 'hermes skills install').",
        "Pinned skills (marked via 'hermes curator pin') CAN be improved — ",
    ]

    required_azure = [
        "Use for ``doppel doctor`` /",
        "Designed for ``doppel doctor`` and the wizard preflight",
        "Run `doppel doctor` or `az login` to recover.",
    ]
    forbidden_azure = [
        "Use for ``hermes doctor`` /",
        "Designed for ``hermes doctor`` and the wizard preflight",
        "Run `hermes doctor` or `az login` to recover.",
    ]

    for needle in required_background:
        assert needle in background_text, needle
    for needle in forbidden_background:
        assert needle not in background_text, needle

    for needle in required_azure:
        assert needle in azure_text, needle
    for needle in forbidden_azure:
        assert needle not in azure_text, needle
