---
title: 'AI Engineering Metrics: Why Lines of Code and PR Counts No Longer Work'
url: https://bharatsharma.pro/articles/activity-based-engineering-metrics-are-obsolete
site_name: tldr
content_file: tldr-ai-engineering-metrics-why-lines-of-code-and-pr-co
fetched_at: '2026-09-15T15:27:50.825001'
original_url: https://bharatsharma.pro/articles/activity-based-engineering-metrics-are-obsolete
author: Bharat Sharma
date: '2026-09-15'
published_date: '2026-09-15'
description: AI has made activity proxies like lines of code, commits and PR counts actively misleading. Here is what to measure instead, and a 90-day plan to get there.
tags:
- tldr
---

AI has not made engineering metrics obsolete. It has made one specific class of them, the activity proxies most organizations still put in front of their boards, actively misleading. At the same time it has made system-level outcome measures more important than they have ever been. That split is the whole argument. The evidence for it is now good enough to act on.

Here's the shape of the problem. A 2026 Halkwinds survey of 758 engineering organizations found 76% had rolled out at least one AI coding assistant organization-wide, up from 41% in 2024. Only 34% could point to a measurable, audited change in delivery metrics from that rollout.

Two-thirds of adopters can't tell whether the thing worked. Not because it didn't. Because the instruments they're reading were built for a world where writing code was the expensive part.

## The research doesn't agree with itself, and that's the finding

If you go looking for AI's productivity coefficient you will not find one. You'll find a scatter plot.

METR's 2025 randomized controlled trial put 16 highly experienced open-source developers on 246 tasks in mature repositories they already knew well. With AI tools they were 19% slower, and they had believed beforehand that they would be faster. Peer-reviewed randomized field experiments at Microsoft, Accenture and a Fortune 100 company, 4,867 developers in total, estimated 26.08% more completed tasks. An observational analysis of 16,223 developers showed up to 40.5% more PRs among heavy GitHub Copilot users, though "heavy users" is a self-selected group, and the people who lean hardest on a new tool may already have been your most prolific committers. Read that one as an upper bound, not a forecast.

Reported change in developer output with AI tools, by study
Three estimates on one axis: METR's randomized trial at minus 19 percent, the Microsoft, Accenture and Fortune 100 field experiments at plus 26 percent, and an observational analysis of heavy Copilot users at plus 40.5 percent, marked as an upper bound.
no change
METR RCT, 2025: -19% (16 expert maintainers, own repos)
METR RCT, 2025
16 expert maintainers, own repos
-19%
Microsoft / Accenture / Fortune 100 RCTs: +26% (4,867 developers, assigned tasks)
Microsoft / Accenture / Fortune 100 RCTs
4,867 developers, assigned tasks
+26%
Heavy Copilot users, observational: +40.5% (16,223 developers, self-selected)
Heavy Copilot users, observational
16,223 developers, self-selected
+40.5%
-20%
0%
+20%
+40%
self-selected sample: an upper bound
Reported change in developer output with AI tools. Same question, three cohorts, results 60 points apart.

So which is it? All of them. The METR cohort was expert maintainers in codebases they knew intimately, doing work where the bottleneck was judgment, not typing. The enterprise cohorts were doing assigned tasks with more boilerplate and less context. AI's effect varies with task type, developer experience and how much the codebase already lives in someone's head. If your engineering org looks more like the METR sample (small, senior, deep in a legacy system) you should expect friction. If it looks more like the enterprise field studies (large, mixed seniority, lots of well-trodden patterns) you should expect gains, at least in raw output.

The point isn't that one study is wrong. It's that a metric which can't distinguish between those two situations is useless to you.

## What's actually broken

Most engineering scorecards still lean on activity: commits, PRs, story points. Activity is cheap to count. AI removes the last excuse for that. When a feature branch costs seconds to generate, counting branches measures nothing.

Lines of code.AI generates boilerplate for free. Good engineering often means deleting code. LOC has always punished the refactor and rewarded the bloat; now the bloat is automated.

Commit and PR counts.A 2026 analysis of roughly 110,000 open-source PRs found Claude Code-authored PRs averaging about six times the size of human-authored ones. Padding, not progress.

Story points.Still fine for a team planning its sprint. Not fine as a productivity signal, because historical calibration assumed human effort per point, and that assumption is now wrong in ways that differ task by task.

Frankly, none of this is a new critique. What's new is that the distortion is no longer a rounding error.

