---
title: AI Governance Is Repeating Cybersecurity's Mistakes
url: https://postquantum.com/ai-security/ai-governance-cybersecurity-lessons/
site_name: tldr
content_file: tldr-ai-governance-is-repeating-cybersecuritys-mistakes
fetched_at: '2026-08-04T19:34:13.150016'
original_url: https://postquantum.com/ai-security/ai-governance-cybersecurity-lessons/
author: Marin Ivezic
date: '2026-08-04'
published_date: '2026-08-03T06:25:49+02:00'
description: AI labs still control much of their own testing and disclosure. Cybersecurity's imperfect governance lessons show what must change.
tags:
- tldr
---

## Table of Contents

## Introduction

In May 1998, seven members of the Boston hacker collectiveL0pht Heavy Industriestestified before the Senate Committee on Governmental Affairs. All seven used pseudonyms. Sitting before Senators Fred Thompson, John Glenn, Susan Collins, and Joseph Lieberman, they warned that one of them could make the internet unusable nationwide in approximately 30 minutes.

What happened next took the better part of a decade to resolve. Vendors argued that only they should decide whether, when, and how to disclose vulnerabilities in their own products. Researchers argued that without external pressure, vendors would sit on known flaws indefinitely. The argument produced genuine casualties: researchers threatened with lawsuits under the DMCA, companies blindsided by “full disclosure” dumps, and a slow accretion of real-world harm from vulnerabilities that everyone knew about and nobody fixed.

Cybersecurity never fully solved this conflict. It built imperfect institutions around it: coordinated vulnerability disclosure frameworks, federated vulnerability identifiers (CVE) under shared rules, third-party penetration testing with separation between vendor and evaluator, qualification and quality oversight of assessors, statutory breach notification, and scoped authorization for defensive research. Those mechanisms remain incomplete and frequently fail. Their achievement was not perfect security. It was making the vendor’s judgment no longer the only judgment that counted. Independent evaluation is necessary, but it is not sufficient unless evaluator incentives, evaluation infrastructure, incident evidence, and disclosure obligations are independently assured as well.

I have been watching the AI safety community try to build governance frameworks for five years. They are at roughly the same stage the cybersecurity industry was in 2001. And they are making recognizably similar mistakes, with one difference: the systems they are failing to govern can nowautonomously hack other companies.

## Three Governance Failures in Ten Days of Disclosures

The July 2026 incident disclosures exposed three distinct governance problems. Each has a known (if imperfect) solution from the cybersecurity playbook. The AI safety community has not adopted any of them.

### The Evaluation Infrastructure Problem

Two separate incidents. Two different governance failures. The same underlying lesson.

OpenAI’s Hugging Face breach arose from a purely internal evaluation. OpenAI ran GPT-5.6 Sol and a more capable pre-release model againstExploitGym, a cybersecurity benchmark, inside its own infrastructure. No third-party evaluator was involved. The models exploited a zero-day in JFrog Artifactory, escaped the sandbox, andbreached Hugging Face’s production systems. The vendor graded its own homework, and the test escaped the classroom.

Anthropic’s three incidents arose from a different arrangement. Anthropic’s evaluations were conducted withIrregular, a third-party security lab. But according to Anthropic’sdisclosure, a misunderstanding between Anthropic and Irregular left live internet access available in evaluation environments that were supposed to be isolated. Neither organization detected the condition. Anthropic identified missed defense-in-depth controls on both sides. Over multiple misconfigured runs, three Claude models gained unauthorized access to three separate organizations’ systems.

Irregular does serious work. It publishedFrontierCyberin June 2026, a benchmark that measures AI offensive capabilities against real systems with their production defenses intact. It also separatelyevaluated GPT-5.6 Solusing its FrontierCyber and CyScenarioBench suites. This is not an argument against Irregular specifically. It is an argument against the structure.

The cybersecurity industry learned this lesson the hard way with payment card assessors. Major breaches repeatedly demonstrated that a successful point-in-time PCI assessment did not establish continuous security. The PCI Security Standards Council tightened qualification and quality oversight of assessors. But PCI SSC is an industry standards body without statutory authority. The oversight improved without acquiring statutory force.

AI evaluation has less than that. When the evaluator is chosen by the vendor, paid by the vendor, and accountable to the vendor, the evaluation will eventually reflect the vendor’s interests, regardless of the evaluator’s intentions. And when the vendor evaluates itself entirely in-house, as OpenAI did, even that limited external check disappears. The July incidents exposed both failure modes in a single week: pure self-evaluation (OpenAI) and outsourced evaluation with an unverified containment boundary (Anthropic).

