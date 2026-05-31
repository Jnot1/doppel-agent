Homebrew packaging notes for Doppel Agent.

Use `packaging/homebrew/doppel-agent.rb` as the preferred formula in the
`jnot1/doppel-agent` tap and keep `packaging/homebrew/hermes-agent.rb` as
the legacy compatibility formula for upgrades from the old package-manager
name.

Key choices:
- Stable builds should target the semver-named sdist asset attached to each GitHub release, not the CalVer tag tarball.
- Until the fork has its own published Homebrew release pipeline, both formula files track the latest upstream `NousResearch/hermes-agent` sdist asset so Homebrew stays installable while the rebrand continues.
- `faster-whisper` now lives in the `voice` extra, which keeps wheel-only transitive dependencies out of the base Homebrew formula.
- Both formulas export the preferred `doppel*` entrypoints and the legacy `hermes*` aliases from the same venv so packaged installs stay Doppel-first without breaking existing automation.
- The wrappers export `HERMES_BUNDLED_SKILLS`, `HERMES_OPTIONAL_SKILLS`, and a formula-specific `HERMES_MANAGED=homebrew:<formula>` stamp so packaged installs keep runtime assets and can surface the exact Homebrew formula name in update guidance.
- The two formulas intentionally `conflicts_with` each other using fully-qualified `jnot1/doppel-agent/...` names because they install the same Doppel Agent binaries.

Typical update flow:
1. Bump the formula `url`, `version`, and `sha256` in both formula files.
2. Refresh Python resources with `brew update-python-resources --print-only doppel-agent` and mirror the stanza changes into `hermes-agent.rb`.
3. Keep `exclude_packages: %w[certifi cryptography pydantic]`.
4. Verify both names with Homebrew tooling (`brew style`, `brew install --dry-run`, and, in a real tap, `brew audit` / `brew test` for both formulas).
