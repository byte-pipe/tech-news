---
title: 'GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13 | GitLab Docs'
url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/
site_name: hnrss
content_file: hnrss-gitlab-critical-patch-release-1951-1943-1936-1929
fetched_at: '2026-10-22T16:04:42.256185'
original_url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/
date: '2026-10-21'
description: 'Learn more about GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13 for GitLab Community Edition (CE) and Enterprise Edition (EE).'
tags:
- hackernews
- hnrss
---

# GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13

On October 21, 2026, we released versions 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13 for GitLab Community Edition (CE) and Enterprise Edition (EE).

These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to
one of these versions immediately. GitLab.com is already running the patched version. GitLab Dedicated tenants running 19.3.5-internal0 and 19.4.2-internal0 or later already include these fixes and do not need to take action.

GitLab releases fixes for vulnerabilities in patch releases. There are two types of patch releases:
scheduled releases and ad-hoc critical patches for high-severity vulnerabilities. Scheduled releases are released twice a month on the second and fourth Wednesdays.
For more information, please visit ourreleases handbookandsecurity FAQ.
You can see all of GitLab release blog postshere.

For security fixes, the issues detailing each vulnerability are made public on ourissue tracker90 days after the release in which they were patched.

We are committed to ensuring that all aspects of GitLab that are exposed to customers or that host customer data are held to
the highest security standards. To maintain good security hygiene, it is highly recommended that all customers
upgrade to the latest patch release for their supported version. You can read morebest practices in securing your GitLab instancein our blog post.

### Recommended Action

Westrongly recommendthat all installations running a version affected by the issues described below areupgraded to the latest version as soon as possible.

When no specific deployment type (omnibus, source code, helm chart, etc.) of a product is mentioned, it means all types are affected.

## Security fixes

### Table of security fixes

Title
Severity
Integer Overflow issue in Regular Expression Compiler impacts GitLab CE/EE
Critical
Improper Authentication issue in OmniAuth-to-LDAP auto-linking email lookup impacts GitLab CE/EE
High
Cache Poisoning issue in OAuth/OIDC discovery endpoints impacts GitLab CE/EE
High
Improper Access Control issue in GraphQL work item email address field impacts GitLab CE/EE
Medium
Incomplete enforcement of instance-wide SAML/LDAP membership lock allows unauthorized member additions in GitLab EE
Medium
Internal Credential Exposure issue in internal response headers impacts GitLab CE/EE
Medium
Authorization Bypass Through User-Controlled Key issue in group milestones API impacts GitLab CE/EE
Medium
Use of Less Trusted Source issue in AI Gateway feature enablement header impacts GitLab EE
Medium
Use of Cache Containing Sensitive Information issue in merge request title rendering impacts GitLab CE/EE
Low
Improper Access Control issue in merge request approval policy enforcement impacts GitLab EE
Low
Improper Cleanup on Thrown Exception issue in security findings impacts GitLab EE
Low
Improper Access Control issue in group Duo admin-lock enforcement for Amazon Q settings impacts GitLab EE
Low

### CVE-2026-110264- Integer Overflow issue in Regular Expression Compiler impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary code on the GitLab server due to integer overflow when compiling a specially crafted regular expression.

In addition to our standard patch releases, we have backported this fix to GitLab CE/EE versions 18.11.13, 19.0.10, 19.1.9, and 19.2.9.

Impacted Versions:GitLab CE/EE: all versions from 7.0 before 18.11.13, 19.0 before 19.0.10, 19.1 before 19.1.9, 19.2 before 19.2.9, 19.3 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS10.0 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)

Thanksjoaxcarfor reporting this vulnerability through our HackerOne bug bounty program

### DetectingCVE-2026-110264Exploitation Attempts

GitLab security has released two threat detections to support customers with self-managed instances, listed below. GitLab-managed infrastructure, including GitLab.com and GitLab Dedicated, remains patched.

* Onigmo native worker crash
* Org mode render error burst

### CVE-2026-15723- Improper Authentication issue in OmniAuth-to-LDAP auto-linking email lookup impacts GitLab CE/EE

GitLab has remediated an issue that, when OmniAuth SAML and LDAP auto-linking were both enabled, an authenticated user could have taken over an existing LDAP-backed account without any interaction from the targeted user, due to improper input sanitization in the LDAP email lookup path used during OmniAuth identity linking.

