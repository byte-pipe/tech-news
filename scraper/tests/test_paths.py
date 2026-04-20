"""Tests for path utility functions."""

import os
import tempfile
import unittest
from unittest.mock import patch

from scraper.utils.paths import (
    build_data_file_path,
    ensure_data_directory,
    ensure_directory,
    get_data_directory_path,
    get_project_root,
)


class TestGetProjectRoot(unittest.TestCase):
    def test_returns_string(self):
        result = get_project_root()
        assert isinstance(result, str)

    def test_is_absolute(self):
        result = get_project_root()
        assert os.path.isabs(result)

    def test_levels_up(self):
        this_file = os.path.abspath(__file__)
        result = get_project_root(start_path=this_file, levels_up=2)
        assert os.path.isdir(result)

    def test_zero_levels_returns_directory(self):
        this_file = os.path.abspath(__file__)
        result = get_project_root(start_path=this_file, levels_up=0)
        assert os.path.isabs(result)


class TestEnsureDirectory(unittest.TestCase):
    def test_creates_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            new_dir = os.path.join(tmp, "new_subdir")
            result = ensure_directory(new_dir)
            assert os.path.isdir(result)

    def test_returns_absolute_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = ensure_directory(tmp)
            assert os.path.isabs(result)

    def test_existing_directory_no_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            ensure_directory(tmp)  # should not raise


class TestEnsureDataDirectory(unittest.TestCase):
    def test_rejects_path_traversal(self):
        with self.assertRaises(ValueError):
            ensure_data_directory("../evil")

    def test_rejects_absolute_date_folder(self):
        with self.assertRaises(ValueError):
            ensure_data_directory("/etc/passwd")

    def test_creates_directory_with_valid_date(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            with patch("scraper.utils.paths.get_project_root", return_value=tmp):
                result = ensure_data_directory("2026-04-20")
            assert os.path.isdir(result)
            assert "2026-04-20" in result

    def test_creates_directory_with_subdir(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            with patch("scraper.utils.paths.get_project_root", return_value=tmp):
                result = ensure_data_directory("2026-04-20", "content")
            assert os.path.isdir(result)
            assert "content" in result

    def test_rejects_invalid_subdir(self):
        with self.assertRaises(ValueError):
            ensure_data_directory("2026-04-20", "../evil")


class TestBuildDataFilePath(unittest.TestCase):
    def test_builds_path_without_subdir(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            with patch("scraper.utils.paths.get_project_root", return_value=tmp):
                result = build_data_file_path("2026-04-20", "github.json")
            assert result.endswith("github.json")
            assert "2026-04-20" in result

    def test_builds_path_with_subdir(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            with patch("scraper.utils.paths.get_project_root", return_value=tmp):
                result = build_data_file_path("2026-04-20", "article.md", "content")
            assert result.endswith("article.md")
            assert "content" in result


class TestGetDataDirectoryPath(unittest.TestCase):
    def test_returns_path_with_date(self):
        result = get_data_directory_path("2026-04-20")
        assert "2026-04-20" in result

    def test_with_subdir(self):
        result = get_data_directory_path("2026-04-20", subdir="content")
        assert "content" in result

    def test_returns_string(self):
        result = get_data_directory_path("2026-04-20")
        assert isinstance(result, str)


if __name__ == "__main__":
    unittest.main()
