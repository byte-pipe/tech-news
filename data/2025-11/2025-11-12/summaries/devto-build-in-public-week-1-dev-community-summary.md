---
title: Build in Public: Week 1 - DEV Community
url: https://dev.to/olgabraginskaya/build-in-public-week-1-o8a
date: 2025-11-08
site: devto
model: llama3.2:1b
summarized_at: 2025-11-12T11:19:38.701521
screenshot: devto-build-in-public-week-1-dev-community.png
---

# Build in Public: Week 1 - DEV Community

**Week 1 Update: Building in Public - DEV Community**

The first week of the project was marked by a challenging transition from our old N8N setup to a normal backend while exploring what "normal" means for us. Additionally, having our first team conflict and real issues with Bright Data forced us to review and revise our approach.

A notable surprise occurred during the first week, with the idea "Build in Public: Day Zero" reaching top 7 of Dev.to's weekly list, sparking interest from others on social media platforms like LinkedIn and Twitter.

**Backend Progress**

After several weeks of collaboration between Alex (Full-Stack Developer) and me (Data Engineer), we've developed a working backend. However, due to our differing technical backgrounds, a significant setback has occurred, with both developers unable to agree on a language or specific approach for the project at this stage.

We're currently focusing on Instagram and utilizing Bright Data's Instagram API scrapers for their asynchronous API. The scraped data includes relevant information such as username, full name, follower count, following, bio, profile image, engagement rate, related accounts, recent posts with captions, likes, and more.

**Model Analysis**

To integrate the scrapped data into our analysis model, we've used OpenRouter from anthropic/claude-3.5-sonnet and Pydantic AI for language models. The response to Taylor Swift's profile was a clean JSON that allows us to reuse the analysis logic later or filter specific information.

**Conclusion**

The first week of the project has been challenging, but we've made significant progress in developing our backend and analyzing scrapped data from Bright Data. As we continue working on this project, we'll aim to refine our approach, adapt to new technologies and requirements, and establish a sustainable workflow for future development.
