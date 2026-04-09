---
title: Claude Code weekly rate limits | Hacker News
url: https://news.ycombinator.com/item?id=44713757
site_name: hackernews
fetched_at: '2025-07-29T16:07:48.003573'
original_url: https://news.ycombinator.com/item?id=44713757
author: thebestmoshe
date: '2025-07-29'
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
Claude Code weekly rate limits
449 points
 by
thebestmoshe

11 hours ago

 |
hide
 |
past
 |
favorite
 |
533 comments
Hi there,

Next month, we're introducing new weekly rate limits for Claude subscribers, affecting less than 5% of users based on current usage patterns.Claude Code, especially as part of our subscription bundle, has seen unprecedented growth. At the same time, we’ve identified policy violations like account sharing and reselling access—and advanced usage patterns like running Claude 24/7 in the background—that are impacting system capacity for all. Our new rate limits address these issues and provide a more equitable experience for all users.What’s changing:
Starting August 28, we're introducing weekly usage limits alongside our existing 5-hour limits:
Current: Usage limit that resets every 5 hours (no change)
New: Overall weekly limit that resets every 7 days
New: Claude Opus 4 weekly limit that resets every 7 days
As we learn more about how developers use Claude Code, we may adjust usage limits to better serve our community.
What this means for you:
Most users won't notice any difference. The weekly limits are designed to support typical daily use across your projects.
Most Max 5x users can expect 140-280 hours of Sonnet 4 and 15-35 hours of Opus 4 within their weekly rate limits. Heavy Opus users with large codebases or those running multiple Claude Code instances in parallel will hit their limits sooner.
You can manage or cancel your subscription anytime in Settings.
We take these decisions seriously. We're committed to supporting long-running use cases through other options in the future, but until then, weekly limits will help us maintain reliable service for everyone.We also recognize that during this same period, users have encountered several reliability and performance issues. We've been working to fix these as quickly as possible, and will continue addressing any remaining issues over the coming days and weeks.–The Anthropic Team

Wowfunhappy

10 hours ago

 |
next

[–]

I'm probably not going to hit the weekly limit, but it makes me nervous that the limit is weekly as opposed to every 36 hours or something. If I
do
 hit the limit, that's it for the
entire week
—a long time to be without a tool I've grown accustomed to!

I feel like someone is going to reply that I'm too reliant on Claude or something. Maybe that's true, but I'd feel the same about the prospect of loosing ripgrep for a week, or whatever. Loosing it for a couple of days is more palatable.Also, I find it notable they said this will affect "less than 5% of users". I'm used to these types of announcements claiming they'll affect less than 1%. Anthropic is saying that one out of every 20 users will hit the new limit.

reply

el_benhameen

10 hours ago

 |
parent
 |
next

[–]

This is how I feel about the 100 msg/wk limit on o3 for the ChatGPT plus plan. There’s no way to see how much I’ve used, and it’s an important enough resource that my lizard brain wants to hoard it. The result is that I way underutilize my plan and go for one of the o4-mini models instead. I would much prefer a lower daily limit, but maybe the underutilization is the point of the weekly limit.

*edited to change “pro” to “plus”

reply

landl0rd

8 hours ago

 |
root
 |
parent
 |
next

[–]

You can tell how it’s intentional with both OpenAI and Anthropic by how they’re intentionally made opaque. I cant see a nice little bar with how much I’ve used versus have left on the given rate limits so it’s pressuring users to hoard. Because it prevents them from budgeting it out and saying “okay I’ve used 1/3 of my quota and it’s Wednesday, I can use more faster.”

reply

xpe

7 hours ago

 |
root
 |
parent
 |
next

[–]

> pressures users to hoard

As a pedantic note, I would say 'ration'. Things you hoard don't magically go away after some period of time.

reply

zamadatix

3 hours ago

 |
root
 |
parent
 |
next

[–]

FWIW neither hoard nor ration imply anything about permanence of the thing to me. Whether you were rationed bread or you hoarded bread, the bread isn't going to be usable forever. At the same time whether you were rationed sugar or hoarded sugar, the sugar isn't going to expire (with good storage).

Rationed/hoarded do imply, to me, something different about how the quantity came to be though. Rationed being given or setting aside a fixed amount, hoarded being that you stockpiled/amassed it. Saying "you hoarded your rations" (whether they will expire) does feel more on the money than "you ration your rations" from that perspective.I hope this doesn't come off too "well aktually", I've just been thinking about how I still realize different meanings/origins of common words later in life and the odd things that trigger me to think about it differently for the first time. A recent one for me was that "whoever" has the (fairly obvious) etymology of who+everhttps://www.etymonline.com/word/whoevervs something like balloon, which has a comparatively more complex historyhttps://www.etymonline.com/word/balloon

reply

14123newsletter

8 minutes ago

 |
root
 |
parent
 |
next

[–]

Isn't hoarding means you can get more bread ? While rationing means: "here is 1kg, use it however you want but you can't get more".

reply

mattkrause

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

For me, the difference between ration and hoard is the uhh…rationality of the plan.

Rationing suggests a deliberate, calculated plan: we’ll eatthis muchattheseparticular times so our food laststhatlong. Hoard seems more ad hoc and fear-driven: better keep yet another beat-up VGA cable, just in case.

reply

jjani

2 hours ago

 |
root
 |
parent
 |
next

[–]

> Hoard seems more ad hoc and fear-driven: better keep yet another beat-up VGA cable, just in case.

Counterexample: animals hoarding food for winter time, etc.

reply

canada_dry

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

OpenAI's "PRO" subscription is really a waste of money IMHO for this and other reasons.

Decided to give PRO a try when I kept getting terrible results from the $20 option.So far it's perhaps 20% improved in complex code generation.It still has the extremely annoying ~350 line limit in its output.It still IGNORES EXPLICIT CONTINUOUS INSTRUCTIONS eg: do not remove existing comments.The opaque overriding rules that - despite it begging forgiveness when it ignores instructions - are extremely frustrating!!

reply

jmaker

26 minutes ago

 |
root
 |
parent
 |
next

[–]

There are things it’s great at and things it deceives you with. In many things I needed it to check something for me I knew was a problem, o3 kept insisting it were possible due to reasons a,b,c, and thankfully gave me links. I knew it used to be a problem so surprised I followed the links only to read black on white it still wasn’t. So I explained to o3 that it’s wrong. Two messages later we were back at square one. One week later it didn’t update its knowledge. Months later it’s still the same.

But at things I have no idea about like medicine it feels very convincing. Am I in hazard?People don’t understand Dunning-Kruger. People are prone to biases and fallacies. Likely all LLMs are inept at objectivity.My instructions to LLMs are always strictness, no false claims, Bayesian likelihoods on every claim. Some modes ignore the instructions voluntarily, while others stick strictly to them. In the end it doesn’t matter when they insist on 99% confidence on refuted fantasies.

reply

sothatsit

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

Anthropic also does this because they will dynamically change the limits to manage load. Tools like ccusage show you how much you've used and I can tell sometimes that I get limited with significantly lower usage than I would usually get limited for.

reply

brookst

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

I think the simple product prioritization explanation makes way more sense than a a second-order conspiracy to trick people into hoarding.

Reality is probably that there’s a backlog item to implement a view, but it’s hard to prioritize over core features.

reply

hinkley

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

> it’s an important enough resource that my lizard brain wants to hoard it.

I have zero doubt that this is working exactly as intended. We will keep all our users at 80% of what we sold them by keeping them anxious about how close they are to the limit.

reply

sitkack

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

Working as Intended.

reply

Wowfunhappy

9 hours ago

 |
root
 |
parent
 |
next

[–]

Well, kind of. If you don't use it at all you're going to unsubscribe.

This isn't like a gym membership where people join aspirationally. No one's new year's resolution is "I'm going to use o3 more often."

reply

mattigames

7 hours ago

 |
root
 |
parent
 |
next

[–]

Yes it is, in the way of "I'm gonna work on X thing that is now much easier thanks to chatGPT" and then never work on it due lack of time or motivation or something else.

reply

christina97

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

What makes you think it’s any different?

reply

gfiorav

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

