---
title: Anthropic launches critical infrastructure program and free OSS Scanner for open source - SiliconANGLE
url: https://siliconangle.com/2026/10/08/anthropic-launches-critical-infrastructure-program-and-free-oss-scanner-for-open-source
site_name: tldr
content_file: tldr-anthropic-launches-critical-infrastructure-program
fetched_at: '2026-10-09T10:16:30.559549'
original_url: https://siliconangle.com/2026/10/08/anthropic-launches-critical-infrastructure-program-and-free-oss-scanner-for-open-source
author: Duncan Riley
date: '2026-10-09'
published_date: '2026-10-08T22:42:53+00:00'
description: Anthropic launches critical infrastructure program and free OSS Scanner for open source - SiliconANGLE
tags:
- tldr
---

UPDATED 18:42 EDT / OCTOBER 08 2026

 
SECURITY

### Anthropic launches critical infrastructure program and free OSS Scanner for open source

byDuncan Riley

Anthropic PBC todaylaunched a programthat brings its frontier models and onsite engineers to the security companies protecting power grids, water systems and other critical infrastructure.

OSS Scanner, launched with it, offers open-source projects free periodic vulnerability scans from the company’s strongest models. Both fall under a new effort Anthropic calls the Anthropic Cyber Mission.

The Critical Infrastructure Defense Program starts with the outside providers that operators of every size already rely on for advice on which fixes are safe to apply to a running system. Eleven of those providers signed on as founding partners.

Accenture plc, Booz Allen Hamilton Inc., Deloitte & Touche LLP and PricewaterhouseCoopers LLP come from the consulting side, where they run security programs for operators. Security vendors make up the biggest bloc, with industrial specialists Dragos Inc., Insane Cyber Inc. and Nozomi Networks Inc. joining CrowdStrike Holdings Inc. and Palo Alto Networks Inc. Hitachi Ltd. and Rockwell Automation Inc. build and patch the hardware itself.

The program is aimed at operational technology in plants, substations and water systems, where equipment built to run for decades often cannot be taken offline for a patch. Known flaws can sit there for years. Anthropic said several partners are already using Claude to fix vulnerabilities and to help their customers do the same. More partners and sectors are due to join over the coming months.

Andrew Turner, president of commercial cyber at Booz Allen, called operational technology “the next frontier for autonomous AI-enabled attacks” in comments published with the announcement. What matters now, he said, is how much control artificial intelligence can gain over an industrial process and how fast.

The announcement leaves out the commercial terms. Axios notedin its coveragethat Anthropic has not said whether partners get free model access or who covers the computing costs. The same report questioned how partners will test and deploy fixes without disrupting utility operations.

The open-source half of today’s news grew out of a backlog in Anthropic’s own disclosure work. Of the more than 29,000 candidate vulnerabilities its models turned up in widely used software over the past six months, staff have manually reviewed about 6,000. A growing number of maintainers who received early reports asked for the whole unreviewed batch, proposed patches included, and nearly 5,000 such reports have gone out so far.

OSS Scanner turns that arrangement into a standing service for other eligible projects. Google LLC’s OSS-Fuzz, which runs fuzzers against open-source code, inspired the setup.

Every report includes a self-contained reproducer. Early tester Anton Arapov of the OpenSSL Corporation said a report with a real exploit attached is “basically job done for an engineer.” Where the model can manage it, a candidate patch comes with the write-up, and a bisection of the code history shows when the flaw was introduced.

Reports from the new service go straight to maintainers without human review so they arrive faster. Some will contain mistakes as a result, such as a wrong severity rating, Anthropic said.

To gauge how often that happens, Anthropic tested the scanner’s accuracy before opening it to more projects. The expert penetration testers who vet the company’s coordinated disclosures checked 97 critical and high-severity findings from an early version across 48 projects and cleared 85 for disclosure.

Of the other 12, all but one were real bugs that duplicated known issues or other findings from the scan. Embedded encryption library developer wolfSSL Inc. said all but two of the 74 reports it received during early trials were valid and that five became CVEs.

