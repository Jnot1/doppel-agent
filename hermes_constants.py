"""Shared constants for Doppel Agent.

Import-safe module with no dependencies — can be imported from anywhere
without risk of circular imports.
"""

import os
import sys
import sysconfig
from contextvars import ContextVar, Token
from pathlib import Path


_profile_fallback_warned: bool = False
_UNSET = object()
_HERMES_HOME_OVERRIDE: ContextVar[str | object] = ContextVar(
    "_HERMES_HOME_OVERRIDE", default=_UNSET
)


PREFERRED_AGENT_NAME = "Doppel Agent"
LEGACY_AGENT_NAME = "Hermes Agent"
PREFERRED_SHORT_NAME = "Doppel"
LEGACY_SHORT_NAME = "Hermes"
PREFERRED_CLI_COMMAND = "doppel"
LEGACY_CLI_COMMAND = "hermes"
PREFERRED_HOME_ENV = "DOPPEL_HOME"
LEGACY_HOME_ENV = "HERMES_HOME"
PREFERRED_NATIVE_HOME_DIR = ".doppel"
LEGACY_NATIVE_HOME_DIR = ".hermes"
PACKAGE_DISTRIBUTION_NAME = "hermes-agent"
HOMEBREW_FORMULA_NAME = PACKAGE_DISTRIBUTION_NAME
DOCKER_IMAGE_NAME = "nousresearch/hermes-agent"
MANAGED_CHECKOUT_NAMES = ("doppel-agent", "hermes-agent")
GATEWAY_SERVICE_BASE = "doppel-gateway"
LEGACY_GATEWAY_SERVICE_BASES = ("hermes-gateway",)
LAUNCHD_GATEWAY_LABEL_BASE = "ai.doppel.gateway"
LEGACY_LAUNCHD_GATEWAY_LABEL_BASES = ("ai.hermes.gateway",)
WINDOWS_GATEWAY_TASK_BASE = "Doppel_Gateway"
LEGACY_WINDOWS_GATEWAY_TASK_BASES = ("Hermes_Gateway",)
WINDOWS_GATEWAY_TASK_DESCRIPTION = f"{PREFERRED_AGENT_NAME} Gateway - Messaging Platform Integration"
FORK_REPO_SLUG = "Jnot1/doppel-agent"
UPSTREAM_REPO_SLUG = "NousResearch/hermes-agent"
FORK_REPO_WEB_URL = f"https://github.com/{FORK_REPO_SLUG}"
FORK_REPO_URL = f"{FORK_REPO_WEB_URL}.git"
UPSTREAM_REPO_WEB_URL = f"https://github.com/{UPSTREAM_REPO_SLUG}"
UPSTREAM_REPO_URL = f"{UPSTREAM_REPO_WEB_URL}.git"
UPSTREAM_REPO_SSH_URL = f"git@github.com:{UPSTREAM_REPO_SLUG}"
UPSTREAM_REPO_GIT_URLS = frozenset({
    UPSTREAM_REPO_URL,
    f"{UPSTREAM_REPO_SSH_URL}.git",
    UPSTREAM_REPO_WEB_URL,
    UPSTREAM_REPO_SSH_URL,
})


def get_cli_prog_name(argv0: str | None = None) -> str:
    """Return the user-facing CLI command name for the current invocation."""
    raw = argv0 if argv0 is not None else (sys.argv[0] if sys.argv else "")
    stem = Path(raw).stem.lower()
    if stem in {"hermes", "hermes-agent"}:
        return LEGACY_CLI_COMMAND
    if stem in {"doppel", "doppel-agent"}:
        return PREFERRED_CLI_COMMAND
    return PREFERRED_CLI_COMMAND


def get_distribution_package_name() -> str:
    """Return the Python package distribution name used for upgrades."""
    return PACKAGE_DISTRIBUTION_NAME


def get_homebrew_formula_name() -> str:
    """Return the Homebrew formula name for this distribution."""
    return HOMEBREW_FORMULA_NAME


def get_docker_image_name() -> str:
    """Return the published Docker image name for this distribution."""
    return DOCKER_IMAGE_NAME


def get_official_upstream_repo_slug() -> str:
    """Return the canonical upstream GitHub slug."""
    return UPSTREAM_REPO_SLUG


def get_official_upstream_repo_url() -> str:
    """Return the canonical upstream git remote URL."""
    return UPSTREAM_REPO_URL


def get_official_repo_urls() -> frozenset[str]:
    """Return normalized official upstream remote URL variants."""
    return UPSTREAM_REPO_GIT_URLS


