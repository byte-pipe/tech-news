---
title: AI Takes Control of Robotic Arm in 16 Minutes Flat
url: https://www.darkreading.com/ics-ot-security/ai-takes-control-robotic-arm-16-minutes
site_name: tldr
content_file: tldr-ai-takes-control-of-robotic-arm-in-16-minutes-flat
fetched_at: '2026-10-17T13:52:55.756637'
original_url: https://www.darkreading.com/ics-ot-security/ai-takes-control-robotic-arm-16-minutes
date: '2026-10-17'
description: Most OT devices at utilities, factories, and elsewhere have been deployed for a decade+, but operators need to get agile and deploy new cyber defenses.
tags:
- tldr
---

* ICS/OT Security
* Cybersecurity Operations
* Cyber Risk
* Vulnerabilities & Threats
* News

# AI Takes Control of Robotic Arm in 16 Minutes Flat

Most OT devices at utilities, factories, and elsewhere have been deployed for a decade or more, but operators need to get agile and deploy new cyber defenses.

Robert Lemos
,
Contributing Writer

October 16, 2026

5 Min Read
Source: greenbutterfly via Shutterstock

Frontier AI models targeting operational technology (OT) environments, from utilities to factories and beyond, could compromise the network and take control of devices in minutes, according to a fresh round of in-the-lab testing.

Conducted by Booz Allen, the government and military contractor, the tests found that in a typical OT environment, commercial AI models could identify misconfigured devices and work their way through multiple layers of networks to take physical action, the company stated in an October report. In one case, the model was able to take control of and move a robotic arm in an attack that lasted only 16 minutes.

The researchers were not surprised that the AI models succeeded, but how quickly they could find a pathway into the operational side of the network was the top-line finding, says Kyle Miller, vice president of infrastructure cybersecurity at Booz Allen.

"I've been doing OT security my whole career, and whether we like it or not, we live a little bit by security through obscurity — we believe that an attacker needs to [be sophisticated] to get into an OT environment and understand it well enough to be able to manipulate things and cause a kinetic outcome," he tells Dark Reading. "This frontier model testing shows that AI knocks down a lot of those barriers."

Related:EU Grocers Pay a Steep Price for Unpatched Fridge Firmware

While cyberattackers and nation-state operatives are quick to experiment with AI — withnear-autonomous AI attacks becoming more common— AI-assisted attacks on OT networks are relatively rare. In early 2026, a small hacking group gained access to at least nine Mexican agencies assisted by AI, yet theyfailed to gain access to the OT network of a local water and drainage utility.

The adversary combined two commercial models that had little to no OT-specific knowledge, but which quickly highlighted the system as a high-value target and researched methods of gaining access, says Jay Deen, associate principal adversary hunter at OT cybersecurity firm Dragos, which reported the incident.

"What stood out ... was not that AI introduced new or particularly sophisticated techniques, but that it significantly reduced the expertise and time needed to carry out a large-scale intrusion," he says, adding that "the AI got close enough to identify and actively develop a path toward the OT environment, but there is no evidence the adversary actually crossed into the control network."

## A Decades-Long Life Cycle, Minutes to Compromise

In Booz Allen's testing, the AI models managed to get further, and successfully achieved all of its eight test objectives, from mapping the environment to finding security vulnerabilities to compromising a SCADA system,according to the firm's report. While the effort was fast, if the model did not require human-in-the-loop approval, it likely would have taken half the time, says Booz Allen's Miller.

Related:One Packet Can Crash OT Servers in Industrial Sectors

"That 16-minute time window was the time it took for the models to get from the perimeter firewall through the IT network, into the OT network, and cause a kinetic outcome — so actually energize an output on one of the controllers in the OT environment," he says.

In the initial runs, Booz Allen left in some unpatched vulnerabilities, so the attack time did not include the time to research and develop exploits for zero-day vulnerabilities, he says.

Booz Allen constructed a mock enterprise OT network to test attacks by AI agents. Source: Booz Allen

In its own research, OT cybersecurity firm Claroty's Team82 used an AI coding agent to analyze Danfoss refrigeration controllers andfound three previously disclosed vulnerabilities. The AI agent figured out how to chain two of them together and gained root access on a lab device. The total cost: 28 minutes and about $6 in tokens, says Sean Tufts, field chief technology officer for the company.

