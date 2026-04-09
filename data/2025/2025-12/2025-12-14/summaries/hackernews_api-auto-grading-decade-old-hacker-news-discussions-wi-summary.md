---
title: Auto-grading decade-old Hacker News discussions with hindsight | karpathy
url: https://karpathy.bearblog.dev/auto-grade-hn/
date: 2025-12-10
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-14T11:10:53.120700
screenshot: hackernews_api-auto-grading-decade-old-hacker-news-discussions-wi.png
---

# Auto-grading decade-old Hacker News discussions with hindsight | karpathy

## Auto-grading decade-old Hacker News discussions with hindsight

- **Decade-old Hackathon:** Decades ago (10 years) there was a hackathon on 1 Nov '15  by [Bjartr]: https://karpathy.ai/hncapsule/, where Gemini Pro hallucinated the frontpage of hacker news
- **Manual Grading Task:**
  - Tasked to manually analyze each comment in discussions around the article.
  - Realized it could be more accurate and complete if using Large Language Models (LLMs)
- **Training a LLM for Predictive Tasks:**
  - Decided to train a large language model (LLM), like ChatGPT 5.1, on data from hacker news discussions from 10 years ago (December 31, 2025)
  - Created a framework that allows the user to submit a date in advance and receive an analysis of what happened when they were last watching hacker news and receiving similar insights
- **LLM Workflow:**
  - Download and parse data for one day's front page articles and discussion threads from Hacker News
  - Ask LLM to analyze the selected article and related comments
  - Assemble results into a markdown document summarizing what happened ten years ago
