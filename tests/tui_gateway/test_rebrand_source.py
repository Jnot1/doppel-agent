from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_tui_gateway_customer_surfaces_prefer_doppel() -> None:
    server = _read("tui_gateway/server.py")

    assert "Re-read ``~/.hermes/.env`` into the gateway process" not in server
    assert "Re-read ``~/.doppel/.env`` into the gateway process" in server

    assert "bare `hermes` is interactive — use `/hermes chat -q …` or run `hermes` in another terminal" not in server
    assert "bare `doppel` is interactive — use `/doppel chat -q …` or run `doppel` in another terminal" in server
    assert "`hermes setup` needs a full terminal — run it outside the TUI" not in server
    assert "`doppel setup` needs a full terminal — run it outside the TUI" in server
    assert "`hermes gateway` is long-running — run it in another terminal" not in server
    assert "`doppel gateway` is long-running — run it in another terminal" in server
    assert "`hermes sessions browse` is interactive — use /resume here, or run browse in another terminal" not in server
    assert "`doppel sessions browse` is interactive — use /resume here, or run browse in another terminal" in server
    assert "`hermes config edit` needs $EDITOR in a real terminal" not in server
    assert "`doppel config edit` needs $EDITOR in a real terminal" in server
    assert "run `hermes model` to configure" not in server
    assert "run `doppel model` to configure" in server
    assert "# Save the key to ~/.hermes/.env" not in server
    assert "# Save the key to ~/.doppel/.env" in server
    assert "appends every unhandled exception to ~/.hermes/logs/tui_gateway_crash.log" not in server
    assert "appends every unhandled exception to ~/.doppel/logs/tui_gateway_crash.log" in server
