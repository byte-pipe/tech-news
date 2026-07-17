---
title: $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol · TryAI
url: https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6
date: 2026-07-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-17T11:33:05.292706
---

# $100 AI Music Video: Claude Fable 5 vs. GPT-5.6 Sol · TryAI

**Overview of the Music Video Generation Process**

The article describes a small agnostic harness built to generate music videos using machine learning models. The process involves providing the model with:

* A song
* A hard dollar budget ($25 or $100)
* A set of tools (plan, web_search, get_budget, generate_image, and run_command)

The model then researches, generates, and edits the video.

**Setup and Four Different Runs**

Each model runs an autonomous tool-calling loop with six tools using open-source software. The four models differ in their approach:

* Claude Fable 5 and GPT-5.6 Sol ran two $25 budgets.
* Both models ran five runs total.
* Each run includes a song, description, and lyric transcript.

**Results**

The article provides the time-to-finished video for each model, with the cost of generated footage included:

* Claude Fable 5 · $25
Claude Fable 5: $24.30 (39m10s)
* GPT-5.6 Sol · $25
GPT-5.6 Sol: $23.18 (42m52s)
* GPT-5.6 Sol · $100
GPT-5.6 Sol: $36.57 (49m39s)

**Variations and Insights**

The article highlights the difference between models running on limited budgets ($25) versus unlimited budgets ($100). The results show that using more budget leads to:

* Longer video lengths

Additionally, the article notes that tools like image-to-video pipeline were used, but most importantly, they didn't affect the outcome. This indicates that other aspects of the model are more critical in determining the final output.

**Open-Source and Accessible**

The code is open-source on GitHub at `github.com/hershalb/music-video-arena`, making it possible for users to clone and test the setup independently of commercial tools.