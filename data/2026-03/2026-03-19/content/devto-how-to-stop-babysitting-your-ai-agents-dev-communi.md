---
title: How to Stop Babysitting Your AI Agents - DEV Community
url: https://dev.to/jrswab/how-to-stop-babysitting-your-ai-agents-4376
site_name: devto
content_file: devto-how-to-stop-babysitting-your-ai-agents-dev-communi
fetched_at: '2026-03-19T11:17:42.082260'
original_url: https://dev.to/jrswab/how-to-stop-babysitting-your-ai-agents-4376
author: J. R. Swab
date: '2026-03-18'
description: Define focused LLM agents in plain text. Run them from anywhere. Chain them with pipes. Tagged with llmagents, cli, devtools, go.
tags: '#llmagents, #cli, #devtools, #go'
---

Every time I need an LLM to do something, the ritual is the same. Open a chat window. Type a prompt. Read the response. Decide if it's good enough. Repeat tomorrow. That's not automation that's a new job I didn't apply for.

The frustrating part isn't the AI. The frustrating part is that I'm the scheduler, the context manager, and the output parser all at once. I'm writing the same prompt variations over and over because nothing persists. I'm watching a spinner because there's no way to fire and forget. The tool is supposed to be doing the work.

So I built a 12MB binary to fix it.

## Unix already solved this

You don't open a chat window to rungrep. You pipe input in, get output out, and chain it with something else. Small tools, one job each, composable by design.

The Unix philosophy isn't clever it's right.. and it's been right for fifty years.

AI agents should work the same way. One job. Clean input/output. Plugs into your existing workflows. The problem is that most AI tooling goes the opposite direction. Massive context windows, general-purpose sessions, chat interfaces bolted onto automation primitives. The chat interface made sense when we were exploring what LLMs could do.

It's time to stop treating every task like an open-ended conversation.

This is where Axe comes in. Axe is a CLI that runs single-purpose LLM agents defined in plain text config files. You define an agent, give it a job, and run it from wherever you'd run any other command.

## What it actually looks like

Here's a PR reviewer that runs before every commit via a git hook:

git diff
--cached
 | axe run pr-reviewer

Enter fullscreen mode

Exit fullscreen mode

Stdin is always accepted. Output goes to stdout. That's it. No setup wizard, no subscription tier, no "connect your workspace." The git hook already exists. Axe just sits in the pipe.

Or say you want nightly log analysis. Drop this in a cron job:

cat
 /var/log/app/error.log | axe run log-analyzer

Enter fullscreen mode

Exit fullscreen mode

Debug info goes to stderr so it doesn't pollute your pipeline. Clean findings go to stdout. Wire it into whatever monitoring you already have like email, Slack, or a file.

Axe doesn't care.

The part I find most useful is chaining agents. A parent agent can delegate to sub-agents for focused subtasks. Each sub-agent runs with its own isolated context window and returns only the result. The previous agent never sees the sub-agent's internal reasoning, intermediate files, working memory, or even its output.

## Under the hood (briefly)

Agent config is TOML:

name

=

"pr-reviewer"

description

=

"Reviews git diffs for issues"

model

=

"anthropic/claude-sonnet-4-20250514"

[params]

temperature

=

0.3

[memory]

enabled

=

true

last_n

=

10

Enter fullscreen mode

Exit fullscreen mode

The agent's instructions live in aSKILL.mdfile next to the config. Plain markdown. Human-readable, version-controllable, greppable. No database, no embeddings, no proprietary format. If you want to know what an agent does, you open the file. If you want to change what it does, you edit the file. That's the whole interface.

The--dry-runflag shows the full resolved context, system prompt, skill file contents, any piped stdin, model parameters, without calling the LLM. Useful for debugging. Also useful if you want to estimate token cost before committing to a run. I use it more than I expected to.

Agents can also remember across runs. Memory is plain markdown: each run appends a timestamped entry to a file sitting next to the config. No database, no schema migration. If something looks wrong, you open the file and edit it.

## What it's not

Not a framework. Not a platform. Not a chat window. Not a SaaS dashboard with an "Agents" tab and a usage graph you'll check twice before forgetting it exists.

Axe aims for minimal dependencies. It's a single binary, no daemon running in the background, no runtime to install. It just runs wherever you drop it. Licensed as Apache 2.0 and free forever, pull requests welcome.

Axe is the executor, not the scheduler. Use cron, git hooks,entr,fswatch, whatever you already have. Axe doesn't want to own your workflow. It wants to run one agent, cleanly, and get out of the way.

If you want agents to feel like infrastructure instead of products you have to babysit, that's what this is for.

The repo is atgithub.com/jrswab/axe.

Go try it. Build something weird with it like a commit message writer, a nightly changelog summarizer, whatever you keep doing manually.

If it saves you from being the scheduler, the context manager, and the output parser all at once. That's the whole point.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
