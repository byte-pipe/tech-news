---
title: DEV Follower Analysis - DEV Community
url: https://dev.to/annavi11arrea1/dev-follower-analysis-4dhc
date: 2025-11-19
site: devto
model: llama3.2:1b
summarized_at: 2025-11-22T11:11:02.210480
screenshot: devto-dev-follower-analysis-dev-community.png
---

# DEV Follower Analysis - DEV Community

**GitHub Followers Data Extraction and Analysis via GraphQL**

### TLDR

This article describes a personal analysis project for extracting meaningful data from GitHub followers using the DEV API. The goal is to identify patterns, languages, and technologies of interested individuals.

**Key Points:**

* Gathered publicly available user data about GitHub followers using the DEV API
* Scraped follower links and analyzed language usage on their GitHub profiles
* Identified common interests among fellow developers

### Data Collection and Analysis

* Created a Node.js script to fetch GitHub data from the DEV API, utilizing `fs` and `path` modules for file system operations
* Set up an async function `fetchAllPages` to retrieve data in chunks using pagination logic (`PER_PAGE=1000`)
* Utilized `fetch` API with JSON payload and set headers for authentication (API key and Content-Type)
