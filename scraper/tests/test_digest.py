"""Tests for the daily digest generator."""

import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch  # noqa: F401

from scraper.core.digest import DigestGenerator


class TestParseFrontmatter(unittest.TestCase):
    """Test the frontmatter parser, especially YAML-hostile titles."""

    def test_clean_yaml(self):
        text = "---\ntitle: Simple Title\nurl: https://example.com\nsite: test\n---\n\nBody text"
        meta, body = DigestGenerator._parse_frontmatter(text)
        assert meta["title"] == "Simple Title"
        assert meta["url"] == "https://example.com"
        assert body == "Body text"

    def test_colon_in_title(self):
        text = "---\ntitle: GitHub - user/repo: A description here\nurl: https://github.com\nsite: github\n---\n\nBody"
        meta, body = DigestGenerator._parse_frontmatter(text)
        assert "GitHub" in meta["title"]
        assert "description" in meta["title"]
        assert meta["site"] == "github"

    def test_no_frontmatter(self):
        text = "Just plain text"
        meta, body = DigestGenerator._parse_frontmatter(text)
        assert meta == {}
        assert body == "Just plain text"

    def test_empty_string(self):
        meta, body = DigestGenerator._parse_frontmatter("")
        assert meta == {}

    def test_frontmatter_only(self):
        text = "---\ntitle: Only FM\n---\n"
        meta, body = DigestGenerator._parse_frontmatter(text)
        assert meta["title"] == "Only FM"

    def test_multiple_colons_in_value(self):
        text = "---\ntitle: Time: 10:30 AM: Report\nsite: news\n---\n\nContent"
        meta, body = DigestGenerator._parse_frontmatter(text)
        assert "10:30" in meta["title"] or "Time" in meta["title"]
        assert meta["site"] == "news"


