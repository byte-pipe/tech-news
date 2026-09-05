---
title: AI agents help compress ransomware intrusion to under 10 hours, raising stakes for CISOs | CSO Online
url: https://www.csoonline.com/article/4217976/ai-agents-help-compress-ransomware-intrusion-to-under-10-hours-raising-stakes-for-cisos.html
site_name: tldr
content_file: tldr-ai-agents-help-compress-ransomware-intrusion-to-un
fetched_at: '2026-09-05T10:35:40.947642'
original_url: https://www.csoonline.com/article/4217976/ai-agents-help-compress-ransomware-intrusion-to-under-10-hours-raising-stakes-for-cisos.html
date: '2026-09-05'
description: The attack exploited exposed credentials and trust relationships spanning development and cloud environments, showing how access in one system can enable more privileged actions in another.
tags:
- tldr
---

by									
Prasanth Aby Thomas

# AI agents help compress ransomware intrusion to under 10 hours, raising stakes for CISOs

News

Sep 3, 2026
5 mins

A ransomware attacker used AI agents to move through an enterprise network in less than 10 hours, according to Palo Alto Networks researchers, who estimated that similar work could have taken human operators about two weeks.

The incident involved more than 50 techniques mapped to the MITRE ATT&CK framework, according to the company’sUnit 42 threat research team. The techniques themselves were largely familiar. The notable difference, according to Unit 42, was the use ofAI agentsthat could interpret the results of their actions and adapt subsequent steps during the intrusion.

Unit 42 said it observed several indicators consistent with AI use during its investigation. The threat actor also told researchers during negotiations that frontier AI models and attack-specific agentic frameworks had been used.

The attacker initially entered through a public-facing API endpoint before an automated reconnaissance agent mapped internal microservices, Unit 42 said. Other agents searchedsource-code repositoriesfor exposed credentials, which helped the attacker gain access to a secrets-management system and obtain administrative credentials.

“The actor hijacked an enterprise code application via custom workflows to exfiltrate cloud access keys,” Unit 42 said. “They attempted to plant backdoors in Terraform configurations.” The researchers said existing branch protections prevented the attempted changes.

Stolen cloud credentials were later used to access the victim’s AI services, effectively turning its own computing resources into infrastructure that could support further attacker activity, according to Unit 42.

The incident does not establish that the attack was fully autonomous. “The evidence points to a human-directed intrusion in which AI orchestrated delegated tactical work,” saidSanchit Vir Gogia, chief analyst at Greyhound Research.

## Faster attack cycles strain containment

The speed demonstrated in the Unit 42 investigation puts pressure on security teams to reduce the interval between identifying malicious activity and taking containment action, saidJonathan Ong, senior analyst for managed security services at Omdia.“Enterprises do not necessarily need a new threat model, but they do need to operate on a new clock,” saidSakshi Grover, senior research manager for IDC Asia Pacific Cybersecurity Services.

Faster attacks also increase the importance of controlling non-human identities. CISOs should reduce reliance on long-lived credentials and move towardshort-lived, narrowly scoped identitiesfor workloads and services, Grover said.

CISOs may also need to examine how much authority their security providers have to act once malicious activity is detected. A provider could, for example, be authorized to disable a compromised account and invalidate its active credentials before the attacker can continue using them.

Incident-response playbooks should also be adapted to the organization and allow providers to “automate containment without requiring in-house approval where feasible,” Ong said.

That does not mean handing unrestricted control to a third party. Ong said organizations should clearly establish responsibilities in advance and periodically test their response procedures through tabletop exercises.

## Detection needs broader context

The attack also illustrates the difficulty of detecting malicious activity that crosses systems which may be monitored separately. Ong said detection engineering should be tuned to an organization’s normal activity so unusual behavior can be identified against that baseline.

A suspicious action in one environment may not be enough to generate a meaningful alert. Its significance can become clearer when combined with activity elsewhere.

For CISOs, that increases the importance of correlating telemetry across security systems rather than evaluating alerts largely within separate technology domains.

## Authority can travel across systems

Looking at systems in isolation can miss risks created by the connections between them.

“Each platform may have had controls, but the relationships between them created the exploitable path,” Grover said.

Gogia described one manifestation of this problem as “transitive authority,” where access in one system can enable a more privileged action elsewhere.

