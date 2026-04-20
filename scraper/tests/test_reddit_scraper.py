"""Tests for RedditScraper (reddit.py wrapper)."""

import unittest
from unittest.mock import MagicMock, patch


class TestRedditScraper(unittest.TestCase):
    def setUp(self):
        with patch("scraper.scrapers.reddit_optimized.get_config") as mock_cfg:
            mock_cfg.return_value.project_root = "/tmp"
            from scraper.scrapers.reddit import RedditScraper
            self.scraper = RedditScraper(test_mode=True, test_output_dir="/tmp")

    def test_init_sets_site_name(self):
        assert self.scraper.site_name == "reddit"

    def test_init_creates_optimized_scraper(self):
        from scraper.scrapers.reddit_optimized import OptimizedRedditScraper
        assert isinstance(self.scraper._scraper, OptimizedRedditScraper)

    def test_scrape_delegates_to_optimized(self):
        self.scraper._scraper.scrape = MagicMock(return_value=[{"title": "X"}])
        result = self.scraper.scrape(output_format="json")
        assert result == [{"title": "X"}]
        self.scraper._scraper.scrape.assert_called_once_with(output_format="json")

    def test_extract_data_empty(self):
        result = self.scraper._extract_data([])
        assert result == []

    def test_extract_data_with_full_json_structure(self):
        post = {"kind": "t3", "data": {"title": "Test Post", "author": "user1", "score": 500, "num_comments": 20, "subreddit": "programming", "permalink": "/r/programming/comments/1/test/"}}
        items = [{"data": {"children": [post]}}]
        result = self.scraper._extract_data(items)
        assert len(result) == 1
        assert result[0]["title"] == "Test Post"
        assert "reddit.com" in result[0]["url"]

    def test_extract_data_flat_posts(self):
        post = {"data": {"title": "Article", "author": "alice", "score": 100, "num_comments": 5, "subreddit": "tech", "permalink": "/r/tech/comments/2/art/"}}
        result = self.scraper._extract_data([post])
        assert len(result) == 1
        assert result[0]["title"] == "Article"

    def test_extract_data_skips_non_dict(self):
        result = self.scraper._extract_data(["not_a_dict"])
        assert result == []

    def test_remove_duplicates_delegates(self):
        posts = [{"url": "https://a.com"}, {"url": "https://a.com"}, {"url": "https://b.com"}]
        result = self.scraper._remove_duplicates(posts)
        assert len(result) == 2


if __name__ == "__main__":
    unittest.main()
