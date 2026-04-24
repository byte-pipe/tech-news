---
title: Anthropic's Most Dangerous Model Just Got Accessed by People Who Weren't Supposed to Have It - DEV Community
url: https://dev.to/om_shree_0709/anthropics-most-dangerous-model-just-got-accessed-by-people-who-werent-supposed-to-have-it-14dn
site_name: devto
content_file: devto-anthropics-most-dangerous-model-just-got-accessed
fetched_at: '2026-04-25T08:21:40.078069'
original_url: https://dev.to/om_shree_0709/anthropics-most-dangerous-model-just-got-accessed-by-people-who-werent-supposed-to-have-it-14dn
author: Om Shree
date: '2026-04-22'
description: Anthropic built a model so dangerous they refused to release it publicly. Then a Discord group got in... Tagged with ai, security, discuss, claude.
tags: '#discuss, #ai, #security, #claude'
---

Accessed via predictable URL patterns

Anthropic built a model so dangerous they refused to release it publicly. Then a Discord group got in anyway.

## The Model They Wouldn't Ship

Claude Mythos Previewis Anthropic's most capable model to date for coding and agentic tasks.AnthropicBut it was never meant to reach the public. During testing, Mythos improved to the point where it mostly saturated existing cybersecurity benchmarks, prompting Anthropic to shift focus to novel real-world security tasks — specifically zero-day vulnerabilities, bugs that were not previously known to exist.Anthropic

What they found was stark. Mythos Preview had already identified thousands of zero-day vulnerabilities across critical infrastructure — many of them critical — in every major operating system and every major web browser.AnthropicIn one documented case, Mythos fully autonomously identified and exploited a 17-year-old remote code execution vulnerability in FreeBSD that allows anyone to gain root on a machine running NFS. No human was involved in either the discovery or exploitation of this vulnerability after the initial request to find the bug.Anthropic

This is why the model never went public.

## Project Glasswing: The Controlled Release

Announced on April 7, Mythos was deployed as part of Anthropic's "Project Glasswing," a controlled initiative under which select organizations are permitted to use the unreleased Claude Mythos Preview model for defensive cybersecurity.Yahoo!

Launch partners included Amazon Web Services, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks. Access was also extended to over 40 additional organizations that build or maintain critical software infrastructure.AnthropicThe logic was clear: get defenders ahead of the curve before the capabilities proliferate to actors who won't use them carefully.

Claude Mythos Preview is available to Project Glasswing participants at $25/$125 per million input/output tokens, accessible via the Claude API, Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry. Anthropic committed $100M in model usage credits to cover Project Glasswing throughout the research preview.Anthropic

The perimeter was tight by design. The news today is that it didn't hold.

## How the Discord Group Got In

A "private online forum," the members of which have not been publicly identified, managed to gain access to the tool through a third-party vendor. The unauthorized group tried a number of different strategies to gain access to the model, including using "access" enjoyed by a person currently employed at a third-party contractor that works for Anthropic.TechCrunch

Members of the group are part of a Discord channel that seeks out information about unreleased AI models. The group has been using Mythos regularly since gaining access to it, and provided evidence to Bloomberg in the form of screenshots and a live demonstration of the software.TechCrunch

The method they used to find the endpoint is particularly revealing. The group, which gained access on the very same day Mythos was publicly announced, "made an educated guess about the model's online location based on knowledge about the format Anthropic has used for other models."TechCrunchThis wasn't a sophisticated breach — it was pattern recognition applied to a known naming convention. The group reportedly described themselves as being interested in exploring new models, not causing harm.

Anthropic said it is investigating the claims and, so far, has seen no sign that its own systems were affected — the allegation points to possible misuse of access outside Anthropic's core network, not a confirmed breach of the company's internal defenses.Prism News

## Why This Is a Bigger Deal Than It Looks

The immediate reassurance — no core systems compromised, the group wasn't malicious — is accurate but beside the point. The problem isn't what this specific group did. It's what this incident reveals about the entire premise of Project Glasswing.

Anthropic's controlled release strategy rests on the assumption that access can be meaningfully gated through vendor relationships. A small group of unauthorized users reportedly accessed Mythos on the same day Anthropic announced limited testingPrism News— meaning the access controls failed within hours of the first public announcement, before most Glasswing partners had even begun their work. If the group could guess the model's endpoint from Anthropic's known URL patterns, so can threat actors with more resources and worse intentions.

There's also a pattern here worth naming. This is the third significant information control failure at Anthropic in recent weeks. The Claude Code source leak in March exposed 512,000 lines of unobfuscated TypeScript via a missing .npmignore entry. Before that, a draft blog post describing Mythos as "by far the most powerful AI model" ever built at Anthropic was left in a publicly accessible data store. That March 26 leak of draft materials — which Anthropic said resulted from human error in its content-management configuration — was actually Mythos's first public exposure.Prism News

Then there's the government subplot. The National Security Agency is using Mythos Preview despite top officials at the Department of Defense — which oversees the NSA — insisting Anthropic is a "supply chain risk." The department moved in February to cut off Anthropic and force its vendors to follow suit. The military is now broadening its use of Anthropic's tools while simultaneously arguing in court that using those tools threatens U.S. national security.AxiosMeanwhile, CISA — the agency whose entire mandate is critical infrastructure protection — reportedly does not have access to the model.Axios

The entity designed to defend critical systems can't get in. A Discord group can.

## What Anthropic Actually Said

"We're investigating a report claiming unauthorized access to Claude Mythos Preview through one of our third-party vendor environments," an Anthropic spokesperson said. The company found no evidence that the supposedly unauthorized activity impacted Anthropic's systems at all.TechCrunch

That's a factually careful statement. It's also a familiar shape: acknowledge the narrow, deny the broader implication. Anthropic has been here before.

## The Vendor Problem Nobody Wants to Solve

The deeper structural issue is that enterprise AI deployments at frontier capability levels require trust chains that extend across dozens of organizations. Anthropic's 40-organization Glasswing rollout means 40 distinct security postures, 40 sets of contractors, and 40 potential lateral entry points for anyone who knows what they're looking for.

Anthropic said it does not plan to make Mythos Preview generally available, but its eventual goal is to enable users to safely deploy Mythos-class models at scale — for cybersecurity purposes, but also for the myriad other benefits that such highly capable models will bring.Simon WillisonThat goal is legitimate. But reaching it requires solving vendor access governance at a level the industry hasn't had to reckon with before. This incident is an early indication of what the stakes look like when the effort falls short.

A model capable of finding zero-days in every major operating system and browser has now been accessed by people outside the intended perimeter. The question isn't whether the Discord group caused harm. It's whether the perimeter can hold when the people on the other side are actually trying.

The line between "interested in playing around" and "interested in breaking things" isn't enforced by intent. It's enforced by access controls. Anthropic's have now failed twice in the same month.

Follow for more coverage on MCP, agentic AI, and AI infrastructure.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (16 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse