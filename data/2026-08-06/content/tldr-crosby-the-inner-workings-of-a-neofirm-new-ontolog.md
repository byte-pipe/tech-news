---
title: 'Crosby: The Inner Workings of a Neofirm — New Ontologies'
url: https://www.new-ontologies.com/posts/Crosby/
site_name: tldr
content_file: tldr-crosby-the-inner-workings-of-a-neofirm-new-ontolog
fetched_at: '2026-08-06T12:55:17.103892'
original_url: https://www.new-ontologies.com/posts/Crosby/
date: '2026-08-06'
description: Selling outputs instead of hours
tags:
- tldr
---

John Sarihan (left) and Ryan Daniels (right), CTO and CEO of Crosby

If you think law is a matter of binary right and wrong answers, you haven’t spent enough time with great lawyers. Law, as I came to see in my two weeks immersed withCrosby, is not an airless sect of transcendent values. It is an arena of taste and judgment.

As an outsider to the legal world, shadowing at Crosby meant learning an entirely new vocabulary. I perched in a corner of the company’s largest conference room, packed and uncommonly quiet. The “time trials” were about to begin: Crosby’s internal contests where lawyers race to redline a contract against the clock.

Two lawyers sat facing each other, close as chess players over a board, and started redlining. Looking over one lawyer’s shoulder, I watched him accept the AI’s redlines with a tap, then slow over a single clause. He deleted an “or” and typed “and.” It looked like eye-watering work.

He finished the Non Disclosure Agreement in four minutes and fifty-three seconds with the help of an internal AI redlining harness. Everyone clapped.Was this fast?I wasn’t sure, so I slacked a team member across the room. Turns out, the same document would usually take a human lawyer with no technology around 58 min to complete.

That day the productivity lift was 10x, though in a sterile environment: a known sample, one contract type. The figure was impressive, but it spurred many questions. What would this look like in the wild? Would lawyers really trust its outputs?

Ross and Bijan, two of the lawyers at Crosby, discussing a complicated contract

Crosby is an AI native law firm. They call it a neofirm: equal parts lawyers from elite law firms like Kirkland and Ellis and Wachtell, and engineers from top startups like Ramp and Stripe. They employ lawyers, own liability, and take on the work end to end. The two sides of the firm are represented by the two founders: Ryan Daniels, a Stanford-educated attorney, and John Sarihan, one of the earliest software engineers at Ramp. They’ve raised $85M from Sequoia, Lux, Index, Elad Gil, BCV, and serve customers like Ramp, Cognition, Cursor, and Clay.

They take on commercial contracts, the likes of Non Disclosure Agreements (NDAs), Master Services Agreements (MSAs) and more moving up the complexity curve. These contracts are the basic units of doing business, often bottlenecked by speed to agreement.

I spent over two weeks sitting in their All Hands, product brainstorming sessions, engineering meetings, and even shadowed lawyers. Here’s what I wanted to find out: What gives Crosby a structural advantage over other law firms with pedigreed names and stature? Why would clients trust an AI-native law firm? What happens to the role of the lawyer?

The market is far from being wide open. The foundation models threaten to erode the legal application layer entirely, and legacy firms like Kirkland & Ellis, one of the premier big law firms, are spending$500Mbuilding internal technology. Crosby is a hybrid team of engineers and lawyers trying to capture the upside of AI automation, while at heart, distilling and amplifying the human relational value lawyers serve as trusted advisors.

In every field study, I enter not knowing what I will witness. I think of the great biographer Robert Caro asking the question “What did you see?” again and again until the shape of a story emerges.

Over 25 conversations later, the story that formed in my mind was bigger than just one company. Crosby is one representation of what I see as a stark tide turning in wider professional services. How lawyers, but more broadly all knowledge workers – bankers,consultants, and doctors, will contend with the shape of work changing, and the agency, or lack thereof, that comes with it.

## Wall Street Lawyers and the Death of the Billable Hour

Crosby’s rooftop view of the New York skyline

Everyone is trying to make a buck, or find a little glory, in New York. Here, capital flows through the streets like oil, and is fracked out of the cracks: repurposed, spent, wasted. Walk past the white table-clothed tables where raconteurs conduct business dinners, past the florists and tarot card readers and booksellers and bankers, and you’d arrive at the big law offices like stars orbiting the Park-Lexington-Madison belt.

These “Wall Street Lawyers,” coined by the enterprising sociologist Erwin O Smigel, who interviewed over 188 lawyers between 1957 and 1963, were the unofficial “spokespeople for big business.” The moniker was less about the domain in which they practiced, and more about shrewd business conscience – advising clients on “not only what is permissible but also what is desirable.”

