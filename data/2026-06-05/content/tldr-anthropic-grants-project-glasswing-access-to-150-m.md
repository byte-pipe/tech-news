---
title: Anthropic grants Project Glasswing access to 150 more companies, with a focus on critical infrastructure | CSO Online
url: https://www.csoonline.com/article/4180265/anthropic-grants-project-glasswing-access-to-150-more-companies-with-a-focus-on-critical-infrastructure.html
site_name: tldr
content_file: tldr-anthropic-grants-project-glasswing-access-to-150-m
fetched_at: '2026-06-05T12:04:00.675391'
original_url: https://www.csoonline.com/article/4180265/anthropic-grants-project-glasswing-access-to-150-more-companies-with-a-focus-on-critical-infrastructure.html
date: '2026-06-05'
description: As the number of vulnerabilities identified soars, analysts see a patch development bottleneck as the big problem; vendors can’t keep up now.
tags:
- tldr
---

by									
Evan Schuman

Contributor

# Anthropic grants Project Glasswing access to 150 more companies, with a focus on critical infrastructure

News

Jun 2, 2026
7 mins
 

## As the number of vulnerabilities identified soars, analysts see a patch development bottleneck as the big problem; vendors can’t keep up now.

 

							Credit: 															T. Schneider / Shutterstock													

Anthropic on Tuesday announced that it was adding 150 more companies to its Project Glasswing AI-based vulnerability hunting initiative, with a particular focus on critical infrastructure companies including those involved in “power, water, healthcare, communications and hardware.”

Analysts and security vendors agreed that the move is a positive step, noting that the more companies involved in bug identification, the better. But the bigger background issue is a practical one: the bottleneck problem.

If Project Glasswing, and similar projects from other major AI vendors, increase the stream of vulnerability identifications by 10 or more times, will vendors be able to triage and patch them in a timely manner? Vendors have historically been notoriously slow to patch known security issues. Microsoft, for example,recently argued with a security researcherwho went public with holes because he felt that Microsoft was too slow in addressing them.

And even if those vendors can keep up, are enterprise SOCs going to be able to keep up with the avalanche of patches? And if extensive automation is deployed to generate those patches, will CISOs trust them enough to let them be deployed without manual verification? Trust is not a common CISO trait.

“What each partner has in common is that a successful attack on their codebase could be catastrophic. For most partners, we estimate that a major attack could affect more than 100 million people, with important ramifications for both global and national security,”Anthropic said in its blog postannouncing the new participants. “This expansion is the next step toward our long-term goals: for AI to make all software more secure, and for us to help the industry adjust to how AI could change many of the core assumptions of cybersecurity.”

Glasswingwas announced on April 7 and was initially supported by AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks. Okta later confirmed that it was also involved.

## The patch bottleneck

The bottleneck problem is a difficult one to solve, given that even the largest vendors can only cost-justify so many resources for patching security holes and distributing those patches.

“The biggest issue is adaptability: once a vulnerability or weakness is found, defenders have to validate it, prioritize it, and fix it before attackers can operationalize the same insight. And that validation step matters,” saidTom Findling, CEO of Conifers.ai. “While testing the tool ourselves, we saw a lot of false positives, which means organizations cannot simply treat every finding as immediately actionable. They need the ability to separate signal from noise quickly, then adapt their processes, engineering workflows, and patching pipelines around the real issues.”

“The most important metric for organizations to track may not just be how many vulnerabilities are found, but how long it takes them to adapt once a credible issue is identified. For some organizations, that adaptation cycle can still take months,” he added. “Reducing that time-to-adapt is what will determine whether AI-assisted vulnerability discovery actually improves defense or just increases the speed and volume of security noise.”

## A remediation problem

Justin Greis, CEO of consulting firm Acceligence, agreed that the Glasswing expansion may simply demonstrate to CISOs how much the security hole problem is shifting, not shrinking.

“It’s no secret that cybersecurity has been treated as a vulnerability discovery problem. AI is proving that it was really a remediation problem all along. The industry already struggles to validate, prioritize, patch, test, and deploy fixes fast enough. It may even be worse if security teams own the vulnerability identification and the IT teams, or the business teams, own the patching itself,” Greis said. “If AI can identify vulnerabilities 10x or 100x faster than humans, the bottleneck simply moves downstream. Organizations may soon find themselves in the uncomfortable position of knowing about far more vulnerabilities than they can realistically address. AI is turning cybersecurity from a visibility problem into an execution problem.”

Greis added a frightening prediction: “AI could make organizations simultaneously more secure and more overwhelmed, if that’s possible. They’ll have unprecedented visibility into their risk, but they’ll also discover just how large that risk really is.”

## Trust required

Grace Trinidad, research director for AI security at IDC, said the bottleneck problem at the enterprise needs to be addressed via extensive automation. But given the lack of trust by cybersecurity staff, vendors must have a rigorous method for producing a numerical confidence score for every patch.

“Having a confidence score accompanying these patches is a new concept. There must be an ability of the enterprise to identify, triage and address the vulnerabilities that are specific to their environment,” Trinidad said. “We are learning a skillset that we are not ready for: How do we trust automated technologies? Given that we are having to move at this speed, that trust is going to get broken. Confidence scoring is a discipline that needs transparency. Don’t make the confidence [explanation] so complicated that you can’t explain it to a human being.”

