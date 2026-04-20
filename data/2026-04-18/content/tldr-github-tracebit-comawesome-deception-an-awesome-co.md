---
title: 'GitHub - tracebit-com/awesome-deception: An awesome collection of articles, papers, conferences, guides, and tools relating to deception in cybersecurity. · GitHub'
url: https://github.com/tracebit-com/awesome-deception
site_name: tldr
content_file: tldr-github-tracebit-comawesome-deception-an-awesome-co
fetched_at: '2026-04-18T19:41:05.968399'
original_url: https://github.com/tracebit-com/awesome-deception
date: '2026-04-18'
description: An awesome collection of articles, papers, conferences, guides, and tools relating to deception in cybersecurity. - tracebit-com/awesome-deception
tags:
- tldr
---

tracebit-com



/

awesome-deception

Public

* NotificationsYou must be signed in to change notification settings
* Fork9
* Star108




 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

279 Commits
279 Commits
AGENTS.md
AGENTS.md
 
 
README.MD
README.MD
 
 
View all files

## Repository files navigation

# 🥷 Awesome Deception

An awesome collection of articles, papers, conferences, guides, and tools relating to deception in cybersecurity. For a list of open source honeypots, seeawesome-honeypots.

# Contents

* Articles
* Research
* Guides
* Talks
* Conferences
* Communities
* Frameworks
* Related Lists

NOTE- This repo is a fork of a fork (emilyanncr/awesome-deception->tolgadevsec/Awesome-Deception) and aims to be a more regularly updated awesome deception list.

# Articles

* Explain Like I'm Five:Poison Records(2018) (Honeypots for Database Tables). (code)Acra Poison Records.
* Deception Engineering: exploring the use ofWindows Service Canaries(2021) against ransomware. (code)KilledProcessCanary.
* Valve usedsecret memory access “honeypot”(2023) to detect 40K Dota 2 cheaters.Discussion on Hacker Newson potential implementation techniques.
* Discussion on Hacker Newson potential implementation techniques.
* Introducing HASH: The HTTP Agnostic SoftwareHoneypot framework(2023) for creating HTTP low-interaction honeypots. (code)HASH.
* CloudActive Defense(2024): Open-source cloud protection. (code)Cloud Active Defense.
* Thinkst’s It’s Baaack…Credit Card Canarytokens(2024) are now on your Consoles.
* UK’s NCSC onbuilding a nation-scale evidence base(2024) outlines the UK’s goals for large-scale deception deployment.
* LLM Agent Honeypot(2024-2025) - a live experiment tracking AI-assisted attack activity in the wild.
* Wiz’sHoneyBee threat research(2025) covers their open-source honeypot deployment tooling for misconfiguration and exploitation detection.
* GreyNoise ondeploying MCP honeypots(2025) shares results from observing MCP exploitation attempts.
* Building a Military Honeypot(2025) - Penn State’s effort to build deceptive camera and network environments for military use.
* Deel/Rippling lawsuit(2025) - a public case where an insider was detected via a honeypot Slack channel.
* Grafana’ssecurity update on a GitHub workflow issue(2025) includes notes on deploying thousands of canaries.
* AWS onimproving active defense to empower customers(2025) covers its large-scale honeypot system.
* Grafana’scanary tokens “unsung heroes” write-up(2025) shares ROI and lessons learned.
* watchTowr Labs onCanary Credentials in the wild(2025) highlights credential leakage via online tooling.
* UK’s NCSC oncyber deception trials(2025) shares early findings from UK-wide product trials.
* SpecterOps onmapping deception with BloodHound OpenGraph(2025) details how to model deception coverage in BloodHound.
* Resecurity onsynthetic data for cyber deception and honeypots(2025) explores synthetic data to improve honeypot realism.
* Forescout ona hacktivist attack targeting OT/ICS(2025) analyzes the incident, including honeypot use and defensive takeaways.
* UpGuard onpreventing supply chain attacks with honeytokens(2025).

# Research

### Papers

