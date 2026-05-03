---
title: HN SOTA — Model popularity | HN Update
url: https://hnup.date/hn-sota
site_name: hackernews_api
content_file: hackernews_api-hn-sota-model-popularity-hn-update
fetched_at: '2026-05-04T06:00:17.277082'
original_url: https://hnup.date/hn-sota
author: yunusabd
date: '2026-05-03'
description: 'LLM model popularity from Hacker News: how we detect models from the OpenRouter catalog and score sentiment from discussions.'
tags:
- hackernews
- trending
---

# State of the Art of Coding Models,According to Hacker News Commenters

 

The space of AI-assisted coding is evolving rapidly. This is an attempt at staying up to date
			with the latest developments, by capturing popularity and user sentiment of coding models fromHacker Newscomments. Updated daily.

 

Each day, the pipeline

 
1. Gets the 200 most popular posts in a 24h window from the Hacker News API.
2. Prompts an LLM to select those posts whose titles are about LLMs or coding in general (max.
				50), as we expect more relevant discussions in those posts (assumption on my part).
3. For each post, sends the title and comments to Gemini and asks it to identify models from
				the OpenRoutermodel listand rate the sentiment towards each mentioned model per comment.
 

I wanted the ability to audit the process and the results, for debugging and for occasional
				sanity checks of the model outputs. So the results are logged to aGoogle Sheet, where you can see the comment IDs that mention specific models and the sentiment that the
				model determined for that comment and model.

 

You can open a comment by appending the comment ID tohttps://news.ycombinator.com/item?id=.

 

## Top 10 Model Popularity

 

Total mentions and user sentiment of specific models, 10 days trailing aggregate (2026/4/23 to 2026/5/2).

 
 
Scale bars to 100%
 
 
 

Google Sheets linkwith granular results.

 

Home

 

LingoLingo - Learn languages with YouTube!