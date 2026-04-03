"""
Browser utility module for Selenium-based web scraping.

This module provides helpers for setting up Selenium WebDriver instances
in a consistent way that works across both local and CI environments.
"""

import logging
from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger(__name__)

try:
    from webdriver_manager.chrome import ChromeDriverManager

    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    logger.warning("webdriver_manager not installed. Falling back to system ChromeDriver.")
    WEBDRIVER_MANAGER_AVAILABLE = False


def get_chrome_options(headless=True):
    """
    Create Chrome options with sensible defaults for scraping.

    Args:
        headless: Whether to run Chrome in headless mode

    Returns:
        Chrome options object
    """
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")

    # Common options for stability, especially in CI environments
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    return chrome_options


def get_chrome_driver(headless=True):
    """
    Create a Chrome WebDriver instance with appropriate settings.

    This function handles the differences between local and CI environments
    by using webdriver-manager if available.

    Args:
        headless: Whether to run Chrome in headless mode

    Returns:
        Chrome WebDriver instance
    """
    options = get_chrome_options(headless)

    if WEBDRIVER_MANAGER_AVAILABLE:
        # Use webdriver-manager to get the appropriate ChromeDriver automatically
        logger.info("Using webdriver-manager to install ChromeDriver")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        # Fall back to system ChromeDriver
        logger.info("Using system ChromeDriver")
        driver = webdriver.Chrome(options=options)

    return driver


@contextmanager
def chrome_driver_context(headless=True):
    """
    Context manager for Chrome WebDriver that ensures proper cleanup.

    Args:
        headless: Whether to run Chrome in headless mode

    Yields:
        Chrome WebDriver instance
    """
    driver = None
    try:
        driver = get_chrome_driver(headless)
        logger.info("Chrome driver initialized successfully")
        yield driver
    except Exception as e:
        logger.error(f"Error initializing Chrome driver: {str(e)}")
        raise
    finally:
        if driver:
            try:
                driver.quit()
                logger.info("Chrome driver closed successfully")
            except Exception as e:
                logger.error(f"Error closing Chrome driver: {str(e)}")
