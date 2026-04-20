---
title: 'The Eternal Promise: A History of Attempts to Eliminate Programmers'
url: https://www.ivanturkovic.com/2026/01/22/history-software-simplification-cobol-ai-hype/
site_name: hnrss
content_file: hnrss-the-eternal-promise-a-history-of-attempts-to-elimi
fetched_at: '2026-02-28T19:08:40.657162'
original_url: https://www.ivanturkovic.com/2026/01/22/history-software-simplification-cobol-ai-hype/
author: ivan.turkovic
date: '2026-02-25'
published_date: '2026-01-22T11:46:43+00:00'
description: From COBOL in the 1960s to AI in the 2020s, every generation promises to eliminate programmers. Explore the recurring cycles of software simplification hype.
tags:
- hackernews
- hnrss
---

When I look back at the history of software, one pattern emerges with remarkable consistency: the promise to simplify software creation, to make it cheaper, and ultimately to eliminate the need for programmers altogether. This is not a new idea. It has been the driving ambition of our industry since the 1960s. And while each generation believes they are witnessing something unprecedented, they are actually participating in a cycle that has repeated itself for over six decades.

Today, as large language models generate code and AI assistants pair-program with developers, we hear familiar refrains: programming as we know it is ending, software development will be democratized, and soon anyone will be able to build complex systems without writing a single line of code. These claims deserve scrutiny, not because they are entirely wrong, but because they echo promises made in 1959, in 1973, in 1985, and in 2015. Understanding this history is essential for anyone trying to make sense of where we actually are and where we might be going.

## The Original Sin: COBOL and the Business User Dream

The story begins in the late 1950s, when programming was genuinely arcane. Programmers wrote in assembly language or machine code, manipulating registers and memory addresses directly. The work required deep technical knowledge and was painfully slow. Businesses needed software, but the people who understood business problems rarely understood computers, and the people who understood computers rarely understood business problems.

Enter Grace Hopper and the CODASYL committee. In 1959, they created COBOL, the Common Business-Oriented Language. The explicit goal was revolutionary: create a programming language so close to English that business managers could read it, understand it, and eventually write it themselves. The syntax was deliberately verbose. Instead of cryptic symbols, COBOL used words like MOVE, ADD, MULTIPLY, and PERFORM. A program read almost like a bureaucratic memo.

The marketing was clear: COBOL would eliminate the bottleneck of specialized programmers. Business analysts would write their own programs. The priesthood of technical experts would be disbanded. Software creation would be democratized.

It did not work out that way.

COBOL succeeded spectacularly as a programming language. It became the backbone of banking, insurance, and government systems worldwide. Billions of lines of COBOL code still run today, processing trillions of dollars in transactions. But COBOL did not eliminate programmers. Instead, it created a new profession of COBOL programmers. The language was readable, but writing correct, efficient, maintainable COBOL still required specialized skills, deep understanding of the underlying systems, and years of experience.

The irony is profound. A language created to eliminate the need for programmers became one of the most enduring job creators in the history of computing. Today, COBOL programmers are in high demand precisely because so few people learned the language, and the systems they maintain are too critical to replace.

## The First AI Winter: Expert Systems and the 1970s Hype Cycle

Most people discussing AI today seem unaware that we have been here before. The 1960s and early 1970s saw an explosion of optimism about artificial intelligence that makes current predictions seem modest by comparison.

In 1965, Herbert Simon, one of the founders of AI research, predicted that within twenty years, machines would be capable of doing any work a man can do. In 1967, Marvin Minsky, another AI pioneer, predicted that within a generation, the problem of creating artificial intelligence would be substantially solved. The funding poured in. Government agencies, particularly DARPA in the United States, invested heavily in AI research.

The implications for software development were considered revolutionary. If machines could think, surely they could program themselves. Researchers worked on automatic programming, systems that would translate natural language specifications into working code. Expert systems promised to capture human expertise in rule-based engines that could make decisions and solve problems without human intervention.

The vision was compelling. Describe what you want in plain English, and the computer would figure out how to do it. Programming would become specification, and specification would become conversation.

By the mid-1970s, reality had intervened. The Lighthill Report of 1973 devastated AI funding in the United Kingdom by systematically exposing the gap between AI promises and AI achievements. The report noted that early successes in narrow domains had created unrealistic expectations. Systems that worked in toy problems failed in real-world complexity. The combinatorial explosion of possibilities overwhelmed the computational resources of the time.

