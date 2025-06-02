# Project Status

## What This Is

A dead simple daily scraper for tech news with AI summaries.

## Recent Changes (June 2025)

### Simplification ✅
- Replaced argparse with click
- Removed ALL unnecessary options
- Deleted aggregation features (useless)
- Removed exports directories
- Single command: `./daily.py`

### Current State
- **One script**: `daily.py` - just run it
- **Three sources**: GitHub, HackerNews, Lobsters
- **AI summaries**: Using Ollama (gemma2 or tinyllama)
- **Simple structure**: data/YYYY-MM-DD/{raw,content,summaries}

## Usage

```bash
./daily.py         # Good summaries (slow)
./daily.py --quick # Fast summaries
```

## Philosophy

This is a personal tool, not open source. Keep it simple. Get the data. Stop overthinking.
