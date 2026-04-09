---
title: How to Stop Your AI Agent From Making Unwanted Code Changes - DEV Community
url: https://dev.to/blockopensource/how-to-stop-your-ai-agent-from-making-unwanted-code-changes-5g85
site_name: devto
fetched_at: '2025-12-17T19:09:46.260254'
original_url: https://dev.to/blockopensource/how-to-stop-your-ai-agent-from-making-unwanted-code-changes-5g85
author: Rizèl Scarlett
date: '2025-12-10'
description: AI agents are often described as brilliant, overeager interns. They're desperate to help, but... Tagged with ai, agents, goose, git.
tags: '#ai, #agents, #goose, #git'
---

AI agents are often described as brilliant, overeager interns. They're desperate to help, but sometimes that enthusiasm leads to changes you never asked for. This is by design: the large language models powering agents are trained to be helpful. But in code, unchecked helpfulness can create chaos. Even with clear instructions and a meticulous plan, you might hear, "Let me just change this too…" A modification that's either unnecessary or, worse, never surfaced for review.

Sure, you can scourgit diffto find and revert issues. But in a multi-step process touching dozens of files, untangling one small, unwanted change becomes a manual nightmare. I've spent hours combing through 70 files to undo a single "helpful" adjustment. Asking the agent to revert is often futile, as conversational memory isn't a snapshot of your codebase.

This problem has a classic engineering solution. We commit early and often to create checkpoints, enabling easy rollbacks and clean collaboration. So, why don't we enforce the same discipline on our AI agents? Here’s the workflow I use withgooseto ensure we're creating snapshots of the codebase:

### 1. Set Up Version Control

I set up theGitHub CLI(gh). I've found Goose interacts with it flawlessly. TheGitHub MCP Serveris a good alternative.

### 2. Branch First

Always start on a new feature branch. Never let an agent commit directly to main.

### 3. Set Rules in a Context File

This is the key. I use a.goosehintsorAGENTS.mdfile with one critical instruction:

"Every time you make a change, make a commit with a clear message."

This does two things: it automates checkpointing so I don't have to babysit the session, and it captures perfect snapshots in time, turning the git history into an undo stack for the entire collaboration.

### 4. Collaborate with Confidence

Now I can prompt goose to build, fix, or refactor. If it veers off course or makes a design choice I dislike, I can instantly review the git log or simply say:

"Revert to commit abc123."

## The Result

By integrating this basic software practice, I replace anxiety with awareness. goose gets to be brilliantly helpful, and I get to stay in control.

No more hunting through 70 files for that one unwanted change. No more hoping the agent remembers what it did three steps ago. Just clean, reversible commits that let me focus on building instead of damage control.

Try out this method withgooseon your next project. Your future self (and your git history) will thank you.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
