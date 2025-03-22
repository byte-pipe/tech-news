# Market Intelligence Scraper Design

## Overview
A simple, personal tool to scrape market intelligence from key websites and store insights in markdown format.

## Directory Structure
```
/scraper/
  ├── config/
  │   └── sites.yaml        # Website configurations
  ├── scrapers/
  │   ├── base.py          # Base scraper class
  │   ├── producthunt.py   # ProductHunt specific
  │   ├── indiehackers.py  # IndieHackers specific
  │   └── hackernews.py    # HackerNews specific
  ├── data/
  │   └── YYYY-MM-DD/      # Daily scrapes
  │       ├── producthunt.md
  │       ├── indiehackers.md
  │       └── hackernews.md
  └── main.py              # Entry point
```

## Components

### 1. Configuration (sites.yaml)
```yaml
sites:
  producthunt:
    url: "https://www.producthunt.com"
    selector: ".post-item"
    fields:
      - title
      - description
      - votes
      - comments
      - url

  indiehackers:
    url: "https://www.indiehackers.com"
    selector: ".post"
    fields:
      - title
      - description
      - revenue
      - url

  hackernews:
    url: "https://news.ycombinator.com"
    selector: ".athing"
    fields:
      - title
      - points
      - comments
      - url
```

### 2. Base Scraper (base.py)
- Common scraping functions
- Error handling
- Rate limiting
- Markdown formatting

### 3. Site-Specific Scrapers
- Inherit from base scraper
- Custom parsing logic
- Site-specific data extraction

### 4. Data Storage
- Daily folders (YYYY-MM-DD)
- Markdown files per site
- Simple, readable format

## Implementation Phases

1. **Phase 1: Basic Setup**
   - Directory structure
   - Base scraper
   - Simple config

2. **Phase 2: First Scraper**
   - Implement one site (e.g., HackerNews)
   - Basic markdown output
   - Error handling

3. **Phase 3: Additional Sites**
   - Add more scrapers
   - Improve error handling
   - Add rate limiting

4. **Phase 4: Enhancement**
   - Add scheduling
   - Improve data formatting
   - Add basic analysis

## Usage
```bash
python main.py --site hackernews
python main.py --all
```

## Future Enhancements
1. Trend analysis
2. Idea generation
3. Email notifications
4. Web interface