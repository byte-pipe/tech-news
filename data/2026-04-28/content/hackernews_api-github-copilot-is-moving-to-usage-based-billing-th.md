---
title: GitHub Copilot is moving to usage-based billing - The GitHub Blog
url: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
site_name: hackernews_api
content_file: hackernews_api-github-copilot-is-moving-to-usage-based-billing-th
fetched_at: '2026-04-28T06:00:18.977444'
original_url: https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
author: Mario Rodriguez
date: '2026-04-28'
published_date: '2026-04-27T15:58:22+00:00'
description: Starting June 1, your Copilot usage will consume GitHub AI Credits.
tags:
- hackernews
- trending
---

Mario Rodriguez
·
@mariorod
 

			April 27, 2026		

|

				4 minutes			

* Share:

TL;DR:Today, we are announcing that all GitHub Copilot plans will transition to usage-based billing onJune 1, 2026.

Instead of counting premium requests, every Copilot plan will include a monthly allotment ofGitHub AI Credits, with the option for paid plans to purchase additional usage. Usage will be calculated based on token consumption, including input, output, and cached tokens, using the listed API rates for each model.

This change aligns Copilot pricing with actual usage and is an important step toward a sustainable, reliable Copilot business and experience for all users.

To help customers prepare, we are also launching apreview billexperience in early May, giving users and admins visibility into projected costs before the June 1 transition. This will be available to users via their Billing Overview page when they log in to github.com.

## Why we’re making this change

Copilot is not the same product it was a year ago.

It has evolved from an in-editor assistant into an agentic platform capable of running long, multi-step coding sessions, using the latest models, and iterating across entire repositories. Agentic usage is becoming the default, and it brings significantly higher compute and inference demands.

Today, a quick chat question and a multi-hour autonomous coding session can cost the user the same amount. GitHub has absorbed much of the escalating inference cost behind that usage, but the current premium request model is no longer sustainable.

Usage-based billing fixes that. It better aligns pricing with actual usage, helps us maintain long-term service reliability, and reduces the need to gate heavy users.

## What’s changing

StartingJune 1, premium request units (PRUs) will be replaced byGitHub AI Credits.

Credits will be consumed based on token usage, including input, output, and cached tokens, according to the published API rates for each model.

A few important details:

* Base plan pricing is not changing.Copilot Pro remains $10/month, Pro+ remains $39/month, Business remains $19/user/month, and Enterprise remains $39/user/month.
* Code completions and Next Edit suggestions remain includedin all plans and do not consume AI Credits.
* Fallback experiences will no longer be available.Today, users who exhaust PRUs may fall back to a lower-cost model and continue working. Under the new model, usage will instead be governed by available credits and admin budget controls.
* Copilot code review will also consume GitHub Actions minutes, in addition to GitHub AI Credits. These minutes are billed at the same per-minute rates as other GitHub Actions workflows.

Last week,we also rolled out temporary changesto Copilot Individual plans, including Free, Pro, Pro+, and Student, and paused self-serve Copilot Business plan purchases. These were reliability and performance measures as we prepare for the broader transition to usage-based billing. We will loosen usage limits once usage-based billing is in effect.

## What this means for individuals

Copilot Pro and Pro+ monthly subscriptions will include monthly AI Credits aligned to their current subscription prices:

* Copilot Pro:$10/month, including $10 in monthly AI Credits
* Copilot Pro+:$39/month, including $39 in monthly AI Credits

Users on a monthly Pro or Pro+ plan will automatically migrate to usage-based billing on June 1, 2026.Users on annual Pro or Pro+ plans will remain on their existing plan with premium request-based pricing until their plan expires.Model multipliers will increase on June 1 (see table)for annual plan subscribersonly. At expiration, they will transition to Copilot Free with the option to upgrade to a paid monthly plan. Alternatively, they may convert to a monthly paid plan before their annual plan expires, and we will provide prorated credits for the remaining value of their annual plan.

## What this means for businesses and enterprises

Copilot Business and Copilot Enterprise monthly seat pricing remains unchanged:

* Copilot Business:$19/user/month, including $19 in monthly AI Credits
* Copilot Enterprise:$39/user/month, including $39 in monthly AI Credits

To support the transition, existing Copilot Business and Copilot Enterprise customers will automatically receive promotional included usage for June, July, and August:

* Copilot Business: $30 in monthly AI Credits
* Copilot Enterprise: $70 in monthly AI Credits

We are also introducing pooled included usage across a business, which helps eliminate stranded capacity. Instead of each user’s unused included usage being isolated, credits can be pooled across the organization.

Admins will also have new budget controls. They will be able to set budgets at the enterprise, cost center, and user levels. When the included pool is exhausted, organizations can choose whether to allow additional usage at published rates or cap spend.

## The bottom line

Plan prices aren’t changing. You’ll have full control over what you spend, tools to track your usage, and the option to purchase more AI Credits if and when you need them.

If you have questions, visit our documentation forindividualsand forbusinesses and enterprises, and ourFAQ and related discussion.

## Written by

Mario Rodriguez leads the GitHub Product team as Chief Product Officer. His core identity is being a learner and his passion is creating developer tools—so much so that he has spent the last 20 years living that mission in leadership roles across Microsoft and GitHub. Mario most recently oversaw GitHub’s AI strategy and the GitHub Copilot product line, launching and growing Copilot across thousands of organizations and millions of users. Mario spends time outside of GitHub with his wife and two daughters. He also co-chairs and founded a charter school in an effort to progress education in rural regions of the United States.

## Related posts

 

Company news
 

### Changes to GitHub Copilot Individual plans

We’re making these changes to ensure a reliable and predictable experience for existing customers.

 

Company news
 

### Bringing more transparency to GitHub’s status page

Changes to the status page will provide more specific data, so you’ll have better insight into the overall health of the platform.

 

News & insights
 

### Developer policy update: Intermediary liability, copyright, and transparency

We’re sharing recent policy updates that developers should know about, updating our Transparency Center with the full year of 2025 data, and looking to what’s ahead.

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

 

Your email address

*

Your email address

Subscribe

							Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the 
GitHub Privacy Statement
 for more details.						

Subscribe