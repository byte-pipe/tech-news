---
title: AI scrapers request commented scripts
url: https://cryptography.dog/blog/AI-scrapers-request-commented-scripts/
date: 2025-11-01
site: hackernews
model: llama3.2:1b
summarized_at: 2025-11-01T11:38:52.555343
screenshot: hackernews-ai-scrapers-request-commented-scripts.png
---

# AI scrapers request commented scripts

# AI Scrapers Request Commented Scripts

Author: Aaron P. MacSween

 Published: 2025-10-31

### Summary

In a recent episode of bot abuse, an author discovered that their server's logfiles contained numerous 404 errors for JavaScript file (//commented-out script tag) due to accidental deployment. The error revealed the presence of malicious scraping scripts, such as `python-httpx`, `Go-http-client`, and `Gulper Web Bot`. These scrapers appear to interpret comments in HTML files recursively in an effort to search for URLs hidden within them. The extent to which they employ different techniques remains unclear.

### Key Points

* AI scrapers were deployed secretly by the author's accidental deployment of a commented-out script tag.
* Scraper requests were sent from various user-agents, including some that self-identified as proper browsers.
* Scrapers treated HTML as text and parsed comments recursively to search for disabled URLs.

### Maintaining Original Perspective

The provided summary aims to preserve the original's grammatical person-viewpoint and narrative style while retaining its critical analysis.
