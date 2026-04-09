---
title: Faking a JPEG
url: https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/
date: 2025-07-13
site: hackernews
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-13T23:41:48.417565
---

# Faking a JPEG

Here's a 3-4 paragraph analysis of the 'Faking a JPEG' article from a solo developer business perspective:

The article discusses the problem of aggressive web crawlers that abuse websites by sending large volumes of requests, often in an attempt to scrape content. The author has created a tool called Spigot that generates fake web pages to feed these crawlers, reducing the burden on his server. However, the author noticed that one of the crawlers, ImageSiftBot, was specifically looking for images to ingest.

This presented an opportunity for the author to create a low-cost solution to generate fake JPEG images that would satisfy the crawler's demands. By analyzing the structure of JPEG files and creating templates from existing images on his site, the author was able to develop a system that could generate thousands of fake JPEG images per second, with minimal CPU usage. This is a clear example of a 'boring problem' that businesses and website owners would likely pay to solve, as it helps reduce the impact of abusive crawlers.

From a technical feasibility standpoint, the approach described in the article seems well within the capabilities of a solo developer. The author was able to implement the core functionality in under 100 lines of Python code, demonstrating the relatively low complexity involved. The main technical challenge was dealing with the Huffman coding used in JPEG files, but the author was able to find a pragmatic solution that reduced the probability of generating invalid images without significantly increasing the CPU requirements.

In terms of business viability, the article suggests that the author has already seen significant adoption of his solution, with ImageSiftBot and other major crawlers actively using the fake JPEG images. While the article does not mention any pricing or revenue figures, the fact that the author is willing to release the code on GitHub indicates that there may be a broader market for this type of tool. Additionally, the low development cost and high-performance generation capabilities make this a potentially attractive offering for solo developers or small teams looking to address the problem of abusive web crawlers.
