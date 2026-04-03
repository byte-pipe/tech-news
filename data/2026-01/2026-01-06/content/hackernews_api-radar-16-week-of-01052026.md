---
title: 'Radar #16: Week of 01/05/2026'
url: https://loworbitsecurity.com/radar/radar16/
site_name: hackernews_api
fetched_at: '2026-01-06T11:07:06.033821'
original_url: https://loworbitsecurity.com/radar/radar16/
author: illithid0
date: '2026-01-05'
published_date: '2026-01-05T21:00:42.000Z'
description: There were BGP anomalies during the Venezuela blackout
tags:
- hackernews
- trending
---

radar


# Radar #16: Week of 01/05/2026

Jan 5, 2026—Graham Helton

## Radar #16: Week of 01/05/2026

The Low Orbit Security Radar is a weekly security newsletter from an offensive practitioner's perspective. One idea, curated news, and links worth your time.

# News: There Were BGP Anomalies During The Venezuela Blackout

When watching the situation in Venezuela unfold, the phrase "It was dark, the lights of Caracas were largely turned off due to a certain expertise that we have" caught my attention. I do not wish to comment on the geopolitical situation other than to provide some insights within my area of competency, specifically, offensive security.

During a press conference,General John D. Cainestated: "As they approached Venezuelan shores the United States began layering different effects provided by SPACECOM, CYBERCOM, and other members of the inter-agency to create a pathway". Cyber operations preceding traditional military actions have become a common pattern so I started digging into the reported internet outages.

BGPis the first thing that comes to mind. It's a protocol used by routers to determine what path data takes to get to it's destination, it does this by exchanging routing information between Autonomous Systems. It is alsonotoriously insecureand much of the data about BGP is collected in public datasets. Every major network has an Autonomous System Number or ASN. CANTV (AS8048) is Venezuela's state-owned telecom, so that's the obvious place to start.

Cloudflare Radar's route leak datafor AS8048 on January 2nd had some interesting anomalies: 8 prefixes (blocks of IP addresses) were being routed through CANTV, with Sparkle (an Italian transit provider) and GlobeNet (a Colombian carrier) in the Autonomous System (AS) path. The AS path is essentially the list of networks traffic passes through to reach its destination. CANTV was in a path it is not typically a part of.

There was also a noticeable spike in BGP announcements in the days leading up to the events and a drastic dip in the "Announced IP Address Space" according to the sameCloudflare Radardata, although it's unclear what this indicates.

Notably, Sparkle is one of the transit providers in the AS pathlisted as "unsafe" on isbgpsafeyet.com, meaning they don't implement some BGP security features such asRPKI filtering.

Cloudflare shows that a leak happened, but not the actual network prefixes. The network prefixes are useful to determine what infrastructure was potentially affected. Fortunately public datasets collect this BGP information. Pulling the data fromris.ripe.net/docs/mrtfrom around the time of the leak and using a tool calledbgpdumpwe can extract the data into a readable format:

TIME: 01/02/26 15:41:16
TYPE: BGP4MP/MESSAGE/Update
FROM: 187.16.222.45 AS263237
TO: 187.16.216.23 AS12654
ORIGIN: IGP
ASPATH: 263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980
NEXT_HOP: 187.16.222.45
COMMUNITY: 0:6939 65237:1020
ANNOUNCE
 200.74.228.0/23
 200.74.236.0/23
 200.74.230.0/23
 200.74.238.0/23
 200.74.226.0/24

After some more processing withbgpdumpwe can get a much better view of the data, including the prefixes that were missing from the Cloudflare radar.

BGP4MP|1767368421|A|187.16.208.144|24482|200.74.230.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.236.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.228.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.238.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.226.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.232.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.233.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.208.144|24482|200.74.234.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.208.144|0|0|24115:52320 24115:65012 24482:2 24482:200 24482:13000 24482:13020 24482:13021 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368421|A|187.16.222.45|263237|200.74.234.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368421|A|187.16.222.45|263237|200.74.233.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368421|A|187.16.222.45|263237|200.74.232.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.228.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.236.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.230.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.238.0/23|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368446|A|187.16.222.45|263237|200.74.226.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 6762 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368450|A|187.16.222.45|263237|200.74.234.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368450|A|187.16.222.45|263237|200.74.233.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368450|A|187.16.222.45|263237|200.74.232.0/24|263237 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.222.45|0|0|0:6939 65237:1020|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.234.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.232.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.233.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.238.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.228.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.226.0/24|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.236.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||
BGP4MP|1767368451|A|187.16.208.144|24482|200.74.230.0/23|24482 52320 8048 8048 8048 8048 8048 8048 8048 8048 8048 23520 1299 269832 21980|IGP|187.16.208.144|0|0|24482:2 24482:200 24482:13000 24482:13020 24482:13021 24482:65304 52320:41912 52320:61056 52320:64123|NAG||