def get_upstream_extracted_dir_name(branch: str) -> str:
    """Return the extracted top-level directory name for an upstream ZIP."""
    return f"{get_distribution_package_name()}-{branch}"


def get_upstream_archive_filename(branch: str) -> str:
    """Return the downloaded ZIP filename for an upstream branch archive."""
    return f"{get_upstream_extracted_dir_name(branch)}.zip"


def get_upstream_archive_url(branch: str) -> str:
    """Return the GitHub archive URL for an upstream branch."""
    return f"{UPSTREAM_REPO_WEB_URL}/archive/refs/heads/{branch}.zip"


def get_upstream_install_script_url(ref: str = "main") -> str:
    """Return the raw install-script URL for the official upstream repo."""
    return (
        f"https://raw.githubusercontent.com/"
        f"{get_official_upstream_repo_slug()}/{ref}/scripts/install.sh"
    )


def get_managed_checkout_names() -> tuple[str, ...]:
    """Return managed checkout directory names recognized during migration.

    Order matters: the current on-disk default stays first until the managed
    checkout rename is explicitly migrated in a later phase.
    """
    return MANAGED_CHECKOUT_NAMES


def is_managed_checkout_name(name: str) -> bool:
    """Return True when *name* is a recognized managed checkout directory."""
    return name in MANAGED_CHECKOUT_NAMES


def get_managed_checkout_dir(root: str | Path | None = None) -> Path:
    """Return the canonical managed checkout path for the current phase."""
    base = Path(root) if root is not None else get_default_hermes_root()
    return base / MANAGED_CHECKOUT_NAMES[0]


def get_managed_checkout_candidates(root: str | Path | None = None) -> tuple[Path, ...]:
    """Return every managed checkout path accepted during migration."""
    base = Path(root) if root is not None else get_default_hermes_root()
    return tuple(base / name for name in MANAGED_CHECKOUT_NAMES)


def find_managed_checkout_dir(root: str | Path | None = None) -> Path | None:
    """Return the first existing managed checkout dir under *root*, if any."""
    for candidate in get_managed_checkout_candidates(root):
        if candidate.exists():
            return candidate
    return None


def get_gateway_service_name(profile_suffix: str = "") -> str:
    """Return the gateway service name for the default profile or a suffix."""
    suffix = str(profile_suffix).strip()
    return f"{GATEWAY_SERVICE_BASE}-{suffix}" if suffix else GATEWAY_SERVICE_BASE


def get_gateway_service_names(profile_suffix: str = "") -> tuple[str, ...]:
    """Return current + legacy gateway service names for a profile suffix."""
    suffix = str(profile_suffix).strip()
    names = [get_gateway_service_name(suffix)]
    for base in LEGACY_GATEWAY_SERVICE_BASES:
        names.append(f"{base}-{suffix}" if suffix else base)
    return tuple(dict.fromkeys(names))


def get_gateway_service_glob() -> str:
    """Return the systemd unit glob used to discover gateway services."""
    return f"{GATEWAY_SERVICE_BASE}*"


def get_gateway_systemd_unit_path(
    profile_suffix: str = "",
    *,
    system: bool = False,
    user_home: str | Path | None = None,
) -> Path:
    """Return the systemd unit path for the gateway service."""
    name = get_gateway_service_name(profile_suffix)
    if system:
        return Path("/etc/systemd/system") / f"{name}.service"
    home = Path(user_home) if user_home is not None else Path.home()
    return home / ".config" / "systemd" / "user" / f"{name}.service"


def get_gateway_launchd_label(profile_suffix: str = "") -> str:
    """Return the launchd label for the default profile or a suffix."""
    suffix = str(profile_suffix).strip()
    return (
        f"{LAUNCHD_GATEWAY_LABEL_BASE}-{suffix}"
        if suffix
        else LAUNCHD_GATEWAY_LABEL_BASE
    )


def get_gateway_launchd_labels(profile_suffix: str = "") -> tuple[str, ...]:
    """Return current + legacy gateway launchd labels for a profile suffix."""
    suffix = str(profile_suffix).strip()
    labels = [get_gateway_launchd_label(suffix)]
    for base in LEGACY_LAUNCHD_GATEWAY_LABEL_BASES:
        labels.append(f"{base}-{suffix}" if suffix else base)
    return tuple(dict.fromkeys(labels))


