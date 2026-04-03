---
title: Anthropic tries to hide Claude's AI actions. Devs hate it • The Register
url: https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/
site_name: hackernews_api
content_file: hackernews_api-anthropic-tries-to-hide-claudes-ai-actions-devs-ha
fetched_at: '2026-02-17T06:00:16.601569'
original_url: https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/
author: beardyw
date: '2026-02-16'
description: Anthropic tries to hide Claude's AI actions. Devs hate it
tags:
- hackernews
- trending
---

#### Devops

# Anthropic tries to hide Claude's AI actions. Devs hate it



## The software doesn't show what files it's working on

Anthropic has updated Claude Code, its AI coding tool, changing the progress output to hide the names of files the tool was reading, writing, or editing. However, developers have pushed back, stating that they need to see which files are accessed.

Version 2.1.20 collapsed the output so that instead of showing, for example, the file names and how many lines were read, it would just print "Read 3 files (ctrl+o to expand)," according to apostcomplaining that "Claude Code is being dumbed down." The full details can still be accessed with the keyboard shortcut, but constantly invoking this is annoying and impractical.

Developers have many reasons for wanting to see the file names, such as for security, for knowing immediately if Claude is pulling context from the wrong files, and for easy audit of past activity by scrolling through conversation. "When I'm working on a complex codebase, knowing what context Claude is pulling helps me catch mistakes early and steer the conversation," one person wrote.

There's also a financial impact. If developers spot that Claude is going down a wrong track, they can interrupt and avoid wasting tokens.

AGitHub issueon the subject drew aresponsefrom Boris Cherny, creator and head of Claude Code at Anthropic, that "this isn't a vibe coding feature, it's a way to simplify the UI so you can focus on what matters, diffs and bash/mcp outputs." He suggested that developers "try it out for a few days" and said that Anthropic's own developers "appreciated the reduced noise."

Cherny said that developers who wanted more detail could enable verbose mode. Responses were lackluster, with one person writing: "Verbose mode is not a viable alternative, there's way too much noise."

Another observation was that the new default output, such as "searched for 2 patterns, read 3 files," conveys no useful information. "It's not a nice simplification, it's an idiotic removal of valuable information,"saida user.

Cherny responded to the feedback by making changes. "We have repurposed the existing verbose mode setting for this," hesaid, so that it "shows file paths for read/searches. Does not show full thinking, hook output, or subagent output (coming in tomorrow's release)."

The problem with this is that making verbose mode less verbose is a bad change for those who wanted the full details.

Cherny also participated in a lengthydiscussionon Hacker News. "Claude has gotten more intelligent, it runs for longer periods of time, and it is able to more agentically use more tools... The amount of output this generates can quickly become overwhelming in a terminal, and is something we hear often from users," he said.

* Investors shove another $30B into the Anthropic money furnace
* OK, so Anthropic's AI built a C compiler. That don't impress me much
* Cloudflare turns websites into faster food for AI agents
* 30+ Chrome extensions disguised as AI chatbots steal users' API keys, emails, other sensitive data

Those users who want the collapsed output seem to be mostly absent from the discussion. "I can't tell you how many times I benefited from seeing the files Claude was reading, to understand how I could interrupt and give it a little more context... saving thousands of tokens,"saidone response.

Cherny said that the repurposed verbose mode was the solution, and that Claude Code will still default to the condensed view.

The debate is important because if AI tools like Claude Code hide what they are doing from developers (or other users), mistakes are more likely to slip through. "I'm a Claude user who has been burned lately by how opaque the system has become,"saidanother developer. "Right now Claude cannot be trusted to get things right without constant oversight and frequent correction, often for just a single step. For people like me, this is make or break. If I cannot follow the reasoning, read the intent, or catch logic disconnects early, the session just burns through my token quota."

Claude Code changes frequently, so it is likely that this aspect will be further tweaked, but there is not yet any indication that it will revert to the old behavior. ®



Get our

Tech Resources

Share

#### More about

* AI
* Anthropic
* Development

More like these

×

### More about

* AI
* Anthropic
* Development

### Narrower topics

* Accessibility
* AIOps
* Claude
* DeepSeek
* Devops
* Gemini
* Google AI
* GPT-3
* GPT-4
* Machine Learning
* MCubed
* Neural Networks
* NLP
* Retrieval Augmented Generation
* Star Wars
* Tensor Processing Unit
* TOPS

### Broader topics

* Large Language Model
* Self-driving Car

#### More about

Share

#### More about

* AI
* Anthropic
* Development

More like these

×

### More about

* AI
* Anthropic
* Development

### Narrower topics

* Accessibility
* AIOps
* Claude
* DeepSeek
* Devops
* Gemini
* Google AI
* GPT-3
* GPT-4
* Machine Learning
* MCubed
* Neural Networks
* NLP
* Retrieval Augmented Generation
* Star Wars
* Tensor Processing Unit
* TOPS

### Broader topics

* Large Language Model
* Self-driving Car

#### TIP US OFF

Send us news