Structurally, little has changed since then. Law is still a sophisticated market for the lending and borrowing of human capital.

Billable hours might be the most personally recognizable totems of this structure. Some lawyers bill $3-4k per hour on the high end. Accusations of “padding hours” for lucrative bonuses run rampant. “Lawyers were always suspected of rounding up,” one ex-big law lawyer tells me covertly, “it would’ve been pretty easy to.”

Crosby arrives at a moment where legacy business models arebreakingin the AI world, even prestige-driven, credence goods such as legal work.

Neo-firms eschew selling human time, and instead charge on outputs – a predictable fixed fee, as opposed to the unexpected final bill of a black-box process. Traditional law firms are partnership structures, where profits get distributed among a small number of partners to maximize profits. Junior lawyers often feel like “operating expenses to be optimized,” and turnover is purposefully high. Crosby, and more broadly the hybrid institutions which will proliferate in the future, are corporations where profits don’t get doled out individually but are re-invested into R&D – continuing to make them faster, cheaper, and better.

## Law is an unverifiable problem space (aka: why is this so hard?)

Ryan Tanenholz (Eng intern) and Raymond Lin (Founding Engineering) whiteboarding together

AI has progressed fastest in coding and math because so many answers are objectively correct. The proof solves or doesn’t, the code compiles or not. The unsolved frontier across multiple AI applications moves towards the nonverifiable, towards judgment – law being one such domain.

What counts as a ‘correct’ answer in law is open to interpretation. Two smart lawyers might disagree about whether a specific edit in a document was necessary, or how to implement it. Whether to replace a full paragraph or only a few sentences. Different things matter to different clients, who often change their minds.

As I shadowed, I got a close look at multiple internal interfaces: an AI contract lifecycle management platform that routes and manages contracts, and agentic redlining, which runs over contracts with a customer-specific knowledge base to recommend changes. Amy Danoff, who leads product, sent me a sheet of recorded redlining times from the time trials with accompanying notes. Week after week, I saw the numbers get drastically better. Much of the speed and leverage comes from AI getting more accurate, more surgical and precise with their redlines such that a lawyer finds more of its suggestions acceptable.

A regular day in the office

Here are the most interesting technical problems they are working on:

### Custom eval systems

They created their own evaluation infrastructure, and have set up online evals to detect when a system has regressed on every edit that’s generated. Then, they grow an offline data set that automatically funnels failure cases so an LLM can automatically discover new failure cases they didn’t discover while developing. It allows lawyers to tune judges and be able to run evals on demand.

### Game theory and high-context on client preferences

Client preferences and playbooks are hard to define ex ante, given they’re constantly evolving. Crosby is building internal systems to encode client preferences that accrue over time in the form of playbooks that make it easy for both humans and AI agents to retrieve. It remembers instructions a client gives Crosby in any format (e.g. Slack messages), keeps relevant context about a company, and creates a living, breathing, corpus of rules. This theoretically gets clients to agreement faster by simulating accurately what a client cares about and is inversely willing to compromise on.

Through our research arm, the question we’re driving toward is how to turn contract review into a more verifiable domain by building custom reward models. Eventually, this can pave the way to autonomous review through reinforcement learning

Sharan Ramjee, Founding Research Engineer

### Infrastructure that supports long running stateful agents

Traditional infrastructure assumes stateless, crashable workloads where retry on failure is acceptable. Crosby’s AI agents are the opposite. They are long-running, stateful, and expensive to restart. Their infra team builds to support large workloads of thousands of contracts being reviewed simultaneously.

In the long term, it’s easy to see Crosby transcend past computer science into game theory. All this nerdsniped me as someone who majored in behavioral economics in college.

By starting with actually delivering legal services, the team believes it allows them to collect data across the full negotiation lifecycle from initial touchpoint to signature, while also owning the unique interaction data from lawyer evaluations.

Evening in the office

Yet they’re the first to admit they haven’t figured it all out. Negotiations are still a really hard technical problem ahead, as John tells me:

How do you actually understand and extract these different preferences from counterparties that we’ve negotiated against? How do you make it easier to negotiate against Figma for the 11th time, or Amazon for the 11th time?

Data from in-house lawyer workflows on contract redlining feeds back and continually improves the product. Grace Isford, the Series B lead investor in Crosby, believes that by pioneering non-verifiable reinforcement learning for contracts, Crosby can eventually become the arbiter of any type of negotiation across different industries.