def get_gateway_task_name(profile_suffix: str = "") -> str:
    """Return the Windows Scheduled Task name for a gateway profile."""
    suffix = str(profile_suffix).strip()
    return (
        f"{WINDOWS_GATEWAY_TASK_BASE}_{suffix}"
        if suffix
        else WINDOWS_GATEWAY_TASK_BASE
    )


def get_gateway_task_names(profile_suffix: str = "") -> tuple[str, ...]:
    """Return current + legacy Windows task names for a profile suffix."""
    suffix = str(profile_suffix).strip()
    names = [get_gateway_task_name(suffix)]
    for base in LEGACY_WINDOWS_GATEWAY_TASK_BASES:
        names.append(f"{base}_{suffix}" if suffix else base)
    return tuple(dict.fromkeys(names))


def _get_launchd_user_home() -> Path:
    """Return the real OS account home for launchd agents."""
    import pwd

    return Path(pwd.getpwuid(os.getuid()).pw_dir)


def get_gateway_launchd_plist_path(
    profile_suffix: str = "",
    *,
    user_home: str | Path | None = None,
) -> Path:
    """Return the launchd plist path for the gateway service."""
    home = Path(user_home) if user_home is not None else _get_launchd_user_home()
    return home / "Library" / "LaunchAgents" / f"{get_gateway_launchd_label(profile_suffix)}.plist"


def set_hermes_home_override(path: str | Path | None) -> Token:
    """Set a context-local Hermes home override and return its reset token.

    This is for in-process, per-task scoping.  It deliberately does not mutate
    ``os.environ`` because that is shared by every thread in the process.
    """
    value: str | object = _UNSET if path is None else str(path)
    return _HERMES_HOME_OVERRIDE.set(value)


def reset_hermes_home_override(token: Token) -> None:
    """Restore the previous context-local Hermes home override."""
    _HERMES_HOME_OVERRIDE.reset(token)


def get_hermes_home_override() -> str | None:
    """Return the active context-local Hermes home override, if any."""
    override = _HERMES_HOME_OVERRIDE.get()
    if override is _UNSET or not override:
        return None
    return str(override)


def _get_env_home_value() -> str:
    """Return the preferred home override from the process environment."""
    return (
        os.environ.get(PREFERRED_HOME_ENV, "").strip()
        or os.environ.get(LEGACY_HOME_ENV, "").strip()
    )


def _get_native_home_roots(home: Path | None = None) -> tuple[Path, Path]:
    """Return the preferred and legacy native home roots for *home*."""
    base = home if home is not None else Path.home()
    return (
        base / PREFERRED_NATIVE_HOME_DIR,
        base / LEGACY_NATIVE_HOME_DIR,
    )


def _select_native_home_root(home: Path | None = None) -> Path:
    """Choose the native home root when no env override is set.

    Fresh installs use the preferred Doppel root. Existing legacy Hermes roots
    are preserved in place until explicitly migrated. When both exist, prefer
    the current Doppel root.
    """
    preferred, legacy = _get_native_home_roots(home)
    if preferred.exists():
        return preferred
    if legacy.exists():
        return legacy
    return preferred


def _display_home_path(path: Path) -> str:
    """Render *path* using ``~/`` shorthand when it lives under ``Path.home()``."""
    try:
        return "~/" + str(path.relative_to(Path.home()))
    except ValueError:
        return str(path)


def _resolve_env_home_root(env_path: Path) -> Path:
    """Resolve an env-specified home or profile path to its root directory."""
    preferred_root, legacy_root = _get_native_home_roots()
    resolved_env_path = env_path.resolve()
    for native_root in (preferred_root, legacy_root):
        try:
            resolved_env_path.relative_to(native_root.resolve())
            return native_root
        except ValueError:
            continue

    if env_path.parent.name == "profiles":
        return env_path.parent.parent

    return env_path


