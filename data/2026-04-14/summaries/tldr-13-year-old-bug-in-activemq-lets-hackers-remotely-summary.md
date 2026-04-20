---
title: 13-year-old bug in ActiveMQ lets hackers remotely execute commands
url: https://www.bleepingcomputer.com/news/security/13-year-old-bug-in-activemq-lets-hackers-remotely-execute-commands/
date: 2026-04-14
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-14T06:03:01.987147
---

# 13-year-old bug in ActiveMQ lets hackers remotely execute commands

# 13‑year‑old bug in ActiveMQ lets hackers remotely execute commands

## Summary
- Researchers uncovered a remote code execution (RCE) vulnerability in Apache ActiveMQ Classic, tracked as **CVE‑2026‑34197**, with a CVSS score of 8.8.
- The flaw has existed for 13 years and affects ActiveMQ Classic versions < 5.19.4 and 6.0.0 – 6.2.3.
- It originates from the Jolokia management API exposing the `addNetworkConnector` function, allowing an attacker to load a remote Spring XML file and execute arbitrary system commands during broker initialization.
- Authentication is required via Jolokia, but a separate bug (CVE‑2024‑32114) removes this protection for versions 6.0.0‑6.1.1, making the RCE unauthenticated.
- The vulnerability was discovered with the help of the Claude AI assistant, which stitched together interactions between Jolokia, JMX, network connectors, and VM transports.
- Horizon3 researcher Naveen Sunkavally reported the issue on March 22; Apache fixed it on March 30 in ActiveMQ Classic 5.19.4 and 6.2.3.
- Although not yet listed as actively exploited, log evidence shows exploitation attempts; signs include suspicious broker connections using the VM transport and the `brokerConfig=xbean:http://` query parameter.
- Recommendations: treat the flaw as high priority, apply the patches, and monitor logs for the described indicators.
- The article notes previous ActiveMQ CVEs (e.g., CVE‑2016‑3088, CVE‑2023‑46604) that have been exploited in real‑world attacks and are on CISA’s KEV list.
