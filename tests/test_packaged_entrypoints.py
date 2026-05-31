import re
import tomllib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def _project_scripts() -> list[str]:
    with (REPO_ROOT / "pyproject.toml").open("rb") as f:
        data = tomllib.load(f)
    return list(data["project"]["scripts"].keys())


def _homebrew_formula_text(name: str) -> str:
    return (REPO_ROOT / "packaging" / "homebrew" / f"{name}.rb").read_text()


def _homebrew_wrapper_list(name: str) -> list[str]:
    content = _homebrew_formula_text(name)
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


def _nix_pname() -> str:
    content = (REPO_ROOT / "nix" / "hermes-agent.nix").read_text()
    match = re.search(r'^\s*pname\s*=\s*"([^"]+)";', content, flags=re.MULTILINE)
    assert match, "Could not locate Nix pname"
    return match.group(1)


def _nixos_module_text() -> str:
    return (REPO_ROOT / "nix" / "nixosModules.nix").read_text()


def _nix_checks_text() -> str:
    return (REPO_ROOT / "nix" / "checks.nix").read_text()


def _nix_workflow_text() -> str:
    return (REPO_ROOT / ".github" / "workflows" / "nix.yml").read_text()


def _homebrew_managed_descriptor(name: str) -> str:
    content = _homebrew_formula_text(name)
    match = re.search(r'HERMES_MANAGED:\s*"([^"]+)"', content)
    assert match, "Could not locate Homebrew managed descriptor"
    return match.group(1)


def _homebrew_formula_source(name: str) -> tuple[str, str]:
    content = _homebrew_formula_text(name)
    url = re.search(r'^\s*url\s+"([^"]+)"', content, flags=re.MULTILINE)
    sha = re.search(r'^\s*sha256\s+"([^"]+)"', content, flags=re.MULTILINE)
    assert url and sha, "Could not locate Homebrew source url/sha256"
    return url.group(1), sha.group(1)


def _homebrew_conflicts_with(name: str) -> str:
    content = _homebrew_formula_text(name)
    match = re.search(r'^\s*conflicts_with\s+"([^"]+)"', content, flags=re.MULTILINE)
    assert match, "Could not locate Homebrew conflicts_with target"
    return match.group(1)


def test_legacy_homebrew_formula_wraps_all_project_scripts():
    assert _homebrew_wrapper_list("hermes-agent") == _project_scripts()


def test_preferred_homebrew_formula_wraps_all_project_scripts():
    assert _homebrew_wrapper_list("doppel-agent") == _project_scripts()


def test_nix_package_wraps_all_project_scripts():
    assert _nix_wrapper_list() == _project_scripts()


def test_nix_main_program_prefers_doppel():
    content = (REPO_ROOT / "nix" / "hermes-agent.nix").read_text()
    assert 'mainProgram = "doppel";' in content


def test_nix_derivation_pname_prefers_doppel_agent():
    assert _nix_pname() == "doppel-agent"


def test_nix_packages_exports_preferred_and_legacy_package_aliases():
    aliases = _nix_packages_aliases()
    assert aliases["default"] == "hermesAgent"
    assert aliases["doppel-agent"] == "hermesAgent"
    assert aliases["hermes-agent"] == "hermesAgent"


def test_nix_overlay_exports_preferred_and_legacy_package_aliases():
    aliases = _nix_overlay_aliases()
    assert aliases["doppel-agent"] == "hermesAgent"
    assert aliases["hermes-agent"] == "hermesAgent"


def test_nixos_module_keeps_legacy_service_namespace():
    content = _nixos_module_text()
    assert "options.services.hermes-agent" in content
    assert "systemd.services.hermes-agent" in content


def test_nixos_module_exposes_doppel_service_option_alias():
    content = _nixos_module_text()
    assert 'lib.mkAliasOptionModule [ "services" "doppel-agent" ] [ "services" "hermes-agent" ]' in content


def test_nixos_module_installs_doppel_systemd_service_alias():
    content = _nixos_module_text()
    assert 'aliases = [ "doppel-agent.service" ];' in content


