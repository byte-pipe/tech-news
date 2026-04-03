import json
import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict, List, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from scraper.core.config import get_config
from scraper.core.data_organizer import DataOrganizer

logger = logging.getLogger(__name__)


class RedditAPIClient:
    """Optimized Reddit API client with connection pooling and retry logic."""

    BASE_URL = "https://www.reddit.com"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    def __init__(self, timeout: int = 30, max_retries: int = 3):
        self.timeout = timeout
        self.session = self._create_session(max_retries)

    def _create_session(self, max_retries: int) -> requests.Session:
        """Create a session with retry strategy and connection pooling."""
        session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(total=max_retries, status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["HEAD", "GET", "OPTIONS"], backoff_factor=1)

        adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=10, pool_maxsize=10)

        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Set headers
        session.headers.update({"User-Agent": self.USER_AGENT, "Accept": "application/json"})

        return session

    def fetch_subreddit_posts(self, subreddit: str, sort: str = "top", time_filter: str = "day", limit: int = 100) -> Optional[Dict]:
        """Fetch posts from a subreddit using the JSON API.

        Args:
            subreddit: Name of the subreddit
            sort: Sort method (hot, new, top, rising)
            time_filter: Time filter for top/controversial (hour, day, week, month, year, all)
            limit: Maximum number of posts to fetch (max 100)

        Returns:
            Dict with Reddit API response or None if error
        """
        url = f"{self.BASE_URL}/r/{subreddit}/{sort}.json"
        params = {"limit": min(limit, 100)}

        if sort in ["top", "controversial"]:
            params["t"] = time_filter

        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching r/{subreddit}: {str(e)}")
            return None

    def close(self):
        """Close the session."""
        self.session.close()


