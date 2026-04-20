---
title: "Making London's hidden film clubs discoverable - DEV Community"
url: https://dev.to/alistairjcbrown/i-built-a-film-club-discovery-tool-for-londons-cinema-community-2md
date: 2026-03-01
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-03-02T08:26:29.163655
---

# Making London's hidden film clubs discoverable - DEV Community

# Summary of “Making London’s hidden film clubs discoverable – DEV Community”

## Context
- The author built Clusterflick, a site that aggregates cinema listings across London.
- Initially it only showed what films were playing at which venues.
- The author realized this missed an important part of the scene: film clubs, many of which are invisible without prior knowledge.
- The goal became to make London’s diverse film club community discoverable and accessible.

## New Features
### Film Club Pages
- Each club gets its own dedicated page at `clusterflick.com/film-clubs`.
- Pages display the club’s logo, a short description, a link to its own site, and the full upcoming lineup across all venues where it screens.
- Accessibility information (relaxed screenings, subtitles, etc.) is highlighted directly from screening data.
- Example clubs showcased:
  - Bar Trash – cult and curiosity films.
  - Pitchblack Playback – immersive dark‑room listening sessions.
  - Lost Reels – reviving forgotten or unavailable films.

### Near Me
- Located at `clusterflick.com/near-me`, it uses the browser’s location API.
- Shows the closest venues, films playing there, and the film clubs attached to those screenings.
- Provides a simple answer to “What’s on near me tonight?” and “What film clubs are near me?” without needing a full map interface.
- Uses a 2‑mile radius as the definition of “near” after testing.

## Demo Links
- Film clubs page: `clusterflick.com/film-clubs`
- Near‑me page: `clusterflick.com/near-me`

## Technical Details
- Built with Next.js and TypeScript, hosted on GitHub Pages.
- Film club pages are server‑side rendered at build time; Near Me is client‑side rendered because it depends on user location.
- Data pipeline (GitHub repo `clusterflick/data-combined`) aggregates cinema data and tags screenings with organizers when available.
- CI/CD runs via GitHub Actions; the data pipeline updates twice daily, triggering automatic site rebuilds.

## Development Process
- Research and curation of club information were assisted by Claude (AI), then manually edited.
- Added 22 clubs initially, with plans to expand.
- Near‑me logic: fetch user coordinates, load venue data, calculate distances, sort, and render.
- The challenge served as a forcing function to ship features that had been pending in multiple GitHub issues.

## Impact
- Transforms Clusterflick from a simple listings aggregator into a community directory.
- Makes hidden film clubs easier to find, understand their accessibility options, and attend events.
- Provides London film‑goers with a practical “near me” tool for both mainstream screenings and niche club events.
