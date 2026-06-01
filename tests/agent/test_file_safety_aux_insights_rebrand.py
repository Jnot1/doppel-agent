from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_file_safety_auxiliary_and_insights_surfaces_prefer_doppel() -> None:
    file_safety = _read("agent/file_safety.py")
    auxiliary_client = _read("agent/auxiliary_client.py")
    insights = _read("agent/insights.py")

    legacy_home_fallback = 'return Path(os.path.expanduser("~/.hermes"))'

    assert legacy_home_fallback not in file_safety
    assert file_safety.count('os.getenv("DOPPEL_HOME")') == 2
    assert file_safety.count('os.getenv("HERMES_HOME")') >= 2
    assert file_safety.count('os.path.expanduser("~/.doppel")') == 2
    assert "or ``cat ~/.hermes/.env`` and exfiltrate the file." not in file_safety
    assert "or ``cat ~/.doppel/.env`` and exfiltrate the file." in file_safety
    assert '"""Return the active profile name derived from HERMES_HOME.' not in file_safety
    assert '"""Return the active profile name derived from DOPPEL_HOME.' in file_safety
    assert '``~/.hermes``              -> ``"default"``' not in file_safety
    assert '``~/.doppel``              -> ``"default"``' in file_safety
    assert '``~/.hermes/profiles/X``  -> ``"X"``' not in file_safety
    assert '``~/.doppel/profiles/X``  -> ``"X"``' in file_safety

    assert "3. Nous Portal (~/.hermes/auth.json active provider)" not in auxiliary_client
    assert "3. Nous Portal (~/.doppel/auth.json active provider)" in auxiliary_client
    assert '"""Read and validate ~/.hermes/auth.json for an active Nous provider.' not in auxiliary_client
    assert '"""Read and validate ~/.doppel/auth.json for an active Nous provider.' in auxiliary_client

    assert "Session Insights Engine for Hermes Agent." not in insights
    assert "Session Insights Engine for Doppel Agent." in insights
    assert "adapted for Hermes Agent's" not in insights
    assert "adapted for Doppel Agent's" in insights
