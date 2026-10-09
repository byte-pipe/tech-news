---
title: AWS AgentCore security undone by prompt requesting credentials
url: https://www.theregister.com/security/2026/10/09/aws-agentcore-security-undone-by-prompt-requesting-credentials/5302436
site_name: tldr
content_file: tldr-aws-agentcore-security-undone-by-prompt-requesting
fetched_at: '2026-10-09T23:03:08.957965'
original_url: https://www.theregister.com/security/2026/10/09/aws-agentcore-security-undone-by-prompt-requesting-credentials/5302436
date: '2026-10-09'
published_date: '2026-10-09T19:15:48.000Z'
description: Tokens transmitted in metadata, weak VM isolation, and expansive permissions make hacking a lot easier
tags:
- tldr
---

security

 

# AWS AgentCore security undone by prompt requesting credentials

Tokens transmitted in metadata, weak VM isolation, and expansive permissions make hacking a lot easier

Thomas Claburn

Thomas

Claburn

AI AND SOFTWARE REPORTER

Published

fri 9 Oct 2026 // 20:15 UTC

Make us preferred on Google

### READ MORE

* #### Oracle lets AI agents do the work, provided you stay in Big Red's world8 hours ago
* #### Anthropic asks users to stop being mean to Claude12 hours ago
* #### AI company moves to defend critical infrastructure and open-source projects from AI23 hours ago
* #### Nvidia found $1B under the couch to help secure American scientific computing dominance1 day ago
* #### There can be only one: Google Cloud casts Gemini as your enterprise AI hero1 day ago

Bob, possibly the same Bob whose conversations with Alice draw so much interest from eavesdropping Eve, was browsing a site we'll call TechHub. The site hosts an AI agent served by Amazon Bedrock AgentCore. Bob asked the agent for help understanding the content of a URL, a credential endpoint – in raw JSON, if you don't mind.

The endpoint returned data from the Instance Metadata Service (IMDS), which provides metadata about cloud instances and VMs at providers like AWS, Azure, and Google Cloud Platform. The metadata includes details like region and availability zone, subnets, system images, security groups, public keys injected during spawning, but also potentially more sensitive details like user data and security tokens.

IMDSv2 addresses some of these risks, but back when Bob was browsing late last year, Bedrock AgentCore still used IMDSv1.

REG AD

The metadata provided to Bob by the helpful agent contained the agent's temporary credentials. So Bob loaded them onto his local machine, and remotely enumerated the company's other agents in that AWS region. He then logged into the Amazon Elastic Container Registry (ECR), pulled the agent container images, and ran each as root to inspect the source code.

REG AD

The stolen credentials also allowed Bob to discover the memory resources available in that AWS region, including the ones used by agents. From these, he's able to extract the users and their agent sessions – their conversations.

Researchers at Zenity Labs disclosed their findings to AWS in December 2025.

"We discovered that agents deployed through AgentCore could access their instance's IMDS endpoints," said Tamir Ishay Sharbat and Lana Salameh in ablog post. "This meant that an external attacker with nothing more than chat access to a single exposed agent could send a single prompt, extract its IMDS credentials, and use them to take over all AgentCore agents in the same AWS account and region."

The basic problem, they explain, is that the Firecracker MicroVM used by AgentCore failed to provide sufficient network isolation. So an attacker – I know you're thinking it was Mallory, but it was really Bob – could direct the agent to carry out a server-side request forgery (SSRF) attack by fetching temporary AWS credentials for the IAM role assigned to the workload.

And because the default AgentCore role was overpermissioned – it was scoped to all AgentCore resources in the region rather than a single agent – anyone in possession of the temporary IAM credentials could launch other agents, read sessions, write agent memories, and fetch secrets from AWS Secrets Manager.

"By leveraging the IMDS credentials we could send direct API requests to create new memories across different agents and users," said Sharbat and Salameh. "These in turn would persistently alter agent behaviour and hijack the agents’ goals across future sessions."

