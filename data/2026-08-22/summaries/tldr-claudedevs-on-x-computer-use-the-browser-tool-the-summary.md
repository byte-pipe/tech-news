---
title: "ClaudeDevs on X: \"Computer use, the browser tool, the Skills API, and the Files API are now generally available on the Claude Platform. Automate work..."
url: https://x.com/ClaudeDevs/status/2090540270219567575
date: 2026-08-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-22T06:01:03.898212
---

# ClaudeDevs on X: "Computer use, the browser tool, the Skills API, and the Files API are now generally available on the Claude Platform. Automate work...

# ClaudeDevs on X – Announcement Summary

## Announcement
- Computer use, the browser tool, the Skills API, and the Files API are now generally available on the Claude Platform.  
- Goal: automate work in applications without native APIs, reduce round trips per task, and enable Claude Managed Agents built on versioned skills and reusable files.

## Technical Improvements
- **Computer toolset (`computer_toolset_20260801`)** now performs multiple actions per turn (click, type, key, screenshot) instead of a single action per round‑trip.  
  - Early‑access customers reported 20‑40 % fewer round trips per task, leading to faster completion and lower cost.  
- **Browser toolset (`browser_toolset_20260801`)** shifts from pixel‑based automation to element‑reference automation, making scripts resilient to layout changes.  

## Skills API
- Provides a way to upload a team’s procedure once, version it, and pin each request to a specific `version_id` or to `latest`.  
- Serves as a core building block for Claude Managed Agents.  

## Files API Enhancements
- Allows a single upload to be reused across requests via a `file_id`.  
- New features in the update:  
  - `expires_in_seconds` parameter.  
  - 5× higher rate limits (500 RPM).  
  - 1 TB storage per organization.  

## Community Feedback
- **David Mlcoch** (Asteroid Inc.) shared early‑access results on healthcare workflows:  
  - 32‑52 % fewer model calls.  
  - 25‑32 % lower cost per task.  
  - 100 % completion rate on every workflow.  

## References
- Documentation: Computer use tool (platform.claude.com).  
- Documentation: Agent Skills (platform.claude.com).  
- Blog post: “Build production agents with computer use, the Skills API, and the Files API” (claude.com).  
- Asteroid case study: “Claude computer use in healthcare” (asteroid.ai).