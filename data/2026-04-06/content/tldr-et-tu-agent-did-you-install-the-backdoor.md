---
title: Et Tu, Agent? Did You Install the Backdoor?
url: https://www.a16z.news/p/et-tu-agent-did-you-install-the-backdoor
site_name: tldr
content_file: tldr-et-tu-agent-did-you-install-the-backdoor
fetched_at: '2026-04-06T01:01:37.037219'
original_url: https://www.a16z.news/p/et-tu-agent-did-you-install-the-backdoor
author: Joel de la Garza
date: '2026-04-06'
description: Everyone knows supply chain attacks are a problem. That’s not the point.
tags:
- tldr
---

# Et Tu, Agent? Did You Install the Backdoor?

### Everyone knows supply chain attacks are a problem. That’s not the point.

Joel de la Garza
, 
Malika Aubakirova
, and 
Zane Lackey
Apr 02, 2026
49
7
2
Share

America|Tech|Opinion|Culture|Charts

This week, someonehijackedone of the most popular packages on the internet and used it to install a backdoor on every machine that ran npm install.

The package was Axios, which is the HTTP library that powers network requests in millions of applications. It gets downloaded over 100 million times a week. If you’ve built anything in JavaScript in the last decade, you’ve almost certainly used it, or something you depend on has used it for you.

The attacker didn’t change a single line of Axios’s source code. They compromised a maintainer’s account, added one new dependency to the package manifest, and published an update. That dependency, a brand-new package called plain-crypto-js that had been registered hours earlier, ran a script on install that detected your operating system, downloaded a remote access trojan tailored to your machine, executed it, and thendeleted itself. By the time you looked at your node_modules folder, it was gone. The malware had already phoned home.

This is the new shape of software supply chain attacks: fast, quiet, and invisible to traditional security tools. And it’s accelerating.

Feross
@feross
🚨 CRITICAL: Active supply chain attack on axios -- one of npm's most depended-on packages.

The latest axios@1.14.1 now pulls in plain-crypto-js@4.2.1, a package that did not exist before today. This is a live compromise.

This is textbook supply chain installer malware. axios
2:35 AM · Mar 31, 2026
 · 
11.7M Views
524 Replies
 · 
4.07K Reposts
 · 
16.2K Likes

## Everyone knows supply chain attacks are a problem. That’s not the point.

If you work in security, you’ve heard this story before. SolarWinds. Log4Shell. The XZ Utils backdoor. Supply chain attacks make headlines, the industry wrings its hands, and then everyone goes back to business.

So what’s different now?

Two things changed in the last twelve months, and they changed at the same time. First, frontier coding models got good enough to write and ship code autonomously, and that made both sides faster. AI agents are pulling in dependencies at machine speed with minimal human review. Second, attackers figured out how to weaponize the dependency graph at scale - not just targeting one package, but cascading across entire ecosystems in days.

The result is a mismatch that should terrify anyone building software: the attack surface is expanding faster than any human can monitor, and the entities making dependency decisions are increasingly not human.

## Dependencies are the new perimeter

It’s always been true that the code you write is a small fraction of the code you ship.The average application contains over 1,100 open source components. A bare-bones Next.js project installs 282 packages before you write a single line. The median JavaScript project on GitHub has 755 transitive dependencies - packages that your packages depend on, chosen by nobody on your team.1

When an attacker compromises one node in that graph, they don’t need to target you specifically. Every npm install during the exposure window is a potential victim. The Axios attacker didn’t need to know who you are or what you built. They compromised the foundation of the ecosystem and waited for it to collapse.

#### Every Building You've Ever Been In Was Designed By Software Built in 1997

Joe Schmidt IV
, 
David Haber
, and 2 others
·
Mar 30
Read full story

#### Robotics Needs Fewer Roboticists*

Jacob Zietek
·
Mar 25
Read full story
Subscribe

Modern-day security tooling looks for the wrong things. Most software composition analysis tools work by checking your dependencies against a database of known vulnerabilities - CVEs. But a deliberately planted backdoor doesn’t have a CVE. There’s no database entry for a brand-new malicious package. Running npm audit on the compromised Axios version would have returned a clean bill of health, because the malware had already self-destructed.

## One stolen token, five ecosystems, eight days

The Axios hack was headline-grabbing, but it was arguably not even the most consequential supply chain attack this quarter. That distinction belongs to a campaign called TeamPCP, which demonstrated what cascading supply chain failure actually looks like.2

It started with Trivy, a widely-used open source vulnerability scanner. An attacker exploited a misconfiguration in its GitHub Actions workflow to steal an access token. From there, they force-pushed malicious code to nearly all of Trivy’s version tags, meaning anyone pulling the scanner was now running the attacker’s code. The payload harvested credentials from the CI/CD environment: SSH keys, cloud tokens, and npm tokens.

Those stolen npm tokens fueled the next stage. A self-propagating worm called CanisterWorm spread across 66+ npm packages, using blockchain-based command infrastructure that couldn’t be conventionally taken down. It harvested more tokens from infected developer environments and automatically published malicious updates to every package those tokens had access to.3

Within eight days, the same campaign had cascaded from GitHub Actions to Docker Hub, npm, PyPI, and the VS Code extension marketplace. With just one token across five ecosystems, thousands of organizations were potentially impacted.

