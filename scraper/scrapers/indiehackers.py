import logging
import os
from datetime import datetime

from bs4 import BeautifulSoup
from scraper.utils.browser import chrome_driver_context
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base import BaseScraper

logger = logging.getLogger(__name__)


class IndieHackersScraper(BaseScraper):
    SITE_NAME = "indiehackers"
    URL = "https://www.indiehackers.com"
    SELECTOR = "div.feed-item, article.feed-item"  # Updated selector for current IndieHackers

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def scrape(self, output_format="markdown"):
        """Custom scrape method for IndieHackers since it requires Selenium for JavaScript rendering.

        Args:
            output_format: Format to save the data in - one of 'markdown', 'json', or 'csv'
                           Default is 'markdown'

        Returns:
            List of dictionaries containing scraped data, or empty list if no data was extracted
        """
        try:
            # Get data using Selenium
            data = self._extract_data([])  # We pass an empty list since we get items differently

            if not data:
                self.logger.error("No data extracted from IndieHackers.")
                return []

            # Remove duplicates
            data = self._remove_duplicates(data)

            # Save the data
            now = datetime.now()
            date_folder = now.strftime("%Y-%m-%d")
            timestamp = now.strftime("%Y%m%d-%H%M%S")

            # Create date folder if it doesn't exist
            folder_path = os.path.join(self.project_root, "data", date_folder)
            os.makedirs(folder_path, exist_ok=True)

            # Use the appropriate file extension based on the output format
            if output_format == "json":
                file_extension = ".json"
            elif output_format == "csv":
                file_extension = ".csv"
            else:  # default to markdown
                file_extension = ".md"

            file_path = os.path.join(folder_path, f"{self.site_name}-{timestamp}{file_extension}")
            self._save_data(data, file_path, format=output_format)

            self.logger.info(f"Successfully extracted and saved {len(data)} items from {self.site_name} in {output_format} format")
            return data

        except Exception as e:
            self.logger.error(f"Error scraping {self.site_name}: {str(e)}")
            return []

    def _extract_data(self, items, fields=None):
        """Extract data from IndieHackers using Selenium for JavaScript rendering.

        Note: The items parameter is not used here since we extract directly with Selenium.
        """
        data = []
        base_url = self.URL

        # Use the chrome_driver_context to ensure proper setup and cleanup
        with chrome_driver_context(headless=True) as driver:
            try:
                # Navigate to the page
                self.logger.info(f"Navigating to {base_url}")
                driver.get(base_url)

                # Wait for posts to load - might need longer wait time for IndieHackers
                self.logger.info("Waiting for posts to load")
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.SELECTOR)))

                # Get all post elements
                posts = driver.find_elements(By.CSS_SELECTOR, self.SELECTOR)
                self.logger.info(f"Found {len(posts)} posts")

                for post in posts:
                    try:
                        # Convert Selenium element to HTML and create a BeautifulSoup object
                        post_html = post.get_attribute("outerHTML")
                        post_soup = BeautifulSoup(post_html, "html.parser")

                        # Use standardized extraction methods with updated selectors
                        title = self.extract_title(post_soup, selectors=["h2", ".feed-item__title", ".post__title"])
                        description = self.extract_description(post_soup, selectors=[".feed-item__description", ".post__content p"])

                        # Extract URL
                        url_elem = post_soup.select_one("a.feed-item__title-link, a.post__title-link")
                        url = url_elem["href"] if url_elem and url_elem.has_attr("href") else ""
                        # Make sure URL is absolute
                        if url and not url.startswith("http"):
                            url = f"{base_url}{url}"

                        # Extract specific IndieHackers data
                        revenue = ""
                        revenue_elem = post_soup.select_one(".feed-item__revenue, .revenue-label")
                        if revenue_elem:
                            revenue = revenue_elem.text.strip()

                        # Get comment count
                        comments = "0"
                        comments_elem = post_soup.select_one(".feed-item__comments-count, .post__comment-count")
                        if comments_elem:
                            comments_text = comments_elem.text.strip()
                            # Extract just the number from text like "5 comments"
                            import re

                            comments_match = re.search(r"\d+", comments_text)
                            if comments_match:
                                comments = comments_match.group(0)

                        # Extract author
                        author = self.extract_author(post_soup, selectors=[".feed-item__author", ".user__name"])

                        # Extract tags/categories if available
                        tags = self.extract_tags(post_soup, selectors=[".category-tag", ".topic-tag"])
                        tags_str = ", ".join(tags) if tags else ""

                        # Get likes/reactions if available
                        likes = "0"
                        likes_elem = post_soup.select_one(".reaction-count, .likes-count")
                        if likes_elem:
                            likes_text = likes_elem.text.strip()
                            likes_match = re.search(r"\d+", likes_text)
                            if likes_match:
                                likes = likes_match.group(0)

                        post_data = {"title": title, "description": description, "url": url, "revenue": revenue, "comments": comments, "author": author, "tags": tags_str, "likes": likes}

                        # Only add if we have a title and URL
                        if title and url:
                            data.append(post_data)
                            self.logger.debug(f"Processed post: {title}")
                    except Exception as e:
                        self.logger.error(f"Error processing post: {str(e)}")
                        continue

            except Exception as e:
                self.logger.error(f"Error fetching IndieHackers data: {str(e)}")

        if not data:
            self.logger.warning("No data was extracted from IndieHackers")
        else:
            self.logger.info(f"Successfully extracted {len(data)} posts from IndieHackers")

        return data


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = IndieHackersScraper(test_mode=False)
    scraper.scrape()
