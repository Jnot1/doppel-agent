from pathlib import Path


def test_status_and_subscription_surfaces_prefer_doppel() -> None:
    status_text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/status.py"
    ).read_text(encoding="utf-8")
    subscription_text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/nous_subscription.py"
    ).read_text(encoding="utf-8")

    required_status = [
        '"(not set)" placeholder in dim color to match ``doppel config``\'s',
    ]
    forbidden_status = [
        '"(not set)" placeholder in dim color to match ``hermes config``\'s',
    ]

    required_subscription = [
        "# Tool Gateway via `doppel model`, so direct credentials should NOT",
    ]
    forbidden_subscription = [
        "# Tool Gateway via `hermes model`, so direct credentials should NOT",
    ]

    for needle in required_status:
        assert needle in status_text, needle
    for needle in forbidden_status:
        assert needle not in status_text, needle

    for needle in required_subscription:
        assert needle in subscription_text, needle
    for needle in forbidden_subscription:
        assert needle not in subscription_text, needle