I nervously hover over the VSCode Copilot icon, watching the premium requests slowly accumulate. It’s not an enjoyable experience (whether you know how much you've used or not :) )

reply

milankragujevic

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

Where did you find this info? I am unable to find in on OpenAI's website.
https://help.openai.com/en/articles/6950777-what-is-chatgpt-...

I haven't yet run into this limit...

reply

milankragujevic

1 hour ago

 |
root
 |
parent
 |
next

[–]

Found it:
https://help.openai.com/en/articles/9824962-openai-o3-and-o4...

reply

oc1

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

They know this psychology. This dark pattern is intentional so you will use their costly service less.

reply

hn_throwaway_99

6 hours ago

 |
root
 |
parent
 |
next

[–]

I don't think this counts as a "dark pattern". The reality is that these services are resource constrained, so they are trying to build in resource limits that are as fair as possible and prevent people from gaming the system.

reply

const_cast

3 hours ago

 |
root
 |
parent
 |
next

[–]

The dark pattern isn't the payment pattern, that's fine. The dark pattern is hiding how much you're using, thereby tricking the human lizard brain into irrationally fearing they are running out.

The human brain is stupid and remarkably exploitable. Just a teensy little bit of information hiding can illicit strange and self-destructive behavior from people.You aren't cut off until you're cut off, then it's over completely. That's scary, because there's no recourse. So people are going to try to avoid that as much as possible. Since they don't know how much they're using, they're naturally going to err on the side of caution - paying for more than they need.

reply

hshdhdhj4444

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

Besides the click mazes to unsubscribe I’m struggling to think of a darker pattern than having usage limits but not showing usage.

The dark pattern isn’t the usage limit. It’s the lack of information about current and remaining usage.

reply

aspenmayer

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

> prevent people from gaming the system

If I sit down for dinner at an all-you-can-eat buffet, I get to decide how much I’m having for dinner. I don’t mind if they don’t let me take leftovers, as it is already understood that they mean as much as I can eat in one sitting.If they don’t want folks to take advantage of an advertised offer, then they should change their sales pitch. It’s explicitlynotgaming any system to use what you’re paying for in full. That’s your right and privilege as that’s the bill of goods you bought and were sold.

reply

Wowfunhappy

2 hours ago

 |
root
 |
parent
 |
next

[–]

I feel like using Claude Code overnight while you sleep or sharing your account with someone else is equivalent to taking home leftovers from an all-you-can-eat buffet.

I also find it hard to believe 5% of customers are doing that, though.

reply

aspenmayer

2 hours ago

 |
root
 |
parent
 |
next

[–]

If that’s off-peak time, I’d argue the adjacent opposite point, that Anthropic et al could implement deferred and/or scheduled jobs natively so that folks can do what they’re going to do anyway in a way that comports with reasonable load management that all vendors must do.

For example, I don’t mind that Netflix pauses playback after playing continuously for a few episodes of a show, because the options they present me with acknowledge different use cases. The options are: stop playing, play now and ask me again later, and play now and don’t ask me again. These options are kind to the user because they don’t disable the power user option.

reply

artursapek

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

Just curious, what do people use these expensive reasoning models for?

reply

wahnfrieden

2 hours ago

 |
root
 |
parent
 |
next

[–]

Code

reply

littlestymaar

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

> This is how I feel about the 100 msg/wk limit on o3 for the ChatGPT

Do I read this correctly? Only 100 messages per week, on the pro plan worth a few hundred buck a month?!

reply

CSMastermind

9 hours ago

 |
root
 |
parent
 |
next

[–]

That's definitely not correct because I'm on the pro plan and make extensive use of o3-pro for coding. I've sent 100 messages in a single day with no limitation.

Per their website:https://help.openai.com/en/articles/9793128-what-is-chatgpt-...There are no usage caps on pro users (subject to some common sense terms of use).

reply

mhl47

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

No it's 100 a week for plus users.

reply

el_benhameen

9 hours ago

 |
root
 |
parent
 |
next

[–]

Sorry, yes, plus, not pro.

reply

doorhammer

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

I think it’s just a mistype

I have a pro plan and I hammer o3–I’d guess more than a hundred a day sometimes—and have never run into limits personallyWouldn’t shock me if something like that happened but haven’t seen evidence of it yet

reply

jstummbillig

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

If it behaves anything like the GPT-4.5 Limit, it will let you know when you near the limit.

reply

yencabulator

7 hours ago

 |
root
 |
parent
 |
next

[–]

Claude daily limit sure didn't.

reply

forty

8 hours ago

 |
parent
 |
prev
 |
next

[–]

It makes me sad that devs start relying on proprietary online services to be able to work. We have been lucky enough to have FOSS tools to do everything and not to have to rely on any specific service or company to work and some of us are deciding to become like Monsanto-addicted farmers who forgot how to do their jobs without something they have to pay every month.

reply

brookst

4 hours ago

 |
root
 |
parent
 |
next

[–]

I remember being beholden to commercial (cough, pirated, cough) compilers and assemblers back in the day. FOSS is awesome but often lags because capital sees a chance to make money and can move faster.

It will change. There will be FOSS models, once it no longer takes hundreds of millions of dollars to train them.

reply

pythonguython

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

Do you mind sharing what industry you’re in where you can fully rely on FOSS? In my industry we’re dependent on MATLAB, Xilinx tools, closed source embedded software and more. To name a few industries: game devs might be stuck with unity, finance quant devs might be stuck with Bloomberg terminals, iOS app devs are stuck with apple’s tooling etc… this isn’t just an LLM problem IMO.

reply

aprdm

2 hours ago

 |
root
 |
parent
 |
next

[–]

backend web services
devops
frontend javascript

just three possible examples

reply

stingraycharles

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

Devs have been doing this for years. If Github goes down, it has a huge impact on dev productivity.

reply

forty

39 minutes ago

 |
root
 |
parent
 |
next

[–]

Has it? We don't use GitHub in my company, but our self hosted Gitlab occasionally goes down, and while it prevents us from merging (including doing code reviews) and deploying code, it does not prevent us from doing most of our work (ie designing and creating software). It merely delays the moment when things are shipped.

If you meant goes down for good, then I'm sure it would be annoying for a few weeks for the FOSS ecosystem, just the time to migrate elsewhere, but their is not much GitHub specific we would really miss.

reply

arvinsim

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

I think it's less about reliance and more about competition.

Sure, devs can still work without AI.But if the developer who uses AI has more output than the one that doesn't, it naturally incentives everyone to leverage AI more and more.

reply

forty

34 minutes ago

 |
root
 |
parent
 |
next

[–]

That's a big if. People might feel faster because there is more "movement", but it's not clear if overall they are actually signicantly faster (though everyone would like us to believe so).

And note that I objected online services, local LLM don't have the same issues.

reply

danielbln

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

The very recent agentic open weights models seem to be shaping up, so if all fails you can host one of these yourself (if you have the vram) or host it yourself somewhere.

reply

sneak

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

We can and did work without it. It just makes us many times faster.

Nothing about using an LLM removes skills and abilities you already had before it.

reply

3836293648

5 hours ago

 |
root
 |
parent
 |
next

[–]

For the industry as a whole it absolutely does. And for the individual it absolutely does kill your ability to do it unless you actually do practice.

And yes, the goal might be to only use it for boilerplate or first draft. But that's today, people are lazy, just wait for the you of tomorrow

reply

umbra07

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

If you don't use a skill, it atrophies.

Now, maybe thatisthe future (no more/extremely little human-written code). Maybe that's a good thing in the same way that "xtechnological advancement meansyskill is no longer necessary" - like how the advent of readily-accessible live maps means you don't need to memorize street intersections and directions or whatever. But it is true.

reply

brookst

4 hours ago

 |
root
 |
parent
 |
next

[–]

I am terrible at computing sine and cosine, for sure. It doesn’t bother me.

reply

hoppp

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

My experience was that reviewing generated code can take longer than writing it from scratch.

There was research about vibe coding that had similar conclusion. Feels productive but can take longer to review.the moment you generate code you don't instantly understand you are better off reading the docs and writing it yourself

reply

blitzar

9 hours ago

 |
parent
 |
prev
 |
next

[–]

> Anthropic is saying that one out of every 20 users will hit the new limit.

I regularly hit the the Pro limits 3 times a day using sonnet. If I use claude code & claude its over in about 30 minutes. No multi 24/7 agent whatever, no multiple windows open (except using Claude to write a letter between claude code thoughts).I highly doubt I am a top 5%er - but wont be shocked if my week ends on a wednessday. I was just starting to use Claude chat more as it is in my subscription but if I can not rely on it to be available for multiple days its functionally useless - I wont even bother.

reply

Aurornis

9 hours ago

 |
root
 |
parent
 |
next

[–]

> If I use claude code & claude its over in about 30 minutes.

Can you share what you're doing? I've been experimenting with Claude Code and I feel like I have to be doing a lot with it before I even start seeing the usage warning limits on the $20/month plan.When I see people claiming they're getting rate limited after 30 minutes on the $100/month plan I have a hard time understanding what they're doing so different.For what it's worth I don't use it every day, so maybe there's a separate rate that applies to heavy and frequent users?

reply

flutas

7 hours ago

 |
root
 |
parent
 |
next

[–]

$20/mo plan doesn't include opus (the larger model) like the $100+ plans do, it's likely they are hitting the opus limit which is fairly low.

reply

r053bud

4 hours ago

 |
root
 |
parent
 |
next

[–]

The $20/month plan most definitely does include Opus. Just not a ton of usage allowed.

reply

eagleinparadise

3 hours ago

 |
root
 |
parent
 |
next

[–]

Only opus on web. Not Claude code

reply

bogtog

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

> I highly doubt I am a top 5%er - but wont be shocked if my week ends on a wednessday. I was just starting to use Claude chat more as it is in my subscription but if I can not rely on it to be available for multiple days its functionally useless - I wont even bother.

You very well might be a top 5%er among people only on the Pro rather than Max plan

reply

ketzo

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

What does your Claude code usage look like if you’re getting limited in 30 minutes
without
 running multiple instances? Massive codebase or something?

reply

blitzar

8 hours ago

 |
root
 |
parent
 |
next

[–]

I set claude about writing docstrings on a handful of files - 4/5 files couple 100 lines each - couple of classes in each - it didnt need to scan codebase (much).

Low danger task so I let it do as it pleased - 30 minutes and was maxed out. Could probably have reduced context with a /clear after every file but then I would have to participate.

reply

Kurtz79

12 minutes ago

 |
root
 |
parent
 |
next

[–]

If I understand correctly, looking at API pricing for Sonnet, output tokens are 5 times more expensive than input tokens.

So, if rate limits are based on an overall token cost, it is likely that one will hit them first if CC reads a few files and writes a lot of text as output (comments/documentation) rather than if it analyzes a large codebase and then makes a few edits in code.

reply

tlbsofware

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

You can tell it to review and edit each file within a Task/subagent and can even say to run them in parallel and it will use a separate context for each file without having to clear them manually

reply

blitzar

8 hours ago

 |
root
 |
parent
 |
next

[–]

Every day is a school day - I feel like this is a quicker way to burn usage but it does manage context nicely.

reply

tlbsofware

8 hours ago

 |
root
 |
parent
 |
next

[–]

I haven’t ran any experiments about token usage with tasks, but if you ran them all together without tasks, then each files full operation _should_ be contributing as cached tokens for each subsequent request. But if you use a task then only the summary returned from that task would contribute to the cached tokens. From my understanding it actually might save you usage rates (depending on what else it’s doing within the task itself).

I usually use Tasks for running tests, code generation, summarizing code flows, and performing web searches on docs and summarizing the necessary parts I need for later operations.Running them in parallel is nice if you want to document code flows and have each task focus on a higher level grouping, that way each task is hyper focused on its own domain and they all run together so you don’t have to wait as long, for example:- “Feature A’s configuration”
- “Feature A’s access control”
- “Feature A’s invoicing”

reply

stuaxo

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

I hope you thoroughly go through these as a human, purely AI written stuff can be horrible to read.

reply

blitzar

8 hours ago

 |
root
 |
parent
 |
next

[–]

Docstring slop is better than code slop - anyway that is what git commits are for - and I have 4.5 hours to do that till next reset.

reply

debo_

7 hours ago

 |
root
 |
parent
 |
next

[–]

Coding is turning into an MMO!

reply

rapind

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

I think you'll want to specify your /model to not use opus. Strangely unintuitive, but I opted out of opus on the max plan myself and aren't really having any usage issues since.

reply

_jab

9 hours ago

 |
parent
 |
prev
 |
next

[–]

> Anthropic is saying that one out of every 20 users will hit the new limit.

Very good point, I find it unlikely that 1/20 users is account sharing or running 24/7 agentic workflows.

reply

Terretta

9 hours ago

 |
root
 |
parent
 |
next

[–]

Moreover, if you run a SaaS, generally somewhere from 1 in 5 to 1 in 20 users are using you for real, while the others are mostly not using you.

The stat would be more interesting if instead of 1 in 20 users, they said x in y of users with at least one commit per business day, or with at least one coding question per day, or whatever.I suspect this could be a significantly higher percentage of professional users they plan to throttle. Be careful of defining Pro like Apple does if you market to actual professionals who earn based on using your product. Your DAUs might be a different ratio than you expect.

reply

0cf8612b2e1e

8 hours ago

 |
root
 |
parent
 |
next

[–]

… if you run a SaaS, generally somewhere from 1 in 5 to 1 in 20 users are using you for real, while the others are mostly not using you.That is a hilarious and believable stat. Has anyone published such numbers or is it a dirty secret about how many corporate licenses are purchased and never used by the rank and file?I can personally think of a few internally licensed products, announced with huge fan fare, which never get used beyond the demo to a VP.

reply

xxpor

5 hours ago

 |
root
 |
parent
 |
next

[–]

https://en.wikipedia.org/wiki/Pareto_distribution
 /
https://en.wikipedia.org/wiki/Pareto_principle

reply

data-ottawa

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

Anecdotally that’s my observation as well.

reply

rapind

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

A decent chunk (more than 1/20) account shared netflix. Also there are probably some who are account sharing with more than one other person. I don't really doubt it.

reply

matt3210

31 minutes ago

 |
parent
 |
prev
 |
next

[–]

>If I do hit the limit, that's it for the entire week

Now your vibes can be at the beach.

reply

furyofantares

8 hours ago

 |
parent
 |
prev
 |
next

[–]

> I'm probably not going to hit the weekly limit, but it makes me nervous that the limit is weekly as opposed to every 36 hours or something. If I do hit the limit, that's it for the entire week—a long time to be without a tool I've grown accustomed to!

Well, not the entire week, however much of it is left. You said you probably won't hit it -- if you do, it's very likely to be in the last 36 hours (20% of a week) then, right? And you can pay for API usage anyway if you want.

reply

arghwhat

9 hours ago

 |
parent
 |
prev
 |
next

[–]

> but I'd feel the same about the prospect of loosing ripgrep for a week, or whatever. Loosing it for a couple of days is more palatable.

Just to nitpick: When the limit is a week, going over it does not mean losing access for a week, but for the remaining time which would assuming the limits aren't overly aggressive mean losing access for at most a couple of days (which you say is more palatable).I wouldn't say you're too reliant, but it's still good to stay sharp by coding manually every once in a while.

reply

stingraycharles

1 hour ago

 |
parent
 |
prev
 |
next

[–]

Yeah, if this happens, I’m probably going to do the inevitable: get two accounts. If I could pay $500 a month for Claude 100x I would probably do it at this point.

Given that I rarely hit the session limits I’m hopeful I won’t be affected, but the complete and utter lack of transparency is really frustrating.

reply

Aeolun

24 minutes ago

 |
root
 |
parent
 |
next

[–]

Like, I understand why they do it, usage patterns aren’t the same all over the world, and they paid for the GPU’s anyway, so they want to utilize them. People in parts of the world that see less CC utilization get to do more with their CC plan than people in very busy areas of the world.

reply

arach

9 hours ago

 |
parent
 |
prev
 |
next

[–]

if it affects only a minority of accounts, why not figure out how to special case them without affecting everyone else is the primary question I would ask myself if I worked on this

the principle: let's protect against outliers without rocking the behavior of the majority, not at this stage of PMF and market discoveryi'd also project out just how much the compute would cost for the outlier cohort - are we talking $5M, $100M, $1B per year? And then what behaviors will simply be missed by putting these caps in now - is it worth missing out on success stories coming from elite and creative users?I'm sure this debate was held internally but still...

reply

vineyardmike

9 hours ago

 |
root
 |
parent
 |
next

[–]

Because the goal is to extract more money from the people who have significant usage. These users are the actual targets of the product. The idea that it’s a few bad actors is misdirection of blame to distract “power users”.

They undercharged for this product to collect usage data to build better coding agents in the future. It was a ploy for data.Anecdotally, I use Claude Code with the $20/mo subscription. I just use it for personal projects, so I figured $20 was my limit on what I’d be willing to spend to play around with it. I historically hit my limits just a few times, after ~4hrs of usage (resets every 5hrs). They recently updated the system and I hit my limits consistently within an hour or two. I’m guessing this weekly limit will affect me.I found a CLI tool (which I found in this thread today) that estimates I’m using ~$150/mo in usage if I paid through the API. Obviously this is very different from my payments. If this was a professional tool, maybe I’d pay, but not as a hobbyist.

reply

Uehreka

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

> why not figure out how to special case them without affecting everyone else

I’m guessing that they did, and that that’s what this policy is.If you’re talking about detecting account sharing/reselling, I’m guessing they have some heuristics, but they really don’t want the bad press from falsely accusing people of that stuff.

reply

arach

8 hours ago

 |
root
 |
parent
 |
next

[–]

fair enough - DS probably ran through data and came up with 5% and some weekly cutoff as a good starting point until they have better measures in place

my point is that 5% still a large cohort and they happen to be your most excited/creative cohort. they might not all want to pay a surchageyetwhile everyone is discovering the use cases / patterns / etchaving said that, entirely possible burn rate math and urgency requires this approach

reply

data-ottawa

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

They did have several outages last week, it would be good to find better plans for those huge users but I can also see them wanting to just stop the bleeding.

reply

arach

9 hours ago

 |
root
 |
parent
 |
next

[–]

I've noticed the frequent perf issues and I'm on the 20x plan myself - good point that you'd want to stop the bleeding or bad actors to make sure the majority have a better experience

reply

Aurornis

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

> why not figure out how to special case them without affecting everyone else is the primary question I would ask myself if I worked on this

The announcement says that using historical data less than 5% of users would even be impacted.That seems kind of clear: The majority of users will never notice.

reply

arach

8 hours ago

 |
root
 |
parent
 |
next

[–]

5% of a large number is a large number - this why it's both a significant problem for them and why I'm thinking out loud about the downsides of discouraging good actors who happen to be power users.

that 5% is probably the most creative and excited cohort. obviously it's critical to not make the experience terrible for the 95% core, but i'd hate to lose even a minority of the power users who want to build incredible things on the platformhaving said that, the team is elite, sure they are thinking about all angles of this issue

reply

0cf8612b2e1e

8 hours ago

 |
root
 |
parent
 |
next

[–]

5% seems like a huge number of previously ecstatic customers who may suddenly be angry. Especially when it is trivial to identify the top 0.1% of users who are doing something insane.

reply

nharada

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

What do you think they should have done instead?

reply

actsasbuffoon

8 hours ago

 |
root
 |
parent
 |
next

[–]

At a bare minimum there needs to be some way to understand how close you are to these limits. People shouldn’t be wondering if this is going to impact them or not.

reply

arach

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

It’s tricky without seeing the actual data. 5% of a massive user base can still be a huge number so I get that it’s hard to be surgical.

But those power users are often your most creative, most productive, and most likely to generate standout use cases or case studies. Unless they’re outright abusing the system, I’d lean toward designing for them, not against them.if the concern is genuine abuse, that feels like something you handle with escalation protocols: flag unusual usage, notify users, and apply adaptive caps if needed. Blanket restrictions risk penalizing your most valuable contributors before you’ve even discovered what they might build

reply

smileysteve

7 hours ago

 |
root
 |
parent
 |
next

[–]

5% of a massive user base could also be huge if 50% of users are on an enterprise plan and barely using it.

reply

arach

5 hours ago

 |
root
 |
parent
 |
next

[–]

in other words, these limits will help introduce Enterprise (premium) plans?

reply

bananapub

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

> if it affects only a minority of accounts, why not figure out how to special case them without affecting everyone else

that's exactly what they have done - the minority of accounts that consume many standard deviations above the mean of resources will be limited, everyone else will be unaffected.

reply

arach

9 hours ago

 |
root
 |
parent
 |
next

[–]

"You're absolutely right!" i misread the announcement - thought everyone moved to primarily a weekly window but seems like 5hr window still in place and they're putting in place another granularity level control that DS teams will adjust to cutoff mostly bad actors.

correct me if I'm wrong, it's not like we have visibility into the token limit logic, even on the 5hr window?

reply

jonas21

9 hours ago

 |
parent
 |
prev
 |
next

[–]

You can use an API key to get more usage on a pay-as-you-go basis.

reply

blitzar

9 hours ago

 |
root
 |
parent
 |
next

[–]

You can set cash on fire if you want to.

reply

thejazzman

8 hours ago

 |
root
 |
parent
 |
next

[–]

i've gotten months of usage out of openai and claude where i seeded each with only $5

but if you use an agent and it tries to include a 500kb json file, yeah, you will light cash on fire(this happened to me today but the rate limit bright it to my attention.)

reply

blitzar

7 hours ago

 |
root
 |
parent
 |
next

[–]

Fortunately Ai companies are not (currently) like AWS - you can only burn as much money as you have on account.

For brief, low context interactions, it is crazy how far your money goes.

reply

fullstackwife

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

you spend 400$ per month on api usage, but your AI builds the next unicorn worth billions, where is the problem?

reply

blitzar

9 hours ago

 |
root
 |
parent
 |
next

[–]

For $2 you can have a lottery ticket that will win you a quater of a billion dollars.

reply

edude03

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

You might have better odds buying scratchers - assuming you even have $400/m to invest in an enterprise without cash flow

reply

Wowfunhappy

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

Yes, but that's so expensive I will never do it!

reply

tqwhite

7 hours ago

 |
root
 |
parent
 |
next

[–]

With one months exception, I've never gotten past $150 with API. I plan to do the $100 plan and use the API for overflow. I think I will come out ahead.

reply

Wowfunhappy

7 hours ago

 |
root
 |
parent
 |
next

[–]

Well, lucky you! Before Claude Max was an option, I burned a
lot
 of money using Claude Code, and that was while I was trying my best to use it as little as possible.

reply

wahnfrieden

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

Just buy several Max tier subscriptions...

reply

swalsh

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I used about $300 worth of credits based on ccusage ($20 pro plan). It's pretty easy to hit the limit once you get going.

reply

blitzar

9 hours ago

 |
root
 |
parent
 |
next

[–]

I use about $20 a day - 6 days a week, on the $20 plan.

reply

jcims

8 hours ago

 |
parent
 |
prev
 |
next

[–]

Cursor sent me a note yesterday that at my current usage rate I was going to exceed whatever cap was in place at some date in the future. I thought that was very helpful.

reply

mattlangston

4 hours ago

 |
parent
 |
prev
 |
next

[–]

I have both a Claude subscription plan and console credits as my backup, which I thought was a reasonable solution.

reply

jonfw

5 hours ago

 |
parent
 |
prev
 |
next

[–]

GitHub copilot has a monthly rate limit for premium models- much worse! I ran into mine within hours of using Claude

reply

tqwhite

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Don't you also have an API subscription to provide overflow capacity?

reply

lerchmo

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Time to start using Claude code proxy and other models. This black box rate limit is really lame.

reply

wahnfrieden

2 hours ago

 |
parent
 |
prev
 |
next

[–]

It is becoming typical to counter this (and the multi-hour limits) simply by purchasing multiple Max tier subscriptions.

reply

tkiolp4

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Don’t worry, just give them more money.

reply

jey

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Get two subscriptions if it's delivering that much value and you hit the limits?

reply

mrits

9 hours ago

 |
parent
 |
prev
 |
next

[–]

I imagine they will add some features soon where you have more control. It could get complicated quickly. Before they put this in I think they should have at least given you an easy way to buy more credits at a hugely discounted rate.

I know entire offices in Bangladesh share some of these accounts, so I can see how it is a problem.

reply

fuzzzerd

9 hours ago

 |
root
 |
parent
 |
next

[–]

That is exactly the use case they're trying to stop. Sharing accounts.

reply

mrits

9 hours ago

 |
root
 |
parent
 |
next

[–]

Which is why I said I see how it could be a problem :)

reply

j45

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Getting in early on a plan may not have as much of an upside where the computational costs and guaranteed heavily can look different than other services.

If it's affecting 5% of users, it might be people who are really pushing it and might not know (hopefully they get a specialized notice that they may see usage differences).

reply

ekianjo

5 hours ago

 |
parent
 |
prev
 |
next

[–]

the first rule of APIs is do not expect them to work 24/7. and you are never in control of any change that can occur. Thats why its really important to cultivate local LLMs.

reply

douglaswlance

9 hours ago

 |
parent
 |
prev
 |
next

[–]

pay for another account to double your limit.

reply

draxil

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Of course ripgrep runs on your machine and you control it.

reply

dewey

9 hours ago

 |
root
 |
parent
 |
next

[–]

ripgrep is an example for "tool I've grown accustomed to", where it runs is irrelevant.

reply

sva_

8 hours ago

 [flagged]
 |
parent
 |
prev
 |
next

[6 more]

> —

Is it really necessary to use GPT to write a simple comment like that?

reply

tomhow

1 minute ago

 |
root
 |
parent
 |
next

[–]

Please don't do this here. If a comment seems unfit for HN, please flag it and email us at hn@ycombinator.com so we can have a look.

reply

Wowfunhappy

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

On a Mac, you can use option-shift-dash to insert an emdash, which is muscle memory for me.

If Ihadused an LLM, maybe I wouldn't have misspelled "losing" not once buttwiceand not noticed until after the edit window. <_<

reply

adastra22

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

Was it necessary to post this?

FYI many input methods (including my own) turn two hyphens into an em dash. The em-dash-means-LLM thing is bogus.

reply

seb1204

7 hours ago

 |
root
 |
parent
 |
next

[–]

Ms word does this by default

reply

fredoliveira

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

You can't possibly think that using an em dash is exclusive to AI-generated output.

reply

jimbo808

11 hours ago

 |
prev
 |
next

[–]

I'm not sure how this will play out long term, but I really am not a fan of having to feel like I'm using a limited resource whenever I use an LLM. People like unlimited plans, we are used to them for internet, text messaging, etc. The current pricing models just feel bad.

reply

andruby

11 hours ago

 |
parent
 |
next

[–]

Unlimited works well for everything that is “too cheap to meter”.

Internet, text messages, etc are roughly that: the direct costs are so cheap.That’s not the case with LLM’s at this moment. There are significant direct costs to each long-running agent.

reply

rmujica

10 hours ago

 |
root
 |
parent
 |
next

[–]

Internet and SMS used to be expensive and metered until they weren't thanks to technological advances and expanded use. I think LLMs will follow the same path, maybe on a shorter timespan.

reply

cmsjustin

10 hours ago

 |
root
 |
parent
 |
next

[–]

They were not expensive to operate, they were only expensive for consumers

reply

tialaramex

10 hours ago

 |
root
 |
parent
 |
next

[–]

Right, that's crucial to understand. In 1985 you could make a direct dial from England to the US but it was
eye wateringly
 expensive. £2 per minute. An hour's call to your mum? That's over £100.

But the cost to Bell and British Telecom was not £2 per minute, or £1 per minute, or even 1p per minute, it was nothing at all. Their costs were not for the call, but for the infrastructure over which the call was delivered, a transatlantic cable. If there was one call for ten minutes, once a week essentially at random, that cable must still exist, but if there are 10 thousand call minutes per week, a thousand times more, it's the same cable.So the big telcos all just picked a number and understood it as basically free income. If everybody agrees this call costs £2 then it costs £2 right, and those 10 thousand call minutes generate a Million pound annual income.It's maybe easier for Americans to understand if you tell them thatoutsidethe US the local telephone calls cost money back then. Why were your calls free? Because why not, the decision to charge for the calls is arbitrary, the calls don't actually cost anything, but you will need to charge somehow to recoup the maintenance costs. In the US the long distance calls were more expensive to make up for this for a time, today it's all absorbed in a monthly access fee on most plans.

reply

tqwhite

7 hours ago

 |
root
 |
parent
 |
next

[–]

There was some capital expenditure that had to be paid for.

In the US, ATT was just barely deregulated by then so the prices were not just 'out of thin air'.

reply

daveguy

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

This analysis doesn't concern the limited bandwidth available for call delivery on plain old telephone networks (POTS). They did squeeze extra money out of the system with their networks as a monopoly, but the cost was zero only if you don't consider the cost of operating and maintaining the network, or the opportunity cost of having much less bandwidth than currently available. For the former, they still had to fix problems. For the latter if they had made calls pennies everyone would have had "all circuits are busy" all the time. A single line
wasn't capable of carrying 10,000 calls
 back then. Pricing to limit usage to available bandwidth was as important as recouping infrastructure costs and ongoing maintenance. There's also a lemonade stand pricing effect. If you charge too little you don't get enough to cover costs. But if you charge too much, not enough people will do business and you won't cover costs. Also, ma bell was broken up in 1982, but regional monopolies lasted a lot longer (telecommunications act of 1996).

reply

tialaramex

7 hours ago

 |
root
 |
parent
 |
next

[–]

TAT-7 which was in operation in 1985 when I cited the £2 per minute price carried 4000 simultaneous calls, ie up to £8000 per minute

Its successor TAT-8 carried ten times as many calls a few years later, industry professionals opined that there was likely no demand for so many transatlantic calls and so it would never be full. Less than two years later TAT-8 capacity maxed out and TAT-9 was already being planned.Today lots of people havehome Internet servicesignificantly faster thanall three of these transatlantic cables put together.

reply

daveguy

2 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you for confirming my statements.

reply

KaiserPro

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

To lay the cables required a huge amount of capital, to make that feasible its required financial engineering. That translates to high operating expenses.

reply

AlotOfReading

10 hours ago

 |
root
 |
parent
 |
next

[–]

SMS was originally piggybacking off unused bytes in packets already being sent to the tower, which was being paid for by existing phone bills. The only significant expenses involved transiting between networks. That was a separate surcharge in the early days.

reply

ssk42

9 hours ago

 |
root
 |
parent
 |
next

[–]

Used to be? What changed?

reply

daveguy

9 hours ago

 |
root
 |
parent
 |
next

[–]

People started sending a lot more texts and making a lot fewer phone calls. And you can only piggyback so many text messages on the call packets.

reply

hkt

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

Competition is the thing. Prices will drop as more AI code assistants get more adoption.

Prices will probably also drop if anyone ever works out how to feasibly compete with NVIDIA. Not an expert here, but I expect they're worried about competition regulators, who will be watching them very closely.

reply

troupo

8 hours ago

 |
root
 |
parent
 |
next

[–]

> Prices will drop as more AI code assistants get more adoption.

