---
title: AI’s brave new world of technical debt | InfoWorld
url: https://www.infoworld.com/article/4178964/ais-brave-new-world-of-technical-debt.html
site_name: tldr
content_file: tldr-ais-brave-new-world-of-technical-debt-infoworld
fetched_at: '2026-06-03T20:09:11.167451'
original_url: https://www.infoworld.com/article/4178964/ais-brave-new-world-of-technical-debt.html
date: '2026-06-03'
description: AI agents make work easier by adding layers of delegation. Those layers become dependencies, and those dependencies become risk.
tags:
- tldr
---

by									
Matt Asay

Contributing Writer

# AI’s brave new world of technical debt

opinion

Jun 1, 2026
9 mins
 

## AI agents make work easier by adding layers of delegation. Those layers become dependencies, and those dependencies become risk.

 

							Credit: 															Rob Schultz / Shutterstock													

Mitchell Hashimotowants you to stop updating your dependencies, which, from a historical context, is certifiably insane. In fact, in the wake ofMythosand thepotential to make zero-day exploits common, it still may sound insane. Yet after the spring npm just had, Hashimoto’s counsel may actually sound less like heresy and more like control.

His rule? Fork your dependencies, trim them to what you actually use, and don’t update unless something breaks for your users. In Hashimoto’s view, you don’t update just because GitHub’s Dependabot opened a pull request or even because there’s a newer (presumably more secure) version. If you do update, the work of understanding every relevant commit in the transitive tree is yours, not the maintainer’s.

In an industry trained to equate “latest” with “secure,” this sounds reckless, until you look at what happened this spring. In two of the year’s worst npm attacks, many of the people most exposed were the ones pulling fresh versions. Whenthe axios HTTP client library was compromised, attackers pushed two poisoned releases that dropped a remote-access Trojan on every machine that ran a fresh install during a roughly three-hour window. If you were pinned to a clean version and didn’t reinstall, you slept through it. Kudos to you. Weeks later, on the heels of apoisoned node-ipc release, theMini Shai-Hulud wormself-propagated through TanStack and on to Mistral, UiPath, and a long tail of packages downloaded millions of times a week.

How do you defend against that?

Maybe by doing nothing. After all, the single most effective defense against Mini Shai-Hulud wasn’t a scanner or a signature. It was a cooldown. StepSecurity held newly published versions for a configurable window, around 10 days, before serving them to anyone. Customers on the cooldown kept getting the last known-good release and were never exposed, while the rest of the world found out the hard way.

In other words, the defense that worked was the unfashionable (and historically foolish) one: Don’t take the new version just because it’s new. Ironically, the industry’s answer to AI development seems to be to add more dependencies. What could go wrong?

## The dependency tree escaped the package manager

For decades we’ve outsourced undifferentiated work to libraries, and mostly that’s good. After all, no one wants every team to hand-roll Transport Layer Security, date parsing, logging, etc., except perhaps the sort of person who compiles Gentoo for fun. (We know who you are!) Open source works because we specialize and share.

Sharing means we also borrow each other’s package managers, maintainer accounts,CI/CD pipelines, release scripts, etc. The miracle of modern software is that a small team can build something world-class out of a thousand components it didn’t write. That’s also the risk.

AI compounds this risk because the dependency tree is no longer confined to code.

A coding agent doesn’t just import packages: It also reads repo instructions, follows system prompts, picks tools, talks toModel Context Protocol(MCP) servers, and runs shell commands. Each capability is another dependency on behavior that lives outside the model. Some of this is useful, of course, but all of it is surface area, open to attack.

Consider that in astudy of 117,062 dependency changes across seven ecosystems, researchers at Purdue found that AI agents selected known-vulnerable package versions more often than humans, 2.46% of the time versus 1.64%. The agents’ bad picks were also harder to undo: 36.8% required a major-version upgrade to remediate, against 12.9% for humans. At the aggregate level, agent-driven dependency work produced a net increase of 98 vulnerabilities while human-authored work produced a net reduction of 1,316. Agents also invent dependencies that don’t exist, which become an attack surface the moment someone registers the hallucinated name, as myInfoWorld colleague Lucian Constantin has covered.

Don’t take this as proof that humans always win. After all, developers have been making a mess of dependency graphs well before chatbots learned to obsequiously apologize. But letting agents “helpfully” add and update dependencies without guardrails is asking for a familiar problem at lightning-fast speed.

The MCP layer is its own version of the same trap.Microsoft has documented tool poisoning, in which malicious instructions hide inside the tool metadata a model reads to decide what to call. In its own red-team work, Microsoftfound that relying on the model to follow safety instructionsproduced policy violations more than 25% of the time and concluded that instruction-following alone shouldn’t be treated as a security boundary.OWASP said it more plainly: A tool response goes straight into the model’s context with no equivalent of the review a tool description gets at connect time, and a prompt restriction like “don’t read files outside/tmp” is enforced by the model’s goodwill, not by access control.

That’s bad. Are prompts even worse?

Sean Goedecke recentlyargued that prompts also introduce technical debtand decay silently. A prompt that worked against one model behaves differently against the next. Pile enough of them together—theAGENTS.mdandCLAUDE.mdfiles, the skills, the rules, the tool descriptions—and you’ve quietly built an alternate control plane for how your software gets written. Most teams never test it, review it, or prune it, leaving your agents to make worse decisions while sounding perfectly reasonable.

## ‘Latest’ is not the same as safe

The extreme version of Hashimoto’s rules won’t fix this, and frankly, they won’t work for most teams. Most enterprises don’t have the staff, the patience, or the judgment for it. But strip away that extreme version and the discipline underneath is exactly right: Every dependency should have a reason to exist, and every update should have a reason to land.

