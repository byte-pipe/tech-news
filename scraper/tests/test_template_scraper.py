"""Tests for TemplateScraper."""

import unittest
from unittest.mock import patch

from bs4 import BeautifulSoup


class TestTemplateScraper(unittest.TestCase):
    def setUp(self):
        from scraper.scrapers.template_scraper import TemplateScraper
        self.scraper = TemplateScraper(test_mode=True, test_output_dir="/tmp")

    def _make_item(self, title="Test Title", url="/test", description="Test desc"):
        html = f"""
        <div class="item">
            <h2><a href="{url}">{title}</a></h2>
            <p class="description">{description}</p>
        </div>
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.find("div", class_="item")

    def test_extract_data_basic(self):
        item = self._make_item(title="Hello World", url="/hello")
        result = self.scraper._extract_data([item])
        assert len(result) == 1
        assert result[0]["title"] == "Hello World"

    def test_extract_data_relative_url_made_absolute(self):
        item = self._make_item(url="/relative/path")
        result = self.scraper._extract_data([item])
        assert result[0]["url"].startswith("https://example.com")

    def test_extract_data_absolute_url_unchanged(self):
        item = self._make_item(url="https://other.com/page")
        result = self.scraper._extract_data([item])
        assert result[0]["url"] == "https://other.com/page"

    def test_extract_data_no_title_skipped(self):
        html = '<div class="item"><p>no title</p></div>'
        soup = BeautifulSoup(html, "html.parser")
        item = soup.find("div")
        result = self.scraper._extract_data([item])
        assert result == []

    def test_extract_data_empty_list(self):
        assert self.scraper._extract_data([]) == []

    def test_extract_data_multiple_items(self):
        items = [
            self._make_item(title="A", url="/a"),
            self._make_item(title="B", url="/b"),
        ]
        result = self.scraper._extract_data(items)
        assert len(result) == 2

    def test_scrape_json_api_no_data(self):
        with patch("scraper.scrapers.template_scraper.fetch_json_with_retry", return_value=None):
            self.scraper.scrape()  # Should not raise

    def test_scrape_json_api_empty_items(self):
        with patch("scraper.scrapers.template_scraper.fetch_json_with_retry", return_value={"data": {"items": []}}):
            self.scraper.scrape()  # Should not raise

    def test_scrape_json_api_with_items(self):
        data = {"data": {"items": [
            {"title": "Article 1", "description": "desc", "url": "https://x.com/1"},
            {"title": "Article 2", "description": "desc2", "url": "https://x.com/2"},
        ]}}
        with patch("scraper.scrapers.template_scraper.fetch_json_with_retry", return_value=data):
            with patch.object(self.scraper, "_save_data"):
                self.scraper.scrape()  # Should not raise

    def test_scrape_exception_handled(self):
        with patch("scraper.scrapers.template_scraper.fetch_json_with_retry", side_effect=Exception("network error")):
            self.scraper.scrape()  # Should not raise

    def test_normalize_whitespace_in_module(self):
        from scraper.scrapers.template_scraper import normalize_whitespace
        assert normalize_whitespace("  hello   world  ") == "hello world"
        assert normalize_whitespace("") == ""
        assert normalize_whitespace(None) == ""


if __name__ == "__main__":
    unittest.main()
