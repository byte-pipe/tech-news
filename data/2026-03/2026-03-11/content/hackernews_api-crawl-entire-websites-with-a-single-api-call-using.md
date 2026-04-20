---
title: Crawl entire websites with a single API call using Browser Rendering · Changelog
url: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/
site_name: hackernews_api
content_file: hackernews_api-crawl-entire-websites-with-a-single-api-call-using
fetched_at: '2026-03-11T11:16:13.009093'
original_url: https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/
author: jeffpalmer
date: '2026-03-10'
description: Browser Rendering's new /crawl endpoint lets you submit a starting URL and automatically discover, render, and return content from an entire website as HTML, Markdown, or structured JSON.
tags:
- hackernews
- trending
---

# Changelog



New updates and improvements at Cloudflare.



 Subscribe to RSS


 View RSS feeds








←

Back to all posts





## Crawl entire websites with a single API call using Browser Rendering



Mar 10, 2026



Browser Rendering






You can now crawl an entire website with a single API call usingBrowser Rendering's new/crawlendpoint, available in open beta. Submit a starting URL, and pages are automatically discovered, rendered in a headless browser, and returned in multiple formats, including HTML, Markdown, and structured JSON. This is great for training models, building RAG pipelines, and researching or monitoring content across a site.

Crawl jobs run asynchronously. You submit a URL, receive a job ID, and check back for results as pages are processed.

Terminal window
# Initiate a crawl
curl

-X

POST

'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl'

\

-H

'Authorization: Bearer <apiToken>'

\

-H

'Content-Type: application/json'

\

-d

'{

"url": "https://blog.cloudflare.com/"

}'

# Check results
curl

-X

GET

'https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}'

\

-H

'Authorization: Bearer <apiToken>'

Key features:

* Multiple output formats- Return crawled content as HTML, Markdown, and structured JSON (powered byWorkers AI)
* Crawl scope controls- Configure crawl depth, page limits, and wildcard patterns to include or exclude specific URL paths
* Automatic page discovery- Discovers URLs from sitemaps, page links, or both
* Incremental crawling- UsemodifiedSinceandmaxAgeto skip pages that haven't changed or were recently fetched, saving time and cost on repeated crawls
* Static mode- Setrender: falseto fetch static HTML without spinning up a browser, for faster crawling of static sites
* Well-behaved bot- Honorsrobots.txtdirectives, includingcrawl-delay

Available on both the Workers Free and Paid plans.

To get started, refer to thecrawl endpoint documentation.
If you are setting up your own site to be crawled, review therobots.txt and sitemaps best practices.
