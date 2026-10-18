---
title: Sphinx — you can outsource your thinking, but not your understanding
url: https://sphinx-six-theta.vercel.app/
site_name: hackernews_api
content_file: hackernews_api-sphinx-you-can-outsource-your-thinking-but-not-you
fetched_at: '2026-10-18T21:14:49.219655'
original_url: https://sphinx-six-theta.vercel.app/
author: critiquebrowser
date: '2026-10-18'
description: A Git hook for agent-assisted development. Before your agent’s code ships, Sphinx asks you a question about what it actually does.
tags:
- hackernews
- trending
---

* Free
* FOSS

“You can outsource your thinking,but not yourunderstanding.”

—Sun Tzu

Sphinx is a Git hook for agent-assisted development. Before your agent’s code ships, it asks you a question about what that code actually does.

$ 
npm install -g sphinx-understand
Copy

Built to run on minimal tokens, from your existing coding agent, OpenRouter, or any OpenAI-compatible endpoint.

$
 git push origin main
sphinx · understanding check for main
11 files changed · 
+5,012
 
−3,147

Sphinx

Your webhook handler now saves the event IDbeforecallingcharge(). Stripe times out and sends the same event again. What happens on the retry?

You

It runs twice, so the customer is charged twice.

Sphinx

Not quite. The retry finds the saved ID and returns 200 without charging. But that ID is stored before the charge succeeds. Ifcharge()fails, what does the next retry do?

You

It skips the charge, so the customer is never billed.

✓
 Understood. Pushing to origin/main.

An illustrative exchange. Real questions come from your diff.

1. 01### You push.Or your agent does. Git pauses on the branches you protect.
2. 02### Sphinx asks.A reviewer that never saw your chat reads the diff and asks what the change does when things go wrong.
3. 03### You answer.Get it wrong and you learn why, then try a new scenario. Get it right and the push continues.
The real questionnaire: a push waits, you answer, Git continues.

Works withCodex, Claude Code, Cursor, OpenCode,andPi, or plain Git. Your answers never reach the coding agent, and.envfiles and keys are never opened. In a hurry?sphinx yololets pushes through, and every skip is logged.

## Start in a minute.

# Node 22.19+ · macOS, Linux, or WSL

npm install -g sphinx-understand

sphinx install

# then push as usual

git push

sphinx installconnects Git and your coding agents and asks which model should review.Read the docsfor everything else.