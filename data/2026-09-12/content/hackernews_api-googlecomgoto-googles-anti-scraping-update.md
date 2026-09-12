---
title: 'google.com/goto: Google''s anti-scraping update'
url: https://www.autom.dev/blog/google-search-goto-links
site_name: hackernews_api
content_file: hackernews_api-googlecomgoto-googles-anti-scraping-update
fetched_at: '2026-09-12T13:52:47.768250'
original_url: https://www.autom.dev/blog/google-search-goto-links
author: 1e1a
date: '2026-09-12'
description: Google is rolling out google.com/goto redirect URLs on SERPs. Here is what changed, why it targets scrapers, and how Autom updated its Google Search API.
tags:
- hackernews
- trending
---

## What's happening

Google Search is rewriting organic result links togoogle.com/goto?url=...instead of exposing the destination URL directly in the HTML.

When you click a result, Google redirects you to the real page. Theurlparameter uses a custom, Google-specific encoding. It is not a plain base64 of the target URL. In practice, it looks like an opaque reference to Google's index record for that page.

As of late August 2026, this is showing up consistently across searches when you are logged out or browsing in private mode. It may still be an experiment, but it is no longer limited to a small slice of SERPs.

## Not the same as google.com/url

Google has used redirect wrappers before. The older format isgoogle.com/url?q=[URL-encoded destination], where the target link is readable in the query string.

The newgotoformat is different:

* The resulthrefis/goto, not the destination
* You cannot decode theurl=blob offline
* The real URL is in theLocationheader on/goto. Request that URL. Do not follow the redirect.

Google still needs the destination to draw the SERP (domain, favicon, attribution), so copies of the URL remain on the page. That is a separate story from readingLocation. The walkthrough is here:google.com/goto: read Location with HEAD.

That shift matters for anyone building a search index from SERP data at scale.

## Why Google is doing this

This fits Google's broader push against automated SERP harvesting, especially from AI crawlers and SEO scrapers that bulk-extract result URLs to build their own indexes.

With plaintext links, a scraper could parse thousands of URLs from HTML without touching Google again. Withgoto, each result needs a request back to Google just to learn the destination. You readLocation; you do not follow through to the page. That is slower, noisier, and gives Google a clear signal when the same client resolves hundreds of links in sequence.

Combined with earlier moves like removing&num=100and tightening BotGuard/SearchGuard, Google is steadily raising the cost of naive SERP scraping.

## What we saw at Autom

We first spottedgotolinks on a small percentage of SERPs. At that level, it was hard to ship a reliable fix without breaking responses for everyone else.

As of late August 2026, the pattern is much more consistent for logged-out and private sessions. Result URLs on Google Search are effectively allgotoin those conditions.

We have been monitoring the rollout and testing against it.

## Update at Autom.dev

We have updated our Google Search pipelineto resolvegoogle.com/gotolinks (readLocation, no follow) and return the final destination URL in API responses, in the same structured fields customers already use.

If you call Autom's Google Search endpoints, you should keep getting usable destination URLs without changing your integration. We will keep watching Google's rollout and adjust if the redirect format shifts again.

## Related reading

* google.com/goto: read Location with HEAD
* Google killed num=100
* Google sues SerpAPI: What SearchGuard reveals
* Scraping SERP with Google, Bing, and Brave

Need live SERP data while Google keeps moving the goalposts? Try 1,000 free requests onAutom pricing, or get an API key atapp.autom.dev/register.

### Read also

Google

## Need To Know About Google Search API

Autom Team
|
Jan 15, 2026

Google

## Google tests dropping 100 results per page parameter

Autom Team
|
Sep 12, 2025

Automation

## SERP Scraping for Paperclip AI Agents: Real Search Data at Scale

Autom Team
|
Mar 11, 2026

Google

## 4 HasData Alternatives For Google Search Scraping in 2026

Autom Team
|
Mar 6, 2026

## SERPAPI

Discover why Autom is the preferred API provider for developers.

Deploy your SERP scraper
View pricing