"""Tests for the AI summarization module."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

# Import the OpenAI class directly in the test
try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    # Mock OpenAI for tests when it's not available
    OpenAI = MagicMock
    OPENAI_AVAILABLE = False

# Import the code to test
from scraper.utils.summarizer import ArticleSummarizer


class TestSummarizer(unittest.TestCase):
    """Test the ArticleSummarizer class."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_content = """
        # Test Article

        This is a test article with some content that should be summarized.
        The article discusses various aspects of Python programming.

        ## Key Points

        - Python is a versatile language
        - It has a rich ecosystem of libraries
        - It's widely used in data science

        ## Conclusion

        Python continues to grow in popularity.
        """

        self.test_metadata = {"title": "Test Article", "url": "https://example.com/test", "site_name": "testsite", "author": "Test Author"}

        self.summarizer = ArticleSummarizer(model_name="test-model")

    @patch("scraper.utils.summarizer.OPENAI_AVAILABLE", True)
    def test_summarize(self):
        """Test that summarization works correctly."""
        # Mock the client and OpenAI class
        with patch("scraper.utils.summarizer.OpenAI") as mock_openai_class:
            # Mock the OpenAI client response
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_choice = MagicMock()
            mock_message = MagicMock()

            mock_message.content = "- Python is versatile\n- Rich ecosystem\n- Popular in data science"
            mock_choice.message = mock_message
            mock_response.choices = [mock_choice]
            mock_client.chat.completions.create.return_value = mock_response

            # Set up the mock
            mock_openai_class.return_value = mock_client
            self.summarizer.client = mock_client

            # Call the method
            result = self.summarizer.summarize(self.test_content, "Test Article")

            # Verify results
            self.assertIsNotNone(result)
            self.assertEqual(result, "- Python is versatile\n- Rich ecosystem\n- Popular in data science")

            # Verify the client was called correctly
            mock_client.chat.completions.create.assert_called_once()
            call_args = mock_client.chat.completions.create.call_args[1]
            self.assertEqual(call_args["model"], "test-model")
            self.assertEqual(len(call_args["messages"]), 2)
            self.assertEqual(call_args["messages"][0]["role"], "system")
            self.assertTrue("Test Article" in call_args["messages"][0]["content"])
            self.assertEqual(call_args["messages"][1]["role"], "user")

    def test_create_slug(self):
        """Test slug creation."""
        test_cases = [
            ("Simple Title", "simple-title"),
            ("Title with ! Special $ Characters", "title-with-special-characters"),
            ("Very Long Title That Should Be Truncated To A Maximum Length", "very-long-title-that-should-be-truncated-to-a-maximum"),
            ("", ""),
            ("   Spaces   ", "spaces"),
        ]

        for title, expected in test_cases:
            with self.subTest(title=title):
                result = self.summarizer._create_slug(title)
                self.assertEqual(result, expected)

    @patch("scraper.utils.summarizer.OPENAI_AVAILABLE", True)
    @patch("scraper.utils.summarizer.ArticleSummarizer.summarize")
    def test_save_summary(self, mock_summarize):
        """Test saving a summary to a file."""
        # Setup
        mock_summarize.return_value = "- Key point 1\n- Key point 2\n- Key point 3"

        with tempfile.TemporaryDirectory() as temp_dir:
            # Call the method
            file_path = self.summarizer.save_summary("- Key point 1\n- Key point 2\n- Key point 3", self.test_metadata, temp_dir)

            # Verify results
            self.assertIsNotNone(file_path)
            self.assertTrue(os.path.exists(file_path))

            # Check file contents
            with open(file_path, "r") as f:
                content = f.read()
                self.assertIn("---", content)  # Has YAML frontmatter
                # Check for title and site with flexible formatting (handles quotes)
                self.assertTrue("Test Article" in content)
                self.assertIn("site:", content)
                self.assertIn("testsite", content)
                self.assertIn("- Key point 1", content)
                self.assertIn("- Key point 2", content)
                self.assertIn("- Key point 3", content)
                self.assertIn("summarized_at:", content)


    @patch("scraper.utils.summarizer.OPENAI_AVAILABLE", True)
    @patch("scraper.utils.summarizer.ArticleSummarizer.summarize")
    def test_save_summary_uses_content_file(self, mock_summarize):
        """Test that save_summary derives filename from content_file when present."""
        mock_summarize.return_value = "Summary text"
        metadata_with_cf = {
            **self.test_metadata,
            "content_file": "github-my-cool-repo",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = self.summarizer.save_summary("Summary text", metadata_with_cf, temp_dir)
            self.assertIsNotNone(file_path)
            self.assertTrue(file_path.endswith("github-my-cool-repo-summary.md"))

    @patch("scraper.utils.summarizer.OPENAI_AVAILABLE", True)
    @patch("scraper.utils.summarizer.ArticleSummarizer.summarize")
    def test_save_summary_falls_back_without_content_file(self, mock_summarize):
        """Test that save_summary uses slug fallback when content_file is absent."""
        mock_summarize.return_value = "Summary text"

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = self.summarizer.save_summary("Summary text", self.test_metadata, temp_dir)
            self.assertIsNotNone(file_path)
            # Should use site_name-slug pattern
            filename = os.path.basename(file_path)
            self.assertTrue(filename.startswith("testsite-"))
            self.assertTrue(filename.endswith("-summary.md"))


if __name__ == "__main__":
    unittest.main()
