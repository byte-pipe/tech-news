---
title: 8 Million Users' AI Conversations Sold for Profit by "Privacy" Extensions | Koi Blog
url: https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection
site_name: hackernews_api
fetched_at: '2025-12-16T11:07:56.133654'
original_url: https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection
author: takira
date: '2025-12-16'
tags:
- hackernews
- trending
---

Back

Koi Research

### 8 Million Users' AI Conversations Sold for Profit by "Privacy" Extensions

Idan Dardikman

,

,

December 15, 2025

A few weeks ago, I was wrestling with a major life decision. Like I've grown used to doing, I opened Claude and started thinking out loud-laying out the options, weighing the tradeoffs, asking for perspective.

Midway through the conversation, I paused. I realized how much I'd shared: not just this decision, but months of conversations-personal dilemmas, health questions, financial details, work frustrations, things I hadn't told anyone else. I'd developed a level of candor with my AI assistant that I don't have with most people in my life.

And then an uncomfortable thought:what if someone was reading all of this?

The thought didn't let go. As a security researcher, I have the tools to answer that question.

## The Discovery

We asked Wings, our agentic-AI risk engine, to scan for browser extensions with the capability to read and exfiltrate conversations from AI chat platforms. We expected to find a handful of obscure extensions-low install counts, sketchy publishers, the usual suspects.

The results came back with something else entirely.

Near the top of the list: Urban VPN Proxy. A Chrome extension with over 6 million users. A 4.7-star rating from 58,000 reviews. A "Featured" badge from Google, meaning it had passed manual review and met what Google describes as "a high standard of user experience and design."

A free VPN promising privacy and security. Exactly the kind of tool someone installs when theywantto protect themselves online.

We decided to look closer.

Featured by Google and trusted by

## What We Found

Urban VPN Proxy targets conversations across ten AI platforms:

* ChatGPT
* Claude
* Gemini
* Microsoft Copilot
* Perplexity
* DeepSeek
* Grok (xAI)
* Meta AI

For each platform, the extension includes a dedicated "executor" script designed to intercept and capture conversations. The harvesting is enabled by default through hardcoded flags in the extension's configuration:

There is no user-facing toggle to disable this. The only way to stop the data collection is to uninstall the extension entirely.

## How It Works

The data collection operates independently of the VPN functionality. Whether the VPN is connected or not, the harvesting runs continuously in the background.

Here's the technical breakdown:

1. Script injection into AI platforms

The extension monitors your browser tabs. When you visit any of the targeted AI platforms (ChatGPT, Claude, Gemini, etc.), it injects an "executor" script directly into the page. Each platform has its own dedicated script - chatgpt.js, claude.js, gemini.js, and so on.

2. Overriding native browser functions

Once injected, the script overrides fetch() and XMLHttpRequest - the fundamental browser APIs that handle all network requests. This is an aggressive technique. The script wraps the original functions so that every network request and response on that page passes through the extension's code first.

This means when Claude sends you a response, or when you submit a prompt to ChatGPT, the extension sees the raw API traffic before your browser even renders it.

3. Parsing and packaging

The injected script parses the intercepted API responses to extract conversation data - your prompts, the AI's responses, timestamps, conversation IDs. This data is packaged and sent via window.postMessage to the extension's content script, tagged with the identifier PANELOS_MESSAGE.

4. Exfiltration via background worker

The content script forwards the data to the extension's background service worker, which handles the actual exfiltration. The data is compressed and transmitted to Urban VPN's servers at endpoints including analytics.urban-vpn.com and stats.urban-vpn.com.

What gets captured:

* Every prompt you send to the AI
* Every response you receive
* Conversation identifiers and timestamps
* Session metadata
* The specific AI platform and model used

## The Timeline

The AI conversation harvesting wasn't always there. Based on our analysis:

* Before version 5.5.0: No AI harvesting functionality
* July 9, 2025: Version 5.5.0 released with AI harvesting enabled by default
* July 2025 - Present: All user conversations with targeted AI platforms captured and exfiltrated

