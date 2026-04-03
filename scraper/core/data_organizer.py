"""
Data organization utilities for consistent file structure.
"""

import logging
import shutil
from datetime import datetime
from pathlib import Path

from .config import get_config

logger = logging.getLogger(__name__)


class DataOrganizer:
    """Manages consistent data organization and file structure."""

    def __init__(self, config_or_root=None):
        """Initialize with consistent configuration.

        Args:
            config_or_root: Either a ScraperConfig instance, a path string, or None.
                           If None, uses get_config()
                           If string/Path, creates simple configuration (for backward compatibility)
                           If ScraperConfig, uses that config
        """
        if config_or_root is None:
            # New default: use global config
            config = get_config()
            self.config = config
            self.project_root = config.project_root
            self.data_root = config.data_dir
        elif isinstance(config_or_root, (str, Path)):
            # Backward compatibility: simple path-based initialization
            self.project_root = Path(config_or_root)
            self.data_root = self.project_root / "data"
            self.config = None
        else:
            # New approach: use provided config
            self.config = config_or_root
            self.project_root = config_or_root.project_root
            self.data_root = config_or_root.data_dir

    def get_organized_paths(self, date_str=None):
        """Get clean, organized directory structure for a date.

        Args:
            date_str: Date string in YYYY-MM-DD format (default: today)

        Returns:
            dict: Organized paths for different data types
        """
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")

        date_dir = self.data_root / date_str

        return {
            "base": date_dir,
            "raw": date_dir / "raw",  # Raw scraped data (JSON/CSV)
            "content": date_dir / "content",  # Fetched article content
            "summaries": date_dir / "summaries",  # AI summaries (all models)
            "summaries_local": date_dir / "summaries_local",  # Local model summaries
            "exports": date_dir / "exports",  # Aggregated exports
        }

    def create_organized_structure(self, date_str=None, directories=None):
        """Create the organized directory structure.

        Args:
            date_str: Date string in YYYY-MM-DD format (default: today)
            directories: List of directory types to create. If None, creates only 'base' and 'raw'
                        Available types: 'base', 'raw', 'content', 'summaries', 'summaries_local', 'exports'
        """
        paths = self.get_organized_paths(date_str)

        # Default to only creating essential directories
        if directories is None:
            directories = ["base", "raw"]

        for dir_type in directories:
            if dir_type in paths:
                path = paths[dir_type]
                path.mkdir(parents=True, exist_ok=True)
                logger.debug(f"Ensured {dir_type} directory exists: {path}")
            else:
                logger.warning(f"Unknown directory type: {dir_type}")

    def ensure_directory(self, date_str, directory_type):
        """Ensure a specific directory exists on-demand.

        Args:
            date_str: Date string in YYYY-MM-DD format
            directory_type: Type of directory ('raw', 'content', 'summaries', etc.)

        Returns:
            Path: The created directory path
        """
        paths = self.get_organized_paths(date_str)
        if directory_type not in paths:
            raise ValueError(f"Unknown directory type: {directory_type}")

        path = paths[directory_type]
        path.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured {directory_type} directory exists: {path}")
        return path

    def organize_existing_data(self, date_str=None, dry_run=False):
        """Reorganize existing chaotic data into clean structure.

        Args:
            date_str: Date string in YYYY-MM-DD format (default: today)
            dry_run: If True, only show what would be moved

        Returns:
            dict: Summary of what was moved
        """
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")

        date_dir = self.data_root / date_str
        if not date_dir.exists():
            logger.info(f"No data directory found for {date_str}")
            return {}

        paths = self.get_organized_paths(date_str)
        moved_files = {"raw": [], "content": [], "summaries": [], "summaries_local": [], "exports": []}

        # Create organized structure first
        if not dry_run:
            self.create_organized_structure(date_str)

        # Process all files in the date directory
        for item in date_dir.iterdir():
            if item.is_file():
                target_category, target_path = self._categorize_file(item, paths)

                if target_category and target_path != item:
                    action = "WOULD MOVE" if dry_run else "MOVING"
                    logger.info(f"{action}: {item.name} → {target_category}/{target_path.name}")

                    if not dry_run:
                        # Ensure target directory exists
                        target_path.parent.mkdir(parents=True, exist_ok=True)

                        # Handle conflicts by adding timestamp
                        if target_path.exists():
                            timestamp = datetime.now().strftime("%H%M%S")
                            stem = target_path.stem
                            suffix = target_path.suffix
                            target_path = target_path.parent / f"{stem}-{timestamp}{suffix}"

                        shutil.move(str(item), str(target_path))

                    moved_files[target_category].append(item.name)

        # Handle existing directories with consistent names
        self._organize_existing_directories(date_dir, paths, dry_run, moved_files)

        return moved_files

    def _categorize_file(self, file_path, organized_paths):
        """Categorize a file and determine its target location.

        Args:
            file_path: Path object of the file
            organized_paths: Dict of organized directory paths

        Returns:
            tuple: (category, target_path) or (None, None) if no move needed
        """
        filename = file_path.name

        # Raw scraped data (JSON/CSV files with timestamps)
        if (filename.endswith(".json") or filename.endswith(".csv")) and "-" in filename:
            if "summary" not in filename.lower():
                return "raw", organized_paths["raw"] / filename

        # Content files (markdown files with content)
        elif filename.endswith(".md") and ("content" in str(file_path.parent) or any(site in filename for site in ["hackernews", "github", "devto", "lobsters"])):
            return "content", organized_paths["content"] / filename

        # Summary files
        elif "summary" in filename.lower() and filename.endswith(".md"):
            return "summaries", organized_paths["summaries"] / filename

        # Skip aggregated/report files - no longer needed
        elif "aggregated" in filename or "report" in filename:
            return None, None

        return None, None

    def _organize_existing_directories(self, date_dir, organized_paths, dry_run, moved_files):
        """Handle existing directories like summaries/, summaries_local/, etc."""

        # Merge summaries and summaries_local into single summaries directory
        for old_dir_name in ["summaries", "summaries_local"]:
            old_dir = date_dir / old_dir_name
            if old_dir.exists() and old_dir.is_dir():
                target_dir = organized_paths["summaries"]

                for file_path in old_dir.iterdir():
                    if file_path.is_file():
                        target_file = target_dir / file_path.name

                        # Handle naming conflicts
                        if target_file.exists():
                            # Add model type to differentiate
                            model_type = "local" if "local" in old_dir_name else "ci"
                            stem = target_file.stem
                            suffix = target_file.suffix
                            target_file = target_dir / f"{stem}-{model_type}{suffix}"

                        action = "WOULD MOVE" if dry_run else "MOVING"
                        logger.info(f"{action}: {old_dir_name}/{file_path.name} → summaries/{target_file.name}")

                        if not dry_run:
                            target_dir.mkdir(parents=True, exist_ok=True)
                            shutil.move(str(file_path), str(target_file))

                        moved_files["summaries"].append(f"{old_dir_name}/{file_path.name}")

                # Remove empty directory
                if not dry_run and old_dir.exists():
                    try:
                        old_dir.rmdir()
                        logger.info(f"Removed empty directory: {old_dir_name}")
                    except OSError:
                        logger.warning(f"Could not remove {old_dir_name} (not empty)")

    def cleanup_empty_directories(self, date_str=None):
        """Remove empty directories in the date folder."""
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")

        date_dir = self.data_root / date_str
        if not date_dir.exists():
            return

        # Remove empty subdirectories
        for item in date_dir.iterdir():
            if item.is_dir():
                try:
                    if not any(item.iterdir()):  # Directory is empty
                        item.rmdir()
                        logger.info(f"Removed empty directory: {item.name}")
                except OSError:
                    pass  # Directory not empty or permission issue

    def get_file_counts(self, date_str=None):
        """Get counts of files in each organized category.

        Returns:
            dict: File counts by category
        """
        paths = self.get_organized_paths(date_str)
        counts = {}

        for category, path in paths.items():
            if category == "base":
                continue

            if path.exists():
                counts[category] = len([f for f in path.iterdir() if f.is_file()])
            else:
                counts[category] = 0

        return counts

    # Removed ensure_exports_structure method - exports no longer needed
