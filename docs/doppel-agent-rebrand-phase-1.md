# Doppel Agent Rebrand: Phase 1

This branch completes the first customer-facing rebrand pass from Hermes Agent to Doppel Agent without doing a risky global rename of internal package/module paths.

## What changed

- User-facing CLI/help/docs/install text now prefers `doppel`, `doppel setup`, `doppel doctor`, and `doppel update`.
- Fresh installs now prefer `DOPPEL_HOME` / `~/.doppel` while keeping `HERMES_HOME` / `~/.hermes` compatibility.
- README, docs landing pages, setup/install/update guidance, and major CLI surfaces now describe Doppel Agent as "Your Everyday Personal AI Assistant."
- `NOTICE.md` documents the fork relationship and preserves required Hermes Agent / Nous Research attribution.

## What intentionally still says Hermes

- Python package/module namespaces such as `hermes_cli`, `hermes_constants`, and many `HERMES_*` environment variables.
- Managed install checkout directory names such as `~/.doppel/hermes-agent` and `/usr/local/lib/hermes-agent`.
- Legacy command aliases such as `hermes`.
- Service identifiers that are already baked into runtime behavior and existing installs, including `hermes-gateway` and `ai.hermes.gateway`.
- Packaging and distribution names that still resolve to the current ecosystem, including the PyPI package name `hermes-agent`.

## Why those internals were left alone

Those names are tied to imports, installer/update paths, backups, gateway supervision, service migration logic, tests, and external packaging. Renaming them in the same pass would have created a much higher risk of broken upgrades, broken service restarts, or broken installs.

## Recommended next phase

1. Centralize managed-install path and service-name resolution behind shared helpers used by installer, updater, gateway, backup, and profile code.
2. Add targeted tests for checkout-dir naming, service migration, package entrypoints, and upgrade flows across fresh and legacy installs.
3. Rename the managed checkout directory and selected service labels only after those helpers and tests are in place.
4. Re-evaluate package/distribution renames (`hermes-agent` on PyPI/Nix/etc.) as a separate release with explicit migration guidance.
