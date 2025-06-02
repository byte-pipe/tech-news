import json
import logging
import os
import re
from datetime import datetime

from bs4 import BeautifulSoup

from .base import BaseScraper

logger = logging.getLogger(__name__)


class VentureBeatScraper(BaseScraper):
    SITE_NAME = "venturebeat"
    URL = "https://venturebeat.com/"
    SELECTOR = "article, .vb-card, .post, .entry, [data-article-id]"  # Fallback selectors

    # Category URLs to ensure we get comprehensive coverage
    CATEGORY_URLS = [
        "https://venturebeat.com/ai/",
        "https://venturebeat.com/games/",
        "https://venturebeat.com/business/",
        "https://venturebeat.com/data-infrastructure/",
        "https://venturebeat.com/security/",
    ]

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)
        self.logger = logging.getLogger(__name__)

    def _extract_data(self, items, fields=None):
        data = []
        try:
            self.logger.info(f"Processing {len(items)} VentureBeat articles")

            # Try extracting links directly from articles
            for item in items:
                try:
                    # Try multiple selectors for finding article links
                    links = item.select("a")

                    for link in links:
                        href = link.get("href", "")
                        # Skip non-article links
                        if not href or href.startswith("#") or "mailto:" in href:
                            continue

                        # Check if it looks like an article URL pattern
                        if "/202" in href and not href.endswith(".jpg") and not href.endswith(".png"):  # More specific URL pattern
                            # Ensure it's a full URL
                            if href.startswith("/"):
                                url = f"https://venturebeat.com{href}"
                            elif not href.startswith("http"):
                                url = f"https://venturebeat.com/{href}"
                            else:
                                url = href

                            # Only process VentureBeat URLs and skip home page
                            if "venturebeat.com" not in url or url == "https://venturebeat.com/":
                                continue

                            # Skip year-only URLs
                            if url.endswith("/2025/") or url.endswith("/2024/") or url.endswith("/2023/"):
                                continue

                            # Extract title - try the link text or look for a heading
                            title = link.text.strip()

                            # Clean up title - remove unwanted text
                            if title.startswith("Partner Content"):
                                title = title.replace("Partner Content", "").strip()

                            # If title is too short or empty, try to find a heading
                            if not title or len(title) < 10:  # Too short to be a title
                                heading = item.select_one("h1, h2, h3")
                                if heading:
                                    title = heading.text.strip()

                            # If we still don't have a good title, try to extract it from the URL
                            if not title or len(title) < 10:
                                # Extract the last part of the URL path
                                url_title = url.rstrip("/").split("/")[-1].replace("-", " ").replace("_", " ")
                                if len(url_title) > 10:
                                    title = url_title.title()  # Convert to title case

                            # Extract date from URL
                            date = ""
                            date_match = re.search(r"/(\d{4}/\d{2}/\d{2})/", url)
                            if date_match:
                                date_str = date_match.group(1).replace("/", "-")
                                date = date_str

                            # Extract author if available
                            author = ""
                            author_elem = item.select_one(".author, .byline, [rel='author']")
                            if author_elem:
                                author = author_elem.text.strip()
                                if author.startswith("By "):
                                    author = author[3:].strip()

                            # Extract description if available
                            description = ""
                            desc_elem = item.select_one("p.excerpt, .description, .summary")
                            if desc_elem:
                                description = desc_elem.text.strip()

                            # Extract category from URL if possible
                            categories = []
                            cat_match = re.search(r"venturebeat.com/([^/]+)/", url)
                            if cat_match:
                                cat = cat_match.group(1)
                                if cat not in ["2025", "2024", "2023"]:  # Skip year folders
                                    categories.append(cat)

                            # If we have a URL and either a title or date, add it
                            if url and (title or date):
                                article_data = {"title": title, "author": author, "description": description, "date": date, "categories": ", ".join(categories), "url": url}
                                data.append(article_data)
                except Exception as e:
                    self.logger.error(f"Error extracting article data: {str(e)}")

            self.logger.info(f"Extracted {len(data)} articles from VentureBeat")
        except Exception as e:
            self.logger.error(f"Error extracting VentureBeat data: {str(e)}")

        return data

    def scrape(self):
        """Custom scrape method for VentureBeat that scrapes both homepage and category pages."""
        try:
            data = []

            # First, try to extract articles from the main page
            html = self._get_page(self.url)
            if html:
                self.soup = BeautifulSoup(html, "html.parser")
                self._process_page(self.soup, "homepage", data)

            # Then, try each category page to ensure comprehensive coverage
            for cat_url in self.CATEGORY_URLS:
                try:
                    cat_name = cat_url.split("/")[-2] if cat_url.endswith("/") else cat_url.split("/")[-1]
                    self.logger.info(f"Fetching category page: {cat_name}")

                    cat_html = self._get_page(cat_url)
                    if cat_html:
                        cat_soup = BeautifulSoup(cat_html, "html.parser")
                        self._process_page(cat_soup, cat_name, data)
                except Exception as e:
                    self.logger.error(f"Error processing category {cat_url}: {str(e)}")

            # Additionally, try to extract structured data that might be embedded in the page
            try:
                scripts = self.soup.select('script[type="application/ld+json"]')
                for script in scripts:
                    try:
                        json_data = json.loads(script.string)
                        if isinstance(json_data, dict) and json_data.get("@type") == "Article":
                            article_data = self._extract_from_json_ld(json_data)
                            if article_data and article_data.get("url") not in [a.get("url") for a in data]:
                                data.append(article_data)
                        elif isinstance(json_data, list):
                            for item in json_data:
                                if isinstance(item, dict) and item.get("@type") == "Article":
                                    article_data = self._extract_from_json_ld(item)
                                    if article_data and article_data.get("url") not in [a.get("url") for a in data]:
                                        data.append(article_data)
                    except (json.JSONDecodeError, AttributeError) as e:
                        self.logger.debug(f"Error parsing JSON-LD: {str(e)}")
            except Exception as e:
                self.logger.error(f"Error extracting structured data: {str(e)}")

            # Save the data if any articles were found
            if not data:
                self.logger.error("No articles extracted from VentureBeat.")
                return

            # Remove duplicates based on URL
            unique_articles = {}
            for article in data:
                if article.get("url") and article["url"] not in unique_articles:
                    unique_articles[article["url"]] = article

            data = list(unique_articles.values())
            self.logger.info(f"Extracted {len(data)} unique articles from VentureBeat")

            # Save the data
            now = datetime.now()
            date_folder = now.strftime("%Y-%m-%d")
            timestamp = now.strftime("%Y%m%d-%H%M%S")

            # Create date folder if it doesn't exist
            folder_path = os.path.join(self.project_root, "data", date_folder)
            os.makedirs(folder_path, exist_ok=True)

            file_path = os.path.join(folder_path, f"{self.site_name}-{timestamp}.md")
            self._save_data(data, file_path)

        except Exception as e:
            self.logger.error(f"Error scraping VentureBeat: {str(e)}")

    def _process_page(self, soup, page_name, data):
        """Process a page and extract articles."""
        # Try multiple selectors to find articles
        for selector in ["article", "div.post", ".entry", ".story", "[data-article-id]", ".article", ".card", ".item", "div.post-wrapper", "li.article-item"]:
            articles = soup.select(selector)
            if articles:
                self.logger.info(f"Found {len(articles)} articles with selector {selector} on {page_name}")
                new_data = self._extract_data(articles)
                if new_data:
                    data.extend(new_data)
                    break

        # Fallback: try to find article links directly
        if not data:
            links = soup.select("a[href*='/venturebeat.com/']")
            links.extend(soup.select("a[href^='/20']"))  # Relative URLs for articles

            article_urls = set()
            for link in links:
                href = link.get("href", "")
                # Check if it looks like an article URL pattern
                if "/20" in href and not href.endswith(".jpg") and not href.endswith(".png"):
                    if href.startswith("/"):
                        full_url = f"https://venturebeat.com{href}"
                    elif not href.startswith("http"):
                        full_url = f"https://venturebeat.com/{href}"
                    else:
                        full_url = href
                    article_urls.add(full_url)

            self.logger.info(f"Found {len(article_urls)} article URLs directly on {page_name}")

            # Extract minimal data from links
            for url in article_urls:
                title = ""
                # Try to find the link element and extract title
                for link in soup.select(f"a[href*='{url.split('venturebeat.com/')[-1]}']"):
                    if link.text.strip() and len(link.text.strip()) > 15:  # Likely a title
                        title = link.text.strip()
                        break

                # Extract date from URL pattern like /2025/05/19/
                date = ""
                date_match = re.search(r"/(\d{4}/\d{2}/\d{2})/", url)
                if date_match:
                    date_str = date_match.group(1).replace("/", "-")
                    date = date_str

                if url and (title or date):
                    data.append({"title": title, "author": "", "description": "", "date": date, "categories": page_name if page_name != "homepage" else "", "url": url})

    def _extract_from_json_ld(self, json_data):
        """Extract article data from JSON-LD structured data."""
        try:
            # Extract required fields
            headline = json_data.get("headline", "")
            url = json_data.get("url", "")

            # Skip if required fields are missing
            if not headline or not url:
                return None

            # Extract optional fields
            author = ""
            author_data = json_data.get("author", {})
            if isinstance(author_data, dict):
                author = author_data.get("name", "")
            elif isinstance(author_data, list) and len(author_data) > 0:
                author = author_data[0].get("name", "")

            # Extract date
            date = ""
            date_str = json_data.get("datePublished", "")
            if date_str:
                try:
                    date = datetime.fromisoformat(date_str.replace("Z", "+00:00")).strftime("%Y-%m-%d")
                except (ValueError, AttributeError):
                    date = date_str

            # Extract description
            description = json_data.get("description", "")

            # Extract categories
            categories = []
            about = json_data.get("about", [])
            if isinstance(about, list):
                for item in about:
                    if isinstance(item, dict) and "name" in item:
                        categories.append(item["name"])

            return {"title": headline, "author": author, "description": description, "date": date, "categories": ", ".join(categories), "url": url}
        except Exception as e:
            self.logger.error(f"Error extracting from JSON-LD: {str(e)}")
            return None


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = VentureBeatScraper(test_mode=False)
    scraper.scrape()
