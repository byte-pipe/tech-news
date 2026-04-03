import json
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional

from bs4 import BeautifulSoup

from .base import BaseScraper

logger = logging.getLogger(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


class HackerNoonScraper(BaseScraper):
    SITE_NAME = "hackernoon"
    URL = "https://hackernoon.com"
    SELECTOR = "article.story-card"
    main_selector = "script#__NEXT_DATA__"  # This contains the JSON data

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def _extract_data(self, items, fields=None):
        """Extract data from HackerNoon items.

        This method is implemented to override the base class method, but
        in practice we use the custom scrape() implementation for HackerNoon
        since it requires special JSON handling.
        """
        data = []

        try:
            # Look for the script tag with JSON data
            for item in items:
                if item.name == "script" and "id" in item.attrs and item["id"] == "__NEXT_DATA__":
                    # Parse the JSON data
                    json_data = json.loads(item.string)

                    # Navigate to the articles data
                    articles = json_data.get("props", {}).get("pageProps", {}).get("stories", [])

                    if not articles:
                        self.logger.warning("No articles found in JSON data")
                        continue

                    # Process all articles
                    for article in articles:
                        # Extract article data
                        title = article.get("title", "").strip()
                        author = article.get("profile", {}).get("displayName", "").strip()
                        read_time = article.get("readTime", "")

                        # Parse date with error handling
                        date = ""
                        try:
                            date = datetime.fromtimestamp(article.get("publishedAt", 0)).strftime("%Y-%m-%d")
                        except Exception as e:
                            self.logger.warning(f"Failed to parse date: {e}")
                            date = str(article.get("publishedAt", ""))

                        # Get tags
                        tags = [tag.strip() for tag in article.get("tags", [])]
                        url = f"https://hackernoon.com/{article.get('slug', '')}"

                        data.append({"title": title, "author": author, "read_time": read_time, "date": date, "tags": ", ".join(tags), "url": url})
        except Exception as e:
            self.logger.error(f"Error extracting data from HackerNoon: {str(e)}")

        return data

    def parse_item(self, item: BeautifulSoup) -> Optional[List[Dict[str, str]]]:
        """Parse a HackerNoon article item.

        Note: This method now returns a list of articles, not just one.
        """
        try:
            # Extract the JSON data from the script tag
            json_data = json.loads(item.string)

            # Navigate to the articles data
            articles = json_data.get("props", {}).get("pageProps", {}).get("stories", [])

            if not articles:
                self.logger.warning("No articles found in JSON data")
                return None

            result = []
            # Process all articles
            for article in articles:
                # Extract article data
                title = article.get("title", "").strip()
                author = article.get("profile", {}).get("displayName", "").strip()
                read_time = article.get("readTime", "")
                date = datetime.fromtimestamp(article.get("publishedAt", 0)).strftime("%Y-%m-%d")
                tags = [tag.strip() for tag in article.get("tags", [])]
                url = f"https://hackernoon.com/{article.get('slug', '')}"

                result.append({"title": title, "author": author, "read_time": read_time, "date": date, "tags": ", ".join(tags), "url": url})

            return result

        except (json.JSONDecodeError, KeyError, IndexError) as e:
            self.logger.error(f"Error parsing article: {str(e)}")
            return None

    def get_items(self) -> List[BeautifulSoup]:
        """Get all article items from the page."""
        try:
            # Find the script tag containing the JSON data
            script_tag = self.soup.select_one(self.main_selector)
            if not script_tag:
                self.logger.error("Could not find JSON data script tag")
                return []

            return [script_tag]

        except Exception as e:
            self.logger.error(f"Error getting items: {str(e)}")
            return []

    def _extract_title(self, article):
        """Extract title with fallbacks."""
        if "title" in article:
            return article.get("title", "").strip()
        elif "headline" in article:
            return article.get("headline", "").strip()
        elif "name" in article:
            return article.get("name", "").strip()
        return ""

    def _extract_author(self, article):
        """Extract author with multiple paths."""
        if "profile" in article and isinstance(article.get("profile"), dict):
            return article.get("profile", {}).get("displayName", "").strip()
        elif "author" in article and isinstance(article.get("author"), dict):
            return article.get("author", {}).get("name", "").strip()
        elif "user" in article and isinstance(article.get("user"), dict):
            return article.get("user", {}).get("name", "").strip()
        elif "authorName" in article:
            return article.get("authorName", "").strip()
        return ""

    def _extract_read_time(self, article):
        """Extract read time with fallbacks."""
        if "readTime" in article:
            return article.get("readTime", "")
        elif "readTimeMinutes" in article:
            return f"{article.get('readTimeMinutes', '')} min"
        elif "minutesToRead" in article:
            return f"{article.get('minutesToRead', '')} min"
        return ""

    def _extract_date(self, article):
        """Extract and format date from various possible fields."""
        date_fields = ["publishedAt", "dateAdded", "publishDate", "date"]

        for field in date_fields:
            if field not in article:
                continue

            date_val = article.get(field, 0)

            try:
                if isinstance(date_val, str):
                    # Try ISO format first
                    try:
                        return datetime.fromisoformat(date_val.replace("Z", "+00:00")).strftime("%Y-%m-%d")
                    except ValueError:
                        # Try parsing as timestamp string
                        return datetime.fromtimestamp(float(date_val)).strftime("%Y-%m-%d")
                elif isinstance(date_val, (int, float)):
                    return datetime.fromtimestamp(date_val).strftime("%Y-%m-%d")
            except Exception as e:
                self.logger.warning(f"Failed to parse {field}: {e}")

        return ""

    def _extract_tags(self, article):
        """Extract tags with fallbacks."""
        if "tags" in article and isinstance(article.get("tags"), list):
            return [tag.strip() for tag in article.get("tags", [])]
        elif "categories" in article and isinstance(article.get("categories"), list):
            return [cat.strip() for cat in article.get("categories", [])]
        return []

    def _extract_url(self, article):
        """Extract URL with fallbacks and ensure absolute URL."""
        url = ""
        if "slug" in article:
            url = f"https://hackernoon.com/{article.get('slug', '')}"
        elif "canonical" in article:
            url = article.get("canonical", "")
        elif "url" in article:
            url = article.get("url", "")
        elif "href" in article:
            url = article.get("href", "")

        # Add absolute URL if relative
        if url and not url.startswith("http"):
            url = f"https://hackernoon.com{url if url.startswith('/') else '/' + url}"

        return url

    def _find_articles_in_json(self, json_data):
        """Find articles in various possible JSON structures."""

        # Debug: Log the top-level JSON structure
        self.logger.info(f"HackerNoon JSON top-level keys: {list(json_data.keys())}")

        # Check for different possible paths to articles
        props = json_data.get("props", {})
        self.logger.info(f"Props keys: {list(props.keys())}")

        page_props = props.get("pageProps", {})
        self.logger.info(f"PageProps keys: {list(page_props.keys())}")

        # Based on the logs, we can see the structure has 'data' key in pageProps
        data = page_props.get("data", {})
        if data:
            self.logger.info(f"Data keys: {list(data.keys())}")

        # NEW Path: Check if data contains stories or a relevant articles list
        if isinstance(data, dict):
            # Check if there's a top stories or featured stories key
            for possible_key in ["topStories", "featuredStories", "stories", "articles", "latestStories"]:
                if possible_key in data:
                    possible_articles = data.get(possible_key, [])
                    if possible_articles and len(possible_articles) > 0:
                        self.logger.info(f"Found {len(possible_articles)} articles in pageProps.data.{possible_key}")
                        return possible_articles

            # If still no articles, try looking at other keys in data
            article_lists = []
            for key, value in data.items():
                if isinstance(value, list) and len(value) > 0 and isinstance(value[0], dict):
                    # This might be a list of articles - log it for inspection
                    self.logger.info(f"Potential articles in pageProps.data.{key}: {len(value)} items")
                    # Check if items look like articles (have title, etc.)
                    sample = value[0]
                    if any(k in sample for k in ["title", "headline", "slug", "url"]):
                        self.logger.info(f"Found likely articles in pageProps.data.{key}")
                        self.logger.info(f"Sample keys for {key}: {list(sample.keys())}")
                        article_lists.append(value)

            # Combine all article lists if found
            if article_lists:
                self.logger.info(f"Combining {len(article_lists)} article lists")
                all_articles = []
                for article_list in article_lists:
                    all_articles.extend(article_list)
                return all_articles

        # The original paths as fallback
        # Path 1: Original path
        stories = page_props.get("stories", [])
        if stories:
            self.logger.info(f"Found {len(stories)} stories in pageProps.stories")
            return stories

        # Path 2: Try homepage structure
        home_articles = page_props.get("homepage", {}).get("articles", [])
        if home_articles:
            self.logger.info(f"Found {len(home_articles)} articles in pageProps.homepage.articles")
            return home_articles

        # Path 3: Try mainFeed structure
        main_feed = page_props.get("mainFeed", [])
        if main_feed:
            self.logger.info(f"Found {len(main_feed)} articles in pageProps.mainFeed")
            return main_feed

        self.logger.error("Could not find articles in any expected JSON path")
        return []

    def scrape(self):
        """Custom scrape method for HackerNoon to handle JSON-based articles."""
        try:
            html = self._get_page(self.url)
            if not html:
                self.logger.error("No HTML content fetched.")
                return

            self.soup = BeautifulSoup(html, "html.parser")
            items = self.get_items()
            if not items:
                self.logger.error("No items found in HackerNoon JSON data.")
                return

            # Parse the JSON data from the script tag
            try:
                json_data = json.loads(items[0].string)
                articles = self._find_articles_in_json(json_data)

                if not articles:
                    self.logger.error("Could not find articles in any expected JSON path")
            except Exception as e:
                self.logger.error(f"Error loading JSON from script tag: {str(e)}")
                return

            data = self._process_articles(articles)

            if not data:
                self.logger.error("No articles extracted from HackerNoon JSON data.")
                return

            # Save the data
            self._save_scraped_data(data)

        except Exception as e:
            self.logger.error(f"Error scraping HackerNoon: {str(e)}")

    def _process_articles(self, articles):
        """Process and extract data from articles."""
        data = []

        # Log a sample article to debug structure
        if articles:
            self.logger.info(f"Sample article keys: {list(articles[0].keys())}")

        for article in articles[:20]:  # Limit to 20 articles
            try:
                article_data = self._extract_article_data(article)
                data.append(article_data)
            except Exception as e:
                self.logger.error(f"Error parsing article: {str(e)}")

        return data

    def _extract_article_data(self, article):
        """Extract all data from a single article."""
        title = self._extract_title(article)
        author = self._extract_author(article)
        read_time = self._extract_read_time(article)
        date = self._extract_date(article)
        tags = self._extract_tags(article)
        url = self._extract_url(article)

        return {"title": title, "author": author, "read_time": read_time, "date": date, "tags": ", ".join(tags), "url": url}

    def _save_scraped_data(self, data):
        """Save scraped data to file."""
        now = datetime.now()
        date_folder = now.strftime("%Y-%m-%d")

        # Create date folder if it doesn't exist
        folder_path = os.path.join(self.project_root, "data", date_folder)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, f"{self.site_name}.md")
        self._save_data(data, file_path)
        self.logger.info(f"Saved {len(data)} HackerNoon articles to {file_path}")


# When run directly, execute the scraper
if __name__ == "__main__":
    scraper = HackerNoonScraper(test_mode=False)
    scraper.scrape()
