"""
Centralized scraper registry for all available scrapers.
"""

from scraper.scrapers.devto import DevToScraper
from scraper.scrapers.github import GitHubScraper
from scraper.scrapers.hackernews_api import HackerNewsAPIScraper
from scraper.scrapers.hackernoon import HackerNoonScraper
from scraper.scrapers.hnrss import HNRSSScraper
from scraper.scrapers.lobsters import LobstersScraper
from scraper.scrapers.newsfeed import NewsFeedScraper
from scraper.scrapers.reddit import RedditScraper
from scraper.scrapers.reddit_optimized import OptimizedRedditScraper
from scraper.scrapers.tldr import TLDRScraper


class ScraperRegistry:
    """Registry for all available scrapers."""

    # Define all available scrapers
    SCRAPERS = {
        "github": GitHubScraper,
        "reddit": RedditScraper,
        "reddit_optimized": OptimizedRedditScraper,
        "lobsters": LobstersScraper,
        "newsfeed": NewsFeedScraper,
        "devto": DevToScraper,
        "hackernews_api": HackerNewsAPIScraper,
        "hackernoon": HackerNoonScraper,
        "hnrss": HNRSSScraper,
        "tldr": TLDRScraper,
    }

    @classmethod
    def get_scraper_class(cls, name: str):
        """Get scraper class by name."""
        return cls.SCRAPERS.get(name)

    @classmethod
    def get_all_scraper_names(cls):
        """Get list of all available scraper names."""
        return list(cls.SCRAPERS.keys())

    @classmethod
    def get_all_scraper_classes(cls):
        """Get list of all scraper classes."""
        return list(cls.SCRAPERS.values())

    @classmethod
    def get_scrapers_for_names(cls, names):
        """Get scraper classes for given names."""
        if "all" in names:
            return cls.get_all_scraper_classes()
        return [cls.SCRAPERS[name] for name in names if name in cls.SCRAPERS]