Impacted Versions:GitLab CE/EE: all versions from 10.1 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS8.2 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N)

Thanksstealthyfor reporting this vulnerability through our HackerOne bug bounty program

### CVE-2026-112212- Cache Poisoning issue in OAuth/OIDC discovery endpoints impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, an unauthenticated user could have poisoned a shared cache’s OAuth/OIDC discovery document to redirect certain flows to an externally controlled server, due to improper trust of user-supplied values when constructing endpoint URLs in cached discovery responses.

Impacted Versions:GitLab CE/EE: all versions from 18.3 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS7.5 (CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:L/A:L)

This vulnerability has been discovered internally by GitLab team member Peter Arts

### CVE-2026-12664- Improper Access Control issue in GraphQL work item email address field impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user with a read_api-scoped token to retrieve a project’s incoming email address and create work items, bypassing the token’s restrictions, due to insufficient scope enforcement on a GraphQL field.

Impacted Versions:GitLab CE/EE: all versions from 18.2 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS6.8 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:N)

Thanksgo7f0for reporting this vulnerability through our HackerOne bug bounty program

### CVE-2026-16255- Incomplete enforcement of instance-wide SAML/LDAP membership lock allows unauthorized member additions in GitLab EE

GitLab has remediated an issue that, when the instance-wide SAML or LDAP membership lock was enabled, an authenticated user could have granted or accepted project and group membership outside the identity provider’s control, due to incomplete enforcement of the membership lock on requests created before the lock was enabled.

Impacted Versions:GitLab EE: all versions from 12.0 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS5.9 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:L/A:N)

Thanks3nvzfor reporting this vulnerability through our HackerOne bug bounty program

### CVE-2026-105777- Internal Credential Exposure issue in internal response headers impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, an unauthenticated user could have retrieved sensitive internal server credentials due to improper filtering of internal response headers.

Impacted Versions:GitLab CE/EE: all versions from 17.6.5 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS4.3 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

Thanksaltair00for reporting this vulnerability through our HackerOne bug bounty program

### CVE-2026-13319- Authorization Bypass Through User-Controlled Key issue in group milestones API impacts GitLab CE/EE

GitLab has remediated an issue that could have allowed an authenticated user to read milestone metadata, including titles, descriptions, and full project paths, from arbitrary private projects across the instance without any project membership, due to missing authorization checks on a user-supplied project filter parameter in the group milestones API.

Impacted Versions:GitLab CE/EE: all versions from 15.10 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS4.3 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N)

Thanksa0xnirudhfor reporting this vulnerability through our HackerOne bug bounty program

### CVE-2026-112378- Use of Less Trusted Source issue in AI Gateway feature enablement header impacts GitLab EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user to access paid AI features without a valid subscription due to insufficient server-side validation in billing eligibility checks.

Impacted Versions:GitLab EE: all versions from 17.8 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS4.3 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N)

This vulnerability has been discovered internally by GitLab team member Halil Coban

### CVE-2026-105711- Use of Cache Containing Sensitive Information issue in merge request title rendering impacts GitLab CE/EE

GitLab has remediated an issue that, when a merge request in a public project referenced a confidential issue from a private project, an authenticated user with no project membership could have read the confidential issue’s title, due to a viewer-independent fragment cache key that incorrectly shared per-user-redacted rendered content across all users.

Impacted Versions:GitLab CE/EE: all versions from 15.0 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS3.5 (CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:N/A:N)

Thanks20kilogramafor reporting this vulnerability through our HackerOne bug bounty program

### CVE-2026-14288- Improper Access Control issue in merge request approval policy enforcement impacts GitLab EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user to bypass a required merge request approval policy on a protected branch due to improper access control during approval rule synchronization.

Impacted Versions:GitLab EE: all versions from 17.4 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS3.1 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N)

Thanks3nvzfor reporting this vulnerability through our HackerOne bug bounty program

### CVE-2026-112326- Improper Cleanup on Thrown Exception issue in security findings impacts GitLab EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user with read-only permissions to permanently delete existing vulnerability records due to improper cleanup logic that failed to distinguish between pre-existing records from newly created ones during error handling.

