---
title: Abbott probes two cyber incidents amid extortion claims
url: https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/
site_name: tldr
content_file: tldr-abbott-probes-two-cyber-incidents-amid-extortion-c
fetched_at: '2026-07-22T11:37:38.251804'
original_url: https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/
date: '2026-07-22'
description: Abbott Laboratories is investigating two separate cybersecurity incidents after confirming unauthorized access to internal legacy Exact Sciences systems in its Cancer Diagnostics business, while also investigating a separate claim that attackers breached its LabCentral portal and stole company data.
tags:
- tldr
---

# Abbott probes two cyber incidents amid extortion claims

 By 

###### Lawrence Abrams

* July 17, 2026
* 04:45 PM
* 0

Abbott Laboratories is investigating two separate cybersecurity incidents after confirming unauthorized access to internal legacy Exact Sciences systems in its Cancer Diagnostics business, while also investigating a separate claim that attackers breached its LabCentral portal and stole company data.

The company confirmed the Cancer Diagnostics incident after the ShinyHunters extortion gang added Abbott to its data leak site, initially threatening to publish allegedly stolen data after July 18 unless the company negotiated with the group, before later extending the deadline to July 21.

Abbott's Exact Sciences is listed on ShinyHunters extortion site
Source: BleepingComputer

When BleepingComputer asked Abbott about the alleged ShinyHunters incident, Abbott directed BleepingComputer to a statement published on its website.

"Abbott is investigating a cyber incident in which there was unauthorized access to a limited number of internal systems in our Cancer Diagnostics business only,"the company said.

"This does not impact any business operations, product or product availability, manufacturing or lab operations, or our ability to serve patients."

Abbott added that the security incident has not impacted any other Abbott businesses or systems, and said the legacy Exact Sciences systems are separate from Abbott's.

The company said it activated its incident response procedures after it learned of the incident, engaged cybersecurity experts, and notified law enforcement.

Abbott also stated that it does not expect the incident to have a material impact on its business or financial results.

ShinyHunters claimed to BleepingComputer that it gained access through a vishing attack targeting several Abbott employees in mid-June. According to the threat actor, the attack allowed it to compromise a Microsoft Entra single sign-on (SSO) account and gain access to internal systems.

Since last year, the extortion group has been conductingsocial engineering campaignsthat target employees' Microsoft Entra, Okta, and Google SSO accounts.

After gaining access to a corporate SSO account, the threat actors steal data from connected SaaS applications such as Salesforce, Microsoft 365, Google Workspace, SAP, Slack, Adobe, Atlassian, Zendesk, Dropbox, and many others.

The extortion gang has been increasingly targeting medtech companies, includingMedtronic, OneMedical, and AdaptHealth. BleepingComputer has learned that ShinyHunters was also behind theiRhythm data breachand targeted Stryker soon afterthe company recoveredfrom adestructive Iranian data-wiping attack.

When asked what data was allegedly stolen, ShinyHunters claimed it exfiltrated data from Microsoft Entra, ServiceNow, SharePoint, Databricks, and Coupa, including internal documents, contracts, and customer information.

The threat actor further claimed to have stolen more than 30 million rows of customer personally identifiable information (PII) from multiple datasets containing names, email addresses, phone numbers, physical addresses, dates of birth, and more than one million Social Security numbers.

The group also claimed to have stolen over 22 million client notes containing doctor-patient conversations, more than 20 million medical orders, and customer agreements and NDAs.

BleepingComputer has not independently verified the threat actor's claims regarding the stolen data.

## Alleged breach at LabCentral customer portal

The second incident involves a threat actor known as ShadowByt3$, who contacted BleepingComputer claiming to have breached Abbott's Core Laboratory diagnostics business through its LabCentral customer portal.

The threat actor said it breached the unit via its LabCentral customer portal using compromised customer credentials after identifying what it described as a "weak point" in the environment.

According to the threat actor, they gained access on July 4, 2026, after which they slowly exfiltrated files by targeting API endpoints.

ShadowByt3$ claims the stolen data includes CE manufacturing certificates, operation manuals, technical specifications, regulatory documentation, product requirement archives, calibrator value assignments, assay files, and other product documentation related to Abbott's laboratory diagnostic systems.

The group says no customer data was stolen, but claims it obtained sensitive business documents and intellectual property. It also provided BleepingComputer with screenshots and a file listing as purported proof of the intrusion.

Abbott confirmed to BleepingComputer that it is aware of the "potential" cyber incident but disputed the threat actor's characterization of the data it claims to have stolen, stating that all data stored in the environment is public and not sensitive.

"LabCentral is an externally facing third-party hosted portal used by Abbott's core laboratory diagnostics business," an Abbott spokesperson told BleepingComputer.

"It houses publicly available technical product reference documents, including operating manuals, troubleshooting checklists and product specifications, and does not contain proprietary/sensitive customer or business information."

At this time, neither ShinyHunters nor ShadowByt3$ has publicly released data they claim to have stolen from Abbott.

## Test every layer before attackers do

Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.

The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.

Get the whitepaper

### Related Articles:

NAIC says public data stolen in ShinyHunters' PeopleSoft breach

Kodak confirms data breach claimed by ShinyHunters extortion gang

Nottingham University data breach affects over 450,000 students

Charter confirms data breach after ShinyHunters extortion threat

7-Eleven confirms data breach claimed by the ShinyHunters gang