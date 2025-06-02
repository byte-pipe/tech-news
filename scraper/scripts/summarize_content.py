#!/usr/bin/env python3
"""
Standalone script for summarizing scraped content.
Can be run independently from the main scraping workflow.
"""

import argparse
import logging
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.core.ai_processor import summarize_content, summarize_with_local_model  # noqa: E402


def get_available_dates(data_dir):
    """Get list of available date directories with content."""
    available_dates = []

    for item in os.listdir(data_dir):
        if os.path.isdir(os.path.join(data_dir, item)):
            # Check if it matches date format YYYY-MM-DD
            try:
                datetime.strptime(item, "%Y-%m-%d")
                content_dir = os.path.join(data_dir, item, "content")
                if os.path.exists(content_dir) and os.listdir(content_dir):
                    available_dates.append(item)
            except ValueError:
                continue

    return sorted(available_dates, reverse=True)


def main():
    """Main entry point for standalone summarization."""
    parser = argparse.ArgumentParser(description="Summarize scraped content independently from the main workflow")
    parser.add_argument(
        "--date",
        help="Date to process (YYYY-MM-DD format). Default: today",
        default=datetime.now().strftime("%Y-%m-%d"),
    )
    parser.add_argument(
        "--days-back",
        type=int,
        help="Process content from N days back",
        default=0,
    )
    parser.add_argument(
        "--list-dates",
        action="store_true",
        help="List available dates with content",
    )
    parser.add_argument(
        "--model",
        default="llama3.2:1b",
        help="Model to use for summarization (default: llama3.2:1b)",
    )
    parser.add_argument(
        "--local-model",
        action="store_true",
        help="Use powerful local model for high-quality summaries",
    )
    parser.add_argument(
        "--local-model-name",
        default="gemma2:27b",
        help="Local model name (default: gemma2:27b)",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Maximum files to summarize (0 = all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually summarizing",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-summarization even if summaries exist",
    )

    args = parser.parse_args()

    # Set up logging
    logger = logging.getLogger(__name__)

    # Find project root and data directory
    project_root = Path(__file__).parent.parent.parent.parent
    data_dir = project_root / "data"

    # Handle --list-dates
    if args.list_dates:
        available_dates = get_available_dates(data_dir)
        if available_dates:
            logger.info("Available dates with content:")
            for date in available_dates:
                content_dir = data_dir / date / "content"
                file_count = len(list(content_dir.glob("*.md")))
                logger.info(f"  {date}: {file_count} files")
        else:
            logger.info("No dates with content found")
        return 0

    # Determine date to process
    if args.days_back > 0:
        target_date = datetime.now() - timedelta(days=args.days_back)
        date_str = target_date.strftime("%Y-%m-%d")
    else:
        date_str = args.date

    # Validate date format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        logger.error(f"Invalid date format: {date_str}. Use YYYY-MM-DD")
        return 1

    # Check if content directory exists
    content_dir = data_dir / date_str / "content"
    if not content_dir.exists():
        logger.error(f"No content directory found for {date_str}")
        logger.info("Use --list-dates to see available dates")
        return 1

    # Count content files
    content_files = list(content_dir.glob("*.md"))
    if not content_files:
        logger.error(f"No content files found in {content_dir}")
        return 1

    logger.info(f"Found {len(content_files)} content files for {date_str}")

    # Check for existing summaries
    if args.local_model:
        summary_dir = data_dir / date_str / "summaries_local"
    else:
        summary_dir = data_dir / date_str / "summaries"

    if summary_dir.exists() and not args.force:
        existing_summaries = list(summary_dir.glob("*.md"))
        if existing_summaries:
            logger.warning(f"Found {len(existing_summaries)} existing summaries")
            logger.info("Use --force to re-summarize")
            if not args.dry_run:
                return 0

    # Dry run mode
    if args.dry_run:
        logger.info("\n=== DRY RUN MODE ===")
        logger.info(f"Would process date: {date_str}")
        logger.info(f"Content directory: {content_dir}")
        logger.info(f"Summary directory: {summary_dir}")
        logger.info(f"Model: {args.local_model_name if args.local_model else args.model}")
        logger.info(f"Max files: {args.max_files or 'all'}")

        # Show sample of files
        logger.info("\nSample content files:")
        for i, f in enumerate(content_files[:5]):
            logger.info(f"  - {f.name}")
        if len(content_files) > 5:
            logger.info(f"  ... and {len(content_files) - 5} more")

        return 0

    # Run summarization
    logger.info("\n=== STARTING SUMMARIZATION ===")

    try:
        if args.local_model:
            # Use powerful local model
            success, summary_files = summarize_with_local_model(date_dir=date_str, model_name=args.local_model_name, max_files=args.max_files, only_latest=False)
        else:
            # Use fast model for CI
            success, summary_files = summarize_content(date_dir=date_str, model_name=args.model, max_files=args.max_files, fallback_model="tinyllama:1.1b")

        if success:
            logger.info(f"\n✅ Successfully created {len(summary_files)} summaries")
            return 0
        else:
            logger.error("\n❌ Summarization failed")
            return 1

    except Exception as e:
        logger.error(f"\n❌ Summarization error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
