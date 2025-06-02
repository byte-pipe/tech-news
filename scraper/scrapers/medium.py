import logging

from .base import BaseScraper

logger = logging.getLogger(__name__)


class MediumScraper(BaseScraper):
    SITE_NAME = "medium"
    URL = "https://medium.com/top-stories"
    SELECTOR = "article"

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def _extract_data(self, items, fields=None):
        """Extract data from Medium articles.

        This is a placeholder implementation. Medium's website heavily relies on
        JavaScript and may require a more sophisticated approach like Selenium
        or using their API.
        """
        data = []
        base_url = "https://medium.com"

        try:
            for item in items:
                # Use standardized extraction methods
                title = self.extract_title(item, selectors=["h2", "h3"])
                url = self.extract_url(item, base_url=base_url)
                author = self.extract_author(item)
                description = self.extract_description(item)
                date_str, _ = self.extract_date(item)
                tags = self.extract_tags(item)

                if title and url:
                    data.append({"title": title, "author": author, "description": description, "date": date_str, "tags": ", ".join(tags), "url": url})
        except Exception as e:
            self.logger.error(f"Error extracting Medium data: {str(e)}")

        return data


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = MediumScraper(test_mode=False)
    scraper.scrape()
