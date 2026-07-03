---
title: AI and Security - if enterprises rush in where developers fear to tread, what’s the answer?
url: https://diginomica.com/ai-and-security-if-enterprises-rush-where-developers-fear-tread-whats-answer
site_name: tldr
content_file: tldr-ai-and-security-if-enterprises-rush-in-where-devel
fetched_at: '2026-07-03T19:33:11.354345'
original_url: https://diginomica.com/ai-and-security-if-enterprises-rush-where-developers-fear-tread-whats-answer
date: '2026-07-03'
published_date: 2026-07-02T00:05:02-0700
description: Cybersecurity surveys tend to focus on the user and the enterprise. But how secure are the processes of our software providers? Not great, according to one...
tags:
- tldr
---

Main content
 

 

Recent reports suggest that as organizations hand functions to agentic systems, they are losing control and oversight – despite demanding both. As previously reported, that was the finding of the recent Economist Enterprise survey, which found that 98% of adopters have suffered significant incidents related to that loss of human agency.

As its white paperPower Without Control – Re-thinking Cybersecurity for the Age of Agentic AIexplained:

AI agents are breaking things and organizations know it. [But] they are deploying more anyway. […] 90% say they are deploying agents faster than their security teams can evaluate or govern them […] because competitive pressure to adopt agents outpaces the infrastructure to control them.

However, a new report from security unicorn Aikido suggests that a similar problem exists among software developers: the faster the industry moves, the more code is shipped with known or untested vulnerabilities, because of the same commercial pressures and FOMO. Penetration testing (pentesting) is vital, therefore, but how can it be done in such a chaotic and pressured environment?

The Ghent, Belgium and San Francisco headquartered vendor has published its own 47-page white paper,The State of AI in Pentesting 2026. It documents the same world as Economist Enterprise, but from the developers’ perspective, noting thatsecurity-testing new releases was “designed for a slower world”. But, as ever, slowing down does not seem to be an option, though commonsense suggests otherwise.

Sapio Research surveyed 200 security leaders (CISO or equivalent) and 200 senior engineering leaders (VPs of Engineering, CTOs, or equivalent) for Aikido Security and found that 76% have had to intervene to stop or restrict AI behavior, while 71% say AI has made security incidents much harder to detect, investigate, or fix.

Most troubling, perhaps, is the finding that security testing can’t keep pace with software delivery. Over three-quarters (76%) of those surveyed release updates weekly or faster, while over half (51%) admit that pentesting would delay software releases, which would have commercial impacts. So, many ship despite knowing the threats – ornotknowing them – which dumps all the risk on customers. Only 21% validate security on every release, says the report, and most fixes are not verified.

## Impact

So, what are the effects of all this? Aikido says that 51% of security leaders admit that logic flaws, broken access controls, and multi-step vulnerabilities are missed “always or often”, with that number rising to 92% for teams shipping daily or faster. Meanwhile, over half of the developer teams admit they lack visibility into whatwastested.

That isn’t news to anyone who has used a buggy app in a world of ‘release now, patch later’, but the AI dimension makes the situation more alarming, given that user organizations and developers alike have handed control over vital processes to agentic systems, largely due to hype. Many are like driverless cars careening through traffic on a crowded highway: no one is sure of the destination, but everyone was handed the same instruction to get in!

There is another dimension to all this. AI can no longer be separated from software development. Vibe coding has become orthodox less than four years on from the launch of ChatGPT, while co-pilot-assisted coding is standard practice. This is another risk, notes Aikido, as 42% of developers’ security leaders say that incorrect or hallucinated findings – across any internal process – are the biggest trust breaker, above missed vulnerabilities (32%).

So, it is hardly surprising that leaders want security testing and validation to happen more often: 69% would validate security on every release – or at least quarterly, if the technical (and therefore financial/commercial) restraints disappear. (At this point I can imagine the rictus grins of disbelief on users’ faces as they realize that only two-thirds would do it, if they didn’t lose money and traction...)

That developers want to go faster isn’t news, and neither is enterprises’ susceptibility to hype and 'me-too' tactical pressure.But clearly, all this is a massive challenge for red, blue, and purple teams within enterprises of every kind – both users and developers. Their job is to find and plug vulnerabilities in systems, after all; in the red team’s case by thinking like an attacker. Penetration testing (pentesting) is vital, therefore, but how to manage it successfully?

Often, the tech industry’s response is to say that only AI can solve the problem of AI and face down its disruptive tendencies and security holes: fight fire with fire. But earlier this year, my interview with ThreatLocker CEO Danny Jenkins at Zero Trust World in Orlando suggested it is not as simple as that. He told me:

AI is changing the world, but it's changing it for attackers. It's making their life a hell of a lot easier. […] One of the illusions that has been propagated is, ‘Oh, we're going to have an AI-based defence and it's going to stop the AI attacks’.

