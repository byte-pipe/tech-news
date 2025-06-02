#!/usr/bin/env python3
"""
Dead simple daily scraper. Just run this.
"""

import sys
from datetime import datetime

from scraper.core.ai_processor import summarize_with_local_model
from scraper.core.logging_config import setup_logging
from scraper.core.scraper_registry import ScraperRegistry
from scraper.core.scraper_runner import run_scrapers_parallel


def main():
    """Get the fucking data."""
    logger = setup_logging()

    # Quick mode?
    model = "tinyllama:1.1b" if "--quick" in sys.argv else "gemma2:27b"

    logger.info(f"🚀 Daily scrape with {model}")

    # Scrape - use ALL working scrapers!
    scrapers = ["github", "hackernews_api", "devto", "hackernews", "hackernoon", "medium", "techcrunch", "technode", "venturebeat", "reddit", "reddit_optimized"]
    selected = ScraperRegistry.get_scrapers_for_names(scrapers)
    success, _ = run_scrapers_parallel(selected, "json", False, True, 10)

    if success == 0:
        logger.error("❌ Scraping failed")
        return 1

    # Summarize
    date = datetime.now().strftime("%Y-%m-%d")
    ok, files = summarize_with_local_model(date, model, True)

    logger.info(f"✅ Done. {len(files) if ok else 0} summaries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
