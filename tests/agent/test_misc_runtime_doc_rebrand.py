from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_misc_runtime_and_doc_surfaces_prefer_doppel() -> None:
    compression = _read("agent/conversation_compression.py")
    models_dev = _read("agent/models_dev.py")
    secret_sources = _read("agent/secret_sources/__init__.py")

    assert "process (or `hermes update`) to resync." not in compression
    assert "process (or `doppel update`) to resync." in compression

    assert "Disk cache (~/.hermes/models_dev_cache.json)" not in models_dev
    assert "Disk cache (~/.doppel/models_dev_cache.json)" in models_dev

    assert "credentials at process startup, _after_ ~/.hermes/.env has loaded." not in secret_sources
    assert "credentials at process startup, _after_ ~/.doppel/.env has loaded." in secret_sources