## Where the work went

AI doesn't remove engineering work. It moves it downstream. The discipline is shifting from authoring to comprehension: reading, validating, reviewing, deciding whether the thing that appeared in the PR should exist at all.

You see it in the pipeline first. Developers generate code fast, the code floods CI, human reviewers drown. GitClear's longitudinal analysis of 211 million lines of code from 2020 to 2024 found copy/pasted duplicate code exceeding moved (refactored) code for the first time in its dataset. Separate Q1 2026 research puts code churn among heavy AI users at up to nine times that of non-users.

You see it in security next. Veracode's 2025 GenAI Code Security Report ran over 100 large language models through controlled coding tasks; 45% of the generated samples failed security tests, with OWASP Top 10 issues like cross-site scripting and log injection. That's the lab. The field: Apiiro's telemetry across Fortune 50 enterprise repositories between December 2024 and June 2025 found AI-assisted developers committing at three to four times the standard rate. Critical architectural flaws rose with them, and privilege escalation paths specifically were up 322%.

And you see it in people. Under deadline pressure, engineers accept working code they don't fully understand. The gap between "it passes" and "I know why it passes" is where the next incident lives.

The industry has started calling the resulting pattern a J-curve: an initial productivity dip after AI rollout, then recovery. The dip is well documented; it is everything above. The recovery is asserted more often than it's shown. Treat it as a hypothesis about your organization, and instrument for it, rather than a promise from a vendor deck.

## The senior/junior inversion

One thing the split evidence does tell you clearly. The enterprise field experiments found less-experienced developers adopted AI more readily and gained more from it. The METR maintainers, the most experienced people in the sample, gained nothing and lost time. Put those together and you get something managers should sit with: AI compresses the production gap between junior and senior engineers while widening the validation gap. Seniors become more valuable as reviewers, architects and the people who say no. That has consequences for career ladders that most organizations haven't touched. If a junior can produce senior-looking output but can't yet tell when it's wrong, what exactly are you promoting on? And if your seniors spend their week reviewing machine output, how long do they stay?

The senior/junior inversion: output converges, judgment diverges
Two panels of paired bars. Before AI, junior engineers trail senior engineers on both output and judgment. With AI, junior output rises close to senior output while the judgment gap stays wide or grows.
Before AI
Before AI, Output: junior 40, senior 90 (illustrative)
Output
Before AI, Judgment: junior 35, senior 90 (illustrative)
Judgment
With AI
With AI, Output: junior 82, senior 95 (illustrative)
gap narrows
Output
With AI, Judgment: junior 30, senior 95 (illustrative)
gap widens
Judgment
junior engineer
senior engineer
illustrative, not measured
AI compresses the production gap between junior and senior engineers while widening the validation gap.

## What to measure instead

Keep DORA-style delivery outcomes. Demote the activity proxies. Add a small number of diagnostics that expose where the displaced work is piling up.

None of these are new inventions. Most are re-weightings of things already in DORA, SPACE or your CI logs. What changes is which ones you look at first.

Category
Diagnostic
Definition
Unit of analysis
Delivery flow
Review queue time
First substantive review timestamp − PR-ready timestamp
Team, weekly
Code quality
Short-horizon rework
Lines changed or reverted within 14 days ÷ lines introduced
Repo, weekly
Infrastructure health
Validation failure rate
PRs failing required test/security gates ÷ PRs entering validation
Pipeline, weekly
Production quality
Post-deployment rework
Deployments needed to remediate user-facing defects ÷ total deployments
Service, monthly
Cost
Rework per unit of AI spend
Short-horizon rework lines ÷ AI tooling spend (seat + token) for the same period
Org, monthly

Some rules that matter more than the formulas:

* Track trends against a pre-AI baseline, not absolute numbers. A rising rework ratio in the months after rollout is the earliest signal that generation is outrunning comprehension.
* Never report any of these at the individual level. Not once. The moment it's visible per engineer it becomes a leaderboard, and leaderboards get gamed within weeks.
* The cost line is there because the CFO will ask. Adoption percentage tells them nothing. Rework per dollar of AI spend, trending down, is something they can act on.
* Add SPACE's satisfaction dimension alongside these. If the review load lands on your senior engineers, burnout shows up in pulse surveys before it shows up in attrition, and attrition is the expensive version.

