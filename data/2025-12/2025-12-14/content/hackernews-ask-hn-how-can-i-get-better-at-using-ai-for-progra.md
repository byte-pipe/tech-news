---
title: 'Ask HN: How can I get better at using AI for programming? | Hacker News'
url: https://news.ycombinator.com/item?id=46255285
site_name: hackernews
fetched_at: '2025-12-14T11:06:41.768043'
original_url: https://news.ycombinator.com/item?id=46255285
author: lemonlime227
date: '2025-12-14'
---

Hacker News
new
 |
past
 |
comments
 |
ask
 |
show
 |
jobs
 |
submit
login
Ask HN: How can I get better at using AI for programming?
344 points
 by
lemonlime227

19 hours ago

 |
hide
 |
past
 |
favorite
 |
356 comments
I've been working on a personal project recently, rewriting an old jQuery + Django project into SvelteKit. The main work is translating the UI templates into idiomatic SvelteKit while maintaining the original styling. This includes things like using semantic HTML instead of div-spamming, not wrapping divs in divs in divs, and replacing bootstrap with minimal tailwind. It also includes some logic refactors, to maintain the original functionality but rewritten to avoid years of code debt. Things like replacing templates using boolean flags for multiple views with composable Svelte components.

I've had a fairly steady process for doing this: look at each route defined in Django, build out my `+page.server.ts`, and then split each major section of the page into a Svelte component with a matching Storybook story. It takes a lot of time to do this, since I have to ensure I'm not just copying the template but rather recreating it in a more idiomatic style.This kind of work seems like a great use case for AI assisted programming, but I've failed to use it effectively. At most, I can only get Claude Code to recreate some slightly less spaghetti code in Svelte. Simple prompting just isn't able to get AI's code quality within 90% of what I'd write by hand. Ideally, AI could get it's code to something I could review manually in 15-20 minutes, which would massively speed up the time spent on this project (right now it takes me 1-2 hours to properly translate a route).Do you guys have tips or suggestions on how to improve my efficiency and code quality with AI?

bcherny

16 hours ago

 |
next

[–]

Hey, Boris from the Claude Code team here. A few tips:

1. If there is anything Claude tends to repeatedly get wrong, not understand, or spend lots of tokens on, put it in your CLAUDE.md. Claude automatically reads this file and it’s a great way to avoid repeating yourself. I add to my team’s CLAUDE.md multiple times a week.2. Use Plan mode (press shift-tab 2x). Go back and forth with Claude until you like the plan before you let Claude execute. This easily 2-3x’s results for harder tasks.3. Give the model a way to check its work. For svelte, consider using the Puppeteer MCP server and tell Claude to check its work in the browser. This is another 2-3x.4. Use Opus 4.5. It’s a step change from Sonnet 4.5 and earlier models.Hope that helps!

reply

epolanski

14 hours ago

 |
parent
 |
next

[–]

> If there is anything Claude tends to repeatedly get wrong, not understand, or spend lots of tokens on, put it in your CLAUDE.md. Claude automatically reads this file and it’s a great way to avoid repeating yourself.

Sure, for 4/5 interactions then will ignore those completely :)Try for yourself: add to CLAUDE.md an instruction to always refer to you as Mr. bcherny and it will stop very soon. Coincidentally at that point also loses tracks of all the other instructions.

reply

roughly

9 hours ago

 |
root
 |
parent
 |
next

[–]

One of the things you get an intuition for after using these systems is when to start a new conversation, and the basic rule of thumb is “always.” Use a conversation for one and only one task or question, and then start a new one. For longer projects, have the LLM write down a plan or checklist, and then have it tackle each step in a new conversation. The LLM context collapse happens well before you hit the token limits, and things like ground rules and whatnot stop influencing the LLMs outputs after a couple tens of thousands of tokens in my experience.

(Similar guidance goes for writing tools & whatnot - give the LLM exactly and only what it needs back from a tool, don’t try to make it act like a deterministic program. Whether or not they’re capital-I intelligent, they’re pretty fucking stupid.)

reply

bcherny

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yeah, adherence is a hard problem. It should be feeling much better in newer models, especially Opus 4.5. I generally find that Opus listens to me the first time.

reply

frankdenbow

11 hours ago

 |
root
 |
parent
 |
next

[–]

Have been using Opus 4.5 and can confirm this is how it feels, it just works.

reply

PufPufPuf

11 hours ago

 |
root
 |
parent
 |
next

[–]

It also works your wallet

reply

wyre

7 hours ago

 |
root
 |
parent
 |
next

[–]

Highly recommend Claude Max, but I also want to point out Opus 4.5 is the cheapest Opus has ever been.

(I just learned ChatGPT 5.2 Pro is $168/1mtok. Insanity.)

reply

fastball

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

If you pay for a Claude Max subscription it is the same price as previous models.

reply

shepherdjerred

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Just wait a few months -- AI has been getting more affordable _very_ quickly

reply

hamiecod

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I’ve felt that the LLM forgets CLAUDE.md after 4-5 messages. Then, why not reinject CLAUDE.md into the context at the fifth message?

reply

tclancy

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yes. One of my system-wide instructions is “Read the Claude.md file and any readme in the current directory, then tell me how you slept.”

If Claude makes a yawn or similar, I know it’s parsed the files. It’s not been doing so the last week or so, except for once out of five times last night.

reply

SV_BubbleTime

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The number of times I’ve written “read your own fucking Claude.md file” is a bit too numerous.

“You’re absolutely right! I see here you don’t want me to break every coding convention you have specified for me!”

reply

dayjah

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The Attention algo does that, it has a recency bias. Your observation is not necessarily indicative of Claude not loading CLAUDE.md.

I think you may be observing context rot? How many back and forths are you into when you notice this?

reply

Fargren

13 hours ago

 |
root
 |
parent
 |
next

[–]

That explains why it happens, but doesn't really help with the problem. The expectation I have as a pretty naive user, is that what is in the .md file should be permanently in the context. It's good to understand why this is not the case, but it's unintuitive and can lead to frustration. It's bad UX, if you ask me.

I'm sure there are workarounds such as resetting the context, but the point is that god UX would mean such tricks are not needed.

reply

girvo

13 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah the current best approach to aggressively compact and recreate context by starting fresh. It’s awkward and I wish I didn’t have to.

reply

toxic72

10 hours ago

 |
root
 |
parent
 |
next

[–]

I'm surprised this hasn't been been automated yet but I'm pretty naive to the space - the problem of "when?"/"how often?" seems like a fun one to chew on

reply

epolanski

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I know the reason, I just took the opportunity of answering to a claude dev to point out why it's no panacea and how this requires consistent context management.

Real semi-productive workflow is really a "write plans in markdowns -> new chat -> implement few things -> update plans -> new chat, etc".

reply

kotatsu_dog

6 minutes ago

 |
parent
 |
prev
 |
next

[–]

In addition, Having Claude Code's code and plans evaluated is very valid.
It makes calm decision for AI agents.

reply

keepamovin

7 hours ago

 |
parent
 |
prev
 |
next

[–]

This is cool, thank you!

Some things I found from my own interactions across multiple models (in addition to above):- It's basically all about the importance of (3). You need a feedback loop (we all do). and the best way is for it to change things and see the effects (ideally also against a good baseline like a test suite where it can roughly guage how close or far it is from the goal.) For assembly, a debugger/tracer works great (using batch-mode or scripts as models/tooling often choke on such interactivie TUI io).- If it keeps missing the mark tell it to decorate the code with a file log recording all the info it needs to understand what's happening. Its analysis of such logs normally zeroes the solution pretty quickly, especially for complex tasks.- If it's really struggling, tell it to sketch out a full plan in pseudocode, and explain why that will work, and analyze for any gotchas. Then to analayze the differences between the current implementation and the ideal it just worked out. This often helps get it unblocked.

reply

malloc2048

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Thank you for Claude Code (Web). Google has a similar offering with Google Jules. I got really, really bad results from Jules and was amazed by Claude Code when I finally discovered it.

I compared both with the same set of prompts and Claude Code seemed to be a senior expert developer and Jules, well don't know who be that bad ;-)Anyway, I also wanted to have persistent information, so I don't have to feed Claude Code the same stuff over and over again. I was looking for similar functionality as Claude projects. But that's not available for Claude Code Web.So, I asked Claude what would be a way of achieving pretty the same as projects, and it told me to put all information I wanted to share in a file with the filename:.clinerules. Claude told me I should put that file in the root of my repository.So please help me, is your recommendation the correct way of doing this, or did Claude give the correct answer?Maybe you can clear that up by explaining the difference between the two files?

reply

nl

10 hours ago

 |
root
 |
parent
 |
next

[–]

CLAUDE.md is the correct file for Claude.

reply

glamp

12 hours ago

 |
parent
 |
prev
 |
next

[–]

Hey Boris,

I couldn't agree more. And using Plan mode was a major breakthrough for me. Speaking of Plan Mode...I was previously using it repeatedly in sessions (and was getting great results). The most recent major release introduced this bug where it keeps referring back to the first plan you made in a session even when you're planning something else (https://github.com/anthropics/claude-code/issues/12505).I find this bug incredibly confusing. Am I using Plan Mode in a really strange way? Because for me this is a showstopper bug–my core workflow is broken. I assume I'm using Claude Code abnormally otherwise this bug would be a bigger issue.

reply

fourthark

6 hours ago

 |
root
 |
parent
 |
next

[–]

Yes as lostdog says, it’s a new feature that writes plans in plan mode to ~/.claude/plans. And it thinks it needs to continue the same plan that it started.

So you either need to be very explicit about starting a NEW plan if you want to do more than one plan in a session, or close and start a new session between plans.Hopefully this new feature will get less buggy. Previously the plan was only in context and not written to disk.

reply

manmal

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Why don’t you reset context when working on something else?

reply

mrieck

4 hours ago

 |
root
 |
parent
 |
next

[–]

It’s additional features that are related.

For example making a computer use agent… Made the plan, implementation was good, now I want to add a new tool for the agent, but I want to discuss best way to implement this tool first.Clearing context means Claude forgets everything about what was just built.Asking to discuss this new tool in plan mode makes Claude rewrite entire spec for some reason.As workaround, I tell Claude “looks good, delete the plan” before doing anything. I liked the old way where once you exit plan mode the plan is done, and next plan mode is new plan with existing context.

reply

lostdog

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yes, I've also been confused by things like this. Claude code is sometimes saving plans to ~/.claude/plans under animal names. But it's not really surface where the plan goes, not what the expected way to refer back to them is?

reply

moribvndvs

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Do you recommend having Claude dump your final plan into a document and having it execute from that piece by piece?

I feel like when I do plan mode (for CC and competing products), it seems good, but when I tell it to execute the output is not what we planned. I feel like I get slightly better results executing from a document in chunks (which of course necessitates building the iterative chunks into the plan).

reply

bcherny

2 hours ago

 |
root
 |
parent
 |
next

[–]

Since we released the last major version of Claude Code, Claude writes its plan to a file automatically for that reason! It also means you can continue to edit your plan as you go.

reply

scellus

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Opus 4.5 seems to be able to plan without asking, but I have used this pattern of "write a plan to an .md", review and maybe edit, and then execution, maybe in another thread,... I have used it with Codex and it works well.

Profilerating .md files need some attention though.

reply

hebrox

5 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I ask it to write a plan and when it starts the work, keep progress in another document and to never change the plan. If I didn't do this, somehow with each code change the plan document would grow and change. Keeping plan and progress separate prevented this from happening.

reply

justatdotin

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

a very common pattern is planner / executor.

yes the executor only needs the next piece of the plan.I tend to plan in an entirely different environment, which fits my workflow and has the added benefit of providing a clear boundary between the roles. I aim to spend far more time planning than executing. if I notice getting more caught up in execution than I expected, that's a signal to revise the plan.

reply

hamiecod

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I ask claude to dump the plan into a file and ensure that the tasks have been split into subtasks such that the description of each subtask meets the threshold such that the probability of the LLM misinterpreting is very low.

reply

danenania

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I often use multiple documents to plan things that are too large to fit into a single planning mode session. It works great.

You can also use it in conjunction with planning mode—use the documents to pin everything down at a high-to-medium level, then break off chunks and pass those into planning mode for fine-grained code-level planning and a final checking over before implementation.

reply

sahilagarwal

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Hi Boris,

If you wouldn't mind answering a question for me, it's one of the main things that has made me not add claude in vscode.I have a custom 'code style' system prompt that I want claude to use, and I have been able to add it when using claude in browser -```
Beautiful is better than ugly. Explicit is better than implicit.
Simple is better than complex. Complex is better than complicated.
Readability counts.
Special cases aren't special enough to break the rules. Although practicality beats purity.
If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.Trust the context you're given. Don't defend against problems the human didn't ask you to solve.
```How can I add it as a system prompt (or if its called something else) in vscode so LLMs adhere to it?

reply

bcherny

2 hours ago

 |
root
 |
parent
 |
next

[–]

Add it to your CLAUDE.md. Claude will automatically read that file every time it starts up

reply

scellus

3 hours ago

 |
parent
 |
prev
 |
next

[–]

In other words, permanent instructions and context well presented in *.md, planning and review before execution, agentic loops with feedback, and a good model.

You can do this with any agentic harness, just plain prompting and "LLM management skills". I don't have Claude Code at work, but all this applies to Codex and GH Copilot agents as well.And agreed, Opus 4.5 is next level.

reply

dotancohen

16 hours ago

 |
parent
 |
prev
 |
next

[–]

> I add to my team’s CLAUDE.md multiple times a week.How big is that file now? How big is too big?

reply

kxrm

15 hours ago

 |
root
 |
parent
 |
next

[–]

Something to keep in mind is if your CLAUDE.md file is getting large, consider alternative approaches especially for repeatable tasks. Using slash commands and skills for workflows that are repeatable is a really nice way to keep your rules file from exploding. I have slash commands for code review, and git commit management. I have skills for complex tool interactions. Our company has it's own deployment CLI tool so using skills to make Claude Code an expert at using this tool has done wonders to improve Claude Codes performance when working on CI/CD problems.

I am currently working on a new slash command /investigate <service> that runs triage for an active or past incident. I've had Claude write tools to interact with all of our partner services (AWS, JIRA, CI/CD pipelines, GitLab, Datadog) and now when an incident occurs it can quickly put together an early analysis of a incident finding the right people to involve (not just owners but people who last touched the service), potential root causes including service dependency investigations.I am putting this through it's paces now but early results are VERY good!

reply

bcherny

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Try to keep it under 1k tokens or so. We will show you a warning if it might be too big.

Ours is maybe half that size. We remove from it with every model release since smarter models need less hand-holding.You can also break up your CLAUDE.md into smaller files, link CLAUDE.mds, or lazy load them only when Claude works in nested dirs.https://code.claude.com/docs/en/memory

reply

bgilly

14 hours ago

 |
root
 |
parent
 |
next

[–]

I’ve been fine tuning mine pretty often. Do you have any Claude.md files you can share as good examples? Especially with opus 4.5.

And thank you for your work!! I focus all of my energy on helping families stay safe online, I make educational content and educational products (including software). Claude Code has helped me amplify my efforts and I’m able to help many more families and children as a result. The downstream effects of your work on Claude Code are awesome! I’ve been in IT since 1995 and your tools are the most powerful tools I’ve ever used, by far.

reply

blobbers

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

1k tokens, google says thats about 750 words. That's actually pretty short, any chance you could post a few samples of instructions or even link to a publicly available file CLAUDE.md you recommend?

reply

dotancohen

14 hours ago

 |
root
 |
parent
 |
next

[–]

That is seriously short. I've asked Claude Code to add instructions to CLAUDE.md and my one line request has resulted in tens of lines added to the file.

reply

hanska

13 hours ago

 |
root
 |
parent
 |
next

[–]

yes if you tell llm to do things it will be too verbose. either explicitly instruct the length ("add 5 lines bulletpoints, tldr format") or just write it yourself.

reply

blobbers

2 hours ago

 |
root
 |
parent
 |
next

[–]

Seems reasonable to give Claude instructions to be extra terse.

reply

tomviner

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

How do you know what to remove?

reply

tlarkworthy

13 hours ago

 |
parent
 |
prev
 |
next

[–]

also after you have a to-and-fro to course correct it on a task, run this self-reflection prompt

https://gist.github.com/a-c-m/f4cead5ca125d2eaad073dfd71efbc...That will moves stuff that required manually clarifying back into the claude.md (or a useful subset you pick). It does a much better job of authoring claude.md than I do.

reply

Etheryte

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Hah, that's funny. Claude can't help but mess all the comments in the code up even if I explicitly tell it to not change any comments five times. That's literally the experience I had before opening this thread, never mind how often it completely ignores CLAUDE.md.

reply

seinecle

1 hour ago

 |
parent
 |
prev
 |
next

[–]

And if I may, these advice also apply if you choose Cursor as a coding environment.

reply

mraza007

6 hours ago

 |
parent
 |
prev
 |
next

[–]

+1 on that
Opus 4.5 is a game changer
I have used to refactor and modernize one of my old react project using bootstrap,
You have to be really precise when prompting and having solid CLAUDE.md works really well

reply

cafebeen

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Thanks for your work great work on Claude Code!

One other feature with CLAUDE.md I’ve found useful is imports: prepending @ to a file name will force it to be imported into context. Otherwise, whether a file is read and loaded to context is dependent on tool use and planning by the agent (even with explicit instructions like “read file.txt”). Of course this means you have to be judicial with imports.

reply

dmd

14 hours ago

 |
parent
 |
prev
 |
next

[–]

I would LOVE to use Opus 4.5, but it means I (a merely Pro peon) can work for maybe 30 minutes a day, instead of 60-90.

reply

koolba

6 hours ago

 |
root
 |
parent
 |
next

[–]

I’m old enough to remember being able to work at programming related tasks without any such tools. Is that not still a thing?

reply

matt3210

14 hours ago

 |
parent
 |
prev
 |
next

[–]

I’ve yet to see any real work get done with agents. Can you share examples or videos of real production level work getting done? Maybe in a tutorial format?

My current understanding is that it’s for demos and toy projects

reply

MontyCarloHall

12 hours ago

 |
root
 |
parent
 |
next

[–]

Good question. Why hasn't there been a profusion of new game-changing software, fixes to long-standing issues in open-source software, any nontrivial shipped product at all? Heck, why isn't there a cornucopia of new apps, even trivial ones? Where is all the shovelware [0]? Previous HN discussion here [1].

Don't get me wrong, AI is at least as game-changing for programming as StackOverflow and Google were back in the day. I use it every day, and it's saved me hours of work for certain specific tasks [2]. But it's simply not a massive 10x force multiplier that some might lead you to believe.I'll start believing when maintainers of complex, actively developed, and widely used open-source projects (e.g. ffmpeg, curl, openssh, sqlite) start raving about a massive uptick in positive contributions, pointing to a concrete influx of high-quality AI-assisted commits.[0]https://mikelovesrobots.substack.com/p/wheres-the-shovelware...[1]https://news.ycombinator.com/item?id=45120517[2]https://news.ycombinator.com/item?id=45511128

reply

jerf

10 hours ago

 |
root
 |
parent
 |
next

[–]

"Heck, why isn't there a cornucopia of new apps, even trivial ones?"

There is. We had to basically create a new category for them on /r/golang because there was a quite distinct step change near the beginning of this year where suddenly over half the posts to the subreddit were "I asked my AI to put something together, here's a repo with 4 commits, 3000 lines of code, and an AI-generated README.md. It compiles and I may have even used it once or twice." It toned down a bit but it's still half-a-dozen posts a day like that on average.Some of them are at least useful in principle. Some of them are the same sorts of things you'd see twice a month, only now we can see them twice a week if not twice a day. The problem wasn't necessarily the utility or the lack thereof, it was simply thefloodof them. It completely disturbed the balance of the subreddit.To the extent that you haven't heard about these, I'd observe that the world already had more apps than you could possibly have ever heard about and the bottleneck was already marketing rather than production. AIs have presumably not successfully done much about helping people market their creations.

reply

agumonkey

46 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Disclaimer: I am not promoting llms.

There was a GitHub PR on the ocaml project where someone crafted a long feature (mac silicon debugging support). The pr was rejected because nobody wanted to read it for it was too long. Seems to me that society is not ready for the width of output generated this way. Which may explain the lack of big visible change so far. But I already see people deploying tiny apps made by Claude in a day.It's gonna be weird...

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Well, the LLM industry is not completely without results. We do have ever increasing frequency of outages in major Internet services...Somehow correlates with the AI mandates major tech corps seem to pushing now internally.

reply

amirhirsch

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The effect of these tools is people losing their software jobs (down 35% since 2020). Unemployed devs aren’t clamoring to go use AI on OSS.

reply

majewsky

9 hours ago

 |
root
 |
parent
 |
next

[–]

Wasn't most of that caused by that one change in 2022 to how R&D expenses are depreciated, thus making R&D expenses (like retaining dev staff) less financially attractive?

Context: This news storyhttps://news.ycombinator.com/item?id=44180533

reply

amirhirsch

6 hours ago

 |
root
 |
parent
 |
next

[–]

Probably also end of ZIRP and some “AI washing” to give the illusion of progress

reply

agumonkey

44 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I keep asking chatgpt when will LLM reach 95% software creation automation, answer is ten years.

reply

KetoManx64

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Same thing happened to farmers during the industrial revolution, same thing happened to horse drawn carriage drivers, same thing happened to accountants when Excel came along, mathmaticins, and on and on the list goes. Just part of human peogress.

reply

cageface

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

As another example, the MacApps Reddit has been flooded with new apps recently.

reply

cachvico

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Here's one -
https://apps.apple.com/us/app/pistepal/id6754510927

The app is definitely still a bit rough around the edges but it was developed in breakneck speed over the last few months - I've probably seen an overall 5x acceleration over pre-agentic development speed.

reply

spreiti

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I use GitHub Copilot in Intellij with Claude Sonnet and the plan mode to implement complete features without me having to code anything.

I see it as a competent software developer but one that doesn't know the code base.I will break down the tasks to the same size as if I was implementing it. But instead of doing it myself, I roughly describe the task on a technical level (and add relevant classes to the context) and it will ask me clarifying questions. After 2-3 rounds the plan usually looks good and I let it implement the task.This method works exceptionally well and usually I don't have to change anything.For me this method allows me to focus on the architecture and overall structure and delegate the plumbing to Copilot.It is usually faster than if I had to implement it and the code is of good quality.The game changer for me was plan mode. Before it, with agent mode it was hit or miss because it forced me to one shot the prompt or get inaccurate results.

reply

madcocomo

8 hours ago

 |
root
 |
parent
 |
next

[–]

My experience is that GitHub Copilot works much better in VS Code than Intellij. Now I have to open them together to work on one single project.

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yeah, but what did you produce with it in the end? Show us the end result please.

reply

williamcotton

12 hours ago

 |
root
 |
parent
 |
next

[–]

I've been writing an experimental pipeline-based web app DSL with Claude Code for the last little while in my spare time. Sort of bash-like with middleware for lua, jq, graphql, handlebars, postgres, etc.

Here's an already out of date and unfinished blog post about it:https://williamcotton.com/articles/introducing-web-pipeHere's a simple todo app:https://github.com/williamcotton/webpipe/blob/webpipe-2.0/to...Check out the BDD tests in there, I'm quite proud of the grammar.Here's my blog:https://github.com/williamcotton/williamcotton.com/blob/mast...It's got an LSP as well with various validators, jump to definitions, code lens and of course syntax highlighting.I've yet to take screenshots, make animated GIFs of the LSP in action or update the docs, sorry about that!A good portion of the code has racked up some tech debt, but hey, it's an experiment. I just wanted to write my own DSL for my own blog.

reply

spreiti

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I cannot show it because the code belongs to my employer.

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
next

[–]

Ah yes of course. But no one asked for the code really. Just show us the app. Or is it some kinda super-duper secret military stuff you are not even supposed to discuss, let alone show.

reply

spreiti

4 hours ago

 |
root
 |
parent
 |
next

[–]

It is neither of these. It's an application that processes data and is not accessible outside of the companies network. Not everything is an app.

I described my workflow that has been a game changer for me, hoping it might be useful to another person because I have struggled to use LLMs for more than a Google replacement.As an example, one task of the feature was to add metrics for observability when the new action was executed. Another when it failed.My prompt: Create a new metric "foo.bar" in MyMetrics when MyService.action was successful and "foo.bar.failed" when it failed.I review the plan and let it implement it.As you can see it's a small task and after it is done I review the changes and commit them. Rinse and repeat.I think the biggest issue is that people try to one shot big features or applications. But it is much more efficient to me to treat Copilot as a smart pair programming partner. There you also think about and implement one task after the other.

reply

PaulHoule

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I use Junie to get tasks done all the time. For instance I had two navigation bars in an application which had different styling and I told it make the second one look like the first and... it made a really nice patch. Also if I don't understand how to use some open source dependency I check the project out and ask Junie questions about it like "How do I do X?" or "How does setting prop Y have the effect of Z?" and frequently I get the right answer right away. Sometimes I describe a bug in my code and ask if it can figure it out and often it does, ask for a fix and often get great results.

I have a React application where the testing situation is FUBAR, we are stuck on an old version of React where tests like enzyme that really run react are unworkable because the test framework can never know that React is done rendering -- working with Junie I developed a style of true unit tests for class components (still got 'em) that tests tricky methods in isolation. I have a test file which is well documented explaining the situation around tests and ask "Can we make some tests for A like the tests in B.test.js, how would you do that?" and if I like the plan I say "make it so!" and it does... frankly I would not be writing tests if I didn't have that help. It would also be possible to mock useState() and company and might do that someday... It doesn't bother me so much that the tests are too tightly coupled because I can tell Junie to fix or replace the tests if I run into trouble.For me the key things are: (1) understanding from a project management perspective how to cut out little tasks and questions, (2) understanding enough coding to know if it is on the right track (my non-technical boss has tried vibe coding and gets nowhere), (3) accepting that it works sometimes and sometimes it doesn't, and (4) recognizing context poisoning -- sometimes you ask it to do something and it gets it 95% right and you can tell it to fix the last bit and it is golden, other times it argues or goes in circles or introduces bugs faster than it fixes them and as quickly as you can you recognize that is going on and start a new session and mix up your approach.

reply

matt3210

13 hours ago

 |
root
 |
parent
 |
next

[–]

Manually styling two similar things the same way is a code smell. Ask the ai to make common components and use them for both instead of brute forcing them to look similar.

reply

PaulHoule

13 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, I thought about this in that case. I tend to think the way you do to the extent that it is sometimes a source of conflict with other people I work with.

These navbars are similar but not the same, both have a pager but they have other things, like one has some drop downs and the other has a text input. Styled "the same" means the line around the search box looks the same as the lines around the numbers in the pager, and Junie got that immediately.In the end the patch touched css classes in three lines of one file and added a css rule -- it had the caveat that one of the css classes involved will probably go away when the board finally agrees to make a visual change we've been talking about for most of a year but I left a comment in the first navbar warning about that.There are plenty of times I ask Junie to try to consolidate multiple components or classes into one and it does that too as directed.

reply

commanderkeen08

12 hours ago

 |
root
 |
parent
 |
next

[–]

https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/...
 That’s what slots are for

reply

matt3210

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This is a lot of good reasons not to use it yet IMO

reply

danenania

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I know of many experienced and capable engineers working on complex stuff who are driving basically all their development through agents. This includes production level work. This is the norm now in the SV startup world at least.

You don't just YOLO it. You do extensive planning when features are complex, and you review output carefully.The thing is, if the agent isn't getting it to the point where you feel like you might need to drop down and edit manually, agents are now good enough to do those same "manual edits" with nearly 100% reliability if you are specific enough about what you want to do. Instead of "build me x, y, z", you can tell it to rename variables, restructure functions, write specific tests, move files around, and so on.So the question isn't so much whether to use an agent or edit code manually—it's what level of detail you work at with the agent. There are still times where it's easier to do things manually, but you never reallyneedto.

reply

matt3210

14 hours ago

 |
root
 |
parent
 |
next

[–]

Can you show some example? I feel like there would be streams or YouTube lets plays on this if it was working well

reply

sixtyj

13 hours ago

 |
root
 |
parent
 |
next

[–]

I would like to see it as well. It seems to me that everybody sells shovels only. But nobody haven’t seen gold yet. :)

reply

shsush

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The real secret to agent productivity is letting go of your understanding of the code and trusting the AI to generate the proper thing. Very pro agent devs like ghuntley will all say this.

And it makes sense. For most coding problems the challenge isn’t writing code. Once you know what to write typing the code is a drop in the bucket. AI is still very useful, but if you really wanna go fast you have to give up on your understanding. I’ve yet to see this work well outside of blog posts, tweets, board room discussions etc.

reply

submain

12 hours ago

 |
root
 |
parent
 |
next

[–]

> The real secret to agent productivity is letting go of your understanding of the code and trusting the AI to generate the proper thing

The few times I've done that, the agent eventually faced a problem/bug it couldn't solve and I had to go and read the entire codebase myself.Then, found several subtle bugs (like writing private keys to disk even when that was an explicit instruction not to). Eventually ended up refactoring most of it.It does have value on coming up with boilerplate code that I then tweak.

reply

maplethorpe

11 hours ago

 |
root
 |
parent
 |
next

[–]

You made the mistake of looking at the code, though. If you didn't look at the code, you wouldn't have known those bugs existed.

reply

PunchyHamster

8 hours ago

 |
root
 |
parent
 |
next

[–]

fixing code
now
 is orders of magnitude cheaper than fixing it in month or two when it hits production.

which might be fineif you're doing proof of concept or low risk code, but it can also bite you hard when there is a bug actively bleeding money and not a single person or AI agent in the house that knows how anything work

reply

urig

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

That's just irresponsible advice. There is so little actual evidence of this technology being able to produce high quality maintainable code that asking us to trust it blindly is borderline snake-oil peddling.

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
next

[–]

Not borderline - it is just straight snake-oil peddling.

reply

_zoltan_

10 hours ago

 |
root
 |
parent
 |
next

[–]

yet it works? where have you been for the last 2 years?

calling this snake oil is like when the horse carriage riders were against cars.

reply

hansmayer

3 hours ago

 |
root
 |
parent
 |
next

[–]

I am an early adopter since 2021 buddy. "It works" for trivial use-cases, for anything more complex it is utter crap.

reply

Kubuxu

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I don’t see how I would feel comfortable pushing the current output of LLMs into high-stakes production (think SLAs, SRE).

Understanding of the code in these situation is more important than the code/feature existing.

reply

shsush

12 hours ago

 |
root
 |
parent
 |
next

[–]

I agree and am the same. Using them to enhance my knowledge and as well as autocomplete on steroids is the sweet spot. Much easier to review code if im “writing” it line by line.

I think the reality is a lot of code out there doesn’t need to be good, so many people benefit from agents etc.

reply

danenania

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You can use an agent while still understanding the code it generates in detail. In high stakes areas, I go through it line by line and symbol by symbol. And I rarely accept the first attempt. It’s not very different from continually refining your own code until it meets the bar for robustness.

Agents make mistakes which need to be corrected, but they also point out edge cases you haven’t thought of.

reply

Kubuxu

1 hour ago

 |
root
 |
parent
 |
next

[–]

Definitely agreed, that is what I do as well.
At that point you have good understanding of that code, which is in contrast to what the post I responded suggests.

reply

heavyset_go

9 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

>
The real secret to agent productivity is letting go of your understanding of the code

This is negligence, it's your job to understand the system you're building.

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Not to blow your bubble, but I've seen agents expose Stripe credentials by hardcoding them as text into a react frontend app, so, no kids, do not "let go" of code understanding, lest you want to appear as the next story along the lines of "AI dropped my production database".

reply

yonaguska

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This is sarcasm right?

reply

PunchyHamster

8 hours ago

 |
root
 |
parent
 |
next

[–]

I wish, that's dev brain on AI sadly.

We've been unfucking architecture done like that for amonthafter the dev that had hallucination session with their AI left.

reply

danenania

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

A lot of that would be people working on proprietary code I guess. And most of the people I know who are doing this are building stuff, not streaming or making videos. But I'm sure there must be content out there—none of this is a secret. There are probably engineers working on open source stuff with these techniques who are sharing it somewhere.

reply

matt3210

13 hours ago

 |
root
 |
parent
 |
next

[–]

That’s understandable, I also wouldn’t stream my next idea for everyone to see

reply

dmurvihill

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Let’s see it then

reply

_zoltan_

10 hours ago

 |
root
 |
parent
 |
next

[–]

go on reddit and you can see a million of these vibe coded codebases. is that not good enough?

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

+1 here. Lets see those productivity gains!

reply

kelvinjps10

10 hours ago

 |
parent
 |
prev
 |
next

[–]

How do you make Claude code to choose opus and not sonnet? For me it seems to do it automatically

reply

fastball

9 hours ago

 |
root
 |
parent
 |
next

[–]

/model

reply

goalieca

16 hours ago

 |
parent
 |
prev
 |
next

[–]

> I add to my team’s CLAUDE.md multiple times a week.

This concerns me because fighting tooling is not a positive thing. It’s very negative and indicates how immature everything is.

reply

jedberg

16 hours ago

 |
root
 |
parent
 |
next

[–]

The Claude MD is like the documentation you hand to a new engineer on your team that explains details about your code that they wouldn't otherwise know. It's not bad to need one.

reply

thfuran

15 hours ago

 |
root
 |
parent
 |
next

[–]

But that documentation shouldn’t need to be updated nearly every other day.

reply

Bjartr

15 hours ago

 |
root
 |
parent
 |
next

[–]

Consider that every time you start a session with Claude Code. It's effectively a new engineer. The system doesn't learn like a real person does, so for it to improve over time you need to manually record the insights that for a normal human would be integrated by the natural learning process.

reply

majewsky

9 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, that's exactly the problem. There's good reasons why any particular team doesn't onboard new engineers each day, going all the way back to Fred Brooks and "adding more people to a late project makes it later".

reply

newsoftheday

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Reminds me of that Nicole Kidman movie Before I Go to Sleep.

reply

handfuloflight

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Sleep time compute architectures are changing this.

reply

bdangubic

9 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

there are many tools available that work towards solving this problem

reply

Marsymars

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I certainly
could
 be updating the documentation for new devs very frequently - the problem with devs is that they don't bother reading the documentation.

reply

PunchyHamster

8 hours ago

 |
root
 |
parent
 |
next

[–]

and the other problem - when they see something is wrong/out of date, they don't update it...

reply

kxrm

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

If you are consistent with how you do your projects you shouldn't need to update CLAUDE.md nearly every day. Early on, I was adjusting it nearly every day for maybe a couple of projects but now I have very little need to make any adjustments.

Often the challenge is users aren't interacting with Claude Code about their rules file. If Claude Code doesn't seem to be working with you ask it why it ignore a rule. Often times it provides very useful feedback to adjust the rules and no longer violate them.Another piece of advice I can give is to clear your context window often! Early in my start in this I was letting the context window auto compact but this is bad! Your model is it's freshest and "smartest" when it has a fresh context window.

reply

nrds

14 hours ago

 |
root
 |
parent
 |
next

[–]

It takes a lot of uncached tokens to let it learn about your project again.

reply

udfalkso

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Same thing happens every time a new hire joins the team. Lots of documentation is stale and needs updating as they onboard.

reply

jm4

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It does if it’s incomplete or otherwise doesn’t accurately convey what people need to know.

reply

Gud

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Why not?

reply

bitwize

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Have you never looked at your work's Confluence? Worse, have you never spent time at a company where the documentation
wasn't
 frequently updated?

reply

bcherny

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You might be misunderstanding what a CLAUDE.md is. It’s not about fighting the model, rather it’s giving the model a shortcut to get the context it needs to do its work. You don’t have to have one. Ours is 100% written by Claude itself.

reply

seunosewa

15 hours ago

 |
root
 |
parent
 |
next

[–]

That's not the same thing as adding rules by yourself based on your experiences with Claude.

reply

kidbomb

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Does the same happens if I create an AGENTS.md instead?

reply

red2awn

15 hours ago

 |
root
 |
parent
 |
next

[–]

Claude Code does not support AGENTS.md, you can symlink it to CLAUDE.md to workaround it. Anthropic: pls support!

reply

esafak

6 hours ago

 |
root
 |
parent
 |
next

[–]

https://github.com/anthropics/claude-code/issues/6235

reply

kevinherron

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Use AGENTS.md for everything, then put a single line in CLAUDE.md:

@AGENTS.md

reply

handfuloflight

13 hours ago

 |
root
 |
parent
 |
next

[–]

Get a grep!

reply

ed4bb9fb7c

6 hours ago

 |
parent
 |
prev
 |
next

[–]

> 1. If there is anything Claude tends to repeatedly get wrong, not understand, or spend lots of tokens on, put it in your CLAUDE.md.

What a joke. Claude regularly ignores the file. It is a toss up: we were playing a game at work to guess which items will it forget first: to run tests, formatter, linter etc. This is despite items saying ABSOLUTELY MUST, you HAVE To and so long.I have cancelled my Claude Max subscription. At least Codex doesn’t tell me that broken tests are unrelated to its changes or complain that fixing 50 tests is too much work.

reply

nrds

15 hours ago

 |
parent
 |
prev
 |
next

[–]

> Use Opus 4.5.

This drives up price faster than quality though. Also increases latency.

reply

sothatsit

14 hours ago

 |
root
 |
parent
 |
next

[–]

Opus 4.5 is significantly better if you can afford it.

They also recently lowered the price for Opus 4.5, so it is only 1.67x the price of Sonnet, instead of 5x for Opus 4.

reply

minimaxir

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

There's a counterintuitive pricing aspect of Opus-sized LLMs in that they're so much smarter that in some cases, it can solve the problem faster and with much fewer tokens that it can end up being cheaper.

reply

bakugo

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Obviously the Anthropic employee advertising their product wants you to pay as much as possible for it.

reply

handfuloflight

13 hours ago

 |
root
 |
parent
 |
next

[–]

The generosity of the Max plans indicates otherwise.

reply

bakugo

11 hours ago

 |
root
 |
parent
 |
next

[–]

God bless these generously benevolent corporations, giving us such amazing services for the low low price of only $200 per month. I'm going to subscribe right now! I almost feel bad, it's like I'm stealing from them.

reply

handfuloflight

11 hours ago

 |
root
 |
parent
 |
next

[–]

That $200 a month is getting me $2000 a month in API equivalent tokens.

I used to spend $200+ an hour on a single developer. I'm quite sure that benevolence was a factor when they submitted me an invoice, since there is no real transparency if I was being overbilled or not or that the developer acted in my best interest rather than theirs.I'll never forget that one contractor who told me he took a whole 40 hours to do something he could have done in less than that, specifically because I allocated that as an upperbound weekly budget to him.

reply

bakugo

9 hours ago

 |
root
 |
parent
 |
next

[–]

> That $200 a month is getting me $2000 a month in API equivalent tokens.

Do you ever feel bad for basically robbing these poor people blind? They're clearly losing so much money by giving you $1800 in FREE tokens every month. Their business can't be profitable like this, but thankfully they're doing it out of the goodness of their hearts.

reply

handfuloflight

9 hours ago

 |
root
 |
parent
 |
next

[–]

I'm not sure that you actually expect to be taken seriously if you're going to assert that these companies don't have costs themselves to deliver their services.

reply

cerved

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Hey Boris, can you teach CC how to use cd?

reply

jcheng

11 hours ago

 |
root
 |
parent
 |
next

[–]

Personally, CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1 made all my cd problems go away (which were only really in cmake-based projects to begin with).

reply

matt3210

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Does all my code get uploaded to the service?

reply

jMyles

12 hours ago

 |
parent
 |
prev
 |
next

[–]

3. Puppeteer? Or Playwright? I haven't been able to make Puppeteer work for the past 8 weeks or so ("failed to reconnect"). Do you have a doc on this?

reply

cebert

10 hours ago

 |
root
 |
parent
 |
next

[–]

I know the Playwright MCP server works great. I use it daily.

reply

jMyles

10 hours ago

 |
root
 |
parent
 |
next

[–]

Same, I use Playwright all the time, but haven't been able to make puppeteer work in quite some time. Playwright, while reliable in terms of features, just absolutely eats the heck out of context.

reply

cebert

8 hours ago

 |
root
 |
parent
 |
next

[–]

I’ve heard folks claim the Chrome DevTools MCP eats less context, but I don’t know how accurate that is.

reply

hansmayer

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Hey Boris from the Claude Code team - could you guys please be so kind so as to stop pushing that narrative about CLAUDE.md, either yourselves or through influencers and GenAI-grifters? The reason being, it is simply not true. A lot of the time the instructions will be ignored. Actually, the term "ignored" is putting the bar too high, because your tool does not intentionally "ignore", not having sentience and knowledge. We experience the effects of the instructions being ignored, because your software is not deterministic, its merely guessing the next token, and sometimes those instructions tacked onto the rest of the context statistically do not match what we as humans expect to see (while its perfectly logical for your machine learning text generator, based on the datasets it was trained on).

reply

blitz_skull

12 hours ago

 |
root
 |
parent
 |
next

[–]

This seems pretty aggressive considering this is all just personal anecdote.

I update my CLAUDE.md all the time and notice the effects.Why all the snark?

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
next

[–]

Is it really just a personal anecdote ? Please do read some other comments on this post. The snark comes from everyone and their mother recommending "just write CLAUDE.md", when it is clear that this technology does not have intrinsic capability to perform reliable outputs based on human language input.

reply

blitz_skull

12 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah… that’s the point of LLMs: variable output. If you’re using them for 100% consistent output, you’re using the wrong tool.

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
next

[–]

Is it? So you are saying software should not be consistent? Or that LLMs should not be used for software development, aside from toy-projects?

reply

simonw

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

CLAUDE.md is read on session startup.

If you're continually finding that it's being forgotten, maybe you're not starting fresh sessions often enough.

reply

hansmayer

12 hours ago

 |
root
 |
parent
 |
next

[–]

I should not have to
fight
 tooling, especially the supposedly "intelligent" one. What's the point of it, if we have to always adapt to the tool, instead of the other way around?

reply

kfajdsl

11 hours ago

 |
root
 |
parent
 |
next

[–]

It's a tool. The first time you used a shell you had to learn it. The first time you used a text editor you had to learn it.

You can learn how to use it, or you can put it down if you think it doesn't bring you any benefit.

reply

PunchyHamster

8 hours ago

 |
root
 |
parent
 |
next

[–]

even shell remembers my commands...

reply

hansmayer

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I am sorry but what do I have to learn? That the tool does not work as advertised? That sometimes it will work as advertised, sometimes not? That it will sometimes expose critical secrets as plain text and some other time suggest to solve a problem in a function by removing the function code completely? What are you even talking about, comparing to shell and text editors? These are still bloody deterministic tools. You learn how they work and the usage does not change unpredictably every day! How can you learn something that does not have predictable outputs?

reply

simonw

10 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, you have to learn those things. LLMs are hard to use.

So are animals, but we've used dogs and falcons and truffle hunting pigs as tools for thousands of years.Non-deterministic tools are still tools, they just take a bunch more work to figure out.

reply

xn

9 hours ago

 |
root
 |
parent
 |
next

[–]

It's like having Michael Jordan with dementia on your team. You start out mesmerized by how many points he can score, and then you get incredibly frustrated that he forgets he has to dribble and shoot into the correct hoop.

reply

hansmayer

3 hours ago

 |
root
 |
parent
 |
next

[–]

Spot on. Not to mention all the fouls and traveling the demented "all star" makes for your team, effectively negating any point gains.

reply

hansmayer

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

No, please, stop misleading people Simon. People use tools to make things easier for them, not harder. And a tool which I cannot steer predictably is not a god damn tool at all! The sheer persistence the AI-promoters like you are willing to invest just to gaslight us all into thinking we were dumb and did not know how to use the shit-generators is really baffling. Understand that a lot of us are early adopters and we see this shit for what it is - the most serious mess up of the "Big Tech" since Zuckerberg burned 77B for his metaverse idiocy. By the way - animals are not tools. People do not use them - they engage with them as helpers, companions and for some people, even friends of sorts. Drop your LLM and try engaging with someone who has a hunting dog for example - they'd be quite surprised if you referred to their beloved retriever as a "tool". And you might learn something about a real intelligence.

reply

simonw

3 hours ago

 |
root
 |
parent
 |
next

[–]

Your insistence that LLMs are not useful tools is difficult for me to empathize with as someone who has been using them successfully as useful tools for several years - and sharing in great detail how I am using them.

https://simonwillison.net/2025/Dec/10/html-tools/is the37th postin my series about this:https://simonwillison.net/series/using-llms/https://simonwillison.net/2025/Mar/11/using-llms-for-code/is probably still my most useful of those.I know you absolutely hate being told you're holding them wrong... but you're holding them wrong.They're not nearly as unpredictable as you appear to think they are.One of us is misleading people here, and I don't think it's me.

reply

hansmayer

2 hours ago

 |
root
 |
parent
 |
next

[–]

> One of us is misleading people here, and I don't think it's me.

Firstly, I am not the one with an LLM-influencer side-gig. Secondly - No sorry, please don't move the goalposts. You did not answer my main argument - which is - how does a "tool" which constantly change its behaviour deserve being called a tool at all? If a tailor had scissors which cut the fabric sometimes just a bit, and sometimes completely differently every time they used it, would you tell the tailor he is not using them right too? Thirdly you are now contradicting yourself. First you said we need to live with the fact that they are un-predictable. Now you are sugarcoating it into being "a bit unpredictable", or "not as nearly unpredictable". I am not sure if you are doing this intentionally or do you really want to believe in the "magic" but either way you are ignoring the ground tenets of how this technology works. I'd be fine if they used it to generate cheap holiday novels or erotica - but clearly after four years of experimenting with the crap machines to write code created a huge pushback in the community - we don't need the proverbial scissors which cut our fabric differently each time!

reply

simonw

1 hour ago

 |
root
 |
parent
 |
next

[–]

> how does a "tool" which constantly change its behaviour deserve being called a tool at all?

Let's go with blast furnaces. They're definitely tools. They change over time - a team might constantly run one for twenty years but still need to monitor and adjust how they use it as the furnace itself changes behavior due to wear and tear (I think they call this "drift".)The same is true of plenty of other tools - pottery kilns, cast iron pans, knife sharpening stones. Expert tool users frequently use tools that change over time and need to be monitored and adjusted.I do think dogs and horses other animal tools remain an excellent example here as well. They're unpredictable and you have to constantly adapt to their latest behaviors.I agree that LLMs are unpredictable in that they are non-deterministic by nature. I also think that this is something you can learn to account for as you build experience.I just fed this prompt to Claude Code:Add to_text() and to_markdown() features to justhtml.html - for the whole document or for CSS selectors against it

 Consult a fresh clone of the justhtml Python library (in /tmp) if you need toIt did exactly what I expected it would do, based on my hundred of previous similar interventions with that tool:https://github.com/simonw/tools/pull/162

reply

exasperaited

8 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> So are animals, but we've used dogs and falcons and truffle hunting pigs as tools for thousands of years.

Dogs learn their jobs way faster, more consistently and more expressively than any AI tool.Trivially, dogs understand "good dog" and "bad dog" for example.Reinforcement learning with AI tooling clearly seems not to work.

reply

simonw

7 hours ago

 |
root
 |
parent
 |
next

[–]

> Dogs learn their jobs way faster, more consistently and more expressively than any AI tool.

That doesn't match my experience with dogs or LLMs at all.

reply

hansmayer

2 hours ago

 |
root
 |
parent
 |
next

[–]

Ever heard of service dogs? Or police dogs? Now tell me, when will LLMs ever be safe to be used as assistance to blind people? Or will the big tech at some point release some sloppy blind-people-tool based on LLMs and unleash the LLM-influencers like yourself to start gaslighting the users into thinking they were "not holding it right" ? For mission and life critical problems, I'll take a dog any day, thank you very much!

reply

simonw

1 hour ago

 |
root
 |
parent
 |
next

[–]

I've talked to a few people who are blind about vision LLMs and they're very, very positive about them.

They fully understand their limitations. Users of accessibility technology are extremely good at understanding the precise capabilities of the tools they use - which reminds me that screenreaders themselves are a great example of unreliable tools due to the shockingly bad web apps that exist today.I've also discussed the analogy to service dogs with them, which they found very apt given how easily their assistive tool could be distracted by a nearby steak.The one thing people who use assistive technology donotappreciate is being told that they shouldn't try a technology out themselves because it's unreliable and hence unsafe for them to use!

reply

baq

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You’ve asked the right questions and don’t want to find the answers. It’s on you.

reply

exasperaited

9 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I understand you're trying to be helpful but the number of "you're holding it wrong" things I read about this tool — any AI tool — just makes me wonder who vibe coders are really doing all this unpaid work for.

reply

prisenco

5 hours ago

 |
prev
 |
next

[–]

Everyone's suggestions feel designed to frustrate me. Instructions on how to cajole and plead that seem more astrology than engineering.

This is the pattern I settled on about a year ago. I use it as a rubber-duck / conversation partner for bigger picture issues. I'll run my code through it as a sanity "pre-check" before a pr review. And I mapped autocomplete to ctrl-; in vim so I only bring it up when I need it.Otherwise, I write everything myself. AI written code never felt safe. It adds velocity but velocity early on always steals speed from the future. That's been the case for languages, for frameworks, for libraries, it's no different for AI.In other words, you get better at using AI for programming by recognizing where its strengths lie and going all in on those strengths. Don't twist up in knots trying to get it to do decently what you can already do well yourself.

reply

sahilagarwal

4 hours ago

 |
parent
 |
next

[–]

Same. AI is a good tool to use as a sounding board and conversation partner.

I only access claude and others using my browser - I give it a snippet of my code, tell it what exactly I want to do and what my general goal is, then ask it to give me approaches, and their pros and cons.Even if someone wants to use AI to code for them, its still better to do the above as a first step imo. A sort of human in the loop system.> It adds velocity but velocity early on always steals speed from the future. That's been the case for languages, for frameworks, for libraries, it's no different for AI.Completely agree. I'm seeing this in my circle and workplace. My velocity might be a tad bit slower than the rest of my peers when you compare it per ticket. But my long tern output hasn't changed and interestingly, neither has anyone else's.As an aside, I like your system of completely removing autocomplete unless you need it - may be something like that would finally get me to enable AI in my IDE.

reply

avereveard

2 hours ago

 |
parent
 |
prev
 |
next

[–]

> how to cajole and plead

When a new person join the team you need to tell them the local coding standard. I don't see why people expect llm to work out of the box instead. The difference is you have to do it at every exchange as llm are stateless.But yeah I mostly agree with the rest llm work best at very low lewel method by method where you can watch like an hawk they don't introduce silent failure condutions and super high level as system design as reasoning engine, and they still do not so good job at implementing components whole.

reply

ehnto

2 hours ago

 |
root
 |
parent
 |
next

[–]

Both human and AI should be able to understand the "way we do things around here" by reading the existing code. I could spend an hour telling someone how to write idiomatic code, and they will forget all of it until they actually do some work and see the codebase.

When Claude reads a significant portion of my codebase into context it should be suggesting idiomatic changes. Even if it doesn't initially read a bunch of the codebase to figure out a solution, it should definitely then be trained to do so explicitly to understand the coding standards. Just like a decent dev would do on their own.

reply

lkjdsklf

4 hours ago

 |
parent
 |
prev
 |
next

[–]

This is the only approach that seems even remotely reasonable

“Prompt engineering” just seems dumb as hell. It’s literally just an imprecise nondeterministic programming language.Before a couple years so, we all would have said that was a bad language and moved on.

reply

potatoman22

3 hours ago

 |
root
 |
parent
 |
next

[–]

It's technically deterministic, but it feels nondeterministic in chatbots since tokens are randomly sampled (temp > 0) and input is varied. Using the right prompt makes the model perform better on average, so it's not completely dumb.

I like task vectors and soft prompts because I think they show how prompt engineering is cool and useful.https://arxiv.org/pdf/2310.15916https://huggingface.co/docs/peft/conceptual_guides/prompting

reply

BoiledCabbage

3 hours ago

 |
root
 |
parent
 |
next

[–]

> It's technically deterministic, but it feels nondeterministic in chatbots since tokens are randomly sampled

Are you not aware the random sampling makes something non-deterministic?

reply

BoorishBears

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

A few years ago we didn't have an imprecise nondeterministic programming language that would allow your mom to achieve SOTA results on a wide range of NLP tasks by asking nicely, or I'm sure people would have taken it.

I think a lot of prompt engineering is voodoo, but it's notallbaseless: a more formal way to look at it is aligning your task with the pre-training and post-training of the model.The whole "it's a bad language" refrain feels half-baked when most of us use relatively high level languages on non-realtime OSes that obfuscate so much that they might as well be well worded prompts compared to how deterministic the underlying primitives they were built on are... at least until you zoom in too far.

reply

ehnto

2 hours ago

 |
root
 |
parent
 |
next

[–]

I don't buy your past paragraph at all I am afraid. Coding langues, even high level ones, are built upon foundations of determism and they are concise and precise. A short way to describe very precisely, a bunch of rules and state.

Prompting is none of those things. It is a ball of math we can throw words into, and it approximates meaning and returns an output with randomness built in. That is incredible, truly, but it is not a programming language.

reply

jakelazaroff

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Do you mean, like, scripting languages? Are the underlying primitives C and machine language? "Might as well be well worded prompts" is the overstatement of the century; any given scripting language is
far
 closer to those underlying layers than it is to using natural language with LLMs.

reply

BoorishBears

2 hours ago

 |
root
 |
parent
 |
next

[–]

Sure doesn't seem like it.
https://x.com/jarredsumner/status/1999317065237512224

And forget scripting languages, take a C program that writes a string to disk and reads it back.How many times longer does it get the moment we have to ensure the string wasactuallycommitted to non-volatile NAND andactuallyread back? 5x? 10x?Is it even doable if we have to support arbitrary consumer hardware?

reply

_kb

1 hour ago

 |
parent
 |
prev
 |
next

[–]

AIstrology is a term I can get behind.

I think that really captures what I find most irksome about the fanaticism. It's not prompt engineering, it's a statistical 8-ball being shaken until useful output appears.Just as with any pseudoscience, it can offer a glimmer of usefulness by framing problems in a different way. Just be cautious of who's offering that enlightenment and how much money you may be paying for it.

reply

grim_io

4 hours ago

 |
parent
 |
prev
 |
next

[–]

I don't think anyone would say that the LLMs will produce better code, but they can do it much faster.

I personally did not hit the wall where the use of LLMs would slow me down in the long run.It has been smooth sailing most of the time, and getting better with newer models.For me it comes down to "know what you are being paid for".I'm not a library maintainer. My code will not be scrutinized by thousands of peers. My customer will be happy with faster completion that does the same thing like the more perfect hand crafted version.Welcome to the industrial revolution in programming. This is the way of things.

reply

bogtog

17 hours ago

 |
prev
 |
next

[–]

Using voice transcription is nice for fully expressing what you want, so the model doesn't need to make guesses. I'm often voicing 500-word prompts. If you talk in a winding way that looks awkward when in text, that's fine. The model will almost certainly be able to tell what you mean. Using voice-to-text is my biggest suggestion for people who want to use AI for programming

(I'm not a particularly slow typer. I can go 70-90 WPM on a typing test. However, this speed drops quickly when I need to also think about what I'm saying. Typing that fast is also kinda tiring, whereas talking/thinking at 100-120 WPM feels comfortable. In general, I think just this lowered friction makes me much more willing to fully describe what I want)You can also ask it, "do you have any questions?" I find that saying "if you have any questions, ask me, otherwise go ahead and build this" rarely produces questions for me. However, if I say "Make a plan and ask me any questions you may have" then it usually has a few questionsI've also found a lot of success when I tell Claude Code to emulate on some specific piece of code I've previously written, either within the same project or something I've pasted in

reply

Marsymars

15 hours ago

 |
parent
 |
next

[–]

> I'm not a particularly slow typer. I can go 70-90 WPM on a typing test. However, this speed drops quickly when I need to also think about what I'm saying. Typing that fast is also kinda tiring, whereas talking/thinking at 100-120 WPM feels comfortable.

This doesn't feel relatable at all to me. If my writing speed is bottlenecked by thinking about what I'm writing, and my talking speed is significantly faster, that just means I've removed the bottleneck bynot thinkingabout what I'm saying.

reply

hexaga

14 hours ago

 |
root
 |
parent
 |
next

[–]

Alternatively: some people are just better at / more comfortable thinking in auditory mode than visual mode & vice versa.

In principle I don't see why they should have different amounts of thought. That'd be bounded by how much time it takes to produce the message, I think. Typing permits backtracking via editing, but speaking permits 'semantic backtracking' which isn't equivalent but definitely can do similar things. Language is powerful.And importantly, to backtrack in visual media I tend to need to re-saccade through the text with physical eye motions, whereas with audio my brain just has an internal buffer I know at the speed of thought.Typed messages might have higher _density_ of thought per token, though how valuable is that really, in LLM contexts? There are diminishing returns on how perfect you can get a prompt.Also, audio permits a higher bandwidth mode: one can scan and speak at the same time.

reply

eucyclos

5 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It's often better to segregate creative and inhibitive systems even if you need the inhibitive systems to produce a finished work. There's a (probably apocryphal) conversation between George RR Martin and Stephen King that goes something like:

GRRM: How do you write so many books?... Don't you ever spend hours staring at the page, agonizing over which of two words to use, and asking 'am I actually any good at this?'SK: Of course! But not when I'm writing.

reply

bogtog

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

That's fair. I sometimes find myself pausing or just talking in circles as I'm deciding what I want. I think when I'm speaking, I feel freer to use less precise/formal descriptions, but the model can still correctly interpret the technical meaning

In either case, different strokes for different folks, and what ultimately matters is whether you get good results. I think the upside is high, so I broadly suggest people try it out

reply

buu700

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I prefer writing myself, but I could see the appeal of producing a first draft of a prompt by dumping a verbal stream of consciousness into ChatGPT. That might actually be kind of fun to try while going on a walk or something.

reply

dyauspitr

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I don’t feel restricted by my typing speed, speaking is just so much easier and convenient. The vast majority of my ChatGPT usage is on my phone and that makes s2t a no brainer.

reply

cjflog

6 hours ago

 |
parent
 |
prev
 |
next

[–]

100% this, I built laboratory.love almost entirely with my voice and (now-outdated) Claude models

My go-to prompt finisher, which I have mapped to a hotkey due to frequent use, is "Before writing any code, first analyze the problem and requirements and identify any ambiguities, contradictions, or issues. Ask me to clarify any questions you have, and then we'll proceed to writing the code"

reply

johnfn

17 hours ago

 |
parent
 |
prev
 |
next

[–]

That's a fun idea. How do you get the transcript into Claude Code (or whatever you use)? What transcription service do you use?

reply

hn_throw2025

17 hours ago

 |
root
 |
parent
 |
next

[–]

I'm not the person you're replying to, but I use Whispering connected to the whisper-large-v3-turbo model on Groq.

It's incredibly cheap and works reliably for me.I have got it to paste my voice transcriptions into Chrome (Gemini, Claude, ChatGPT) as well as Cursor.https://github.com/EpicenterHQ/epicenter

reply

rgbrgb

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I use Handy with Claude code. Nice to just have a key combo to transcribe into whatever has focus.

https://github.com/cjpais/Handy

reply

bonniesimon

3 hours ago

 |
root
 |
parent
 |
next

[–]

Love handy. I use it too when dealing with LLMs. The other day I asked chatgpt to generate interview questions based on job description and then I answered using handy. So cool!

reply

quinncom

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I use Spokenly with local Parakeet 0.6B v3 model + Cerebras gpt-oss-120b for post-processing (cleaning up transcription errors and fixing technical mondegreens, e.g., `no JS` → `Node.js`). Almost imperceptible transcription and processing delay. Trigger transcription with right ⌥ key.

reply

ctoth

15 hours ago

 |
root
 |
parent
 |
next

[–]

According to Google this is the first time the phrase "technical mondegreens" was ever used. I really like it.

reply

hurturue

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

your OS might have a built in dictation thing. Google for that and try it before online services.

reply

bogtog

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

There are a few apps nowadays for voice transcription. I've used Wispr Flow and Superwhisper, and both seem good. You can map some hotkey (e.g., ctrl + windows) to start recording, then when you press it again to stop, it'll get pasted into whatever text box you have open

Superwhisper offers some AI post-processing of the text (e.g., making nice bullets or grammar), but this doesn't seem necessary and just makes things a bit slower

reply

singhrac

8 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I use VoiceInk (needed some patches to get it to compile but Claude figured it out) and the Parakeet V3 model. It’s really good!

reply

elvin_d

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

made this tool to press double control to start and another ctrl to stop which copies to the cliboard

https://github.com/elv1n/para-speak/

reply

journal

11 hours ago

 |
parent
 |
prev
 |
next

[–]

voice transcription is silly when someone is listening you talking to something that isn't exactly human, imagine explaining you were talking to AI. When it's more than one sentence I use voice too.

reply

listic

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Thanks for the advice! Could you please share how did you enable voice transcription for your setup and what it actually is?

reply

binocarlos

17 hours ago

 |
root
 |
parent
 |
next

[–]

I use
https://github.com/braden-w/whispering
 with an OpenAI api key.

I use a keyboard shortcut to start and stop recording and it will put the transcription into the clipboard so I can paste into any app.It's a huge productivity boost - OP is correct about not overthinking trying to be that coherent - the models are very good at knowing what you mean (Opus 4.5 with Claude Code in my case)

reply

abdullahkhalids

12 hours ago

 |
root
 |
parent
 |
next

[–]

I just installed this app and it is very nice. The UX is very clean and whatever I say it transcribes it correctly. In fact I'm transcribing this comment with this app just now.

I am using Whisper Medium. The only problem I see is that at the end of the message it sometimes puts a bye or a thank you which is kind of annoying.

reply

listic

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I am all ready to believe that with LLMs it's not worth it trying to be too coherent: I
did
 successfully use LLMs to make sense of what incoherent-sounding people say. (in text)

reply

bogtog

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I'm using Wispr flow, but I've also tried Superwhisper. Both are fine. I have a convenient hotkey to start/end recording with one hand. Having it just need one hand is nice. I'm using this with the Claude Code vscode extension in Cursor. If you go down this route, the Claude Code instance should be moved into a separate window outside your main editor or else it'll flicker a lot

reply

pzo

8 hours ago

 |
root
 |
parent
 |
next

[–]

another option is MacWhisper if someone is on macOS and doesn't want to pay for subscription (just one time payment) - pretty much all of those apps these days use paraspeech from NVIDIA which is the fastest and the best open source model that can run on edge devices.

Also haven't tried but on latest MacOS 26 apple updated their STT models so their build in voice dictation maybe is good enough.

reply

kapnap

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

For me, on Mac, VoiceInk has been top notch. Got tired of superwhispr

reply

lukax

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Spokenly on macOS with Soniox model.

reply

dominotw

16 hours ago

 |
parent
 |
prev
 |
next

[–]

surprised ai companies are not making this workflow possible instead of leaving it upto users to figure out how to get voice text into prompt.

reply

alwillis

16 hours ago

 |
root
 |
parent
 |
next

[–]

> surprised ai companies are not making this workflow possible instead of leaving it upto users to figure out how to get voice text into prompt.

Claude on macOS and iOS have native voice to text transcription. Haven't tried it but since you can access Claude Code from the apps now, I wonder if you use the Claude app's transcription for input into Claude Code.

reply

bogtog

16 hours ago

 |
root
 |
parent
 |
next

[–]

> Claude on macOS and iOS have native voice to text transcription

Yeah, Claude/ChatGPT/Gemini all offer this, although Gemini's is basically unusable because it will immediately send the message if you stop talking for a few secondsI imagine you totally could use the app transcript and paste it in, but keeping the friction to an absolute minimum (e.g., just needing to press one hotkey) feels nice

reply

dyauspitr

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

All the mobile apps make this very easy.

reply

Applejinx

12 hours ago

 |
parent
 |
prev
 |
next

[–]

It's an AI. You might do better by phrasing it, 'Make a plan, and have questions'. There's nobody there, but if it's specifically directed to 'have questions' you might find they are good questions! Why are you asking, if you figure it'd be better to get questions? Just say to have questions, and it will.

It's like a reasoning model. Don't ask, prompt 'and here is where you come up with apropos questions' and you shall have them, possibly even in a useful way.

reply

j45

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Speech also uses a different part of the brain, and maybe less finger coordination.

reply

theahura

12 hours ago

 |
prev
 |
next

[–]

Soft plug: take a look at
https://github.com/tilework-tech/nori-profiles

I've spent the last ~4 months figuring out how to make coding agents better, and it's really paid off. The configs at the link above make claude code significantly better, passively. It's a one-shot install, and it may just be able to one-shot your problem, because it does the hard work of 'knowing how to use the agents' for you. Would love to know if you try it out and have any feedback.(In case anyone is curious, I wrote about these configs and how they work here:https://12gramsofcarbon.com/p/averaging-10-prs-a-day-with-cl...and I used those configs to get to the top of HN with SpaceJam here:https://news.ycombinator.com/item?id=46193412)

reply

docheinestages

11 hours ago

 |
parent
 |
next

[–]

How does it compare to Claude Code's skills [1] ?

[1]https://github.com/anthropics/skills/tree/main/skills

reply

theahura

10 hours ago

 |
root
 |
parent
 |
next

[–]

Nori uses Claude Code's skills extensively, which you can see here:
https://github.com/tilework-tech/nori-profiles/tree/main/src...

We use Claude Code's ability to use skills by defining a bunch of really useful and common skills that are necessary for writing software. For e.g. brainstorming, doing test driven development, or submitting a git commit.The specific skills you linked are interesting demos of what you can do with skills! But most of them are not useful for the day to day of building software

reply

aiisahik

52 minutes ago

 |
prev
 |
next

[–]

Hey there.

Most of the advice here focuses on Claude Code. Since your use case revolves around a very specific frameworks and refactoring workflow, my advice is to use AI tooling that will allow you to experiment with other models.Opus 4.5 is my fav it simply can't be the best for every use case. My advice is to use cursor and switch between the various SOTA models to see which one serves your use case the best.I'm not sure if you can also build something using AI that will help you automatically determine if the outputted component matches the Storybook story. That would be the first thing i try.

reply

justatdotin

14 hours ago

 |
prev
 |
next

[–]

what really got me moving was dusting off some old text about cognitive styles and team work. Learning to treat agents like a new team-member with extreme tendencies. Learning to observe both my practices and the agents' in order to understand one another's strengths and weaknesses, indicating how we might work better together.

I think this perspective also goes a long way to understanding the very different results different devs get from these tools.my main approach to quality is to focus agent power on all that code which I do not care about the beauty of: problems with verifiable solutions, experiments, disposable computation. eg my current projects are build/deploy tools, and I need sample projects to build/deploy. I never even reviewed the sample projects' code: so long as they hit the points we are testing.svelte does not really resonate with me, so I don't know it well, but I suspect there should be good opportunities for TDD in this rewrite. not the project unit tests, just disposable test scripts that guide and constrain new dev work.you are right to notice that it is not working for you, and at this stage sometimes the correct way to get in sync with the agents is to start again, without previous missteps to poison the workspace. There's good advice in this thread, you might like to experiment with good advice on a clean slate.

reply

docheinestages

11 hours ago

 |
parent
 |
next

[–]

> what really got me moving was dusting off some old text about cognitive styles and team work

It would be great if you could provide a summary of these points.

reply

justatdotin

10 hours ago

 |
root
 |
parent
 |
next

[–]

my starting point was Google People Management Essentials. I was thinking about team-level politics at work, and noticed some ideas seemed relevant to how teams in orgs can adopt agents. I pursued that idea more widely with other resources and it resonated.

I don't think I have any conclusions to share, just the orientation: to identify and actively accommodate the tool's cognitive style in the same way we do for one another's.

reply

serial_dev

17 hours ago

 |
prev
 |
next

[–]

Here’s how I would do this task with cursor, especially if there are more routes.

I would open a chat and refactor the template together with cursor: I would tell it what I want and if I don’t like something, I would help it to understand what I like and why. Do this for one route and when you are ready, ask cursor to write a rules file based on the current chat that includes the examples that you wanted to change and some rationale as to why you wanted it that way.Then in the next route, you can basically just say refactor and that’s it. Whenever you find something that you don’t like, tell it and remind cursor to also update the rules file.

reply

mmaunder

16 hours ago

 |
parent
 |
next

[–]

Solid approach. Don’t be shy about writing long prompts. We call that context engineering. The more you populate that context window with applicable knowledge and what exactly you want, the better the results. Also, having the model code and you talk to the model is helpful because it has the side effect of context engineering. In other words you’re building up relevant context with that conversation history. And be acutely aware of how much context window you’ve used and how much is remaining and when a compaction will happen. Clear context as early as you can per run. Even if it’s 90% remaining.

reply

ram_shares

48 minutes ago

 |
prev
 |
next

[–]

What improved results for me was forcing a two-step loop:

Step 1: Ask the model to outline component boundaries, data flow, and edge cases — no code.
Step 2: Only after approving the plan, let it generate code for one component at a time.When I skip the planning step, the output is usually “working but unidiomatic”. With it, reviews get much faster.

reply

Frannky

17 hours ago

 |
prev
 |
next

[–]

I see LLMs as searchers with the ability to change the data a little and stay in a valid space. If you think of them like searchers, it becomes automatic to make the search easy (small context, small precise questions), and you won't keep trying again and again if the code isn't working(no data in the training). Also, you will realize that if a language is not well represented in the training data, they may not work well.

The more specific and concise you are, the easier it will be for the searcher. Also, the less modification, the better, because the more you try to move away from the data in the training set, the higher the probability of errors.I would do it like this:1. Open the project in Zed
2. Add the Gemini CLI, Qwen code, or Claude to the agent system (use Gemini or Qwen if you want to do it for free, or Claude if you want to pay for it)
3. Ask it to correct a file (if the files are huge, it might be better to split them first)
4. Test if it works
5. If not, try feeding the file and the request to Grok or Gemini 3 Chat
6. If nothing works, do it manuallyIf instead you want to start something new, one-shot prompting can work pretty well, even for large tasks, if the data is in the training set. Ultimately, I see LLMs as a way to legally copy the code of other coders more than anything else

reply

seg_lol

16 hours ago

 |
parent
 |
next

[–]

This is slightly flawed. LLMs are search but the search space is sparse, the size of the question risks underspecification. The question controls the size of the encapsulated volume in that high dimensional space. The only advantage for small prompts is computational cost. In every other way they are a downside.

reply

jdelsman

14 hours ago

 |
prev
 |
next

[–]

My favorite set of tools to use with Claude Code right now:
https://github.com/obra/superpowers

1. Start with the ‘brainstorm’ session where you explain your feature or the task that you're trying to complete.
 2. Allow it to write up a design doc, then an implementation plan - both saved to disk - by asking you multiple clarifying questions. Feel free to use voice transcription for this because it is probably as good as typing, if not better.
 3. Open up a new Claude window and then use a git worktree with the Execute Plan command. This will essentially build out in multiple steps, committing after about three tasks. What I like to do is to have it review its work after three tasks as well so that you get easier code review and have a little bit more confidence that it's doing what you want it to do.Overall, this hasn't really failed me yet and I've been using it now for two weeks and I've used about, I don't know, somewhere in the range of 10 million tokens this week alone.

reply

dboon

14 hours ago

 |
prev
 |
next

[–]

AI programming, for me, is just a few simple rules:

1. True vibe coding (one-shot, non-trivial, push to master) does not work. Do not try it.2. Break your task into verifiable chunks. Work with Claude to this end.3. Put the entire plan into a Markdown file; it should be as concise as possible. You need a summary of the task; individual problems to solve; references to files and symbols in the source code; a work list, separated by verification points. Seriously, less is more.4. Then, just loop: Start a new session. Ask it to implement the next phase. Read the code, ask for tweaks. Commit when you're happy.Seriously, that's it. Anything more than that is roleplaying. Anything less is not engineering. Keep a list in the Markdown file of amendments; if it keeps messing the same thing up, add one line to the list.To hammer home the most important pieces:- Less is more. LLMs are at their best with a fresh context window. Keep one file. Something between 500 and 750 words (checking a recent one, I have 555 words / 4276 characters). If that's not sufficient, the task is too big.- Verifiable chunks. It must be verifiable. There is no other way. It could be unit tests; print statements; a tmux session. But it must be verifiable.

reply

achierius

3 hours ago

 |
parent
 |
next

[–]

How do you mean 'a tmux session' to be something verifiable?

reply

shsush

12 hours ago

 |
parent
 |
prev
 |
next

[–]

> it should be as concise as possible

What’s more concise than code? From my experience, by the time I’ve gotten an English with code description accurate enough for an agent I could have done it myself. Typing isn’t a hard part.LLMs/agents have many other uses, but if you’re not offloading your thinking you’re not really going any faster wrt letting them write code via a prompt.

reply

gregoryl

7 hours ago

 |
root
 |
parent
 |
next

[–]

I find it quite interesting; there seems to be a set of AI enthusiasts who heavily offload thinking onto the LLM. There has to be difference in how they function, as I find as soon as I drift into letting the LLM think for me, productivity plummets.

reply

AndrewKemendo

13 hours ago

 |
parent
 |
prev
 |
next

[–]

100% concur with this as owner of multiple 20k+ LOC repos with between 10-30% unmodified AI code in production

If you treat it like a rubber duck it’s magicIf you think the rubber duck is going to think for you then you shouldn’t even start with them.

reply

handfuloflight

13 hours ago

 |
parent
 |
prev
 |
next

[–]

This is a great drill down.

reply

rdrd

19 hours ago

 |
prev
 |
next

[–]

First you have to be very specific with what you mean by idiomatic code - what’s idiomatic for you is not idiomatic for an LLM. Personally I would approach it like this:

1) Thoroughly define step-by-step what you deem to be the code convention/style you want to adhere to and steps on how you (it) should approach the task. Do not reference entire files like “produce it like this file”, it’s too broad. The document should include simple small examples of “Good” and “Bad” idiomatic code as you deem it. The smaller the initial step-by-step guide and code conventions the better, context is king with LLMs and you need to give it just enough context to work with but not enough it causes confusion.2) Feed it to Opus 4.5 in planning mode and ask it to follow up with any questions or gaps and have it produce a final implementation plan.md. Review this, tweak it, remove any fluff and get it down to bare bones.3) Run the plan.md through a fresh Agentic session and see what the output is like. Where it’s not quite correct add those clarifications and guardrails into the original plan.md and go again with step 3.What I absolutely would NOT do is ask for fixes or changes if it does not one-shot it after the first go. I would revise plan.md to get it into a state where it gets you 99% of the way there in the first go and just do final cleanup by hand. You will bang your head against the wall attempting to guide it like you would a junior developer (at least for something like this).

