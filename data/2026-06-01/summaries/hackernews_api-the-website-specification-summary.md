---
title: The Website Specification
url: https://specification.website/
date: 2026-05-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:19:57.520744
---

# The Website Specification

# Summary of “The Website Specification”

## Overview
- Provides a platform‑agnostic specification of technical features every decent website should have, from basic HTML elements to `.well-known/security.txt` and WCAG contrast tools.
- Intended for both human readers and automated agents.
- Includes a checklist and a GitHub repository for contributions.

## Categories
Ten main areas, each mapped to widely‑accepted standards:

- Foundations – HTML, head, and document basics.
- SEO – robots.txt, sitemaps, canonical links, structured data.
- Accessibility – WCAG‑aligned rules for all abilities.
- Security – headers, transport security, policies.
- Well‑Known URIs – standard paths under `/.well-known/`.
- Agent Readiness – features that make the site legible to AI agents and crawlers.
- Performance – Core Web Vitals, caching, images, fonts, network behavior.
- Privacy – consent signals and respecting visitor choices.
- Resilience – error pages, offline handling, redirects.
- Internationalisation – language, locale, direction, and translated content.

## Core Principles
- **Standards, not opinions** – Each topic links to its source standard (WHATWG, W3C, IETF RFCs, WCAG, MDN, etc.).
- **Platform agnostic** – The specification applies equally to WordPress, Drupal, TYPO3, Next.js, Astro, Hugo, Django, plain HTML, or any other stack; implementation hints follow the spec.
- **Built in the open** – Every page has an “Edit on GitHub” link; pull requests are welcomed and sources are credited.

## Agent Access
- The full specification is available as a read‑only open MCP server (no authentication).
- An Agent Skill is published to teach compatible agents when and how to use the spec.
- Per‑page Markdown can be retrieved via `/llms.txt` or by requesting `Accept: text/markdown` on any spec URL.
- Example MCP server configuration is provided in JSON format.

## How to Use the Site
1. **Audit** – Run through the checklist; each item is a yes/no question about the site.
2. **Learn** – Click any item to see its definition, importance, and implementation guidance.
3. **Improve** – If a gap, outdated fact, or missing topic is found, open a pull request with required sources.