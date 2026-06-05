---
title: Agent-led devs need serverless OpenSearch, Amazon claims
url: https://www.theregister.com/databases/2026/06/01/agent-led-devs-need-serverless-opensearch-amazon-claims/5249033
site_name: tldr
content_file: tldr-agent-led-devs-need-serverless-opensearch-amazon-c
fetched_at: '2026-06-05T19:36:45.009284'
original_url: https://www.theregister.com/databases/2026/06/01/agent-led-devs-need-serverless-opensearch-amazon-claims/5249033
date: '2026-06-05'
published_date: '2026-06-01T12:45:00.000Z'
description: System relies on a proprietary storage layer as AWS moves to separate storage and compute to fit mega AI demands
tags:
- tldr
---

Databases

 

# Agent-led devs need serverless OpenSearch, Amazon claims

System relies on a proprietary storage layer as AWS moves to separate storage and compute to fit mega AI demands

Lindsay Clark

Lindsay

Clark

Published

mon 1 Jun 2026 // 13:45 UTC

Amazon has re-engineered its serverless OpenSearch database service, separating storage and compute in a move it claims will benefit developers faced with new demand characteristics of agentic AI.

The new serverless system would avoid the problem of users paying for idle compute capacity between demand bursts, the vendor claims.

Speaking toThe Register, Tia White, Director of OpenSearch, AWS said: “Collections can shrink all the way to zero when nothing's happening. We have mitigated the cold start problem, so they spin back up in seconds when traffic is needed as agents restart. It auto-scales 20 times faster than before.”

REG AD

AWS promises a fully managed search and vector engine designed for customers building AI agents, offering up to 60 percent cost savings compared to the cost of OpenSearch Service clusters provisioned for peak capacity.

REG AD

AWS has integrated OpenSearch Serverless into Vercel, letting developers spin up new search backends directly from the Vercel console without leaving their workflow. The service also powers the OpenSearch Launchpad inside Kiro - AWS's new agentic coding IDE - providing guided, end-to-end architecture planning for search applications. Broader AI development platform support is coming.

## MORE CONTEXT

* ### If cores are what agents crave, Intel's new Clearwater Xeon 6+ might just quench their thirst
* ### Okta writes its own license to kill rogue AI agents
* ### AI and data sovereignty in Postgres: An answer to the datacenter energy crisis
* ### Snowflake buys Natoma to help freeze out rogue agents

White said the most immediate application would be with developer coding agents. “Historically, search has not had to decouple [storage and compute], because the traffic was pretty predictable. Now with agentic workloads, even the most sophisticated technical teams need to use a serverless offering. Agentic, production-allied workloads are only going to continue to proliferate and grow.”

At the turn of the decade, ElasticSearch was the de facto database manager developers used for enterprise search. However, in 2021,Elastic adopted a more restrictive software licensein order to restrict cloud service providers from creating a DBaaS based on the free open source software and making money from it.AWS responded by forking the codeto create OpenSearch, which is governed by the Linux Foundation, with contributing organizations including Uber and SAP.

MongoDB and MariaDB have trodden a similar path to Elastic, with debate continuing over whether the cloud giants should be able to make money from database services without paying for the core database itself, or whether a more permissive open source development model is the best option.

White said some of the logic in the new OpenSearch serverless offering is available in the open source project, but a custom-built AWS proprietary storage layer is part of the intellectual property and is not fully open source. She could not rule out AWS making the technology open source in the future, as it has done with some IP in the past, but says there are no current plans to do so.

The OpenSearch serverless launch might be good news for people building on AWS, but bad news for Elastic.

Elastic launched its serverless search offering in 2024, promising decoupled storage and compute and auto-scaling. Itupdated the service in January, claiming 50 percent higher indexing throughput and 37 percent lower search latency using new AWS Graviton instances at no extra cost to users.

According to theDB-Engines ranking— which is based on website mentions, technical discussions, Google search trends, and jobs ads — ElasticSearch continues to place well above OpenSearch. The pair rank at 11th and 31st place respectively, although ElasticSearch’s ranking has fallen steadily over the last few years. ®

REG AD

databases

agentic ai

amazon

REG AD

SPONSORED LINKS

Building the New Trust Architecture for AI - Watch Now

security

## Yet another Cisco SD-WAN 0-day under attack, and no patch in sight

Good luck, sys admins

SCIENCE

## Serious ISS air leak forces NASA astronauts to temporarily take shelter in Dragon capsule

Business is back to normal in the orbital station, but one of two newly discovered leaks is still unrepaired

## China Mobile Jiangsu and ZTE unveil intelligent complaint analysis agent to reshape core network O&M

PARTNER CONTENT: Leveraging multi-modal LLMs and agent technology to automate signaling analysis and shift core network O&M from experience to knowledge-driven

science

## Trump pumps federal funds into coal plants in the name of energy security

DoE wants to keep 13 coal-fired power generators going at the same time as funding nuclear research

SaaS

## AWS reportedly to tuck Elon Musk's Grok into Bedrock, despite zero enterprise demand

The energy drink of frontier models

## ZTE showcases AI-driven project management innovations at the 14th IPMA Research Conference 2026

