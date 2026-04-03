"""
Centralized configuration management for the scraper system.
Provides single source of truth for paths, settings, and validation.
"""

import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class ScraperConfig:
    """
    Centralized configuration management for the scraper system.
    Eliminates path resolution chaos and provides single source of truth.
    """

    def __init__(self, project_root: Optional[str] = None):
        """
        Initialize configuration with reliable path resolution.

        Args:
            project_root: Optional explicit project root path
        """
        self.project_root = self._resolve_project_root(project_root)
        self.data_dir = self.project_root / "data"
        self.logs_dir = self.project_root / "scraper" / "logs"
        self.config_dir = self.project_root / "scraper" / "config"

        # Validate environment on initialization
        self._validate_environment()

    def _resolve_project_root(self, explicit_root: Optional[str] = None) -> Path:
        """
        Reliably resolve project root with multiple fallback strategies.

        Args:
            explicit_root: Explicitly provided project root

        Returns:
            Path: Resolved project root directory

        Raises:
            RuntimeError: If project root cannot be determined
        """
        if explicit_root:
            root = Path(explicit_root).resolve()
            if self._is_valid_project_root(root):
                logger.info(f"Using explicit project root: {root}")
                return root
            else:
                # If explicit root was provided but invalid, raise immediately
                raise RuntimeError(f"Invalid project root: {explicit_root}")

        # Strategy 1: Use __file__ path traversal (works in most cases)
        try:
            # From config.py: scraper/core/config.py -> project root (2 levels up)
            current_file = Path(__file__).resolve()
            potential_root = current_file.parents[2]
            if self._is_valid_project_root(potential_root):
                logger.info(f"Resolved project root via __file__: {potential_root}")
                return potential_root
        except (IndexError, OSError) as e:
            logger.debug(f"__file__ strategy failed: {e}")

        # Strategy 2: Search upward from current working directory
        try:
            current = Path.cwd()
            for _ in range(10):  # Limit search depth
                if self._is_valid_project_root(current):
                    logger.info(f"Resolved project root via cwd search: {current}")
                    return current
                if current.parent == current:  # Reached filesystem root
                    break
                current = current.parent
        except OSError as e:
            logger.debug(f"CWD search strategy failed: {e}")

        # Strategy 3: Environment variable fallback
        try:
            env_root = os.environ.get("SCRAPER_PROJECT_ROOT")
            if env_root:
                root = Path(env_root).resolve()
                if self._is_valid_project_root(root):
                    logger.info(f"Resolved project root via environment: {root}")
                    return root
        except OSError as e:
            logger.debug(f"Environment variable strategy failed: {e}")

        # If all strategies fail, raise an error
        raise RuntimeError("Cannot determine project root directory. " "Please set SCRAPER_PROJECT_ROOT environment variable or " "ensure the script is run from the project directory.")

    def _is_valid_project_root(self, path: Path) -> bool:
        """
        Validate that a path is the project root by checking for key files.

        Args:
            path: Path to validate

        Returns:
            bool: True if path appears to be project root
        """
        if not path.exists() or not path.is_dir():
            return False

        # Check for key project files/directories
        required_paths = [
            path / "scraper",
            path / "pyproject.toml",
        ]

        return all(p.exists() for p in required_paths)

    def _validate_environment(self) -> None:
        """
        Validate that the environment is properly set up.

        Raises:
            RuntimeError: If environment validation fails
        """
        # Check project root validity
        if not self._is_valid_project_root(self.project_root):
            raise RuntimeError(f"Invalid project root: {self.project_root}")

        # Ensure critical directories can be created
        try:
            self.data_dir.mkdir(parents=True, exist_ok=True)
            self.logs_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError as e:
            raise RuntimeError(f"Cannot create required directories: {e}")

        # Test write permissions
        test_file = self.data_dir / ".write_test"
        try:
            test_file.write_text("test")
            test_file.unlink()
        except (PermissionError, OSError) as e:
            raise RuntimeError(f"Data directory not writable: {e}")

        logger.info(f"Environment validated successfully. Project root: {self.project_root}")

    def get_organized_paths(self, date_str: Optional[str] = None) -> Dict[str, Path]:
        """
        Get organized directory structure for a date.

        Args:
            date_str: Date string in YYYY-MM-DD format (default: today)

        Returns:
            Dict[str, Path]: Organized paths for different data types
        """
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")

        date_dir = self.data_dir / date_str

        return {
            "base": date_dir,
            "raw": date_dir / "raw",
            "content": date_dir / "content",
            "summaries": date_dir / "summaries",
            "summaries_local": date_dir / "summaries_local",
            "exports": date_dir / "exports",
        }

    def ensure_date_structure(self, date_str: Optional[str] = None) -> Dict[str, Path]:
        """
        Ensure date-based directory structure exists.

        Args:
            date_str: Date string in YYYY-MM-DD format (default: today)

        Returns:
            Dict[str, Path]: Created directory paths

        Raises:
            RuntimeError: If directories cannot be created
        """
        paths = self.get_organized_paths(date_str)

        try:
            for path_type, path in paths.items():
                if path_type != "base":  # Skip base path
                    path.mkdir(parents=True, exist_ok=True)
                    logger.debug(f"Ensured {path_type} directory exists: {path}")

            return paths
        except OSError as e:
            raise RuntimeError(f"Failed to create directory structure: {e}")

    def get_config_file(self, filename: str) -> Path:
        """
        Get path to a configuration file.

        Args:
            filename: Configuration file name

        Returns:
            Path: Path to configuration file

        Raises:
            FileNotFoundError: If configuration file doesn't exist
        """
        config_path = self.config_dir / filename
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        return config_path

    def get_fallback_directory(self, dir_type: str, date_str: Optional[str] = None) -> Path:
        """
        Get fallback directory when organized structure fails.

        Args:
            dir_type: Type of directory (raw, content, exports, etc.)
            date_str: Date string in YYYY-MM-DD format (default: today)

        Returns:
            Path: Fallback directory path
        """
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")

        if dir_type in ["raw", "content", "summaries", "exports"]:
            fallback_dir = self.data_dir / date_str / dir_type
        else:
            # Default fallback
            fallback_dir = self.data_dir / date_str

        # Ensure fallback directory exists
        try:
            fallback_dir.mkdir(parents=True, exist_ok=True)
            return fallback_dir
        except OSError as e:
            raise RuntimeError(f"Cannot create fallback directory {fallback_dir}: {e}")

    @property
    def sites_config_path(self) -> Path:
        """Get path to sites.yaml configuration file."""
        return self.get_config_file("sites.yaml")

    def __str__(self) -> str:
        """String representation of configuration."""
        return f"ScraperConfig(project_root={self.project_root}, data_dir={self.data_dir})"


# Global configuration instance
_global_config: Optional[ScraperConfig] = None


def get_config() -> ScraperConfig:
    """
    Get the global configuration instance.
    Creates one if it doesn't exist.

    Returns:
        ScraperConfig: Global configuration instance
    """
    global _global_config
    if _global_config is None:
        _global_config = ScraperConfig()
    return _global_config


def set_config(config: ScraperConfig) -> None:
    """
    Set the global configuration instance.

    Args:
        config: Configuration instance to use globally
    """
    global _global_config
    _global_config = config
