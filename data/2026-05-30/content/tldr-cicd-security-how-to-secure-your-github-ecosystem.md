---
title: 'CI/CD security: How to secure your GitHub ecosystem | Datadog'
url: https://main.d2372vaejiu5h9.amplifyapp.com/blog/secure-your-github-ecosystem/
site_name: tldr
content_file: tldr-cicd-security-how-to-secure-your-github-ecosystem
fetched_at: '2026-05-30T11:32:37.761022'
original_url: https://main.d2372vaejiu5h9.amplifyapp.com/blog/secure-your-github-ecosystem/
author: Juvenal Araujo, Julie Agnes-Sparks, Bowen Chen
date: '2026-05-30'
description: Learn how to apply a detection-based threat model to secure your GitHub ecosystem by identifying key inputs, identities, and their associated risks.
tags:
- tldr
---

Juvenal Araujo

 
 
 
 
 
 

Julie Agnes-Sparks

 
 
 
 
 
 

Bowen Chen

 

In Part 1 of this series, we discussed the CI/CD security boundary, mapped out potential attack vectors with a CI/CD threat matrix, and introduced a simple threat model focused on ideating detection workflows. In this post,we’ll apply these principles to a real-world source code management (SCM) tool examplethat every developer is familiar with: GitHub.

In addition to threat modeling, we’ll also betaking a closer look at historical attacks on GitHub and GitHub Actions ecosystems. Based on these attacks, we’ll discuss preventative measures to help you secure your environment as well as response workflows.

## Threat modeling for GitHub

As we previously discussed, a threat model is a structured representation of all the information surrounding the security of an application or ecosystem. To apply our detection-based threat model to GitHub, we’ll first identify theinputs,identities, andinfrastructurethat pertain to the SCM and their correspondingrisks.

Inputs:

* Authentication
* Source code (through pushes, PRs, reviews, commits)
* Instructions for the CI/CD phase
* GitHub configurations (including webhooks)
* Secrets (if using GitHub Actions)

Theidentitiesthat can access these inputs are then:

* Authenticated users via SSO, SSH,personal access tokens (PATs), and GitHub Apps
* Unauthenticated users (if public repositories exist)

In this case, we can omit infrastructure because it falls outside of the scope for GitHub as a SaaS platform.

When it comes torisks, for each input, we need to ask ourselves, “What is at risk if an attacker gains control of this input or accesses previously inputted data?”

 
 
 
 
 
 
Input
Risk
 
 
 
 
 
Authentication
Unauthorized access
 
 
Source code (pushes, PRs, code review, commits)
backdoor entry, code vulnerability, data exfiltration
 
 
GitHub configurations
Disable protections or exfiltrate data
 
 
Instructions for CI/CD
Execute malicious code
 
 
Secrets (if using GitHub Actions)
Expose secrets
 
 
 
 
 
 

As an example, consider the inputinstructions for CI/CD. For each risk associated with this input (in this case, malicious code execution), we need to identify how an attacker can realize the risk, the log sources that surface each attack pathway, and develop detection methods based on the available logs. Starting from the risks, we can map these variables out as shown below:

 
 
 
 
 
 
 
 
 
 
 
 
 
 
Close dialog

 
 
 
 
 
 

Given that an identity already has access to the instructions for CI/CD input, they can realize the risk of malicious code execution in several ways, such as:

