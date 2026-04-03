---
title: How I learned to “use AI” in 3 baby steps - DEV Community
url: https://dev.to/miffens/how-i-learned-to-use-ai-in-3-baby-steps-2216
site_name: devto
fetched_at: '2025-11-12T11:07:14.037011'
original_url: https://dev.to/miffens/how-i-learned-to-use-ai-in-3-baby-steps-2216
author: miffens
date: '2025-11-11'
description: In recent conversations, I've heard a lot of anxiety about "AI fluency." Between companies pushing... Tagged with ai, beginners, tutorial, chatgpt.
tags: '#ai, #beginners, #tutorial, #chatgpt'
---

In recent conversations, I've heard a lot of anxiety about "AI fluency." Between companies pushing adoption and jobseekers getting interviewed on how they "use AI," coders worry they're falling behind. On the other hand, they’re also uncomfortable drastically changing what works well for them.

If you feel you need to "use AI" but aren't sure how, here’s what I did to go from "intimidated" to "fluent" without getting disrupted.

### Step 1: Make it exist in your IDE

Set up Cursor or Copilot and... do nothing special. Ignore the chat for now, only let it suggest completions and docstrings as you type. Sometimes it seems psychic, other times it'll phrase comments more eloquently than you could, and often it's nonsense. Continue going about your usual workflow while occasionally accepting its suggestions.

Congrats! You've taken your first steps towards "AI fluency." At this point, it's really a smarter autocomplete and shouldn't overhaul your existing workflow. I stayed in this stage for about a month.

### Step 2: Try inline editing

You know those tiny snags: awkward syntax, a type error, a small refactor where your intent is too nuanced to find a direct Stack Overflow answer for? Hovering over the red squiggly line or highlighting some lines should make a "quick edit"/ "fix with AI" option appear. Give it a go! Accept if it fixes it and otherwise undo. If you're up for it, edit the default prompt to add context or specific instructions to up your chances at a good edit.

From the Cursorinline edit docs. Yes 'unused' is misspelled, maybe to show that LLM's are forgiving of them?😀

### Step 3: Use the chat agent

When I posted codebase questions on Slack, coworkers would reply, "here's what I know, but have you also tried asking Cursor? It's pretty good at answering your type of question." That was my sign from the universe to try the chat agent for bigger stuck moments and legacy spelunking. As I interacted with it, I started to build an intuition for what it does and doesn't do well.

What I ask most:

* Fixing - "My code isn't working. I expect X but it's doing Y. Here's the error log."
* Explanations - "Help me understand how function X affects rendering. Walk me through concrete examples."

I write to it like a coworker who is helping me, providing all the context on what the problem is and what I've tried so far.

Nonsensical rambles could happen, but often, it will point to the right neighborhood even if it doesn't hand me the final fix. Once in a while, it nails it. I review its edits as if a coworker edited my branch, with about 20% extra caution.

Switching from 'Auto' to the best model and the largest context window my company provides, GPT-5 MAX, led to slower but much better answers. Getting helpful answers more often motivated me to keep experimenting with it.

For a structured course on chat agent skills, I genuinely recommend the freeAnthropic AI fluency course(1-2 hours) which emphasizes how to collaborate effectively and ethically with LLM's:

* Delegation: Thoughtfully deciding what work to do with AI vs. doing yourself
* Description: Communicating clearly with AI systems
* Discernment: Evaluating AI outputs and behavior with a critical eye
* Diligence: Ensuring you interact with AI responsibly

## Conclusion

Now that you have a sense of when to leverage autocompletes, quick edits, and the chat agent, you know how to "use AI" at work. Congrats! With these fundamentals, you should have the confidence to lean further into more advanced usages if you're so inclined.

The learning curve is non-zero, but your Stack Overflow, pair programming, and code tracing strategies both transfer directly and mix-and-match with your new skill. Baby steps will get you there. You got this!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
