from .base import BaseScraper
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class ProductHuntScraper(BaseScraper):
    SITE_NAME = "producthunt"
    URL = "https://www.producthunt.com"
    SELECTOR = "div.styles_item__Dk_nz"

    def __init__(self):
        super().__init__()

    def _extract_data(self, items, fields=None):
        data = []
        try:
            for item in items:
                product_data = {
                    'title': item.select_one('h3').text.strip() if item.select_one('h3') else '',
                    'description': item.select_one('div.styles_tagline__8bU9j').text.strip() if item.select_one('div.styles_tagline__8bU9j') else '',
                    'url': item.select_one('a')['href'] if item.select_one('a') else '',
                    'votes': item.select_one('span.styles_votesCount__yQwJT').text.strip() if item.select_one('span.styles_votesCount__yQwJT') else ''
                }
                data.append(product_data)
        except Exception as e:
            logger.error(f"Error extracting ProductHunt data: {str(e)}")
        return data