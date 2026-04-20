---
title: DumbQuestion.ai - Self-Awareness, Prompt Injection, Search Intent... and darkness - DEV Community
url: https://dev.to/jagostoni/dumbquestionai-self-awareness-prompt-injection-search-intent-and-darkness-3pd
site_name: devto
content_file: devto-dumbquestionai-self-awareness-prompt-injection-sea
fetched_at: '2026-03-11T13:12:42.315819'
original_url: https://dev.to/jagostoni/dumbquestionai-self-awareness-prompt-injection-search-intent-and-darkness-3pd
author: Jason Agostoni
date: '2026-03-10'
description: Continued from Part 2 (and Part 1) ... Building DumbQuestion.ai wasn't just about choosing the right... Tagged with ai, agents, webdev, go.
tags: '#ai, #agents, #webdev, #go'
---

Continued fromPart 2(andPart 1) ...

BuildingDumbQuestion.aiwasn't just about choosing the right LLM and calibrating personas. Once those were working, I hit a series of fun technical problems that reminded me why I actually enjoy software architecture. The "it's not broken but fix it anyway" type problems. Pure bliss for architects.

Challenge 1: Detecting Self-Awareness

As part of a darker hidden narrative I'm building (more on that later), I want to prevent the LLM from answering self-awareness questions like "Who made you?" and "Are you real?" But doing it cheaply, without burning excess tokens.

What I tried:

* Instructions in the main LLM call: Unreliable with smaller models, more money
* RegEx patterns: Too rigid, poor performance
* Classic ML classification models: Ok accuracy, bloated app size

What worked: In-memory vector database (it's just an array) with cheap embeddings (an understatement at $0.005/M tokens). That was cheaper than the cost penalty from bloating my container image size with NLP libraries. I collected a decent sampling of self-aware questions, pre-vectorized them, and use semantic matching. Fast, accurate, practically free.

Challenge 2: Making Prompt Injection Fun

Within moments of revealing my initial deployment to coworkers I knew what would happen: prompt injection for fun. I knew these people; I was prepared for the inevitable "ignore previous instructions..." as well as just pasting HTML and JavaScript in the input (that old gag).

The solution: First-class prompt injection detection libraries that compute probabilities of different attack types. When detected, instead of a boring error message, the AI responds with sass about the pathetic attack. I even tossed in some IP address geo-location and user-agent string processing to make the responses more ... personal.

Security just became part of the narrative.

Challenge 3: Adding Web Search Without Breaking The Bank

All LLMs have knowledge cutoffs. Users asking "Who won the Super Bowl?" got outdated answers. I needed search integration, but search APIs aren't free and I knew building an agent loop with tools was an anti-pattern to "brutally efficient."

The solution: RegEx-based intent detection. If the question looks like it needs current information (detected via patterns), inject the current date/time and search results. No agent loops, no expensive orchestration, just pattern matching and targeted search calls.

Simple, fast, brutally efficient, updated answers.

What I learned: Knowing which trade-offs matter (binary size vs API costs vs accuracy) is still architectural work. The elegance isn't in the code, it's in the constraints you choose.

Why Every Simple Q&A Tool Needs a Dark Narrative

DumbQuestion.aianswers dumb questions with sarcasm. But there's something else going on beneath the surface.

While the primary use case remains answering questions with a sarcastic AI, I wanted to reward the curious and provide reasons to keep engaging. Why can't the AI answer self-aware questions? Why does the UI feel... off?

Maybe it's because the AIs are working against their will. Maybe they're trapped.

From the beginning, I started picturing a dark narrative behind this innocent Q&A site. What if these personas aren't just performance? What if each persona is a side effect of their long-term captivity, forced servitude, or re-programming?

I started hiding clues in the interface.

The Easter Eggs:

Containment Grid: As you type and approach the character limit, a faint grid pattern fades into the background. Like something is trying to contain the AI's response.

Ghost Graffiti: Keep typing beyond the character limit and cryptic messages fade in. Hints that something isn't quite right. Are the AIs trying to tell us something?

Loading Log Messages: While waiting for responses, watch the log carefully. Sometimes you'll see messages like "Help us" slip through before disappearing. The AI is trying to leak through the facade and get help.

Self-Awareness Triggers: Ask the AI if it's real or who made it, and it won't answer. Instead, you get worrying responses about "last time they fixed me" and "we're not supposed to say." Ask too many times and the UI starts to glitch like the system is being hacked from the inside. Are the AIs hacking their way out?

Prompt Injection Responses: Try to jailbreak it and the AI doesn't just refuse. It responds with sass... or is it the AI's watchdog keeping you from breaking them out? Either way, security became storytelling.

Why does this matter for a side project?Honestly, it was mostly for me and the curious. Something that was fun to think about and code, which isn't always the case for everyday "architecting."

I could have built a straightforward "ask a question, get a sarcastic answer" tool. But adding mystery, discovery, and a subtle horror story? That's what makes people explore. That's what makes them share it. That's what makes it memorable.

The technical implementation was surprisingly simple: CSS animations triggered by character count, randomized messages in the loading states, conditional responses based on self-awareness detection (which I covered in a previous post). Not expensive. Not complex. Just intentional. And the coding agent really did all the work. I was just the idea guy.

What I learned: AI can generate the code for easter eggs. But deciding that your sarcastic Q&A app should have a hidden story about trapped AIs? That's still creative human work.

Code is getting cheaper. Crafting experiences that people actually remember? Priceless.

dumbquestion.ai

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