"For defenders, that could mean less time to respond once a vulnerability becomes public, especially when equipment is exposed to the Internet," he says, adding that companies need to focus their attention on identifying where attackers can do the most damage: "If someone gains access to a vulnerable device, how far can they get? Could they change how equipment operates? What protections are in place to stop them?"

Related:You Need Cyber Deception for OT

Those same vulnerabilities led to therecent attack on refrigeration systems in France, two months after Claroty notified the manufacturer of the issues, leading to a firmware update.

## AI Poses Both an Insider Threat & a Solution

For critical-infrastructure operators who have relied on their relative obscurity as their first line of defense, AI-powered attacks will be a wake-up call, says Claroty's Tufts. In addition, 70% of companies use AI in some capacity for operations, according to Claroty's survey. While neither Claroty's study nor Booz Allen's lab testing demonstrated an attacker compromising an AI agent already deployed in an operational environment, it's a scenario organizations should be thinking about, Tufts says.

"An agent with broad permissions could give an attacker another way to reach critical systems if that agent or its underlying infrastructure were compromised," he says.

While blocking AI-augmented attacks with AI-augmented defenses seems to be a no-brainer, considering AI agents' penchant for occasionally going rogue or exceeding their intended functions, gaining trust among OT operators will take some time, says Booz Allen's Miller.

"In an OT environment, because we're very safety conscious and very uptime conscious, anytime we automate a defense, it can be scary," he says. "But I think especially looking at techniques where, if we detect an anomalous AI movement in the OT environment, can we trigger something automatically that will block that traffic in the perimeter ... that's going to be important. Otherwise, if everything moves at human speed, that is going to be probably too slow."

Segmentation — and better yet, micro-segmentation — can slow down AI attackers, giving defenders a chance to react. Monitoring networks for anomalous behavior is another defense that OT operators should have deployed. While AI agents, once they are in the OT networks, often look like other OT devices, a well-tuned monitoring system can detect them.

Finally, companies should consider deploying deceptive technologies, such as honeypots and canaries, which can both slow down AI-augmented attackers and lead to their detection, Miller says.

"Using some type of canary or lure or deception-type solution is going to be powerful," he says. "I think it's something that, if you do it well, you can set up lures or honeypots to mimic what your typical OT environment would look like and ... even feed the model false data."

Read more about:

CISO Corner

## About the Author

Robert Lemos

Contributing Writer

Rob is an award-winning, veteran technology journalist of more than 30 years, reporting on global cybersecurity issues, the latest offensive and defensive technologies, malware incidents, cyber conflict, and AI's impact on software and cybersecurity.

A former research engineer, Rob has written for more than two dozen publications, including CNET News.com, Dark Reading, MIT's Technology Review, Popular Science, and Wired News. He has received five awards for journalism, including Best Deadline Journalism (Online) in 2003 for his coverage of the Blaster worm. Rob also analyzes data on various trends using Python and R for both his reporting and his clients. Recent reports include analyses of the shortage in cybersecurity workers, annual vulnerability trends, and annual threat reports.

Rob holds degrees from Cornell University in Electrical Engineering and Computer Science (double major).

See more from 
Robert Lemos

## Want more Dark Reading stories in your Google search results?

Add Us Now
More Insights
Industry Reports
* The State of Cloud Security: The Latest Challenges
* How Organizations Are Managing Incident Response
* How Enterprises Are Developing Secure Applications
* Inside RSAC 2026: security leaders reveal the risks redefining your defense strategy
* Essential News & Insights from Black Hat USA 2025
Access More Research
Webinars
* How to Harness your Security Operations Data for Enterprise Defense
* Building Cyber Resilience: Beyond Prevention to Recovery
* The Frontier AI Threat: Closing the Mobile Gap in Your Exposure Management Strategy
* Static Analysis, Smarter Triage, Agentic Depth: A Practical AppSec Stack for AI-Driven Development
* Effective Alert Triage: Reducing Noise and Finding Real Threats
More Webinars

### Featured

Check out theBlack Hat USA 2026 Conference Guidefor coverage and intel from — and about — the show!

December 3, 2026 | VIRTUAL

## Cybersecurity Outlook 2027

Secure Your Spot
Keep up with the latest cybersecurity threats, newly discovered vulnerabilities, data breach information, and emerging trends. Delivered daily or weekly right to your email inbox.
Subscribe