---
title: Ask HN: Alternatives to GitHub | Hacker News
url: https://news.ycombinator.com/item?id=49331033
date: 2026-08-17
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-18T12:12:17.472612
---

# Ask HN: Alternatives to GitHub | Hacker News

# Summary of “Ask HN: Alternatives to GitHub”

## Main Question
- The original post asks whether it makes sense to switch from GitHub, citing frequent outages over recent months.

## Experiences with Self‑Hosted GitLab
- A user shared a 6‑year experience running GitLab on‑premises:
  - Automated daily Docker image upgrades worked well, but occasional rollbacks and configuration issues (e.g., low `pg_shared_buffers`) caused problems.
  - Major version upgrades sometimes broke pipelines, requiring coordinated upgrades of many repositories.
  - Frequent critical security patches were received, likely due to automated vulnerability scanning.
- Compared to GitHub Enterprise:
  - Self‑hosted GitLab had far less downtime, though it could be slower.
  - Required more operational effort (“toil”) but offered better access granularity, documentation, and integrations.
  - UI improvements were noted, though initial configuration could be time‑consuming.
- Recommended hardware for a small team (50‑100 users): at least 16 GB RAM (32 GB ideal), 4 CPU cores, and a decent SSD; a small dedicated ops team (1‑3 people) is advisable.
- For runners, a lightweight Kubernetes (k3s) cluster can efficiently manage resources.

## Runner Services and Tools
- A comment promoted “GitLab Runners as a Service” (RocketRunner):
  - Provides one‑click provisioning of Hetzner machines as runners, linked to self‑managed GitLab or GitLab.com.
  - Users can test the service free for 48 hours.
- Feedback highlighted missing ISO 27001 / SOC 2 certifications, which are important for compliance‑focused customers.
- Users praised GitLab’s runner registration for being simpler and more flexible than GitHub’s, especially regarding custom cache locations.
- Several participants reported high uptime (≈99.99%) for their self‑hosted GitLab setups and expressed interest in the runner service.

## Other Alternatives and Considerations
- Some users migrated from GitLab to Gitea after a sudden price increase and feature changes in GitLab’s paid tiers.
- One comment noted that self‑hosting gives control over upgrade timing and incident response, reducing reliance on external schedules.
- Concerns were raised about GitLab Inc.’s support for SMB/Mid‑market self‑hosted users, despite the product’s strengths.
- Personal preference for GitLab.com over Microsoft‑owned GitHub was expressed by a user who values the platform for personal projects.

## Community Sentiment
- Overall, the thread reflects a mixed view:
  - Self‑hosted GitLab is seen as a viable, more reliable alternative when teams can handle the operational overhead.
  - Managed services (GitHub, GitLab.com) are convenient but may suffer from outages, pricing volatility, and limited control.
  - Emerging tools like RocketRunner aim to reduce the friction of managing runners for self‑hosted GitLab.