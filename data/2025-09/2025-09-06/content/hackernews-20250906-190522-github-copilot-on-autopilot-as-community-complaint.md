---
title: GitHub Copilot on autopilot as community complaints persist • The Register
url: https://www.theregister.com/2025/09/05/github_copilot_complaints/
site_name: hackernews
fetched_at: '2025-09-06T19:05:22.673687'
original_url: https://www.theregister.com/2025/09/05/github_copilot_complaints/
author: latexr
date: '2025-09-06'
---

#### Devops

# Let us git rid of it, angry GitHub users say of forced Copilot features



## Unavoidable AI has developers looking for alternative code hosting options

Among the software developers who use Microsoft's GitHub, the most popular community discussion in the past 12 months has been a request for a way to block Copilot, the company's AI service, from generating issues and pull requests in code repositories.

The second most popular discussion – where popularity ismeasured in upvotes– is a bug report that seeks a fix for the inability of users to disable Copilot code reviews.

Both of these questions,the firstopened in May andthe secondopened a month ago, remain unanswered, despite an abundance of comments critical of generative AI and Copilot.

The author of the first, developer Andi McClure, publisheda similar requestto Microsoft's Visual Studio Code repository in January, objecting to the reappearance of a Copilot icon in VS Code after she had uninstalled the Copilot extension.

Microsoft and GitHub, not to mention rivals like Google, have gone all-in on a technology that a sizable or at least vocal portion of their customers simply don't want. And withbillions in capital expendituresto recoup, they're making it difficult to avoid.

During Microsoft's July 30, 2025 earnings call, CEO Satya NadellasaidGitHub Copilot continued to exhibit strong momentum and had reached 20 million users.

"GitHub Copilot Enterprise customers increased 75 percent quarter over quarter as companies tailor Copilot to their own codebases," said Nadella, noting that AI adoption has increased usage of GitHub over the past year.

I deeply resent that on top of Copilot seemingly training itself on my GitHub-posted code in violation of my licenses, GitHub wants me to look at (effectively) ads for this project I will never touch

"I've been for a while now filing issues in the GitHub Community feedback area when Copilot intrudes on my GitHub usage," McClure toldThe Registerin an email. "I deeply resent that on top of Copilot seemingly training itself on my GitHub-posted code in violation of my licenses, GitHub wants me to look at (effectively) ads for this project I will never touch. If something's bothering me, I don't see a reason to stay quiet about it. I think part of how we get pushed into things we collectively don't want is because we stay quiet about it."

It's not just the burden of responding to AI slop, anongoing issuefor Curl maintainer Daniel Stenberg. It's the permissionless copying andregurgitation of speculation as fact, mitigated only by small print disclaimers that generative AI may produce inaccurate results. It's also GitHub'sdisavowal of liabilityif Copilot code suggestions happen to have reproduced source code that requires attribution.

It's what the Servo project characterizes in itsban on AI code contributionsas the lack of code correctness guarantees, copyright issues, and ethical concerns. Similar objections have been used to justify AI code bans in GNOME'sLoupeproject,FreeBSD,Gentoo,NetBSD, andQEMU.

McClure said she has been filing requests to opt out of Copilot for a few years now, but in the last six months, her posts have been attracting more community support.

Two issues, about the abovementioned Copilot menu in VS Code and the inability to block Copilot-generated issues and pull requests, she said, have continued to attract comments.

"People keep finding these issues somehow and tacking on to them," McClure said. "Although Microsoft's been forcing the Copilot 'asks' into more and more places in the interface for a while, sometime this year they hit an inflection point where mass numbers of people don't feel like ignoring it anymore, where before they could shrug and ignore it or find the off switch."

In the past month, she said, there's been a second change in the way people see GitHub – GitHub'sdemotion from distinct subsidiary to part of Microsoft's CoreAI group.

* Bot shots: US Army enlists AI startup to provide target-tracking
* OpenAI eats jobs, then offers to help you find a new one at Walmart
* Boffins build automated Android bug hunting system
* Atlassian acquisition drives dream of AI-powered ChromeOS challenger

"Despite being a symbolic change, it seems to have galvanized the open source community from just complaining about Copilot to now actively moving away from GitHub," said McClure. "Many of my contacts in the open source community have been talking about plans to move from GitHub to Codeberg or a self-hosted Forgejo (Forgejo is the software used by Codeberg) over the last month, and the comments in those two always-busy GitHub threads have increasingly been people describing how Copilot is inspiring them to move to Codeberg as well."

Calls to shun Microsoft and GitHub go back a long way in the open source community, but moved beyond simmering dissatisfaction in 2022 when the Software Freedom Conservancy (SFC)urged free software supporterstogive up GitHub, a position SFC policy fellow Bradley M. Kuhnrecently reiterated.

Some of the developers participating in the issues raised by McClure and by others have said they intend to move away from GitHub over its stance on AI.

