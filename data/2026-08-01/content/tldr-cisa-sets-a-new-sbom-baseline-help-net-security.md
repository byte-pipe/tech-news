---
title: CISA sets a new SBOM baseline - Help Net Security
url: https://www.helpnetsecurity.com/2026/07/30/cisa-sbom-guidance-updated/
site_name: tldr
content_file: tldr-cisa-sets-a-new-sbom-baseline-help-net-security
fetched_at: '2026-08-01T19:28:20.414211'
original_url: https://www.helpnetsecurity.com/2026/07/30/cisa-sbom-guidance-updated/
author: Anamarija Pogorelec
date: '2026-08-01'
published_date: '2026-07-30T12:23:36+00:00'
description: CISA updates SBOM guidance with new minimum elements covering modern software, improving software supply chain transparency and automation.
tags:
- tldr
---

Anamarija Pogorelec
, Senior Staff Writer, Help Net Security
 

July 30, 2026
 

Share
 

# CISA sets a new SBOM baseline

The US Cybersecurity and Infrastructure Security Agency (CISA), together with its co-authoring partners, has released the 2026 Minimum Elements for a Software Bill of Materials (SBOM), replacing the 2021 guidance published by the National Telecommunications and Information Administration (NTIA).

An SBOM is a list of the components that make up a software package and their supply chain relationships. It helps organizations understand what is included in their software, assess software supply chain risks, and make informed security decisions.

The revision incorporates feedback received during a 2025 public comment period and applies the minimum elements to SBOMs for all software.

Theupdateintroduces new minimum SBOM elements, including component hash algorithms, component licenses, the name of the SBOM generation tool, and generation context. It also renames several existing fields to improve clarity and consistency, making SBOMs easier to use for automated software supply chain and vulnerability management.

### Future areas for SBOM development

The document ends with a Discussion section looking at four tricky areas where the guidance may need to grow: cloud software, AI, checking that an SBOM is trustworthy, and linking SBOMs to security alerts.

Cloud and software-as-a-service (SaaS) products are hard to pin down because responsibility is split between the company that builds the service and the one that runs it, and because the software changes constantly. Producing a fresh SBOM every time could bury both sides in paperwork, so the authors suggest tools like automated snapshots can help, and they leave the door open to adding cloud-specific elements later.

AI raises a similar problem. Because AI is still software, the standard elements already capture a lot, but AI systems have extra pieces – such as the “model cards” and “data cards” that describe how a model was built and trained – that a normal SBOM misses. For now, CISA holds off on adding AI-specific fields and instead points readers toseparateAI SBOM guidance the G7 published in May 2026.

The last two topics are about getting value out of SBOMs. To help recipients confirm an SBOM is genuine and unaltered, the guidance adds a digital signature field, though it notes that fully verifying an SBOM’s accuracy goes beyond what these minimum elements cover. And by connecting an SBOM to security alerts (using formats like VEX and CSAF that flag which components are vulnerable), an organization can quickly check whether a newly discovered flaw affects its software.

Read more:

* AIBOMs are the new SBOMs: The missing link in AI risk management

More about

* AI
* CISA
* cybersecurity
* open source
* SaaS
* software

Share