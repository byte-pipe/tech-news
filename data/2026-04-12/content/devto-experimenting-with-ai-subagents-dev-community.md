---
title: Experimenting with AI subagents - DEV Community
url: https://dev.to/nfrankel/experimenting-with-ai-subagents-pc7
site_name: devto
content_file: devto-experimenting-with-ai-subagents-dev-community
fetched_at: '2026-04-12T19:39:34.307078'
original_url: https://dev.to/nfrankel/experimenting-with-ai-subagents-pc7
author: Nicolas Fränkel
date: '2026-04-09'
description: I like to analyze codebases I start working on, or that I left for months. I ask my coding assistant,... Tagged with ai, agents, subagents, softwareengineering.
tags: '#ai, #agents, #subagents, #softwareengineering'
---

Narrowing scope to avoid agent hallucinations

I like to analyze codebases I start working on, or that I left for months. I ask my coding assistant, case in point, Copilot CLI: "analyze the following codebase and report to me improvements and possible bugs." It's vague enough to leave room for crappy feedback, but also for some interesting insights.

I did it last week on a code base. Copilot returned a list of a dozen items. I asked it to create a GitHub issue for each, with the relevant labels, including priority.

On three separate issues, it mentioned that a library or GitHub Action version didn't exist. On all of them, it was plain wrong. I used a version more recent than the data it was trained on. Closed as won't fix.

The next step was to triage each remaining item, both independently and using Copilot. Some of them felt a bit fishy, some of them felt solid. In the end, I closed about half of them. Four remained. They were pretty good. I wanted to act upon them in the most productive way possible, so I decided to use sub-agents.

## Using sub-agents

When newbies decide to use sub-agents, chances are they'll waste a lot of time. Because they are autonomous, you want to give themeverypossible bit of information, so that they choose the best course of action without input. You must qualify every issue independently. While you can still technically interact with the sub-agents when they work, it drops their value significantly.

However, this work can be done in the previous triage step. If you have enough data to accept or close the item, there's a high chance you dug to get enough details. Refer toHow I Use Claude Code, and especially thethe Annotation Cyclesection, for more details.

Here's my prompt to trigger the agents, formatted for you, not for the agent. Feel free to improve it, and don't hesitate to give me feedback.

For each issue X, Y, & Z, I want you to launch a sub-agent that:

* Fetch the issue using theghtool
* Read its description
* Create a dedicated branch using thegit worktreecommand
* Implement the feature or fix the issue
* If the feature/issue warrants it, create a test or tests around it
* All tests must pass before you continue
* Commit using a semantic commit
* Push it on its own branch to GitHub
* Create a PR with this branch, using the following naming pattern

Two things of note.

First, Copilot connects to the GitHub MCP Server by default, but only in read-only mode. If you want to actually create (or update) issues, my advice is to usegh. Authenticate in a terminal with it, and run Copilot CLI in the same terminal. It will allow Copilot to interact with GitHub with all permissions.

Then,git branchworks in the same folder. Each agent would step on the other's toes.Git worktreessolves the solution elegantly. In short, the command allows mapping a branch to a dedicated folder on the filesystem:

A git repository can support multiple working trees, allowing you to check out more than one branch at a time. Withgit worktree adda new working tree is associated with the repository, along with additional metadata that differentiates that working tree from others in the same repository. The working tree, along with this metadata, is called a "worktree".

Fun fact: I have known worktrees for some time, but I never had a use case for them.

The obvious benefit of using sub-agents is parallel processing. While you must research each item sequentially, sub-agents can implement them in parallel. However, IMHO, the main benefit iscontext isolation.

## Context engineering

Sub-agents are a boon: each one starts with a fresh context. You don't pollute the main context with irrelevant data.

As a reminder, the context is everything the agent will act upon:

* System prompts,e.g., "You are an expert Java developer and architect with more than 20 years of experience"
* User prompts,e.g., "Refactor this class to use immutable values when possible"
* Additional information set byRAG
* Previous messages,i.e., the conversation
* Available tools
* Tools' potential output
* etc.

The temptation is huge to put everything in the context. However, context capacity is limited and is measured in tokens. A perfectly-crafted context contains all the necessary data for the task at hand, but nothing more. As engineers, we strive for efficiency, not for perfection. For every unrelated task, we should start a new context. Interestingly enough, Claude Code recently started offering context optimization after each request. It's up to you to decide whether to keep it or not.

## Conclusion

We now manage a team of agents instead of a team of junior developers. The situation is somehow similar. You must be very clear about what you want. You must design in detail upstream. Those you delegate to won't probably ask questions, and might end up in the wrong place. You need to carefully review the results.

There are two main differences, though. You'll get outputs in minutes, not days. On the flip side, we aren't teaching the next generation of developers.

It makes sense at every company's level: why train junior developers if the AI can replace them? Market numbers already show this trend. But seniors aren't born. They are former junior developers who went through all the steps. For me, it doesn't change a thing. In the grand scheme of things, user companies are going to beverysorry about their shortsightedness in a couple of years, once they'll realize how dependent they have become on vendors and when they face a shortage of seniors.

To go further:

* How I Use Claude Code

Originally published atA Java Geekon April 5th, 2026.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse