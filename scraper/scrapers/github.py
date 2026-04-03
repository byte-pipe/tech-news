import logging
import os
import re

from scraper.constants import GITHUB_STARS_MULTIPLIER
from scraper.utils.datetime_utils import get_date_folder
from scraper.utils.paths import ensure_directory

from .base import BaseScraper

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    SITE_NAME = "github"
    URL = "https://github.com/trending"
    SELECTOR = "article.Box-row"
    # Add time periods to get more variety
    TIME_PERIODS = ["daily", "weekly", "monthly"]

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)

    def scrape(self, output_format="markdown"):
        """Custom scrape method to fetch multiple pages of GitHub trending repos.

        Args:
            output_format: Format to save the data in - one of 'markdown', 'json', or 'csv'
                           Default is 'markdown'
        """
        try:
            all_data = []

            # Fetch trending repositories for different time periods
            for period in self.TIME_PERIODS:
                period_url = f"{self.URL}?since={period}"
                self.logger.info(f"Fetching GitHub trending repositories for period: {period}")

                html = self._get_page(period_url)
                if not html:
                    self.logger.error(f"No HTML content fetched for period: {period}")
                    continue

                items = self._parse_html(html, self.SELECTOR)
                if not items:
                    self.logger.error(f"No items found for period: {period}")
                    continue

                # Extract data from the items
                period_data = self._extract_data(items)
                if period_data:
                    # Add time period as metadata
                    for item in period_data:
                        item["period"] = period

                    self.logger.info(f"Found {len(period_data)} trending repositories for period: {period}")
                    all_data.extend(period_data)

            # Use the base class method for deduplication
            final_data = self._remove_duplicates(all_data)
            self.logger.info(f"Found {len(final_data)} unique GitHub trending repositories across all time periods")

            # Save the data
            if final_data:
                date_folder = get_date_folder()

                # Create date folder if it doesn't exist
                folder_path = os.path.join(self.project_root, "data", date_folder)
                ensure_directory(folder_path)

                # Use the appropriate file extension based on the output format
                if output_format == "json":
                    file_extension = ".json"
                elif output_format == "csv":
                    file_extension = ".csv"
                else:  # default to markdown
                    file_extension = ".md"

                file_path = os.path.join(folder_path, f"{self.site_name}{file_extension}")
                self._save_data(final_data, file_path, format=output_format)
                self.logger.info(f"Saved {len(final_data)} GitHub repositories to {file_path} in {output_format} format")
                return final_data
            else:
                self.logger.error("No GitHub trending repositories found")
                return []

        except Exception as e:
            self.logger.error(f"Error scraping GitHub trending: {str(e)}")
            return None

    def _extract_data(self, items, fields=None):
        """Extract repository data using standardized methods."""
        data = []
        base_url = "https://github.com"  # Use full GitHub URL for repositories

        for item in items:
            try:
                # Use standardized extraction methods
                # Get the full title first
                full_title = self.extract_title(item, selectors=["h2 a", "h1 a"])

                # Extract repository owner/author
                author = ""
                author_elem = item.select_one("h2 a span.text-normal")
                if author_elem:
                    # Clean up the author name - remove slashes and extra spaces
                    author = author_elem.text.strip().strip("/").strip()

                # Extract the repository name (title without owner)
                # If author is found, remove it from the full title
                title = full_title
                if author and author in full_title:
                    title = full_title.replace(author, "").replace("/", "").strip()

                url = self.extract_url(item, base_url=base_url, selectors=["h2 a", "h1 a"])
                description = self.extract_description(item, selectors=["p"], max_length=200)

                # GitHub-specific data: stars
                stars_elem = item.select_one('a[href*="stargazers"]')
                stars = "0"
                if stars_elem:
                    stars_text = stars_elem.text.strip()
                    if "k" in stars_text.lower():
                        # Convert 'k' notation to actual numbers (e.g., 1.2k -> 1200)
                        stars = str(int(float(stars_text.replace("k", "").replace("K", "")) * GITHUB_STARS_MULTIPLIER))
                    else:
                        stars = stars_text.replace(",", "")  # Remove commas from large numbers

                # Extract programming language
                language_elem = item.select_one('span[itemprop="programmingLanguage"]')
                language = language_elem.text.strip() if language_elem else "N/A"

                # Extract forks if available
                forks = "0"
                forks_elem = item.select_one('a[href*="network/members"]')
                if forks_elem:
                    forks_text = forks_elem.text.strip()
                    if "k" in forks_text.lower():
                        forks = str(int(float(forks_text.replace("k", "").replace("K", "")) * GITHUB_STARS_MULTIPLIER))
                    else:
                        forks = forks_text.replace(",", "")

                # Extract today's stars if available
                today_stars = "0"
                today_elem = item.select_one("span.d-inline-block.float-sm-right")
                if today_elem:
                    today_text = today_elem.text.strip()
                    stars_match = re.search(r"(\d+(?:[,.]\d+)*)\s+stars\s+today", today_text)
                    if stars_match:
                        today_stars = stars_match.group(1).replace(",", "")

                data.append({"title": title, "author": author, "description": description, "stars": stars, "forks": forks, "today_stars": today_stars, "language": language, "url": url})
            except Exception as e:
                self.logger.error(f"Error extracting repository data: {str(e)}")
                continue

        return data


# Enable standalone execution
if __name__ == "__main__":
    from scraper.utils.runner import run_scraper

    run_scraper(GitHubScraper)
