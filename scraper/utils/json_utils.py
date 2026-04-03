"""
JSON utilities for the scraper package.

This module provides common JSON handling functionality.
"""

import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """Safely parse a JSON string with error handling.

    Args:
        json_str: JSON string to parse
        default: Default value to return if parsing fails

    Returns:
        Parsed JSON data or default value
    """
    if not json_str:
        return default

    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError, ValueError) as e:
        logger.debug(f"Error parsing JSON: {str(e)}")
        return default


def safe_json_dumps(data: Any, indent: int = 2, ensure_ascii: bool = False, default: str = "{}") -> str:
    """Safely serialize data to JSON string with error handling.

    Args:
        data: Data to serialize
        indent: JSON indentation level
        ensure_ascii: Whether to escape non-ASCII characters
        default: Default value to return if serialization fails

    Returns:
        JSON string or default value
    """
    try:
        return json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)
    except (TypeError, ValueError) as e:
        logger.error(f"Error serializing to JSON: {str(e)}")
        return default


def load_json_file(file_path: str, default: Any = None) -> Any:
    """Load JSON data from a file with error handling.

    Args:
        file_path: Path to JSON file
        default: Default value to return if loading fails

    Returns:
        Loaded JSON data or default value
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        logger.error(f"Error loading JSON file {file_path}: {str(e)}")
        return default


def save_json_file(data: Any, file_path: str, indent: int = 2, ensure_ascii: bool = False) -> bool:
    """Save data to a JSON file with error handling.

    Args:
        data: Data to save
        file_path: Path to save file
        indent: JSON indentation level
        ensure_ascii: Whether to escape non-ASCII characters

    Returns:
        True if successful, False otherwise
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)
        return True
    except (TypeError, ValueError, OSError) as e:
        logger.error(f"Error saving JSON file {file_path}: {str(e)}")
        return False


def merge_json_objects(obj1: Dict, obj2: Dict, deep: bool = True) -> Dict:
    """Merge two JSON objects.

    Args:
        obj1: First JSON object (base)
        obj2: Second JSON object (to merge in)
        deep: Whether to perform deep merge for nested objects

    Returns:
        Merged JSON object
    """
    if not isinstance(obj1, dict) or not isinstance(obj2, dict):
        logger.warning("Both objects must be dictionaries for merging")
        return obj1 if isinstance(obj1, dict) else {}

    result = obj1.copy()

    for key, value in obj2.items():
        if deep and key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_json_objects(result[key], value, deep=True)
        else:
            result[key] = value

    return result


def extract_nested_value(data: Dict, keys: List[str], default: Any = None) -> Any:
    """Extract a nested value from a JSON object using a list of keys.

    Args:
        data: JSON object to extract from
        keys: List of keys representing the path to the value
        default: Default value if path doesn't exist

    Returns:
        Extracted value or default
    """
    current = data

    try:
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current
    except (TypeError, KeyError):
        return default


def flatten_json(data: Dict, separator: str = "_", parent_key: str = "") -> Dict:
    """Flatten a nested JSON object.

    Args:
        data: JSON object to flatten
        separator: Separator for nested keys
        parent_key: Parent key prefix

    Returns:
        Flattened JSON object
    """
    items = []

    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key

        if isinstance(value, dict):
            items.extend(flatten_json(value, separator, new_key).items())
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    items.extend(flatten_json(item, separator, f"{new_key}{separator}{i}").items())
                else:
                    items.append((f"{new_key}{separator}{i}", item))
        else:
            items.append((new_key, value))

    return dict(items)
