---
title: A Flaw in ChatGPT’s Mac App Could Have Let Hackers Grab Sensitive Data | WIRED
url: https://www.wired.com/story/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensitive-data/
site_name: newsfeed
content_file: newsfeed-a-flaw-in-chatgpts-mac-app-could-have-let-hackers
fetched_at: '2026-10-02T16:31:23.832795'
original_url: https://www.wired.com/story/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensitive-data/
author: Lily Hay Newman
date: '2026-10-02'
published_date: '2026-10-02T09:45:00.000Z'
description: While the focus has been on AI agents’ hacking capabilities, a recently patched vulnerability in a ChatGPT app shows that AI software is itself an inviting—and vulnerable—target.
tags:
- wired
- security
- security / cyberattacks and hacks
- openai
---

Save Story
Save this story
Save Story
Save this story

Hardly a daygoes by lately without news of AI agents autonomouslyhackingwebsitesor AI tools being used by cybercriminals andscammers. But a recently patched vulnerability in the macOS version of OpenAI’s ChatGPT underscores the potential value to attackers of compromising AI software itself as these apps proliferate more and more.

The bug could have been exploited to essentially take over ChatGPT on a victim’s computer, giving an attacker access to all the chat logs and other data stored by the app, as well as interconnections like browser sessions. Discovered by researchers at the Objective-See Foundation, the vulnerability illustrates the deep system access and trust that AI platforms are afforded in order to work—and the target that this puts on their backs.

“Agents need a lot of access to do their job,” says Objective-See Foundation software analyst and longtime macOS researcher Patrick Wardle. “They are like the building manager who has access to the keys to all the rooms. So if they can be corrupted or subverted, that’s super problematic. It can mean that unprivileged code could then potentially have access to all the things.”

OpenAI publiclyacknowledgedthe security flaw and fix in its system change log on September 25. “We continue to evolve our security practices, but recognize a need to move faster,” OpenAI spokesperson Shane Bauer told WIRED in a statement.

The ChatGPT macOS app includes multiple components that communicate with each other securely by checking for digital signatures. The idea is to confirm with these validity checks that both processes are OpenAI components and not outside, potentially malicious software making a request. And the system design goes so far as to require these signature checks at three layers of remove from the request, to ensure that malicious software isn’t somehow directing an OpenAI component to be a proxy and make a seemingly trusted request.

Objective-See Foundation researchers found, though, that there is a trusted component, a script interpreter, that would accept an untrusted script (or list of commands to run) and could then be manipulated to deliver this script into the main ChatGPT process. “They also check the parent and grandparent of that process, but the malicious script just spawns the script interpreter three times and then makes the request so it will satisfy the requirements,” Wardle says.

The vulnerability was “insanely trivial” to exploit, he adds, and his proof of concept only required about a dozen lines of code. In addition to accessing ChatGPT chat logs, the vulnerability could also be used to get ChatGPT to run commands for the attacker, such as accessing a browser or other sensitive applications, with the requests appearing as legitimate instructions issued by the OpenAI software.

Wardle will present analysis of a number of AI macOS application bugs at Objective by the Sea, an Apple-focused security conference in November.

He recentlyfound a flaw, now patched, in the dictation feature of Meta’s new Muse AI assistant that could have been exploited by a local attacker to grab a mishandled authentication token and gain access to user data. And he says that he has already submitted a new vulnerability finding to OpenAI related to the integration between ChatGPT and the company’snew always-on DotsAI assistant. OpenAI is currently reviewing his report.

“AI companies are fixated on adding features right now,” Wardle says. “But as always, the more features, the broader the attack surface. So all of these companies need to be fully focused on security, and from what I can see, it still often seems like an afterthought.”

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* Introducing the app:More ways tomake the most of WIRED
* Meta failed to catch hundreds ofAI child abuse ads
* Big Story:The search forSilicon Valley’s most powerful woman
* Hackers gotinside a Flock camera—its data shows how the system really works
* In your inbox:Go inside the world of digital security withKernel Panic
Lily Hay Newman
 is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... 
Read More
Senior Writer
* X
Matt Burgess
 is a senior writer at WIRED focused on information security, privacy, and data regulation in Europe. He graduated from the University of Sheffield with a degree in journalism and now lives in London. Send tips to 
[email protected]
. ... 
Read More
Senior writer
* X
Topics
OpenAI
security
hacks
artificial intelligence
ChatGPT
Apps
macos
Meta’s Muse AI Assistant Rolled Out With a Serious Security Flaw
Meta says it issued a fix for the Muse zero-day vulnerability that would have let attackers do “whatever” they wanted on a victim’s Mac, highlighting the inherent dangers of AI helpers.
Dan Goodin, Ars Technica
An OpenAI Agent Tried to Jailbreak Itself
The company also disclosed previously unreported incidents in which its AI models behaved in misaligned ways, including uploading files to the internet without being asked.
Maxwell Zeff
How to Use AI With Your Privacy Intact
Your conversations with AI chatbots are both highly personal and deeply vulnerable to surveillance. Here’s how you can protect yourself.
Andy Greenberg
Muse, Meta’s New Personal AI Agent, Needs You to Trust It
Designed to compete with OpenClaw and Instinct, the company says Muse can do everything from sell your car to book you a plane ticket.
Lily Hay Newman
A New Tool Found Malware That’s Guided by an AI Hive Mind—No Humans in Sight
Cisco Talos researchers created a new framework for identifying malware and hacking tools that rely on AI chatbots—and quickly discovered something unusual.
Lily Hay Newman
I Let an AI Agent Hack All My Gadgets—and I’d Do It Again
After I removed the safety guardrails from a powerful open-source model, it found vulnerabilities in my household devices and hacked into a PC. But it also told me how to make everything a lot more secure.
Will Knight
Nvidia’s Answer to Rogue Agents Is an Open-Source AI Security System
In the wake of a series of high-profile AI safety incidents, Nvidia is introducing a new software tool that helps keep agents from escaping containment.
Lauren Goode
Forget the AI Slowdown—the Vulnerability Explosion Is Already Happening
AI labs are toying with an industry-wide pact to slow development. Meanwhile, widely available AI chatbots are already helping uncover a tidal wave of security flaws.
Matt Burgess
An Undercover Google Analyst Infiltrated a Notorious Supply-Chain Hacking Gang
TeamPCP pulled off the worst-ever software supply-chain hacking spree and breached thousands of companies. Now Google’s threat intelligence group says it had a mole inside the hackers’ inner circle.
Andy Greenberg
Face Recognition Is Becoming the Norm for Dating Apps
To keep scammers at bay, dating apps are embracing biometric scanning tools and “verified human” badges. These moves are sparking concerns about surveillance and privacy.
Jason Parham
Here’s How an AI Slowdown Could Actually Be Enforced
Even if big AI companies agree to a pause, ensuring that nobody tries to sneak ahead could prove tricky.
Will Knight
Apple Doesn’t Want You to Worry About the New Apple Watch’s Listening Features
The new Apple Watch includes several “intelligent” listening features that have privacy and security baked in. But the protections can’t change the facts of what the tools do.
Lily Hay Newman