---
title: Zig quits GitHub, gripes about Microsoft's AI obsession • The Register
url: https://www.theregister.com/2025/12/02/zig_quits_github_microsoft_ai_obsession/
site_name: hackernews_api
fetched_at: '2025-12-04T11:08:06.835133'
original_url: https://www.theregister.com/2025/12/02/zig_quits_github_microsoft_ai_obsession/
author: Brajeshwar
date: '2025-12-03'
description: Zig quits GitHub, says Microsoft's AI obsession has ruined the service
tags:
- hackernews
- trending
---

#### Devops

# Zig quits GitHub, says Microsoft's AI obsession has ruined the service



## Zig prez complains about 'vibe-scheduling' after safe sleep bug goes unaddressed for eons

The Foundation that promotes the Zig programming language has quit GitHub due to what its leadership perceives as the code sharing site's decline.

The drama began in April 2025 when GitHub user AlekseiNikiforovIBM started athreadtitled “safe_sleep.sh rarely hangs indefinitely.” GitHub addressed the problem in August, but didn’t reveal that in the thread, which remained open until Monday.

The code uses 100 percent CPU all the time, and will run forever

That timing appears notable. Last week, Andrew Kelly, president and lead developer of the Zig Software Foundation,announcedthat the Zig project is moving to Codeberg, a non-profit git hosting service, because GitHub no longer demonstrates commitment to engineering excellence.

One piece of evidence he offered for that assessment was the “safe_sleep.sh rarely hangs indefinitely” thread.

"Most importantly, Actions hasinexcusable bugswhile beingcompletely neglected," Kelly wrote. "After theCEO of GitHub said to 'embrace AI or get out', it seems the lackeys at Microsoft took the hint, because GitHub Actions started 'vibe-scheduling' – choosing jobs to run seemingly at random. Combined with other bugs and inability to manually intervene, this causes our CI system to get so backed up that not even master branch commits get checked."

### Older and deeper

Kelly’s gripe seems justified, as the bug discussed in the thread appears to have popped up followinga code changein February 2022 that users flagged in prior bug reports.

The code change replaced instances of the posix "sleep" command with a "safe_sleep" script that failed to work as advertised. It was supposed to allow the GitHub Actions runner – the application that runs a job from a GitHub Actions workflow – to pause execution safely.

"The bug in this 'safe sleep' script is obvious from looking at it: if the process is not scheduled for the one-second interval in which the loop would return (due to $SECONDS having the correct value), then it simply spins forever," wrote Zig core developer Matthew Lugg ina commentappended to the April bug thread.

"That can easily happen on a CI machine under extreme load. When this happens, it's pretty bad: it completely breaks a runner until manual intervention. On Zig's CI runner machines, we observed multiple of these processes which had been running for hundreds of hours, silently taking down two runner services for weeks."

The fix wasmergedon August 20, 2025, from a separate issue opened back in February 2024. The related bug report from April 2025 remained openuntil Monday, December 1, 2025. A separate CPU usage bugremains unresolved.

* Microsoft appears to move on from its most loyal 'customers' – Contoso and Fabrikam
* UK gov blames budget leak on misconfigured WordPress plugin, server
* Google Antigravity vibe-codes user's entire drive out of existence
* OpenAI cuts off Mixpanel after analytics leak exposes API users

Jeremy Howard, co-founder of Answer.AI and Fast.AI, said in a series of social mediapoststhat users’ claims about GitHub Actions being in a poor state of repair appear to be justified.

"The bug,"he wrote, "was implemented in a way that, very obviously to nearly anyone at first glance, uses 100 percent CPU all the time, and will run forever unless the task happens to check the time during the correct second."

I can't see how such an extraordinary collection of outright face-palming events could be made

Headdedthat the platform-independent fix for the CPU issue proposed last February lingered for a year without review and wasclosedby the GitHub bot in March 2025 before being revived and merged.

"Whilst one could say that this is just one isolated incident, I can't see how such an extraordinary collection of outright face-palming events could be made in any reasonably functioning organization," Howardconcluded.

GitHub did not immediately respond to a request for comment.

While Kelly has gone on toapologizefor the incendiary nature of his post, Zig is not the only software project publicly parting ways with GitHub.

Over the weekend, Rodrigo Arias Mallo, creator of the Dillo browser project,saidhe's planning to move away from GitHub owing to concerns about over-reliance on JavaScript, GitHub's ability to deny service, declining usability, inadequate moderation tools, and "over-focusing on LLMs and generative AI, which are destroying the open web (or what remains of it) amongother problems."

