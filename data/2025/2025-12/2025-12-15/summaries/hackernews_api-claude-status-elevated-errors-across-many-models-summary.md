---
title: Claude Status - Elevated errors across many models
url: https://status.claude.com/incidents/9g6qpr72ttbr
date: 2025-12-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-15T11:20:44.670479
screenshot: hackernews_api-claude-status-elevated-errors-across-many-models.png
---

# Claude Status - Elevated errors across many models

* **Incident Summary: Elevated errors across many models on Claude and Platform**
	+ Incident occurred between 13:25 and 14:43PT today
	+ A network routing misconfiguration caused traffic to backend infrastructure to be dropped, preventing requests from completing
	+ The misconfiguration has been reverted and service is fully restored
* **Postmortem Report**
	+ Full recovery across all models as of 14:43PT / 22:43 UTC
	+ The issue was identified and a fix is being implemented
	+ Investigation ongoing, with Sonnet 4.0, Sonnet 4.5, and Opus 4.5 involved in the affected models
* **Key Points**
	+ The incident affects claude.ai - Claude AI, platform.claude.com (formerly console.anthropic.com), Claude API (api.anthropic.com), and Claude Code
	+ Submitters are now updating via email and text message for notifications
	+ Investigation is ongoing with sonnet4.0, sonnet4.5, opus4.5 among other models
