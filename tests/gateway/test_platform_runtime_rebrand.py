from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def test_platform_runtime_surfaces_prefer_doppel() -> None:
    dingtalk = _read("gateway/platforms/dingtalk.py")
    slack = _read("gateway/platforms/slack.py")
    feishu = _read("gateway/platforms/feishu.py")
    feishu_comment_rules = _read("gateway/platforms/feishu_comment_rules.py")
    email = _read("gateway/platforms/email.py")
    weixin = _read("gateway/platforms/weixin.py")
    wecom = _read("gateway/platforms/wecom.py")
    sms = _read("gateway/platforms/sms.py")
    telegram = _read("gateway/platforms/telegram.py")
    matrix = _read("gateway/platforms/matrix.py")

    assert '"title": "Hermes"' not in dingtalk
    assert '"title": "Doppel"' in dingtalk

    assert "Hermes handoff" not in slack
    assert "Doppel handoff" in slack
    assert "own Hermes session" not in slack
    assert "own Doppel session" in slack

    assert "what Hermes currently supports" not in feishu
    assert "what Doppel currently supports" in feishu
    assert "Another local Hermes gateway is already using this Feishu app_id" not in feishu
    assert "Another local Doppel gateway is already using this Feishu app_id" in feishu
    assert '"User-Agent": "Mozilla/5.0 (compatible; HermesAgent/1.0)"' not in feishu
    assert '"User-Agent": "Mozilla/5.0 (compatible; DoppelAgent/1.0)"' in feishu
    assert "supported by Hermes webhook mode" not in feishu
    assert "supported by Doppel webhook mode" in feishu
    assert "that Hermes does not act on" not in feishu
    assert "that Doppel does not act on" in feishu
    assert "onto Hermes' SessionSource fields" not in feishu
    assert "onto Doppel's SessionSource fields" in feishu
    assert "`hermes gateway setup`" not in feishu
    assert "`doppel gateway setup`" in feishu

    assert "Config: ~/.hermes/feishu_comment_rules.json" not in feishu_comment_rules
    assert "Config: ~/.doppel/feishu_comment_rules.json" in feishu_comment_rules
    assert "Pairing store: ~/.hermes/feishu_comment_pairing.json." not in feishu_comment_rules
    assert "Pairing store: ~/.doppel/feishu_comment_pairing.json." in feishu_comment_rules

    assert "Email platform adapter for the Hermes gateway." not in email
    assert "Email platform adapter for the Doppel gateway." in email
    assert "Allows users to interact with Hermes by sending emails." not in email
    assert "Allows users to interact with Doppel by sending emails." in email

    assert "Connects Hermes Agent to WeChat personal accounts" not in weixin
    assert "Connects Doppel Agent to WeChat personal accounts" in weixin
    assert "Native Hermes adapter for Weixin personal accounts." not in weixin
    assert "Native Doppel adapter for Weixin personal accounts." in weixin
    assert "may never reach Hermes regardless of this " not in weixin
    assert "may never reach Doppel regardless of this " in weixin
    assert "not in Hermes." not in weixin
    assert "not in Doppel." in weixin

    assert '"User-Agent": "HermesAgent/1.0"' not in wecom
    assert '"User-Agent": "DoppelAgent/1.0"' in wecom

    assert "Twilio SMS <-> Hermes gateway adapter." not in sms
    assert "Twilio SMS <-> Doppel gateway adapter." in sms
    assert "own Hermes session" not in sms
    assert "own Doppel session" in sms

    assert "when ``hermes update --gateway``" not in telegram
    assert "when ``doppel update --gateway``" in telegram
    assert "CLI ``hermes model`` picker" not in telegram
    assert "CLI ``doppel model`` picker" in telegram
    assert "Scripts live in ~/.hermes/scripts/gmail-triage/." not in telegram
    assert "Scripts live in ~/.doppel/scripts/gmail-triage/." in telegram
    assert "Telegram groups can contain several Hermes bot profiles." not in telegram
    assert "Telegram groups can contain several Doppel bot profiles." in telegram

    assert 'normal phrases like "Hermes Agent" become "Agent".' not in matrix
    assert 'normal phrases like "Doppel Agent" become "Agent".' in matrix