* Adding malicious code to CI configuration files such as those stored in.github/workflows/*
* Manipulating tests and scripts that CI jobs run
* Adding malicious or vulnerable dependencies to files such aspackage.jsonandrequirements.txt

Consider the most direct attack pathway: adding malicious code to CI job instructions. Because GitHub audit logs don’t log changes to code files, we need to rely on a code scanner such asDatadog Static Code Analysis (SAST), CodeQL, or Dependabot. AI security tools such asBewAIrecan also automatically review the diff of each PR and classify them as benign or malicious by evaluating intent from code changes and contextual metadata. Using these tools, you can detect changes to triggers executed by CI jobs, code that enumerates or logs environment variables, the use of external command-line utilities such ascurlandwget, and new third-party dependencies that were not originally present in your code.

Let’s take a quick look at a different risk example: data exfiltration given a compromised source code input.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
Close dialog

 
 
 
 
 
 

For the risk of data exfiltration, any authenticated GitHub user can realize the risk via multiple avenues such as mass cloning of private repositories onto their local machine, scanning the codebase for secrets, or making a private repo go public.

Once an attacker gains authenticated access, for example via a compromised PAT, they can clone private repositories at scale to their local device and scan them for secrets that would enable lateral movement. This and other common attacker behavior are recorded events in GitHub audit logs, which enables them to be detected by cloud SIEM tools. For example, using Datadog’s out-of-the-box (OOTB) security rules, you can detect events such as themass exfiltration via cloning of repositoriesusing a PAT or when a PAT is used by apreviously unseen user agent.

## Tips to protect your GitHub environment against known attacks

Previously, we discussed how to anticipate the different risks associated with inputs in your GitHub environment and how to ideate detection mechanisms. However, we can also glean detection opportunities from historical attacks on GitHub environments.

### The Shai Hulud npm worms

In late 2025, two self-replicating npm worms dubbedShai-HuludandShai-Hulud 2.0compromised over 1,000 unique npm packages, affecting over 500 unique GitHub users and over 14,000 GitHub repositories. The Shai-Hulud worms use thepost-installandpre-installscripts of thepackage.jsonfile to install and run their payload. During this execution, the malware downloads and runsTruffleHog, a legitimate open source tool that the malware uses to scan its host for API keys, secrets, and other hardcoded credentials. These are then exfiltrated to a hardcoded webhook endpoint and public GitHub repositories.

What makes the Shai-Hulud worms so pervasive is that when they discover additional npm or GitHub publishing credentials, they create and publish a new version of npm packages with the malicious payload inserted in the install script. Downstream consumers that install or update the compromised packages then become infected, repeating the cycle above.

 
 
 
 
 
Sample process tree of a supply chain attack involving a malicious npm package. Credentials are harvested and exfiltrated using the GitHub API.
 
 
 
 
 
 
 
 
Sample process tree of a supply chain attack involving a malicious npm package. Credentials are harvested and exfiltrated using the GitHub API.
 
 
 
Close dialog

 
 
 
 
 
 

To stay up-to-date with the latest compromised packages, Datadog maintains the open sourcesupply chain firewall security (SCFW) CLI tool. SCFW automatically blocks the installation of known malicious npm and PyPI packages when developers run these package managers from their CLI, protecting your environment against malware such as Shai-Hulud before the payload has the chance to be installed and executed.

However, this type of traditional security tooling can only protect againstknown compromised packages. When installing code, you also need to answer,“does this code look malicious?”GuardDog answers this exact question—it statically scans code from sources such as npm, PyPI, and GitHub Actions using heuristics that flag common malware patterns, such as the use ofcurlorwget, persistent lifecycle scripts, and self-propagation logic.

### Unauthorized OAuth token access

Let’s look at another supply chain attack. In 2022, attackers gainedunauthorized access to OAuth tokensissued to third-party integrations, Heroku and Travis CI, which were then used to access GitHub’s API and exfiltrate data in a workflow similar to our last threat model example. Attackers were able to surface secrets, such as AWS API keys stored in private repositories that were then used to enumerate cloud resources and exfiltrate data from S3 storage.

Compromising OAuth token access is a common target entry point for attackers, who try to gain transitive access via authorized third-party integrations or through phishing schemes that attempt to have authenticated GitHub users grant permissions to malicious applications. For example,in this recent phishing scheme, fake security alerts were sent to GitHub users notifying them of “unusual access attempts.” The alert recommended several methods to secure their account, all of which led to an authorization page for agitsecurityappthat requested a wide scope of risky permissions, enabling attackers to gain full access to the target user’s accounts and repositories.

Using security products such asDatadog Cloud SIEM, you can detect common attack behavior that stems from compromised OAuth tokens and PATs. Normally, OAuth token usage occurs from a subset of fixed IP addresses or a consistent set ofAutonomous System Numbers (ASNs), which are large groups of IP addresses from a single network or cloud provider.

Once an attacker gains access to an OAuth token, they will often use it from their own server or environment to enumerate access and exfiltrate data.Cloud SIEM’s OOTB detection rulescan identify when OAuth tokens are used from different ASNs and user agents and alert your security team so they can temporarily block the user in GitHub while they conduct a follow-up investigation.

Similarly, Cloud SIEM also offers rules todetect mass zip file exfiltrations of repositoriesusing OAuth access tokens, which is a common end goal for malicious actors. It also flags whenOAuth application access restrictions are disabled, a configuration change that enables attackers to persistently access your environment via third-party OAuth applications.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
Close dialog

 
 
 
 
 
 

### Compromised third-party dependencies

In October 2021, a widely used JavaScript library npm packageua-parser.jswas hijacked and modified with malicious code that targeted secrets stored as environment variables and also ran a cryptominer. If an organization updated to the newest version ofua-parser.js, the compromised package wouldtrigger a GitHub Actions workflowto execute the info-stealing script on a GitHub-hosted runner. Because cloud credentials, API keys, and other secrets are stored within the runner’s environment variables, they were accessible to the malicious pre-install script that was executed during CI.

To safeguard your GitHub environment against vulnerabilities introduced by third-party dependencies—including compromised npm packages and open source libraries—you’ll need to use a static code analyzer or dependency checker such asDatadog Code SecurityorGitHub Dependabot. UsingCode Security’s Software Composition Analysis (SCA), you can scan your open source libraries to detect known and emerging security vulnerabilities before package changes get pushed to production.

This process enables the detection of changes to preinstall and postinstall scripts, which should always be treated with caution. Below is a basic template for an SCA rule to detect preinstall scripts, which were a primary vector in the Shai-Hulud 2.0 attack. This template can be modified to be more granular, looking for deeper patterns such as commands to download files from external sources, open network connections, or modify file systems.

 
1
rules:
2
 
- id: suspicious-preinstall-script
3
 
name: Detect preinstall script in package.json
4
 
languages: [json]
5
 
severity: WARNING
6
 
message: >
7
 
Suspicious: A "preinstall" script was found in package.json. This can be abused
8
 
and is a common tactic in malicious npm packages.
9
 
pattern: |
10
 
{
11
 
"scripts": {
12
 
"preinstall": ...
13
 
}
14
 
}
15
 
metadata:
16
 
category: supply-chain
17
 
technology: nodejs
18
 
tags: [npm, scripts, preinstall, supply-chain, malware]
19
 
confidence: HIGH
 

## Secure your supply chain with Datadog

In this blog, we appliedthe threat model discussed in the previous part of this seriesto GitHub and mapped out different control inputs, their associated risks, and identities. We also reviewed historical supply chain attacks and discussed how different Datadog Security products can help you protect your CI/CD systems against these attacks.

Check out our Cloud Security documentationto learn how to get started. You can read more about emerging threats and vulnerabilities—such as the Shai-Hulud worms and other security research—at Datadog Security Labs.

If you don’t already have a Datadog account, see how you can protect your environment bysigning up for a free 14-day trial.

 
 

 
 

Further reading

 
 

White Paper: DevSecOps Maturity Model

 
 
 
 
 
 
 

Get a blueprint for assessing and advancing your DevSecOps practices.

 
 
Download to learn more
 
 
 
 
 

## Related jobs at Datadog

 
 

### We're always looking for talented people to collaborate with

 
 

Featured positions

 
 
 
 
 
 
 
 
 
 
 

We havepositions

 
 
 
 
View all
 
 
 
 
 
 
 

## Start monitoring your metrics in minutes

 
find out how