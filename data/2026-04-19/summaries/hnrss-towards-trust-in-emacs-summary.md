---
title: Towards Trust in Emacs
url: https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html
date: 2026-04-15
site: hnrss
model: llama3.2:1b
summarized_at: 2026-04-19T06:11:46.917933
---

# Towards Trust in Emacs

Towards Trust in Emacs (Up To Version 30)

Emacs has introduced an explicit notion of trust, distinguishing between trusted and untrusted files since version 30. As a result, security issues such as CVE-2024-53920 arose when arbitrary code execution vulnerabilities were reported.

**Explicit Trust Mechanism**

To address these security concerns, Emacs 30 introduced `trust-manager`, which enables an explicit trust system, where potentially risky features are only enabled for trusted files. All input files are initially marked as untrusted by default.

However, this approach poses a problem - users may need to disable security measures frequently to work efficiently. To overcome this issue, trust-managersolve this common pitfall in the current Emacs trust situation.

**Key Points**

* Trust is implemented differently for trusted and untrusted files.
* `trust-manager` helps eliminate friction with its minimalistic approach.
* Users can grant trust just-in-time by enabling trust-manager-mode in their init file.
* The system remembers chosen settings, so users only need to mark the project directory as trusted.

## Granting Trust Just-In-Time

The new `trust-manager` package provides a simple and convenient way to enforce explicit trust using minimal friction. By enabling trust-manager-mode at initialization and trusting/untrusting files accordingly, users can avoid requiring frequent updates of their trust settings.

**Benefits**

* Simplifies security concerns by introducing an explicit trust mechanism.
* Enables just-in-time enforcement of trust settings for all input files.
* Reduces friction associated with updating trust settings.

## Trust-Manager Customization

`trust-manager` offers additional customization options, such as editing trusted or untrusted settings at any time using `trust-manager-customize`. This flexibility is ideal for users who find the initial setup cumbersome.