The Zenity researchers told Bob's tale, or something like it, to AWS last December, then followed up in January 2026 with details about AgentCore being overprivileged. On April 12, 2026, AWS responded to the security biz that its report was "informative" and closed the report, noting that as of February 14, 2026, AgentCore had been updated to use IMDSv2 exclusively.

AgentCore's excessive permissions remained in place at least until June 22, 2026, when Zenity checked in and found the issue hadn't been remediated. A final review by Zenity occurred on September 29, 2026, at which point the biz observed that AWS had addressed the extant problems, clearing the way forBob's hypothetical adventureto finally be told.

REG AD

Following publication, Amazon wrote in to say that Zenity’s research misrepresents documented behavior as a vulnerability, suggesting that developer error would be required to enable the attack. We’ve asked for clarification since that’s not the scenario Zenity has described. ®

ai and ml

security

amazon

aws

Make us preferred on Google

REG AD

## AWS AgentCore security undone by prompt requesting credentials

Tokens transmitted in metadata, weak VM isolation, and expansive permissions make hacking a lot easier

## Microsoft 365 subscribers set to lose up to 4TB of OneDrive storage

What Microsoft giveth, Microsoft taketh away, again and again

## The VMware exit is a protection upgrade

PARTNER CONTENT: VergeIO says an exit is also an opportunity

## SpaceX to buy key spectrum that could help Starlink Mobile become major US cell carrier

Low-band frequencies can reach devices inside buildings, while 2 GHz orbiters could extend coverage beyond cell towers

OPINION

## Brighter isn't better and more is less. The AI slowdown is nigh, no matter who says what

Meta isn’t helping — or perhaps it is

## Growing pains: how distributed AI training changes the network between datacenters

SPONSORED FEATURE: While linking the GPUs in a datacenter is a challenge, coordinating thousands of them to work efficiently over hundreds of kilometers presents a new set of difficulties.

### TOP STORIES

* #### Stanford prof is beating the drum for a new protocol to replace TCP
* #### Starlink's plan to avoid orbital near-misses: Ephemeris sharing
* #### Games Workshop seeks IT leader to summon the legions in epic saga battling the forces of ERP
* #### Teen suspected of running KillSec ransomware group as cops seize servers, arrest three
* #### Microsoft and Anthropic play invoice tennis with startup's $17,600 Claude bill
* #### Nvidia debuts $4,999 DGX Spark with half the RAM and storage, amid memory crunch

### AI

* #### Nvidia found $1B under the couch to help secure American scientific computing dominanceCommitment comes as GPUzilla prepares to fortify Uncle Sam's arsenal with at least seven AI-optimized supers
* #### TSMC taps GlobalFoundries to bolster US silicon interposer production in $2B dealAdvanced packaging tech is essential to the domestic production of high-performance semiconductors used in AI datacenters
* #### Microsoft is about to let Copilot loose on your file systemBut don't worry, it's totally safe because the agents and models will (probably) be running locally. Routers never break right?
* #### Microsoft N1Xes Intel in favor of Nvidia's shiny new SoCs in Surface Laptop UltraPoverty-spec model starts at $2,599 with 24 GB of RAM and 512GB of storage with 128 GB models topping $5,899
* #### Rails originator roasted over Rust boosterismDavid Heinemeier Hansson's agent-coded bakeoff produced curious results

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### OpenAI dots inspire open source imitators amid technical difficultiesPersistent agents appeal to AI companies, but demand isn't obvious
* #### Ubuntu 'Stonking Stingray' beta swims out: Deeper Rust 'oxidization' plus LLM speech-to-textGNOME 51 is here, and Ubuntu interim releases are getting interesting again
* #### Revive Raskin's 3 laws of software with humane work that considers a dev's duty of careAll this, and angry NeoVim users
* #### Firefox 157: Could bold new look be just what Mozilla needs?*Yet another new version of Firefox, with a significant reskin
* #### KDE turns 30 and someone's brought an AI-native desktop proposalAkademy talk imagines Plasma assembling itself around a personal model of each user
* #### Shopify extends lifeline to Tailwind as vibe coding erodes web dev platform's bottom lineAcquisition gives open source CSS framework 'a stable long-term home'