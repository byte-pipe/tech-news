"""Tests for the ScraperRegistry class."""

import unittest

from scraper.core.scraper_registry import ScraperRegistry


class TestScraperRegistry(unittest.TestCase):
    def test_get_scraper_class_github(self):
        cls = ScraperRegistry.get_scraper_class("github")
        assert cls is not None
        assert cls.__name__ == "GitHubScraper"

    def test_get_scraper_class_hackernews_api(self):
        cls = ScraperRegistry.get_scraper_class("hackernews_api")
        assert cls is not None

    def test_get_scraper_class_unknown(self):
        assert ScraperRegistry.get_scraper_class("nonexistent") is None

    def test_get_all_scraper_names(self):
        names = ScraperRegistry.get_all_scraper_names()
        assert isinstance(names, list)
        assert len(names) > 0
        assert "github" in names
        assert "hackernews_api" in names
        assert "reddit" in names

    def test_get_all_scraper_classes(self):
        classes = ScraperRegistry.get_all_scraper_classes()
        assert isinstance(classes, list)
        assert len(classes) > 0

    def test_get_scrapers_for_names_specific(self):
        classes = ScraperRegistry.get_scrapers_for_names(["github", "reddit"])
        assert len(classes) == 2

    def test_get_scrapers_for_names_all(self):
        all_classes = ScraperRegistry.get_all_scraper_classes()
        selected = ScraperRegistry.get_scrapers_for_names(["all"])
        assert selected == all_classes

    def test_get_scrapers_for_names_unknown_skipped(self):
        classes = ScraperRegistry.get_scrapers_for_names(["github", "nonexistent"])
        assert len(classes) == 1

    def test_scrapers_dict_has_expected_keys(self):
        expected = {"github", "reddit", "reddit_optimized", "lobsters", "newsfeed", "devto", "hackernews_api", "hnrss", "tldr"}
        assert expected.issubset(set(ScraperRegistry.SCRAPERS.keys()))


if __name__ == "__main__":
    unittest.main()
