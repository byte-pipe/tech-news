---
title: 'Hours, Not Weeks: How AI Rewrote the Clock of Software Security - DEV Community'
url: https://dev.to/james_anderson_h/security-changed-with-ai-and-small-teams-are-falling-behind-5ebg
site_name: devto
content_file: devto-hours-not-weeks-how-ai-rewrote-the-clock-of-softwa
fetched_at: '2026-10-29T20:59:58.563570'
original_url: https://dev.to/james_anderson_h/security-changed-with-ai-and-small-teams-are-falling-behind-5ebg
author: James Anderson
date: '2026-10-24'
description: The third week of October 2026 was a rough one for anyone who runs software on the internet. Two... Tagged with security, ai, startup, discuss.
tags: '#discuss, #security, #ai, #startup'
---

Highlights the impossible burden on micro-teams

The third week of October 2026 was a rough one for anyone who runs software on the internet.

Two critical bugs in PHP, nicknamed PHP2Shell, were found by security teams using frontier AI models. Estimates said they touched a huge share of the web. Governments told organisations to patch immediately, and plenty of people simply pulled their servers offline. In the same few days, LiteLLM had a malicious release pushed to PyPI (for the second time this year), Railway disclosed that attackers had gotten into customer environment variables, GitLab shipped fixes for maximum-severity bugs, and a handful of Linux kernel vulnerabilities got posted to the wrong mailing list.

Drew Silcock wrote a great roundup of all of it inIs this the new cyber normal?, and it's worth reading in full.

But after going through it, the thing that stuck with me wasn't any particular bug. It was a simpler thought: who is actually supposed to deal with all this when your entire company is four people?

## The clock got shorter

Security used to have a rhythm. A vulnerability got announced, a patch came out, and you had some time. Maybe days, sometimes weeks, before anyone figured out how to actually exploit it. "We'll patch it this week" was a reasonable plan.

That rhythm is gone. Today, the moment a security patch is published, people point AI agents at the code. The agent reads through the changes, spots what looks like a security fix, works backwards to the hole it closes, and helps build an exploit. What used to take a skilled researcher weeks can now happen in hours.

With PHP2Shell, attacks were reportedly happening before the official patch was even available. "This week" isn't a plan anymore. "Today" barely is.

## Attacking got cheap

Here's the part that changes everything. Finding a serious bug and turning it into a working attack used to require rare skills and a lot of time. That made it expensive, and expensive things happen less often.

Now an attacker can throw an AI model at a codebase and see what comes out. A lot of it is junk. AI produces plenty of "exploits" that don't actually work. But attackers don't need everything to work. They need one thing to work. When trying costs almost nothing, you can afford to try a thousand times.

## Defending didn't get cheap

On the other side, almost nothing got cheaper.

When a critical bug drops, somebody still has to read the advisory, figure out whether you're affected, check which of your services use the vulnerable thing, test the patch, deploy it, and then dig through logs to see if anyone got in before you fixed it. If you use AI to scan your own code first, great, but that costs money too, and every bug it finds is a bug someone now has to fix.

AI made finding problems cheaper for everyone. It didn't make fixing them cheaper for anyone. And the attacker only has to find. You have to fix.

## This is where size starts to matter

A big company handles a week like that with a security team, an on-call rotation, incident playbooks, and people whose literal job is to drop everything and respond. It's painful for them too, but they're built for it.

A small team isn't. In a four-person startup, the person who handles security is usually also the person who handles deployments, the database, customer support tickets, and the feature that was supposed to ship Friday. There's no rotation. There's just whoever happens to be awake.

And when the advice is "take your servers offline until you patch," the cost hits differently. A large company can survive a day of downtime. A small product with a few hundred paying customers might lose some of them for good.

## You inherit everyone else's problems

Small teams don't build everything themselves. They can't. They stand on a stack of frameworks, packages, hosting platforms, and AI tools, all written by someone else.

That's normally a strength. It's how a tiny team ships something real. But it also means that when one of those pieces gets compromised, the problem becomes yours instantly. You didn't write the LiteLLM backdoor, but if you installed that release, your credentials might be gone. You didn't misconfigure Railway, but if your secrets lived there, you now have to rotate every one of them.

For a big company, that's a ticket for the security team. For a small team, it's an entire day of product work gone, spent cleaning up a mess you didn't make.

## The tools we adopted to move faster

There's an irony here. Small teams have been some of the fastest to adopt AI tools, because AI promises exactly what they need: more output from fewer people.

But every one of those tools comes with something attached. Another API key. Another dependency. Another service with access to your code or your data. One of the incidents that week, a data leak at a database company, reportedly exposed API keys for several AI providers that had been pasted into internal tickets. Keys spread quietly, and every one of them is something an attacker would love to find.

The tools that help small teams keep up are also handing attackers more things to go after.

## Falling behind isn't the same as not caring

I don't think small teams are ignoring security. Most developers I know care about it a lot. The problem is that the math changed underneath them.

Defending at the new speed assumes things a small team doesn't have: people on call around the clock, budget for scanning tools, time to audit every dependency, room to absorb downtime. When attacks got faster and cheaper but defense stayed slow and expensive, the gap didn't hit everyone equally. It landed hardest on the people with the fewest resources.

## I don't have a neat answer

Maybe this is a temporary spike. Maybe AI is just clearing out years of old bugs all at once, and things will calm down once the backlog is gone. Or maybe this is simply what security looks like now.

Either way, it feels like we're in a period where the cost of defending software is rising quickly, and small teams are the ones feeling it first.

If you're on a small team, I'd genuinely like to know how that week went for you. Did you patch in time, pull things offline, or only find out afterwards?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (45 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse