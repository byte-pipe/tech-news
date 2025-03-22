import logging
from .base import BaseScraper
from typing import List, Dict, Optional
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup

def normalize_whitespace(text):
    import re
    return re.sub(r'\s+', ' ', text).strip() if text else ''

class HackerNoonScraper(BaseScraper):
    SITE_NAME = "hackernoon"
    URL = "https://hackernoon.com"
    SELECTOR = "article.story-card"
    main_selector = "script#__NEXT_DATA__"  # This contains the JSON data

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def get_items(self) -> List[BeautifulSoup]:
        try:
            script_tag = self.soup.select_one(self.main_selector)
            if not script_tag:
                self.logger.error("Could not find JSON data script tag")
                return []
            return [script_tag]
        except Exception as e:
            self.logger.error(f"Error getting items: {str(e)}")
            return []

    def scrape(self):
        """Custom scrape method for HackerNoon to handle JSON-based articles and log JSON structure for debugging."""
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
            try:
                json_data = json.loads(items[0].string)
                # Log the top-level keys for debugging
                self.logger.error(f"HackerNoon JSON top-level keys: {list(json_data.keys())}")
                # Try to log deeper keys if possible
                props = json_data.get('props', {})
                self.logger.error(f"props keys: {list(props.keys())}")
                pageProps = props.get('pageProps', {})
                self.logger.error(f"pageProps keys: {list(pageProps.keys())}")
                # Try to extract stories as before
                articles = pageProps.get('stories', [])
            except Exception as e:
                self.logger.error(f"Error loading JSON from script tag: {str(e)}")
                return
            data = []
            for article in articles:
                try:
                    title = article.get('title', '').strip()
                    author = article.get('profile', {}).get('displayName', '').strip()
                    read_time = article.get('readTime', '')
                    date = datetime.fromtimestamp(article.get('publishedAt', 0)).strftime('%Y-%m-%d')
                    tags = [tag.strip() for tag in article.get('tags', [])]
                    url = f"https://hackernoon.com/{article.get('slug', '')}"
                    data.append({
                        'title': title,
                        'author': author,
                        'read_time': read_time,
                        'date': date,
                        'tags': ', '.join(tags),
                        'url': url
                    })
                except Exception as e:
                    self.logger.error(f"Error parsing article: {str(e)}")
            if not data:
                self.logger.error("No articles extracted from HackerNoon JSON data.")
                return
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            file_path = os.path.join(self.project_root, "data", f"{self.site_name}-{timestamp}.md")
            self._save_data(data, file_path)
            self.logger.info(f"Saved {len(data)} HackerNoon articles to {file_path}")
        except Exception as e:
            self.logger.error(f"Error scraping HackerNoon: {str(e)}")