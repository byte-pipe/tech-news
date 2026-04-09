---
title: Lobsters Interview with Hwayne | Lobsters
url: https://lobste.rs/s/bc53lh/lobsters_interview_with_hwayne
site_name: lobsters
fetched_at: '2025-08-09T23:06:46.309932'
original_url: https://lobste.rs/s/bc53lh/lobsters_interview_with_hwayne
date: '2025-08-09'
description: ☶
tags: formalmethods, interview, person
---

1. 51Lobsters Interview with Hwayne☶formalmethodsinterviewpersonauthored byveqq25 hours ago

For thisinterview, I spoke withhwaynea few times.

Last week, we talked toicefox, next week we’ll hear frommatklad. Thank you to my proof readers! <3

Yo! To prove it’s me, here’s a hash of our last PM:a4332cf8fb02ff3f02de333343958021. Not for security, but to signal my values!

Much of my childhood online was collecting common wisdom, memes, fuddlore and repeating them to signal my virtue. Growing has been the long path of killing those darlings. Anyway, I love your work!

Let’s see how fast I can disillusion you!

Introduce yourself! How’d you discover programming andFormal Methods(FM)?

I’m Hillel. I’m mostly known online for writing about software, especially FM (to make it more accessible), and history. In my free time Ijuggleand make chocolate.

I always liked computers and tried to learn C++ to make video games as a teen: not an experience I’d recommend to people. (Actually, I learned Drape and Visual Basic before that. I also miss VB6, it had nice features). In college I did Physics and Math with the hope of becoming a physicist, but got scared off by grad school, because all of my friends who graduated before me, seemed miserable. Long hours, low pay, bad social life, and for five years…

Besides, universities and industrial labs push the boundaries of human knowledge, but I really like “pop research”: aggregating existing knowledge and presenting it in engaging or entertaining form. My dives into exotic languages are a good example, likeJand Picat. Indeed, FM is a manifestation of my real passion of falling down rabbit holes researching. Besides, community puts me in touch with lots of academics and exotic tool users, who love to share their weird stuff with me, likeMiniZincand constraint solving!

Anyway, I pivoted into programming because at the time (2013) that was the easiest way for educated people to switch career paths. And all the money was in webdev, so I became a webdev. Later atespark, which managed iPad apps for elementary schools, our system ended up being “accidentally distributed”: interactions between us, Apple APIs, school infrastructure, and their mobile device managers led to lots of issues you see in distributed systems, despite us all doing Rails and JavaScript. At this point, two things happened:

1. I researched Idris, which led me to internet arguments about FM, which in turn led me to reading the Amazon TLA+ paper “Use of FM at AWS”.
2. I was officially diagnosed with ADHD and put on Ritalin.

Important question for the interviewer: have you ever taken ADHD meds?

I have not!Basically, for the first couple of days after you start meds, you are a GOD. Nothing can stop you. You can do anything. After a few days, your body adjusts and balances out, so you get the ability to focus without the mania. For my first two days, I crammed TLA+. This head start really helped get over the hump. I immediatelycaught some major bugs in the redesign, which made me fall in love.Cue years of trying to make it more accessible for people without the Ritalin God-mode head start!

But evangelism is difficult. Atespark, nobody else wanted to learn TLA+ because I already knew it. The vibe was that it solved a one-off problem and they wouldn’t need it again. After I left, about once a quarter they would tell me about a new hairy bug that would have been caught by TLA+, always “a one-off problem that won’t happen again”.

I see this as a manifestation of just how high the cost is for these tools. If it took five minutes to learn and apply, they’d do it. But they expect weeks of practice to study and solve problems and think “ugh no”.

In your evangelism, you talk of the business case sometimes. How do you balance that for a company vs. the personal effort/career hurdles of developers?

I often ask myself: Does spending ten hours learning FM or bash scripting really well help the average engineer more? Probably bash.Right now, FM is a very bottom-up practice where developers see it, get inspired, and apply it at their work. Very rarely is it top-down, where a VP or director mandates it. The researchers and evangelists —including me— are devs. The TLA+ foundation is trying to figure out how to make that jump though. We haveanecdotalclaims of FM catching expensive bugs and saving money, but it’s hard to put numbers or measure the cost/reward, which makes decision-makers shy away.