Codeberg, for its part, has doubled its supporting membership since January, going frommore than 600 memberstoover 1,200as of last week.

GitHub has not disclosed how many of its users pay for its services presently. The code hosting biz had "over 1.3 million paid GitHub Copilot subscribers, up 30 percent quarter-over-quarter," Microsoft CEO Satya Nadella said on the company'sQ2 2024 earnings call.

In Q4 2024, when GitHub reportedan annual revenue run rate of $2 billion, GitHub Copilot subscriptions accounted for about 40 percent of the company's annual revenue growth.

Nadella offered a different figure during Microsoft'sQ3 2025 earnings call: "we now have over 15 million GitHub Copilot users, up over 4X year-over-year." It's not clear how many GitHub users pay for Copilot, or for runner scripts that burned CPU cycles when they should have been sleeping. ®



Get our

Tech Resources

Share

#### More about

* AI
* Developer
* GitHub

More like these

×

### More about

* AI
* Developer
* GitHub
* Microsoft
* Software

### Narrower topics

* Active Directory
* AdBlock Plus
* AIOps
* API
* App
* Application Delivery Controller
* Audacity
* Azure
* Bing
* BSoD
* Confluence
* Database
* DeepSeek
* Excel
* Exchange Server
* FOSDEM
* FOSS
* Gemini
* Google AI
* GPT-3
* GPT-4
* Grab
* Graphics Interchange Format
* HoloLens
* IDE
* Image compression
* Internet Explorer
* Jenkins
* Large Language Model
* Legacy Technology
* LibreOffice
* LinkedIn
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Build
* Microsoft Edge
* Microsoft Fabric
* Microsoft Ignite
* Microsoft Office
* Microsoft Surface
* Microsoft Teams
* Mobile Device Management
* .NET
* Neural Networks
* NLP
* Office 365
* OpenOffice
* OS/2
* Outlook
* Patch Tuesday
* Pluton
* Programming Language
* QR code
* Retrieval Augmented Generation
* Retro computing
* Search Engine
* SharePoint
* Skype
* Software bug
* Software License
* SQL Server
* Star Wars
* Tensor Processing Unit
* Text Editor
* TOPS
* User interface
* Visual Studio
* Visual Studio Code
* WebAssembly
* Web Browser
* Windows
* Windows 10
* Windows 11
* Windows 7
* Windows 8
* Windows Server
* Windows Server 2003
* Windows Server 2008
* Windows Server 2012
* Windows Server 2013
* Windows Server 2016
* Windows Subsystem for Linux
* Windows XP
* WordPress
* Xbox
* Xbox 360

### Broader topics

* Bill Gates
* Git
* Self-driving Car

#### More about

Share

#### More about

* AI
* Developer
* GitHub

More like these

×

### More about

* AI
* Developer
* GitHub
* Microsoft
* Software

### Narrower topics

* Active Directory
* AdBlock Plus
* AIOps
* API
* App
* Application Delivery Controller
* Audacity
* Azure
* Bing
* BSoD
* Confluence
* Database
* DeepSeek
* Excel
* Exchange Server
* FOSDEM
* FOSS
* Gemini
* Google AI
* GPT-3
* GPT-4
* Grab
* Graphics Interchange Format
* HoloLens
* IDE
* Image compression
* Internet Explorer
* Jenkins
* Large Language Model
* Legacy Technology
* LibreOffice
* LinkedIn
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Build
* Microsoft Edge
* Microsoft Fabric
* Microsoft Ignite
* Microsoft Office
* Microsoft Surface
* Microsoft Teams
* Mobile Device Management
* .NET
* Neural Networks
* NLP
* Office 365
* OpenOffice
* OS/2
* Outlook
* Patch Tuesday
* Pluton
* Programming Language
* QR code
* Retrieval Augmented Generation
* Retro computing
* Search Engine
* SharePoint
* Skype
* Software bug
* Software License
* SQL Server
* Star Wars
* Tensor Processing Unit
* Text Editor
* TOPS
* User interface
* Visual Studio
* Visual Studio Code
* WebAssembly
* Web Browser
* Windows
* Windows 10
* Windows 11
* Windows 7
* Windows 8
* Windows Server
* Windows Server 2003
* Windows Server 2008
* Windows Server 2012
* Windows Server 2013
* Windows Server 2016
* Windows Subsystem for Linux
* Windows XP
* WordPress
* Xbox
* Xbox 360

### Broader topics

* Bill Gates
* Git
* Self-driving Car

#### TIP US OFF

Send us news