def get_hermes_home() -> Path:
    """Return the Hermes home directory (default: ~/.doppel).

    Reads ``DOPPEL_HOME`` first, then ``HERMES_HOME``, and finally falls back
    to the native Doppel or legacy Hermes root for local installs.
    This is the single source of truth — all other copies should import this.

    When neither home env is set but an ``active_profile`` file indicates a
    non-default profile is active, emits a loud one-shot warning to stderr so
    cross-profile data corruption is diagnosable instead of silent. Behavior
    is unchanged otherwise — we still return the selected native root —
    because raising here would brick 30+ module-level callers that import
    this at load time. Subprocess spawners are expected to propagate
    ``DOPPEL_HOME`` explicitly (legacy ``HERMES_HOME`` also works). See
    https://github.com/NousResearch/hermes-agent/issues/18594.
    """
    override = get_hermes_home_override()
    if override:
        return Path(override)

    val = _get_env_home_value()
    if val:
        return Path(val)

    native_root = _select_native_home_root()

    # Guard: if a non-default profile is sticky-active, warn once that
    # the fallback to the default profile is almost certainly wrong.
    global _profile_fallback_warned
    if not _profile_fallback_warned:
        try:
            active_path = native_root / "active_profile"
            active = active_path.read_text().strip() if active_path.exists() else ""
        except (UnicodeDecodeError, OSError):
            active = ""
        if active and active != "default":
            _profile_fallback_warned = True
            # Write directly to stderr.  We intentionally do NOT route this
            # through ``logging`` because (a) this function is called at
            # module-import time from 30+ sites, often before logging is
            # configured, and (b) root-logger propagation would double-emit
            # on consoles where a StreamHandler is already attached.
            import sys
            msg = (
                f"[{PREFERRED_HOME_ENV} fallback] {PREFERRED_HOME_ENV}/"
                f"{LEGACY_HOME_ENV} are unset but active profile is "
                f"{active!r}. Falling back to {_display_home_path(native_root)}, "
                f"which is the DEFAULT profile root — not {active!r}. Any "
                f"data this process writes will land in the wrong profile. "
                f"The subprocess spawner should pass {PREFERRED_HOME_ENV} "
                f"explicitly (legacy {LEGACY_HOME_ENV} also works; see issue "
                f"#18594)."
            )
            try:
                sys.stderr.write(msg + "\n")
                sys.stderr.flush()
            except Exception:
                pass

    return native_root


def get_default_hermes_root() -> Path:
    """Return the root Hermes directory for profile-level operations.

    In standard deployments this prefers ``~/.doppel`` while preserving an
    existing ``~/.hermes`` root in place until migration.

    In Docker or custom deployments where the selected home env points outside
    the native roots (e.g. ``/opt/data``), returns that env path directly
    — that IS the root.

    In profile mode where the selected home env is ``<root>/profiles/<name>``,
    returns ``<root>`` so that ``profile list`` can see all profiles.
    Works both for standard (``~/.doppel/profiles/coder`` or
    ``~/.hermes/profiles/coder``) and Docker
    (``/opt/data/profiles/coder``) layouts.

    Import-safe — no dependencies beyond stdlib.
    """
    env_home = _get_env_home_value()
    if not env_home:
        return _select_native_home_root()
    return _resolve_env_home_root(Path(env_home))


def _get_packaged_data_dir(name: str) -> Path | None:
    """Return an installed data-files directory if one exists.

    Used to discover bundled skills/optional-skills when Hermes is installed
    from a wheel that emitted them via setuptools data_files.
    """
    candidates = []
    for scheme in ("data", "purelib", "platlib"):
        raw = sysconfig.get_path(scheme)
        if raw:
            candidates.append(Path(raw) / name)
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def get_optional_skills_dir(default: Path | None = None) -> Path:
    """Return the optional-skills directory, honoring package-manager wrappers.

    Packaged installs may ship ``optional-skills`` outside the Python package
    tree and expose it via ``HERMES_OPTIONAL_SKILLS``.
    """
    override = os.getenv("HERMES_OPTIONAL_SKILLS", "").strip()
    if override:
        return Path(override)
    packaged = _get_packaged_data_dir("optional-skills")
    if packaged is not None:
        return packaged
    if default is not None:
        return default
    return get_hermes_home() / "optional-skills"


def get_optional_mcps_dir(default: Path | None = None) -> Path:
    """Return the optional-mcps directory, honoring package-manager wrappers.

    Mirrors :func:`get_optional_skills_dir` for the MCP catalog (Nous-approved
    Model Context Protocol servers shipped with the repo but disabled by
    default). Packaged installs may ship ``optional-mcps`` outside the Python
    package tree and expose it via ``HERMES_OPTIONAL_MCPS``.
    """
    override = os.getenv("HERMES_OPTIONAL_MCPS", "").strip()
    if override:
        return Path(override)
    packaged = _get_packaged_data_dir("optional-mcps")
    if packaged is not None:
        return packaged
    if default is not None:
        return default
    return get_hermes_home() / "optional-mcps"


