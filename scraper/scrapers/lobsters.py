import logging
import os
from datetime import datetime

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from scraper.utils.browser import chrome_driver_context

from .base import BaseScraper

logger = logging.getLogger(__name__)


class LobstersScraper(BaseScraper):
    SITE_NAME = "lobsters"
    URL = "https://lobste.rs"
    SELECTOR = "div.story_liner"

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def scrape(self, output_format="markdown"):
        """Custom scrape method for Lobsters since it requires Selenium.

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
                self.logger.error("No data extracted from Lobsters.")
                return []

            # Remove duplicates
            data = self._remove_duplicates(data)

            # Save the data
            now = datetime.now()
            date_folder = now.strftime("%Y-%m-%d")

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

            file_path = os.path.join(folder_path, f"{self.site_name}{file_extension}")
            self._save_data(data, file_path, format=output_format)

            self.logger.info(f"Successfully extracted and saved {len(data)} items from {self.site_name} in {output_format} format")
            return data

        except Exception as e:
            self.logger.error(f"Error scraping {self.site_name}: {str(e)}")
            return None

    def _extract_data(self, items, fields=None):
        """Extract data using Selenium for Lobsters.

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

                # Wait for stories to load
                self.logger.info("Waiting for stories to load")
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "story_liner")))

                # Get all story elements
                stories = driver.find_elements(By.CLASS_NAME, "story_liner")
                self.logger.info(f"Found {len(stories)} stories")

                for story in stories:
                    try:
                        # Convert Selenium element to HTML and create a BeautifulSoup object
                        story_html = story.get_attribute("outerHTML")
                        story_soup = BeautifulSoup(story_html, "html.parser")

                        # Use standardized extraction methods
                        title = self.extract_title(story_soup, selectors=["a.u-url", "a.story_title"])
                        url = self.extract_url(story_soup, base_url=base_url, selectors=["a.u-url", "a.story_title"])

                        # Get score
                        score = "0"
                        try:
                            score_elem = story.find_element(By.CSS_SELECTOR, "a.upvoter")
                            score = score_elem.text.strip()
                        except Exception as e:
                            self.logger.debug(f"Error extracting score: {str(e)}")

                        # Get comments - they don't show comment count on the main page anymore
                        comments = "0"

                        # Extract author using standardized method
                        author = self.extract_author(story_soup, selectors=[".byline a"])

                        # Extract tags using standardized method
                        tags_list = self.extract_tags(story_soup, selectors=[".tags a"])
                        tags = ", ".join(tags_list) if tags_list else ""

                        # Extract description if possible
                        description = self.extract_description(story_soup, max_length=200)

                        # Get current date as we don't have date information on the homepage
                        date_str, _ = self.extract_date(story_soup, default_format="%Y-%m-%d")

                        data.append({"title": title, "author": author, "score": score, "comments": comments, "tags": tags, "url": url, "date": date_str, "description": description})
                        self.logger.debug(f"Processed story: {title}")
                    except Exception as e:
                        self.logger.error(f"Error processing story: {str(e)}")
                        continue

            except Exception as e:
                self.logger.error(f"Error fetching Lobsters data: {str(e)}")

        if not data:
            self.logger.warning("No data was extracted from Lobsters")
        else:
            self.logger.info(f"Successfully extracted {len(data)} stories from Lobsters")

        return data


# When run directly, execute the scraper
if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    scraper = LobstersScraper()
    scraper.scrape()
