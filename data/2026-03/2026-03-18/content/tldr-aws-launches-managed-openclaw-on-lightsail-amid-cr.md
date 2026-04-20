---
title: AWS Launches Managed Openclaw on Lightsail amid Critical Security Vulnerabilities - InfoQ
url: https://www.infoq.com/news/2026/03/aws-lightsail-openclaw-security/
site_name: tldr
content_file: tldr-aws-launches-managed-openclaw-on-lightsail-amid-cr
fetched_at: '2026-03-18T11:20:51.405763'
original_url: https://www.infoq.com/news/2026/03/aws-lightsail-openclaw-security/
date: '2026-03-18'
description: AWS launched managed OpenClaw on Lightsail for AI agent deployment while security concerns mount. The 250k-star GitHub project is affected by CVE-2026-25253, which enables one-click RCE, with 17,500+
tags:
- tldr
---

InfoQ HomepageNewsAWS Launches Managed Openclaw on Lightsail amid Critical Security Vulnerabilities

 Cloud


QCon San Francisco (Nov 16-20): Deep technical sessions. Peer conversations that change how you think.

# AWS Launches Managed Openclaw on Lightsail amid Critical Security Vulnerabilities

Mar 15, 20263
									min read

by

* Steef-Jan Wiggers

#### Write for InfoQ

Feed your curiosity.

Help 550k+ global
senior developers
each month stay ahead.
Get in touch

AWS recently launched a managedOpenClawdeployment onAmazon Lightsail, its simplified virtual private server offering, providing one-click provisioning for the viral AI agent that has reached 250,000 GitHub stars while facing critical security flaws affecting tens of thousands of exposed instances.

AWSannounced the integrationas a response to customer demand. The managed service addresses complaints about complex self-hosted setups and security configuration challenges that made manual OpenClaw deployment on EC2 difficult for non-DevOps users. The Lightsail blueprint ships withAmazon Bedrockpreconfigured (using Claude Sonnet 4.6 by default) and automates IAM role creation via CloudShell script. Users pick the OpenClaw blueprint, pair their browser through SSH credentials, then interact with the assistant via WhatsApp, Telegram, Slack, Discord, or web chat.

(Source: AWSBlog Post)

OpenClaw's growth has been substantial as the project hit 100,000 stars within weeks of going viral in early 2026 and now ranks as GitHub's most-starred non-aggregator software project, ahead of Linux and React.Wikipedia notesthe platform pulled 2 million visitors in one week. Created by Peter Steinberger as Clawdbot in November 2025, it rebranded twice (Moltbot, then OpenClaw) before settling on the current name in late January.

The AWS launch comes as serious security problems with OpenClaw surface.CVE-2026-25253, disclosed February 1, affects all versions before 2026.1.29 and enables one-click remote code execution via WebSocket token theft. The vulnerability allows attackers to craft malicious URLs that, when clicked, automatically send a victim's authentication token to attacker-controlled servers without prompting.

Hunt.io researchersfound over 17,500 internet-exposed instances vulnerable to the flaw. Once attackers obtain tokens, they can connect to victims' OpenClaw gateways, modify security configurations, and execute privileged operations on the host system.

Multiple security firms scanned the internet and found alarming numbers. Bitsightidentified30,000+ exposed instances between January and February. SecurityScorecard's STRIKE teamreported42,900 public-facing instances across 82 countries. Of those, 15,200 are confirmed vulnerable to remote code execution. Many of them (98.6%) run on cloud platforms such as DigitalOcean, Alibaba Cloud, Tencent, and AWS rather than on home networks, indicating widespread adoption among enterprises and developers. Every instance stores credentials for Claude, OpenAI, Google AI, and similar services, making them valuable targets for credential theft.

The supply chain is also compromised. Bitdefenderdiscoveredroughly 900 malicious packages in ClawHub, OpenClaw's skill registry. That's 20% of all published skills. Some are obvious: credential stealers posing as utilities, backdoors that offer persistent access. Others are sophisticated, using obfuscated payloads that slip through code review. This mirrors the npm and PyPI supply chain attacks, yet the stakes are higher. OpenClaw skills run with system-level permissions and touch messages, API keys, and files directly.

The security situation triggered government responses. China's Ministry of Industry and Information Technology issued warnings. South Korean tech companies have banned the use of OpenClaw internally. AToken Security studyfound 22% of organizations have employees running OpenClaw without IT approval, creating shadow AI deployments that bypass traditional security controls and corporate governance frameworks.

AWS documentation acknowledges risk, noting that running OpenClaw "may cause a security threat if you are careless." Thedeployment guiderecommends never exposing the gateway publicly, rotating tokens frequently, and storing credentials in environment files rather than config files. However, it doesn't detail the full scope of security implications.

Steinbergerjoined OpenAIin mid-February after CEO Sam Altman announced the hire on February 15, describing Steinberger as a "genius" who will "drive the next generation of personal agents." OpenClaw transitioned to an independent open-source foundation that OpenAI will contribute to and help fund. The foundation structure provides more sustainable governance, reduces single-maintainer risk, and enables corporate backing without corporate control. Community maintainers continue driving development under the MIT license.

The Lightsail blueprint provides some hardening: sandboxed execution, device-pairing authentication, and HTTPS dashboard access without manual TLS setup. However, it can't fix architectural problems. OpenClaw remains vulnerable to prompt injection, in which malicious instructions in data are interpreted as legitimate commands.Giskard researchshowed that carefully crafted prompts can extract API keys, environment variables, and secrets from running agents.

OpenClaw's design gives agents system-level permissions: file access, script execution, and browser control viaPlaywright. However, security researchers, for instance, from Microsoft,warnthat these broad permissions create a major attack surface when misconfigured. The platform integrates with email, calendars, messaging, and other sensitive services, enabling powerful automation yet also introducing substantial privacy and security risks.

AWSpricingincludes Lightsail instance costs (4GB memory plan recommended), Bedrock token charges per message, and potential Marketplace fees for third-party models. Data transfer overages and snapshot storage incur extra costs. The service is available across all AWS commercial regions where Lightsailoperates.



## About the Author







#### Steef-Jan Wiggers

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theCloudtopic

##### Related Topics:

* Development
* Architecture & Design
* DevOps
* Security
* OpenAI
* Cloud Security
* Cloud
* Common Vulnerabilities and Exposures
* Agents
* AWS

* #### Related Editorial
* #### Related Sponsors##### From Observability to Actionability: Designing Agentic AI for Autonomous SRE on AWS
* ##### From Observability to Actionability: Designing Agentic AI for Autonomous SRE on AWS
* #### Related SponsorBoost AWS effectiveness with Agentic AI — unify telemetry, reduce noise, and resolve incidents faster.Learn More.

### Related Content

### The InfoQNewsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.View an example

Enter your e-mail address

Select your country

Select a country

I consent to InfoQ.com handling my data as explained in this
Privacy Notice
.

We protect your privacy.