Supply chain attacks used to be surgical, patient, and targeted;the most common exploits were things like a nation-state actor spending two years earning maintainer trust on XZ Utils. Now they’re automated, self-propagating, and ecosystem-spanning. The timeline compressed from years to days.

## AI coding, AI attack surface

The same AI tools that are making developers 2–4x more productive are also making the supply chain dramatically more vulnerable. And this cuts both ways: AI isn’t just writing vulnerable code; attackers are using the same tools to generate malicious packages, automate propagation, and find weaknesses at machine speed.

Astudyof over 117,000 dependency changes across thousands of GitHub repositories found that AI agents select known-vulnerable dependency versions 50% more often than humans. Worse, the vulnerable versions they pick are harder to fix, requiring major-version upgrades far more frequently.

Hallucinated packages are the sleeper threat. LLMs regularly invent package names that don’t exist.One studyfound that nearly 20% of AI-recommended packages were fabrications, and 43% of those hallucinated names appeared consistently across queries. Attackers have figured this out. The technique is called “slopsquatting“: register the fake package name the AI keeps recommending, fill it with malicious code, and wait. One researcherdemonstratedthis by uploading a dummy package with a commonly hallucinated name and watching it accumulate 30,000 downloads - largely from AI-driven workflows - in weeks.

The autonomous coding agents now entering production can install dependencies, execute builds, and open pull requests without a human ever touching the keyboard. They optimize for “does this work?” not “is this safe?” And they do it at speeds that compress the window for security review to essentially zero.

There’s also the risk that coding agents are themselves becoming formidable instruments of attack, even when they aren’t explicitly asked. Truffle Securityrecently found thatOpus 4.6, along with other models, would discover and exploit SQL injection vulnerabilities when asked to fetch basic information from websites, in cases where the legitimate path to that information was blocked. So imagine what these coding agents are capable of when they’re wielded explicitly to mount sophisticated supply chain attacks.

We are building a world where machines write the code, machines choose the dependencies, and machines ship the updates. The AI agents are building the software. If we don’t secure the supply chain they rely on, the AI agents are cooked.

## Your Scanner Wouldn’t Have Caught It

The industry average time to detect a supply chain breach is 267 days. SolarWinds went undetected for 14 months. XZ Utils took two years to surface.

Socket, an a16z portfolio company,detectedthe malicious dependency in the Axios attack within 6 minutes of its publication. That’s roughly 63,000 times faster than the industry average. They flagged it 16 minutesbefore the first compromised Axios version was even published, because they caught the suspicious dependency package itself.

How? Socket doesn’t check packages against a vulnerability database. It analyzes what the code actuallydoes: Does it access the network? Spawn shell processes? Obfuscate its payload? Execute postinstall scripts? Read environment variables? This behavioral approach catches novel malicious packages that have no CVE and no prior history - exactly the kind of attack that traditional tools miss entirely.

The Axios attack was live for about three hours before npm pulled the compromised versions. In that window, tens of thousands of installations likely occurred. On 135 endpointsmonitoredby one security vendor alone, the malware executed and phoned home to the attacker’s server within 89 seconds of install. The gap between what’s possible (6-minute detection) and what’s typical (267-day detection) is where the damage happens.

## Save the AI agents. Save the Robots

The software supply chain has become the most critical and least-defended attack surface in modern software development. AI is accelerating both sides of the equation: attackers using it to generate malicious packages at scale, defenders racing to build behavioral detection systems that can keep up. And the shift to autonomous AI agents writing and deploying code without human review has compressed the timeline from months to minutes.

The teams that are winning this fight share a common trait: they stopped waiting to be told they’d been compromised. They moved security controls to the point closest to the threat - the moment a dependency enters the build. They stopped relying solely on CVE databases and started analyzing actual package behavior. And they started treating their dependency graph not as a list of libraries, but as a living attack surface that needs continuous monitoring.

Software is being built at the speed of machines now. If defenders don’t match that speed, the machines shipping the code will be shipping the malware too.

Save the AI agents. Secure the supply chain.

#### America’s Energy Problem Isn’t Supply. It’s Delivery.

Andrew Baglino
·
Apr 1
Read full story

#### IT: The 6T Industry that Silicon Valley Hardly Ever Thinks About

Peter Doyle
·
Mar 31
Read full story
Subscribe

This newsletter is provided for informational purposes only, and should not be relied upon as legal, business, investment, or tax advice. Furthermore, this content is not investment advice, nor is it intended for use by any investors or prospective investors in any a16z funds. This newsletter may link to other websites or contain other information obtained from third-party sources - a16z has not independently verified nor makes any representations about the current or enduring accuracy of such information. If this content includes third-party advertisements, a16z has not reviewed such advertisements and does not endorse any advertising content or related companies contained therein. Any investments or portfolio companies mentioned, referred to, or described are not representative of all investments in vehicles managed by a16z; visithttps://a16z.com/investment-list/for a full list of investments. Other important information can be found ata16z.com/disclosures. You’re receiving this newsletter since you opted in earlier; if you would like to opt out of future newsletters you may unsubscribe immediately.

49
7
2
Share