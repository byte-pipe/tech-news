"""
Pytest configuration and fixtures for scraper tests.
"""

import os
import shutil
import tempfile
from unittest.mock import patch

import pytest


@pytest.fixture
def test_output_dir():
    """Create a temporary directory for test outputs.

    This fixture creates a temporary directory for test files and
    cleans it up after the test is complete.

    Returns:
        str: Path to the temporary directory
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    yield temp_dir

    # Clean up after the test
    shutil.rmtree(temp_dir)


@pytest.fixture
def test_env_with_output_dir():
    """Set up environment variables for testing and create a temp directory.

    This fixture:
    1. Creates a temporary directory
    2. Sets the SCRAPER_TEST_MODE and SCRAPER_TEST_OUTPUT_DIR environment variables
    3. Cleans up after the test

    Returns:
        str: Path to the temporary directory
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Set environment variables
    old_test_mode = os.environ.get("SCRAPER_TEST_MODE")
    old_test_dir = os.environ.get("SCRAPER_TEST_OUTPUT_DIR")

    os.environ["SCRAPER_TEST_MODE"] = "true"
    os.environ["SCRAPER_TEST_OUTPUT_DIR"] = temp_dir

    yield temp_dir

    # Clean up after the test
    shutil.rmtree(temp_dir)

    # Restore old environment variables
    if old_test_mode is not None:
        os.environ["SCRAPER_TEST_MODE"] = old_test_mode
    else:
        os.environ.pop("SCRAPER_TEST_MODE", None)

    if old_test_dir is not None:
        os.environ["SCRAPER_TEST_OUTPUT_DIR"] = old_test_dir
    else:
        os.environ.pop("SCRAPER_TEST_OUTPUT_DIR", None)


@pytest.fixture
def mock_scraper_base():
    """Mock the BaseScraper's methods that interact with external systems.

    This fixture patches:
    1. _get_page - to avoid actual network requests
    2. _parse_html - to return controlled test data

    The mocks are automatically restored after the test.
    """
    with patch("scrapers.base.BaseScraper._get_page") as mock_get_page, patch("scrapers.base.BaseScraper._parse_html") as mock_parse_html:
        yield {"get_page": mock_get_page, "parse_html": mock_parse_html}
