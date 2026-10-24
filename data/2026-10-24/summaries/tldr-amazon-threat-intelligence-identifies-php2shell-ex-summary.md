---
title: Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog
url: https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot
date: 2026-10-24
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-24T14:32:52.337670
---

# Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog

## Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot

Amazon Threat Intelligence discovered a PHP2Shell exploitation attempt on October 17, 2026, in MadPot telemetry, four days prior to the public disclosure of CVE-2026-109618 and CVE-2026-109619. The exploit originated from an IP address associated with a commercial anonymization network.

## Vulnerability Embargo and Public Disclosure

The vulnerability was under embargo, set to be lifted on October 21, 2026, at 14:00 UTC. On that day, Amazon Threat Intelligence identified multiple proof-of-concept exploits for the vulnerability, with the earliest around 2026-10-21 02:00 UTC.

## Exploitation Attempts and Anonymized Infrastructure

Subsequently, from October 21, 2026, 02:00 UTC to 2026-10-21 08:00 UTC, Amazon Threat Intelligence identified additional exploitation attempts targeting MadPot from additional anonymized infrastructure. The actual payloads and choices in anonymization infrastructure varied.

## Lessons Learned

* An embargo protects defenders only until someone else finds the same bug.
* Coordinated disclosure is still the right model, but defenders should not assume the public disclosure date is the earliest date of exploitation.
* The time from patch to working exploit is shrinking due to AI-assisted analysis.

## Security Implications

* For critical vulnerabilities in internet-facing systems, measure patch and mitigation timelines in hours.
* Start investigations from the earliest known exploitation, not from the disclosure date (starting from October 17th).
* Invest in detections that don't rely on a signature for a specific CVE.
* Consider alternative approaches for handling vulnerabilities, such as using threat intelligence to anticipate exploitation attempts.