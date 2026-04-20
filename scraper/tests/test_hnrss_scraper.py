"""
Tests for the HNRSSScraper class.
"""

import shutil
import tempfile
import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

from scraper.scrapers.hnrss import HNRSSScraper


class TestHNRSSScraper(unittest.TestCase):
    """Test cases for HNRSSScraper."""

    def setUp(self):
        self.test_output_dir = tempfile.mkdtemp()
        self.scraper = HNRSSScraper(test_mode=True, test_output_dir=self.test_output_dir)

    def tearDown(self):
        shutil.rmtree(self.test_output_dir, ignore_errors=True)

    def _make_entry(self, title="Test Story", link="https://example.com/article", comments="https://news.ycombinator.com/item?id=12345", description="<p>Points: 139</p><p># Comments: 63</p>", published_parsed=(2026, 2, 8, 12, 0, 0, 5, 39, 0)):  # noqa: E501
        """Create a mock feedparser entry."""
        entry = MagicMock()
        entry.title = title
        entry.link = link
        entry.comments = comments
        entry.description = description
        entry.summary = description
        entry.published_parsed = published_parsed
        return entry

    def test_normalize_entry_basic(self):
        """Test basic entry normalization."""
        entry = self._make_entry()
        result = self.scraper._normalize_entry(entry)

        self.assertIsNotNone(result)
        self.assertEqual(result["title"], "Test Story")
        self.assertEqual(result["url"], "https://example.com/article")
        self.assertEqual(result["score"], 139)
        self.assertEqual(result["comments"], 63)
        self.assertEqual(result["discussion_url"], "https://news.ycombinator.com/item?id=12345")
        self.assertEqual(result["site_name"], "hnrss")
        self.assertIn("hackernews", result["tags"])
        self.assertIn("hnrss", result["tags"])

    def test_normalize_entry_no_title(self):
        """Test that entries without titles are skipped."""
        entry = self._make_entry(title="")
        result = self.scraper._normalize_entry(entry)
        self.assertIsNone(result)

    def test_normalize_entry_no_link(self):
        """Test that entries without links are skipped."""
        entry = self._make_entry(link="")
        result = self.scraper._normalize_entry(entry)
        self.assertIsNone(result)

    def test_parse_points_comments(self):
        """Test extracting points and comments from description HTML."""
        html = "<p>Points: 256</p><p># Comments: 102</p>"
        points, comments = self.scraper._parse_points_comments(html)
        self.assertEqual(points, 256)
        self.assertEqual(comments, 102)

    def test_parse_points_comments_missing(self):
        """Test parsing when points/comments info is missing."""
        points, comments = self.scraper._parse_points_comments("")
        self.assertEqual(points, 0)
        self.assertEqual(comments, 0)

    def test_parse_points_comments_partial(self):
        """Test parsing when only points are present."""
        html = "<p>Points: 50</p>"
        points, comments = self.scraper._parse_points_comments(html)
        self.assertEqual(points, 50)
        self.assertEqual(comments, 0)

    def test_normalize_entry_no_published_parsed(self):
        """Test entry without published_parsed uses today's date."""
        entry = self._make_entry()
        entry.published_parsed = None
        result = self.scraper._normalize_entry(entry)
        self.assertIsNotNone(result)
        self.assertEqual(result["date"], datetime.now().strftime("%Y-%m-%d"))

    def test_extract_data_returns_empty(self):
        """Test that _extract_data returns empty (placeholder)."""
        self.assertEqual(self.scraper._extract_data([]), [])

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_success(self, mock_parse):
        """Test successful scraping with mock feed."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = [
            self._make_entry(title="Story A", link="https://a.com", description="<p>Points: 200</p><p># Comments: 50</p>"),
            self._make_entry(title="Story B", link="https://b.com", description="<p>Points: 150</p><p># Comments: 30</p>"),
        ]
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")

        self.assertEqual(len(result), 2)
        # Should be sorted by score descending
        self.assertEqual(result[0]["title"], "Story A")
        self.assertEqual(result[0]["score"], 200)
        self.assertEqual(result[1]["title"], "Story B")
        self.assertEqual(result[1]["score"], 150)

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_empty_feed(self, mock_parse):
        """Test scraping with empty feed."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = []
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(result, [])

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_bozo_feed_no_entries(self, mock_parse):
        """Test scraping with a malformed feed and no entries."""
        mock_feed = MagicMock()
        mock_feed.bozo = True
        mock_feed.entries = []
        mock_feed.bozo_exception = "XML parsing error"
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(result, [])

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_bozo_feed_with_entries(self, mock_parse):
        """Test that bozo feeds with entries still work."""
        mock_feed = MagicMock()
        mock_feed.bozo = True
        mock_feed.entries = [self._make_entry()]
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(len(result), 1)

    def test_normalize_entry_bad_published_parsed_falls_back(self):
        """Test that invalid published_parsed tuple falls back to today."""
        entry = self._make_entry()
        entry.published_parsed = (9999, 13, 40, 99, 99, 99, 0, 0, 0)  # invalid date
        result = self.scraper._normalize_entry(entry)
        self.assertIsNotNone(result)
        # Should fall back to today's date
        today = datetime.now().strftime("%Y-%m-%d")
        self.assertEqual(result["date"], today)

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_all_entries_normalize_to_none(self, mock_parse):
        """Test when all entries fail normalization."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        entry = self._make_entry(title="", link="")  # both empty → normalize returns None
        mock_feed.entries = [entry]
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(result, [])

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_csv_format(self, mock_parse):
        """Test scraping with csv output format."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = [self._make_entry()]
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="csv")
        self.assertEqual(len(result), 1)

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_markdown_format(self, mock_parse):
        """Test scraping with markdown output format."""
        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = [self._make_entry()]
        mock_parse.return_value = mock_feed

        result = self.scraper.scrape(output_format="markdown")
        self.assertEqual(len(result), 1)

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_exception_returns_none(self, mock_parse):
        """Test that scrape exception returns None."""
        mock_parse.side_effect = RuntimeError("network error")

        result = self.scraper.scrape(output_format="json")
        self.assertIsNone(result)

    @patch("scraper.scrapers.hnrss.feedparser.parse")
    def test_scrape_non_test_mode_uses_project_root(self, mock_parse):
        """Test scraping in non-test mode uses project root path (line 147)."""
        import tempfile
        tmp = tempfile.mkdtemp()
        from scraper.scrapers.hnrss import HNRSSScraper
        # Instantiate without test_mode
        scraper = HNRSSScraper(test_mode=False)
        scraper.project_root = tmp  # Override to avoid creating files in real project

        mock_feed = MagicMock()
        mock_feed.bozo = False
        mock_feed.entries = [self._make_entry()]
        mock_parse.return_value = mock_feed

        result = scraper.scrape(output_format="json")
        self.assertIsNotNone(result)

        import shutil
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
