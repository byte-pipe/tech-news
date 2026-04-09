---
title: Faking a JPEG
url: https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/
date: 2025-07-12
site: hackernews_api
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-13T23:41:34.270616
---

# Faking a JPEG

Here's a 3-4 paragraph analysis of the article 'Faking a JPEG' from a solo developer business perspective:

The article discusses the problem of aggressive web crawlers that abuse websites by generating large numbers of requests, often in an attempt to hide their identity. The author has created a tool called Spigot that generates fake web pages to feed these crawlers, reducing the load on the server. However, the author noticed that one of the crawlers, ImageSiftBot, was specifically looking for images to ingest.

This presented an opportunity for the author to create a low-cost solution to generate fake JPEG images that would satisfy the crawler's demands. By analyzing the structure of JPEG files and creating templates from existing images, the author was able to generate realistic-looking JPEG files on the fly, filling the compressed data sections with random bytes. This approach is highly efficient, allowing the author to generate around 900 such images per second on their web server.

From a solo developer business perspective, this project demonstrates several promising signals. The author has identified a specific user pain point (aggressive web crawlers) and developed a technical solution that is both effective and efficient to implement. The ability to generate 190MB/s of fake JPEG data suggests a high degree of technical feasibility for a solo developer. Additionally, the author mentions that the fake images are being eagerly consumed by several major web crawlers, indicating a clear market demand and willingness to pay for such a solution. While the author has not disclosed any revenue figures, the low development cost and high throughput suggest this could be a viable business opportunity for a solo developer.
