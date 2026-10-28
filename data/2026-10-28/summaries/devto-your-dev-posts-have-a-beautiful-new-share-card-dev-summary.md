---
title: Your DEV posts have a beautiful new share card ✨ - DEV Community
url: https://dev.to/devteam/your-dev-posts-have-a-beautiful-new-share-card-4be8
date: 2026-10-27
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-28T12:08:54.741724
---

# Your DEV posts have a beautiful new share card ✨ - DEV Community

# Your DEV posts have a beautiful new share card ✨ - DEV Community

## Overview
- Introduced a generated social image for articles that lack a cover image (covers 73 % of recent posts).  
- Replaces the old title‑based card with a quote card that displays the opening of the post, author byline, and brand colors.  
- One image works on X, LinkedIn, Slack, iMessage, and other platforms, sized to respect X’s 80 px keep‑clear zone.

## Design details
- Card mimics a browser window frame over a soft mesh gradient.  
- Byline row includes avatar, author name, publish date, reading time, and the community logo (fallback to default logo).  
- X’s title label sits only on the gradient; the card is vertically centered for other platforms.  
- Quote extraction (Images::SocialImageQuote):
  * Uses top‑level opening paragraphs, skipping fully italic paragraphs, headings, code blocks, images, blockquotes, and paragraphs that repeat the title.  
  * Joins short paragraphs until at least 80 characters, then cuts at the last sentence end within 180 characters or at a word with “…”.  
  * Falls back to the title when no suitable paragraph exists.  
- Colors:
  * Author’s brand color (or organization’s background color) creates an analogous palette.  
  * If no brand color is set, one of four Forem gradient palettes is chosen based on the article ID (only ~6 % of cover‑less posts have a brand color).

## Regeneration triggers
- Image is regenerated when title, publish date, author, reading time, or the selected quote changes.  
- Edits to later paragraphs that do not affect the quote do not cause a re‑render.

## Bug fixes addressed
- Proper escaping of user text in ImageMagick `caption:/label:` to prevent stray backslashes and file‑read attacks.  
- Unicode handling: stylized Unicode names are NFKC‑normalized; unsupported emoji are removed.  
- Font settings are applied before draw calls, fixing missing fonts on the date.  
- Text wrapping now uses real glyph widths instead of simple character counts.

## Performance
- Approximately 1–2 seconds per article on the developer’s machine.  
- Intermediate steps use uncompressed MIFF; PNG is encoded only once, eliminating a previous bottleneck.  
- Gradient drawn at 400 × 209 and scaled up.  
- Final output: 8‑bit RGB PNG, about 100 KB.  
- No external services or AI; pure ImageMagick 6 operations (compatible with Debian bullseye).

## QA instructions
1. Publish a post without a cover image and let `Images::SocialImageWorker` run; verify `article.social_image`.  
2. Paste the post URL into X’s composer and LinkedIn’s preview; confirm the quote and byline are fully visible, with X’s title label covering only the gradient.  
3. Edit the first paragraph → image regenerates; edit a later paragraph (same reading time) → no regeneration.

## Tests added
- Paragraph selection, skip rules, sentence/word cuts, Unicode cleanup, title fallback.  
- Image generation for Article/User/Organization with correct X keep‑clear zone and vertical centering.  
- Real ImageMagick render at 1200 × 627.  
- Regression test for `@`/`%` escaping, palette selection, name/meta helpers, logo caching.  
- Triggers for quote change, later edits, and reading‑time updates.

## Deployment notes
- No database migration or backfill required.  
- Existing images update automatically when relevant fields change.

## User‑facing description
- Every post now receives a quote card that shows the opening lines, author avatar, name, publish date, and reading time.  
- Color is derived from the author’s brand color or a rotating palette, giving a varied and bright appearance.  
- A single image unfurls everywhere; top and bottom margins keep details clear even when platforms overlay their own labels.  
- Additional polish: clean handling of `@` and `%` in names, proper rendering of stylized Unicode names, and automatic refresh when reading time changes.