"""Tests for the runner utility module."""

import unittest
from unittest.mock import MagicMock, patch


class TestRunScraper(unittest.TestCase):
    def test_run_scraper_calls_scrape(self):
        from scraper.utils.runner import run_scraper

        mock_scraper_instance = MagicMock()
        mock_class = MagicMock(return_value=mock_scraper_instance)

        with patch("scraper.utils.runner.configure_scraper_logging"):
            run_scraper(mock_class, output_format="markdown")

        mock_class.assert_called_once_with(test_mode=False, test_output_dir=None)
        mock_scraper_instance.scrape.assert_called_once_with(output_format="markdown")

    def test_run_scraper_test_mode(self):
        from scraper.utils.runner import run_scraper

        mock_scraper_instance = MagicMock()
        mock_class = MagicMock(return_value=mock_scraper_instance)

        with patch("scraper.utils.runner.configure_scraper_logging"):
            run_scraper(mock_class, test_mode=True, test_output_dir="/tmp/test")

        mock_class.assert_called_once_with(test_mode=True, test_output_dir="/tmp/test")

    def test_run_scraper_json_format(self):
        from scraper.utils.runner import run_scraper

        mock_scraper_instance = MagicMock()
        mock_class = MagicMock(return_value=mock_scraper_instance)

        with patch("scraper.utils.runner.configure_scraper_logging"):
            run_scraper(mock_class, output_format="json")

        mock_scraper_instance.scrape.assert_called_once_with(output_format="json")

    def test_run_scraper_configures_logging(self):
        from scraper.utils.runner import run_scraper

        mock_class = MagicMock(return_value=MagicMock())

        with patch("scraper.utils.runner.configure_scraper_logging") as mock_log:
            run_scraper(mock_class)

        mock_log.assert_called_once()


if __name__ == "__main__":
    unittest.main()
