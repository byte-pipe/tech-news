---
title: RCE in React Server Components · Advisory · vercel/next.js · GitHub
url: https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp
date: 2025-12-04
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-04T11:12:49.626108
screenshot: hackernews-rce-in-react-server-components-advisory-vercel-nex.png
---

# RCE in React Server Components · Advisory · vercel/next.js · GitHub

**RCE in React Server Components Advisory**

### Vulnerability Description

A critical vulnerability affects several React packages used by Next.js 15.x and 16.x, including `react-server-dom-parcel`, `react-server-dom-turbopack`, and `react-server-dom-webpack`. This issue is tracked as CVE-2025-55182.

### Affected Versions

* >=14.3.0-canary.77
* >=15
* >=16

### Fixed Versions

* React: 19.0.1, 19.1.2, 19.2.1
* Next.js:
	+ <=15.x
	+ <=16.x (affected)

**Key Takeaways**

Due to a critical vulnerability in several React packages used by Next.js, there is a high risk of successful remote code execution (RCE) via denial-of-service (DoS) attacks.

**Upgrades and Downgradings**

For users on stable 15.x or 16.x Next.js versions:

* Upgrade to a patched, stable version immediately.
* For canary releases starting with >=14.3.0-canary.77, use the specific canary release build instead of upgrading to the patched version.

**Mitigations and Recommended Actions**

To minimize the risk of RCE vulnerabilities:

* Follow best practices for secure coding.
* Use a package manager like npm or yarn to update dependencies regularly.
* Review your codebase to ensure it adheres to security guidelines.