None of these measures business value directly. Pair them with whatever the work was meant to move: revenue, adoption, retention, cost-to-serve, reliability. Otherwise you've built a faster factory with no idea what it's for.

## The amplifier

AI acts as a magnifying glass on the engineering culture you already have. The 2025 DORA report formalized this as the amplifier effect: where organizations had strong automated testing and high-quality internal platforms, AI correlated with higher throughput. The same data showed AI adoption correlating with higher instability, more change failures, more rework, longer recovery. Correlation, in both directions. But the practical reading is clear enough: if your platform is weak, AI makes it weaker faster, and activity metrics will report that as success.

Ironclad, a legal-contracting AI company, hit this directly when unconstrained AI adoption started overloading their CI. Their response was to stop counting generation and start counting what survives review: a "Trusted Throughput" measure that uses AI to assign a complexity t-shirt size to merged PRs. Mingsheng Hong, Ironclad's VP of AI, describes it as an evolving proxy, not a finished answer. They also capped agentic loop steps and enforced token hygiene so autonomous tools couldn't sit in a retry loop hammering a failing pipeline.

Worth saying: there are teams where activity metrics haven't broken. Small, senior, greenfield, everyone reviewing everyone. PR count there is still a rough but honest signal, because the review step is doing its job. The breakage is a function of scale and of how far apart generation and validation have drifted.

## A 90-day playbook

Days 1–30: baseline.If AI isn't broadly deployed yet, take the six months of delivery telemetry you already have and freeze it. If it is deployed, reconstruct the baseline from history and find your natural control groups: teams or task categories with materially different adoption. GitHub and GitLab APIs give you PR timestamps and review events; CI logs give you gate failures; Jira or Linear give you the defect-remediation deployments. Nothing here needs a new vendor.

Days 31–60: guardrails.Programmatic limits on PR size. Hard caps on agentic loop iterations. Required gates that can't be bypassed by an autonomous tool. This is the unglamorous part and it's the part that protects shared infrastructure from a thousand-line unreviewed drop at 4pm on a Friday.

Days 61–90: rewire the report.Remove LOC, commit count and raw PR count from every executive deck. Replace with review queue time and short-horizon rework, per team, trended against the baseline. Assign one owner for the dashboard: a platform or DevEx lead, not a delivery manager with a target to hit.

## The one risk that eats all the others

Goodhart's Law. When a measure becomes a target it stops being a measure.

Any AI-usage dashboard visible to engineers becomes a leaderboard. Once ranked, people optimize for rank: more tokens, bigger PRs, more agentic runs, none of which is product value. This isn't a hypothetical about weak-willed engineers; it's what incentives do. The mitigation is structural, not cultural. The dashboards stay diagnostic, they stay at team level or above, and they are never an input to individual performance review. Say that out loud, in writing, before the first one ships.

## Do this next quarter

Take LOC, commit count and PR count out of the board pack. Put review queue time and 14-day rework in, per team, against the six months before rollout. If those two lines don't move the right way, your adoption percentage doesn't matter. If they do, you'll finally be able to say so with numbers a board will believe.

## Sources

1. Halkwinds: Software Engineering Productivity Benchmark Report 2026
2. METR: Early-2025 AI and experienced open-source developer productivity
3. TU Delft: Investigating autonomous agent contributions in the wild
4. GitClear AI Code Quality Research 2025
5. GitClear developer cohort analysis: AI tools attract top developers, but do they create them?
6. Veracode 2025 GenAI Code Security Report
7. Apiiro: 4x velocity, 10x vulnerabilities
8. 2025 DORA report
9. DORA research publications
10. Mingsheng Hong, AI Engineer World's Fair: From tokenmaxxing to trusted throughput
#
AI
#
Engineering Leadership
#
Developer Productivity
#
Metrics
#
DORA

Keep reading

Engineering Leadership
6
 min read

### Productivity Is Not Capability

AI raises an engineer's productivity faster than it raises their capability. Junior work was an accidental apprenticeship, and leaders have to design its replacement.

September 6, 2026
Read
AI Transformation
9
 min read

### When Code Becomes Cheap, Judgment Becomes the Craft

AI coding tools make implementation faster, but trusted software still depends on human judgment, verification, systems thinking, and accountability.

August 22, 2026
Read
Engineering Leadership
6
 min read

### Accountability Runs Both Ways

We raised the bar on what engineers are expected to deliver with AI. Most leadership teams never raised the bar on themselves.

July 28, 2026
Read