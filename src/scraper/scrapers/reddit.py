from .base import BaseScraper
import requests
import json
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class RedditScraper(BaseScraper):
    SITE_NAME = "reddit"
    URL = "https://www.reddit.com/r/startups/top.json?t=day"
    SELECTOR = None  # Not used for JSON API

    def __init__(self):
        super().__init__()

    def _extract_data(self, items, fields=None):
        data = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            # Use the JSON API
            response = requests.get(self.URL, headers=headers)
            response.raise_for_status()
            posts = response.json()['data']['children']

            for post in posts:
                post_data = post['data']
                data.append({
                    'title': post_data['title'],
                    'score': str(post_data['score']),
                    'comments': str(post_data['num_comments']),
                    'url': f"https://www.reddit.com{post_data['permalink']}"
                })

        except Exception as e:
            logger.error(f"Error fetching Reddit data: {str(e)}")

        return data