No, they won't. Because "AI assistants" are mostly wrapped around a very limited number of third-party providers.And those providers are hemorrhaging money like crazy, and will raise the prices, limit available resources and cut off external access — all at the same time. Some of it is already happening.

reply

alwillis

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

Yes and no.

It’s very expensive to create these models and serve them at scale.Eventually the processing power required to create them will come down, but that’s going to be a while.Even if there was a breakthrough GPU technology announced tomorrow, it would take several years before it could be put into production.And pretty much only TSMC can produce cutting edge chips at scale and they have their hands full.Between Anthropic, xAI and OpenAI, these companies have raised about $84billiondollars in venture capital… VCs are going to want a return on their investment.So it’s going to be a while…

reply

margalabargala

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

SMS was designed from the start to fit in the handul of unused bytes in the tower handshake that was happening anyway, hence the 160 char limit. Its marginal cost has always been free on the supply side.

reply

RF_Savage

9 hours ago

 |
root
 |
parent
 |
next

[–]

SMS routing and billing systems did cost money.
Especially billing, as the standards had nothing for it, so it was done by 3rd party software for a very long time.

reply

margalabargala

9 hours ago

 |
root
 |
parent
 |
next

[–]

Of course, how pleasingly circular. "It's so expensive because it costs so much to charge you for it".

reply

baq

8 hours ago

 |
root
 |
parent
 |
next

[–]

Exactly! AWS is so expensive because it can be so cheap. Billing was the true innovation.

reply

xtracto

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

I think LLMs follow more of an Energy analogy: Gas or Electricity, or even water.

How much has any if these decreased over the last 5 decades? The problem is that as of right now, LLM cost is linearly (if not exponentially) related to the output. It's basically "transferring energy" converted into bytes. So unless we see some breakthrough in energy generation, or better use it, it will be difficult to scale.This makes me wonder, would it be possible to pre-compue some kind of "rainbow tables" equivalent for LLMs? Either stored in the client or in the server; so as to reduce the computing needed for inference.

reply

valenterry

1 hour ago

 |
root
 |
parent
 |
next

[–]

I don't think so. Yes, LLMs use electricity. But they use electricity in the data-center, not in your home. That's very different, because it's cheap to transfer tokens from the data-center to your home, but it's not cheap to transfer electricity from the data-center to your home. And that matters, because we can build a data-center in a place where there's lots of renewable and hence cheap energy (e.g. from solar or from water/wind).

If you think about it, LLMs are used mostly when people are awake, at least right now. And when is the sun shining? Right. So, build a data-center somewhere where land is cheap and lots of solar panels can be build right next to it. Sure, some other energy source will be used for stability etc., but it won't be as expensive as the energy price for your home.> This makes me wonder, would it be possible to pre-compue some kind of "rainbow tables" equivalent for LLMs?Already happening. Read up on how those companies do caching prompt-prefixes etc.

reply

whimsicalism

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

maybe, but they are not nearly as comparable as you’re making it out to be

reply

MuffinFlavored

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

> That’s not the case with LLM’s at this moment.

I'd be curious to know how many tokens the average $200/mo user uses and what the cost on their end for it is.

reply

KronisLV

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I personally take an issue with them expecting that your usage would be more or less consistent throughout the month. Instead, I might have low usage throughout most of the month and then an 11 hour binge a few days, which in most cases would involve running into rate limits (either that, or just token limitations for inputs).

That's why using the API directly and paying for tokens anything past that basic usage feels a bit nicer, since it's my wallet that becomes the limitation then, not some arbitrary limits dreamed up by others. Plus with something like OpenRouter, you can also avoid subscription tier related limits likehttps://docs.anthropic.com/en/api/rate-limits#rate-limitsThough for now Gemini 2.5 Pro seems to work a bit better than Claude for my code writing/refactoring/explanation/exploration needs. Curious what other cost competitive options are out there.

reply

tqwhite

7 hours ago

 |
root
 |
parent
 |
next

[–]

This is my strategy as well. I definitely have surges of usage.

Except for one catastrophic binge where I accidentally left Opus on for a whole binge (KILL ME!!!), I use around $150/month. I like having the spigot off when I am not working.Would the $100/month plan plus API for overflow come out ahead? Certainly on some months. Over the year, I don't know. I'll let you know.

reply

bugglebeetle

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

Gemini 2.5 Pro is a better coding model, but Gemini CLI is way behind Claude Code, perhaps because the model itself isn’t well-tuned for agentic work. If you’re just doing targeted refactoring and exploration, you can copy and paste back and forth from the web app for $20 a month.

reply

KronisLV

8 hours ago

 |
root
 |
parent
 |
next

[–]

I mostly use RooCode nowadays, which works well enough with both Claude and Gemini and other models, even locally hosted ones. Decoupling the LLM vendor from the tools might miss out on some finer features, but also gives me a little bit more freedom, much like how you can also do with the Copilot plugins and Continue.dev and a few others.

Note: all of them sometimes screw up applying diffs, but in general are good enough.

reply

ewoodrich

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

Gemini 2.5 Pro made some big post-launch improvements for tool calling/agentic usage that made it go from “pulling teeth” to “almost as smooth as Claude” in Cline/Roo Code (which is saying something since Cline was originally built around Claude tool use specifically).

So the team at least seems to be aware of its shortcomings in that area and working to improve it with some success which I appreciate.But you are correct that Gemini CLI still lags behind for whatever reason. It gets stuck in endless thought loops way too often for me, like maybe 1/15 tasks hits a thought loop burning API credits or it just never exits from the “Completing task, Verifying completion, Reviewing completion, Assessing completion status…” phase (watching the comical number of ways it rephrases it is pretty funny though).Meanwhile I’ve only had maybe one loop over a period of a couple months using Gemini 2.5 Pro heavily in Roo Code with the most recent version so it seems like an issue with the CLI specifically.

reply

jjani

2 hours ago

 |
root
 |
parent
 |
next

[–]

Even just a week ago Gemini was still outputting the same message twice almost every time in Cline, I doubt that has changed in the last week.

reply

j45

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

Can anyone help compare a cost comparison between Gemini 2.5 pro vs Claude Code on a plan or API?

reply

Jcampuzano2

10 hours ago

 |
parent
 |
prev
 |
next

[–]

My opinion is all of these tools should completely get rid of the "pay 20/month, 200/month", etc just to get access to some beholden rate limited amount that becomes hard to track.

Mask off completely and just make it completely usage based for everyone. You could do something for trial users like first 20 (pick your number here) requests are free if you really need to in order to get people on board. Or you could do tiered pricing like first 20 free, next 200 for X rate, next 200 for X*1.25 rate, and then for really high usage users charge the full cost to make up for their extreme patterns. With this they can still subsidize for the people who stay lower on usage rates for market share. Of course you can replace 200 requests with just token usage if that makes sense but I'm sure they can do the math to make it work with request limits if they work hard enough.Offer better than open-router pricing and that keeps people in your system instead of reaching for 3rd party tools.If your tool is that good, even with usage based it will get users. The issue is all the providers are both subsidizing users to get market share, but also trying to prohibit bad actors and the most egregious usage patterns. The only way this 100% becomes a non-issue is usage based for everything with no entry fee.But this also hurts some who pay a subscription but DONT use enough to account for the usage based fees. So some sales people probably don't like that option either. It also makes it easier for people to shop around instead of feeling stuck for a month or two since most people don't want multiple subs at once.

reply

vineyardmike

9 hours ago

 |
root
 |
parent
 |
next

[–]

> My opinion is all of these tools should completely get rid of the "pay 20/month, 200/month", etc just to get access.

I think that you should just subscribe to a preset allotment of tokens at a certain price, or a base tier with incremental usage costs for models that aren’t tiny (like paid per minute “long distance calling”).I use an LLM tool that shows the cost associated with each message/request and most are pennies each. There’s a point where the friction of paying is a disincentive to using it. Imagine you had to pay $0.01 every time you Google searched something? Most people would never use the product because trying to pay $0.30/mo for one day a month of usage is annoying. And no one would want to prepay and fund an account if you weren’t familiar with the product. No consumer likes micro transactionsNo one wants to hear this, but the answer is advertising and it will change the game of LLMs. Once you can subsidize the lowest end usage, the incentive for businesses to offer these $20 subscriptions will change, and they’d charge per-usage rates for commercial users.

reply

troupo

8 hours ago

 |
root
 |
parent
 |
next

[–]

> you should just subscribe to a preset allotment of tokens at a certain price

The problem is that there's no way to gauge or control token usage.I have no idea why Claude Code wrote that it consumed X tokens now, and Y tokens later, and what to do about it

reply

CodeBrad

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

I think Claude Code also already has the option to provide an API key directly for usage based pricing.

I'm a fan of having both a subscription and a usage based plan available. The subscription is effectively a built in spending limit. If I regularly hit it and need more value, I can switch to an API key for unlimited usage.The downside is you are potentially paying for something you don't use, but that is the same for all subscription services.

reply

tqwhite

7 hours ago

 |
root
 |
parent
 |
next

[–]

I use API but think about getting the $100/mo plan and using API for overflow if it occurs.

But I have slow months and think that might not actually be the winner. Basically I'm going to wait and see before I sign up for auto-pay.

reply

raincole

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

Giving how expensive Claude Code is if you use API key, I think it's safe to assume the subscription model is bleeding money out.

reply

jononor

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

Investors love MRR/ARR, so I do not think we will see that as the main option anytime soon.
That said, you can use the Claude API to get usage-based billing.

reply

bananapub

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

> Mask off completely and just make it completely usage based for everyone.

you can already pay per token by giving Claude Code an API key, if you want.thus, the subtext of every complaint on this thread is thatpeople want "unlimited" and they want their particular use to be under whatever the cap is, and they want it to be cheap.

reply

Wowfunhappy

5 hours ago

 |
root
 |
parent
 |
next

[–]

No, I'm explicitly
not
 saying that! I'm saying that I'd really like the rolling window to be less than a full week, because that's such a long time to wait if I exhaust the limit!

reply

thorum

10 hours ago

 |
parent
 |
prev
 |
next

[–]

The long term is unlimited access to local LLMs that are better than 2025’s best cloud models and good enough for 99% of your needs, and limited access to cloud models for when you need to bring more intelligence to bear on a problem.

LLMs will become more efficient, GPUs, memory and storage will continue to become cheaper and more commonplace. We’re just in the awkward early days where things are still being figured out.

reply

pakitan

10 hours ago

 |
root
 |
parent
 |
next

[–]

I'm often using LLMs for stuff that requires recent data. No way I'm running a web crawler in addition to my local LLM. For coding it could theoretically work as you don't always need latest and greatest but would still make me anxious.

reply

data-ottawa

9 hours ago

 |
root
 |
parent
 |
next

[–]

That’s a perfect use case with MCP though.

My biggest issue is local models I can run on my m1/m4 mbp are not smart enough to use tools consistently, and the context windows are too small for iterative uses.The last year has seen a lot of improvement in small models though (gemma 3n is fantastic), so hopefully it’s only a matter of time.

reply

qiller

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm ok using a limited resource _if_ I know how much of it I am using. The lack of visible progress towards limits is annoying.

reply

steveklabnik

10 hours ago

 |
root
 |
parent
 |
next

[–]

npx ccusage@latest

I'm assuming it'll get updated to include these windows as well. Pass in "blocks --live" to get a live dashboard!

reply

data-ottawa

10 hours ago

 |
root
 |
parent
 |
next

[–]

Oh wow, this showed me the usage stats for the period before ccusage was installed, that’s very helpful especially considering this change.

ETA: You don’t need to authenticate or share your login with this utility, basically zero setup.

reply

mtmail

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

Package page (with screenshot)
https://www.npmjs.com/package/ccusage

reply

bravura

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

Does ccusage (or claude code with subscription) actually tell you what the limits are or how close you are too them?

reply

steveklabnik

10 hours ago

 |
root
 |
parent
 |
next

[–]

https://ccusage.com/guide/live-monitoring

See that screenshot. It certainly shows you when your 5 hour session is set to refresh, in my understanding it also attempts to show you how you're doing with other limits via projection.

reply

blalezarian

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

Totally agree with this. I live in constant anxiety not knowing how far into my usage I am in all the time.

reply

flkiwi

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

It's not exactly the same thing, but imagine my complete surprise when, in the middle of a discussion with Copilot and without warning, it announced that the conversation had reached its length limit and I had to start a new one with absolutely no context from the current one. Copilot has many, many usability quirks, but that was the first that actually made me mad.

reply

jononor

9 hours ago

 |
root
 |
parent
 |
next

[–]

ChatGPT and Claude do the same. And I have noticed that model performance can often degrade a lot before such a hard limit. So even when not hitting the hard limit, splitting out to a new session can be useful.
Context management is the new prompt engineering...

reply

stronglikedan

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

The craziest thing to me is that it actually completely stopped you in your tracks instead of upselling you on the spot to continue.

reply

mvieira38

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

You can't really predict usage of output tokens, too, so this is especially concerning

reply

qiller

7 hours ago

 |
root
 |
parent
 |
next

[–]

Like when Claude suddenly decides it's not happy with a tiny one-off script and generates 20 refined versions :D

reply

andix

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I guess you need to get used to it. LLM token usage directly translates to energy consumption. There are also no flat fee electricity plans, it doesn't make any sense.

reply

idunnoboutthat

10 hours ago

 |
root
 |
parent
 |
next

[–]

that's true of everything on the internet.

reply

andix

10 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, but for most things it's not significant.

For example Stack Overflow used to handle all their traffic from 9 on-prem servers (not sure if this is still the case). Millions of daily users. Power consumption and hardware cost is completely insignificant in this case.LLM inference pricing is mostly driven by power consumption and hardware cost (which also takes a lot of power/heat to manufacture).

reply

Twirrim

10 hours ago

 |
root
 |
parent
 |
next

[–]

> For example Stack Overflow used to handle all their traffic from 9 on-prem servers (not sure if this is still the case). Millions of daily users. Power consumption and hardware cost is completely insignificant in this case.

They just finished their migration to the cloud, unracked their servers a few weeks agohttps://stackoverflow.blog/2025/07/16/the-great-unracking-sa...

reply

jononor

9 hours ago

 |
root
 |
parent
 |
next

[–]

Would have loved to get some more insights. Cost estimates, before and after, for example. But also if any architectural changes where needed, or what kind of other challenges and learnings they got from the migration.

reply

tracker1

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

An "AI" box with a few high end gpu/npu cards takes more energy in a 4u box than an entire rack of commodity hardware takes. It's not nearly comparible... meaning entirely new and expansive infrastructure costs to support the high energy. That also doesn't count the needs for really high bandwidth networking to these systems. Not to mention the insanely more expensive hardware costs.

The infrastructure and hardware costs are seriously more costly than typical internet apps and storage.

reply

jm4

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Blame the idiots who abused it. Like that guy who posted a video a couple weeks ago where he had like 6 instances going nonstop and he was controlling it with his voice. There was some other project posted recently that was queuing up requests so that you could hit the limits in every time block. I've seen reddit posts where people were looking for others to share team accounts. It's always the morons who ruin a good thing.

Unless/until I start having problems with limits, I'm willing to reserve judgment. On a max plan, I expect to be able to use it throughout my workday without hitting limits. Occasionally, I run a couple instances because I'm multitasking and those were the only times I would hit limits on the 5x plan. I can live with that. I don't hit limits on the 20x plan.

reply

jjani

2 hours ago

 |
root
 |
parent
 |
next

[–]

Such abusers are very rarely a whole 5% of accounts, almost certainly <=2%.

reply

NicuCalcea

7 hours ago

 |
parent
 |
prev
 |
next

[–]

> I really am not a fan of having to feel like I'm using a limited resource whenever I use an LLM

Well, it is a limited resource, I'm glad they're making that clear.

reply

hn_throwaway_99

6 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, this sentence "I really am not a fan of having to feel like I'm using a limited resource whenever I use an LLM" felt like "I'm not a fan of reality" to me.

Lots of things still have usage-based pricing (last I checked no gas stations are offering "all you can fill up" specials), and those things work out fine.

reply

NicuCalcea

6 hours ago

 |
root
 |
parent
 |
next

[–]

These subscriptions only work because lighter users subsidise heavier users, but I guess the really heavy users are such big outliers that the maths isn't working out for Anthropic. I'm really not liking this neo-rentier capitalism we find ourselves in.

reply

xtracto

7 hours ago

 |
parent
 |
prev
 |
next

[–]

This is actually so fascinating to me. I remember when we had metered & very expensive long distance calls, "metered" dial-up Internet (Todito Card!), then capped DSL internet, then metered Mobile calls, SMSs and then Metered Mobile internet (that last one we still do).

The stuff that we do now, my 13 year old self in 1994 would never dream of! When I dialed my 33.6kbps modem and left it going the whole night, to download an mp3.It's exciting that nowadays we complain about Intelligent Agents bandwidth plans!! Can you imagine! I cannot imagine the stuff that will be built when this tech has the same availability as The Internet, or POTS!

reply

WD-42

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Try running one locally and observe as the temperature in your office rises a few degrees and the lights dim with every prompt. I didn’t really get the pricing myself until I got a desktop to do local inference. There’s a reason why these companies want to build nuclear plants next to their data centers.

reply

furyofantares

10 hours ago

 |
parent
 |
prev
 |
next

[–]

The Sonnet usage does not really look limited at 240-480 hours per week (a week has 168 hours in it).

Opus at 24-40 looks pretty good too. A little hard to believe they aren't losing a bunch of money still if you're using those limits tbh.

reply

clharman

10 hours ago

 |
root
 |
parent
 |
next

[–]

Pretty sure they are still losing money on it, which is great for us. And these limits wouldn't even be happening if there weren't people bragging about having their CC running constantly for 30 hours writing 2 million lines of (doubtless bad) code. And sharing accounts to try to get even MORE usage. It's all that swarm guy tbh and he's proud of it.

reply

wrs

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

You can run multiple instances of Claude Code at the same time.

reply

furyofantares

9 hours ago

 |
root
 |
parent
 |
next

[–]

I know, I do it all the time! I wasn't calling out 240 hours as being impossible to hit in 168 hour weeks. I suppose "does not really look limited" could be read multiple ways - I did not mean it's literally unlimited, just that it doesn't look very limited.

You can make your own comparison to however many hours you usually spend working in a week and how many sessions you have active on average during that time.

reply

j45

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

The calculation of hours is a little tough to imagine sometimes, is it the inference time itself, or the period of time used? Is there an average token cost per hour of use (average or explicit?)

reply

raincole

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Unlimited plans = the users who use it least subsidize the users who use it a lot.

I don't really know how it's sustainable for something like SOTA LLMs.

reply

belter

10 hours ago

 |
parent
 |
prev
 |
next

[–]

The real bottleneck isn’t Jevons paradox, it’s the Theory of Constraints. A human brain runs on under 20 W, yet every major LLM vendor is burning cash and running up against power supply limits.

If anything pops this bubble, it won’t be ethics panels or model tweaks but subscription prices finally reflecting those electricity bills.At that point, companies might rediscover the ROI of good old meat based AI.

reply

alwillis

7 hours ago

 |
root
 |
parent
 |
next

[–]

At that point, companies might rediscover the ROI of good old meat based AI.

That’s like saying when the price of gasoline gets too high, people will stop driving.Once a lifestyle is based on driving (like commuting from the suburbs to a job in the city), it’s quite difficult and in some cases, impossible without disrupting everything else.A gallon of gas is about 892% higher in 2025 than it was in 1970 (not adjusted for inflation) and yet most people in the US still drive.The benefits of LLMs are too numerous to put that genie back in the bottle.We’re at the original Mac (128K of RAM, 9-inch B&W screen, no hard drive) stage of LLMs as a mainstream product.

