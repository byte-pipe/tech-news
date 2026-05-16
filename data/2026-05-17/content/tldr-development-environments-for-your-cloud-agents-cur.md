---
title: Development environments for your cloud agents · Cursor
url: https://cursor.com/blog/cloud-agent-development-environments
site_name: tldr
content_file: tldr-development-environments-for-your-cloud-agents-cur
fetched_at: '2026-05-17T06:00:59.783163'
original_url: https://cursor.com/blog/cloud-agent-development-environments
author: Nick Bradford
date: '2026-05-17'
description: Cloud agents are easier to parallelize than local agents, continue working when your laptop is closed, and can run autonomously in response to programmatic triggers.
tags:
- tldr
---

Blog
 
/
 
product

Cloud agents are easier to parallelize than local agents, continue working when your laptop is closed, and can run autonomously in response to programmatic triggers.

But agents are only as capable as the environments they run in. An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work.

To take engineering tasks from start to finish, cloud agents need a development environment similar to the setup on your laptop: cloned repositories, installed dependencies, credentials for internal toolchains, and access to build systems. Effective development environments give agents full context on your codebase and organization, so they can test and verify their work.

Today we're shipping new tools for configuring cloud agent development environments. Cursor also can use these tools to set up and maintain your environments. Together, this release makes it easier for teams to run fleets of parallelized agents that handle tasks end-to-end, inside development environments you fully control.

## #Multi-repo environments

Most engineering work in the enterprise spans multiple codebases and repositories. Larger organizations running microservices often have many repos that need to move in tandem. An agent confined to a single repo has limited usefulness because it can't reason across all the required context.

Cloud agents and automations now support multi-repo environments, building off our work onmulti-root workspaces. You can configure a single environment with all the repositories an agent needs for its work, with re-use across sessions. With multiple repos in scope, agents can reason about how a change in one part of the codebase affects others and work across repos to deliver, test, and verify changes.

Hear directly from some of our customers using multi-repo environments:

Amplitude
Decagon
Snyk
BILT

We run Cursor Automations across public Slack channels at Amplitude. Multi-repo support is what makes them actually useful. An agent can investigate a reported issue, figure out which repos it touches, and open a PR with the fix in the right places with full context.

Steven Cheng
Senior Engineering Manager, Amplitude

## #Environment configuration as code

To make it easier to change, debug, and review environment definitions, we have improved Dockerfile-based configuration. This includes support for build secrets, making it easy to securely access private package registries directly from Dockerfiles. Build secrets are scoped to the build step and aren't passed to the running agent's environment.

We've also upgraded layer caching, so that only the updated layers of your image rebuild when you change the Dockerfile. Builds that hit the cache run 70% faster.

For teams that don't want to write Dockerfiles from scratch, Cursor can configure the Dockerfile for you. Cursor will inspect your repos, figure out the tools and dependencies required, and produce a configuration you can edit and version. This feature is in private beta and will be rolling out to Enterprise teams over the coming weeks.

## #Improved agent-led environment setup

As Cursor configures your environment, it will ask you questions, flag missing credentials, and validate that your environment is set up properly.

Cursor is also more aware of development environments. It will show you the version of the environment your agent is running in. If your environment configuration fails, Cursor will default to a base image with clear warning signs so that your cloud agents can keep running instead of immediately failing.

## #Environment governance and security controls

Every development environment now has its own version history that users can review and roll back. Admins can also restrict rollback permissions to admins only. An audit log captures every action team members take on environments, giving security teams full visibility into who changed what.

Egress and secrets can now be scoped at the development environment level. Teams can restrict outbound network access to a specific allowlist for one environment while leaving a different environment more permissive. Additionally, secrets configured for one environment aren't accessible from any other.

## #What's next

Today, environments are configured at a point in time and rebuilt when they fall out of sync with the codebase. We are building towards environment setups that evolve autonomously as your codebase evolves.

To get started with cloud agent development environments, read thedocsor visit yourcloud agents dashboard.

## Related posts

Mar 25, 2026
·
Product

Run cloud agents in your own infrastructure

Katia Bazzi
 · 
4 min read
Mar 5, 2026
·
Product

Build agents that run automatically

Jack, Jon & Josh
 · 
8 min read
Feb 26, 2026
·
Product

Closing the code review loop with Bugbot Autofix

Jon Kaplan
 · 
3 min read
View more posts
 →