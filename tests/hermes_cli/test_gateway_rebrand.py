from pathlib import Path


def test_gateway_module_prefers_doppel_customer_facing_copy() -> None:
    source = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/gateway.py"
    ).read_text(encoding="utf-8")

    required = [
        "profiles (the pre-7923 global behaviour).  ``doppel update``",
        "current Doppel profile are returned.",
        '"""Return running gateway PIDs mapped to Doppel profiles via PID files."""',
        "with no running gateway until they re-invoke ``doppel gateway``",
        "This is NOT our Doppel Docker image",
        "Return ``[(unit_name, unit_path, is_system)]`` for legacy gateway units from older installs.",
        "Return True when any legacy gateway unit files exist.",
        "Warn about legacy gateway unit files if any are installed.",
        "Stop, disable, and remove legacy gateway unit files.",
        "Remove legacy launchd plist files from older macOS installs.",
        "`doppel gateway start` re-bootstraps when it detects the job is unloaded.",
        "foreground `doppel gateway run` still",
        "`doppel gateway restart` which already",
        "`doppel gateway start/restart` — leaving the gateway vulnerable to",
        "Without this, ``doppel gateway stop --all`` and ``... restart --all``",
        "The direct ``doppel gateway install|uninstall|start|stop|restart``",
        "``doppel gateway run`` are unaffected.",
        "process itself — i.e. when s6-supervise execs ``doppel gateway",
        "or a clone that ``doppel update`` later relocates/removes",
    ]
    forbidden = [
        "profiles (the pre-7923 global behaviour).  ``hermes update``",
        "current Hermes profile are returned.",
        '"""Return running gateway PIDs mapped to Hermes profiles via PID files."""',
        "with no running gateway until they re-invoke ``hermes gateway``",
        "This is NOT our Hermes Docker image",
        "Return ``[(unit_name, unit_path, is_system)]`` for legacy Hermes gateway units.",
        "Return True when any legacy Hermes gateway unit files exist.",
        "Warn about legacy Hermes gateway unit files if any are installed.",
        "Stop, disable, and remove legacy Hermes gateway unit files.",
        "Remove legacy Hermes launchd plist files from older macOS installs.",
        "`hermes gateway start` re-bootstraps when it detects the job is unloaded.",
        "foreground `hermes gateway run` still",
        "`hermes gateway restart` which already",
        "`hermes gateway start/restart` — leaving the gateway vulnerable to",
        "Without this, ``hermes gateway stop --all`` and ``... restart --all``",
        "The direct ``hermes gateway install|uninstall|start|stop|restart``",
        "``hermes gateway run`` are unaffected.",
        "process itself — i.e. when s6-supervise execs ``hermes gateway",
        "or a clone that ``hermes update`` later relocates/removes",
    ]

    for text in required:
        assert text in source, text
    for text in forbidden:
        assert text not in source, text