reply

belter

5 hours ago

 |
root
 |
parent
 |
next

[–]

> when the price of gasoline gets too high

People get electric cars or public transport....

reply

dotancohen

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

> good old meat based AI.NI, or really just I.Though some of us might fall into the NS category instead.

reply

TeMPOraL

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

Where is this oft-repeated idea coming from? Inference isn't
that
 expensive.

reply

belter

7 hours ago

 |
root
 |
parent
 |
next

[–]

My back of envelope estimate, is that even a partly restricted plan, would need to cost roughly $4,000–$4,500 per month just to break even.

reply

margalabargala

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

Meat has far higher input requirements for good performance above raw energy

reply

hkt

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

I suspect for this reason we are going to see a lot of attempts at applied AI: I saw an article semi-recently about an AI weather forecasting model using considerably less power than it's algorithmic predecessor, for instance. The answer is, as ever, to climb the value chain and make every penny (and joule) count.

reply

gedy

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I get it, and feel the same way but the current LLMs are very resource intensive. To the point that I'm reluctant to go all in on these tools if in future we get rug-pulled once companies admit "okay, this was not sustainable at that price.."

reply

andix

10 hours ago

 |
root
 |
parent
 |
next

[–]

Some people claim we already reached peak-LLM. It's cheap and powerful right now, in the future it might just get more expensive, or worse quality for the same price.

reply

sergiotapia

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Think of an insane number of requests. Now 20x it, that's what the top 1% of Claude users are at. Just fleecing the service dry. hard problem, what else could Claude do tbh

reply

handfuloflight

10 hours ago

 |
root
 |
parent
 |
next

[–]

...maybe use their superintelligent AI to come up with a solution that specifically targets the abusers?

reply

SatvikBeri

10 hours ago

 |
root
 |
parent
 |
next

[–]

...like adding limits that only affect a small fraction of users?

reply

Yossarrian22

10 hours ago

 |
root
 |
parent
 |
next

[–]

Is 1/20 small?

reply

dotancohen

10 hours ago

 |
root
 |
parent
 |
next

[–]

I'm Jewish. We take that right off the top shortly after birth.

reply

dom96

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

Easy, they just gotta hit up the AI on each request with a prompt like "You are an AI that detects abuse, if this request is abusive block it" /s

reply

blitzar

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

Claude says - The key is maintaining user agency—let them choose how to manage their usage rather than imposing arbitrary cutoffs.

It suggests:Transparent queueing - Instead of blocking, queue requests with clear wait time estimates. Users can choose to wait or reschedule.Usage smoothing - Soft caps with gradually increasing response times (e.g., 2s → 5s → 10s) rather than hard cutoffs.Declared priority queues - Let users specify request urgency. Background tasks get lower priority but aren't blocked.Time-based scheduling - Allow users to schedule non-urgent work during off-peak hours at standard rates.Burst credits - Banking system where users accumulate credits during low usage periods for occasional heavy use.

reply

volleygman180

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Agreed. The internet would be livid if Apple Music or Hulu limited how many hours you were allowed to stream per week. Especially the users who pay for the top-tier packages that include 4K (or lossless for music), extra channel add-ons, etc.

reply

beepbooptheory

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm sure people hate this mindset here, but any time I use an LLM I just picture the thousands of fans spinning, the heat of the datacenter... I treat each prompt like a painful interval where I am leaving my door open on a hot day.

I know nobody else really cares.. In some ways I wishIdidn't think like this.. But its at this point not even an ethical thing, its just a weird fixation. Like I can't help but feel we are all using ovens when we would be fine with a toasters.

reply

vlan0

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Do you wonder why that feeling arising inside of you?

reply

strictnein

10 hours ago

 |
prev
 |
next

[–]

Confused on the Max 5x vs Max 20x. I'm on the latter, and in my email it says:

> "Most Max 20x users can expect 240-480 hours of Sonnet 4 and 24-40 hours of Opus 4 within their weekly rate limits."In this post it says:> "Most Max 5x users can expect 140-280 hours of Sonnet 4 and 15-35 hours of Opus 4 within their weekly rate limits."How is the "Max 20x" only an additional 5-9 hours of Opus 4, and not 4x that of "Max 5x"? At least I'd expect a doubling, since I'm paying twice as much.

reply

thomasfromcdnjs

6 hours ago

 |
parent
 |
next

[–]

Would love more feedback on this, I will definitely downgrade from Max 20x if it is the case. Cost me $350 a month in Australia...

reply

ImaCake

1 hour ago

 |
parent
 |
prev
 |
next

[–]

The ambiguity here is awful marketing practice. This bitter pill would be much easier to swallow if it was a hard number instead of these vague ranges. It would serve Anthropic better too - telling people they only get 300hrs vs between 240-480 (which they will naturally evaluate as 240hrs) will mean less users leaving the platform.

reply

dawnerd

1 hour ago

 |
parent
 |
prev
 |
next

[–]

They really need to to just a limit so you can see how much you've used, not some vague hours per week or whatever. Github copilot will tell you, you have 300 requests with sonnet a month, makes it really easy to know when you're blowing past without having to worry about how long something has run.

reply

akmarinov

9 hours ago

 |
parent
 |
prev
 |
next

[–]

I upgraded to 20x because i was constantly running against Opus limits and now it seems the 20x is almost equal to the 5x in that regard

reply

lvl155

9 hours ago

 |
parent
 |
prev
 |
next

[–]

This is why I stopped using the MAX. Downgraded to Pro and started using o3 and others via API. I really don’t need that many hours to game plan in the beginning. At most it will cost me $10 between o3, Gemini, and Opus per project. There are new model releases every couple of weeks and I’d hate to get stuck with just one provider.

reply

yobid20

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Someone should do a study then file a class action if their marketing material is false.

reply

gabriel666smith

3 hours ago

 |
root
 |
parent
 |
next

[–]

I've been tracking usage in my first month of "20x" Max (which was, unfortunately, this month). Depending on how this usage is amortised (working days, which is what matters to me, or 5 hour periods, or I guess, now weeks..?) their marketing material has been varying degrees of false. This has ranged from 'a bit false' to 'extremely false'.

That is true both on a relative scale ("20x") compared to my previous use of the $20 plan, but - more dishonestly, in my opinion - absolutely false when comparing my (minimal, single-session, tiny codebase) usage to the approximate usage numbers quoted in the marketing materials. The actual usage provided has regularly been 10% of the quoted allowance before caps are hit.I have had responses from their CS team, having pointed this out, in the hope they would _at least_ flag to users times that usage limits are dramatically lower so that I can plan my working day a little better. I haven't received any sort of acknowledgement of the mismatch between marketing copy and delivered product, beyond promised "future fixes". I have, of course, pointed out that promised and hypothetical future fixes do not have any bearing on a period of paid usage that exists in the past. No dice!I'm, unfortunately, a UK customer, and from my research any sort of recourse is pretty limited. But it has - without question - been one of the least pleasant customer experiences I've had with a company in some time, even allowing for Anthropic experiencing extremely high-growth.Claude Code Router has been a Godsend for my usage level. I'm not sure I can justify the time and effort to care and pursue Anthropic's functional bait-and-switch offering more than I already have, because being annoyed about things doesn't make me happy.But I completely second this: it's not acceptable to sell customers a certain amount of a thing - then and deliver another - and I hope US customers (who I believe should have more recourse) take action. There are few other industries where "it's a language and compute black box!" would be a reasonable defence, and I think it sets a really bad precedent going forward for LLM providers.One might imagine that Anthropic's recent ~$200m US gov contract (iirc) might allow for a bit of spare cash to, for example, provide customers with the product they paid for (let alone refund them, where necessary) but that does not seem to be the case.It makes me sad to see a great product undermined like this, which is, I think, a feeling lots of people share. If anyone is actually working towards wider recourse, and would find my (UK) usage data useful, they're very welcome to get in touch.

reply

foota

9 hours ago

 |
parent
 |
prev
 |
next

[–]

You're paying for prioritization during high traffic periods, not for 2x usage.

reply

strictnein

9 hours ago

 |
root
 |
parent
 |
next

[–]

That's not what they claim:

https://www.anthropic.com/pricing> Max
 > Choose 5x or 20x more usage per session than Pro*
 > Higher output limits for all tasks
 > Priority access at high traffic timesThat first bullet pretty clearly implies 4x the usage and the last one implies that Max gets priority over Pro, not that 20x gets priority over 5x.

reply

foota

7 hours ago

 |
root
 |
parent
 |
next

[–]

That is sort of what it implies, but I don't think that's what's actually happening on the backend. I was looking at this yesterday though and I agree that it's all a bit hand-wavy. I feel for them somewhat though because it's hand-wavy because it's a difficult problem to solve. They're essentially offering spot instances.

reply

jjani

18 minutes ago

 |
root
 |
parent
 |
next

[–]

Or go here:
https://claude.ai/upgrade/max
. What does it say on top, on the actual pricing page?

Max plan5x more usage than Pro
$100.00/month + taxSave 50%
20x more usage than Pro
$200.00/month + taxEspecially with the "save 50%", if they're not actually offering 4x that of 5x, that's easily illegal false advertising in half the territories Anthropic's customers are located in.

reply

foota

7 minutes ago

 |
root
 |
parent
 |
next

[–]

I want to say again that I don't think their plan pricing is straightforward, but (at least when I was looking at it the other day) I came away with the (correct, imo) impression that the 5x and 20x were just marketing terms and I should take it with a grain of salt. I agree it's not literally what it sounds like.

I think the disconnect here is that the 5x or 20x is true within a single session (and you'll see their website seems to always say this, clearly their legal team went over it with a fine tooth comb). The above about weekly quotas etc., isn't within a single session so the 5 or 20x no longer applies.

reply

jjani

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

It's not "sort of what it implies" - it's literally what it says.

> Choose 5x or 20x more usage per session than Pro*If a recruiter tells you you'll be getting "20x more money per hour" at this new startup, and you go there and you get only 6x, you're going to have a very different tone than "you sort of implied 20x".

reply

buzzerbetrayed

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

Some say hand wavy where others say dishonest. You’re justifying their dishonesty because telling the truth would cost them customers.

Gross.

reply

serf

11 hours ago

 |
prev
 |
next

[–]

200 bucks a month isn't enough. Fine. Make a plan that
is
 enough so that I will be left alone about time limits and enforced breaks.

NOTHINGbreaks flow better than "Woops! Times up!"; it's worse than credit quotas -- at least then I can make a conscious decision to spend more money or not towards the project.This whole 'twiddle your thumbs for 5 hours while the gpus cool off' concept isn't productive for me.'35 hours' is absolutely nothing when you spawn lots of agents, and the damn thing is built to support that behavior.

reply

Aurornis

9 hours ago

 |
parent
 |
next

[–]

> '35 hours' is absolutely nothing when you spawn lots of agents, and the damn thing is built to support that behavior.

I wouldn't call "spawning a lot of agents" to be a typical use case of the personal plan.That was always in the domain of switching to a pay as you go API. It's nice that they allowed it on the fixed rate plans, but those plans were always advertised ashigherlimits, not unlimited.

reply

nojs

8 hours ago

 |
root
 |
parent
 |
next

[–]

It’s literally recommended in “Best practices”:
https://www.anthropic.com/engineering/claude-code-best-pract...

reply

ankit219

10 hours ago

 |
parent
 |
prev
 |
next

[–]

API has fewer limits, and practically limitless. Claude is also on Aws and gcp, where you get more quotas (probably credits as well) and different rate limits.

reply

AstroBen

2 hours ago

 |
parent
 |
prev
 |
next

[–]

It's quite possible changing plans to something that's enough to make them profitable would push everyone to a competitor

Slowly bringing up prices as people get dependent sounds like a pretty decent strategy if they have the money to burn

reply

samrus

2 hours ago

 |
root
 |
parent
 |
next

[–]

Changing plans? They could just keep the old plans and add a new one, like OAIs 2k/month plan

reply

ChadMoran

9 hours ago

 |
parent
 |
prev
 |
next

[–]

This. Optimize for the good actors, not the bad ones.

reply

chomp

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Just use the API

reply

wahnfrieden

2 hours ago

 |
root
 |
parent
 |
next

[–]

Just buy multiple Max subscriptions.

reply

whalesalad

5 hours ago

 |
parent
 |
prev
 |
next

[–]

I use the API. Just pay-per-use. Refill it $100 at a time.

reply

nojito

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Use the API.

reply

strictnein

10 hours ago

 |
root
 |
parent
 |
next

[–]

The API is far more expensive. For Opus 4 it's almost priced in a way that says "don't use this".

reply

chomp

10 hours ago

 |
root
 |
parent
 |
next

[–]

That’s not what the parent commenter asked though, they wanted a price for not being concerned about limits. The API pricing is that.

reply

johnpaulkiser

10 hours ago

 |
root
 |
parent
 |
next

[–]

I doubts thats what they want. They want a static fixed price, $5k a month for example and never have to think about it.

reply

qeternity

9 hours ago

 |
root
 |
parent
 |
next

[–]

Take the API and assume 24/7 usage (or whatever working hours are). That’s your fixed cost.

It’s more likely that this sum is higher than they want. So really it’s not about predictability.

reply

paxys

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

Even if you used the API 24x7 for a single session (no parallel requests) I doubt you'd be able to hit $5k/mo in usage for Claude 4 Sonnet.

reply

awestroke

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

I use Claude Code authenticated via the API (Anthropic Console). There's no limits for me. And I also assume API-metered requests are prioritized, so it's faster as well.

reply

data-ottawa

9 hours ago

 |
root
 |
parent
 |
next

[–]

The API does have limits but they’re determined by your monthly spend. I did a trial of tier 1 spend and did hit the limits, but on on tier two spending it was much much better.

https://docs.anthropic.com/en/api/rate-limits#requirements-t...

reply

porridgebrain

10 hours ago

 |
parent
 |
prev
 |
next

[4 more]

[flagged]
tough

10 hours ago

 |
root
 |
parent
 |
next

[–]

Or just use any other CLI and API provider and let Anthropic hang with their -alignment- and selling out to warmongers

actually you can keep using claude code (cli) tool with any provider, just replace the env endpoints.https://github.com/musistudio/claude-code-router

reply

garciasn

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

I know how to program; I just don’t have the time to do it all and my company doesn’t have the revenue to support more devs. So; this is the best way to make do with what I have.

reply

steve_adams_86

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

What if they're using it to help them learn to program? There are plenty of valid uses people might have. And ultimately, it's their call, right? Capitalism and all that. I suppose the argument then is "just use the API", and sure, that's a solution. Yet it's odd to have an expensive subscription that's heavily rate limited like this.

It's a non-issue for me. When I hit the limit, which is rare, I go back to analog life where I use my head's brain to do the heavy lifting and that has all kinds of perks that Claude doesn't have. I get why people are frustrated, though.

reply

alwillis

10 hours ago

 |
prev
 |
next

[–]

From Anthropic’s Reddit account:

One user consumed tens of thousands in model usage on a $200 plan. Though we're developing solutions for these advanced use cases, our new rate limits will ensure a more equitable experience for all users while also preventing policy violations like account sharing and reselling access.This is why we can’t have nice things.

reply

Aurornis

9 hours ago

 |
parent
 |
next

[–]

I worked at a startup that offered an unlimited option.

It's amazing how fast you go from thinking nobody could ever use that much of your service to discovering how many of your users are creatively abusing the service.Accounts will start using your service 24/7 with their request rating coming at 95% of your rate limiter setting. They're accessing it from a diverse set of IPs. Depending on the type of service and privacy guarantees you might not be able to see exactly what they're doing, but it's clearly not the human usage pattern you intended.At first you think you can absorb the outliers. Then they start multiplying. You suspect batches of accounts are actually other companies load-splitting their workload across several accounts to stay under your rate limits.Then someone shows a chart of average profit or loss per user, and there's a giant island of these users deep into the loss end of the spectrum consuming dollar amounts approaching the theoretical maximum. So the policy changes. You lose those 'customers' while 90+% of your normal users are unaffected. The rest of the people might experience better performance, lower latencies, or other benefits because the service isn't being bombarded by requests all day long.Basically every startup with high usage limits goes through this.

reply

SlowTao

28 minutes ago

 |
root
 |
parent
 |
next

[–]

Not only startups, when OneDrive (was still SkyDrive at that point) started to offer unlimited online storage, from memory they said there was about 70 users that had over a petabyte of data each on the system.

Essentially people had all their security cameras and PVR units uploading endlessly to the cloud and Microsoft was footing the bill.Then the 1TB limit came in to stop that.

reply

0xbadcafebee

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

If you launch your service without knowing how much it costs to offer your service at the maximum rate it could be used, then this will definitely happen. Engineering directors need to require performance testing benchmarks and do the math to figure out where the ceiling is. If you happen to be "lucky" enough to scale very fast, you don't want to then bang your customer's heads repeatedly on a ceiling.

reply

tomwphillips

9 hours ago

 |
parent
 |
prev
 |
next

[–]

I think it might actually be because they're selling services at a loss.

reply

eldenring

8 hours ago

 |
parent
 |
prev
 |
next

[–]

I don't understand why the current setup for rate limits wouldn't be sufficient to stop this kind of thing.

reply

ookblah

46 minutes ago

 |
parent
 |
prev
 |
next

[–]

okay? why not just ban or create a special pricing for the 1% of less of users obviously abusing it. i get that they had to do this, but to frame it as some kind of community benefit is a little disingenuous. we know you're operating at a loss and trying to figure out a path forward.

pointing to the most extreme example as if you can't stop it in it's tracks is a bad argument. its like saying we will now restrict sending of emails for everyone because this one spammer was sending 1000x the amount of an avg or even power user when you should just be solving the actual problem (identifying and stopping those that disrupt).

reply

Tokumei-no-hito

9 hours ago

 |
parent
 |
prev
 |
next

[–]

guy was bragging about it on twitter yesterday. $13,200 of spend for his $200 account. he said he had like 4-5 opus only agents running nonstop and calling each other recursively.

clearly that's abusive and should be targeted. but in general idk how else any inference provider can handle this situation.cursor is fucked because they are a whole layer of premium above the at-cost of anthropic / openai etc. so everyone leaves goes to cc. now anthropic is in the same position but they can't cut any premium off.you can't practically put a dollar cap on monthly plans because they are self exposing. if you say 20/mo caps at 500/mo usage then that's the same as 480/500 (95%) discount against raw API call. that's obviously not sustainable.there's a real entitled chanting going on too. i get that it sucks to get used to something and have it taken away but does anyone understand that just the cap/opex alone is unsustainable let alone the RD to make the models and tools.I’m not really sure what can be done besides a constant churn of "fuck [whoever had to implement sustainable pricing], i'm going to [next co who wants to subsidize temporarily in exchange for growth]".i think it's shitty the way it's playing out though. these cos should list these as trial periods and be up front about subsidizing. people can still use and enjoy the model(s) during the trial, and some / most will leave at the end, but at least you don't get the uproar.maybe it would go a long way to be fully transparent about the cap/op/rdex. nobody is expecting a charity, we understand you need a profit margin. but it turns it from the entitled "they're just being greedy" chanting to "ok that makes sense why i need to pay X to have 1+ tireless senior engineers on tap".

reply

const_cast

3 hours ago

 |
root
 |
parent
 |
next

[–]

> clearly that's abusive and should be targeted.

You can't abuse a company by buying their services and using them to their own terms and conditions. The T&C is already stacked against you, you're in a position of no leverage.The correct solution is what Anthropic is doing here - change the T&C so you can make money. If you offer unlimited stuff, people will use it... unlimitedly. So, don't let them call your bluff.

reply

Tokumei-no-hito

3 hours ago

 |
root
 |
parent
 |
next

[–]

we differ on the opinion that you can be abusive without breaking ToS. perhaps a charitable view is that this type of [abuse || acceptable use] helps lawyers stay employed so they can [eliminate exploitation of || more adequately describe] their ToS.

reply

const_cast

3 hours ago

 |
root
 |
parent
 |
next

[–]

IMO abuse requires an exercise of power. End-users have no power - they hold zero leverage over the contract, and they have zero room to negotiate. It's a fully take-it-or-leave-it deal, and pray they do not alter the deal further.

Because of that, IMO end-userscan'tabuse the contract, no matter how hard they try. It's not on them to do that, because they have zero control over the contract. It's a have-your-cake-and-eat-it-too problem.Anthropic simultaneously retains complete control of the contract, but they want to "outsource" responsibility for how it's used to their end-users. No... it's either one or the other. Either you're in complete control and therefore hold complete accountability, or you share accountability.

reply

Tokumei-no-hito

2 hours ago

 |
root
 |
parent
 |
next

[–]

it's not a court of law.

end users did have power. the power to use the service legitimately, even as a power user. two choices were possible, with the users given the power to decide:1. use it for an entire 8 hour workday with 1-2 agents at most - limited by a what a human could possibly entertain in terms of review and guidance.2. use for 24 hours a day, 7 days a week with recursive agents on full opus blast. no human review could even be possible with this much production. its the functional equivalent of one person managing a team of 10-20 cracked engineers on adderall that pump out code 24 hours a day.the former was the extreme of a power user with a practical deliverable. the latter is a circus whose sole purpose is to push the bounds and tweet about it.now the lawyers get some fresh work to do and everyone gets throttled. oh and that 2nd group? they'll be, and are, the loudest about how they've been "rug pulled just like cursor".

reply

Tokumei-no-hito

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

there's a famous quote that i think captures the spirit of what i'm trying to express

"you're not wrong, you're just an asshole" - the dude to walter.(no particular offense directed, the you here is of course the "royal you").

reply

const_cast

2 hours ago

 |
root
 |
parent
 |
next

[–]

I just fundamentally am resistant to calling the "little people" the assholes.

Look, in my view, Anthropic made a mistake. And that's okay, we all do.But I'm not going to let a multi-billion dollar company off the hook because some nobodies called them out on their bluff. No, Anthropic made the mistake, and now they're fixing it.Ultimately, this came out of greed - but not the greed of the little people. Anthropic chose aggressive pricing because, like all somewhat large corporations, they usually opt for cheating instead of winning by value. What I mean is, Anthropic didn't strive for The Best product, they instead used their capital as collateral to sell a service at loss to squeeze competitors, particularly small, non-incumbent ones.And, that's fine, it's a legitimate business strategy. Walmart does it, Amazon does it, whatever. But if that backfires, I don't care and I won't extend sympathy. Such a strategy isinherently risky. They gambled, people called their bluff, and now they're folding.

reply

Tokumei-no-hito

2 hours ago

 |
root
 |
parent
 |
next

[–]

i get it, fuck the "man" and so forth.

I’m not suggesting you be sympathetic to anthropic. I’m suggesting sympathy for people who were using it legitimately, such as myself and others in areas where $200/mo is an extraordinary commitment, and we're not blind but appreciative to their subsidizing the cost.the core of my position is, was it necessary for people to use it wastefully because they could? what was gained from that activity? sticking it to that greedy corporation? did it outweigh what was lost to the other 95%+ of users?i don't think we're debating from compatible viewpoints. i maintain it's not wrong, just abusive. you maintain it's not wrong, it is [was] allowed. so be it.the party's over anyways. the result is an acceleration on the path of normalizing the true cost of usage and it's clear that will unfortunately, or maybe justifiably in your eyes, exclude a lot of people who can't afford it. cheers man.

reply

Aurornis

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

> guy was bragging about it on twitter yesterday. $13,200 of spend for his $200 account. he said he had like 4-5 opus only agents running nonstop and calling each other recursively.

Do you have a link?I'm always curious to see these users after working at a startup that was the target of some creative use from some outlier customers.

reply

Tokumei-no-hito

2 hours ago

 |
root
 |
parent
 |
next

[–]

sorry i went looking but couldn't find it. asked grok to search too. it wasn't creative use imo, it was extremism for the sake of attention since as far as i could tell they weren't producing anything (i'm sure they would have told everyone). although to be fair, the recursive opus chaining could be considered creative but only if it had a practical application.

