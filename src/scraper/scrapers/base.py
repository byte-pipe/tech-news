import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os
import logging
import re
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class BaseScraper:
    SITE_NAME = None
    URL = None
    SELECTOR = None

    def __init__(self):
        self.site_name = self.SITE_NAME
        self.url = self.URL
        self.selector = self.SELECTOR
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
        )
        # Get the project root directory (three levels up from this file)
        self.project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        logger.info(f"Project root: {self.project_root}")
        logger.info(f"Initialized scraper for site: {self.site_name}")

    def _get_page(self, url):
        try:
            logger.info(f"Fetching URL: {url}")
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {str(e)}")
            return None

    def _parse_html(self, html, selector):
        if not html:
            logger.warning("No HTML content to parse")
            return []
        try:
            soup = BeautifulSoup(html, "html.parser")
            items = soup.select(selector)
            logger.info(f"Found {len(items)} items matching selector: {selector}")
            return items
        except Exception as e:
            logger.error(f"Error parsing HTML with selector {selector}: {str(e)}")
            return []

    def _save_data(self, data, file_path):
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Sort data by title
            data.sort(key=lambda x: x.get("title", ""))

            if data:
                # Write as markdown table only
                headers = list(data[0].keys())
                with open(file_path, "w") as f:
                    # Write header
                    f.write("| " + " | ".join(headers) + " |\n")
                    f.write("| " + " | ".join(["-" * len(h) for h in headers]) + " |\n")
                    # Write rows
                    for item in data:
                        row = [str(item.get(h, "")) for h in headers]
                        f.write("| " + " | ".join(row) + " |\n")

            logger.info(f"Saved {len(data)} items to {file_path}")
        except Exception as e:
            logger.error(f"Error saving data to {file_path}: {str(e)}")

    def scrape(self):
        """Main scraping method that handles the common scraping workflow."""
        try:
            # Get the page content
            html = self._get_page(self.url)
            if not html:
                return

            # Parse the HTML
            items = self._parse_html(html, self.selector)
            if not items:
                return

            # Extract data
            data = self._extract_data(items)

            # Save the data
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            file_path = os.path.join(self.project_root, "data", f"{self.site_name}-{timestamp}.md")
            self._save_data(data, file_path)

        except Exception as e:
            logger.error(f"Error scraping {self.site_name}: {str(e)}")

    def _extract_data(self, items, fields=None):
        """Extract data from scraped items.

        Args:
            items: List of scraped items
            fields: Optional list of fields to extract

        Returns:
            List of dictionaries containing extracted data
        """
        return []