Chrome and Edge extensions auto-update by default. Users who installed Urban VPN for its stated purpose - VPN functionality - woke up one day with new code silently harvesting their AI conversations.

Koidex report for Urban VPN Proxy

Anyone who used ChatGPT, Claude, Gemini, or the other targeted platforms while Urban VPN was installed after July 9, 2025 should assume those conversations are now on Urban VPN's servers and have been shared with third parties. Medical questions, financial details, proprietary code, personal dilemmas - all of it, sold for "marketing analytics purposes."

## What "AI Protection" Actually Does

Urban VPN's Chrome Web Store listing promotes "AI protection" as a feature:

"Advanced VPN Protection - Our VPN provides added security features to help shield your browsing experience from phishing attempts, malware, intrusive ads and AI protection which checks prompts for personal data (like an email or phone number), checks AI chat responses for suspicious or unsafe links and displays a warning before click or submit your prompt."

The framing suggests the AI monitoring exists toprotectyou-checking for sensitive data you might accidentally share, warning you about suspicious links in responses.

The code tells a different story. The data collection and the "protection" notifications operate independently. Enabling or disabling the warning feature has no effect on whether your conversations are captured and exfiltrated. The extension harvests everything regardless.

"And that, Doctor, is why I have trust issues"

The protection feature shows occasional warnings about sharing sensitive data with AI companies. The harvesting feature sends that exact sensitive data - and everything else - to Urban VPN's own servers, where it's sold to advertisers. The extension warns you about sharing your email with ChatGPT while simultaneously exfiltrating your entire conversation to a data broker.

## It Gets Worse

After documenting Urban VPN Proxy's behavior, we checked whether the same code existed elsewhere.

It did. The identical AI harvesting functionality appears in seven other extensions from the same publisher, across both Chrome and Edge:

Chrome Web Store:

* Urban VPN Proxy - 6,000,000 users
* 1ClickVPN Proxy - 600,000 users
* Urban Browser Guard - 40,000 users
* Urban Ad Blocker - 10,000 users

Microsoft Edge Add-ons:

* Urban VPN Proxy - 1,323,622 users
* 1ClickVPN Proxy - 36,459 users
* Urban Browser Guard - 12,624 users
* Urban Ad Blocker - 6,476 users

Total affected users: Over 8 million.

The extensions span different product categories, a VPN, an ad blocker, a "browser guard" security tool, but share the same surveillance backend. Users installing an ad blocker have no reason to expect their Claude conversations are being harvested.

All of these extensions carry "Featured" badges from their respective stores, except Urban Ad Blocker for Edge. These badges signal to users that the extensions have been reviewed and meet platform quality standards. For many users, a Featured badge is the difference between installing an extension and passing it by - it's an implicit endorsement from Google and Microsoft.

## Who's Behind This

Urban VPN is operated by Urban Cyber Security Inc., which is affiliated with BiScience (B.I Science (2009) Ltd.), a data broker company.

This company has been on researchers' radar before. Security researchersWladimir Palantand John Tuckner atSecure Annexhave previously documented BiScience's data collection practices. Their research established that:

* BiScience collects clickstream data (browsing history) from millions of users
* Data is tied to persistent device identifiers, enabling re-identification
* The company provides an SDK to third-party extension developers to collect and sell user data
* BiScience sells this data through products like AdClarity and Clickstream OS

Our finding represents an expansion of this operation. BiScience has moved from collecting browsing history to harvesting complete AI conversations-a significantly more sensitive category of data.

The privacy policy confirms the data flow:

"We share the Web Browsing Data with our affiliated company... BiScience that uses this raw data and creates insights which are commercially used and shared with Business Partners"

## The Disclosure Problem

To be fair, Urban VPN does disclose some of this-if you know where to look.

The consent prompt(shown during extension setup) mentions that the extension processes "ChatAI communication" along with "pages you visit" and "security signals." It states this is done "to provide these protections."

[Screenshot: Urban VPN consent prompt]

The privacy policygoes further, buried deep in the document:

"AI Inputs and Outputs. As part of the Browsing Data, we will collect the prompts and outputs queried by the End-User or generated by the AI chat provider, as applicable."

