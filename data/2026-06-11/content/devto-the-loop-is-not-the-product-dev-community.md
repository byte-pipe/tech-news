---
title: The Loop Is Not the Product - DEV Community
url: https://dev.to/dannwaneri/the-loop-is-not-the-product-466d
site_name: devto
content_file: devto-the-loop-is-not-the-product-dev-community
fetched_at: '2026-06-11T12:23:38.260322'
original_url: https://dev.to/dannwaneri/the-loop-is-not-the-product-466d
author: Daniel Nwaneri
date: '2026-06-09'
description: 'A tweet landed on my timeline from Peter Steinberger — OpenClaw founder, now at OpenAI: "Here''s... Tagged with ai, webdev, discuss, productivity.'
tags: '#discuss, #ai, #webdev, #productivity'
---

AI compute costs vs human labor

A tweet landed on my timeline from Peter Steinberger — OpenClaw founder, now at OpenAI:

"Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."

He's right about the mechanic. He's not asking the harder question.

Before agents, we had cron jobs.

0 2 * * * ./process_reports.sh

That's the whole contract. Run at 2am. Do what you said. Fail loudly or silently. Nobody wrote a think piece about cron jobs disrupting knowledge work. Nobody raised a seed round on a well-tuned crontab.

But structurally? A cron job is a loop that prompts a process on a schedule. It just had the decency to be honest about what it was.

Cron jobs → Airflow → event-driven pipelines → agents. Each layer added adaptability and removed legibility. Cron is maximally legible. You can read the entire logic in one line. An agent doing "the same job" is a probability distribution with a system prompt and a credit card attached.

Now we've gone further. We have multi-agent systems. Specialist agents. Orchestrator agents that decide which specialist to call. Verification agents that check the output. Agents that self-correct when they fail.

And companies are quietly running the math and going pale.

Uber burned through its entire annual AI budget in four months. An NVIDIA vice president said publicly that AI computing costs now exceed employee labor costs. The FinOps Foundation's 2026 State of FinOps report found 73% of enterprises say AI costs exceeded original projections. Not a few bad actors. Not early adopters who didn't know better. Seventy-three percent.

The mechanism has a name now: the agentic loop multiplier. A simple query in 2023 cost $0.04 per interaction. A multi-step orchestrated agent workflow in 2026 costs $1.20 — thirty times higher. Gartner puts the range at 5-30x more tokens per task than the chatbot pilots that justified the budget. The ROI calculations that approved the deployment assumed chatbot-level consumption. The invoices arrived with agent-level reality.

A mid-level developer runs $80-120k. Fully loaded with benefits and overhead, maybe $250k. That sounds expensive until the token bill lands.

The human compounds. They learn your codebase, your culture, your shortcuts. They remember the decision you made last quarter and why. The agent starts fresh every session. Every morning you're paying for the same orientation meeting. Context reconstruction — re-reading docs, re-loading state, re-establishing what "done" means — isn't free. You're billing for memory the human already had.

The demo never shows you this. The demo is a single agent, single task, cherry-picked problem, running for 90 seconds while someone claps at a conference. The production reality is a fleet burning tokens on retries, tool calls that fail and get reattempted, coordination overhead between agents nobody budgeted for.

You've built a bureaucracy. A token-denominated bureaucracy with no union and no lunch breaks and no salary cap.

Back to Steinberger's tweet.

"Designing loops that prompt your agents" is a real architectural upgrade over manual prompting. If you're still narrating every step to an agent like you're dictating to a secretary, the loop is the upgrade. Prompts from state — test results, diffs, error logs — not from you typing.

But designing the loop is just procrastination with better posture if there's no customer at the end of it.

Because someone still has to decide what the loop optimizes for. What "done" looks like. When to break. What counts as a failure worth stopping for. That's not automation — that's system design with higher stakes, because now the mistakes compound before anyone sees them.

And "designing loops" is genuinely hard in a way prompting isn't. Most people who can write a good prompt cannot design a feedback loop with appropriate exit conditions, cost governors, and human checkpoints. The tweet makes the upgrade sound like switching from tabs to spaces. It's closer to switching from writing functions to designing distributed systems.

What I want to know: what breaks in the loop that a prompt would have caught? Every abstraction hides something. Prompting hides scale. Loops hide drift. At some point the agent has been running for six hours optimizing a metric nobody remembers choosing, and the loop is beautiful and the output is garbage.

Here's what nobody in the agent hype cycle wants to sit with:

The old model had a forcing function built in. You shipped, a human used it, something broke, you fixed it. Feedback was physical. A user opened a ticket. A client called. Reality interrupted the loop.

Agents don't have that governor. The loop is the product. And when the loop is the product, you can optimize indefinitely without ever confronting whether the output matters.

Token burn becomes a proxy for progress. Iteration velocity becomes a stand-in for value creation. The agent looks productive because it never stops — but stopping is exactly what would force the question.

Autonomy used to mean delegated judgment. You trust someone to make calls because they understand the goal and can feel when something's off. What most agents have is delegated execution. They can do the steps. They have no stake in the outcome, no access to the silence that follows a bad result, no way to know the customer churned three weeks later because the feature was technically correct and completely wrong.

Automate the tedious middle of a known, stable process. Data pipeline, alert triage, code linting, content reformatting. Stuff where the definition of done is actually defined. That's real. That's useful. A cron job with taste.

The inflated version — the one burning the tokens — is the agent as a substitute for product thinking. If you don't know what to build, an agent that builds constantly feels like momentum.

It isn't. It's expensive randomness with good logging.

Consider Spotify.

A company that built its entire brand on one rule: only ship what users ask for. Feature requests drove the roadmap. That's it.

Then AI became mainstream and the calculus changed publicly. Spotify's workforce went from 7,721 employees at the start of 2024 to 7,242 by Q3 — shrinking every quarter while revenue grew 19% year over year. Their filings note it plainly: profitability driven by "lower personnel and related costs." They're doing more with fewer people. The numbers look good on a slide.

But nobody's asking the follow-up question. The features that built Spotify's loyalty — Discover Weekly — came from people who understood the product, the listener, the culture of music discovery. Accumulated judgment. What does the agent fleet ship? What user asked for it? What happens when "only build what users want" gets replaced by "ship what the loop produces"?

We don't know yet. The invoices look better. The product debt is still accumulating.

I builtseo-agent— an open-source SEO audit agent using Python, Browser Use, Claude API, and Playwright.

I could leave it burning tokens 24/7. I didn't. Not because of the money. Because I couldn't answer the basic question: what would it actually be doing?

I wired a cron job to run it on schedule. It analyzes logs. It surfaces what's broken. Then I look at the output, decide what matters, and go into my codebase with Claude Code to write the fix and the test. The agent handles the tedious middle. I handle the judgment at the edges.

Call that old fashioned. I'd call it honest.

The loop runs. But it runs to me. Not into a void.

My Bookmark Brain — a RAG system trained on 50,000 of my own X bookmarks — flagged this pattern when I showed it the tweet:

"Designing the loop is just procrastination with better posture if there's no customer at the end of it. Automated nobody is still nobody."

The stack was never the problem. It was always the most comfortable place to hide from the problem.

Cron jobs ran quietly and failed loudly. Agents run loudly and fail quietly. The failure is just spread across enough API calls that the bill arrives before the reckoning does.

Design better loops. Ship to someone who asked.

This article used AI tools for research verification and editing.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (27 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse