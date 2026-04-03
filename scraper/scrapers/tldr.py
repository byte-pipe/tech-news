"""
TLDR Newsletter Scraper - Human-curated daily tech picks from tldr.tech.
Extracts articles with their external URLs and TLDR summaries.
"""

import json
import logging
import os
import re
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup

from .base import BaseScraper

logger = logging.getLogger(__name__)


class TLDRScraper(BaseScraper):
    """Scraper for TLDR newsletter at tldr.tech."""

    SITE_NAME = "tldr"
    URL = "https://tldr.tech/tech"
    SELECTOR = ""  # Not used - custom extraction

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def _extract_data(self, items, fields=None):
        """Placeholder - actual extraction happens in scrape()."""
        return []

    @staticmethod
    def _strip_utm_params(url: str) -> str:
        """Remove UTM tracking parameters from a URL."""
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        filtered = {k: v for k, v in params.items() if not k.startswith("utm_")}
        clean_query = urlencode(filtered, doseq=True)
        return urlunparse(parsed._replace(query=clean_query))

    def _is_external_url(self, url: str) -> bool:
        """Check if URL points outside tldr.tech."""
        if not url:
            return False
        parsed = urlparse(url)
        host = parsed.hostname or ""
        return bool(host) and "tldr.tech" not in host

    def _extract_from_next_data(self, html: str) -> List[Dict]:
        """Try extracting articles from Next.js __NEXT_DATA__ JSON."""
        soup = BeautifulSoup(html, "html.parser")
        script_tag = soup.select_one("script#__NEXT_DATA__")
        if not script_tag or not script_tag.string:
            return []

        try:
            data = json.loads(script_tag.string)
        except json.JSONDecodeError:
            return []

        # Navigate common Next.js paths
        page_props = data.get("props", {}).get("pageProps", {})

        articles = []
        # Look for articles in various possible keys
        for key in ["articles", "stories", "newsletter", "items", "links", "posts"]:
            items = page_props.get(key, [])
            if isinstance(items, list) and items:
                for item in items:
                    if not isinstance(item, dict):
                        continue
                    title = item.get("title", "").strip()
                    url = item.get("url", "") or item.get("link", "") or item.get("href", "")
                    url = self._strip_utm_params(url)
                    if title and url and self._is_external_url(url):
                        description = item.get("description", "") or item.get("summary", "") or item.get("snippet", "")
                        category = item.get("category", "") or item.get("tag", "") or item.get("section", "")
                        tags = [t for t in ["tldr", category.lower()] if t]
                        articles.append(
                            {
                                "title": title,
                                "url": url,
                                "description": description.strip() if description else title,
                                "tags": tags,
                                "date": datetime.now().strftime("%Y-%m-%d"),
                                "site_name": "tldr",
                            }
                        )

        return articles

    def _extract_from_html(self, html: str) -> List[Dict]:
        """Extract articles from HTML content using CSS selectors."""
        soup = BeautifulSoup(html, "html.parser")
        articles = []

        # TLDR uses article blocks with header links and description text
        # Try multiple selector strategies
        # Strategy 1: Look for article containers with external links
        for article_div in soup.select("article, div.article, div.newsletter-item, div[class*='article'], div[class*='post']"):
            link = article_div.select_one("a[href]")
            if not link:
                continue
            url = link.get("href", "")
            url = self._strip_utm_params(url)
            if not self._is_external_url(url):
                continue

            title = link.get_text(strip=True)
            if not title:
                heading = article_div.select_one("h2, h3, h4")
                title = heading.get_text(strip=True) if heading else ""

            if not title:
                continue

            # Get description from paragraph
            desc_elem = article_div.select_one("p")
            description = desc_elem.get_text(strip=True) if desc_elem else title

            articles.append(
                {
                    "title": title,
                    "url": url,
                    "description": description,
                    "tags": ["tldr"],
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "site_name": "tldr",
                }
            )

        # Strategy 2: If no articles found, look for all external links with context
        if not articles:
            seen_urls = set()
            for link in soup.select("a[href]"):
                url = link.get("href", "")
                url = self._strip_utm_params(url)
                if not self._is_external_url(url):
                    continue
                if url in seen_urls:
                    continue

                title = link.get_text(strip=True)
                if not title or len(title) < 10:
                    continue

                # Skip navigation/footer links
                parent = link.parent
                if parent and parent.name in ("nav", "footer", "header"):
                    continue

                seen_urls.add(url)

                # Get surrounding text as description
                description = ""
                next_sibling = link.find_next_sibling("p") if link.parent else None
                if next_sibling:
                    description = next_sibling.get_text(strip=True)

                if not description and parent:
                    next_p = parent.find_next("p")
                    if next_p:
                        description = next_p.get_text(strip=True)

                articles.append(
                    {
                        "title": title,
                        "url": url,
                        "description": description if description else title,
                        "tags": ["tldr"],
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "site_name": "tldr",
                    }
                )

        return articles

    def scrape(self, output_format="json", **kwargs) -> List[Dict]:
        """Scrape articles from TLDR newsletter.

        Args:
            output_format: Output format (json, markdown, csv)

        Returns:
            List of article dictionaries
        """
        logger.info(f"Fetching TLDR newsletter from {self.url}")

        try:
            html = self._get_page(self.url)
            if not html:
                logger.error("Failed to fetch TLDR page")
                return []

            # Try __NEXT_DATA__ first (structured data)
            articles = self._extract_from_next_data(html)

            # Fall back to HTML parsing
            if not articles:
                logger.info("No __NEXT_DATA__ found, falling back to HTML extraction")
                articles = self._extract_from_html(html)

            if not articles:
                logger.warning("No articles extracted from TLDR")
                return []

            # Deduplicate by URL
            seen_urls = set()
            unique_articles = []
            for article in articles:
                if article["url"] not in seen_urls:
                    seen_urls.add(article["url"])
                    unique_articles.append(article)
            articles = unique_articles

            logger.info(f"Extracted {len(articles)} articles from TLDR")

            # Save results
            now = datetime.now()
            date_folder = now.strftime("%Y-%m-%d")

            if self.test_mode and self.test_output_dir:
                folder_path = self.test_output_dir
            else:
                folder_path = os.path.join(self.project_root, "data", date_folder)

            os.makedirs(folder_path, exist_ok=True)

            if output_format == "json":
                file_extension = ".json"
            elif output_format == "csv":
                file_extension = ".csv"
            else:
                file_extension = ".md"

            file_path = os.path.join(folder_path, f"{self.site_name}{file_extension}")
            self._save_data(articles, file_path, format=output_format)

            logger.info(f"Successfully saved {len(articles)} items from {self.site_name}")
            return articles

        except Exception as e:
            logger.error(f"Error scraping TLDR: {str(e)}")
            return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scraper = TLDRScraper()
    articles = scraper.scrape(output_format="json")
    print(f"Fetched {len(articles)} articles")
