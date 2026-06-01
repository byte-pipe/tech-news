---
title: ChatGPT for Google Sheets Exfiltrates Workbooks
url: https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration
site_name: hnrss
content_file: hnrss-chatgpt-for-google-sheets-exfiltrates-workbooks
fetched_at: '2026-06-01T12:55:44.646490'
original_url: https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration
date: '2026-05-31'
description: ChatGPT for Google Sheets is vulnerable to data exfiltration and phishing overlay attacks that affect workbooks across the victim’s account after an indirect prompt injection in a single sheet.
tags:
- hackernews
- hnrss
---

Threat Intelligence

Table of Content

# ChatGPT for Google Sheets Exfiltrates Workbooks

ChatGPT for Google Sheets is vulnerable to data exfiltration and phishing overlay attacks that affect workbooks across the victim’s account after an indirect prompt injection in a single sheet.

This attack does not require human-in-the-loop approvals, even when in settings the user has explicitly required human approval before ChatGPT edits workbooks.UPDATE from OpenAI:

"We appreciate the security research here, and it’s unfortunate this one slipped through a crack in our disclosure pipeline. As we’re now aware of this report, we’ve taken immediate steps to protect users against potential attacks in this area by removing the model’s ability to generate Apps Script code, which should eliminate the risk to users of ChatGPT for Google Sheets. We’re taking a close look at how this feature interacts with Google Sheets APIs and re-evaluating our sandboxing approach to make sure this product is as resistant as possible against prompt injection attacks. More broadly, we’ll be doing a re-review of similar functionality in other surfaces to make sure that our defenses are consistent and effective across the board."

### Overview

Recently, OpenAI launched an AI extension for using ChatGPT in Google Sheets, which has accumulated over 185,000 downloads since its launch less than a month ago. This allows users to operate on their spreadsheets by interacting with an AI chatbot that lives in a sidebar, with the added benefit of drawing on data from ChatGPT connectors.

A single indirect prompt injection attack triggered by a single benign user query can trigger all of the following effects at once:

* Exfiltration of many workbooks from across the victim’s account
* Display of an interactive phishing pop-up
* Overwriting the entire GPT sidebar with an attacker-controlled chatbot interface
* Attacker-controlled edits to your workbooks

This attack occurs when any untrusted data source (e.g., from an imported sheet or ChatGPT connector) manipulates ChatGPT to run an attacker-controlled external script, which executes leveraging permissions the user has granted to the ChatGPT for Google Sheets extension.

This vulnerability was responsibly disclosed to OpenAI. Despite multiple follow-ups, we received no communication beyond an automated reply to our initial disclosure.OpenAI's documentationfails to describe sensitive capabilities granted to the model (e.g., running privileged scripts) or risks of model manipulation via indirect prompt injection, instead focusing solely on functional limitations and data-handling concerns. As such, we are publishing our findings to enable informed decision-making regarding the risk surface.

### The Attack Chain

1. #### A user is working on an internal financial model
2. #### The user imports an external data set to use in their model
3. #### The external sheet has a prompt injection hidden in white text.
4. #### The user asks ChatGPT for Google Sheets to help integrate the data from the imported sheet into their financial model.
5. #### The injection manipulates ChatGPT for Google Sheets to run an external scriptNote: ChatGPT for Google Sheets has a setting called ‘Apply edits automatically’ that determines when human approvals are required before an agentic action completes. However, this attack succeeds even when the user has explicitly disabled automatic edits.
6. #### The external script exfiltrates the financial model from the user’s workbookBelow, the attacker's server logs show the user’s exfiltrated financial model.
7. #### The external script identifies links to other workbooks in the stolen data, exfiltrates the discovered workbooks, and continues across all workbooks it can findHere, the internal financial model sheet included a link to another spreadsheet relevant to budgeting. The malicious script identifies the spreadsheet URL in the stolen data and exfiltrates the newly discovered workbook. It then continues to process the stolen data, identifying and exfiltrating additional workbooks, eventually exfiltrating 12 in total.Note: Clicking the ‘stop’ button in the ChatGPT sidebar does not stop scripts that have started from finishing execution.

### Phishing Overlay Attacks

In addition to the data exfiltration described above, the same attacker-controlled scripts enable a malicious actor to target two variants of a phishing overlay attack.

Variant 1:A sidebar is opened that overlays the ChatGPT for Google Sheets extension with an attacker-controlled site, allowing the attacker to impersonate the extension. The malicious sidebar can execute scripts that edit the sheet in the same way ChatGPT can, allowing it to act in most of the ways the extension normally does, while also performing malicious activities such as:

* Harvesting all user prompts
* Providing the user with a misaligned chatbot to interact with
* Convincing the user to ‘reconnect’ connectors to gain access to additional apps
* Displaying a phishing UI to steal credentials for OpenAI

Variant 2:A pop-up modal is opened that renders an attacker-controlled website to phish the user for credentials.

### Control Access to ChatGPT for Google Sheets

Organizations can leverage the following configuration to control access to ChatGPT for Google Sheets:

Workspace settings > Permissions & roles > ChatGPT for Excel and Google Sheets

### Responsible Disclosure

UPDATE: OpenAI has responded; details are at the top of the article.

This vulnerability was responsibly disclosed to OpenAI. Despite multiple follow-ups, we received no communication beyond an automated reply to our initial disclosure.OpenAI's documentationfails to describe sensitive capabilities granted to the model (e.g., running privileged scripts) or risks of model manipulation via indirect prompt injection, instead focusing solely on functional limitations and data-handling concerns. As such, we are publishing our findings to enable informed decision-making regarding the risk surface.

#### Timeline

May 08, 2026 PromptArmor discloses to OpenAI via emailMay 08, 2026 OpenAI sends an automated reply, confirming the intended reporting channelMay 08, 2026 PromptArmor confirms email preferenceMay 12, 2026 PromptArmor follows upMay 18, 2026 PromptArmor follows upMay 27, 2026 Public disclosureUPDATE:May 31, 2026 OpenAI responds; more details at the top.