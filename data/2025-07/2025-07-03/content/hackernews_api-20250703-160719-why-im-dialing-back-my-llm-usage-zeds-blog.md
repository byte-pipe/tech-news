---
title: Why I'm Dialing Back My LLM Usage — Zed's Blog
url: https://zed.dev/blog/dialing-back-my-llm-usage-with-alberto-fortin
site_name: hackernews_api
fetched_at: '2025-07-03T16:07:19.381523'
original_url: https://zed.dev/blog/dialing-back-my-llm-usage-with-alberto-fortin
author: sagacity
date: '2025-07-02'
published_date: 07/01/2025
description: 'From the Zed Blog: Alberto Fortin shares his honest reflection on the reality of using LLMs in production code and why he''s taking a more measured approach.'
tags:
- hackernews
- trending
---

← Back to Blog

# Why I'm Dialing Back My LLM Usage

Alberto Fortin

From theAgentic Engineering Sessions

|

Aired onJuly 1st, 2025

We invitedAlberto Fortin, a seasoned software engineer with 15 years of experience, to share his candid journey with AI. Alberto initially embraced LLMs with genuine enthusiasm, hoping they would revolutionize his development workflow. However, after encountering significant challenges while rebuilding his infrastructure with Go and ClickHouse, he wrote athoughtful blog postreflecting on the gap between AI hype and reality.
For this conversation, Alberto also prepared adetailed follow-up analysistesting newer models like Claude Opus 4, examining whether recent improvements have addressed the core issues he encountered.

His experience provides practical lessons for engineers evaluating LLMs in production environments—balancing realistic expectations with an understanding of where these tools genuinely add value versus where they still fall short.

You canwatch the session on YouTubeor read below for some selected quotes.

## The Reality Check: When AI Hype Meets Production Code

"I was really shocked at the poor quality of some things, and it was not just about bugs and features not working. I think as a developer who wants to maintain this codebase for the next few years, I also care about it being neat enough."

"I feel like I'm a week away from fixing this, but actually a new small error would come up and then that will take another two weeks to fix."

"I will give my error output to the LLM and then it will spit out something new that will kind of fix it, but also make things a bit more messed up—and break something else in the process."

## The Productivity Illusion

"I think everyone just got a little bit overexcited about it because the first iteration, the first little feature, the first autocomplete is like, 'Oh my God, this is amazing. This is like reading my mind.' So you kind of get duped into it a little bit."

"I think we've gotten to a level where we can do probably 10 times as much coding. So we kind of expect that to happen and we require that from the LLMs, but I think everyone just gets a little bit overexcited about it."

## Taking Control: The Mental Shift

"I think this is the biggest difference, like a mental shift... I am the software engineer, the senior software engineer, I am the architect. The LLM is the assistant. The assistant responds to me; I make the plan."

"I lost all my trust in LLMs, so I wouldn't give them a big feature again. I'll do very small things like refactoring or a very small-scoped feature."

"I started fixing the bugs myself. Because as soon as you understand this—you have a hundred percent understanding of your codebase and what everything is doing—it's so much easier and quicker for you to go in and fix something."

## Practical Wisdom

"If you are confident enough in your skills—you know, a senior developer—and this is not working for you, there's nothing wrong with you. Just try to do the things that you always did and use AI to leverage your knowledge a little bit."

"We've gone up a level, it's great. But also, let's be mindful we're not there yet at the next level... We are offloading some of the programming work, but we still need to do architectural abstractions and make the decisions for the product."

"Let's just try to calm down all this hype and find a balanced approach towards AI. Use it, because I think it's such an amazing revolution in technology, but we're not there yet."
