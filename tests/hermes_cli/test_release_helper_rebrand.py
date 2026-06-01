from pathlib import Path


def test_release_and_livetest_helpers_prefer_doppel_customer_facing_copy() -> None:
    release_script = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/scripts/release.py"
    ).read_text(encoding="utf-8")
    livetest_readme = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/scripts/LIVETEST_README.md"
    ).read_text(encoding="utf-8")
    tool_search_livetest = Path(
        "/Users/macshelton/Documents/DoppelFork-repair2/scripts/tool_search_livetest.py"
    ).read_text(encoding="utf-8")

    release_required = [
        '"""Doppel Agent Release Script',
        'lines.append(f"# Doppel Agent v{semver} ({tag_name})")',
        'lines.append("> for Doppel Agent. See below for everything included in this initial release.")',
        'parser = argparse.ArgumentParser(description="Doppel Agent Release Tool")',
        'print(f"  Doppel Agent Release Preview")',
        'f"Doppel Agent v{new_version} ({calver_date})\\n\\nWeekly release"',
        '--title", f"Doppel Agent v{new_version} ({calver_date})"',
        "gh release create {tag_name} --title 'Doppel Agent v{new_version} ({calver_date})' ",
    ]
    release_forbidden = [
        '"""Hermes Agent Release Script',
        'lines.append(f"# Hermes Agent v{semver} ({tag_name})")',
        'lines.append("> for Hermes Agent. See below for everything included in this initial release.")',
        'parser = argparse.ArgumentParser(description="Hermes Agent Release Tool")',
        'print(f"  Hermes Agent Release Preview")',
        'f"Hermes Agent v{new_version} ({calver_date})\\n\\nWeekly release"',
        '--title", f"Hermes Agent v{new_version} ({calver_date})"',
        "gh release create {tag_name} --title 'Hermes Agent v{new_version} ({calver_date})' ",
    ]

    readme_required = [
        "Requires `OPENROUTER_API_KEY` set or present in `~/.doppel/.env`.",
    ]
    readme_forbidden = [
        "Requires `OPENROUTER_API_KEY` set or present in `~/.hermes/.env`.",
    ]

    livetest_required = [
        "\"\"\"Live test harness for Doppel Agent's Tool Search feature.",
        '"""Create a fresh ~/.doppel/ for one test, copying minimal credentials.',
        "Also reads OPENROUTER_API_KEY from the user's real ``~/.doppel/.env`` so",
        'home_dir = Path(tempfile.mkdtemp(prefix="doppel_ts_live_"))',
        'doppel_home = home_dir / ".doppel"',
    ]
    livetest_forbidden = [
        "\"\"\"Live test harness for Hermes Agent's Tool Search feature.",
        '"""Create a fresh ~/.hermes/ for one test, copying minimal credentials.',
        "Also reads OPENROUTER_API_KEY from the user's real ``~/.hermes/.env`` so",
        'home_dir = Path(tempfile.mkdtemp(prefix="hermes_ts_live_"))',
        'hermes_home = home_dir / ".hermes"',
    ]

    for text in release_required:
        assert text in release_script, text
    for text in release_forbidden:
        assert text not in release_script, text
    for text in readme_required:
        assert text in livetest_readme, text
    for text in readme_forbidden:
        assert text not in livetest_readme, text
    for text in livetest_required:
        assert text in tool_search_livetest, text
    for text in livetest_forbidden:
        assert text not in tool_search_livetest, text
