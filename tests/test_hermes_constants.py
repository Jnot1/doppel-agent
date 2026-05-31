"""Tests for hermes_constants module."""

import os
from pathlib import Path

import pytest

import hermes_constants
from hermes_constants import (
    VALID_REASONING_EFFORTS,
    display_hermes_home,
    get_api_server_model_owner,
    get_api_server_platform_id,
    get_default_api_server_model_name,
    get_distribution_package_name,
    get_default_hermes_root,
    get_docker_image_name,
    get_gateway_launchd_label,
    get_gateway_launchd_plist_path,
    get_gateway_service_name,
    get_gateway_systemd_unit_path,
    get_hermes_home,
    get_homebrew_formula_name,
    get_managed_checkout_dir,
    get_managed_checkout_names,
    get_official_repo_urls,
    get_official_upstream_repo_url,
    find_managed_checkout_dir,
    is_container,
    is_managed_checkout_name,
    parse_reasoning_effort,
    secure_parent_dir,
    get_upstream_archive_filename,
    get_upstream_archive_url,
    get_upstream_extracted_dir_name,
    get_upstream_install_script_url,
)


class TestGetDefaultHermesRoot:
    """Tests for get_default_hermes_root() — Docker/custom deployment awareness."""

    def test_no_hermes_home_returns_native(self, tmp_path, monkeypatch):
        """Fresh installs default to ~/.doppel when no override is set."""
        monkeypatch.delenv("DOPPEL_HOME", raising=False)
        monkeypatch.delenv("HERMES_HOME", raising=False)
        monkeypatch.setattr(Path, "home", lambda: tmp_path)

        assert get_default_hermes_root() == tmp_path / ".doppel"

    def test_hermes_home_is_native(self, tmp_path, monkeypatch):
        """When HERMES_HOME = ~/.hermes, returns ~/.hermes."""
        native = tmp_path / ".hermes"
        native.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("HERMES_HOME", str(native))
        assert get_default_hermes_root() == native

    def test_doppel_home_is_native(self, tmp_path, monkeypatch):
        """When DOPPEL_HOME = ~/.doppel, returns ~/.doppel."""
        native = tmp_path / ".doppel"
        native.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("DOPPEL_HOME", str(native))
        monkeypatch.delenv("HERMES_HOME", raising=False)
        assert get_default_hermes_root() == native

    def test_existing_legacy_home_is_preserved_when_env_unset(self, tmp_path, monkeypatch):
        """No env override should keep using ~/.hermes when that install already exists."""
        legacy = tmp_path / ".hermes"
        legacy.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.delenv("DOPPEL_HOME", raising=False)
        monkeypatch.delenv("HERMES_HOME", raising=False)
        assert get_default_hermes_root() == legacy

    def test_preferred_home_wins_when_both_native_homes_exist(self, tmp_path, monkeypatch):
        """When both roots exist, prefer the rebrand-native ~/.doppel home."""
        legacy = tmp_path / ".hermes"
        current = tmp_path / ".doppel"
        legacy.mkdir()
        current.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.delenv("DOPPEL_HOME", raising=False)
        monkeypatch.delenv("HERMES_HOME", raising=False)
        assert get_default_hermes_root() == current

    def test_doppel_home_override_beats_legacy_home_override(self, tmp_path, monkeypatch):
        """DOPPEL_HOME is the preferred override when both env vars are set."""
        doppel_home = tmp_path / "doppel-home"
        hermes_home = tmp_path / "hermes-home"
        doppel_home.mkdir()
        hermes_home.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("DOPPEL_HOME", str(doppel_home))
        monkeypatch.setenv("HERMES_HOME", str(hermes_home))
        assert get_default_hermes_root() == doppel_home

    def test_hermes_home_is_profile(self, tmp_path, monkeypatch):
        """When HERMES_HOME is a profile under ~/.hermes, returns ~/.hermes."""
        native = tmp_path / ".hermes"
        profile = native / "profiles" / "coder"
        profile.mkdir(parents=True)
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("HERMES_HOME", str(profile))
        assert get_default_hermes_root() == native

    def test_hermes_home_is_docker(self, tmp_path, monkeypatch):
        """When HERMES_HOME points outside ~/.hermes (Docker), returns HERMES_HOME."""
        docker_home = tmp_path / "opt" / "data"
        docker_home.mkdir(parents=True)
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("HERMES_HOME", str(docker_home))
        assert get_default_hermes_root() == docker_home

    def test_hermes_home_is_custom_path(self, tmp_path, monkeypatch):
        """Any HERMES_HOME outside ~/.hermes is treated as the root."""
        custom = tmp_path / "my-hermes-data"
        custom.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("HERMES_HOME", str(custom))
        assert get_default_hermes_root() == custom

    def test_docker_profile_active(self, tmp_path, monkeypatch):
        """When a Docker profile is active (HERMES_HOME=<root>/profiles/<name>),
        returns the Docker root, not the profile dir."""
        docker_root = tmp_path / "opt" / "data"
        profile = docker_root / "profiles" / "coder"
        profile.mkdir(parents=True)
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("HERMES_HOME", str(profile))
        assert get_default_hermes_root() == docker_root


