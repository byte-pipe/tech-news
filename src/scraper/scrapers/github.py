from .base import BaseScraper
from bs4 import BeautifulSoup
import logging
import os
import re
from datetime import datetime

logger = logging.getLogger(__name__)

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip() if text else ''

class GitHubScraper(BaseScraper):
    SITE_NAME = "github"
    URL = "https://github.com/trending"
    SELECTOR = "article.Box-row"

    def __init__(self):
        super().__init__()

    def _extract_data(self, items, fields=None):
        data = []
        base_url = self.URL

        for item in items:
            # Get title and description
            title_elem = item.select_one('h2 a')
            description_elem = item.select_one('p')

            if not title_elem:
                continue

            title = normalize_whitespace(title_elem.text)
            description = normalize_whitespace(description_elem.text) if description_elem else ''

            # Get stars and language
            stars_elem = item.select_one('a[href*="stargazers"]')
            stars = '0'
            if stars_elem:
                stars_text = stars_elem.text.strip()
                if 'k' in stars_text:
                    stars = str(int(float(stars_text.replace('k', '')) * 1000))
                else:
                    stars = stars_text

            language = item.select_one('span[itemprop="programmingLanguage"]')
            language = normalize_whitespace(language.text) if language else 'N/A'

            # Get URL
            url = title_elem.get('href', '')
            if url and not url.startswith('http'):
                url = f"{base_url}{url}"

            data.append({
                'title': title,
                'description': description,
                'stars': stars,
                'language': language,
                'url': url
            })

        return data