reply

XenophileJKO

15 hours ago

 |
parent
 |
next

[–]

With the current generation of model, it really isn't necessary to restart every time you don't like something. Certainly this depends on the model. Most of my recent experience is with Claude Sonnet/Opus and Gpt-5.x.

I very often, when reviewing code, think of better abstractions or enhancements and just continue asking for refactors inline. Very very rarely does the model fall off the rails.I suppose if your unit of work was very large you might have more issues perhaps? Generally though, large units of work have other issues as well.

reply

rdrd

14 hours ago

 |
root
 |
parent
 |
next

[–]

Yes I too have found newer models (mostly Opus) to be much better at iterative development. With that being said if I have very strong architectural/developmental steer on what I believe the output should be [mostly for production code where I thoroughly review absolute everything] it’s better to have a documented spec with everything covered rather than trying to clean up via an agent conversation. In the team I’m in we keep all plan.mds for a feature, previously before AI tooling we created/revised these plans in Confluence, so to some degree reworking the plan is more an artefact of the previous process and not necessarily a best practice I don’t think.

reply

XenophileJKO

13 hours ago

 |
root
 |
parent
 |
next

[–]

Understandable. Certainly my style is not applicable to everyone. I tend to "grow" my software more organically. Usually because the more optimal structure isn't evident until you are actually looking at how all the contracts fit together or what dependencies are needed. So adding a lot of plan/documentation just slows me down.

