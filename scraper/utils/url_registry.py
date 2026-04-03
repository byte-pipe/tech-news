"""
Centralized URL registry to track previously processed URLs across all runs.

This prevents re-fetching and re-summarizing the same articles that appear
on multiple days or in multiple scraper runs.
"""

import json
import logging
import os
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

# Default registry file location
DEFAULT_REGISTRY_FILE = "data/url_registry.json"


class URLRegistry:
    """Simple JSON-based registry to track processed URLs."""

    def __init__(self, registry_path: Optional[str] = None, project_root: Optional[str] = None):
        """Initialize the URL registry.

        Args:
            registry_path: Path to the registry JSON file. If None, uses default.
            project_root: Project root directory. If None, auto-detected.
        """
        if project_root is None:
            # Get project root (3 levels up from this file)
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        self.project_root = project_root

        if registry_path is None:
            self.registry_path = os.path.join(project_root, DEFAULT_REGISTRY_FILE)
        else:
            self.registry_path = registry_path

        self._registry = self._load()

    def _load(self) -> dict:
        """Load the registry from disk."""
        if os.path.exists(self.registry_path):
            try:
                with open(self.registry_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    logger.debug(f"Loaded URL registry with {len(data.get('urls', {}))} entries")
                    return data
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load URL registry: {e}. Starting fresh.")
                return {"urls": {}, "metadata": {"created_at": datetime.now().isoformat()}}
        return {"urls": {}, "metadata": {"created_at": datetime.now().isoformat()}}

    def _save(self) -> None:
        """Save the registry to disk."""
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.registry_path), exist_ok=True)

        self._registry["metadata"]["updated_at"] = datetime.now().isoformat()
        self._registry["metadata"]["total_urls"] = len(self._registry["urls"])

        with open(self.registry_path, "w", encoding="utf-8") as f:
            json.dump(self._registry, f, indent=2, ensure_ascii=False)

    def is_processed(self, url: str) -> bool:
        """Check if a URL has already been processed.

        Args:
            url: The URL to check.

        Returns:
            True if the URL has been processed before, False otherwise.
        """
        return url in self._registry["urls"]

    def get_entry(self, url: str) -> Optional[dict]:
        """Get the registry entry for a URL.

        Args:
            url: The URL to look up.

        Returns:
            Dictionary with entry data if found, None otherwise.
        """
        return self._registry["urls"].get(url)

    def mark_processed(self, url: str, site_name: str, title: str = "", content_path: str = "", summary_path: str = "") -> None:
        """Mark a URL as processed.

        Args:
            url: The URL that was processed.
            site_name: The source site name.
            title: Optional title of the article.
            content_path: Optional path to the saved content file.
            summary_path: Optional path to the saved summary file.
        """
        self._registry["urls"][url] = {
            "first_seen": datetime.now().isoformat(),
            "site_name": site_name,
            "title": title,
            "content_path": content_path,
            "summary_path": summary_path,
            "seen_count": 1,
            "seen_dates": [datetime.now().strftime("%Y-%m-%d")],
        }
        self._save()
        logger.debug(f"Marked URL as processed: {url}")

    def record_reappearance(self, url: str) -> None:
        """Record that a URL has reappeared in scraping results.

        Args:
            url: The URL that reappeared.
        """
        if url in self._registry["urls"]:
            entry = self._registry["urls"][url]
            entry["seen_count"] = entry.get("seen_count", 1) + 1
            entry["last_seen"] = datetime.now().isoformat()

            # Track dates when this URL appeared
            today = datetime.now().strftime("%Y-%m-%d")
            seen_dates = entry.get("seen_dates", [])
            if today not in seen_dates:
                seen_dates.append(today)
                entry["seen_dates"] = seen_dates

            self._save()
            logger.debug(f"Recorded reappearance #{entry['seen_count']} for URL: {url}")

    def update_entry(self, url: str, **kwargs) -> None:
        """Update an existing registry entry.

        Args:
            url: The URL to update.
            **kwargs: Fields to update (e.g., summary_path, content_path).
        """
        if url in self._registry["urls"]:
            self._registry["urls"][url].update(kwargs)
            self._registry["urls"][url]["last_updated"] = datetime.now().isoformat()
            self._save()

    def get_stats(self) -> dict:
        """Get statistics about the registry.

        Returns:
            Dictionary with registry statistics.
        """
        urls = self._registry["urls"]
        sites = {}
        for entry in urls.values():
            site = entry.get("site_name", "unknown")
            sites[site] = sites.get(site, 0) + 1

        return {
            "total_urls": len(urls),
            "by_site": sites,
            "created_at": self._registry["metadata"].get("created_at"),
            "updated_at": self._registry["metadata"].get("updated_at"),
        }


# Global singleton instance
_registry_instance: Optional[URLRegistry] = None


def get_url_registry(project_root: Optional[str] = None) -> URLRegistry:
    """Get the global URL registry instance.

    Args:
        project_root: Optional project root to use.

    Returns:
        The global URLRegistry instance.
    """
    global _registry_instance
    if _registry_instance is None:
        _registry_instance = URLRegistry(project_root=project_root)
    return _registry_instance


def reset_registry_instance() -> None:
    """Reset the global registry instance (useful for testing)."""
    global _registry_instance
    _registry_instance = None