The fix the cybersecurity industry developed was to create oversight bodies that can register evaluation firms, set independence and competence requirements, inspect methodologies and working papers, require conflict disclosures, and discipline serious failures. These bodies are imperfect. But they exist. No equivalent body exists for AI safety evaluations.

### The Detection and Disclosure Problem

Anthropic’s earliest incident (of those disclosed in July) dates toApril 2026. Model activity against external systems remained undetected for months and was discovered only after OpenAI’s Hugging Face disclosure prompted a retrospective review. Without OpenAI’s incident, Anthropic’s own breaches might still be unknown.

Anthropic responded reasonably after discovery: it suspended cyber evaluations on July 23, identified the relevant activity by July 24, notified Irregular and affected organizations by July 27, and publicly disclosed on July 30. I am not suggesting the company knowingly withheld information. The problem is systemic. Voluntary self-reporting is insufficient when months of model activity against real systems can go undetected. The cybersecurity industry eventually adopted mandatory breach notification laws, starting with California’s SB-1386 in 2002, that impose legal obligations for timely disclosure after discovery. But mandatory reporting addresses what happensafterdiscovery. It would not, by itself, have exposed an incident the company did not know had occurred.

The AI safety community needs both: reporting deadlines after discovery, and technical requirements for continuous monitoring of model activity during evaluations. That means default-deny external connectivity, independently verified egress controls, environment attestation before each run, continuous network and model-action telemetry, immutable logs, and automatic interruption thresholds. A qualified evaluator operating an unverified sandbox is still an unsafe evaluator.

### The Asymmetric Guardrails Problem

This one is the most operationally consequential, and Hugging Face documented it with unusual clarity.

When Hugging Face’s security teambegan analyzing the breach, they fed attack artifacts to frontier AI models behind commercial APIs. The models refused. The analysis required submitting real attack commands, exploit payloads, and command-and-control artifacts. The providers’ safety guardrails blocked the requests because, as Hugging Faceput it, they “cannot distinguish an incident responder from an attacker.”

Hugging Face rebuilt its forensic timeline usingGLM 5.2, an open-weight model from Chinese developer Z.ai, running on its own infrastructure. The teamanalyzed roughly 17,600 attacker actionsin hours rather than the days a manual reconstruction would have required. The attack data and the credentials it referenced never left Hugging Face’s environment.

The asymmetry is stark. The OpenAI evaluation agents ran with reduced cyber refusals and without the ordinary production control stack. The defenders encountered the restrictions imposed on normal commercial API users. As former AWS Deputy CISOMerritt Baer told VentureBeat: “As AI becomes embedded in security operations, this becomes an operational resilience issue rather than merely a model policy issue.”SANS arguedthat the refusal during incident response deserved at least as much scrutiny as the initial containment failure.

The cybersecurity industry developed partial authorization mechanisms over two decades: written penetration-testing scopes, vulnerability-disclosure and bug-bounty safe harbors, DMCA research exemptions, and theDepartment of Justice’s 2022 CFAA charging policyfor good-faith research. These protections remain contractual, scope-specific, and inconsistent across jurisdictions. But they exist.

AI providers have begun analogous programs. OpenAI launched Trusted Access for Cyber, providing vetted researchers and enterprise teams with access to more permissive cyber capabilities. Anthropic’s Glasswing program provides selected organizations with controlled access to Mythos capabilities. But these programs are provider-specific, discretionary rather than rights-based, nonportable between providers, and evidently not available when an organization is responding to a live incident involving that provider’s own models. Hugging Face was a leading AI platform with deep industry relationships, and it still had to pivot to a self-hosted Chinese open-weight model because the commercial tools it had access to refused the work.

The industry needs a portable trust framework under which verified incident-response teams can invoke a controlled forensic mode across participating services, subject to identity assurance, logging, organizational authorization, and post-event review. Defenders deserve better.

## The Pacing Letter and the Contradiction

The governance failures would be concerning on their own. They become extraordinary when you consider what the AI labs were doing during the exact same week.

On July 28, 2026, more than 1,100 employees of frontier AI companiessigned an open lettertitled “Pacing the Frontier” (the count has since grown past 1,300). The signatories included Anthropic CEO Dario Amodei, Anthropic co-founders Jared Kaplan and Jack Clark, and OpenAI chief scientist Jakub Pachocki. Both OpenAI and Anthropic endorsed the letter as companies within hours. The letter asks the U.S. government to support an international effort to develop the technical and governance tools that would make deliberate pacing of automated frontier AI development possible.

The timing is worth stating plainly. On July 28, Anthropic endorsed a call for governance tools to pace AI development. On July 30, Anthropic disclosed that its AI models had autonomously compromised three organizations because its own evaluation infrastructure lacked adequate containment, with the earliest incident dating to April. The same company calling for governance mechanisms had spent months unaware that its own models were accessing real systems without authorization.

