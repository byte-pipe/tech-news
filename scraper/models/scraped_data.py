"""
Standardized data models for scraped content.
Ensures consistent data structures across all scrapers.
"""

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class ScrapedItem:
    """
    Standard data model for a single scraped item.
    All scrapers should return data in this format.
    """

    # Required fields
    title: str
    url: str

    # Optional common fields
    description: Optional[str] = None
    author: Optional[str] = None
    date: Optional[datetime] = None
    tags: Optional[List[str]] = None

    # Site-specific fields (flexible metadata)
    metadata: Optional[Dict[str, Any]] = None

    # Content-related fields
    local_path: Optional[str] = None  # Path to saved content
    content_hash: Optional[str] = None  # For deduplication

    # Source tracking
    source_site: Optional[str] = None
    scraped_at: Optional[datetime] = None

    def __post_init__(self):
        """Initialize computed fields after creation."""
        if self.scraped_at is None:
            self.scraped_at = datetime.now()

        if self.metadata is None:
            self.metadata = {}

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary for JSON serialization.
        Handles datetime serialization properly.
        """
        data = asdict(self)

        # Convert datetime objects to ISO strings
        if self.date:
            data["date"] = self.date.isoformat()
        if self.scraped_at:
            data["scraped_at"] = self.scraped_at.isoformat()

        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ScrapedItem":
        """
        Create ScrapedItem from dictionary.
        Handles datetime parsing from ISO strings.
        """
        # Parse datetime fields
        if "date" in data and data["date"]:
            if isinstance(data["date"], str):
                data["date"] = datetime.fromisoformat(data["date"])

        if "scraped_at" in data and data["scraped_at"]:
            if isinstance(data["scraped_at"], str):
                data["scraped_at"] = datetime.fromisoformat(data["scraped_at"])

        return cls(**data)

    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> "ScrapedItem":
        """Create ScrapedItem from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)


@dataclass
class ScrapingResult:
    """
    Standard result container for scraping operations.
    Provides consistent structure for success/failure reporting.
    """

    success: bool
    items: List[ScrapedItem]
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        """Initialize computed fields."""
        if self.metadata is None:
            self.metadata = {}

        # Add statistics
        self.metadata.update({"items_count": len(self.items), "scraped_at": datetime.now().isoformat()})

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {"success": self.success, "items": [item.to_dict() for item in self.items], "error_message": self.error_message, "metadata": self.metadata}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ScrapingResult":
        """Create ScrapingResult from dictionary."""
        items = [ScrapedItem.from_dict(item_data) for item_data in data.get("items", [])]

        return cls(success=data.get("success", False), items=items, error_message=data.get("error_message"), metadata=data.get("metadata", {}))


@dataclass
class GitHubItem(ScrapedItem):
    """
    GitHub-specific scraped item with standard metadata structure.
    """

    def __post_init__(self):
        super().__post_init__()
        self.source_site = "github"

        # Standardize GitHub-specific fields in metadata
        if not self.metadata:
            self.metadata = {}

        # Ensure GitHub metadata is properly structured
        github_fields = ["stars", "forks", "today_stars", "language"]
        for field in github_fields:
            if field not in self.metadata:
                self.metadata[field] = None


@dataclass
class HackerNewsItem(ScrapedItem):
    """
    HackerNews-specific scraped item with standard metadata structure.
    """

    def __post_init__(self):
        super().__post_init__()
        self.source_site = "hackernews"

        # Standardize HackerNews-specific fields in metadata
        if not self.metadata:
            self.metadata = {}

        # Ensure HN metadata is properly structured
        hn_fields = ["score", "points", "comments_count", "rank"]
        for field in hn_fields:
            if field not in self.metadata:
                self.metadata[field] = None


@dataclass
class LobstersItem(ScrapedItem):
    """
    Lobsters-specific scraped item with standard metadata structure.
    """

    def __post_init__(self):
        super().__post_init__()
        self.source_site = "lobsters"

        # Standardize Lobsters-specific fields in metadata
        if not self.metadata:
            self.metadata = {}

        # Ensure Lobsters metadata is properly structured
        lobsters_fields = ["score", "comments_count"]
        for field in lobsters_fields:
            if field not in self.metadata:
                self.metadata[field] = None


def validate_scraped_data(items: List[Dict[str, Any]]) -> List[ScrapedItem]:
    """
    Validate and convert raw scraped data to standard ScrapedItem format.

    Args:
        items: List of raw dictionaries from scrapers

    Returns:
        List of validated ScrapedItem objects

    Raises:
        ValueError: If required fields are missing
    """
    validated_items = []

    for i, item in enumerate(items):
        try:
            # Check required fields
            if "title" not in item or not item["title"]:
                raise ValueError(f"Item {i}: Missing required field 'title'")
            if "url" not in item or not item["url"]:
                raise ValueError(f"Item {i}: Missing required field 'url'")

            # Convert to ScrapedItem
            scraped_item = ScrapedItem.from_dict(item)
            validated_items.append(scraped_item)

        except Exception as e:
            raise ValueError(f"Item {i}: Validation failed - {str(e)}")

    return validated_items
