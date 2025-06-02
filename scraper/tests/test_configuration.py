"""
Tests for configuration validation.
"""

# flake8: noqa: E402

import os
import sys

# Add parent directory to path before other imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import glob
import unittest

from scrapers import base


class TestScraperConfiguration(unittest.TestCase):
    """Test cases for scraper configuration."""

    def setUp(self):
        """Set up test fixtures."""
        # Get all scraper modules in the scrapers directory
        scrapers_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scrapers")
        self.scraper_files = glob.glob(os.path.join(scrapers_dir, "*.py"))

        # Exclude base.py
        self.scraper_files = [f for f in self.scraper_files if not f.endswith("base.py") and not f.endswith("__init__.py")]

        # Import all scraper classes
        self.scraper_classes = []
        for file_path in self.scraper_files:
            module_name = os.path.basename(file_path)[:-3]  # Remove .py extension

            # Import the module dynamically
            try:
                module = __import__(f"scrapers.{module_name}", fromlist=["*"])

                # Find all classes in the module that inherit from BaseScraper
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, base.BaseScraper) and obj != base.BaseScraper:
                        self.scraper_classes.append((module_name, obj))
            except ImportError as e:
                print(f"Error importing {module_name}: {e}")

    def test_required_class_attributes(self):
        """Test that all scrapers have the required class attributes."""
        for module_name, scraper_class in self.scraper_classes:
            # Check SITE_NAME is set and not None
            self.assertIsNotNone(scraper_class.SITE_NAME, f"{module_name}.{scraper_class.__name__} must define SITE_NAME")

            # Check URL is set and not None
            self.assertIsNotNone(scraper_class.URL, f"{module_name}.{scraper_class.__name__} must define URL")

            # Check URL is a valid URL
            self.assertTrue(scraper_class.URL.startswith("http"), f"{module_name}.{scraper_class.__name__}.URL must be a valid URL")

            # Check SELECTOR is set (can be None for special scrapers)
            self.assertTrue(hasattr(scraper_class, "SELECTOR"), f"{module_name}.{scraper_class.__name__} must define SELECTOR")

    def test_instantiation(self):
        """Test that all scrapers can be instantiated without errors."""
        for module_name, scraper_class in self.scraper_classes:
            try:
                instance = scraper_class()
                self.assertIsInstance(instance, base.BaseScraper, f"{module_name}.{scraper_class.__name__} must inherit from BaseScraper")
            except Exception as e:
                self.fail(f"Failed to instantiate {module_name}.{scraper_class.__name__}: {e}")

    def test_extract_data_method(self):
        """Test that all scrapers implement the _extract_data method."""
        for module_name, scraper_class in self.scraper_classes:
            instance = scraper_class()

            # Get the method implementations
            extract_data = getattr(instance.__class__, "_extract_data")
            base_extract_data = getattr(base.BaseScraper, "_extract_data")

            # Check if the method is overridden
            self.assertIsNot(extract_data, base_extract_data, f"{module_name}.{scraper_class.__name__} must override _extract_data method")

    def test_standalone_execution(self):
        """Test that all scrapers have standalone execution capability."""
        for module_name, _ in self.scraper_classes:
            # Get the actual file path
            file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scrapers", f"{module_name}.py")

            # Read the file and check for the __main__ block
            with open(file_path, "r") as f:
                content = f.read()
                self.assertIn('if __name__ == "__main__"', content, f"Scraper {module_name}.py should have standalone execution capability with a __main__ block")


if __name__ == "__main__":
    unittest.main()
