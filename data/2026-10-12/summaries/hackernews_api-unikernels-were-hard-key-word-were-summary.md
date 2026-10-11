---
title: unikernels were hard. key word: were.
url: https://ghuntley.com/unikernels/
date: 2026-10-11
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-12T06:01:06.219064
---

# unikernels were hard. key word: were.

# Unikernels were hard. Key word: were. Now we have AI

## what a unikernel is, and why they were hard
- A unikernel bundles the application and the OS into a single binary; there is no separate userland.
- Early work (circa 2015) on MirageOS showed the difficulty of providing basic services (TCP, HTTPS) while lacking storage drivers, forcing developers to pull drivers from NetBSD.
- The perception that technologies like Nix, Bazel, and unikernels are “hard” is now embedded in model weights; prompting an AI model can bypass that dogma.

## the operating system is design debt
- Traditional OSes originated from human operators on mainframes; they act as a layer of design debt for modern applications.
- Unikernels reduce attack surface because there is no shell or interpreter that an attacker can invoke.
- While containers can strip shells, they often retain interpreters and other execution pathways; unikernels eliminate the OS layer entirely, turning generic exploits into targeted attacks that require source‑level access.

## you can just port the missing libraries now
- AI agents can automate porting libraries (e.g., converting a Go Stripe client to OCaml) by using an existing implementation as an oracle and generating equivalent code in the target language.
- Example: rewriting `mkfs.xfs` in Rust to produce byte‑for‑byte identical filesystems, validated against the original tool’s output.
- For storage, the recommended pattern is “S3 for everything” with a local NVMe cache and an LRU policy, providing infinite, multi‑user storage as long as latency is acceptable.

## nix machine tests and overlays
- Nix’s language is considered difficult, but Nixpkgs and NixOS machine tests are powerful: they spin up fleets of machines to validate network rules and application interactions.
- When upstream dependencies break, a Nix overlay can patch the issue locally, avoiding reliance on maintainers and manual delays.
- Agents should be able to modify the world directly via first‑party patches rather than invoking humans.

## if you care about security, you have two choices
1. Use a formally verified OS such as seL4 for high‑assurance environments (e.g., satellites).
2. Adopt unikernels for most other workloads, designing security from the ground up instead of hardening a vulnerable stack.
- Modern AI can provide ring‑level separation for unikernels, improving security over single‑privilege designs.
- Enterprise patch fatigue is highlighted by incidents like the KVM exploit that could compromise major cloud providers.

## spaceleans: a distributed unikernel operating system
- Recent exploration of unikernels led to the creation of “spaceleans,” a distributed unikernel OS that extends Mirage‑style concepts across multiple nodes.
- The author shared their Mirage folder with Justin, confirming that the mental model of unikernels aligns with practical implementations.