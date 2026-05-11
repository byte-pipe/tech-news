---
title: A DOD contractor’s API flaw exposed military course data and service member records | CyberScoop
url: https://cyberscoop.com/schemata-dod-contractor-api-flaw-military-data-exposure/
site_name: tldr
content_file: tldr-a-dod-contractors-api-flaw-exposed-military-course
fetched_at: '2026-05-11T19:47:29.505399'
original_url: https://cyberscoop.com/schemata-dod-contractor-api-flaw-military-data-exposure/
author: Greg Otto
date: '2026-05-11'
published_date: '2026-05-06T21:15:13+00:00'
description: A basic API flaw in Schemata’s AI training platform exposed U.S. service member records and confidential military manuals. Researchers at Strix detail a 150-day disclosure struggle before the DOD contractor patched the vulnerability.
tags:
- tldr
---

Advertisement

Subscribe to our daily newsletter.

Subscribe

Close

A defense technology company with Department of Defense contracts exposed user records and military training materials through API endpoints that lacked meaningful authorization checks, according toan account published by Strix, an open-source autonomous security testing project.

The issue affected Schemata, anAI-powered virtual training platform used in military and defense settings. According to Strix, an ordinary low-privilege account was able to access data across multiple tenants, including user listings, organization records, course information, training metadata and direct links to documents hosted on the Schemata’s Amazon Web Services instances.Strix said the exposed materials included a 3D virtual training course for naval maintenance personnel with documentation marked confidential and proprietary, a course containing Army field manuals on explosive ordnance handling and tactical deployment, and hundreds of user records linked to bases and training enrollments. Additionally, the exposed information included names, email addresses, enrollment details and the military bases where U.S. service members were stationed.

Schemata acknowledged the affected endpoints were exposed May 1, after what Strix described as a 150-daydisclosureprocess. Strix said it verified remediation before publication and published its account earlier this week, 152 days after its initial disclosure attempt.

The reported vulnerability did not require a complex exploit. Strix said it used a low-privilege account to watch normal browser traffic, identifyAPIendpoints exposed through the application, and request high-value data using the same session. According to Strix, those requests returned records from outside the account’s own organization, suggesting the API was not properly enforcing tenant boundaries or user permissions.

Advertisement

In multi-tenant software, authorization controls are intended to ensure users can access only the data and functions assigned to their account or organization. The failure described by Strix would represent a basic breakdown in that model. The firm said some routes also appeared “write-enabled,” meaning a malicious actor could potentially modify or delete courses through update or delete requests, though the account does not say Strix performed destructive testing.

Strix did not respond to CyberScoop’s request for comment.

Schemata’s platform serves military and defense training environments, where user identities, assignments and course enrollments can reveal sensitive operational context. Even when information is not classified, records showing where service members are based, what training they are enrolled in and which materials they can access may create risks if exposed outside intended channels.

In a statementposted on the company’s website, Schemata said it did not have “evidence that any third party exploited the vulnerability to access customer data.”

The disclosure timeline also raises questions about how companies handling sensitive government-related data receive and respond to vulnerability reports. Strix said it first contacted Schemata on Dec. 2, 2025. According to the account, Schemata’s CEO initially responded, “I would love to hear what the vulnerability is, but I assume you want to get paid for it. Is that the play?”

Advertisement

Strix said it clarified the same day that compensation was not required and that its priority was user safety. It said it sent multiple follow-ups from Dec. 8-29, warning that the vulnerability was critical and asking where to send details. Five months later, after telling Schemata that researchers were publishing the information publicly, Schemata responded, acknowledged the exposed endpoints and said it would patch the issue immediately.

“After we received actionable details about the vulnerability and confirmed the security researcher appeared to be legitimate, our team remediated the vulnerability the same day, and the researcher independently verified the fix before publishing their findings,” Schemata’s statement reads. “We appreciate the security researcher bringing this to our attention and their contribution to the security of our platform.”

Schemata said it’s working with cybersecurity consultants to assist with its response and improve its security posture. The company also said it is in contact with government authorities about the vulnerability.

Defense contractors that handle Controlled Unclassified Information, or CUI, must report cyber incidents to the Department of Defense Cyber Crime Center (DC3). The center did not respond to CyberScoop’s request for comment.

According to contracting data, the company holds $3.4 million in contracts with the Department of Defense. In May 2025, Schemataannounced $5 million in venture fundingfrom several firms, including Andreessen Horowitz.

## Latest Podcasts

 

#### When iPhone exploits turn into commodities

 

#### Can you prove which agent did what?

 

#### How government and Industry can raise the cost of cybercrime

 

#### Proving Identity in the age of agents

### Government

* Trump officials are steering a cybersecurity scholarship program toward AI
* One House Democrat is pressing Commerce on the government’s spyware use
* CISA wants critical infrastructure to operate ‘weeks to months’ in isolation during conflict
* CISA boasts AI automation improvements to threat analysis, mission support

### Technology

* A college student is suing a dating app that allegedly used her TikTok videos to target men in her dormitory
* US government, allies publish guidance on how to safely deploy AI agents
* Surveillance campaigns use commercial surveillance tools to exploit long-known telecom vulnerabilities
* Vuln in Google’s Antigravity AI agent manager could escape sandbox, give attackers remote code execution

### Threats

* Ivanti customers confront yet another actively exploited zero-day
* American duo sentenced for hosting laptop farms for North Korean IT workers
* A critical Palo Alto PAN-OS zero-day is being exploited in the wild
* Latvian national sentenced for ransomware attacks run by former Conti leaders

### Policy

* FCC tightens KYC rules for telecoms, closes loophole for banned foreign services
* Congress kicks the can down the road on surveillance law (again)
* Congress, industry ponder government posture for protecting data centers
* Chinese national extradited to US for pandemic-era Silk Typhoon attacks