There’s then the perennial challenge of “okay we’ve modeled the specification, how do we actually make sure our implementation matches this?”

The Go team wrote 2 implementations, to keep thespechonest.

Part of the value of a formal specification (spec) is that it can be so abstract. Specs omit many details a generator must make. But there’s vast potential in using specs totestcode. MongoDB has done a lot and I’ve made “test generators” for clients (which I’ll blog about.) I’m generally a fan of test driven development, because I know if I don’t write them ahead of time, I’ll never write them.TDDand robusttestingalso mirror writing specifications, starting with simple types and actions in the state space and properties which should fail. (It’s always fun to see how much ground a single property test covers!) I wonder how Prolog would be for writing these kinds of tests.

I recently gave atalkon FM where I proposed a concept of “test strength”:S => Wmeans that if test S passes, test T will pass too. A trivial example of this is thatmax([1,2,3]) == 3 => max([1,2,3]) in [1,2,3]. Strong tests give you more bounds on the correctness of your code, weak tests give you more information about where bugs are. Wherever we have strong and weak tests, cultures tend to prefer few strong ones and lots of weak ones.

What’s your modeling workflow? For personal projects, I’ll e.g. start with comments on the steps required, then make tests for them, then code to solve the tests.

A common workflow with specs is:

1. Write a spec
2. Generate its state space
3. Take some of its behaviors as sequences of steps, then turn them into commands on the program [1]
4. Verify that the program ends up in the same state(s) when fed those commands

The tricky bit’s that complex systems present idiosyncrasies when converting between specs and tests, precluding a one-size-fits-all solution. MongoDB just published apaperon this. And you have to do it for a given language (and I was specifyingRubyof all things!)

By the way, most of my work in FM is coming up with rigorous designs, not formally verifying code.

How do you handle notations?

Give ’em JSON! I have a gadget for turning TLA+ traces into JSON traces to parse in whatever language. Familiarity beats appropriateness 90% of the time.

One of the important things about FM is that people only want to spend one innovation token. They don’t want to learn TLA+andRaku, they want something they can maintain after I’m gone, and that means limiting the amount of novelty. FM is already super novel.

How would you compare FM to Prolog?

Anyway, on the surface they’re very different. Logic Programming (LP) is first and foremost programming, while FM (well, formal specification) is about modeling a system. There’s ideally no I/O in FM. But both heavily rely on formal logic, in different ways. You can’t get anywhere in FM without a strong understanding of quantifiers and implication, and so much of Prolog is defining things in terms of existentials, in my experience.

Functional core, imperative shell ~ Functional… FM armor for your core?

Unification and model checking are both representable as search problems. If Prolog is “depth-first search – the programming language”, then TLA+’s model checker is “breadth first search – the model checker”. This is more obvious in planner programming, where you write the list of steps a system can perform and have the unifier find a sequence that reaches a goal.Picathas this built in, I think you can do it in Prolog with DCGs. Anyway, “this system violates property X” is equivalent to “the planner can reach goal !X”.

You once asked me “why didn’t Prolog catch on” which has been bouncing around in my head ever since. God, I wish I knew why things succeeded or failed in general. It’s easy to come up with possible reasons, but so much harder to see if those reasons actually mattered. My own speculation is it’s less that LP failed and more that Structured Imperative Programming won. Perhaps, languages only become successful if they fulfill the population’s needs. For Haskell, the population was academics and the need was “write papers”. To be clear, this is not a dig against them: that need is valuable in society and has led to lots of amazing discoveries in FP. But the biggest need is “make money” and it seems the best languages for this (i.e. the languages businesses consistently adopt and have adopted) are imperative languages.

Like, since 2010, what were some of the biggest success stories in programming languages? Kotlin, Swift, Rust. Almost Go and Clojure. It’s debatable if that’s actually evidence: it could be that they were all just trying to be backwards compatible with existing imperative languages and/or were for low-level programming, where imperative dominates. Maybe this is a dead end without a lot more information and research. Maybe there’s something on how it’s easier to glue together libraries in an imperative framework or it’s the default for reasoning in certain circumstances…

