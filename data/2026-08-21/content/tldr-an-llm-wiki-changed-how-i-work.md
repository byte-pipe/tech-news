---
title: An LLM wiki changed how I work
url: https://www.platformer.news/karpathy-llm-wiki-journalism-productivity/
site_name: tldr
content_file: tldr-an-llm-wiki-changed-how-i-work
fetched_at: '2026-08-21T19:25:17.918606'
original_url: https://www.platformer.news/karpathy-llm-wiki-journalism-productivity/
date: '2026-08-21'
published_date: '2026-08-19T00:28:38.000Z'
description: And everything else I learned about productivity this year
tags:
- tldr
---

This is a column about AI. My fiancé works at Anthropic. See my full ethics disclosurehere.

At the beginning of April, the prominent AI researcher Andrej Karpathytweetedout an idea that was, for a certain kind of productivity nerd, an infohazard. He described the idea this way: “Something I’m finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest.” He proceeded to describe his process: adding source documents to a local folder and using an LLM to extract and organize their contents into a Markdown wiki that gets updated as he adds new material.

Karpathy’s AI-related pronouncements are closely followed online — he is, after all, the person whocoinedthe term “vibe coding.” And so, seemingly within hours, the web had filled up with GitHub repos, YouTube videos and Substack posts about how to set up an LLM wiki for yourself. I call the idea an infohazard because, simply by becoming aware of it, I had ensured that I would devote the next several weeks to building it, without having any idea whether it would benefit me at all.

As it so happens, it has. Of everything I tried this year to get better at the deskbound parts of my job, the LLM wiki has easily been the most useful. Like a vintage sports car, it requires a fair degree of maintenance, and there are almost certainly easier ways to create a personal knowledge base. But if you do any sort of work that has made you crave the help of a good research assistant, an LLM wiki might be worth your time.

The wiki is the centerpiece for my annual productivity post, where I run down any changes to the way I work that might be interesting to others afflicted by an inexplicable enthusiasm for software. (Here are the posts from2023,2024, and2025.)

So with that, here’s what I’m still doing from last year, what I stopped doing, and what’s new.

### What I'm still doing

Given how often I switch apps, the best test for whether something actually makes me more productive is longevity. Do I install the app on a new machine? Do I renew the subscription when it’s time? Can I point to the places where it actually saves me time?

Three apps I’ve recommended in previous years still clear that bar.

Raycast, a launcher app that replaces Spotlight, remains my preferred way to navigate a computer. When I press ⌘-space, the Raycast window instantly materializes and lets me perform actions across most of the apps that I use. I look up words; I do math; I reposition windows; I access my clipboard history; I open websites. And thanks to a paid upgrade, I do tons of simple AI searches in the Raycast window. (I use GPT-5.5 Instant here for the high quality-to-speed ratio.) When I’m done, there’s no getting lost in a jumble of open tabs or windows — Raycast simply fades back into the background. At this point, I really can’t imagine my Mac without it. And in a nice development since last year, it’s now available forWindowsas well.

Capacities, which bills itself as “a studio for your mind,” is where I keep my daily journal. Each morning, I write a bit about whatever’s on my mind. Then, I add notable news links fromTechmemeto the bottom of my journal and tag them. The result is that when I’m writing a story or preparing for a podcast, I can click a tag like “Labor” and instantly see all the stories I’ve saved on that subject since I started building this system a couple years ago. This has been enormously helpful in planning our current podcast miniseries on AI and productivity, since we discuss jobs news on each episode. I used to spend a lot of time digging through databases or running fruitless Google searches in an effort to jog my memory about something I had read; Capacities ensures that it’s all just a click away. You could easily do this with any number of apps, but after three years I still find myself appreciating the simplicity and calm of Capacities.

Finally, last year I mentioned testing an app calledRecallthat (anticipating the LLM wiki!) helps you save and organize content from the web. I found myself using it less for that purpose over the past year, except for one remaining killer use case: its Chrome extension provides near-instant text summaries of YouTube videos. Over the past year, I’ve saved myself many hours by dumping podcasts I feel like I should listen to for work into Recall and simply skimming the summaries.

### What I stopped doing

The two things I stopped doing over the past year are related to each other — and to the LLM wiki. For years now, I’ve been seeking a solution to problems of memory. I’ve been a tech reporter for almost 16 years, have written a newsletter for almost nine, and have written this newsletter for six. For much of that time, I’ve been publishing stories and saving research materials in various places. And when a news story comes along that draws on some of that history, I want to find that context as quickly as possible.

Last year I talked about how Notion had shipped a feature I’d wanted for years: an agent that could search across the thousands of links I had saved into it over the years. It worked well enough, but I couldn’t turn it into a habit. The search feature in the database itself is a simple keyword-based search; agentic search takes place on one of the app’s many other surfaces; and the agent often failed to cite its sources without additional prompting. It worked, but it was effortful.

