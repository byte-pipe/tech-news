---
title: AIR raises $50M to help companies vet the skills and add-ons AI agents use | TechCrunch
url: https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/
site_name: newsfeed
content_file: newsfeed-air-raises-50m-to-help-companies-vet-the-skills-an
fetched_at: '2026-09-01T21:38:05.735418'
original_url: https://techcrunch.com/2026/09/01/air-raises-50m-to-help-companies-vet-the-skills-and-add-ons-ai-agents-use/
author: Ram Iyer
date: '2026-09-01'
published_date: '2026-09-01T15:45:51+00:00'
description: AIR's platform can discover agents running at a company, continuously vets any skills and add-ons they use, and blocks any unwanted behavior.
tags:
- techcrunch
- ai
- security
- startups
---

As companies start giving AI agents access to an increasing portion of their systems, a nascent software supply chain seems to be forming around the new tooling AI agents are using: skills, plug-ins, MCP servers, and add-ons that let them interact with the internet.

AI security startupAIRbelieves companies will need a way to monitor that supply chain, and it’s now coming out of stealth with $50 million raised across two seed rounds to build that product.

Founded by Yair Saban (CEO) and Niv Hoffman (CTO), veterans of Israel’s Unit 8200 intelligence corps, where they worked on offensive cybersecurity, AIR offers a platform that can discover agents running inside companies, continuously vet any skills, tools, and components those agents use, and block them from interacting with software or external sources that don’t pass security criteria. It also offers a marketplace of vetted add-ons and skills for AI agents.

The funding rounds closed within weeks of each other, Saban told TechCrunch, with the first round raising $10 million, and the second $40 million. Sequoia led the first round, while Greenoaks led the second, Saban said. Swish, Netz, and Zach Frankel (president of Cognition), Yinon Costica (co-founder of Wiz), Ofir Ehrlich (co-founder of Eon), Anne Neuberger, Omer Adam, Varun Anand (co-founder of Clay), and other angel investors also participated.

AIR’s pitch goes thusly: The way AI agents are used wholesale at companies is beginning to resemble operating systems, but the tools they use, or the software they can install, aren’t yet being given the kind of oversight we give to drivers or applications.

“In the early 2000s, whenever you installed a driver, the driver didn’t need to be signed. Today, every time you install a driver, you see a signature saying who signed it, because the driver is actually loading code into the kernel,” Saban said. “You don’t have that with skills or plug-ins or MCPs, and it’s a shame, because it’s the same mechanism, it’s the same lesson, but we haven’t learned it.”

The big risk, he argues, is that as AI agents start working more autonomously across databases and enterprise systems, and connecting to the internet, attackers can poison the content an AI agent consumes instead of attacking it directly.

The startup says it can solve that with a visibility product that finds agents active across a company’s environment, as well as identifies employees who use AI tools unapproved by IT departments or those who use personal accounts. Then, it uses an enforcement layer that hooks into agents to intercept and analyze actions, like loading a skill or fetching content from the internet. Lastly, AIR also checks the tools, add-ons, or software an agent wants to use against a whitelist the startup maintains.

Saban says the startup maintains this whitelist by evaluating skills and add-ons openly available on the internet for changes and malicious behavior, as a previously approved skill could become risky if a package it downloads changes, or its developer’s account is compromised. He added that AIR’s platform currently filters out about 27% of the add-ons and skills it finds online.

AIR claims it has more than 20 customers, and Saban said roughly a quarter of these are large enterprises. He said the company has so far seen the strongest demand in heavily regulated industries, particularly financial services and pharmaceutical companies.

However, AIR is hardly alone in this space.Noma Securityoffers discovery, access controls, and runtime monitoring for agents, MCP servers, and skills, whileZenitysells security and governance tools that work similarly.Astrix Security‘s identity platform also lets companies discover and control agents and MCP servers, andOperant AIoffers agent protections as well as an MCP gateway.

There is significant venture money chasing the category, too. Zenity raised a $125 million Series C in August, while Noma raised a $100 million Series B last year.

Saban thinks AIR’s moat lies in its ability to continuously vet the skills and add-ons ecosystem growing around AI agents. “Continuously vetting skills and plug-in websites, this is a hard mission to do. Gaining visibility over the endpoint, that is easy. Everybody’s going to do it. It’s hard to create a moat around that,” he said.

And while the CEO acknowledged that AI labs and providers will eventually build in security checks and policies to filter out malicious skill and tool usage, he thinks companies will still want to buy an independent product that works across vendors.

“This is not a scanning problem, it is a continuous re-verification problem,” Bogomil Balkansky, partner at Sequoia, told TechCrunch in an emailed statement. “Inspecting every skill, plugin, MCP server and sub-agent an enterprise’s agents touch, re-inspecting each one every time it changes, in real time and across an entire company’s agent fleet, is an infrastructure problem long before it is a security problem. Air has spent the last year building that pipeline. You do not catch up to it by writing a better scanner.”

AIR currently has around 40 employees. Saban said the new capital will primarily go toward hiring researchers and expanding the company’s go-to-market efforts in the U.S. and Europe.

Topics

AI
, 
AI agents
, 
ai security
, 
Greenoaks Capital
, 
Security
, 
Sequoia Capital
, 
Startups
 

When you purchase through links in our articles,we may earn a small commission. This doesn’t affect our editorial independence.

			Ram Iyer	

Editor

Ram is a financial and tech reporter and editor. He covered North American and European M&A, equity, regulatory news and debt markets at Reuters and Acuris Global, and has also written about travel, tourism, entertainment and books.

You can contact or verify outreach from Ram by emailingram.iyer@techcrunch.com.

 

View Bio