* Demystifying Deception Technology: A Survey(2018) - survey of deception taxonomies, deployment models, and evaluation gaps.
* Deception Techniques in Computer Security: A Research Perspective(2019) - broad survey of deception methods and research directions.
* The Tularosa Study: An Experimental Design and Implementation to Quantify the Effectiveness of Cyber Deception(2019) - HICSS study with 130+ red teamers, manipulating deception presence and awareness while tracking cognitive and physiological effects.
* When Announcing Deception Technology Can Change Attacker Decisions(2024) - study on how disclosure of deception influences attacker behavior.
* Prospect Theoretic Hypothesis Testing-based Cyber Deception(2025) - study on using prospect theory to shape deception during reconnaissance.
* Towards bio-inspired cyber-deception: a case study of SSH and Telnet honeypots(2025) - evaluates bio-inspired deception strategies in Cowrie SSH/Telnet honeypots.
* Koney: A Cyber Deception Orchestration Framework for Kubernetes(2025) - orchestrates deception assets across Kubernetes clusters.
* Applying game theory to deception(2025) - models attacker-defender dynamics using game-theoretic approaches.
* Database Deception using Large Language Models(2025) - applies LLMs to create deceptive database artifacts.
* A Descriptive Model for Modelling Attacker Decision-Making in Cyber-Deception(2025) - proposes a model of attacker engagement decisions under deception cues.
* Agentic AI for Cyber Resilience: A New Security Paradigm and Its System-Theoretic Foundations(2025) - argues for agentic resilience with cyber deception case studies.
* SoK: Honeypots & LLMs, More Than the Sum of Their Parts?(2025) - systematizes LLM-powered honeypot research and evaluation trends.
* HoneyTrap: Deceiving Large Language Model Attackers to Honeypot Traps with Resilient Multi-Agent Defense(2026) - proposes a deceptive LLM defense framework with multi-agent coordination, plus a progressive jailbreak dataset and new metrics for measuring misdirection and attacker cost.
* Measuring the Efficacy of Cyber Deception(2026) - examines how to measure cyber deception effectiveness by reviewing existing evaluation approaches and proposing new metrics and frameworks to assess deceptive tactics in modern, AI-augmented threat environments.
* Q-Cowrie: Reinforcement Learning for Adaptive Honeypot Deception(2026) - presents “Q-Cowrie,” a reinforcement learning-enhanced Cowrie honeypot that models attacker decisions with an MDP and adapts responses during attacker interaction.
* Deception and Detection: Why Artificial Intelligence Empowers Cyber Defense over Offense(2026) - argues that AI automation benefits cyber defense more than offense, widening an offense-defense automation gap as stakes increase.

### Code Repositories

* Evaluating Deception and Moving Target Defense with Network Attack Simulation
* Honeyquest
* Knocking on Admin’s Door: Protecting Critical Web Applications with Deception
* SCANTRAP: Protecting Content Management Systems from Vulnerability Scanners with Cyber Deception and Obfuscation

# Guides

* Birding Guide - Detect attackers without breaking the bank
* Taxonomy and terminology- terminology and definitions for cyber deception.

# Talks

* Deception & Operations Planning Frameworks(2025) - ShmooCon talk on a physical deception operation.
* Applying Deception to the Attack Lifecycle(2025) - Tim Pappa and Skylar Simmons (Walmart) on using deception across the attacker journey.
* Sweet Deception: Mastering AWS Honey Tokens to Detect and Outsmart Attackers(2025) - Nick Frichette.
* Continuous Integration / Continuous Deception: Trying my luck as a malicious maintainer(2025) - Benedikt Haußner.
* Turning The Tables: Using Cyber Deception To Hunt Phishers At Scale(2024) - BSides Exeter.
* Counter Deception: Defending Yourself in a World Full of Lies(2024) - DEF CON 32 (August 2024), Tom Cross and Greg Conti.
* Mirage: Cyber Deception Against Autonomous Cyber Attacks(2024) - Black Hat USA 2024, Ron Alford and Michael Kouremetis.

# Conferences

* Active Defense & Deception (AD&D)- Active conference, most recent event in 2025.
* Honeynet Workshops- Active conference, most recent event in 2025.

# Communities

* /r/cyber_deception
* The Honeynet Project

# Frameworks

* MITRE Engage™EngageData Repository.
* EngageData Repository.
* MITRE D3FEND™D3FENDSoftware Repositories.
* D3FENDSoftware Repositories.
* Deception-as-Detection

# Related Lists

* awesome-honeypots- A thorough and fairly regularly updated list of open source honeypots.

## About

An awesome collection of articles, papers, conferences, guides, and tools relating to deception in cybersecurity.

github.com/tracebit-com/awesome-deception

### Topics

 awesome

 honeypot

 cybersecurity

 awesome-list

 awesome-lists

 deception

 honeypots

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

108

 stars


### Watchers

3

 watching


### Forks

9

 forks


 Report repository



## Contributors1

* andy-smith-tracebitAndy Smith
