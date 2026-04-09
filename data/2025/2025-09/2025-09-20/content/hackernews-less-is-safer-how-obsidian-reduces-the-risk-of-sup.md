---
title: 'Less is safer: how Obsidian reduces the risk of supply chain attacks - Obsidian'
url: https://obsidian.md/blog/less-is-safer/
site_name: hackernews
fetched_at: '2025-09-20T11:05:39.492718'
original_url: https://obsidian.md/blog/less-is-safer/
author: saeedesmaili
date: '2025-09-20'
description: Supply chain attacks are malicious updates that sneak into open source code used by many apps. Here’s how we design Obsidian to ensure that the app is a secure and private environment for your thoughts.
---

Supply chain attacks are malicious updates that sneak into open source code used by many apps. Here’s how we design Obsidian to ensure that the app is asecure and privateenvironment for yourthoughts.

### Less is safer

It may sound obvious but the primary way we reduce the risk of supply chain attacks is to avoid depending on third-party code. Obsidian has a low number of dependencies compared to other apps in our category. See a list of open source libraries onour Creditspage.

Features likeBasesandCanvaswere implemented from scratch instead of importing off-the-shelf libraries. This gives us full control over what runs inObsidian.

* For small utility functionswe almost always re-implement them in ourcode.
* For medium moduleswe fork them and keep them inside our codebase if the licenses allowsit.
* For large librarieslike pdf.js, Mermaid, and MathJax, we include known-good, version-locked files and only upgrade occasionally, or when security fixes land. We read release notes, look at upstream changes, and test thoroughly beforeswitching.

This approach keeps our dependency graph shallow with few sub-dependencies. A smaller surface area lowers the chance of a malicious update slippingthrough.

### What actually ships in theapp

Only a handful of packages are part of the app you run, e.g. Electron, CodeMirror, moment.js. The other packages help us build the app and never ship to users, e.g. esbuild oreslint.

### Version pinning andlockfiles

All dependencies are strictly version-pinned and committed with a lockfile. The lockfile is the source of truth for builds so we get deterministic installs. This gives us a straightforward audit trail when reviewingchanges.

We do not run postinstall scripts. This prevents packages from executing arbitrary code duringinstallation.

### Slow, deliberate upgrades

When we do dependency updates,we:

1. Read the dependency’s changelogline-by-line.
2. Check sub-dependencies introduced by the newversion.
3. Diff upstream when the change set is large orrisky.
4. Run automated and manual tests across platforms and critical userpaths.
5. Commit the new lockfile only after these reviewspass.

In practice, we rarely update dependencies because they generally work and do not require frequent changes. When we do, we treat each change as if we were taking a newdependency.

### Time is abuffer

We don’t rush upgrades. There is a delay between upgrading any dependency and pushing a release. That gap acts as an early-warning window: the community and security researchers often detect malicious versions quickly. By the time we’re ready to ship, the ecosystem has usually flagged any problematicreleases.

No single measure can eliminate supply chain risk. But choosing fewer dependencies, shallow graphs, exact version pins, no postinstall, and a slow, review-heavy upgrade cadence together make Obsidian much less likely to be impacted, and give us a long window to detect problems before code reachesusers.

If you’re curious about our broader approach to security, see oursecurity pageand pastaudits.
