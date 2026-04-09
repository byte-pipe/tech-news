---
title: "From Permanent Access to Just-in-Time: A Startup's IAM Journey Part 1 - DEV Community"
url: https://dev.to/ccscaesar/from-permanent-access-to-just-in-time-a-startups-iam-journey-part-1-4lbn
date: 2025-10-10
site: devto
model: llama3.2:1b
summarized_at: 2025-10-14T11:10:47.416971
screenshot: devto-from-permanent-access-to-just-in-time-a-startup-s.png
---

# From Permanent Access to Just-in-Time: A Startup's IAM Journey Part 1 - DEV Community

**Moving from Permanent Access to Just-in-Time: A Startup's IAM Journey Part 1 - DEV Community**

* **The Problem**: Rapid growth in a FinTech startup led to an "always-on" access model with several security issues, including:
  - Single-Factor Authentication not enforced for AWS console logins
  - Permanent "Always-On" Access granting broad administrative privileges across multiple services and environments
  - Lack of separation of duties and overly permissive roles
* **Existing Setup**: A combination of outdated security measures and lack of effective management led to potential disasters such as account hijacking, insider threats, and ransomware attacks
* **The Blueprint**:
  - Implement risk-based Multi-Factor Authentication (MFA)
  - Eliminate permanent human access to production environments
  - Enforce the principle of least privilege for every IAM role
  - Establish a clear separation of duties
* **Choosing the Right Tools**: Implemented AWS IAM Identity Center, AWS IAM Access Analyzer, Entra ID Privileged Identity Management (PIM), and Entra ID Conditional Access
* **4-Phase Implementation Plan**
1. Initial Setup
2. Configuration and Optimization
3. Cleanup and Review

**To be continued in Part 2:**

Detailed steps for implementing the new Just-in-Time IAM model, from setting up AWS configuration to finalizing cleanup tasks
