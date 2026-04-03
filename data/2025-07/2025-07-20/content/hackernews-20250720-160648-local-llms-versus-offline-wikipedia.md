---
title: Local LLMs versus offline Wikipedia
url: https://evanhahn.com/local-llms-versus-offline-wikipedia/
site_name: hackernews
fetched_at: '2025-07-20T16:06:48.704607'
original_url: https://evanhahn.com/local-llms-versus-offline-wikipedia/
author: EvanHahn
date: '2025-07-20'
published_date: '2025-07-19T00:00:00+00:00'
description: How do the sizes of local LLMs compare to the size of offline Wikipedia downloads?
---

# Local LLMs versus offline Wikipedia

by
Evan Hahn
,
posted

Jul 19, 2025

Two days ago, MIT Technology review published“How to run an LLM on your laptop”. It opens with an anecdote about using offline LLMs in an apocalypse scenario. “‘It’s like having a weird, condensed, faulty version of Wikipedia, so I can help reboot society with the help of my little USB stick,’ [Simon Willison] says.”

This made me wonder: how do the sizes of local LLMs compare to the size of offline Wikipedia downloads?

I compared some models from theOllama libraryto various downloads onKiwix. I chose models that could be run on some consumer-grade hardware, and Wikipedia bundles that didn’t have images for a better comparison. Here’s what I found, ordered by size:

Name
Download size
Best of Wikipedia (best 50K articles, no details)
356.9MB
Simple English Wikipedia (no details)
417.5MB
Qwen 3 0.6B
523MB
Simple English Wikipedia
915.1MB
Deepseek-R1 1.5B
1.1GB
Llama 3.2 1B
1.3GB
Qwen 3 1.7B
1.4GB
Best of Wikipedia (best 50K articles)
1.93GB
Llama 3.2 3B
2.0GB
Qwen 3 4B
2.6GB
Deepseek-R1 8B
5.2GB
Qwen 3 8B
5.2GB
Gemma3n e2B
5.6GB
Gemma3n e4B
7.5GB
Deepseek-R1 14B
9GB
Qwen 3 14B
9.3GB
Wikipedia (no details)
13.82GB
Mistral Small 3.2 24B
15GB
Qwen 3 30B
19GB
Deepseek-R1 32B
20GB
Qwen 3 32B
20GB
Wikipedia: top 1 million articles
48.64GB
Wikipedia
57.18GB

This comparison has many caveats:

* This is an apples-to-oranges comparison. Encyclopedias and LLMs have different purposes, strengths, and weaknesses. They are fundamentally different technologies!
* File size is not the only important detail. LLMs, even local ones, can use lots of memory and processor power. Offline Wikipedia will work better on my ancient, low-power laptop.
* Other entries might be more useful for a specific purpose. For example, you can download a selection of Wikipedia articles about chemistry, or an LLM that’s better tuned for your hardware. (And Kiwix has lots of other things you can download, like all of Stack Overflow.)
* I picked these entries based on vibes. Nothing rigorous about this comparison!

Despite those caveats, I thought it was interesting that Wikipedia’s best 50,000 articles are, very roughly, equivalent to Llama 3.2 3B. Or that Wikipedia can be smaller than the smallest LLM, and larger than the largest ones—at least in an offline scenario on consumer hardware.

Maybe I’ll download both, just in case.
