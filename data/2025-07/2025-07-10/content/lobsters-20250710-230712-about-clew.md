---
title: About Clew
url: https://clew.se/about/
site_name: lobsters
fetched_at: '2025-07-10T23:07:12.287788'
original_url: https://clew.se/about/
date: '2025-07-10'
description: Clew is a web search engine trying to be different from the rest. We focus on writing by independent creators and downrank sites with ads and trackers.
tags: web
---

Clew is a web search engine trying to be different from the rest.

* We focus on writing by independent creators. There's no point in indexing Wikipedia; it has its own perfectly serviceable search bar.
* We are not ad-supported; currently, Clew is a labor of love by Benjamin Hollon anddonation-supported.
* Because our funding source is not dependent on the interests of for-profit businesses and corporations, our search rankings are unbiased and apply the same standards equally to all indexed domains.
* In addition, we incorporate variables that would not be in the interests of commercial search engines, such as whether we detect invasive ads or tracking on a site and how much bandwidth pages require to download, perfect for individuals who want to see whether a website will respect their privacy and databeforeopening it.

## Behind the Name

A lot of thought went into the name "Clew". A clew is a ball of thread or yarn; specifically, we envisioned the clew from the Greek myth of Theseus and the Minotaur which leads Theseus safely through the labyrinth. This is an excellent metaphor for the task of a search engine; our job is to guide you safely through the labyrinthian World Wide Web safely to your destination.

We've also incorporated other names from the Theseus myth into our naming; our web crawler, for example, is named after Ariadne, who gave Theseus the clew.

## Disallowing our Crawler

If you would like to keep Ariadne from crawling your site, add the following to your/robots.txtfile:

User-agent: Ariadne
Disallow: /

We cache your old/robots.txtfor up to 24 hours, to avoid spamming your server with new requests for it every time we want to check a page, so it may take that long for Ariadne to stop crawling your site. Once we discover the change, though, we will remove affected pages from our index (discovering the change may take more than a week if we don't crawl your site during that time).

You can also set a crawl-delay to slow down the speed we crawl your site at:

User-agent: Ariadne
Crawl-delay: 10

The above would send a maximum of one request per ten seconds to your site. We assume a default crawl delay of two seconds.

We have seen some sites with ridiculously-high crawl delays (for example,86400seconds), and based on our research have concluded that other search engines use a cap on the crawl-delay (when they honor it at all), in which case such a high crawl-delay is, in-effect, a request to crawl atourcap. The cap for Ariadne is120seconds; if your server can't handle one request per two minutes, you should probably just disallow crawlers altogether.

Return home ↩
