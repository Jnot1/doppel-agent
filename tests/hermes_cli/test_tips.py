"""Tests for hermes_cli/tips.py — random tip display at session start."""

from hermes_cli.tips import TIPS, get_random_tip


class TestTipsCorpus:
    """Validate the tip corpus itself."""

    def test_has_at_least_200_tips(self):
        assert len(TIPS) >= 200, f"Expected 200+ tips, got {len(TIPS)}"

    def test_no_duplicates(self):
        assert len(TIPS) == len(set(TIPS)), "Duplicate tips found"

    def test_all_tips_are_strings(self):
        for i, tip in enumerate(TIPS):
            assert isinstance(tip, str), f"Tip {i} is not a string: {type(tip)}"

    def test_no_empty_tips(self):
        for i, tip in enumerate(TIPS):
            assert tip.strip(), f"Tip {i} is empty or whitespace-only"

    def test_max_length_reasonable(self):
        """Tips should fit on a single terminal line (~120 chars max)."""
        for i, tip in enumerate(TIPS):
            assert len(tip) <= 150, (
                f"Tip {i} too long ({len(tip)} chars): {tip[:60]}..."
            )

    def test_no_leading_trailing_whitespace(self):
        for i, tip in enumerate(TIPS):
            assert tip == tip.strip(), f"Tip {i} has leading/trailing whitespace"

    def test_cron_tip_is_doppel_first(self):
        assert (
            'Cron jobs can attach skills: doppel cron add --skill blogwatcher "Check for new posts".'
            in TIPS
        )
        assert not any("hermes cron add --skill blogwatcher" in tip for tip in TIPS)

    def test_cli_tip_examples_are_doppel_first(self):
        assert (
            'doppel -c resumes your most recent CLI session. doppel -c "project name" resumes by title.'
            in TIPS
        )
        assert (
            "doppel doctor --fix diagnoses and auto-repairs config and dependency issues."
            in TIPS
        )
        assert not any("hermes " in tip for tip in TIPS)

    def test_product_branding_in_tips_is_doppel_first(self):
        assert (
            "Ctrl+Z suspends Doppel to the background — run fg in your shell to resume."
            in TIPS
        )
        assert (
            "Doppel runs on 21 messaging platforms: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, IRC, Microsoft Teams, email, and more."
            in TIPS
        )
        assert not any("Hermes" in tip for tip in TIPS)

    def test_context_file_tips_prefer_doppel_filenames(self):
        assert (
            "Context files (.doppel.md, AGENTS.md) are security-scanned for prompt injection before loading."
            in TIPS
        )
        assert (
            "Doppel loads project context from .doppel.md, AGENTS.md, CLAUDE.md, or .cursorrules (first match)."
            in TIPS
        )
        assert not any(".hermes.md" in tip for tip in TIPS)
        assert not any("legacy .hermes.md" in tip for tip in TIPS)


class TestGetRandomTip:
    """Validate the get_random_tip() function."""

    def test_returns_string(self):
        tip = get_random_tip()
        assert isinstance(tip, str)
        assert len(tip) > 0

    def test_returns_tip_from_corpus(self):
        tip = get_random_tip()
        assert tip in TIPS

    def test_randomness(self):
        """Multiple calls should eventually return different tips."""
        seen = set()
        for _ in range(50):
            seen.add(get_random_tip())
        # With 200+ tips and 50 draws, we should see at least 10 unique
        assert len(seen) >= 10, f"Only got {len(seen)} unique tips in 50 draws"


class TestTipIntegrationInCLI:
    """Test that the tip display code in cli.py works correctly."""

    def test_tip_import_works(self):
        """The import used in cli.py must succeed."""
        from hermes_cli.tips import get_random_tip
        assert callable(get_random_tip)

    def test_tip_display_format(self):
        """Verify the Rich markup format doesn't break."""
        tip = get_random_tip()
        color = "#B8860B"
        markup = f"[dim {color}]✦ Tip: {tip}[/]"
        # Should not contain nested/broken Rich tags
        assert markup.count("[/]") == 1
        assert "[dim #B8860B]" in markup