class OptimizedRedditScraper:
    """Optimized Reddit scraper that directly works with the JSON API."""

    SITE_NAME = "reddit"
    DEFAULT_SUBREDDITS = ["startups", "programming", "technology", "python", "MachineLearning", "datascience", "webdev", "entrepreneur", "worldnews", "geopolitics"]

    def __init__(self, subreddits: Optional[List[str]] = None, time_filter: str = "day", test_mode: bool = False, test_output_dir: Optional[str] = None):
        self.site_name = self.SITE_NAME
        self.subreddits = subreddits or self.DEFAULT_SUBREDDITS
        self.time_filter = time_filter
        self.test_mode = test_mode
        self.test_output_dir = test_output_dir
        config = get_config()
        self.project_root = str(config.project_root)
        self.client = RedditAPIClient()
        self.logger = logger

    def extract_post_data(self, post_data: Dict) -> Dict:
        """Extract relevant data from a Reddit post.

        Args:
            post_data: Raw post data from Reddit API

        Returns:
            Dict with extracted post information
        """
        return {
            "title": post_data.get("title", ""),
            "author": post_data.get("author", "[deleted]"),
            "score": post_data.get("score", 0),
            "comments": post_data.get("num_comments", 0),
            "subreddit": post_data.get("subreddit", ""),
            "url": f"{RedditAPIClient.BASE_URL}{post_data.get('permalink', '')}",
            "created_utc": post_data.get("created_utc", 0),
            "upvote_ratio": post_data.get("upvote_ratio", 0),
            "is_self": post_data.get("is_self", False),
            "link_flair_text": post_data.get("link_flair_text", ""),
            "domain": post_data.get("domain", ""),
            "external_url": post_data.get("url", "") if not post_data.get("is_self") else "",
        }

    def fetch_subreddit_concurrent(self, subreddit: str) -> List[Dict]:
        """Fetch posts from a single subreddit.

        Args:
            subreddit: Name of the subreddit

        Returns:
            List of extracted post data
        """
        self.logger.info(f"Fetching posts from r/{subreddit}")

        response = self.client.fetch_subreddit_posts(subreddit, sort="top", time_filter=self.time_filter)

        if not response or "data" not in response:
            return []

        posts = response["data"].get("children", [])
        extracted_posts = []

        for post in posts:
            if post.get("kind") == "t3" and "data" in post:
                extracted_posts.append(self.extract_post_data(post["data"]))

        self.logger.info(f"Extracted {len(extracted_posts)} posts from r/{subreddit}")
        return extracted_posts

    def scrape(self, output_format: str = "json") -> List[Dict]:
        """Scrape Reddit posts from configured subreddits.

        Args:
            output_format: Output format (json, markdown, csv)

        Returns:
            List of all scraped posts
        """
        try:
            all_posts = []

            # Use ThreadPoolExecutor for concurrent fetching
            with ThreadPoolExecutor(max_workers=5) as executor:
                future_to_subreddit = {executor.submit(self.fetch_subreddit_concurrent, sub): sub for sub in self.subreddits}

                for future in as_completed(future_to_subreddit):
                    subreddit = future_to_subreddit[future]
                    try:
                        posts = future.result()
                        all_posts.extend(posts)
                    except Exception as e:
                        self.logger.error(f"Error processing r/{subreddit}: {str(e)}")

            # Remove duplicates based on URL
            unique_posts = self._remove_duplicates(all_posts)

            if not unique_posts:
                self.logger.warning("No Reddit posts extracted")
                return []

            # Sort by score (descending)
            unique_posts.sort(key=lambda x: x.get("score", 0), reverse=True)

            # Save the data
            self._save_data(unique_posts, output_format)

            return unique_posts

        except Exception as e:
            self.logger.error(f"Error during Reddit scraping: {str(e)}")
            return None
        finally:
            self.client.close()

    def _remove_duplicates(self, posts: List[Dict]) -> List[Dict]:
        """Remove duplicate posts based on URL.

        Args:
            posts: List of post dictionaries

        Returns:
            List with duplicates removed
        """
        seen_urls = set()
        unique_posts = []

        for post in posts:
            url = post.get("url", "")
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_posts.append(post)

        self.logger.info(f"Removed {len(posts) - len(unique_posts)} duplicate posts")
        return unique_posts

    def _save_data(self, data: List[Dict], output_format: str) -> str:
        """Save scraped data to file.

        Args:
            data: List of post dictionaries
            output_format: Output format (json, markdown, csv)

        Returns:
            Path to saved file
        """
        now = datetime.now()
        date_folder = now.strftime("%Y-%m-%d")

        # Determine output directory
        if self.test_mode and self.test_output_dir:
            folder_path = self.test_output_dir
        else:
            data_organizer = DataOrganizer()
            try:
                # Only create the raw directory for scraped data
                folder_path = data_organizer.ensure_directory(date_folder, "raw")
            except Exception as e:
                self.logger.error(f"Failed to create organized directory structure: {str(e)}")
                # Fallback to basic directory creation
                folder_path = os.path.join(self.project_root, "data", date_folder)
                self.logger.warning(f"Using fallback raw data directory: {folder_path}")

        os.makedirs(folder_path, exist_ok=True)

        # Determine file extension
        extensions = {"json": ".json", "csv": ".csv", "markdown": ".md"}
        file_extension = extensions.get(output_format, ".json")

        file_path = os.path.join(folder_path, f"{self.SITE_NAME}{file_extension}")

        # Save based on format
        if output_format == "json":
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        elif output_format == "csv":
            self._save_as_csv(data, file_path)
        else:  # markdown
            self._save_as_markdown(data, file_path)

        self.logger.info(f"Saved {len(data)} Reddit posts to {file_path}")
        return file_path

    def _save_as_csv(self, data: List[Dict], file_path: str):
        """Save data as CSV."""
        import csv

        if not data:
            return

        # Define the fields we want in the CSV
        fieldnames = ["title", "author", "score", "comments", "subreddit", "url", "upvote_ratio", "link_flair_text", "domain"]

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(data)

    def _save_as_markdown(self, data: List[Dict], file_path: str):
        """Save data as markdown."""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Reddit Top Posts - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"*Scraped {len(data)} posts from: {', '.join(self.subreddits)}*\n\n")

            for i, post in enumerate(data, 1):
                f.write(f"## {i}. {post['title']}\n\n")
                f.write(f"- **Subreddit**: r/{post['subreddit']}\n")
                f.write(f"- **Author**: u/{post['author']}\n")
                f.write(f"- **Score**: {post['score']} points ({post.get('upvote_ratio', 0):.0%} upvoted)\n")
                f.write(f"- **Comments**: {post['comments']}\n")
                if post.get("link_flair_text"):
                    f.write(f"- **Flair**: {post['link_flair_text']}\n")
                if post.get("external_url"):
                    f.write(f"- **External Link**: {post['external_url']}\n")
                f.write(f"- **Reddit URL**: {post['url']}\n\n")


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Run the scraper
    scraper = OptimizedRedditScraper()
    results = scraper.scrape(output_format="json")
    print(f"Scraped {len(results)} total posts")
