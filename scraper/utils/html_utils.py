"""
HTML parsing utilities for the scraper package.

This module provides common HTML parsing and processing functionality.
"""

import logging
from typing import List, Optional

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def create_soup(html_content: str, parser: str = "html.parser") -> Optional[BeautifulSoup]:
    """Create a BeautifulSoup object from HTML content.

    Args:
        html_content: HTML content to parse
        parser: Parser to use (default: "html.parser")

    Returns:
        BeautifulSoup object or None if parsing fails
    """
    if not html_content:
        logger.warning("No HTML content to parse")
        return None

    try:
        return BeautifulSoup(html_content, parser)
    except Exception as e:
        logger.error(f"Error parsing HTML: {str(e)}")
        return None


def select_elements(soup: BeautifulSoup, selector: str) -> List:
    """Select elements from a BeautifulSoup object with error handling.

    Args:
        soup: BeautifulSoup object to search
        selector: CSS selector string

    Returns:
        List of matching elements (empty list if none found or error)
    """
    if not soup:
        logger.warning("No soup object provided")
        return []

    try:
        elements = soup.select(selector)
        logger.debug(f"Found {len(elements)} elements matching selector: {selector}")
        return elements
    except Exception as e:
        logger.error(f"Error selecting elements with selector {selector}: {str(e)}")
        return []


def select_one_element(soup: BeautifulSoup, selector: str):
    """Select a single element from a BeautifulSoup object with error handling.

    Args:
        soup: BeautifulSoup object to search
        selector: CSS selector string

    Returns:
        First matching element or None if not found/error
    """
    if not soup:
        logger.warning("No soup object provided")
        return None

    try:
        return soup.select_one(selector)
    except Exception as e:
        logger.error(f"Error selecting element with selector {selector}: {str(e)}")
        return None


def safe_get_text(element, strip: bool = True, default: str = "") -> str:
    """Safely extract text from an element.

    Args:
        element: BeautifulSoup element
        strip: Whether to strip whitespace
        default: Default value if extraction fails

    Returns:
        Extracted text or default value
    """
    if not element:
        return default

    try:
        text = element.get_text(strip=strip)
        return text if text else default
    except Exception as e:
        logger.debug(f"Error extracting text from element: {str(e)}")
        return default


def safe_get_attribute(element, attribute: str, default: str = "") -> str:
    """Safely extract an attribute from an element.

    Args:
        element: BeautifulSoup element
        attribute: Attribute name to extract
        default: Default value if extraction fails

    Returns:
        Attribute value or default value
    """
    if not element:
        return default

    try:
        if element.has_attr(attribute):
            return element[attribute]
        return default
    except Exception as e:
        logger.debug(f"Error extracting attribute {attribute}: {str(e)}")
        return default


def remove_unwanted_elements(soup: BeautifulSoup, tags_to_remove: List[str] = None, classes_to_remove: List[str] = None) -> BeautifulSoup:
    """Remove unwanted elements from a BeautifulSoup object.

    Args:
        soup: BeautifulSoup object to clean
        tags_to_remove: List of tag names to remove
        classes_to_remove: List of class names to remove

    Returns:
        Cleaned BeautifulSoup object
    """
    if not soup:
        return soup

    # Default tags to remove
    if tags_to_remove is None:
        tags_to_remove = ["script", "style", "nav", "header", "footer", "aside", "iframe"]

    # Default classes to remove
    if classes_to_remove is None:
        classes_to_remove = ["sidebar", "navigation", "menu", "ads", "advertisement", "social-share", "comments", "related-posts"]

    try:
        # Remove unwanted tags
        for tag in soup.find_all(tags_to_remove):
            tag.decompose()

        # Remove elements with unwanted classes
        for class_name in classes_to_remove:
            for element in soup.find_all(class_=lambda x: x and class_name in x):
                element.decompose()

    except Exception as e:
        logger.warning(f"Error removing unwanted elements: {str(e)}")

    return soup
