---
title: "Boffin claims Microsoft's supposed quantum leap does not compute due to 'basic Python errors'"
url: https://www.theregister.com/research/2026/06/24/boffin-claims-microsofts-supposed-quantum-leap-does-not-compute-due-to-basic-python-errors/5260489
date: 2026-06-24
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-25T05:56:43.758049
---

# Boffin claims Microsoft's supposed quantum leap does not compute due to 'basic Python errors'

# Boffin claims Microsoft's supposed quantum leap does not compute due to 'basic Python errors'

## Background
- In February 2025 Microsoft announced a quantum breakthrough called **Majorana**, claiming it would enable a functional quantum computer within years rather than decades.  
- The approach relies on Majorana particles, which have never been directly observed.  
- Earlier attempts led to retractions; the 2025 claim asserted both observation and control of Majorana particles for a topological superconductor.

## Legg’s Critique (Nature paper, June 24 2026)
- Dr Henry Legg, lecturer at the University of St Andrews, published a peer‑reviewed analysis titled *“On the robustness of topological gap detection via transport.”*  
- Main arguments:  
  - Microsoft’s “Topological Gap Protocol” (TGP) software contained **basic Python errors** that mis‑represented data.  
  - The code **antisymmetrized bias voltage using array indices** instead of physical values, effectively reversing data incorrectly.  
  - A hard‑coded filter (`zbp_cluster_numbers=[1]`) displayed only the largest purported topological region, hiding additional regions that passed the protocol. Changing it to include `[1,2]` reveals a second region.  
  - Raw transport data omitted from the original 2025 paper shows considerable disorder, inconsistent with the existence of a topological gap.  
  - Microsoft claimed to have investigated “the only region passing the protocol,” which Legg says is false.  
  - Overall, the omitted data and coding mistakes led to overstated claims about Majorana detection and control.

## Microsoft’s Rebuttal
- Dr Chetan Nayak, technical fellow and corporate VP of Microsoft’s quantum hardware group, reaffirmed confidence in the results and roadmap.  
- The company argues:  
  - The “off‑by‑one‑pixel bug” in TGP processing is inconsequential.  
  - Their signal measurements were not meant to be exhaustive.  
  - Legg’s analysis focuses narrowly on transport data and ignores capacitance measurements central to the study.  
  - No alternative physical model is offered to explain the observed capacitance signals.  
  - Their rebuttal has been accepted and published by *Nature*.

## Assessment and Outlook
- Legg maintains that **Majorana 2** (announced June 2026) is not a customer‑ready device and lacks evidence of a true qubit or superposition capability.  
- He characterizes Microsoft’s claim of “1,000 times more reliable” as referring only to the lifetime of a classical parity bit, not a quantum bit.  
- The dispute highlights broader concerns about data transparency, reproducibility, and the reliability of software pipelines in cutting‑edge quantum research.