import os
import shutil
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def migrate_data():
    """Migrate old data files to new format."""
    # Get the project root directory (three levels up from this file)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    data_dir = os.path.join(project_root, "data")
    logger.info(f"Looking for data directory at: {data_dir}")
    if not os.path.exists(data_dir):
        logger.error(f"Data directory does not exist at: {data_dir}")
        return
    # Process each date directory
    for date_dir in os.listdir(data_dir):
        date_path = os.path.join(data_dir, date_dir)
        if not os.path.isdir(date_path):
            continue
        try:
            # Parse date from directory name
            date = datetime.strptime(date_dir, "%Y-%m-%d")
            # Process each file in the date directory
            for file in os.listdir(date_path):
                if not file.endswith(".md"):
                    continue
                # Get site name from filename
                site_name = file.replace(".md", "")
                # Create new filename with timestamp
                timestamp = date.strftime("%Y%m%d-120000")  # Use noon as default time
                new_filename = f"{site_name}-{timestamp}.md"
                # Move and rename file
                old_path = os.path.join(date_path, file)
                new_path = os.path.join(data_dir, new_filename)
                shutil.move(old_path, new_path)
                logger.info(f"Moved {old_path} to {new_path}")
            # Remove empty date directory
            if not os.listdir(date_path):
                os.rmdir(date_path)
                logger.info(f"Removed empty directory: {date_path}")
        except ValueError as e:
            logger.error(f"Error processing directory {date_dir}: {str(e)}")
            continue
    logger.info("Data migration completed")


if __name__ == "__main__":
    migrate_data()
