"""
Base test class for scraper tests.

This module provides common test setup and teardown functionality.
"""

import os
import shutil
import tempfile
import unittest

from scraper.utils.logging_utils import setup_logging


class BaseScraperTest(unittest.TestCase):
    """Base test class with common setup and teardown for scraper tests."""

    def setUp(self):
        """Set up test environment with temporary directory and logging."""
        # Create temporary test output directory
        self.test_output_dir = tempfile.mkdtemp(prefix="scraper_test_")

        # Set up logging for tests
        setup_logging()

        # Store original environment variables
        self._original_env = os.environ.get("SCRAPER_TEST_OUTPUT_DIR")
        os.environ["SCRAPER_TEST_OUTPUT_DIR"] = self.test_output_dir

    def tearDown(self):
        """Clean up test environment."""
        # Clean up temporary directory
        if hasattr(self, "test_output_dir") and os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)

        # Restore environment variables
        if self._original_env is not None:
            os.environ["SCRAPER_TEST_OUTPUT_DIR"] = self._original_env
        elif "SCRAPER_TEST_OUTPUT_DIR" in os.environ:
            del os.environ["SCRAPER_TEST_OUTPUT_DIR"]

    def create_test_file(self, filename: str, content: str = "") -> str:
        """Create a test file in the temporary directory.

        Args:
            filename: Name of the file to create
            content: Content to write to the file

        Returns:
            Full path to the created file
        """
        file_path = os.path.join(self.test_output_dir, filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return file_path

    def assert_file_exists(self, filename: str):
        """Assert that a file exists in the test output directory.

        Args:
            filename: Name of the file to check
        """
        file_path = os.path.join(self.test_output_dir, filename)
        self.assertTrue(os.path.exists(file_path), f"File {filename} does not exist")

    def assert_file_contains(self, filename: str, content: str):
        """Assert that a file contains specific content.

        Args:
            filename: Name of the file to check
            content: Content that should be in the file
        """
        file_path = os.path.join(self.test_output_dir, filename)
        self.assert_file_exists(filename)

        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()

        self.assertIn(content, file_content)


class BaseScraperMockTest(BaseScraperTest):
    """Base test class with additional mocking support for scraper tests."""

    def setUp(self):
        """Set up test environment with mocking support."""
        super().setUp()

        # Store for mock objects that need cleanup
        self.mocks = []

    def tearDown(self):
        """Clean up mocks and test environment."""
        # Stop all mocks
        for mock in self.mocks:
            if hasattr(mock, "stop"):
                mock.stop()

        super().tearDown()

    def add_mock(self, mock):
        """Add a mock to be cleaned up automatically.

        Args:
            mock: Mock object to track for cleanup
        """
        self.mocks.append(mock)
        return mock