Anyway, Prolog has unpredictable performance and didn’t evolve. I mean, how different is Go from the first imperative languages? Most people would say “not very” but it’s enormously different! Fortran → Algol-60 → CPL → BCPL → B → C and Go borrows from other places too like CLU. Picat? The chain goes Prolog → Picat. MiniKanren? Unsure, but it’s probably something short too. Compare these highly-iterated imperative languages (which again, might be very well suited for a broad range of business tasks) against low-iterated logic languages. If LP should get more popular, maybe it needs to be introduced via “LP-flavored imperative”. I don’t know.

How would you situate planner programming?

Any community which defines itsinterchange formatin S-expressions must be Lisp-based. But Picat is the first language I encountered with planning and it fits the logic paradigm really really well. I keep looking for problems I could solve with planning, a hammer in search of a nail. But they’re often solvable with plain-old constraint solving.

How do you choose and approach diving into exotic languages?

I let ADHD guide me. Sometimes I learn a little bit and go “okay maybe some other time”, sometimes I get completely absorbed. But my backlog has grown really long from the book I’m writing.

Consulting is TLA+/Alloy. Personally, I can already solve a problem with tools I know, but I want to know what the “optimum” tool looks like. That’s what started me on LP. I was planning some activities for a vacation, with unusual enough constraints that a constraint solver wasn’t appropriate. While it was easy enough to do by hand, I wondered “what would happen if I tried LP?” This all, of course, depends on being exposed to a wide variety of niche tools, which Lobsters naturally encourages.

Another important factor is whether I can write about it. When learning something new, I constantly ask myself: How can I explain why this is interesting to others? What would an article about this look like?

How do you approach a blog post?

Embarrassingly, I havetwo“blogs”:hillelwayne.comand anewsletter. The website’s for when I want feedback before publishing while the newsletter was written in a day (mission-creeped to 2–3 days.) This led to a weekly newsletter cadence and a monthly blog cadence, though I’ve been on hiatus due to the book consuming me.

These constraints affect how I approach “designing” written material. If it’s a newsletter, I try to form the idea fully in my head and then just write it out, usually making adjustments if things are proving too messy. If it’s a blog post, I design and write with the expectation that it will not be close to the final product, that every word in it might be erased and replaced with a different structure. It’s never a waste of time to throw away a draft. The draft gives you the actual, better idea for the overarching structure.

How do you approach books?

For my first book, having a publisher with a hard deadline really helped me, because I couldn’t dilly-dally. The current book is self-published, so I have to set my own deadlines. “Early access” helps here, seeing sales and feedback is a strong motivator.

How does self-publishing compare to writing a book with a publisher?Logic for Programmersis self-published, why?

Self-publishing is a ton more work! I have to pay for the book cover and copyediting, get an ISBN number, market beyond word of mouth, and stick to my own schedule. It’s all harder and less convenient. In return:

1. I get to use the tech stack I want. ForPractical TLA+, I had to submit chapters to my publisher as Word documents. This is really hard for a technical book! ForLogic for ProgrammersI can write my books inSphinxand compile them to LaTeX, which has its own issues, but gets me a lot more of the benefits I need.
2. I was able to put the book on “early access”, so people could buy it before it was done. So far it’s sold over 1,000 copies! That’s a huge motivation to get it finished.
3. It pays a lot better. This was honestly the reason that led me to do this in the first place. My old publisher pays me 10% royalties on net profit of books sold, which ends up being more like 5% of the sale price. Leanpub is paying 80% on sticker price as royalties. One copy of LfP sold nets me about as much as 15 copies of Practical TLA+.

I expected writing a book to make no financial sense directly.

I’m hoping I can turn this into talks/workshops/general consulting to make the bulk of the money back. But with self-publishing you do make some money: LfP has made about 20k while in prerelease, so I think it can potentially make a few multiples of that. It’s nothing like working full time as a software engineer though.

How would you approach your next book?

I’m 100% for sure not writing another book after this, ever. I said the same thing after writingPractical TLA+, but this time Imeanit. The biggest question is “can this topic support a whole book?” Many important and interesting topics in our field aren’t book-worthy, they’re blog or website worthy. It’s amazing that we have this great means of disseminating written information without people paying for a book. A book only makes sense if you have a lot to say. So is the topic something I have a lot to say about?