class TestGetHermesHome:
    def test_no_env_uses_preferred_native_home(self, tmp_path, monkeypatch):
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.delenv("DOPPEL_HOME", raising=False)
        monkeypatch.delenv("HERMES_HOME", raising=False)

        assert get_hermes_home() == tmp_path / ".doppel"

    def test_existing_legacy_root_is_preserved_when_env_unset(self, tmp_path, monkeypatch):
        legacy = tmp_path / ".hermes"
        legacy.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.delenv("DOPPEL_HOME", raising=False)
        monkeypatch.delenv("HERMES_HOME", raising=False)

        assert get_hermes_home() == legacy

    def test_doppel_home_override_wins(self, tmp_path, monkeypatch):
        preferred = tmp_path / "preferred-home"
        preferred.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.setenv("DOPPEL_HOME", str(preferred))
        monkeypatch.setenv("HERMES_HOME", str(tmp_path / "legacy-home"))

        assert get_hermes_home() == preferred

    def test_display_hermes_home_uses_preferred_native_path(self, tmp_path, monkeypatch):
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        monkeypatch.delenv("DOPPEL_HOME", raising=False)
        monkeypatch.delenv("HERMES_HOME", raising=False)

        assert display_hermes_home() == "~/.doppel"


class TestManagedCheckoutNames:
    def test_includes_legacy_and_rebrand_checkout_names(self):
        """Managed installs should recognize both legacy and rebrand dirs."""
        assert get_managed_checkout_names() == ("doppel-agent", "hermes-agent")

    def test_name_match_accepts_both_checkout_dirs(self):
        """Both managed checkout names are valid while migration is in progress."""
        assert is_managed_checkout_name("hermes-agent")
        assert is_managed_checkout_name("doppel-agent")
        assert not is_managed_checkout_name("hermes")

    def test_canonical_checkout_dir_uses_rebrand_name(self, tmp_path):
        assert get_managed_checkout_dir(tmp_path) == tmp_path / "doppel-agent"

    def test_find_managed_checkout_dir_prefers_rebrand_dir(self, tmp_path):
        legacy = tmp_path / "hermes-agent"
        current = tmp_path / "doppel-agent"
        legacy.mkdir()
        current.mkdir()

        assert find_managed_checkout_dir(tmp_path) == current

    def test_find_managed_checkout_dir_falls_back_to_legacy_dir(self, tmp_path):
        legacy = tmp_path / "hermes-agent"
        legacy.mkdir()

        assert find_managed_checkout_dir(tmp_path) == legacy


class TestDistributionIdentity:
    def test_api_server_default_model_name(self):
        assert get_default_api_server_model_name() == "doppel-agent"

    def test_api_server_platform_id(self):
        assert get_api_server_platform_id() == "doppel-agent"

    def test_api_server_model_owner(self):
        assert get_api_server_model_owner() == "doppel"

    def test_package_distribution_name(self):
        assert get_distribution_package_name() == "hermes-agent"

    def test_homebrew_formula_name(self):
        assert get_homebrew_formula_name() == "hermes-agent"

    def test_docker_image_name(self):
        assert get_docker_image_name() == "nousresearch/hermes-agent"


