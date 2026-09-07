---
title: 'Ask HN: How do you manage skills files? | Hacker News'
url: https://news.ycombinator.com/item?id=49589914
site_name: hnrss
content_file: hnrss-ask-hn-how-do-you-manage-skills-files-hacker-news
fetched_at: '2026-09-07T16:17:41.162925'
original_url: https://news.ycombinator.com/item?id=49589914
date: '2026-09-06'
description: 'Ask HN: How do you manage skills files?'
tags:
- hackernews
- hnrss
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
Ask HN: How do you manage skills files?
236 points
 by 
imadtaieber
 
16 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
215 comments
How do you find skills, keep them organized, and make sure they actually work? Do you keep improving them over time?

I believe skills will eventually be eating by model capabilities, but until then I'm just looking for a better way to manage things.

 
help

nhod
 
1 minute ago
 
 | 
next
 
[–]

I've been using a project called SX 
https://github.com/sleuth-io/sx
 to manage them. It has its quirks, but overall I find it to be very useful.

One thing I've had to write as a layer on top of it is a way to assemble agent-specific CLAUDE.md / AGENTS.md from fragments.For example, I have a little fragment that has all agents respond to me in ordered list format. (Since they often ask a bunch of question all jumbled throughout a response, the ordered list format allows me to respond to those specific questions.) And I also have a growing anti-Claudeism fragment as well.Then I combine this with project-specific fragments and have it assembled into into a single CLAUDE.md / AGENTS.md. The layer also does a little reporting on the length of the resulting files and notifies me if it ever grows beyond a certain size.

reply

picklenerd
 
5 minutes ago
 
 | 
prev
 | 
next
 
[–]

I don’t find skills. I write my own skills based on things I do frequently and repeatably. I keep them version controlled locally and in GitHub, and I symlink that folder to my various agent skill folders so they all stay up to date.

I feel like downloading a bunch of skills is another one of those useless collections people make purely because they have infinite options. It’s like those collections of thousands of bookmarks you’re never going to click or pirated ebooks you’re never going to read.It’s trivial to write your own skills with agents. The best way to use them, imo, is to make them when you have repeatable agent workflows, written to your own personal taste, and updated as your workflows change.Here’s what I have for reference:- Remove agent-speak from code, docs, and markdown files.- Ask sequences of questions the way I like to be asked questions. Used instead of the question tool. This is my primary design skill as well.- How to use jj the way I want my agent to use jj- Dispatch subagents with 6 different sets of priorities. Those priorities are defined in the skill, so I can always dispatch all 6 of them to write or review code. Includes a template for code reviews- Manage a local MD issue tracker for personal projects

reply

darren0
 
27 minutes ago
 
 | 
prev
 | 
next
 
[–]

Skills are encoding a process. The more niche the process the more useful the skill. As the process grows to a larger audience it becomes more generic and thus converges with the models knowledge. So skills are better for a smaller group of people. And similarly how it's packaged and maintained becomes specific to that group.

reply

avaer
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Skills are mostly snake oil, the way people use them (the aspiration to download kung foo from a celebrity).

There was a time when maybe it mattered (last year), but with good repos and good prompts today's agents can find exactly what they need without any skills."Skills" as developer macros can be useful, but at most those are things shared with the team (in the repo), not something you download from the internet. If you have so many skills that you feel the need to manage them, that's a code smell.

reply

itishappy
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

My company ran a test and found that they reduce token output on flagship model by something like 2-4x, and that number has been 
increasing
 with newer models. I suspect the increased subagent usage is driving this trend, because this means we're relying on models to do their own prompt engineering.

Yes, they are just text, and can therefore be replaced with good prompting. However, this also means they confer a real benefit: a good set of skills creates a transferable baseline, raising the skill floor and offering a more consistent experience across the organization.

reply

colechristensen
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am somewhat confused by takes like this. Of course skills are just prompts, this is the whole point.

A skill is just a stored prompt you want to put more information into than you're likely to type out every time you intend to do that thing. Documentation of a business process.

reply

woud420
 
41 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's not just a stored prompt, you can attach re-useable scripts to them to offer more determinism. ex: a script that validates that a PR follows exactly the template you want, with a max of N lines per entry.

The more determinism you have, the more consistent you can be and the more leverage you can build. (yes I understand that skill calls are non deterministic).

reply

bakies
 
31 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's just a stored prompt that references a script :)

reply

verdverm
 
28 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

We do that, but keep the scripts in the code and just tell them in the markdown where the scripts are, same with "references" (docs/) for us. It never made sense to me to put those in a skill dir, many are useful across skills and for humans (many written for humans before agents were a thing)

One of the more interesting benefits to skills is that many harnesses now run the inline command(s) in backticks, shortcutting the model needing to make a tool call. This is helpful for deterministically building up context content for the skill before the agent ever sees it.We take this further in some instances and have workflows that (1) does deterministic context gathering (2) invokes an agent (3) processes a file the agent is told to produce. This has made our PR review agent much better and removed it's access to all credential files. We have a step that gathers the diff + existing pull request comments into a .review dir, let the agent process that and create a comments.jsonl, then run a script in a new step to apply the comments against the API

reply

estearum
 
56 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What are you confused by? You're saying the same thing they said.

They added the additional claim that writing the skills down (apparently) prevents the models from having to self-prompt on the fly and therefore reduces token consumption.

reply

sigmoid10
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

>but with good repos and good prompts

I think waaay more people struggle with this than HN would have you believe. In the real world, not everyone is a software dev with a developer mindset to using these tools. Normal people essentially type the equivalent of "Make me X!"
and complain when the model assumes anything in their underspecified mess of a prompt. There are skills like grill-me that can potentially help these people a lot, but in the end I believe models will just be smart enough to understand your level of knowledge and intent to do this stuff on their own. They are getting much better on pushing back on poor user input already. The problem is that when they double down on hallucinations (very rare nowadays but I still see it happen in enterprise projects with the latest models). So you kind of need to know when to push back on the model as well. But for that you have to be really good at the subject.

reply

kristianc
 
1 minute ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's interesting as grill-me and the other Matt skills are very much positioned to people who would consider themselves as developers. In fact, I'm not sure if people who were completely new to development would have heard of him at all.

reply

wongarsu
 
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

I tend to agree. Skill files become less useful as developer skill increases.

As a skilled developer my repetitive instructions are mostly one or two sentence phrases for staring something like a highly-interactive planning session, or a self-supervised implementation session with my preferred setup of implementation and review subagents. I can specify those out by hand, or save a couple keystrokes with a tiny skill file.But if you are not a software dev you might lack the vocabulary to tell the agent what you want. If you don't know what tenant isolation is, chances are your app will have a broken security model because you can't ask for it, and probably won't think to ask the agent for a security review either. Skills can mitigate a lot here

reply

HumblyTossed
 
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

> I think waaay more people struggle with this than HN would have you believe.

I'm sure we all know. I mean, just ask anyone to write a story and break it into small tasks that can each be accomplished completely in a day.

reply

ma2kx
 
23 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's maybe the case if you always use the most popular framework and restrict your environment to a basic setup. But as soon as you e.g. build a website with SolidJS, Bulma and vite++ (vp), at least the models I tried are all the time somewhat confused, want to steer your project in a certain direction and build strange workaround so it works the way they are trained on.

Same with mcp. I want them to use the jsdelivr cdn instead of them scraping github against the rate limit. etc. But if I dont explicitly state to strictly use the $%!$@@! mcp for searching in repositories they simply ignore the mcp and even if clearly instructed, they still often fall back to gh.Putting every detailed instruction in the AGENTS.md would just unnecessarily bloat the context and it works well enough to just instruct them in the AGENTS.md when to use which skill. Yet I agree that Skills are not some voodoo magic to provide your model super capabilities.

reply

misja111
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not about giving hints to agents because they wouldn't find it out otherwise. It's about saving the work of them having to find out. Good skills files save tokens.

reply

listingbott
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

How do you actually measure the token savings? Do you compare the same task with and without the skill, or is it more of a noticeable difference over time?

reply

mathgeek
 
57 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Both, in a way. In order to be sure it's the skill reducing token usage, you measure it with and without the skill, and then you do that periodically to account for all the other variables.

Alternatively, you pick a belief based on prior evidence from either approach you mentioned, which is the natural thing that many of us do.

reply

sejje
 
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

By watching them get it the first time, instead of watching them hit 10 locations before finding it.

reply

mpalmer
 
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

Having too many skills files increase tokens even when they don't get fully read. It's a fine line.

reply

nextaccountic
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's why you need to curate and adapt the skills for your specific project. That is, don't blindly accumulate skills downloaded from the web

reply

jaapz
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> "Skills" as developer macros can be useful, but at most those are things shared with the team (in the repo), not something you download from the internet. If you have so many skills that you feel the need to manage them, that's a code smell.

I have three development machines. You kinda need something like git to keep everyone in sync!And there's still value in encoding a process in a skill - it's way more token efficient to tell the model what but also HOW to do something. Otherwise, it just spends a lot of tokens figuring out something that they previously did already.

reply

ryaniscool
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

There needs to be a word for this type of interaction because it’s so common in software engineering:

Q: I need help doing XA: if you’re doing X, you’re doing it wrong.I propose the word shamesplaining. What do you think?Not saying your opinion isn’t valid. It just doesn’t answer the question and it’s disturbing that this is the top voted answer. It sounds more like a criticism than an answer.

reply

SoftTalker
 
32 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The corrollary interaction is this:

Q: I need help doing XA: What are youreallytrying to do?

reply

skinfaxi
 
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

It's called the xy problem already.

reply

InsideOutSanta
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Depends on what you do. If you work with proprietary tech that is not in LLM training data and can't easily be found on the internet, you're cooked without good skill files.

reply

specproc
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah, this is my use case for skills. Even with good documentation, it feels better to have things local and easy to tweak.

I'd add to that I've also used them as a style guide. The project involved taking in unstructured inputs and creating structured outputs. Lots of choices along the way, and it seemed a neat way to encapsulate decisions we'd made as a team.Storage, well it's just for the one project, so the repo. Can't say I've used them beyond that.

reply

p2detar
 
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

I agree it depends, but I can offer another angle: By writing a few py tools and creating skills around them I was able to save tokens, so these skills were cost-effective in my case, they lowered the cost of the tasks I execute.

reply

JauntyHatAngle
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, skills as a "portable power" isn't really the use case for me unless it's entirely generic and even then sparingly.

I've mostly followed what anthropic suggests, which is putting less into context and more into skills, to keep the "how" out of context until it is needed to reduce context bloat.Skills have some instructions but are primarily informed repo specific instructions and keep their context away from the rest of the repo to keep things sanitised for me.I've found it to be useful in that context.

reply

tetha
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Skills have some instructions but are primarily informed repo specific instructions and keep their context away from the rest of the repo to keep things sanitised for me.

Skills and agents in the Claude world can also be extended and evolved over time, as they are committed "code".For example, we have an agent which can take a statement or a support ticket and identifies the services, tenants and infrastructure components likely meant in the ticket or request. Similar to a skill, Claude can invoke this on demand in a conversation.This started very simple, but various people spent time tuning it over the last 4-6 months. They have "taught" it to pick up on jargon from different departments, writing style of different departments, how they think about their systems.With all of that tuning over time it has become quite "clever" in identifying the mentioned systems and - if requested - the train of thought leading to this conclusion.Similar things are happening with skills for various task, be it Ansible integration tests, upgrade chores and so on. The first version can be fairly underwhelming, but continuously improving it after each usage can make them very powerful.

reply

seer
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hah I think if a repo is “standard” enough that an agent can navigate it freely without any help or direction, maybe it’s not worth having altogether?

Even fable _regularly_ stumbles as big repos or custom configurations, even for projects that fable itself built with high dev quality standards and modern design direction.It just can’t hold it all in its context and will be forced to do “software archeology” all the time to figure things out - yeah it will work _most_ of the time, but to truly be able to scale and have autonomous agents reliably work and mold your codebase you need a lot more structure - tests, lints, compilers, validators etc. Your “skills” or policy files are there so agents can resolve issues and heal things themselves without your explicit direction.If I have several tabs, each holding an agent team, with each agent spawning subagents as it sees fit, all of that apparatus has to ground itself _somewhere_ and if you don’t make decisions yourself, it will make decisions for you, save them in its own skill files, but some of these you might not like.

reply

saejox
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

i agree, skills downloaded from the internet are all snake oil.

creating your own skills however good for both reducing the token usage & increasing reliability. those damn llms are not deterministic, asking same thing twice produces 2 different results.

reply

Azkar
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This has been my experience (with downloaded skills), and currently my workflow is almost 100% skill driven.

Every feature I build uses a skill that does the following:1. Read a ticket and get context on the task. The ticket was probably written by another agent after a conversation with myself about what is happening/needs to happen, etc.2. Plan the task, asking for clarification where needed3. Pressure test the plan, and validate the plans logic (subagents)4. Implement5. Runtime/local validation6. Post PR, review it using applicable agents (database, security, code, prose...)7. Fix PR based on feedbackI generally get excellent results out of this process, and I cannot imagine trying to orchestrate this without a skill. But I also can imagine my workflow isn't tuned to be super usable for anyone else.

reply

mat_b
 
21 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What does your prompting look like for step 3 - pressure test the plans?

reply

xpnsec
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Where they are very useful is as a documentation source for LLMs. For example, I work in infosec and often have to reference DSLs (Cobalt Strike aggressor script for example). Having a skill which is an offline index to carved up function docs, which an LLM can use without having to think, then search for, then download huge 1 page documents with all function documentation, and pollute the context… very useful.

reply

mstr32
 
17 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Looks like this is a combination of documentation with a skill, right? 
How do you manage these skills across projects?

reply

mhh__
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

They're literally just documentation with a hat on. I don't mind a skill saying where the docs are but an overreliance on skills is simply proof someone isn't able to reason about the gestalt

reply

breckenedge
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My approach is different. Skills I write mostly use Python to save on the agent needing to run its own loops.

I use these loops to monitor the CI build and PR approvals rather than having the agent poll, and even Opus gets the commands wrong enough to make it worth it.Last week I wired up a skill for the agent to share screenshots in PRs via specific S3 buckets and AWS CLIs. Again, the agents guess at the right commands often enough to make it worth being explicit.Sure these could have gone in CLAUDE.md, but not every agent needs the context.And at the company level, I can push skills to everyone’s Claude via the Teams function, they don’t need to edit configs or even know what a skill is.

reply

mhh__
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

small behaviours are fine, yes, what i was referring to was people making "foobar api skill" with just a bad compression of the foobar docs in a .md

reply

lovetocode
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This could be better summed up to the misuse of skills. Skills were not designed to be a way to make an agent more intelligent. Instead, skills are designed to allow agents to have certain tasks that are repeatable and predictable. It’s a misnomer really.

reply

buffalobuffalo
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you are spending time on all text forums like this, you are likely a person whose skill set skews towards the verbalization of abstract concepts. This is also the exact skill set needed to use LLMs well. If you are able to articulate exactly what you want in a concise prompt, little else is needed.

I think we tend to overlook the fact that LLMs have tilted the scalesheavilyin favor of those with good verbal skills. A huge portion of the population (including a portion of highly skilled software engineers) is not great at doing this. For them, harness skills still act as a kind of scaffolding; they support automated work on a project in cases where insufficient details is given in the prompt.

reply

SoftTalker
 
21 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In my experience, while software engineers can be socially awkward/introverted, they generally do have good verbal skills, an excellent vocabulary and can be concise and articulate in writing, when there's no social pressure. There are some exceptions of course, but being able to translate an idea or set of tasks into a concise written language form is essentially what programming is.

reply

frumiousirc
 
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

The closest I get to finding skills useful is when I find myself repeating myself to an LLM. This tends to happen most when I am starting new projects and want to communicate basic design principles and patterns to follow and libraries to use. What I did was to factor and store these "chunks" of instruction in some text files. I then made a little script that can list what chunks are available and when given a subset will essentially `cat` the selected files to emit AGENTS.md content which I save into the new project or append to shore up an existing one.

Your observation on the readership bias of HN is a good one for people to add to their HUMANS.md before reading and commenting. :)

reply

8fingerlouie
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I find them useful for deploying task specific agents, like reviewing Jira tickets, or otherwise ensuring compliance in open format submissions.

Otherwise I agree, and you don't even have to be that verbose with prompt engineering these days as LLMs have gotten increasingly good at figuring out what you want.

reply

igor_nast
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

100% - influencers pretend they know something and produce all in one skills pack - that doesn't make sense

reply

walthamstow
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Great way to go viral though

reply

0x696C6961
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The only useful generic skill I have is the ast-grep one.

reply

nsonha
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Not everyone use AI only for coding, for “code smell” being even applicable here. Many of my skills are just processes distilled from actual sessions doing odd tasks and coordinating different tools. It’s pretty reasonable to assume that it saves the agent from repeating that first time exploration fumbling

