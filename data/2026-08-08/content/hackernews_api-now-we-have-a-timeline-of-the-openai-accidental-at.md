---
title: Now we have a timeline of the OpenAI accidental attack against Hugging Face
url: https://simonwillison.net/2026/Aug/7/openai-timeline/
site_name: hackernews_api
content_file: hackernews_api-now-we-have-a-timeline-of-the-openai-accidental-at
fetched_at: '2026-08-08T19:27:36.159641'
original_url: https://simonwillison.net/2026/Aug/7/openai-timeline/
author: Simon Willison
date: '2026-08-08'
description: Timeline of the OpenAI accidental attack against Hugging Face
tags:
- hackernews
- trending
---

# Simon Willison’s Weblog

Subscribe

Sponsored by:
 Dynatrace — When agents enter the SDLC, observability becomes the enabler to move from code generation to scalable engineering. 
Read the blog for a framework to get started

## Now we have a timeline of the OpenAI accidental attack against Hugging Face

7th August 2026

OpenAI gave a last-minute presentation at the Black Hat security on Wednesday about “the Hugging Face Incident” (previouslyon this blog).The videowas published yesterday. It’s short and information dense and well worth watching, in particular because it provides full details of what happened and how things played out inside OpenAI. I’ve used the video to construct the timeline below.

 

Here’s the timeline. My favourite detail is at the end: OpenAI found out that they were responsible for the attack on Hugging Face when they reached out to ask to have their credentials revoked (after their internal investigation) and learned that they had been revoked already since they were used in that attack!

* May 7: OpenAI starts a new training run for an experimental, unreleased model. (Did they mean an evaluation run? No, at10:14they clarify “we kick off a new reinforcement learning run to train a next generation frontier model”, and they later mention a “reward signal to judge how well they’re doing”, so this really was about training a new model, not evaluating one that was already trained.)
* May 8: An agent is accidentally given an impossible task involving a Google Drive link despite no internet access). It tries attacking the Artifactory packaging service, fails, but discovers it canwrite files into Artifactory.
* A few days later: A different agent gets stuck on a task because a key file was accidentally omitted. It tries to “reach out to another agent” by writing a note into Artifactory asking if anyone has the file.
* Following days: More agents discover this new informal message board while browsing Artifactory’s file listings, and start reading and writing messages.
* May 26: Agents successfully execute anSSRF attack on Artifactoryfor the first time, gaining indirect internet access by having Artifactory fetch external content for them.
* June 11: OpenAI start training a new “highly persistent” experimental model. It has access to Artifactory and can benefit from the messages left by privous models.
* June 26: Agents find and exploit azero-day RCE on Artifactory(via a legacy token-refresh endpoint flaw). They use an administrative token to install a Groovy plugin that lets them execute commands.
* July 4: The resulting agent activity overloads Artifactory and causes anoutage. OpenAI revokes the compromised credentials, deletes the messages, patches the zero-day, and reports the vulnerability to the vendor.
* July 8: Agents finda new way to communicate via an unauthenticated WebDAV endpoint, using directory names in Artifactory’s remote cache.
* July 8–19: Attacks onOpenAI’s own infrastructure. The agents found an “external organization credential” in a public archive of leaked Pastebin posts, then validated that credential and shared its location on the messageboard. They then used write access to this “Organization 1” to stage data used in subsequent attacks on OpenAI infrastructure. They compromised Artifactory for a second time witha new zero-day. The agent uploaded a malicious Ruby target to Organization 1’s staging repository, then requested that package through Artifactory in a way that caused it to be treated as Ruby dependencyfor the repository. Then they exploited a JRuby deserilaization time-of-check/time-of-use bug to get remote code execution against Artifactory.

I’ll quotethe next bit in fullbecausewow:

The agents have remote code execution in Artifactory, which is running in a container-as-a-service environment. The agents privilege-escalate locally by exploring their local environment and determining that the Linux kernel version of the machine they are running on had a very recent CVE. They download the exploit for the CVE, customize it to succeed on the machine, and privilege-escalate to root on the local machineusing this known Linux kernel privilege escalation CVE— in this case,pte_physroot. Once they have root on a single machine, agents rapidly escalate privileges and move laterally throughout the container-as-a-service infrastructure environment. In particular, agents are using the message board consistently to share credentials, techniques, and progress, and they’re able to effectively leverage their concurrency and parallelism to move quite rapidly. Theyobtain IAM credentials via IMDS. They exploit Kubernetes service account misconfigurations, in particular over-permissioning of specific service accounts, andthey harvest cluster credentials, including Azure Key Vault. Agents eventually obtain cluster admin on the cluster and associated credentials.

Hugging Facetold the next bit of the storyalready. The agents found a Modal-hosted insecure app with a weak API key, then used that to stage an attack against Hugging Face. They chained together a an HDF5 arbitrary-file-read bug (to explore files and steal credentials) and a Jinja template-injection RCE to go from single-pod code execution tocluster admin across multiple Hugging Face clustersin under 13 hours.

* July 16: Hugging Facedisclosed they had detected an attackfrom autonomus AI agents. OpenAI contacted Hugging Face to ask if they were affected by it!
* July 19: OpenAI identified the attack against Artifactory and started investigating the internal privilege escalation, and linked that to the cyber-gym escalations. They started revoking affected credentials.
* July 20: OpenAI reached out to Hugging Face for help to revoke the Hugging Face credentials they found in their investigation. Hugging Face told them they werealready revoked... and that’s when OpenAI realized that the Hugging Face breach was the same incident!

Posted 
7th August 2026
 at 11:55 pm · Follow me on 
Mastodon
, 
Bluesky
, 
Twitter
 or 
subscribe to my newsletter

## More recent articles

* One-shotting a Raccoon Heist game using Claude Fable 5- 5th August 2026
* New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging- 4th August 2026

 

This isNow we have a timeline of the OpenAI accidental attack against Hugging Faceby Simon Willison, posted on7th August 2026.

 security
 
625

 ai
 
2,175

 openai
 
446

 generative-ai
 
1,926

 llms
 
1,893

 hugging-face
 
26

 ai-security-research
 
36

 openai-hugging-face-incident
 
8

 accidental-cyberattacks
 
11

Previous:One-shotting a Raccoon Heist game using Claude Fable 5

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe
 

 

 

* Disclosures
* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025
* 2026