def test_nixos_module_exposes_container_name_option_with_legacy_default():
    content = _nixos_module_text()
    assert "containerName = cfg.container.name;" in content
    assert "name = mkOption {" in content
    assert 'default = "hermes-agent";' in content


def test_nixos_module_derives_container_runtime_identity_from_service_identity():
    content = _nixos_module_text()
    assert 'containerHomeDir = "/home/${cfg.user}";' in content
    assert 'containerProvisionMarker = "/var/lib/${cfg.user}-tools-provisioned";' in content
    assert 'containerSudoersFile = "/etc/sudoers.d/${cfg.user}";' in content
    assert 'GROUP_NAME="${cfg.group}"' in content
    assert 'TARGET_USER="${cfg.user}"' in content
    assert 'TARGET_HOME="${containerHomeDir}"' in content


def test_nixos_module_container_identity_hash_covers_runtime_identity_inputs():
    content = _nixos_module_text()
    assert "name = containerName;" in content
    assert "user = cfg.user;" in content
    assert "group = cfg.group;" in content
    assert "home = containerHomeDir;" in content
    assert "workDir = containerWorkDir;" in content


def test_nix_checks_encode_package_alias_contracts():
    content = _nix_checks_text()
    assert 'package-alias-contracts =' in content
    assert 'defaultPackage.drvPath != preferredPackage.drvPath' in content
    assert 'legacyPackage.pname != "doppel-agent"' in content


def test_nix_workflow_builds_default_and_alias_packages():
    content = _nix_workflow_text()
    assert "nix build --print-build-logs .#default .#doppel-agent .#hermes-agent" in content


def test_nix_workflow_evaluates_package_alias_pnames_on_linux_and_macos():
    content = _nix_workflow_text()
    assert '.#packages.x86_64-linux.default.pname' in content
    assert '.#packages.x86_64-linux.doppel-agent.pname' in content
    assert '.#packages.x86_64-linux.hermes-agent.pname' in content
    assert '.#packages.aarch64-darwin.default.pname' in content
    assert '.#packages.aarch64-darwin.doppel-agent.pname' in content
    assert '.#packages.aarch64-darwin.hermes-agent.pname' in content
    assert '.#checks.aarch64-darwin.package-alias-contracts.drvPath' in content


def test_nix_docs_mention_preferred_doppel_service_alias():
    content = (REPO_ROOT / "website" / "docs" / "getting-started" / "nix-setup.md").read_text()
    assert "`services.doppel-agent`" in content
    assert "`doppel-agent.service`" in content
    assert "`container.name`" in content
    assert "systemctl status doppel-agent" in content
    assert 'user = "doppel";' in content
    assert 'group = "doppel";' in content
    assert 'stateDir = "/var/lib/doppel";' in content


def test_zh_nix_docs_mention_preferred_doppel_service_alias():
    content = (
        REPO_ROOT
        / "website"
        / "i18n"
        / "zh-Hans"
        / "docusaurus-plugin-content-docs"
        / "current"
        / "getting-started"
        / "nix-setup.md"
    ).read_text()
    assert "`services.doppel-agent`" in content
    assert "`doppel-agent.service`" in content
    assert "`container.name`" in content
    assert "systemctl status doppel-agent" in content
    assert 'user = "doppel";' in content
    assert 'group = "doppel";' in content
    assert 'stateDir = "/var/lib/doppel";' in content


def test_homebrew_formulae_share_the_same_release_source():
    assert _homebrew_formula_source("hermes-agent") == _homebrew_formula_source("doppel-agent")


def test_homebrew_formula_stamps_legacy_formula_descriptor():
    assert _homebrew_managed_descriptor("hermes-agent") == "homebrew:hermes-agent"


def test_homebrew_formula_stamps_preferred_formula_descriptor():
    assert _homebrew_managed_descriptor("doppel-agent") == "homebrew:doppel-agent"


def test_homebrew_formulae_conflict_using_qualified_tap_names():
    assert _homebrew_conflicts_with("doppel-agent") == "jnot1/doppel-agent/hermes-agent"
    assert _homebrew_conflicts_with("hermes-agent") == "jnot1/doppel-agent/doppel-agent"
