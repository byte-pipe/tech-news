"""
Data models for the scraper system.
"""

from .scraped_data import GitHubItem, HackerNewsItem, LobstersItem, ScrapedItem, ScrapingResult, validate_scraped_data

__all__ = ["ScrapedItem", "ScrapingResult", "GitHubItem", "HackerNewsItem", "LobstersItem", "validate_scraped_data"]
