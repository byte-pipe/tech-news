---
title: Agents as scaffolding for recurring tasks. | Irrational Exuberance
url: https://lethain.com/agents-as-scaffolding/
site_name: tldr
content_file: tldr-agents-as-scaffolding-for-recurring-tasks-irration
fetched_at: '2026-04-15T11:56:01.237040'
original_url: https://lethain.com/agents-as-scaffolding/
date: '2026-04-15'
published_date: '2026-04-12T10:00:00-07:00'
description: One of my gifts/curses is an endless fixation with how processes can be optimized. For a brief moment early in my career, that was focused on improving how humans collaborate, but that quickly switched to figuring out how we can minimize human involvement, and eliminate human-to-human handoffs as much as possible. Lately, every time I perform a recurring task–or see someone else perform one–I think about how we might eliminate the human’s involvement entirely by introducing agents. This both has worked well, but also worked poorly, and I wanted to highlight the pattern I’ve found useful.
tags:
- tldr
---

One of my gifts/curses is an endless fixation with how processes can be optimized.
For a brief moment early in my career, that was focused on improving how humans collaborate,
but that quickly switched to figuring out how we can minimize human involvement, and eliminate
human-to-human handoffs as much as possible.
Lately, every time I perform a recurring task–or see someone else perform one–I think about
how we might eliminate the human’s involvement entirely by introducing agents.
This both has worked well, but also worked poorly, and I wanted to highlight the pattern
I’ve found useful.

For a concrete example, a problem that all software companies have is patching security vulnerabilities.
We have that problem too, and I check our security dashboards periodically to ensure nothing has gone awry.
Sometimes when I check that dashboard, I’ll notice a finding that’s precariously close to our resolution SLAs,
and either fix it myself or track down the appropriate team to fix it.
However, this feels like a process that shouldn’t require me checking on it.

Five to six months ago, I added Github Dependabot webhooks as an input into our internal agent framework.
Then I set up an agent to handle those webhooks, including filtering incoming messages down to the highest priority issues.
About a month ago, when I upgraded from GPT 4.1 to GPT 5.4 with high reasoning, I noticed that it got
quite good at using the Github MCP to determine the appropriate owners for a given issue, using the same variety
of techniques that a human would use: looking at Codeowners files where available, looking at recent commits on
the repository, and so on. The alerts and owners were already getting piped into a Slack channel.

So, this worked! However, it didn’t actually work that well, because despite repeated iteration on the prompt,
including numerousCRITICAL: you must...statements, it simply could not reliably restrict itself tocriticalseverity alerts. It would also include somehighseverity alerts, and even the occasionalmediumseverity alert.
This is a recurring issue with using agents as drop-in software replacement: they simply are not perfect, and interrupting
your colleagues requires a level of near-perfection.

If I’d hired someone on our Security team to notify teams about critical alerts, and they occasionally flagged non-critical alerts,
eventually someone would pop into my DMs to ask me what was going wrong. That didn’t happen here, because the knowledge that those DMs
would show up prevented me from rolling the notifications out more aggressively.
Coding agents address this sort of issue by running tests, typechecking, or linting, but less structured tasks
are either harder or more expensive to verify. For example, I could have added an eval verifying messages didn’t mention medium or high
severity tasks before allowing it to send to Slack, but I found that somewhat unsatisfying despite knowing that it would work.

Instead, after some procrastination on other tasks, I finally prompted Claude to update this agent to rely on
acode-driven workflowwhere flow-control is managed by software by default, and only
cedes control to an agent where ideal.
That workflow looks like:

1. A webhook comes in from Dependabot
2. Script extracts the severity and action (e.g. is it a new issue versus a resolved issue),
and filters out low priority or non-actionable webhooks
3. The code packages the metadata into a list of issues and repositories
4. The code passes each repository-scoped bundle to an agent with our internal ownership skill and
the Github MCP to determine appropriate folks to notify for each issue
5. The issues and ownership data are passed to a second agent that formats them
as a Slack message

This works 100% of the time, while still allowing us to rely on our internal ownership skill to
determine the most likely teams or individuals to notify for a given problem.
It’s now something I can rollout more aggressively.

The immediate fast follow was a weekly follow-up ping for open critical issues,
relying on the same split of deterministic and agentic behaviors.
The next improvement will be automating the generation of the vulnerability fixes,
such that the human involvement is just reviewing the change before it automatically
deploys.
(Wealready do this for Dependabot generated PRs,
but in my experience Dependabot can solve a reasonable subset of identified issues,
but far from all of them.)

That is the pattern that I’ve found effective:

1. Prototype with agent-driven workflow until I get a feel for the workflow and what’s difficult about it
2. Refactor agent-driven control away, increasingly relying on code-driven workflow for more and more of the solution
3. End with a version that narrowly relies on agents for their strengths (navigating ambiguous problems like identifying code owners)

This has worked well for pretty much every problem I’ve encountered. The end-result is faster, cheaper, and more maintainable.
It’s also a cheap transition, generally I can take logs of some recent runs, the agent’s prompt, and some brief instructions,
throw them into Codex/Claude, and get a working replacement in a few minutes.