not the tweet but here's a leaderboard of claude clowns bragging about their spend. maybe you can find their handles and ask them what MRR they hit spending $500k (not a typo) in credits.https://www.viberank.app/

reply

what

1 hour ago

 |
root
 |
parent
 |
next

[–]

There’s zero chance the top rankings are real. 13B tokens in two days?

reply

jjmarr

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

If VCs want to give me free money in exchange for using their product, do you expect me to say no?

reply

Tokumei-no-hito

2 hours ago

 |
root
 |
parent
 |
next

[–]

of course not. the buffet said all you can eat, didn't it? i don't expect you to do anything less but engorge your body to the point of hospitalization while 95% of the remaining customers look in horror.

reply

xdennis

31 minutes ago

 |
parent
 |
prev
 |
next

[–]

>> preventing policy violations like account sharing and reselling access.

> This is why we can’t have nice things.We're living in the worst world that Stallman could have predicted. One in which even HN agrees that people shouldn't be allowed to share or resell what they pay for.

reply

jjcm

11 hours ago

 |
prev
 |
next

[–]

They need metered billing for their plans.

All AI companies are hitting the same thing and dealing with the same play - they don't want users to think about cost when they're prompting, so they offer high cost flat fee plans.The reality is though there will always be a cohort of absolute power users who will push the limits of those flat fee plans to the logical extremes. Startups like Terragon are specifically engineered to help you optimize your plan usage. This causes a cat and mouse game where they have to keep lowering limits as people work around them, which often results in people thinking about price more, not less.Cursor has adjusted their limits several times, now Anthropic is, others will soon follow as they decide to stop subsidizing the 10% of extreme power users.Just offer metered plans that let me use the web interface.

reply

paxys

11 hours ago

 |
parent
 |
next

[–]

The API exists. You can generate a token and use Claude Code with it directly, no plan needed.

reply

tough

11 hours ago

 |
root
 |
parent
 |
next

[–]

then why sell fake -unlimited- plans to hook people up

It lasted less than a week -unlimited- been a shit show cutting down since then

reply

paxys

10 hours ago

 |
root
 |
parent
 |
next

[–]

If 95% of users are under the limit then it isn't a "fake" plan.

reply

Dylan16807

9 hours ago

 |
root
 |
parent
 |
next

[–]

That really depends. Like, if Opus can't make it through a full work week then at least for Opus the unlimited is pretty darn fake even if 95% of people are under that.

I'm reminded of online storage plans with various levels of "unlimited" messaging around them that can't even hold a single medium to large hard drive of data. Very few users hit that, most of whom don't even have a hard drive they regularly use, but it means they shouldn't be going anywhere near the word "unlimited".

reply

paxys

8 hours ago

 |
root
 |
parent
 |
next

[–]

They never advertised "unlimited", just higher limits

reply

tough

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

fake for 5% of users.

will they refund me my sub?when I subbed It was unlimited, they've rugged the terms twice already since then in less than a month

reply

paxys

10 hours ago

 |
root
 |
parent
 |
next

[–]

> Starting August 28

Read the announcement. You are getting a full month's notice. If you don't like the limits, don't renew your subscription. Of course that doesn't help if your primary goal is to be an online outrage culture warrior.

reply

geodel

9 hours ago

 |
root
 |
parent
 |
next

[–]

True. If it were easy to pirate these warriors would be claiming policy change as reason to pirate.

reply

Aurornis

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

> when I subbed It was unlimited,

Where did you see unlimited usage? The Max plan was always advertised as higher limits, not unlimited usage.

reply

Tokumei-no-hito

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

you were rugged? you sincerely expected you could run parallel opus agents 24/7 for $200/mo? who did the rugging here? did it occur to you that paying $7/day for a 24/7 team of dedicated senior engineers, roughly being paid 30 cents an hour, was not sustainable?

yes it was unlimited. so is the public water fountain. but if you show up and hold the button down to run nonstop while chanting "it says unlimited free water doesn't it??" you must expect that it will no longer be unlimited.we went from reasonably unlimited, which 95% of users enjoyed, respected and recognized was subsidized, to no unlimited anymore because 5% wanted to abuse it. now you can scream about being rugged, just like you did for cursor, and jump to the next subsidized provider that you can abuse until there's none left. you do realize that every time "unlimited" gets abused it raises the standard of limits and pricing across the board until it becomes normalized. this was going to happen anyways on a longer timeframe where providers could optimize inference and models over time so the change wasn't so shocking, but abuse accelerated it.

reply

Aurornis

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

They never advertised the plan as unlimited Opus usage, as far as I know.

reply

bravesoul2

7 hours ago

 |
parent
 |
prev
 |
next

[–]

It's 1990s shared hosting again!

reply

richwater

10 hours ago

 |
parent
 |
prev
 |
next

[–]

> Just offer metered plans that let me use the web interface.

The problem is this would reveal how expensive it _actually_ is to service interference right now at the scale that people use it for productive things.

reply

throwdbaaway

6 hours ago

 |
root
 |
parent
 |
next

[–]

Another problem is that it works like a slot machine -- sometimes the code is good, most of the time the code is mediocre and full of bugs.

Last Friday I spent about $15 in 1 hour using claude code with API key, and the code doesn't really work, even though all the unit tests passed. I am not going to touch it for weeks, while the loss is fresh in my mind.With a subscription though, you can keep on gambling, until you get a hit.

reply

OtherShrezzing

8 hours ago

 |
prev
 |
next

[–]

This email could have been a lot more helpful if it read “in the following months, your account entered one of these rate limits: Aug 2024, Jan 2025, May 2025” or similar.

I have no idea if I’m in the top 5% of users. Top 1% seems sensible to rate limit, but top 5% at most SaaS businesses is the entire daily-active-users pool.

reply

rstupek

11 hours ago

 |
prev
 |
next

[–]

"... and advanced usage patterns like running Claude 24/7 in the background" this is why we can't have nice things

reply

serial_dev

11 hours ago

 |
parent
 |
next

[–]

All of these AI services tell everyone how amazing AI is, it can run things, solve things on its own, while the developers are drinking coffee or sleeping. Some developers could actually do that with the service they paid for, fully in agreement with the terms and now it is their fault?

reply

OtherShrezzing

8 hours ago

 |
root
 |
parent
 |
next

[–]

Anthropic put out a press release over the weekend describing the internal team’s hints and tips to make CC useful. The 2nd tip was “run it in a bunch of different features at once”.

reply

furyofantares

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

Many such people have been in HN threads bragging about having servers running 24/7 and how they're getting $10,000 worth of compute (based on API pricing) for $200 per month. If anyone doing that is surprised that it wasn't going to last, then lmfao.

reply

ohdeargodno

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

"they paid for"

$100 doesn't even cover the electricity of running the servers every night, they were abusing a service and now everyone suffers because of them.

reply

serial_dev

10 hours ago

 |
root
 |
parent
 |
next

[–]

It is still not the users fault, pricing is not their responsibility. As a user, I check the price and what the service offers, then I subscribe and I use it. If these users did something illegal or breaking some conditions, any service would be free to block them. But they didn’t, meaning the AI tools promised too much for the price so they update their conditions, they are basically figuring out the pricing.

I don’t know what is there to be mad about, and using dramatic language like “everyone suffers because of them”

reply

currymj

9 hours ago

 |
root
 |
parent
 |
next

[–]

a lot of "all you can eat" restaurants have to charge extra for uneaten food. there are people who just enjoy the feeling of abundance they get from paying a flat fee and then wasting something.

This is clearly what was happening with the most extreme Claude Code users, because it's not actually that smart yet and still requires a human to often be in the loop.However, Anthropic can't really identify "wasted code".

reply

jedberg

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

Tragedy of the commons. You are totally right, they didn't violate any policy. But they violated their moral obligation to not abuse a shared resource.

reply

const_cast

3 hours ago

 |
root
 |
parent
 |
next

[–]

It's not a public good - these people weren't shitting in the park. It's a paid-for service and they were paying customers, getting their money's worth.

The price simply did not reflect the cost, and that's a problem. It happens to a lot of business and sometimes consumer's call their bluff. Whoops.You wanna cheat and undercut competitors by shooting yourself in the foot with costs that exceed price? Fine. It's a tale as old as time. Here, have your loss lead - xoxo, every consumer.Just charge per unit.

reply

jedberg

3 hours ago

 |
root
 |
parent
 |
next

[–]

I never said it was a public good. I said it was a shared resource.

The tragedy of the commons is the concept that, if many people enjoy unfettered access to a finite, valuable resource, such as a GPU farm, they will tend to overuse it and may end up destroying its value altogether.That is exactly what happened here. The price was fine if everyone upheld their moral obligation not to abuse it.

reply

const_cast

3 hours ago

 |
root
 |
parent
 |
next

[–]

There is no moral obligation, only the terms and conditions. That's your actual obligation.

There's only one person who made a mistake here - Anthropic. They purposefully make their terms and conditions bad, and then when people played by the contractthey set forth, they lost money. It's calling a bluff.Anthropic purposefully priced this far too aggressively to undercut their competitors. Companies with stupid amounts of investor capital do that all the time. They flew too close to the sun.You can't create a contract, have all the power in the world to rig the contract in your favor, and then complain about said contract. Everyone was following the rules. The problem was the rules were stupid.To be more specific - abuse requires an exercise of power. End-users have no power at all. They have literally zero leverage over the contract and they have no power to negotiate. They can't abuse anything, they're too weak.

reply

48terry

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

Just in case everybody in this comment tree forgot: Claude is not some common, public good. It barely even qualifies as a digital commons, if it does. It is a private tool owned by a private, for-profit company. Nobody has a common obligation to make Anthropic profitable or to reduce its expenses.

reply

jedberg

3 hours ago

 |
root
 |
parent
 |
next

[–]

I never said anything about a public good. See my sibling comment.

reply

48terry

2 hours ago

 |
root
 |
parent
 |
next

[–]

The "finite, valuable resource" in this case being "something a private company is actively trying to produce and pocket wealth with".

Again, there is no moral obligation to ensure Anthropic's business goes well and conveniently.

reply

Tokumei-no-hito

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

depends on your view of collectivist vs individualistic.

if your actions are defined by legal ToS then no, they didn't do anything wrong. they paid, it's the company's fault for not expecting someone to use 50-100x a reasonable usage.if your actions are defined by ethical use then you understood that 50-100x the use would inevitably lead to ruining the party for everyone.it's like a buffet. everyone pays a flat price and can enjoy a big meal for themselves. maybe sometimes having a few extra pieces of cake here and there. until someone shows up and starts stacking plates well beyond any reasonable expectation (not rule based) of a buffet customer. what's the result? stringent rules that are used for legal rather than rational enforcement.it's obvious that even "reasonable use" is being subsidized, and the company was okay with doing so. until we have people running 10 opus instances in a glutinous orchestra of agents just because they can. now the party is over. and i'd love to know what these claude agencies were even producing running 24/7 on opus. i can't imagine what human being even has the context to process what 24/7 teams of opus can put out. much like i can't imagine the buffet abuser actually enjoying the distending feast. but here we are.

reply

Aurornis

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

> I don’t know what is there to be mad about, and using dramatic language like “everyone suffers because of them”

Why are you assuming everyone will suffer?They backtested the new limits on usage data and found it will begin to impact less than 5% of users.

reply

Dylan16807

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

Any good numbers on what it costs? I can look up how many watts a GPU needs but I don't know how the batching is typically done to understand how many users are sharing those watts.

But a compute-focused datacenter is probably not paying more than 10 cents per kWh, so $100 would pay for more than a 24/7 kilowatt of GPU plus cooling plus other overhead.

reply

Modified3019

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Yeah that part made me laugh. Clearly the work of Benevolent World Exploders trying to hasten the heat death of the universe.

reply

taylorbuley

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I imagine this was not surprising. This had to have been well-considered by the teams in the first round of pricing. I'm guessing they just didn't want it to be a blocker for release and the implementation is now catching up.

reply

bad_haircut72

10 hours ago

 |
parent
 |
prev
 |
next

[–]

They set the pricing how is this even wrong - I will run my claude subscription non stop until they cut me off, I paid for it they should honor what they sold. And yes Im a max subscriber who still frequently hits limits

reply

volkk

11 hours ago

 |
parent
 |
prev
 |
next

[–]

i mean, this is exactly how price discovery works. if you give loose usage requirements, you'll have actors who take full advantage of it. not on the people using it but ultimately on the company that pretends they can sustain something like this, and then claw back the niceties

reply

404mm

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I got the same email (for my Pro account). And all the limits they set have nothing to do with their reason for setting them. Pro is so limited already that people “running 24/7” is a total nonsense.

reply

swalsh

10 hours ago

 |
prev
 |
next

[–]

That's fine, please make it VERY CLEAR how much of my limit is left, and how much i've used.

reply

loufe

9 hours ago

 |
parent
 |
next

[–]

Seriously. I still find it ridiculous that even after they upped Opus' limit from 60% to 80% they don't show usage % below that. It's sapping my ability to use it quickly on the 5x plan.

reply

0xbadcafebee

5 hours ago

 |
prev
 |
next

[–]

Possibly dumb suggestion, but what about adaptive limits?

Option 1: You start out bursting requests, and then slow them down gradually, and after a "cool-down period" they can burst again. This way users can still be productive for a short time without churning your servers, then take a break and come back.Option 2: "Data cap": like mobile providers, a certain number of high requests, and after that you're capped to a very slow rate, unless you pay for more. (this one makes you more money)Option 3: Infrastructure and network level adaptive limits. You can throttle process priority to de-prioritize certain non-GPU tasks (though I imagine the bulk of your processing is GPU?), and you can apply adaptive QoS rules to throttle network requests for certain streams. Another one might be different pools of servers (assuming you're using k8s or similar), and based on incoming request criteria, schedule the high-usage jobs to slower servers and prioritize faster shorter jobs to the faster servers.And aside from limits, it's worth spending a day tracing the most taxing requests to find whatever the least efficient code paths are and see if you can squash them with a small code or infra change. It's not unusual for there to be inefficient code that gives you tons of extra headroom once patched.

reply

steve_adams_86

11 hours ago

 |
prev
 |
next

[–]

I'm well within the 95%. I might lack an imagination here, but... What are you guys doing that you hit or exceed limits so easily, and if you do... Why does it matter? Sometimes I'd like to continue exploring ideas with Claude, but once I hit the limit I make a mental note of the time it'll come back and carry on planning and speccing without it. That's fine. If anything, some time away from the slot machine often helps with ensuring I stay on course.

reply

throwup238

10 hours ago

 |
parent
 |
next

[–]

Opus + extended thinking + deep research = 3-5 messages/reports per five hour limit. That’s the fastest way I’ve found to blow through the Pro plan.

Some stuff I’ve used it for in the last day: figuring out what a family member needs for FAFSA as a nontraditional student, help identify and authenticate some rare first editions and incunabula for a museum collection I volunteer at, find a list of social events in my area (based on my preferences) that are coming up in the next week (Chatgpt Agent works surprisingly well for this too), adapting Directus and Medusa to my project’s existing schema and writing up everything I need to migrate, and so on.Deep research really hits the Claude limits hard and that’s the best way to avoid hallucinations when asking an important question or making it write complex code. I just switch from Claude to ChatGPT/Gemini until the limits reset but Claude’s deep research seems to handily beat Gemini (and OpenAI isnt even in the running). DR queries take much longer (5-10 min in average) but have much more in depth and accurate answers.

