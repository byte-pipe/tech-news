import logging
import os
from datetime import datetime

from bs4 import BeautifulSoup

from .base import BaseScraper

logger = logging.getLogger(__name__)


class TechNodeScraper(BaseScraper):
    SITE_NAME = "technode"
    URL = "https://technode.com/"
    SELECTOR = ".wp-block-newspack-blocks-homepage-articles article"

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)
        self.logger = logging.getLogger(__name__)

    def _extract_data(self, items, fields=None):
        data = []
        try:
            self.logger.info(f"Processing {len(items)} TechNode articles")
            for item in items:
                try:
                    # Extract title
                    title_elem = item.select_one(".entry-title")
                    if not title_elem:
                        continue
                    title = title_elem.text.strip()

                    # Extract URL
                    link_elem = title_elem.select_one("a")
                    url = link_elem.get("href", "") if link_elem else ""

                    # Extract author
                    author_elem = item.select_one(".avatar + a, .author a, .byline a")
                    author = author_elem.text.strip() if author_elem else ""

                    # If no author found, try to extract from the byline
                    if not author:
                        byline = item.select_one(".byline")
                        if byline:
                            author_text = byline.text.strip()
                            # Extract author name from "By Author Name"
                            if author_text.startswith("By "):
                                author = author_text[3:].strip()

                    # Extract date
                    date_elem = item.select_one(".entry-meta time, .entry-date, .posted-on time")
                    date = ""
                    if date_elem:
                        date_str = date_elem.get("datetime", "") or date_elem.text.strip()
                        try:
                            # Try to parse ISO date if available
                            if "T" in date_str:
                                date = datetime.fromisoformat(date_str.replace("Z", "+00:00")).strftime("%Y-%m-%d")
                            else:
                                # Try common date formats
                                for fmt in ["%B %d, %Y", "%b %d, %Y", "%d %B %Y", "%d %b %Y"]:
                                    try:
                                        parsed_date = datetime.strptime(date_str, fmt)
                                        date = parsed_date.strftime("%Y-%m-%d")
                                        break
                                    except ValueError:
                                        continue

                                # If all formats failed, use the raw string
                                if not date:
                                    date = date_str
                        except Exception as e:
                            self.logger.warning(f"Could not parse date: {date_str}, error: {e}")
                            date = date_str

                    # Extract description
                    excerpt_elem = item.select_one("p.entry-content, .excerpt")
                    excerpt = excerpt_elem.text.strip() if excerpt_elem else ""

                    # Extract categories
                    category_elems = item.select(".cat-links a, .entry-meta .tags-links a")
                    categories = [cat.text.strip() for cat in category_elems if cat.text.strip()]

                    # Clean up categories - don't include very long strings that are likely headlines
                    categories = [cat for cat in categories if len(cat) < 40]

                    # Create article data
                    article_data = {"title": title, "author": author, "description": excerpt, "date": date, "categories": ", ".join(categories), "url": url}

                    data.append(article_data)
                except Exception as e:
                    self.logger.error(f"Error extracting article data: {str(e)}")

            self.logger.info(f"Extracted {len(data)} articles from TechNode")
        except Exception as e:
            self.logger.error(f"Error extracting TechNode data: {str(e)}")

        return data

    def scrape(self):
        """Custom scrape method for TechNode to handle multiple article sections."""
        try:
            html = self._get_page(self.url)
            if not html:
                self.logger.error("No HTML content fetched.")
                return

            self.soup = BeautifulSoup(html, "html.parser")

            # Extract articles from all article sections
            all_articles = self.soup.select(self.SELECTOR)
            self.logger.info(f"Found {len(all_articles)} articles on TechNode homepage")

            # Extract data from articles
            data = self._extract_data(all_articles)

            # Save the data if any articles were found
            if not data:
                self.logger.error("No articles extracted from TechNode.")
                return

            # Remove duplicates based on URL
            unique_articles = {}
            for article in data:
                if article["url"] not in unique_articles:
                    unique_articles[article["url"]] = article

            data = list(unique_articles.values())
            self.logger.info(f"Extracted {len(data)} unique articles from TechNode")

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
            self.logger.error(f"Error scraping TechNode: {str(e)}")


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = TechNodeScraper(test_mode=False)
    scraper.scrape()
