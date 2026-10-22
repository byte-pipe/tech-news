---
title: GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13 | GitLab Docs
url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/
date: 2026-10-21
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-22T16:10:30.641244
---

# GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13 | GitLab Docs

## GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13

### Important Security Releases

On October 21, the GitLab team released versions 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, and 18.11.13 for the GitLab Community Edition (CE) and Enterprise Edition (EE) to address critical and security vulnerabilities.

### Key Bug and Security Fixes

These versions include important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to one of these versions immediately.

### Security Updates

There are two types of patch releases: scheduled releases and ad-hoc critical patches for high-severity vulnerabilities. Scheduled releases are released twice a month on the second and fourth Wednesdays, and ad-hoc critical patches are issued in response to high-severity vulnerabilities.

### Commitment to Security

GitLab is committed to ensuring that all aspects of GitLab that are exposed to customers or that host customer data are held to the highest security standards. To maintain good security hygiene, it is highly recommended that all customers upgrade to the latest patch release for their supported version.

### Recommended Action

It is strongly recommended that all installations running a version affected by the security fixes described above are upgraded to the latest version as soon as possible.

### Security Fixes Table

| Title          | Severity | Integer Overflow issue in Regular Expression Compiler |
|----------------|-----------|-----------------------------------------------|
| GitLab CE/EE | Critical | Improper Authentication issue in OmniAuth-to-LDAP auto-linking email lookup |
| GitLab EE  | High     | Cache Poisoning issue in OAuth/OIDC discovery endpoints |
| GitLab CE/EE | High     | Improper Access Control issue in GraphQL work item email address field |
| GitLab CE/EE | Medium   | Internal Credential Exposure issue in internal response headers |
| GitLab EE   | Medium   | Authorization Bypass Through User-Controlled Key issue in group milestones API |
| GitLab EE | Medium   | Use of Less Trusted Source issue in AI Gateway feature enablement header |
| GitLab EE | Low      | Use of Cache Containing Sensitive Information issue in merge request title rendering |

Note: This summary is concise, informative, and preserves the original perspective while adhering to Markdown conventions.