reply

steve_adams_86

10 hours ago

 |
root
 |
parent
 |
next

[–]

I hadn't considered that. I'm using it almost exclusively to validate logic, kind of like a fuzzer in nature ("What if we need to do this with this logic/someone tries to do that/what am I missing/etc"), or to fill in specifications ("what feature would compliment this/what could be trimmed to achieve MVP more easily/does this spec appear to be missing anything according to this set of requirements"), which requires a lot of review, and using more expensive models like Opus doesn't appear to provide meaningfully better results. After prompting it, I typically have a lot to think about and the terminal goes quiet, or I prompt it on a related matter that will similarly require my eyes and brain for long enough that I won't be able to limit out.

I can see how work involving larger contexts and deeper consideration would lead to exhausting limits a lot faster though, even if you aren't using it like a slot machine.

reply

theshrike79

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

"find a list of social events in my area"

Isn't this something you can do with a simple Google search? Or Perplexity?No need to shove by far the most expensive LLM (Claude Opus 4) at it.

reply

throwup238

10 hours ago

 |
root
 |
parent
 |
next

[–]

Not for the Los Angeles metro area. There isn’t a single calendar or event aggregator that covers the entire area and with an LLM I can give it complex schedules (i.e. a dump of my calendar for that week) and preferences to filter the list of events for the stuff I like, including vague stuff like “I like country music in the style of ‘Take Me Home, Country Roads’ but not modern country radio”.

reply

tkiolp4

7 hours ago

 |
root
 |
parent
 |
next

[–]

Killing a fly with a cannonball.

reply

throwup238

6 hours ago

 |
root
 |
parent
 |
next

[–]

Doesn’t really matter when the marginal cost of the cannonball is effectively zero - I’m already paying the monthly subscription.

Then not using the canonball is just a waste of time, which is a heck of a lot more valuable than some purist aversion to using LLMs to save time and effort.

reply

steve_adams_86

6 hours ago

 |
root
 |
parent
 |
next

[–]

One could argue this is like paying a subscription for gasoline and saying you better use it up or it's a waste. There's an externality at play.

I know LLMs aren't as much of an environmental scourge as people sometimes make them out to be, but if they're used eagerly and aggressively, their impacts certainly have a capability of scaling in concerning ways.

reply

xboxnolifes

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

Where is the fly swatter at?

reply

Zopieux

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

Gosh I so despise this new normal. Just when I thought I could fight bloat and unnecessary tech in my own tiny corner of the world, only for a few to ruin it with ridiculous LLM (ab)use.

reply

Terretta

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

When you say not even in the running, is that including Deep Research on o3-pro?

reply

throwup238

4 hours ago

 |
root
 |
parent
 |
next

[–]

I haven't tried o3-pro, but my fundamental problem with ChatGPT Deep Research is that it only searches for a few dozen sources, whereas Claude and Gemini regularly use 400+ sources.

reply

zarzavat

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I agree. I'm on the base plan, yet to hit any limits. The bottleneck is my ability to review the code it writes, and to write prompts detailed enough for the output to be useful to me.

I assume that the people hitting limits are just letting it cycle, but doesn't that just create garbage if you don't keep it on a tight leash? It's very eager but not always intelligent.

reply

loufe

9 hours ago

 |
root
 |
parent
 |
next

[–]

Switching to Opus is an eye-opening experience. You hit limits often, and need to get creative to avoid burning through limits, but the difference is seriously impressive. You'll waste a lot less time with dead ends and bad code.

reply

zarzavat

2 hours ago

 |
root
 |
parent
 |
next

[–]

The issue (with Sonnet, I'm not using Opus), is not always that the code is bad per se, but merely that it doesn't solve the problem in the way I expected.

I have two problems with that. Firstly, I want my code to be written a particular way, so if it's doing something out of left field then I have to reject it on stylistic grounds. Secondly, if its solution is too far from my expectation, I have to put more work into review to check that its solution is actually correct.So I give it a "where, what, how" prompt. For example, "In file X add feature Y by writing a function with signature f(x: t), and changing Z to do W..."It's very good at following directions, if you give it thehowhints to narrow the solution space.

reply

steve_adams_86

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

I think this is it. They use it like a slot machine, and when something isn't quite what they wanted, they provide broad instructions to refine and do better. Progress is slow and questionable, but anticipation and (sometimes) reward is increased.

The issue could be, in part, that a lot of users don't care to be efficient with token usage and maintaining condensed, efficient, focused contexts to work with.

reply

Tokumei-no-hito

9 hours ago

 |
root
 |
parent
 |
next

[–]

i wonder how many are negligent vs ignorant. negligence would be senior engineers that could scope and work with context properly but are lazy or don't care. ignorance would be vibe coders that genuinely can't express anything beyond plain english and superficial descriptions of issues and changes.

reply

mendor

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I've found that asking for deep research consumes my quota quite fast, so If I run 2 or 3 and normal use I hit the limit and have to wait to reset

reply

steve_adams_86

10 hours ago

 |
root
 |
parent
 |
next

[–]

Me too. I've also found that even when trying to restrict models meant for these tasks, they tend to go on tangents and waste tremendous amounts of tokens without providing meaningfully better outputs. I'm not yet sold on these models for anything outside of fuzzy tasks like "does this logic seem sound?". They tend to be good at that (though they often want to elaborate excessively or propose solutions excessively).

reply

SaucyWrong

10 hours ago

 |
parent
 |
prev
 |
next

[–]

One way I've seen personally is that folks are using tools that drive many Claude Code sessions at once via something like git-worktree as a way of multitasking in a single codebase. Even with garden-variety model use, these folks are hitting the existing 5-hourly rate limits routinely.

reply

steve_adams_86

10 hours ago

 |
root
 |
parent
 |
next

[–]

I use this approach because I like to work on features or logical components in isolation and then bring them together. I still can't limit out most of the time because I need to actually look at the outputs and think about what I'm building. At the moment I have 3 directories in my work tree. Sometimes I prompt in more than one at a time, especially at interfacing code, but that could mean 30–90 minutes of reviewing and implementing things in each directory. Over a work day I apparently send an average of ~40 messages according to `claude --resume`

reply

bad_haircut72

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Im not a formula 1 driver but why do they have those big padel things on the back? looks dumbo IMHO I just dont get it

reply

steve_adams_86

10 hours ago

 |
root
 |
parent
 |
next

[–]

I respectfully consider this analogy void, but welcome an explanation of why I'm wrong.

I haven't yet seen anyone doing anything remarkable with their extensive use of Claude. Without frequent human intervention, all of it looks like rapid regression to the mean, or worse.

reply

knowsuchagency

9 hours ago

 |
prev
 |
next

[–]

One feature I would love to have is the ability to switch the model used for a message using a shorthand like #sonnet. Often, I don't want or need opus but I don't want to engage in a 3 step process where I need to:

1. switch models using /model
2. message
3. switch back to opus using /modelHelp me help you (manage usage) by allowing me to submit something like "let's commit and push our changes to github #sonnet". Tasks like these rarely need opus-level intelligence and it comes up all the time.

reply

vunderba

9 hours ago

 |
parent
 |
next

[–]

Agreed. I was hoping that they would add this (model selection) to the template for defining subagents.

https://docs.anthropic.com/en/docs/claude-code/sub-agents

reply

gardnr

7 hours ago

 |
parent
 |
prev
 |
next

[–]

That would be great! I want to plan and analyze with opus but happy to use sonnet for code gen. Sonnet is faster and just as good at codegen. Opus is better at planning a change.

reply

manveerc

10 hours ago

 |
prev
 |
next

[–]

For most people, this is a tool we use daily. What’s the reasoning behind choosing a weekly usage limit instead of a daily one? Is it because the top 5 percent of users tend to have spiky usage on certain days, such as weekends? If that’s the case, has there been any consideration of offering different usage tiers for weekdays and weekends?

I’m just curious how this decision came about. In most cases, I’ve seen either daily or monthly limits, so the weekly model stood out.

reply

lucb1e

9 hours ago

 |
prev
 |
next

[–]

> affecting less than 5% of users

Probably phrased to sound like little but as someone used to seeing like 99% (or, conversely, 1% down) as a bad uptime affecting lots and lots of users, this feels massive. If you have half a million users (I have no idea, just a ballpark guess), then you're saying this will affect just shy of the25 thousand people that use your product the most. Oof!

reply

_boffin_

9 hours ago

 |
parent
 |
next

[–]

Reminds me of gym membership utilization rates. You have something like 50% not even going. A large % left only go a few times a month…. Yada yada

reply

lucb1e

9 hours ago

 |
root
 |
parent
 |
next

[–]

Exactly! And then you alienate the top 10% fans among the members that ever go (since 10% of those 50% is 5%). They must know this is terrible for the brand so I guess there is a real good financial reason for doing this

(Congrats on 777 karma btw :). No matter the absolute number on sites like these, I always still love hitting palindromes or round numbers or such myself)

reply

ripped_britches

12 minutes ago

 |
prev
 |
next

[–]

Everybody freaking out about this should just pay for API access like an adult

reply

sea-gold

11 hours ago

 |
prev
 |
next

[–]

Official Anthropic post on Reddit:
https://www.reddit.com/r/ClaudeAI/comments/1mbo1sb/updating_...

reply

codethief

9 hours ago

 |
parent
 |
next

[–]

Thanks, I had been wondering what the source was.

reply

slimebot80

2 hours ago

 |
prev
 |
next

[–]

Overall I think this is as positive - protecting the system from being hit heavily 24/7 and with multiple agents from some users might make the system more sustainable for a wider population of users.

This one thing that bugs me is the visibility of how far through your usage you are. Being told when you're close to the end means I cannot plan. I'm not expecting an exact %, but a few notices at intervals (eg: halfway through) would help a lot. Not providing this kinda makes me worry they don't want us to measure. (I don't want to closely measure, but I do want to have a sense of where I am at)

reply

raytopia

9 hours ago

 |
prev
 |
next

[–]

I was wondering when the free lunch for these tools was going to end. All the AI stuff has been incredibly subsidized by investors and it'll be interesting to see whay the real cost is going to be when companies like Anthropic and OpenAI need to make money.

reply

lucb1e

8 hours ago

 |
parent
 |
next

[–]

Wasn't it like 2$ in electricity for every 1$ they take in revenue at OpenAI? I think it was a Flemish podcast where they mentioned that such numbers had leaked (episode was recorded a month ago), hard to find back among a 2-hour podcast episode but as a ballpark figure

reply

nurettin

10 minutes ago

 |
prev
 |
next

[–]

I feel rug pull after rug pull ($10->$20, hourly quotas, weekly quotas) because they can't scale and they aggressively focus on the $200+ customers and limit the lower tier to maximize profits.

reply

mkl

10 hours ago

 |
prev
 |
next

[–]

Other thread:
https://news.ycombinator.com/item?id=44713837

reply

catigula

11 hours ago

 |
prev
 |
next

[–]

Some equivocation here between legitimate 'heavy use', which is obviously relative and actually referenced in this document, and 'policy violations', which are used at the rationale/justification for it.

reply

sauwan

9 hours ago

 |
prev
 |
next

[–]

Would be great to see how our previous months usage stacked up and when, if at all, we would have been rate limited.

I'd be pretty surprised if I were to get rate limited, but I do use it a fair amount and really have no feel for where I stand relative to other users. Am I in the top 5%? How should I know?

reply

tough

10 hours ago

 |
prev
 |
next

[–]

I cancelled my subscription

I'll keep openAI and they dont even let me use CLI's with it, but they're at least Honest about their offerings.Also their app doesnt tell you to go fuck off ever, if you're Pro

reply

data-ottawa

9 hours ago

 |
prev
 |
next

[–]

The 5% being ‘abusive’ limit seems high (1/20 users — that feels like an arbitrary cost cut based on customer numbers rather than objective based on costs/profit). I would have much preferred to see a scalpel applied to the abusive accounts than this — and from what I’ve seen those users should be very obvious (I’ve seen posts on Reddit with people running dozens of CC instances 24/7).

I also have to wonder how much Sub Agents and MCP are adding to the use, sub agents are brand new and won’t even be in that 95% statistic.At the end of this email there a lot of unknowns for me (am I in the 5%, will I get cut off, am I about to see my usage increase now that I added a few sub agents?). That’s not a good place to be as a customer.

reply

ehnto

2 hours ago

 |
prev
 |
next

[–]

I am pretty interested in what the person letting it run 24/7 is achieving. Is it a continuously processing workload of some kind that pipes into the model? Maybe a 24/7 chat support with high throughput? Very curious.

reply

debian3

1 hour ago

 |
parent
 |
next

[–]

Share your account with people on different timezone

reply

flashgordon

10 hours ago

 |
prev
 |
next

[–]

Ok I really really have to figure out how to have a local setup of the open-source LLMs. I know i know - the "fixed costs" are high. But I have a strong feeling being able to setup local LLMs (and the rig for it) is the next build-your-own-PC phase. All I want is a coding agent and the grunt power to run it locally. Everything else Il build (generate) with it.

I see so many folks claiming crazy hardware rigs and performance numbers so no idea where to begin. Any good starting points on this?(Ok budget is TBD - but seeing a you get X for $Y would atleast help make an informed decision).

reply

colonCapitalDee

10 hours ago

 |
parent
 |
next

[–]

You should consider self-hosting in the cloud. When you start coding run a script that spins up a new VM and loads the LLM of your choice, then run another script to spin it back down when you're done. For intermittent use this works great and is much cheaper than buying your own hardware, plus it's future proof. It does admittedly lack the cool factor of truly running locally though.

reply

flashgordon

10 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah this is the setup I am thinking for now as it is all the "Freedom" with only hardware dependence. Wierdly enough I noticed Qwen3 (coder) was also almost same price as opus 4 which was wierd.

reply

cpursley

10 hours ago

 |
root
 |
parent
 |
next

[–]

Qwen pricing on fireworks.ai is pretty good

reply

paxys

10 hours ago

 |
parent
 |
prev
 |
next

[–]

You can build a decent rig for yourself with:

- 2x 4070 Ti (32 GB total VRAM) - $2200- 64 GB RAM - $200-250- Core i9/Ryzen 9 CPU - $450- 2 TB SSD - $150- Motherboard, cooler, case, PSU - $500-600Total - ~$3500-3700, say $4000 with extras.

reply

flashgordon

10 hours ago

 |
root
 |
parent
 |
next

[–]

wow - do you mind sharing any links to a specific setup? Also whats the biggest model anybody has run on this?

reply

paxys

9 hours ago

 |
root
 |
parent
 |
next

[–]

You can run a
decent
 model on it, say highly quantized Qwen or Deepseek R1 getting 5-10 tokens/sec output, but it will be nothing in comparison to a commercial offering like Claude, o3 or Gemini. For that you need a datacenter-class GPU going for $50K-100K a pop.

reply

icelancer

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

Every model you run on that setup will be at best half as good as Sonnet 4.

reply

lossolo

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

Unfortunately, you will not be able to run any model on this that is comparable to the Claude models.

reply

richwater

10 hours ago

 |
parent
 |
prev
 |
next

[–]

If you're okay with lower quality output, a $10k Mac Studio will get you there. But you _will_ have to accept lower quality outputs compared to todays' frontier models.

reply

OtherShrezzing

8 hours ago

 |
root
 |
parent
 |
next

[–]

>But you _will_ have to accept lower quality outputs compared to todays' frontier models.

I'm curious how much lower quality we're talking about here. Most of the work I ever get an LLM to do is glue-code, or trivial features. I'd expect some fine-tuned Codestral type model with well focused tasks could achieve good performance locally. I don't really need worlds-leading-expert quality models to code up a hamburger menu in a React app & set the background-color to #A1D1C1.

reply

gnator

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

Has anyone tried running with a tenstorrent card? Wanted to see how they fare

reply

flashgordon

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

Yeah I was actually thinking about a proper rig - My gut feel is a rig wouldnt be as expensve as a mac and would actually have a higher ROI (at the expense of portability)?

My other worry about the mac is how unupgradable it is. Again not sure how fruitful it is - in my (probably fantasy land) view if I can setup a rig and then keep updating components as needed - it might last me a good 5 years say for 20k over that period? Or is that too hopeful?So for 20K over 5 years or 4k per year - it comes to about 400 a month (ish). The equivalent of 2 MAX pro subscriptions. Let us be honest - right now with these limits running more than 1 in parallel is going to be forbidden.if I can run 2 claude level models (assuming the DS and Qwens are there) then I am already breaking even but without having to participating in training with all my codebases (and I assume I can actually unlock something new in the process of being free).

reply

lossolo

10 hours ago

 |
root
 |
parent
 |
next

[–]

Buy 4–8 used 3090s (providing 96–192 GB of VRAM), depending on the model and weight quantization you want to run. Used 3090 costs around $800. Add more RAM to offload layers if needed. This setup currently offers the best value for performance.

https://www.reddit.com/r/LocalLLaMA/comments/1iqpzpk/8x_rtx_...You can look for more rig examples on that subreddit.

reply

esskay

9 hours ago

 |
root
 |
parent
 |
next

[–]

I do wonder what the ongoing cost there would be. The ~$9k hardware cost is an easy thing to quantify, but going with a bank of very hot, power hungry GPU's is going to rack up a hefty monthly bill in many parts of the world.

I imagine theres also going to be some problems hooking something like that up to a normal wall socket in North America? (I like the reddit poster am in Europe so on 220v)

reply

icelancer

9 hours ago

 |
root
 |
parent
 |
next

[–]

It's not too bad - I run 6x RTX 3090s on a 2nd-gen Threadripper with PCIe bifurcation cards. The energy usage is only really bad if you're training models constantly, but inference is light enough.

I use 208V power but 120V can indeed be a challenge. The USA has split phase wiring; every house has 220-240V if they need it. Bit of a misunderstanding of how our power works - we have 220-240V on tap, but typical outlets are 110-120V.

reply

flashgordon

8 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah at this point the goal is to see how to maximize for inference. For training it is impossible from the get go to compete with the frontier labs anyway. Im trying to calculate (even amortized over 2 years) the daily cost of running the equivalent rig that can get close to a single claude agent performance. (without needing a 6-digit gpu).

reply

flashgordon

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

Yeah this was what I was doubting too. Like the hardware is one off but how much do you have to modernize your house (lines, cooling, eletrical-fire-safety etc)?

reply

flashgordon

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

Also I wonder if like the old days you could "try" these out somewhere first. Imaging plonking down 5-10k and nothing works (which is fine if you can get a refund ha).

reply

matt_cogito

39 minutes ago

 |
prev
 |
next

[–]

Let's start with stating, that Opus 4 + Sonnet 4 are a gift to humanity. Or at least to developers.

The two models are not just the best models for coding at this point (in areas like UX/UI and following instructions they are unmatched); they come package with possibly the best command line tool today.The invite developers to use them a lot. Yet for the first time ever, I can feel how I cannot 100% fully rely on the tool and feel a lot of pressure, when using it. Not because I don't want to pay, but because the options are either:> A) Pay $200 and be constantly warned by the system that you are close to hitting your quota (very bad UX)
> B) Pay $$$??? via the API and see how your bill grows to +$2k per month (this is me this month via Cursor)I guess Anthropic has the great dilemma now: should they make the models more efficient to use and lower the prices to increase limits and boost usage OR should they cash in their cash cows while they can?I am pretty sure no other models comes even close in terms of developer-hours at this point. Gemini would be my 2nd best guess, but Gemini is still lagging behind Claude, and not that good at agentic workloads.

