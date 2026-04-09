---
title: You're using a too-old browser
url: https://utcc.utoronto.ca/~cks/space/blog/programming/ErrorsShouldRequireFixing
site_name: hackernews
fetched_at: '2025-12-21T11:07:26.053183'
original_url: https://utcc.utoronto.ca/~cks/space/blog/programming/ErrorsShouldRequireFixing
author: todsacerdoti
date: '2025-12-21'
---

# You're using a suspiciously old browser

You're probably reading this page because you've attempted to access
some part ofmy blog (Wandering Thoughts)orCSpace, the wiki thing it's part of. Unfortunately
you're using a browser version that my anti-crawler precautions consider
suspicious, most often because it's too old (most often this applies to
versions of Chrome). Unfortunately, as of early 2025 there's a plague
of high volume crawlers (apparently in part to gather data for LLM
training) that use a variety of old browser user agents, especially
Chrome user agents. To reduce the load onWandering ThoughtsI'm experimenting with
(attempting to) block all of them, and you've run into this.

If this is in error and you're using a current version of your
browser of choice, you can contact me atmy current place at the
university(you should be able to work out the email address
from that). If possible, please let me know what browser you're
using and so on, ideally with its exact User-Agent string.

## A special note for people using archive.*

You may be seeing this through archive.today, archive.ph, archive.is,
and so on. Unfortunately, archive.* crawls pages to archive in a way that
is impossible to distinguish from malicious actors. They use old Chrome
User-Agent values, crawl from IP address blocks that are widely distributed
and not clearly identified as theirs, and some of their IP addresses have
falsified reverse DNS entries that claim they are googlebot IP addresses
(which is something that is normally done only by quite bad actors). I
suggest that you use archive.org, which is a better behaved archival
crawler and can crawlmy blog (Wandering Thoughts).

Chris Siebenmann, 2025-02-17
