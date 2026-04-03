---
title: A first guide to building APIs with AI | Nate Meyvis
url: https://www.natemeyvis.com/a-first-guide-to-building-apis-with-ai/
site_name: tldr
content_file: tldr-a-first-guide-to-building-apis-with-ai-nate-meyvis
fetched_at: '2026-03-03T06:01:04.274749'
original_url: https://www.natemeyvis.com/a-first-guide-to-building-apis-with-ai/
date: '2026-03-03'
description: Simon Willison's Agentic Engineering Patterns project makes me want to compile notes on building APIs in a AI-first world. (I'm writing as someone who has...
tags:
- tldr
---

# A first guide to building APIs with AI

27 Feb, 2026

Simon Willison'sAgentic Engineering Patternsproject makes me want to compile notes on building APIs in a AI-first world.

(I'm writing as someone who has maintained many APIs and whois optimistic aboutbuilding usable APIs quickly with AI. I have only basic working-professional knowledge of building APIs at scale, ofsecuringAPIs, and related subjects.)

1. Most importantly:build the API, or at least consider it. It's a bitlikemigrationsin that it's plenty of work, but work that AI is good at. Andit gets easier every time.
2. Expose the documentation for the API programmatically: the easier it is for AI to find the documentation, the better. Telling the AI to call/api/helpis in general better than putting all that information into another document, where it threatens to clutter a context window when it's not helping.
3. Relatedly, don't clutter up the documentation. Humans often need more examples than AI does, and human-facing API documentation often includes identical text in the descriptions of many endpoints. Do document the API completely, but remember that AI consumers pay a cost for everything you put there.
4. Consider building a non-destructive API intended for safe AI usage. Note that "safe AI usage" can include writes: these writes can be "candidates," to be reviewed by a human (or another AI!) before they're committed. (I mean "committed" in a general sense; it'll be different by domain. For the recipe site, it just means "added to your recipe collection.")
5. Your AI tools know a lot about rate limiting, monitoring, alarming, and so on. In my experience, however, they're very fallback-happy, which can beterriblein this context. Do review this code carefully. Check explicitly for fallbacks that disguise bugs or introduce security holes. (Prompting the same or a different AI to comb through the code for bad fallbacks is well worth doing.1)

1. Perhaps by the time you read this, AI tools will be better about distinguishing good and bad defensive code. As I write this, they are far too eager to implement fallbacks in a wide variety of situations. (But that's another post.)↩

#APIs#Simon Willison#generative AI#software