---
title: Microsoft says bug causes Copilot to summarize confidential emails
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/
site_name: hackernews_api
content_file: hackernews_api-microsoft-says-bug-causes-copilot-to-summarize-con
fetched_at: '2026-02-19T06:00:17.444580'
original_url: https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/
author: tablets
date: '2026-02-18'
description: Microsoft says a Microsoft 365 Copilot bug has been causing the AI assistant to summarize confidential emails since late January, bypassing data loss prevention (DLP) policies that organizations rely on to protect sensitive information.
tags:
- hackernews
- trending
---

# Microsoft says bug causes Copilot to summarize confidential emails

 By

###### Sergiu Gatlan

* February 18, 2026
* 07:03 AM
* 4

Microsoft says a Microsoft 365 Copilot bug has been causing the AI assistant to summarize confidential emails since late January, bypassing data loss prevention (DLP) policies that organizations rely on to protect sensitive information.

According to a service alert seen by BleepingComputer, this bug (tracked underCW1226324and first detected on January 21) affects the Copilot "work tab" chat feature, which incorrectly reads and summarizes emails stored in users' Sent Items and Drafts folders, including messages that carry confidentiality labels explicitly designed to restrict access by automated tools.

Copilot Chat (short for Microsoft 365 Copilot Chat) is the company's AI-powered, content-aware chat that lets users interact with AI agents. ​Microsoftbegan rolling out Copilot Chatto Word, Excel, PowerPoint, Outlook, and OneNote for paying Microsoft 365 business customers in September 2025.

"Users' email messages with a confidential label applied are being incorrectly processed by Microsoft 365 Copilot chat," Microsoft said when it confirmed this issue.

"The Microsoft 365 Copilot 'work tab' Chat is summarizing email messages even though these email messages have a sensitivity label applied and a DLP policy is configured."

Microsoft has since confirmed that an unspecified code error is responsible and said it began rolling out a fix in early February. As of Wednesday, the company said it was continuing to monitor the deployment and is reaching out to a subset of affected users to verify that the fix is working.

"A code issue is allowing items in the sent items and draft folders to be picked up by Copilot even though confidential labels are set in place," Microsoft added.

Microsoft has not provided a final timeline for full remediation and has not disclosed how many users or organizations were affected, saying only that the scope of impact may change as the investigation continues.

However, this ongoing incident has been tagged as an advisory, a flag commonly used to describe service issues typically involving limited scope or impact.

## The future of IT infrastructure is here

Modern IT infrastructure moves faster than manual workflows can handle.

In this new Tines guide, learn how your team can reduce hidden manual delays, improve reliability through automated response, and build and scale intelligent workflows on top of tools you already use.

Get the guide

### Related Articles:

Microsoft fixes Outlook bug blocking access to encrypted emails

Microsoft: Windows update blocks access to Cloud PC sessions

Microsoft fixes bug that blocked Google Chrome from launching

Microsoft 365 outage takes down admin center in North America

Microsoft announces new mobile-style Windows security controls
