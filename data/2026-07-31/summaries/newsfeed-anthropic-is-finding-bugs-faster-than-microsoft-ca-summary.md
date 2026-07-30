---
title: Anthropic is finding bugs faster than Microsoft can fix them - Ars Technica
url: https://arstechnica.com/security/2026/07/anthropic-is-finding-bugs-faster-than-microsoft-can-fix-them/
date: 2026-07-29
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-07-31T06:02:27.916990
---

# Anthropic is finding bugs faster than Microsoft can fix them - Ars Technica

# Summary of “Anthropic is finding bugs faster than Microsoft can fix them – Ars Technica”

## Background
- Anthropic released the AI model **Mythos** and gave limited access to organizations that develop widely used software.
- The goal: let these partners discover security flaws before hostile actors (e.g., nation‑state hackers) can exploit them.
- Project Glasswing was Microsoft’s internal effort to use Mythos for vulnerability hunting.

## Meeting Highlights (mid‑May)
- Dozens of Microsoft engineers and managers gathered to discuss progress on Project Glasswing.
- A manager confirmed that Mythos was “living up to the hype” and surfacing bugs faster than Microsoft could patch them.
- Engineers were urged to fix as many April‑found bugs as possible before a **May 31** deadline, after which “the rest of the world will have caught up.”
- Participants expressed concern that adversaries could exploit the same bugs shortly after public release.

## Mythos Findings
- In April, Mythos identified **90 critical** and **141 important** bugs in SharePoint alone; numbers increased in early May.
- Across Microsoft 365, Teams, and Copilot, Mythos had uncovered **hundreds** of critical or important flaws, most still unpatched by mid‑May.
- The AI can chain multiple low‑ or moderate‑severity bugs into a high‑severity exploit.

## Microsoft’s Response and Triage Strategy
- Microsoft prioritizes fixing **critical** and **important** bugs; moderate‑severity bugs are slated for later work; low‑severity bugs receive no mention.
- The company defends its triage based on exploitability, impact, and established risk‑analysis practices.
- A spokesperson downplayed the May 31 deadline, noting that rapid exploitation of new vulnerabilities is not new, but emphasized a heightened sense of urgency.

## Risks of the Current Approach
- Security experts warn that chaining several low‑level flaws can produce a severe attack vector, potentially “underpricing” risk under the current triage model.
- Unpatched moderate and low bugs could become entry points for sophisticated, AI‑assisted attacks.

## Patch Activity
- Microsoft’s monthly “Patch Tuesday” releases have surged:
  - June: fixes for **>200** bugs (record at the time).
  - July 14: fixes for **>600** bugs, with only seven low/moderate severity; one of those was actively exploited.
- The volume of discovered bugs is expected to keep rising, according to Microsoft.

## Outlook
- The Five Eyes intelligence alliance warned that the window for pre‑emptive patching is closing within months.
- Internal documents suggest Microsoft’s SharePoint team will remain occupied for months, moving from critical to important bugs, then to roughly **300 moderate** bugs.
- Anthropic declined comment; Microsoft declined to disclose how many bugs have been patched since the May meeting.