class TestUpstreamIdentity:
    def test_official_upstream_repo_url(self):
        assert get_official_upstream_repo_url() == "https://github.com/NousResearch/hermes-agent.git"

    def test_official_repo_urls(self):
        assert get_official_repo_urls() == frozenset({
            "https://github.com/NousResearch/hermes-agent.git",
            "git@github.com:NousResearch/hermes-agent.git",
            "https://github.com/NousResearch/hermes-agent",
            "git@github.com:NousResearch/hermes-agent",
        })

    def test_upstream_archive_url(self):
        assert (
            get_upstream_archive_url("main")
            == "https://github.com/NousResearch/hermes-agent/archive/refs/heads/main.zip"
        )

    def test_upstream_archive_filename(self):
        assert get_upstream_archive_filename("main") == "hermes-agent-main.zip"

    def test_upstream_extracted_dir_name(self):
        assert get_upstream_extracted_dir_name("main") == "hermes-agent-main"

    def test_upstream_install_script_url(self):
        assert (
            get_upstream_install_script_url()
            == "https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh"
        )


class TestGatewayNamingHelpers:
    def test_gateway_service_name_default_profile(self):
        assert get_gateway_service_name() == "doppel-gateway"

    def test_gateway_service_name_profile_suffix(self):
        assert get_gateway_service_name("coder") == "doppel-gateway-coder"

    def test_gateway_service_names_include_legacy_alias(self):
        names_fn = getattr(hermes_constants, "get_gateway_service_names", None)
        assert callable(names_fn)
        assert names_fn("coder") == (
            "doppel-gateway-coder",
            "hermes-gateway-coder",
        )

    def test_gateway_systemd_unit_path_user_scope(self, tmp_path):
        user_home = tmp_path / "alice"
        assert get_gateway_systemd_unit_path("coder", user_home=user_home) == (
            user_home / ".config" / "systemd" / "user" / "doppel-gateway-coder.service"
        )

    def test_gateway_systemd_unit_path_system_scope(self):
        assert get_gateway_systemd_unit_path("coder", system=True) == Path(
            "/etc/systemd/system/doppel-gateway-coder.service"
        )

    def test_gateway_launchd_label_default_profile(self):
        assert get_gateway_launchd_label() == "ai.doppel.gateway"

    def test_gateway_launchd_label_profile_suffix(self):
        assert get_gateway_launchd_label("coder") == "ai.doppel.gateway-coder"

    def test_gateway_launchd_labels_include_legacy_alias(self):
        labels_fn = getattr(hermes_constants, "get_gateway_launchd_labels", None)
        assert callable(labels_fn)
        assert labels_fn("coder") == (
            "ai.doppel.gateway-coder",
            "ai.hermes.gateway-coder",
        )

    def test_gateway_launchd_plist_path(self, tmp_path):
        user_home = tmp_path / "alice"
        assert get_gateway_launchd_plist_path("coder", user_home=user_home) == (
            user_home / "Library" / "LaunchAgents" / "ai.doppel.gateway-coder.plist"
        )

    def test_gateway_task_name_default_profile(self):
        name_fn = getattr(hermes_constants, "get_gateway_task_name", None)
        assert callable(name_fn)
        assert name_fn() == "Doppel_Gateway"

    def test_gateway_task_name_profile_suffix(self):
        name_fn = getattr(hermes_constants, "get_gateway_task_name", None)
        assert callable(name_fn)
        assert name_fn("coder") == "Doppel_Gateway_coder"

    def test_gateway_task_names_include_legacy_alias(self):
        names_fn = getattr(hermes_constants, "get_gateway_task_names", None)
        assert callable(names_fn)
        assert names_fn("coder") == (
            "Doppel_Gateway_coder",
            "Hermes_Gateway_coder",
        )