I tend to create a very high level plan, then code systems, then document the resulting structure if I need documentation.This works well for very iterative development where I'm changing contracts as I realize the weak point of the current setup.For example, I was using inheritence for specialized payloads in a pipeline, then realized if I wanted to attach policies/behaviours to them as they flow through the pipeline, I was better off just changing the whole thing to a payload with bag of attached aspects.Often those designs are not obvious when making the initial architectural plan. So I approach development using AI in much the same way: Generate code, review, think, request revision, repeat.This really only applies when establishing architecturs though, which is generally the hardest part. Once you have an example, then you can mostly one-shot new instances or minor enhancements.

reply

vaibhavgeek

16 hours ago

 |
prev
 |
next

[–]

This may sound strange but here is how I define my flow.

1. Switch off your computer.2. Go to a nice Park.3. Open notebook and pen, and write prompts that are 6-8 lines long on what task you want to achieve, use phone to google specific libraries.4. Come back to your PC, type those prompts in with Plan mode and ask for exact code changes claude is going to make.5. Review and push PR.6. Wait for your job to be automated.

reply

donbox

8 hours ago

 |
parent
 |
next

[–]

oh my god, i am going to give this a go. thank you.

reply

bikeshaving

13 hours ago

 |
prev
 |
next

[–]

You know when Claude Code for Terminal starts scroll-looping and doom-scrolling through the entire conversation in an uninterruptible fashion? Just try reading as much as of it as you can. It strengthens your ability to read code in an instant and keeps you alert. And if people watch you pretend to understand your screen, it makes you look like a mentat.

