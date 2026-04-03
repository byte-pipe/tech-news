---
title: Augmented Intelligence (AI) Coding using Markdown Driven-Development - DEV Community
url: https://dev.to/simbo1905/augmented-intelligence-ai-coding-using-markdown-driven-development-pg5
site_name: devto
fetched_at: '2025-09-30T11:08:58.336073'
original_url: https://dev.to/simbo1905/augmented-intelligence-ai-coding-using-markdown-driven-development-pg5
author: Simon Massey
date: '2025-09-28'
description: 'TL;DR: Deep research the feature, write the documentation first, go YOLO, work backwards... Then... Tagged with llm, ai, softwaredevelopment, coding.'
tags: '#llm, #ai, #softwaredevelopment, #coding'
---

TL;DR: Deep research the feature, write the documentation first, go YOLO, work backwards... Then magic. ✩₊˚.⋆☾⋆⁺₊✧

In mylast post, I outlined how I was using Readme-Driven Development with LLMs. In this post, I will describe how I implemented a 50-page RFC over the course of a single weekend.

My steps are:

Step 1: Design the feature documentation with an online thinking modelStep 2: Export a description-only "coding prompt"Step 3: Paste to an Agent in YOLO mode (--dangerously-skip-permissions)Step 4: Force the Agent to "Work Backwards"

## Step 1: Design the feature documentation with an online thinking model

Open a new chat with an LLM that can search the web or do "deep research". Discuss what the feature should achieve. Do not let the online LLM write code. Create the user documentation for the feature you will write (e.g., README.md or a blog page). I start with an open-ended question to research the feature. That will prime the model. Your exit criteria is that you like the documentation or promotional material enough to want to write the code.

To exit this step, have it create a "documentation artefact" in markdown (e.g. the README.md or blog post). Save that to disk so that you can point the coding agent at it.

If you don't want to pay for a subscription for an expensive model, you can install Dive AI Desktop and use pay-as-you-go models of much better value. Here is a video on setting up Dive AI to do web research with Mistral:

## Step 2: Export a description-only "coding prompt"

Next, tell the online model to "create a description only coding prompt (do not write the code!)". Do not accept the first answer. The more effort you put into perfectingboththe markdown feature documentationandthe coding prompt, the better.

If the coding prompt is too long, then the artefact is too big! Start a fresh chat and create something smaller. This is Augmented Intelligence ticket grooming in action!

## Step 3: Paste to an Agent in YOLO mode (--dangerously-skip-permissions)

Now paste in the groomed coding prompt and the documentation, and let it run. I always use a git branch so that I can let the agent go flat out. Cursor background agents, Copilot agents, OpenHands, Codex, Claude Code are becoming more accurate with each update.

I only restrictgit commitandgit push. I ask it first to make a GitHub issue using theghcli and tell it to make a branch and PR.

## Step 4: Force the Agent to "Work Backwards"

The models love to dive into code, break it all, get distracted, forget to update the documentation, hit compaction, and leave you with a mess. Do not let them be a caffeine-fuelled flying squirrel!

The primary tool I am using now prints out a Todos list. This is usually the opposite of the correct way to do things safely!

Here is an edited version of a real Todo list to fix a bug with JDT "Match Any{}"

⏺ Update Todos
 ⎿ ☐ Remove all compatibility mode handling
 ☐ Make `{}` always compile as strict
 ☐ Update Test_X to expect failures for `{}`
 ☐ Add regression test Test_Y
 ☐ Add INFO log warning when `{}` is compiled
 ☐ Update README.md with Empty Schema Semantics section
 ☐ Update AGENTS.md with guidance

Enter fullscreen mode

Exit fullscreen mode

That list is in a perilous order. Logically, it is this:

1. Delete logic - so broken code, invalid old tests!
2. Change logic - so more broken code, more invalid old tests!
3. Change old tests - focusing on the old, not the new!
4. Add one test - finally working on the new feature!
5. Change the README.md and AGENTS.md - invalid docs used in steps 1-4!

If the agent context compacts, things go sideways, you get distracted, and you will end up with a bag of broken code.

So I set it to "plan mode", else immediately interrupt it, and force it to reorder the Todo list:

1. Change the README.md and AGENTS.mdfirst
2. Add one test (insist the test is not runyet!)
3. Change one test (insist the test is not runyet!)
4. Add/Change logic (cross-check the plan with a different model!)
5. Now run the tests
6. Delete things last

That is a safe order where things are far less likely to be blown off course. I used to struggle with any feature that went beyond a single compaction; that is now far less of an issue.

## Todos Are All You Need?

I am not actually a big fan of the built-inTodoslist of the two big AI labs. The models really struggle with any changes to the plan. The Kimi K2 Turbo appears to be more capable of pivoting. I have a few tricks for that, but I will save them for another post.

## Does This Work ForRealCode?

This past weekend, I decided to write an RFC 8927 JSON Type Definition validator based on the experiemental JDKjava.util.jsonparser. The PDF of the spec is 51 pages. There is a ~4000-line compatibility test suite.

We wrote 509 unit tests. We have the full compatibility test suite running. Yet we had bugs. We found them as we wrote a jqwik property test that generates 1000 random JTDs, and the corresponding JSON to validate, which uncovered several bugs. Codex also automatically reviewed the PRs and flagged some very subtle issues, which turned out to be real bugs. It took about a dozen PRs over the weekend to get the job done properly to a professional level.

## End Notes

Using a single model family is a Bad Idea (tm). For online research, I alternate between full-fat ChatGPT Desktop, Claude Desktop, and Dive Desktop to utilise each of GPT5-High, Opus 4.1, or Kimi K2 Turbo.

For Agents, I have used all the models and many services. Microsoft kindly allows me to use full-fat Copilot with Agents for open-source projects for free ❤️ I have a cursor sub to use their background agents. I use Codex, Claude Code, and Gemini CLI locally. I use Codex in Codespaces. There are also background agents for Cursor, Codex, and OpenHands, among others. The actual model seems less important than writing the documentation first and writing tight prompts.

I am currently using an open-weight model at $3 per million tokens for the heavy lifting, which is pay-as-you-go. However, I will cross-check its plans with GPT5 and Sonnet 4.

Whenever things get complicated, I always ask a model from a different family to review every change on every bug hunt. That has reduced rework to almost zero. 💫

If you are a veteran, you may enjoy the YT channel Vibe Coding With Steve and Gene. My journey over the past year has been very similar to theirs.

End.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
