---
title: Anthropic launches critical infrastructure program and free OSS Scanner for open source - SiliconANGLE
url: https://siliconangle.com/2026/10/08/anthropic-launches-critical-infrastructure-program-and-free-oss-scanner-for-open-source
date: 2026-10-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-09T10:17:06.797946
---

# Anthropic launches critical infrastructure program and free OSS Scanner for open source - SiliconANGLE

# Anthropic launches critical infrastructure program and free OSS Scanner for open source

## Key announcements
- Anthropic PBC introduced two initiatives under the **Anthropic Cyber Mission**:
  - A Critical Infrastructure Defense Program that brings Anthropic’s frontier models and engineers to operators of power grids, water systems, and other essential facilities.  
  - OSS Scanner, a free service that provides periodic vulnerability scans for eligible open‑source projects using Anthropic’s strongest models.  

## Critical Infrastructure Defense Program
- Targets operational technology (OT) in plants, substations, and water systems where equipment cannot be taken offline for patches.  
- Eleven founding partners have signed on, including consulting firms (Accenture, Booz Allen Hamilton, Deloitte, PwC) and security vendors (Dragos, Insane Cyber, Nozomi Networks, CrowdStrike, Palo Alto Networks, Hitachi, Rockwell Automation).  
- Partners are already using Anthropic’s Claude model to identify and remediate vulnerabilities; additional partners and sectors are expected to join in coming months.  
- Booz Allen’s Andrew Turner warned that OT is “the next frontier for autonomous AI‑enabled attacks,” emphasizing the speed and control AI could gain over industrial processes.  

## OSS Scanner for open source
- Originated from Anthropic’s internal disclosure backlog: >29,000 candidate vulnerabilities found in six months, ~6,000 manually reviewed.  
- The service automates delivery of vulnerability reports—including reproducible exploits, candidate patches, and code‑history bisections—directly to maintainers.  
- Inspired by Google’s OSS‑Fuzz; reports are sent without human review to accelerate delivery, accepting occasional errors (e.g., mis‑rated severity).  
- Early testing by penetration‑testing experts cleared 85 of 97 critical/high‑severity findings for disclosure; most of the remaining reports were duplicates or known issues.  
- wolfSSL reported that 5 of its 74 early‑trial reports became CVEs.  

## Testing, accuracy, and enrollment
- Anthropic evaluated scanner accuracy before broader release, achieving a high validation rate in expert reviews.  
- Core maintainers can enroll by submitting a pull request to an Anthropic GitHub repository.  
- Eligibility follows OSS‑Fuzz criteria of “critical impact on infrastructure and user security,” assessed case‑by‑case.  
- Projects lacking resources for raw findings will continue to receive human‑verified reports via Anthropic’s existing disclosure process.  

## Funding and sustainability
- The Defender Advantage Fund, created in August, finances the free OSS Scanner.  
- Anthropic has also contributed to the Python Software Foundation, Apache Software Foundation, Alpha‑Omega, and the OpenSSF through the Linux Foundation.  

## Background and outlook
- Both launches build on lessons from Project Glasswing, which gave vetted organizations access to Claude Mythos before folding into an expanded Cyber Verification Program.  
- Anthropic believes AI will favor defenders within two years; while exploitation costs decline, verification and remediation remain labor‑intensive, especially for OT that may require decades before a safe fix can be deployed.  

---  

*The article was written by Duncan Riley and updated on October 8 2026.*