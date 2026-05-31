---
title: The Website Specification
url: https://specification.website/
site_name: hackernews_api
content_file: hackernews_api-the-website-specification
fetched_at: '2026-06-01T04:17:21.414332'
original_url: https://specification.website/
author: k1m
date: '2026-05-31'
description: A platform-agnostic, full specification of the technical features a good website should have. Built in the open under an MIT licence.
tags:
- hackernews
- trending
---

# What a good website does.

 

A platform-agnostic specification of the technical features every
 decent website should have — from<title>to/.well-known/security.txt,
 from WCAG contrast tollms.txt.
 Written for humans and agents.

 
 

Browse all 128 topics →

 

Get the checklist

 

★ on GitHub

 
 
 
 
 
 
 

## Categories

 

Ten areas, mapped to widely-accepted standards.

 
 
All topics →
 
 
* ### Foundations14The HTML, head, and document basics every page needs.
* ### SEO13Search visibility — robots.txt, sitemaps, canonicals, structured data.
* ### Accessibility20WCAG-aligned rules so people of all abilities can use the site.
* ### Security12Headers, transport, and policies that keep visitors safe.
* ### Well-Known URIs9Standard, agreed-upon paths under /.well-known/.
* ### Agent Readiness18Things that make a site legible to AI agents and crawlers.
* ### Performance19Core Web Vitals, caching, images, fonts, network behaviour.
* ### Privacy6Consent, signals, and respecting visitor choice.
* ### Resilience5Graceful failure — error pages, offline, redirects.
* ### Internationalisation12Language, locale, direction, and translated content.
 
 
 
 
 

### Standards, not opinions

 

Each topic links back to the source standard — WHATWG, W3C, IETF RFCs, WCAG, MDN, and the organisations defining the modern web.

 
 
 

### Platform agnostic

 

Whether you ship WordPress, Drupal, TYPO3, Next.js, Astro, Hugo, a Django app, or plain HTML, the spec is the spec. Implementation hints follow it, not the other way round.

 
 
 

### Built in the open

 

Every page has anEdit on GitHublink. PRs welcome. Sources credited on every page.

 
 
 
 
 
 
 
 

## Let your agent query the spec.

 

The whole spec is available as an openMCPserver — read-only, no auth — plus a publishedAgent Skillthat teaches any compatible agent when and how to use it. Per-page Markdown is available via/llms.txtandAccept: text/markdownon any spec URL.

 
 
Connect MCP →
 
Agent Skill
 
llms.txt
 
Agent-readiness spec →
 
 
 
{
 "mcpServers": {
 "specification-website": {
 "transport": "http",
 "url": "https://mcp.specification.website/mcp"
 }
 }
}
 
 
 
 
 

## How to use this site

 
1. 01### AuditRun through thechecklist. Each item is a “does the site do this — yes or no.”
2. 02### LearnClick into any item for what it is, why it matters, and how to implement it.
3. 03### ImproveFound a gap, a stale fact, or a missing topic? Open a PR. Sources required.