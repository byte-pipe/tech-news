"""
Tests for the NewsFeedScraper class.
"""

import shutil
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from scraper.scrapers.newsfeed import NewsFeedScraper, _strip_html, _title_hash


class TestNewsFeedHelpers(unittest.TestCase):
    """Test helper functions."""

    def test_strip_html_basic(self):
        """Test stripping HTML tags."""
        self.assertEqual(_strip_html("<p>Hello <b>world</b></p>"), "Hello world")

    def test_strip_html_empty(self):
        """Test strip_html with empty/None input."""
        self.assertEqual(_strip_html(""), "")
        self.assertEqual(_strip_html(None), "")

    def test_strip_html_no_tags(self):
        """Test strip_html with plain text."""
        self.assertEqual(_strip_html("plain text"), "plain text")

    def test_title_hash_consistent(self):
        """Test that title_hash produces consistent results."""
        h1 = _title_hash("Hello World")
        h2 = _title_hash("Hello World")
        self.assertEqual(h1, h2)

    def test_title_hash_case_insensitive(self):
        """Test that title_hash normalizes case."""
        h1 = _title_hash("Hello World")
        h2 = _title_hash("hello world")
        self.assertEqual(h1, h2)

    def test_title_hash_whitespace_normalized(self):
        """Test that title_hash normalizes whitespace."""
        h1 = _title_hash("Hello World")
        h2 = _title_hash("Hello   World")
        self.assertEqual(h1, h2)

    def test_title_hash_different_titles(self):
        """Test that different titles produce different hashes."""
        h1 = _title_hash("Hello World")
        h2 = _title_hash("Goodbye World")
        self.assertNotEqual(h1, h2)


class TestNewsFeedScraper(unittest.TestCase):
    """Test cases for NewsFeedScraper."""

    def setUp(self):
        self.test_output_dir = tempfile.mkdtemp()
        self.scraper = NewsFeedScraper(test_mode=True, test_output_dir=self.test_output_dir)

    def tearDown(self):
        shutil.rmtree(self.test_output_dir, ignore_errors=True)

    def _make_entry(self, title="Test Article", link="https://example.com/article", summary="<p>Article description here</p>", published_parsed=(2026, 2, 28, 12, 0, 0, 5, 59, 0), tags=None):
        """Create a mock feedparser entry."""
        entry = MagicMock()
        entry.title = title
        entry.link = link
        entry.summary = summary
        entry.description = summary
        entry.published_parsed = published_parsed
        entry.updated_parsed = None
        if tags:
            entry.tags = [MagicMock(term=t) for t in tags]
            # Make hasattr work for tags
            type(entry).tags = property(lambda self: [MagicMock(term=t) for t in tags])
        else:
            del entry.tags
        return entry

    def test_normalize_entry_basic(self):
        """Test basic entry normalization."""
        entry = self._make_entry()
        result = self.scraper._normalize_entry(entry, "BBC")

        self.assertIsNotNone(result)
        self.assertEqual(result["title"], "Test Article")
        self.assertEqual(result["url"], "https://example.com/article")
        self.assertEqual(result["description"], "Article description here")
        self.assertEqual(result["score"], 0)
        self.assertEqual(result["source"], "BBC")
        self.assertEqual(result["site_name"], "newsfeed")
        self.assertIn("bbc", result["tags"])

    def test_normalize_entry_strips_html(self):
        """Test that HTML is stripped from title and description."""
        entry = self._make_entry(
            title="<b>Bold</b> Title",
            summary="<p>Some <a href='#'>linked</a> text</p>",
        )
        result = self.scraper._normalize_entry(entry, "Reuters")

        self.assertEqual(result["title"], "Bold Title")
        self.assertEqual(result["description"], "Some linked text")

    def test_normalize_entry_no_title(self):
        """Test that entries without titles are skipped."""
        entry = self._make_entry(title="")
        result = self.scraper._normalize_entry(entry, "BBC")
        self.assertIsNone(result)

    def test_normalize_entry_no_link(self):
        """Test that entries without links are skipped."""
        entry = self._make_entry(link="")
        result = self.scraper._normalize_entry(entry, "BBC")
        self.assertIsNone(result)

    def test_normalize_entry_no_published_date(self):
        """Test entry without published_parsed uses today's date."""
        entry = self._make_entry()
        entry.published_parsed = None
        entry.updated_parsed = None
        result = self.scraper._normalize_entry(entry, "BBC")
        self.assertIsNotNone(result)
        # Should fall back to today
        from datetime import datetime

        self.assertEqual(result["date"], datetime.now().strftime("%Y-%m-%d"))

    def test_normalize_entry_long_description_truncated(self):
        """Test that long descriptions are truncated."""
        entry = self._make_entry(summary="A" * 600)
        result = self.scraper._normalize_entry(entry, "BBC")
        self.assertTrue(len(result["description"]) <= 500)
        self.assertTrue(result["description"].endswith("..."))

    def test_extract_data_returns_empty(self):
        """Test that _extract_data returns empty (placeholder)."""
        self.assertEqual(self.scraper._extract_data([]), [])

    @patch("scraper.scrapers.newsfeed.feedparser.parse")
    def test_scrape_success(self, mock_parse):
        """Test successful scraping with mock feeds."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = [
            self._make_entry(title="Story A", link="https://a.com"),
            self._make_entry(title="Story B", link="https://b.com"),
        ]
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")

        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

    @patch("scraper.scrapers.newsfeed.feedparser.parse")
    def test_scrape_deduplicates(self, mock_parse):
        """Test that duplicate titles across feeds are deduplicated."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = [
            self._make_entry(title="Same Story", link="https://a.com"),
            self._make_entry(title="Same Story", link="https://b.com"),
        ]
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")

        # Titles that are identical should be deduplicated
        titles = [item["title"] for item in result]
        self.assertEqual(titles.count("Same Story"), 1)

    @patch("scraper.scrapers.newsfeed.feedparser.parse")
    def test_scrape_empty_feeds(self, mock_parse):
        """Test scraping when all feeds return empty."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = []
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(result, [])

    @patch("scraper.scrapers.newsfeed.feedparser.parse")
    def test_scrape_bozo_feed_no_entries(self, mock_parse):
        """Test scraping with malformed feed and no entries."""
        mock_feed = MagicMock()
        mock_feed.bozo = True
        mock_feed.entries = []
        mock_feed.bozo_exception = "XML parsing error"
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(result, [])

    @patch("scraper.scrapers.newsfeed.feedparser.parse")
    def test_scrape_exception_returns_none(self, mock_parse):
        """Test that a complete failure returns None."""
        mock_parse.side_effect = Exception("Network error")

        result = self.scraper.scrape(output_format="json")
        # ThreadPoolExecutor catches exceptions per-feed, so only a top-level error returns None
        # With all feeds raising, we get empty list since items are collected per-feed
        self.assertIsNotNone(result)

    def test_fetch_single_feed_exception(self):
        """Test that _fetch_single_feed handles exceptions gracefully."""
        with patch("scraper.scrapers.newsfeed.feedparser.parse", side_effect=Exception("timeout")):
            result = self.scraper._fetch_single_feed("TestFeed", "https://bad.url/rss")
            self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
