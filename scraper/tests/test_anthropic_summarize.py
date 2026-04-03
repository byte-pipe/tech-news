#!/usr/bin/env python3
"""Test script to diagnose Anthropic summarization issues."""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from scraper.core.ai_processor import summarize_with_anthropic  # noqa: E402


def test_anthropic_summarize():
    """Test Anthropic summarization with detailed output."""

    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        print("To set it: export ANTHROPIC_API_KEY='your-key-here'")
        return

    print(f"✓ API key found (length: {len(api_key)})")

    # Get today's date

    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"✓ Testing with date: {date_str}")

    # Check if content directory exists
    content_dir = Path(f"data/{date_str}/content")
    if not content_dir.exists():
        print(f"❌ Content directory not found: {content_dir}")
        return

    content_files = list(content_dir.glob("*.md"))
    print(f"✓ Found {len(content_files)} content files")

    if not content_files:
        print("❌ No content files to summarize")
        return

    # Test with just one file
    print("\nTesting Anthropic summarization with 1 file...")

    def progress_callback(current, total, filename):
        print(f"  Progress: {current}/{total} - {filename}")

    success, summary_files = summarize_with_anthropic(date_dir=date_str, api_key=api_key, model="claude-3-haiku-20240307", max_files=1, progress_callback=progress_callback)

    if success:
        print(f"\n✅ Success! Created {len(summary_files)} summary files:")
        for f in summary_files:
            print(f"  - {f}")
    else:
        print("\n❌ Summarization failed")

    # Check if directory was created
    summary_dir = Path(f"data/{date_str}/summaries_anthropic")
    if summary_dir.exists():
        files = list(summary_dir.glob("*.md"))
        print(f"\n✓ summaries_anthropic directory exists with {len(files)} files")
    else:
        print("\n❌ summaries_anthropic directory was not created")


if __name__ == "__main__":
    test_anthropic_summarize()