What followed was the first AI winter. Funding collapsed. Research programs were canceled. The phrase artificial intelligence became an embarrassment in some circles. Researchers rebranded their work as expert systems, knowledge engineering, or computational intelligence to distance themselves from the discredited hype.

The lesson should have been clear: translating human intent into working software is fundamentally difficult. The gap between natural language specification and correct implementation is not a technical problem to be solved but a conceptual challenge that reflects deep truths about human communication and software complexity.

## Fourth-Generation Languages: The 1980s Promise

By the early 1980s, a new hope emerged: fourth-generation languages, or 4GLs. The reasoning was seductive. Assembly language was first generation. FORTRAN and COBOL were second generation. Structured languages like Pascal and C were third generation. The fourth generation would abstract away even more complexity, allowing non-programmers to create applications through high-level declarations rather than procedural code.

Products like FOCUS, NOMAD, Ramis, and later PowerBuilder and Microsoft Access promised to revolutionize software development. Instead of writing code, users would define data structures, specify business rules, and design screens through graphical interfaces. The underlying code would be generated automatically.

The marketing materials were remarkably similar to what we hear about no-code platforms today. End users would build their own applications. IT departments would become enablers rather than bottlenecks. Development time would be reduced by factors of ten or more.

4GLs achieved genuine success in certain domains. Report generation, simple database applications, and departmental tools were built faster with these technologies. Microsoft Access, in particular, empowered millions of users to create functional applications without traditional programming.

But the fundamental promise once again went unfulfilled. Complex applications still required complex thinking. When business logic became intricate, when performance mattered, when systems needed to integrate with other systems, 4GLs revealed their limitations. Generated code was often inefficient. Customization was difficult. And the most sophisticated users of 4GLs were not business analysts but specialized developers who understood both the tools and the underlying principles.

The pattern repeated: tools that promised to eliminate programmers instead created new categories of programming work.

## CASE Tools and the Cathedral Builders

The late 1980s and early 1990s saw the rise of Computer-Aided Software Engineering, or CASE tools. The vision was comprehensive: model your entire system using diagrams and specifications, and the tools would generate complete, working applications.

Companies invested millions in CASE tool suites. Conferences were held. Methodologies were developed. The promise was that software engineering would finally become real engineering, with predictable outcomes, repeatable processes, and automatic generation of code from specifications.

I remember this era vividly. Consultants would arrive with massive data dictionaries and entity-relationship diagrams. Projects would spend months in the modeling phase, producing elaborate documentation that was supposed to capture every requirement and design decision. The code generation phase would then transform these models into working systems.

The reality was disappointing. Generated code was often bloated and inefficient. The models were difficult to maintain as requirements changed. And the fundamental problem remained: getting the specification right was at least as hard as writing the code directly. The diagrams and models were just another programming language, one that happened to use boxes and arrows instead of text.

By the mid-1990s, CASE tools had largely faded from prominence. Some concepts survived in object-oriented analysis and design tools like Rational Rose, but the grand vision of automatic code generation from specifications had proven illusory.

## The Second AI Wave: Expert Systems Redux

The 1980s also saw a second wave of AI enthusiasm, focused on expert systems. Companies like Inference Corporation, Intellicorp, and Teknowledge promised to capture human expertise in rule-based systems that could make decisions as well as human experts.

The applications were compelling: medical diagnosis, financial analysis, equipment configuration, and yes, automatic programming. Systems like R1/XCON at Digital Equipment Corporation achieved genuine success, saving the company millions by automatically configuring computer systems.

The Japanese Fifth Generation Computer Project, launched in 1982 with massive government investment, aimed to create computers that could reason using logic programming. The explicit goal was to leapfrog Western technology and create machines capable of natural language understanding, automatic programming, and artificial intelligence.

By 1990, the Fifth Generation Project had largely failed to achieve its goals. Expert systems proved brittle, failing in unexpected ways when confronted with situations outside their narrow expertise. Maintaining the rule bases became increasingly difficult as systems grew. And the fundamental challenge of knowledge acquisition, getting human experts to articulate their expertise in a form machines could use, proved far harder than anticipated.

The second AI winter arrived in the early 1990s. Again, funding collapsed. Again, researchers rebranded their work. Again, the fundamental promise of machines that could program themselves receded into the future.

## The Internet Era: Web Development and the Democratization Dream

The mid-1990s brought the World Wide Web, and with it a new hope for simplified software creation. HTML was supposed to be so simple that anyone could build web pages. And indeed, millions learned to create basic websites with nothing more than a text editor and some determination.

But the web quickly became more complex. JavaScript added interactivity. CSS added styling. Server-side programming became essential. Databases backed the content. Security became critical. Performance became competitive.

