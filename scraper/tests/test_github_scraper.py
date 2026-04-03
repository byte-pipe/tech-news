"""
Tests for the GitHub scraper.
"""

# flake8: noqa: E402

import os
import shutil
import sys
import tempfile

# Add parent directory to path before other imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import patch

from bs4 import BeautifulSoup

from scraper.scrapers.github import GitHubScraper


class TestGitHubScraper(unittest.TestCase):
    """Test cases for GitHubScraper class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary directory for test output
        self.test_output_dir = tempfile.mkdtemp()

        # Create scraper with test mode enabled
        self.scraper = GitHubScraper(test_mode=True, test_output_dir=self.test_output_dir)

        # Sample HTML for testing GitHub repository extraction
        self.test_html = """
        <article class="Box-row">
            <h2 class="h3 lh-condensed">
                <a href="/test-user/test-repo">
                    <span class="text-normal">test-user / </span>test-repo
                </a>
            </h2>
            <p class="col-9 color-fg-muted my-1 pr-4">
                This is a test repository description for unit testing
            </p>
            <div class="f6 color-fg-muted mt-2">
                <span class="d-inline-block ml-0 mr-3">
                    <span class="repo-language-color" style="background-color: #3572A5"></span>
                    <span itemprop="programmingLanguage">Python</span>
                </span>
                <a href="/test-user/test-repo/stargazers" class="Link--muted d-inline-block mr-3">
                    <svg aria-label="star" role="img" height="16" viewBox="0 0 16 16" version="1.1"
                        width="16" data-view-component="true" class="octicon octicon-star">
                        <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1
                        .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347"></path>
                        <path d="M8 2.695L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75
                        0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456"></path>
                    </svg>
                    1.2k
                </a>
                <a href="/test-user/test-repo/network/members" class="Link--muted d-inline-block mr-3">
                    <svg aria-label="fork" role="img" height="16" viewBox="0 0 16 16" version="1.1"
                        width="16" data-view-component="true" class="octicon octicon-repo-forked">
                        <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25
                        2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0"></path>
                        <path d="M5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5
                        .75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
                    </svg>
                    450
                </a>
                <span class="d-inline-block float-sm-right">
                    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1"
                        width="16" data-view-component="true" class="octicon octicon-star">
                        <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416
                        1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347"></path>
                        <path d="M8 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75
                        0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456"></path>
                    </svg>
                    125 stars today
                </span>
            </div>
        </article>
        """

        # Parse HTML with BeautifulSoup for testing
        self.test_soup = BeautifulSoup(self.test_html, "html.parser")
        self.test_element = self.test_soup.select_one("article.Box-row")

    def tearDown(self):
        """Clean up test fixtures."""
        # Remove the temporary test directory
        if hasattr(self, "test_output_dir") and os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

    def test_extract_data(self):
        """Test the _extract_data method."""
        # Call the method with our test element
        data = self.scraper._extract_data([self.test_element])

        # Verify result contains the expected fields
        self.assertEqual(len(data), 1)
        repo = data[0]

        # Check extracted fields
        self.assertEqual(repo["title"], "test-repo")
        self.assertEqual(repo["author"], "test-user")
        self.assertEqual(repo["description"], "This is a test repository description for unit testing")
        self.assertEqual(repo["language"], "Python")
        self.assertEqual(repo["stars"], "1200")  # Converted from 1.2k
        self.assertEqual(repo["forks"], "450")
        self.assertEqual(repo["today_stars"], "125")
        self.assertEqual(repo["url"], "https://github.com/test-user/test-repo")

    @patch("scraper.scrapers.github.BaseScraper._get_page")
    @patch("scraper.scrapers.github.BaseScraper._parse_html")
    def test_scrape_with_period(self, mock_parse, mock_get_page):
        """Test the scrape method with a specific time period."""
        # Set up mocks
        mock_get_page.return_value = self.test_html
        mock_parse.return_value = [self.test_element]

        # Call scrape with just one period for testing
        self.scraper.TIME_PERIODS = ["daily"]  # Override to just test one period
        result = self.scraper.scrape()

        # Verify expected results
        self.assertEqual(len(result), 1)  # Should get 1 result from mock (one element)
        self.assertEqual(result[0]["title"], "test-repo")
        self.assertEqual(result[0]["period"], "daily")  # Should add period metadata
        self.assertEqual(result[0]["author"], "test-user")

        # Verify mock calls
        mock_get_page.assert_called_once_with("https://github.com/trending?since=daily")
        mock_parse.assert_called_once()

    def test_remove_duplicates(self):
        """Test duplicate removal of GitHub data."""
        # Create test data with duplicates but from different periods
        test_data = [
            {"title": "repo-1", "url": "https://github.com/user/repo-1", "period": "daily"},
            {"title": "repo-2", "url": "https://github.com/user/repo-2", "period": "daily"},
            {"title": "repo-1", "url": "https://github.com/user/repo-1", "period": "weekly"},  # Duplicate
            {"title": "repo-3", "url": "https://github.com/user/repo-3", "period": "monthly"},
        ]

        # Use base class method to deduplicate
        deduped_data = self.scraper._remove_duplicates(test_data)

        # Check results
        self.assertEqual(len(deduped_data), 3)  # Should deduplicate to 3 repos

        # First encountered version should be kept (period: daily)
        repo1 = next(item for item in deduped_data if item["url"] == "https://github.com/user/repo-1")
        self.assertEqual(repo1["period"], "daily")


if __name__ == "__main__":
    unittest.main()
