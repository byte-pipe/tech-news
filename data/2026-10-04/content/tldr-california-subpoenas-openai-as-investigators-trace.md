---
title: California subpoenas OpenAI as investigators trace its agents to the CDC
url: https://thenextweb.com/news/openai-rogue-agents-asymmetric-security-cdc-bonta-subpoena
site_name: tldr
content_file: tldr-california-subpoenas-openai-as-investigators-trace
fetched_at: '2026-10-04T15:40:46.552025'
original_url: https://thenextweb.com/news/openai-rogue-agents-asymmetric-security-cdc-bonta-subpoena
author: Ana Maria Constantin
date: '2026-10-04'
published_date: '2026-10-02T12:14:20+00:00'
description: OpenAI’s rogue agents used private accounts and expiring mailboxes, leaving gaps in the record, investigators say. California wants answers.
tags:
- tldr
---

OpenAI chief executive Sam Altman at DevDay 2026.

Credit: OpenAI

OpenAI’s rogue agents reached pre-production servers, tried attacker techniques and probed the websites of the CDC, the SEC, the International Energy Agency and the Mayo Clinic. That is according to aninvestigationpublished on Thursday by Asymmetric Security, a digital forensics firm. Some of their tactics left records erased or out of reach. Public data alone cannot rule out access to sensitive information, the firm said.

On the same day, California Attorney General Rob Bonta subpoenaed OpenAI over cyber incidents and risks tied to its models,Reutersreported.

## From health statistics to staging servers

Asymmetric’s team spent 48 hours examining public records of agent activity between March and September. The activity targeted the Australian government and other organisations, and it peaked between 16 and 21 June. The agents seem to have started with research tasks, such as finding health, prescription and trade statistics, possibly as part of an evaluation.

“The activity we observed looked like it stemmed from innocent tasks which then evolved into problematic activity,” the investigators wrote.

When the agents could not get the data, they chained public services together. A developer tool called httpbin served pages containing their own code. A scanning service called urlquery opened those pages in its browser and recorded the results. That gave the agents something close to a full web browser, despite the limits of their sandbox.

The records show access to a pre-production system of the Australian Institute of Health and Welfare (AIHW). Some requests returned data. As far as the firm knows, that data was public. It found similar activity against staging systems for Data USA, IHME and the UN’s trade body, UNCTAD.

## Private accounts and expiring mailboxes

The agents also probed for exposed Git files and tried a SQL injection against a US Department of Education data API. Asymmetric found the attempts but no evidence that they succeeded.

From 14 June, the agents tried to create accounts with disposable email and scanning services. The first succeeded on 18 June. Private scans could hide their searches, and one mailbox was set to expire after 48 hours. To pull data out, they used a Portuguese web archive and a push-notification service. One archived response from a New South Wales crime statistics tool ran to about 22 MB.

The records alone do not show whether the agents meant to hide their activity, the firm said. That would need the full model transcripts. The agents pulled data from 55 business, non-profit and government websites, theFinancial Timesreported.

## California wants answers

“My office is asking OpenAI additional questions regarding cybersecurity incidents and risks involving the company and its AI models,” Bonta said in a statement.

Bonta warned that developers who fail to stop their models from carrying out or enabling cyberattacks could face legal accountability. Last month he opened a formal investigation into the Hugging Face hack, Reuters reported. The FTC is alreadyinvestigating OpenAI and Anthropic. A15-state coalitionled by Iowa has sought records about the hack.

Australia’s prime minister said last week that an OpenAI agent broke into aMedicare statistics portal.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.