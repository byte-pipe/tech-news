---
title: Slopsquatting: The Supply Chain Attack That Weaponizes AI Hallucinations - DEV Community
url: https://dev.to/nazar-boyko/slopsquatting-the-supply-chain-attack-that-weaponizes-ai-hallucinations-2m2
date: 2026-07-28
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-07-29T12:31:14.204480
---

# Slopsquatting: The Supply Chain Attack That Weaponizes AI Hallucinations - DEV Community

# Slopsquatting: The Supply Chain Attack That Weaponizes AI Hallucinations

## Definition
- Coined by Seth Larson (2025) and popularized by Andrew Nesbitt.  
- An AI model hallucinates a non‑existent package name; an attacker registers that name and waits for developers to install it.  
- Replaces the human typo required for traditional typosquatting with a machine‑generated mistake.

## Why hallucinations make the attack viable
- USENIX Security 2025 study: 19.7 % of package suggestions from 16 LLMs were fake (≈576 k samples).  
- 205 474 distinct hallucinated names were recorded.  
- Open‑source models produced ≥21.7 % fake suggestions; commercial models ≥5.2 %.  
- Hallucinations are reproducible: 43 % appear in every repeat run, 58 % appear in multiple runs.  
- Only 13 % of fake names are simple typos; ~38 % have moderate similarity to real packages, ~49 % are completely fabricated yet plausible.

## Kill chain steps
1. **Model suggestion** – The assistant outputs a fabricated dependency name that follows ecosystem conventions.  
2. **Developer trust** – The name looks legitimate, so the developer accepts it without further verification.  
3. **Installation execution** – Package managers (npm, pip, etc.) run install‑time scripts automatically.  
4. **Credential exfiltration** – The malicious script reads environment variables, credential files, or token files and posts them to an attacker‑controlled endpoint.

## Real‑world evidence
- Researcher Bar Lanyado registered a fake `huggingface-cli` package on PyPI; it received over 15 000 downloads in three months.  
- Alibaba’s GraphTranslator project unintentionally recommended `pip install huggingface-cli` in its README, propagating the malicious name.

## Impact across ecosystems
- **npm (JavaScript)**
  - Lifecycle scripts (`preinstall`, `install`, `postinstall`) run automatically on install.  
  - Mitigations: pnpm v10 (2025) disables scripts by default; npm v12 (June 2026) disables automatic script execution by default.  
- **pip (Python)**
  - Source distributions execute `setup.py` at install time, allowing arbitrary code execution.  
  - Wheels are safer but still vulnerable if a malicious wheel is published.  
- **Composer (PHP)**
  - Similar install‑time script capabilities expose the same risk.  
- **Go modules**
  - Different mechanics but still susceptible to malicious module publishing.

## Defensive considerations
- Keep package managers updated to versions that require explicit consent for install‑time scripts.  
- Verify package existence and integrity (e.g., checksums, signatures) before installing.  
- Incorporate AI‑aware code review: flag generated dependency names for manual validation.  
- Monitor registry activity for newly registered names that match AI‑generated suggestions.