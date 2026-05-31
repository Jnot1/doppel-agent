import re
import tomllib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def _project_scripts() -> list[str]:
    with (REPO_ROOT / "pyproject.toml").open("rb") as f:
        data = tomllib.load(f)
    return list(data["project"]["scripts"].keys())


def _homebrew_wrapper_list() -> list[str]:
    content = (REPO_ROOT / "packaging" / "homebrew" / "hermes-agent.rb").read_text()
    match = re.search(r"%w\[(?P<body>[^\]]+)\]\.each do \|exe\|", content)
    assert match, "Could not locate Homebrew wrapper list"
    return match.group("body").split()


def _nix_wrapper_list() -> list[str]:
    content = (REPO_ROOT / "nix" / "hermes-agent.nix").read_text()
    anchor = content.index('lib.concatMapStringsSep "\\n"')
    match = re.search(r"\n\s*\[\n(?P<body>(?:\s*\"[^\"]+\"\n)+)\s*\]", content[anchor:])
    assert match, "Could not locate Nix wrapper list"
    return re.findall(r'"([^"]+)"', match.group("body"))


def _nix_packages_aliases() -> dict[str, str]:
    content = (REPO_ROOT / "nix" / "packages.nix").read_text()
    return dict(
        re.findall(r"^\s*([A-Za-z0-9_-]+)\s*=\s*(hermesAgent)\s*;$", content, flags=re.MULTILINE)
    )


def _nix_overlay_aliases() -> dict[str, str]:
    content = (REPO_ROOT / "nix" / "overlays.nix").read_text()
    return dict(
        re.findall(r"^\s*([A-Za-z0-9_-]+)\s*=\s*(hermesAgent)\s*;$", content, flags=re.MULTILINE)
    )


def _homebrew_managed_descriptor() -> str:
    content = (REPO_ROOT / "packaging" / "homebrew" / "hermes-agent.rb").read_text()
    match = re.search(r'HERMES_MANAGED:\s*"([^"]+)"', content)
    assert match, "Could not locate Homebrew managed descriptor"
    return match.group(1)


def test_homebrew_formula_wraps_all_project_scripts():
    assert _homebrew_wrapper_list() == _project_scripts()


def test_nix_package_wraps_all_project_scripts():
    assert _nix_wrapper_list() == _project_scripts()


def test_nix_main_program_prefers_doppel():
    content = (REPO_ROOT / "nix" / "hermes-agent.nix").read_text()
    assert 'mainProgram = "doppel";' in content


def test_nix_packages_exports_preferred_and_legacy_package_aliases():
    aliases = _nix_packages_aliases()
    assert aliases["default"] == "hermesAgent"
    assert aliases["doppel-agent"] == "hermesAgent"
    assert aliases["hermes-agent"] == "hermesAgent"


def test_nix_overlay_exports_preferred_and_legacy_package_aliases():
    aliases = _nix_overlay_aliases()
    assert aliases["doppel-agent"] == "hermesAgent"
    assert aliases["hermes-agent"] == "hermesAgent"


def test_homebrew_formula_stamps_legacy_formula_descriptor():
    assert _homebrew_managed_descriptor() == "homebrew:hermes-agent"
