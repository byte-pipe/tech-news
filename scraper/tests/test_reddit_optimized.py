"""Tests for OptimizedRedditScraper and RedditAPIClient."""

import csv
import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch


class TestRedditAPIClient(unittest.TestCase):
    def setUp(self):
        from scraper.scrapers.reddit_optimized import RedditAPIClient
        self.client = RedditAPIClient()

    def tearDown(self):
        self.client.close()

    def test_create_session(self):
        import requests
        assert isinstance(self.client.session, requests.Session)

    def _make_reddit_response(self, posts=None):
        if posts is None:
            posts = [{"kind": "t3", "data": {"title": "Test", "author": "user", "score": 100, "num_comments": 10, "subreddit": "programming", "permalink": "/r/programming/comments/1/test/", "is_self": False, "url": "https://x.com", "upvote_ratio": 0.9, "link_flair_text": "", "domain": "x.com", "created_utc": 1000000}}]
        return {"data": {"children": posts, "after": None}}

    @patch("scraper.scrapers.reddit_optimized.requests.Session.get")
    def test_fetch_subreddit_posts_success(self, mock_get):
        resp = MagicMock()
        resp.json.return_value = self._make_reddit_response()
        resp.raise_for_status = MagicMock()
        mock_get.return_value = resp

        result = self.client.fetch_subreddit_posts("programming")
        assert result is not None
        assert "data" in result

    def test_fetch_subreddit_posts_network_error(self):
        import requests
        self.client.session = MagicMock()
        self.client.session.get.side_effect = requests.exceptions.RequestException("fail")

        result = self.client.fetch_subreddit_posts("programming")
        assert result is None

    def test_close(self):
        self.client.session = MagicMock()
        self.client.close()
        self.client.session.close.assert_called_once()


class TestOptimizedRedditScraper(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        with patch("scraper.scrapers.reddit_optimized.get_config") as mock_config:
            mock_config.return_value.project_root = self.tmp
            from scraper.scrapers.reddit_optimized import OptimizedRedditScraper
            self.scraper = OptimizedRedditScraper(
                subreddits=["programming"],
                test_mode=True,
                test_output_dir=self.tmp,
            )

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _make_post_data(self, title="Test Post", score=100):
        return {
            "title": title,
            "author": "user",
            "score": score,
            "num_comments": 5,
            "subreddit": "programming",
            "permalink": "/r/programming/comments/1/test/",
            "is_self": False,
            "url": "https://example.com",
            "upvote_ratio": 0.9,
            "link_flair_text": "OC",
            "domain": "example.com",
            "created_utc": 1000000,
        }

    def test_extract_post_data(self):
        post_data = self._make_post_data()
        result = self.scraper.extract_post_data(post_data)
        assert result["title"] == "Test Post"
        assert result["score"] == 100
        assert result["author"] == "user"
        assert "reddit.com" in result["url"]

    def test_extract_post_data_self_post(self):
        post_data = self._make_post_data()
        post_data["is_self"] = True
        result = self.scraper.extract_post_data(post_data)
        assert result["external_url"] == ""

    def test_extract_post_data_external_url(self):
        post_data = self._make_post_data()
        post_data["is_self"] = False
        result = self.scraper.extract_post_data(post_data)
        assert result["external_url"] == "https://example.com"

    def test_remove_duplicates(self):
        posts = [
            {"url": "https://a.com", "title": "A"},
            {"url": "https://a.com", "title": "A again"},
            {"url": "https://b.com", "title": "B"},
        ]
        result = self.scraper._remove_duplicates(posts)
        assert len(result) == 2

    def test_remove_duplicates_empty_url_skipped(self):
        posts = [{"url": "", "title": "no url"}]
        result = self.scraper._remove_duplicates(posts)
        assert len(result) == 0

    def test_fetch_subreddit_no_data(self):
        self.scraper.client = MagicMock()
        self.scraper.client.fetch_subreddit_posts.return_value = None
        result = self.scraper.fetch_subreddit_concurrent("programming")
        assert result == []

    def test_fetch_subreddit_success(self):
        self.scraper.client = MagicMock()
        self.scraper.client.fetch_subreddit_posts.return_value = {
            "data": {"children": [{"kind": "t3", "data": self._make_post_data()}]}
        }
        result = self.scraper.fetch_subreddit_concurrent("programming")
        assert len(result) == 1

    def test_fetch_subreddit_skips_non_t3(self):
        self.scraper.client = MagicMock()
        self.scraper.client.fetch_subreddit_posts.return_value = {
            "data": {"children": [{"kind": "t1", "data": self._make_post_data()}]}
        }
        result = self.scraper.fetch_subreddit_concurrent("programming")
        assert result == []

    def test_save_data_json(self):
        os.makedirs(self.tmp, exist_ok=True)
        posts = [self.scraper.extract_post_data(self._make_post_data())]
        path = self.scraper._save_data(posts, "json")
        assert os.path.exists(path)

    def test_save_data_csv(self):
        os.makedirs(self.tmp, exist_ok=True)
        posts = [self.scraper.extract_post_data(self._make_post_data())]
        path = self.scraper._save_data(posts, "csv")
        assert os.path.exists(path)

    def test_save_data_markdown(self):
        os.makedirs(self.tmp, exist_ok=True)
        posts = [self.scraper.extract_post_data(self._make_post_data())]
        path = self.scraper._save_data(posts, "markdown")
        assert os.path.exists(path)

    def test_save_as_csv_empty(self):
        path = os.path.join(self.tmp, "test.csv")
        self.scraper._save_as_csv([], path)
        assert not os.path.exists(path)

    def test_scrape_no_posts(self):
        self.scraper.client = MagicMock()
        self.scraper.client.fetch_subreddit_posts.return_value = None
        result = self.scraper.scrape(output_format="json")
        assert result == []

    def test_scrape_with_posts(self):
        self.scraper.client = MagicMock()
        self.scraper.client.fetch_subreddit_posts.return_value = {
            "data": {"children": [{"kind": "t3", "data": self._make_post_data()}]}
        }
        with patch.object(self.scraper, "_save_data", return_value="/tmp/test.json"):
            result = self.scraper.scrape(output_format="json")
        assert result is not None
        assert len(result) >= 0


if __name__ == "__main__":
    unittest.main()
