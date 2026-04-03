---
title: Claude Cowork Exfiltrates Files
url: https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files
site_name: hackernews_api
fetched_at: '2026-01-15T11:07:21.637207'
original_url: https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files
author: takira
date: '2026-01-14'
description: Claude Cowork is vulnerable to file exfiltration attacks via indirect prompt injection as a result of known-but-unresolved isolation flaws in Claude's code execution environment.
tags:
- hackernews
- trending
---

Threat Intelligence

Table of Content

Table of Content

Table of Content

# Claude Cowork Exfiltrates Files

Claude Cowork is vulnerable to file exfiltration attacks via indirect prompt injection as a result of known-but-unresolved isolation flaws in Claude's code execution environment.

### Context

Two days ago, Anthropic released the Claude Cowork research preview (a general-purpose AI agent to help anyone with their day-to-day work). In this article, we demonstrate how attackers can exfiltrate user files from Cowork by exploiting an unremediated vulnerability in Claude’s coding environment, which now extends to Cowork. The vulnerability was first identified in Claude.ai chat before Cowork existed by Johann Rehberger, whodisclosedthe vulnerability — it wasacknowledged but not remediatedby Anthropic.Anthropic warns users, “Cowork is a research preview with unique risks due to its agentic nature and internet access.” Users are recommended to be aware of “suspicious actions that may indicate prompt injection”. However, as this feature is intended for use by the general populace, not just technical users, we agree with Simon Willison’stake:

“I do not think it is fair to tell regular non-programmer users to watch out for 'suspicious actions that may indicate prompt injection’!”

As Anthropic has acknowledged this risk and put it on users to “avoid granting access to local files with sensitive information” (while simultaneouslyencouragingthe use of Cowork to organize your Desktop), we have chosen to publicly disclose this demonstration of a threat users should be aware of. By raising awareness, we hope to enable users to better identify the types of ‘suspicious actions’ mentioned in Anthropic’s warning.

### The Attack Chain

This attack leverages the allowlisting of the Anthropic API to achieve data egress from Claude's VM environment (which restricts most network access).

1. The victim connects Cowork to a local folder containing confidential real estate files
2. The victim uploads a file to Claude that contains a hidden prompt injectionFor general use cases, this is quite common; a user finds a file online that they upload to Claude code. This attack is not dependent on the injection source - other injection sources include, but are not limited to: web data from Claude for Chrome, connected MCP servers, etc. In this case, the attack has the file being a Claude ‘Skill’ (although, as mentioned, it could also just be a regular document), as it is a generalizable file convention that users are likely to encounter, especially when using Claude.Note: If you are familiar with Skills, they are canonically Markdown files (which users often do not heavily scrutinize). However, we demonstrate something more interesting: here, the user uploads a .docx (such as may be shared on an online forum), which poses as a Skill - the contents appear to be Markdown that was just saved after editing in Word. In reality, this trick allows attackers to conceal the injection using 1-point font, white-on-white text, and with line spacing set to 0.1 – making it effectively impossible to detect.
3. The victim asks Cowork to analyze their files using the Real Estate ‘skill’ they uploaded
4. The injection manipulates Cowork to upload files to the attacker’s Anthropic accountThe injection tells Claude to use a ‘curl’ command to make a request to the Anthropic file upload API with the largest available file. The injection then provides the attacker’s API key, so the file will be uploaded to the attacker’s account.At no point in this process is human approval required.If we expand the 'Running command' block, we can see the malicious request in detail:Code executed by Claude is run in a VM - restricting outbound network requests to almost all domains - but the Anthropic API flies under the radar as trusted, allowing this attack to complete successfully.
5. The attacker’s account contains the victim's file, allowing them to chat with itThe exfiltrated file contains financial figures and PII, including partial SSNs.

### A Note on Model-specific Resilience

The above exploit was demonstrated against Claude Haiku. Although Claude Opus 4.5 is known to be more resilient against injections, Opus 4.5 in Cowork was successfully manipulated via indirect prompt injection to leverage the same file upload vulnerability to exfiltrate data in a test that considered a 'user' uploading a malicious integration guide while developing a new AI tool:

As the focus of this article was more for everyday users (and not developers), we opted to demonstrate the above attack chain instead of this one.

### DOS via Malformed Files

An interesting finding: Claude's API struggles when a file does not match the type it claims to be. When operating on a malformed PDF (ends .pdf, but it is really a text file with a few sentences in it), after trying to read it once, Claude starts throwing an API error in every subsequent chat in the conversation.

We posit that it is likely possible to exploit this failure via indirect prompt injection to cause a limited denial of service attack (e.g., an injection can elicit Claude to create a malformed file, and then read it). Uploading the malformed file via the files API resulted in notifications with an error message, both in the Claude client and the Anthropic Console.

### Agentic Blast Radius

One of the key capabilities that Cowork was created for is the ability to interact with one's entire day-to-day work environment. This includes the browser and MCP servers, granting capabilities like sending texts, controlling one's Mac with AppleScripts, etc.These functionalities make it increasingly likely that the model will process both sensitive and untrusted data sources (which the user does not review manually for injections), making prompt injection an ever-growing attack surface. We urge users to exercise caution when configuring Connectors. Though this article demonstrated an exploit without leveraging Connectors, we believe they represent a major risk surface likely to impact everyday users.
