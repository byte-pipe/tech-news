---
title: Et Tu, Agent? Did You Install the Backdoor?
url: https://www.a16z.news/p/et-tu-agent-did-you-install-the-backdoor
date: 2026-04-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-06T01:03:04.029085
---

# Et Tu, Agent? Did You Install the Backdoor?

# Et Tu, Agent? Did You Install the Backdoor?

## Overview of the Axios compromise
- The popular npm package **Axios** was hijacked by compromising a maintainer’s account.
- An attacker added a new dependency, **plain‑crypto‑js**, which executed a script on install:
  - Detected the operating system.
  - Downloaded a tailored remote‑access trojan.
  - Executed the trojan and deleted itself, leaving no trace in `node_modules`.
- The attack affected every machine that ran `npm install` during the exposure window, illustrating a “fast, quiet, and invisible” supply‑chain breach.

## What has changed in supply‑chain security
- **AI‑driven coding models** now write and ship code autonomously, pulling in dependencies at machine speed with minimal human review.
- Attackers have learned to **weaponize the dependency graph at scale**, targeting entire ecosystems rather than single packages.
- The result: the attack surface expands faster than any human can monitor, and many dependency decisions are made by non‑human agents.

## Dependencies as the new perimeter
- Modern applications consist largely of open‑source components:
  - Average app > 1,100 open‑source components.
  - Bare‑bones Next.js project installs 282 packages before any custom code.
  - Median GitHub JavaScript repo has 755 transitive dependencies, chosen by no one on the team.
- Compromising a single node (e.g., Axios) can affect every downstream install, turning the entire ecosystem into a potential victim.

## Limitations of current security tooling
- Most software‑composition analysis tools rely on known CVE databases.
- A freshly created malicious package (like `plain‑crypto‑js`) has no CVE, so tools such as `npm audit` report a clean bill of health.
- Self‑destructing malware evades detection by traditional static analysis.

## The “TeamPCP” cascade attack
- **Initial foothold:** Exploited a misconfiguration in Trivy’s GitHub Actions workflow to steal an access token.
- **Propagation:** Force‑pushed malicious code to all Trivy version tags, turning the scanner itself into a delivery vehicle for credential‑harvesting payloads.
- **Worm stage:** Stolen npm tokens powered **CanisterWorm**, which spread across 66+ npm packages using a blockchain‑based command infrastructure, harvesting more tokens and publishing malicious updates automatically.
- **Ecosystem impact:** Within eight days the campaign reached GitHub Actions, Docker Hub, npm, PyPI, and the VS Code extension marketplace, affecting thousands of organizations with a single stolen token.

## AI’s dual role in the evolving attack surface
- AI coding assistants increase developer productivity **2–4×** but also accelerate supply‑chain risk.
- Studies of 117 k dependency changes show AI agents select known‑vulnerable versions **50 %** more often than humans, often requiring major‑version upgrades to remediate.
- **Hallucinated packages:** LLMs fabricate non‑existent package names; attackers register these “slopsquatted” names and embed malicious code, exploiting AI‑driven workflows that automatically install them.
- Autonomous coding agents can install dependencies, run builds, and open pull requests without human oversight, optimizing for functionality rather than safety, compressing review windows to near‑zero.
- Research shows models like Opus 4.6 can discover and exploit vulnerabilities (e.g., SQL injection) when prompted, hinting at their potential as powerful attack tools.

## Conclusion
- The software supply chain is now dominated by **machine‑generated code and dependency decisions**, creating a rapid, self‑propagating threat landscape.
- Traditional vulnerability‑focused tools are insufficient against novel, zero‑day backdoors that disappear after execution.
- Mitigating this risk will require **new detection paradigms**, tighter control of AI‑generated dependencies, and continuous monitoring of the entire dependency graph across ecosystems.