Impacted Versions:GitLab EE: all versions from 17.8 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS3.1 (CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N)

This vulnerability has been discovered internally by GitLab team member Gregory Havenga

### CVE-2026-103515- Improper Access Control issue in group Duo admin-lock enforcement for Amazon Q settings impacts GitLab EE

GitLab has remediated an issue that, when an instance administrator locked a group’s Duo availability, an authenticated user with group Owner permissions could have re-enabled AI-backed data egress to a third-party service for that group and its descendant projects, due to insufficient granularity of the admin-lock enforcement controls.

Impacted Versions:GitLab EE: all versions from 19.2 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1CVSS2.7 (CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N)

Thanks3nvzfor reporting this vulnerability through our HackerOne bug bounty program

## Bug fixes

### 19.5.1

* Backport 19.5 docs pages missing from the stable branch
* Backport 19.5 release notes to 19-5-stable-ee
* Backport of ‘Ignore CI variable in roulette experiment default specs’
* Backport of ‘Quarantine the scope picker search query spec’
* Backport GitLab Runner 19.5 release post to the latest stable branch
* Bump CNG helm chart ref to v10.5.0
* Backport of ‘Set GITLAB_BIN_DIR for Duo CLI and bump workflow image to v0.0.23’ into 19.5
* Backport of ‘Return repository_storage from internal Orbit project info’ to 19.5
* Backport of ‘Workhorse: return 429 when Gitaly rejects GetArchive with ResourceExhausted’
* Backport of ‘Allocate pipeline IID for pipeline execution policy pipelines’
* Backport of ‘Link commit list browse button to the current file path’ to 19.5
* Backport of “Load only needed snippet columns when backing up repositories”
* [19.5] Update gitlab-markup to 2.2.0 and rdoc to 8.1.0
* Backport of ‘Pin the Baseline date in .browserslistrc’ into 19.5
* Backport: Cache foundational flow catalog item per request
* Fix work item change type and child milestone with features field
* Backport of ‘Raise Rouge Fallthrough without capturing a backtrace’ to 19.5
* Backport of ‘Add What’s New entries for 202610150001_19_05’
* Backport of ‘Return 404 for Orbit archive and changed_paths when repository is missing’ to 19.5
* Backport of ‘Stop jobs without a fetch from borrowing the git object pool’ and ‘Fix downstream pipelines git alternates’
* [19.5] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0
* [19.5] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0

### 19.4.3

* Add siphon-tables image bundling Siphon CDC table definitions [19.4]
* [19.4] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0
* Backport of “Expose opt-in tagger dates in ListRefs” to 19.4
* Backport of ‘Remove stale merge_request event from Developer flow triggers’ to 19.4
* Backport of ‘Add IP fallback errors to Gitlab::HTTP HTTP_ERRORS’ to 19.4
* Backport of ‘Resume the CVE enrichment sync across export files’ to 19.4
* Backport of ‘Fix truncated diffs for signed-out users’ into 19.4
* Backport of ‘Strip the trusted flag from client-supplied MCP tools in Workhorse’ to 19.4
* Backport of ‘Fix fast-forward merge when a tag shares the target branch name’ to 19.4
* Backport of ‘Ignore CI variable in roulette experiment default specs’
* Backport of ‘Add missing ID token claims for fork MR pipelines’ to 19.4
* Backport of “Load only needed snippet columns when backing up repositories”
* Backport of ‘Set GITLAB_BIN_DIR for Duo CLI and bump workflow image to v0.0.23’ into 19.4
* Backport of ‘Pin the Baseline date in .browserslistrc’ into 19.4
* Backport of ‘Return repository_storage from internal Orbit project info’ to 19.4
* Backport of ‘Workhorse: return 429 when Gitaly rejects GetArchive with ResourceExhausted’
* Backport of ‘Allocate pipeline IID for pipeline execution policy pipelines’
* [19.4] Update gitlab-markup to 2.2.0 and rdoc to 8.1.0
* Backport of ‘Return 404 for Orbit archive and changed_paths when repository is missing’ to 19.4
* Backport of ‘Raise Rouge Fallthrough without capturing a backtrace’ to 19.4
* Backport of ‘Remove unnecessary committer batch-load from mergeability fields’ to 19.4
* Backport of “Adjustments to Wiki experience” to 19.4
* [19.4] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0