reply

enraged_camel
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

No, not really. Yesterday I asked Opus if it can read the logs from the sessions I have on the local ChatGPT app. It looked around and said no, that’s not possible. I said “what about these jsonl files in this folder?” It read them and said “ah yes these seem to be it!”

So I went ahead and created a skill for it. This is so that future Opus agents won’t come to the wrong conclusion the first one did. I can say “read the codex session titled ‘X’” And they will know exactly what to do and do it effortlessly.

reply

Narciss
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Woaaah buddy this is such a wrong statement that I’d delete it if I were you.

Can’t believe that people confidently spew blatantly false statements like this.Skills matter, a lot, to every action that requires the AI to find stuff out, so that it doesn’t have to find the same stuff out again. Operating a website, building PowerPoints the way you like them, operating across different surfaces like APIs + GUIs…otherwise the AI has to relearn how to do it every time.Be confident about things you know. Study about things you don’t.

reply

lxgr
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don’t feel strongly on skills either way, but why would you suggest GP delete their comment, without which we wouldn’t even be having this (in my view productive) discussion?

reply

theahura
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

First, a lot of people in thread are saying you don't need skills. This is pretty wrong. There is a lot of alpha in using any set of skills that implements SPACE (search, plan, assert, code, evaluate). See: 
https://open.substack.com/pub/theahura/p/agentics-using-meta...

Second, we share all of our sets of skills in a purpose built registry:https://noriskillsets.dev/you can use any of our public skillsets from there. If you're on a team you can also sign up to get your own private registry. Makes organization much easier.Finally, for local development, we use this CLI to manage skills (https://github.com/tilework-tech/nori-skillsets). This is a tool that lets you bundle skills into groups, and then switch between those groups. So for eg if I'm making a slide deck I'll use an admin skillset, and for coding I'll use a swe skillset, and for debugging I'll use a debugging skillset.We do keep tinkering with our skillsets, but not very much. I don't get the need to adjust things for every model release, doesn't seem necessary for us in practice

reply

bensyverson
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

I'm building something similar with `Agents`[0] (think of it as a package manager for AGENTS.md snippets). I'm getting good results by including detailed instructions for certain tasks in the repo, and providing hints in AGENTS.md about when to use them. It's basically a simpler version of Skills—but it feels like AGENTS.md adherence is higher than Skill adherence.

[0]:https://github.com/bensyverson/agents/

reply

alexhans
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

- I don't find skills, I create them

- Keep them organised in software repos that you install with symlinks for all coding harnesses that you have. Progressive disclosure based on the frontmatter does the rest.- I make sure they work with AI evals. Think of them like integration tests to prove behaviour. They're useful to optimize your flows. I try to make my skills be mostly a translation between natural language and good small fast tools that they call.- I change them as a new problem arises. Not just because.Skills can't be eaten by model capabilities if skills represent a workflow that is custom to my team or my person.I wrote about a good mental model in the past:https://alexhans.github.io/posts/series/evals/building-agent...

reply

stingraycharles
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

People always say this about the evals, but I find it hard to have a practical implementation of such a thing where you won’t end up spending 100x the amount of time on the evals than building the skill itself.

Like, ok, I have a debugging skill, now how do I make evals except for the most trivial things?

reply

RicDan
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You don't. If you're using skills to force the AI to fullfill some must criterias, it's not going to work. Must criterias need deterministic checks -> be it hooks or what not.

This is also my biggest gripe with AI. I.e. for specifications, no matter what hype machine I tried, it never fulfilled my criterias, which are: easily verifiable, concise, small specs. Hence I builthttps://github.com/RicardoMonteiroSimoes/Yamletinitially for claude code, but then decided to use extend it for pi.dev. I now have a dedicated docker image for pi.dev, that only contains Yamlet plugin, and whenever I work on spec I spin it up.The end result is a .yaml file that easily works in git + git diff, so that I can then proceed with the technical specs-

reply

jurgenburgen
 
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

Why do you have a debugging skill? Just tell it to read the docs.

Skills are for packaging instructions for how to interact with your organizations homebrew process and tools. By definition skills shouldn’t be useful outside of your org because they’re just docs and third party tools already have them for humans.

reply

stingraycharles
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That’s one, very narrow use case of skills.

reply

well_ackshually
 
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

Anthropic must love you. Re-blow hundred of thousands of tokens to relearn how to use your profiler and build system at every debugging attempt.

reply

mark_l_watson
 
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

I am starting to wonder if I am doing something wrong: I ignore evals and instead I just try new models or new harnesses (or tweak my own harnesses) by solving problems I want to solve in any case; I just use new tools and form my own subjective opinions of them.

reply

TobTobXX
 
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

A skill should only document behaviour the LLM didn't/couldn't exhibit on its own.

So you take your failed case (eg. working with gdb or whatever), write a skill and then test for that failed case.

reply

hakunin
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There are also skills that help LLM do the thing it can do without the skill, but faster (by cutting out unnecessary discovery). I guess for such skills the fail case is "being slow"?

I imagine many fail cases can burn a lot of tokens/usage/time because failing LLMs can be very persistent. Maybe some upper bound (turn count, timeout) would help too.

reply

resonious
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Big yes on this. I do not understand the appeal of skill shopping. The one exception I have is things like the Axiom Apple development skills and e.g. the official Flutter skills. At that point the skills are just docs though. It's either I remember to paste a URL to the official docs or I just install the skill. But shopping around for random skills just sounds extremely unappealing.

reply

flurdy
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I do both, or rather I do 'skill browsing', for new ideas to then evaluate the skill with my agent if they are useful. Most are not, but some I extract ideas from to augment my own skills 
https://github.com/flurdy/agent-skills/tree/main/skills#shar...

Though most of the time my skills are just things I found useful and could avoid repeating myself by having as a skill.That I also use it to route model used withhttps://github.com/flurdy/pi-skill-model-routeris also a reason

reply

imadtaieber
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What about skills that you need across projects?

reply

gregwebs
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Get them under version control.
I have a git repo with my skills for software development [1]. There is an installer script that symlinks to the skills. Updating the skills on a machine is then just a matter of advancing the git repo. One of the skills comes with some bash scripts, but the rest are effectively just prompts.
Putting project specific skills in projects works well.

I make sure they work by understanding every skill, reviewing pull requests, and testing the end product. The result is rarely perfect, so I am constantly tweaking the skills and how I use AI.[1]https://github.com/gregwebs/skills-sdlc/

reply

WatchDog
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I don't use any skills, what kinds of skills are people finding most useful?

For general tasks, the model seems perfectly capable of figuring out things itself, for project or environment specific tasks, I just put that information in the readme or agents.md file.

reply

pletnes
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

I make skills for «this is how I like to do things in this company / project». Query test database, git branch names, commit message style, which cloud things can be inspected like logs etc. I don’t see the point in trying to teach the models things that is in the documentation of git, python, what have you. They already know.

reply

stanmancan
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Isn’t that what the agents.md in your project is for?

reply

jbeninger
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's possible I invented skills before they were common. I've always had some instructions in agents.md that are something like "when working with typescript, read prompts/conventions.ts.md, when working with our fooBar module, read prompts/foobar.md"

I'm not sure if this differs greatly from skills. Maybe my wording makes these "skills" less likely to be read at the correct times, but I haven't seen an issue.

reply

paool
 
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

I try to keep agents/Claude.md as tiny as possible. With high level "truths" that don't change. Stack used, invariants, file structure, and some scripts.

Skills are more for things you do often. I run mutation tests, type check,linting,etc. I _could_ just prompt and copy/paste the same prompt each time I need to, or I can just run /tests.I also have skills for specialized tasks I need every once in a while, like a ux skill, a text skill optimized for xyz, etc.

reply

jpalomaki
 
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

Depends on how much information and details you have. The agents.md always goes into context. Detailed testing or process information might be excessive, when agent is working on UI. Skills are pulled when needed.

reply

distances
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I handle the context problem by splitting the details to dozens of small md files. Agents.md acts as a router that directs the llm to correct documentation file/folder according to the task at hand.

This documentation is its own git repo, and the agents.md file has an explicit instruction to update the docs when it has learned something general that can be useful in future sessions. I then occasionally review and prune those docs.

reply

oakesm9
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's exactly what skills do.

The description in the front-matter (at the top of the skill markdown file) is the only thing in the context and used by the agent to determine when to read in the rest of the skill file.

reply

jve
 
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

Skills are evaluated by short description whether to read them into context.

Skills itself may be lengthy so...

reply

ygjb
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

