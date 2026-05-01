---
title: Stop Using Your Clipboard to Share Context - DEV Community
url: https://dev.to/thisisryanswift/stop-using-your-clipboard-to-share-context-3941
site_name: devto
content_file: devto-stop-using-your-clipboard-to-share-context-dev-com
fetched_at: '2026-05-01T11:58:28.846651'
original_url: https://dev.to/thisisryanswift/stop-using-your-clipboard-to-share-context-3941
author: Ryan Swift
date: '2026-04-30'
description: We're all learning how to code with agents. If you're "in the bubble" it can feel like everyone is... Tagged with ai, agents, mcp, cli.
tags: '#ai, #agents, #mcp, #cli'
---

We're all learning how to code with agents. If you're "in the bubble" it can feel like everyone is tokenmaxxing. Automating everything. Spinning up overnight agents to write full apps while they sleep. The reality I see with a lot of developers is much more normal:

They are copying and pasting code back and forth from VS Code and ChatGPT.

I am seeing slow adoption of built-in chat interfaces in IDEs like Copilot, Cursor, and Antigravity. CLI agents still feel relatively fringe among next-gen developers. I know this likely is not what you're hearing or seeing on Twitter.

Anyway, I've roasted plenty of developers for copying code back and forth from their IDEs into web chat interfaces. This week, I realized I have been doing the same thing, just with more terminal panes. A test fails in one terminal pane. An agent is working in another. I copy the error, paste it into the agent, wait, run another command, copy the next error, paste again.

My cool hacker-y CLI workflow suddenly felt... less cool.

The obvious fix is: let the agent read the terminal. The less obvious problem is: I do not want agents casually reading every terminal pane I have open.

## The CLI Version Of Copy/Paste

I useZellijas my terminal multiplexer. If you have used Tmux, it is the same general idea: panes, tabs, sessions, and a bunch of terminal state living in one place. I really like Zellij. I struggled with Tmux for whatever reason and never looked back. I seem to be in a minority here though.

I use a variety of CLI coding agents: OpenCode, Gemini CLI, Claude Code, Codex, and whatever else I am trying that week.

A normal tab looks like OpenCode on the left, and one or two panes on the right for running commands, observing tests, or watching a dev server.

But the panes are distinct. Agents do not automatically know what happened in the test pane. My test pane does not know what the agent is trying to debug. So I become the bridge, manually ferrying errors and logs back and forth.Copying and pasting.

Integrated agent shells help sometimes, but they are not the whole answer. Long-running commands eat up agent time. Many commands need elevated permissions. Plus, I already have a terminal layout and workflow I like.

I did not want to move everything into the agent. I wanted the agent to see what I see.

## Everything Means Everything

The naive version of my project was easy: give the agent full access. Let it read the whole Zellij session. And call it a day.

Except... secrets and security are a thing. I already play it too fast and loose with my agents. I'm trying to be better about that. I needed selected-pane awareness, not full terminal visibility.

That became the design constraint forzellij-agent-tools: agents should only read panes I explicitly approve, and that approval should be visible where the pane actually lives.

## Zellij As The Consent Surface

The project is a Zellij plugin plus a local MCP sidecar.

The Zellij plugin is the human-facing part. It lists panes, asks for approval, marks watched panes, and lets me revoke access.

The sidecar is the agent-facing part. It exposes a small set of MCP tools so agents can list watched panes and read bounded output from the panes I approved.

I did not want consent hidden inside an agent chat. I can see the agent calling the tools in line, but I approve it in the Zellij plugin. I wanted separate surfaces. MCP is the agent interface. Zellij is the human interface.

That feels like the right boundary.

The v1 tool surface is intentionally boring. Just: ask to watch a pane, list watched panes, read a bounded snapshot, read output after a cursor, check status.

That is enough to stop me from copy/pasting every error by hand.

## Not Security Itself

I'm not naive to the fact that agents can probably get around this. If an agent has unrestricted shell access as my user, it may be able to call the Zellij CLI directly or do other things I did not intend.

I am not trying to solve malicious local code here. I am trying to make my normal workflow less sloppy.

The goal is for the easy path to be the safer path: ask for the pane, show the user, read only what was approved, fail closed when state is stale or revoked.

That already feels better than copy/paste chaos or full terminal visibility.

## More To Do

I still have plenty to do on this project. It's a very rough first pass. But the direction feels right and I think it solves a real problem that I imagine other folks have.

I'm gonna keep using it and iterating on it for my workflows.Feel free to check it out!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse