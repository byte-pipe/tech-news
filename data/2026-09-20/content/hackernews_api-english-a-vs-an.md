---
title: 'English: a vs an'
url: https://www.redblobgames.com/blog/2026-09-16-english-a-vs-an/
site_name: hackernews_api
content_file: hackernews_api-english-a-vs-an
fetched_at: '2026-09-20T14:30:43.997556'
original_url: https://www.redblobgames.com/blog/2026-09-16-english-a-vs-an/
author: azhenley
date: '2026-09-19'
description: 'English: A vs. An'
tags:
- hackernews
- trending
---

Blog post:
 16 Sep 2026

{Note: this is a short blog post introducing theactual project page}

In English, there is an “indefinite” articleathat can go before a word. For example,a raccoon. But for some words, we usean. For example,an apple.

When procedurally generating text, I want a functiona_or_an("apple")that tells me which article to use. That seems
like it’d be easy. We can check the first letter to see if it’s a
vowel. But that would mean we outputan unicorn, nota unicorn.

Visualization showing whether the first two letters of a word are enough to determine whether it should have “a” or “an”. It is not.

The actual rule is not whether thewrittenword starts with a
vowel letter, but whether thespokenword starts with a vowel
sound. The word<unicorn>starts with a vowel letter (<u>) but a
consonant sound (cmudictY, ipa/j/), so it getsa. The word<hour>starts with a consonant letter (<h>) but a vowel sound (cmudictAW, ipa/aʊ/), so it getsan.

I was curious how often these exceptions occurred, and whether they can be grouped together, soI spent a day looking at the data and building some visualizations and wrote up the results.I was surprised that only 129 of the 32,455 words in my list needed exceptions.

[LLM note: I didnotuse LLMs to write any of this code, but in hindsight, I should have. This is one-off code to answer a question. It doesn’t need to be clean or maintainable. It only needs to be correct. If I had used the LLM to parse cmudict and make the d3.js visualizations, I could’ve spent more of my time coding a better trie analysis algorithm.]