---
title: What is an "agentic harness," actually? - DEV Community
url: https://dev.to/googleai/what-is-an-agentic-harness-actually-4oie
site_name: devto
content_file: devto-what-is-an-agentic-harness-actually-dev-community
fetched_at: '2026-07-17T11:31:52.328201'
original_url: https://dev.to/googleai/what-is-an-agentic-harness-actually-4oie
author: Tilde A. Thurium
date: '2026-07-16'
description: I've been hearing the word "harness" thrown around a lot lately. I assumed it just meant "the IDE" or... Tagged with ai, agents, discuss, llm.
tags: '#discuss, #ai, #agents, #llm'
---

I've been hearing the word "harness" thrown around a lot lately. I assumed it just meant"the IDE"or"whatever app is running your agent."Turns out, it goes a little deeper than that.

So I sat down with@greggyband asked him to explain it from the ground up: what an LLM actually does, what turns it into an agent, and where the harness fits into all of it.

## What's in the video

* Simon Willison's definition of an agent: an LLM with tools, running in a loop to accomplish a goal
* What "tools" really means under the hood, and how function calling lets an LLM pull in context it wasn't trained on
* The loop part: how an agent programmatically checks its own output to decide if it's actually done
* Why the harness is everythingafterthe LLM, and why that's a different thing than the interface
* Why you can swap interfaces without touching the underlying harness, and why some agents don't need a UI at all

The point that stuck with me is the harness isn't the app you're looking at. It's the invisible plumbing deciding whether the agent keeps going or calls it done.

Did your mental model of "harness" match up? Or were you picturing something else too?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse