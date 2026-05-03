---
title: GitHub is sinking – David Bushell – Web Dev (UK)
url: https://dbushell.com/2026/04/29/github-is-sinking/
date: 2026-05-04
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-04T06:02:16.853872
---

# GitHub is sinking – David Bushell – Web Dev (UK)

# GitHub is sinking

## TL;DR
- GitHub, once popular, now feels like a deteriorating Microsoft product.
- Official uptime charts look okay, but missing status pages suggest worse reliability.
- The author views GitHub as a “lame slop graveyard” and urges migration.

## GitHub’s historic uptime
- After Microsoft’s acquisition, the author claims GitHub’s reliability has declined.
- Mentions the “Copilot circle of hell” and self‑inflicted DDoS‑like issues.
- Cites public departures (e.g., Lonami, Mitchell Hashimoto, Armin Ronacher, Jonas Hietala) as evidence of dissatisfaction.

## Git is not GitHub
- Emphasizes that Git (the distributed VCS) is separate from the GitHub service.
- Warns that GitHub’s network effects, fake star economy, and bot noise diminish its value.
- Criticizes GitHub Actions and CI pipelines as over‑engineered and unreliable.
- Encourages users to start migrating rather than staying on a “sinking ship.”

## Alternatives
- Suggests other centralized Git forges as “lifeboats,” noting none are perfect:
  - **Codeberg** – non‑profit, community‑led, based on Forgejo.
  - **Tangled** – early‑stage startup with AT protocol integration, good for small solo projects.
  - **Gitea** – original open‑source project offering cloud‑managed hosting.
  - **GitLab** – enterprise‑grade, feature‑rich but heavyweight.
  - **Bitbucket** – another corporate option, generally discouraged.
- Mentions additional projects (Game of Trees, Radicle, Sourcehut) for further investigation.

## Self‑hosted options
- Recommends self‑hosting a Git forge with actions and releases; primary suggestion is **Forgejo**.
- Notes potential federation between Forgejo instances (and Tangled) but not imminent.
- Highlights that Gitea and GitLab also provide self‑hosted deployments, though GitLab is resource‑heavy.
- Reminds that raw Git over SSH is always possible, with collaboration managed via mailing lists or other tools.

## Closing thought
- The author’s stance: use anything but GitHub and maintain an exit plan in case other services follow the same trajectory.