"""
Multi-source RSS News Feed Scraper.

Fetches RSS feeds from major news outlets covering tech, science, engineering,
AI, world news, and geopolitics. Runs feeds in parallel via ThreadPoolExecutor.
"""

import hashlib
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict, List, Optional

import feedparser

from .base import BaseScraper

logger = logging.getLogger(__name__)

# RSS feed sources grouped by category
RSS_FEEDS = {
    # Tech / AI
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index",
    "Wired": "https://www.wired.com/feed/rss",
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "MIT Tech Review": "https://www.technologyreview.com/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    # Science / Engineering
    "Nature": "https://www.nature.com/nature.rss",
    "IEEE Spectrum": "https://spectrum.ieee.org/feeds/feed.rss",
    "New Scientist": "https://www.newscientist.com/section/news/feed/",
    # World / Geopolitics
    "Reuters": "https://www.reutersagency.com/feed/",
    "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
    "Guardian": "https://www.theguardian.com/world/rss",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "AP News": "https://rsshub.app/apnews/topics/apf-topnews",
    "NPR": "https://feeds.npr.org/1001/rss.xml",
    "Economist": "https://www.economist.com/international/rss.xml",
}

MAX_WORKERS = 6
MAX_ITEMS_PER_FEED = 15


def _strip_html(text: str) -> str:
    """Remove HTML tags from a string."""
    if not text:
        return ""
    return re.sub(r"<[^>]+>", "", text).strip()


def _title_hash(title: str) -> str:
    """MD5 hash of a normalized title for deduplication."""
    normalized = re.sub(r"\s+", " ", title.lower().strip())
    return hashlib.md5(normalized.encode("utf-8")).hexdigest()


class NewsFeedScraper(BaseScraper):
    """Scraper for multiple RSS news feeds in parallel."""

    SITE_NAME = "newsfeed"
    URL = "https://feeds.bbci.co.uk/news/rss.xml"  # placeholder for base class
    SELECTOR = ""  # Not used for RSS

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def _extract_data(self, items, fields=None):
        """Placeholder - actual extraction happens in scrape()."""
        return []

    def _normalize_entry(self, entry, source_name: str) -> Optional[Dict]:
        """Convert an RSS feed entry to our standard format.

        Args:
            entry: A feedparser entry object
            source_name: Name of the feed source (e.g. "BBC", "Ars Technica")

        Returns:
            Normalized dict or None if entry is invalid
        """
        title = _strip_html(getattr(entry, "title", "")).strip()
        if not title:
            return None

        url = getattr(entry, "link", "").strip()
        if not url:
            return None

        # Parse description
        raw_desc = getattr(entry, "summary", "") or getattr(entry, "description", "")
        description = _strip_html(raw_desc)
        if len(description) > 500:
            description = description[:497] + "..."

        # Parse published date
        date_str = ""
        for date_attr in ("published_parsed", "updated_parsed"):
            parsed = getattr(entry, date_attr, None)
            if parsed:
                try:
                    date_str = datetime(*parsed[:6]).strftime("%Y-%m-%d")
                    break
                except Exception:
                    pass
        if not date_str:
            date_str = datetime.now().strftime("%Y-%m-%d")

        # Extract tags/categories from feed entry
        tags = [source_name.lower().replace(" ", "-")]
        if hasattr(entry, "tags"):
            for tag in entry.tags[:3]:
                term = getattr(tag, "term", "")
                if term:
                    tags.append(term.lower().strip())

        return {
            "title": title,
            "url": url,
            "description": description or title,
            "date": date_str,
            "score": 0,
            "tags": tags,
            "source": source_name,
            "site_name": "newsfeed",
            "fetched_at": datetime.now().isoformat(),
        }

    def _fetch_single_feed(self, source_name: str, feed_url: str) -> List[Dict]:
        """Fetch and parse a single RSS feed.

        Args:
            source_name: Human-readable name of the source
            feed_url: URL of the RSS feed

        Returns:
            List of normalized entry dicts
        """
        try:
            feed = feedparser.parse(feed_url)

            if feed.bozo and not feed.entries:
                logger.warning(f"Failed to parse {source_name}: {getattr(feed, 'bozo_exception', 'unknown')}")
                return []

            items = []
            for entry in feed.entries[:MAX_ITEMS_PER_FEED]:
                normalized = self._normalize_entry(entry, source_name)
                if normalized:
                    items.append(normalized)

            logger.info(f"Got {len(items)} items from {source_name}")
            return items

        except Exception as e:
            logger.warning(f"Error fetching {source_name}: {e}")
            return []

    def scrape(self, output_format="json", **kwargs) -> Optional[List[Dict]]:
        """Scrape all RSS feeds in parallel.

        Args:
            output_format: Output format (json, markdown, csv)

        Returns:
            List of story dictionaries, or None on complete failure
        """
        logger.info(f"Fetching {len(RSS_FEEDS)} RSS feeds with {MAX_WORKERS} workers")

        all_items = []

        try:
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = {executor.submit(self._fetch_single_feed, name, url): name for name, url in RSS_FEEDS.items()}

                for future in as_completed(futures):
                    source_name = futures[future]
                    try:
                        items = future.result()
                        all_items.extend(items)
                    except Exception as e:
                        logger.warning(f"Feed {source_name} raised exception: {e}")

            if not all_items:
                logger.warning("No items collected from any feed")
                return []

            # Deduplicate by title hash
            seen_hashes = set()
            unique_items = []
            for item in all_items:
                h = _title_hash(item["title"])
                if h not in seen_hashes:
                    seen_hashes.add(h)
                    unique_items.append(item)

            # Sort by date descending (newest first)
            unique_items.sort(key=lambda x: x["date"], reverse=True)

            logger.info(f"Collected {len(unique_items)} unique items from {len(RSS_FEEDS)} feeds (before dedup: {len(all_items)})")

            if not unique_items:
                logger.warning("No items after deduplication")
                return []

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
            self._save_data(unique_items, file_path, format=output_format)

            logger.info(f"Successfully saved {len(unique_items)} items from {self.site_name}")
            return unique_items

        except Exception as e:
            logger.error(f"Error scraping news feeds: {str(e)}")
            return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scraper = NewsFeedScraper()
    stories = scraper.scrape(output_format="json")
    if stories:
        print(f"Fetched {len(stories)} stories")
    else:
        print("No stories fetched")
