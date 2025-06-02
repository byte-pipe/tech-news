"""
Tests for scraper_runner metrics integration.
"""

import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.scraper_runner import fetch_content_for_results, run_scraper, run_scrapers_parallel  # noqa: E402
from scrapers.base import BaseScraper  # noqa: E402
from utils.structured_logger import get_metrics_collector, reset_metrics  # noqa: E402


class MockScraper(BaseScraper):
    """Mock scraper for testing."""

    def __init__(self, test_mode=False, test_output_dir=None):
        super().__init__(test_mode=test_mode, test_output_dir=test_output_dir)
        self.url = "http://example.com"
        self.name = "mock"
        self.selector = "div"
        self.site_name = "mock"

    def _get_page(self, url):
        return "<html><div>Test content</div></html>"

    def _parse_html(self, html, selector):
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        return soup.select(selector)

    def _extract_data(self, items):
        return [{"title": "Test Item", "url": "http://example.com/test"}]


class TestScraperRunnerMetrics(unittest.TestCase):
    """Test metrics collection in scraper_runner."""

    def setUp(self):
        """Set up test fixtures."""
        reset_metrics()
        self.test_dir = tempfile.mkdtemp()
        self.metrics_collector = get_metrics_collector()

    def tearDown(self):
        """Clean up test fixtures."""
        # Clean up temp directory
        import shutil

        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    @patch("core.scraper_runner.logger")
    @patch("core.scraper_runner.structured_logger")
    def test_run_scraper_success_metrics(self, mock_structured_logger, mock_logger):
        """Test that successful scraper runs record metrics."""
        # Mock the scraper to return data
        with patch.object(MockScraper, "scrape", return_value=[{"title": "Item 1", "url": "http://example.com/1"}, {"title": "Item 2", "url": "http://example.com/2"}]):
            result = run_scraper(MockScraper, output_format="json", test_mode=True, test_output_dir=self.test_dir)

        self.assertTrue(result)

        # Check metrics were recorded
        metrics = self.metrics_collector.get_summary()
        self.assertEqual(metrics["scrapers"]["total_runs"], 1)
        self.assertEqual(metrics["scrapers"]["by_scraper"]["MockScraper"]["success"], 1)
        self.assertEqual(metrics["scrapers"]["by_scraper"]["MockScraper"]["items_total"], 2)
        self.assertEqual(metrics["items"]["total_scraped"], 2)

        # Check structured logger was used
        mock_structured_logger.log_scraper_result.assert_called_once()
        call_args = mock_structured_logger.log_scraper_result.call_args
        self.assertEqual(call_args[0][0], "MockScraper")  # scraper_name
        self.assertTrue(call_args[1]["success"])
        self.assertEqual(call_args[1]["items_count"], 2)

    @patch("core.scraper_runner.logger")
    @patch("core.scraper_runner.structured_logger")
    def test_run_scraper_failure_metrics(self, mock_structured_logger, mock_logger):
        """Test that failed scraper runs record metrics."""
        # Mock the scraper to raise an exception
        with patch.object(MockScraper, "scrape", side_effect=Exception("Test error")):
            result = run_scraper(MockScraper, output_format="json", test_mode=True, test_output_dir=self.test_dir)

        self.assertFalse(result)

        # Check metrics were recorded
        metrics = self.metrics_collector.get_summary()
        self.assertEqual(metrics["scrapers"]["total_runs"], 1)
        self.assertEqual(metrics["scrapers"]["by_scraper"]["MockScraper"]["failed"], 1)
        self.assertEqual(metrics["scrapers"]["by_scraper"]["MockScraper"]["success"], 0)
        self.assertEqual(len(metrics["errors"]), 1)
        self.assertIn("Test error", metrics["errors"][0]["error"])

        # Check structured logger was used
        mock_structured_logger.log_scraper_result.assert_called_once()
        call_args = mock_structured_logger.log_scraper_result.call_args
        self.assertEqual(call_args[0][0], "MockScraper")  # scraper_name
        self.assertFalse(call_args[1]["success"])
        self.assertEqual(call_args[1]["error"], "Test error")

    @patch("core.scraper_runner.logger")
    @patch("core.scraper_runner.structured_logger")
    @patch("core.scraper_runner.ContentFetcher")
    def test_fetch_content_metrics(self, mock_content_fetcher_class, mock_structured_logger, mock_logger):
        """Test that content fetching records HTTP metrics."""
        # Mock content fetcher
        mock_fetcher = MagicMock()
        mock_content_fetcher_class.return_value = mock_fetcher

        # Mock successful and failed fetches
        mock_fetcher.fetch_content.side_effect = [{"url": "http://example.com/1", "local_path": "/path/1"}, {"url": "http://example.com/2"}, Exception("Network error")]  # Success  # No local_path = failure  # Exception

        results = [{"title": "Item 1", "url": "http://example.com/1"}, {"title": "Item 2", "url": "http://example.com/2"}, {"title": "Item 3", "url": "http://example.com/3"}]

        with patch("time.sleep"):  # Skip delays in tests
            fetch_content_for_results("test_site", results)

        # Check HTTP request metrics
        metrics = self.metrics_collector.get_summary()
        self.assertEqual(metrics["http_requests"]["total"], 3)
        self.assertEqual(metrics["http_requests"]["success"], 1)
        self.assertEqual(metrics["http_requests"]["failed"], 2)

        # Check operation duration metrics
        self.assertIn("content_fetch", metrics["performance"]["by_operation"])
        self.assertEqual(metrics["performance"]["by_operation"]["content_fetch"]["count"], 2)  # Only 2 successful calls

    @patch("core.scraper_runner.logger")
    @patch("core.scraper_runner.structured_logger")
    def test_parallel_execution_metrics(self, mock_structured_logger, mock_logger):
        """Test that parallel execution records metrics."""

        # Create mock scrapers
        class SuccessScraper(MockScraper):
            pass

        # Override FailureScraper to properly work with the mock setup
        with patch("time.sleep"):  # Skip delays in tests
            # Mock one scraper to succeed and one to fail
            with patch.object(MockScraper, "scrape") as mock_scrape:
                mock_scrape.side_effect = [[{"title": "Success", "url": "http://example.com"}], Exception("Test failure")]  # First call succeeds  # Second call fails

                success_count, critical_failures = run_scrapers_parallel([MockScraper, MockScraper], output_format="json")  # Use same class but mock will vary behavior

        self.assertEqual(success_count, 1)
        # Critical failures should be empty since run_scraper catches exceptions
        # The failure is recorded in metrics but not in critical_failures

        # Check structured logger recorded parallel execution
        mock_structured_logger.log_metric.assert_called()
        metric_calls = [call for call in mock_structured_logger.log_metric.call_args_list if call[0][0] == "parallel_execution_complete"]
        self.assertEqual(len(metric_calls), 1)

        call_kwargs = metric_calls[0][1]
        self.assertEqual(call_kwargs["total_scrapers"], 2)
        self.assertEqual(call_kwargs["failed_scrapers"], 1)

    def test_metrics_summary(self):
        """Test metrics summary generation."""
        # Record various metrics
        self.metrics_collector.record_scraper_run("TestScraper", True, 10, 2.5)
        self.metrics_collector.record_scraper_run("TestScraper", False, 0, 1.0, "Error")
        self.metrics_collector.record_http_request(200, True, 0.5)
        self.metrics_collector.record_http_request(404, False, 0.3)
        self.metrics_collector.record_operation_duration("test_op", 1.5)

        summary = self.metrics_collector.get_summary()

        # Verify summary calculations
        self.assertEqual(summary["scrapers"]["total_runs"], 2)
        self.assertEqual(summary["scrapers"]["success_rate"], 50.0)
        self.assertEqual(summary["items"]["total_scraped"], 10)
        self.assertEqual(summary["http_requests"]["total"], 2)
        self.assertEqual(summary["errors_count"], 1)


if __name__ == "__main__":
    unittest.main()
