---
title: GitHub - jordan-gibbs/hyperresearch: Agent-driven research knowledge base. Agents collect, search, and synthesize web research into a persistent, sear...
url: https://github.com/jordan-gibbs/hyperresearch
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-12T01:23:05.081753
---

# GitHub - jordan-gibbs/hyperresearch: Agent-driven research knowledge base. Agents collect, search, and synthesize web research into a persistent, sear...

# Hyperresearch – Agent‑driven Deep Research Harness  

- **Purpose**: Turns Claude Code into a deep‑research agent that builds adversarially‑audited reports with full source provenance, currently leading the DeepResearch‑Bench RACE leaderboard.  

- **Core Features**  
  - Retrieves 250+ sources per run; citation chasing doubles the corpus size.  
  - Every citation is verified by a skeptical cite‑checker; hallucinated quotes are blocked.  
  - Independence audit de‑duplicates syndicated copies, counting them as a single source.  
  - Four parallel adversarial critics review drafts; a tool‑locked patcher applies only surgical edits.  
  - Paywalled papers are fetched via Unpaywall/Europe PMC; full texts are stored and disclosed.  
  - All sources are saved in a searchable markdown + SQLite vault for reuse in later sessions.  
  - Runs can resume from the exact step where they crashed.  
  - Scales from 30‑minute fact surveys to 4‑8‑hour dissertation‑length reports (25 K–80 K words).  

- **Installation**  
  ```bash
  cd your-project
  pip install hyperresearch && hyperresearch install
  hyperresearch <prompt>
  ```  
  Supports Python 3.11–3.13; global install adds the agent to every Claude Code session.  

- **16‑Step Research Pipeline**  
  1. **Decompose** – split query into atomic items, coverage matrix, tier classification.  
  2. **Width sweep** – generate multi‑perspective search plan and launch parallel fetches.  
  3. **Contradiction graph** – cluster contradictory statements.  
  4. **Loci analysis** – parallel analysts score loci with source budgets.  
  5. **Depth investigation** – parallel investigators produce interim notes.  
  6. **Cross‑locus reconcile** – merge positions into `comparisons.md`.  
  7. **Source tensions** – extract expert disagreements (`source‑tensions.json`).  
  8. **Corpus critic** – identify gaps and fetch targeted sources.  
  9. **Evidence digest** – compile top claims and verbatim quotes.  
  10. **Triple draft** – per‑angle curation and three parallel draft sub‑orchestrators.  
  11. **Synthesize** – plan, outline, and generate final report.  
  12. **Critics** – four adversarial critics produce findings.  
  13. **Gap‑fetch** – fetch missing sources identified by critics.  
  14. **Patcher** – apply surgical edit hunks.  
  14.5 **Cite‑check** – verify citation‑sentence bindings.  
  15. **Polish** – hygiene and filler pass.  
  16. **Readability audit** – apply JSON‑driven readability suggestions.  

- **Tiers & Gears (Scale Levers)**  
  - **light**: bounded factual queries; steps 1‑2‑10‑15‑16; ~30‑40 min.  
  - **full** (default): deep argumentative analysis; all 16 steps + cite‑check; ~1.5‑2.5 h.  
  - **dissertation**: chaptered mega‑runs (300‑450 sources, 25 K‑80 K words); ~4‑8 h.  
  - Gears adjust source targets, depth budgets, and word limits; custom gears defined in `hyperresearch/config.toml`.  

- **Levers (Report Voice & Style)**  
  - **register**: `teach`, `survey`, `analyze` (default), `advocate`.  
  - **domain_notes**: freeform notes on sourcing strategy, evidence norms, recency window.  
  - **inference_depth**: `surface`, `standard`, `deep`.  
  - Levers are parsed from the prompt; explicit directives override defaults.  

- **Design Principles**  
  1. **Patch, never regenerate** – after synthesis, only surgical patches modify the report.  
  2. **Persisted vault** – every fetched source remains searchable for future sessions.  

- **Additional Tools**  
  - `hyperresearch levers set <tag> inference_depth=deep --rerender` to deepen inference mid‑run.  
  - `hyperresearch run status -j` to view tier selection made by step 1.  

- **Documentation & Community**  
  - README, CHANGELOG, CONTRIBUTING, and roadmap files are included.  
  - Repository holds example reports, tests, and assets for further exploration.