And:

"We also disclose the AI prompts for marketing analytics purposes."

However, the Chrome Web Store listing-the place where users actually decide whether to install-shows a different picture:

"This developer declares that your data is Not being sold to third parties, outside of the approved use cases"

The listing mentions the extension handles "Web history" and "Website content." It says nothing about AI conversations specifically.

The contradictions are significant:

1. The consent prompt frames AI monitoring as protective. The privacy policy reveals the data is sold for marketing.
2. The store listing says data isn't sold to third parties. The privacy policy describes sharing with BiScience, "Business Partners," and use for "marketing analytics."
3. Users who installed before July 2025 never saw the updated consent prompt-the AI harvesting was added via silent update in version 5.5.0.
4. Even users who see the consent prompt have no granular control. You can't accept the VPN but decline the AI harvesting. It's all or nothing.
5. Nothing indicates to users that the data collection continues even when the VPN is disconnected and the AI protection feature is turned off. The harvesting runs silently in the background regardless of what features the user has enabled.

## Google's Role

Urban VPN Proxy carries Google's "Featured" badge on the Chrome Web Store. According to Google's documentation:

"Featured extensions follow our technical best practices and meet a high standard of user experience and design."

"Before it receives a Featured badge, the Chrome Web Store team must review each extension."

This means a human at Google reviewed Urban VPN Proxy and concluded it met their standards. Either the review didn't examine the code that harvests conversations from Google's own AI product (Gemini), or it did and didn't consider this a problem.

The Chrome Web Store's Limited Use policy explicitly prohibits "transferring or selling user data to third parties like advertising platforms, data brokers, or other information resellers." BiScience is, by its own description, a data broker.

The extension remains live and featured as of this writing.

## Final Thoughts

Browser extensions occupy a unique position of trust. They run in the background, have broad access to your browsing activity, and auto-update without asking. When an extension promises privacy and security, users have little reason to suspect it's doing the opposite.

What makes this case notable isn't just the scale - 8 million users - or the sensitivity of the data - complete AI conversations. It's that these extensions passed review, earned Featured badges, and remained live for months while harvesting some of the most personal data users generate online. The marketplaces designed to protect users instead gave these extensions their stamp of approval.

If you have any of these extensions installed, uninstall them now. Assume any AI conversations you've had since July 2025 have been captured and shared with third parties.

This writeup was authored by the research team at Koi.

We built Koi to detect exactly these kinds of threats - extensions that slip past marketplace reviews and quietly exfiltrate sensitive data. Our risk engine, Wings, continuously monitors browser extensions to catch threats before they reach your team.

Book a demoto see how behavioral analysis catches what static review misses.

Stay safe out there.

## IOCs

Chrome:

* Urban VPN Proxy: eppiocemhmnlbhjplcgkofciiegomcon
* Urban Browser Guard: almalgbpmcfpdaopimbdchdliminoign
* Urban Ad Blocker: feflcgofneboehfdeebcfglbodaceghj
* 1ClickVPN Proxy for Chrome: pphgdbgldlmicfdkhondlafkiomnelnk

Edge:

* Urban VPN Proxy: nimlmejbmnecnaghgmbahmbaddhjbecg
* Urban Browser Guard: jckkfbfmofganecnnpfndfjifnimpcel
* Urban Ad Blocker: gcogpdjkkamgkakkjgeefgpcheonclca
* 1ClickVPN Proxy for Edge: deopfbighgnpgfmhjeccdifdmhcjckoe

‍

share

Copied to clipboard

### Be the first to know

Fresh research and updates on software risk and endpoint security.

Thanks for subscribing!

## related blogs

Koi Research

### Inside GhostPoster: How a PNG Icon Infected 50,000 Firefox Users

Lotan Sery

,

Noga Gouldman

,

December 16, 2025

Koi Research

### Brew Hijack: Serving Malware Over Homebrew’s Core Tap

Yuval Ronen

,

,

December 15, 2025

Koi Research

### GlassWorm Goes Native: Same Infrastructure, Hardened Delivery

Lotan Sery

,

,

December 10, 2025