class TestIsContainer:
    """Tests for is_container() — Docker/Podman detection."""

    def _reset_cache(self, monkeypatch):
        """Reset the cached detection result before each test."""
        monkeypatch.setattr(hermes_constants, "_container_detected", None)

    def test_detects_dockerenv(self, monkeypatch, tmp_path):
        """/.dockerenv triggers container detection."""
        self._reset_cache(monkeypatch)
        monkeypatch.setattr(os.path, "exists", lambda p: p == "/.dockerenv")
        assert is_container() is True

    def test_detects_containerenv(self, monkeypatch, tmp_path):
        """/run/.containerenv triggers container detection (Podman)."""
        self._reset_cache(monkeypatch)
        monkeypatch.setattr(os.path, "exists", lambda p: p == "/run/.containerenv")
        assert is_container() is True

    def test_detects_cgroup_docker(self, monkeypatch, tmp_path):
        """/proc/1/cgroup containing 'docker' triggers detection."""
        import builtins
        self._reset_cache(monkeypatch)
        monkeypatch.setattr(os.path, "exists", lambda p: False)
        cgroup_file = tmp_path / "cgroup"
        cgroup_file.write_text("12:memory:/docker/abc123\n")
        _real_open = builtins.open
        monkeypatch.setattr("builtins.open", lambda p, *a, **kw: _real_open(str(cgroup_file), *a, **kw) if p == "/proc/1/cgroup" else _real_open(p, *a, **kw))
        assert is_container() is True

    def test_negative_case(self, monkeypatch, tmp_path):
        """Returns False on a regular Linux host."""
        import builtins
        self._reset_cache(monkeypatch)
        monkeypatch.setattr(os.path, "exists", lambda p: False)
        cgroup_file = tmp_path / "cgroup"
        cgroup_file.write_text("12:memory:/\n")
        _real_open = builtins.open
        monkeypatch.setattr("builtins.open", lambda p, *a, **kw: _real_open(str(cgroup_file), *a, **kw) if p == "/proc/1/cgroup" else _real_open(p, *a, **kw))
        assert is_container() is False

    def test_caches_result(self, monkeypatch):
        """Second call uses cached value without re-probing."""
        monkeypatch.setattr(hermes_constants, "_container_detected", True)
        assert is_container() is True
        # Even if we make os.path.exists return False, cached value wins
        monkeypatch.setattr(os.path, "exists", lambda p: False)
        assert is_container() is True


class TestParseReasoningEffort:
    """Tests for parse_reasoning_effort() — string → reasoning config dict."""

    @pytest.mark.parametrize("value", ["", "   ", "\t", "\n"])
    def test_empty_or_whitespace_returns_none(self, value):
        """Empty / whitespace-only input falls back to caller default (None)."""
        assert parse_reasoning_effort(value) is None

    def test_none_disables_reasoning(self):
        """The literal "none" disables reasoning explicitly."""
        assert parse_reasoning_effort("none") == {"enabled": False}

    @pytest.mark.parametrize("level", list(VALID_REASONING_EFFORTS))
    def test_each_valid_level(self, level):
        """Every level listed in VALID_REASONING_EFFORTS is accepted as-is."""
        assert parse_reasoning_effort(level) == {"enabled": True, "effort": level}

    @pytest.mark.parametrize(
        "raw, expected_effort",
        [
            ("MEDIUM", "medium"),
            ("High", "high"),
            ("  low  ", "low"),
            ("\tXHIGH\n", "xhigh"),
            ("None", False),
        ],
    )
    def test_case_and_whitespace_normalized(self, raw, expected_effort):
        """Mixed case and surrounding whitespace are normalized before lookup."""
        result = parse_reasoning_effort(raw)
        if expected_effort is False:
            assert result == {"enabled": False}
        else:
            assert result == {"enabled": True, "effort": expected_effort}

    @pytest.mark.parametrize(
        "value",
        ["bogus", "very-high", "max", "0", "off", "true", "default"],
    )
    def test_unknown_levels_return_none(self, value):
        """Unrecognized strings fall back to the caller default (None)."""
        assert parse_reasoning_effort(value) is None

    def test_known_supported_levels_are_documented(self):
        """Guard against silently dropping a documented level.

        The docstring promises "minimal", "low", "medium", "high", "xhigh".
        If someone removes one from VALID_REASONING_EFFORTS without updating
        the docstring, this test will fail and force the call out.
        """
        documented = {"minimal", "low", "medium", "high", "xhigh"}
        assert documented.issubset(set(VALID_REASONING_EFFORTS))


