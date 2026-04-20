---
title: Fake Claude Code source downloads actually delivered malware • The Register
url: https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/
date: 2026-04-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-06T01:03:12.317379
---

# Fake Claude Code source downloads actually delivered malware • The Register

# Summary of “Fake Claude Code source downloads actually delivered malware • The Register”

## Background
- A large number of users searched for and downloaded what they believed to be the leaked source code of Anthropic’s Claude Code CLI.
- Cyber‑criminals created a fake GitHub repository that masqueraded as the leaked TypeScript source, using the hype around the accidental exposure to lure victims.

## Malicious Repository Details
- Repository owner: **idbzoomh**.
- The README claims the code was reconstructed from a `.map` file in the npm package and offers “unlocked” enterprise features.
- The repo appeared near the top of Google search results for “leaked Claude Code”.
- At the time of reporting, at least two trojanised repos remained on GitHub; one had 793 forks and 564 stars.
- The releases section contains a `.7z` archive named **Claude Code – Leaked Source Code** that includes a Rust‑based dropper called `ClaudeCode_x64.exe`.

## Payload and Impact
- When executed, the dropper installs two malicious components:
  - **Vidar v18.7** – an infostealer that harvests account credentials, credit‑card data, browser history, and other sensitive information.
  - **GhostSocks** – a proxy tool that turns the infected machine into part of a proxy network used by criminals to hide their activity.
- The combined effect is credential theft and the creation of a botnet‑like proxy infrastructure.

## Related Campaigns
- A similar campaign in March used the OpenClaw AI‑agent platform as a GitHub lure to deliver the same Vidar and GhostSocks payloads (reported by Huntress).
- Both cases illustrate how quickly attackers exploit buzzworthy AI products or news events for financial gain.

## Security Recommendations
- Monitor GitHub for trojanised repositories that mimic popular or leaked projects.
- Use the indicators of compromise (IoC) published by Zscaler’s ThreatLabz (repository URLs, malware hashes) for threat‑hunting.
- Verify the authenticity of downloads, especially when they are tied to recent leaks or hype.
- Keep endpoint protection and network monitoring tools updated to detect and block Vidar, GhostSocks, and related droppers.
