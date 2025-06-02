---
date: 2025-06-01
description: "\u2636"
enhanced_prompting: true
fetched_at: '2025-06-01T01:56:22.775760

  '
local_model: true
model: gemma3:27b
original_url: 'https://lobste.rs/s/ytefme/when_was_last_time_you_broke_production

  '
site_name: lobsters
summarization_type: local_high_quality
summarized_at: '2025-06-01T02:02:06.856123'
summary_type: local_high_quality
tags: ask, practices
title: When was the last time you broke production and how? | Lobsters
url: 'https://lobste.rs/s/ytefme/when_was_last_time_you_broke_production

  '
---

• Here's a technical summary of the "When was the last time you broke production and how? | Lobsters" article, formatted as requested:
• **Contextual Security Restrictions & Privilege Escalation:** The incident revolved around restricting capabilities within a privileged UI context in Firefox (bypassing the Same-Origin Policy). The goal was enhanced security by limiting access to external URLs, but the implementation inadvertently broke core functionality. This highlights the risks of overly aggressive security hardening without comprehensive testing of all dependent features.
• **Test Environment Discrepancies:** The root cause was a more permissive configuration within the CI testing environment. While intended to avoid false positives, this masked the impact of the security restrictions, leading to a false sense of security and a successful CI build despite the production-breaking change. This underscores the critical need for test environments to closely mirror production configurations.
• **Importance of Production-Parity Testing:** The article serves as a cautionary tale against code that behaves differently in testing versus production. The author explicitly advocates for minimizing discrepancies between these environments to prevent unforeseen issues and ensure reliable deployments. This is a core tenet of robust software engineering practices.
