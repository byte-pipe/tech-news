import logging

from scraper.utils.text_utils import normalize_whitespace

from .base import BaseScraper

logger = logging.getLogger(__name__)


class DevToScraper(BaseScraper):
    SITE_NAME = "devto"
    URL = "https://dev.to/top/week"
    SELECTOR = "div.crayons-story"

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def _extract_data(self, items, fields=None):
        """Extract data from Dev.to articles using standardized methods."""
        data = []
        base_url = "https://dev.to"

        try:
            for item in items:
                try:
                    # Use standardized extraction methods
                    title = self.extract_title(item, selectors=["h2 a", "h2"])
                    url = self.extract_url(item, base_url=base_url, selectors=["h2 a"])

                    # Make sure the URL is absolute
                    if url and not url.startswith("http"):
                        url = base_url + url

                    # Extract author information
                    author = self.extract_author(item, selectors=[".crayons-story__meta a.crayons-story__secondary", ".profile-preview-card__name"])

                    # Extract date
                    date_str, _ = self.extract_date(item, selectors=["time", ".crayons-story__meta time"])

                    # Extract description
                    description = self.extract_description(item, selectors=[".crayons-story__snippet", ".crayons-story__body"])

                    # Extract tags
                    tags = self.extract_tags(item, selectors=[".crayons-tag", ".crayons-story__tags a"])

                    # Dev.to specific metrics: Reactions and Comments
                    reactions_elem = item.select_one("div.crayons-story__details a.crayons-btn")
                    reactions = normalize_whitespace(reactions_elem.text) if reactions_elem else "0"

                    comments_elem = item.select_one("div.crayons-story__details a.crayons-btn:nth-child(2)")
                    comments = normalize_whitespace(comments_elem.text) if comments_elem else "0"

                    # Create data entry
                    article_data = {"title": title, "author": author, "date": date_str, "description": description, "tags": ", ".join(tags), "reactions": reactions, "comments": comments, "url": url}

                    # Only add articles with valid titles and URLs
                    if title and url:
                        data.append(article_data)
                except Exception as e:
                    self.logger.error(f"Error extracting article data: {str(e)}")
        except Exception as e:
            self.logger.error(f"Error extracting Dev.to data: {str(e)}")

        return data


# Enable standalone execution
if __name__ == "__main__":
    from scraper.utils.runner import run_scraper

    run_scraper(DevToScraper)
