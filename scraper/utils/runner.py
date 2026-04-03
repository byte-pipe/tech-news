"""
Common runner utility for standalone scraper execution.

This module provides a standardized way to run scrapers when executed directly.
"""

from typing import Optional, Type

from scraper.scrapers.base import BaseScraper
from scraper.utils.logging_utils import configure_scraper_logging


def run_scraper(scraper_class: Type[BaseScraper], output_format: str = "markdown", test_mode: bool = False, test_output_dir: Optional[str] = None):
    """Run a scraper when executed as a standalone script.

    Args:
        scraper_class: The scraper class to instantiate and run
        output_format: The output format to use (markdown, json, csv)
        test_mode: Whether to run in test mode
        test_output_dir: Directory for test output if in test mode
    """
    # Set up logging
    configure_scraper_logging()

    # Create and run the scraper
    scraper = scraper_class(test_mode=test_mode, test_output_dir=test_output_dir)
    scraper.scrape(output_format=output_format)