Trinidad also noted that the Anthropic announcement pointed out that each of the 150 new participants, in Anthropic’s phrasing, “will need to meet our security requirements before they gain access.”

Trinidad said the security requirement claim doesn’t build confidence, because “nobody knows what those security requirements are.”

One possible solution is for security vendors to use high-trust third parties so that they are not seen as ‘grading their own homework’. Enterprise software vendor Workday is using a similar third-party approach, relying on trusted services that use public standards such as Mitre ATLAS to validate the security and compliance of AI agents using its platform.Workday’s approachdeals with security checks and not reliability scores, but the idea could potentially be tweaked.

## Expansion creates security concerns

Carmi Levy, an independent technology analyst, was more skeptical about what Glasswing will ultimately be able to accomplish by adding 150 more participants.

“The entire point of Project Glasswing was to allow Anthropic to work closely with a small, fully vetted group of vendors to develop stronger defenses against the cybersecurity risks posed by what was, and is, an entirely new LLM class that would otherwise pose unacceptable risks to existing protective technologies and protocols,” Levy said. “Expanding access into the hundreds may very well bring in more minds to build better defensive measures, but it simultaneously introduces significant concerns around potential leaks. And this from a company that has already reported two leaks involving this same model.”

Levy added, “in an ideal world, Anthropic would announce alongside this major expansion a parallel effort to tighten internal security protocols to ensure the code doesn’t fall into the wrong hands. Bringing in a much larger cohort of researchers signals to potential attackers that they will soon have a larger pool of potential targets, and fails to allay fears of future breaches.”

Artificial Intelligence
Security
 

 

				SUBSCRIBE TO OUR NEWSLETTER			

### From our editors straight to your inbox

				Get started by entering your email address below.			

 

Please enter a valid email address

Subscribe

 

														by 															

																Evan Schuman															

Contributor

1. Follow Evan Schuman on LinkedIn

Evan Schuman has covered IT issues for a lot longer than he'll ever admit. The founding editor of retail technology site StorefrontBacktalk, he's been a columnist forCBSNews.com,RetailWeek,Computerworld, andeWeek, and his byline has appeared in titles ranging from BusinessWeek,VentureBeat, andFortunetoThe New York Times,USA Today,Reuters,The Philadelphia Inquirer,The Baltimore Sun,The Detroit News, andThe Atlanta Journal-Constitution. Evan is a frequent contributor toCIO,CSO,Network WorldandInfoWorld.Evan won a gold 2025 AZBEE award in the Enterprise News category for this story:Design flaw has Microsoft Authenticator overwriting MFA accounts, locking users outHe can be reached at eschuman@thecontentfirm.com and he can be followed onLinkedIn.

## More from this author

* news### Microsoft and security researcher’s dueling posts about cybersecurity disclosures get nastyMay 29, 20267 mins
* news### Microsoft May security patch fails for some due to boot partition size glitchMay 18, 20265 mins
* news### Questions raised about how LinkedIn uses the petabytes of data it collectsApr 8, 20264 mins
* news### A core infrastructure engineer pleads guilty to federal charges in insider attackApr 3, 20263 mins
* news### Cloudflare’s new CMS is not a WordPress killer, it’s a WordPress alternativeApr 2, 20267 mins
* feature### It’s time to rethink CISO reporting linesFeb 24, 20266 mins
* news### Anthropic’s Claude Code Security rollout is an industry wakeup callFeb 24, 20269 mins
* news analysis### PayPal launches latest struggle to get rid of SMS for MFAFeb 20, 20267 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

news
 
 

### OpenAI responds to White House executive order on AI governance

 
By Gyana Swain
Jun 4, 2026
5 mins

Government
IT Governance
Markets

news analysis
 
 

### Hugging Face Transformers RCE flaw enables stealthy compromise via AI model configs

 
By Lucian Constantin
Jun 4, 2026
7 mins

Artificial Intelligence
Python
Vulnerabilities

news
 
 

### Beware the ‘son of Mythos,’ security experts warn

 
By John Leyden
Jun 4, 2026
4 mins

Artificial Intelligence
Security Software
Threat and Vulnerability Management

podcast
 
 

### Why AI Is Forcing a Rethink of Data Security

 
By Joan Goodchild
Jun 4, 2026
7 mins

Data and Information Security

podcast
 
 

### Security Blind Spots: What the Louvre Heist Reveals About Your Organization

 
By Joan Goodchild
May 21, 2026
34 mins

Cybercrime

podcast
 
 

### CSO Executive Sessions ASEAN: From Compliance to Cyber Resilience-Securing Patient Trust in Southeast Asia’s Hospitals

 
By Estelle Quek
25 Feb 2026
23 mins

Cyberattacks
Cybercrime
Ransomware

video
 
 

### Why AI Is Forcing a Rethink of Data Security

 
By Joan Goodchild
Jun 4, 2026
7 mins

Data and Information Security

video
 
 

### Security Blind Spots: What the Louvre Heist Reveals About Your Organization

 
By Joan Goodchild
May 21, 2026
34 mins

Cybercrime

video
 
 

### The Human Side of Cybersecurity: Stress, Deepfakes & the Hidden Cost of Breaches

 
By Joan Goodchild
May 7, 2026
25 mins

Data and Information Security