This cuts against the grain of modern development, where adding a package feels cheaper than thinking. It cuts even harder against how agents work. Agents are very good at finding a library, importing it, and moving on. They optimize for the fastest path to a passing test, not for the long-term health of your dependency graph. This is the same gapI keep coming back to with evals: AI doesn’t eliminate engineering discipline; it raises the price of skipping it. The model can make the change faster. It can’t reliably tell you whether the change belongs in your system.That judgment is still yours.

## Latent bugs won’t stay latent

Still, there’s a problem with Hashimoto’s approach, even the non-extreme version. Hashimoto’s bet assumes the undiscovered flaw in your frozen dependency stays undiscovered. For most of software history that was a safe assumption, because finding a deep logic bug in mature code was slow, expensive, human work. With AI that assumption no longer holds true.

In April, Anthropic’sClaude Mythos Previewautonomously found and built working exploits for a 16-year-old bug in FFmpeg and a 17-year-old root-access flaw in FreeBSD’s NFS server for under $20,000 across about a thousand runs. A month later, Google’s threat researchersflagged the first AI-developed zero-dayseen in the wild, a semantic logic flaw of exactly the sort traditional scanners miss.

These old dependencies felt safe, but now a hacker can inexpensively rent the discovery of chinks in the armor.

This doesn’t refute Hashimoto, but it does require a refinement of his rules. Trimming a dependency to just your use case yields better control, because every function you didn’t import can’t be turned into a zero-day against you. Forking lets you patch on your own time instead of waiting on an upstream maintainer. Importantly, the same models scoring your code for the attackers can (and must) score it for you first.

The rule was never really not to update. It’s instead to know your surface, keep it small, and keep scoring it, because now everyone else is.

## Fewer things, better understood

Yes, this changes the game. The best AI engineering teams won’t be the ones that wire agents into everything, sexy though that sounds. No, smart engineers will know precisely what they’ve wired in, why it’s there, and what happens when it changes.

That doesn’t mean banning MCP servers, agent tools, or third-party packages. That would be dumb. Rather it means treating all of them as production dependencies, because that’s what they are. If an MCP server can read email, query customer data, or execute code, it deserves thescrutiny of any other privileged integration. If a prompt file shapes how an agent edits your codebase, it belongs in version control, gets reviewed, and gets deleted when it stops being useful. This is where Goedecke’s advice and the governance instinct meet: Goedecke would keep that configuration layer as thin as he could, on the logic that the cheapest debt is the prompt you never wrote. The governance crowd would version, review, and gate whatever survives.

This isn’t really new. The history of this industry is littered with technologies that looked liberating until they became operational burdens, and the way to deal with them is usually the same.Microserviceswere going to free us from the monolith until many teams discovered they’d traded one big problem for 200 small ones connected by unreliable networks.Kuberneteswas going to standardize infrastructure until companies realized they’dimported a distributed-systems project into every team.

Agents are following the same pattern, only faster. They make work easier by adding layers of delegation. Those layers become dependencies, and those dependencies become risk. That’s not an argument to stop, but itisan argument to be more thoughtful.

Artificial Intelligence
Code Security
Security
Development Tools
Software Development
Security Practices
Generative AI
 

 

														by 															

																Matt Asay															

Contributing Writer

1. Follow Matt Asay on X
2. Follow Matt Asay on LinkedIn

Matt Asay runs developer marketing atOracle. Previously Asay ran developer relations atMongoDB, and before that he was a Principal atAmazon Web Services and Head of Developer Ecosystem forAdobe. Prior to Adobe, Asay held a range of roles at open source companies: VP of business development, marketing, and community at MongoDB; VP of business development at real-time analytics company Nodeable (acquired by Appcelerator); VP of business development and interim CEO at mobile HTML5 start-up Strobe (acquired by Facebook); COO atCanonical, the Ubuntu Linux company; and head of the Americas at Alfresco, a content management startup. Asay is an emeritus board member of theOpen Source Initiative (OSI)and holds a JD from Stanford, where he focused on open source and other IP licensing issues. The views expressed in Matt’s posts are Matt’s, and don’t represent the views of his employer.

## More from this author

* opinion### AI coding agents need good software engineersMay 25, 20268 mins
* opinion### The new AI lock-inMay 18, 20267 mins
* opinion### Your AI doesn’t need another databaseMay 11, 20268 mins
* opinion### Improving AI agents through better evaluationsMay 4, 202610 mins
* opinion### Google begins putting the guardrails on agentic AIApr 27, 20267 mins
* opinion### Making agents dullApr 20, 20268 mins
* opinion### Mastering the dull reality of sexy AIApr 13, 20266 mins
* opinion### Multi-agent AI is the new microservicesApr 6, 20267 mins
 

## Show me more

Popular
Articles
Videos

feature
 
 

### Pyrefly 1.0: A fast, forward-looking Python linter

 
By Serdar Yegulalp
Jun 3, 2026
6 mins

Development Tools
Programming Languages
Python

news
 
 

### Snowflake’s Horizon Context aims to give AI agents a common understanding of the business

 
By Anirban Ghoshal
Jun 2, 2026
6 mins

Artificial Intelligence
Data Governance
Data Management

news
 
 

### Workday launches Agent Passport to test and monitor AI agents in the enterprise

 
By Lynn Greiner
Jun 2, 2026
3 mins

Artificial Intelligence
Development Tools
Software Development

video
 
 

### A look at Mojo 1.0, a Python-like Rust contender

 
Jun 2, 2026
5 mins

Python

video
 
 

### The AI rewrite of Bun in Rust is making shock waves

 
May 26, 2026
4 mins

Python

video
 
 

### Why developers are so divided about using AI tools

 
May 19, 2026
6 mins

Python