Moreover, it only looked backward. I also had a need for a system that would help me organize stories around new concepts, and at scale. In Capacities, I took to creating pages I called “blips” (inspiredby Andy Matuschak) where I could gather loose string. For example, in the summer of 2024 I created a blip called “AI could create massive job loss,” and added relevant links to stories about AI and jobs as I encountered them during my daily journaling.

For a few months I felt extremely clever, because I created a dynamic object in the template for my daily journal in Capacities that would show me a selection of blips at random. This would regularly remind me of blips that I had forgotten to update, and worked better than any system I had previously devised for tracking long-term stories.

Ultimately, though, even this system asked a bit too much of me. As the number of blips proliferated, my ability to consistently track stories across all of them waned. This, in turn, made me more reluctant to create new blips.

And that’s why, when I saw Karpathy’s tweet, I sat a little straighter in my chair. What if AI could write and update all those blips for me?

The wiki page for the Hugging Face agentic breach (Casey Newton / Platformer)

### The LLM wiki

Really, the most important change in my productivity over the past year is that …I make software now? Like seemingly everyone else at the end of last year, I began messing around with Claude Code, and have since made a small handful of apps that I really do use all the time. Sometimes I useGlaze, another app from the maker of Raycast; it excels at design and polish.

For the LLM wiki, though, I just asked Claude Fable 5 to write me a prompt that would get me a “Karpathy-style LLM wiki.” I pasted the result into the terminal (I useGhostty), and before too long I had created a new folder of Markdown files in Obsidian.

One thing that makes the wiki particularly valuable for me is that I first seeded it with my own writing: the entirePlatformerarchive, from which Claude expertly extracted all the various people, companies, and concepts that I’ve covered here since 2020 and wrote them up in Markdown files that live on my computer.

These files can get quite long; my page for Meta runs to more than 12,000 words and contains more than 1,300 links to other pages in the wiki. Day to day, that isn’t of much practical use. But I’ve lost more than one afternoon browsing the archive in the same state of blissed-out curiosity that I browse Wikipedia, remembering old stories and reasoning about how they fit into current events.

But I wanted more than a wiki of my own work. And so now each morning after I journal, I save a selection of stories into the wiki via Obsidian’s web clipper, which converts them into Markdown. Then a script on my computer reads the stories and figures out where they fit into the wiki.

The result is that I now have more than 1,440 wiki pages covering most of what has ever interested me atPlatformer: from the content moderation focus of the first few years to my growing interest in child safety and AI progress. The wiki creates detailed timelines that link to original sources, and I can ask it questions using a simple Obsidian plugin namedClaudian.

How does this make me more productive? I’ve found it highly useful in fast-evolving, complex cases likethe OpenAI / Hugging Face agentic breach, where we learned a little more about the story every few days for a matter of weeks. Each day as I prepared to write, or podcast, or go on someone else’s podcast, I would pull up the page and refresh my memory — while also opening up the original sources to make sure nothing I was about to say was hallucinated. Given the real complexity of that story —how exactly did the agent escape? From where? To where?— this saved me tons of time.

It also gives me useful story ideas — and it does it by automating my old blips system. Each day as it reads, the wiki generates new pages for concepts in the news — like “tokenmaxxing,” or “youth social media bans,” or “AI copyright.” It also updates a “home” page every morning that highlights stories in the news. This week, spotting the “AI and Congress” concept in my wiki led me to open the page and see a number of recent stories on the subject; I later pitched it as a podcast segment.

All of that is great. What’s less great is that the wiki needs more or less constant maintenance. Pages grow too long and need to be compacted. An error in the code means that one process or another stops running and has to be fixed. And Claude’s hyper-compressed, borderline-unreadable house style (seethis tweetandthis one) led me to use GPT-5.6 Sol to rewrite much of the system to more closely approximate AP style. (It did a great job.)

It has now been just over a month since I created the wiki, and I find myself looking forward to checking in on it in the morning to see what it has built. On one hand, it seems too specific to me and too clunky for me to confidently recommend. On the other, “self-organizing knowledge base” strikes me as the teleological end of whatever process began the day I first installed Evernote on my Mac in 2008.

That’s one reason why I sought out Town CEO Jean-Denis Greze foran interviewlast week; one way of thinking about that product (or what it might evolve into) is a kind of Karpathy LLM wiki for work. As ever, the price of using these tools at the bleeding edge is that I arrive everywhere much too early. The payoff is that, somehow, I am enjoying myself quite a lot.

A MESSAGE FROM OUR SPONSOR

### The shared card era is over

Mercury Spend is expense management built into Mercury. Give your team and agents cards, set spending limits per person or team, and the policies enforce themselves. Receipts arrive automatically from Gmail or via text, and cards with overdue tasks auto-lock until resolved. No end-of-month scramble.

Explore Mercury Spend

*Mercury is a fintech company, not an FDIC-insured bank. Banking services provided through Choice Financial Group and Column N.A., Members FDIC. The IO Card is issued by Patriot Bank, N.A., Member FDIC, pursuant to a license from Mastercard International Incorporated.

