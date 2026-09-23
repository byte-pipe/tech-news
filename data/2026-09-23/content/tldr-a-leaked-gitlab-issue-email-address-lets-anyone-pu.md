---
title: A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You
url: https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html
site_name: tldr
content_file: tldr-a-leaked-gitlab-issue-email-address-lets-anyone-pu
fetched_at: '2026-09-23T22:02:12.576363'
original_url: https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html
author: The Hacker News
date: '2026-09-23'
description: GitLab’s non-expiring incoming email token can let a holder commit code with a user’s permissions and trigger CI/CD jobs.
tags:
- tldr
---

# A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You


Swati Khandelwal

Sep 23, 2026
DevOps Security / Supply Chain

The private email address GitLab gives you for filing issues by email is a credential. Anyone who gets it can email a patch that GitLab commits in your name, to any branch you can push to, including main, and can start CI/CD jobs that run as you.

GitLab shows each user this address behind a button labeled "Email work item to this project." Mail sent to it opens an issue in that project, authored by you.

The string in the middle of the address is a token tied to your account, and GitLab's documentation says it does not expire.

The address looks like it belongs to one project. It does not.Aikido Security, which reported the behavior, found that the addresses GitLab creates for a user's different projects all share the same token, and that the token applies to every project the account can open, public or private.

GitLab does not check who sent the email. Any mailbox can write to the address, and GitLab acts on the message as if it came from you. Whoever holds the address can both sign in as you and act with your permissions, without ever touching your mailbox.

The address does more than file bugs. Aikido showed how a holder turns it into a way to commit code, using GitLab's ownmerge request by emailfeature:

1. Change the address suffix from -issue to -merge-request. GitLab then opens a merge request instead of an issue.
2. Write a patch, and put the name of a target branch in the email subject line.
3. Attach the patch and send it. GitLab applies the patch to that branch, and creates the branch if it does not already exist.
4. The change lands as a commit on that branch, authored by you. If it is a branch you can push to, that includes main.
5. If the patch edits the project's .gitlab-ci.yml file and your role allows it, GitLab runs the attacker's job as you.

The merge request itself cannot be directed at a copy of the project the attacker controls, which is why the attached patch, not the merge request, carries the code.

Two things keep this from being worse. The token carries only your own permissions, so how far an attacker gets depends on your role. A leaked address for a Guest account is nearly useless, whereas one for a Maintainer can access protected branches and CI/CD secrets.

Reaching a project also takes more than the address. GitLab works out the target from the project's path and its numeric ID, so an attacker who wants a particular project needs that project's path and ID as well as the token. Public projects publish both. A private project takes a separate leak that names it, though GitLab's project IDs are easy to guess.

Because incoming email is exempt from IP restrictions, the attack can originate from outside an IP allowlist. GitLab's documentation states that incoming email isnot subject to IP restrictions.

Aikido locked a private project to a single IP address that was not its own. GitLab blocked its browser and refused a git clone, but it accepted the merge request email, and the commit landed on main.

The same path skips two-factor authentication. GitLab's documentation notes that incoming email features workwithout 2FA, even on instances that require it.

Every GitLab.com account has one of these tokens, and so does every self-managed GitLab instance with incoming email turned on, which is the default on GitLab.com.

GitLab Dedicated does not appear to be affected, because GitLab limits the feature to self-managed and GitLab.com, but Aikido said it could not test Dedicated directly.

### What to do

You cannot stop other people from having the feature, but you can cut off a leaked address.

* Reset your incoming email token from thepersonal access tokens pagein your profile. The reset replaces every project address at once, so an address you are actively using will stop working until you hand out the new one.
* Look through your own READMEs, contributing guides, and support pages for a posted address. Aikido said it found about a dozen live addresses this way, most of them published on purpose as places to send bug reports, and a few in widely used open-source projects.
* On a self-managed instance, an administrator can turn incoming email off for the whole instance. There is no setting that lets an individual user turn off email-based issue or merge request creation.

GitLab changed the text around the token after Aikido's report. The description now says the address can create issues and merge requests, whereas before it listed only work items, and GitLab removed a line stating that the token could not be used to access any other data.

The behavior has not changed. The token still does not expire, GitLab still does not check who sent the email, and there is still no switch for an individual user to turn off the feature.

GitLab hasopened an issueto look at accepting these emails only from an address verified on the account owner, but that is under consideration, not in place.

Aikido said it first reported the behavior through HackerOne in May 2026, where it was closed as intended behavior, and then filed a confidential issue with GitLab in June. GitLab's position, as Aikido described it, is that this is a token like any other, and that any leaked credential leads to bad outcomes.

The Hacker News has reached out to GitLab and Aikido for comment.

Found this article interesting? Follow us on 
Google News
, 
Twitter
 and 
LinkedIn
 to read more exclusive content we post.

SHARE










Tweet


Share


Share


Share

SHARE 


DevOps Security
, 
Gitlab
, 
Identity Security
, 
Supply Chain

⚡ Top Stories This Week

Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws

Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up

OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads

Public Exploits Released for Four Linux Kernel Flaws That Enable Local Root

New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution

Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root

ThreatsDay: Self-Rewriting Agents, 800+ Flaws Patched, Insider SIM Swaps and 22 More New Stories

Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone

Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks

Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers

Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories

Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation

KREMLIN Banking Malware Hijacks Chrome and Edge to Steal Credentials and Session Tokens

LiteSpeed Enterprise Flaw Could Let One Hosting Account Gain Root Access on a Shared Server

China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE

Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution

New DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing

⚡ Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits

Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users

Attackers Use Passkey Phishing to Hijack Microsoft Cloud Accounts and Exfiltrate Data

N0va Phishkit Targets US and EU Businesses: A New Challenge for Identity Security

An Abandoned CDN Domain Was Re-Registered. Thousands of Sites Still Call It.

How to Evaluate a Unified Security Platform Using a One-Incident Test

Stop Trying to Control AI Behavior. Control What AI Can Reach

⭐ Featured Resources

Validation Summit ’26: See How Pen Testing, Exposure Validation and BAS Work Together

Red Teams: Learn How Attack Path Chaining Changes Automated Security Testing

Turn Threat Intelligence Into Verified Risk With Threat-Led Penetration Testing

Deploy Browser Security Monitoring in Minutes With a Single Header