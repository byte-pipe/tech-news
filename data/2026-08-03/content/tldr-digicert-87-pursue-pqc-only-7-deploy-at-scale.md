---
title: 'DigiCert: 87% Pursue PQC, Only 7% Deploy at Scale'
url: https://postquantum.com/security-pqc/digicert-quantum-readiness-outlook-2026/
site_name: tldr
content_file: tldr-digicert-87-pursue-pqc-only-7-deploy-at-scale
fetched_at: '2026-08-03T19:33:26.987254'
original_url: https://postquantum.com/security-pqc/digicert-quantum-readiness-outlook-2026/
author: Marin Ivezic
date: '2026-08-03'
published_date: '2026-08-02T19:53:59+02:00'
description: 'DigiCert''s 2026 survey: 87% of organizations pursue PQC initiatives, but only 7% report quantum-safe cryptography across most certificates.'
tags:
- tldr
---

## Table of Contents

July 23, 2026— DigiCert released its second annualQuantum Readiness Outlook, surveying 1,001 IT and cybersecurity decision-makers across the United States, the United Kingdom, and Australia. The headline finding: 87% of organizations report they are planning, testing, or implementing post-quantum cryptography (PQC) initiatives. Only 7% report that more than half of their digital certificates currently use quantum-safe or hybrid cryptography.

DigiCert describes that as an increase of less than two percentage points from itsMay 2025 survey, which found 5% of enterprises had deployed quantum-safe encryption. Google had already set a2029 PQC migration targetbefore the survey was fielded.Executive Order 14412, setting federal migration deadlines for 2030 and 2031, followed in June, after data collection. Those developments increase the urgency surrounding the findings, but they cannot explain the measured result.

The survey was conducted in May 2026 by Propeller Insights, the same firm that ran DigiCert’s 2025 survey. Respondents included professionals responsible for cybersecurity, IT infrastructure, risk management, compliance, and technology strategy.

Other findings from the report:

85% of respondents believe current encryption standards will be broken within a decade. Fifty percent believe it will happen within five years. Only 7% expect current encryption to remain secure for more than ten years.

84% believe at least some of their encrypted data is vulnerable toharvest now, decrypt later (HNDL)attacks. More than a third believe over 25% of their encrypted data is exposed.

When asked what attackers will target first once decryption becomes possible, 58% named financial transaction records and banking data. Crypto assets followed at 53%, then corporate IP and trade secrets (40%), government classified documents (38%), military systems (34%), personal messages (33%), medical records (23%), and leaked documents (21%).

On the execution side, 50% of organizations have conducted quantum risk assessments, 45% have developed transition plans, and 44% have created cryptographic inventories. The top barrier to deployment is legacy system complexity, cited by 26% of respondents, followed by performance impact and budget constraints (both at 19%). Skills gaps accounted for 10%, while interoperability, standards uncertainty, and executive buy-in each registered at 8%. Only 3% cited uncertainty about where to start.

Readiness varies more by industry than by geography. On DigiCert’s self-reported preparedness scores, MedTech led (+24.0), followed by telecommunications and media (+21.6), banking and financial services (+16.2), science and technology (+16.0), and high tech (+13.5). Manufacturing was the most polarized sector (+1.3), with respondents nearly evenly split between those who felt extremely prepared and those who felt not prepared at all. Retail was the only major industry where more respondents reported being unprepared than highly prepared (-7.9).

By country, the United Kingdom had the highest share of organizations identifying themselves as leading edge in quantum readiness (18%), followed by the United States (17%) and Australia (10%).

The largest group of respondents (39%) expects the full transition to take three to five years.

## My Analysis

The most useful data point in DigiCert’s report is not the headline 7%. It is the barrier breakdown.

DigiCert’s 2025 survey found that 69% of organizations recognized the quantum threat but only 5% had deployed quantum-safe encryption. The implicit story a year ago was that the problem was ignorance or indifference at the top.

The 2026 barrier data tells a different story. When respondents identified their single biggest challenge, executive buy-in ranked at only 8%, tied with standards uncertainty and interoperability. Uncertainty about where to start registered at 3%. The top barriers are legacy system complexity (26%), performance impact (19%), and budget constraints (19%). These are implementation problems, not awareness problems. Organizations know what needs to happen. They are stuck on how to make it happen across complex, heterogeneous estates.

This is exactly the pattern I described inQuantum Readyand theApplied Quantum PQC Migration Framework: PQC migration is not a technology upgrade. It is an enterprise transformation where, for every direct cryptographic change, there are approximately three tasks of organizational, procedural, and infrastructural work required to make that change possible, sustainable, and auditable. The 26% citing legacy complexity are discovering that ratio firsthand.

### What the Certificate Lens Shows and What It Hides

A necessary caveat about the 7% headline: this is a certificate-focused metric from a certificate authority. DigiCert measures deployment as the percentage of organizations that have deployed quantum-safe or hybrid certificates on a meaningful scale. That is a legitimate and important measurement, but it captures one dimension of PQC migration. An organization might have completed its cryptographic inventory, be running hybrid key exchange in TLS across its web infrastructure, and have updated its internal PKI policies while still showing as part of the 93% that has not deployed quantum-safe certificates at scale.

Conversely, an organization that has swapped its TLS certificates to hybrid but has not inventoried its embedded cryptography, assessed its vendor dependencies, or addressed its code-signing and authentication infrastructure is not quantum-ready in any meaningful operational sense. MyPQC Readiness Self-Assessment Scorecardtracks eleven domains precisely because certificate deployment alone does not capture the scope of the problem.

