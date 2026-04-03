---
title: Two things LLM coding agents are still bad at | ʕ☞ᴥ ☜ʔ Kix Panganiban's blog
url: https://kix.dev/two-things-llm-coding-agents-are-still-bad-at/
site_name: hackernews_api
fetched_at: '2025-10-09T19:07:11.782793'
original_url: https://kix.dev/two-things-llm-coding-agents-are-still-bad-at/
author: kixpanganiban
date: '2025-10-09'
description: I’ve been trying to slowly ease into using LLMs for coding help again lately (after quitting ), but something always feels off -- like we’re not quite on the...
tags:
- hackernews
- trending
---

# Two things LLM coding agents are still bad at

09 Oct, 2025

I’ve been trying to slowly ease into using LLMs for coding help again lately (after quittingcold turkey), but something always feels off -- like we’re not quite on the same wavelength. Call it vibe coding orvibe engineering, but I think I’ve finally pinned down two big reasons why their approach to code feels so awkward.

1. LLMs don’t copy-paste (or cut and paste) code. For instance, when you ask them to refactor a big file into smaller ones, they’ll "remember" a block or slice of code, use adeletetool on the old file, and then awritetool to spit out the extracted code from memory. There are no realcutorpastetools. Every tweak is just them emittingwritecommands from memory. This feels weird because, as humans, we lean on copy-paste all the time. It’s how we know the code we moved is exactly the same as where we copied it from. I've only seen Codex go against the grain here, sometimes I'd see it issuesedandawkto try and replicate that copy-paste interaction, but it doesn't always work.
2. And it’s not just how they handle code movement -- their whole approach to problem-solving feels alien too. LLMs are terrible at asking questions. They just make a bunch of assumptions and brute-force something based on those guesses. Good human developers always pause to ask before making big changes or when they’re unsure (hence the mantra of"there are no bad questions"). But LLMs? They keep trying to make it work until they hit a wall -- and then they just keep banging their head against it. Sure, you can overengineer your prompt to try get them to ask more questions (Roo for example, does a decent job at this) -- but it's very likely they still won't. Maybe the companies building these LLMs do their RL based on making writing code "faster".

These quirks are why I contest the idea that LLMs are replacing human devs -- they’re still more like weird, overconfident interns. I can’t fully vibe with them yet.

#ai#coding#musings

99
