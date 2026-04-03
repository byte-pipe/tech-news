"""
HackerNews API Scraper - More reliable than HTML scraping.
Uses the official HackerNews Firebase API to fetch top stories.
"""

import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict, List, Optional

import requests
import urllib3

from .base import BaseScraper

# Disable urllib3 connection pool warnings
urllib3.disable_warnings()
logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)

logger = logging.getLogger(__name__)


class HackerNewsAPIScraper(BaseScraper):
    """Scraper for HackerNews using the official Firebase API."""

    SITE_NAME = "hackernews_api"
    URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
    SELECTOR = ""  # Not used for API

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)
        self.api_base = "https://hacker-news.firebaseio.com/v0"
        self.session = requests.Session()
        # Configure adapter with larger connection pool
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry

        adapter = HTTPAdapter(pool_connections=20, pool_maxsize=20, max_retries=Retry(total=3, backoff_factor=0.3))
        self.session.mount("https://", adapter)
        # Set a reasonable timeout for API requests
        self.timeout = 10

    def close(self):
        """Close the HTTP session and clean up resources."""
        # Close our specific session
        if hasattr(self, "session"):
            self.session.close()
        # Also call parent close method
        super().close()

    def _extract_data(self, items, fields=None):
        """
        Override the extract_data method from BaseScraper.

        This method is a placeholder since HackerNewsAPIScraper doesn't use the standard
        HTML parsing logic but instead uses the API directly in the scrape method.

        Args:
            items: List of items to extract data from
            fields: Optional fields to extract

        Returns:
            List of dictionaries with extracted data
        """
        # This is a placeholder implementation to satisfy the test requirement
        # The actual data extraction happens in the scrape method using the API
        return []

    def _fetch_story_details(self, story_id: int) -> Optional[Dict]:
        """Fetch individual story details from the API.

        Args:
            story_id: HackerNews story ID

        Returns:
            Story data dict or None if failed
        """
        try:
            url = f"{self.api_base}/item/{story_id}.json"
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()

            story = response.json()

            # Filter out deleted stories, jobs, polls, etc.
            if not story or story.get("type") != "story" or story.get("deleted"):
                return None

            # Must have a URL (skip self-posts for now)
            if not story.get("url"):
                return None

            return story

        except Exception as e:
            logger.warning(f"Failed to fetch story {story_id}: {str(e)}")
            return None

    def _parallel_fetch_stories(self, story_ids: List[int], max_workers: int = 20) -> List[Dict]:
        """Fetch multiple stories in parallel.

        Args:
            story_ids: List of HackerNews story IDs
            max_workers: Maximum number of concurrent requests

        Returns:
            List of story data dicts
        """
        stories = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all fetch tasks
            future_to_id = {executor.submit(self._fetch_story_details, story_id): story_id for story_id in story_ids}

            # Collect results as they complete
            for future in as_completed(future_to_id):
                story_id = future_to_id[future]
                try:
                    story = future.result()
                    if story:
                        stories.append(story)
                except Exception as e:
                    logger.warning(f"Exception fetching story {story_id}: {str(e)}")

        return stories

    def _normalize_story_data(self, story: Dict) -> Dict:
        """Convert API story data to our standard format.

        Args:
            story: Raw story data from HackerNews API

        Returns:
            Normalized story data
        """
        # Convert Unix timestamp to readable date
        timestamp = story.get("time", 0)
        date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d") if timestamp else ""

        return {
            "title": story.get("title", ""),
            "url": story.get("url", ""),
            "author": story.get("by", ""),
            "date": date_str,
            "score": story.get("score", 0),
            "comments": story.get("descendants", 0),
            "id": story.get("id", 0),
            "discussion_url": f"https://news.ycombinator.com/item?id={story.get('id', 0)}",
            "description": story.get("title", ""),  # Use title as description
            "tags": ["hackernews", "trending"],
            "site_name": "hackernews_api",
            "fetched_at": datetime.now().isoformat(),
        }

    def scrape(self, output_format="json", **kwargs) -> List[Dict]:
        """Scrape top stories from HackerNews API.

        Args:
            output_format: Output format (json, markdown, csv)
            **kwargs: Additional parameters (max_stories, min_score)

        Returns:
            List of story dictionaries
        """
        # Extract parameters from kwargs with defaults
        max_stories = kwargs.get("max_stories", 30)
        min_score = kwargs.get("min_score", 50)
        logger.info(f"Fetching top {max_stories} HackerNews stories via API")

        try:
            # Step 1: Get top story IDs
            logger.info("Fetching top story IDs...")
            response = self.session.get(self.url, timeout=self.timeout)
            response.raise_for_status()

            story_ids = response.json()
            if not story_ids:
                logger.error("No story IDs received from API")
                return []

            # Take top N story IDs (they're already sorted by HN)
            top_story_ids = story_ids[: max_stories * 2]  # Fetch extra to account for filtering
            logger.info(f"Got {len(top_story_ids)} story IDs, fetching details...")

            # Step 2: Fetch story details in parallel
            stories = self._parallel_fetch_stories(top_story_ids)
            logger.info(f"Successfully fetched {len(stories)} story details")

            # Step 3: Normalize and filter
            normalized_stories = []
            for story in stories:
                normalized = self._normalize_story_data(story)

                # Apply minimum score filter
                if normalized["score"] >= min_score:
                    normalized_stories.append(normalized)

            # Step 4: Sort by score (descending) and limit
            normalized_stories.sort(key=lambda x: x["score"], reverse=True)
            final_stories = normalized_stories[:max_stories]

            logger.info(f"Filtered to {len(final_stories)} stories (min_score: {min_score})")

            if not final_stories:
                logger.warning("No stories met the filtering criteria")
                return []

            # Log some stats
            top_score = final_stories[0]["score"] if final_stories else 0
            avg_score = sum(s["score"] for s in final_stories) / len(final_stories) if final_stories else 0
            logger.info(f"Score range: {top_score} (top) to {final_stories[-1]['score']} (bottom), avg: {avg_score:.1f}")

            # Step 5: Save results (BaseScraper handles saving logic)
            now = datetime.now()
            date_folder = now.strftime("%Y-%m-%d")

            # Determine folder path based on test mode
            if self.test_mode and self.test_output_dir:
                folder_path = self.test_output_dir
                logger.info(f"TEST MODE: Using test output directory: {folder_path}")
            else:
                folder_path = os.path.join(self.project_root, "data", date_folder)

            # Create folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Use the appropriate file extension based on the output format
            if output_format == "json":
                file_extension = ".json"
            elif output_format == "csv":
                file_extension = ".csv"
            else:  # default to markdown
                file_extension = ".md"

            file_path = os.path.join(folder_path, f"{self.site_name}{file_extension}")
            self._save_data(final_stories, file_path, format=output_format)

            logger.info(f"Successfully extracted and saved {len(final_stories)} items from {self.site_name} in {output_format} format")
            return final_stories

        except Exception as e:
            logger.error(f"Error scraping HackerNews API: {str(e)}")
            return None


if __name__ == "__main__":
    # Test the scraper
    pass

    logging.basicConfig(level=logging.INFO)

    scraper = HackerNewsAPIScraper()
    stories = scraper.scrape(output_format="json", max_stories=10)

    print(f"\nFetched {len(stories)} stories:")
    for i, story in enumerate(stories[:5], 1):
        print(f"{i}. {story['title']} (Score: {story['score']})")
