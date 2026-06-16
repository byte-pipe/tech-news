---
title: My Homelab AI Dev Platform • Rsgm's Blog
url: https://rsgm.dev/post/ai-dev-platform/
site_name: hnrss
content_file: hnrss-my-homelab-ai-dev-platform-rsgms-blog
fetched_at: '2026-06-16T12:37:27.172707'
original_url: https://rsgm.dev/post/ai-dev-platform/
author: Rsgm
date: '2026-06-15'
published_date: '2026-06-14T00:00:00.000Z'
description: Self-hosting OpenCode Web for GitOps style homelab changes.
tags:
- hackernews
- hnrss
---

I set up OpenCode Web UI with Git access to make my homelab easier to manage.
OpenCode pushes changes to Git, I approve the PRs, GitOps deploys the changes.
Best of all, OpenCode runs as a server with persistent coding sessions synced across devices.

I’ll share my homelab setup soon.
There are about a dozen docker compose stacks for the services that I manage.
I recently moved them to Arcane so I can manage/deploy them with GitOps.
The next logical step was using AI tooling to help maintain my services.

The first use that came to mind was using AI to help with container updates.
Previously, I would spend time looking up the release notes for each of the services, checking for any breaking changes, running the updates,
and manually checking each of the services for issues.
I would spend a few hours on this. Now I can read a summary of the release notes in a few minutes, making version upgrades easier and safer.
On top of that, I’ve used AI to add healthchecks to most of the containers to make it faster to spot issues.

## OpenCode

I mainly used Claude Code, but AI providers have been really squeezing the value out of customers recently through token limits,
so I took the opportunity to look into other options.
I wanted something that was vendor agnostic and supported by the major plugins.
I ended onOpenCode.
There are probably other decent coding environments, but this was my favorite of the ones I tried.

Then I found it ships with abuilt in webserver and web UI, which gave me an idea.

## AI Dev Platform

I set up a simple VM on the Truenas host with basic dev tooling and added OpenCode webserver as a systemd unit.
It’s a solid environment with a built in terminal, file browser, and git diffs,
as well as git worktree support for managing multiple coding sessions at the same time.
Plus, OpenCode had the best the question/answer popups in the mobile web UI that I’ve seen.

I gave OpenCode its own user on my Git server with dedicated SSH keys.
It can clone projects and push branches, but it cannot push straight to the deploy branch.

My workflow keeps the AI behind PR review. OpenCode writes the change and I merge it myself in a PR.
I think it’s cute, but more importantly, it keeps unreviewed code from getting deployed.

The VM has internet access and access to my Git server, but it cannot reach my actual services.
Because the blast radius is small, I am comfortable giving OpenCode root on the VM when it needs to install build tools or test dependencies.

I could see building this into a production developer platform. Ephemeral containers available to developers with preinstalled tooling,
access guardrails, and audit logs. But for me, it does what I need it to without too many moving parts.

## Workflow

My basic workflow is:

1. Plan out a feature or improvement in OpenCode (spec, implementation plan, and self-reviews)
2. I’ll test or verify changes if possible
3. Iterate with OpenCode on things I don’t like
4. OpenCode pushes changes to a feature branch
5. I’ll open a PR for this branch
6. I’ll merge the PR once I’m happy
7. GitOps takes over from there
- Arcane for docker service changes, GitOps plugin for Home Assistant config changes, Cloudflare Pages worker for blog changes

I migrated my services from Truenas to Arcane GitOps projects.
This was mainly to have git-backed storage for all the docker compose stacks I was running in Truenas previously.
I was surprised how well this worked in conjunction with adding OpenCode.
Being able to update the networking across all containers, for example, from my phone makes the sprawl much easier to manage.
Before it would take hours to comb through all of the compose stacks, tracing out network connectivity.
Now I can point OpenCode at the codebase with a goal, check the resulting PR changes, and merge.

The main missing piece is CI feedback.
On GitHub, I like pointing a coding agent at Actions logs so it can diagnose failing tests, linter errors, stack traces, and IaC plan changes.
This helps maintain a fast feedback loop for changes that unit tests don’t cover.

Forgejo makes that harder.
Forgejo Actions does not expose job logs through the public API.
There are undocumented APIs, but I would rather not build around those.

This setup lets me make home infra changes from any device without giving AI direct access to the services it’s changing.
I can start a change from my computer, review the PR from my phone, and let GitOps handle the deploy.