## Following

### OpenAI's safety reset

What happened:

OpenAIintroduced“ChatGPT for Teens,” a new mode with safeguards designed to protect teen users. The company announced work on the feature last September, after they’d been sued by a number of families of teens who had died by suicide following conversations with ChatGPT.

OpenAI also announcednew measuresto protect adult humans (including themselves) from its own products. The company says its new models might have reached a “critical” level of cybersecurity capabilities — which among other things increases the risk their agents will escape containment and hack into other companies, as happenedrecently.

The company said in ablog postthat it paused training on its latest generation of models for the past two weeks as it improved security systems. OpenAI will also postpone a planned large training run until it has done more assessments of the systems’ safety.

Why we’re following:The company's heightened focus on safeguards in the wake of high-profile safety incidents is welcome, even if it is arguably overdue.

ChatGPT for Teens will apply safeguards “designed to reduce exposure to content that may be harmful or developmentally inappropriate” for users under 18. It will build on OpenAI’s earlier parental control features that allow caregivers to set quiet hours and get alerts about concerning activity.

“ChatGPT should not use romantic language, encourage emotional dependence, or imply that it has feelings or consciousness,” the company said.

The feature takes a similar approach to under-18 accounts created by social media companies in response to child safety concerns. (Ask social media companieshow that's going!) And as with teen accounts, the safeguards can be evaded, as OpenAIsaid themselvesin a blog post a few months ago: “Guardrails help, but they’re not foolproof and can be bypassed if someone is intentionally trying to get around them.”

Were I a parent, I’m not sure I’d trust my teen around a model with “critical” cyber capabilities. So let’s hope OpenAI keeps taking the time it needs to ensure it’s safe!

What people are saying:OnX, Ex-OpenAI board memberHelen Tonerapproved of OpenAI’s decision to pause training. “Really good to see this,”she wrote. OpenAI’s policy, she wrote, is “by far the best way to think about "pacing the frontier"— not as some fixed amount of time (e.g. 'six month pause' or 'go 10% slower'), but simply making sure that enough time is taken to meet a reasonable safety/assurance bar.”

—Ella Markianos

### Meta’s social media addiction trial opens (again)

What happened:Four states —California,Colorado,Kentucky,New Jersey—went up against Metatoday in a landmark trial in California over allegations thatMetadesigned its platforms to be addictive for young users and misled the public about the risks.

In opening arguments,Megan O’Neill, deputy attorney general at California’s justice department, said Meta’s business model could besummed up as follows: “Hook the users; hold them for as long as they can; harvest their data; hide the truth from the public when making public statements.”

Meta knew about the addictive effects its platforms had on children’s mental health, O’Neill said, despite the company telling Congress and parents thatInstagramandFacebookwere safe. “All the while it hid the truth,” she said.

The first witness of the case, whistleblower and a former leader of Facebook’s Integrity and Care teamArturo Béjar, testified that Meta’s metric for measuring harm was “very narrow” and that the company under-reports the prevalence of harmful content.

Meta lawyerPaul Schmidtargued that the company has not targeted children and said he will present data that shows more than 90 percent of Facebook users are adults (he conceded Instagram skewed younger, but said the data was similar). Plus, he pointed to past statements fromMark Zuckerbergand Instagram headAdam Mosseristating the platforms were not designed to be addictive, and that research hasn’t yet supported the concept of social media addiction.

Why we’re following:Meta has been facing an onslaught of lawsuits over child safety. And it’s losing.

Just a few days ago, aNew Mexicocourtordered the companyto pay $567 million on top of the initial $375 million in civil penalties to fund the state’s abatement plan after the company was deemed to have contributed to a teen mental health crisis. In that trial, the judge called Meta a “public nuisance” akin to air pollution.

Separately in March, aLos Angelesjury found Meta andGoogleliable for a young woman’s depression and anxiety after she compulsively used social media as a child.

This landmark trial could also mean potential changes to Meta’s platforms, including a change in recommendation algorithms, parental verification, and the end of “autoplay” for video content.

What people are saying:Kentucky attorney generalRussell Colemanwas the latest tocompare this trialto the states’ success against tobacco companies in the 1990s: “AGs are in the perfect position to get this done. We did it with the Tobacco Settlement in the 1990s…We’ll do it again with Meta.”

Meta, for its part, has consistently denied the allegations. Schmidt painted the company as one that has actually dealt with its issues: “There can be no dispute that Meta has recognized people struggle, or can struggle, with their use of social media, and has come up with tools to try and address that.”

Meta’s motto was to “move fast and break things,” California attorney generalRob Bontasaid. “Unfortunately, the thing that was broken here was the mental health of our children.”

—Lindsey Choo

### Those good posts

For more good posts every day,follow Casey’s Instagram stories.

(Link)

(Link)

(Link)

### Talk to us

Send us tips, comments, questions, and LLM wiki suggestions:casey@platformer.news. Readour ethics policy here.