---
title: 'Forking Paseo: Mobile vibe coding for me - DEV Community'
url: https://dev.to/thisisryanswift/forking-paseo-mobile-vibe-coding-for-me-48pa
site_name: devto
content_file: devto-forking-paseo-mobile-vibe-coding-for-me-dev-commun
fetched_at: '2026-04-30T12:31:16.854681'
original_url: https://dev.to/thisisryanswift/forking-paseo-mobile-vibe-coding-for-me-48pa
author: Ryan Swift
date: '2026-04-29'
description: TLDR - I wanted to upgrade my coding-from-my-phone workflow. I found Paseo, forked it, and used AI... Tagged with ai, agents, vibecoding, opensource.
tags: '#ai, #agents, #vibecoding, #opensource'
---

TLDR - I wanted to upgrade my coding-from-my-phone workflow. I foundPaseo, forked it, and used AI agents to make the parts I cared about work better for me.

I'm spending a few weeks thinking about the process of coding with AI agents. Not just "which model is best" or "which harness performs best," but my actual mechanics. How I use these tools day-to-day. Where sessions live. How I know what an agent is doing when I am not staring at the same terminal.

On my laptop and desktop, I am slowly getting that into shape. The missing piece is my phone. I am admittedly obsessed with vibe coding, and lugging my laptop around everywhere is a bit of a social faux pas. Or at least I feel like it is.

I want to be able to check on agents, answer prompts, nudge a task forward, and occasionally kick off work when I do not have a computer in front of me.

The tool I wanted needed to match how I actually work:

* Linux support
* Android support
* Local coding, not a cloud service or Saas
* Support for the agents I already use, especially OpenCode
* A way to continue or inspect sessions from my real dev environment

SSH on a phone technically exists, but that is not the workflow I wanted. I wanted a control plane, not a tiny, inconvenient terminal.

### Paseo Mostly Worked

Paseowas the first thing I found that felt shaped like the problem I actually had.

There are other apps in this space. I also looked atEmdash,SoloTerm, and a handful of other projects. I suspect that Google, Anthropic, OpenAI, and other providers will continue to develop their own handoff to phone workflows. But I wanted one consistent layer across agents.

Paseo is a local-first app for monitoring and controlling coding agents remotely. A daemon runs on your machine. The mobile app talks to that. Your code does not need to move into a cloud workspace just so you can poke an agent from the couch. This was important. I did not want a separate mobile coding environment. I wanted a remote control for the environment I already have.

Paseo was also open source, which turned out to be the difference between "this is close" and "I can probably make this work."

Paseo already handled the working usable mobile app.

### The Gaps Were My Gaps

Paseo was already thoughtfully designed and looked great on mobile. It supported the core agents I cared about, but my OpenCode workflow exposed some rough edges.

The biggest one was session handoff. I would start a session in terminal OpenCode, then later want to pick it up in Paseo. Not a new agent. Not a fresh chat. The same session, with the same context. The details matter here. Who owns the session right now? What happens if the terminal and Paseo both try to drive it?

There were smaller papercuts too. Slash command autocomplete did not quite feel like OpenCode. Typing/qshould obviously mean quit, but the app's ranking and visual ordering could make that feel wrong. Workspace defaults mattered too. If OpenCode already knows the right model or mode for a project, Paseo should not casually override that with its own preferences.

And then there were subagents. OpenCode can spawn subagents, but in Paseo those could look like generic long-running tool calls. From the phone, that read as "is this thing stuck?" even when the agent is doing exactly what it should be doing.

Gemini CLI support is also on my list, but that is probably a future rabbit hole.

Paseo doesn't currently richly support subagents for OpenCode.

### I CanProbablyFix That

Turns out, if I can articulate a problem, agents can solve it. So I forked Paseo and used AI coding agents to improve Paseo's support for my needs.

Most of the work was not me sitting down with a perfect design doc and typing code by hand. It was me steering with human language:

* "I want to resume an OpenCode session that started outside Paseo."
* "This resumed session looks empty, but I know there is history."
* "Make/qbehave more like terminal OpenCode."
* "Subagents look like mysterious hangs. What's going on?"

The agents investigated the codebase, made changes, wrote tests, and occasionally wandered into a wall like agents do. I still had to make decisions and review the results. I was less "implementing a feature" and more describing the workflow I wanted until the software caught up.

I fear professional developers will cringe at parts of my approach. But I also think I am part of an interesting archetype that software people should pay attention to: technical enough to prompt well, inspect results, and push through rough edges, but not necessarily approaching every problem like a traditional dev.

That is not a replacement for engineering discipline. It is a new on-ramp to shaping software.

### What I Changed

I think my fork now has a much better OpenCode handoff story. But I really only focused on three areas where the "mobile gap" was most painfulto me:

* Zero-Friction Handoffs:The app now discovers active OpenCode sessions in any workspace. I can resume a session and immediately see a preview of recent history, making the jump from laptop to phone feel seamless rather than like a context-switch.
* Muscular Defaults:We tuned the UX to respect OpenCode's workspace settings and ranked slash commands so that common intents like/qor/exitare always at the top. The mobile keyboard is enough of a hurdle; the software shouldn't add to it.
* Subagent Transparency:Instead of opaque "tool calls," subagents now report their identity and current task status directly in the timeline. If I can't see what a subagent is doing, I'm inclined to assume it's stuck. Surfacing that intent turns a mysterious "hang" into a visible, productive task.

Better in-line support for OpenCode subagents.

### Where This Is Going

I am really interested in personal software right now. I am contributing small changes back to Paseo's main branch when appropriate, but I would not be surprised if my fork keeps diverging. That is kind of the point. I am trying to make it work for me and my workflows.

Gemini CLI integration is probably next. I am also interested in usage tracking across providers. I want Paseo to become a sort of home base for my available usage, active projects, and the agents I can point at them. A control plane for my agents and projects.

Open source plus coding agents made the gap between "this tool is close" and "this tool fits me" much smaller. Open source software has always invited tinkering. AI agents make the tinkering cheaper.

And now, apparently, some of that tinkering can happen from my phone. Which is either very cool or a sign I should touch grass.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse