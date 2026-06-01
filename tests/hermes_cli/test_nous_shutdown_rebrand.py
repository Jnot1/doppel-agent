from pathlib import Path


def test_nous_account_and_shutdown_forensics_prefer_doppel_copy() -> None:
    nous_account = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/nous_account.py"
    ).read_text(encoding="utf-8")
    shutdown_forensics = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/gateway/shutdown_forensics.py"
    ).read_text(encoding="utf-8")

    required = [
        "Doppel Agent could not verify your Nous Portal entitlement, so {capability} ",
        "is unavailable. Run `doppel model` to refresh your login, or check ",
        "Nous inference credentials are configured, but Doppel Agent cannot verify ",
        "`doppel model` to enable Portal-managed features. Billing and ",
        "Log in to Nous Portal to use {capability}: run `doppel model`. ",
        "Doppel Agent could not verify your Nous Portal paid access, so {capability} ",
        "Run `doppel model` to refresh your session.",
        "login, so {capability} is unavailable. Run `doppel model` to ",
        "If you recently bought credits, run `doppel model` to refresh Doppel Agent.",
        "upgraded doppel-agent but never re-ran ``doppel setup`` to regenerate",
    ]
    forbidden = [
        "Hermes could not verify your Nous Portal entitlement, so {capability} ",
        "is unavailable. Run `hermes model` to refresh your login, or check ",
        "Nous inference credentials are configured, but Hermes cannot verify ",
        "`hermes model` to enable Portal-managed features. Billing and ",
        "Log in to Nous Portal to use {capability}: run `hermes model`. ",
        "Hermes could not verify your Nous Portal paid access, so {capability} ",
        "Run `hermes model` to refresh your session.",
        "login, so {capability} is unavailable. Run `hermes model` to ",
        "If you recently bought credits, run `hermes model` to refresh Hermes.",
        "upgraded hermes-agent but never re-ran ``hermes setup`` to regenerate",
    ]

    combined = "\n".join([nous_account, shutdown_forensics])
    for text in required:
        assert text in combined, text
    for text in forbidden:
        assert text not in combined, text