Jenkins then set out detailed, evidenced examples of how easy it is to fool an AI into acting maliciously or ignoring code that has a hostile purpose, explaining:

[The AIs] are no good, because they have no concept of intent. What’s the difference between a remote access tool that an attacker uses and a remote access tool that an IT professional uses? There is none. And what is the difference between backup software and data exfiltration software? The answer is both have the exact same functions. So, it all depends on the user’s intent. AI can tell you a function, but it can't tell you the intent. And that is why AI can't stop AI, because you can't read the mind of the creator of the software. It’s why you must have a human in the loop, and it’s why we're all about zero trust. The belief that AI can detect if something is good or bad is delusional.

## The Aikido view

I put all this to Aikido Security’s own CISO, Mike Wilkes, as his company offers autonomous pentesting. Speaking first in general terms about the FOMO foam on the wave of agentic AI, he says:

One of my NYU students had this great metaphor. Human knowledge is like sunlight, and Large Language Models and AI are like moonlight – just a reflection of human knowledge. Even though you have vampires like Sam Altman howling at the moon, saying ‘This is the shit, this is the shit’, at the end of the day, sustainable life on earth doesn't exist without sunlight. You can't live on moonlight alone.

As for ThreatLocker’s point about how easy it is to game an AI, which, of course, is a vital consideration when pentesting new software, Aikido’s Wilkes explains:

All we have to do in some cases [to make an AI do something unethical or illegal] is threaten to sue it, and then it conforms with the request. That’s because there's a deeply litigious grain of respect and fear in these models, coming from the training data in America, so when it says, ‘I don't want to do that, and I say, ‘Well, I'm going to sue you’, then it does it. All it ‘knows’ is tokens and predictions, so the gravitas around lawsuits gives it the extra bump. We're not necessarily using uncensored models to do our autonomous pentesting. That's one of the things I spoke about recently at Google, where I coined the term ‘Mythos Ready’. The reality is that zero companies right now, including Anthropic, are Mythos ready, at least for Mythos-level classes of attacks.

So, what about the common findings from Economist Enterprise and Aikido’s own survey? Wilkes acknowledges the similarity:

Of those that ship daily, 92% stop, restrict, and roll back AI. But I think that's actually a healthy indication that your governance policies are effective! One of the KPIs I've suggested is that if you're not blocking privilege escalation attempts by agentic agents and workflows daily, then you don't have AI governance, because it should be trying to level up, right? And privilege escalates everywhere it's operating.

The growing pursuit of tech sovereignty adds another dimension to this, Wilkes agrees:

You can be riding the FOMO train, yet still be deeply concerned about silent subpoenas, right, and running your own GPUs in your own data center. I think there's a huge RFP [Request for Proposal] for a European data center right now, despite Amazon launching a sovereign entity. So, why would Amazon create a separate legal European entity to service European data center markets, when they already have GPUs, CPUs and infrastructure in place? Well, I infer that it's because of the ‘silent subpoena’: the risk of the US administration saying, ‘Hey, I want to watch and know what's in all those data buckets [in Europe]'.

He continues:

One of the things that came up at the Google meeting, which was under Chatham House rules, so I can't say who said it, is ‘The CVE [list of Common Vulnerabilities and Exposures] is dead, long live the CVE.’ The National Vulnerability Database is also dead in water. Nobody should be focused entirely on CVEs and vulnerabilities anyway, because that's only 20% of what we like to call now.

## Advice

What then is to be done? Wilkes suggests:

If you take a more positive approach, the ‘protect surface’, as opposed to the attack surface, then you should ask what you need to protect, because not everything that's internet facing is of equal risk, and I think AI seems like an easy path. So, there's an inordinate focus now on CVEs, because that's something that CISOs can wrap their heads around. We must patch within hours instead of days, right? And we must automate the QA and testing… all of that's true. But that’s just the basic hygiene of application security being accelerated from a daily or weekly cadence to hourly mitigations and patching cycles. And the QA and regression testing required for that is a discipline that a lot of companies don't have!

But most of the stuff we're finding via our autonomous pentesting is going to be business logic flaws, and misconfigurations. And so, with those kinds of things you do have a defender's advantage, because you get to test your stuff first with a white-box pentest. And if you're not doing that, then you're just launching code that you know is vulnerable, but you don't know where. And when attackers come at it, they're coming at it with a black box. They don't get to see the code base for your custom-built API.

What we found was a ratio of maybe seven-to-one, so if you found five vulnerabilities in a black box pen test of an API, then we would find 35 with a white-box pen test. So, there is an advantage to running continuous autonomous pentesting, and what we're calling self-securing software, and getting that capacity in front of people. And not needing Mythos to do it!

## My take

Entertaining stuff from the ever-quotable Wilkes. But unlike many security white papers, Aikido’s is adept at identifying the scale of the problem, but less so at offering workable solutions.