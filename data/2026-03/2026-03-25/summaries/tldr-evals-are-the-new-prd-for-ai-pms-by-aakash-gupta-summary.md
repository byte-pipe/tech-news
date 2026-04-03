---
title: Evals are the new PRD for AI PMs - by Aakash Gupta
url: https://www.news.aakashg.com/p/ankur-goyal-podcast
date: 2026-03-25
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-25T01:02:31.284271
---

# Evals are the new PRD for AI PMs - by Aakash Gupta

# Evals are the new PRD – Playbook Overview  

## Podcast Context  
- Episode of **The Growth Podcast** featuring **Ankur Goyal**, Founder & CEO of **Braintrust**.  
- Hosted by **Aakash Gupta**, focusing on how evaluation frameworks (“evals”) replace traditional Product Requirement Documents (PRDs) for AI product managers.  

## Core Premise  
- In AI‑centric product development, **evals serve as the living specification** that guides feature design, prioritization, and success measurement.  
- Unlike static PRDs, evals are **iterative, data‑driven, and continuously validated** against model performance and user outcomes.  

## Key Takeaways from the Playbook  

| Aspect | Insight |
|--------|----------|
| **Definition** | An *eval* is a structured set of metrics, test cases, and acceptance criteria that quantifies whether an AI model meets product goals. |
| **Why replace PRDs?** | Traditional PRDs lack mechanisms to capture model behavior, bias, and drift; evals embed these concerns directly into the product roadmap. |
| **Components of an effective eval** | 1. **Clear hypothesis** – what problem the model solves.<br>2. **Quantitative metrics** – accuracy, latency, fairness, etc.<br>3. **Benchmark datasets** – representative of real‑world usage.<br>4. **Success thresholds** – concrete numbers for go/no‑go decisions. |
| **Workflow Integration** | - **Design → Eval Draft → Review → Implementation → Continuous Monitoring**.<br>- Eval results feed back into backlog grooming and sprint planning. |
| **Collaboration Model** | Cross‑functional teams (PMs, data scientists, engineers, UX) co‑own evals, ensuring alignment on expectations and trade‑offs. |
| **Tooling & Automation** | Use CI/CD pipelines to run eval suites on every model iteration; surface results in dashboards for rapid stakeholder visibility. |
| **Risk Management** | Evals surface model failures early (e.g., bias spikes, performance regressions), enabling proactive mitigation before release. |
| **Metrics Evolution** | As product context changes, evolve eval criteria—add new fairness checks, latency caps, or domain‑specific KPIs. |
| **Case Study – Braintrust** | Braintrust built a talent‑matching AI; they defined evals around **match quality**, **time‑to‑fill**, and **bias reduction**, which directly informed roadmap priorities and investor reporting. |
| **Leadership Advice** | - Treat evals as **living documents**, not one‑off deliverables.<br>- Prioritize **interpretability** of metrics so non‑technical stakeholders can act on results.<br>- Embed a **culture of measurement**: celebrate wins when eval thresholds are met, and treat misses as learning opportunities. |

## Practical Steps for AI PMs  

1. **Identify business outcomes** you want the AI to impact.  
2. **Translate outcomes into measurable metrics** (precision, recall, fairness scores, latency, cost).  
3. **Curate or create benchmark datasets** that reflect production data distributions.  
4. **Set explicit success thresholds** and document them in an eval spec.  
5. **Integrate eval runs into the CI pipeline**; monitor drift continuously.  
6. **Review eval results each sprint** to adjust scope, prioritize fixes, or pivot features.  
7. **Communicate findings** through shared dashboards and concise reports to stakeholders.  

## Conclusion  
- **Evals are the new PRD** for AI product management: they provide a concrete, testable, and continuously updated blueprint that aligns technical development with business goals.  
- By institutionalizing evals, teams can **reduce uncertainty**, **accelerate iteration**, and **deliver trustworthy AI products** that meet both user expectations and regulatory standards.