In the case of Logic for Programmers, the answer was almost “no”. I was originally inspired to write about logic from teaching TLA+: I found that a couple of basic concepts in logic —implication and existential quantifiers— were huge stumbling blocks for students. They just had never been exposed to these tools before, which surprised me because I use them in so many different ways. In 2021, I started writing, then realized it didn’t need to be a book but 3 blog posts, at most. So I started writing those blog posts and realized I had a lot more to say, so it turned into a book again!

This applies to everything, really. My first talk rehearsals look nothing like the final talks. Most LfP chapters have been rewritten unrecognizably from their originals.

Writing is an important tool of thought!

I can think without writing, I just can’t be thorough. I can still think about the emotional touchstones of a piece, or what feel like good examples, or what seems like the hardest to explain, etc. A surprising amount of time spent brainstorming a piece is finding a good example.An example showcases the topic without requiring too much background context, without feeling trivial, artificial or dismissible.

How do you approach teaching a course? It’s interesting how you massage the map of information for different formats and audiences.

The hard part of designing a course, for me, is feedback. With writing or talks, you can get rapid feedback on your draft. But you need to run a course for feedback. It’s bad enough for a 2 hour course, but some last 8 or 24 hours! Your only QA is the customer.

As you say, I have a map of the information, so I know what needs to be covered. Courses don’t have to be as comprehensive as books and you’re under time pressure, so you have to throw away auxiliary or even essential information, due to priorities. In a class, everything has to feel useful and real.

It’s so easy to make a class that makes something useful in an artificial environment, but then the students think “okay, but it doesn’t do anything forme” or “it doesn’t work in the real world with real problems”. This demands more of examples, not just good butreal. So I always end FM courses by getting a specification from the class and modeling it live to show “yes, this can actually help you with your system, it’s not just make-believe”. This has the happy consequence of surfacing special topics particular to the class’ interests, so they get exposure to e.g. recursive data structure representations, reading specs in from CSVs or debug-modes.

What does engineering mean to you?

I think about this a lot. I did aprojectcomparing software engineering to traditional engineering. They’re pretty similar but it didn’t get to the essence of engineering itself. To me, what separates software “engineering” from “programming” in general is the treatment of the software itself as a meaningful artifact and product. Many people program: artists, grad students, scientists, data people, Excel jockeys, people in game jams… But they rarely care about version control, backwards compatibility, API usability, modularity, etc. They think of software as a step to getting something done, not something important itself.

Unexpected! When looking at the legacy of Naur, of people late career coming to epiphanies that software’s less important than the mental models (documented through software)…

I think here are 2 mental models: of the problem and of the software solving the problem. Softwareengineeringbuilds the second model too. Software engineering’s when you can’t just tell the LLM to “write a program to do X” and be satisfied, because you have to consider constraints and scope beyond the individual problem, beyond the functional requirements. Performance, security, auditability, privacy, compliance, even compatibility with your current tech stack, considering them makes it engineering.

How do you collect requirements adequately? You discussed thespec->implementationproblem, what about the BA problem ofmysterious-world->spec?

The answer is surprisingly boring: spend a lot of time speccing it with a domain expert. FM helps an engineer do their job better, but it doesn’t help an engineer who doesn’t want to do the job. Part of that job is figuring out what the problem to solve is.

Our industry ignores correctness. Tell me why!

Just the boring, cynical answer: “bugs don’t cost enough to be worth squashing early”. The companies most receptive to FM expect really expensive bugs to be both possible and subtle. Many companies aren’t interested because they think they can catch their bugs with other methods or think they don’t have expensive bugs at all. And if they’re wrong, they find out too late.

How technical does management need to be to consider these things? I find many businesses have poor oversight of internal operations and make poor assumptions when deciding opportunity costs, etc.I believe management should be quite technical to catch these things, but I don’t want to be too judgmental; I have very little insight into what large businesses look like from the top. Maybe I’d take one look at that and give up on FM forever. Past a few hundred employees and you can’t form a good mental model of all your employees.

[1] The original phrasing was:

One common way of doing that: 1. write a spec. 2. generate the spec’s state space 3. take behaviors in that state space, sequences of steps, and turn that into a sequence of commands on the program. When fed the same commands, the program should end up in the same states.
