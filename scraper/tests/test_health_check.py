"""
Tests for the health check system.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraper.core.config import ScraperConfig, set_config  # noqa: E402
from scraper.utils.health_check import HealthChecker, HealthCheckResult, HealthStatus, run_health_check  # noqa: E402


class TestHealthCheckResult(unittest.TestCase):
    """Test the HealthCheckResult dataclass."""

    def test_health_check_result_creation(self):
        """Test creating a health check result."""
        result = HealthCheckResult(name="test_check", status=HealthStatus.HEALTHY, message="Test passed")

        self.assertEqual(result.name, "test_check")
        self.assertEqual(result.status, HealthStatus.HEALTHY)
        self.assertEqual(result.message, "Test passed")
        self.assertIsNotNone(result.timestamp)

    def test_health_check_result_to_dict(self):
        """Test converting result to dictionary."""
        result = HealthCheckResult(name="test_check", status=HealthStatus.DEGRADED, message="Test warning", details={"key": "value"})

        data = result.to_dict()

        self.assertEqual(data["name"], "test_check")
        self.assertEqual(data["status"], "degraded")
        self.assertEqual(data["message"], "Test warning")
        self.assertEqual(data["details"]["key"], "value")
        self.assertIn("timestamp", data)


class TestHealthChecker(unittest.TestCase):
    """Test the HealthChecker class."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temp_dir.name)

        # Create project structure
        (self.project_root / "src" / "scraper" / "config").mkdir(parents=True)
        (self.project_root / "pyproject.toml").touch()

        # Create sites.yaml
        sites_config = """
github:
  url: "https://github.com/trending"
  selector: ".Box-row"
hackernews:
  url: "https://news.ycombinator.com"
  selector: ".athing"
"""
        (self.project_root / "src" / "scraper" / "config" / "sites.yaml").write_text(sites_config)

        # Set up configuration
        self.config = ScraperConfig(str(self.project_root))
        set_config(self.config)

        self.checker = HealthChecker()

    def tearDown(self):
        """Clean up."""
        self.temp_dir.cleanup()

    def test_check_filesystem_healthy(self):
        """Test filesystem check when everything is OK."""
        result = self.checker.check_filesystem()

        self.assertEqual(result.status, HealthStatus.HEALTHY)
        self.assertIn("Filesystem permissions OK", result.message)

    def test_check_filesystem_no_write_permission(self):
        """Test filesystem check with no write permission."""
        # Make data directory read-only
        self.config.data_dir.chmod(0o555)

        try:
            result = self.checker.check_filesystem()
            self.assertEqual(result.status, HealthStatus.UNHEALTHY)
            self.assertIn("Cannot write", result.message)
        finally:
            # Restore permissions for cleanup
            self.config.data_dir.chmod(0o755)

    def test_check_disk_space(self):
        """Test disk space check."""
        result = self.checker.check_disk_space()

        # Should always have some result
        self.assertIn(result.status, [HealthStatus.HEALTHY, HealthStatus.DEGRADED, HealthStatus.UNHEALTHY])
        self.assertIsNotNone(result.details)
        self.assertIn("free_gb", result.details)

    @patch("requests.head")
    def test_check_network_connectivity_all_healthy(self, mock_head):
        """Test network check when all services are reachable."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_head.return_value = mock_response

        result = self.checker.check_network_connectivity()

        self.assertEqual(result.status, HealthStatus.HEALTHY)
        self.assertIn("All services reachable", result.message)

    @patch("requests.head")
    def test_check_network_connectivity_some_failures(self, mock_head):
        """Test network check with some service failures."""
        # First call succeeds, second fails
        responses = [Mock(status_code=200), Mock(status_code=503)]
        mock_head.side_effect = responses

        result = self.checker.check_network_connectivity()

        self.assertEqual(result.status, HealthStatus.DEGRADED)
        self.assertIn("Some services unreachable", result.message)

    @patch("requests.get")
    def test_check_ollama_service_healthy(self, mock_get):
        """Test Ollama check when service is available."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"models": [{"name": "llama2"}, {"name": "codellama"}]}
        mock_get.return_value = mock_response

        result = self.checker.check_ollama_service()

        self.assertEqual(result.status, HealthStatus.HEALTHY)
        self.assertIn("2 models", result.message)

    @patch("requests.get")
    def test_check_ollama_service_not_running(self, mock_get):
        """Test Ollama check when service is not running."""
        import requests

        mock_get.side_effect = requests.exceptions.ConnectionError("Connection refused")

        result = self.checker.check_ollama_service()

        self.assertEqual(result.status, HealthStatus.DEGRADED)
        self.assertIn("not running", result.message)

    def test_check_configuration_healthy(self):
        """Test configuration check when valid."""
        result = self.checker.check_configuration()

        self.assertEqual(result.status, HealthStatus.HEALTHY)
        self.assertIn("2 sites", result.message)
        self.assertIn("github", result.details["sites"])
        self.assertIn("hackernews", result.details["sites"])

    def test_check_all(self):
        """Test running all health checks."""
        # Mock external dependencies
        with patch("requests.head") as mock_head:
            with patch("requests.get") as mock_get:
                # Mock network checks
                mock_head.return_value = Mock(status_code=200)

                # Mock Ollama check
                mock_get.return_value = Mock(status_code=200, json=lambda: {"models": []})

                overall_status, results = self.checker.check_all()

                # Should get results for all checks
                self.assertGreater(len(results), 5)

                # Overall status should be based on individual results
                self.assertIn(overall_status, [HealthStatus.HEALTHY, HealthStatus.DEGRADED, HealthStatus.UNHEALTHY])

                # Check that all results have required fields
                for result in results:
                    self.assertIsInstance(result, HealthCheckResult)
                    self.assertIsNotNone(result.name)
                    self.assertIsNotNone(result.status)
                    self.assertIsNotNone(result.message)


class TestHealthCheckIntegration(unittest.TestCase):
    """Integration tests for health check system."""

    def setUp(self):
        """Set up test environment."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temp_dir.name)

        # Create minimal project structure
        (self.project_root / "src" / "scraper" / "config").mkdir(parents=True)
        (self.project_root / "pyproject.toml").touch()
        (self.project_root / "src" / "scraper" / "config" / "sites.yaml").write_text("test: {}")

        self.config = ScraperConfig(str(self.project_root))
        set_config(self.config)

    def tearDown(self):
        """Clean up."""
        self.temp_dir.cleanup()

    def test_run_health_check_function(self):
        """Test the main run_health_check function."""
        with patch("requests.head") as mock_head:
            with patch("requests.get") as mock_get:
                # Mock external calls
                mock_head.return_value = Mock(status_code=200)
                mock_get.return_value = Mock(status_code=200, json=lambda: {"models": []})

                # Run without verbose
                status, results = run_health_check(verbose=False)

                self.assertIsInstance(status, HealthStatus)
                self.assertIsInstance(results, list)
                self.assertGreater(len(results), 0)

    def test_health_check_print_report(self):
        """Test report printing functionality."""
        checker = HealthChecker()

        test_results = [
            HealthCheckResult("test1", HealthStatus.HEALTHY, "All good"),
            HealthCheckResult("test2", HealthStatus.DEGRADED, "Some issues", {"detail": "value"}),
            HealthCheckResult("test3", HealthStatus.UNHEALTHY, "Failed"),
        ]

        # Should not raise any exceptions
        with patch("builtins.print"):
            checker.print_report(test_results)


if __name__ == "__main__":
    unittest.main()
