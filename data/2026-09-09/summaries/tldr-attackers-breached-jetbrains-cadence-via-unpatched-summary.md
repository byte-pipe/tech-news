---
title: Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials
url: https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
date: 2026-09-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-09T08:37:35.973864
---

# Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials

# Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials

## Incident Overview
- JetBrains advises all Cadence users to revoke or rotate every credential after a breach discovered in August 2026.  
- Unidentified threat actors exploited CVE‑2026‑63077 (deserialization of untrusted data, CVSS 9.8) in TeamCity to bypass authentication and run OS commands on the TeamCity server.  
- The exploitation was first seen by JetBrains on 23 August 2026; activity occurred between 8 and 24 August 2026.  
- The compromised Cadence server (api.cadence.jetbrains.com) has been taken offline; the server should have been patched but was not.

## Impact
- Access to a 2024 Cadence server backup that contained credentials, configuration files, artifacts, logs and other data.  
- Extraction of multiple AWS IAM users and their secrets, including accounts belonging to JetBrains employees.  
- Retrieval of files stored in S3 buckets within JetBrains AWS accounts used by Cadence.  
- Exposure of personal data: usernames, real names, email addresses, last‑login timestamps and last‑access IP addresses.  
- Potential compromise of source code synchronized from PyCharm projects to the Cadence server.

## Recommendations to Users
- Immediately revoke or rotate all credentials and secrets used in Cadence executions.  
- Treat every past execution, including inputs and outputs, as potentially untrusted.  
- Review connected systems—AWS accounts, S3 buckets, deployment environments, package/container registries—for suspicious activity.  
- Audit source‑code repositories for unauthorized clones, commits, secret changes, or new collaborators.  
- Monitor for unexpected authentication attempts, new service accounts, IAM role or policy changes, and unusual access to cloud storage.

## Indicators of Compromise
- Activity starting 8 August 2026 using credentials stored in or accessible through Cadence.  
- IP addresses observed during exploitation:  
  - 150.109.230.104  
  - 43.153.227.206  
  - 62.210.127.48  
  - 210.247.242.190  
  - 15.235.225.205  
  - 152.233.30.18  
- Unexpected repository clones, downloads, commits, or changes to secrets, webhooks, collaborators, and permissions.  
- Creation or modification of personal access tokens, API tokens, SSH keys, or service accounts in external services.  
- Unusual changes to cloud IAM roles, policies, or permissions and unexpected access to S3 buckets or objects.

## Consequences
- Exposed personal data raises the risk of targeted phishing, social engineering, impersonation, and other malicious communications.

## Additional Notes
- CISA added CVE‑2026‑63077 to its Known Exploited Vulnerabilities (KEV) catalog on 5 August 2026.  
- JetBrains has invalidated all access tokens used by the JetBrains Cadence plugin in PyCharm.