The response was predictable: new tools promising to simplify web development. Dreamweaver, FrontPage, and later WordPress and Wix promised that anyone could build professional websites without coding. Content management systems abstracted away the complexity.

These tools succeeded in making basic web presence accessible to non-developers. But professional web development became more complex, not simpler. The rise of single-page applications, mobile-first design, progressive web apps, and the modern JavaScript ecosystem created new layers of complexity that required new categories of specialists.

The pattern continued: tools that simplified basic tasks enabled more ambitious projects, which required more sophisticated skills, which created demand for more specialized developers.

## Model-Driven Architecture and the UML Dream

The early 2000s saw another attempt at automatic code generation through Model-Driven Architecture, or MDA. The Object Management Group proposed that platform-independent models could be transformed into platform-specific implementations through automated tooling.

The Unified Modeling Language (UML) became the standard notation. Tools like Rational Rose, Together, and Enterprise Architect promised to generate complete applications from UML diagrams. The vision was familiar: model your system at a high level of abstraction, and let the tools handle the implementation details.

MDA achieved some success in specialized domains, particularly where the mapping from models to code was well-understood and the generated code did not need extensive customization. But for most applications, the approach proved cumbersome. Maintaining synchronization between models and code was difficult. The models themselves became complex, requiring specialized skills to create and maintain.

By the 2010s, MDA had faded from mainstream practice, though its concepts influenced modern code generation and domain-specific languages.

## The No-Code and Low-Code Renaissance

Starting around 2015, a new generation of no-code and low-code platforms emerged. Names like Bubble, Webflow, Airtable, Zapier, and Microsoft Power Platform promised to enable citizen developers to build applications through visual interfaces and drag-and-drop components.

The marketing echoed the promises of every previous generation. Business users would build their own applications. IT backlogs would disappear. Digital transformation would accelerate. Programmers would become obsolete, or at least far less necessary.

No-code tools have achieved genuine success in their domains. Simple applications, workflow automation, basic websites, and internal tools can be built faster with these platforms than with traditional development. For certain categories of problems, they represent a genuine advancement.

But the pattern holds. Complex applications still require complex thinking. When requirements exceed the platforms’ capabilities, users hit walls. Integration with existing systems is often difficult. Performance at scale is challenging. And the most sophisticated users of no-code platforms are often former developers who understand the underlying principles.

More importantly, no-code has not reduced the demand for traditional developers. If anything, the explosion of digital applications has increased demand. The market for software developers continues to grow, even as no-code platforms proliferate.

## Large Language Models: The Current Wave

Which brings us to the present moment. Large language models like GPT-4, Claude, and Gemini can generate functional code from natural language descriptions. GitHub Copilot and similar tools assist developers in real-time, suggesting completions and generating boilerplate. The improvements are genuine and impressive.

The predictions are predictably bold. Programming jobs will be eliminated. Software development will be democratized. Anyone will be able to build complex systems by describing what they want in plain English.

We have heard this before. In 1959, with COBOL. In 1973, with expert systems. In 1985, with 4GLs. In 1995, with CASE tools. In 2015, with no-code.

This does not mean the current wave is identical to previous waves. Large language models represent a genuine capability breakthrough. They can perform tasks that previous technologies could not. The code they generate is often correct and useful. The productivity improvements for skilled developers are real.

But the fundamental challenge remains unchanged: translating human intent into correct, efficient, maintainable, secure software is hard. Not because the tools are inadequate, but because the problem is inherently complex.

## Why the Promise Always Falls Short

Understanding why each wave of simplification tools falls short of its promises requires examining the nature of software development itself.

Software is not just code. It is a precise specification of behavior under all possible conditions. When you say you want a simple e-commerce application, you are implicitly specifying thousands of decisions about user authentication, payment processing, inventory management, shipping calculations, tax handling, error recovery, accessibility, performance under load, and security against attacks. Most of these decisions are not obvious from a high-level description.

The hard part of software development has never been typing code. It has always been figuring out exactly what the software should do, and ensuring it actually does that under all circumstances. This is why specification languages and automatic code generation repeatedly fail to eliminate programmers: they simply move the complexity from code to specification, and specification is at least as difficult.

Furthermore, software exists in an ecosystem. It must integrate with other software, adapt to changing requirements, run on evolving platforms, and serve users whose needs constantly shift. Maintaining and evolving software over time requires understanding that transcends any specification language or generation tool.

