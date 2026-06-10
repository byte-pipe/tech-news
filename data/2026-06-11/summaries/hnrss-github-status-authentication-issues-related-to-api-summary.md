---
title: GitHub Status - Authentication issues related to API requests
url: https://www.githubstatus.com/incidents/fcj3088jg1wx
date: 2026-06-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-11T06:01:46.408891
---

# GitHub Status - Authentication issues related to API requests

# Authentication issues related to API requests – Summary

## Overview
- GitHub experienced sporadic authentication failures affecting roughly **15 % of API traffic**.
- Erroneous **401 Unauthorized** responses caused many applications to trigger unnecessary authentication flows.
- The issue impacted the **API Requests** and **Issues** services.

## Timeline of Events (June 10 2026, UTC)

| Time (UTC) | Update |
|------------|--------|
| 15:20 | Initial investigation began after reports of degraded performance across several GitHub services. |
| 15:23 | API Requests showed degraded availability. |
| 15:27 | Issues service experienced degraded performance. |
| 15:27 | Continued investigation into the degraded performance. |
| 15:46 | First statement confirming investigation of sporadic authentication failures (~15 % of API traffic). |
| 15:46 | Re‑affirmed ongoing investigation and promised further updates. |
| 15:46 | Noted that the degradation affecting Issues had been mitigated and monitoring continued. |
| 16:21 | Identified a problematic component in the infrastructure; work began to mitigate the issue. |
| 16:36 | Declared that the degradation affecting API Requests had been mitigated; monitoring ongoing. |
| 16:37 | Confirmed that the overall degradation had been mitigated and stability was being monitored. |
| 16:39 | Incident marked **Resolved**; a detailed root‑cause analysis will be shared when available. |

## Impact
- Approximately **15 % of API requests** returned 401 errors.
- Applications relying on GitHub’s API experienced unexpected authentication prompts.
- Users of the **Issues** feature saw slower performance.

## Resolution
- The faulty infrastructure component was isolated and fixed.
- Both **API Requests** and **Issues** services returned to normal operation.
- Ongoing monitoring is in place to ensure stability.

## Next Steps
- GitHub will publish a detailed root‑cause analysis.
- Continued monitoring to prevent recurrence.