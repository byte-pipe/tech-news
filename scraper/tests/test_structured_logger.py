"""
Tests for the structured logging system.
"""

import json
import os
import sys
import time
import unittest
from unittest.mock import patch

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraper.utils.structured_logger import StructuredLogger, get_metrics_collector, reset_metrics, timed_operation  # noqa: E402


class TestStructuredLogger(unittest.TestCase):
    """Test the StructuredLogger class."""

    def setUp(self):
        """Set up test fixtures."""
        self.logger = StructuredLogger("test_logger")

    def test_format_log_entry(self):
        """Test log entry formatting."""
        entry = self.logger._format_log_entry("INFO", "Test message", custom_field="value")

        self.assertEqual(entry["level"], "INFO")
        self.assertEqual(entry["message"], "Test message")
        self.assertEqual(entry["logger"], "test_logger")
        self.assertEqual(entry["custom_field"], "value")
        self.assertIn("timestamp", entry)

    def test_add_context(self):
        """Test adding persistent context."""
        self.logger.add_context(user="test_user", session="abc123")

        entry = self.logger._format_log_entry("INFO", "Test message")

        self.assertEqual(entry["context"]["user"], "test_user")
        self.assertEqual(entry["context"]["session"], "abc123")

    def test_with_context_manager(self):
        """Test temporary context manager."""
        self.logger.add_context(persistent="value")

        with self.logger.with_context(temporary="temp_value"):
            entry = self.logger._format_log_entry("INFO", "Inside context")
            self.assertEqual(entry["context"]["persistent"], "value")
            self.assertEqual(entry["context"]["temporary"], "temp_value")

        # After context, temporary should be gone
        entry = self.logger._format_log_entry("INFO", "Outside context")
        self.assertEqual(entry["context"]["persistent"], "value")
        self.assertNotIn("temporary", entry["context"])

    def test_timer_functionality(self):
        """Test timer start/stop functionality."""
        self.logger.start_timer("test_operation")
        time.sleep(0.1)  # Sleep for 100ms
        elapsed = self.logger.stop_timer("test_operation")

        self.assertIsNotNone(elapsed)
        self.assertGreater(elapsed, 0.09)  # Should be at least 90ms
        self.assertLess(elapsed, 0.2)  # But less than 200ms

    @patch("logging.Logger.info")
    def test_timer_context_manager_success(self, mock_info):
        """Test timer context manager for successful operations."""
        with self.logger.timer("test_operation"):
            time.sleep(0.05)

        # Should have logged start and completion
        self.assertEqual(mock_info.call_count, 2)

        # Check the completion log
        completion_call = mock_info.call_args_list[1]
        log_data = json.loads(completion_call[0][0])
        self.assertEqual(log_data["status"], "completed")
        self.assertEqual(log_data["operation"], "test_operation")
        self.assertIn("duration_seconds", log_data)

    @patch("logging.Logger.error")
    @patch("logging.Logger.info")
    def test_timer_context_manager_failure(self, mock_info, mock_error):
        """Test timer context manager for failed operations."""
        with self.assertRaises(ValueError):
            with self.logger.timer("test_operation"):
                raise ValueError("Test error")

        # Should have logged start (info) and failure (error)
        self.assertEqual(mock_info.call_count, 1)
        self.assertEqual(mock_error.call_count, 1)

        # Check the error log
        error_call = mock_error.call_args_list[0]
        log_data = json.loads(error_call[0][0])
        self.assertEqual(log_data["status"], "failed")
        self.assertEqual(log_data["error"], "Test error")
        self.assertEqual(log_data["error_type"], "ValueError")

    @patch("logging.Logger.info")
    def test_log_metric(self, mock_info):
        """Test metric logging."""
        self.logger.log_metric("items_scraped", 42, scraper="github", status="success")

        mock_info.assert_called_once()
        log_data = json.loads(mock_info.call_args[0][0])

        self.assertEqual(log_data["metric_name"], "items_scraped")
        self.assertEqual(log_data["metric_value"], 42)
        self.assertEqual(log_data["scraper"], "github")
        self.assertEqual(log_data["status"], "success")

    @patch("logging.Logger.info")
    def test_log_scraper_result(self, mock_info):
        """Test scraper result logging."""
        self.logger.log_scraper_result("github", success=True, items_count=25, duration=3.14)

        mock_info.assert_called_once()
        log_data = json.loads(mock_info.call_args[0][0])

        self.assertEqual(log_data["scraper"], "github")
        self.assertTrue(log_data["success"])
        self.assertEqual(log_data["items_count"], 25)
        self.assertEqual(log_data["duration_seconds"], 3.14)