Finally, software reflects human decisions about tradeoffs. Performance versus maintainability. Security versus usability. Flexibility versus simplicity. These decisions require judgment that cannot be automated because they depend on context, priorities, and values that differ across situations.

## What Actually Changes

Each wave of simplification tools does change something real, just not what the marketers promise.

COBOL did not eliminate programmers, but it did make business programming more accessible and created an enormous industry. 4GLs did not replace traditional languages, but they did enable rapid development of certain categories of applications. No-code platforms do not make developers obsolete, but they do empower non-developers to create useful tools.

The pattern is consistent: new tools lower the barrier to entry for simple tasks, which increases the total amount of software being created, which creates demand for more sophisticated software, which creates demand for more sophisticated developers.

This is not a failure. It is how technology evolves. Each abstraction layer enables new capabilities. Each simplification enables new ambitions. The overall effect is positive, even if the specific predictions prove wrong.

## Learning from History

What should we take from this history as we navigate the current wave of AI-powered development tools?

First, skepticism about extreme predictions is warranted. Claims that programming will be eliminated within a few years echo claims made in every previous decade. The pattern suggests that such predictions consistently overestimate the pace of change and underestimate the complexity of the challenge.

Second, genuine improvements are real. Large language models do provide productivity gains for developers. They do make certain tasks easier. Dismissing these improvements because previous hype cycles failed would be as mistaken as accepting the most extreme predictions uncritically.

Third, the nature of programming work will continue to evolve. Just as COBOL programmers do different work than assembly language programmers, and web developers do different work than COBOL programmers, future developers will do different work than current developers. The work will change, but it will not disappear.

Fourth, human skills remain essential. Understanding requirements, making design decisions, debugging unexpected behaviors, maintaining systems over time, and communicating with stakeholders are skills that every wave of automation has failed to replace. These skills may become more important, not less, as tools handle more of the routine work.

Fifth, the developers who thrive will be those who learn to use new tools effectively while maintaining deep understanding of underlying principles. Tools come and go, but fundamental knowledge about algorithms, data structures, system design, and software architecture remains valuable across generations.

## The Enduring Value of Understanding

Perhaps the most important lesson from six decades of promised simplification is this: there is no substitute for understanding.

Every successful use of COBOL required understanding of business processes and data management. Every successful use of 4GLs required understanding of databases and application architecture. Every successful use of no-code platforms requires understanding of workflow design and system integration. And every successful use of AI code generation requires understanding of software principles, code quality, and system design.

The tools change. The languages change. The platforms change. But the need for people who deeply understand what they are building, and why, remains constant.

This is not a bug in the system. It reflects something fundamental about the nature of software and the nature of problem-solving. Software is crystallized thought. Creating good software requires good thinking. No tool can substitute for that.

## Looking Forward with Clear Eyes

As we look to the future, the history of software simplification offers a valuable perspective. We should expect AI tools to become more capable. We should expect new promises of revolutionary change. We should expect some of those promises to be fulfilled in unexpected ways, and others to fall short of the hype.

Most importantly, we should expect the fundamental challenge to remain: building software that does what people actually need, reliably, efficiently, and securely, in a world where requirements constantly change and systems must work together in complex ways.

That challenge has never been primarily about the difficulty of typing code. It has always been about the difficulty of thinking clearly, communicating precisely, and making good decisions under uncertainty. Those are human skills, and they will remain valuable for as long as software matters.

The programmers of the future may write less code directly. They may work at higher levels of abstraction. They may use tools we cannot currently imagine. But they will still be doing the essential work of translating human intent into software that works. And that work will continue to require skill, judgment, and understanding that no tool has yet replaced.

History suggests that reports of programming’s death have been greatly exaggerated, repeatedly, for over sixty years. There is no reason to believe this time is fundamentally different. There is every reason to believe that those who invest in deep understanding will continue to be valuable, regardless of what tools emerge.

### Final Thoughts

If you found this perspective valuable, I encourage you to follow my work. I write regularly about the intersection of software engineering, technology history, and the evolving role of AI in our industry. My goal is always to cut through the hype and offer calm, analytical perspectives grounded in real experience.

You can find me onLinkedInwhere I share shorter insights and engage with the broader technology community. For longer explorations like this one, this blog remains my primary home.

I would love to hear your thoughts on this topic. Have you lived through any of these hype cycles? Do you see patterns in your own experience that echo this history? What do you think makes the current AI wave different, or similar, to what came before?

Leave a comment below, reach out via the contact page, or connect with me on social media. The best insights often come from the community, from people who are building, leading, and thinking about these questions every day.

Until next time, keep building wisely.
