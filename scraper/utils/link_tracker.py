"""
CSV-based link tracker for analysis and visualization.

Maintains a single CSV file (data/links.csv) with all scraped links,
updated incrementally after each scrape run.
"""

import csv
import logging
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

import yaml

logger = logging.getLogger(__name__)

DEFAULT_CSV_PATH = "data/links.csv"

COLUMNS = [
    "url",
    "title",
    "source",
    "score",
    "comments",
    "author",
    "date_published",
    "date_scraped",
    "category",
    "tags",
    "description",
    "language",
    "seen_count",
]


class LinkTracker:
    """Append-only CSV tracker for scraped links."""

    def __init__(self, project_root: Optional[str] = None):
        if project_root is None:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.project_root = project_root
        self.csv_path = os.path.join(project_root, DEFAULT_CSV_PATH)
        self._categories = None
        self._existing_keys: Optional[set] = None

    # ------------------------------------------------------------------
    # Category assignment
    # ------------------------------------------------------------------

    def _load_categories(self) -> Dict[str, Any]:
        if self._categories is not None:
            return self._categories
        cat_path = os.path.join(self.project_root, "scraper", "config", "categories.yaml")
        try:
            with open(cat_path, "r", encoding="utf-8") as f:
                self._categories = yaml.safe_load(f).get("categories", {})
        except Exception:
            self._categories = {}
        return self._categories

    def _assign_category(self, title: str, description: str) -> str:
        categories = self._load_categories()
        searchable = (title + " " + description).lower()
        best_cat = "uncategorized"
        best_score = 0
        for cat_key, cat_def in categories.items():
            score = sum(1 for kw in cat_def.get("keywords", []) if kw.lower() in searchable)
            if score > best_score:
                best_score = score
                best_cat = cat_key
        return best_cat

    # ------------------------------------------------------------------
    # Dedup index
    # ------------------------------------------------------------------

    def _load_existing_keys(self) -> set:
        """Load (url, source, date_scraped) tuples from existing CSV for dedup."""
        if self._existing_keys is not None:
            return self._existing_keys
        self._existing_keys = set()
        if not os.path.exists(self.csv_path):
            return self._existing_keys
        try:
            with open(self.csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    key = (row.get("url", ""), row.get("source", ""), row.get("date_scraped", ""))
                    self._existing_keys.add(key)
        except Exception as e:
            logger.warning(f"Could not read existing CSV for dedup: {e}")
        return self._existing_keys

    # ------------------------------------------------------------------
    # Normalize a scraped item into a CSV row
    # ------------------------------------------------------------------

    def _normalize(self, item: Dict[str, Any], source: str, date_scraped: str) -> Dict[str, str]:
        title = str(item.get("title", "")).strip()
        description = str(item.get("description", "")).strip()

        # Score: different scrapers use different field names
        score = item.get("score", "") or item.get("stars", "") or item.get("today_stars", "") or item.get("reactions", "")
        score = str(score).replace(" reactions", "").strip()

        comments = str(item.get("comments", "")).replace("Comments ", "").replace(" comments", "").strip()

        tags = item.get("tags", [])
        if isinstance(tags, list):
            tags = ", ".join(str(t) for t in tags)

        category = self._assign_category(title, description)

        return {
            "url": item.get("url", ""),
            "title": title,
            "source": source or item.get("site_name", ""),
            "score": score,
            "comments": comments,
            "author": item.get("author", ""),
            "date_published": item.get("date", ""),
            "date_scraped": date_scraped,
            "category": category,
            "tags": tags,
            "description": description[:300],
            "language": item.get("language", ""),
            "seen_count": str(item.get("seen_count", 1)),
        }

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def track_items(self, items: List[Dict[str, Any]], source: str, date_scraped: Optional[str] = None) -> int:
        """Append new items to the CSV. Returns count of new rows added."""
        if not items:
            return 0

        if date_scraped is None:
            date_scraped = datetime.now().strftime("%Y-%m-%d")

        existing = self._load_existing_keys()
        file_exists = os.path.exists(self.csv_path)

        new_rows = []
        for item in items:
            row = self._normalize(item, source, date_scraped)
            key = (row["url"], row["source"], row["date_scraped"])
            if key not in existing and row["url"]:
                new_rows.append(row)
                existing.add(key)

        if not new_rows:
            return 0

        os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)
        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            # Write header if file is empty/new
            if f.tell() == 0:
                csv.DictWriter(f, fieldnames=COLUMNS).writeheader()
            csv.DictWriter(f, fieldnames=COLUMNS).writerows(new_rows)

        logger.info(f"Tracked {len(new_rows)} new links from {source} ({date_scraped})")
        return len(new_rows)

    def backfill_from_json_files(self) -> int:
        """Populate CSV from all existing JSON data files in data/."""
        import json

        data_dir = os.path.join(self.project_root, "data")
        total = 0

        # Walk all date directories (both YYYY-MM-DD and YYYY-MM/YYYY-MM-DD layouts)
        json_files = []
        for root, _dirs, files in os.walk(data_dir):
            for fname in files:
                if fname.endswith(".json") and fname != "url_registry.json":
                    fpath = os.path.join(root, fname)
                    # Skip raw/ subdirectories
                    if "/raw/" in fpath:
                        continue
                    json_files.append(fpath)

        json_files.sort()
        for fpath in json_files:
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    items = json.load(f)
                if not isinstance(items, list):
                    continue

                # Derive source from filename (e.g., github.json -> github, hackernews-api.json -> hackernews-api)
                fname = os.path.basename(fpath)
                source = fname.rsplit(".", 1)[0]

                # Derive date from directory name
                parent = os.path.basename(os.path.dirname(fpath))
                try:
                    datetime.strptime(parent, "%Y-%m-%d")
                    date_scraped = parent
                except ValueError:
                    date_scraped = ""

                added = self.track_items(items, source, date_scraped)
                total += added
            except Exception as e:
                logger.warning(f"Skipping {fpath}: {e}")

        return total

    def backfill_from_registry(self) -> int:
        """Enrich CSV with seen_count data from url_registry.json."""
        import json

        registry_path = os.path.join(self.project_root, "data", "url_registry.json")
        if not os.path.exists(registry_path):
            return 0

        with open(registry_path, "r", encoding="utf-8") as f:
            registry = json.load(f).get("urls", {})

        if not os.path.exists(self.csv_path):
            return 0

        # Read all rows, update seen_count, rewrite
        rows = []
        updated = 0
        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row.get("url", "")
                if url in registry:
                    reg_count = str(registry[url].get("seen_count", 1))
                    if row.get("seen_count", "1") != reg_count:
                        row["seen_count"] = reg_count
                        updated += 1
                rows.append(row)

        if updated > 0:
            tmp_path = self.csv_path + ".tmp"
            with open(tmp_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=COLUMNS)
                writer.writeheader()
                writer.writerows(rows)
            os.replace(tmp_path, self.csv_path)
            logger.info(f"Updated seen_count for {updated} rows from registry")

        return updated


# Singleton access
_tracker: Optional[LinkTracker] = None


def get_link_tracker(project_root: Optional[str] = None) -> LinkTracker:
    global _tracker
    if _tracker is None:
        _tracker = LinkTracker(project_root)
    return _tracker
