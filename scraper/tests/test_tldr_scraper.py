"""
Tests for the TLDRScraper class.
"""

import json
import os
import shutil
import tempfile
import unittest
from unittest.mock import patch

from scraper.scrapers.tldr import TLDRScraper

SAMPLE_HTML = """
<html>
<body>
<article>
    <a href="https://example.com/article1?utm_source=tldrnewsletter&utm_medium=email">AI Breakthrough in 2026</a>
    <p>Researchers have made a significant breakthrough in AI reasoning.</p>
</article>
<article>
    <a href="https://techblog.com/post/42">New Rust Features Released</a>
    <p>Rust 2026 edition brings exciting new features to the language.</p>
</article>
<article>
    <a href="https://tldr.tech/internal-page">TLDR Internal Link</a>
    <p>This should be filtered out.</p>
</article>
<nav>
    <a href="https://navsite.com">Nav Link</a>
</nav>
</body>
</html>
"""

SAMPLE_NEXT_DATA = json.dumps(
    {
        "props": {
            "pageProps": {
                "articles": [
                    {
                        "title": "GPT-5 Released",
                        "url": "https://openai.com/gpt5?utm_source=tldrnewsletter",
                        "description": "OpenAI releases GPT-5 with improved reasoning.",
                        "category": "AI",
                    },
                    {
                        "title": "Kubernetes 2.0",
                        "url": "https://kubernetes.io/blog/k8s-2",
                        "description": "Major Kubernetes release.",
                        "category": "DevOps",
                    },
                    {
                        "title": "Internal Page",
                        "url": "https://tldr.tech/some-page",
                        "description": "Should be filtered.",
                    },
                ]
            }
        }
    }
)

SAMPLE_HTML_WITH_NEXT_DATA = f"""
<html>
<head>
<script id="__NEXT_DATA__" type="application/json">{SAMPLE_NEXT_DATA}</script>
</head>
<body></body>
</html>
"""


class TestTLDRScraper(unittest.TestCase):
    """Test cases for TLDRScraper."""

    def setUp(self):
        self.test_output_dir = tempfile.mkdtemp()
        self.scraper = TLDRScraper(test_mode=True, test_output_dir=self.test_output_dir)

    def tearDown(self):
        shutil.rmtree(self.test_output_dir, ignore_errors=True)

    def test_strip_utm_params(self):
        """Test UTM parameter removal."""
        url = "https://example.com/page?utm_source=tldr&utm_medium=email&ref=123"
        result = TLDRScraper._strip_utm_params(url)
        self.assertNotIn("utm_source", result)
        self.assertNotIn("utm_medium", result)
        self.assertIn("ref=123", result)

    def test_strip_utm_params_no_params(self):
        """Test URL without any params stays clean."""
        url = "https://example.com/page"
        result = TLDRScraper._strip_utm_params(url)
        self.assertEqual(result, url)

    def test_is_external_url(self):
        """Test external URL detection."""
        self.assertTrue(self.scraper._is_external_url("https://example.com"))
        self.assertTrue(self.scraper._is_external_url("https://techcrunch.com/article"))
        self.assertFalse(self.scraper._is_external_url("https://tldr.tech/something"))
        self.assertFalse(self.scraper._is_external_url(""))
        self.assertFalse(self.scraper._is_external_url("/relative/path"))

    def test_extract_from_next_data(self):
        """Test extracting articles from __NEXT_DATA__."""
        articles = self.scraper._extract_from_next_data(SAMPLE_HTML_WITH_NEXT_DATA)

        # Should get 2 articles (tldr.tech internal link filtered)
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0]["title"], "GPT-5 Released")
        # UTM params should be stripped
        self.assertNotIn("utm_source", articles[0]["url"])
        self.assertEqual(articles[0]["url"], "https://openai.com/gpt5")
        self.assertEqual(articles[1]["title"], "Kubernetes 2.0")

    def test_extract_from_html(self):
        """Test extracting articles from HTML selectors."""
        articles = self.scraper._extract_from_html(SAMPLE_HTML)

        # Should get 2 external articles (internal tldr.tech and nav links filtered)
        self.assertEqual(len(articles), 2)
        titles = [a["title"] for a in articles]
        self.assertIn("AI Breakthrough in 2026", titles)
        self.assertIn("New Rust Features Released", titles)

        # Check UTM params stripped
        for article in articles:
            self.assertNotIn("utm_source", article["url"])

    def test_extract_from_html_empty(self):
        """Test extraction from empty HTML."""
        articles = self.scraper._extract_from_html("<html><body></body></html>")
        self.assertEqual(articles, [])

    def test_extract_data_returns_empty(self):
        """Test that _extract_data returns empty (placeholder)."""
        self.assertEqual(self.scraper._extract_data([]), [])

    @patch.object(TLDRScraper, "_get_page")
    def test_scrape_with_next_data(self, mock_get_page):
        """Test full scrape using __NEXT_DATA__."""
        mock_get_page.return_value = SAMPLE_HTML_WITH_NEXT_DATA

        result = self.scraper.scrape(output_format="json")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["site_name"], "tldr")

    @patch.object(TLDRScraper, "_get_page")
    def test_scrape_fallback_to_html(self, mock_get_page):
        """Test scrape falls back to HTML when no __NEXT_DATA__."""
        mock_get_page.return_value = SAMPLE_HTML

        result = self.scraper.scrape(output_format="json")

        self.assertEqual(len(result), 2)

    @patch.object(TLDRScraper, "_get_page")
    def test_scrape_empty_page(self, mock_get_page):
        """Test scraping an empty page."""
        mock_get_page.return_value = "<html><body></body></html>"

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(result, [])

    @patch.object(TLDRScraper, "_get_page")
    def test_scrape_fetch_failure(self, mock_get_page):
        """Test scraping when page fetch fails."""
        mock_get_page.return_value = None

        result = self.scraper.scrape(output_format="json")
        self.assertEqual(result, [])

    @patch.object(TLDRScraper, "_get_page")
    def test_scrape_deduplicates(self, mock_get_page):
        """Test that duplicate URLs are removed."""
        html = """
        <html><body>
        <article><a href="https://example.com/same">Title A</a><p>Desc A</p></article>
        <article><a href="https://example.com/same">Title B</a><p>Desc B</p></article>
        <article><a href="https://other.com/diff">Title C</a><p>Desc C</p></article>
        </body></html>
        """
        mock_get_page.return_value = html

        result = self.scraper.scrape(output_format="json")
        urls = [a["url"] for a in result]
        self.assertEqual(len(set(urls)), len(urls))


if __name__ == "__main__":
    unittest.main()
