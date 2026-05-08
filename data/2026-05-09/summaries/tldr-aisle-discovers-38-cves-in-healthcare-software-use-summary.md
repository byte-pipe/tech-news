---
title: AISLE Discovers 38 CVEs in Healthcare Software Used by 100,000 Medical Providers | AISLE
url: https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers
date: 2026-05-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-09T07:55:51.174790
---

# AISLE Discovers 38 CVEs in Healthcare Software Used by 100,000 Medical Providers | AISLE

# AISLE Discovers 38 CVEs in Healthcare Software Used by 100,000 Medical Providers

## Overview
- Healthcare digitization is outpacing security, while attackers leverage AI to find vulnerabilities quickly.  
- OpenEMR, an open‑source electronic health record platform, is used by over 100,000 providers, serving more than 200 million patients in 34 languages.  
- OpenEMR 8.0 (released Feb 2026) is ONC‑certified, meeting the full set of Privacy and Security criteria.  

## Findings at a Glance
- AISLE AI analyzer examined the OpenEMR codebase in Q1 2026 and identified **38 CVEs**, representing more than half of all OpenEMR security advisories posted on GitHub during that period.  
- The prior major independent audit (Project Insecurity, 2018) uncovered 23 vulnerabilities after a lengthy manual effort; AISLE found 38 in a single quarter.  
- The most severe issues were SQL injection flaws that could lead to full database compromise, PHI exfiltration, and remote code execution.  

## Notable Findings
- **CVE‑2026‑24908 – SQL Injection in Patient REST API sort parameter**  
  - `sort` value concatenated directly into `ORDER BY` clause without validation or escaping.  
  - Authenticated clients with an OAuth2 token could execute UNION SELECT, time‑based blind injection, and, if the DB user had FILE privileges, arbitrary file read/write and RCE.  

- **CVE‑2026‑23627 – SQL Injection in Immunization search/report (Web UI)**  
  - `patient_id` form parameter split on commas and stitched into `WHERE` clause without parameterization.  
  - Enabled straightforward UNION SELECT data extraction, time‑based injection, and potential file access/RCE.  

- **CVE‑2026‑24487 – FHIR Patient Compartment Bypass in CareTeam**  
  - CareTeam service failed to implement the `IPatientCompartmentResourceService` marker interface, so patient‑scoped OAuth2 tokens did not trigger filtering.  
  - Resulted in exposure of care team data for all patients.  

## Autonomous Issue Fixes
- AISLE generated repository‑native patch proposals that reused OpenEMR’s existing abstractions, authorization patterns, and sanitization helpers.  
- For the critical CVE‑2026‑23627, AISLE produced the patch independently; other fixes were adapted by OpenEMR maintainers from AISLE’s suggestions.  
- This approach reduced remediation time and streamlined integration of security fixes.  

## Partnership for Patient Safety
- Engagement began Dec 2025; initial findings reported Jan 2026.  
- OpenEMR Foundation collaborated closely, reviewing disclosures, iterating on fixes, and shipping most patches in OpenEMR 8.0.0 on Feb 11 2026 (≈4 weeks after first disclosure).  
- Remaining fixes were released across three patch versions in March 2026.  
- In April 2026, AISLE PRO (AI‑powered commit analyzer) was integrated into OpenEMR’s code‑review workflow to catch vulnerabilities before they reach production.  

## From Disclosure to Prevention
- AI‑driven attacks target healthcare for PHI theft, extortion, and service disruption.  
- The OpenEMR case demonstrates a practical defense: autonomous analysis discovers real bugs, rapid patching brings fixes to production, and continuous AI monitoring prevents new issues at the code‑review stage.  

## Full Advisory List – Summary Categories
- **Missing or incorrect authorization** (largest category) – endpoints accepted user‑supplied identifiers without verifying access rights (IDOR).  
- **Absent ACL checks** – some endpoints allowed any authenticated user to perform admin‑level actions.  
- **Authentication bypass** – at least one endpoint could be accessed without any authentication.  

If your organization relies on software for patient care, schedule a demo to see AISLE in action.