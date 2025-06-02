import logging
import os
from datetime import datetime

from bs4 import BeautifulSoup

from .base import BaseScraper

logger = logging.getLogger(__name__)


class TechCrunchScraper(BaseScraper):
    SITE_NAME = "techcrunch"
    URL = "https://techcrunch.com/"
    SELECTOR = "article"  # This is a fallback, we're using a custom implementation

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def scrape(self):
        """Custom scrape method for TechCrunch to handle different article sections."""
        try:
            html = self._get_page(self.url)
            if not html:
                self.logger.error("No HTML content fetched.")
                return

            self.soup = BeautifulSoup(html, "html.parser")

            # Extract articles using custom logic to get more comprehensive results
            data = []

            # Try to extract JSON-LD data first - may contain more structured data
            json_ld_data = self.extract_metadata_from_json_ld(html)
            if json_ld_data:
                self.logger.info(f"Extracted {len(json_ld_data)} articles from JSON-LD")
                data.extend(json_ld_data)

            # Process regular articles from the homepage
            article_cards = self.soup.select(".loop-card, article.post-block, .features-item")
            self.logger.info(f"Found {len(article_cards)} article cards on the homepage")
            data.extend(self._process_article_cards(article_cards))

            # Process latest news articles
            latest_posts = self.soup.select(".wp-block-latest-posts__list li")
            self.logger.info(f"Found {len(latest_posts)} latest news posts")
            data.extend(self._process_latest_posts(latest_posts))

            # Save the data if any articles were found
            if not data:
                self.logger.error("No articles extracted from TechCrunch.")
                return

            # Remove duplicates based on URL
            unique_articles = {}
            for article in data:
                if article.get("url") and article["url"] not in unique_articles:
                    unique_articles[article["url"]] = article

            data = list(unique_articles.values())
            self.logger.info(f"Extracted {len(data)} unique articles from TechCrunch")

            # Save the data
            now = datetime.now()
            date_folder = now.strftime("%Y-%m-%d")
            timestamp = now.strftime("%Y%m%d-%H%M%S")

            # Create date folder if it doesn't exist
            folder_path = os.path.join(self.project_root, "data", date_folder)
            os.makedirs(folder_path, exist_ok=True)

            file_path = os.path.join(folder_path, f"{self.site_name}-{timestamp}.md")
            self._save_data(data, file_path)

        except Exception as e:
            self.logger.error(f"Error scraping TechCrunch: {str(e)}")

    def _process_article_cards(self, cards):
        """Process the main article cards on the homepage."""
        results = []
        base_url = "https://techcrunch.com"

        for card in cards:
            try:
                # Use standardized extraction methods
                title = self.extract_title(card, selectors=[".loop-card__title", "h2 a", ".features-item__title", ".post-block__title"])

                url = self.extract_url(card, base_url=base_url)

                author = self.extract_author(card, selectors=[".loop-card__byline", ".river-byline__authors", ".post-block__author"])

                description = self.extract_description(card, selectors=[".loop-card__excerpt", ".features-item__excerpt", ".post-block__content"], max_length=200)

                date_str, _ = self.extract_date(card, selectors=["time"])

                # Extract categories/tags
                tags = self.extract_tags(card, selectors=[".tc-category", ".river-byline__category-link a", ".article__category-link"])

                # Create data entry
                article_data = {"title": title, "author": author, "description": description, "date": date_str, "tags": ", ".join(tags), "url": url}

                # Only add articles with valid titles and URLs
                if title and url:
                    results.append(article_data)
            except Exception as e:
                self.logger.error(f"Error extracting article data: {str(e)}")

        return results

    def _process_latest_posts(self, posts):
        """Process the latest news posts section."""
        results = []
        base_url = "https://techcrunch.com"

        for post in posts:
            try:
                # Use standardized extraction methods
                title = self.extract_title(post, selectors=["a"])
                url = self.extract_url(post, base_url=base_url)
                date_str, _ = self.extract_date(post, selectors=["time"])

                # Create data entry
                article_data = {"title": title, "author": "", "description": "", "date": date_str, "tags": "", "url": url}  # Latest news often doesn't show authors

                # Only add articles with valid titles and URLs
                if title and url:
                    results.append(article_data)
            except Exception as e:
                self.logger.error(f"Error extracting latest news data: {str(e)}")

        return results

    def _extract_data(self, items, fields=None):
        """Extract data from a list of article elements.

        This is used when the standard scrape method is called, which uses the SELECTOR class variable.
        """
        results = []
        base_url = "https://techcrunch.com"

        for item in items:
            try:
                # Use standardized extraction methods
                title = self.extract_title(item)
                url = self.extract_url(item, base_url=base_url)
                author = self.extract_author(item)
                date_str, _ = self.extract_date(item)
                description = self.extract_description(item, max_length=200)
                tags = self.extract_tags(item)

                # Create data entry
                article_data = {"title": title, "author": author, "description": description, "date": date_str, "tags": ", ".join(tags), "url": url}

                # Only add articles with valid titles and URLs
                if title and url:
                    results.append(article_data)
            except Exception as e:
                self.logger.error(f"Error extracting article data: {str(e)}")

        return results


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = TechCrunchScraper(test_mode=False)
    scraper.scrape()
