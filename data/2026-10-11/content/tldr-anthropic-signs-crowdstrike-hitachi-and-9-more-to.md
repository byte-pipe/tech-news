---
title: Anthropic signs CrowdStrike, Hitachi and 9 more to defend power and water
url: https://thenextweb.com/news/anthropic-cyber-mission-critical-infrastructure-oss-scanner
site_name: tldr
content_file: tldr-anthropic-signs-crowdstrike-hitachi-and-9-more-to
fetched_at: '2026-10-11T22:41:14.209089'
original_url: https://thenextweb.com/news/anthropic-cyber-mission-critical-infrastructure-oss-scanner
author: Ana Maria Constantin
date: '2026-10-11'
published_date: '2026-10-09T19:25:43+00:00'
description: '“Hard to defend in many ways that AI cannot fix”: the Anthropic Cyber Mission enlists CrowdStrike, Hitachi and PwC to guard grids and water.'
tags:
- tldr
---

Credit: Anthropic

Anthropic will give its frontier Claude models, engineers and threat research to the companies that guard critical infrastructure. That means power grids, water utilities and transport networks. The Critical Infrastructure Defense Program is the first part of the Anthropic Cyber Mission. The companyannounced it on Thursdayas a long-term effort to support defenders.

The second part is OSS Scanner, a free service that scans open-source code with Anthropic’s strongest models. It sends the findings straight to maintainers, without a human checking them first.

## Eleven founding partners

Accenture, Booz Allen, CrowdStrike, Deloitte and Dragos joined as founding partners. So did Hitachi, Insane Cyber, Nozomi Networks, Palo Alto Networks, PwC and Rockwell Automation. Anthropic said they are the consultancies, security companies and equipment makers that operators already rely on. Several are already using Claude to fix vulnerabilities, it said.

The programme targets operational technology: the controllers, control software and industrial networks that run plants for decades. Operators often cannot take these systems offline to patch them, so known flaws can stay open for years. Anthropic will start with a small group of providers to learn what works.

“Critical infrastructure is hard to defend in many ways that AI cannot fix,” Anthropic said in its announcement.

Hitachi said inits own statementthat it will join the programme’s working groups. It will also share its operational technology expertise. The Japanese group signed a strategic partnership with Anthropic in May and joined Project Glasswing in June.

Anthropic did not say who will pay for the computing, or whether partners get free model access,Axios reported. Axios had the announcement first. It added that it is unclear how partners will test fixes without disrupting utilities.

In June, Anthropic started a similar programme for US state, local, tribal and territorial governments. It said it has since given Claude models and technical support to more than half of US states. OpenAI put$1bn behind cyber defencefor water utilities and community banks in September.

## Bug reports no human has checked

OSS Scanner is opt-in and modelled on Google’s OSS-Fuzz. Enrolled projects get periodic scans from Anthropic’s most capable models, including Claude Mythos, according to aFrontier Red Team post. Each report carries a proof of concept, an explanation and, where possible, a suggested patch.

Anthropic expects more than 90% of the findings to be real. Its penetration testers checked 97 critical and high-severity findings from 48 projects. Of those, 85 met the bar for its disclosure process. Another 11 were real but repeated known issues, and only one was a false positive.

Over six months, Anthropic’s models flagged more than 29,000 candidate vulnerabilities. Its staff could only review about 6,000. Nearly 5,000 unchecked reports went to maintainers who asked to receive everything.

Todd Ouska of wolfSSL said his project got 74 reports and all but two were valid. Five became CVEs.

“OSS Scanner has helped us find multiple issues in curl worthy of addressing, including one of the worst curl vulnerabilities reported in the last few years,” said Daniel Stenberg of curl.

Anthropic picks projects case by case, and only takes established ones with a critical impact on infrastructure and user security. Itsservice agreementwarns that reports may misjudge severity or propose patches that break things. Maintainers must review every report, and Anthropic caps its liability at $1,000. Anthropic’s consumer terms also apply.

## Attackers ahead for now

“Our forecast is that in two years, AI will favor defense,” Anthropic said.

The company added that this may not hold in the near term. Exploiting flaws has become cheaper, while verifying and fixing them still depends on people. In Glasswing, months often passed between finding a flaw and fixing it, and on running machinery a fix can in rare cases wait decades.

Last week Anthropic said aChinese model nearly matchesMythos at cyber exploits. This week it merged Glasswing into its expanded Cyber Verification Program. TheDefender Advantage Fundit launched in August keeps OSS Scanner free.

Anthropic has also funded the Python Software Foundation, the Apache Software Foundation, and Alpha-Omega and OpenSSF through the Linux Foundation. CrowdStrike, one of the new partners, alreadyworks with both labs.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.