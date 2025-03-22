from .base import BaseScraper
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class IndieHackersScraper(BaseScraper):
    SITE_NAME = "indiehackers"
    URL = "https://www.indiehackers.com"
    SELECTOR = "div.feed-item"

    def __init__(self):
        super().__init__()

    def _extract_data(self, items, fields=None):
        data = []
        try:
            for item in items:
                project_data = {
                    'title': item.select_one('h2').text.strip() if item.select_one('h2') else '',
                    'description': item.select_one('div.feed-item__description').text.strip() if item.select_one('div.feed-item__description') else '',
                    'url': item.select_one('a.feed-item__title-link')['href'] if item.select_one('a.feed-item__title-link') else '',
                    'revenue': item.select_one('span.feed-item__revenue').text.strip() if item.select_one('span.feed-item__revenue') else '',
                    'comments': item.select_one('span.feed-item__comments').text.strip() if item.select_one('span.feed-item__comments') else ''
                }
                data.append(project_data)
        except Exception as e:
            logger.error(f"Error extracting IndieHackers data: {str(e)}")
        return data