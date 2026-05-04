---
date: '2026-05-05'
model: gpt-oss:120b-cloud
generated_at: '2026-05-05T00:55:24.684453'
---

## Executive Summary
- A JAX port of Karpathy’s NanoChat demonstrates XLA’s strengths in cross‑hardware scaling while exposing debugging and performance gaps.  
- Two social‑experiment pieces go viral: a systematic “talk to strangers at the gym” study and a novel “underdrawing” technique that dramatically improves numeric accuracy in AI‑generated images.  
- Amazon launches a B2B logistics platform, while TechCrunch promotes a limited‑time 50 % discount on a second Disrupt 2026 pass, signaling aggressive market‑expansion moves.  
- The Citizen Lab uncovers a global telecom‑surveillance infrastructure spanning dozens of countries, highlighting systemic privacy risks.  
- In the software arena, GameStop’s $55.5 bn bid for eBay, a trademark dispute over a fake Notepad++ Mac release, and a resurgence of terminal user interfaces dominate headlines, underscoring consolidation, IP protection, and UI‑tooling debates.

---

## AI and Machine Learning (8 articles)

### I Rebuilt Karpathy's NanoChat in JAX. Here's What XLA Gets Right and What It Gets Dead Wrong. – DEV Community  
A JAX/Flax rewrite of Karpathy’s NanoChat trains an 885 k‑parameter model in under 10 minutes on a single GPU and runs unchanged on TPU, showcasing XLA’s ability to eliminate Python overhead and provide device‑agnostic code. The port also reveals pain points: debugging inside JIT‑compiled functions is cumbersome and the lack of high‑performance kernels like Flash‑Attention 3 slows attention compared with the original PyTorch version.

### Talking to 35 Strangers at the Gym – Summary – Hacker News (trending)  
A recent graduate conducted a month‑long experiment of approaching a different gym‑goer each day, customizing opening lines based on visual cues. The effort yielded a handful of ongoing acquaintances and demonstrated that low‑pressure, personalized outreach can modestly alleviate social isolation in fitness settings.

### Using “underdrawings” for accurate text and numbers – Hacker News (trending)  
The author proposes a two‑stage pipeline where deterministic SVG/HTML underdrawings embed exact text and numbers, which are then stylized by a multimodal image model (e.g., Gemini 3.0 Pro). This method dramatically improves numeric fidelity in AI‑generated images, turning artistic output into a reliable medium for precise data presentation.

### Discovering Hard Disk Physical Geometry through Microbenchmarking – Hacker News  
A deep‑dive into 17 hard drives (45 MB to 5 TB) uses microbenchmarks to infer RPM, track pitch, sector layout, and defect clusters, revealing that modern drives no longer adhere to classic CHS geometry and that seek‑time curves expose acoustic management strategies.

### 5 days to get 50% off a second Disrupt 2026 pass – TechCrunch  
TechCrunch announces a limited‑time BOGO promotion (ends May 8 PT) offering 50 % off a second Disrupt 2026 ticket, with savings ranging from $149 to $499, encouraging attendees to bring colleagues for broader networking and deal flow.

### Amazon opens up its global logistics network to all businesses – TechCrunch  
Amazon launches “Amazon Supply Chain Services,” extending its freight, fulfillment, and parcel capabilities to enterprises of any size, directly challenging UPS and FedEx and mirroring the AWS model of infrastructure‑as‑a‑service.

### Armenia hosts major EU summits in pivot away from Russia – Al Jazeera  
Yerevan hosted two high‑profile EU summits on security, trade, and the Ukraine war, signaling Armenia’s strategic shift toward deeper EU ties and away from its traditional alignment with Russia.

### Reddit – Please wait for verification – Reddit  
No article content was provided.

---

## Cybersecurity and Privacy (1 article)

### Bad Connection: Uncovering Global Telecom Exploitation by Covert Surveillance Actors – The Citizen Lab (trending)  
The Citizen Lab reveals a multi‑vector surveillance ecosystem that abuses 3G/4G signaling and malicious SMS to turn phones into covert beacons, leveraging operator identifiers across at least 18 countries. Persistent campaigns exploit weak inter‑carrier OPSEC, demonstrating how the global telecom trust model can be repurposed for clandestine location tracking.

---

## Software Engineering and Dev Tools (8 articles)

### I Love Tailwind. Sorry Not Sorry – DEV Community (trending)  
A seasoned CSS developer argues that Tailwind’s utility‑first approach delivers speed, consistency, and maintainability for large teams, while still requiring a solid CSS foundation for custom or performance‑critical UI work.

### GameStop makes $55.5bn takeover offer for eBay – BBC News (trending)  
GameStop proposes a cash‑and‑stock deal valuing eBay at $125 per share, financing the $55.5 bn acquisition with $20 bn of debt. The bid promises $2 bn cost cuts and a “live commerce” network via GameStop’s stores, but analysts question strategic fit and the added debt burden.

### Trademark Violation: Fake Notepad++ for Mac – Notepad++ (trending)  
A fraudulent website claims an official macOS version of Notepad++, misusing the trademark and misleading users. The project’s maintainer has issued a public warning and urges the community to correct misinformation wherever it appears.

### Why TUIs are back – Hacker News (trending)  
The author chronicles the decline of native GUI toolkits on Windows, Linux, and macOS, the rise of Electron, and argues that terminal user interfaces (TUIs) offer a fast, uniform, keyboard‑centric alternative that sidesteps fragmented UI ecosystems.

### text-to-cad: Open source harness for generating CAD models – GitHub (hnrss)  
The “text‑to‑CAD” repository provides a local, AI‑driven workflow for creating, editing, and exporting 3D models (STEP, STL, GLB, etc.) using coding agents like Codex and Claude, complete with a web‑based CAD explorer and support for robot URDF generation.

### Tar Files Created on macOS Display Errors When Extracting on Linux – Hacker News  
macOS’s default `bsdtar` embeds Apple‑specific extended attributes, producing `._*` files and unknown‑header warnings on Linux. The issue can be avoided with `--no-xattrs`, `--disable-copyfile`, or by switching to GNU tar.

### Arsenal vs Atletico Madrid: Champions League – team news, start and lineups – Al Jazeera  
Preview of the Champions League semifinal second leg at the Emirates Stadium, highlighting Arsenal’s return of Bukayo Saka and Atletico’s reliance on Julian Alvarez. Both sides list injury updates and predicted line‑ups ahead of the decisive match.

### ‘Heartbreaking’: Iranian scientists on losing labs, libraries and liberty – Newsfeed  
Amid the 2026 Iran‑Israel‑US conflict, multiple Iranian universities have been bombed, libraries destroyed, and internet shut down, severely disrupting research. Scientists call for greater international awareness and flexibility from journals when evaluating Iranian submissions.

---

## Notable Mentions
- Google to sell TPU chips to ‘select’ customers in latest shot at Nvidia – TLDR  
- Polars — Handling Schema Issues in Polars – TLDR  
- Healthy Brands Begin With Strategic Integrity – Branding Strategy Insider – TLDR  
- How I Do Content Engineering with Claude Code – TLDR  
- The “Bug‑Free” Workforce: How AI Efficiency Is Subtly Disrupting The Interactions That Build Strong Teams — Smashing Magazine – TLDR