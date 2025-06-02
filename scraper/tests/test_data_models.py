"""
Tests for standardized data models.
"""

import os
import sys
import unittest
from datetime import datetime

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.scraped_data import GitHubItem, HackerNewsItem, LobstersItem, ScrapedItem, ScrapingResult, validate_scraped_data  # noqa: E402


class TestScrapedItem(unittest.TestCase):
    """Test the base ScrapedItem model."""

    def test_minimal_item_creation(self):
        """Test creating item with only required fields."""
        item = ScrapedItem(title="Test Title", url="https://example.com")

        self.assertEqual(item.title, "Test Title")
        self.assertEqual(item.url, "https://example.com")
        self.assertIsNone(item.description)
        self.assertIsNotNone(item.scraped_at)
        self.assertEqual(item.metadata, {})

    def test_full_item_creation(self):
        """Test creating item with all fields."""
        test_date = datetime(2025, 6, 1, 12, 0, 0)

        item = ScrapedItem(
            title="Full Test Title", url="https://example.com/full", description="Test description", author="Test Author", date=test_date, tags=["tag1", "tag2"], metadata={"custom": "value"}, source_site="test_site"
        )

        self.assertEqual(item.title, "Full Test Title")
        self.assertEqual(item.description, "Test description")
        self.assertEqual(item.author, "Test Author")
        self.assertEqual(item.date, test_date)
        self.assertEqual(item.tags, ["tag1", "tag2"])
        self.assertEqual(item.metadata["custom"], "value")
        self.assertEqual(item.source_site, "test_site")

    def test_to_dict_conversion(self):
        """Test converting item to dictionary."""
        test_date = datetime(2025, 6, 1, 12, 0, 0)

        item = ScrapedItem(title="Dict Test", url="https://example.com/dict", date=test_date)

        data = item.to_dict()

        self.assertEqual(data["title"], "Dict Test")
        self.assertEqual(data["url"], "https://example.com/dict")
        self.assertEqual(data["date"], test_date.isoformat())
        self.assertIsInstance(data["scraped_at"], str)  # Should be ISO string

    def test_from_dict_creation(self):
        """Test creating item from dictionary."""
        data = {"title": "From Dict", "url": "https://example.com/from-dict", "description": "Created from dict", "date": "2025-06-01T12:00:00", "scraped_at": "2025-06-01T13:00:00"}

        item = ScrapedItem.from_dict(data)

        self.assertEqual(item.title, "From Dict")
        self.assertEqual(item.description, "Created from dict")
        self.assertIsInstance(item.date, datetime)
        self.assertIsInstance(item.scraped_at, datetime)

    def test_json_serialization(self):
        """Test JSON serialization and deserialization."""
        original_item = ScrapedItem(title="JSON Test", url="https://example.com/json", description="JSON test description")

        # Convert to JSON and back
        json_str = original_item.to_json()
        restored_item = ScrapedItem.from_json(json_str)

        self.assertEqual(original_item.title, restored_item.title)
        self.assertEqual(original_item.url, restored_item.url)
        self.assertEqual(original_item.description, restored_item.description)


class TestScrapingResult(unittest.TestCase):
    """Test the ScrapingResult container."""

    def test_successful_result(self):
        """Test creating successful scraping result."""
        items = [ScrapedItem(title="Item 1", url="https://example.com/1"), ScrapedItem(title="Item 2", url="https://example.com/2")]

        result = ScrapingResult(success=True, items=items)

        self.assertTrue(result.success)
        self.assertEqual(len(result.items), 2)
        self.assertIsNone(result.error_message)
        self.assertEqual(result.metadata["items_count"], 2)
        self.assertIn("scraped_at", result.metadata)

    def test_failed_result(self):
        """Test creating failed scraping result."""
        result = ScrapingResult(success=False, items=[], error_message="Network timeout")

        self.assertFalse(result.success)
        self.assertEqual(len(result.items), 0)
        self.assertEqual(result.error_message, "Network timeout")
        self.assertEqual(result.metadata["items_count"], 0)

    def test_result_serialization(self):
        """Test result serialization to dict."""
        items = [ScrapedItem(title="Test", url="https://example.com")]
        result = ScrapingResult(success=True, items=items)

        data = result.to_dict()

        self.assertTrue(data["success"])
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["items"][0]["title"], "Test")
        self.assertIsInstance(data["metadata"], dict)


class TestSiteSpecificItems(unittest.TestCase):
    """Test site-specific item types."""

    def test_github_item(self):
        """Test GitHub-specific item."""
        item = GitHubItem(title="Test Repo", url="https://github.com/test/repo")

        self.assertEqual(item.source_site, "github")
        self.assertIn("stars", item.metadata)
        self.assertIn("forks", item.metadata)
        self.assertIn("language", item.metadata)

    def test_hackernews_item(self):
        """Test HackerNews-specific item."""
        item = HackerNewsItem(title="HN Story", url="https://news.ycombinator.com/item?id=123")

        self.assertEqual(item.source_site, "hackernews")
        self.assertIn("score", item.metadata)
        self.assertIn("points", item.metadata)
        self.assertIn("comments_count", item.metadata)

    def test_lobsters_item(self):
        """Test Lobsters-specific item."""
        item = LobstersItem(title="Lobsters Story", url="https://lobste.rs/s/abc123")

        self.assertEqual(item.source_site, "lobsters")
        self.assertIn("score", item.metadata)
        self.assertIn("comments_count", item.metadata)


class TestDataValidation(unittest.TestCase):
    """Test data validation functions."""

    def test_valid_data_validation(self):
        """Test validation of valid data."""
        raw_data = [{"title": "Valid Item 1", "url": "https://example.com/1"}, {"title": "Valid Item 2", "url": "https://example.com/2", "description": "With desc"}]

        validated_items = validate_scraped_data(raw_data)

        self.assertEqual(len(validated_items), 2)
        self.assertIsInstance(validated_items[0], ScrapedItem)
        self.assertEqual(validated_items[0].title, "Valid Item 1")
        self.assertEqual(validated_items[1].description, "With desc")

    def test_missing_title_validation(self):
        """Test validation fails with missing title."""
        raw_data = [{"url": "https://example.com/1"}]  # Missing title

        with self.assertRaises(ValueError) as context:
            validate_scraped_data(raw_data)

        self.assertIn("Missing required field 'title'", str(context.exception))

    def test_missing_url_validation(self):
        """Test validation fails with missing URL."""
        raw_data = [{"title": "Valid Title"}]  # Missing URL

        with self.assertRaises(ValueError) as context:
            validate_scraped_data(raw_data)

        self.assertIn("Missing required field 'url'", str(context.exception))

    def test_empty_title_validation(self):
        """Test validation fails with empty title."""
        raw_data = [{"title": "", "url": "https://example.com/1"}]  # Empty title

        with self.assertRaises(ValueError) as context:
            validate_scraped_data(raw_data)

        self.assertIn("Missing required field 'title'", str(context.exception))


if __name__ == "__main__":
    unittest.main()
