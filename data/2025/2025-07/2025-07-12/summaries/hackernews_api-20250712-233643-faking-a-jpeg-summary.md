---
title: Faking a JPEG
url: https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/
date: 2025-07-11
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-07-12T23:36:43.343614
---

# Faking a JPEG

**Analysis**

The author, a solo developer, has been working on a web application called Spigot that generates fake JPEG images to evade aggressive web crawlers. The problem (or opportunity) being discussed is the need for a new solution to help keep this technology free and usable by legitimate users.

**Market Indicators**

- Over 1 million pages per day are served via Spigot within a few months, indicating its popularity.
- Two heavy-hitting crawler groups are utilizing automated botnets.
- The author finds these groups' actions suspicious, feeling sorry for their purposeful methods.

**Technical Feasibility**

- Parsing JPEGs to identify the compressed data and structure can be achieved with basic knowledge of file formats and compression algorithms (e.g., JPEG's chunking system).
- Since existing files are available, scanning them could provide a dataset for analysis.

**Business Viability Signals**

- There seems to be an audience willing to pay for solutions like this; no mention is made about pricing or revenue.
- The author provides open-source code and describes how to use it, suggesting that the project's existence benefits from having an example source (although there are no references to such).

**Actionable Insights**

- By scanning existing JPEGs, the author can identify new fake crawler groups and prioritize which ones should be targeted with optimizations like random data injection.
- A custom dataset should be created for analysis, possibly containing a representative selection of legitimate web pages in similar size distributions.
- Since crawling is performed remotely without user input or permission, using publicly available web platforms (e.g., public websites) could provide more reliable data sources.

Extracted numbers:
- Over 1 million pages per day served by Spigot.
- New crawler group discovered (ImageSiftBot).
- Thousands of requests made by ImageSiftBot per hour.

Quotes about pain points:
- "Eating excessive CPU on my server" to maintain efficiency for Spigot's functionality.
- Crawler groups' behavior is causing concerns ("Sad to think about how they're trying...")

Mentions of pricing or revenue: None as the description appears focused on development, open-source code sharing.
