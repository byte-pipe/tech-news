---
title: Auto-grading decade-old Hacker News discussions with hindsight | karpathy
url: https://karpathy.bearblog.dev/auto-grade-hn/
date: 2025-12-11
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-11T11:11:14.996288
screenshot: hackernews-auto-grading-decade-old-hacker-news-discussions-wi.png
---

# Auto-grading decade-old Hacker News discussions with hindsight | karpathy

## Auto-grading decade-old Hacker News discussions with hindsight

### Key Points
- The author stumbled upon an HN thread about the future of the front page five years ago
- They decided to replicate this exercise using LLMs and the newly released Opus 4.5
- The goal is to analyze what happened in retrospect, even better than manually doing it
- This involves downloading 30 articles each from December 31st, 2015 to December 2019, parsing comments and extracting relevant data

### Structure
* Download front pages for 30 articles each from December 2015 to December 2019 using the Algolia API
* Extract detailed information about the discussion threads using natural language processing (NLP)
* Analyze what happened in retrospect with hindsight, considering possible future scenarios and potential errors
* Package insights into a markdown prompt

### Code Explanation
The code is implemented using Open Source Technologies like Opus 4.5, Algolia API and GitHub repository: `karpathy/hn-time-capsule`. Here it explains:

1. **Initial Steps**: Given a date (in this case December), the script downloads the front page of 30 articles.
2. **Article Parsing**: For each article, extract article contents using Algolia API
3. **Comment Analysis**: Download and parse full comment threads for all relevant articles

### Advantages for LLMs

- It can better handle large amounts of data and time complexities due to scalability and memory efficiency
- Potential improvements in understanding human behavior and knowledge retrieval
