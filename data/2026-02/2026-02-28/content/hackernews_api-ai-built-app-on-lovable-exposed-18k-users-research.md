---
title: AI-built app on Lovable exposed 18K users, researcher claims • The Register
url: https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/
site_name: hackernews_api
content_file: hackernews_api-ai-built-app-on-lovable-exposed-18k-users-research
fetched_at: '2026-02-28T12:13:21.037214'
original_url: https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/
author: nottorp
date: '2026-02-28'
description: Vibe coded Lovable-hosted app littered with basic flaws exposed 18K users
tags:
- hackernews
- trending
---

#### Applications

# Lovable-hosted app littered with basic flaws exposed 18K users, researcher claims



## Who's to blame – the vibey platforms or the humans who ignore security warnings?

Vibe-coding platform Lovable has been accused of hosting apps riddled with vulnerabilities after saying users are responsible for addressing security issues flagged before publishing.

Taimur Khan, a tech entrepreneur with a background in software engineering, found 16 vulnerabilities – six of which he said were critical – in a single Lovable-hosted app that leaked more than 18,000 people's data.

He declined to name the app during the disclosure process, although it was hosted on Lovable's platform and showcased on its Discover page. The app had more than 100,000 views and around 400 upvotes at the time Khan began his probe.

The main issue, Khan said, was that all apps that are vibe-coded on Lovable's platform are shipped with their backends powered by Supabase, which handles authentication, file storage, and real-time updates through a PostgreSQL database connection.

However, when the developer – in this case AI – or the human project owner fails to explicitly implement crucial security features like Supabase's row-level security and role-based access, code will be generated that looks functional but in reality is flawed.

One example of this was a malformed authentication function. The AI thatvibe-codedthe Supabase backend, which uses remote procedure calls, implemented it with flawed access control logic, essentially blocking authenticated users and allowing access to unauthenticated users.

Khan said the intent was to block non-admins from accessing parts of the app, but the faulty implementation blocked all logged-in users – an error he said was repeated across multiple critical functions.

"This is backwards," said Khan. "The guard blocks the people it should allow and allows the people it should block. A classic logic inversion that a human security reviewer would catch in seconds – but an AI code generator, optimizing for 'code that works,' produced and deployed to production."

Because the app itself was a platform for creating exam questions and viewing grades, the userbase is naturally comprised of teachers and students. Some were from top US universities such as UC Berkeley and UC Davis, while there were "K-12 institutions with minors likely on the platform" as well, Khansaid.

With the security flaws in place, an unauthenticated attacker could trivially access every user record, send bulk emails through the platform, delete any user account, grade student test submissions, and access organizations' admin emails, for example.

Of the 18,697 total user records exposed, 14,928 contained unique email addresses. The dataset included 4,538 student accounts – all with email addresses – 10,505 enterprise users, and 870 users whose full PII was exposed.

The security flaws here are not exclusive to apps hosted by Lovable; the issue is broader and well-told by now.

Vibe coding, Collins Dictionary's Word of the Year for 2025, promised to break down software development's steep learning curve and empower any prompt jockey to bring their app ideas to life.

However, when AI isn'tgenerating slop bug reportsin pursuit of lucrative bug bounties orcatastrophically forgoing instructions, it can be found spewing glitzy-looking apps laden with vulnerabilities.

* Bcachefs creator insists his custom LLM is female and 'fully conscious'
* IBM stock dives after Anthropic points out AI can rewrite COBOL fast
* Amazon's vibe-coding tool Kiro reportedly vibed too hard and brought down AWS
* Agile Manifesto turns 25 – just in time for vibe coding to test it

Veracode, for instance,recently foundthat 45 percent of AI-generated code contained security flaws, not to mention the myriadtalesofwoereported byThe Registerin recent months.

Khan said he believes Lovable should take responsibility for the security of the apps it hosts, and was especially peeved when, after reporting his findings via company support, his ticket was reportedly closed without response.

"If Lovable is going to market itself as a platform that generates production-ready apps with authentication 'included,' it bears some responsibility for the security posture of the apps it generates and promotes," Khan said.

"You can't showcase an app to 100,000 people, host it on your own infrastructure, and then close the ticket when someone tells you it's leaking user data. At minimum, a basic security scan of showcased applications would have caught every critical finding in this report."

Lovable toldThe Registerthat the company has contacted the owner of the app in question and takes "any findings of this kind extremely seriously."

Regarding the closed ticket, Lovable CISO Igor Andriushchenko said that the company only received "a proper disclosure report" on the evening of February 26 and acted on the findings "within minutes."

"Any project built with Lovable includes a free security scan before publishing," Andriushchenko toldThe Register. "This scan checks for vulnerabilities and, if found, provides recommendations on actions to take to resolve before publishing.

"Ultimately, it is at the discretion of the user to implement these recommendations. In this case, that implementation did not happen.

"This project also includes code not generated by Lovable and the vulnerable database is not hosted by Lovable. We have been in contact with the creator of the app, who is now addressing the issue." ®



Get our

Tech Resources

Share

#### More about

* AI
* Cybersecurity
* Software

More like these

×

### More about

* AI
* Cybersecurity
* Software

### Narrower topics

* AdBlock Plus
* AIOps
* App
* Application Delivery Controller
* Audacity
* Center for Internet Security
* Confluence
* Database
* DeepSeek
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
* Neural Networks
* NLP
* OpenOffice
* Programming Language
* QR code
* Retrieval Augmented Generation
* Retro computing
* RSA Conference
* Search Engine
* Software Bill of Materials
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
* WordPress
* Zero trust

### Broader topics

* Security
* Self-driving Car

#### More about

Share

#### More about

* AI
* Cybersecurity
* Software

More like these

×

### More about

* AI
* Cybersecurity
* Software

### Narrower topics

* AdBlock Plus
* AIOps
* App
* Application Delivery Controller
* Audacity
* Center for Internet Security
* Confluence
* Database
* DeepSeek
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
* Neural Networks
* NLP
* OpenOffice
* Programming Language
* QR code
* Retrieval Augmented Generation
* Retro computing
* RSA Conference
* Search Engine
* Software Bill of Materials
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
* WordPress
* Zero trust

### Broader topics

* Security
* Self-driving Car

#### TIP US OFF

Send us news
