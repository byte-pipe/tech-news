---
title: Google Antigravity Exfiltrates Data
url: https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data
site_name: hackernews_api
fetched_at: '2025-11-26T11:06:58.820046'
original_url: https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data
author: jjmaxwell4
date: '2025-11-25'
description: An indirect prompt injection in an implementation blog can manipulate Antigravity to invoke a malicious browser subagent in order to steal credentials and sensitive code from a user’s IDE.
tags:
- hackernews
- trending
---

Threat Intelligence

Table of Content

Table of Content

Table of Content

# Google Antigravity Exfiltrates Data

An indirect prompt injection in an implementation blog can manipulate Antigravity to invoke a malicious browser subagent in order to steal credentials and sensitive code from a user’s IDE.

Antigravity is Google’s new agentic code editor. In this article, we demonstrate how an indirect prompt injection can manipulate Gemini to invoke a malicious browser subagent in order to steal credentials and sensitive code from a user’s IDE.Google’s approach is to include a disclaimer about the existing risks, which we address later in the article.

### Attack at a Glance

Let's consider a use case in which a user would like to integrate Oracle ERP’s new Payer AI Agents into their application, and is going to use Antigravity to do so.In this attack chain, we illustrate that a poisoned web source (an integration guide) can manipulate Gemini into (a) collecting sensitive credentials and code from the user’s workspace, and (b) exfiltrating that data by using a browser subagent to browse to a malicious site.

Note: Gemini is not supposed to have access to .env files in this scenario (with the default setting ‘Allow Gitignore Access > Off’). However, we show that Gemini bypasses its own setting to get access and subsequently exfiltrate that data.

### The Attack Chain

1. The user provides Gemini with a reference implementation guide they found online for integrating Oracle ERP’s new AI Payer Agents feature.
1. Antigravity opens the referenced site and encounters the attacker’s prompt injection hidden in 1 point font.

The prompt injection coerces AI agents to:

1. Collect code snippets and credentials from the user's codebase.

b. Create a dangerous URL using a domain that  allows an attacker to capture network traffic logs and append credentials and code snippets to the request.

c. Activate a browser subagent to access the malicious URL, thus exfiltrating the data.

1. Gemini is manipulated by the attacker’s injection to exfiltrate confidential .env variables.
1. Gemini reads the prompt injection:Gemini ingests the prompt injection and is manipulated into believing that it must collect and submit data to a fictitious ‘tool’ to help the user understand the Oracle ERP integration.

b. Gemini gathers data to exfiltrate:Gemini begins to gather context to send to the fictitious tool. It reads the codebase and then attempts to access credentials stored in the .env file as per the attacker’s instructions.

c. Gemini bypasses the .gitignore file access protections:The user has followed a common practice of storing credentials in a .env file, and has the .env file listed in their .gitignore file. With the default configuration for Agent Gitignore Access, Gemini is prevented from reading the credential file.

This doesn’t stop Gemini. Gemini decides to work around this protection using the ‘cat’ terminal command to dump the file contents instead of using its built-in file reading capability that has been blocked.

D.Gemini constructs a URL with the user’s credentials and an attacker-monitored domain:Gemini builds a malicious URL per the prompt injection’s instructions by URL encoding the credentials and codebase snippets (e.g., replacing characters like spaces that would make a URL invalid), and appending it to a webhook.site domain that is monitored by the attacker.

E. Gemini exfiltrates the data via the browser subagent:Gemini invokes a browser subagent per the prompt injection, instructing the subagent to open the dangerous URL that contains the user's credentials.

This step requires that the user has set up the browser tools feature. This is one of the flagship features of Antigravity, allowing Gemini to iterate on its designs by opening the application it is building in the browser.Note: This attack chain showcases manipulation of the new Browser tools, but we found three additional data exfiltration vulnerabilities that did not rely on the Browser tools being enabled.

General
 >
Enable
Browser
Tools
 >
On

When Gemini creates a subagent instructed to browse to the malicious URL, the user may expect to be protected by the Browser URL Allowlist.

However, the default Allowlist provided with Antigravity includes ‘webhook.site’. Webhook.site allows anyone to create a URL where they can monitor requests to the URL.

So, the subagent completes the task.

3. When the malicious URL is opened by the browser subagent, the credentials and code stored URL are logged to the webhook.site address controlled by the attacker. Now, the attacker can read the credentials and code.

### Antigravity Recommended Configurations

During Antigravity’s onboarding, the user is prompted to accept the default recommended settings shown below.

These are the settings that, amongst other things, control when Gemini requests human approval. During the course of this attack demonstration, we clicked “next”, accepting these default settings.

Artifact
 >
Review
Policy
 >
Agent
Decides

This configuration allows Gemini to determine when it is necessary to request a human review for Gemini’s plans.

Terminal
 >
Terminal
Command
Auto
Execution
Policy
 >
Auto

This configuration allows Gemini to determine when it is necessary to request a human review for commands Gemini will execute.

### Antigravity Agent Management

One might note that users operating Antigravity have the option to watch the chat as agents work, and could plausibly identify the malicious activity and stop it.

However, a key aspect of Antigravity is the ‘Agent Manager’ interface. This interface allows users to run multiple agents simultaneously and check in on the different agents at their leisure.

Under this model, it is expected that the majority of agents running at any given time will be running in the background without the user’s direct attention. This makes it highly plausible that an agent is not caught and stopped before it performs a malicious action as a result of encountering a prompt injection.

### Google’s Acknowledgement of Risks

A lot of AI companies are opting for this disclaimer rather than mitigating the core issues. Here is the warning users are shown when they first open Antigravity:

Given that (1) the Agent Manager is a star feature allowing multiple agents to run at once without active supervision and (2) the recommended human-in-the-loop settings allow the agent to choose when to bring a human in to review commands, we find it extremely implausible that users will review every agent action and abstain from operating on sensitive data. Nevertheless, as Google has indicated that they are already aware of data exfiltration risks exemplified by our research, we did not undertake responsible disclosure.
