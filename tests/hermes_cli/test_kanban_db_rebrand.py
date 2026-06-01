from pathlib import Path


def test_kanban_db_customer_facing_surfaces_prefer_doppel() -> None:
    path = Path("/Users/macshelton/Documents/DoppelFork-repair2/hermes_cli/kanban_db.py")
    text = path.read_text(encoding="utf-8")

    required = [
        "``<root>`` is the **shared Doppel root**",
        "``doppel -p <profile>`` joins the same board",
        "the profile's Doppel home but are otherwise isolated",
        "Written by ``doppel kanban boards",
        "In standard installs ``<root>`` is ``~/.doppel``.",
        "``/opt/doppel``), ``<root>`` is ``HERMES_HOME``.",
        "written by ``doppel kanban boards switch <slug>``",
        "set by ``doppel kanban boards",
        "so that ``doppel kanban boards switch <typo>`` returns an error",
        "board — makes ``doppel kanban log`` unambiguous",
        "CLI ``doppel kanban init``",
        "``doppel kanban list --sort``",
        "manual `doppel kanban recompute`",
        "CLI user calling ``doppel kanban complete`` on a",
        "CLI user calling ``doppel kanban complete <ready-task>",
        "``doppel kanban block <id>``).",
        "completion (``doppel kanban complete <id>``) works without requiring",
        "via ``doppel kanban show <id>`` and the dashboard.",
        "reading `doppel kanban tail`",
        "`doppel kanban log` on a specific board reads its own file",
        "so ``doppel kanban daemon`` is systemd-friendly.",
        "- ``doppel kanban assignees`` for the terminal.",
        '"""Return the shared Doppel root that anchors the kanban board.',
        "all sources Doppel treats as user-controlled-but-trusted",
        "subtrees hold Doppel's own DB, metadata, and logs",
        "outside Doppel-managed storage.",
        "rather than a Doppel",
        '"""Return the interpreter-bound Doppel CLI invocation."""',
        '"""Return an absolute filesystem path for a resolved Doppel shim."""',
        '"""Return argv for a resolved Doppel executable path.',
        '"""Resolve the preferred Doppel CLI invocation as argv parts.',
        "the worker activates a profile (``doppel -p <name>``)",
        "home (``~/.doppel``), which ships the bundled skill.",
        "the implicit ``default`` profile when the default Doppel root exists",
    ]
    forbidden = [
        "``<root>`` is the **shared Hermes root**",
        "``hermes -p <profile>`` joins the same board",
        "the profile's Hermes home but are otherwise isolated",
        "Written by ``hermes kanban boards",
        "In standard installs ``<root>`` is ``~/.hermes``.",
        "``/opt/hermes``), ``<root>`` is ``HERMES_HOME``.",
        "written by ``hermes kanban boards switch <slug>``",
        "set by ``hermes kanban boards",
        "so that ``hermes kanban boards switch <typo>`` returns an error",
        "board — makes ``hermes kanban log`` unambiguous",
        "CLI ``hermes kanban init``",
        "``hermes kanban list --sort``",
        "manual `hermes kanban recompute`",
        "CLI user calling ``hermes kanban complete`` on a",
        "CLI user calling ``hermes kanban complete <ready-task>",
        "``hermes kanban block <id>``).",
        "completion (``hermes kanban complete <id>``) works without requiring",
        "via ``hermes kanban show <id>`` and the dashboard.",
        "reading `hermes kanban tail`",
        "`hermes kanban log` on a specific board reads its own file",
        "so ``hermes kanban daemon`` is systemd-friendly.",
        "- ``hermes kanban assignees`` for the terminal.",
        '"""Return the shared Hermes root that anchors the kanban board.',
        "all sources Hermes treats as user-controlled-but-trusted",
        "subtrees hold Hermes' own DB, metadata, and logs",
        "outside Hermes-managed storage.",
        "rather than a Hermes",
        '"""Return the interpreter-bound Hermes CLI invocation."""',
        '"""Return an absolute filesystem path for a resolved Hermes shim."""',
        '"""Return argv for a resolved Hermes executable path.',
        '"""Resolve the preferred Doppel/Hermes CLI invocation as argv parts.',
        "the worker activates a profile (``hermes -p <name>``)",
        "home (``~/.hermes``), which ships the bundled skill.",
        "the implicit ``default`` profile when the default Hermes root exists",
    ]

    for snippet in required:
        assert snippet in text, f"missing {snippet!r}"
    for snippet in forbidden:
        assert snippet not in text, f"forbidden {snippet!r}"
