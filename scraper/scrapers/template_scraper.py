"""
Template Scraper

This file provides a template for creating new scrapers. Use this as a starting point
when adding support for a new website.

Usage:
1. Copy this file to a new file named after the site you're scraping (e.g., example_site.py)
2. Update the class name and constants (SITE_NAME, URL, SELECTOR)
3. Implement the _extract_data method
4. Add the scraper to the main.py file

The template includes examples for both HTML and JSON-based scrapers.
"""

import logging
import os
import re
from datetime import datetime
from typing import Any, Dict, List

from bs4 import BeautifulSoup
from scraper.utils.network import fetch_json_with_retry

from .base import BaseScraper

logger = logging.getLogger(__name__)


def normalize_whitespace(text):
    """Normalize whitespace in text."""
    return re.sub(r"\s+", " ", text).strip() if text else ""


class TemplateScraper(BaseScraper):
    """
    Template scraper class. Copy this to create a new scraper.

    This template includes examples for both:
    1. HTML-based scraping (using BeautifulSoup)
    2. JSON API-based scraping

    Delete the sections you don't need and implement the required methods.
    """

    # Update these constants for your scraper
    SITE_NAME = "template"
    URL = "https://example.com"
    SELECTOR = "div.item"  # CSS selector for items, use None for JSON APIs

    def __init__(self, test_mode=False, test_output_dir=None):
        """Initialize the scraper."""
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)
        self.logger = logging.getLogger(__name__)

    ############################################################################
    # OPTION 1: HTML-based scraping (using BeautifulSoup)
    ############################################################################

    def _extract_data(self, items: List[BeautifulSoup], fields=None) -> List[Dict[str, Any]]:
        """
        Extract data from BeautifulSoup items.

        Args:
            items: List of BeautifulSoup items to extract data from
            fields: Optional fields to extract

        Returns:
            List of dictionaries containing extracted data
        """
        data = []

        for item in items:
            try:
                # Example selectors - update these for your site
                title_elem = item.select_one("h2 a")
                description_elem = item.select_one("p.description")

                if not title_elem:
                    continue

                # Extract text and normalize
                title = normalize_whitespace(title_elem.text)
                description = normalize_whitespace(description_elem.text) if description_elem else ""

                # Extract URL if present
                url = title_elem.get("href", "")
                if url and not url.startswith("http"):
                    # Handle relative URLs
                    url = f"https://example.com{url}"

                # Create data item
                data.append(
                    {
                        "title": title,
                        "description": description,
                        "url": url,
                        # Add more fields as needed
                    }
                )

            except Exception as e:
                self.logger.error(f"Error extracting item data: {str(e)}")
                continue

        return data

    ############################################################################
    # OPTION 2: JSON API-based scraping
    ############################################################################

    def scrape(self):
        """
        Custom scrape method for JSON API-based scrapers.

        Delete this method if you're using HTML-based scraping.
        """
        try:
            self.logger.info(f"Fetching data from {self.URL}")

            # Custom headers if needed
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", "Accept": "application/json"}

            # Fetch JSON data with retry
            json_data = fetch_json_with_retry(self.URL, headers=headers)

            if not json_data:
                self.logger.error("Failed to fetch JSON data")
                return

            # Example: Extract items from JSON response
            # Update the JSON path to match your API's structure
            items = json_data.get("data", {}).get("items", [])

            if not items:
                self.logger.error("No items found in JSON data")
                return

            # Process items
            data = []
            for item in items:
                try:
                    # Extract fields from JSON - update for your API
                    title = item.get("title", "").strip()
                    description = item.get("description", "").strip()
                    url = item.get("url", "")

                    # Add to data list
                    data.append(
                        {
                            "title": title,
                            "description": description,
                            "url": url,
                            # Add more fields as needed
                        }
                    )
                except Exception as e:
                    self.logger.error(f"Error processing item: {str(e)}")

            # Save the extracted data
            if not data:
                self.logger.error("No data extracted")
                return

            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            file_path = os.path.join(self.project_root, "data", f"{self.site_name}-{timestamp}.md")
            self._save_data(data, file_path)
            self.logger.info(f"Saved {len(data)} items to {file_path}")

        except Exception as e:
            self.logger.error(f"Error scraping {self.site_name}: {str(e)}")


# USAGE EXAMPLE:
"""
To create a new scraper:

1. Copy this file to a new file named after your site
2. Update the class name and constants
3. Implement either the _extract_data method (HTML) or the scrape method (JSON)
4. Add to main.py's scraper list

Example:

```python
# In examplesite.py
class ExampleSiteScraper(BaseScraper):
    SITE_NAME = "examplesite"
    URL = "https://example.com/trending"
    SELECTOR = "div.trending-item"

    def _extract_data(self, items, fields=None):
        data = []
        for item in items:
            # Extract and process data
            data.append({...})
        return data

# In main.py
from scraper.scrapers.examplesite import ExampleSiteScraper

scrapers = [
    # existing scrapers
    ExampleSiteScraper,
]
```
"""

if __name__ == "__main__":
    # Set up logging
    import logging

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Instantiate the scraper in test mode
    scraper = TemplateScraper(test_mode=True)

    # Run the scraper (this is just a template - won't actually scrape)
    print("This is a template scraper. Please customize it for your specific site.")
    print("See the comments and docstrings for instructions on how to use this template.")
