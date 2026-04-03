"""
Path utilities for the scraper package.

This module provides common path manipulation utilities.
"""

import os
from pathlib import Path
from typing import Optional


def get_project_root(start_path: Optional[str] = None, levels_up: int = 2) -> str:
    """Get the project root directory by going up from a start path.

    Args:
        start_path: Starting path (defaults to current file location)
        levels_up: Number of directory levels to go up

    Returns:
        Absolute path to the project root
    """
    if start_path is None:
        # Get the directory of the current file
        start_path = os.path.abspath(__file__)

    path = Path(start_path)

    # Go up the specified number of levels
    for _ in range(levels_up):
        path = path.parent

    return str(path.absolute())


def ensure_data_directory(date_folder: str, subdir: str = "") -> str:
    """Ensure a data directory exists and return its path.

    Args:
        date_folder: The date folder name (e.g., "2025-06-01")
        subdir: Optional subdirectory within the date folder

    Returns:
        Absolute path to the directory

    Raises:
        ValueError: If the path contains directory traversal attempts
    """
    project_root = get_project_root()

    # Normalize and validate inputs to prevent path traversal
    date_folder = os.path.normpath(date_folder)
    if ".." in date_folder or date_folder.startswith("/") or date_folder.startswith("\\"):
        raise ValueError(f"Invalid date_folder: {date_folder}")

    if subdir:
        subdir = os.path.normpath(subdir)
        if ".." in subdir or subdir.startswith("/") or subdir.startswith("\\"):
            raise ValueError(f"Invalid subdir: {subdir}")
        data_path = os.path.join(project_root, "data", date_folder, subdir)
    else:
        data_path = os.path.join(project_root, "data", date_folder)

    # Ensure the final path is within the project directory
    data_path = os.path.abspath(data_path)
    expected_prefix = os.path.abspath(os.path.join(project_root, "data"))
    if not data_path.startswith(expected_prefix):
        raise ValueError(f"Path traversal attempt detected: {data_path}")

    os.makedirs(data_path, exist_ok=True)
    return data_path


def ensure_directory(path: str) -> str:
    """Ensure a directory exists, creating it if necessary.

    Args:
        path: Directory path to ensure exists

    Returns:
        Absolute path to the directory
    """
    os.makedirs(path, exist_ok=True)
    return os.path.abspath(path)


def build_data_file_path(date_folder: str, filename: str, subdir: str = "") -> str:
    """Build a complete file path within the data directory structure.

    Args:
        date_folder: The date folder name (e.g., "2025-06-01")
        filename: The filename to create path for
        subdir: Optional subdirectory within the date folder

    Returns:
        Complete file path
    """
    directory = ensure_data_directory(date_folder, subdir)
    return os.path.join(directory, filename)


def get_data_directory_path(date_folder: str, subdir: str = "") -> str:
    """Get the path to a data directory without creating it.

    Args:
        date_folder: The date folder name (e.g., "2025-06-01")
        subdir: Optional subdirectory within the date folder

    Returns:
        Absolute path to the directory
    """
    project_root = get_project_root()

    if subdir:
        return os.path.join(project_root, "data", date_folder, subdir)
    else:
        return os.path.join(project_root, "data", date_folder)
