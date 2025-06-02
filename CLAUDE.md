# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Market Intelligence Scraper project designed to collect, analyze, and aggregate trending content from various tech and business websites. The system scrapes data from multiple sources (GitHub, HackerNews, Dev.to, Reddit, etc.), organizes it into readable formats, and provides aggregation capabilities for trend analysis.

## Core Commands

### Running the Scraper

```bash
# Run all scrapers with default settings (JSON format)
poetry run python src/scraper/main.py
# Run specific scrapers
poetry run python src/scraper/main.py --scrapers github hackernews
# Change output format to markdown or CSV
poetry run python src/scraper/main.py --format markdown
poetry run python src/scraper/main.py --format csv
# Preview mode (no files saved)
poetry run python src/scraper/main.py --dry-run
# Clean up empty files after scraping
poetry run python src/scraper/main.py --cleanup
```

### Data Aggregation

```bash
# Run scrapers and generate aggregated data
poetry run python src/scraper/main.py --format json --aggregate
# Just aggregate existing data
poetry run python src/scraper/main.py --aggregate-only
# Aggregate data from the last 48 hours
poetry run python src/scraper/main.py --aggregate-only --hours 48
# Generate markdown files from JSON data
poetry run python src/scraper/main.py --format json --generate-markdown
# Run the daily aggregation script
poetry run ./src/scraper/scripts/run_daily_aggregation.sh
# Generate high-quality summaries using powerful local models
poetry run python src/scraper/main.py --local-model --local-model-name gemma2:27b
# Compare CI vs local model quality (run both)
poetry run python src/scraper/main.py --summarize --local-model
```

### Standalone Summarization (NEW - Optimized Workflow)

```bash
# List available dates with content
poetry run python src/scraper/scripts/summarize_content.py --list-dates

# Summarize today's content with fast model (llama3.2:1b)
poetry run python src/scraper/scripts/summarize_content.py

# Summarize specific date
poetry run python src/scraper/scripts/summarize_content.py --date 2025-06-01

# Summarize content from N days ago
poetry run python src/scraper/scripts/summarize_content.py --days-back 3

# Use high-quality local model
poetry run python src/scraper/scripts/summarize_content.py --local-model --local-model-name gemma2:27b

# Dry run to see what would be done
poetry run python src/scraper/scripts/summarize_content.py --dry-run

# Force re-summarization even if summaries exist
poetry run python src/scraper/scripts/summarize_content.py --force

# Limit number of files to summarize
poetry run python src/scraper/scripts/summarize_content.py --max-files 10
```

### Batch Summarization (Process Multiple Dates)

```bash
# Process last 7 days with fast model
poetry run python src/scraper/scripts/batch_summarize.py

# Process specific date range
poetry run python src/scraper/scripts/batch_summarize.py --start-date 2025-05-20 --end-date 2025-05-25

# Use local model for high-quality summaries
poetry run python src/scraper/scripts/batch_summarize.py --local-model --days-back 3

# Skip dates that already have summaries
poetry run python src/scraper/scripts/batch_summarize.py --skip-existing

# Dry run to see what would be processed
poetry run python src/scraper/scripts/batch_summarize.py --dry-run

# Limit files per date
poetry run python src/scraper/scripts/batch_summarize.py --max-files-per-date 5
```

### Testing

```bash
# Run all tests
poetry run python src/scraper/tests/run_tests.py
# Run specific test file
poetry run python -m unittest src/scraper/tests/test_base_scraper.py
poetry run python -m unittest src/scraper/tests/test_github_scraper.py
```

## Architecture

### Core Components

1. **Main Entry Point (`main.py`)**: Orchestrates the scraping process, handles CLI arguments, and manages execution flow.
2. **Base Scraper (`scrapers/base.py`)**: Foundation class with common functionality:
   - Standard methods for data extraction (titles, URLs, descriptions)
   - Output formatting (markdown, JSON, CSV)
   - Error handling and logging
3. **Site-Specific Scrapers**: Individual scrapers inherit from the base scraper and implement site-specific parsing logic:
   - `github.py`, `hackernews.py`, `devto.py`, etc.
4. **Configuration System**: `config/sites.yaml` defines site-specific settings, selectors, and fields.
5. **Data Aggregation**: `utils/aggregator.py` combines data from multiple scraping runs for trend analysis.

### Data Flow

1. User runs `main.py` with parameters
2. System scrapes specified sites (or all by default)
3. Data is extracted and normalized
4. Results are saved to date-based directories (`data/YYYY-MM-DD/`)
5. Optional aggregation combines data across time periods
6. Aggregated data is stored in `data/aggregated/`

## Key Design Patterns

1. **Inheritance Model**: Site scrapers inherit from a base class to promote code reuse and standardization.
2. **Configuration-Driven Development**: Site-specific settings are defined in YAML rather than hardcoded.
3. **Sequential Execution**: Scrapers run sequentially for stability (removed threading due to issues).
4. **Time-Based Organization**: Data files are organized in date-based directories with standardized naming.
5. **Multiple Output Formats**: The system supports markdown, JSON, and CSV formats with appropriate handling for each.
6. **Aggregation Pipeline**: Data is processed through collection, deduplication, and aggregation stages.

## 🚨 MANDATORY Testing Commands - Run After EVERY Code Change 🚨

**ALWAYS run these commands after making ANY code changes:**

```bash
# 1. Quick test to verify basic functionality
poetry run pytest src/scraper/tests/test_base_scraper.py src/scraper/tests/test_data_models.py src/scraper/tests/test_circuit_breaker.py -v

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
poetry run flake8 src/
poetry run black src/ --check
poetry run isort src/ --check-only
```

## Important Instructions

- **CRITICAL**: After making code changes, ALWAYS run the mandatory testing commands above.
- This is NOT optional - these checks ensure code quality and prevent regressions.
- Do what has been asked; nothing more, nothing less.
- NEVER create files unless they're absolutely necessary for achieving your goal.
- ALWAYS prefer editing an existing file to creating a new one.
- NEVER proactively create documentation files (*.md) or README files unless explicitly requested.
