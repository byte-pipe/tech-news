#!/usr/bin/env python3
"""
Batch summarization script for processing multiple dates efficiently.
Designed for post-processing workflow after scraping.
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


def get_dates_to_process(data_dir, days_back=7, start_date=None, end_date=None):
    """Get list of dates to process based on criteria."""
    dates_to_process = []

    if start_date and end_date:
        # Process range
        current = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        while current <= end:
            date_str = current.strftime("%Y-%m-%d")
            content_dir = data_dir / date_str / "content"
            if content_dir.exists() and list(content_dir.glob("*.md")):
                dates_to_process.append(date_str)
            current += timedelta(days=1)
    else:
        # Process last N days
        for i in range(days_back):
            date = datetime.now() - timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            content_dir = data_dir / date_str / "content"
            if content_dir.exists() and list(content_dir.glob("*.md")):
                dates_to_process.append(date_str)

    return sorted(dates_to_process)


def main():
    """Main entry point for batch summarization."""
    parser = argparse.ArgumentParser(description="Batch summarize content from multiple dates")
    parser.add_argument(
        "--days-back",
        type=int,
        default=7,
        help="Process content from last N days (default: 7)",
    )
    parser.add_argument(
        "--start-date",
        help="Start date for range (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--end-date",
        help="End date for range (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--model",
        default="llama3.2:1b",
        help="Model for summarization (default: llama3.2:1b)",
    )
    parser.add_argument(
        "--local-model",
        action="store_true",
        help="Use powerful local model",
    )
    parser.add_argument(
        "--local-model-name",
        default="gemma2:27b",
        help="Local model name (default: gemma2:27b)",
    )
    parser.add_argument(
        "--max-files-per-date",
        type=int,
        default=0,
        help="Max files to summarize per date (0 = all)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip dates that already have summaries",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without summarizing",
    )

    args = parser.parse_args()
    logger = logging.getLogger(__name__)

    # Find project root
    project_root = Path(__file__).parent.parent.parent.parent
    data_dir = project_root / "data"

    # Get dates to process
    dates = get_dates_to_process(data_dir, days_back=args.days_back, start_date=args.start_date, end_date=args.end_date)

    if not dates:
        logger.info("No dates with content found to process")
        return 0

    logger.info(f"Found {len(dates)} dates to process: {', '.join(dates)}")

    # Process each date
    total_summaries = 0
    failed_dates = []

    for date_str in dates:
        logger.info(f"\n=== Processing {date_str} ===")

        # Check for existing summaries if skip_existing
        if args.skip_existing:
            summary_dir = data_dir / date_str / ("summaries_local" if args.local_model else "summaries")
            if summary_dir.exists() and list(summary_dir.glob("*.md")):
                logger.info(f"Skipping {date_str} - summaries already exist")
                continue

        if args.dry_run:
            content_dir = data_dir / date_str / "content"
            file_count = len(list(content_dir.glob("*.md")))
            logger.info(f"Would summarize {file_count} files from {date_str}")
            continue

        # Run summarization
        try:
            if args.local_model:
                success, summary_files = summarize_with_local_model(date_dir=date_str, model_name=args.local_model_name, max_files=args.max_files_per_date, only_latest=False)
            else:
                success, summary_files = summarize_content(date_dir=date_str, model_name=args.model, max_files=args.max_files_per_date, fallback_model="tinyllama:1.1b")

            if success:
                logger.info(f"✅ Created {len(summary_files)} summaries for {date_str}")
                total_summaries += len(summary_files)
            else:
                logger.error(f"❌ Failed to summarize {date_str}")
                failed_dates.append(date_str)

        except Exception as e:
            logger.error(f"❌ Error processing {date_str}: {str(e)}")
            failed_dates.append(date_str)

    # Final report
    logger.info("\n=== BATCH SUMMARY ===")
    logger.info(f"Dates processed: {len(dates) - len(failed_dates)}/{len(dates)}")
    logger.info(f"Total summaries created: {total_summaries}")

    if failed_dates:
        logger.error(f"Failed dates: {', '.join(failed_dates)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
