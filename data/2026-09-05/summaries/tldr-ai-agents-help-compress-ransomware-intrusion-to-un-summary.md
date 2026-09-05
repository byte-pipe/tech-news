---
title: AI agents help compress ransomware intrusion to under 10 hours, raising stakes for CISOs | CSO Online
url: https://www.csoonline.com/article/4217976/ai-agents-help-compress-ransomware-intrusion-to-under-10-hours-raising-stakes-for-cisos.html
date: 2026-09-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-05T10:35:57.325701
---

# AI agents help compress ransomware intrusion to under 10 hours, raising stakes for CISOs | CSO Online

# AI agents help compress ransomware intrusion to under 10 hours, raising stakes for CISOs

## Incident overview
- Palo Alto Networks Unit 42 observed a ransomware attack that traversed an enterprise network in under 10 hours, a timeline they estimate would take human operators about two weeks.  
- The intrusion employed more than 50 MITRE ATT&CK techniques; the novelty lay in AI agents that interpreted action results and adapted subsequent steps.  
- Attackers entered via a public‑facing API endpoint, used an automated reconnaissance agent to map internal micro‑services, and leveraged agents to scan source‑code repositories for exposed credentials.  
- Obtained administrative credentials from a secrets‑management system, hijacked a code application to exfiltrate cloud access keys, and attempted to insert backdoors in Terraform configurations (blocked by existing branch protections).  
- Stolen cloud credentials were used to access the victim’s own AI services, turning the organization’s compute resources into infrastructure for further malicious activity.  
- Researchers concluded the attack was human‑directed with AI orchestrating tactical work, not fully autonomous.

## Faster attack cycles strain containment
- The speed of AI‑assisted attacks forces security teams to shorten the gap between detection and containment.  
- CISOs are urged to move away from long‑lived credentials toward short‑lived, narrowly scoped identities for workloads and services.  
- Security providers may need pre‑authorized authority to disable compromised accounts and invalidate credentials without waiting for internal approval.  
- Incident‑response playbooks should allow automated containment where feasible, while clearly defining responsibilities and regularly testing procedures through tabletop exercises.

## Detection needs broader context
- Malicious activity that spans multiple, separately monitored systems can evade traditional alerts.  
- Detection engineering should be tuned to an organization’s normal baseline so that anomalous behavior stands out.  
- Correlating telemetry across security tools is essential; a single suspicious event may only become meaningful when combined with activity elsewhere.

## Authority can travel across systems
- Isolating systems can miss risks created by their interconnections.  
- “Transitive authority” occurs when access in one system enables privileged actions in another (e.g., a repository account altering a workflow that assumes a cloud admin role).  
- Entitlement reviews must consider the downstream effects of an identity’s actions, not just its direct permissions.  
- Preventive controls such as branch protection retain high value as attack decision cycles compress; they do not need to outrun the attacker.

## Recommendations for security leaders
- Compare the time required for a realistic attack path to reach a critical asset with the organization’s detection‑to‑containment time; a gap indicates structural weakness.  
- Conduct agent‑assisted red‑team exercises to measure that gap and identify where controls fail.  
- Recognize that AI does not introduce fundamentally new techniques but reduces the time, expertise, and cost needed to execute existing techniques at scale.  
- Boards should focus on whether existing controls can stop a credible attack path before it compromises critical business systems.

## Author information
- Prasanth Aby Thomas is a freelance technology journalist covering semiconductors, security, AI, and EVs. His work has appeared in DigiTimes Asia, asmag.com, and other publications. He holds master’s degrees in international journalism (Bournemouth University) and visual communication (Loyola College), a bachelor’s in English (Mahatma Gandhi University), and studied Chinese at National Taiwan University.