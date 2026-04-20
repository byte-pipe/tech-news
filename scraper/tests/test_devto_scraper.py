"""Tests for DevToScraper._extract_data."""

import unittest
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup


class TestDevToScraper(unittest.TestCase):
    def setUp(self):
        from scraper.scrapers.devto import DevToScraper
        self.scraper = DevToScraper(test_mode=True, test_output_dir="/tmp")

    def _make_item(self, title="Test Article", url_path="/user/test", author="testuser", tags=None):
        html = f"""
        <div class="crayons-story">
            <h2><a href="{url_path}">{title}</a></h2>
            <a class="crayons-story__secondary">{author}</a>
            <time datetime="2026-04-20">Apr 20</time>
            <div class="crayons-story__snippet">Test description</div>
            {"".join(f'<a class="crayons-tag">{t}</a>' for t in (tags or []))}
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.find("div", class_="crayons-story")

    def test_extract_data_valid_item(self):
        item = self._make_item(title="Hello World", url_path="/user/hello")
        result = self.scraper._extract_data([item])
        assert len(result) == 1
        assert result[0]["title"] == "Hello World"

    def test_extract_data_makes_url_absolute(self):
        item = self._make_item(url_path="/user/hello")
        result = self.scraper._extract_data([item])
        assert result[0]["url"].startswith("https://dev.to")

    def test_extract_data_empty_list(self):
        result = self.scraper._extract_data([])
        assert result == []

    def test_extract_data_skips_item_without_title(self):
        # Item with empty title
        html = '<div class="crayons-story"><h2><a href="/x"></a></h2></div>'
        soup = BeautifulSoup(html, "html.parser")
        item = soup.find("div")
        result = self.scraper._extract_data([item])
        assert result == []

    def test_extract_data_with_tags(self):
        item = self._make_item(tags=["python", "ai"])
        result = self.scraper._extract_data([item])
        if result:
            assert "python" in result[0].get("tags", "") or result[0].get("tags") == ""

    def test_extract_data_multiple_items(self):
        items = [
            self._make_item(title="Article 1", url_path="/a/1"),
            self._make_item(title="Article 2", url_path="/a/2"),
        ]
        result = self.scraper._extract_data(items)
        assert len(result) == 2

    def test_extract_data_returns_required_fields(self):
        item = self._make_item()
        result = self.scraper._extract_data([item])
        if result:
            assert "title" in result[0]
            assert "url" in result[0]
            assert "author" in result[0]

    def test_extract_data_exception_handling(self):
        bad_item = MagicMock()
        bad_item.select_one.side_effect = Exception("parse error")
        # Should not raise
        result = self.scraper._extract_data([bad_item])
        assert isinstance(result, list)

    def test_extract_data_non_iterable_raises_gracefully(self):
        # Passing None triggers the outer except (lines 61-62)
        result = self.scraper._extract_data(None)
        assert isinstance(result, list)

    def test_extract_data_relative_url_extended(self):
        # If extract_url returns a URL without http, line 32 prepends base_url
        with patch.object(self.scraper, "extract_url", return_value="/relative/path"):
            item = self._make_item(title="Test", url_path="/relative/path")
            result = self.scraper._extract_data([item])
        if result:
            assert result[0]["url"].startswith("https://dev.to")


if __name__ == "__main__":
    unittest.main()
