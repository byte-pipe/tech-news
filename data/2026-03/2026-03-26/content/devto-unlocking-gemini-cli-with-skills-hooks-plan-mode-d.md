---
title: Unlocking Gemini CLI with Skills, Hooks & Plan Mode - DEV Community
url: https://dev.to/googleai/unlocking-gemini-cli-with-skills-hooks-plan-mode-2bgf
site_name: devto
content_file: devto-unlocking-gemini-cli-with-skills-hooks-plan-mode-d
fetched_at: '2026-03-26T11:22:38.623923'
original_url: https://dev.to/googleai/unlocking-gemini-cli-with-skills-hooks-plan-mode-2bgf
author: Greg Baugues
date: '2026-03-20'
description: In Unlocking Gemini CLI with Skills, Hooks &amp; Plan Mode, we moved past the basics and into the... Tagged with gemini, ai, cli.
tags: '#gemini, #ai, #cli'
---

In Unlocking Gemini CLI with Skills, Hooks & Plan Mode, we moved past the basics and into the "power user" features ofGemini CLI.

I was joined by Jack Wotherspoon from the Gemini CLI team to show how developers can exert more control over their AI agents and handle complex, multi-step projects with confidence.From a 20-minute app build to the introduction of a "read-only" research mode, this episode was packed with tools designed to bridge the gap between AI autonomy and developer intent.

## The 20-minute build: From idea to deployment

 

To set the stage, Jack showcased Memory Wall, a digital bulletin board built using React, Three.js, and Firebase. The kicker? It took only 20 minutes to go from a blank slate to a live-deployed application.

This served as the playground for the day's deep dives:

## 1. Deterministic control with hooks

One of the biggest hurdles with AI agents is their non-deterministic nature.Hookschange that. They are scripts that run at specific lifecycle points—like at session start or before a tool call.

 

* The "dev server" hook: Jack demonstrated a hook that checks if a local dev server is running on startup. If not, Gemini CLI alerts the user and offers to start it.
* Safety first: You can use hooks to run linters or "security guards" that prevent the AI from writing messy code or deleting sensitive files.

Pro tip: Use the new Background Tasks feature (Control + B) to keep your dev servers running in the terminal without blocking your conversation with Gemini.

## 2. "Expert Hats": These specialized skills help to refine the behavior of these tools

If you’ve ever worried about "context bloat"—where an AI gets confused by too much information—skills are your solution. Jack described these as "library books on a shelf."

 

* Progressive disclosure:Instead of loading every best practice into every prompt, Skills load specialized knowledge (like Three.js expertise or documentation style guides) only when they are triggered
* The skill creator:Gemini CLI now has a built-in skill to help you build skills. Just ask: "Create a docs-writer skill for this project," and the CLI will walk you through a setup interview.

## 3. The "Ask User" tool

 

Gone are the days of the CLI just guessing what you want. With the newAsk Usertool, Gemini CLI can pause and present interactive dialogues, multiple-choice questions, and yes/no prompts. This ensures the agent is aligned with your vision before it touches a single line of code.

## 4. Look before you leap with Plan Mode (preview)

Perhaps the most anticipated feature is Plan Mode, currently in preview. It transforms Gemini CLI into a read-only researcher.

 

* Research first:In Plan Mode, the agent explores your codebase and external docs to create a structured "battle plan."
* User approval:It presents this plan to you for feedback. Only once you give the "green light" does it switch to execution mode to start editing files.

## Ready to dive deeper?

Watch: Missed the live demo?Catch the full replayhere.

* Learn:Take the freeDeepLearning.aicourse to get hands-on and learn more.
* Contribute:Gemini CLI is open-source! Check out the "Help Wanted" labels onGitHub.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse