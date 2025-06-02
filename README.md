# Daily Tech Scraper

Gets tech news from 11+ sources with AI summaries.

## Setup

```bash
poetry install
```

## Daily Routine (2 min)

```bash
poetry run daily         # Full AI summaries (slow but good)
poetry run daily --quick # Fast summaries
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

That's it. Stop overcomplicating shit.
