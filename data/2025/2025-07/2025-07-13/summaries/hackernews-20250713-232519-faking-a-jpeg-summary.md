---
title: Faking a JPEG
url: https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/
date: 2025-07-13
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-13T23:25:19.030294
---

# Faking a JPEG

**Analysis**

The article discusses the solo developer business, Spigot, which creates fake JPEG images for web crawlers to ingest and use to identify aggressive crawling behavior. The author's goal is to find a more efficient way to generate these fake images without overloading the server with excessive CPU usage. They propose an idea of modifying existing fake JPEG files to make them look more random, thus deceiving crawlers.

**Market Indicators**

* Over a million pages are generated per day by Spigot.
* Two hard-to-trace crawlers target multiple servers in the past few months.
* The article mentions that crawl behavior can be tracked and reported on the Spigot front page.
* Currently, there is no mention of revenue or pricing information.

**Technical Feasibility**

* Requires a basic understanding of JPEG file structure and formatting.
* Can be done relatively quickly with existing tools and knowledge.
* CPU efficiency could be improved by using templates and compression optimization techniques.

**Business Viability Signals**

* Existing competition for crawlers is limited, although unmentioned.
* Willingness to pay: no specific mention of pricing or revenue, but the author mentions being "sorry" for the heavy hitter's plight, implying a business case making more efficient image generation worthwhile.
* Distribution channels: likely self-contained server and potential public access (unmentioned).

**Actionable Insights**

1. **Prioritize efficient compression**: Improving template construction to reduce CPU load on Spigot will help alleviate resource strain.
2. **Use existing tools effectively**: The article encourages the author to leverage their existing knowledge of JPEG file structure, which is a time-and-money-saving approach.
3. **Optimize for performance**: Experiment with compression optimization techniques and modular designs to further enhance CPU efficiency.

Note: The author's primary goal appears to be satisfying the heavy hitter without compromising Spigot's operations or scalability. By generating throw-away garbage that looks random during compression, they can redirect excess computational resources towards generating more complex and realistic fake images in the future, thus increasing the value proposition for their solo developer business.