class TestLoadSummaries(unittest.TestCase):
    """Test loading and parsing summary files from disk."""

    def test_loads_valid_summaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary_dir = Path(tmp)
            (summary_dir / "test-summary.md").write_text("---\ntitle: Test Article\nurl: https://example.com\nsite: devto\n---\n\nSummary body here.")
            gen = DigestGenerator.__new__(DigestGenerator)
            summaries = gen._load_summaries(summary_dir)
            assert len(summaries) == 1
            assert summaries[0]["title"] == "Test Article"
            assert summaries[0]["url"] == "https://example.com"
            assert summaries[0]["site"] == "devto"
            assert "Summary body here" in summaries[0]["body"]

    def test_loads_broken_yaml_gracefully(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary_dir = Path(tmp)
            (summary_dir / "broken-summary.md").write_text("---\ntitle: GitHub - user/repo: Description with colons\nsite: github\n---\n\nBody")
            gen = DigestGenerator.__new__(DigestGenerator)
            summaries = gen._load_summaries(summary_dir)
            assert len(summaries) == 1
            assert "GitHub" in summaries[0]["title"]

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = DigestGenerator.__new__(DigestGenerator)
            summaries = gen._load_summaries(Path(tmp))
            assert summaries == []

    def test_skips_non_md_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary_dir = Path(tmp)
            (summary_dir / "data.json").write_text('{"key": "value"}')
            gen = DigestGenerator.__new__(DigestGenerator)
            summaries = gen._load_summaries(summary_dir)
            assert summaries == []


class TestCategorizeSummaries(unittest.TestCase):
    """Test keyword-based article categorization."""

    def _sample_categories(self):
        return {
            "ai_ml": {"label": "AI and Machine Learning", "keywords": ["ai", "machine learning", "llm", "gpt"]},
            "cybersecurity": {"label": "Cybersecurity and Privacy", "keywords": ["security", "vulnerability", "breach"]},
            "devtools": {"label": "Software Engineering and Dev Tools", "keywords": ["rust", "python", "compiler", "api"]},
        }

    def test_categorize_assigns_correct_category(self):
        summaries = [
            {"title": "New GPT model released", "body": "OpenAI launches a new LLM with AI capabilities", "site": "hn", "url": "https://a.com"},
            {"title": "Critical vulnerability in Linux", "body": "A security breach was discovered", "site": "reddit", "url": "https://b.com"},
            {"title": "Rust 2.0 compiler improvements", "body": "New API for the Rust programming language", "site": "devto", "url": "https://c.com"},
        ]
        result = DigestGenerator._categorize_summaries(summaries, self._sample_categories())

        assert "ai_ml" in result
        assert len(result["ai_ml"]) == 1
        assert result["ai_ml"][0]["title"] == "New GPT model released"

        assert "cybersecurity" in result
        assert len(result["cybersecurity"]) == 1

        assert "devtools" in result
        assert len(result["devtools"]) == 1

    def test_uncategorized_fallback(self):
        summaries = [
            {"title": "Random cooking recipe", "body": "How to make pasta from scratch", "site": "blog", "url": "https://d.com"},
        ]
        result = DigestGenerator._categorize_summaries(summaries, self._sample_categories())
        assert "uncategorized" in result
        assert len(result["uncategorized"]) == 1

    def test_empty_categories(self):
        summaries = [
            {"title": "Something", "body": "Body text", "site": "test", "url": "https://e.com"},
        ]
        result = DigestGenerator._categorize_summaries(summaries, {})
        assert "uncategorized" in result

    def test_empty_summaries(self):
        result = DigestGenerator._categorize_summaries([], self._sample_categories())
        assert result == {}


class TestDetectCrossSource(unittest.TestCase):
    """Test cross-source story detection via title similarity."""

    def test_similar_titles_different_sources_grouped(self):
        summaries = [
            {"title": "OpenAI releases GPT-5 model", "site": "hackernews", "url": "https://a.com"},
            {"title": "OpenAI releases GPT-5 model today", "site": "reddit", "url": "https://b.com"},
            {"title": "Totally unrelated article", "site": "devto", "url": "https://c.com"},
        ]
        groups = DigestGenerator._detect_cross_source(summaries)
        assert len(groups) == 1
        assert len(groups[0]) == 2
        sites = {s["site"] for s in groups[0]}
        assert "hackernews" in sites
        assert "reddit" in sites

    def test_same_source_not_grouped(self):
        summaries = [
            {"title": "Same title article", "site": "hackernews", "url": "https://a.com"},
            {"title": "Same title article", "site": "hackernews", "url": "https://b.com"},
        ]
        groups = DigestGenerator._detect_cross_source(summaries)
        assert len(groups) == 0

    def test_no_similar_titles(self):
        summaries = [
            {"title": "Apple announces new iPhone", "site": "hn", "url": "https://a.com"},
            {"title": "Rust compiler performance boost", "site": "reddit", "url": "https://b.com"},
        ]
        groups = DigestGenerator._detect_cross_source(summaries)
        assert len(groups) == 0

    def test_empty_summaries(self):
        groups = DigestGenerator._detect_cross_source([])
        assert groups == []


class TestApplyPreferences(unittest.TestCase):
    """Test blocklist filtering via preferences."""

    def test_keyword_blocklist(self):
        summaries = [
            {"title": "Bitcoin hits new high", "body": "cryptocurrency market surges", "url": "https://a.com"},
            {"title": "AI model released", "body": "New neural network", "url": "https://b.com"},
        ]
        prefs = {"blocklist": {"keywords": ["cryptocurrency"], "domains": []}}
        result = DigestGenerator._apply_preferences(summaries, prefs)
        assert len(result) == 1
        assert result[0]["title"] == "AI model released"

    def test_domain_blocklist(self):
        summaries = [
            {"title": "Article One", "body": "content", "url": "https://medium.com/article-1"},
            {"title": "Article Two", "body": "content", "url": "https://github.com/repo"},
        ]
        prefs = {"blocklist": {"keywords": [], "domains": ["medium.com"]}}
        result = DigestGenerator._apply_preferences(summaries, prefs)
        assert len(result) == 1
        assert result[0]["title"] == "Article Two"

    def test_empty_blocklist_returns_all(self):
        summaries = [
            {"title": "Article", "body": "body", "url": "https://a.com"},
        ]
        prefs = {"blocklist": {"keywords": [], "domains": []}}
        result = DigestGenerator._apply_preferences(summaries, prefs)
        assert len(result) == 1

    def test_missing_blocklist_key(self):
        summaries = [{"title": "Article", "body": "body", "url": "https://a.com"}]
        result = DigestGenerator._apply_preferences(summaries, {})
        assert len(result) == 1


class TestLoadCategories(unittest.TestCase):
    """Test YAML category loading."""

    def test_loads_from_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            config_dir = Path(tmp)
            (config_dir / "categories.yaml").write_text("categories:\n  ai_ml:\n    label: AI\n    keywords: [ai, ml]\n")
            gen = DigestGenerator.__new__(DigestGenerator)
            gen.config_dir = config_dir
            cats = gen._load_categories()
            assert "ai_ml" in cats
            assert cats["ai_ml"]["label"] == "AI"
            assert "ai" in cats["ai_ml"]["keywords"]

    def test_missing_file_returns_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = DigestGenerator.__new__(DigestGenerator)
            gen.config_dir = Path(tmp)
            cats = gen._load_categories()
            assert cats == {}


class TestLoadPreferences(unittest.TestCase):
    """Test user preferences loading with graceful fallback."""

    def test_loads_from_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            config_dir = Path(tmp)
            (config_dir / "preferences.yaml").write_text("blocklist:\n  keywords: [nft]\n  domains: []\ndigest:\n  max_stories_per_section: 5\n")
            gen = DigestGenerator.__new__(DigestGenerator)
            gen.config_dir = config_dir
            prefs = gen._load_preferences()
            assert prefs["blocklist"]["keywords"] == ["nft"]
            assert prefs["digest"]["max_stories_per_section"] == 5

    def test_missing_file_returns_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = DigestGenerator.__new__(DigestGenerator)
            gen.config_dir = Path(tmp)
            prefs = gen._load_preferences()
            assert prefs["blocklist"]["keywords"] == []
            assert prefs["blocklist"]["domains"] == []
            assert prefs["digest"]["max_stories_per_section"] == 8


class TestBuildDigestPrompt(unittest.TestCase):
    """Test prompt construction for the LLM."""

    def _make_generator(self):
        gen = DigestGenerator.__new__(DigestGenerator)
        gen.config_dir = Path(__file__).parent.parent / "config"
        return gen

    def test_basic_prompt_with_categorized(self):
        gen = self._make_generator()
        categorized = {
            "ai_ml": [
                {"title": "AI Article", "url": "https://a.com", "site": "devto", "body": "AI content."},
            ],
        }
        prompt = gen._build_digest_prompt(categorized, [], {}, gen._default_preferences())
        assert "AI" in prompt
        assert "AI Article" in prompt

    def test_top_stories_in_prompt(self):
        gen = self._make_generator()
        top_stories = [
            [
                {"title": "Breaking News", "url": "https://a.com", "site": "hn"},
                {"title": "Breaking News", "url": "https://b.com", "site": "reddit"},
            ]
        ]
        prompt = gen._build_digest_prompt({}, top_stories, {}, gen._default_preferences())
        assert "TOP STORIES" in prompt
        assert "Breaking News" in prompt
        assert "hn" in prompt
        assert "reddit" in prompt

    def test_trending_indicator_in_prompt(self):
        gen = self._make_generator()
        categorized = {
            "devtools": [{"title": "Hot Topic", "url": "https://hot.com", "site": "hn", "body": "Trending."}],
        }
        trending = {"https://hot.com": 5}
        prompt = gen._build_digest_prompt(categorized, [], trending, gen._default_preferences())
        assert "trending: seen 5x" in prompt

    def test_truncation(self):
        gen = self._make_generator()
        # Create enough data to exceed MAX_DIGEST_INPUT_CHARS (60000)
        categorized = {
            "devtools": [{"title": f"Article {i}", "url": f"https://example.com/{i}", "site": "test", "body": "x" * 5000} for i in range(50)],
        }
        prefs = gen._default_preferences()
        prefs["digest"]["max_stories_per_section"] = 50  # Don't cap, let truncation trigger
        prompt = gen._build_digest_prompt(categorized, [], {}, prefs)
        assert "truncated" in prompt

    def test_max_stories_per_section_overflow(self):
        gen = self._make_generator()
        categorized = {
            "ai_ml": [{"title": f"AI Article {i}", "url": f"https://a.com/{i}", "site": "hn", "body": "Content."} for i in range(12)],
        }
        prefs = gen._default_preferences()
        prefs["digest"]["max_stories_per_section"] = 3
        prompt = gen._build_digest_prompt(categorized, [], {}, prefs)
        # First 3 should be in main section, rest in notable mentions
        assert "Notable Mentions" in prompt


class TestSaveDigest(unittest.TestCase):
    """Test digest file saving."""

    def test_saves_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = DigestGenerator.__new__(DigestGenerator)
            gen.project_root = Path(tmp)
            gen.model_name = "test-model"

            date_str = "2026-01-15"
            result = gen._save_digest(date_str, "# Digest Content\n\nHello world.")
            assert result is not None

            digest_path = Path(tmp) / "data" / date_str / "digest.md"
            assert digest_path.exists()

            content = digest_path.read_text()
            assert "date: '2026-01-15'" in content
            assert "model: test-model" in content
            assert "# Digest Content" in content


class TestGetPeriodRange(unittest.TestCase):
    """Test date range calculation for periodic digests."""

    def _make_generator(self):
        gen = DigestGenerator.__new__(DigestGenerator)
        return gen

    def test_weekly_from_sunday(self):
        """Monday trigger -> yesterday is Sunday -> Mon-Sun of that week."""
        gen = self._make_generator()
        start, end = gen._get_period_range("weekly", "2026-04-05")  # Sunday
        assert start == "2026-03-30"  # Monday
        assert end == "2026-04-05"  # Sunday

    def test_weekly_from_saturday(self):
        gen = self._make_generator()
        start, end = gen._get_period_range("weekly", "2026-04-04")  # Saturday
        assert start == "2026-03-30"  # Monday of that week
        assert end == "2026-04-05"  # Sunday of that week

    def test_weekly_from_monday(self):
        gen = self._make_generator()
        start, end = gen._get_period_range("weekly", "2026-03-30")  # Monday
        assert start == "2026-03-30"
        assert end == "2026-04-05"

    def test_monthly_end_of_march(self):
        """1st April trigger -> yesterday is March 31 -> full March."""
        gen = self._make_generator()
        start, end = gen._get_period_range("monthly", "2026-03-31")
        assert start == "2026-03-01"
        assert end == "2026-03-31"

    def test_monthly_february_non_leap(self):
        gen = self._make_generator()
        start, end = gen._get_period_range("monthly", "2026-02-15")
        assert start == "2026-02-01"
        assert end == "2026-02-28"

    def test_monthly_february_leap_year(self):
        gen = self._make_generator()
        start, end = gen._get_period_range("monthly", "2028-02-15")  # 2028 is leap
        assert start == "2028-02-01"
        assert end == "2028-02-29"

    def test_monthly_december(self):
        gen = self._make_generator()
        start, end = gen._get_period_range("monthly", "2026-12-25")
        assert start == "2026-12-01"
        assert end == "2026-12-31"

    def test_yearly(self):
        """Jan 1 trigger -> yesterday is Dec 31 -> full year."""
        gen = self._make_generator()
        start, end = gen._get_period_range("yearly", "2025-12-31")
        assert start == "2025-01-01"
        assert end == "2025-12-31"

    def test_yearly_mid_year(self):
        gen = self._make_generator()
        start, end = gen._get_period_range("yearly", "2026-06-15")
        assert start == "2026-01-01"
        assert end == "2026-12-31"


class TestCollectDailyDigests(unittest.TestCase):
    """Test collecting daily digest files from data directories."""

    def _make_generator(self, tmp_dir):
        gen = DigestGenerator.__new__(DigestGenerator)
        gen.project_root = Path(tmp_dir)
        return gen

    def test_collects_digests_in_range(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            # Create digest files for 3 days
            for day in ["2026-04-01", "2026-04-02", "2026-04-03"]:
                d = Path(tmp) / "data" / day
                d.mkdir(parents=True)
                (d / "digest.md").write_text(f"---\ndate: '{day}'\n---\n\nDigest for {day}")

            digests = gen._collect_daily_digests("2026-04-01", "2026-04-03")
            assert len(digests) == 3
            assert "2026-04-01" in digests[0]
            assert "2026-04-03" in digests[2]

    def test_skips_missing_dates(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            # Only create day 1 and 3, skip day 2
            for day in ["2026-04-01", "2026-04-03"]:
                d = Path(tmp) / "data" / day
                d.mkdir(parents=True)
                (d / "digest.md").write_text(f"---\ndate: '{day}'\n---\n\nDigest for {day}")

            digests = gen._collect_daily_digests("2026-04-01", "2026-04-03")
            assert len(digests) == 2

    def test_empty_range(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            digests = gen._collect_daily_digests("2026-04-01", "2026-04-03")
            assert len(digests) == 0

    def test_strips_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            d = Path(tmp) / "data" / "2026-04-01"
            d.mkdir(parents=True)
            (d / "digest.md").write_text("---\ndate: '2026-04-01'\nmodel: test\n---\n\nActual content here")

            digests = gen._collect_daily_digests("2026-04-01", "2026-04-01")
            assert len(digests) == 1
            assert "Actual content here" in digests[0]
            assert "model: test" not in digests[0]

    def test_handles_nested_month_directories(self):
        """Test data/YYYY-MM/YYYY-MM-DD/ layout."""
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            d = Path(tmp) / "data" / "2026-03" / "2026-03-15"
            d.mkdir(parents=True)
            (d / "digest.md").write_text("---\ndate: '2026-03-15'\n---\n\nNested digest")

            digests = gen._collect_daily_digests("2026-03-15", "2026-03-15")
            assert len(digests) == 1
            assert "Nested digest" in digests[0]


class TestAutoGeneratePeriodic(unittest.TestCase):
    """Test auto-trigger logic based on date."""

    def _make_generator(self, tmp_dir):
        gen = DigestGenerator.__new__(DigestGenerator)
        gen.project_root = Path(tmp_dir)
        gen.client = None  # No actual LLM calls
        gen.model_name = "test"
        return gen

    @patch.object(DigestGenerator, "generate_periodic")
    def test_monday_triggers_weekly(self, mock_gen):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            gen.auto_generate_periodic("2026-04-06", force=True)  # Monday
            mock_gen.assert_called_once_with("weekly", end_date="2026-04-05", force=True)

    @patch.object(DigestGenerator, "generate_periodic")
    def test_tuesday_no_trigger(self, mock_gen):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            gen.auto_generate_periodic("2026-04-07", force=True)  # Tuesday
            mock_gen.assert_not_called()

    @patch.object(DigestGenerator, "generate_periodic")
    def test_first_of_month_triggers_monthly(self, mock_gen):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            gen.auto_generate_periodic("2026-04-01", force=True)  # 1st, not Monday
            mock_gen.assert_called_once_with("monthly", end_date="2026-03-31", force=True)

    @patch.object(DigestGenerator, "generate_periodic")
    def test_first_of_month_on_monday_triggers_both(self, mock_gen):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            # Find a date that is both Monday and 1st of month
            # 2026-06-01 is a Monday
            gen.auto_generate_periodic("2026-06-01", force=True)
            assert mock_gen.call_count == 2
            calls = [c.args[0] for c in mock_gen.call_args_list]
            assert "weekly" in calls
            assert "monthly" in calls

    @patch.object(DigestGenerator, "generate_periodic")
    def test_jan_first_triggers_all_three(self, mock_gen):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            # 2026-01-01 is Thursday: triggers monthly + yearly but not weekly
            gen.auto_generate_periodic("2026-01-01", force=True)
            calls = [c.args[0] for c in mock_gen.call_args_list]
            assert "monthly" in calls
            assert "yearly" in calls

    @patch.object(DigestGenerator, "generate_periodic")
    def test_jan_first_on_monday_triggers_all(self, mock_gen):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            # 2029-01-01 is Monday
            gen.auto_generate_periodic("2029-01-01", force=True)
            assert mock_gen.call_count == 3
            calls = [c.args[0] for c in mock_gen.call_args_list]
            assert "weekly" in calls
            assert "monthly" in calls
            assert "yearly" in calls


class TestGeneratePeriodic(unittest.TestCase):
    """Test periodic digest generation end-to-end (with mocked LLM)."""

    def _make_generator(self, tmp_dir):
        gen = DigestGenerator.__new__(DigestGenerator)
        gen.project_root = Path(tmp_dir)
        gen.model_name = "test-model"
        gen.client = MagicMock()
        return gen

    def _create_daily_digests(self, tmp_dir, dates):
        for date in dates:
            d = Path(tmp_dir) / "data" / date
            d.mkdir(parents=True)
            (d / "digest.md").write_text(f"---\ndate: '{date}'\n---\n\n## Summary for {date}\nSome content.")

    @patch("scraper.core.digest.OPENAI_AVAILABLE", True)
    def test_weekly_digest_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            dates = ["2026-03-30", "2026-03-31", "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05"]
            self._create_daily_digests(tmp, dates)

            # Mock LLM response
            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = "# Weekly Digest\n\nWeekly summary content."
            gen.client.chat.completions.create.return_value = mock_response

            result = gen.generate_periodic("weekly", end_date="2026-04-05", force=True)
            assert result is not None
            assert "digest-weekly.md" in result

            # Verify file was written
            weekly_path = Path(tmp) / "digest-weekly.md"
            assert weekly_path.exists()
            content = weekly_path.read_text()
            assert "period: weekly" in content
            assert "Weekly summary content" in content

    @patch("scraper.core.digest.OPENAI_AVAILABLE", True)
    def test_monthly_digest_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            # Create digests for a few days in March
            dates = ["2026-03-01", "2026-03-10", "2026-03-20", "2026-03-31"]
            self._create_daily_digests(tmp, dates)

            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = "# Monthly Digest\n\nMonthly summary."
            gen.client.chat.completions.create.return_value = mock_response

            result = gen.generate_periodic("monthly", end_date="2026-03-31", force=True)
            assert result is not None

            monthly_path = Path(tmp) / "digest-monthly.md"
            assert monthly_path.exists()
            content = monthly_path.read_text()
            assert "period: monthly" in content
            assert "source_count: 4" in content

    @patch("scraper.core.digest.OPENAI_AVAILABLE", True)
    def test_no_digests_returns_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            result = gen.generate_periodic("weekly", end_date="2026-04-05", force=True)
            assert result is None

    @patch("scraper.core.digest.OPENAI_AVAILABLE", True)
    def test_skip_existing_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            # Create existing weekly digest
            (Path(tmp) / "digest-weekly.md").write_text("existing")

            result = gen.generate_periodic("weekly", end_date="2026-04-05", force=False)
            assert result is not None
            # LLM should NOT have been called
            gen.client.chat.completions.create.assert_not_called()

    def test_unknown_period_returns_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            result = gen.generate_periodic("biweekly", end_date="2026-04-05")
            assert result is None

    @patch("scraper.core.digest.OPENAI_AVAILABLE", True)
    def test_correct_prompt_used_per_period(self):
        """Verify the right system prompt is used for each period."""
        from scraper.core.digest import MONTHLY_DIGEST_PROMPT, WEEKLY_DIGEST_PROMPT, YEARLY_DIGEST_PROMPT

        with tempfile.TemporaryDirectory() as tmp:
            gen = self._make_generator(tmp)
            dates = [f"2026-03-{d:02d}" for d in range(1, 8)]
            self._create_daily_digests(tmp, dates)

            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = "Content"
            gen.client.chat.completions.create.return_value = mock_response

            gen.generate_periodic("weekly", end_date="2026-03-07", force=True)
            call_args = gen.client.chat.completions.create.call_args
            system_msg = call_args.kwargs["messages"][0]["content"]
            assert system_msg == WEEKLY_DIGEST_PROMPT

            # Reset and test monthly
            gen.client.chat.completions.create.reset_mock()
            gen.client.chat.completions.create.return_value = mock_response
            gen.generate_periodic("monthly", end_date="2026-03-31", force=True)
            call_args = gen.client.chat.completions.create.call_args
            system_msg = call_args.kwargs["messages"][0]["content"]
            assert system_msg == MONTHLY_DIGEST_PROMPT


if __name__ == "__main__":
    unittest.main()
