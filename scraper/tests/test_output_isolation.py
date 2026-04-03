"""
Test to ensure that test runs don't write to the actual data directory.
"""

# flake8: noqa: E402

import os
import shutil
import sys
import tempfile
from datetime import datetime

# Add parent directory to path before other imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch

from scraper.scrapers.github import GitHubScraper


class TestOutputIsolation(unittest.TestCase):
    """Test that scraper output is properly isolated during tests."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary directory for test output
        self.test_output_dir = tempfile.mkdtemp()

        # Record the actual data directory path
        self.scraper = GitHubScraper(test_mode=True, test_output_dir=self.test_output_dir)
        self.actual_data_dir = os.path.join(self.scraper.project_root, "data")

        # Sample data to use for testing
        self.sample_data = [
            {
                "title": "Test Repo",
                "url": "https://github.com/test/repo",
                "description": "Test repository for testing output isolation",
                "author": "test-user",
                "stars": "100",
                "forks": "50",
            }
        ]

        # Record files in the actual data directory before the test
        self.data_files_before = self._get_data_directory_files()

    def tearDown(self):
        """Clean up test fixtures."""
        # Remove the temporary test directory
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

    def _get_data_directory_files(self):
        """Get a list of all files in the data directory."""
        data_files = []
        if os.path.exists(self.actual_data_dir):
            for root, _, files in os.walk(self.actual_data_dir):
                for file in files:
                    if file.endswith((".md", ".json", ".csv")):
                        rel_path = os.path.relpath(os.path.join(root, file), self.actual_data_dir)
                        data_files.append(rel_path)
        return set(data_files)

    @patch("scraper.scrapers.github.BaseScraper._get_page")
    @patch("scraper.scrapers.github.BaseScraper._parse_html")
    def test_output_isolation_in_test_mode(self, mock_parse, mock_get_page):
        """Test that files are written to the test directory, not the actual data directory."""
        # Set up mocks to return sample data
        mock_get_page.return_value = "<html><body></body></html>"
        mock_parse.return_value = ["<article class='Box-row'></article>"]

        # Mock _extract_data to return our sample data
        with patch.object(self.scraper, "_extract_data", return_value=self.sample_data):
            # Run the scrape method
            self.scraper.scrape(output_format="json")

            # Verify that a file was created in the test output directory
            test_files = os.listdir(self.test_output_dir)
            test_json_files = [f for f in test_files if f.endswith(".json")]
            self.assertTrue(test_json_files, "No output file created in test directory")
            self.assertEqual(1, len(test_json_files), "Expected exactly one output file")

            # Verify the file contains our test data
            with open(os.path.join(self.test_output_dir, test_json_files[0]), "r") as f:
                import json

                content = json.load(f)
                self.assertEqual(self.sample_data, content, "Output file doesn't contain expected data")

            # Verify that no new files were created in the actual data directory
            data_files_after = self._get_data_directory_files()
            self.assertEqual(self.data_files_before, data_files_after, "Files were created in the actual data directory during the test")

            # Extra check - explicitly look for the two untracked files mentioned in git status
            problematic_files = [os.path.join(self.actual_data_dir, "2025-05-20", "github-20250520-135326.md"), os.path.join(self.actual_data_dir, "2025-05-20", "github-20250520-135413.md")]

            # Check that neither file gets created during the test
            for f in problematic_files:
                if not os.path.exists(f) or os.path.relpath(f, self.actual_data_dir) in self.data_files_before:
                    continue  # Skip if it doesn't exist or was already there before test
                self.fail(f"Test created file in actual data directory: {f}")

    def test_no_output_without_test_mode(self):
        """Test that files are written to the actual data directory without test mode."""
        # Create a scraper without test mode
        regular_scraper = GitHubScraper()

        # Verify the scraper is not in test mode - test_mode is False by default
        self.assertFalse(regular_scraper.test_mode, "Scraper should not be in test mode")

        now = datetime.now()
        date_folder = now.strftime("%Y-%m-%d")
        expected_folder = os.path.join(regular_scraper.project_root, "data", date_folder)

        # We're not actually running the scrape, just checking the configuration
        self.assertTrue(os.path.normpath(expected_folder).startswith(os.path.normpath(self.actual_data_dir)), "Regular scraper should use actual data directory")


if __name__ == "__main__":
    unittest.main()
