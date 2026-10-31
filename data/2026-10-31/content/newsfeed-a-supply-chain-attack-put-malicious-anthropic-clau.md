---
title: A Supply Chain Attack Put Malicious Anthropic Claude Extensions on Thousands of Devices | WIRED
url: https://www.wired.com/story/trojan-malware-targets-thousands-of-anthropic-claude-developer-systems/
site_name: newsfeed
content_file: newsfeed-a-supply-chain-attack-put-malicious-anthropic-clau
fetched_at: '2026-10-31T19:03:53.136640'
original_url: https://www.wired.com/story/trojan-malware-targets-thousands-of-anthropic-claude-developer-systems/
author: Lily Hay Newman
date: '2026-10-30'
published_date: '2026-10-30T20:38:46.195Z'
description: Thanks to a lucky break, flawed code in a tainted Claude extension prevented the attacker from fully worming their way into some 5,000 developer machines.
tags:
- wired
- security
- security / cyberattacks and hacks
- malware
---

Save Story
Save this story
Save Story
Save this story

The AI software-development platform Cursor, which is owned bySpaceX, had a maliciousAnthropic Claude Codeextension for Windows, macOS, and Linux live in its integrated development environment extension marketplace for roughly 11 hours on Thursday. The company says the rogue extension was downloaded by “at most 5,000 users.” Cursor briefly shut down the extension marketplace while it investigated the situation, which the company says did not impact any other extensions.

The tainted extension was designed with a backdoor to give attackers access to victim devices—the type of implant that malicious hackers often use as a stepping stone to deeper control inside a target network. Cursorpublishedremediation steps on Thursday for the roughly 5,000 affected targets. A saving grace of the situation, though, was a flaw in the malware's design that blocked it from fully establishing itself on the vast majority of targets.

“Everyone was so lucky here, this was potentially a really dangerous foothold for an attacker,” says Calum Hall, cofounder and CEO of the detection firm Phorion, the first researchers tospotthe malicious extension after detecting it on a customer's Mac.

What is still unclear is how the malicious extension made its way into the Cursor marketplace at all. Some researchers initially speculated that it came from a compromised Anthropic system. But Cursor said in its Thursday security alert that “these malicious versions of the extension were not developed by Anthropic.”

Felix Rieseberg, a member of Anthropic's technical staff,postedon X on Friday: “We’re working with Cursor on this incident, but it wasn’t a compromise of Anthropic’s systems or employee laptops. A malicious actor used access to Cursor’s marketplace to publish a tampered copy of the Claude Code extension, which we didn’t build or publish. The versions on our official channels are not affected and this only impacts Cursor users.”

David Dworken, who works on security at Anthropic,postedon X shortly after, explaining that “this did not involve a compromise of any Anthropic systems … We were not involved with building, publishing, or hosting this.”

Cursor did not return WIRED's request for comment about how the malicious upload happened and whether it was the result of a breach at Cursor.

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:For life-tested picks, sign up for our Gear newsletters
* Airbnb hosts are furiousthey can no longer make guests do their chores
* big story:cool kids write inall lowercase—does that make you mad?
* I worked for a whole day using only the iPhone Duo
* WIRED event:The technologies, people, and ideas transforming our world
Lily Hay Newman
 is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... 
Read More
Senior Writer
* X
Topics
malware
hackers
hacking
cybersecurity
security
Anthropic
Claude
Most Servers on the Planet Are Vulnerable to This Firmware Code-Execution Flaw
The critical flaw in UEFI firmware—used by most server vendors and data centers—allows attackers to execute code early in the boot process.
Dan Goodin, Ars Technica
‘This Is Not a Drill’: Critical PHP Vulnerabilities Are Setting the Internet on Fire
The PHP Foundation has revealed two serious vulnerabilities that could impact millions of websites. Security experts warn that failure to quickly patch the flaws could have dire consequences.
Matt Burgess
A Flaw in ChatGPT’s Mac App Could Have Let Hackers Grab Sensitive Data
While the focus has been on AI agents’ hacking capabilities, a recently patched vulnerability in a ChatGPT app shows that AI software is itself an inviting—and vulnerable—target.
Lily Hay Newman
The ‘Pain in the Ass’ Math That Could Save Vibe Coding From Itself
A new startup called &Truth is joining the race to automate formal verification, a painstaking process that uses math to prove software works as intended.
Paresh Dave
A Defense Contractor Gave Their Personal AI Agent Access to a Secure Pentagon System
Sources tell WIRED that an Accenture employee’s personal Claude agent ran on a DOD network for two months before it was identified and the vulnerability could be patched.
Vittoria Elliott
Hackers Exploited the PHP Vulnerabilities Days Before They Were Patched
Amazon Web Services logged attempts to leverage the internet-melting PHP2Shell bugs four days ago. They’re now being “broadly exploited” across the internet.
Lily Hay Newman
AI Hacks Leave a Mess That AI Companies Aren’t Paying For
Powerful AI models continue to cause chaos, but their targets aren’t widely seeking justice. Instead, they’re being encouraged to adopt those same tools.
Paresh Dave
A Hacker Targeted High-Stakes Poker Players With Malware That Exposed Their Cards
Illicit software on the computers of some of the world’s best online poker players allowed the accused cheater to see what cards were in the victims’ hands—and trounce them at the tables.
Ben Dowsett
AI Guardrails Aren’t Stopping Criminal Hackers
Hackers around the world are all-in on using agentic AI to wage attacks—and manipulating tools like Anthropic’s Claude to help them carry out their crimes.
Lily Hay Newman
WhatsApp Help Pages Leaked Hidden Instructions for a Meta Chatbot
Around 80 pages on WhatsApp’s website exposed instructions that were designed for its chatbot, including “WHAT NOT TO SAY.” Meta says a bug caused the issue.
Matt Burgess
The PHP Meltdown Shows How AI Makes Bugs More Exploitable
Security researchers used AI tools to help uncover years-old vulnerabilities in the PHP web scripting language. Then the AI-assisted attacks began.
Lily Hay Newman
A Design Flaw in Share Links Exposes Users’ Personal Conversations With Meta’s Muse
The company is suspending the feature after security researchers discovered how easy it was to access sensitive information shared with the AI assistant.
Dan Goodin, Ars Technica