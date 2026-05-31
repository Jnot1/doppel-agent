"""Runtime smoke tests for the PowerShell installer.

These tests execute ``scripts/install.ps1`` with a real PowerShell engine when
available. They intentionally avoid the full installer flow and instead cover
safe, bounded behaviors:

- stage-protocol metadata commands via the existing PowerShell smoke harness
- managed checkout migration in the repository stage against a local git fixture
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent
INSTALL_PS1 = REPO_ROOT / "scripts" / "install.ps1"
STAGE_PROTOCOL_SMOKE = REPO_ROOT / "scripts" / "tests" / "test-install-ps1-stage-protocol.ps1"
POWERSHELL = shutil.which("pwsh") or shutil.which("powershell")


pytestmark = pytest.mark.skipif(POWERSHELL is None, reason="requires pwsh or powershell")


def _run(cmd: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd or REPO_ROOT),
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def _runtime_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("LOCALAPPDATA", None)
    return env


def test_install_ps1_stage_protocol_smoke_runs_under_available_powershell() -> None:
    result = _run(
        [
            POWERSHELL,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(STAGE_PROTOCOL_SMOKE),
        ],
        env=_runtime_env(),
    )

    assert result.returncode == 0, (
        f"stdout:\n{result.stdout}\n\nstderr:\n{result.stderr}"
    )


def test_install_ps1_repository_stage_migrates_legacy_checkout(tmp_path: Path) -> None:
    origin = tmp_path / "origin.git"
    work = tmp_path / "work"
    hermes_home = tmp_path / ".hermes"
    legacy_checkout = hermes_home / "hermes-agent"
    preferred_checkout = hermes_home / "doppel-agent"

    _run(["git", "init", "--bare", str(origin)]).check_returncode()
    work.mkdir(parents=True, exist_ok=True)
    _run(["git", "-C", str(work), "init", "-b", "main"]).check_returncode()
    _run(["git", "-C", str(work), "config", "user.name", "test"]).check_returncode()
    _run(["git", "-C", str(work), "config", "user.email", "test@example.com"]).check_returncode()
    (work / "README.md").write_text("ok\n", encoding="utf-8")
    _run(["git", "-C", str(work), "add", "README.md"]).check_returncode()
    _run(["git", "-C", str(work), "commit", "-m", "seed"]).check_returncode()
    _run(["git", "-C", str(work), "remote", "add", "origin", str(origin)]).check_returncode()
    _run(["git", "-C", str(work), "push", "-u", "origin", "main"]).check_returncode()
    _run(["git", "clone", str(origin), str(legacy_checkout)]).check_returncode()

    result = _run(
        [
            POWERSHELL,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(INSTALL_PS1),
            "-HermesHome",
            str(hermes_home),
            "-NonInteractive",
            "-Json",
            "-Stage",
            "repository",
        ],
        env=_runtime_env(),
    )

    assert result.returncode == 0, (
        f"stdout:\n{result.stdout}\n\nstderr:\n{result.stderr}"
    )
    assert preferred_checkout.joinpath(".git").exists()
    assert not legacy_checkout.exists()