reply

QuadmasterXLII

8 hours ago

 |
prev
 |
next

[–]

Their business model with the pro plan is to sell a dollar for 80 cents for a while to gain market share. Once they have spent the money allocated to this plan and bring it to a close, don’t expect them to resume it in response to righteous indignation: the money will be gone. See also Uber, MoviePass etc

reply

reasonableklout

6 hours ago

 |
parent
 |
next

[–]

Inference costs have been in freefall since ChatGPT[1], so this is different than Uber/MoviePass. The primary cost is a technology which is getting cheaper as more investment is put into algorithm + hardware R&D.

[1]:https://epoch.ai/data-insights/llm-inference-price-trends

reply

what

31 minutes ago

 |
root
 |
parent
 |
next

[–]

Just because they’re slashing they’re prices while they compete for users doesn’t mean the cost of inference came down at the same rate or at all.

reply

bravesoul2

7 hours ago

 |
parent
 |
prev
 |
next

[–]

That elusive free lunch.

reply

vessenes

5 hours ago

 |
prev
 |
next

[–]

Do not love. I used opus on api billing for some time before the new larger plans came out, so I switched. I routinely hit the opus limits in an hour or two ($100 plan). There are some tasks sonnet is good with but for many it’s worse, and sometimes subtly so.

Upshot - I will probably go back to api billing and cancel. For my use cases (once or twice a week coding binges) it’s probably cheaper and definitely less frustrating.

reply

neom

9 hours ago

 |
prev
 |
next

[–]

I'm working on a coding agent for typescript teams and I'm curious how people would like to consume these things generallyin terms of price a predictability. I've thought through a bunch of stuff, not sure what is best... Right now I have a base fee and then a concept of credits, the base fee ($500) includes 10k credits, and the credits are tied to PRs, it works out to 100 "credits" per simple PR and 200 "credits" for a complex PR, Commit is 20 credits. 20 credits are $5. PR reviews are free.

Is this way too complicated? It feels complicated to me and I worked on it, so I presume it is?I don't want to end up in some "you can work for X number of hours" situation that seems... not useful to engineers?How do real world devs wanna consume this stuff and pay for it so there is some predictability and it's useful still?Thank you. :)

reply

OtherShrezzing

8 hours ago

 |
parent
 |
next

[–]

That suggested pricing structure is too complicated - especially when it boils down to $5 for a simple PR, and $10 for a big one.

reply

eigenvalue

9 hours ago

 |
prev
 |
next

[–]

They need to come up with a better way of detecting people who are actively breaking the ToS by using the Max plans as a kind of backdoor API key, because those users are obviously not using it in the way it was intended and abusing the system. Not sure how they would do that, but I'm guessing you could fingerprint the pattern of requests and see that some of the requests don't fit the expected pattern of genuine requests made by the Claude Code client.

Anyway, I've been resigned to this for a while now (seehttps://x.com/doodlestein/status/1949519979629469930) and ready to pay more to support my usage. It was really nice while it lasted. Hopefully, it's not 5x or 10x more.

reply

shreezus

9 hours ago

 |
prev
 |
next

[–]

I wonder if this is related to the capacity/uptime issues Anthropic has had lately. I got quite a lot of errors last week!

Hopefully they sort it out and increase limits soon. Claude Code has been a game-changer for me and has quickly become a staple of my daily workflows.

reply

westonplatter0

9 hours ago

 |
prev
 |
next

[–]

To make it easier for users to know what to expect, can you release a monitor for users to run locally?

I can understand setting limits, and I'd like to be aware of them as I'm using the service rather than get hit with a week long rate limit / lockout.

reply

jacquesm

8 hours ago

 |
prev
 |
next

[–]

I hope that this communication is not typical of the output of Claude, but if it is it should get a prize of sorts for vagueness and poor style. No way for users to find out if they are affected or not, lots of statements that carry zero information. Not impressed, to put it mildly, besides, they should have enforced their limits from day #1 as they were, not allow people to spend 10K worth of resources on a $200 plan. Now they risk those that are not even affected from re-thinking their relationship with the company.

reply

pxc

7 hours ago

 |
prev
 |
next

[–]

Could this be in part because many of the recent Chinese models (which seem great, tbh) show signs of having been distilled from one or another Claude models?

Or is that a silly idea, because distillation is unlikely to be stopped by rate limits (i.e., if distillation is a worthwhile tactic, companies that want to distill from Anthropic models will gladly spend a lot more money to do it, use many, many accounts to generate syntheitc data, etc.)?

reply

dsrtslnd23

10 hours ago

 |
prev
 |
next

[–]

the rate limits already were very low - and now they are getting even lower, wow.
On a max plan I can use Opus for only a few minutes per day.

reply

esskay

9 hours ago

 |
prev
 |
next

[–]

Starting to realise the business model of LLM's has some serious flaws I see.

reply

yumraj

9 hours ago

 |
prev
 |
next

[–]

> These changes will not be applied until the start of your next billing cycle.

If I’m on annual Pro, does it mean these won’t apply to me till my annual plan renews which is several months away.

reply

mkbelieve

9 hours ago

 |
parent
 |
next

[–]

Same boat. Feels like a nice, big bait & switch.

reply

LTL_FTC

9 hours ago

 |
prev
 |
next

[–]

I have been using Gemini for some time now. I switched away from Claude because I was frustrated with the rate limits and how quickly I seemed to reach them. Last week I decided to give it Claude another try so I resigned up. I linked a personal repository I am working on, prompted it for suggestions on potential refactoring recommendations and hit send. It immediately stopped and said this prompt would reach my limits. Immediately reconsidered my subscription.

reply

3cats-in-a-coat

39 minutes ago

 |
prev
 |
next

[–]

If you wanted a more equitable experience for all you wouldn't just limit the high-end users, but return the money to low-end users.

Charging a low flat fee per use and still warning when certain limits hit is possible. But it's market segmentation not to do it. Just charge a flat fee, then lop off the high-end, and you maximize profit.

reply

wdb

11 hours ago

 |
prev
 |
next

[–]

Guess the reason why they recently introduced agents? ;)
This is not a great change if you ask me. I will have to figure out how badly this affects and if needed just cancel the subscription and find an alternative.

reply

jeswin

4 hours ago

 |
prev
 |
next

[–]

I am a Max 20x subscriber, and I'm not unhappy that Anthropic is putting this in place.

Claude is vital to me and I want it to be a sustainable business. I won't hit these limits myself, and I'm saving many times what I would have spent in API costs - easily among the best money I've ever spent.I'm middle aged, spending significant time on a hobby project which may or may not have commercial goals (undecided). It required long hours even with AI, but with Claude Code I am spending more time with family and in sports. If anyone from Anthropic is reading this, I wanted to say thanks.

reply

browningstreet

3 hours ago

 |
prev
 |
next

[–]

I was actually going to $ign up this week. Now I have to study everything before committing.

reply

mushufasa

9 hours ago

 |
prev
 |
next

[–]

I think they should totally do this but I think they should call it "rate-limiting" instead of "weekly limit". Seems pretty clear to me that the purpose is to avoid situations where people are running 5 background agents 24/7, not the person working during business hours normally. Reframing this makes it more clear this is about bots not users.

reply

brainless

7 hours ago

 |
prev
 |
next

[–]

Tools that generate code will have a lot of competition. It's good that Athropic is refining it's pricing but would have been better if users got to know their exact usage and apply own controls.

Frustrated users, who are probably using the tools the most will try other code generation tools.

reply

wg0

9 hours ago

 |
prev
 |
next

[–]

To be fair - abuse is real. This also shows that "AI" is on "VC ventilators" of greed.

Waiting for higher valuations till someone pulls the trigger for acquisition.IPOs I don't see to be successful because not everyone gets a conman like Elon as their frontman that can consistently inflate the balloon with unrealistic claims for years.

reply

computegabe

9 hours ago

 |
prev
 |
next

[–]

I think we'll see a lot more contextual engineering efforts soon. It is really inefficient to be uploading your entire codebase pretty much every request, which is what a lot of people are doing. When in reality, very few parts need the full context when programming. Although, big token doesn't seem to care, and often encourages this (including the editors).

reply

cheschire

9 hours ago

 |
parent
 |
next

[–]

I could see a front-end / back-end split in the future where a completely on-client LLM is used to trim down the request and context before shoving the request off to the back-end.

reply

geor9e

7 hours ago

 |
prev
 |
next

[–]

>affecting less than 5% of users

Notice they didn't say 5% of Max users. Or 5% of paid users. To take it to the extreme - if the free:paid:max ratio were 400:20:1 then 5% of users would mean 100% of a tier. I can't tell what they're saying.

reply

JyB

2 hours ago

 |
prev
 |
next

[–]

I thought Claude code was pay as you go!?

reply

mattnewton

9 hours ago

 |
prev
 |
next

[–]

Can I have an option to easily "fall back" to metered spend when hitting these hard limits? I wouldn't mind spending $5-10 on api credits to not interrupt my flow one day, and right now that means switching to another tool or logging out and re-logging in when the rate limit switches back.

reply

TheServitor

7 hours ago

 |
prev
 |
next

[–]

Zero surprise. Some of you were really going nuts out there.

Then again, to scale is human

reply

anonzzzies

10 hours ago

 |
prev
 |
next

[–]

We will see but I hit the limit multiple times a day so I am a bit scared that this would mean looking for alternatives.

reply

garciasn

10 hours ago

 |
parent
 |
next

[–]

Using Claude Code or the web UI? If when using Claude Code, you may need to break your codebase up into smaller chunks to help.

That said, there's no fucking way I am getting what they claim w/Opus in hours. I may get two to three queries answered w/Opus before it switches to Sonnet in CC.

reply

anonzzzies

9 hours ago

 |
root
 |
parent
 |
next

[–]

Claude Code cli. Yeah, I gave up on Opus as I deed it switches really fast (200 sub). I made my own flow tooling and prompting which uses way less than it does on its own, but I still hit the limits.

reply

mkbelieve

9 hours ago

 |
prev
 |
next

[–]

I understand, but I also will not pay a subscription fee for limited service. I canceled as soon as I got this e-mail. Too bad I signed up for an annual subscription last month.

This is also exactly why I feel this industry is sitting atop a massive bubble.

reply

OtherShrezzing

8 hours ago

 |
parent
 |
next

[–]

As far as the email says, this change is triggered at your next billing cycle. So your account is grandfathered in until next year.

reply

bananapub

6 hours ago

 |
parent
 |
prev
 |
next

[–]

> I also will not pay a subscription fee for limited service.

you...already were? it already had a variety of limits, they've just added one new one (total weekly use to discourage highly efficient 24/7 use of their discounted subscriptions).

reply

ComplexSystems

11 hours ago

 |
prev
 |
next

[–]

These are limits for the $200/mo plan?

reply

Disposal8433

9 hours ago

 |
parent
 |
next

[–]

There
are
 limits for $200 per month?

reply

CSMastermind

11 hours ago

 |
parent
 |
prev
 |
next

[–]

That's the subscription I have and this looks like the email that I got.

reply

steveklabnik

10 hours ago

 |
parent
 |
prev
 |
next

[–]

"Max" is the name for both the $100 and $200 plan.

reply

neutrinobro

4 hours ago

 |
prev
 |
next

[–]

This was bound to happen at some point, but probably net-on-net won't affect most users. I think it's pretty useful for a variety of tasks, but those tend to fall into a rather narrow category (boilerplate, simple UI change requests, simple doc-strings/summaries), and there is only so much of that work which is required in a month. I certainly won't be cancelling my plan over this change, but so far I also haven't seen a reason to increase it over the hobbyist-style $20/mo plan. When I do run into usage limits, its usually already at the end of the day, or I just pivot to another task where it isn't helpful.

reply

koolba

11 hours ago

 |
prev
 |
next

[–]

This is like when the all-you-can-eat buffet tells you you're only allowed to go the buffet line once.

reply

gingersnap

11 hours ago

 |
parent
 |
next

[–]

No, it's not. It's the all you can eat buffet saying that 95% can eat all they want, but the 5% that keep sneaking food in their backpack to eat when they get can't do that anymore.

reply

koolba

10 hours ago

 |
root
 |
parent
 |
next

[–]

There's no lobster rolls stuffed into a backpack here. It's using the service as it was pitched, an all-you-can-eat buffer of API calls. Anything that limits what that means is scaling back access to that buffet.

If the new limits are anything less than 24 * 7 / 5 times the previous limits then power users are getting shafted (which understandably is the point of this).What's worse with this model is that a runaway process could chew through your weekly API allotment on a wild goose chase. Whereas before the 5-hour quantization was both a limiter and guard rails.

reply

jononor

9 hours ago

 |
root
 |
parent
 |
next

[–]

It was never unlimited. The 5 hourly limit was there from before.

reply

Eggpants

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

The fact you believe the 5% number is pretty interesting.

reply

volkk

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

No it's not. It's like an all you can eat buffet stating you can eat as much as you want and feed your friends and the homeless outside for a one time fee, and then realizing that the economic model made 0 sense to begin with and need to either state that you're only allowed to eat what you personally can, or increase the price to something that can sustain the amount of food being removed from the buffet.

reply

brenm

6 hours ago

 |
prev
 |
next

[–]

This is bad.

I switched to Claude Code because of Cursor’s monthly limits.If I run out of my ability to use Claude Code, I’m going to just switch back to Cursor
and stay there. I’m sick of these games.If you think it’s ok, then make Anthropic dog food it by putting every employee in the pro plan and continue to tell them they must use it for their work but they can’t upgrade and see how they like it.

reply

bravesoul2

7 hours ago

 |
prev
 |
next

[–]

I'm the other way around. Below my rate floor for bothering to renew! Work provides AI and don't have too much time to play at the weekend.

reply

taormina

7 hours ago

 |
prev
 |
next

[–]

I feel like I am constantly hitting the 5 hour limits not doing very much. I feel like I will quit using Claude Code outright if my usage is gone by Tuesday.

reply

Oras

9 hours ago

 |
prev
 |
next

[–]

> affecting less than 5% of users based on current usage patterns.

How about adding ToS clause to prevent abuse? wouldn't that be better than having a statement with negative effect on the rest of 95%?

reply

jononor

9 hours ago

 |
parent
 |
next

[–]

That just gives your team another thing to do, trying to police a ToS clause. And one would have to define abuse somehow, which is quite tricky. There are a lot of guite legitimate but expensive ways to use such a general thing as LLM compute.

reply

natch

9 hours ago

 |
prev
 |
next

[–]

I wish you could allow some concept of rollover of credits, even if only fractional, for cases where someone has to be away for a few days and the clock is ticking with no usage.

reply

verelo

7 hours ago

 |
prev
 |
next

[–]

Am i missing something? Why don’t people just add an api key to Claude…are the subscription models that much better?

reply

resonious

6 hours ago

 |
parent
 |
next

[–]

The subscription models are more cost effective.

reply

ChadMoran

9 hours ago

 |
prev
 |
next

[–]

Okay but when will we get visibility into this other than we're at the 50% of the limit? If you're going to introduce week long limits, transparency into use is critical.

reply

vonneumannstan

9 hours ago

 |
prev
 |
next

[–]

Apparently people are consistently getting thousands of dollars worth of tokens for their $200/mo sub so this was just obviously unsustainable for Anthropic.

reply

acaloiar

8 hours ago

 |
prev
 |
next

[–]

LLM Token and usage limit anxiety aught to pair nicely with battery and range anxiety. All part of a head-healthy diet.

reply

thoughtfulappco

10 hours ago

 |
prev
 |
next

[–]

I don't get the idea that using more compute or running a continuous agent is considered "power user". Consuming more =! power users lol

reply

thoughtfulappco

10 hours ago

 |
prev
 |
next

[–]

Yes, yes let the normies who wait for their pizza to cook while running one prompt at a time "eat" so to speak mwuahahah #deathtopowerusers

reply

lerchmo

4 hours ago

 |
prev
 |
next

[–]

Why don’t they just offer a $500/m plan?

reply

christophilus

11 hours ago

 |
prev
 |
next

[–]

Hm. I run Claude Code in several containers, though generally only one is active at a time. I wonder if they’ll see that as account sharing?

reply

andix

11 hours ago

 |
parent
 |
next

[–]

This is a very common usage pattern, I don't think they will restrict that.

The daily limits are probably there to fix the account sharing issue. For example I wanted to ask a friend who uses the most expensive subscription for work, if I could borrow the account at night and on weekends. I guess that's the kid of pattern they want to stop.

reply

itsalotoffun

10 hours ago

 |
root
 |
parent
 |
next

[–]

No. They're just desperately trying to limit the number of tokens burned per $200/mo account. It's trivial to burn 1-3x that dollar amount per DAY even before you're loaning your account out to friends in different timezones. And as ccusage will show, if you were paying API pricing rates your $200/mo plan would consume closer to $3-5k/mo in "credits".

Somehow you're "not allowed" to run your account 24/7. Why the hell not? Well because then they're losing money. So it's "against their ToS". Wtf? Basically this whole Claude Code "plan" nonsense is Anthropic lighting VC on fire to aggressively capture developer market share, but enough "power users" (and don't buy the bullshit that it's "less than 5%") are inverting that cost:revenue equation enough to make even the highly capitalized Anthropic take pause.They could have just emailed the 4.8% of users doing the dirty, saying "hey, bad news". But instead EVERYONE gets an email saying "your access to Claude Code's heavily subsidized 'plans' has been nerfed".It's the bait and switch that just sucks the most here, even if it was obviously and clearly coming a mile away. This won't be the last cost/fee balancing that happens. This game has only gotten started. 24/7 agents are coming.

reply

discordance

2 hours ago

 |
parent
 |
prev
 |
next

[–]

When you ship the container, do you also ship Claude Code and its config with it?

reply

jdboyd

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I think that is a common use case. If you run the containers at the same time, it sounds to me like you will just run into the usage limits more quickly.

reply

Workaccount2

6 hours ago

 |
prev
 |
next

[–]

The pitfalls of being beholden to 3rd parties for hardware.

reply

Bluestein

9 hours ago

 |
prev
 |
next

[–]

Gosh, maybe there's something I am not understandinng, but 24/7? Wow.-

PS. Ah! Of course. Agents ...

reply

nbbaier

10 hours ago

 |
prev
 |
next

[–]

Will there be a native way to track in Claude Code how close we are to hitting those weekly rate limits?

reply

oidar

10 hours ago

 |
prev
 |
next

[–]

How do we know when we are close to hitting these limits? Will there be a way to check that?

reply

aeternum

7 hours ago

 |
prev
 |
next

[–]

If you're paying per-month why are the limits weekly?

reply

jongjong

2 hours ago

 |
prev
 |
next

[–]

For the sake of saying something positive on HN, Claude Code is great. I haven't run into any limits yet. My code is quite minimalist and the output of Claude Code is also minimalist, maybe that's why.

If you work on some overengineered codebase, it will produce overengineered code; this requires more tokens.

reply

GiorgioG

8 hours ago

 |
prev
 |
next

[–]

This is fantastic news. They're burning through too much cash too fast. They're going to have to sooner or later charge more money at which point businesses will balk at the price and the AI hype cycle will come to an end. I can't wait.

reply

submeta

9 hours ago

 |
prev
 |
next

[–]

This explanation is so vague that it’s hard to take seriously. Anthropic has full access to usage data—they could easily identify abusive users and throttle them specifically. But they don’t. Why? Because it was never really about stopping abuse. The truth is: Anthropic can’t handle the traffic and growth, and now they’re looking for a convenient excuse to limit access and point fingers at so-called “heavy users.”

