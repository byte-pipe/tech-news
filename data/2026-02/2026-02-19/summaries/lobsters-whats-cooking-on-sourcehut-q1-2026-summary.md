---
title: "What's cooking on SourceHut? Q1 2026"
url: https://sourcehut.org/blog/2026-02-18-whats-cooking-q1-2026/
date: 2026-02-19
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-19T06:02:59.815368
---

# What's cooking on SourceHut? Q1 2026

# SourceHuT Q1 2026 Update

## Drew’s Update

*   New pricing for new customers is now in effect. Existing users are grandfathered into their current price, but can opt-in to the new pricing via a button on their billing dashboard.
*   New user profile pages have been implemented, linking to resources across all SourceHuT services and allowing for avatars and pronouns. Avatar usage will be limited to profiles.
*   Support for `format=flowed` on the lists.sr.ht UI is now available, improving readability on mobile devices.
*   "Resource IDs" (RIDs) have been rolled out to GraphQL APIs, providing unique, stable, and lexicographically sortable identifiers for resources. This enables more direct fetching of resources via ID.
*   Future plans include adding more RIDs to GraphQL APIs, working with Simon on a project hub API, enabling GBP payments, and addressing technical debt.
*   A major focus for the quarter is the ongoing development of support for organizations.

## Conrad’s Update

*   SourceHuT-migrate now supports initializing databases, completing the replacement of the old Alembic Python scripts and restoring full functionality.
*   A structured PXE-boot setup for servers is now in place for emergency recovery.
*   Monitoring of baseboard management controllers via IPMI has been finalized.
*   Significant refactoring of Go packages is underway with the goal of rewriting the builds.sr.ht shell in Go to reduce Python usage.
*   Efforts are being made to clean up the SSH key database as a precursor to refactoring the SSH keys table and enabling SSH deploy keys for git.sr.ht.

## Everyone Else

*   SourceHuT is free and open-source, relying on community contributions.
*   Simon Martin has made numerous contributions, including finer-grained control over build submissions, features for mailing list build submissions and post-submission job tag editing, multi-line selections for paste.sr.ht, more detailed software version information in APIs, and links to superseded patchsets.
*   Community maintainers have shipped updates for various software images: Fedora 43 (Gary Kim), FreeBSD 15.x (CismonX), OpenBSD 7.8 (Marek Marecki), and Alpine 3.23 (Achill Gilgenast).
*   Varun Narravula contributed a patch to resolve an email-based resolution bug for todo.sr.ht tickets.
*   Many other small bug fixes and improvements have been made by various contributors.
