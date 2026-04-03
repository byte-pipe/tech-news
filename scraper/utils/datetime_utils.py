"""
Date and time utilities for the scraper package.

This module provides common date/time operations used across the scraper.
"""

from datetime import datetime
from typing import Tuple

from scraper.constants import DATE_FOLDER_FORMAT, TIMESTAMP_FORMAT


def get_current_datetime() -> datetime:
    """Get the current datetime.

    Returns:
        Current datetime object
    """
    return datetime.now()


def get_date_and_timestamp() -> Tuple[str, str]:
    """Get formatted date folder and timestamp strings.

    Returns:
        Tuple of (date_folder, timestamp) strings
    """
    now = datetime.now()
    date_folder = now.strftime(DATE_FOLDER_FORMAT)
    timestamp = now.strftime(TIMESTAMP_FORMAT)
    return date_folder, timestamp


def get_date_folder(dt: datetime = None) -> str:
    """Get date folder string for a given datetime.

    Args:
        dt: Datetime object (defaults to current time)

    Returns:
        Date folder string in format YYYY-MM-DD
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(DATE_FOLDER_FORMAT)


def get_timestamp(dt: datetime = None) -> str:
    """Get timestamp string for a given datetime.

    Args:
        dt: Datetime object (defaults to current time)

    Returns:
        Timestamp string in format YYYYMMDD-HHMMSS
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(TIMESTAMP_FORMAT)


def get_iso_timestamp(dt: datetime = None) -> str:
    """Get ISO format timestamp string for a given datetime.

    Args:
        dt: Datetime object (defaults to current time)

    Returns:
        ISO format timestamp string
    """
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()


def parse_date_folder(date_str: str) -> datetime:
    """Parse a date folder string into a datetime object.

    Args:
        date_str: Date string in YYYY-MM-DD format

    Returns:
        Datetime object

    Raises:
        ValueError: If date string format is invalid
    """
    return datetime.strptime(date_str, DATE_FOLDER_FORMAT)


def format_for_filename(dt: datetime = None) -> str:
    """Get a datetime string suitable for use in filenames.

    Args:
        dt: Datetime object (defaults to current time)

    Returns:
        Filename-safe timestamp string
    """
    return get_timestamp(dt)
