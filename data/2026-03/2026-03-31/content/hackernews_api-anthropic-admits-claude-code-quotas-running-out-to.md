---
title: Anthropic admits Claude Code quotas running out too fast • The Register
url: https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/
site_name: hackernews_api
content_file: hackernews_api-anthropic-admits-claude-code-quotas-running-out-to
fetched_at: '2026-03-31T19:26:42.879363'
original_url: https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/
author: samizdis
date: '2026-03-31'
description: Claude Code users hitting usage limits 'way faster than expected'
tags:
- hackernews
- trending
---

#### Devops

# Anthropic admits Claude Code users hitting usage limits 'way faster than expected'

 

## Unexpected quota drain prompts complaints, breaks automated workflows

Users of Claude Code, Anthropic's AI-powered coding assistant, are experiencing high token usage and early quota exhaustion, disrupting their work.

Anthropic has acknowledged the issue,statingthat "people are hitting usage limits in Claude Code way faster than expected. We're actively investigating... it's the top priority for the team."

A user on the Claude Pro subscription ($200 annually) said on the company's Discord forum that "it's maxed out every Monday and resets at Saturday and it's been like that for a couple of weeks... out of 30 days I get to use Claude 12."

The Anthropic forum on Reddit is buzzing with complaints. "I used up Max 5 in 1 hour of working, before I could work 8 hours,"saidone developer today. The Max 5 plan costs $100 per month.

There are several possible factors in the change. Last week, Anthropicsaidit was reducing quotas during peak hours, a change that engineer Thariq Shihipar said would affect around 7 percent of users, while also claiming that "we've landed a lot of efficiency wins to offset this."

March 28 was also the last day of a Claudepromotionthat doubled usage limits outside a six-hour peak window.

A third factor is that Claude Code may have bugs that increase token usage. A userclaimedthat after reverse engineering the Claude Code binary, they "found two independent bugs that cause prompt cache to break, silently inflating costs by 10-20x." Some users confirmed that downgrading to an older version helped. "Downgrading to 2.1.34 made a very noticeable difference,"saidone.

Thedocumentationon prompt caching says that the cache "significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements." That said, the cache has only a five-minute lifetime, which means stopping for a short break, or not using Claude Code for a few minutes, results in higher costs on resumption.

* Contracts are in C++26 despite disagreement over their value
* Linear moves sideways to agentic AI as CEO declares issue tracking dead
* JetBrains shifts to agentic dev with Central, retires pair programming
* Mozilla introduces cq, describing it as 'Stack Overflow for agents'

Developers can upgrade the cache lifetime to one hour but "1-hour cache write tokens are 2 times the base input tokens price," the documentation states. A cache read token is 0.1 times the base price, so this is a key area for optimization.

Anthropic does not state the exact usage limits for its plans. For example, the Pro plan promises only "at least five times the usage per session compared to our free service." The Standard Team plan promises "1.25x more usage per session than the Pro plan." This makes it hard for developers to know what their usage limits are, other than by examining their dashboard showing how much quota they have consumed.

Problems like this are not unusual. Earlier this month, users of Google Antigravity wereprotestingabout similar issues.

Bugs aside, what we are seeing is an implicit negotiation between users and providers over what is an acceptable pricing and usage model for AI development. Users want to control costs and providers need to make a profit. There is also a disconnect between vendor marketing that urges developers to insert AI into every process, including in some cases automated workflows, and a quota system that can cause AI tools to stop responding.

"For folks running Claude Code in automated workflows: rate-limit errors need to be caught explicitly – they look like generic failures and will silently trigger retries. One session in a loop can drain your daily budget in minutes,"observedone user. ®

 

Get our
 
Tech Resources

Share

#### More about

* Anthropic
* Claude
* Developer

More like these

×

### More about

* Anthropic
* Claude
* Developer

### Narrower topics

* API
* Git
* Programming Language
* Software bug

### Broader topics

* Large Language Model

#### More about

Share

#### More about

* Anthropic
* Claude
* Developer

More like these

×

### More about

* Anthropic
* Claude
* Developer

### Narrower topics

* API
* Git
* Programming Language
* Software bug

### Broader topics

* Large Language Model

#### TIP US OFF

Send us news