An immense amount of trust building for both clients and internal lawyers has to be earned over time. Sarah Zeng, the Chief of Staff at Braintrust, a customer of Crosby, told me “cross checking” features, detailed internal notes, and “estimated time of arrival” metrics were invaluable for giving them the confidence to migrate all of Braintrust’s contracts over.

Aveek Duttagupta (Founding Engineer) and Henry Klein (Founding Legal Recruiter) catching up in the kitchen

Despite these open questions, the team has vivid imaginations for the future. Lawyers that can create scalable agent versions of themselves which encode their expertise, client preferences, and negotiation style into parallelizable legal agents. Becoming the “contract infrastructure for the internet,” or an “end to end agentic commercial counsel.” Or as Hunter Morales, VP of Ops, says “I want Crosby to be a household verb. Can you Crosby that?”

## Ryan and John: Genchi Genbutsu, Go see for yourself

Ryan in front of the contract review scoreboard

“Technology is promethean. You can create something from nothing.” Ryan in front of their contract review scoreboard.

June marked the start of monsoon season in Bangalore, not that Ryan got to see much outside of his white-walled hotel conference room. He noticed his legal peers were spending millions a year on outsourced legal firms in India. While the rest of the industry grew sluggishly at 2% annually, these outsourced firms were growing like weeds at 30%.

Naturally, he got himself a plane ticket from New York to Bengaluru to investigate. For 14 hours a day, he conducted a series of “interviews” with offshore Indian contract workers and peppered them with questions. He found many of these remote workers were exercising creative judgments like rolling over tax benefits for oil magnates, or negotiating directly with counterparties.

This origin story is very core to Ryan, who I’d label a default seeker. This is the spirit ofGenchi Genbutsu,he tells me, a principle from the Toyota production system. It translates roughly to:go see for yourself.

What’s it like being in Ryan’s orbit? After spending time with him you’d realize he can’t tolerate dogma. Trained as a lawyer at Stanford, serving at Cooley, and as an in-house General Counsel, he felt he had to tamp it down, but it “drove him nuts.”

When I asked him what it was like being a junior lawyer, this is what he replied

At a law firm it felt like you were constantly wearing kid gloves. No, you can’t even edit the document. You can just write on it with a pen. It was kinda belittling. It did make everything failproof, because the most likely person to make a mistake is the junior associate.

But I was just like: How am I going to learn?

He’ll pepper you with questions, but it never feels invasive. He likes subversion and is a fan of little delights – once he hired a band off the streets of New York to play late night jazz in the office on a random Tuesday night. In Slack, there’s a channel called #ryan-diary where he discusses the books he is reading in great detail. His current pick isUnreasonable Hospitalityby the co-owner of Eleven Madison Park on how a great restaurant obsesses over small details in service. Now Crosby is no restaurant or hotel, they are selling work - but they care about ‘magical moments’ all the same, like custom building interactive elements in Slack so clients can accept or reject redlines from direct messages, or creating trackers that give ETAs on important documents.

He is, to the nth degree, obsessed with talent. He met with his current VP of Operations, Hunter, for coffee consistently over a year to convince her to leave her role as Head of Ops at Scale AI. He put together an internal “hit squad” to maniacally work on getting the best talent - which he describes as 10+ hours per week of focused hiring pipeline on top of their regular job. At 9pm at a party they were hosting, I saw him send around a legal notepad and tell everyone to write down the names of their smartest friends.

The current Crosby office is actually on Crosby Street

It takes two tothink. If Ryan is philosophical, charismatic, a steward of people, John Sarihan, Crosby’s CTO, is a deeply pragmatic and an execution oriented thought partner. Multiple people told me they were each other’s foil.

Ryan Kim, a partner at Bain Capital Ventures who incubated Crosby, shared with me one of Ryan’s essential skills is “sincerity” and intellectual curiosity, fantastic at “creating reality distortion fields,” while John is all “fast clock speeds and quiet competence.” The abrasion is good for them.

Little has been written online about John Sarihan because he has been resolutely and purposefully off the radar. Luckily for me, we went to Penn together so I can perhaps divulge a little more. In our junior year sitting next to each other in finance class, he waxed poetic about a really small and scrappy fintech company he was intent on joining as an early engineer. At the time I thought it sounded niche. Cards and payment rails? The world definitely didn’t need another credit card. I was proven wrong. That small company was called Ramp.

John would go on to lead Ramp’s travel product, and the company 1000xed revenue while he was there. He was mentored by Karim Atiyeh, the co-CEO at Ramp, and picked up a huge bias toward speed over perfection from him.

