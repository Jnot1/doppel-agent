from pathlib import Path


def test_secrets_cli_customer_facing_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/secrets_cli.py")
    text = path.read_text(encoding="utf-8")

    required = [
        '"""CLI handlers for ``doppel secrets bitwarden ...``.',
        "``doppel secrets`` parser.",
        "Secrets will be pulled at the start of every Doppel process.",
        "  Status:  [cyan]doppel secrets bitwarden status[/cyan]",
        "  Refresh: [cyan]doppel secrets bitwarden sync[/cyan]",
        "  Disable: [cyan]doppel secrets bitwarden disable[/cyan]",
        "Run [cyan]doppel secrets bitwarden setup[/cyan] to enable.",
        "Enabled but {token_env} is not set — Doppel will skip BSM",
        "`doppel secrets bitwarden setup` first.",
        "Doppel invocation.",
        "[cyan]doppel secrets bitwarden setup[/cyan] and pick EU or ",
    ]
    forbidden = [
        '"""CLI handlers for ``hermes secrets bitwarden ...``.',
        "``hermes secrets`` parser.",
        "Secrets will be pulled at the start of every Hermes process.",
        "  Status:  [cyan]hermes secrets bitwarden status[/cyan]",
        "  Refresh: [cyan]hermes secrets bitwarden sync[/cyan]",
        "  Disable: [cyan]hermes secrets bitwarden disable[/cyan]",
        "Run [cyan]hermes secrets bitwarden setup[/cyan] to enable.",
        "Enabled but {token_env} is not set — Hermes will skip BSM",
        "`hermes secrets bitwarden setup` first.",
        "Hermes invocation.",
        "[cyan]hermes secrets bitwarden setup[/cyan] and pick EU or ",
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
