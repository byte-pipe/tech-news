"""Tests for the LinkTracker class."""

import csv
import os
import tempfile
import unittest
from unittest.mock import patch

from scraper.utils.link_tracker import COLUMNS, LinkTracker


class TestLinkTracker(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.tracker = LinkTracker(project_root=self.tmp_dir)
        # Create data dir so CSV path is valid
        os.makedirs(os.path.join(self.tmp_dir, "data"), exist_ok=True)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def _make_item(self, url="https://example.com", title="Test Article", **kwargs):
        item = {"url": url, "title": title, "description": "desc"}
        item.update(kwargs)
        return item

    def test_track_items_creates_csv(self):
        items = [self._make_item()]
        count = self.tracker.track_items(items, "github", "2026-04-20")
        assert count == 1
        assert os.path.exists(self.tracker.csv_path)

    def test_track_items_returns_count(self):
        items = [self._make_item(url="https://a.com"), self._make_item(url="https://b.com")]
        count = self.tracker.track_items(items, "github", "2026-04-20")
        assert count == 2

    def test_track_empty_list(self):
        count = self.tracker.track_items([], "github", "2026-04-20")
        assert count == 0

    def test_deduplicates_same_url_same_day(self):
        items = [self._make_item()]
        self.tracker.track_items(items, "github", "2026-04-20")
        count = self.tracker.track_items(items, "github", "2026-04-20")
        assert count == 0

    def test_allows_same_url_different_day(self):
        items = [self._make_item()]
        self.tracker.track_items(items, "github", "2026-04-20")
        count = self.tracker.track_items(items, "github", "2026-04-21")
        assert count == 1

    def test_csv_has_header(self):
        self.tracker.track_items([self._make_item()], "github", "2026-04-20")
        with open(self.tracker.csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            assert set(COLUMNS).issubset(set(reader.fieldnames))

    def test_skips_item_without_url(self):
        items = [{"title": "No URL", "description": "test"}]
        count = self.tracker.track_items(items, "github", "2026-04-20")
        assert count == 0

    def test_normalizes_score(self):
        items = [self._make_item(score=42)]
        self.tracker.track_items(items, "hn", "2026-04-20")
        with open(self.tracker.csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            row = next(reader)
        assert row["score"] == "42"

    def test_normalizes_stars_field(self):
        items = [self._make_item(stars=100)]
        self.tracker.track_items(items, "github", "2026-04-20")
        with open(self.tracker.csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            row = next(reader)
        assert row["score"] == "100"

    def test_normalizes_tags_list(self):
        items = [self._make_item(tags=["python", "ai"])]
        self.tracker.track_items(items, "devto", "2026-04-20")
        with open(self.tracker.csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            row = next(reader)
        assert "python" in row["tags"]
        assert "ai" in row["tags"]

    def test_description_truncated_at_300(self):
        long_desc = "x" * 500
        items = [self._make_item(description=long_desc)]
        self.tracker.track_items(items, "github", "2026-04-20")
        with open(self.tracker.csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            row = next(reader)
        assert len(row["description"]) <= 300

    def test_uses_today_when_date_not_provided(self):
        items = [self._make_item()]
        count = self.tracker.track_items(items, "github")
        assert count == 1

    def test_category_assigned(self):
        items = [self._make_item(title="Python machine learning tutorial")]
        self.tracker.track_items(items, "devto", "2026-04-20")
        with open(self.tracker.csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            row = next(reader)
        assert row["category"]  # some category assigned

    def test_load_existing_keys_on_second_tracker(self):
        items = [self._make_item()]
        self.tracker.track_items(items, "github", "2026-04-20")

        tracker2 = LinkTracker(project_root=self.tmp_dir)
        count = tracker2.track_items(items, "github", "2026-04-20")
        assert count == 0

    def test_load_existing_keys_handles_bad_csv(self):
        os.makedirs(os.path.dirname(self.tracker.csv_path), exist_ok=True)
        with open(self.tracker.csv_path, "w") as f:
            f.write("not,valid,csv\x00garbage")
        # Should not raise; returns empty set
        keys = self.tracker._load_existing_keys()
        assert isinstance(keys, set)

    def test_assign_category_with_matching_keyword(self):
        with patch.object(self.tracker, "_load_categories", return_value={"ai": {"keywords": ["machine learning", "neural"]}, "python": {"keywords": ["python"]}}):
            cat = self.tracker._assign_category("Python tutorial for beginners", "learn python")
        assert cat == "python"

    def test_assign_category_no_match_returns_uncategorized(self):
        with patch.object(self.tracker, "_load_categories", return_value={"ai": {"keywords": ["machine learning"]}}):
            cat = self.tracker._assign_category("banana smoothie recipe", "")
        assert cat == "uncategorized"


class TestLinkTrackerBackfill(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        from scraper.utils.link_tracker import LinkTracker
        self.tracker = LinkTracker(project_root=self.tmp_dir)
        os.makedirs(os.path.join(self.tmp_dir, "data"), exist_ok=True)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def test_backfill_from_json_files_empty_data_dir(self):
        total = self.tracker.backfill_from_json_files()
        assert total == 0

    def test_backfill_from_json_files_processes_json(self):
        import json
        date_dir = os.path.join(self.tmp_dir, "data", "2026-04-20")
        os.makedirs(date_dir, exist_ok=True)
        items = [{"url": "https://example.com/1", "title": "Test", "description": "desc"}]
        with open(os.path.join(date_dir, "github.json"), "w") as f:
            json.dump(items, f)

        total = self.tracker.backfill_from_json_files()
        assert total == 1

    def test_backfill_from_json_files_skips_non_list(self):
        import json
        date_dir = os.path.join(self.tmp_dir, "data", "2026-04-20")
        os.makedirs(date_dir, exist_ok=True)
        with open(os.path.join(date_dir, "config.json"), "w") as f:
            json.dump({"key": "value"}, f)

        total = self.tracker.backfill_from_json_files()
        assert total == 0

    def test_backfill_from_json_files_skips_url_registry(self):
        import json
        data_dir = os.path.join(self.tmp_dir, "data")
        with open(os.path.join(data_dir, "url_registry.json"), "w") as f:
            json.dump({}, f)

        total = self.tracker.backfill_from_json_files()
        assert total == 0

    def test_backfill_from_registry_no_registry_file(self):
        total = self.tracker.backfill_from_registry()
        assert total == 0

    def test_backfill_from_registry_no_csv(self):
        import json
        registry_path = os.path.join(self.tmp_dir, "data", "url_registry.json")
        with open(registry_path, "w") as f:
            json.dump({"urls": {"https://example.com": {"seen_count": 3}}}, f)

        total = self.tracker.backfill_from_registry()
        assert total == 0  # no CSV to update

    def test_backfill_from_registry_updates_seen_count(self):
        import json
        # Create CSV first
        self.tracker.track_items([{"url": "https://example.com", "title": "T"}], "github", "2026-04-20")

        # Create registry with higher seen_count
        registry_path = os.path.join(self.tmp_dir, "data", "url_registry.json")
        with open(registry_path, "w") as f:
            json.dump({"urls": {"https://example.com": {"seen_count": 5}}}, f)

        updated = self.tracker.backfill_from_registry()
        assert updated == 1


if __name__ == "__main__":
    unittest.main()