Karim asked me in my Ramp interview: what do you want to be long term? And I said: I want to start a company. He told me, Hell yeah, you have to come work at Ramp – it’s a founder bootcamp. From him I learned: hire for slope and take big bets on people. Now at Crosby we have the same ethos. I want to hire people who are either like: this is my last job, or this is my second to last job because I’m starting a company after.

The engineering team tells me that John is deeply methodical; he isn’t afraid to get off the soapbox and “get shit done.” Most of all, he’s impatient (in a good way!) He hates lag for the sake of lag. He defaults to breaking down complex problems into “little brick walls that you can run through.” He’s Zen externally, appears unperturbed by much. But I wouldn’t confuse that with contentment. He’s constantly hungry for feedback. After a public speaking event he turned to me, stone-cold serious, and asked me: “forget the niceties, what could I have improved?”

If you spent time with both of them, you’d acutely feel the feverishness of their vision. I sense the motivation is not making the most money or raising shiny capital, but building a seamless end to end service. Their shared internal mantra is that Crosby, more than a product, is an “experience you talk about at dinner.”

## Misfit lawyers who run evals

Tenzin Dolkar (Director, Legal) and Kush Pandey (Founding Ops) hitting the Crosby Sales Gong

Ask the lawyers what type of person would give up prestigious jobs at white-shoe firms like Sullivan and Cromwell, or Kirkland and Ellis, making upwards of millions in cash compensation a year to join an upstart – and you’d hear words like: impatient, disillusioned with tedium, out of distribution. If Tenzin Dolkar, one of the first lawyers at Crosby, had to use one word to describe the personality patterning at Crosby, she would use “awake.”

If the lawyers were initially scared of their job being automated away long term, it soon became clear that usage and trust relied on a high performing lawyer being in the loop. Ross Weiser, who came from Sullivan and Cromwell – routinely ranked as a top 5 law firm globally and one of the absolute best in New York for corporate practice – tells me he initially thought clients would just trust and interact with Crosby differently as an AI law firm. Instead, he found one constant:

They want to know that they can trust us. They want to know who’s responsible. It is just so human.

In my eyes, even after witnessing the gains to efficiency using AI, the value of a lawyer who is great at negotiating will continue to be very high. The best lawyers move from being transactional to integrative, allocating risk to both parties in a way that makes them both feel like they’ve won.

The lawyers are running evals! If you talked to Ross, you’d find it hard to put him in the pure lawyer-shaped box. When we talked he sounded more like an engineer to me. Now he works in the new multi-hyphenated role of legal engineering. He’s currently working on a playbook schema for the eval system, and LLM as a judge system for grading Crosby’s AI outputs as compared against what a reviewer actually sent out.

Ross Weiser, who is a “risk-on” lawyer

The change in the role of the lawyer, or any profession, merits personal and psychological pliability. Success probably means something more than just the best technology, but motivating and running a team of professionals that feel they have a stake in the future, with a sports team-like sense of drive to win.

Inevitably not all neofirms will get this right. The team at Crosby is pretty opinionated that product choices really matter in preserving lawyer choice and agency. In aggregate you can either make the lawyers feel like they are at the service of a robot or they are in control, directing them and orchestrating. One lawyer describes,

That feeling: that I’m commanding an army of agents, if you can create it, feels amazing. That feels empowering. It’s very intoxicating to find leverage on productivity rather than just proofreading which feels reductive or commoditized.

If we were to imagine a “lawyer utopia,” one of Crosby’s secret goals, it would be a firm where lawyers get the best of all worlds. They only do expert work, solving intellectually tricky problems, while working reasonable hours. “What happens when the lawyers go direct?” Bijan Motiwalla, one of the lawyers who joined from Kirkland hypothesizes, “At traditional law firm models the business context is generally handled by a separate business development team. If you own the relationship end to end, you own trust.”

## Crosby’s Internal Culture: A Library in New York

A Wednesday lunch at Crosby

Hunter Morales (VP of Operations, Legal) leading a Crosby team huddle

#### A Slack History of Crosby, Writing and Reading Culture

Scroll back all the way in Slack and you get to see a miniature written history of the company. Reading it, you viscerally feel how fast things are moving in the AI age. Crosby raised a Series A and B in the same year (2025), and employees that have been there a year are already amongst the most tenured. I see all the hesitations, frustrations and “chewing glass” in the early messages: Ryan has classic founder paranoia that they are “leaving the flank exposed” even as he excitedly writes in one fateful thread that “Claude code is coming!”