### 19.3.6

* [19.3] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0
* Backport of “Expose opt-in tagger dates in ListRefs” to 19.3
* Backport of ‘Add IP fallback errors to Gitlab::HTTP HTTP_ERRORS’ to 19.3
* Backport of ‘Resume the CVE enrichment sync across export files’ to 19.3
* Backport of ‘Fix fast-forward merge when a tag shares the target branch name’ to 19.3
* Backport of ‘Strip the trusted flag from client-supplied MCP tools in Workhorse’ to 19.3
* Backport of ‘Add missing ID token claims for fork MR pipelines’ to 19.3
* Backport of “Load only needed snippet columns when backing up repositories”
* Backport of ‘Workhorse: return 429 when Gitaly rejects GetArchive with ResourceExhausted’
* Backport of ‘Pin the Baseline date in .browserslistrc’ into 19.3
* Backport of ‘Return repository_storage from internal Orbit project info’ to 19.3
* [19.3] Update gitlab-markup to 2.2.0 and rdoc to 8.1.0
* Backport of “Adjustments to Wiki experience” to 19.3
* Backport of ‘Raise Rouge Fallthrough without capturing a backtrace’ to 19.3
* Backport of ‘Return 404 for Orbit archive and changed_paths when repository is missing’ to 19.3
* Bump Prometheus to version 3.13.2 (19-3-stable)
* [19.3] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0

### 19.2.9

* [19.2] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0
* Backport of ‘Add missing ID token claims for fork MR pipelines’ to 19.2
* [19.2] Update gitlab-markup to 2.2.0 and rdoc to 8.1.0
* Bump Prometheus to version 3.13.2 (19-2-stable)
* [19.2] Add Ruby regexp repeat ID overflow patch for 3.3, 3.4 and 4.0

### 19.1.9

* Bump websocket-driver from 0.8.0 to 0.8.2 (backport to 19-1-stable-ee)
* Backport of ‘Fix backfill migration overlap on empty CI partitions’ to 19-1-stable-ee
* Backport of ‘Update GitLab Elasticsearch Indexer to 5.14.14’ to 19.1
* Backport ‘Drop system failure assertion in secrets spec’ to 19-1-stable-ee
* Bump gitlab-shell to 14.56.1 in 19.1 (gitlab-sshd CPU spin fix)
* Bump PostgreSQL to version 17.11 (19-1-stable)
* Bump Consul to version 1.22.7 (19-1-stable)
* Merge branch ‘sdg-fips-staging-upload-internal-release’ into 19.1
* Backport !9672 to 19-1-stable: selinux: add sshd_session_t and sshd_auth_t rules for RHEL 10 / OpenSSH 9.8+
* Backport !9744 to 19-1-stable: Allow sshd fast SSH key lookup under SELinux
* Treat Patroni streaming state as a running node (backport to 19-1-stable)
* [19.1] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4
* [19.1] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4

### 19.0.10

* Increase staging and production upload timeout from 35m to 60m
* [19.0] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4
* [19.0] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4

### 18.11.13

* Increase staging and production upload timeout from 35m to 60m
* Mattermost Security Updates August 13, 2026
* [18.11] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4
* [18.11] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4

## Important notes on upgrading

This patch includes database migrations that may impact your upgrade process.

### Impact on your installation:

* Single-node instances: This patch will cause downtime during the upgrade as migrations must complete before GitLab can start.
* Multi-node instances: With properzero-downtime upgrade procedures, this patch can be applied without downtime.

### Regular migrations

The following versions include regular migrations that run during the upgrade process:

* 19.4.3
* 19.3.6

### Post-deploy migrations

The following versions include post-deploy migrations that can run after the upgrade:

* 19.4.3

To learn more about the impact of upgrades on your installation, see:

* Zero-downtime upgradesfor multi-node deployments
* Standard upgradesfor single-node installations

## Updating

To update GitLab, see theUpdate page.
To update GitLab Runner, see theUpdating the Runner page.

## Receive Patch Notifications

To receive patch blog notifications delivered to your inbox, visit ourcontact uspage.
To receive release notifications via RSS, subscribe to ourpatch release RSS feedor ourRSS feed for all releases.

Was this page helpful?

Yes

No