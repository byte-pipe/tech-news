from .base import BaseScraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class LobstersScraper(BaseScraper):
    SITE_NAME = "lobsters"
    URL = "https://lobste.rs"
    SELECTOR = "div.story_liner"

    def __init__(self):
        super().__init__()

    def _extract_data(self, items, fields=None):
        data = []
        base_url = self.URL
        driver = None

        try:
            # Set up Chrome options
            chrome_options = Options()
            chrome_options.add_argument('--headless')  # Run in headless mode
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

            # Initialize the Chrome driver
            logger.info("Initializing Chrome driver for Lobsters scraper")
            driver = webdriver.Chrome(options=chrome_options)

            # Navigate to the page
            logger.info(f"Navigating to {base_url}")
            driver.get(base_url)

            # Wait for stories to load
            logger.info("Waiting for stories to load")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "story_liner"))
            )

            # Get all story elements
            stories = driver.find_elements(By.CLASS_NAME, "story_liner")
            logger.info(f"Found {len(stories)} stories")

            for story in stories:
                try:
                    # Get title and URL
                    title_elem = story.find_element(By.CSS_SELECTOR, "a.u-url")
                    title = title_elem.text.strip()
                    url = title_elem.get_attribute('href')

                    # Get score
                    score_elem = story.find_element(By.CSS_SELECTOR, "a.upvoter")
                    score = score_elem.text.strip()

                    # Get comments - they don't show comment count on the main page anymore
                    comments = "0"

                    data.append({
                        'title': title,
                        'score': score,
                        'comments': comments,
                        'url': url
                    })
                    logger.debug(f"Processed story: {title}")
                except Exception as e:
                    logger.error(f"Error processing story: {str(e)}")
                    continue

        except Exception as e:
            logger.error(f"Error fetching Lobsters data: {str(e)}")
        finally:
            # Clean up
            if driver:
                try:
                    driver.quit()
                    logger.info("Chrome driver closed successfully")
                except Exception as e:
                    logger.error(f"Error closing Chrome driver: {str(e)}")

        if not data:
            logger.warning("No data was extracted from Lobsters")
        else:
            logger.info(f"Successfully extracted {len(data)} stories from Lobsters")

        return data