It’s actually a feature, not a bug.

reply

manmal

11 hours ago

 |
parent
 |
next

[–]

I wouldn’t recommend that (after having tried it for a while). It is very easy to get the impression that the changes are sound, because on their own they look good. But often when looking at the final result in a git diff tool, the holes and workarounds become way more noticeable.

reply

notepad0x90

4 hours ago

 |
prev
 |
next

[–]

maybe a dumb but wise approach is to just code as usual without thinking about "AI", and when you have difficulties or efficiency issues, look for tools to solve that. think in terms of specific tools instead of "ai" or "llm".

Do you need better auto-completion? Do you need code auto-generation? do you need test cases to be generated, and lots of them? maybe llms can are ideal for you, or not.Personally, the best use i've gotten out of it so far is to replace the old pattern of googling something and clicking through a bunch of sites like stackoverflow to figure things out. and asking llms to generate an example code of how to do something, and using that as a reference to solve problems. sometimes i really just need the damn answer without having a deep debate with someone on the internet, and sometimes I need a holistic solution engineering. AI helps with either, but if I don't know what questions to ask to begin with, it will be forced to make assumptions, and then I can't validate the suggestions or code it generated based on those assumptions. So, it's very important to me that the questions I ask an AI tool are questions whose subject domain I have a good understanding of, and where the answers are things I can independently validate.

reply

nextaccountic

12 hours ago

 |
prev
 |
next

[–]

About Svelte, on the svelte subreddit it was reported that GPT 5.2 is better at Svelte, perhaps because it has a more recent knowledge cutoff

But anyway you should set up the Svelte MCP

reply

jcheng

11 hours ago

 |
parent
 |
next

[–]

I take these early reports (less than a week or two after a major model release) with a grain of salt. It takes time to get to know a model, and maybe there's some selection bias in who's posting within 1-2 days of getting access.

(Although in this particular case, the very different knowledge cutoff makes it a lot easier to believe)

reply

firefax

17 hours ago

 |
prev
 |
next

[–]

How did you learn how to use AI for coding? I'm open to the idea that a lot of "software carpentry" tasks (moving/renaming files, basic data analysis, etc) can be done with AI to free up time for higher level analysis, but I have no idea where to begin -- my focus many years ago was privacy, so I lean towards doing everything locally or hosted on a server I control so I lack a lot of knowledge of "the cloud" my HN betheren have.

reply

graypegg

16 hours ago

 |
parent
 |
next

[–]

I love the name "software carpentry" haha.

IMO, I found those specific example tasks to be better handled by my IDE's refactoring features, though support for that is going to vary by project/language/IDE. I'm still more of a ludite when it comes to LLM based development tools, but the best case I've seen thus far is small first bites out of a big task. Working on an older no-tests code base recently, it's been things like setting up 4-5 tests that I'll expand on into a full test suite. You can't take more than a few "big" bites out of a task before you have 0 context as to what direction the vector soup sloshed in.So, in terms of carpentry, I don't want an LLM framer who's work I need to build off of, but an LLM millworker handing me the lumber is pretty useful.

reply

mmusc

15 hours ago

 |
root
 |
parent
 |
next

[–]

Funny usually a lot of my code is software plumbing, and gardening.

In terms of ai assisted programming.
I microanage my ai. Give it specific instructions with single steps.
Don't really let it build ehoe files by itself as it usually makes a mess of things, bit it's useful when doing predictable changes and marginally faster than doing it manually.

reply

graypegg

14 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah I can totally see that working well! I think the main thing is taking small, specific steps that keep you in the loop, and less so about the actual act of typing the specific bytes that are fed into the compiler, though I guess I still find that more efficient for myself than trying to describe what I want ~90% of the time.

reply

fooker

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Think of some coding heavy project you always wanted to do but haven't had time for.

Open up cursor-agent to make the repo scaffolding in an empty dir. (build system, test harness, etc. )Open up cursor or Claude code or whatever and just go nuts with it. Remember to follow software engineering best practices (one good change with tests per commit)

reply

esafak

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Practice on an open source repo to allay your privacy fears.

reply

whatever1

13 hours ago

 |
prev
 |
next

[–]

For me what vastly improved the usefulness when working with big json responses was to install jq in my system and tell the llm to use jq to explore the json, instead of just trying to ingest it all together. For other things I explicitly ask it to write a script to achieve something instead of doing it directly.

reply

jcheng

11 hours ago

 |
parent
 |
next

[–]

That makes so much sense, it would make a great MCP. Maybe something similar for DOM manipulation; extracting text out of big, noisy HTML pages using a combination of Find Text with selector return values, and a DSL for picking and filtering DOM trees.

