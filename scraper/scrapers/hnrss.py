"""
hnrss Scraper - HackerNews stories filtered by engagement via hnrss.org RSS feed.
Fetches front page stories with 100+ points for quality-filtered content.
"""

import logging
import os
import re
from datetime import datetime
from typing import Dict, List, Optional

import feedparser

from .base import BaseScraper

logger = logging.getLogger(__name__)


class HNRSSScraper(BaseScraper):
    """Scraper for HackerNews via hnrss.org RSS feed, filtered by points."""

    SITE_NAME = "hnrss"
    URL = "https://hnrss.org/frontpage?points=100&count=30"
    SELECTOR = ""  # Not used for RSS

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def _extract_data(self, items, fields=None):
        """Placeholder - actual extraction happens in scrape()."""
        return []

    def _parse_points_comments(self, description_html: str) -> tuple:
        """Extract points and comment count from RSS description HTML.

        The description contains lines like:
        <p>Points: 139</p>
        <p># Comments: 63</p>
        """
        points = 0
        comments = 0

        points_match = re.search(r"Points:\s*(\d+)", description_html)
        if points_match:
            points = int(points_match.group(1))

        comments_match = re.search(r"#\s*Comments:\s*(\d+)", description_html)
        if comments_match:
            comments = int(comments_match.group(1))

        return points, comments

    def _normalize_entry(self, entry) -> Optional[Dict]:
        """Convert an RSS feed entry to our standard format.

        Args:
            entry: A feedparser entry object

        Returns:
            Normalized dict or None if entry is invalid
        """
        title = getattr(entry, "title", "").strip()
        if not title:
            return None

        url = getattr(entry, "link", "").strip()
        if not url:
            return None

        # Discussion URL is in the 'comments' field of RSS
        discussion_url = getattr(entry, "comments", "")

        # Parse published date
        date_str = ""
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            try:
                date_str = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
            except Exception:
                date_str = datetime.now().strftime("%Y-%m-%d")
        else:
            date_str = datetime.now().strftime("%Y-%m-%d")

        # Extract points and comments from description
        description_html = getattr(entry, "description", "") or getattr(entry, "summary", "")
        points, comment_count = self._parse_points_comments(description_html)

        return {
            "title": title,
            "url": url,
            "description": title,
            "date": date_str,
            "score": points,
            "comments": comment_count,
            "discussion_url": discussion_url,
            "tags": ["hackernews", "hnrss"],
            "site_name": "hnrss",
            "fetched_at": datetime.now().isoformat(),
        }

    def scrape(self, output_format="json", **kwargs) -> List[Dict]:
        """Scrape HackerNews stories via hnrss.org RSS feed.

        Args:
            output_format: Output format (json, markdown, csv)

        Returns:
            List of story dictionaries
        """
        logger.info(f"Fetching hnrss feed from {self.url}")

        try:
            feed = feedparser.parse(self.url)

            if feed.bozo and not feed.entries:
                logger.error(f"Failed to parse RSS feed: {getattr(feed, 'bozo_exception', 'unknown error')}")
                return []

            if not feed.entries:
                logger.warning("No entries found in hnrss feed")
                return []

            logger.info(f"Got {len(feed.entries)} entries from hnrss feed")

            # Normalize entries
            stories = []
            for entry in feed.entries:
                normalized = self._normalize_entry(entry)
                if normalized:
                    stories.append(normalized)

            # Sort by score descending
            stories.sort(key=lambda x: x["score"], reverse=True)

            logger.info(f"Normalized {len(stories)} stories from hnrss feed")

            if not stories:
                logger.warning("No stories after normalization")
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
            self._save_data(stories, file_path, format=output_format)

            logger.info(f"Successfully saved {len(stories)} items from {self.site_name}")
            return stories

        except Exception as e:
            logger.error(f"Error scraping hnrss: {str(e)}")
            return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scraper = HNRSSScraper()
    stories = scraper.scrape(output_format="json")
    print(f"Fetched {len(stories)} stories")
