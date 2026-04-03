# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Market Intelligence Scraper project designed to collect, analyze, and aggregate trending content from various tech and business websites. The system scrapes data from multiple sources (GitHub, HackerNews, Dev.to, Reddit, etc.), organizes it into readable formats, and provides aggregation capabilities for trend analysis.

## Core Commands

```bash
# Get help on all commands
poetry run scraper --help

# Scrape content
poetry run scraper scrape           # Scrape all 8 sources (~45 seconds)

# Summarize content
poetry run scraper summarize --list-dates                    # List available dates
poetry run scraper summarize                                 # Summarize today with default model from config
poetry run scraper summarize --date 2025-06-01               # Summarize specific date
poetry run scraper summarize --days-back 3                   # Summarize 3 days ago
poetry run scraper summarize --model tinyllama:latest         # Use fast/small model
poetry run scraper summarize --force                         # Force re-summarization
poetry run scraper summarize --dry-run                       # Preview what would be done
poetry run scraper summarize --quiet                         # No output (errors only)

# Batch summarize multiple dates
poetry run scraper summarize-batch                           # Last 7 days with default model
poetry run scraper summarize-batch --days-back 14            # Last 14 days
poetry run scraper summarize-batch --start-date 2025-05-20 --end-date 2025-05-25
poetry run scraper summarize-batch --model tinyllama:latest   # Use fast model for batch
poetry run scraper summarize-batch --skip-existing           # Skip dates that already have summaries

# Summarize with Anthropic Claude API
poetry run scraper summarize-anthropic                      # Summarize today's content
poetry run scraper summarize-anthropic --api-key YOUR_KEY   # Provide API key directly
poetry run scraper summarize-anthropic --model claude-3-opus-20240229  # Use different model

# Check system health
poetry run scraper health           # Basic health check
poetry run scraper health -v        # Verbose health check
poetry run scraper health --json    # JSON output
```

### Testing

```bash
# Run specific test files (recommended for speed)
poetry run pytest scraper/tests/test_base_scraper.py scraper/tests/test_data_models.py scraper/tests/test_circuit_breaker.py -v

# Run all tests (slower)
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=scraper --cov-report=html
```

## Architecture

### Core Components

1. **Main Entry Point (`main.py`)**: Single unified command-line interface for all operations
2. **Base Scraper (`scrapers/base.py`)**: Foundation class with common functionality:
   - Standard methods for data extraction (titles, URLs, descriptions)
   - Output formatting (markdown, JSON, CSV)
   - Error handling and logging
3. **Site-Specific Scrapers**: Individual scrapers inherit from the base scraper:
   - `github.py`, `hackernews_api.py`, `lobsters.py`, etc.
4. **Configuration System**: `config/sites.yaml` defines site-specific settings and selectors
5. **AI Processing**: `core/ai_processor.py` handles content summarization:
   - Automatically selects mode based on model size (small models = fast mode, large models = quality mode)
   - Default models configured in `scraper/config/models.yaml`
   - Use `--model tinyllama:latest` for faster processing
   - Anthropic API integration available via `summarize-anthropic` command

### Data Flow

1. User runs `poetry run scraper scrape`
2. System scrapes 3-6 sources based on mode selected
3. Data is extracted and normalized
4. Results are saved to date-based directories (`data/YYYY-MM-DD/`)
5. Content is fetched and saved as markdown files in `content/` subdirectory
6. Summaries can be generated using `poetry run scraper summarize`
7. Summaries are stored in `summaries/` or `summaries_anthropic/` directories

## Key Design Patterns

1. **Inheritance Model**: Site scrapers inherit from a base class to promote code reuse and standardization.
2. **Configuration-Driven Development**: Site-specific settings are defined in YAML rather than hardcoded.
3. **Sequential Execution**: Scrapers run sequentially for stability (removed threading due to issues).
4. **Time-Based Organization**: Data files are organized in date-based directories with standardized naming.
5. **Multiple Output Formats**: The system supports markdown, JSON, and CSV formats with appropriate handling for each.
6. **Aggregation Pipeline**: Data is processed through collection, deduplication, and aggregation stages.
7. **Progress Display**: Uses rich library for progress bars and console output instead of verbose logging.

## Scraper Sources

Default scrape runs 8 sources: GitHub, HackerNews API, Dev.to, Reddit, Reddit Optimized, TLDR, hnrss, NewsFeed (multi-source RSS)

Available but not in default: HackerNoon

## 🚨 MANDATORY Testing Commands - Run After EVERY Code Change 🚨

**ALWAYS run these commands after making ANY code changes:**

```bash
# 1. Quick test to verify basic functionality
poetry run pytest scraper/tests/test_base_scraper.py scraper/tests/test_data_models.py scraper/tests/test_circuit_breaker.py -v

# 2. Type checking
poetry run mypy .

# 3. Run ALL pre-commit hooks (includes black, isort, flake8, etc.)
pre-commit run --all-files
```

If any of these fail, fix the issues before proceeding.

### Full Testing Suite (when needed)

```bash
# Full test suite (may take time)
poetry run pytest

# Individual quality checks
poetry run flake8 scraper/
poetry run black scraper/ --check
poetry run isort scraper/ --check-only
poetry run bandit -c pyproject.toml scraper/
```

## Code Style and Preferences

- **CLI Framework**: Use click instead of argparse for command-line interfaces
- **Logging**: Configure the root logger with basicConfig(force=True) for simple, clean logging
- **Progress Display**: Use rich library for progress bars and console output instead of verbose logging
- **Line Length**: 222 characters (configured in black, isort, and flake8)
- **Python Version**: 3.11+ required
- **Testing Framework**: pytest with coverage requirements (minimum 15%)

## Configuration Files

- **pyproject.toml**: Poetry dependencies, tool configurations (black, isort, mypy, pytest)
- **.pre-commit-config.yaml**: Automated code quality checks
- **.flake8**: Linting configuration
- **scraper/config/sites.yaml**: Site-specific scraper configurations
- **scraper/config/categories.yaml**: Keyword-to-category mappings for pre-clustering articles before digest generation
- **scraper/config/preferences.yaml**: User-editable filtering preferences (blocklist, min scores, digest display settings)

## Important Instructions

- **CRITICAL**: After making code changes, ALWAYS run the mandatory testing commands above.
- This is NOT optional - these checks ensure code quality and prevent regressions.
- Do what has been asked; nothing more, nothing less.
- NEVER create files unless they're absolutely necessary for achieving your goal.
- ALWAYS prefer editing an existing file to creating a new one.
- NEVER proactively create documentation files (\*.md) or README files unless explicitly requested.
