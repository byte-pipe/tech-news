---
title: Origin Code Hosting · Cursor
url: https://cursor.com/changelog/origin-code-hosting
date: 2026-08-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-19T04:07:24.402581
---

# Origin Code Hosting · Cursor

# Summary of “Origin Code Hosting · Cursor” (Aug 17 2026)

## Overview
- Origin, a new code‑hosting service, is launched in early beta for all paid Cursor plans (excluding enterprise orgs that opt out).  
- Initial features focus on agent‑scale essentials: repositories, pull requests, code browsing, and GitHub synchronization.  
- Additional agent‑native capabilities and app extensions are slated for future releases.

## #Origin Repos
- The **Codebase** tab hosts Origin repositories.  
- Create a repo via **Click + New**, give it a name, and follow the displayed CLI instructions to clone or push a project.  
- The repo URL follows the pattern `cursor.com/codebase/<codebase‑name>`.

## Bringing GitHub Repos
- Connect a GitHub account, select an organization, and choose which repos to sync.  
- Synced repos appear alongside Origin‑hosted repos, marked with distinct icons.  
- Sync is real‑time: browsing, searching, and pulling occur in Origin, while pushes continue to update GitHub as the source of truth.  
- Access permissions (read/write) are mirrored; repos can be disconnected at any time.

## Pull Requests
- Every repo supports pull requests showing timeline, commits, checks, and file changes.  
- Users can review diffs, comment, and merge directly in Cursor.  
- For synced repos, comments and actions sync bidirectionally with GitHub within seconds, enabling review and merge from either platform.

## Agents in Every Repo
- Code, PRs, and Cursor agents coexist in the same workspace.  
- Users can ask Cursor questions about the code they are viewing; the agent can answer, modify code, update PRs, or push new branches.

## App Extensions for Cursor Repos
- An app ecosystem integrates the full development stack with Origin.  
- Available integrations: **Vercel**, **Depot**, and **Buildkite** (more to come).  
- Example workflow: connect Vercel via a repo’s **Apps** tab, receive preview deployments for each PR, comment, and merge to ship to production.  
- CI integrations run existing GitHub Actions workflows (Depot) or native pipelines (Buildkite).

## Settings
- Each repo includes a settings page to:  
  - View GitHub sync status.  
  - Manage access permissions.  
  - See connected apps.

## Rollout Details
- Early‑beta rollout begins today for all paid plan users; enterprise admins may opt out.  
- Users are prompted to name their codebase and create the first repo.  
- Further documentation is available in the Cursor docs.