"""
Tests for the DataOrganizer class.
"""

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# Add parent directory to path before other imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.data_organizer import DataOrganizer  # noqa: E402


class TestDataOrganizer(unittest.TestCase):
    """Test cases for DataOrganizer class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary directory as project root
        self.test_root = tempfile.mkdtemp()

        # Create a temporary data directory
        self.test_data_dir = os.path.join(self.test_root, "data")
        os.makedirs(self.test_data_dir, exist_ok=True)

        # Initialize DataOrganizer with test directory
        self.organizer = DataOrganizer(self.test_root)

    def tearDown(self):
        """Clean up test fixtures."""
        # Remove test directory and all its contents
        if os.path.exists(self.test_root):
            shutil.rmtree(self.test_root)

    def test_get_organized_paths(self):
        """Test get_organized_paths method creates correct path structure."""
        # Test with default date (today)
        paths = self.organizer.get_organized_paths()
        self.assertIn("base", paths)
        self.assertIn("raw", paths)
        self.assertIn("content", paths)
        self.assertIn("summaries", paths)

        # Verify paths are under the data directory
        for path_type, path in paths.items():
            self.assertTrue(str(path).startswith(str(self.test_data_dir)))

        # Test with specific date
        test_date = "2025-05-21"
        paths = self.organizer.get_organized_paths(test_date)
        self.assertTrue(str(paths["base"]).endswith(test_date))
        self.assertTrue(str(paths["raw"]).endswith(os.path.join(test_date, "raw")))

    def test_create_organized_structure(self):
        """Test create_organized_structure creates directories."""
        # Test with default date
        self.organizer.create_organized_structure()

        # Verify directories were created
        paths = self.organizer.get_organized_paths()
        for path_type, path in paths.items():
            self.assertTrue(path.exists())
            self.assertTrue(path.is_dir())

        # Test with specific date
        test_date = "2025-05-21"
        self.organizer.create_organized_structure(test_date)

        # Verify directories were created
        paths = self.organizer.get_organized_paths(test_date)
        for path_type, path in paths.items():
            self.assertTrue(path.exists())
            self.assertTrue(path.is_dir())

    def test_get_file_counts(self):
        """Test get_file_counts method."""
        # Create test date directory with files
        test_date = "2025-05-21"
        Path(self.test_data_dir) / test_date

        # Create directories and sample files
        paths = self.organizer.get_organized_paths(test_date)
        for path_type, path in paths.items():
            if path_type != "base":
                path.mkdir(parents=True, exist_ok=True)
                # Create some sample files
                for i in range(3):
                    sample_file = path / f"sample_{i}.txt"
                    with open(sample_file, "w") as f:
                        f.write(f"Sample content for {path_type} file {i}")

        # Get file counts
        counts = self.organizer.get_file_counts(test_date)

        # Verify counts
        self.assertEqual(counts["raw"], 3)
        self.assertEqual(counts["content"], 3)
        self.assertEqual(counts["summaries"], 3)

        # Test with nonexistent directory
        nonexistent_date = "2099-12-31"
        counts = self.organizer.get_file_counts(nonexistent_date)
        for category, count in counts.items():
            self.assertEqual(count, 0)

    def test_categorize_file(self):
        """Test _categorize_file method."""
        # Create test paths
        test_date = "2025-05-21"
        paths = self.organizer.get_organized_paths(test_date)

        # Test JSON file categorization
        raw_file = Path(self.test_data_dir) / test_date / "github-20250521-123456.json"
        category, target_path = self.organizer._categorize_file(raw_file, paths)
        self.assertEqual(category, "raw")
        self.assertEqual(target_path, paths["raw"] / "github-20250521-123456.json")

        # Test markdown content file categorization
        md_file = Path(self.test_data_dir) / test_date / "hackernews-20250521-123456.md"
        category, target_path = self.organizer._categorize_file(md_file, paths)
        self.assertEqual(category, "content")
        self.assertEqual(target_path, paths["content"] / "hackernews-20250521-123456.md")

        # Test summary file categorization - note that 'summary' must be in the filename
        summary_file = Path(self.test_data_dir) / test_date / "article-summary.md"
        category, target_path = self.organizer._categorize_file(summary_file, paths)
        self.assertEqual(category, "summaries")
        self.assertEqual(target_path, paths["summaries"] / "article-summary.md")

        # Test with different summary naming pattern
        summary_alt_file = Path(self.test_data_dir) / test_date / "test-summary.md"
        category, target_path = self.organizer._categorize_file(summary_alt_file, paths)
        self.assertEqual(category, "summaries")
        self.assertEqual(target_path, paths["summaries"] / "test-summary.md")

        # Test aggregated file categorization
        agg_file = Path(self.test_data_dir) / test_date / "github-2025-05-21-aggregated.json"
        category, target_path = self.organizer._categorize_file(agg_file, paths)
        # The categorize_file method actually puts JSON files in 'raw' even if they have 'aggregated' in the name
        # This is based on how the method is implemented in the DataOrganizer class
        self.assertEqual(category, "raw")
        self.assertEqual(target_path, paths["raw"] / "github-2025-05-21-aggregated.json")

        # Test uncategorized file
        other_file = Path(self.test_data_dir) / test_date / "random.txt"
        category, target_path = self.organizer._categorize_file(other_file, paths)
        self.assertIsNone(category)
        self.assertIsNone(target_path)

    def test_cleanup_empty_directories(self):
        """Test cleanup_empty_directories method."""
        # Create test date directory with empty subdirectories
        test_date = "2025-05-21"
        date_dir = Path(self.test_data_dir) / test_date
        date_dir.mkdir(parents=True, exist_ok=True)

        # Create empty directories
        empty_dir1 = date_dir / "empty1"
        empty_dir1.mkdir()
        empty_dir2 = date_dir / "empty2"
        empty_dir2.mkdir()

        # Create non-empty directory
        non_empty_dir = date_dir / "non_empty"
        non_empty_dir.mkdir()
        with open(non_empty_dir / "file.txt", "w") as f:
            f.write("Some content")

        # Run cleanup
        self.organizer.cleanup_empty_directories(test_date)

        # Verify empty directories were removed
        self.assertFalse(empty_dir1.exists())
        self.assertFalse(empty_dir2.exists())

        # Verify non-empty directory remains
        self.assertTrue(non_empty_dir.exists())

        # Test with nonexistent directory
        nonexistent_date = "2099-12-31"
        # This should not raise an exception
        self.organizer.cleanup_empty_directories(nonexistent_date)

    def test_organize_existing_data_simple(self):
        """Test organize_existing_data method with a simplified approach."""
        # Create test date directory with sample files
        test_date = "2025-05-21"
        date_dir = Path(self.test_data_dir) / test_date
        date_dir.mkdir(parents=True, exist_ok=True)

        # Create a raw JSON file
        github_json = date_dir / "github-20250521-123456.json"
        with open(github_json, "w") as f:
            f.write('{"name": "test"}')

        # Run organize
        result = self.organizer.organize_existing_data(test_date)

        # Verify JSON file was moved
        self.assertIn("github-20250521-123456.json", result["raw"])

        # Verify file is in the correct location
        paths = self.organizer.get_organized_paths(test_date)
        self.assertTrue((paths["raw"] / "github-20250521-123456.json").exists())

        # Test dry run mode
        # Create a new file to test dry run
        with open(date_dir / "test-dry-run.json", "w") as f:
            f.write('{"test": "dry run"}')

        # Run organize with dry_run=True
        result_dry = self.organizer.organize_existing_data(test_date, dry_run=True)

        # Verify file was not moved but is in the result
        self.assertIn("test-dry-run.json", result_dry["raw"])
        self.assertFalse((paths["raw"] / "test-dry-run.json").exists())
        self.assertTrue((date_dir / "test-dry-run.json").exists())

        # Test with nonexistent directory
        nonexistent_date = "2099-12-31"
        result_nonexistent = self.organizer.organize_existing_data(nonexistent_date)
        self.assertEqual(result_nonexistent, {})


if __name__ == "__main__":
    unittest.main()
