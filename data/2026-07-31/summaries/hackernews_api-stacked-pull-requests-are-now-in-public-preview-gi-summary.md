---
title: Stacked pull requests are now in public preview - GitHub Changelog
url: https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/
date: 2026-07-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-31T06:01:59.675325
---

# Stacked pull requests are now in public preview - GitHub Changelog

# Stacked pull requests – public preview

## Overview
- Stacked pull requests (PRs) split large changes into an ordered series of small, focused PRs.
- Each PR represents a layer of the overall change and can be reviewed independently.
- All layers can be merged together with a single click, eliminating the need for manual rebasing across multiple branches.

## Benefits for teams
- **Parallel review** of short, narrowly scoped PRs keeps large changes moving.
- Maintains quality by applying existing branch protections and required checks to every layer.
- Flexible merging: land an entire stack at once or merge individual layers as they become ready.
- Integrated with GitHub’s existing review, check, and merge mechanisms.

## Getting started
- Install the CLI extension:  
  `gh extension install github/gh-stack`
- Create the first stack from a branch and PR, then add additional branches/PRs on top, each targeting the layer below.

## Workflow
- **Review**: Open any PR in the stack to see only its specific diff; a stack map at the top shows its position in the overall change.
- **Collaboration**: Team members can review different layers simultaneously without blocking progress.
- **Merge**: Merging the latest ready PR lands it and all unmerged lower layers in one operation. Merging lower layers keeps upper PRs open, automatically rebasing and retargeting them.

## Availability
- Public preview rollout to all repositories over the coming days.
- Merge‑queue support for stacked PRs will be introduced progressively in the following weeks.
- Documentation and feedback discussion are available in the “stacks” discussion area.

## Related posts
- Jul 23 – Agent automation controls in GitHub Issues (public preview)  
- Jul 22 – Upcoming GHES change impacting uploading support bundles (retired)  
- Jul 16 – Repository admins can archive pull requests  
- Jul 09 – New pull requests dashboard now generally available  
- Jun 30 – Releases: Sidebar navigation and per‑asset download counts  
- Jun 29 – Restrict issue creation to collaborators only  
- Jun 25 – GitHub Copilot for Jira now generally available  
- Jun 18 – Copilot‑authored pull requests included in author searches  
- Jun 18 – Repository switcher generally available in global navigation  

## Newsletter
- Subscribe to the developer newsletter for tips, technical guides, and best practices.  
- Enter your email and agree to GitHub’s privacy terms to receive the bi‑weekly updates.