PARTNER CONTENT: Integrating AI into the iEPMS platform to achieve a 98% quality review accuracy rate and slash report generation times, leveraging experience from 240,000 global projects

### MOST POPULAR

* AI and ML#### Netflix wiz creates app to slash AI bills, then open sources it
* Security#### Disgruntled 0-day hunter 'humiliated' by Microsoft pledges 'bone shattering drop' as Redmond calls cops
* SECURITY#### All the passwords were stored in Active Directory description fields
* Security#### Troops’ phones gave away location data to foreign adversaries
* Personal tech#### California passes bill declaring death-by-algorithm to 3D-printed ghost guns

## EVENTS

* ### Overcoming the trade-offs in data sovereigntyWhat does data sovereignty actually mean for your network, which trade-offs are unavoidable? Learn more.
* ### From Prompt to Exploit: How LLMs Are Changing API AttacksModern applications are API-driven, interconnected, and often over-permissioned, making them an ideal target for AI-assisted attacks.
* ### Architecting the Future: Unlocking Enterprise Data Services for KubernetesJoin us to discover how to eliminate infrastructure silos and establish a standardized, enterprise-grade cloud-native platform.
* ### Catch the Advanced Attacks Microsoft 365 Misses with Behavioral AI SecurityMicrosoft 365 is the backbone of enterprise communication, and its native security filters out the known and the noisy.
* ### Virtual Cyber Recovery SimStep into the chaos of a live ransomware breach, test your response skills, and team up with other IT and security pros to outsmart cybercriminals
* ### Virtual Cyber Recovery SimulationRansomware attacks aren’t slowing down, and neither are we. Druva’s hit event, Escape Ransomware, is now fully virtual.
* ### Zero Trust for the Agentic AI EraThe identity and access models most organizations rely on were built for human users, not non-human identities operating independently.
* ### Zero Trust for the Agentic AI EraThe identity and access models most organizations rely on were built for human users, not non-human identities operating independently.
* ### Agentic AI at Scale: From Pilot to ProductionJoin us to learn how to unlock real ROI by driving adoption of AI at scale.

 EXPLORE ALL OF OUR EVENTS
 

### AI

* databases#### Microsoft allows BYOL for Amazon RDS. Repeat, Microsoft allows BYOL for Amazon RDSSQL Server licenses can now be consumed in the rival cloud's DBaaS
* security#### World Food Programme breach exposes data of 600k vulnerable Gazan familiesThose receiving aid in the famine-threatened, war-torn territory told support will remain
* SYSTEMS#### Gigabyte packs 40 Intel Lunar Lake PCs in a pizza boxWho needs one big CPU when you could have dozens of little ones?
* Personal tech#### Raspberry Pi's profits are up. So is its DRAM billForecasts earnings well ahead of expectations, even as it taps credit facilities to lock in memory supply
* Saas#### Capita £370M bid 40% under UK.gov estimate for Oracle HR and finance system project, court case revealsCost model designed to protect against low-cost bid bias, claims rival

### Infosec

* security#### Yet another Cisco SD-WAN 0-day under attack, and no patch in sightGood luck, sys admins
* SCIENCE#### Serious ISS air leak forces NASA astronauts to temporarily take shelter in Dragon capsuleBusiness is back to normal in the orbital station, but one of two newly discovered leaks is still unrepaired
* science#### Trump pumps federal funds into coal plants in the name of energy securityDoE wants to keep 13 coal-fired power generators going at the same time as funding nuclear research
* #### ZTE showcases AI-driven project management innovations at the 14th IPMA Research Conference 2026PARTNER CONTENT: Integrating AI into the iEPMS platform to achieve a 98% quality review accuracy rate and slash report generation times, leveraging experience from 240,000 global projects
* #### China Mobile Jiangsu and ZTE unveil intelligent complaint analysis agent to reshape core network O&MPARTNER CONTENT: Leveraging multi-modal LLMs and agent technology to automate signaling analysis and shift core network O&M from experience to knowledge-driven

### FOSS

* #### Yet another Cisco SD-WAN 0-day under attack, and no patch in sightGood luck, sys admins
* #### Serious ISS air leak forces NASA astronauts to temporarily take shelter in Dragon capsuleBusiness is back to normal in the orbital station, but one of two newly discovered leaks is still unrepaired
* #### Trump pumps federal funds into coal plants in the name of energy securityDoE wants to keep 13 coal-fired power generators going at the same time as funding nuclear research
* #### ZTE showcases AI-driven project management innovations at the 14th IPMA Research Conference 2026PARTNER CONTENT: Integrating AI into the iEPMS platform to achieve a 98% quality review accuracy rate and slash report generation times, leveraging experience from 240,000 global projects
* #### China Mobile Jiangsu and ZTE unveil intelligent complaint analysis agent to reshape core network O&MPARTNER CONTENT: Leveraging multi-modal LLMs and agent technology to automate signaling analysis and shift core network O&M from experience to knowledge-driven
* #### Agentic AI hype races ahead as enterprises remain stuck in pilot modeMost orgs remain trapped between flashy demos and real-world deployment, despite 75% saying adoption is racing ahead