That said, the trajectory is genuinely concerning. Less than two percentage points in a year, during a period when NIST standards were gaining traction andregulatory deadlines were hardening globally, is slow. If even a two-point annual rate held (and DigiCert’s own data suggests the actual rate may be lower), enterprises would reach roughly 15% certificate deployment by the time NIST’sIR 8547deprecation window opens after 2030. Two data points do not make a trend line, but the direction should concern every CISO reading this.

### The HNDL Numbers Are High, the Signature Gap Is Silent

The HNDL self-assessed exposure numbers are striking: 84% believe at least some of their encrypted data is vulnerable to harvest-and-decrypt attacks. That level of recognition would have been difficult to find in enterprise surveys even recently, and it confirms that theHNDLmessage has penetrated the enterprise security community.

What the report does not address, and what I find more telling than what it includes, is theTrust Now, Forge Later (TNFL)threat. HNDL threatens data confidentiality: encrypted data harvested today can be decrypted once acryptographically relevant quantum computer (CRQC)exists. TNFL threatens digital trust itself: the ability to forge digital signatures retroactively, undermining code signing, software updates, certificate authorities, and the entire PKI infrastructure that DigiCert’s own business depends on.

For a report produced by a certificate authority, the omission is notable. The distinction between key establishment (where HNDL operates) and digital signatures (where TNFL operates) is not academic.EO 14412splits these into separate deadlines for exactly this reason: key establishment by December 31, 2030, and digital signatures by December 31, 2031. The migration paths, the performance trade-offs, and the urgency profiles are different for each. A survey that collapses them into a single “quantum readiness” question misses the fact that most organizations are further behind on signature migration than on key establishment, because the ecosystem tooling for PQC signatures is less mature and the performance overhead is more severe.

### The Timeline Beliefs Are Opinions, Not Evidence

Fifty percent of respondents believe current encryption will be broken within five years. I would note that this finding tells us about sentiment, not aboutCRQCengineering timelines. The relevant question for a CISO is not when individual IT professionals believe encryption will be broken. It is what the publishedresource estimatesshow, what thecapability milestonesindicate, and what the regulators, insurers, and counterparties have already decided regardless of the physics.

As I have argued in detail:forget Q-Day predictions. Regulators, insurers, investors, and clients are your new quantum clock.The reason to migrate is no longer contingent on when a CRQC arrives. NIST will deprecate quantum-vulnerable algorithms after 2030 and disallow them after 2035. The UK’s NCSC targets discovery complete by 2028 and high-priority migration by 2031. EO 14412 directs the FAR Council to require covered federal contractors to comply with FIPS PQC standards by 2030. Google has committed to completing its own migration by 2029 and Microsoft has set a similar target. These instruments carry different legal force (binding executive directives, draft standards, indicative national timelines, corporate engineering goals), but they all point in the same direction: the operational window for treating PQC migration as discretionary is closing. These are not Q-Day predictions. They are institutional deadlines, and they do not care when the CRQC arrives.

The DigiCert survey data indirectly confirms this shift: only 3% of respondents identify uncertainty about where to start as their biggest challenge, and only 8% cite standards uncertainty as the top barrier. The initial algorithm-selection question is settled. ML-KEM, ML-DSA, and SLH-DSA are finalized FIPS standards, and organizations can and should be migrating now. The starting line is behind most organizations.

### The Geographic Blind Spot

The survey covers three Anglophone markets: the United States (500 respondents), the United Kingdom (251), and Australia (250). This is a reasonable sample for those three countries, but it excludes continental Europe (where the EU coordinated roadmap sets its own deadlines), the Gulf states (where quantum investment is accelerating rapidly), and Asia beyond Australia (where South Korea, Japan, India, and Singapore all have active PQC programs and, in some cases, sovereign algorithm development).

The absence of EU member state respondents is the most significant gap. The EU’s coordinated PQC roadmap calls on member states to develop transition plans and begin migration, with high-risk use cases targeted for transition by 2030. EU-based enterprises operate within distinct regulatory, certification, and assurance requirements, and in some cases face different algorithm preferences than their Anglophone counterparts. A survey that wants to inform global quantum readiness should eventually reflect that.

### What the Data Actually Tells You

Strip away the framing and the DigiCert survey delivers one clear, actionable message: the PQC migration problem has changed character. It is no longer a persuasion problem. CISOs and CTOs do not need to be convinced that the quantum threat is real or that PQC migration is necessary. The 87% planning figure and the near-zero “don’t know where to start” number confirm that.

It is now an execution problem, and execution problems are harder to solve with awareness campaigns and vendor pitch decks. They requirecryptographic inventoriesthat actually cover the estate, migration frameworks that sequence the work by priority and dependency, vendor governance programs that extract real delivery commitments, and budget processes that treat PQC as a multiyear capital program rather than a discretionary line item.

ThePQC Migration Frameworkexists precisely for this phase. For organizations still in the 87% who are planning but not deploying, the question is no longer whether to start. It is whether you have a structured methodology for converting plans into operational cryptographic change across your enterprise, or whether you are accumulating slideware while the deadline clock runs.

DigiCert’s own data provides the answer for most organizations. Less than two percentage points of certificate deployment in a year. At that velocity, the deadlines will arrive first.

Marin Ivezic

Follow on X

Send an email

August 2, 2026

 7 minutes read
 

 Share

 
X

 
LinkedIn

 
Reddit

 
Flipboard

 
WhatsApp

 
Telegram

 
Viber

 
Line

 
Share via Email

 
Print