So the term used internally is to make things "Determinishtic". I use skills extensively, combined with SOPs, scripts and MCP servers.

An example skill I have is SessionMiner, which is installed via post session hooks in Claude and Kiro, and analyzes the session, what was accomplished, and whether or not it should be turned into a skill, then when it summarizes it, the decisions it came to and either fires off a message to me for followup if it decides a new skill or tool should be built, or it catalogues the approach so that future analysis can identify trends in how I use the tools.Over time it has built me a fairly decent stable of repeatable skills and tools, and highlighted process deficiencies and nominated process changes that I have pursued.Another skill is a communications analysis skill; I started using it summer last year I think, and it scans my communications across a broad cross-section of my activity online. It tracks the commitments I make, ensures that I follow up with people that I might miss, ranks and scoresmycommunication against my own personal targets that I set to make sure that I am communicating effectively. As a person who has had a decently successful career despite autism spectrum and unmedicated ADHD (I was medicated, but unfortunately each medication I tried had adverse side effects), it has made me much more effective in tracking work and following through, especially on the "boring" stuff that is actually critical to being a dependable team member, and effective partner for the teams I support.Just a couple of examples.

reply

hypfer
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You're putting a lot of trust into the judgement abilities of what is just a next token predictor there.

I can see what the goals are there, and they do make sense I suppose, but I'm not confident that what you're handing off there can be handed off to that degree.But maybe that is not the point and the point instead is to see what the LLM thinks would be correct, and then think about that and collect learnings about the world from it.
It might not be right, but it still tells you how normal people think. So that's useful.Just a very roundabout way to achieve that, but that's fine, I guess.

reply

Zambyte
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Your agents.md is a good place for high level facts, but if you have something that requires a lot of info to explain (ie: if there is a complex build process, testing patterns, things like that), loading up your agents.md for every request may be a bad idea. Offloading that information to a skill ensures it's only included in the context if you're actually using it.

reply

Zambyte
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Something else I want to add on to be more specific is that I use skills to document tasks that my model doesn't know how to do out of the box. For example, there is a jira cli[0] that I use for interfacing with jira. If I just say something like "add an issue for X on jira", the model will have no idea how to interface with jira. I could add that the jira cli is installed on my system, but it's not popular enough for the model I use to just know how to use the CLI, and it will end up spending a lot of tokens guessing how to use it, failing, reading the help output, trying again, etc. Adding a skill for jira lets me capture how to use the cli, and makes prompts like the original usually work first try. If something still requires the model to iterate with the cli, I will ask the model why it failed originally, and ask it to update the skill file accordingly, to avoid the same failures in the future.

[0]https://github.com/ankitpokhrel/jira-cli

reply

sampullman
 
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

How about linking to a separate docs file from the Readme, same as how you'd split separate topics into different files for humans? The context cost is low and as far as I can tell it's pretty much how Claude's "memory" feature works.

reply

matsemann
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That splitting is basically what a skill is, with some instructions as to when to load it. Depending on the harness used it might be quite equivalent, but not sure how easy it follows links in the readme compared to skills (which is just a glorified name of a readme anyways)

reply

sampullman
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Right, it's all just text file management. My point is that if I can add a few lines of description with links in my readme/agents/etc instead of manually including skills in the prompt, without any downside, I'd rather do that.

reply

swingboy
 
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

The content of AGENTS.md is typically included in the system prompt and benefits from prompt caching.

reply

dxjxjdjsssb
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I use skills for offloading work onto subagents. By configuring the skill to use a specific model it gets enforced at the harness instead of depending on the good will of the orchestrating model to actually delegate. This also saves context.

Today Fable had to fetch a zip file from a web page with a eula prompt, then get at a file in a disk image in the zip.This is something that will need to happen a lot as part of this project.I asked Fable for a skill/script combo suitable for Haiku to accomplish the task, and now that task happens at minimal cost during an analysis run.

reply

jeffreygoesto
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Did you consider writing a small Python script for that?

reply

nottorp
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

... or telling the LLM to write a small python script for that and install it as a mcp or something ...

reply

sjanes
 
51 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I made an agent skill for `tsort` and that unlocked a lot of interesting things.

Giving the agent an external tool to consider the sequencing of anything with dependencies led to some creative construction and offloading sequencing not unlike offloading calculation. (I also made a `bc` skill).https://github.com/sj4nes/clanker-toolsis where I've been riffing on this. My plan is to collect not "just skills" so much but "capsules" of reliable knowledge that agents can pull without confabulation. I'm already hitting the organizational stumbles, so this HN thread is right-on-time.

reply

skybrian
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I have a couple of skills with project-specific conventions for how to write a plan and how to write HTML-generating code. But they could probably just as well be .md files in a docs directory, linked to from the AGENTS.md file.

reply

gavmor
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Well, for 
non
-general tasks, of course. For example particular tooling that's required for the environment.

I will often make a skill out of the docs for any of the frameworks or libraries that we're using but with which I'm unfamiliar. When I'm creating that skill, I focus on idiomatic implementation and usage. It's not enough for the code to work—I want it to work "with the grain" and "through the front door", as it were.By default, these models are just all too willing to reinvent the wheel and monkeypatch as they go.

reply

nvch
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

For starters, if you repeat a specific prompt multiple times per day, you may save it as a skill.

reply

LTL_FTC
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Claude will do this for you after a few times. But yes, I have a skill called plan-to-epic which creates a Jira epic and ticket per milestone. It helps my agents persist context and, because I’m terrible at competing with my coworkers for “visibility,” means I can point to all my work if asked.

reply

killingtime74
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not that, is for: 
Ensuring certain vetted implementation method is used. E.g. you always want tests or docs, or always done.

Caching certain scripts so it's not reinvented each time with risk of error/need reviewing.

reply

kkarpkkarp
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> I don't use any skills, what kinds of skills are people finding most useful?

I create/edit/delete at least one skill per day. I can't imagine working effectively without those files.The most common case: if I see something took AI too much time and tokens and it is done, I ask my Cursor immedietly after to save it as skill. So next time I do the same I just refer to skill. I don't need to remember the name of the skill, I just mention something like "do {explaining briefly the task}, you have done something similar in the past and it is saved as skill"

reply

petesergeant
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Gateway drug is “/grilling” by Matt Pocock.

reply

squirrellous
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

One way I use skills, which I don’t see mentioned very often, is as “shortcuts”. Imagine some frequently issued prompt like “fetch origin and rebase this branch onto origin/master and resolve conflicts”. I make that into a little skills file called “rebase” with a one sentence description, and next time just type something like “/reb-tab-enter”.

reply

vzaliva
 
28 minutes ago
 
 | 
prev
 | 
next
 
[–]

I've used this to install some 3rd party skills: 
https://github.com/vercel-labs/skills

It allows to install and update skills.

Caveat: It works for Claude Code and Codex, but does not work for Claude Desktop.

reply

FailMore
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Surprised it has not been mentioned, but I think relying on 
https://github.com/vercel-labs/skills
 is sound. It handles global installs for a wide range of coding agents. If I was working on an internal only skill I'd probably still use the same foundation.

reply

jve
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Last week I had to reuse homemade skills on different project. I very much liked the AI proposed solution and it works quite well: ship as a plugin and add your git repo as a marketplace.

The installation is effortless and I don't have to mess with symlinks as I may be working with same codebase on different platforms which would make things.. different.codex plugin marketplace add "https://path-to-my-git-repo"
 codex plugin add agent-tools@mycompany

 claude plugin marketplace add "https://path-to-my-git-repo"
 claude plugin install agent-tools@mycompanyLet the AI generate .json files for marketplace.Haven't got to these bits yet, but I'm sure they will work as easy as install does.claude plugin marketplace update mycompany
 claude plugin update agent-tools@mycompany

reply

sotilrac
 
42 minutes ago
 
 | 
prev
 | 
next
 
[–]

I use a handful of skills I keep in a repo (to track updates) with an install script. Mainly is to replicate them across my various dev computers, and to share them with the team.

https://asmat.ca/blog/mad-skills/

reply

chandureddyvari
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I commit them to git(so complete team leverages them)., each repo has kind of different skills and the skills are the ones which I update at least twice a week. I’ve skills on how to add instrumentation , debug, code, code review, tech design review etc. I found most of the skills I find on skills.sh are not very useful for me., but I browse occasionally to get some inspiration. One more paradigm I’m seeing good results on adding new skills is ‘how to do X’, for instance ‘how to add logs’., “how to review code” etc., if i’m not able to frame it that way I don’t think it’s a good use case for me to add that skill to the llm arsenal.

