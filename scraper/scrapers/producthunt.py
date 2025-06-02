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


class ProductHuntScraper(BaseScraper):
    SITE_NAME = "producthunt"
    URL = "https://www.producthunt.com"
    SELECTOR = "div[data-test='product-item']"  # Updated selector for current ProductHunt

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def scrape(self, output_format="markdown"):
        """Custom scrape method for ProductHunt since it requires Selenium for JavaScript rendering.

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
                self.logger.error("No data extracted from ProductHunt.")
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
        """Extract data from ProductHunt using Selenium for JavaScript rendering.

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

                # Wait for products to load
                self.logger.info("Waiting for products to load")
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.SELECTOR)))

                # Get all product elements
                products = driver.find_elements(By.CSS_SELECTOR, self.SELECTOR)
                self.logger.info(f"Found {len(products)} products")

                for product in products:
                    try:
                        # Convert Selenium element to HTML and create a BeautifulSoup object
                        product_html = product.get_attribute("outerHTML")
                        product_soup = BeautifulSoup(product_html, "html.parser")

                        # Use standardized extraction methods with updated selectors
                        title = self.extract_title(product_soup, selectors=["h3", "[data-test='product-name']"])
                        description = self.extract_description(product_soup, selectors=["[data-test='product-tagline']", "p"])

                        # Extract URL from the title link
                        url_relative = ""
                        url_elem = product_soup.select_one("a[href^='/posts/']")
                        if url_elem and url_elem.has_attr("href"):
                            url_relative = url_elem["href"]
                        url = f"{base_url}{url_relative}" if url_relative else ""

                        # Extract specific ProductHunt data
                        votes = "0"
                        votes_elem = product_soup.select_one("[data-test='vote-button'] span")
                        if votes_elem:
                            votes = votes_elem.text.strip()

                        # Extract comments count
                        comments = "0"
                        comments_elem = product_soup.select_one("[data-test='comment-count']")
                        if comments_elem:
                            comments = comments_elem.text.strip()

                        # Try to extract product maker info
                        maker = self.extract_author(product_soup, selectors=["[data-test='maker-name']"])

                        # Extract category/topics if available
                        topics = self.extract_tags(product_soup, selectors=["[data-test='topic-name']"])
                        topics_str = ", ".join(topics) if topics else ""

                        product_data = {"title": title, "description": description, "url": url, "votes": votes, "comments": comments, "maker": maker, "topics": topics_str}

                        # Only add if we have a title and URL
                        if title and url:
                            data.append(product_data)
                            self.logger.debug(f"Processed product: {title}")
                    except Exception as e:
                        self.logger.error(f"Error processing product: {str(e)}")
                        continue

            except Exception as e:
                self.logger.error(f"Error fetching ProductHunt data: {str(e)}")

        if not data:
            self.logger.warning("No data was extracted from ProductHunt")
        else:
            self.logger.info(f"Successfully extracted {len(data)} products from ProductHunt")

        return data


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = ProductHuntScraper(test_mode=False)
    scraper.scrape()