class TestSecureParentDir:
    """Tests for secure_parent_dir() — prevents chmod on / or top-level dirs."""

    def test_safe_path_calls_chmod(self, tmp_path, monkeypatch):
        """Normal nested path (depth >= 3) should call os.chmod."""
        safe_dir = tmp_path / "home" / "user" / ".hermes"
        safe_dir.mkdir(parents=True)
        target = safe_dir / "auth.json"
        target.touch()

        called_with = []
        monkeypatch.setattr(os, "chmod", lambda p, m: called_with.append((str(p), m)))

        secure_parent_dir(target)
        assert len(called_with) == 1
        assert called_with[0] == (str(safe_dir), 0o700)

    def test_root_dir_skipped(self, monkeypatch):
        """Parent resolving to / must NOT be chmod'd."""
        called_with = []
        monkeypatch.setattr(os, "chmod", lambda p, m: called_with.append((str(p), m)))

        # Path("/foo").parent == Path("/")
        secure_parent_dir(Path("/foo"))
        assert called_with == []

    def test_top_level_dir_skipped(self, monkeypatch):
        """Parent resolving to a top-level dir (depth 2) must NOT be chmod'd."""
        called_with = []
        monkeypatch.setattr(os, "chmod", lambda p, m: called_with.append((str(p), m)))

        # Path("/usr/foo").parent == Path("/usr") — depth 2
        secure_parent_dir(Path("/usr/foo"))
        assert called_with == []

    def test_two_component_path_skipped(self, monkeypatch):
        """Parent with < 3 resolved parts must NOT be chmod'd.

        Uses monkeypatch to avoid macOS firmlink resolution of /home.
        """
        called_with = []
        monkeypatch.setattr(os, "chmod", lambda p, m: called_with.append((str(p), m)))

        # Mock Path.resolve to return a short path regardless of OS quirks
        original_resolve = Path.resolve
        def mock_resolve(self):
            if str(self) == "/x/y":
                return Path("/x")
            return original_resolve(self)
        monkeypatch.setattr(Path, "resolve", mock_resolve)

        secure_parent_dir(Path("/x/y"))
        assert called_with == []

    def test_oserror_suppressed(self, tmp_path, monkeypatch):
        """OSError from chmod should be silently caught."""
        safe_dir = tmp_path / "a" / "b" / "c"
        safe_dir.mkdir(parents=True)
        target = safe_dir / "file.json"
        target.touch()

        def raise_oserror(p, m):
            raise OSError("permission denied")

        monkeypatch.setattr(os, "chmod", raise_oserror)
        # Should not raise
        secure_parent_dir(target)

    def test_symlink_resolved(self, tmp_path, monkeypatch):
        """Symlinks should be resolved before checking depth."""
        real_dir = tmp_path / "a" / "b"
        real_dir.mkdir(parents=True)
        target = real_dir / "file.json"
        target.touch()

        # Create a symlink with fewer path components
        link = tmp_path / "link"
        link.symlink_to(real_dir)
        link_target = link / "file.json"

        called_with = []
        monkeypatch.setattr(os, "chmod", lambda p, m: called_with.append((str(p), m)))

        # Even though /tmp/link has only 3 parts, the resolved path has 4
        # The resolved parent (real_dir) has depth 4, so it should be chmod'd
        secure_parent_dir(link_target)
        assert len(called_with) == 1
        assert called_with[0] == (str(real_dir), 0o700)
