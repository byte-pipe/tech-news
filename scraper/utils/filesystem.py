"""
Filesystem utilities for the scraper.
"""

import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)


def get_project_root():
    """Get the project root directory.

    Returns:
        str: Path to the project root directory
    """
    # Get the path to this file, then go up 4 levels to reach project root
    # utils/filesystem.py -> utils -> scraper -> src -> project_root
    current_file = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_file))))


def get_data_file_path(project_root, site_name, create_dirs=True):
    """
    Get the file path for saving scraped data, using a date-based folder structure.

    Args:
        project_root (str): Project root directory
        site_name (str): Name of the site being scraped
        create_dirs (bool): Whether to create directories if they don't exist

    Returns:
        tuple: (file_path, date_folder, timestamp)
    """
    now = datetime.now()
    date_folder = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%Y%m%d-%H%M%S")

    # Create date folder if it doesn't exist
    folder_path = os.path.join(project_root, "data", date_folder)

    if create_dirs:
        try:
            os.makedirs(folder_path, exist_ok=True)
            logger.debug(f"Created or verified directory: {folder_path}")
        except Exception as e:
            logger.error(f"Error creating directory {folder_path}: {str(e)}")

    # Create the full file path
    file_path = os.path.join(folder_path, f"{site_name}-{timestamp}.md")

    return file_path, date_folder, timestamp


def cleanup_empty_files():
    """Delete empty files from the data directory."""
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "data")
    if not os.path.exists(data_dir):
        logger.info("Data directory does not exist")
        return

    # Recursively walk through all date folders
    deleted_files = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            # Check supported file extensions
            if not file.endswith((".md", ".json", ".csv")):
                continue

            file_path = os.path.join(root, file)

            # Check for empty files first
            if os.path.getsize(file_path) == 0:
                try:
                    os.remove(file_path)
                    deleted_files.append(file)
                    logger.info(f"Deleted empty file: {file}")
                except Exception as e:
                    logger.error(f"Error deleting file {file}: {str(e)}")
                continue

            # For each format, check if the file has meaningful content
            try:
                if file.endswith(".md"):
                    # Check if markdown file only contains header
                    with open(file_path, "r") as f:
                        content = f.read().strip()
                        if content.count("\n") <= 1:  # Only header line
                            os.remove(file_path)
                            deleted_files.append(file)
                            logger.info(f"Deleted markdown file with only header: {file}")

                elif file.endswith(".json"):
                    # Check if JSON file only contains empty array
                    with open(file_path, "r") as f:
                        content = f.read().strip()
                        if content in ["[]", "{}"]:  # Empty array or object
                            os.remove(file_path)
                            deleted_files.append(file)
                            logger.info(f"Deleted JSON file with empty data: {file}")

                elif file.endswith(".csv"):
                    # Check if CSV file only contains header
                    with open(file_path, "r") as f:
                        content = f.read().strip()
                        if content.count("\n") == 0:  # Only header line
                            os.remove(file_path)
                            deleted_files.append(file)
                            logger.info(f"Deleted CSV file with only header: {file}")
            except Exception as e:
                logger.error(f"Error checking/deleting file {file}: {str(e)}")

    if deleted_files:
        logger.info(f"Cleaned up {len(deleted_files)} empty files: {', '.join(deleted_files)}")
    else:
        logger.info("No empty files found to clean up")


def check_empty_outputs():
    """Check for empty output files and log errors."""
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "data")
    if not os.path.exists(data_dir):
        logger.error(f"Data directory {data_dir} does not exist")
        return

    empty_files = []
    # Recursively walk through all date folders
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            # Check supported file extensions
            if not file.endswith((".md", ".json", ".csv")):
                continue

            file_path = os.path.join(root, file)

            # Check for empty files first
            if os.path.getsize(file_path) == 0:
                empty_files.append(file)
                logger.error(f"Empty output file detected: {file}")
                continue

            # For each format, check if the file has meaningful content
            try:
                if file.endswith(".md"):
                    # Check if markdown file only contains header
                    with open(file_path, "r") as f:
                        content = f.read().strip()
                        if content.count("\n") <= 1:  # Only header line
                            empty_files.append(file)
                            logger.error(f"Markdown file contains only header: {file}")

                elif file.endswith(".json"):
                    # Check if JSON file only contains empty array
                    with open(file_path, "r") as f:
                        content = f.read().strip()
                        if content in ["[]", "{}"]:  # Empty array or object
                            empty_files.append(file)
                            logger.error(f"JSON file contains empty data: {file}")

                elif file.endswith(".csv"):
                    # Check if CSV file only contains header
                    with open(file_path, "r") as f:
                        content = f.read().strip()
                        if content.count("\n") == 0:  # Only header line
                            empty_files.append(file)
                            logger.error(f"CSV file contains only header: {file}")
            except Exception as e:
                logger.error(f"Error checking file {file}: {str(e)}")

    if empty_files:
        logger.error(f"Found {len(empty_files)} empty or invalid output files: {', '.join(empty_files)}")
    else:
        logger.info("All output files contain data")