def get_bundled_skills_dir(default: Path | None = None) -> Path:
    """Return the bundled skills directory for source and packaged installs.

    Resolution order:
        1. ``HERMES_BUNDLED_SKILLS`` env var (Nix wrapper / explicit override)
        2. Wheel-installed ``<sysconfig data>/skills`` (pip install path)
        3. Caller-supplied ``default`` (typically the source-checkout path)
        4. ``<HERMES_HOME>/skills`` last-resort
    """
    override = os.getenv("HERMES_BUNDLED_SKILLS", "").strip()
    if override:
        return Path(override)
    packaged = _get_packaged_data_dir("skills")
    if packaged is not None:
        return packaged
    if default is not None:
        return default
    return get_hermes_home() / "skills"


def get_hermes_dir(new_subpath: str, old_name: str) -> Path:
    """Resolve a Hermes subdirectory with backward compatibility.

    New installs get the consolidated layout (e.g. ``cache/images``).
    Existing installs that already have the old path (e.g. ``image_cache``)
    keep using it — no migration required.

    Args:
        new_subpath: Preferred path relative to HERMES_HOME (e.g. ``"cache/images"``).
        old_name: Legacy path relative to HERMES_HOME (e.g. ``"image_cache"``).

    Returns:
        Absolute ``Path`` — old location if it exists on disk, otherwise the new one.
    """
    home = get_hermes_home()
    old_path = home / old_name
    if old_path.exists():
        return old_path
    return home / new_subpath


def display_hermes_home() -> str:
    """Return a user-friendly display string for the current HERMES_HOME.

    Uses ``~/`` shorthand for readability::

        default:  ``~/.doppel``
        profile:  ``~/.doppel/profiles/coder``
        custom:   ``/opt/doppel-custom``

    Use this in **user-facing** print/log messages instead of hardcoding
    ``~/.doppel`` or ``~/.hermes``. For code that needs a real ``Path``, use
    :func:`get_hermes_home` instead.
    """
    return _display_home_path(get_hermes_home())


def secure_parent_dir(path: Path) -> None:
    """Chmod ``0o700`` on the parent directory of *path*, but only if safe.

    Refuses to chmod ``/`` or any top-level directory (resolved parent with
    fewer than 3 parts, i.e. ``/`` or any direct child like ``/usr``) to
    prevent catastrophic host bricking when ``HERMES_HOME`` or other path
    env vars resolve to an unexpected location.

    See https://github.com/NousResearch/hermes-agent/issues/25821.
    """
    parent = path.parent.resolve()
    # Refuse root and its direct children (/usr, /home, /var, /tmp, …).
    if parent == Path("/") or len(parent.parts) < 3:
        return
    try:
        os.chmod(parent, 0o700)
    except OSError:
        pass


def get_subprocess_home() -> str | None:
    """Return a per-profile HOME directory for subprocesses, or None.

    When ``{HERMES_HOME}/home/`` exists on disk, subprocesses should use it
    as ``HOME`` so system tools (git, ssh, gh, npm …) write their configs
    inside the Hermes data directory instead of the OS-level ``/root`` or
    ``~/``.  This provides:

    * **Docker persistence** — tool configs land inside the persistent volume.
    * **Profile isolation** — each profile gets its own git identity, SSH
      keys, gh tokens, etc.

    The Python process's own ``os.environ["HOME"]`` and ``Path.home()`` are
    **never** modified — only subprocess environments should inject this value.
    Activation is directory-based: if the ``home/`` subdirectory doesn't
    exist, returns ``None`` and behavior is unchanged.
    """
    hermes_home = (
        get_hermes_home_override()
        or os.getenv(PREFERRED_HOME_ENV)
        or os.getenv(LEGACY_HOME_ENV)
    )
    if not hermes_home:
        return None
    profile_home = os.path.join(hermes_home, "home")
    if os.path.isdir(profile_home):
        return profile_home
    return None


VALID_REASONING_EFFORTS = ("minimal", "low", "medium", "high", "xhigh")


def parse_reasoning_effort(effort: str) -> dict | None:
    """Parse a reasoning effort level into a config dict.

    Valid levels: "none", "minimal", "low", "medium", "high", "xhigh".
    Returns None when the input is empty or unrecognized (caller uses default).
    Returns {"enabled": False} for "none".
    Returns {"enabled": True, "effort": <level>} for valid effort levels.
    """
    if not effort or not effort.strip():
        return None
    effort = effort.strip().lower()
    if effort == "none":
        return {"enabled": False}
    if effort in VALID_REASONING_EFFORTS:
        return {"enabled": True, "effort": effort}
    return None


