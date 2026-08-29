---
title: GitHub - bigskysoftware/htmx: </> htmx - high power tools for HTML · GitHub
url: https://github.com/bigskysoftware/htmx
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:03:05.468399
---

# GitHub - bigskysoftware/htmx: </> htmx - high power tools for HTML · GitHub

# htmx – high power tools for HTML

## Overview
- Small (~14 KB gzipped), dependency‑free JavaScript library.
- Provides AJAX, CSS transitions, WebSockets, and Server‑Sent Events via HTML attributes.
- Extensible and positioned as the successor to intercooler.js.

## Motivation
- Removes arbitrary HTML constraints:
  - Not limited to `<a>` and `<form>` for HTTP requests.
  - Not limited to click and submit events.
  - Supports methods beyond GET and POST.
  - Enables partial page updates instead of full‑screen replacement.

## Quick Start
- Include the library from a CDN:
```html
<script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.10/dist/htmx.min.js"
        integrity="sha384-H5SrcfygHmAuTDZphMHqBJLc3FhssKjG7w/CeCpFReSfwBWDTKpkzPP8c+cLsK+V"
        crossorigin="anonymous"></script>
```
- Example button that posts via AJAX and swaps its own HTML:
```html
<button hx-post="/clicked" hx-swap="outerHTML">Click Me</button>
```

## Installation
- npm package: `npm install htmx.org --save` (the older package named `htmx` is broken).

## Documentation & Website
- Main site: https://htmx.org
- Documentation: https://htmx.org/docs

## Contributing & Sponsorship
- Contribution guidelines are provided in the repository.
- Sponsorship is welcomed for those unable to contribute code.

## Development Guide
- Install development dependencies: `npm install`.
- Run a local server: `npx serve`.
- Access the test suite at `http://0.0.0.0:3000/test/`.
- Test structure includes core, attribute‑specific, extension, manual, and regression tests.
- Uses mocha, chai, and sinon for testing.

## Haiku
- javascript fatigue: longing for a hypertext already in hand