# Daily Tech Scraper

Gets tech news from 11+ sources with AI summaries.

## Setup

```bash
poetry install
```

## Daily Routine (2 min)

```bash
# Full scrape + AI summaries (6 sources, ~45s + summarization time)
poetry run scraper scrape
poetry run scraper summarize

# Quick mode (3 fast sources, ~15s + summarization time)
poetry run scraper scrape --quick
poetry run scraper summarize

# Quiet mode for scripts/automation
poetry run scraper scrape --quick --quiet
poetry run scraper summarize --quiet
```

## Review (5 min)

Check `data/YYYY-MM-DD/`:
- `summaries/` - AI analysis of trending stuff
- `content/` - Full articles if you want details

## What It Scrapes

- GitHub trending
- HackerNews (API + web)
- Dev.to
- HackerNoon
- Medium
- TechCrunch
- TechNode
- VentureBeat
- Reddit
- Reddit Optimized

## Migration from Old Commands

The `poetry run daily` command has been replaced with:
- `poetry run scraper scrape` - Scrape content
- `poetry run scraper summarize` - Generate AI summaries

For the old `daily --quick` behavior, use:
```bash
poetry run scraper scrape --quick
poetry run scraper summarize
```

That's it. Stop overcomplicating shit.
