---
title: HN SOTA — Model popularity | HN Update
url: https://hnup.date/hn-sota
date: 2026-05-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-04T06:01:42.962212
---

# HN SOTA — Model popularity | HN Update

# State of the Art of Coding Models, According to Hacker News Commenters

## Overview
- Daily pipeline monitors AI‑assisted coding model popularity and user sentiment from Hacker News comments.  
- Steps:
  1. Retrieve the 200 most popular posts from the Hacker News API within a 24‑hour window.  
  2. Prompt an LLM to select up to 50 posts whose titles relate to LLMs or coding.  
  3. Send each post’s title and comments to Gemini, which identifies models (from the OpenRouter list) and rates sentiment toward each mentioned model per comment.  

## Data Collection & Auditing
- All results are logged to a Google Sheet for transparency, debugging, and occasional sanity checks.  
- The sheet records comment IDs, the models mentioned, and the sentiment assigned by the model.  
- A comment can be opened directly by appending its ID to `https://news.ycombinator.com/item?id=`.  

## Recent Findings (10‑day aggregate, 2026‑04‑23 to 2026‑05‑02)
- Displays total mentions and aggregated user sentiment for each model.  
- Visualized with scale bars normalized to 100 %.  
- The “Top 10 Model Popularity” list ranks models based on combined mention count and sentiment score (full details available in the Google Sheet).  

## Access Links
- Google Sheets link provides granular results and underlying data.  
- Additional navigation links: Home and a reference to “LingoLingo – Learn languages with YouTube!” (unrelated to the analysis).