A repository account, for example, may not have cloud administrator privileges itself but could alter a workflow that assumes a more powerful cloud role. Entitlement reviews should therefore consider what an identity can cause another system to do, rather than only what it can access directly, he said.

Gogia also pointed to the branch protection that blocked the attempted Terraform change as an example of the value of preventive controls when attack cycles accelerate.

“As adversary decision cycles compress, prevention gains relative value precisely because it never has to outrun anyone,” he said.

The key question for security leaders is whether attackers can now move faster than existing controls can contain them. One practical test is to compare how quickly a realistic attack path can reach a critical system with how long the organization actually takes to detect and contain it.

Grover said agent-assisted red-team exercises could be used to measure that gap. If an attack path can be completed before containment takes effect, the weakness is structural rather than hypothetical.

“The principal risk is not that AI suddenly creates entirely new attack techniques,” she said. “It lowers the time, expertise, and cost required to execute existing techniques concurrently and at scale.” For boards, the issue is less about whether AI-enabled ransomware is an emerging threat than about whether existing controls can stop a credible attack path before it reaches a critical business system.

Ransomware
Malware
Cybercrime
Security
Artificial Intelligence
 

														by 															

																Prasanth Aby Thomas															

Prasanth Aby Thomas is a freelance technology journalist who specializes in semiconductors, security, AI, and EVs. His work has appeared in DigiTimes Asia and asmag.com, among other publications.Earlier in his career, Prasanth was a correspondent for Reuters covering the energy sector. Prior to that, he was a correspondent for International Business Times UK covering Asian and European markets and macroeconomic developments.He holds a Master's degree in international journalism from Bournemouth University, a Master's degree in visual communication from Loyola College, a Bachelor's degree in English from Mahatma Gandhi University, and studied Chinese language at National Taiwan University.

## More from this author

* news### China-linked hackers turn Cisco routers into covert attack infrastructureSep 1, 20265 mins
* news### Trusted Chrome, Edge extensions weaponized in supply chain campaignAug 31, 20265 mins
* news### AI helps Chinese-speaking hackers speed up attacks on exposed serversAug 25, 20265 mins
* news### Trump administration opens door to private-sector cyber offensivesAug 13, 20264 mins
* news### OpenAI launches GPT-5.6-Cyber as AI narrows vulnerability response windowAug 11, 20264 mins
* news### Google ADK flaws reveal what happens when AI agents trust the wrong messageAug 4, 20265 mins
* news### Russian hackers turn Exchange flaw into ‘half-click’ mailbox takeoverJul 30, 20264 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

news
 
 

### FBI investigates breach of 153 million driving license records at IDscan.net

 
By Peter Sayer and Maxwell Cooter
Sep 4, 2026
2 mins

Cyberattacks
Data Breach
Data Privacy

news
 
 

### Bidding war for defunct Spirit Airlines’ employee data will not die

 
By Maxwell Cooter
Sep 4, 2026
2 mins

Data Privacy
Markets
Transportation and Logistics Industry

news
 
 

### OpenAI launches GPT-6 Astra, its first model to cross a critical cybersecurity threshold

 
By Gyana Swain
Sep 4, 2026
5 mins

Artificial Intelligence
Generative AI
Security

podcast
 
 

### Cybersecurity on the Front Lines of Critical Infrastructure

 
By Joan Goodchild
Aug 12, 2026
10 mins

Cyberattacks

podcast
 
 

### Cloud Security at a Breaking Point: AI, Complexity, and the Future of Trust

 
By Joan Goodchild
Aug 6, 2026
17 mins

Cybercrime

podcast
 
 

### Moving Beyond the Checkbox in Human Risk Management

 
By Joan Goodchild
Jul 30, 2026
9 mins

Cyberattacks

video
 
 

### Cybersecurity on the Front Lines of Critical Infrastructure

 
By Joan Goodchild
Aug 12, 2026
10 mins

Cyberattacks

video
 
 

### Cloud Security at a Breaking Point: AI, Complexity, and the Future of Trust

 
By Joan Goodchild
Aug 6, 2026
17 mins

Cybercrime

video
 
 

### Moving Beyond the Checkbox in Human Risk Management

 
By Joan Goodchild
Jul 30, 2026
9 mins

Cyberattacks