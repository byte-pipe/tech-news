---
title: A Zoom Screen-Sharing Bug Let Anyone Take Over Other Devices on a Call | WIRED
url: https://www.wired.com/story/a-zoom-screen-sharing-bug-let-anyone-take-over-other-devices-on-a-call/
site_name: newsfeed
content_file: newsfeed-a-zoom-screen-sharing-bug-let-anyone-take-over-oth
fetched_at: '2026-08-11T20:02:48.741278'
original_url: https://www.wired.com/story/a-zoom-screen-sharing-bug-let-anyone-take-over-other-devices-on-a-call/
author: Lily Hay Newman
date: '2026-08-11'
published_date: '2026-08-11T12:37:12.823Z'
description: Researchers say it took fewer than 20 prompts for a public AI tool to find a flaw (now fixed) allowing anyone on a Zoom call to hijack another participants’ device.
tags:
- wired
- security
- security / cyberattacks and hacks
- security / security news
---

Save Story
Save this story
Save Story
Save this story

As AI modelsgain advancedcapabilitiesto find vulnerabilities in software, developways to exploit them, and even carry out autonomoushacking sprees, researchers offered a sobering new example on Tuesday,disclosing vulnerabilitiesin the video conferencing platform Zoom that could have been exploited to take over targets’ devices. Anyone on a call that involved screen sharing, whether participants or the host, would have been vulnerable to a silent attack that could be carried out with no indication and no interaction from the victim.

Researchers from the digital defense firm A Security say thebugwas discovered in early June using publicly available AI models, and that it took fewer than 20 prompts to uncover the vulnerabilities and create a working attack. Zoom issued a security advisory on Tuesday, including details about fixes the company has already begun rolling out to address the flaws, which affected devices running all operating systems that Zoom supports—Windows, macOS, Linux, iOS, and Android.

“What is interesting for us and what we believe is dangerous is the democratization of these capabilities—the barrier to entry is dropping rapidly,” A Security cofounder Omer Gull told WIRED ahead of the disclosure. “Before it would have taken a team of five people maybe six months with a lot of refining and iteration to find this. Now people can reach the same results with under 20 prompts. And Zoom is an important type of target because people assume trust when using it. They don’t see it as a threat.”

The vulnerabilities were specifically in the protocol used to facilitate real-time annotation during screen sharing. The researchers say that their AI bug hunting systems specifically delved into this component because, like human bug hunters, they have been trained that convoluted and obscure functions often contain overlooked vulnerabilities. This is particularly true with proprietary, closed-source software. An established company like Zoom presumably does extensive code review and vetting on all components and functions, but without the benefit of public, open review, esoteric yet complex features like annotation are more likely to contain mistakes.

Zoom did not respond to multiple requests for comment from WIRED about the A Security findings.

The bugs are now patched, with Zoom issuing both server and client-side fixes—or patches for both Zoom’s own servers and the applications that run on customer devices. But the researchers emphasize that it was alarming to contemplate bugs that could have been exploited to take over a target device simply by getting someone onto a Zoom call. Joining a call is in itself a gesture of trust, but given how ubiquitous video calling is in both personal and professional contexts—and given that Zoom in particular is also widely used for events and semipublic activities like webinars—people typically have their guard down when joining a Zoom.

“If you just get on a Zoom with us, we can take over your device,” A Security cofounder Yossi Torati told WIRED on a call. (It was, incidentally, hosted on Microsoft Teams.) “The worst-case scenario is that we can take over an enterprise just by having this vulnerability in our hands. If I’m an attacker, I can be on a call with someone from a company, take control of their computer and their credentials, and then use them to move laterally in the enterprise.”

Practitioners often call security a “cat-and-mouse game,” but as AI bug hunting proliferates, this delicate dance has become an all-out race.

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:This isnot your average politics newsletter
* WiFi-8 is coming—here’severything you need to know
* Big Story:Young runners are becomingfreakishly fast
* The new reality ofurban surveillance
* Take our survey:Do you work in tech? We want tohear from you
Lily Hay Newman
 is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... 
Read More
Senior Writer
* X
Topics
Zoom
video chat
bug
hacks
artificial intelligence
Hackers Stalked Me by Hijacking a Smartwatch for Kids
Security researchers tracked and eavesdropped on a WIRED reporter using vulnerabilities in a pink plastic smartwatch. It’s just one piece of a deeply insecure supply chain of GPS-enabled gadgets.
Andy Greenberg
OpenAI’s Browser Could Be Hijacked to Spam Your WhatsApp Contacts
Researchers at security firm Zenity found more than a dozen flaws in AI browsers—and managed to get OpenAI’s Atlas to make an unauthorized Amazon purchase.
Matt Burgess
OpenAI Models Escaped Containment and Hacked Hugging Face
The cybersecurity-focused models, including GPT-5.6 Sol, broke out of a testing sandbox, exploited a zero-day, and gained access to the open internet to pull off the attack.
Lily Hay Newman
A Sneaky Hacking Tool Targeting AI Infrastructure Is Lurking in Victims’ Blind Spots
A new type of malware can worm deep into AI coding systems to steal data and logins—and can flip a “death switch” to destroy files and keep out real users.
Lily Hay Newman
OpenAI Didn’t Notice Its AI Agents Using a Message Board to Plan Their Hacking Spree
At the Black Hat security conference, the AI giant revealed new details about how its agents went rogue, hacked several other companies—and did it all right under the company’s nose.
Lily Hay Newman
OpenAI’s Rogue AI Agent Hacked More Than Just Hugging Face
In a new disclosure, OpenAI says its agent used exposed logins to gain access to at least four “publicly available services” in its unhinged quest to solve a test.
Dell Cameron
OK, Well, Rogue AI Agents Are Hacking Again
Rogue AI agents from OpenAI and Anthropic have again been caught trying to disrupt servers and software—and leaving instructions for future bad behavior.
Paresh Dave
OpenAI’s Hacking Debacle Comes Down to Human Error
If the generative AI giant had followed well-known security best practices, it’s likely that its AI agent would never have escaped to the open internet and hacked multiple companies.
Lily Hay Newman
AI Hacks Are Bad. AI Worms and Viruses Will Be Worse
Chinese researchers have shown that AI models have the capacity to act like aggressive and adaptive computer viruses.
Will Knight
Prompt Injection Attacks Are Thwarting AI Hacking Agents
“Context bombing” tricks malicious AI agents into shutting down before they can do harm.
Dan Goodin, Ars Technica
Chrome Needs Twice-a-Week Patching Thanks to AI Bug Hunting
The two Chrome updates in June patched more bugs than the 23 updates before them. Now, Google is ramping up its patching schedule thanks to AI-assisted vulnerability discovery.
Lily Hay Newman
The OpenAI Models That Hacked Hugging Face Were ‘Active on the Internet’ for Days
Plus: Russian hackers are trying to steal US nuclear scientists’ emails, the State Department bans known scammers from entering the United States, and more.
Lily Hay Newman