from .base import BaseScraper
from bs4 import BeautifulSoup
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class HackerNewsScraper(BaseScraper):
    SITE_NAME = "hackernews"
    URL = "https://news.ycombinator.com"
    SELECTOR = "tr.athing"

    def __init__(self):
        super().__init__()

    def _extract_data(self, items, fields=None):
        data = []
        for item in items:
            # Get the title and URL
            title_elem = item.select_one('.titleline a')
            if not title_elem:
                continue

            title = title_elem.text
            url = title_elem.get('href', '')

            # Get points and comments
            next_row = item.find_next_sibling('tr')
            if not next_row:
                continue

            subtext = next_row.select_one('.subtext')
            if not subtext:
                continue

            points = subtext.select_one('.score')
            points = points.text.split()[0] if points else '0'

            comments = subtext.select_one('a:last-child')
            comments = comments.text.split()[0] if comments else '0'

            data.append({
                'title': title,
                'url': url,
                'points': points,
                'comments': comments
            })

        return data
