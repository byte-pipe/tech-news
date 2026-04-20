"""Tests for HackerNewsAPIScraper."""

import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch


class TestHackerNewsAPIScraper(unittest.TestCase):
    def setUp(self):
        with patch("scraper.scrapers.hackernews_api.requests.Session"):
            from scraper.scrapers.hackernews_api import HackerNewsAPIScraper
            self.scraper = HackerNewsAPIScraper(test_mode=True, test_output_dir="/tmp")

    def test_extract_data_returns_empty(self):
        result = self.scraper._extract_data([])
        assert result == []

    def test_normalize_story_data_basic(self):
        story = {
            "title": "Test Story",
            "url": "https://example.com",
            "by": "testuser",
            "score": 150,
            "descendants": 42,
            "id": 12345,
            "time": 1000000,
        }
        result = self.scraper._normalize_story_data(story)
        assert result["title"] == "Test Story"
        assert result["url"] == "https://example.com"
        assert result["author"] == "testuser"
        assert result["score"] == 150
        assert result["comments"] == 42
        assert result["id"] == 12345
        assert "discussion_url" in result
        assert "hackernews" in result["tags"]

    def test_normalize_story_data_no_time(self):
        story = {"title": "No time story", "url": "https://x.com", "score": 10, "id": 1, "time": 0}
        result = self.scraper._normalize_story_data(story)
        assert result["date"] == ""

    def test_normalize_story_data_site_name(self):
        story = {"title": "x", "url": "https://x.com", "score": 1, "id": 1, "time": 1000000}
        result = self.scraper._normalize_story_data(story)
        assert result["site_name"] == "hackernews_api"

    def test_fetch_story_details_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "type": "story",
            "url": "https://example.com",
            "title": "Test",
            "id": 1,
        }
        mock_response.raise_for_status = MagicMock()
        self.scraper.session = MagicMock()
        self.scraper.session.get.return_value = mock_response

        result = self.scraper._fetch_story_details(1)
        assert result is not None
        assert result["url"] == "https://example.com"

    def test_fetch_story_details_deleted(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"type": "story", "deleted": True, "id": 1}
        mock_response.raise_for_status = MagicMock()
        self.scraper.session = MagicMock()
        self.scraper.session.get.return_value = mock_response

        result = self.scraper._fetch_story_details(1)
        assert result is None

    def test_fetch_story_details_no_url(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"type": "story", "id": 1}
        mock_response.raise_for_status = MagicMock()
        self.scraper.session = MagicMock()
        self.scraper.session.get.return_value = mock_response

        result = self.scraper._fetch_story_details(1)
        assert result is None

    def test_fetch_story_details_not_story_type(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"type": "job", "url": "https://x.com", "id": 1}
        mock_response.raise_for_status = MagicMock()
        self.scraper.session = MagicMock()
        self.scraper.session.get.return_value = mock_response

        result = self.scraper._fetch_story_details(1)
        assert result is None

    def test_fetch_story_details_exception(self):
        self.scraper.session = MagicMock()
        self.scraper.session.get.side_effect = Exception("network error")

        result = self.scraper._fetch_story_details(1)
        assert result is None

    def test_parallel_fetch_stories(self):
        story_data = {"type": "story", "url": "https://x.com", "title": "Test", "id": 1}
        mock_response = MagicMock()
        mock_response.json.return_value = story_data
        mock_response.raise_for_status = MagicMock()
        self.scraper.session = MagicMock()
        self.scraper.session.get.return_value = mock_response

        results = self.scraper._parallel_fetch_stories([1, 2], max_workers=2)
        assert isinstance(results, list)

    def test_close(self):
        self.scraper.session = MagicMock()
        with patch.object(type(self.scraper).__bases__[0], "close", return_value=None):
            self.scraper.close()
        self.scraper.session.close.assert_called_once()

    def test_scrape_api_failure(self):
        self.scraper.session = MagicMock()
        self.scraper.session.get.side_effect = Exception("API down")

        result = self.scraper.scrape(output_format="json")
        assert result is None

    def test_scrape_empty_story_ids(self):
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = MagicMock()
        self.scraper.session = MagicMock()
        self.scraper.session.get.return_value = mock_response

        result = self.scraper.scrape(output_format="json")
        assert result == []

    def test_scrape_all_filtered_out(self):
        ids_resp = MagicMock()
        ids_resp.json.return_value = [1, 2]
        ids_resp.raise_for_status = MagicMock()

        story_resp = MagicMock()
        story_resp.json.return_value = {"type": "story", "url": "https://x.com", "title": "Low", "id": 1, "score": 5, "time": 1000000}
        story_resp.raise_for_status = MagicMock()

        self.scraper.session = MagicMock()
        self.scraper.session.get.side_effect = [ids_resp, story_resp, story_resp]

        result = self.scraper.scrape(output_format="json", min_score=9999)
        assert result == []


if __name__ == "__main__":
    unittest.main()