class TestTimedOperationDecorator(unittest.TestCase):
    """Test the timed_operation decorator."""

    def setUp(self):
        """Set up test fixtures."""
        self.logger = StructuredLogger("test_logger")

    @patch("logging.Logger.info")
    def test_timed_operation_decorator(self, mock_info):
        """Test the timed operation decorator."""

        @timed_operation(self.logger, "test_function")
        def test_function(x, y):
            return x + y

        result = test_function(2, 3)

        self.assertEqual(result, 5)
        # Should log start and completion
        self.assertEqual(mock_info.call_count, 2)


class TestMetricsCollector(unittest.TestCase):
    """Test the MetricsCollector class."""

    def setUp(self):
        """Set up test fixtures."""
        reset_metrics()
        self.collector = get_metrics_collector()

    def test_record_scraper_run_success(self):
        """Test recording successful scraper run."""
        self.collector.record_scraper_run("github", success=True, items_count=10, duration=2.5)

        metrics = self.collector.metrics

        self.assertEqual(metrics["scrapers"]["github"]["runs"], 1)
        self.assertEqual(metrics["scrapers"]["github"]["success"], 1)
        self.assertEqual(metrics["scrapers"]["github"]["items_total"], 10)
        self.assertEqual(metrics["scrapers"]["github"]["total_duration"], 2.5)
        self.assertEqual(metrics["items"]["total_scraped"], 10)

    def test_record_scraper_run_failure(self):
        """Test recording failed scraper run."""
        self.collector.record_scraper_run("hackernews", success=False, duration=1.0, error="Network timeout")

        metrics = self.collector.metrics

        self.assertEqual(metrics["scrapers"]["hackernews"]["runs"], 1)
        self.assertEqual(metrics["scrapers"]["hackernews"]["failed"], 1)
        self.assertEqual(len(metrics["errors"]), 1)
        self.assertEqual(metrics["errors"][0]["error"], "Network timeout")

    def test_record_http_request(self):
        """Test recording HTTP request metrics."""
        self.collector.record_http_request(status_code=200, success=True)
        self.collector.record_http_request(status_code=404, success=False)
        self.collector.record_http_request(status_code=200, success=True)

        metrics = self.collector.metrics["http_requests"]

        self.assertEqual(metrics["total"], 3)
        self.assertEqual(metrics["success"], 2)
        self.assertEqual(metrics["failed"], 1)
        self.assertEqual(metrics["by_status"]["200"], 2)
        self.assertEqual(metrics["by_status"]["404"], 1)

    def test_record_operation_duration(self):
        """Test recording operation durations."""
        self.collector.record_operation_duration("fetch_page", 1.0)
        self.collector.record_operation_duration("fetch_page", 2.0)
        self.collector.record_operation_duration("fetch_page", 1.5)

        op_metrics = self.collector.metrics["performance"]["by_operation"]["fetch_page"]

        self.assertEqual(op_metrics["count"], 3)
        self.assertEqual(op_metrics["total_duration"], 4.5)
        self.assertEqual(op_metrics["min_duration"], 1.0)
        self.assertEqual(op_metrics["max_duration"], 2.0)

    def test_get_summary(self):
        """Test getting metrics summary."""
        # Record some metrics
        self.collector.record_scraper_run("github", True, 10, 2.0)
        self.collector.record_scraper_run("hackernews", True, 20, 3.0)
        self.collector.record_scraper_run("lobsters", False, 0, 1.0, "Error")

        summary = self.collector.get_summary()

        self.assertEqual(summary["scrapers"]["total_runs"], 3)
        self.assertAlmostEqual(summary["scrapers"]["success_rate"], 66.67, places=1)
        self.assertEqual(summary["items"]["total_scraped"], 30)
        self.assertEqual(summary["errors_count"], 1)

    def test_global_metrics_collector(self):
        """Test global metrics collector functionality."""
        collector1 = get_metrics_collector()
        collector2 = get_metrics_collector()

        # Should be the same instance
        self.assertIs(collector1, collector2)

        # Reset should create new instance
        reset_metrics()
        collector3 = get_metrics_collector()
        self.assertIsNot(collector1, collector3)


if __name__ == "__main__":
    unittest.main()
