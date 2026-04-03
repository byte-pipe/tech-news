---
title: A Horrible Conclusion · Addison Crump
url: https://addisoncrump.info/research/a-horrible-conclusion/
site_name: lobsters
content_file: lobsters-a-horrible-conclusion-addison-crump
fetched_at: '2026-02-08T13:38:53.197592'
original_url: https://addisoncrump.info/research/a-horrible-conclusion/
date: '2026-02-08'
description: Homepage for Addison Crump
tags: ai, security
---

Published: 2026-02-06

I amnot fond of this recent genenerative AI movement.
It is a profound waste of resources, a theft machine masquerading as intelligence, and generally a tool which enables numerous social harms at scale.
I am a firm proponent that we (academics) should not be involved in the rat race to improve or to use these systems because of their enormous ethical violations.

Yet there is a cold calculus which demands their inclusion in security testing.
Not reliance, but inclusion.
And though I stand by my choice to ensure that none of my research nor personal work includes these tools, I must acknowledge their impact on my domain.
That impact is, so far, mostly fraudulent.

# A little context

Security testing is, in principle, mostly a means to mitigate harms from bad design decisions.
As an example,memory safety should no longer be a concern, yet it is because of technical debt and stubbornness.
Old systems are still used in many places because we understand their reliability under normal scenarios, even if they aren't secure (looking at you, industrial control systems andbank python).
Pretty much every issue in security testing is a problem induced by resources being limited, and thus we need to use the duct tape of security testing to hold it in place.

But the question in testing is never, "can we make sure this system is bug-free?"
The question is, "can we make it bug-freeenough?"

### Bug-freeenough?

Students who take security courses in university will generally be taught risk analysis: there is some threat with the capacity to do some harm with some likelihood; the risk is the potential damages times the probability that the damage occurs.
Of course, this is wildly simplified, but the general objective of such calculations is to estimate how much one should spend on security testing or on extra time during design to mitigate things in advance.
I've never been fond of such calculations because they tend to be used to justifynotspending as much as one should on security or safety by underestimating damages (intentionally or not) or only calculating damages incurred by the subject of the calculation (Ford Pinto, anyone?).
As a result, I don't put too much thought into such measures of risk or balance of harms and benefits.

Risk calculation like this is a ham-fisted approximation of similar concepts in ethical analyses.
Though widely mocked for its contrivedness, the trolley problem corresponds to real decision-making scenarios.
Sometimes, one must make choices which balance harms and benefits.

# AI and security

The maintainers of curl note that AI has, in addition to anoverwhelming amount of slop, foundhundreds of valid bugs in curl.
This result is meaningful: these tools (appear to) have the means to automate the discovery of bugs in code that would not have been discovered without extremely careful analysis by human reviewers.
Some of these finds (<10?) were legitimate vulnerabilities.

This result suggests that these tools represent a meaningful step in vulnerability research -- for both attackers and defenders.
In the hands of a few experts, these tools significantly increased vulnerability discovery throughput.

### Allegedly

