---
title: 13-year-old bug in ActiveMQ lets hackers remotely execute commands
url: https://www.bleepingcomputer.com/news/security/13-year-old-bug-in-activemq-lets-hackers-remotely-execute-commands/
site_name: tldr
content_file: tldr-13-year-old-bug-in-activemq-lets-hackers-remotely
fetched_at: '2026-04-14T06:00:40.487525'
original_url: https://www.bleepingcomputer.com/news/security/13-year-old-bug-in-activemq-lets-hackers-remotely-execute-commands/
date: '2026-04-14'
description: Security researchers discovered a remote code execution (RCE) vulnerability in Apache ActiveMQ Classic that has gone undetected for 13 years and could be exploited to execute arbitrary commands.
tags:
- tldr
---

# 13-year-old bug in ActiveMQ lets hackers remotely execute commands

 By

###### Bill Toulas

* April 8, 2026
* 01:26 PM
* 0

Security researchers discovered a remote code execution (RCE) vulnerability in Apache ActiveMQ Classic that has gone undetected for 13 years and could be exploited to execute arbitrary commands.

The flaw was uncovered using the Claude AI assistant, which identified an exploit path by analyzing how independently developed components interact.

Tracked asCVE-2026-34197, the security issue received a high severity score of 8.8 and affects versions of Apache ActiveMQ/Broker before 5.19.4, and all versions from 6.0.0 up to 6.2.3

This is also the reason why it was missed for more than a decade.

Apache ActiveMQ is an open-source message broker written in Java that handles asynchronous communication via message queues or topics.

Although ActiveMQ has released a newer ‘Artemis’ branch with better performance, the ‘Classic’ edition impacted by CVE-2026-34197 is widely deployed in enterprise, web backends, government, and company systems built on Java.

Horizon3 researcher Naveen Sunkavally found the issue "with nothing more than a couple of basic prompts" in Claude. "This was 80% Claude with 20% gift-wrapping by a human," he said.

Sunkavally notes that Claude pointed to the issue after examining multiple individual components (Jolokia, JMX, network connectors, and VM transports).

"Each feature in isolation does what it’s supposed to, but they were dangerous together. This is exactly where Claude shone - efficiently stitching together this path end to end with a clear head free of assumptions."

The researcher reported the vulnerability to Apache maintainers on March 22, and the developeraddressed it on March 30in ActiveMQ Classic versions 6.2.3 and 5.19.4.

A report fromHorizon3explainsthat the flaw stems from ActiveMQ’s Jolokia management API exposing a broker function (addNetworkConnector) that can be abused to load external configurations.

By sending a specially crafted request, an attacker can force the broker to fetch a remote Spring XML file and execute arbitrary system commands during its initialization.

The issue requires authentication via Jolokia, but becomes unauthenticated on versions 6.0.0 through 6.1.1 due to a separate bug, CVE-2024-32114, which exposes the API without access control.

Unauthenticated RCE on specific ActiveMQ versions
Source: Horizon3

Horizon3 researchers highlighted the risk posed by the newly disclosed flaw, citing other ActiveMQ CVEs that hackers have targeted in real-world attacks.

“We recommend organizations running ActiveMQ treat this as a high priority, as ActiveMQ has been a repeated target for real-world attackers, and methods for exploitation and post-exploitation of ActiveMQ are well-known,” Horizon3 says.

“Both CVE-2016-3088, an authenticated RCE affecting the web console, and CVE-2023-46604, an unauthenticated RCE affecting the broker port, are on CISA’s KEV list.”

Although CVE-2026-34197 isn’t reported as actively exploited, the researchers say that signs of exploitation are clear in the ActiveMQ broker logs. They recommend looking for suspicious broker connections that use the internal transport protocol VM and the brokerConfig=xbean:http:// query parameter.

The command execution occurs during multiple connection attempts. If a warning message appears about a configuration problem, the researchers say that the payload has already been executed.

## Automated Pentesting Covers Only 1 of 6 Surfaces.

Automated pentesting proves the path exists. BAS proves whether your controls stop it. Most teams run one without the other.

This whitepaper maps six validation surfaces, shows where coverage ends, and provides practitioners with three diagnostic questions for any tool evaluation.

Get Your Copy Now

### Related Articles:

Max severity Flowise RCE vulnerability now exploited in attacks

CISA: New Langflow flaw actively exploited to hijack AI workflows

Adobe rolls out emergency fix for Acrobat, Reader zero-day flaw

Critical Marimo pre-auth RCE flaw now under active exploitation

Critical Fortinet Forticlient EMS flaw now exploited in attacks
