---
title: 'Cloud Threat Highlights: H1 2026 | Wiz Blog'
url: https://www.wiz.io/blog/cloud-threat-highlights-h1-2026
site_name: tldr
content_file: tldr-cloud-threat-highlights-h1-2026-wiz-blog
fetched_at: '2026-08-10T15:30:35.244224'
original_url: https://www.wiz.io/blog/cloud-threat-highlights-h1-2026
date: '2026-08-10'
published_date: '2026-08-06T10:03:03-04:00'
description: Cloud and AI threat activity tracked by Wiz Research and CIRT, January through June 2026
tags:
- tldr
---

Wiz
Pricing
Get a demo
Get a demo

In the first half of 2026, Wiz's Research and CIRT teams tracked threats affecting thousands of cloud environments. We saw a notable increase in the volume of activity, with supply-chain attacks running at a previously unseen scale and developer toolchains and AI infrastructure drawing serious attention. The aftereffects of these widespread access operations reverberated for months, with credentials stolen in these campaigns being used in other groups' operations months after the original theft. The supply-chain attacks themselves were often self-perpetuating; with compromised packages harvesting developer credentials that were used in the next compromise.

## H1 2026 In Numbers

Compared to the previous half,the volume of significant incidents we highlighted to customers was up 60%from H2 2025, the highest we've seen in a single period, and nearly double H1 2025.

Two things drove the increase.Notable supply-chain attacksmore than doubled.They went from making up about 10% of significant incidents in H2 2025 to 25% in H1 2026. TeamPCP, North Korea and at least three independent operations were all running campaigns during the same time period, across npm, PyPI, Composer, VSCode extensions, Jenkins plugins and AUR. Several of those ecosystems hadn't been targeted this way before.

Second,the volume of new vulnerability disclosures we highlighted roughly doubledcompared to the second half of 2025, a trend consistent with the broader acceleration in AI-assisted vulnerability research and weaponization.

Activity targeting AI infrastructure also grew significantly, roughly doubling compared to the second half of 2025.There were unauthenticated RCE vulnerabilities and credential leaks that affected tools present in a third of the cloud environments we monitor.

In contrast to the above, the number of significant incidents taken up by exploitation ofinternet facing applianceswas fairly constant, but did not keep pace with the other types,dropping from 30% of incidents to 17%.

## Software supply chain sprees

### TeamPCP

The dominant story of the half-year was asoftware-supply-chaincampaignrunby TeamPCP. It moved through hundreds of organizations, drew public postmortems from several named victims and reached GitHub itself, which disclosed unauthorized access to its internal repositories after a poisoned VSCode extension compromised an employee’s credentials. The group eventually open-sourced its tooling and posted a bounty for the largest attack using it.

TeamPCP's malicious code was under constant development throughout their spree. The core loop stayed the same: a poisoned npm package steals developer credentials and uses them to reach cloud environments, chaining from one victim's secrets to the next. But the tooling grew more aggressive. The April-Mayvariantwas distributed via PyPI for the first time, exploited GitHub Actions CI misconfigurations to poison build caches and extracted OIDC tokens directly from runner memory. By the AntVcompromisein May, the group was taking over maintainer accounts and pushing malicious versions across hundreds of packages. Wiperstriggeredby token revocation accompanied later payloads, with taunting commit messages and Dune-themed repository names. Across multiple victims, tokens with admin scope were used to strip branch protection and force-push malicious commits.

While at one point, TeamPCP listed roughly four thousand stolen private repositories for sale, the majority of the follow-onactivityto these breaches had a long tail. While some credentials were validated within hours, we also saw personal access tokens stolen in May reused weeks later in a wave of hands-on intrusions aimed at data theft, used by what we believe were different groups.

Figure 1: TeamPCP’s cascade of compromises as of June 5th, 2026. All incidents drawn from public reporting

Wiz has been hard at work improving our responses to these types of incidents and are now able to identify significant compromises within minutes. The focus that Wiz and the rest of the security community has put on this problem has helped to notably decrease the amount of time a malicious package is available for download. This shortening of the uptime for these packages creates an opportunity for enterprises to protect themselves by setting “cooldown” policies to not download packages that have been up for less than 24 hours.

Figure 2: Availability Duration of Malicious Packages

### Follow-on campaigns and IronWorm

On May 12, TeamPCP published the Shai-Hulud worm source code on GitHub with the message: "A Gift From TeamPCP". Campaigns running modified versions appeared within days. Separately, the “Megalodon” campaign pushed thousands of malicious commits into public GitHub repositories, backdooring CI workflows at scale.