Core maintainers can enroll by submitting a pull request to an Anthropic GitHub repository. Eligibility follows the OSS-Fuzz test of “critical impact on infrastructure and user security,” with decisions made case by case. Projects without the staff to keep up with raw findings will still get human-verified reports through Anthropic’s existing disclosure process.

The Defender Advantage Fund that Anthropic set upin Augustpays to keep the scanner free. The company has also put money into the Python Software Foundation and the Apache Software Foundation, as well as Alpha-Omega and OpenSSF through the Linux Foundation.

Both launches draw on lessons from Project Glasswing. That program gave vetted organizations access to Claude Mythos from April until it was folded into an expanded Cyber Verification Programearlier this week. Finding vulnerabilities has never been easier, according to Anthropic. Verifying, prioritizing and fixing them remains hard, and the company said Glasswing has not yet cut cyber risk by enough.

Anthropic expects AI to favor defenders within two years. For now the cost of exploiting a flaw keeps falling, and verifying and repairing one is still slow work that depends on people. With operational technology, a fix may have to wait until it can go safely onto running machinery, and in rare cases that could take decades.

##### Image: Anthropic

# A message from John Furrier, co-founder of SiliconANGLE:

Support our mission to keep content open and free by engaging with theCUBE community.Join theCUBE’s Alumni Trust Network, where technology leaders connect, share intelligence and create opportunities.

* 15M+ viewers of theCUBE videos, powering conversations across AI, cloud, cybersecurity and more
* 11.4k+ theCUBE alumni— Connect with more than 11,400 tech and business leaders shaping the future through a unique trusted-based network

### Are you an AWS customer?Support SiliconANGLE financially by buying your AWS services from ourMarketplace portal page and links:https://siliconangle.com/aws-marketplace/

 

##### About SiliconANGLE Media

SiliconANGLE Media is a recognized leader in digital media innovation, uniting breakthrough technology, strategic insights and real-time audience engagement. As the parent company of 
SiliconANGLE
, 
theCUBE Network
, 
theCUBE Research
, 
CUBE365
, 
theCUBE AI
 and theCUBE SuperStudios — with flagship locations in Silicon Valley and the New York Stock Exchange — SiliconANGLE Media operates at the intersection of media, technology and AI.

Founded by tech visionaries John Furrier and Dave Vellante, SiliconANGLE Media has built a dynamic ecosystem of industry-leading digital media brands that reach 15+ million elite tech professionals. Our new proprietary theCUBE AI Video Cloud is breaking ground in audience interaction, leveraging theCUBEai.com neural network to help technology companies make data-driven decisions and stay at the forefront of industry conversations.

##### LATEST STORIES

* Alphabet spinoff Isomorphic Labs reportedly raising funding at up to $50B valuation
* CoreWeave Forge aims to speed up the AI improvement loop
* AI agent developer Manus raises $500M+ at reported $4B valuation
* CoreWeave makes the case for an open, full-stack AI cloud
* Automation Anywhere acquires Boost.ai to expand customer-facing voice AI
* Liquid AI builds personal AI around device-level context

##### LATEST STORIES

* Alphabet spinoff Isomorphic Labs reportedly raising funding at up to $50B valuationAI- BYMARIA DEUTSCHER.52 MINUTES AGO
* CoreWeave Forge aims to speed up the AI improvement loopAI- BYSLOANE KALI FAYE.1 HOUR AGO
* AI agent developer Manus raises $500M+ at reported $4B valuationAI- BYMARIA DEUTSCHER.2 HOURS AGO
* CoreWeave makes the case for an open, full-stack AI cloudAI- BYSLOANE KALI FAYE.3 HOURS AGO
* Automation Anywhere acquires Boost.ai to expand customer-facing voice AIAI- BYKYT DOTSON.5 HOURS AGO
* Liquid AI builds personal AI around device-level contextAI- BYJONATHAN ANTHONY.6 HOURS AGO