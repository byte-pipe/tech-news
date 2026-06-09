---
title: Auditing GitLab: The CI/CD Kill Chain - Black Hills Information Security, Inc.
url: https://www.blackhillsinfosec.com/auditing-gitlab-the-ci-cd-kill-chain/
date: 2026-06-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-10T07:44:22.427554
---

# Auditing GitLab: The CI/CD Kill Chain - Black Hills Information Security, Inc.

# Auditing GitLab: The CI/CD Kill Chain

## Overview
- Phil Miller, BHIS security consultant, created **GoGatoZ**, a Go‑based tool for auditing GitLab CI/CD pipelines.
- The blog details three large‑scale scans of public GitLab projects, the methodology, findings, and tool capabilities.

## Motivation
- CI/CD pipelines (gitlab-ci.yml) often contain misconfigurations that allow attackers to inject commands, hijack runners, exfiltrate variables, and conduct supply‑chain attacks.
- Prior work (Part I) used ad‑hoc scripts to locate secrets; GoGatoZ consolidates and expands that functionality.

## GoGatoZ Features
- **Five operational modes**  
  - **Search** – discover projects via GitLab API with filters (language, topics, file paths, code content).  
  - **Enumerate** – parse `.gitlab-ci.yml` files, resolve recursive includes, and identify vulnerabilities.  
  - **Parse** – locally transform and deduplicate results, convert formats.  
  - **Attack** – exploit identified misconfigurations (CI injection, secret extraction, runner targeting).  
  - **Pivot** – combine enumeration, attack, and credential harvesting in a breadth‑first search loop.  
- Includes a **Model Context Protocol (MCP) server** for AI‑assisted workflows, enabling natural‑language interaction and storage of findings in SQLite.  
- Supports **SOCKS5 proxies** (authenticated/unauthenticated).  
- For the audit, only Search, Enumerate, Parse, and Report modes were used; Attack mode is demonstrated in a separate CTF course.

## Scan Methodology
### Phase 1 – Broad Sweep (DevOps Keywords)
- Queried public GitLab projects with 20 generic DevOps terms (e.g., `devops`, `kubernetes`, `terraform`).  
- Filtered for presence of `.gitlab-ci.yml`.  
- Results: 1,917 raw hits → 1,715 unique projects scanned.  
- Findings: 64 % of projects had at least one security issue; 7,331 total findings, including 1,580 HIGH severity. Notable outlier: a single project with 363 findings (200 HIGH).

### Phase 2 – Fortune 500 Targeted Scan
- Used 2023 Fortune 500 company list (462 usable names after removing overly generic terms).  
- Executed automated searches per company.  
- Results: 1,738 unique public projects identified.  
- Findings: similar high rate of misconfigurations; many projects were interview assignments or homework repositories.

### Phase 3 – Industry‑Specific Scan
- Focused on law firms, financial services, logistics, and trucking companies.  
- Applied same search/enumeration pipeline to gather sector‑specific data.  
- Contributed to overall total of 3,757 public projects examined across all phases.

## Key Findings
- **Widespread CI/CD misconfigurations**: a majority of public GitLab repositories expose exploitable settings.  
- **High‑severity issues** are common, often stemming from insecure variable handling, permissive runner configurations, and unvalidated includes.  
- **Supply‑chain risk** is significant even without source‑code secrets; attackers can gain persistent access via pipeline abuse.

## Ethical Considerations
- The tool can be misused; author acknowledges the dual‑use nature but proceeds to publish for defensive research.  
- A full attack chain is available only within a controlled CTF environment.

## References & Influences
- Inspired by talks on GitHub Actions security:  
  - RomHack 2024 – “The dark side of GitHub actions” (Adnan Khan)  
  - DEF CON 32 – “Grand Theft Actions: Abusing Self‑Hosted GitHub Runners” (Adnan Khan, John Stawinski)

## Conclusion
- GoGatoZ provides an end‑to‑end solution for discovering, enumerating, and analyzing GitLab CI/CD vulnerabilities at scale.  
- The three‑phase audit demonstrates that CI/CD pipelines are a fertile attack surface across diverse industries, underscoring the need for systematic security reviews and hardened configurations.