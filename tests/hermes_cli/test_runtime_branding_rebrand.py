from pathlib import Path


def test_runtime_branding_and_path_surfaces_prefer_doppel() -> None:
    skin_engine = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/skin_engine.py"
    ).read_text(encoding="utf-8")
    memory_setup = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/memory_setup.py"
    ).read_text(encoding="utf-8")
    bridge = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/scripts/whatsapp-bridge/bridge.js"
    ).read_text(encoding="utf-8")
    bridge_package = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/scripts/whatsapp-bridge/package.json"
    ).read_text(encoding="utf-8")
    container_boot = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/container_boot.py"
    ).read_text(encoding="utf-8")
    cron_jobs = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/cron/jobs.py"
    ).read_text(encoding="utf-8")
    gateway_status = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/gateway/status.py"
    ).read_text(encoding="utf-8")
    cron_scheduler = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/cron/scheduler.py"
    ).read_text(encoding="utf-8")
    gateway_pairing = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/gateway/pairing.py"
    ).read_text(encoding="utf-8")
    channel_directory = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/gateway/channel_directory.py"
    ).read_text(encoding="utf-8")

    skin_required = [
        "Skins are defined as YAML files in ~/.doppel/skins/ or as built-in presets.",
        'agent_name: "Doppel Agent"          # Banner title, status display',
        'response_label: " ⚕ Doppel "       # Response box header label',
        'print(skin.get_branding("agent_name"))  # "Doppel Agent"',
        'set_active_skin("mytheme")            # Switch to user skin from ~/.doppel/skins/',
        "Drop a YAML file in ``~/.doppel/skins/<name>.yaml`` following the schema above.",
    ]
    skin_forbidden = [
        "Skins are defined as YAML files in ~/.hermes/skins/ or as built-in presets.",
        'agent_name: "Hermes Agent"          # Banner title, status display',
        'response_label: " ⚕ Hermes "       # Response box header label',
        'print(skin.get_branding("agent_name"))  # "Hermes Agent"',
        'set_active_skin("mytheme")            # Switch to user skin from ~/.hermes/skins/',
        "Drop a YAML file in ``~/.hermes/skins/<name>.yaml`` following the schema above.",
    ]

    memory_required = [
        "Install a plugin to ~/.doppel/plugins/ and try again.",
        "Install the '{provider_name}' memory plugin to ~/.doppel/plugins/",
    ]
    memory_forbidden = [
        "Install a plugin to ~/.hermes/plugins/ and try again.",
        "Install the '{provider_name}' memory plugin to ~/.hermes/plugins/",
    ]

    bridge_required = [
        "* Doppel Agent WhatsApp Bridge",
        "node bridge.js --port 3000 --session ~/.doppel/whatsapp/session",
        "path.join(process.env.HOME || '~', '.doppel', 'whatsapp', 'session')",
        "path.join(process.env.HOME || '~', '.doppel', 'image_cache')",
        "path.join(process.env.HOME || '~', '.doppel', 'document_cache')",
        "path.join(process.env.HOME || '~', '.doppel', 'audio_cache')",
        "const DEFAULT_REPLY_PREFIX = '⚕ *Doppel Agent*\\n────────────\\n';",
        "browser: ['Doppel Agent', 'Chrome', '120.0'],",
    ]
    bridge_forbidden = [
        "* Hermes Agent WhatsApp Bridge",
        "node bridge.js --port 3000 --session ~/.hermes/whatsapp/session",
        "path.join(process.env.HOME || '~', '.hermes', 'whatsapp', 'session')",
        "path.join(process.env.HOME || '~', '.hermes', 'image_cache')",
        "path.join(process.env.HOME || '~', '.hermes', 'document_cache')",
        "path.join(process.env.HOME || '~', '.hermes', 'audio_cache')",
        "const DEFAULT_REPLY_PREFIX = '⚕ *Hermes Agent*\\n────────────\\n';",
        "browser: ['Hermes Agent', 'Chrome', '120.0'],",
    ]
    bridge_package_required = [
        '"description": "WhatsApp bridge for Doppel Agent using Baileys"',
    ]
    bridge_package_forbidden = [
        '"description": "WhatsApp bridge for Hermes Agent using Baileys"',
    ]

    container_required = [
        "is what ``doppel gateway start`` (no ``-p``) targets. Without it,",
        "bare ``doppel gateway start`` inside the container would land on",
        "# ``doppel gateway start`` (no ``-p``) has somewhere to land;",
    ]
    container_forbidden = [
        "is what ``hermes gateway start`` (no ``-p``) targets. Without it,",
        "bare ``hermes gateway start`` inside the container would land on",
        "# ``hermes gateway start`` (no ``-p``) has somewhere to land;",
    ]

    cron_required = [
        "Jobs are stored in ~/.doppel/cron/jobs.json",
        "Output is saved to ~/.doppel/cron/output/{job_id}/{timestamp}.md",
        "~/.doppel/scripts/; ``.sh`` / ``.bash`` files run via bash,",
    ]
    cron_forbidden = [
        "Jobs are stored in ~/.hermes/cron/jobs.json",
        "Output is saved to ~/.hermes/cron/output/{job_id}/{timestamp}.md",
        "~/.hermes/scripts/; ``.sh`` / ``.bash`` files run via bash,",
    ]
    gateway_status_required = [
        "``~/.doppel`` but can be overridden via the environment variable.",
        '"""Return True when the live PID still looks like the Doppel gateway."""',
        "# ``doppel gateway stop`` on Windows would be misclassified as an",
    ]
    gateway_status_forbidden = [
        "``~/.hermes`` but can be overridden via the environment variable.",
        '"""Return True when the live PID still looks like the Hermes gateway."""',
        "# ``hermes gateway stop`` on Windows would be misclassified as an",
    ]
    cron_scheduler_required = [
        "Uses a file-based lock (~/.doppel/cron/.tick.lock) so only one tick",
        "# Without this, standalone invocations (e.g. after `doppel update` reloads",
    ]
    cron_scheduler_forbidden = [
        "Uses a file-based lock (~/.hermes/cron/.tick.lock) so only one tick",
        "# Without this, standalone invocations (e.g. after `hermes update` reloads",
    ]
    gateway_pairing_required = [
        "Storage: ~/.doppel/pairing/",
    ]
    gateway_pairing_forbidden = [
        "Storage: ~/.hermes/pairing/",
    ]
    channel_directory_required = [
        "~/.doppel/channel_directory.json.  The send_message tool reads this file for",
    ]
    channel_directory_forbidden = [
        "~/.hermes/channel_directory.json.  The send_message tool reads this file for",
    ]

    for text in skin_required:
        assert text in skin_engine, text
    for text in skin_forbidden:
        assert text not in skin_engine, text
    for text in memory_required:
        assert text in memory_setup, text
    for text in memory_forbidden:
        assert text not in memory_setup, text
    for text in bridge_required:
        assert text in bridge, text
    for text in bridge_forbidden:
        assert text not in bridge, text
    for text in bridge_package_required:
        assert text in bridge_package, text
    for text in bridge_package_forbidden:
        assert text not in bridge_package, text
    for text in container_required:
        assert text in container_boot, text
    for text in container_forbidden:
        assert text not in container_boot, text
    for text in cron_required:
        assert text in cron_jobs, text
    for text in cron_forbidden:
        assert text not in cron_jobs, text
    for text in gateway_status_required:
        assert text in gateway_status, text
    for text in gateway_status_forbidden:
        assert text not in gateway_status, text
    for text in cron_scheduler_required:
        assert text in cron_scheduler, text
    for text in cron_scheduler_forbidden:
        assert text not in cron_scheduler, text
    for text in gateway_pairing_required:
        assert text in gateway_pairing, text
    for text in gateway_pairing_forbidden:
        assert text not in gateway_pairing, text
    for text in channel_directory_required:
        assert text in channel_directory, text
    for text in channel_directory_forbidden:
        assert text not in channel_directory, text