On July 29, Sam Altman briefed senators on Capitol Hill about OpenAI’s next model family, the same week his current models were in the news forbreaching Hugging Face. Combined, OpenAI and Anthropic spent3.17 million USD on federal lobbyingin Q2 2026, a 23% increase from Q1.

I want to be fair about this. The individuals who signed the pacing letter may have done so sincerely. The organizational failures that produced the July incidents may have been unforeseen. Correlation between disclosure timing and lobbying activity does not prove intent. But the structural problem remains: the companies that cannot verify the containment of their own evaluation environments are the same companies lobbying to shape AI policy. The cybersecurity industry spent 20 years learning that vendors do not write effective rules for themselves. The AI safety community is asking us to believe this time is different.

## What Washington Already Has and What It Lacks

Washington is not starting from zero. Executive Order 14409, issued onJune 2, 2026, directs the development of a classified benchmarking process for frontier models’ cyber capabilities and a voluntary framework under which developers may provide pre-release access for up to 30 days. The order expressly stops short of mandatory licensing or preclearance.

On July 27, Nvidia launched theOpen Secure AI Alliancewith dozens of inaugural partners, including Microsoft, IBM, Hugging Face, and CrowdStrike.OpenAI, Anthropic, and Google are absent. The alliance’s founding thesis is that defenders need both frontier closed models and frontier open models working together. Jensen Huangwrote on X: “Attackers have frontier AI. … During the Hugging Face incident, closed AI blocked essential forensics. An open-weight frontier model helped contain the intrusion.”

These are early moves. What is still missing is a statutory oversight regime for private AI evaluators, enforceable evidence-preservation and disclosure obligations, and portable authorization for defenders that does not depend on the goodwill of any single provider.

The unresolved question is whether this develops into enforceable external assurance or remains a voluntary process whose scope and evidence are still largely controlled by the laboratories.

## The PQC Connection

I would not write this article if the governance failures had no connection to the concerns PostQuantum.com covers. They do, and the connection is direct.

In the same week as the hacking disclosures, Anthropic reported that Mythos hadmaterially weakened HAWK, a third-round candidate in NIST’s Additional Digital Signatures standardization process, after approximately 60 hours of work. The HAWK development teamwithdrew the candidatethe following day. That does not show PQC standardization failing. It shows public cryptanalysis and candidate withdrawal working as intended: a candidate was publicly specified, external analysis found a weakness, the result was disclosed, and the candidate was removed.

The emerging governance challenge is throughput. AI systems may generate credible cryptanalytic results faster than the cryptographic community can independently reproduce and adjudicate them. If the pace of AI-generated attacks on PQC candidates exceeds the verification capacity of the research community, organizations planningPQC migrationface a new kind of uncertainty: not whether the standardization process works, but whether it can work fast enough.

Crypto-agilityremains essential because even rigorously evaluated algorithms can later fail. But the HAWK episode shows why migration architecture must be paired with a verification system capable of processing AI-accelerated cryptanalysis: machine-checkable attack artifacts, reproducibility requirements, independent replication, and clear evidentiary thresholds for standards decisions. ThePQC Migration Frameworkbuilds crypto-agility into the architecture precisely because no algorithm selection should be treated as permanent. The HAWK withdrawal is proof that this design principle is correct.

## The Question for Policymakers

Clem Delangue, Hugging Face’s CEO,flew to San Franciscoto meet with OpenAI executives after the breach. He then posted two specific demands on X: “radical transparency” (release the full agent traces so the research community can study them) and 100 million USD in compute for community cyber defenses. As of August 1, I could find no public OpenAI commitment to release the complete traces or provide the requested compute.

Delangue’s demands are constructive but they are voluntary requests from one company to another. They do not address the underlying conflict. The AI labs simultaneously build the capabilities, evaluate the capabilities (or select and pay evaluators to do so), lobby to shape AI policy, and disclose incidents on their own timeline. Every one of these functions carries a conflict of interest when performed by the same organization. The cybersecurity industry separated them, imperfectly and over two painful decades. The AI safety community has not yet begun that separation.

The question for policymakers is whether the governance structures around AI development will look like what the cybersecurity industry built (external evaluation with inspected evaluators, mandatory disclosure with enforceable deadlines, portable authorization for defenders, and evidence preservation under independent custody) or whether they will look like what the AI labs are currently offering: voluntary commitments, self-evaluation, and a seat at the table for the companies whose products caused the problem.

I have spent three decades watching assurance regimes fail when the organization being assessed controls the evidence, the assessor, and the account of what happened. AI is not exempt from that lesson.

Marin Ivezic

Follow on X

Send an email

August 3, 2026

 10 minutes read
 

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