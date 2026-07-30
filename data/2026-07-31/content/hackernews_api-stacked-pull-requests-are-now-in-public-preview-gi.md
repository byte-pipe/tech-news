---
title: Stacked pull requests are now in public preview - GitHub Changelog
url: https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/
site_name: hackernews_api
content_file: hackernews_api-stacked-pull-requests-are-now-in-public-preview-gi
fetched_at: '2026-07-31T06:00:49.933195'
original_url: https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/
author: tomzorz
date: '2026-07-31'
description: Stacked PRs are now live on GitHub
tags:
- hackernews
- trending
---

Back to changelog

Stacked pull requests break large changes into small, reviewable pull requests. They’re an ordered series of pull requests that each represent focused layers of your change. With stacks, you can independently review and check each pull request, then merge everything together in one click. No more opening a single large pull request that takes forever to review, or splitting work across multiple branches you have to keep manually rebasing.

“We’ve been using GitHub stacked PRs for Next.js for the past few months. It has helped us introduce smaller individual changes while shipping larger features, making it easier to review PRs. – Tim Neutkens, NextJS lead, Vercel”

With stacked pull requests, teams can:

* Keep large changes movingby reviewing short, narrowly scoped pull requests in parallel.
* Maintain quality across every layerby using focused pull request reviews alongside existing branch protections to protectmain.
* Merge one, some, or allby landing an entire stack altogether or individual layers one at a time.

And because stacked pull requests are built into GitHub, your existing reviews, checks, and merge requirements all work out of the box.

“The new Github Stacked PRs preview is incredible. Landing 5 stacked PRs directly to a merge queue all at once! A+++! This removes so much friction (and the gh cli tools + agent skill help a ton)” – John Resig, creator, jQuery

## Get started with the CLI extension

Install the CLI extension and create your first stack in under a minute:

gh extension install github/gh-stack

## Create stacks from your terminal or github.com

Work with stacks on github.com, the GitHub CLI, the GitHub mobile app, or with a coding agent such as GitHub Copilot using the gh-stack skill. Start with a branch and pull request for your first change. Then add branches and pull requests on top of it; each pull request targets the layer below it.

## Review each layer independently

Open any pull request in the stack to review only the diff for that specific layer. Use the stack map at the top of the pull request to see how the change you’re reviewing fits into the larger work. You and your teammates can each review different layers in parallel without blocking further work.

“AI has made TED’s developers dramatically more productive, but that created a new bottleneck: PRs were growing large enough that reviewers were struggling. Stacked PRs help to solve that. By breaking large changes into small, dependency-ordered pieces, review happens in smaller logical chunks – not just faster PR reviews, but more accurate ones. Stacked PRs tighten our feedback loop and help get stable code to ted.com faster.” – Andy Merryman, CTO, TED

## Merge everything in a single click

Merge the latest ready pull request to land it and every unmerged layer below it in one single operation. To land part of a stack, merge one or more lower layers—the pull requests above it stay open and automatically rebase and retarget. Your existing branch protections and required checks still govern what reachesmain.

“A big change used to mean one giant PR nobody wanted to review. Now it’s a stack of small ones reviewers can actually follow, and the whole stack merges in one shot. It stopped feeling like a tool on top of GitHub and started feeling like GitHub.” – Mayank Saini, connectivity engineer, WHOOP

## Find out more and share your feedback

Stacked pull requests are rolling out in public preview to all repositories over the coming days.Merge queuesupport for stacked pull requests is rolling out progressively over the coming weeks.

For more information, check out thestacked pull requests documentation, and share your feedback with us in thestacks discussion.

## Related Posts

### Jul.23Release

					Agent automation controls in GitHub Issues in public preview				

collaboration tools

copilot

projects & issues

...

				+2			

### Jul.22Retired

					Upcoming GHES change impacting uploading support bundles				

collaboration tools

### Jul.16Release

					Repository admins can archive pull requests				

collaboration tools

### Jul.09Release

					New pull requests dashboard is now generally available				

collaboration tools

### Jun.30Improvement

					Releases: Sidebar navigation and per-asset download counts				

collaboration tools

### Jun.29Improvement

					Restrict issue creation to collaborators only				

collaboration tools

### Jun.25Improvement

					GitHub Copilot for Jira is now generally available				

collaboration tools

copilot

...

				+1			

### Jun.18Improvement

					Copilot-authored pull requests now included in author searches				

client apps

collaboration tools

copilot

...

				+2			

### Jun.18Improvement

					Repository switcher generally available in global navigation				

collaboration tools

 

## Subscribe to our developer newsletter

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

						Enter your email
*

						Subscribe					

By submitting, I agree to let GitHub and its affiliates use my information for personalized communications, targeted advertising, and campaign effectiveness. See theGitHub Privacy Statementfor more details.

				Back to top