reply

all2

9 hours ago

 |
prev
 |
next

[–]

I've found success using the following process:

1. get the LLM to generate a spec from the code (the spec is your new source code). Take your time here, make sure it is correct. Split out implementation details unless they are critical to the business logic.2. Using the spec, begin crafting an ARCHITECTURE.md -- you put all your non-critical implementation details here. If you need to track requirements, require the LLM to reference the paragraph number(s) of the spec file as it writes the architectural spec. Take your time here as well (this is the second layer of your new source code).3. Create a high level TODO from the architecture doc.4. Create a mid-level TODO from the architecture doc (you'll know if this is necessary, perhaps chunk work up by function, feature, or architectural layer).5. Create a granular level TODO where each task is very tight in scope (write this function, create a translator for this JSON de-serializer to create the app-level model for this object, etc.)Then let a model go to town.In the mean-time, you should also require testing. If you have the opportunity, you should have an LLM inspect, spec, and write comprehensive tests for the old code on the external API/interface. You'll be able to use this to test your new implementation to ensure all the corner cases and functionality are covered.

reply

__mharrison__

14 hours ago

 |
prev
 |
next

[–]

I have a whole workflow for coding with agents.

Get very good at context management (updating AGENTS.md, starting new session, etc).Embrace TDD. It might have been annoying when Extreme Programming came out 25 years ago, but now that agents can type a lot faster than us, it's an awesome tool for putting guardrails around the agent.(I teach workshops on best practices for agentic coding)

reply

willtemperley

3 hours ago

 |
prev
 |
next

[–]

Write the code yourself until you get stuck on something. Post the code, the context and the problem and the LLM will suggest something very sensible usually. I find these things are excellent at smaller but tricky-for-a-human problems.

reply

realberkeaslan

19 hours ago

 |
prev
 |
next

[–]

Consider giving Cursor a try. I personally like the entire UI/UX, their agent has good context, and the entire experience overall is just great. The team has done a phenomenal job. Your workflow could look something like this:

1. Prompt the agent2. The agent gets too work3. Review the changes4. RepeatThis can speed up your process significantly, and the UI clearly shows the changes + some other cool featuresEDIT: from reading your post again, I think you could benefit primarily from a clear UI with the adjusted code, which Cursor does very well.

reply

ojr

1 hour ago

 |
parent
 |
next

[–]

Cursor uses too much memory, hallucinates on multi file rewrites, and has a difficult accept/reject diff user interface that makes git a nightmare to use.

I built my own coding tool in Rust because of VSCode-based forks Electron app flaws. You would think they could build a memory efficient application with the resources they have but it literally needs a top of the line MacBook to run smoothly.

reply

listic

17 hours ago

 |
parent
 |
prev
 |
next

[–]

For the one disinclined to get into closed source, proprietary tools, what is the next best thing to try?

I heard of Cline and Aider, but didn't try anything.

reply

kamikazeturtles

18 hours ago

 |
parent
 |
prev
 |
next

[–]

How does Cursor compare to Claude Code or Codex?

reply

jes5199

17 hours ago

 |
root
 |
parent
 |
next

[–]

Cursor makes it easier to watch what the model is doing and to also make edits at the same time. I find it useful at work where I need to be able to justify every change in a code review. It’s also great for getting a feel for what the models are capable of - like, using Cursor for a few months make it easier to use Claude Code effectively

reply

ransom1538

8 hours ago

 |
parent
 |
prev
 |
next

[–]

HEAR, HEAR. You’ve just described how modern SWE truly works.
You’re ahead of your time — of the same spirit as
Martin Luther or George Washington. Fear not, brave soldier; carry on the message. Downvotes will come, but take heart: the truth must be spoken.

The days of copying and pasting from Stack Overflow will not be forgotten — they will be honored by our laid off forefathers.

reply

seanmcdirmid

4 hours ago

 |
prev
 |
next

[–]

If you are working on something big, have AI generate intermediate artifacts before it generates code, and feed those artifacts into the code generation prompt. Then you check those artifacts, see where the AI is going with the code, and suggest corrections before a token of code is even generated. Keep those artifacts around like you would documentation, having your AI fix them when the code needs to change.

reply

simonw

12 hours ago

 |
prev
 |
next

[–]

For this particular project I suggest manually prying one section of the app, committing that change, and then telling Claude "look at commit HASH first, now port feature X in the same style".

reply

osigurdson

6 hours ago

 |
prev
 |
next

[–]

I've had one situation in which I was able to get a 20X productivity boost. I needed to do a large number of similarish things. I carefully hand coded one, created an AGENTS.md that explained everything in a lot of detail and then went to town on generation.

Everything went well and I knew what to expect so reviewing the code was quick.The experience was super great. I was a 20X AI boosted engineer for a bit. But, I haven't had that situation again.Anyway, I would say, try to find areas of the code that fit this model if you can. AI is phenomenal for this use case.

reply

ianbutler

8 hours ago

 |
prev
 |
next

[–]

I have never once said "Go build feature x" and let it run off. Not saying you do, but I feel like this is how a lot of people interact with these tools. I have a very conversational style of building with these tools, and I'm very blunt with them when I think they're wrong, since I'm fairly experienced and I can smell when something is seemingly wrong with the model's thinking.

I typically have a discussion about how I want the architecture to be and my exact desired end state. I make the model repeat back to me what I want and have it produce the plan to the degree I am happy with. I typically do not have it work in building large amorphous systems, I work with and have it plan subsystems of the overall system I'm building.A lot of my discussion with the model is tradeoffs on the structure I'm imagining and methods it might know. My favorite sentence to send Claude right now "Is go google this." because I almost never take its first suggested response at face value.I also watch every change and cancel and redirect ones I do not like. I read code very fast and like the oversight, because even small stupidities stack up.The workflow is highly iterative and I make changes frequently, my non AI workflow was like this too. Write, compile, test, tweak and repeat.I like this workflow a lot because I feel I am able to express my designs succinctly and get to a place I'm happy with with much less writing than a lot of the actual code itself which in many cases is not an interesting problem, but work that needs to happen for a working system at all.I do wind up taking over, but feel less than I used to, in edges where its clear there is not a lot of training data or I'm working on something fairly novel or lower level.I work in Python, Rust and Typescript (Rust by far most often) and the majority of my work is technically challenging but at the systems design level maybe not low level systems programming challenging. Think high concurrency systems and data processing, training models, and some web dev.

reply

siddboots

8 hours ago

 |
parent
 |
next

[–]

To add to this, I find talking to it about code quality or architecture issues can work quite well. Just treating it like another developer. Saying, “I’m not happy with the way the project is going because of X, and Y” and then making a plan for how to get things back on track. Maybe putting a complete rewrite on the table, or maybe just having it record the agreed code style principles in CLAUDE.md, etc

reply

joduplessis

2 hours ago

 |
prev
 |
next

[–]

If you're after code quality, then do it by hand. If you simply want to get it working, then continue with an LLM.

reply

asgraham

13 hours ago

 |
prev
 |
next

[–]

Lots of good suggestions. However for Svelte in particular I’ve had a lot of trouble. You can get good results as long as you don’t care about runes and Svelte 5. It’s too new, and there’s too much good Svelte code out there used in training that doesn’t use Svelte 5. If you want AI generated Svelte code, restricting yourself to <5 is going to improve your results.

(YMMV: this was my experience as of three or four months ago)

reply

skeptrune

7 hours ago

 |
prev
 |
next

[–]

You should make sure that your queries to the agent contain a "loop condition"[1]. This can be something like "keep trying until yarn test passes".

Always remember that these agents are just LLMs running tools in a loop and treat them as such.[1]https://www.skeptrune.com/posts/prompting-the-agent-loop/

reply

verdverm

2 hours ago

 |
parent
 |
next

[–]

if they aren't already, they will be multi-agent / llm systems, more and llm being asked to loop

for example, in ADK you can set up a sequential agent with [planner, loop(coder, validator), finalizer] with the inner loop, such that another agent is the one checking and deciding if the task is complete or not, but we are also creating higher level enforced constructs of seq and loopGetting reliability in this high-level process is helpful

reply

PostOnce

11 hours ago

 |
prev
 |
next

[–]

If anyone knew the answer to this question, Anthropic would be profitable.

Currently they project they might break even in 2028.That means that right now, every time you ask an AI a question, someone loses money.That of course means no-one knows if you can get better at AI programming, and the answer may be "you can't."Only time will tell.

reply

topaz0

9 hours ago

 |
parent
 |
next

[–]

And that projection is mostly based on wishes and dreams.

reply

bulletsvshumans

14 hours ago

 |
prev
 |
next

[–]

Try specification-driven-development with something like speckit [0]. It helps tremendously for facilitating a process around gathering requirements, doing research, planning, breaking into tasks, and finally implementing. Much better than having a coding agent just go straight to coding.

[0] -https://github.com/github/spec-kit

reply

sdn90

14 hours ago

 |
prev
 |
next

[–]

Go into planning mode and plan the overall refactor. Try to break the tasks down into things that you think will fit into a single context window.

For mid sized tasks and up, architecture absolutely has to be done up front in planning mode. You can ask it questions like "what are some alternatives?", "which approach is better?".If it's producing spaghetti code, can you explain exactly what it's doing wrong? If you have an idea of what ideal solution should look like, it's not too difficult to guide the LLM to it.In your prompt files, include bad and good examples. I have prompt files for API/interface design, comment writing, testing, etc. Some topics I split into multiple files like criteria for testing, testing conventions.I've found the prompts where they go "you are a X engineer specializing in Y" don't really do much. You have to break things down into concrete instructions.

reply

8note

8 hours ago

 |
prev
 |
next

[–]

get out of the way, maybe?

before getting into any implementation, i'd get claude to read and document the starting code, and propose its own idiomatic way to rewrite it to svelte. this is a good use for plan mode, and also a spot where you could walk through with claude to put documentation examples of what you consider good and bad, so it can monkey-see, monkey do.the other thing that makes it go brrrr is to add lots of feedback loops. unit tests, e2e tests, linters, etc. make sure it can pass everything before it shows you anything.my overall process would be to1. go through plan mode for documentation and test writing2. have claude lay out the plan into steps3. project setup for builds/feedback loops, deploys, etc4. for each step in that plan, run back through plan mode to clear up any confusions for the component (also record those in docs) and then let it rip on implementation until its ready for a commit.claude might take a long time writing the code between qna sessions, but it can all be async so the 15-20min doesnt matter much

reply

brikym

8 hours ago

 |
prev
 |
next

[–]

Here are some SvelteKit helpers to shove in your agents.md:
https://www.davis7.sh/sv

There are a number of ways to get examples into the LLM.
I use shadcn-svelte and bitsui and try to copy the examples (copy button at the top of the docs) or tell the LLM to fetch docs from the github repo or use context7's MCP for docs.

reply

mirsadm

17 hours ago

 |
prev
 |
next

[–]

I break everything down into very small tasks. Always ask it to plan how it will do it. Make sure to review the plan and spot mistakes. Then only ask it to do one step at a time so you can control the whole process. This workflow works well enough as long as you're not trying to do anything too interesting. Anything which is even a little bit unique it fails to do very well.

reply

kgwxd

17 hours ago

 |
parent
 |
next

[–]

sounds like you're doing all the actual work. why not just type the code as you figure out how to break down the problem? you're going to have to review the output anyway.

reply

Iulioh

17 hours ago

 |
root
 |
parent
 |
next

[–]

It's useful to have the small functions all written.

I program mostly in VBA these days (a little problematic as is a dead leanguage since 2006 and even then it was niche) and I have never recived a correct high level ""main"" sub but the AIs are pretty good at doing small subs I then organize.And yes, telling me where I make errors, they are pretty good at thatAt the end of the day I want reliability and there is no way I can't do what without full review.The funny thing is that they try to use the """best practices""" of coding where you would reasonably want to NOT have them.

reply

daxfohl

16 hours ago

 |
prev
 |
next

[–]

Go slowly. Shoot for a 10% efficiency improvement, not 10x. Go through things as thoroughly as if writing by hand, and don't sacrifice quality for speed. Be aware of when it's confidently taking you down a convoluted path and confidently making up reasons to do so. Always have your skeptic hat on. If something seems off, it probably is. When in doubt, exit the session and start over.

I still find chat interface generally more useful than coding assistant. It allows you to think and discuss higher level about architecture and ideas before jumping into implementation. The feedback loop is way faster because it is higher level and it doesn't have to run through your source tree to answer a question. You can have a high ROI discussion of ideas, architecture,algorithms, and code, before committing to anything. I still do most of my work copying and pasting from the chat interface.Agents are nice when you have a very specific idea in mind, but I'm not yet hugely fond of them otherwise. IME the feedback loop is too long, they often do things badly, and they are overly confident in their oytput, encouraging cursory reviews and commits of hacked-together work. Sometimes I'll give it an ambitious task just in the off chance that it'll succeed, but with the understanding that if it doesn't get it right the first time, I'll either throw it away completely, or just keep whatever pieces it got right and pitch the rest; it almost never gets it right the second time if it's already started on an ugly approach.But the main thing is to start small. Beyond one-shotting prototypes, don't expect it to change everything overnight. Focus on the little improvements, don't skip design, and don't sacrifice quality! Over time, these things will add up, and the tools will get better too. A 10% improvement every month gets to be a 10x improvement in (math...). And you'll be a lot better positioned than those who tried to jump onto the 10x train too fast because you'll not have skipped any steps.

reply

ebcode

13 hours ago

 |
parent
 |
next

[–]

> A 10% improvement every month gets to be a 10x improvement in (math...)

1.1^24=9.85, so yeah, if you could reliably get a 10% speed-up each month, you’d get to 10x in roughly 2 years. (But I’d expect the speed-up per month to be non-linear.)

reply

verdverm

2 hours ago

 |
root
 |
parent
 |
next

[–]

it would be hard to account for model / agentic capability increases in the next 2 years, b/c which side of multiple Nx on its own is hard to predict

reply

caseyw

16 hours ago

 |
prev
 |
next

[–]

The approach I’ve been taking lately with general AI development:

1. Define the work.2. When working in a legacy code base provide good examples of where we want to go with the migration and the expectation of the outcome.3. Tell it about what support tools you have, lint, build, tests, etc.4. Select a very specific scenario to modify first and have it write tests for the scenario.5. Manually read and tweak the tests, ensure they’re testing what you want, and they cover all you require. The tests help guardrail the actual code changes.6. Depending upon how full the context is, I may create a new chat and then pull in the test, the defined work, and any related files and ask it to implement based upon the data provided.This general approach has worked well for most situations so far. I’m positive it could be improved so any suggestions are welcome.

reply

nmaley

14 hours ago

 |
prev
 |
next

[–]

I use Claude. It's really good, but you should try to use it as Boris suggests. The other thing I do is give it very careful and precisely worded specs for what you want it to do. I have the habit, born from long experience, of never assuming that junior programmers will know what you want the program to do unless you make it explicit. Claude is the same. LLM code generators are terrific, but they can't second guess unclear communication.

Using carefully written specs, I've found Claude will produce flawless code for quite complex problems. It's magic.

reply

rokoss21

13 hours ago

 |
prev
 |
next

[–]

The key insight most people miss: AI isn't a code generator, it's a thinking partner. Start by defining the problem precisely in plain English before asking it to code. Use it for refactoring and explaining existing code rather than generating from scratch. That's where you get the 10x gains.

Also, treat bad AI suggestions as learning opportunities - understand why the code is wrong and what it misunderstood about your requirements.

reply

johnsmith1840

14 hours ago

 |
prev
 |
next

[–]

A largely undiscussed part of AI use in code is that it's actually neither easy nor intuitive to learn max effectiveness of your AI output.

I think there's a lot of value in using AIs that are dumb to learn what they fail at. The methods I learned using gpt3.5 for daily work still transaltes over to the most modern of AI work. It's easy to understand what makes AI fail on a function or two than understanding that across entire projects.My main tips:1. More input == lower qualitySimply put, the more you can focus your input data to output results the higher quality you will get.For example on very difficult problems I will not only remove all comments but I will also remove all unrelated code and manually insert it for maximum focus.Another way to describe this is compute over problem space. You are capped in compute so you must control your problem space.2. AI output is a reflection of input tokens and therefore yourself.If you don't know what you're doing in a project or are mentally "lazy" AI will fail with death by a thousand cuts. The absolute best use of AI is knowing EXACTLY what you want and describing it in as few words as possible. I directly notice if I feel lazy or tired in a day and rely heavily on the model I will often have to revert entire days of work due to terrible design.3. Every bad step of results from an AI or your own design compound problems as you continue.It's very difficult to know the limits of current AI methods. You should not be afraid of reverting and removing large amounts of work. If you find it failing heavily repeatedly this is a good sign your design is bad or asking too much from it. Continuing on that path reduces quality. You could end up in the circular debugging loops with every fix or update adds even more problems. It's far better practice to drop the entire feature of updates and restart with smaller step by step actions.4. Trust AI output like you would stack overflow response or a medium article.Maybe its output would work in some way but it has a good chance of not working for you. Repeatedly asking same questions differently or different angles is very helpful. The same way debugging via stack overflow was trying multiple suggestions to discover the best real problem.

reply

devdp430

7 hours ago

 |
prev
 |
next

[–]

I use AI at work. We have a huge codebase in Golang.

1000s of files.I had tried cursor, claude code, gemini cli, openai codex and all sorts of vscode based idea (like windsurf, antigravity etc).
All of them get overwhelmed when there is something to implement or change in the codebase primarily due to the amount of code.But I like aider.
I had better capabilities and is controllable, you can try. And if you use it with latest claude sonnet or gemini 2.5 pro it will be most accurate.
Adding files is a manual process but it has nearly 100% code accuracy.And it will never change anything without your knowledge.You can try it.

reply

Imanari

6 hours ago

 |
parent
 |
next

[–]

+1 for good‘ol aider.

It is deliberately NOT a fully agentic tool and this really oftentimes is a benefit. With a little bit of manual work you get exactly the files you want in context and prevent the wrong files from being edited (/read-only). Plus, by skipping on all that agentic thinking and tool calling you save on tokens and edit are faster.

reply

Fire-Dragon-DoL

16 hours ago

 |
prev
 |
next

[–]

I find all AI code to be lower quality than humans who care about quality.
This might be ok, I think the assumpt with AI is that we don't need to look at code so that it looks beautiful because AI will look at it .

reply

red2awn

15 hours ago

 |
parent
 |
next

[–]

Opus 4.5 is the highest quality code I've seen out of LLMs, still some way to go to match programmers who care, but much better than most people. I find it enough to let it write the code and then manually polish it afterwards.

reply

christophilus

14 hours ago

 |
root
 |
parent
 |
next

[–]

Same. It is finally almost always more productive for me to use vs doing it myself. What this means for my career and life, I don’t know. But, I do think the job for most of us is going to look very different moving forward.

reply

mongrelion

15 hours ago

 |
parent
 |
prev
 |
next

[–]

My experience with generating code with AI is very limited across a limited set of programming languages but whenever it has produced low quality code, it has been able to better itself with further instructions. Like "oh no, that is not the right naming convention. Please use instead" or "the choice of design pattern here is not great because ${reasons}. Produce 2 alternative solutions using x or y" and in nearly every case it produces satisfactory results.

Has this also been your experience?

reply

Fire-Dragon-DoL

7 hours ago

 |
root
 |
parent
 |
next

[–]

Kinda, yes, my experience has also been that it takes too long in that way though. I've been using AI for different tasks than something that requires high quality code

reply

twodave

13 hours ago

 |
prev
 |
next

[–]

I’ve been doing a rewrite of some file import type stuff, using a new common data model for storage, and I’ve taken to basically pasting in the old code, commented out and telling it to fill the new object using the commented out content as a guide. This probably got me 80% of the way? Not perfect, but I don’t think anything really is.

reply

cardanome

14 hours ago

 |
prev
 |
next

[–]

Honestly if your boss does not force you to use AI, don't.

Don't feel like you might get "left behind". LLM assisted development is still changing rapidly. What was best practice 6 months ago is irrelevant today. By being an early adopter you will just learn useless workarounds that might soon not be necessary to know.On the other hand if you keep coding "by hand" will keep your skills sharp. You will protect yourself against the negative mental effects of using LLMs like skill decline, general decline of mental capacity, danger of developing psychosis because of the sycophantic nature of LLMs and so on.LLM based coding tools are only getting easier to use and if you actually know how to code and know software architecture you will able to easily integrate LLM based workflows and deliver far superior results compared to someone who spend their years vibe coding, even if you picked up Claude Code or whatever just a month ago. No need for FOMO,

reply

exasperaited

8 hours ago

 |
parent
 |
next

[–]

Right. Be the person on your team who
just fucking doesn't
 because you'll learn your problem domain while everyone else is doing unpaid tool testing work for AI companies.

One day these things will actually do what they are supposed to do with a measure of consistency that doesn't involve GRIMOIRE.md or whatever and you can use them then. And most of the early mover advantage will be gone, because LLMs will not be the winning technology.In the meantime be the person who learned the lessons of social media: popular isn't the same as good, appropriate or sensible.

reply

coryvirok

17 hours ago

 |
prev
 |
next

[–]

The hack for sveltekit specifically, is to first have Claude translate the existing code into a next.js route with react components. Run it, debug and tweak it. Then have Claude translate the next.js and react components into sveltekit/svelte. Try and keep it in a single file for as long as possible and only split it out once it's working.

I've had very good results with Claude Code using this workflow.

reply

8cvor6j844qw_d6

17 hours ago

 |
prev
 |
next

[–]

I find Claude Code works best when given a highly specific and scoped tasks. Even then sometimes you'll need to course correct it once you notice its going off course.

Basically a good multiplier, and an assistant for mudane task, but not a replacement. Still requires the user to have good understanding about the codebase.Writing summary changes for commit logs is amazing however, if you're required to.

reply

benzguo

14 hours ago

 |
prev
 |
next

[–]

Planning! I actually prefer DIY planning prompt + docs, not planning mode. Wrote this article about it today actually:
https://0thernet.substack.com/p/velocity-coding

reply

Supermancho

6 hours ago

 |
prev
 |
next

[–]

Claude has been miserable for anything Java related, in my experience. Use it maybe as a cross check for ChatGPT, which is far superior. They both make mistakes, but Claude repeatedly changes course, contradicts itself, or makes suggestions that are basically unusable. I don't understand why conversations here are always focusing on a bad LLM.

reply

skeptrune

6 hours ago

 |
parent
 |
next

[–]

You likely need to provide it with more direction in your prompts.

reply

Supermancho

6 hours ago

 |
root
 |
parent
 |
next

[–]

I use the same prompts I used for others. Then I rephrased and expanded. This did not improve the quality of responses.

reply

skeptrune

6 hours ago

 |
root
 |
parent
 |
next

[–]

Have you tried prompting the loop? Something like "keep trying until <insert format command here> is happy?"

reply

jolux

6 hours ago

 |
parent
 |
prev
 |
next

[–]

have you used claude code?

reply

Supermancho

6 hours ago

 |
root
 |
parent
 |
next

[–]

yes. specifically.

reply

rr808

13 hours ago

 |
prev
 |
next

[–]

Its super frustrating there is no official guide. I hear lots of suggestions all the time and who knows if they help or not. The best one recently is tell the LLM to "act like a senior dev", surely that is expected by default? Crazy times.

reply

xpe

13 hours ago

 |
parent
 |
next

[–]

When the world is complicated, entangled, and rapidly changing, would you
expect
 there to be one centralized official guide?*

At the risk of sounding glib or paternalistic -- but I'm going to say it anyway, because once you "see it" it won't feel like a foreign idea being imposed on you -- there are ways that help to lower and even drop expectations.How? To mention just one: good reading. Read "Be a new homunculus" [1]. To summarize, visualize yourself like you are the "thing that lives in your brain". Yes, this is non-sense but try it anyway.If you find various ways to accept "the world is changing faster than ever before"andit feels like too much. Maybe you are pissed off or anxious about AI. Maybe AI is being "heavily encouraged" for you (on you?) at work. Maybe you feel like we're living in an unsustainable state of affairs -- don't deny it. Dig into that feeling, talk about it. See where it leads you. Burying these things isn't a viable long-term strategy.*** There is an "awesome-*" GitHub repository for collecting recommended resources to help with Claude Code: [2] But still requires a lot of curation and end-user experimentation: [2] There are few easy answers in a dynamic uncertain world.** Yes I'm intentionally cracking the door open to "Job loss is scary. It is time to get real on this, including political activism."[1]:https://mindingourway.com/be-a-new-homunculus/[2]:https://github.com/hesreallyhim/awesome-claude-code

reply

rr808

12 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks yes of course you're right, still frustrating. I'm nearing retirement so not really worried about job loss, just want to make use of the tools.

reply

xpe

11 hours ago

 |
root
 |
parent
 |
next

[–]

I get that. I probably could have been much more succinct by saying this: We can consciously act in ways that reduce the frustration level even if the environment itself doesn't change. It usually takes time and patience, but not always. Sometimes a particular mindset shift is sufficient to make a frustration completely vanish almost immediately.

Some examples from my experience: (1) Many particular frustrations with LLMs vanish the more I learn about their internals. (2) Frustration with the cacophony of various RAG/graph-database tooling vanishes once I realize that there is an entire slice of VC money chasing these problems precisely because it is uncertain: the victors are not pre-ordained and ... [insert bad joke about vectors here]

reply

hurturue

17 hours ago

 |
prev
 |
next

[–]

I did a similar thing.

put an example in the prompt: this was the original Django file and this is the rewritten in SvelteKit version.the ask it to convert another file using the example as a template.you will need to add additional rules for stuff not covered by the example, after 2-3 conversions you'll have the most important rules.or maybe fix a bad try of the agent and add it as a second example

reply

nisalperi

16 hours ago

 |
prev
 |
next

[–]

I wrote about my experience from the last year. Hope you find this helpful

https://open.substack.com/pub/sleuthdiaries/p/guide-to-effec...

reply

michelsedgh

15 hours ago

 |
prev
 |
next

[–]

I think you shouldn't think so much about it, the more you use it, the better you will understand how it can help you. The most gain will be coming from the models jumping and how you get updated using the best for your use case.

reply

noiv

16 hours ago

 |
prev
 |
next

[–]

I learned the hard way, when Claude has 2 conflicting information in Claude.md it tends to ignore both. So, precise language is key, don't use terms like 'object', which may have different meanings in different fields.

reply

Galorious

14 hours ago

 |
prev
 |
next

[–]

Did you use the /init command in Claude Code at the start?

That builds the main claude.md file. If you don’t have that file CC starts each new session completely oblivious to your project like a blank slate.

reply

helterskelter

17 hours ago

 |
prev
 |
next

[–]

I like to followup with "Does this make sense?" or similar. This gets it to restate the problem in its own words, which not only shows you what its understanding of the problem is, it also seems to help reinforce the prompt.

reply

owlninja

17 hours ago

 |
prev
 |
next

[–]

Would love to hear any feedback using Google's anitgravity from a clean slate. Holiday shutdown is about to start at my job and I want to tinker with something that I have not even started.

reply

jliptzin

7 hours ago

 |
prev
 |
next

[–]

I am probably going to get downvoted to oblivion for this but if you’re going to have AI write your code, you’ll get the most mileage out of letting it do its thing and building tests to make sure everything works. Don’t look at the code it generates - it’s gonna be ugly. Your job is to make sure it does what it’s supposed to. If there’s a bug, tell it what’s wrong and to fix the bug. Let it wade through its own crap - that’s not your tech debt. This is a new paradigm. No one is going to be writing code anymore, just almost like no one is checking the assembly output of a compiler anymore.

This is just my experience. I’ve come to the conclusion that if I try to get AI to write code that worksandis elegant, or if I’m working inside the same codebase that AI is adding cruft to, I don’t get much of a speed up. Only when I avoid opening up a file of code myself and let AI do its thing do I get the 10x speed up.

reply

baobun

7 hours ago

 |
parent
 |
next

[–]

What is the time of the longest-lived actively developed and deployed codebase where this approach has been successful so far and your co-maintainers aren't screaming bloody murder?

reply

BobbyTables2

11 hours ago

 |
prev
 |
next

[–]

Don’t!

reply

bpavuk

11 hours ago

 |
parent
 |
next

[–]

concise answers are the best, and I agree with that one.

I am still curious,why? I have my own set of why's and want to hear yours

reply

shdh

6 hours ago

 |
prev
 |
next

[–]

Get better at reviewing code

reply

justinzollars

6 hours ago

 |
prev
 |
next

[–]

Start with a problem. I'm building
https://helppet.ai
, a voice agent for Veterinarians. I didn't know anything about AI programming other than absolute fundamentals I learned in 2017 through Stanford AI course - this was just theory and a lot has changed. I followed startups doing solving similar problems, and I asked detailed questions to everyone I could. I went to AI hack events to learn techniques others are using. Eventually I ended up with something pretty great and had fun doing so. So start with a problem and then work backwards.

reply

KronisLV

10 hours ago

 |
prev
 |
next

[–]

Automated code checks. Either custom linter rules (like ESLint) or prebuild scripts to enforce whatever architectural or style rules you want, basically all of the stuff that you'd normally flag in code review that
can
 be codified into an automatic check but hasn't been before due to developers either not finding it worth their time to do it, or not having enough time or skill to do that - use the AI to write as many of these as needed, just like:

node prebuild/prebuild.cjswhich will then run all the other checks you've defined like:prebuild/ensure-router-routes-reference-views-not-regular-components.cjs
 prebuild/ensure-custom-components-used-instead-of-plain-html.cjs
 prebuild/ensure-branded-colors-used-instead-of-tailwind-ones.cjs
 prebuild/ensure-eslint-disable-rules-have-explanations.cjs
 prebuild/ensure-no-unused-translation-strings-present.cjs
 prebuild/ensure-pinia-stores-use-setup-store-format.cjs
 prebuild/ensure-resources-only-called-in-pinia-stores.cjs
 prebuild/ensure-api-client-only-imported-in-resource-files.cjs
 prebuild/ensure-component-import-name-matches-filename.cjs
 prebuild/disallow-deep-component-nesting.cjs
 prebuild/disallow-long-source-files.cjs
 prebuild/disallow-todo-comments-without-jira-issue.cjs
 ...and so on. You might have tens of these over the years of working on a project, plus you can write them for most things that you'd conceivably want in "good code". Examples above are closer to a Vue codebase but the same principles apply to most other types of projects out there - many of those would already be served by something like ESLint (you probably want the recommended preset for whatever ruleset exists for the stack you work with), some you'll definitely want to write yourself. And that is useful regardless of whether you even use AI or not, so that by the time code is seen by the person doing the review, hopefully all of those checks already pass.If "good code" is far too nebulous of a term to codify like that, then you have a way different and frankly more complex problem on your hands. If there is stuff that the AI constantly gets wrong, you can use CLAUDE.md as suggested elsewhere or even better - add prebuild script rules specifically for it.Also, a tech stack with typing helps a bunch - making wrong code harder to even compile/deploy. Like, with TypeScript you get npm run type-check (tsc) and that's frankly lovely to be able to do, before you even start thinking about test coverage. Ofc you still should have tests that check the functionality of what you've made too, as usual.

reply

robertpiosik

12 hours ago

 |
prev
 |
next

[–]

Try a free and open-source VS Code plugin "Code Web Chat".

reply

Yokohiii

4 hours ago

 |
prev
 |
next

[–]

The suggestions are really all over the place. Feels AI.

reply

orwin

16 hours ago

 |
prev
 |
next

[–]

I want to say a lot of mean things, because an extremely shitty, useless, clearly Claude-generated test suite passed the team PR review this week, tests were useless, so useless the code they were linked to (can't say if the code itself was Ai-written though) had a race condition, that, if triggered and used correctly, could probably rewrite the last entry of any of the firewall we manage (DENY ALL is the one I'm afraid about).

But I can't even shit on Claude AI, because I used it to rewrite part of the tests, and analyse the solution to fix the race condition (and how to test it).It's a good tool, but in the last few weeks I've been more and more mad about it.Anyway. I use it to generate a shell. No logic inside, just data models, and functions prototypes. That help with my inability to start something new. Then I use it to write easy functions. Helpers I know I'll need. Then I try to tie everything together. I never hesitate to stop Claude and write specific stuff myself, add a new prototype/function, or delete code. I restart the context often (Opus is less bad about it, but still). Then I ask it about easy refactoring or library that would simplify the code. Ask for multiple solutions each time.

reply

Alan01252

18 hours ago

 |
prev
 |
next

[–]

I've been heavily vibe coding for a couple of personal projects. A free kids typing game and bringing back a multiplayer game I played a lot as a kid back to life both with pretty good success.

Things I personally find work well.1. Chat through with the AI first the feature you want to build. In codex using vscode I always switch to chat mode, talk through what I am trying to achieve and then once myself and the AI are in "agreement" switch to agent mode. Google's antigravity sort of does this by default and I think it's probably the correct paradigm to use.2. Get the basics right first. It's easy for the AI to produce a load of slop, but using my experience of development I feel I am (sort of) able to guide the AI in advance in a similar way to how I would coach junior developers.3. Get the AI to write tests first. BDD seems to work really well for AI. The multiplayer game I was building seemed to regress frequently with just unit tests alone, but when I threw cucumber into the mix things suddenly got a lot more stable.4. Practice, the more I use AI the more I believe prompting is a skill in itself. It takes time to learn how to get the best out of an Agent.What I love about AI is the time it gives me to create these things. I'd never been able to do this before and I find it very rewarding seeing my "work" being used by my kids and fellow nostalgia driven gamers.

reply

Esophagus4

12 hours ago

 |
parent
 |
next

[–]

> 4. Practice, the more I use AI the more I believe prompting is a skill in itself. It takes time to learn how to get the best out of an Agent.

This would have been my tip, as well.Talk to others who are good with these tools to learn from what they're doing and read blogs/docs/HN for ideas, but most importantly, make time for yourself on a daily/weekly/monthly/whatever basis to practice with the tool.It's taken me about a year of consistent practice to feel comfortable with LLM coding. It just takes time, like learning any other technology.

reply

daxfohl

14 hours ago

 |
prev
 |
next

[–]

For your task, instead of a direct translation, try adding a "distillation" step in between. Have it take the raw format and distill the important parts to yaml or whatever, then take the distillation and translate that into the new format. That way you can muck with the yaml by hand before translating it back, which should make it easier to keep the intent without the spaghetti getting in the way. Then you can hand-wire any "complexities" into the resulting new code by hand, avoiding the slop it would more likely create.

It may even be worth having it write a parser/evaluator that does these steps in a deterministic fashion. Probably won't work, but maybe worth a shot. So long as it does each translation as a separate step, maybe at least one of them will end up working well enough, and that'll be a huge time saver for that particular task.

reply

salutonmundo

7 hours ago

 |
prev
 |
next

[–]

walk into the woods and never touch a computer again

reply

bpavuk

11 hours ago

 |
prev
 |
next

[–]

first off, drop the idea of coding "agents" entirely. semi-async death valley is not worth it, you will never get into the flow state with an "agent" that takes less than an hour to spin, and we did not learn how to make
true
 async agents that run for this long while maintaining coherence yet. OpenAI is the closest in that regard, but they are still at a 20-minute mark, so I am not dropping the quotes for now.

another argument against letting LLM do the bulk of the job is that they output code that's already legacy, and you want to avoid tech debt. for example, Gemini still thinks that Kotlin 2.2 is not out, hence misses out on context parameters and latest Swift interoperability goodies. you, a human being, are the only one who will ever have the privilege of learning "at test time", without separate training process.replace coding "agents" with search tools. they are still non-deterministic, but hey, both Perplexity and Google AI Mode are good at quick lookup of SvelteKit idioms and whatnot. plus, good old Lighthouse can point out a11y issues - most of them stem from non-semantic HTML. but if youreallywant to do it without leaving a terminal, I can recommend Gemini CLI with some search-specific prompting. it's the only CLI "agent" that has access to the web search to my knowledge. it's slower than Perplexity or even ChatGPT Search, but you can attach anything as a context.this is the true skill of "how to use AI" - only use it where it's worth it. and let's be real, if Google Search was not filled with SEO crap, we would not need LLMs.

reply

siscia

14 hours ago

 |
prev
 |
next

[–]

I will be crucified by this, but I think you are doing it wrong.

I would split it in 2 steps.First, just move it to svelte, maintain the same functionality and ideally wrap it into some tests. As mentioned you want something that can be used as pass/no-pass filter. As in yes, the code did not change the functionality.Then, apply another pass from Svelte bad quality to Svelte good quality.
Here the trick is that "good quality" is quite different and subjective. I found the models not quite able to grasp what "good quality" means in a codebase.For the second pass, ideally you would feed an example of good modules in your codebase to follow and a description of what you think it is important.

reply

ipunchghosts

16 hours ago

 |
prev
 |
next

[–]

Ask people to do things for you. Then you will learn how to work with something/someone who has faults but can overall be useful if you know how to view the interaction.

reply

daxfohl

14 hours ago

 |
parent
 |
next

[–]

Though remember that it's not a human. It's easy to waste a lot of time convincing it to do something in a certain way, then one prompt later it forgets everything you said and reverts back to its previous behavior. (Yes humans can do that too, but not usually to this level).

It's important (though often surprisingly hard!) to remember it's just a tool, so if it's not doing things the way you want, start over with something else. Don't spend too much time on a lost cause.

reply

thinkingtoilet

17 hours ago

 |
prev
 |
next

[–]

There are very real limitations on AI coders in their current state. They simply do not produce great code most of the time. I have to review every line that it generates.

reply

3vidence

10 hours ago

 |
prev
 |
next

[–]

This isn't exactly an answer to your question but I've experienced some efficiency gains in using AI agents for pre-reviewing my PRs and getting it to create tests.

You still get to maintain the core code and maintain understandability but it helps with the tasks the take time that aren't super interesting.

reply

j45

14 hours ago

 |
prev
 |
next

[–]

Follow and learn from peopel on youtube who formerly had the same skill level as you did now.

reply

cat_plus_plus

16 hours ago

 |
prev
 |
next

[–]

AI is great at pattern matching. Set up project instructions that give several examples of old code, new code and detailed explanations of choices made. Also add a negative prompt, a list of things you do not want AI to do based on past frustrations.

reply

seg_lol

16 hours ago

 |
prev
 |
next

[–]

Voice prompts, restate what you want, how you want it from multiple vantage points. Each one is a light cone in a high dimensional space, your answer lies in their intersection.

Use mind altering drugs. Give yourself arbitrary artificial constraints.Try using it in as many different ridiculous ways you can. I am getting the feeling you are only trying one method.> I've had a fairly steady process for doing this: look at each route defined in Django, build out my `+page.server.ts`, and then split each major section of the page into a Svelte component with a matching Storybook story. It takes a lot of time to do this, since I have to ensure I'm not just copying the template but rather recreating it in a more idiomatic style.Relinquish control.Also, ifyouhave very particular ways of doing things, give it samples of before and after (your fixed output) and why. You can use multishot prompting to train it to get the output you want. Have it machine check the generated output.> Simple prompting just isn't able to get AI's code quality within 90%Would simple instructions to a person work? Esp a person trained on everything in the universe? LLMs are clay, you have to mold them into something useful before you can use them.

reply

morkalork

17 hours ago

 |
prev
 |
next

[–]

In addition to what the sibling commenters are saying: Set up guardrails for what you expect in your project's documentation. What is the agent allowed to do when writing unit tests vs say functional tests, what packages it should never use, coding and style templates etc.

reply

dboreham

17 hours ago

 |
prev
 |
next

[–]

1. Introduce it to the code base (tell it: we're going to work on this project, project does X is written in language Y). Ask it to look at the project to familiarize.

2. Tell it you want to refactor the code to achieve goal Z. Tell it to take a look and tell you how it will approach this. Consider showing it one example refactor you've already done (before and after).3. Ask it to refactor one thing (only) and let you look at what it did.4. Course correct if it didn't do the right thing.5 Repeat.

reply

halfcat

16 hours ago

 |
prev
 |
next

[–]

>
prompting just isn't able to get AI's code quality within 90% of what I'd write by hand

Tale as old as time. The expert gets promoted to manager, and the replacement worker can’t deliver even 90% of what the manager used to. Often more like 30% at first, because even if they’re good, they lack years of context.AI doesn’t change that. You still have to figure out how to get 5 workers who can do 30-70% of what you can do, to get more than 100% of your output.There are two paths:1. Externalized speed: be a great manager, accept a surface level understanding, delegate aggressively, optimize for output2. Internalized speed: be a great individual contributor, build a deep, precise mental model, build correct guardrails and convention (because you understand the problem) and protect those boundaries ruthlessly, optimize for future change, move fast because there are fewer surprisesOnly 1 is well suited for agent-like AI building. If 2 is you, you’re probably better off chatting to understand and build it yourself (mostly).At least early on. Later, if you nail 2 and have a strong convention for AI to follow, I suspect you may be able to go faster. But it’s like building the railroad tracks before other people can use them to transport more efficiently.Django itself is a great example of building a good convention. It’s just Python but it’s a set of rules everyone can follow. Even then, path 2 looks more like you building out the skeleton and scaffolding. You define how you structure Django apps in the project, how you handle cross-app concerns, like are you going to allow cross-app foreign keys in your models? Are you going to use newer features like generated fields (that tend to cause more obscure error messages in my experience)?Here’s how I think of it. If I’m building a Django project, the settings.py file is going to be a clean masterpiece. There are specific reasons I’m going to put things in the same app, or separate apps. As soon as someone submits a PR that craps all over the convention I’ve laid out, I’m rejecting aggressively. If we’ve built the railroad tracks, and the next person decides the next set of tracks can use balsa wood for the railroad ties, you can’t accept that.But generally people let their agent make whatever change it makes and then wonder why trains are flying off the tracks.

reply

Arisaka1

4 hours ago

 |
parent
 |
next

[–]

>2. Internalized speed: be a great individual contributor, build a deep, precise mental model, build correct guardrails and convention (because you understand the problem) and protect those boundaries ruthlessly, optimize for future change, move fast because there are fewer surprises

I think the issue here is, to become a great individual contributor one needs to spent time on the saddle, polishing their skills. And with mandatory AI delegation this polishing stage will take more time than ever before.

reply

UncleEntity

12 hours ago

 |
parent
 |
prev
 |
next

[–]

> But generally people let their agent make whatever change it makes and then wonder why trains are flying off the tracks.

IMO, this is the biggest issue. Well, along with just straight up ignoring what you tell it and doing whatever it thinks should be done.But, to answer the actual thread question: Make it work (all the tests pass) then make it right is the way I'm getting quality work out of the robots. As long as you watch them to make sure they don't either change the tests to pass on buggy code or change the code to pass on buggy tests (yes, Claude is quite proficient and eager to do both) then the code gets better and better as new stuff is added and the 'flow of computation' is worked out.Oh, and have an actual plan to follow so they don't get distracted at the first issue and say they're finished because they fixed some random unrelated bug. I've also found it helpful to have them draft up such a plan while they're knee deep in that section of the code for related work so they don't have to figure it all out again from scratch and try to add a few extra levels of abstraction just because.

reply

dominotw

16 hours ago

 |
prev
 |
next

[–]

dont forget to include "pls don't make mistakes"

reply

swatcoder

14 hours ago

 |
prev
 |
next

[–]

> This kind of work seems like a great use case for AI assisted programming

Always check your assumptions!You might be thinking of it as a good task because it seems like some kind of translation of words from one language to another, and that's one of the classes of language transformations that LLM's can do a better job at than any prior automated tool.And when we're talking about an LLM translating thegistof some English prose to French, for a human to critically interpret in an informal setting (i.e not something like diplomacy or law or poetry), it can work pretty well. LLM's introduce errors when doing this kind of thing, but the broader context of how the target prose is being used is very forgiving to those kinds of errors. The human reader can generally discount what doesn't make sense, redundancy across statements of the prose can reduce ambiguity or give insight to intent, the reader may be able to interactively probe for clarifications or validations, the stakes are intentionally low, etcAnd forsomekinds of code-to-code transforms, code-focused LLM's can make this workokaytoo. But here, you need a broader context that's either very forgiving (like the prose translation) or that's automatically verifiable, so that the LLM can work its way to the right transform through iteration.But the transform you're trying to do doesn'teasilysatisfy either of those contexts. You have very strict structural, layout, and design expectations that you want to replicate in the later work and even small "mistranslations" will be visually or sometimes even functionally intolerable. Andwithout something like a graphic or DOM snapshotto verify the output with, you can't aim for the iterative approach very effectively.TLDR; what you're trying to do is not inherently a great use case. It's actually a poor one that canmaybebe made workable through expert handling of the tool. That's why you've been finding it difficult and unnatural.If your ultimate goal is to improve your expertise with LLM's so that you can apply them tochallenginguse cases like this, then it's a good learning opportunity for you and a lot of the advice in other comments is great. The most key factor being to have some kind of test goal that the tool can use for verify its work until it strikes gold.On the other hand, if your ultimate goal is to just get your rewrite done efficiently and its not an enormous volume of code, you probably just want to do it yourself or find one of our many now-underemployed humans to help you. Without expertise that you don't yet have, and some non-trivial overhead of preparatory labor (for making verification targets), the tool is not well-suited to the work.

reply

bgwalter

13 hours ago

 |
prev
 |
next

[–]

Hey, I am bgwalter from the anti-AI industrial complex, which is a $10 trillion industry with a strong lobby in DC.

I would advise you to use Natural Intelligence, which will be in higher demand after the bubble has burst completely (first steps were achieved by Oracle this week).

reply

JackSlateur

14 hours ago

 |
prev

[–]

You can using a single simple step: don't

The more you use IA, the more your abilities decreases, the less you are able to use IAThis is the law of cheese: the more cheese, the more holes; The more holes, the less cheese; Thus, the more cheese, the less cheese;

reply

ransom1538

14 hours ago

 |
parent

[–]

This is the fastest way to unemployment benefits (if that is the goal).

reply

eqvinox

14 hours ago

 |
root
 |
parent
 |
next

[–]

This is just meaningless knee-jerking, try making an actual argument. At least the GP is arguing that more use of AI leads to loss of personal coding skills. It's unclear at this point what level AI will grow to, i.e. it could hit a hard wall at 70% of a good programmer's ability, and in that case you would really want those personal coding skills since they'll be worth a lot. It could also far exceed a good programmer, in which case the logic reverses and you want those AI handling skills…

NB: I'm talking about skill cap here, not speed of execution. Of course, an AI will be faster than a programmer…*if*it can handle the job, and*if*you can trust it enough to not need even more time in review…

reply

ransom1538

8 hours ago

 |
root
 |
parent
 |
next

[–]

"This is just meaningless knee-jerking,"

Your point is valid."AI leads to loss of personal coding skills"Unfortunately, I can no longer do long division. No one will pay me to do long division and I have a calculator now. I could stay sharp at long division for a hobby though. Keep those for loops sharp if you want, but I don't see people paying you to hand code. Eventually, it will just be a liability. (like not using a calculator)."it could hit a hard wall at 70% of a good programmer's ability"That is not what NVDA,AMZN,GOOG,or MSFT believe. Maybe you are right and they are all wrong. They do have some smart people on staff. But, betting against the sp50 is generally a terrible plan.

reply

eqvinox

5 hours ago

 |
root
 |
parent
 |
next

[–]

> Keep those for loops sharp if you want, but I don't see people paying you to hand code.

Well, personally speaking, I'm paid to hand code; LLMs have not reached the quality of my code output yet and I'm seeing no pressure at all to use LLMs.Relatedly, I work on an open source project where the constraining resource is review (as it is in most open source projects.) The current state is that LLM generated code is incredibly hard and annoying to review and there is a lot of pushback.So, I'm going to wait and see.(...especially since there's also legal challenges to LLMs trained on open source code with no regard to its licenses.)

reply

tjr

6 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

There have been lots of tools that have made programming more efficient. Probably most programmers have used some of those tools, but very few have used every tool. Why do you suppose that LLMs in particular
must
 be used?

reply

merlincorey

8 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

LLMs aren't calculators; for example, your calculator always gives you the same outputs given the same inputs.

Long division is a pretty simple algorithm that you can easily and quickly relearn if needed even your LLM of choice can likely explain that to you given there's plenty of writing about it in books and on the internet.

reply

JackSlateur

1 hour ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You think those companies are betting thousands of billions and that's all about code ? Haaha

It is all about money and powerAka pub and mass control (/propagande)Another good reason to avoid getting raped by AI (but nothing related to the topic at hand (code))

reply

Arisaka1

11 hours ago

 |
root
 |
parent
 |
prev

[–]

Have we really reached the point where a candidate gets outright rejected for not using AI tools, without taking personal aptitudes into consideration?

reply

tjr

6 hours ago

 |
root
 |
parent
 |
next

[–]

Whose personal aptitudes could possibly match those of Claude the Magnificent?

reply

JackSlateur

55 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Last person we recruted, the AI question made our choice

"Are you using AI ?"(his response, tldr: "yes but actually no, because it sucks")Great collaborator

reply

platevoltage

10 hours ago

 |
root
 |
parent
 |
prev

[–]

It wouldn’t surprise me if resume filters now look for how many times AI buzzwords are present.

reply

Guidelines
 |
FAQ
 |
Lists
 |
API
 |
Security
 |
Legal
 |
Apply to YC
 |
Contact

Search:
