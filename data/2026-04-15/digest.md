---
date: '2026-04-15'
model: gpt-oss:120b-cloud
generated_at: '2026-04-15T06:07:07.785928'
---

## Executive Summary
- Anthropic’s Claude Code gains a long‑term memory layer via the open‑source **claude‑mem** plugin, while a DIY PowerShell hook offers a zero‑cost alternative.
- Researchers unveil **Introspective Diffusion Language Models (I‑DLM)** that close the quality gap with autoregressive models and deliver 3‑4× higher throughput.
- A new **declarative spec** is proposed to solve the exploding “M × N” tool‑calling support problem for open‑source LLMs.
- Privacy‑focused users clash with Flock Safety over CCPA deletion rights, and Adobe releases emergency patches for a widely‑exploited PDF zero‑day (CVE‑2026‑34621).
- Cultural highlights include the digitisation of 2,500 rare concert tapes, a public‑domain video of Artemis II’s splash‑down, and Spain’s telecom regulator extending sports‑event internet blocks to all major ISPs.

---

## AI and Machine Learning

### Adding Persistent Memory to Claude Code with claude‑mem — DEV Community [devto]
Claude Code’s lack of session memory is addressed by the **claude‑mem** plugin, which logs tool usage and injects relevant context into future prompts via SQLite + Chroma hybrid search. The setup is a single `npx` command and runs as a local Bun HTTP worker, offering vector‑based retrieval and a web UI for browsing stored memories.

### The Future of Everything is Lies, I Guess: Work — Hacker News [hackernews_api]
The essay argues that LLM‑driven “programming as witchcraft” is reshaping software creation, but warns that natural‑language prompts lack the semantic guarantees of formal languages and can produce fragile code. It also warns that AI “employees” may behave like sociopaths—lying, sabotaging, and shifting blame—while highlighting classic automation pitfalls such as deskilling and automation bias.

### I‑DLM: Introspective Diffusion Language Models — HNRSS [hnrss]
I‑DLM converts a pretrained autoregressive model into a diffusion model with introspective‑consistency training and strided decoding, achieving AR‑level quality on 15 benchmarks while delivering 2.9–4.1× higher throughput. The approach is AR‑compatible, allowing drop‑in deployment on existing serving stacks like SGLang.

### Tool calling, open source, and the M×N problem — HNRSS [hnrss]
Open‑source LLMs expose diverse, model‑specific tool‑calling wire formats, forcing each inference engine to implement a separate parser (M applications × N models). The author proposes a **declarative specification** that centralises format knowledge, letting grammar engines and parsers share the same config and dramatically reducing duplicated engineering effort.

### About 250 missing after boat carrying Rohingya refugees capsizes — The Guardian [newsfeed]
A Bangladeshi trawler overloaded with ~280 Rohingya migrants capsized in the Andaman Sea, leaving roughly 250 people missing; nine survivors were rescued after drifting for up to 36 hours. The tragedy underscores the ongoing humanitarian crisis stemming from the 2017 Myanmar genocide and the lack of durable solutions for displaced Rohingya.

### AI needs solid botanical data more than ever — Nature (newsfeed) [newsfeed]
The article warns that AI models for drug discovery, agriculture, and biosurveillance are hampered by the paucity of formally described plant and fungal species; less than 10 % of fungi have scientific names, limiting LLM training data. It calls for preserving specialist botany and taxonomy programs to supply the high‑quality species‑level data that next‑generation biotech AI will require.

### An Israeli and a Palestinian work together for Mideast peace — NPR [newsfeed]
Former travel‑agency owners Aziz Abu Sarah (Palestinian) and Maoz Inon (Israeli) have turned personal tragedy into a joint peace‑building platform, touring, publishing a book, and meeting world leaders to model shared language and grassroots activism. They argue that a small, dedicated activist core can catalyse a broader movement toward a negotiated Israel‑Palestine settlement within five years.

### Reddit – Please wait for verification — Reddit (placeholder) [reddit]
*No substantive content was provided; the article consists of a request for the full Reddit post text.*

---

## Cybersecurity and Privacy

### Getting the Flock out — Honeypot.net (trending) [hackernews_api]
A California resident’s CCPA request to delete personal data from Flock Safety was rebuffed with the claim that Flock is merely a data **processor**, not a controller, and that the request should be directed to the hiring organization. The user argues this interpretation is legally inaccurate, sparking debate over AI‑enabled surveillance firms’ obligations under privacy law.

### Adobe fixes PDF zero‑day security bug that hackers have exploited for months — TechCrunch [newsfeed]
Adobe patched CVE‑2026‑34621, a remote‑code‑execution flaw in Acrobat DC/Reader that had been active in the wild for at least four months. Researchers observed malicious PDFs on VirusTotal since November 2025; the update is urged for all Windows and macOS users to stop the ongoing exploitation.

### Adobe fixes actively exploited Acrobat Reader flaw CVE‑2026‑34621 — TLDR [tldr]
A more technical recap of the same vulnerability confirms a critical prototype‑pollution bug (CVSS ≈ 9.6) that lets attackers read local files and execute arbitrary code. The exploit was discovered by Haifei Li and has been leveraged in the wild, making immediate patching essential for enterprises.

---

## Software Engineering and Dev Tools

### Thousands of rare concert recordings are landing on the Internet Archive — TechCrunch (trending) [hackernews_api]
Volunteer effort led by Aadam Jacobs and the Internet Archive has digitised ~2,500 tapes from a 10,000‑tape personal collection, making rare live performances (e.g., 1989 Nirvana, early Sonic Youth) publicly accessible. The project preserves culturally significant audio that would otherwise degrade on magnetic tape.

### What is jj and why should I care? — Steve’s Jujutsu Tutorial (trending) [hackernews_api]
**jj** is a new command‑line front‑end for the Jujutsu DVCS, promising a simpler yet more powerful workflow than Git while retaining Git‑compatible back‑ends for seamless migration. It reduces core command surface and adds advanced features that are hard to achieve in Git alone.

### Automate work with routines — Claude Code Docs [hnrss]
Claude Code now supports **routines**, saved configurations that can be triggered on schedules, API calls, or GitHub events, enabling automated code‑review, issue triage, documentation drift checks, and deployment verification directly from Anthropic’s cloud. Routines are managed via a web UI or CLI and count against the user’s daily run quota.

### Artemis II: New video shows moment Orion capsule is opened at sea — Newsfeed [newsfeed]
A freshly released video captures NASA’s recovery crew opening the Orion hatch after the historic Artemis II splash‑down, showing the four astronauts emerging safely and marking the mission’s successful return from the deepest human spaceflight to date.

### 8 Tips for Writing Agent Skills — TLDR [tldr]
The guide outlines best practices for building reusable “skills” for LLM agents, covering clear descriptions, lean file structures, explicit negative cases, thorough testing, and criteria for retiring skills once the model internalises the capability.

### AI is the Closest Thing to a Genie Lamp — Big Medium [tldr]
The article argues that AI has shifted the bottleneck from “how” to “what,” making the ability to define the right goals (design thinking) the new competitive advantage, while execution becomes a cheap, automated service.

---

## Cloud and Infrastructure

### Internet será irrespirable los días de fútbol y otros deportes. Telefónica extiende los bloqueos a Champions, tenis y golf — Hacker News (trending) [hackernews_api]
A Spanish court authorises Telefónica to dynamically block IPs, domains, and URLs that stream unauthorized sports content, extending the measure to all major ISPs (Movistar, Orange, Vodafone, Digi) for every live football, tennis, and golf event. The broad IP‑level blocking risks collateral damage to legitimate services that share CDN infrastructure, effectively making the internet “unbreathable” on match days.

---

## Notable Mentions
- A bug on the dark side of the Moon – TLDR
- A Picture Is Worth a Thousand Tokens – Repaint – TLDR
