from .base import BaseScraper
import logging
from typing import List, Dict, Any
import re

logger = logging.getLogger(__name__)

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip() if text else ''

class DevToScraper(BaseScraper):
    SITE_NAME = "devto"
    URL = "https://dev.to/top/week"
    SELECTOR = "div.crayons-story"

    def __init__(self):
        super().__init__()

    def _extract_data(self, items, fields=None):
        data = []
        try:
            for item in items:
                article_data = {
                    'title': normalize_whitespace(item.select_one('h2').text) if item.select_one('h2') else '',
                    'description': normalize_whitespace(item.select_one('div.crayons-story__snippet').text) if item.select_one('div.crayons-story__snippet') else '',
                    'reactions': normalize_whitespace(item.select_one('div.crayons-story__details a.crayons-btn').text) if item.select_one('div.crayons-story__details a.crayons-btn') else '0',
                    'comments': normalize_whitespace(item.select_one('div.crayons-story__details a.crayons-btn:nth-child(2)').text) if item.select_one('div.crayons-story__details a.crayons-btn:nth-child(2)') else '0',
                    'url': 'https://dev.to' + item.select_one('h2 a')['href'] if item.select_one('h2 a') else ''
                }
                data.append(article_data)
        except Exception as e:
            logger.error(f"Error extracting Dev.to data: {str(e)}")
        return data