Another thing i discovered is less is more (in case of skills as well)., don’t add lots of skills., keep them very handful - I’ve got 9 skills so far (many people have 100s installed from marketplaces and plugins)

reply

floriangoebel
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Thats exactly how I use skills as well and I got great results with it.
I work in a proprietary codebase with a lot of niche or custom tooling, weird technical details and historical quirks. 
What skills do for me, is essentially skip the "learning" phase of an agent working in the codebase. 
With a fitting skill the agent does not need to read the tooling docs, look at existing repos and learn the coding style, but it can get to work immediately.

This is probably less relevant for code that exists a ton in the LLM training data already as an llm is probably competent to some degree in that anyway.A big caveat here is though that now you need to treat your skills repo very carefully as mistakes in there can easily spread to all of the new code you write using a coding agent.

reply

socketcluster
 
49 minutes ago
 
 | 
prev
 | 
next
 
[–]

I make skills to allow AI to integrate with my platform; it's documentation with cURL commands. It can interact with every aspect of my platform via HTTP and access its full capabilities. I can tweak its token permissions as I like and revoke access if necessary.

reply

rgbrgb
 
25 minutes ago
 
 | 
prev
 | 
next
 
[–]

tbh I use 1 custom skill (workflow for completing a github issue and opening dev server/PR) and have it checked-in to my main project repo.

For me, it's like a dev script basically and gets that level of care. I don't need an eval... I'm the only user and I use it like 5 times a day.

reply

SillyUsername
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

