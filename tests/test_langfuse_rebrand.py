from pathlib import Path


ROOT = Path("/Users/macshelton/Documents/DoppelFork-repair2")


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def _section(text: str, heading: str) -> str:
    marker = f"### {heading}"
    start = text.index(marker)
    remainder = text[start:]
    next_heading = remainder.find("\n### ", len(marker))
    if next_heading == -1:
        return remainder
    return remainder[:next_heading]


def test_langfuse_customer_surfaces_prefer_doppel() -> None:
    runtime = _read("plugins/observability/langfuse/__init__.py")
    readme = _read("plugins/observability/langfuse/README.md")
    manifest = _read("plugins/observability/langfuse/plugin.yaml")
    en_doc = _section(
        _read("website/docs/user-guide/features/built-in-plugins.md"),
        "observability/langfuse",
    )
    zh_doc = _section(
        _read(
            "website/i18n/zh-Hans/docusaurus-plugin-content-docs/current/user-guide/features/built-in-plugins.md"
        ),
        "observability/langfuse",
    )

    docs_combined = "\n".join([readme, manifest, en_doc, zh_doc])

    required_docs = [
        "doppel plugins enable observability/langfuse",
        "doppel plugins list",
        "doppel chat -q \"hello\"",
        "~/.doppel/.env",
        "DOPPEL_LANGFUSE_PUBLIC_KEY",
        "DOPPEL_LANGFUSE_SECRET_KEY",
        "DOPPEL_LANGFUSE_BASE_URL",
        "DOPPEL_LANGFUSE_ENV",
        "DOPPEL_LANGFUSE_RELEASE",
        "DOPPEL_LANGFUSE_SAMPLE_RATE",
        "DOPPEL_LANGFUSE_MAX_CHARS",
        "DOPPEL_LANGFUSE_DEBUG",
        "Doppel turn",
    ]
    forbidden_docs = [
        "hermes plugins enable observability/langfuse",
        "hermes plugins list",
        "hermes chat -q \"hello\"",
        "~/.hermes/.env",
        "HERMES_LANGFUSE_PUBLIC_KEY",
        "HERMES_LANGFUSE_SECRET_KEY",
        "HERMES_LANGFUSE_BASE_URL",
        "HERMES_LANGFUSE_ENV",
        "HERMES_LANGFUSE_RELEASE",
        "HERMES_LANGFUSE_SAMPLE_RATE",
        "HERMES_LANGFUSE_MAX_CHARS",
        "HERMES_LANGFUSE_DEBUG",
        "Hermes turn",
        "Optional Langfuse observability for Hermes",
        "This plugin ships bundled with Hermes",
    ]

    for text in required_docs:
        assert text in docs_combined, text
    for text in forbidden_docs:
        assert text not in docs_combined, text

    required_runtime = [
        "DOPPEL_LANGFUSE_PUBLIC_KEY",
        "DOPPEL_LANGFUSE_SECRET_KEY",
        "DOPPEL_LANGFUSE_BASE_URL",
        "DOPPEL_LANGFUSE_ENV",
        "DOPPEL_LANGFUSE_RELEASE",
        "DOPPEL_LANGFUSE_SAMPLE_RATE",
        "DOPPEL_LANGFUSE_MAX_CHARS",
        "DOPPEL_LANGFUSE_DEBUG",
        "Doppel turn",
        '"source": "doppel"',
        'tags=["doppel", "langfuse"]',
    ]
    for text in required_runtime:
        assert text in runtime, text
