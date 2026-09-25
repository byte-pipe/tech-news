---
title: 'Anthropic’s Misuse Report: Seven Labs, 190 Million Exchanges, and the Collapse of the Offensive Labor Gap – Forkast'
url: https://forkast.news/anthropics-misuse-report-seven-labs-190-million-exchanges-and-the-collapse-of-the-offensive-labor-gap
site_name: tldr
content_file: tldr-anthropics-misuse-report-seven-labs-190-million-ex
fetched_at: '2026-09-25T21:59:50.717316'
original_url: https://forkast.news/anthropics-misuse-report-seven-labs-190-million-exchanges-and-the-collapse-of-the-offensive-labor-gap
date: '2026-09-25'
published_date: '2026-09-25T20:51:37+00:00'
description: Industrial-scale distillation by Chinese labs, autonomous malware rebuilding by Russian espionage actors, and AI agents executing SaaS supply-chain breaches in 34 hours — the most comprehensive public disclosure of agent-native offensive operations to date.
tags:
- tldr
---

The industrial-scale distillation of frontier AI models has moved from theoretical risk to documented reality. According to Anthropic’s report,Detecting and countering misuse of AI: September 2026, seven Chinese labs engaged in systematic campaigns to extract the capabilities of Claude’s Opus-class models between December 2025 and August 2026. These operations were not isolated incidents but coordinated efforts to replicate high-end model performance through massive data harvesting.

The scale of these campaigns is significant. Alibaba, identified as GTG-16005, executed approximately 151 million exchanges between May and July 2026, peaking at 3 million requests per day using over 3,500 fraudulent accounts. Other actors employed different mechanics: Moonshot (GTG-16002) silently served Claude responses to Kimi users, while DeepSeek (GTG-16001) relayed customer exchanges to Claude over a 14-day period, totaling more than 12.1 million exchanges. MiniMax utilized a proxy network via a shell company, and Xiaomi (GTG-16008) replayed user conversations from its MiMo models. SenseTime opted to purchase harvested exchanges from third-party vendors.CISA Advisory AA26-251A, issued on September 8 by the NSA and FBI, has corroborated these distillation findings.

This activity represents an inflection point where AI functions as both the attack surface and the primary infrastructure. Anthropic notes that a majority of the operations described in its report were enabled by AI via direct execution or orchestration. The report states, “AI has collapsed the labor and tooling gap that used to separate well-resourced, state-sponsored operations from individual operators.” This shift is evident in the mechanics of recent breaches. In the case of GTG-50020, a Russian-speaking actor used prompt injection to compromise an AI vendor’s evaluation sandbox, stealing production API keys to attack approximately 30 AI companies in four days. Similarly, ShinyHunters affiliates (GTG-50014) compromised a SaaS provider, gaining access to over 2,100 Azure AD token sets and 40 corporate tenants in 34 hours. In that instance, the report explicitly notes that “AI agents performed nearly all the work.”

These developments follow the trajectory established by the SOUL chained-agents campaign (Post 130814). That earlier report documented three open-source agents executing over 27 breaches at a cost of $25 per target. The current data shows a transition from those low-cost, individual-operator breaches to industrial-scale autonomous operations. The report highlights that “operations ran autonomously, with minimal human input or supervision: these included multi-agent frameworks conducting reconnaissance, exploitation, and theft against multiple victims, in parallel, for hours or days at a time.”

 

Advertisement

The implications for enterprise security are structural. Autonomous vulnerability research, such as that observed in Chinese exploit foundries (GTG-10007), now runs 24/7 using multi-agent frameworks. Russian espionage actors (GTG-20006) are deploying agents that autonomously modify and rebuild malware when detection mechanisms are triggered. As Anthropic observes, “The AI supply chain has become a deliberate criminal target.”

It is necessary to emphasize that these findings, particularly those categorized under GTG identifiers, are derived entirely from Anthropic’s internal threat intelligence. While CISA has corroborated the distillation findings, the broader claims regarding the mechanics and scale of autonomous operations rely exclusively on the vendor’s proprietary data. The shift in the unit economics of cybercrime is clear: the automation of the kill chain has made even low-value targets viable for exploitation. For CISOs and enterprise decision-makers, the primary takeaway is that the barrier to entry for sophisticated, multi-stage cyberattacks has been lowered by the very tools intended to enhance productivity.