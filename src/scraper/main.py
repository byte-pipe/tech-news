import argparse
from scrapers.github import GitHubScraper
from scrapers.reddit import RedditScraper
from scrapers.lobsters import LobstersScraper
from scrapers.devto import DevToScraper
from scrapers.hackernews import HackerNewsScraper
from scrapers.producthunt import ProductHuntScraper
from scrapers.indiehackers import IndieHackersScraper
from scrapers.hackernoon import HackerNoonScraper
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def setup_logging():
    """Configure logging for the application."""
    # Create logs directory
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "scraper.log")
    # Create a formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # Create a file handler
    file_handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)  # 10MB per file, keep 5 backups
    file_handler.setFormatter(formatter)
    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


def cleanup_empty_files():
    """Delete empty files from the data directory."""
    logger = logging.getLogger(__name__)
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    if not os.path.exists(data_dir):
        logger.info("Data directory does not exist")
        return
    deleted_files = []
    for file in os.listdir(data_dir):
        if not file.endswith(".md"):
            continue
        file_path = os.path.join(data_dir, file)
        if os.path.getsize(file_path) == 0:
            try:
                os.remove(file_path)
                deleted_files.append(file)
                logger.info(f"Deleted empty file: {file}")
            except Exception as e:
                logger.error(f"Error deleting file {file}: {str(e)}")
        else:
            # Check if file only contains the header
            with open(file_path, "r") as f:
                content = f.read().strip()
                if content.count("\n") <= 1:  # Only header line
                    try:
                        os.remove(file_path)
                        deleted_files.append(file)
                        logger.info(f"Deleted file with only header: {file}")
                    except Exception as e:
                        logger.error(f"Error deleting file {file}: {str(e)}")
    if deleted_files:
        logger.info(f"Cleaned up {len(deleted_files)} empty files: {', '.join(deleted_files)}")
    else:
        logger.info("No empty files found to clean up")


def check_empty_outputs():
    """Check for empty output files and log errors."""
    logger = logging.getLogger(__name__)
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    if not os.path.exists(data_dir):
        logger.error(f"Data directory {data_dir} does not exist")
        return
    empty_files = []
    for file in os.listdir(data_dir):
        if not file.endswith(".md"):
            continue
        file_path = os.path.join(data_dir, file)
        if os.path.getsize(file_path) == 0:
            empty_files.append(file)
            logger.error(f"Empty output file detected: {file}")
        else:
            # Check if file only contains the header
            with open(file_path, "r") as f:
                content = f.read().strip()
                if content.count("\n") <= 1:  # Only header line
                    empty_files.append(file)
                    logger.error(f"Output file contains only header: {file}")
    if empty_files:
        logger.error(f"Found {len(empty_files)} empty or invalid output files: {', '.join(empty_files)}")
    else:
        logger.info("All output files contain data")


def run_scraper(scraper_class):
    """Run a single scraper with proper error handling and logging."""
    logger = logging.getLogger(__name__)
    try:
        scraper = scraper_class()
        logger.info(f"Starting scrape for {scraper.__class__.__name__}")
        scraper.scrape()
        logger.info(f"Completed scrape for {scraper.__class__.__name__}")
        return True
    except Exception as e:
        logger.error(f"Error running {scraper_class.__name__}: {str(e)}")
        return False


def main():
    # Set up logging first
    logger = setup_logging()
    logger.debug("Starting scraper application")
    parser = argparse.ArgumentParser(description="Market Intelligence Scraper")
    parser.add_argument("--cleanup", action="store_true", help="Clean up empty files after scraping")
    args = parser.parse_args()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "sites.yaml")
    scrapers = [
        GitHubScraper,
        RedditScraper,
        LobstersScraper,
        DevToScraper,
        HackerNewsScraper,
        ProductHuntScraper,
        IndieHackersScraper,
        HackerNoonScraper,
    ]
    # Run scrapers in parallel with rate limiting
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for scraper_class in scrapers:
            time.sleep(2)
            futures.append(executor.submit(run_scraper, scraper_class))
        success_count = sum(1 for future in as_completed(futures) if future.result())
        logger.info(f"Completed {success_count}/{len(scrapers)} scrapers successfully")

    # Clean up empty files if requested
    if args.cleanup:
        cleanup_empty_files()

    logger.info("Scraper application completed")


if __name__ == "__main__":
    main()
