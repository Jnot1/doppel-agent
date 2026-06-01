from pathlib import Path


def test_profiles_customer_facing_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/profiles.py")
    text = path.read_text(encoding="utf-8")

    required = [
        "``~/.doppel/profiles/<name>/``.",
        'The "default" profile is the root Doppel home itself — ``~/.doppel``.',
        "Doppel infrastructure directories",
        "``~/.doppel``, profiles live under ``HERMES_HOME/profiles/`` so",
        "In standard deployments this is ``~/.doppel``.",
        "In Docker/custom deployments where HERMES_HOME is outside ``~/.doppel``",
        "special alias for ~/.doppel",
        "the Doppel installation itself or a common system binary.",
        "Checks: reserved names, doppel subcommands, existing binaries in PATH.",
        "conflicts with a doppel subcommand",
        "never break ``doppel profile list`` for an unrelated profile.",
        "``config.yaml`` is the user-facing Doppel config",
        "``doppel profile list``.",
        "root profile (~/.doppel).",
        "Writes to ``~/.doppel/active_profile``. Use ``\"default\"`` to clear.",
        "Returns ``\"default\"`` if HERMES_HOME is not set or points to ``~/.doppel``.",
        "Returns the profile name if HERMES_HOME points into ``~/.doppel/profiles/<name>``.",
        "The default profile IS ~/.doppel itself",
        'Importing as "default" would target ~/.doppel itself',
    ]
    forbidden = [
        "use ``~/.hermes/profiles/<name>/``.",
        "fresh installs, or an existing ``~/.hermes`` root for legacy installs.",
        "Hermes infrastructure directories",
        "``~/.hermes``, profiles live under ``HERMES_HOME/profiles/`` so",
        "In standard deployments this is ``~/.hermes``.",
        "In Docker/custom deployments where HERMES_HOME is outside ``~/.hermes``",
        "special alias for ~/.hermes",
        "the Hermes installation itself or a common system binary.",
        "Checks: reserved names, hermes subcommands, existing binaries in PATH.",
        "conflicts with a hermes subcommand",
        "never break ``hermes profile list`` for an unrelated profile.",
        "``config.yaml`` is the user-facing Hermes config",
        "``hermes profile list``.",
        "legacy ~/.hermes still works",
        "Writes to ``~/.hermes/active_profile``. Use ``\"default\"`` to clear.",
        "Returns ``\"default\"`` if HERMES_HOME is not set or points to ``~/.hermes``.",
        "Returns the profile name if HERMES_HOME points into ``~/.hermes/profiles/<name>``.",
        "The default profile IS ~/.hermes itself",
        'Importing as "default" would target ~/.hermes itself',
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
