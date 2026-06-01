from pathlib import Path


def test_uninstall_and_backup_surfaces_prefer_doppel() -> None:
    uninstall_text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/uninstall.py"
    ).read_text(encoding="utf-8")
    backup_text = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/backup.py"
    ).read_text(encoding="utf-8")

    required_uninstall = [
        '"""Remove installer-managed Doppel PATH entries from shell configs."""',
        '"""Remove managed Doppel CLI wrapper scripts if they exist."""',
        '"""Path-entry substrings that identify Doppel-owned User PATH entries."""',
        '"""Strip Doppel-owned entries from User-scope PATH in the registry.',
        '"""Delete Doppel home vars and Git Bash path from User-scope env vars."""',
        "when the link still resolves into this Doppel home's ``node`` directory.",
        "Doppel) is left untouched so we never break unrelated tooling.",
        'log_info("No Doppel-owned PATH entries in User environment")',
        'log_info("No Doppel-set User env vars to remove")',
        'log_info("Removing Doppel-managed node/npm/npx symlinks...")',
        'log_info("No Doppel-managed node/npm/npx symlinks found")',
        "# 5. Optionally remove ~/.doppel/ data directory (and named profiles)",
    ]
    forbidden_uninstall = [
        '"""Remove installer-managed Doppel/Hermes PATH entries from shell configs."""',
        '"""Remove managed Doppel/Hermes CLI wrapper scripts if they exist."""',
        '"""Path-entry substrings that identify Doppel/Hermes-owned User PATH entries."""',
        '"""Strip Hermes-owned entries from User-scope PATH in the registry.',
        '"""Delete Doppel/Hermes home vars and Git Bash path from User-scope env vars."""',
        "when the link still resolves into this Hermes home's ``node`` directory.",
        "Hermes) is left untouched so we never break unrelated tooling.",
        'log_info("No Hermes-owned PATH entries in User environment")',
        'log_info("No Doppel/Hermes-set User env vars to remove")',
        'log_info("Removing Hermes-managed node/npm/npx symlinks...")',
        'log_info("No Hermes-managed node/npm/npx symlinks found")',
        "# 5. Optionally remove ~/.hermes/ data directory (and named profiles)",
    ]

    required_backup = [
        '"""Check that a zip looks like a Doppel backup.',
        "# Look for telltale files that a doppel home would have",
        "zip does not appear to be a Doppel backup ",
        "hermes_home: Override for the Doppel home directory (tests).",
    ]
    forbidden_backup = [
        '"""Check that a zip looks like a Hermes backup.',
        "# Look for telltale files that a hermes home would have",
        "zip does not appear to be a Hermes backup ",
        "hermes_home: Override for the Hermes home directory (tests).",
    ]

    for needle in required_uninstall:
        assert needle in uninstall_text, needle
    for needle in forbidden_uninstall:
        assert needle not in uninstall_text, needle

    for needle in required_backup:
        assert needle in backup_text, needle
    for needle in forbidden_backup:
        assert needle not in backup_text, needle
