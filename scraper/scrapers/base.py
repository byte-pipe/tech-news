import json
import logging
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Tuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from scraper.constants import CSV_EXTENSION, DEFAULT_REQUEST_TIMEOUT, DEFAULT_USER_AGENT, JSON_EXTENSION, MARKDOWN_EXTENSION, MAX_DESCRIPTION_LENGTH
from scraper.core.data_organizer import DataOrganizer
from scraper.utils.datetime_utils import get_date_folder
from scraper.utils.html_utils import create_soup, select_elements
from scraper.utils.mixins import SessionManagerMixin
from scraper.utils.paths import ensure_directory, get_project_root

logger = logging.getLogger(__name__)


class BaseScraper(SessionManagerMixin):
    SITE_NAME = None
    URL = None
    SELECTOR = None

    def __init__(self, test_mode=False, test_output_dir=None):
        self.site_name = self.SITE_NAME
        self.url = self.URL
        self.selector = self.SELECTOR
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": DEFAULT_USER_AGENT})
        # Get the project root directory using utility function
        self.project_root = get_project_root(levels_up=3)

        # Add test mode configuration
        self.test_mode = test_mode
        self.test_output_dir = test_output_dir
        # If in test mode with no output dir specified, use environment variable if available
        if self.test_mode and not self.test_output_dir:
            self.test_output_dir = os.environ.get("SCRAPER_TEST_OUTPUT_DIR")

        self.logger = logger

    def _get_page(self, url):
        try:
            self.logger.info(f"Fetching URL: {url}")
            response = self.session.get(url, timeout=DEFAULT_REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            self.logger.error(f"Error fetching {url}: {str(e)}")
            return None

    def _parse_html(self, html, selector):
        soup = create_soup(html)
        if not soup:
            return []
        return select_elements(soup, selector)

    def _save_data(self, data, file_path, format="markdown"):
        """Save scraped data to a file in the specified format.

        Args:
            data: List of dictionaries containing scraped data
            file_path: Path to the output file
            format: Output format - one of 'markdown', 'json', or 'csv'

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # If in test mode and test output directory is specified, modify the file path
            if self.test_mode and self.test_output_dir:
                file_name = os.path.basename(file_path)
                file_path = os.path.join(self.test_output_dir, file_name)
                self.logger.info(f"TEST MODE: Redirecting output to {file_path}")

            # Create directory if it doesn't exist
            ensure_directory(os.path.dirname(file_path))

            # If file_path includes an extension, use that to determine format
            # unless format is explicitly specified
            if "." in os.path.basename(file_path) and format == "markdown":
                extension = os.path.splitext(file_path)[1].lower()
                if extension == ".json":
                    format = "json"
                elif extension == ".csv":
                    format = "csv"

            # Sort data by title
            if data:
                data.sort(key=lambda x: x.get("title", ""))

            # Adjust file extension based on format if needed
            if format == "json" and not file_path.lower().endswith(".json"):
                file_path = os.path.splitext(file_path)[0] + ".json"
            elif format == "csv" and not file_path.lower().endswith(".csv"):
                file_path = os.path.splitext(file_path)[0] + ".csv"
            elif format == "markdown" and not file_path.lower().endswith((".md", ".markdown")):
                file_path = os.path.splitext(file_path)[0] + ".md"

            if not data:
                self.logger.warning(f"No data to save to {file_path}")
                # Create an empty file anyway
                with open(file_path, "w") as f:
                    if format == "json":
                        f.write("[]")
                    # For CSV and markdown, just create an empty file
                return True

            # Save data based on format
            if format == "json":
                self._save_as_json(data, file_path)
            elif format == "csv":
                self._save_as_csv(data, file_path)
            else:  # default to markdown
                self._save_as_markdown(data, file_path)

            self.logger.info(f"Saved {len(data)} items to {file_path} in {format} format")
            return True
        except Exception as e:
            self.logger.error(f"Error saving data to {file_path}: {str(e)}")
            return False

    def _save_as_markdown(self, data, file_path):
        """Save data as a markdown table.

        Args:
            data: List of dictionaries containing scraped data
            file_path: Path to the output file
        """
        headers = list(data[0].keys())
        with open(file_path, "w") as f:
            # Write header
            f.write("| " + " | ".join(headers) + " |\n")
            f.write("| " + " | ".join(["-" * len(h) for h in headers]) + " |\n")
            # Write rows
            for item in data:
                row = [str(item.get(h, "")) for h in headers]
                f.write("| " + " | ".join(row) + " |\n")

    def _save_as_json(self, data, file_path):
        """Save data as JSON.

        Args:
            data: List of dictionaries containing scraped data
            file_path: Path to the output file
        """
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _save_as_csv(self, data, file_path):
        """Save data as CSV.

        Args:
            data: List of dictionaries containing scraped data
            file_path: Path to the output file
        """
        import csv

        headers = list(data[0].keys())

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for item in data:
                # Make sure every item has all the fields
                for header in headers:
                    if header not in item:
                        item[header] = ""
                # Convert values to strings
                cleaned_item = {k: str(v) if v is not None else "" for k, v in item.items()}
                writer.writerow(cleaned_item)

    def scrape(self, output_format="markdown"):
        """Main scraping method that handles the common scraping workflow.

        Args:
            output_format: Format to save the data in - one of 'markdown', 'json', or 'csv'
                           Default is 'markdown'

        Returns:
            List of dictionaries containing scraped data, or empty list if no data was extracted
        """
        try:
            # Get the page content
            html = self._get_page(self.url)
            if not html:
                return []

            # Parse the HTML
            items = self._parse_html(html, self.selector)
            if not items:
                return []

            # Extract data
            data = self._extract_data(items)

            # Remove duplicates based on URL
            data = self._remove_duplicates(data)

            if not data:
                self.logger.error(f"No data extracted from {self.site_name}.")
                return []

            # Save the data using organized structure
            date_folder = get_date_folder()

            # Determine folder path based on test mode
            if self.test_mode and self.test_output_dir:
                folder_path = self.test_output_dir
                self.logger.info(f"TEST MODE: Using test output directory: {folder_path}")
            else:
                # Use DataOrganizer to create organized structure
                data_organizer = DataOrganizer()
                try:
                    # Only create the raw directory for scraped data
                    folder_path = data_organizer.ensure_directory(date_folder, "raw")
                    self.logger.info(f"Using organized raw data directory: {folder_path}")
                except Exception as e:
                    self.logger.error(f"Failed to create organized directory structure: {str(e)}")
                    # Fallback to basic directory creation
                    folder_path = os.path.join(self.project_root, "data", date_folder)
                    self.logger.warning(f"Using fallback raw data directory: {folder_path}")

            # Create folder if it doesn't exist
            ensure_directory(folder_path)

            # Use the appropriate file extension based on the output format
            if output_format == "json":
                file_extension = JSON_EXTENSION
            elif output_format == "csv":
                file_extension = CSV_EXTENSION
            else:  # default to markdown
                file_extension = MARKDOWN_EXTENSION

            file_path = os.path.join(folder_path, f"{self.site_name}{file_extension}")
            self._save_data(data, file_path, format=output_format)

            self.logger.info(f"Successfully extracted and saved {len(data)} items from {self.site_name} in {output_format} format")
            return data

        except Exception as e:
            self.logger.error(f"Error scraping {self.site_name}: {str(e)}")
            return None

    def _remove_duplicates(self, data):
        """Remove duplicate items based on URL.

        Args:
            data: List of dictionaries with article data

        Returns:
            Deduplicated list of items
        """
        if not data:
            return []

        # Remove duplicates based on URL if present, otherwise use title
        unique_items = {}
        key_field = "url" if any("url" in item for item in data) else "title"

        for item in data:
            if key_field in item and item[key_field]:
                key = item[key_field]
                if key not in unique_items:
                    unique_items[key] = item
            else:
                # If item has no URL or title, include it anyway
                unique_items[f"item_{id(item)}"] = item

        deduped_data = list(unique_items.values())

        # Log deduplication results
        orig_count = len(data)
        deduped_count = len(deduped_data)
        if orig_count > deduped_count:
            self.logger.info(f"Removed {orig_count - deduped_count} duplicate items from {self.site_name}")

        return deduped_data

    # Standardized extraction methods
    def extract_title(self, element, selectors=None) -> str:
        """Extract title from an element using multiple possible selectors.

        Args:
            element: BeautifulSoup element to extract from
            selectors: List of CSS selectors to try, in order of preference
                       Default selectors tried: h1, h2, h3, .title, [class*="title"],
                                               .headline, .heading, a

        Returns:
            Extracted title string or empty string if not found
        """
        if not selectors:
            selectors = ["h1", "h2", "h3", ".title", '[class*="title"]', ".headline", ".heading", "a"]

        for selector in selectors:
            try:
                title_elem = element.select_one(selector)
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    if title:
                        return title
            except Exception as e:
                self.logger.debug(f"Error extracting title with selector {selector}: {str(e)}")

        # If no selectors matched, try direct text
        if element.get_text(strip=True):
            return element.get_text(strip=True)

        return ""

    def extract_url(self, element, base_url=None, selectors=None) -> str:
        """Extract URL from an element, ensuring it's absolute.

        Args:
            element: BeautifulSoup element to extract from
            base_url: Base URL to resolve relative URLs against
            selectors: List of CSS selectors to try, in order of preference
                       Default selectors tried: a, [href], [data-url]

        Returns:
            Absolute URL string or empty string if not found
        """
        if not selectors:
            selectors = ["a.read-more", "a.u-url", "a", "[href]", "[data-url]", "[data-link]"]

        url = ""

        # Try to find URL using selectors
        for selector in selectors:
            try:
                url_elem = element.select_one(selector)
                if url_elem and url_elem.has_attr("href"):
                    url = url_elem["href"]
                    break
                elif url_elem and url_elem.has_attr("data-url"):
                    url = url_elem["data-url"]
                    break
                elif url_elem and url_elem.has_attr("data-link"):
                    url = url_elem["data-link"]
                    break
            except Exception as e:
                self.logger.debug(f"Error extracting URL with selector {selector}: {str(e)}")

        # Check if the element itself has an href attribute
        if not url and element.has_attr("href"):
            url = element["href"]

        # Make URL absolute if it's relative
        if url and base_url:
            url = urljoin(base_url, url)

        return url.strip()

    def extract_date(self, element, selectors=None, formats=None, default_format=None) -> Tuple[str, datetime]:
        """Extract date from an element, with fallbacks and format detection.

        Args:
            element: BeautifulSoup element to extract from
            selectors: List of CSS selectors to try, in order of preference
                       Default selectors tried: time, [datetime], .date, [class*="date"],
                                              [class*="time"], .published, .meta
            formats: List of date formats to try parsing
                    Default formats tried: "%Y-%m-%d", "%B %d, %Y", "%d %B %Y",
                                          "%b %d, %Y", "%Y/%m/%d", "%d/%m/%Y"
            default_format: Format string for current date if no date found

        Returns:
            Tuple of (date string, datetime object)
        """
        if not selectors:
            selectors = ["time", "[datetime]", ".date", '[class*="date"]', '[class*="time"]', ".published", ".meta", "[pubdate]"]

        if not formats:
            formats = ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ", "%B %d, %Y", "%d %B %Y", "%b %d, %Y", "%Y/%m/%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%m-%d-%Y"]

        date_str = ""
        date_obj = None

        # Try to find date using selectors
        for selector in selectors:
            try:
                date_elem = element.select_one(selector)
                if date_elem:
                    # Check for datetime attribute first
                    if date_elem.has_attr("datetime"):
                        date_str = date_elem["datetime"]
                    elif date_elem.has_attr("pubdate"):
                        date_str = date_elem["pubdate"]
                    else:
                        date_str = date_elem.get_text(strip=True)

                    if date_str:
                        break
            except Exception as e:
                self.logger.debug(f"Error extracting date with selector {selector}: {str(e)}")

        # If date string found, try to parse it
        if date_str:
            # Clean up the date string (remove 'Posted on', 'Published:', etc.)
            date_str = re.sub(r"^(Posted on|Published|Posted|Date|Updated)(\s|:)", "", date_str)
            date_str = date_str.strip()

            # Try different date formats
            for fmt in formats:
                try:
                    date_obj = datetime.strptime(date_str, fmt)
                    date_str = date_obj.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    continue

        # If no date found or parsing failed, use current date or specified default
        if not date_obj:
            date_obj = datetime.now()
            if default_format:
                date_str = date_obj.strftime(default_format)
            else:
                date_str = date_obj.strftime("%Y-%m-%d")

        return date_str, date_obj

    def extract_author(self, element, selectors=None) -> str:
        """Extract author from an element.

        Args:
            element: BeautifulSoup element to extract from
            selectors: List of CSS selectors to try, in order of preference
                      Default selectors tried: .author, [rel="author"],
                                              [class*="author"], .byline

        Returns:
            Author string or empty string if not found
        """
        if not selectors:
            selectors = [".author", '[rel="author"]', '[class*="author"]', ".byline", '[itemprop="author"]', ".meta-author"]

        for selector in selectors:
            try:
                author_elem = element.select_one(selector)
                if author_elem:
                    author = author_elem.get_text(strip=True)
                    if author:
                        # Remove "By" or "Author:" prefixes
                        author = re.sub(r"^(By|Author|Written by)(\s|:)", "", author)
                        return author.strip()
            except Exception as e:
                self.logger.debug(f"Error extracting author with selector {selector}: {str(e)}")

        return ""

    def extract_tags(self, element, selectors=None, delimiter=",") -> List[str]:
        """Extract tags/categories from an element.

        Args:
            element: BeautifulSoup element to extract from
            selectors: List of CSS selectors to try, in order of preference
                      Default selectors tried: .tags, .categories, [class*="tag"],
                                             [class*="category"], .topics
            delimiter: Character used to split multiple tags if found in a single element

        Returns:
            List of tag strings
        """
        if not selectors:
            selectors = [".tags a", ".categories a", '[class*="tag"]', '[class*="category"]', ".topics a", '[rel="category tag"]']

        tags = []

        # Try each selector
        for selector in selectors:
            try:
                # First try to find multiple tag elements
                tag_elems = element.select(selector)
                if tag_elems:
                    for tag_elem in tag_elems:
                        tag = tag_elem.get_text(strip=True)
                        if tag and tag not in tags:
                            tags.append(tag)

                # If no multiple elements found, try a single element that might contain multiple tags
                if not tags:
                    tag_elem = element.select_one(selector)
                    if tag_elem:
                        tag_text = tag_elem.get_text(strip=True)
                        if delimiter in tag_text:
                            split_tags = [t.strip() for t in tag_text.split(delimiter)]
                            tags.extend([t for t in split_tags if t])
                        else:
                            tags.append(tag_text)
            except Exception as e:
                self.logger.debug(f"Error extracting tags with selector {selector}: {str(e)}")

        # If we still don't have tags, try the parent element as it might be a container
        if not tags:
            try:
                # Look for a container element that might have multiple tag elements
                tag_container = element.select_one(".tags, .categories, .topics")
                if tag_container:
                    # Try to find child elements that might be tags
                    tag_children = tag_container.select("a")
                    if tag_children:
                        for tag_child in tag_children:
                            tag = tag_child.get_text(strip=True)
                            if tag and tag not in tags:
                                tags.append(tag)
                    else:
                        # If no children found, the container might have comma-separated tags
                        tag_text = tag_container.get_text(strip=True)
                        if delimiter in tag_text:
                            split_tags = [t.strip() for t in tag_text.split(delimiter)]
                            tags.extend([t for t in split_tags if t])
            except Exception as e:
                self.logger.debug(f"Error extracting tags from container: {str(e)}")

        return tags

    def extract_description(self, element, selectors=None, max_length=MAX_DESCRIPTION_LENGTH) -> str:
        """Extract description/excerpt from an element.

        Args:
            element: BeautifulSoup element to extract from
            selectors: List of CSS selectors to try, in order of preference
                      Default selectors tried: .description, .excerpt, .summary,
                                             [class*="desc"], p
            max_length: Maximum length of description to return

        Returns:
            Description string or empty string if not found
        """
        if not selectors:
            selectors = [".description", ".excerpt", ".summary", '[class*="desc"]', '[class*="excerpt"]', '[itemprop="description"]', "p"]

        for selector in selectors:
            try:
                desc_elem = element.select_one(selector)
                if desc_elem:
                    description = desc_elem.get_text(strip=True)
                    if description:
                        # Truncate to max_length if necessary
                        if len(description) > max_length:
                            return description[:max_length] + "..."
                        return description
            except Exception as e:
                self.logger.debug(f"Error extracting description with selector {selector}: {str(e)}")

        # If no description found with specific selectors, try the first paragraph
        try:
            first_p = element.find("p")
            if first_p:
                description = first_p.get_text(strip=True)
                if description:
                    # Truncate to max_length if necessary
                    if len(description) > max_length:
                        return description[:max_length] + "..."
                    return description
        except Exception as e:
            self.logger.debug(f"Error extracting description from first paragraph: {str(e)}")

        return ""

    def extract_metadata_from_json_ld(self, html_content, property_mapping=None) -> List[Dict[str, Any]]:
        """Extract metadata from JSON-LD structured data in a page.

        Args:
            html_content: HTML content to extract from
            property_mapping: Dict mapping JSON-LD properties to output properties
                           Default: Maps standard Article schema.org properties

        Returns:
            List of dictionaries containing extracted metadata
        """
        if not property_mapping:
            property_mapping = {
                "headline": "title",
                "name": "title",
                "author": "author",
                "creator": "author",
                "datePublished": "date",
                "dateCreated": "date",
                "articleSection": "tags",
                "keywords": "tags",
                "category": "tags",
                "url": "url",
                "description": "description",
            }

        results = []

        try:
            soup = BeautifulSoup(html_content, "html.parser")
            json_ld_scripts = soup.find_all("script", type="application/ld+json")

            for script in json_ld_scripts:
                try:
                    data = json.loads(script.string)

                    # Handle both single items and arrays of items
                    items = data if isinstance(data, list) else [data]

                    for item in items:
                        # Skip non-article types if @type is specified
                        item_type = item.get("@type", "")
                        if item_type and not any(t in item_type for t in ["Article", "BlogPosting", "NewsArticle"]):
                            continue

                        result = {}

                        # Extract properties according to mapping
                        for json_prop, output_prop in property_mapping.items():
                            if json_prop in item:
                                # Handle special cases
                                if json_prop in ["author", "creator"]:
                                    # Author can be a string, object, or list
                                    author_data = item[json_prop]
                                    if isinstance(author_data, str):
                                        result[output_prop] = author_data
                                    elif isinstance(author_data, dict):
                                        result[output_prop] = author_data.get("name", "")
                                    elif isinstance(author_data, list) and author_data:
                                        # Take first author if list
                                        if isinstance(author_data[0], dict):
                                            result[output_prop] = author_data[0].get("name", "")
                                        else:
                                            result[output_prop] = str(author_data[0])
                                elif json_prop in ["keywords", "articleSection", "category"]:
                                    # Tags can be string, list, or comma-separated
                                    tags_data = item[json_prop]
                                    if isinstance(tags_data, str):
                                        if "," in tags_data:
                                            result[output_prop] = [t.strip() for t in tags_data.split(",")]
                                        else:
                                            result[output_prop] = [tags_data]
                                    elif isinstance(tags_data, list):
                                        result[output_prop] = tags_data
                                else:
                                    result[output_prop] = item[json_prop]

                        if result:
                            results.append(result)
                except Exception as e:
                    self.logger.debug(f"Error parsing JSON-LD script: {str(e)}")

        except Exception as e:
            self.logger.error(f"Error extracting JSON-LD metadata: {str(e)}")

        return results

    def _extract_data(self, items, fields=None):
        """Extract data from scraped items.

        Args:
            items: List of scraped items
            fields: Optional list of fields to extract

        Returns:
            List of dictionaries containing extracted data
        """
        raise NotImplementedError(f"{self.__class__.__name__} must implement _extract_data() method. " "This method should extract data from the scraped items and return a list of dictionaries.")
