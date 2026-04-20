"""Tests for the URLRegistry class."""

import json
import os
import tempfile
import unittest

from scraper.utils.url_registry import URLRegistry, reset_registry_instance


class TestURLRegistry(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.registry_path = os.path.join(self.tmp_dir, "test_registry.json")
        self.registry = URLRegistry(registry_path=self.registry_path)
        reset_registry_instance()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tmp_dir, ignore_errors=True)
        reset_registry_instance()

    def test_new_registry_is_empty(self):
        assert not self.registry.is_processed("https://example.com")

    def test_mark_processed(self):
        self.registry.mark_processed("https://example.com", "github", title="Test")
        assert self.registry.is_processed("https://example.com")

    def test_get_entry_after_mark(self):
        self.registry.mark_processed("https://example.com", "github", title="My Article")
        entry = self.registry.get_entry("https://example.com")
        assert entry is not None
        assert entry["site_name"] == "github"
        assert entry["title"] == "My Article"
        assert entry["seen_count"] == 1

    def test_get_entry_unknown_url(self):
        assert self.registry.get_entry("https://unknown.com") is None

    def test_record_reappearance_increments_count(self):
        self.registry.mark_processed("https://example.com", "hn")
        self.registry.record_reappearance("https://example.com")
        entry = self.registry.get_entry("https://example.com")
        assert entry["seen_count"] == 2

    def test_record_reappearance_updates_last_seen(self):
        self.registry.mark_processed("https://example.com", "hn")
        self.registry.record_reappearance("https://example.com")
        entry = self.registry.get_entry("https://example.com")
        assert "last_seen" in entry

    def test_record_reappearance_unknown_url_is_noop(self):
        self.registry.record_reappearance("https://unknown.com")  # should not raise

    def test_update_entry(self):
        self.registry.mark_processed("https://example.com", "hn")
        self.registry.update_entry("https://example.com", summary_path="/path/to/summary.md")
        entry = self.registry.get_entry("https://example.com")
        assert entry["summary_path"] == "/path/to/summary.md"

    def test_update_entry_unknown_url_is_noop(self):
        self.registry.update_entry("https://unknown.com", summary_path="x")  # should not raise

    def test_persists_to_disk(self):
        self.registry.mark_processed("https://example.com", "site")
        new_registry = URLRegistry(registry_path=self.registry_path)
        assert new_registry.is_processed("https://example.com")

    def test_get_stats(self):
        self.registry.mark_processed("https://a.com", "github")
        self.registry.mark_processed("https://b.com", "hn")
        stats = self.registry.get_stats()
        assert stats["total_urls"] == 2
        assert stats["by_site"]["github"] == 1
        assert stats["by_site"]["hn"] == 1

    def test_loads_corrupt_file_fresh(self):
        with open(self.registry_path, "w") as f:
            f.write("not valid json")
        registry = URLRegistry(registry_path=self.registry_path)
        assert registry.get_stats()["total_urls"] == 0

    def test_seen_dates_tracking(self):
        self.registry.mark_processed("https://example.com", "hn")
        self.registry.record_reappearance("https://example.com")
        entry = self.registry.get_entry("https://example.com")
        assert isinstance(entry["seen_dates"], list)
        assert len(entry["seen_dates"]) >= 1

    def test_content_path_stored(self):
        self.registry.mark_processed("https://x.com", "hn", content_path="/data/content.md")
        entry = self.registry.get_entry("https://x.com")
        assert entry["content_path"] == "/data/content.md"

    def test_record_reappearance_adds_new_date_when_not_present(self):
        self.registry.mark_processed("https://example.com", "hn")
        # Override seen_dates to an old date so today triggers append
        entry = self.registry._registry["urls"]["https://example.com"]
        entry["seen_dates"] = ["2025-01-01"]
        self.registry.record_reappearance("https://example.com")
        entry = self.registry.get_entry("https://example.com")
        assert len(entry["seen_dates"]) == 2


if __name__ == "__main__":
    unittest.main()