In June, a campaign branded"Miasma"compromised dozens of packages in the@redhat-cloud-servicesnpm namespace, a widely used trusted scope. The worm was built on the open-sourced Shai-Hulud code but added cloud-identity collectors targeting GCP and Azure metadata services and generated a uniquely encrypted payload per infection so that no two compromised packages shared a hash. A “Hades”-labeled variant followed days later on PyPI.

A separate campaign, dubbed IronWorm, also began on npm in early June. Where Shai-Hulud relied primarily on JavaScript and TypeScript payloads, IronWorm used a compiled Rust binary bundled with a C-compiled eBPF rootkit that filtered process and network data, concealing itself from common user-space tools . It also put more effort into obfuscating its communications, routing them over Tor. A second IronWormoperationemerged in early July.

### Stolen credentials move between groups

Credentials stolen by TeamPCP fed directly into other groups' operations.Lapsus$jointly listed GitHub internal repositories for sale with TeamPCP, pricing access at over $50,000 and in at least one case, a customer extorted by Lapsus$ was initially compromised through a key stolen in a TeamPCP campaign.

### North Korea’s Midnight Neptune (UNC1069)

North Korea has also conducted multiple supply chain operations in the first half of 2026, continuing a campaign that began in2025. In late March 2026, theytrojanizedtheaxiospackage and then on June 17, 2026 they took advantage of a single compromised developer account to trojanize over 140 packages related to@mastra. Though the TeamPCP operations were larger in aggregate, we saw the axios operation impact more customers than any single one of TeamPCP’s compromises and the@mastraoperation’s speed outpaced what TeamPCP was able to do.

Figure 3: The Axios compromise alone was more than twice as big as any single TeamPCP operation

North Korea’s operations have had a different character as well. The initialaxiostrojanization delivered a backdoor, but did not include any of the automated exfiltration or spreading mechanisms present in other actors’ campaigns. This meant that while initial compromise was very widespread, post-compromise activity was limited. In the@mastraoperation, the North Korean actor did add some automated cryptocurrency and cloud secret exfiltration capabilities, but not to the same scale as TeamPCP operations.

## JINX-0163’s emergence

JINX-0163 is a cloud-native extortion gang that Wiz Research began tracking in 2026, initially identified by one of our AI-enabled threat hunting systems. The group consistently targets non-human identities - service accounts and IAM roles - rather than end users. In some cases, they have been able to leverage a single over-privileged identity or exposed state file to pivot and obtain a full inventory of an organization's secrets. They have shown the ability to operate seamlessly across AWS, Azure, GCP, Okta and Snowflake and do so quickly and at scale.

In one of the most severe incidents we attribute to this group, JINX-0163 compromised a cloud-hosted AI development platform. They gained initial access to a single GCP service account and moved laterally, extracting thousands of secrets spread across multiple GCP projects, including customer credentials.

### Extortion is the end goal

Wiz assesses that JINX-0163’s data theft operations are financially motivated and designed to further extortion schemes. Multiple victims of JINX-0163 have received threats from an actor identifying themselves as"FulcrumSec", claiming to have terabytes of victim data and threatening to release it if not paid. Wiz assesses with moderate confidence that FulcrumSec is the public facing identity for JINX-0163; however, we cannot rule out an Extortion-as-a-Service model where multiple actors play different roles.

Wiz’s tracking of this group has led to the deployment of focused detections to identify activity in customer environments. We have also kept our customers up to date with our assessment of the group's goals and tactics, allowing organizations to prioritize their response to the most significant threats.

## AI as a target

AI tooling compromise was an emerging trend this half. While still a relatively low volume, we saw an increase in vulnerability disclosures, misconfigurations and attacker activity trying to take advantage of the growing attack surface presented by AI infrastructure. While some of these discoveries are due to the growing industry focus on AI security (ours included), the rapid growth in deployment of these technologies is likely to make them a focus for malicious actors in the years to come.

### Critical vulnerabilities across the AI toolchain

AI tools drew significantly more attention from attackers and security researchers. LiteLLM, an AI gateway present in over a third of the cloud environments we monitor, had four separate security events in six months: a supply-chain compromise, an SQL injection vulnerability exploited in the wild, a privilege escalation chain and an authentication bypass. Dify, Langflow, n8n and Ollama each had critical unauthenticated vulnerabilities of their own.

### Exposure and misconfiguration

As these are new technologies, the security practices around deploying them haven't caught up to how widely they're adopted. We see AI endpoints exposed to the internet without authentication with access to backend credential stores, coding agents on CI pipelines that process untrusted pull request content with write access to production repositories and AI assistants in messaging platforms holding admin-level cloud credentials.