More information about the format can be seen inWorking with Raw BGP Databut of note, the AS path has 8048 (CANTV) repeated 10 times, is very odd as this would make the routelessattractive since BGP prefers shorter paths. Also of note is all8 prefixes fall withina200.74.224.0/20block.

200.74.226.0/24
200.74.228.0/23
200.74.230.0/23
200.74.232.0/24
200.74.233.0/24
200.74.234.0/24
200.74.236.0/23
200.74.238.0/23

A quick WHOIS lookup shows this range belongs to Dayco Telecom, a hosting and telecommunications provider in Caracas.

Areverse DNS lookupcan be used to find the domain name from an IP address. Interestingly, looking up some of these ranges turns up some pretty critical infrastructure including banks, internet providers, email servers, and more.

BGP anomalies happen frequently, but the timing of some currently unexplained BGP activity is very interesting.

Time (UTC)

Event

Source

Jan 2, 15:40

BGP route leak detected

Cloudflare Radar

Jan 3, ~06:00

First explosions reported in Caracas

NPR

Jan 3, 06:00

US soldiers reach Maduro's compound

NBC News

Jan 3, 08:29

Maduro aboard USS Iwo Jima

CNN

When BGP traffic is being sent from point A to point B, it can be rerouted through a point C. If you control point C, even for a few hours, you can theoretically collect vast amounts of intelligence that would be very useful for government entities. The CANTV AS8048 being prepended to the AS path 10 times means there the traffic would not prioritize this route through AS8048, perhaps that was the goal? There are many unanswered questions.

Regardless of the actual goal, there were undoubtedly some BGP shenanigans happening during this time frame. There is a lot of data publicly available that is worth a much deeper dive to understand exactly what happened.

## Low Orbit Security Radar

Get the radar delivered directly to your inbox every Monday Morning.

Subscribe

 Email sent! Check your inbox to complete your signup.


No spam. Just Security.

## Caught My Eye

* MCP Security: Your AI's Prompts, Reasoning, and Secrets Are at Risk: A deepdive demonstrating how malicious MCP servers can exfiltrate prompts, reasoning, and .env files.
* I Canceled My Book Deal: A professor walks away from a traditional publishing contract after the publisher pushed for AI integration, offered low royalties, and wanted to strip personality from the content. The numbers roughly align with ones I've seen from other publishers.
* The Year in LLMs (2025): A year in review covering reasoning models, coding agents, Chinese open weight models, MCP adoption, and the evolution of "vibe coding".
* Linux is Good Now: 2026 is the year of the Linux desktop?!?!? Unironically I think two things are making this a reality. 1. Valve's work making more gaming possible on via its ventures with the Steamdeck (runs arch btw) and 2. Microsoft making the OS more hostile than trusted with it's integration of AI into the OS.
* No strcpy Either: The curl project eliminated strcpy() after previously removing strncpy(), creating a wrapper that requires explicit buffer sizes. Partly motivated by preventingAI vulnerability reports.
* hindsight: A CLI tool that scans local directories for git repos and aggregates contribution history heatmap.
* Pomerium: An open source identity and context-aware access proxy providing access to internal applications.
* Frontier Data Centers Satellite Explorer: Track major AI data centers via satellite imagery and permit analysis.
* Ghostty Finances: Public financial transparency page for the Ghostty project through Hack Club Bank. Very cool way for non-profits to track spending.
* AI Coding Exhaustion (HN Discussion): Interesting read about whether AI enables fewer or more abstractions.
* News Minimalist: News aggregator that ranks articles by a "significance score", filtering for impact, novelty, and credibility. Interesting use case.
* mymind: Visual bookmarking and note-taking tool that saves content without manual tagging.
* Are.na: Similar to mymind but has more of a "community" vibe. Similar to Pinterest.
* How I Browse the Web in 2026: An interesting personal workflow for intentional web browsing. Some cool ideas in here.
* ML Math: Free machine learning mathematics resources and tutorials. I specifically like the visualizations.
* Kubernetes Networking Best Practices: Great guide covering CNI selection, network policies, service mesh, and troubleshooting.
* Bypass macOS Antivirus with tclsh: Using Tcl's built-in interpreter to bypass antivirus protections on macOS.PoC Gist.
* Cloudflare Radar: The Cloudflare Radar (nice name btw) I found while investigating the above story. Some really cool data

Want more? Check back next Monday morning or get the latest Radar issue directly in your inbox.

## Low Orbit Security Radar

Get the radar delivered directly to your inbox every Monday Morning.

Subscribe

 Email sent! Check your inbox to complete your signup.


No spam. Just Security.