Getting to witness this at all is in part due to the writing and reading culture in the company. There’s a robust book recommendation pipeline, multiple team-wide strategy memos, and even the engineers write long treatises on new agentic architecture. There’s a library of books everyone has read, including one written by a Crosby employee, and an unlimited book budget.

#### Lawyer-Engineer Empathy

The engineers just really want their lawyer coworkers to win. Anthony Corletti, one of the founding engineers, tells me that in the early days of Crosby he shadowed Ryan for weeks watching him “nitpick language.” Shadowing is a practice in everyday empathy.

In the early days we were in this tiny office in Chelsea. I sat with my laptop taking notes for four hours at a time while Ryan was redlining. When I was watching Ryan click accept. I asked, why did you accept? He says we don’t want to have “fluffy language.” Because when we send this contract back, we would like them to say accept all or this is okay, deal is closed. It was unintuitive. You learn so much watching the lawyers work. Shadowing closely just propagated from then.

Anthony Corletti, Founding Engineer

Tight feedback loops happen when lawyers and engineers literally sit next to each other in the office rather than in an ivory tower.

#### “No Sacred Cows” and The Scientific Method

The most surprising thing hidden in plain sight is the sophistication behind the operational arm of Crosby. They developed an in-house internal routing “brain” that calculates supply and demand based on predictive models of outages and seasonality. Such calculation helps them understanding how to scale new customers carefully so they can keep quality high.

More broadly, the team is very metrics and evaluation focused. Ariba Khan, a member of technical staff, tells me “we must run multiple experiments and approaches, or else you’re always stuck at local minimums.”

You need online evals, continuously learning from them, telling you what cases have improved, what cases have progressed. The field is moving so fast, if you don’t have that kind of scalable way to set yourself up correctly, you can never assume that you’re at the frontier.

#### A College Library in New York

Crosby interns, PhD fellows, and lawyers eating together

The office itself feels somewhat like a college library, people flowing in and out, often unfamiliar faces dropping by for a coworking or lunch. It’s generally an exuberant and highly energetic place. There’s a playfulness that feels different to a buttoned up law firm. Lawyer working groups have even coined group names, like “transactional tigers,” “legal eagles,” and “termsformers.” Maybe telling: despite the mixture of pedigreed lawyers and 22 year old whiz kid engineers and PhD researchers, everyone eats lunch together.

I’ve discussed misfit lawyers, but on a broader scale there are a lot of multi-disciplinary generalists at Crosby. Emily Zhang, a member of technical staff, also led brand and design for Crosby’s Intelligence launch, and is heavily involved in recruiting. She tells me insistently: “recruiting is one of the most important ways an engineer can contribute value to a company. When great people work on a hard problem, magic happens.” Billy Gallagher, who leads everything marketing, was once a tech reporter and venture capitalist who wrote a book on Snapchat.

Crosby is also, today, a Very New York Company. Eventually they’ll have to expand, and are expanding, to other parts of the country. But it feels like witnessing a rare and precious moment in time where the team still walks across Manhattan together, watches the World Cup during lunch, and hangs out in Soho until midnight. The office is almost always full to the bursting.

Coworking session with Emily and Sharan (Engineering)

Crosby is a bag of dualities. But dualities are what make a place interesting and alive. The biggest bridge Crosby has to make is between the risk averse legal culture, and the demands and cultural pulse of a startup. The automation potential of technology, with an understanding that all negotiations are ultimately in service of what is deeply human.

No one knows what legal work becomes in the long term, and I wouldn’t trust anyone who spouts oracle wisdom. But inside the neofirm I saw glimpses of the old world vanishing, and hierarchical systems being flipped. If lawyers can spend less time on deadweight tasks, their time becomeseven morerelational - building mutual context and trust between strangers, where the process of getting to an agreement is an end in itself. The lawyer remains more than the last mile. After all, “a contract review is a conversation between two humans,” Ryan said as we walked up and down Crosby street. “It entails feeling.”

This piece came together after over 25 conversations with the team and an immersive two weeks in their New York office in the heart of SoHo. Thank you to individual conversations with Ryan, John, Billy, Emily, Kush, Amy, Hana, Anthony, Steven, Aveek, Ariba, Raymond, Sharan, Hunter, Ross, Bijan, Tenzin, Aidan. And interviews with lead investors and customers Grace Isford (Lux Capital), Ryan Kim (Bain Capital Ventures), Sarah Zeng (Braintrust).

Want to know more? LetRyanorJohnknow you came from here.

behind the scenes

Photos byGibson Chu