---
title: GitHub - bookorbit/bookorbit: BookOrbit: Your Reading Space · GitHub
url: https://github.com/bookorbit/bookorbit
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-27T06:41:15.386338
---

# GitHub - bookorbit/bookorbit: BookOrbit: Your Reading Space · GitHub

# BookOrbit Overview

## What is BookOrbit?
- Self‑hosted platform for ebooks, PDFs, audiobooks, and comics.  
- Provides a web reader and integrates with Kobo and KOReader devices.  
- Syncs progress, highlights, and reading status across all three interfaces.

## Live Demo
- Public demo available without an account.  
- Includes a sample library of public‑domain books.  
- Some admin features are limited; full experience requires self‑hosting.

## Features

### Reading Experience & Sync
- Built‑in web readers for EPUB, KEPUB, MOBI, AZW3, AZW, FB2, PDFs, CBZ/CBR/CB7, and audio formats (M4B, MP3, M4A, OPUS, OGG, FLAC).  
- Three‑way sync between Kobo, KOReader, and BookOrbit (progress and annotations).  
- KOReader plugin with on‑device catalog browser, search, download, and rating management.  
- Unified highlights hub searchable by color, style, and source; exportable as Markdown, CSV, or JSON.  
- Automatic sync to Hardcover, Readwise, and StoryGraph for status, progress, dates, and ratings.  
- Reading statistics, daily goals, heatmaps, streaks, challenges, and 50+ achievements; DNA profile of reading style.

### Library Management
- Support for multiple libraries with isolated folders, custom scan rules, and format priorities.  
- Integration with 14 metadata providers (Google Books, Open Library, Amazon, Goodreads, Kobo, Hardcover, Audible, Audnexus, Libro.fm, iTunes, ComicVine, RanobeDB, Aladin, Lubimyczytać).  
- Cover art sourced from iTunes, DuckDuckGo, and AudiobookCovers.  
- Smart scopes and dynamic collections based on saved filters.

### Platform & Delivery
- Multi‑user accounts with granular permissions and OIDC/SSO support (Authentik, Keycloak, Authelia).  
- Multilingual interface; translations managed via Crowdin.  
- Content delivery via OPDS, Send‑to‑Kindle email, and browser drag‑and‑drop uploads.  
- Automated ingestion through a “Book Dock” drop folder.

## Quick Start (Docker)
1. Create a directory structure and download environment files:  
   ```bash
   mkdir -p bookorbit/books data/app data/postgres
   curl -fsSLo .env https://raw.githubusercontent.com/bookorbit/bookorbit/main/.env.example
   curl -fsSLo docker-compose.yml https://raw.githubusercontent.com/bookorbit/bookorbit/main/docker-compose.yml
   ```
2. Edit `.env` and set required variables: `APP_URL`, `BOOKS_HOST_PATH`, `POSTGRES_PASSWORD`, `JWT_SECRET`, `SETUP_BOOTSTRAP_TOKEN`.  
3. If needed, set `PUID` and `PGID` to match the owner of the books folder (common cause of permission errors).  
4. Optionally set `LIBRARY_BROWSE_ROOT` to change the default library folder picker.  
5. Start the containers: `docker compose up -d`.  
6. Open the URL defined in `APP_URL` and complete setup using the bootstrap token.  
7. Full installation guide (reverse proxy, NAS permissions, external DB, env reference) at `bookorbit.app/installation`.

## KOReader Plugin
1. In BookOrbit, go to **Settings > KOReader**, generate credentials, and download the plugin.  
2. Unzip `bookorbit.koplugin.zip`.  
3. Copy `bookorbit.koplugin` to the KOReader device’s `plugins` folder.  
4. Restart KOReader, open a book, then use **Tools > BookOrbit Sync** to connect.  
5. Plugin is pre‑configured with server URL and credentials; no manual entry required.  
6. Detailed setup and sync options at `bookorbit.app/koreader-plugin`.

## Documentation & Contributing
- Full docs at `bookorbit.app` covering libraries, metadata, readers, Kobo sync, OPDS, users, OIDC, etc.  
- Migration guides for Audiobookshelf and Calibre‑Web Automated.  
- Development notes in `docs/DEVELOPMENT.md`.  
- Contribution workflow in `docs/CONTRIBUTING.md` (branch naming, tests, PR checklist, commit format).

## Translations
- Community translation project hosted on Crowdin.  
- Add new UI strings to `client/src/locales/en.json`; other languages are generated via Crowdin.  
- Localization process detailed in `docs/LOCALIZATION.md`.

## Support
- Questions & discussion: GitHub Discussions.  
- Bug reports & feature requests: GitHub Issues.  
- Security vulnerabilities: follow the private reporting procedure in the repository’s Security Policy.