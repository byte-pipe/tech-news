---
title: GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026 - GitHub Changelog
url: https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/
site_name: hnrss
content_file: hnrss-github-copilot-code-review-will-start-consuming-gi
fetched_at: '2026-04-29T06:00:45.505031'
original_url: https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/
date: '2026-04-28'
description: GitHub Copilot code review will start consuming GitHub Actions minutes
tags:
- hackernews
- hnrss
---

Back to changelog

Developers and engineering teams worldwide use GitHub Copilot for high-quality, agent-powered code reviews on every pull request. We understand that any change is significant to our customers, especially when it relates to billing, so we are sharing this update early to help you plan and prepare. The sections below outline what is changing, why, and how to plan accordingly.

## What’s changing

Last month, we shared how GitHub Copilot code review runs on agentic tool-calling architecture, allowing the code review agent to pull in broader repository context and produce more relevant feedback on each pull request. That agentic architecture runs on GitHub Actions using GitHub-hosted runners (Note: GitHub Copilot code review also supports self-hosted runners and GitHub-hosted larger runners which are billed at different rates than standard GitHub-hosted runners.)

Starting June 1, 2026, each Copilot code review will be billed in two ways:

* All Copilot usage (including code reviews) will be billed as AI Credits under the new usage-based billing model (see the usage-based billing announcement for additional details).
* GitHub Actions minutes will be consumed from your existing plan entitlement for each review that is run on private repositories, with any usage beyond your included minutes billed at standard GitHub Actions rates. You or your organization administrator (for GitHub Teams and Enterprise) can use budgets to manage spending on GitHub Actions. There are no changes to public repositories, where Actions minutes remain free.

This change applies to the following plans:

* GitHub Copilot Pro
* GitHub Copilot Pro+
* GitHub Copilot Business
* GitHub Copilot Enterprise

This includes Copilot code reviews from non-licensed users and billed viadirect org billing.

## When it takes effect

This change takes effect onJune 1, 2026. Until that day, Copilot code review usage will continue to draw only from your existing Copilot premium request unit (PRU) allowance and will not consume GitHub Actions minutes.

## What you need to do

To prepare for the billing change, we recommend the following.

### Review billing and usage

1. Review your current GitHub Actions usage.Billing managers can view minute consumption and entitlements in your account or organization billing settings.
2. Check your budget on spending limits.Confirm that your personal or organizational budgetfor Actions aligns with your expected usage. You or your organization administrators (for GitHub Teams and Enterprise) can adjust spending limits for GitHub Actions at any time.
3. Monitor your Copilot and Actions usage over timeviaGitHub Copilot usage metrics,GitHub Actions metrics, andBilling Usage Report.
4. Review the usage-based billing announcementto understand how Copilot usage itself is being measured going forward.
5. Share this update with your billing administrators and engineering leadsso they are aware of the new usage pattern before June 1, 2026.

### Review runner settings

* No additional setup is required if you already haveGitHub-hosted Runners enabled on your repository.
* If you would like to customize your GitHub Hosted Runner environment, seeUpgrade to larger GitHub-hosted Runners.
* Self-hosted Runners setupis available.

Learn more about these changes inour documentation.

And join the discussion withinGitHub Community.

## Related Posts

### Apr.27Retired

					Copilot Student GPT-5.3-Codex removal from model picker				

copilot

### Apr.27Improvement

					Copilot cloud agent starts 20% faster with Actions custom images				

actions

copilot

...

				+1			

### Apr.24Improvement

					Notice about upcoming new format for GitHub App installation tokens				

actions

application security

client apps

copilot

...

				+3			

### Apr.24Release

					GPT-5.5 is generally available for GitHub Copilot				

copilot

### Apr.24Improvement

					Inline agent mode in preview and more in GitHub Copilot for JetBrains IDEs				

copilot

### Apr.23Improvement

					Copilot Chat improvements for pull requests				

copilot

### Apr.23Release

					Copilot cloud agent fields added to usage metrics				

account management

copilot

enterprise management tools

...

				+2			

### Apr.23Improvement

					Better debugging with GitHub Copilot on the web				

copilot

### Apr.23Release

					View and manage agent sessions from issues and projects				

copilot

projects & issues

...

				+1			

 

## Subscribe to our developer newsletter

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

						Enter your email
*

						Subscribe					

By submitting, I agree to let GitHub and its affiliates use my information for personalized communications, targeted advertising, and campaign effectiveness. See theGitHub Privacy Statementfor more details.

				Back to top