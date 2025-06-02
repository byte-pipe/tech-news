"""
Reddit scraper module.

This module now uses the OptimizedRedditScraper for better performance
and cleaner code structure. The original RedditScraper class is maintained
for backward compatibility but delegates to the optimized version.
"""

import logging
from typing import Dict, List

from .reddit_optimized import OptimizedRedditScraper

logger = logging.getLogger(__name__)


class RedditScraper:
    """Reddit scraper that delegates to the optimized implementation.

    This class maintains the original interface for backward compatibility
    while using the optimized scraper internally.
    """

    SITE_NAME = "reddit"
    URL = "https://www.reddit.com/r/startups/top.json?t=day"  # Kept for compatibility
    SELECTOR = None  # Not used for JSON API
    SUBREDDITS = ["startups", "programming", "technology", "python", "MachineLearning"]
    TIME_FILTER = "day"

    def __init__(self, test_mode=False, test_output_dir=None):
        # Create an instance of the optimized scraper
        self._scraper = OptimizedRedditScraper(subreddits=self.SUBREDDITS, time_filter=self.TIME_FILTER, test_mode=test_mode, test_output_dir=test_output_dir)

        # Maintain compatibility with base scraper interface
        self.site_name = self.SITE_NAME
        self.test_mode = test_mode
        self.test_output_dir = test_output_dir
        self.logger = logger
        self.project_root = self._scraper.project_root

    def scrape(self, output_format: str = "markdown") -> List[Dict]:
        """Scrape Reddit using the optimized implementation.

        Args:
            output_format: Output format (markdown, json, csv)

        Returns:
            List of scraped posts
        """
        return self._scraper.scrape(output_format=output_format)

    def _extract_data(self, items, fields=None):
        """Process Reddit API data for backward compatibility.

        This method is maintained for compatibility but is not actively used
        by the optimized scraper.
        """
        if not items:
            return []

        # If the first "item" is actually the full JSON data structure
        if len(items) == 1 and hasattr(items[0], "get") and items[0].get("data", {}).get("children"):
            posts = items[0]["data"]["children"]
        else:
            posts = items  # Assume items are already post data objects

        data = []
        for post in posts:
            if isinstance(post, dict) and "data" in post:
                post_data = post["data"]
                data.append(
                    {
                        "title": post_data.get("title", ""),
                        "author": post_data.get("author", ""),
                        "score": str(post_data.get("score", 0)),
                        "comments": str(post_data.get("num_comments", 0)),
                        "subreddit": post_data.get("subreddit", ""),
                        "url": f"https://www.reddit.com{post_data.get('permalink', '')}",
                    }
                )

        return data

    def _remove_duplicates(self, data):
        """Remove duplicates for backward compatibility."""
        return self._scraper._remove_duplicates(data)


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = RedditScraper(test_mode=False)
    results = scraper.scrape()
    print(f"Scraped {len(results)} posts")
