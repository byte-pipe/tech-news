"""
Tests for the centralized ScraperConfig class.
"""

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraper.core.config import ScraperConfig, get_config, set_config  # noqa: E402


class TestScraperConfig(unittest.TestCase):
    """Test cases for ScraperConfig class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary project root for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_root = Path(self.temp_dir.name)

        # Create the expected project structure
        (self.project_root / "scraper").mkdir(parents=True)
        (self.project_root / "pyproject.toml").touch()

        # Reset global config
        global _global_config
        import core.config

        core.config._global_config = None

    def tearDown(self):
        """Clean up test fixtures."""
        self.temp_dir.cleanup()

    def test_explicit_project_root(self):
        """Test ScraperConfig with explicit project root."""
        config = ScraperConfig(str(self.project_root))

        # Use resolve() to handle symlinks consistently
        self.assertEqual(config.project_root.resolve(), self.project_root.resolve())
        self.assertEqual(config.data_dir, self.project_root / "data")
        self.assertEqual(config.logs_dir, self.project_root / "logs")

    def test_project_root_validation(self):
        """Test project root validation."""
        # Valid project root should work
        config = ScraperConfig(str(self.project_root))
        self.assertTrue(config._is_valid_project_root(self.project_root))

        # Invalid project root should fail
        invalid_root = self.project_root / "nonexistent"
        self.assertFalse(config._is_valid_project_root(invalid_root))

    def test_environment_validation(self):
        """Test environment validation."""
        config = ScraperConfig(str(self.project_root))

        # Should create data and logs directories
        self.assertTrue(config.data_dir.exists())
        self.assertTrue(config.logs_dir.exists())

    def test_get_organized_paths(self):
        """Test organized paths generation."""
        config = ScraperConfig(str(self.project_root))

        # Test with specific date
        paths = config.get_organized_paths("2025-06-01")
        expected_base = config.data_dir / "2025-06-01"

        self.assertEqual(paths["base"], expected_base)
        self.assertEqual(paths["raw"], expected_base / "raw")
        self.assertEqual(paths["content"], expected_base / "content")
        self.assertEqual(paths["summaries"], expected_base / "summaries")
        self.assertEqual(paths["exports"], expected_base / "exports")

    def test_ensure_date_structure(self):
        """Test date structure creation."""
        config = ScraperConfig(str(self.project_root))

        paths = config.ensure_date_structure("2025-06-01")

        # All directories should be created
        for path_type, path in paths.items():
            if path_type != "base":
                self.assertTrue(path.exists())
                self.assertTrue(path.is_dir())

    def test_get_fallback_directory(self):
        """Test fallback directory creation."""
        config = ScraperConfig(str(self.project_root))

        fallback_dir = config.get_fallback_directory("content", "2025-06-01")
        expected_dir = config.data_dir / "2025-06-01" / "content"

        self.assertEqual(fallback_dir, expected_dir)
        self.assertTrue(fallback_dir.exists())

    def test_invalid_project_root_raises_error(self):
        """Test that invalid project root raises RuntimeError."""
        # Test with a path that definitely doesn't exist
        with self.assertRaises(RuntimeError):
            ScraperConfig("/this/path/definitely/does/not/exist/anywhere")

    def test_global_config_functions(self):
        """Test global configuration functions."""
        # Set explicit config
        config = ScraperConfig(str(self.project_root))
        set_config(config)

        # Get should return the same config
        retrieved_config = get_config()
        self.assertIs(retrieved_config, config)

    @patch.dict(os.environ, {"SCRAPER_PROJECT_ROOT": ""})
    def test_environment_variable_fallback(self):
        """Test environment variable fallback for project root."""
        # Set up environment variable
        test_root = str(self.project_root)
        with patch.dict(os.environ, {"SCRAPER_PROJECT_ROOT": test_root}):
            # Mock __file__ to simulate being in a different location
            with patch("core.config.__file__", "/tmp/fake_location.py"):
                with patch("pathlib.Path.cwd", return_value=Path("/tmp")):
                    config = ScraperConfig()
                    self.assertEqual(config.project_root.resolve(), self.project_root.resolve())


class TestScraperConfigIntegration(unittest.TestCase):
    """Integration tests for ScraperConfig with real project structure."""

    def test_real_project_detection(self):
        """Test that ScraperConfig can detect the real project structure."""
        # This should work when run from the project directory
        try:
            config = ScraperConfig()
            # Should successfully resolve project root
            self.assertTrue(config.project_root.exists())
            self.assertTrue((config.project_root / "src" / "scraper").exists())
        except RuntimeError:
            # This is acceptable if running tests in isolation
            self.skipTest("Cannot detect project root from test environment")

    def test_create_date_structure_real(self):
        """Test creating date structure in real project."""
        try:
            config = ScraperConfig()
            test_date = "2099-12-31"  # Use future date to avoid conflicts

            config.ensure_date_structure(test_date)

            # Clean up test directories

            test_dir = config.data_dir / test_date
            if test_dir.exists():
                shutil.rmtree(test_dir)

        except RuntimeError:
            self.skipTest("Cannot test with real project structure")


if __name__ == "__main__":
    unittest.main()