MCP serversare one example Wiz looked at closely. We found unauthenticated MCP endpoints across hundreds of environments, each one a pre-authenticated proxy holding backend credentials and bridging multiple services. The large majority hand their full tool catalog to an anonymous caller and over a third return real data with no credentials at all - one returned a named person's retirement-account balance, another proxied an internal issue tracker holding millions of tickets alongside hardcoded credentials. We see similar patterns with exposed model-serving endpoints, chatbot backends and coding agent sandboxes running with cloud credentials they don't need.

### What attackers are doing with AI infrastructure

We saw several patterns of malicious activity targeting AI infrastructure this half.

In one case, cryptominers were deployed into model-serving environments across several providers. One miner displayed a fake training-job message to blend in, while in another, an attacker exploited a Langflow RCE and installed the miner to.claude/unicorn, disguising it as AI tooling.

In a separate incident we saw an attempt to use plain English instructions to get a coding agent in a sandbox to probe egress permissions, establish persistence through the agent's configuration, open a reverse shell, loot cached credentials and reach for the AWS metadata service.

## Techniques worth watching for

Not every intrusion is interesting from start to finish, but we regularly observe techniques that stand out and are worth looking for in your own environment.

In one case we investigated, after they established a backdoor admin user, we observed an attacker profiling existing IAM users. They identified an active administrator and created an additional access key on that person's account. This gave the attacker a second persistence foothold that hid behind a legitimate employee identity rather than a newly created user, which is harder to spot in a routine IAM review. Monitoring forCreateAccessKeyevents where the calling principal is not the account owner is an effective detection for this technique.

Attackers with access to managed Kubernetes services can call the VM Run Command API against the underlying nodes and get root code execution outside the Kubernetes layer, bypassing container-level controls. VM Run Command calls in Azure Activity Logs are worth monitoring.

During an incident that occurred in a GCP environment, an attacker with compromised service account keys added a foreign domain to the organization'sallowedPolicyMemberDomainspolicy, leveraged that to grant an external account editor access on a project, then removed the grant and the policy change within thirty minutes. This technique is hard to catch because org policy writes are rarely monitored and the transient permission grant looks like noise in audit logs.SetOrgPolicycalls onallowedPolicyMemberDomainsfrom identities that are not known IAM admins are worth monitoring, especially when followed bySetIamPolicyin the same session.

When attackers steal instance role credentials from a Linux host and use them from their own machine, the mismatch shows up in CloudTrail.Boto3reads the local OS at runtime, so the user-agent field reveals the attacker's operating system rather than the instance's. In one case, credentials stolen from a Linux instance appeared in CloudTrail with os/windows in the user-agent. Additionally, theBoto3feature flagcombinationm/e(CREDENTIALS_CODE) indicates that credentials were loaded explicitly into a script rather than sourced from the metadata service, which legitimate EC2 workloads almost never do. The combination of an OS mismatch on an instance role with that flag is a near-zero-false-positive signal.

## Making Customers Safer

Every confirmed intrusion and proactive research effort described in this report feeds directly into Wiz's detection capabilities. Cross-tenant visibility allows us to identify attacker tooling and behavior patterns that no single monitored environment could surface on its own - when a technique is used against one customer, we build the detection so it gets caught everywhere.

During the first half of 2026, the campaigns and techniques covered here drove new and updated detection rules across cloud runtime, identity and supply-chain surfaces. We continue to expand our coverage as the threat landscape shifts.

Tags
#
Research

## Continue reading

### Wiz Brings Automated DISA STIG Assessment to Amazon Linux 2023 and Windows Server 2025

Daniel Klein
, 
Nicole Vainer
, 
Mike Schimmel
, 
Nic Hall
August 6, 2026

Automating DISA STIG Compliance for Amazon Linux 2023 and Windows Server 2025, giving defense and federal teams immediate and continuous hardening validation.

### Wiz at Black Hat 2026: Driving AI Threat Readiness

+
3
Tal Moriah
, 
Shashank Golla
, 
Snegha Ramnarayanan
 
and 3 more
August 4, 2026

Announcing new capabilities that help organizations prepare for the AI era by expanding visibility and accelerating response, so security teams can defend at machine speed.

### keyv and cacheable npm Package Hijacked in Supply Chain Attack

Merav Bar
, 
Rami McCarthy
August 4, 2026

Wiz Research is actively investigating an ongoing software supply chain attack affecting multiple keyv/cacheable npm packages.

Get a personalized demo

## Ready to see Wiz in action?

"Best User Experience I have ever seen, provides full visibility to cloud workloads."
David Estlick
CISO
"Wiz provides a single pane of glass to see what is going on in our cloud environments."
Adam Fletcher
Chief Security Officer
"We know that if Wiz identifies something as critical, it actually is."
Greg Poniatowski
Head of Threat and Vulnerability Management
Get a demo