---
title: open-index/hacker-news · Datasets at Hugging Face
url: https://huggingface.co/datasets/open-index/hacker-news
date: 2026-03-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-03-19T11:27:04.846572
---

# open-index/hacker-news · Datasets at Hugging Face

# Hacker News Dataset Viewer
=====================================

The Hacker News dataset viewer, available soon, aggregates and provides access to the complete Hacker News archive since 2006. The data is organized in monthly Parquet files sorted by item ID.

## Key Features
---------------

*   Organized as one Parquet file per calendar month, plus 5-minute live files for today's activity.
*   New items are fetched every 5 minutes from the source and committed directly as a single Parquet block at midnight UTC.
*   The entire current month is refetched at midnight UTC.

## Data Structure
-----------------

The dataset includes:

*   Monthly Parquet files: Most recent complete month (2026-03.parquet) up to January (2006 parquet)
*   5-minute live files: Current month's activity

Additional statistics are also provided in CSV files, including item count, ID range, file size, fetch duration, and commit timestamp.

## Breakdown
-------------

The chart below illustrates the number of items committed by hour on March 19th (2026-03).

### Today's Status
-----------------

| Hour | Items |
| --- | --- |
| 0:00 | 514 |
| 1:00 | 432 |
| ... | ... |

## Summary and Conclusion
---------------------------

The Hacker News dataset viewer aggregates the complete archive from 2006 to March 2026, providing a comprehensive mirror of HN data. The system includes automated daily updates, with new items fetched every 5 minutes and committed directly as individual Parquet blocks. Statistics accompany each monthly file, enabling easy verification and tracking progress.

```python
# Hacker News Dataset Viewer Summary

hacker_news_dataset = {
    "description": "Complete Hacker News archive since 2006",
    "features": [
        "Monthly Parquet files sorted by item ID",
        "5-minute live files for current month"
    ],
    "statistics": ["item_count", "id_range", "file_size", "fetch_duration", "commit_timestamp"]
}

# Data Structures
monthly_parquet_files = [f"Hacker News-2026-{month:02d}.parquet" for month in range(2007, 2028)]

# Statistics CSVs and live files are included as separate data sources (csv files)
stats_csv = f"hacker_news_stats.csv"
live_minutes_per_day = [
    f"hacker_news_data-{hour:04}.parquet",
    f"hacker_news_activity-{hour:04}.parquet"
]
```