Of course, we need to take this with a grain of salt.
The reporters here have a financial incentive to say that their security findings are a result of their magic boxes.
Given the relatively low volume of security findings versus the other bugs that were found, I have my reservations about how effective these tools are in reality.
Moreover, some of these security findings are legitimate, but were not reachable in practice (see the krb5-ftp bug from Daniel's blog).
Defense in depth demands we address these findings, but it removes the immediacy of resolution.

# Working it through

Let's suppose that these toolssignificantly increase the rate of vulnerability discovery, as these companies are financially incentivized to claim.
It is well-understood that safeguards are not that meaningful in the presence of a motivated prompter, so this only slows down the initial process of getting a working bug printer.
As a result, we now (supposedly) live in a world where attackers now have access to tools which find security bugs quickly.

The conclusion that we are intended to make is that defendersmustuse these tools now, lest the attackers use them first.
After all, there are many more attackers with far more resources than defenders, and attackers have the same access to these resources as us.
Anthropic has, in principle, positioned themselves an exclusive arms salesman for the security domain.
Even if we don't want to use these tools, we might have a duty to do so -- regardless of the harms these companies cause to the environment and society and their utter disregard for intellectual property, not using these tools could have catastrophic effects when zero days are discovered by attackers who do use these tools.

### Allegedly

Again, this is from a company financially incentivized to convince us that their tools can find vulnerabilities quickly.
Anthropic claim to have "found and validated more than 500 high-severity vulnerabilities", yet only exhibit a few here and don't specify in what projects they've found them.
This is very likelyconfusing value with enumeration.

Moreover, I'm dubious of the quality of the reports they list.
It took a while to hunt down, buthere is the actual commit that resolves the Ghostscript bug.
They did not assign a CVE, nor did they mark it as a security vulnerability (note that that's just the name of the bug report), nor did they cut a release for this; just publicly fixed it.
This is not the "high-severity vulnerabilit[y]" I was promised!

### A back of the hand analysis

Let's suppose again that Anthropic has indeed headlessly gotten Claude to find hundreds of security-relevant bugs (which they don't explicitly claim, but heavily imply).
First, why on earth would they think it appropriate to release this to the public without considerable lead time?
There were onlytwo monthsbetween the release of Opus 4.5 and 4.6, and their claim is that 4.6 was spontaneously capable of far more vulnerability discovery, meaning that they've spent likely less than three months experimenting with this.
That's shorter thanstandard disclosure windows.
Even supposing that the bugs they were finding were truly "high-severity" and "indicating an inflection point in cybersecurity", this is not enough time to do due diligence in applying these tools to open-source repositories, and their financial incentives overcame their duty to security.

Second, let's consider the finances of this.
Anthropic has, withseveral billions of dollars of funding, developed a tool which has "found and validated more than 500 high-severity vulnerabilities".
I will acknowledge that there are other applications of these tools, but let's just consider for a moment that, with a fairly minor redistribution of funds here, there are absolutely security professionals who you could have just hired to find similar vulnerabilities.
The problems that AI proposes to solve are those of scale and (financial/human) resources, but if we just actually used our resources to pay people to find these bugs, we would likely find them much more cost effectively.

# Conclusion

There do indeed appear to be some applications of AI in the security domain, and a naïve analysis based on the claims of the AI companies which are financially incentivized to get you to use their tools would suggest that we have an ethical obligation to do so: the attackers certainly will, so you need to as well to catch up!
A slightly deeper analysis suggests that this is just not the case; these tools are automating some tasks, but they are not actually dramatically affecting vulnerability discovery rates compared to the cost of finding them by "classic" means.
Furthermore, even if it were the case that these tools are massively increasing vulnerability discovery throughput, these companies would be massively negligent if not outright malicious in their early release of these tools.
They utterly fail to take the time to mitigate potential harms of the vulnerabilities they discover (or claim to have, at least) and make laughable safeguards to prevent "malicious" discovery of vulnerabilities,admittingthat it would also kneecap legitimate discovery of the same bugs.

The security community should look at the massive investment into AI companies as a wild misuse of funds.
Just pay an actual researcher or two, dammit.
They'll have better quality findings and they won't try to sell you the means to your own destruction at the same time.

As for academia: perhaps there are still reasons to look into other means of automated vulnerability discovery.
There's room for researching LLM capabilities in vulnerability discovery, but these companies are clearly misrepresenting their efficacy.
Maybe we focus on the things that don't have other massive ethical concerns attached to them, first.

I write this blog on a rather short timeline, and, as such, you might notice that the conclusion is a bit rushed, and maybe the post is a bit more disconnected than usual.
My partner and I are planning to go out for lunch.
Perhaps this topic deserves a bit more polish and evidence -- but I really don't care to give these companies any more time in my mind.
If you disagree with my conclusions here, drop me a message on Mastodon and I'll consider following up on this.
