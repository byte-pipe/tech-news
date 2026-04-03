---
title: Faking a JPEG
url: https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/
date: 2025-07-12
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-07-13T23:22:07.268183
---

# Faking a JPEG

Analysis:

The article discusses the issue of fake or malicious web crawlers using software like Spigot to generate non-existent images for their bots to ingest. The problem is not just about fixing this one issue but also about exploring alternative business opportunities.

**Market indicators:**

* Over a million pages per day on Spigot, indicating significant traffic.
* Two crawler types are highlighted as particularly tough to crack (ImageSiftBot and... another unknown crawler).
* There's no mention of revenue or pricing, suggesting that this business might not generate significant income yet.

**Technical feasibility for a solo developer:**

* Building a JPEG generator without too much complexity would require only basic image processing knowledge.
* The problem of parsing existing JPGs can be solved with scanning existing files, as mentioned.

**Business viability signals:**

* Existing competitors appear to have been trying to fix this issue (e.g., identifying and removing non-existent images from feeds).
* There's no mention of distribution channels or who or what would acquire a solution like this service.
* A potential barrier to entry might be the need for significant upfront investment in either creating the tool itself or acquiring existing JPGs.

Specific insights:
- The author mentions using "loads" of existing JPEGs, indicating the task is relatively manageable with proper tools and software.
- They propose scanning a bunch of existing files to find hidden crawlers or other patterns that could help identify a heavy hitter (e.g., more requests per hour) leading them to add it to Spigot's front page for tracking.

Actionable insights:

* Given the significant traffic on Spigot, exploiting similar vulnerabilities by detecting and removing fake images might provide a quick win.
* Identifying hidden crawlers or patterns that lead to identifying heavy hitters could also yield results (though this would likely require more time than initially proposed).
- The author should also explore other potential business opportunities related to image processing or crawling, focusing on where they can offer solutions rather than just fixing the immediate issue.
