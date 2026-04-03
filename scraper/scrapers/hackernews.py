import logging
import re

from .base import BaseScraper

logger = logging.getLogger(__name__)


class HackerNewsScraper(BaseScraper):
    SITE_NAME = "hackernews"
    URL = "https://news.ycombinator.com"
    SELECTOR = "tr.athing"

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def _extract_data(self, items, fields=None):
        """Extract data from HackerNews items using the standardized extraction methods."""
        data = []
        base_url = self.URL

        for item in items:
            try:
                # Use standardized methods to extract title and URL
                title = self.extract_title(item, selectors=[".titleline a"])
                url = self.extract_url(item, base_url=base_url, selectors=[".titleline a"])

                # Get points and comments from the next row (HackerNews specific structure)
                next_row = item.find_next_sibling("tr")
                if not next_row:
                    continue

                subtext = next_row.select_one(".subtext")
                if not subtext:
                    continue

                # Extract author
                author = self.extract_author(subtext, selectors=[".hnuser"])

                # Extract date (in the format "X hours/days ago")
                date_str, date_obj = self.extract_date(subtext, selectors=[".age a"])

                # Custom extraction for points
                points_elem = subtext.select_one(".score")
                points = points_elem.text.split()[0] if points_elem else "0"

                # Custom extraction for comments
                comments_elem = subtext.select_one("a:last-child")
                comments_text = comments_elem.text if comments_elem else "0"
                # Extract just the number from text like "X comments" using regex
                comments_match = re.search(r"(\d+)\s+comment", comments_text)
                comments = comments_match.group(1) if comments_match else "0"

                # Get the item URL (useful for directly linking to HN discussions)
                item_id = item.get("id", "")
                item_url = f"{base_url}/item?id={item_id}" if item_id else ""

                data.append({"title": title, "url": url, "author": author, "date": date_str, "points": points, "comments": comments, "discussion_url": item_url})
            except Exception as e:
                self.logger.error(f"Error extracting data from HackerNews item: {str(e)}")

        return data


# Enable standalone execution
if __name__ == "__main__":
    from scraper.utils.runner import run_scraper

    run_scraper(HackerNewsScraper)