The problem is, we have no visibility into how much we’ve actually used or how much quota we have left. So we’ll just get throttled without warning—regularly. And not because we’re truly heavy users, but because that’s the easiest lever to pull.And I suspect many of us paying $200 a month will be left wondering, “Did I use it too much? Is this my fault?” when in reality, it never was.

reply

bananapub

9 hours ago

 |
parent
 |
next

[–]

> they could easily identify abusive users and throttle them specifically.

that's exactly what they've done? they've even put rough numbers in the email indicating what they consider to be "abusive"?

reply

submeta

8 hours ago

 |
root
 |
parent
 |
next

[–]

That’s bs. I just switched from 100 EUR a month to 200 EUR plan. Why? Because two days ago Anthropic decided that I had to wait until noon. And I just started my workday and used CC for half an hour.

I use CC 1-3h a day. Three days a week. Am I a heavy user now? Will I be in the 5% group? If I am, who will I argue with? Anthropic says in its mail that I can cancel my subscription.

reply

lvl155

9 hours ago

 |
prev
 |
next

[–]

I think it’s hilarious they roll this out right after subagent introduction.

reply

jjice

8 hours ago

 |
prev
 |
next

[–]

As part of the 95% here, I'm totally cool with this. I'm just a Pro plan user, but holy shit I hit problems with their service constantly. Claude is my preferred LLM currently, but sometimes during a normal 9-5, I can't use it at all due to outages, which really gets in the way while developing an MCP server.

Anthropic seems like they need to boost up their infra as well (glad they called this out), but the insane over-use can only be hurting this.I just can't cosign on the waves of hate that all hinges on them adding additional limits to stop people from doing things like running up $1k bills on a $100 plan or similar. Can we not agree that that's abuse? If we're harping on the term "unlimited", I get the sentiment, but it's absolutely abuse and getting to the point where you're part of the 5% likely indicates that your usage is abusive. I'm sure some innocent usage will be caught in this, but it's nonsense to get mad at a business for not taking the bath on the chunk of users that are annihilating the service.

reply

aliljet

10 hours ago

 |
prev
 |
next

[–]

Maybe this is an unpopular opinion, but it seems like Anthropic has quietly 4x'd the real cost of the Pro plan. There are 168 hours in a week, and if I'm able to (safely) bet on 40 hours of use, realistically, I just lost 75% of the value of the plan.

What are the reasonable local alternatives? 128 GB of ram, reasonably-newish-proc, 12 GB of vram? I'm okay waitign for my machine to burn away on LLM experiments I'm running, but I don't want to simply stop my work and wake up at 3 AM to start working again..

reply

kmac_

10 hours ago

 |
parent
 |
next

[–]

Pro is just a paid demo. I hit the limit all the time on a small project, and I'm not even doing anything weird. The product is still great, though.
At work, we checked out a bunch of options, and almost everyone chose something different, so the competition is though.

reply

bananapub

9 hours ago

 |
parent
 |
prev
 |
next

[–]

> Maybe this is an unpopular opinion, but it seems like Anthropic has quietly 4x'd the real cost of the Pro plan. There are 168 hours in a week, and if I'm able to (safely) bet on 40 hours of use, realistically, I just lost 75% of the value of the plan.

I think you're just confused about what the Pro plan was, it never included being used for 168 hours/week, and was extremely clear that it was limited.> What are the reasonable local alternatives? 128 GB of ram, reasonably-newish-proc, 12 GB of vram? I'm okay waitign for my machine to burn away on LLM experiments I'm running, but I don't want to simply stop my work and wake up at 3 AM to start working again..a $10k mac mini with 192GB ofvramwith any model you can download still isn't close to Claude Sonnet.

reply

lavezzi

6 hours ago

 |
root
 |
parent
 |
next

[–]

not really true per
https://artificialanalysis.ai/?intelligence-tab=coding

reply

thenano2

7 hours ago

 |
prev
 |
next

[–]

Well those who need more than the limits, register a second account and pay for a second subscription... Not the end of the world

reply

wdb

11 hours ago

 |
prev
 |
next

[–]

Guess they ran into the usage limits themselves when they worked on the messaging in Claude Code: "Claude usage limit reached. Your limit will reset at 8pm (UTC)"

Why not use the user's timezone?

reply

serial_dev

10 hours ago

 |
parent
 |
next

[–]

Are you crazy, considering time zones would have burned through their allotted tokens for the week.

reply

SatvikBeri

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Plenty of people using CC from multiple timezones, e.g. I use it from my laptop and from EC2 servers.

reply

bravesoul2

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Leaky bucket. No time zone needed.

reply

bananapub

9 hours ago

 |
parent
 |
prev
 |
next

[–]

this is a super-american thing, not a AI company thing

reply

bitdeep

6 hours ago

 |
prev
 |
next

[–]

deserved for this 5%, people get out of mind and abuse the service.

reply

Xmd5a

4 hours ago

 |
prev
 |
next

[–]

We are the 95%!!

reply

sea-gold

11 hours ago

 |
prev
 |
next

[–]

"Most Pro users can expect 40-80 hours of Sonnet 4 within their weekly rate limits."

reply

blinded

9 hours ago

 |
prev
 |
next

[–]

Dial back the vibe :)

reply

vFunct

11 hours ago

 |
prev
 |
next

[–]

Seems like their business plan is unsustainable. What's a sustainable cost model?

Say an 8xB200 server costs $500,000, with 3 years depreciation, so $166k/year costs for a server. Say 10 people share that server full time per year, so that's going to need $16k/year/person to break even, so ~$1,388/month subscription to break even at 10x users per server.If they get it down to 100 users per server (doubt it), then they can break even at $138/month.And all of this is just server costs...Seems AI coding agents should be a lot more expensive going forward. I'm personally using 3-4 agents in parallel as well..Still, it's a great problem for Anthropic to have. "Stop using our products so much or we'll raise prices!"

reply

jononor

8 hours ago

 |
parent
 |
next

[–]

I do not think they are aiming to be cashflow positive now. That might not be possible. Though if it is within range they might want to go for it. Because the stamina needed to win this race is going to be immense. Especially since OpenAI is going hard for scaling up via investor funding, and Google can afford to loose/invest a couple billions annually by diverting from their main revenue sources.

A realistic business plan would be to burn cash for many years (potentially more than a decade), and bank on being able to decrease costs and increase revenue over that time. Investors will be funding that journey.So it is way too early to tell whether the business plan is unsustainable. For sure the unit economics are going to be different in 5 and 10 years.Right now is very tough though- since it is basically all early adopter power user types, which spend a lot of compute. Later one probably can expect more casuals, maybe even a significant amount of "gym users" that pay but basically never uses the service. Though OpenAI is currently stronger for casuals, I suspect.Over the next decade, hardware costs will go down a lot. But they have go find a way to stay alive (and competitive) until then.

reply

Fade_Dance

11 hours ago

 |
parent
 |
prev
 |
next

[–]

It seems to me that the business model simply won't be making money until a time when jobs are running on new, more efficient hardware a generation or two from now. Like you said, the numbers just don't work currently. I'm under the impression they want to potentially get to break-even for now.

reply

closewith

11 hours ago

 |
prev
 |
next

[–]

It was always too good to last.
I assume this is the end of the viability of the fixed price options.

reply

j45

6 hours ago

 |
prev
 |
next

[–]

Sincerely enjoy and appreciate Claude, feedback based on that:

- It would be nice to know if there was a way to know or infer percentage wise the amount of capacity a user is currently using (rate of usage) and has left, compared to available capacity. Being scared to use something is different than mindful.- Since usage it can feel a little subjective/relative (simple things might use more tokens, or less, etc) to things beyond a user's usage alone, it would be nice to know how much capacity is left both on the current model and in 1 month now to learn.- If there is lower "capacity" usage rates available at night vs the day, or just slower times, it might be worth knowing. It would help users who would like to, plan around it, compared to people who might be just making the most of it.

reply

yieldcrv

6 hours ago

 |
prev
 |
next

[–]

I only began using Claude because OpenAI was fumbling in my use cases. Whenever their public facing offering was rate limiting, or experiencing congestion, or having UX issues like their persistent "network error" in the middle of delivering a response, then I would go to Claude.

You having the same issue kills the point of using you.

reply

sneak

6 hours ago

 |
prev
 |
next

[–]

Why not just have a usage-based pricing system that people can opt in to so that they just pay-as-they-go once they hit these plan limits?

It makes no sense to me that you would tell customers “no”. Make it easy for them to give you more money.

reply

bananapub

5 hours ago

 |
parent
 |
next

[–]

they already do, you can give claude code an API key and it charges per token.

this entire thread is people whinging about the "you get some reasonable use for a flat fee" product having the "reasonable use" level capped a bit at the extreme edge.

reply

sneak

2 hours ago

 |
root
 |
parent
 |
next

[–]

No, I mean, a one-click (or no-click) upgrade path. Having to hit a wall and then go get your API key and stuff sounds like a pain. It should just ask you if you want to switch to usage-based pricing when you hit the limit.

reply

incomingpain

7 hours ago

 |
prev
 |
next

[–]

Claude's vague limits is literally why im not a subscriber.

reply

bachittle

10 hours ago

 |
prev
 |
next

[–]

I'm guessing less than 5% of the users are just letting Claude Code run in an autonomous loop making slop. I tried this too: and Opus 4 isn't good enough to run autonomously yet. The Rube Goldberg machine needs to be carefully calibrated.

reply

swalsh

10 hours ago

 |
parent
 |
next

[–]

This happens when you prompt it poorly. If you want to avoid slop, the first step is to write an extensive BRD. Read it, understand it, make sure it has everything needed. Then write a solutions architecture document. Read it, understand it, make sure it is fully specified including how things are structured, architecture, principles etc. You can use AI to write these documents. Just make sure to read them, and edit them as needed.

When you have your functional spec, and your tech spec, ask it to implement it. Additionally add some basic rules, say stuff like "don't add any fallback mechanisms or placeholders unlessed asked. Keep a todo of where you're at, ask any questions if unsure.The key is to communicate well, ALWAYS READ what you input. Reivew, and provide feedback. Also i'd reccomend doing smaller chunks at a time once things get more complicated.

reply

albertgoeswoof

9 hours ago

 |
root
 |
parent
 |
next

[–]

When do you read the code

reply

swalsh

8 hours ago

 |
root
 |
parent
 |
next

[–]

While it's being generated, I'll spot check it, and after I test the code i'll peek in more detail at it. I review the code in much the same way I review code from a human dev. I almost never look closely at ALL lines. I'll do a quick look through just looking to see if anything jumps out, and then for the areas I intuitively know there might be some funny business I'll do a deeper dive into the code.

reply

bouyaveman6

9 hours ago

 |
prev
 |
next

[–]

Play it fair, and it will be fine

reply

thenaturalist

8 hours ago

 |
prev
 |
next

[–]

Ah, the beauty of price discovery.

Economists are having a field day.

reply

itsalotoffun

10 hours ago

 |
prev
 |
next

[–]

Vibe pricing. That's all this is. "Pay us $200/mo and get... access". There's no way to get a real usage meter (ccusage doesn't count). I want an Anthropic dashboard showing "you've used x% of your paid quota". Instead we get vibe usage. Vibe pricing. "Hey pay us money and we'll give you some level of access but like you won't know what, but don't worry only 5% of our users will trip the switches" bullshit. Someone else in this thread nailed it:

> sounds like it affects pretty much everyone who got some value out of the toolFeels that way.But compared to paying the so-called API pricing (hello ccusage) Claude Code Max is still a steal. I'm expecting to have to run two CC Max plans from August onwards.$400/mo here we come. To the moon yo.

reply

Wowfunhappy

10 hours ago

 |
parent
 |
next

[–]

> I'm expecting to have to run two CC Max plans from August onwards.

...are you allowed to do that? I guess if they don't stop you, you can do whatever you want, but I'd be nervous about an account ban.

reply

thoughtfulappco

10 hours ago

 |
prev
 |
next

[–]

Let the normies who cook things between single prompt to finish "eat" so to speak. wmuahahaha

leveling the playing field i see lol

reply

naze

9 hours ago

 |
prev
 |
next

[–]

Cancelled my subscription.

reply

cheema33

8 hours ago

 |
parent
 |
next

[–]

It is unclear how Anthropic will survive now that you have canceled. Have you moved to a better model that is even cheaper? If so, please do share.

reply

latchkey

10 hours ago

 |
prev
 |
next

[–]

A bunch of words to just say:

We're going to punish the 5% that are using our service too much.

reply

famahar

8 hours ago

 |
parent
 |
next

[–]

What is the use case for that much usage? Are people mass running vibe code agents? Genuinely curious.

reply

taormina

7 hours ago

 |
root
 |
parent
 |
next

[–]

I have been hitting the 5 hour mark just using Claude Code at all on a very reasonably sized Flutter codebase. I’m relatively concerned but it’s very non-critical but I’m more likely to quit using the tool outright instead of paying them more. I hate how black box it is and this is making that worse.

reply

octernion

7 hours ago

 |
prev
 |
next

[–]

wow, a team that has one nine of availability and trending downwards fast is relieving pressure. big surprise!

reply

acedTrex

9 hours ago

 |
prev
 |
next

[–]

oh no, anyway!

reply

cdelsolar

8 hours ago

 |
prev
 |
next

[–]

the party is over

reply

dionian

9 hours ago

 |
prev
 |
next

[–]

afraid im in the 5%. not doing anything nefarious, just lots of parallel usage, no scripting or overnight or anything.

i just found ccusage, which is very helpful. i wish i could get it straight from the source, i dont know if i can trust it... according to this ive spent more my 200$ monthly subscription basically daily in token value.. 30x supposed costive been trying to learn how to make ccode use opus for planning and sonnet for execution automatically, if anyone has a good example of this please share

reply

blalezarian

10 hours ago

 |
prev
 |
next

[–]

Can we PLEASE fix the bug in VS Code where the terminal occasionally scrolls out of control and VS Code crashes? It is very painful and we have to start the context all over again. This happens at least 1x per day.

reply

steveklabnik

10 hours ago

 |
parent
 |
next

[–]

> we have to start the context all over again.

Use /resume

reply

submeta

8 hours ago

 |
prev
 |
next

[–]

Tangential: Is there a similar service we can use in the cli, a replacement for CC? I like Cursor, I pay both for Cursor and CC, but. I live in the terminal (tmux, nvim, claude code, lazygit, yazi), and I prefer to have an agentic coding experience in the terminal. But CC has deteriorated so much in the past weeks that I constantly use repomix to compress whole projects and ask o3 for help because CC just can’t solve tasks that it previously would solve in a single shot.

reply

lavezzi

6 hours ago

 |
parent
 |
next

[–]

use a proxy and use Claude Code with other models.

reply

lvl155

8 hours ago

 |
parent
 |
prev
 |
next

[–]

There are many but none are as polished as CC.

reply

dboreham

10 hours ago

 |
prev
 |
next

[–]

Whenever a marketing person uses the word "unlimited", they mean: "limited".

reply

usernamed7

10 hours ago

 |
prev
 |
next

[–]

I'm sure it's way more than 5%, ISP's pulled the same thing with bandwidth caps to shame people.

Part of the reason there is so much usage is because using claude code is like slot machine, where SOMETIMES it's right, most times it needs to rework what it did, which is convenient for them. Plus their pricing is anything but transparent as for how much usage you actually get.I'll just go back to ChatGPT. This is not worth the headache.

reply

naze

9 hours ago

 |
prev
 |
next

[–]

I cancelled my subscription. The enshittification is hitting this space massively already.

reply

closewith

11 hours ago

 |
prev
 |
next

[–]

It was always too good to last.

I assume this is the end of the viability of the fixed price options.

reply

steveklabnik

11 hours ago

 |
parent
 |
next

[–]

> affecting less than 5% of users based on current usage patterns.

reply

serial_dev

10 hours ago

 |
root
 |
parent
 |
next

[–]

Affecting 5% of users to me sounds like it affects pretty much everyone who got some value out of the tool and is not a casual coder.

reply

steveklabnik

10 hours ago

 |
root
 |
parent
 |
next

[–]

I don't think it's that simple. We'll see though, I am very curious if I'm in that 5% or not.

reply

thoughtfulappco

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

I dont know if running an agent 24/7 means you are "better" than casual coder. Code quality is still a thing, HITL i believe in still (not buying complete agent/mcp hype), I don't know if using more resources = extracting more value atm

reply

serial_dev

10 hours ago

 |
root
 |
parent
 |
next

[–]

Emphasis on “and”.

> it affects pretty much everyone who got some value out of the tool AND is not a casual coder.I didn’t mean casual in the negative sense, so there is no “better”, there is only casual and not casual.My theory is that 5% sounds like a small number until you realize that many people just tried it and and didn’t like it, forgot to cancel, have it paid by their employer wishing for 100x improvements, or most people have found AI useful only in certain scenarios that they face every once in a while etc.

reply

andix

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

I don't really get how those 24/7 agents should work. Claude code is the first tool that gives me really good LLM code, but it needs A LOT of guidance. I even interrupt it often, to stop it following through on bad ideas.

reply

closewith

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

3 hours of Opus usage per work day will be exhausted fast.

reply

i_am_proteus

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

We do not know if that is less than 5% of users or less than 5% of paid users?

We do know that PR teams enjoy framing things in the most favorable light possible.

reply

steveklabnik

10 hours ago

 |
root
 |
parent
 |
next

[–]

We do, they're paid users. These limits are regarding the usage of the paid plans.

reply

SatvikBeri

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

It's talking about subscriptions, which implies paid users.

reply

andix

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

Let's hope that's true, and not some statistics trick.

reply

steveklabnik

10 hours ago

 |
root
 |
parent
 |
next

[–]

I certainly am!

reply

jstummbillig

11 hours ago

 |
parent
 |
prev
 |
next

[–]

This seems to be the exact opposite?

reply

serial_dev

10 hours ago

 |
root
 |
parent
 |
next

[–]

The writing is on the wall, we just need to read it. Fixed price offerings will be either gone or neutered.

reply

jstummbillig

10 hours ago

 |
root
 |
parent
 |
next

[–]

Why? There are a lot of products where fixed price offerings can exist, like internet access in many parts of the world. The way that Anthropic implemented this change and how they explain it, hints that this could work very much the same: There is be a level of borderline abusers that need to be reigned in. The rest are a few power users that are subsidized by a lot of normal users.

I am not saying this is what must happen here, but I see no effort to substantiate why it could not.

reply

malthaus

11 hours ago

 |
prev
 |
next

[–]

im really tired of all those ai players just winging it

can someone please find a conservative, sustainable business model and stick with it for a few months please instead of this mvp moving target bs

reply

motoxpro

11 hours ago

 |
parent
 |
next

[–]

You can use the API. You're using the fixed price becasue it's cheaper. It's cheaper because they price it assuming a certain amount of usage being below a threshold. The usage went above the threshold. The usage was limited because of that, and they will make a plan with an increased fixed price and/or increase the price of the pro plan.

Seems pretty standard to me.

reply

cheema33

8 hours ago

 |
parent
 |
prev
 |
next

[–]

Agree with the other reply here. You are complaining about a problem that does not exist. Want price predictability? Use the API pricing! It is pay per use.

The Buffet-style pricing gets you more bang for the buck. How much more? That bit is uncertain. Adjust your expectations accordingly.

reply

adtac

10 hours ago

 |
parent
 |
prev
 |
next

[–]

if you feel cheated now, I promise you'll feel more cheated if they did this after you rely on it for several months. the least worst option is to change pricing as early as possible.

reply

beiconic

10 hours ago

 |
prev

[–]

I saw this one coming. Going to make more and more people switch over to gemini.

reply

Consider applying for YC's Fall 2025 batch! Applications are open till Aug 4

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