def is_termux() -> bool:
    """Return True when running inside a Termux (Android) environment.

    Checks ``TERMUX_VERSION`` (set by Termux) or the Termux-specific
    ``PREFIX`` path.  Import-safe — no heavy deps.
    """
    prefix = os.getenv("PREFIX", "")
    return bool(os.getenv("TERMUX_VERSION") or "com.termux/files/usr" in prefix)


_wsl_detected: bool | None = None


def is_wsl() -> bool:
    """Return True when running inside WSL (Windows Subsystem for Linux).

    Checks ``/proc/version`` for the ``microsoft`` marker that both WSL1
    and WSL2 inject.  Result is cached for the process lifetime.
    Import-safe — no heavy deps.
    """
    global _wsl_detected
    if _wsl_detected is not None:
        return _wsl_detected
    try:
        with open("/proc/version", "r", encoding="utf-8") as f:
            _wsl_detected = "microsoft" in f.read().lower()
    except Exception:
        _wsl_detected = False
    return _wsl_detected


_container_detected: bool | None = None


def is_container() -> bool:
    """Return True when running inside a Docker/Podman container.

    Checks ``/.dockerenv`` (Docker), ``/run/.containerenv`` (Podman),
    and ``/proc/1/cgroup`` for container runtime markers.  Result is
    cached for the process lifetime.  Import-safe — no heavy deps.
    """
    global _container_detected
    if _container_detected is not None:
        return _container_detected
    if os.path.exists("/.dockerenv"):
        _container_detected = True
        return True
    if os.path.exists("/run/.containerenv"):
        _container_detected = True
        return True
    try:
        with open("/proc/1/cgroup", "r", encoding="utf-8") as f:
            cgroup = f.read()
            if "docker" in cgroup or "podman" in cgroup or "/lxc/" in cgroup:
                _container_detected = True
                return True
    except OSError:
        pass
    _container_detected = False
    return False


# ─── Well-Known Paths ─────────────────────────────────────────────────────────


def get_config_path() -> Path:
    """Return the path to ``config.yaml`` under HERMES_HOME.

    Replaces the ``get_hermes_home() / "config.yaml"`` pattern repeated
    in 7+ files (skill_utils.py, hermes_logging.py, hermes_time.py, etc.).
    """
    return get_hermes_home() / "config.yaml"


def get_skills_dir() -> Path:
    """Return the path to the skills directory under HERMES_HOME."""
    return get_hermes_home() / "skills"



def get_env_path() -> Path:
    """Return the path to the ``.env`` file under HERMES_HOME."""
    return get_hermes_home() / ".env"


# ─── Network Preferences ─────────────────────────────────────────────────────


def apply_ipv4_preference(force: bool = False) -> None:
    """Monkey-patch ``socket.getaddrinfo`` to prefer IPv4 connections.

    On servers with broken or unreachable IPv6, Python tries AAAA records
    first and hangs for the full TCP timeout before falling back to IPv4.
    This affects httpx, requests, urllib, the OpenAI SDK — everything that
    uses ``socket.getaddrinfo``.

    When *force* is True, patches ``getaddrinfo`` so that calls with
    ``family=AF_UNSPEC`` (the default) resolve as ``AF_INET`` instead,
    skipping IPv6 entirely.  If no A record exists, falls back to the
    original unfiltered resolution so pure-IPv6 hosts still work.

    Safe to call multiple times — only patches once.
    Set ``network.force_ipv4: true`` in ``config.yaml`` to enable.
    """
    if not force:
        return

    import socket

    # Guard against double-patching
    if getattr(socket.getaddrinfo, "_hermes_ipv4_patched", False):
        return

    _original_getaddrinfo = socket.getaddrinfo

    def _ipv4_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        if family == 0:  # AF_UNSPEC — caller didn't request a specific family
            try:
                return _original_getaddrinfo(
                    host, port, socket.AF_INET, type, proto, flags
                )
            except socket.gaierror:
                # No A record — fall back to full resolution (pure-IPv6 hosts)
                return _original_getaddrinfo(host, port, family, type, proto, flags)
        return _original_getaddrinfo(host, port, family, type, proto, flags)

    _ipv4_getaddrinfo._hermes_ipv4_patched = True  # type: ignore[attr-defined]
    socket.getaddrinfo = _ipv4_getaddrinfo  # type: ignore[assignment]


# ─── Streaming Response Constants ────────────────────────────────────────────

# Response ID for partial stream stubs used during error recovery
PARTIAL_STREAM_STUB_ID = "partial-stream-stub"

FINISH_REASON_LENGTH = "length"


OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODELS_URL = f"{OPENROUTER_BASE_URL}/models"
