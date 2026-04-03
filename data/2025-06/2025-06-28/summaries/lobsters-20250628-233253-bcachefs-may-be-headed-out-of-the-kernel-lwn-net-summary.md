---
title: Bcachefs may be headed out of the kernel [LWN.net]
url: https://lwn.net/Articles/1027289/
date: 2025-06-28
site: lobsters
model: llama3.2:1b
summarized_at: 2025-06-28T23:32:53.757245
---

# Bcachefs may be headed out of the kernel [LWN.net]

**Analysis**

The article "Bcachefs may be headed out of the kernel" from Linus Torvalds' perspective raises concerns about the implications for the bcaches filesystem in the Linux kernel. According to Torvalds, the development and maintenance team will part ways with bcaches due to its new behavior after a heated discussion. This indicates that the decision is unlikely to be reversed.

The article highlights various user adoption rates, revenue mentions, growth metrics, customer pain points for two main issues:

1.  **Inconsistent kernel updates**: The frequent inclusion of bcaches filesystem changes in merges during the kernel development processes have led to inconsistencies and broken functionality when they change from a maintainer domain like this one.
2.  **Bcaches outside of its domain**: In spite of maintaining its core code, bcaches has limited integration with overlayfs layers which could lead to compatibility issues.

The article also touches on technical feasibility:

1.  **High complexity**: To fix the issues mentioned above bcaches is prone to conflicting changes within the maintainer team.
2.  **Required expertise**: For such major updates and refactorizations, significant resources will likely be required from experienced kernel developers.

Business viability signals point towards existing competition in kernel space:

*   Kernel code maintains are actively working on the same filesystems
*   Integration into separate maintainers and merge windows make it unlikely to change

A final thought is that this changes for new attempts by Kent Overström: he will face more difficulty having his work accepted, making the maintenance of bcaches even harder.

Actionable insights:

| Insight | Action Required |
| ---      | ---                 |
| Problematic relationship between Linus Torvalds and Kent Overstreemaking issues with bcaches be considered seriously.  The discussion about what happens to bcaches filesystem after a pull request in the kernel is clear. |
| Inconsistency in kernel updates due to its behavior for maintaining different domains makes it likely that this decision will not change|
|bcaches might face more challenges introducing major changes and refactorizations into their codebase, especially following integration with overlayfs layers |
| Kernel maintainers like Overström are expected to deal with more compatibility issues if they decide to support bcaches filesystem. To mitigate these chances is probably needed. |
| Changes in their business models due to a decision to discontinue working on the specific filesystem |