5 Stages using local GIT (no remote, don't need it) to prevent preloading in the prompt:

1. A single Skill finder skill, loaded in the prompt, prevents having to import all the summaries in the prompt the harness would add. Uses git's own search.2. Private repo, per agent, contains main (production) and draft-<name of skill> branches.3. Shared repo, like 2, but general access for all group agents.4. Fallback mode, search the harness for skills using the harness mechanism when a relevant skill cannot be found.5. Skill audit cron. Identify junk skills / drafts that have never changed / not in any recent sessions history, and categorise monthly for me to decide.This means it's compatible with existing skill folders, removal of git and the finder skill is non destructive and critically debloats the prompt of skills that aren't used and lazy loads them when needed.

reply

bhkdotdev
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

> "make sure they actually work?"

I've been working on a tool (https://dynobox.xyz) that acts as a deterministic integration test / behavioral test layer for some of the skills i've been working on / sharing.It feels like a full eval suite is a bit heavy handed and really all I care about is if certain files are touched / left alone or if my skill is actually read. The tooling has much more functionality built in if you want to check it out!For skill files / prompts I share I make sure that I use the cross harness functionality since I use codex but a bunch of my coworkers use claude (and then one using antigravity...)

reply

wseqyrku
 
19 minutes ago
 
 | 
prev
 | 
next
 
[–]

I usually use this technology called Shift+Delete

reply

ssivark
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

To the extent that skills are 
contextual guidance
 (for this author, this project, etc) and not just (raw) 
capabilities
 they are unlikely to be eaten by models.

I maintain all my skill files in a central location (like dotfile management) and have guix home sync it to the skill folders of various harnesses that I'm playing with (codex, pi, antigravity, Claude Code, Deepseek harness, etc). They're set up to be bidirectional links rather than read-only like the default configuration, so I can keep editing them / adding to the corpus from any harness.This works well for skills since all harnesses expect the same format, but is more annoying for other features.EDIT: This is actually an example of a potentially useful skill. You might choose to manage your skills slightly differently. All you need to do is write a skill-management skill for your agents to be able to wire things up correctly / access them for edits.Some other nifty skills/plugins in my experience: render latex equations, cetz diagrams inline, jujutsu, guix, code reviewer, writing feedback.

reply

ssivark
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Don't know why the below comment by killix got flagged; it's a legitimate point.

In the current version of my setup, I've decided to accept that tradeoff.But it would also be interesting to check whether agent behavior can be controlled well enough by a skill-management skill telling them to synchronously commit any changes with their signature; that would get the best of both worlds.

reply

mceachen
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Have your agent make a plugin marketplace -- mine is here (feel free to crib): 
https://github.com/photostructure/coding-skills

Be sure to increment unofficial plugin versions when you make edits: codex's auto-update works reasonably well, claude not so much, but when asked, both can fix their own config.And like others have said, imho the skills that are incanted as macros are much more reliably useful. I use my technical project plan skill suite in 90% of my sessions via direct reference, and the stage -> cross-model second-opinion review is how I land all my commits.

reply

cowanon77
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Personally I have found "meta-prompting" to be much more useful than any pre-canned set of skills. Simply ask the AI (inside of a workspace already set up):

Create a standalone prompt to <xyz>The latest AIs will print out a long prompt with all of the assumptions, tools, and general files it plans to use. Review that, and then run the whole prompt in a new context.

reply

cainxinth
 
15 minutes ago
 
 | 
prev
 | 
next
 
[–]

I find the whole Skills.md idea a little silly. We have a technology that struggles to stay within rails due to its inherent makeup. And you think you can fix that by just telling it to?

It makes as much sense as the so-called “humanizer” tools that purport to make LLMs stop using their well-known verbal tells.All you are doing is saying: “Hey you know that thing you can’t stop doing? Can you stop doing that?” The machine will say “Absolutely!” but eventually start doing it again.

reply

appplication
 
13 minutes ago
 
 | 
parent
 | 
next
 
[–]

You’re not wrong, but I don’t see a lot of alternatives. So we just don’t try to fix it? At least skills give us a landing pad for “here’s how to attempt to do things consistently in a way I generally approve of”

reply

jdxcode
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

for skills related to specific cli tools, i just wrote a standard for this! it's obviously not widely used yet, but since mise will support installing the skills alongside the tool, i suspect it will have decent adoption

i used to be a bit bearish on skills—thinking that llms should just use --help, but i've come around on that. i think skills are a great way to describe higher level workflows that use multiple commands.https://jdx.dev/posts/2026-09-05-introducing-packslip/

reply

qznc
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

We have an ongoing discussion and some fans of 
https://microsoft.github.io/apm/

Because it's from Microsoft and sounds sufficiently enterprisey probably.

reply

woadwarrior01
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

You might want to look at this CLI that Tencent released recently.

https://github.com/Tencent/teamai-cli

reply

mstr32
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

The main problem I encountered around this is that skills need to be edited across projects and across team members in a controlled way. Git is of course required for this but is not enough so I built a tool to do just that:

https://github.com/genged/capshelfUsing capshelf I manage my skills across projects.
When I start a new project I can just:$ capshelf add security-reviewFrom the skill repo.And if I create a new skill I can promote it to the repo so everyone can install it:$ capshelf promote security-reviewIt pins the skill content hash so there are no unexpected edits that can break your flow. It also supports MCP configs and agent configs.

reply

meerita
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Here's how I do it:

- Explanation:https://www.minid.net/2026/7/14/how-to-automatise-with-ai- Git source:https://github.com/meerita/monorepo-nextjs-golang-rust-pytho...

reply

fallinditch
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I read somewhere that Boris (created Claude Code) recommends deleting skills, and hooks every so often and then observe how the LLM performs without them.

Maybe better to periodically prune: tweak some skills, shorten some, delete some.

reply

synergy20
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

observing changes is slow and very subjective.
i ask ai itself to update skill once a while

reply

skeledrew
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I mostly prompt my own skills, and add a self-improvement directive (to those I think can use it). Usually if a skill isn't working (well) there will be extra tool calls. Actually that's usually the trigger to create a skill in the first place: multiple tool calls to do a repetitive task, where those tool calls can be reduced. But from comments on most AI-related posts, people are hardly-if-ever reading the agent transcripts (and the self improvement directive doesn't always get triggered) so their skills never improve.

reply

nickreese
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I think people undervalue skills on the cross repo boundaries and how systems interact with other systems.

For instance… how to deploy a service or new service’a docker container. Get secrets in value blind, manage secrets value blind. Those sorts of things have been wildly valuable. Also due to the nature of skills and how they are pulled in by your harness they can really prime the context in a way that is really useful to agent autonomy if that is your thing.

reply

jameshiew
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I manage them as part of my dotfiles using chezmoi. A `.agents/skills/` directory + a symlink to there from `.claude/skills/`.

> Do you keep improving them over time?In my global AGENTS.md I have a note to agents to explain any frustrations they had doing a task, and to suggest any skill/tool/AGENTS.md improvements. I am trying to keep AGENTS.md files small but still finding the balance.

reply

pglevy
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Mostly use homegrown skills. For shared skillset at work, it's a standalone repo with a script for everyone to install the full set. For a personal collection I also use a script to sync a few upstream ones to keep everything in one place.

For evals I use the method outlined in the `skill-creator` skill from Anthropic.In the skills, I try to use scripts, along with templates and json worksheets, as much as possible to scaffold and validate the work to make things more consistent and reliable.

reply

bredren
 
24 minutes ago
 
 | 
prev
 | 
next
 
[–]

I use skills all day, every day. One of my greatest annoyances right now is having to switch between `/` and `$` in moving between CC and codex. At one point I attempted to hack the CC TUI to accept $ but failed, I may yet return to that.

All of my skills are custom to my workflows except Contextify (more on that at the end) This extends to how I distribute them across multiple development machines.They live in my `cli-ai-setup` repo alongside agent settings, git worktree tooling, iTerm workspace restoration (important, machines have to restart and crash sometimes), code review scripts, and machine setup guides. I use git to carry changes between machines and a setup script to symlink the skills into a shared directory that Claude Code and Codex both use.I have a `skills-and-settings` skill specifically for deciding where new skills belong and how to make them available (project, global, application). I also have a custom `skill-create` skill that turns sessios into new skills or updates existing ones.Importantly, I also have entire custom applications I have not yet made open source that my cli-ai-stack relies on. I do expect to distribute these so they live in their own repo and are symlinked or installed in as appropriate.For maintenance, I've largely handled this manually and organically. When a skill is not performing, I'll use the context of the situation as the ~1 shot or pull in more examples for the ai:This skill seems to not be performing as expected on [something]. 
 
 This has happened a couple of times now use /total-recall to find similar recent situations for example [something I remember]"

 Recommend updates to the skill and upon approval commit and push them...etc.My other machines watch this repo and the symlink structure means that the updates are carried into live cli-ai sessions almost immediately.This past week I was exploring the automatic skill improvement behavior described in the Anthropic blog guest post with their partner org. I'd previously build a "dreaming" skill that works okay and think there may be some value yet to plumb there.For skill creation, I have a skill that reads the official skill docs for both Claude Code and Codex. This way the skills are built to handle both platforms particularities. I automatically pull those docs into local Markdown daily, so it has a regularly refreshed reference for what each tool supports.As mentioned above, I have built Contextify (https://contextify.sh) which provides a sql database of all of my Claude Code an Codex session transcripts across all of my development machines. The skill for this (/total-recall) is the most important skill I have and I use it constantly.

reply

invaliduser
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I basically create a skill when I'm tired of always writing the same prompts, and then I adapt it over time.

I have like 3 skills, and so far so good, most of my recent changes have been asking Claude to please stop using metaphors and creative figures of speech that make the documents so much harder to read and understand (maybe it's only annoying to non-native speakers, I don't know)

reply

bjconlan
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I have an old colleague who I've been leaning on for ai things (they're more on the pulse than I) who uses cue (cuelang.org) for distributing and formalizing a set of skills/prompts.

It's the best thing I've come across (that I don't need to mange myself)https://github.com/p3bot/startThe tool itself does more than just manage skills/prompts but I found that part of it particularly good (well new to me; not familiar with cue but the idea seems like a good fit)

reply

mark_l_watson
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I need to manage skill files across 2 Macs and 1 VPS, and also across fast inferencing APIs vs. very slow local models.

The first dimension is easy: I simply keep copies of debugged skill files in iCloud and copy them where I need them.The second dimension is where I spend my time: I use short skill files for fast inference APIs and tiny skill files when I am running slow local models, and I simply spend a lot of time writing and tuning tiny skills files.Of course, with increasingly better models, skill files become less relevant, but not totally irrelevant.

reply

imadtaieber
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

I find myself spending a lot of time updating skills, which is not wasted time, since they are at the system design level work. It's how I automate myself ;)

reply

theletterf
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

We keep the skills in a repo, where an agentic workflow runs biweekly to check if their content drifted compared to the docs and opens PRs if they did. The repo is also a Claude plugin. The biggest problem is keeping skills up to date across users, so I developed a small Go binary that takes care of that across harnesses.

reply

mstr32
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

That's very cool. How does the binary keep skills updated across users?

reply

theletterf
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It clones the skills repo if not present and relies on the git last commit as the "version".

reply

tesnorindian
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I use SKILLS.md to define workflows rather than having instructions in them. Like, delete the foreign keys in the database before loading the table using AWS DMS for CDC. This is required because LLM may not be aware of why we are deleting the foreign keys in the DB in the first place. The SKILLS.md helps the LLM to identify the tables for which foreign keys needs to be deleted before they are loaded by DMS for CDC.

reply

Ro_K
 
42 minutes ago
 
 | 
parent
 | 
next
 
[–]

I like this usecase, I could have used it myself. But I actually moved out of DMS to OLake, its open source and gives ways to operate it via both UI and CLI.
But thanks for sharing this!

reply

sinuhe69
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

When I work on a new problem and the agent struggles with it, I will ask the agent to distill the knowledge and experiences it gained during the session into a skill file. Then I review and publish it depends on the assistant system. I find this is an effective way for the agents to learn new skills, both from its own discoveries but also from my steering and the mistakes it made.

If you work in a niche or on special problems, this template could be useful.

reply

ekns
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I haven't used skills files at all. I think my codebase scaffolding and AGENTS.md just kind of does everything I need.

E.g.https://github.com/eliask/lawvm/blob/master/AGENTS.mdEDIT: Ah, but what I do instead is I constantly refer to my various public essays. I think it's very useful to have externalized thinking like that available for use with LLM contexts.

reply

edf13
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

One thing to consider when you do look at how you manage your installed skills - is the security side of them.

You also need to manage the authority of each skill too. Signed skills is a step in the right direction, but it only proves provenance and doesn't prove behavior.(Related:https://news.ycombinator.com/item?id=49597166)

reply

sformisano
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

SkillCatalog (
https://skillcatalog.dev/
) - stored in git, managed via desktop app (macos) and and CLI

full disclosure: I'm the author

reply

glub
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I only use skills that are docs of software. Anything else is pure garbage.

They get pinned with nix together with the software that they come from.It's just two 3rd party skills now:playwright-cli and herdr.All the rest are skills for the software itself, so they live in the same repo and get updated the same way docs get updated.

reply

_pdp_
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

GitHub. Then you symlink them into the relevant folders. You can write a skill to manage them for you across all harnesses as well.

reply

imadtaieber
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

going to do that, very helpful!

reply

toffelx
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I have created a little system for this, placed directly in the ~.<youragent>/skills folder.

I have a configuration file of marketplaces and other skills to fetch, it can look like. I have my own marketplaces as well, including ones from my company.
I use vercel's tool for managing skills with npx, but to easily handle specifically _which_ skills to fetch, the config file is set up as follows:SOURCES = {
 'some-marketplace-name': [
 'some-skill',
 'another-skill',
 'yet-another',
 ],
 'https://designsystem.yourcompany.com': [], (empty list: fetch all skills)
 }from there I simply run "skills.py" (a single helper) to clean/fetch updated versions of the skills.

reply

Kwpolska
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Skills that are so generic that you can find them on the internet, and which you think can be replaced by model improvements, are useless, possibly even harmful, considering how much the models get clingy to the context. Useful skills describe workflows specific to your project, and they can live in the project repo for everyone to use and improve.

reply

matheusmoreira
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I create and refine my own skills and commit them to my dotfiles repository.

reply

repeekad
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Lookup the Claude managed agents architecture for skills, they have a kind of progressive exposure where skills have a title that triggers the skill, an index file that is loaded when triggered, and additional files and scripts that are available once triggered but not loaded by default.

reply

yatsyk
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Skills live in two source-of-truth git repos (private and public). Agents edit skills by my request, and syncs to all coding agents ~/.claude/skills/, ~/.codex/skills, ~/.pi/agent/skills, ~/.config/opencode/skills etc. with agent written sync-agent-skill script. script ensures that no local changes was made in-place.

reply

KerrickStaley
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Codex and Claude Code both respect ~/.agents/skills; you don't need to have ~/.codex/skills and ~/.claude/skills .

reply

r0b05
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why do you use so many different agents if I may ask?

reply

yatsyk
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I mainly use Claude Code, but I had an idea to build an orchestrator for coding agents, so I experimented with several

reply

osr00
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

> How do you find skills

I try to keep my collection of community skills short, usually a few established names (mattpocock, mcollina, trailsofbit). And then I check new releases (or when mattpocock published a youtube video for instance :D)> keep them organizedFor skills I wrote myself, I have my own private github repo. I use skills like /commands most of the time, so I can tell if they work straight away.For community skills, a package manager really helps. vercel-labs/skills and withastro/rosie are good options. I also built one myself:https://github.com/osrim/ski. It has some cool features like an update command and a security scan.

reply

hellectronic
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I am testing out Skillshare 
https://skillshare.runkids.cc
 and I am using skills.sh to find skills.

You can have your own skill repository with Skillshare and sync across agents (symlinks or copys).

reply

shermantanktop
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I don’t seem much point to intentionally curating a set of skills, and specifically invoking them by name, only to watch the ai skip them all and do better by just reading code and internal/external websites.

reply

songhonglei1985
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

reduce and simplifies your skills periodically . And use workflow to separate skills ,not by functionality . The workflow would be simplified but will always be useful as long as business runs. Such as the software could be build by C/C++/Java/Go/Python but the workflow based on software keeps live.

reply

hypercube33
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm on mobile but the first skill I made was a skill improvement skill. This is basically stating that if the AI struggles in another skill but finds a way that the skill it used needs reworking and it needs to do so.

There is a rule to always use this skill and then track notes in a version file. Then back it up in a share folder or external drive.Skills have made my tools immensely better, cheaper to use and faster. I've also added to it that it should write scripts it can just use in the future to do tasks like query information it needs to answer questions.I wish there was a better way to share these over a team but I haven't taken that time yet.

reply

starefossen
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

For the my branch of the Norwegian Government we have a public skill registry and a tool to sync them locally according to what «profile» you select, 
https://ki-utvikling.nav.no/verktoy

Source at navikt/copilot

reply

winternewt
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I keep my skills in a Home Manager repo and install them into my .claude / .codex / whathaveyou directory through the home manager config. I'll know if they don't work because they are specific instructions on how to git commit, how to merge code, how to author text (without the typical AI tells), or API usage documentation for specific libraries, etc. If they didn't work the agent would do things incorrectly and I'd notice.

And sometimes it doesn't follow the instructions well. I have a skill for that too: it tells the agent, given what it knows about attention and LLM:s in general, to evaluate the instructions and the mistake the LLM made, try to diagnose why it didn't follow the instructions as expected, and come up with an improvement of the skill based on that diagnosis.

reply

brokegrammer
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I don't use skills unless I have something specific to tell the agent. For example, if I want the agent to use Tailwind V3 instead of V4, I'll have a skill for that. Or, if I want the agent to always use the repository pattern for database access, I'll create a skill for that.

I don't need to manage skills files because I have so few of them and they're only a couple lines long.

reply

joshuanapoli
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

We have some company-managed skills, that help coding agents find the relationships between our repos, and our conventions, architecture, and other high-level decisions. These are supposed to be portable between agents, and so distributing them is currently awkward.

We have a bootstrap script to deploy company-managed skills to each developer's "personal" skills. Hooks for codex and claude code try to refresh the skills on each startup.

reply

kaizenb
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I manage them in a GH repo in synch with local, with regular checks and updates.

https://github.com/boraoztunc/skills

reply

sznio
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I don't use them.

Everything is organised into repos, i select the directories with the context the agent needs for the task. If I want it to adjust something in my homelab, I drop it into the homelab repo. Stuff agents need to do commonly has shell scripts to speed it up.I do however have some system prompts. I pick the prompt based on the goal, whether I want to implement something, or just web search, or just need a short one-off command to be done.

reply

backtr4ck
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I run AI on my server. All skills and relevant info is saved to a Wiki. Agent only has an instruction to check the wiki (MCP) at the beginning and get the necessary context.

reply

srijanshukla18
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I've got a skill repository on github, and I got a hermes automation to sync skills repo - this hermes automation is on every device.
Any skills I make on the fly - my global AGENTS.md has instructions to update the skills repo path and place them appropriately in there.

reply

ramon156
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Disclaimer: I hand curate them in the end

I keep most of my sessions in Zed (you can import them there anyway). After some big feature I let a frontier agent go over these sessions and suggest improvements. Typically I use gemini for this because it's really good at pruning text. Claude/GPT really wants to append more text for some reason.I end up with smaller skills but more "actioned" skills. They kind of force the agent to do things the way that works well.

reply

bastawhiz
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Treat skills as runbooks, not as a way to turn your agent into an expert.

reply

anygivnthursday
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

If I have a session with something that I expect to do it again, I ask Claude to make a skill out of it and store at user level somewhere at ~./claude/skills I think, so next time I can do just "/xyreport from-to" for example and dont have worry about leaving out things from the prompt or to rediscover some gotchas the agent ran into.

reply

vkvkakal
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I recently completely overhauled repo’s skill setup.

I tried to control the execution of tasks performed by each project using claude.md within the project, but claude.md is only read at the beginning of each session, so it felt like the instructions weren’t being properly reflected.So I revised the strategy to manage frequently used features in skill units. In doing so, instead of organizing skills by project, it was structured to be integrated into the general skills of the individual repo.When skills are spread out across multiple projects and the number increases, it becomes impossible to keep track of which skills are available, so they end up not being used.I also think that eventually, once Claude(model) advances, it will be able to replace most of the skills, so I believe registering and managing countless skills actually degrades performance.

reply

Sherveen
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I have a repo/project called Loadouts & Summons. It has a primary skill, `capsule`.

All skills, MCPs, CLIs, etc. live inside of it. I have it symlinked to all my dev machines so that it doesn't have to be an MCP.`capsule` is then progressive to dozens of skills/tools thru `capsule` -- ex. `$capsule plannotator [args]`.In some harnesses, I make it human-invoke only, and call it directly. In others, I let the model invoke it, and it has a top-level description that hints at what's inside.Maximal context/session start controlandcapability extension.

reply

maxim-fin
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Nowadays I often create skills myself (or with the aid of coding assisants) for any repeating tasks. For example, I use my own skill to make Claude CLI send the worktree to codex cli for the review, then read the verdict and make changes

reply

serf
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

>I believe skills will eventually be eating by model capabilities

a model capability is never going to fill in an unknowable blank that a custom skill (or whatever equivalent your paradigm supports) can.a model might have the cleverness to whoami and look through the .ssh folder for keys and evidence of past connections when asked to connect to bob, but a skills file can just easily say "We connect to bob using key Z and user X." so that the operation gets done without all this nonsense needless inference as far into the future as the information is valid for.a concise information dense skill is going to always dominate on tokens-burnt for any given task that requires insider knowledge. it simply gets rid of the entire investigative phase of work.

reply

TomEleff
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Agree here. My philosophy is the "general-purpose" coding agent will keep getting better and better, making skills less and less useful. And it will probably get better at a pace far greater than the customization folks can build around them via skills.

This of course is from my own experience writing code, where agents are already good at software engineering conventions. This probably doesn't hold as well for other tasks, say writing marketing copy with a unique voiceFor now, I keep skills pretty minimal - single sentence prompts I send all the time, like "Remove all the slam poetry from the docs in this repo."I also tend to share often. All skills go into a repo my team can access. No pressure, use them, riff on them, add your own - sharing and engaging on how we do the work is more important than making everyone do the work the same way to me.

reply

imadtaieber
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What I meant by skills getting eating by models are the "general use" skills, like design critique, code review...ect

But, for custom use skills, ofc no model will be able to replace them and it's not efficient to try to do that as well. For this type of skills I create and maintain them by myself, my question was about "general use" skills, they are everywhere on the internet, how do you manage them?

reply

SyneRyder
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Do you find any of the general use skills useful? I'm not sure I've ever used any of them, and when I've looked at them it's been some YouTuber trying to make money. That, and their Substack.

I know everyone's down on MCP, but custom-built client side MCP tools are what I find useful instead. But that's me.

reply

thom
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

How do you disseminate that information to humans?

reply

vjvjvjvjghv
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

“ determinist harness around the agent ”

Can you explain what this means?

reply

chickensong
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you can express something deterministically with code, it's better to do that rather than have an agent do it, because it's faster, cheaper, and deterministic. E.g. you regularly copy file A to file B. You can ask the agent to do it, or you can write a script and have the agent call the script via skill. That's the beginning of a harness.

Eventually you arrive at building custom software that does a lot in the traditional way, but delegates certain tasks to the model where it makes sense or it's non-trivial/impossible to express via code.

reply

vjvjvjvjghv
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That makes sense. Sounds similar to what I am usually doing. I let AI write a python script or similar, review it and then use the python script. I don't think I would let AI do anything important directly.

reply

patleeman
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I use an agent plugin spec repo. Codex is already compatible with it and it supports skills + MCP definitions.

https://agent-plugins.org/

reply

slartibardfast0
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

i use an agentic host folder, full methodology here: github.com/connollydavid/host

i then A/B test skills for terseness with weco’s auto-research within this using a much weaker model e.g. Qwen 3.5 4B

reply

itsTyrion
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

wdym "your skills files"

reply

ziofill
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve tried to keep up with “best practices” around AI use, but things are improving so quickly that I’ve largely given up. The vanilla agents are just fine for my needs as they come.

reply

BOOSTERHIDROGEN
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Can you elaborate more how do you setup vanilla agents ? Which agents you use and which use case that it’s greatly show benefit for you. Thanks

reply

rcarmo
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

My agents use 
https://rcarmo.github.io/projects/memento/
 to manage shared skills and propose changes. But I also have template projects with skills baked in for some scenarios.

reply

vira28
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Instead of managing skills as files, I have been using a simple utility which helps me create, update/attach skills and finally search it across sessions 
https://github.com/viggy28/recall/

reply

sornaensis
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I don't like skills. It's a really annoying form of technical debt, especially when people try to fill up company repos with random skills they think are so cool. Same goes for polluting a repo with custom instructions.

I only want the model to have the tools it needs to get the job I ask of it done.

reply

asedali
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Why do you think like that?
"I believe skills will eventually be eating by model capabilities, but until then I'm just looking for a better way to manage things."

reply

Udo
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

A few simple rules worked for me:

- start with zero skills

 - add a skill if you encounter behavior that you want to ward against or if 
 you want to associate a meaningful phrase with a certain method of doing things 

 - NEVER copy a skill from someone, do not clone skills repos, do not let LLMs
 write their own skills

 - occasionally revise or delete a skill, less is more

reply

pletnes
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I have my skills in my dotfiles repo, then symlink them to my home directory and/or projects where I want to use them. Project specific ones go into the project.

reply

matsemann
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Skills is just a tech bro word for a simple markdown file with instructions.

No need to over complicate it. Write down things you feel like re-using. Like how to specifically implement something in your system ("when adding a new API endpoint we need to do x y and z", or "when making a github PR we tag Æ and Å") so you don't have to repeat it. And I mostly add it in cases where it didn't infer it itself. So very reactive, not proactive.Most public skills are useless and over complicated. Lots of people are spending too much time on their harness, than actually making stuff.Edit: but do get inspired by public ones. For instance a "grill me" skill can ve be useful, but I find the public one very mumbo-jumbo. But the idea of forcing the agent to ask clarifying questions is good.

reply

Achshar
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

I believe skills are much more than a simple markdown file with instructions. They are a very powerful script engine. How I organize it is that of course there's a markdown with instructions but I split the work in a hybrid of script + instructions. So all the work that can be deterministic is a python script api surface and all the logical or thinking work is in instructions. and agent is also instructed on how to use the api of the python helper functions. This makes it almost like a normal script but the runtime is a harness and the business logic can be any combination of code + human-level intelligence.

So I like to do all the edge case handling and validation etc via a helper function, and the agent is simply instructed to call the function to do something. It isextremelypowerful and a completely different way of automating things. I am constantly forced to re-think how computers are supposed to work and its limitations.

reply

hypfer
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

My genuine question is:

Are there any "skills" at all that have proven to be useful?
And if so, what's the context?Because, for me anyway, LLMs usually do one thing, and that then produces a durable artifact. So the prompt that got me there by that point expired and is not really needed anymore.I also occasionally have recurring tasks (rarely though), but there, the prompt to do stuff is embedded in code that orchestrates the doing, so I have no use-case for that either.___For the "add this endpoint" example you've described, I just throw commit IDs at the clanker and say "go do that again". That works, and doesn't decouple knowledge from code.

reply

torunar
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I usually rm -rf them.

reply

soapdog
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

by not having them at all.

reply

pdantix
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

the only ones {i use,claude decides to use} regularly come with claude code plugins so they automatically update. i just define the marketplaces and plugins in my .claude/settings.json for the project.

reply

iamflimflam1
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

The internet has broken me. Whenever I see a question like this i now automatically expect it to be some marketing attempt. There will be a product/service/blog post somewhere in the comments.

reply

sdevonoes
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Never understood the “skills” part tbh. Thse models are being trained in trillions of texts. Adding something small and particular about my codebase doesn’t really move the needle

reply

dude250711
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

I think it's developers coping with not coding anymore.

There is this urge to create a non-ephemeral library of at leastsomething.

reply

lazy_afternoons
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I have a separate repo which has to be pulled locally and the skills and agents are sym linked to projects.

reply

daitangio
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Openspec has a subcommand (init) to manage them: clever because they provide also an update path.

reply

someguynamedq
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Skills are workflow caches

reply

RALaBarge
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Any skills, I just add into the tool itself. I then have the py tools in their PWD, don’t bother with mcp.

reply

inopinatus
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

5% git

95% rm

reply

estetlinus
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I am yet to find a skill useful. It’s usually just vibecoded slop-bloat for a one-off somebody thought they document in a markdown file.

reply

0xbadcafebee
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Don't find them. Ask the AI to do something. When it does it correctly, ask it to make a skill for it. Clear the session, try to use the skill, fix any problems found, modify your repo and harness if necessary. Repeat until skill works 0-shot. Improve with the same process.

This largely works with a specific model, specific harness, specific prompt, specific context. You may need to modify your agent harness to manage skills depending on runtime parameters. Pi is a great general purpose agent for the these modifications.If you do find other skills and want to use them, put them through the loop above. But keep in mind that since they were created in their own circumstances, they may not work in yours.Also separate rules from skills. Rules tell AI when to do things, skills tell AI how to do things. Tool call/MCP limitations, agent configurations, and harness extensions, can help it stay on track.

reply

imadtaieber
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Im talking about skills like design critique, landing page creation....ect

reply

shelune
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Not really related but I wonder how people benchmark the effectiveness of skills/agents?

I'm seeing the agent working quite fine with just direct prompting and the agent doing things by itself rather than using skills. Is it better for certain task size?

reply

politician
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I wrote a small command-line tool that installs skill packs into agent-specific project folders. It works pretty much like `brew` (or any package manager, really). The skills are compiled into the binary so that I don't have to worry about where they're located and can quickly move the skills between machines by copying the tool.

Making sure they actually work? Trial and error, mostly. I know some folks have tried auto-researcher approaches, but I haven't found that to be the best use of time in my work.

reply

moomoo11
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

i have a docs/

it has all the skills/docs my particular application needsi treat it as ADRs as it helps the AI understand the parts of the system it is working on

reply

dakolli
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

With a custom skills workspace in mininote

https://mininote.ink/docs/mcp-docsAgent can use mcp to update its own skills, or I can copy template skills into local dorectories via the api. Very useful, like notion on steroids but is completely free.

reply

dyauspitr
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

It’s all nonsense. Just ask it for what you want with natural language. Why would you want to reintroduce all the random magic incantations we’ve had in tech for decades.

reply

dankobgd
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

how did stupid markdown file become a thing, this industry really went to shit.

reply

adastra22
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Skills are no longer useful.

reply

prettyblocks
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

I find them very useful.

reply

adastra22
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have been finding them decreasing in the effectiveness with each model release. We got rid of skills and built a determinist harness around the agent instead.

reply

mercurialsolo
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

One of the engineers I know is building this product called SkillEd for just this. Lemme know if you need an invite

reply

jiaosdjf
 
7 hours ago
 
 | 
prev
 
[–]

WTF is a "skill"? I really think people are getting ahead of themselves here.

You wrote some bullet points so your agent harness doesn't keep making builds in the wrong environment? You have a very specific debugging setup? Your agent doesn't understand when to rebase?README is where you should be writing anything specific to your project, and if you're worried about context size then your README is too long, it should be just enough information for any competent dev or agent to get the gist of how you do things around here and where to look for deeper answers.If your particular harness / orchestrator is just not pushing back enough or can't seem to solve certain problems then thats a tool issue, either edit the tool system prompts or move to better tools or models.Calling this 'skills' is disingenuous, this word was chosen by marketers and implies some kind of deeper learning. I'm not saying there's no value in tuning prompts, but your 'skills' should be managed in only 2 ways: 1. It's specific to your project, it's a README, or 2. It's specific to your tooling, it's part of config, system prompts etc.

reply

invaliduser
 
5 hours ago
 
 | 
parent
 
[–]

I mainly use them as macros. Not even an advanced and smart macro system, just plain basic macros to avoid copy-pasting recurrent prompts. Is there more to them?

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