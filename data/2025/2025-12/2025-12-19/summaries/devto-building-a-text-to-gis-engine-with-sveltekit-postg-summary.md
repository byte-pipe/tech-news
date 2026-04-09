---
title: "Building a \"Text-to-GIS\" Engine with SvelteKit, PostGIS and Open-Source LLMs - DEV Community"
url: https://dev.to/zeekrey/building-a-text-to-gis-engine-with-sveltekit-postgis-and-open-source-llms-57bo
date: 2025-12-18
site: devto
model: llama3.2:1b
summarized_at: 2025-12-19T11:21:04.763934
screenshot: devto-building-a-text-to-gis-engine-with-sveltekit-postg.png
---

# Building a "Text-to-GIS" Engine with SvelteKit, PostGIS and Open-Source LLMs - DEV Community

## Building a "Text-to-GIS" Engine with SvelteKit, PostGIS and Open-Source LLMs - DEV Community Summary

The text describes an innovative approach to building a GIS engine that converts natural language queries into SQL queries for a PostGIS database. The author's goal is to demonstrate how no commercial Large Language Model (LLM) requires sending sensitive schema data or internal customer information to a hyperscaler.

### Key Points and Essential Details:

*   The author works with a local energy provider in Germany as a data scientist, highlighting the importance of understanding local data limitations.
*   SvelteKit serves as the web app framework for developing the system, providing an open-source base that can be run in Germany without relying on a US API.

### Structured Organization:

-   **Background:** A conversation was had between two individuals, with one revealing their expertise as "a human SQL converter," making use of complex PostGIS queries daily.
-   **The Solution:** It is found that users don't necessarily need a huge commercial LLM to execute SQL queries. By injecting schema context and enforcing strict rules, the system can generate valid SQL queries.

### Real-Life Applications:

*   The text mentions building a smallText-to-SQL + PostGIS demo using open data from Leipzig.
*   It also talks about implementing a search query for parks in Leipzig, resulting in a GeoJSON layer that can be rendered on a map.

### Tech Stack and Architecture:

-   SvelteKit: Used as the web app framework due to its open-source base, which allows it to be run locally with minimal dependencies.
-   PostgreSQL + PostGIS: Employed for spatial queries due diligence on potential performance issues.
-   Hosted open-weights code model, Qwen3-Coder:30B AI SDK: Used to integrate LLM calls into the SvelteKit app.

### The Real "Secret" Behind Success:

*   **Schema Context and Rules:** Injecting schema context and enforcing strict rules became the hard part rather than coding. This realization enabled developers to create a more robust and efficient user interface.

This concise summary preserves the original text's meaning, grammar, and narrative style while adhering to Markdown guidelines.