"Today I rejected two Copilot-generated code suggestions on my PR,"wrotea developer who posted to McClure's thread under the name Constantine. "This was very disturbing, so I started googling and found this discussion. I refuse using AI in the same way I don't take drugs or steal things - for me it's a matter of principle. So if this continues and Microsoft does not provide a way to opt out of AI for my repositories soon, I will move my code to a self-hosted solution and won't ever return to GitHub."

McClure said she has been slowly shifting toward Codeberg over the past few months. "I haven't been proactively moving repos but whenever I make a change to a repo I clone it to Codeberg, post the change there, and replace my main branch on the GitHub repo with a relocation notice," she said.

"Microsoft as a company has a running problem where they won't take no for an answer, whether with 'AI' or with any other product they want to ship," said McClure. "A favorite tactic of theirs recently is they will enable a thing by default and put an off switch, wait six months, and then slightly change or rename the feature you turned off, and create a new off switch you have to separately turn off. They did this with Bing in Windows 10 and now they're doing it with Copilot in their developer tools (and presumably Windows 11, I don't know, I don't use Windows 11)."

McClure said that when Microsoft began adding Copilot to everything, starting with Android keyboard SwiftKey, she concluded that the situation would reprise the handling of Bing/Cortana in Windows 10 and turning it off would not be enough.

If you really find Copilot unacceptable – and I do, Copilot is so much more noxious than Microsoft's previous forced bundlings – the only option is to stop using any Microsoft product that Copilot shows up in

"If you really find Copilot unacceptable – and I do, Copilot is so much more noxious than Microsoft's previous forced bundlings – the only option is to stop using any Microsoft product that Copilot shows up in," she said. "I stopped using SwiftKey; I started migrating from desktop Windows to Linux when it became clear mandatory AI surveillance would be a core part of Win11. GitHub and, more sporadically, Visual Studio Code I have had to keep using because they're monopolies in a way even Windows isn't. The network effects (projects whose sole method of communication is GitHub, software whose only IDE integration is a VSCode plugin) are too strong."

Things have progressed as expected, McClure said, with Copilot buttons appearing in VS Code even when Copilot has been uninstalled and poorly labeled buttons that redirect to Copilot searches. She suggests people are starting to tire of the situation and that if it continues, it will weaken the network effects that keep developers tied to GitHub, accelerating further migration.

"When this happens I have no idea if Microsoft will notice or care," said McClure. "The Copilot push at Microsoft appears to be completely top-down and the people at the top seem to have completely forgotten about conventional goals like customer retention. They want to pump up those 'AI' numbers, for whatever reason, and they view their customer base as just a resource to burn to get those metrics up."

GitHub did not respond to a request for comment. ®



Get our

Tech Resources

Share

#### More about

* AI
* GitHub
* Open Source

More like these

×

### More about

* AI
* GitHub
* Open Source
* Software

### Narrower topics

* AdBlock Plus
* AIOps
* App
* Application Delivery Controller
* Audacity
* Confluence
* Database
* DeepSeek
* Digital Public Goods
* FOSDEM
* FOSS
* Gemini
* Google AI
* GPT-3
* GPT-4
* Grab
* Graphics Interchange Format
* IDE
* Image compression
* Jenkins
* Large Language Model
* Legacy Technology
* LibreOffice
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* MySQL
* Neural Networks
* NLP
* OpenOffice
* OpenStack
* Programming Language
* Proxmox
* QR code
* Retrieval Augmented Generation
* Retro computing
* Search Engine
* Software bug
* Software License
* Star Wars
* Tensor Processing Unit
* Text Editor
* TOPS
* User interface
* Visual Studio
* Visual Studio Code
* WebAssembly
* Web Browser
* Wikipedia
* WordPress
* WPF

### Broader topics

* Git
* Self-driving Car

#### More about

Share

#### More about

* AI
* GitHub
* Open Source

More like these

×

### More about

* AI
* GitHub
* Open Source
* Software

### Narrower topics

* AdBlock Plus
* AIOps
* App
* Application Delivery Controller
* Audacity
* Confluence
* Database
* DeepSeek
* Digital Public Goods
* FOSDEM
* FOSS
* Gemini
* Google AI
* GPT-3
* GPT-4
* Grab
* Graphics Interchange Format
* IDE
* Image compression
* Jenkins
* Large Language Model
* Legacy Technology
* LibreOffice
* Machine Learning
* Map
* MCubed
* Microsoft 365
* Microsoft Office
* Microsoft Teams
* Mobile Device Management
* MySQL
* Neural Networks
* NLP
* OpenOffice
* OpenStack
* Programming Language
* Proxmox
* QR code
* Retrieval Augmented Generation
* Retro computing
* Search Engine
* Software bug
* Software License
* Star Wars
* Tensor Processing Unit
* Text Editor
* TOPS
* User interface
* Visual Studio
* Visual Studio Code
* WebAssembly
* Web Browser
* Wikipedia
* WordPress
* WPF

### Broader topics

* Git
* Self-driving Car

#### TIP US OFF

Send us news
