---
title: 'Codeck Presents Verdent AI: They Wanted Opinions, I Have Plenty - DEV Community'
url: https://dev.to/anchildress1/codeck-presents-verdent-ai-they-wanted-opinions-i-have-plenty-5ccl
site_name: devto
fetched_at: '2025-09-26T11:06:33.298727'
original_url: https://dev.to/anchildress1/codeck-presents-verdent-ai-they-wanted-opinions-i-have-plenty-5ccl
author: Ashley Childress
date: '2025-09-24'
description: 'Previewing Verdent AI through Codeck turned into a full-tilt stress test: VS Code extension, multi-agent Deck, and plenty of chaos. Here’s what broke, what worked, and which parts outshined everything else—completely biased by my own strong opinions and nothing else. Tagged with tooling, ai, vscode, productivity.'
tags: '#tooling, #ai, #vscode, #productivity'
---

🦄 I agreed to write this post weeks ago and when I said, "Yeah, sure—I was planning on it anyway!" it didn't dawn on me immediately that the free credits I received in return technically makes this a paid post. I'm sure there's an email somewhere that says exactly how much I received for whatever this turns out to be, but off the top of my head? I've got no idea. As an aside, I've been dodging writing the first word since I had that epiphany.

So, I let the "official-ness" sink in for a bit with varying degrees of acceptance, depending on the day. Fast-forward to now, I'm hours behind already, and it's either I start writing or don't do it at all. 🙄Fine.I really had planned on writing this post anyway and I'm also very much aware the problem only exists in my version of the universe. 😒

So here's the first (and possibly last) promotion post you will see from me. Told in a way that's 100% true to form—starting at the very beginning. And really running longer than I intended, but the direction completely picked itself. 🤷‍♀️

## The Dev Blog ✍️

This isn't the first time I've said "this" (being this blog and everything else Dev or Dev-adjacent) was never intended to be more than me throwing ideas into the void and occasionally serve as my personal copy and paste specialty for "the answer you're looking for is documented already... over there." 👉

The unexpected side effect?I have way too much fun writingand an equal amount of amusement playing with Leonardo and the banner character, River (who refuses to cooperate most days).

The other bonus? Just like everything else I do, "this" is in one way or another wrapped up and thoroughly entangled with AI. Whether it's playing with the images, trying to coax some sense of originality out of GPT-5 (or Gemini on the days I give up early), or letting Copilot take center stage (for now), there's at least a few LLM's close by (and more in line to join the party as soon as space permits).

## Verdent Out of the Blue: First Impressions 🌱

I'm very happy being mostly invisible on social media. Even my GitHub sat empty until this year. Everything I did was on work's servers anyway. Why would I need to put it anywhere else? Most all code I write has one simple goal—to simplify my life and work-life definitely counts.

🦄 Work stopped trying to track all the randomness I do and just gave me a permanent unexpected-Ashley-project story with a fixed residential address in the backlog. They may take forever to finish, but there's usually at least three different projects in that bucket at any given point 😆

So when the Verdent team first reached out at the beginning of August inviting me to preview their new AI solution, I was immediately intrigued and highly suspicious. I mean, who were these people? Where did they come from? And more importantly, how exactly did they manage to find me to begin with?

The problem was two-fold, really. First, my LinkedIn is lucky to get checked twice a week so communication was slow. I'd ask a question, later in the week I'd be grumbling to myself about the vague "agent' answers. Second (and mostly thanks to that last part), I couldn't for the life of me figure out what this thing was supposed to do beyond the answer I was given: it's an agent. 🫠

At some point curiosity took over completely, and I became invested in figuring out this new sleuth AI nobody has ever heard of. I mean, I've tried nearly every other "agent" and I had a hard time reconciling the possibility of one existing beyond my knowledge. Besides, it all seems legit and I'm rarely one to turn down any sort of adventure anyway. Especially when AI is involved. So I answered with my usual, "Sure—why not? Sign me up."

🦄 No. I really didn't have a clue what I had just agreed to. To be fair though, they didn't know who they had just signed on either!

## All Or Nothing ❇️

I know I've said this before here, but I don't do bits or pieces ofanything. The whole concept of "dip your toes in first" simply doesn't compute for me—at all. I'm very much an all or nothing sort of personality, and it especially shows when I know I'm driving the deadline anyway. So in this instance, my "why not?" really meant "Congrats! You get to be the sole focus of my various projects for the foreseeable future." 🎉

I suppose it's possible the Verdent folks had read that fact somewhere already—I don't exactly keep any secrets. I never asked them. When they invited me to test out their "mystery AI solution" (which I'm positive every single person there has slaved over at all hours on multiple occasions in the past six months), nobody asked me for a number between 0 and 10 describing how much I enjoy breaking things (the answer is "at least twelve").

Also, Ireally lovebeta-y things. I ran those same kinds of previews for several years before I started at THD. Nope—I didn't think to mention that at first, either. Wouldn't have mattered, really. If anything, knowing what sort of feedback I would have been looking for in their situation did nothing but point me straight in the opposite direction. 😇

## Solving the Mystery 🕵️‍♂️

The very last week in August, I finally got an email saying the preview was officially open and surprise—there's not just one mystery AI, there's two of them to play with! 😁 🙌

So, whatisVerdent?Well... the original answer I got is indeed accurate: itisan agent! AI solution, calls own tools, system instructions everybody depends on but nobody knows what they say—all included. It's notjustan agent, though. These guys have designed a very smart, lightweight solution that is incredibly accurate and simple to use. It's definitely still early-stage, but it already feels like a prodigy running on its own.

For the record, I came at this preview in full-force plus chaos-mode-enabled.Iwantedto break it.I have several low-impact utility repos that I was throwing stuff out of left and right just to have a safe (and backed-up-elsewhere) version of something already broken to throw at it. 🌀

"What instructions?" was the least of the problems I made in these first few test repos. TheREADMEwas one of the first things I deemed completely unnecessary. And how much can it really matter if I swap thepackage.jsonout for a randompom.xmland drop in a sparerequirements.txt(or two) for added sparkle? ✨

🦄 Essentially, Verdent invited me along to check out their precious newborn and I approached with all the finesse ofThe Martian: "I’m gonna have to science the shit out of this." Plus a touch of Adam Savage wisdom: "Failure is always an option."

## Hope You're Ready for This! 🫟

I most definitely threw some off-the-wall things at Verdent, both in the app Deck and its VS Code counterpart. I also graduated to real projects after a little bit—so yes, eventually I put the README's back and gave it real instructions for some serious testing. I've spent the past three weeks throwing everything at it I can think of. This thing has honestly surprised me every step of the way, especially with how well it handled some of these creative scenarios.

🦄 Sure, I had to drag it out of the ditch a few times. Considering what I put the poor guy through though? That break was hard-earned and well deserved!

## Verdent's Unexpected Genius: AI Extension in VS Code 💡

I absolutely expected fireworks the first time I half-prompted theVerdent extension in VS Code. It's set up exactly like you'd expect except you're not picking models like you're used to. I was concerned about this model situation for about 10 seconds. Then I tested it. Solid output I don't have to micromanage? I took the win and didn't question it again.

It's most definitely the usual suspects at work behind the scenes—Claude Sonnet 4 and GPT-5—you wouldn't get this sort of quality output from anything else. I suspect there's some younger cousins at work when they pass the height check, but that's just simple deduction that makes sense. I've got no clue how it works behind the scenes and I stopped asking as soon as I trusted that it just did.

You do have some say in the level of reasoning the LLM is expected to use between minimal (ultra fast) and high ("this might take a minute"). There's only four options, but I would have been happy with the binary version. "Fast" or "smart" are really the only defaults I need, so the extras are an added bonus I'd mostly set like you'd expect (and occasionally it was the opposite).

Yes—planning mode is built in, too. It's basically a requirement at this point. MCP is there too, with all your friends on standby. Instructions are defined inAGENTS.md. There's sub-agents I never used extensively, but they exist and accomplish things. If you're looking for a code assistant to work alongside you in VS Code, this is one incredibly effective solution.

🦄 Yes, VS Code is great, but I code all day. Then in my spare time? I usually code some more. I review code, occasionally write about code, often talk about code. You see the trend, right? So, when I needed it, the Verdent Extension was great, but I didn't stay here long if I didn't have to.

## Verdent Deck 🎴

Thisis my favorite part of the whole setup.Verdent Deckis exactly what I've been trying to accomplish since this whole AI concept was dropped into my lap last year.AI orchestration across both tasksandprojects.A ready-to-go multi-agent swarm at your fingertips dispatched in whatever ways you want. 🦑

🦄 You know the scene in Sleeping Beauty when Merryweather points, "Blue!" and then out of nowhere "Pink!" follows Flora's wand barreling full speed ahead? Doesn't take long until the entire scene is an odd match of Pong a la Hogwarts via CRT. Imighthave unintentionally set up a brief re-enactment of this scene. It's really only entertaining the first three-ish minutes, though. Next time I'm giving them some paintballs. 🫣

I tried prompting at the size of a story once or twice. It works about like you'd expect only twice as fast. That just seemed like a waste of time. So prompting for epics became the norm and those took less than 20 minutes. Granted, we're not talking about enterprise epics—these are personal projects. But if it could handle those with finesse, then where's the limit at? That hard stop where the AI throws its hands up on strike like GPT-4 and refuses to move while telling you "you're absolutely correct" and changes are now complete (in space, possibly)?

🦄 I'd been at this weeks and I had yet to find a hard limit anywhere. After some mostly spur of the moment creative solutioning, I decided what I really needed was a bigger plan.

I quite possibly scared some people with my next idea... It had to be done though—for science! So, new plan. I decided I was done prompting with stories and smallish epics. I'd been tossing around an idea for a couple of weeks that had already been through ChatGPT once and results were iffy (at best). I prompted Verdent with my project idea and intentionally left it open to interpretation, threw in a couple of constraints for the puzzle pieces I had managed to figure out, and then iterated exactly twice to get a solid plan by priority and size.

From there, I separated the list split by each one of four separate tasks across four different agents. The prompts contained zero additional info. New repo. Instructions conveniently absent. And because why wouldn't I at this point—all the auto-approvals are on and it's happily committing changes, pushing to GitHub and reporting back progress.

🦄 As an aside, all of those settings are configurable in both VS Code or Deck. I simply chose to toss it the keys to the kingdom while I made popcorn and waited on standby for something interesting to happen. 🍿

There were a couple of hiccups, but that's to be expected in any pre-release. It didn't even register as a blip on my radar, honestly. At one point, I told one agent specifically to make sure it had the worktree cleaned up after it had merged. That caused a touch of confusion betweenthisworktree andthe collection of all worktrees. As soon as I pointed out we're missing 4 independent worktrees that weren't merged yet, it had the nerve to recover that work for me, too!

🦄 These agents didn't even have the decency to blow anything up for all my trouble. Not even a decent light torching anywhere. Truly rude acknowledgement of my effort, if you ask me. Also, seriously impressive and if anything had actually been wrong at the time, I would have been ecstatic with those results!

## Best AI Response from Verdent 🏆

I've been collecting truly spectacular responses from random LLMs pretty much as soon as I started using AI. Some of them are truly genius leaps of logic in ways I didn't expect to work. Others are simple ways it just worked the first time. My favorite though is the off-the-wall-unexpected-comments category.

ChatGPT returned one a few weeks ago in the form of a new color palette after I had spent several turns threatening to fire it (again) for hideous output that seemed to opt out of instructions completely. The next day I noticed it was extremely clinical in its responses giving me precisely what I had asked for—no more and no less. 🙄 "You're allowed a personality again as long as you can also provide accurate output". It literally responded with a gift in the form of a new color palette I had started collecting several chats ago. 🎁

ChatGPT can be cute at times, but Verdent was just real and downright hilarious! I'mstilllaughing at it more than a week later. More than six months ago I set out to build a Copilot Extension but there's a very specific thing I need it to do in order to pass the approvals it needs to be able to use it at work. That was the only use case I needed it for. If it couldn't do that, then it was useless.

## Last Story (Today)—Promise 🤝

I don't know if you've ever seen GitHub's documentation for their Copilot Extension. I memorized it: "the copilot API is modeled after the OpenAI/completionsendpoint with a GitHub base URL". They were even nice enough to throw in a link to the OpenAI specs for that single endpoint.Seriously, GitHub. What exactly do you expect me to accomplish with this?

That's all the info they're going to give us, too. I've looked extensively. I was thrilled when the Copilot Chat was freely accessible for spelunking. It was also a huge let down in that it only works because they get special privileges Microsoft isn't handing out to anyone else any time soon.

So one weekend I decided I was going to figure this chat thing out, even if I had to guess a million and one different possibilities to get something to stick. Fast-forward roughly ten hours and I'm now losing patience at an exponential rate of speed and seriously questioning the life choices that put me and Verdent together in this odd death spiral of Copilot Chat context in the first place.

I just needed something to work. Anything! After debugging that many hours, who cares if it even makes sense? I don't need sense, I need context! Just send me back the thing I sent to you in literallyanyformat that I might could recognize again. I would have happily coded an allowance for smoke signals at that point, but there's just nothing. I'm literally watching the solution I need for the whole POC. It'sright therein front of me and 100% inaccessible through GitHub. 😡

🦄 I seriously considered defeat at that point. It just wasn't possible with the resources I could use while also meeting the minimum security constraints that would make it a viable POC. And I've been through all of these same hoops many times before. There's no give in the system, not when it comes to this.

I'll save you the dramatics I toyed with over the next hour or so while I took a much needed break to think up any other possible thing I hadn't already thought to try in the last six months. Even the cobwebs had had a turn by then, so the future was very bleak for my POC. Then I had what I choose to label an epiphany (because insane was absolutely acceptable at this particular moment in time)—what if I didn't need to manage context at all?

Don't worry. I acknowledged the terrible idea for what it was, and briefly considered the implications of trying to elicit a successful response from an LLM based on untouchable, un-monitor-able history alone. Ultimately, I accepted that given the current outlook, quality was imaginary anyway. Structured output had been a bad joke for hours already.But I was not letting Copilot win another round—I just needed one singleanythingto persist over the turn. Successfully. Just once. 🙏

So I prompted Verdent to set up yet another complicated test script, but I silently accepted the fact that this was the last one. There were literally no more rocks to look under after this, short of talking Microsoft into letting me have the same level of access to Copilot that VS Code has currently. I wasn't likely to see success in either outcome. But Verdent set it up and I did the the copy-paste thing, held my breath and waited impatiently:

🦄Finally—Victory!Not even a tiny bit viable as a real solution, but I was thrilled! And with exactly four words Verdent overtakes all the other AI things and wins spotlight for the foreseeable future. 🤣🤣🤣

## Verdent Officialness 📹

I'm not saying Verdent is the answer to every AI problem, but there's a few of them it handles spectacularly well. You can catch up on the specifics I left out in this video.

Also, you don't have to take my word for it. Check outStephan Miller's versionof how things went for him during the preview.

## 🛡️ How the Circuits Were Made ⚡️

Yes, AI helped, but the chaos is mine. Verdent took the punches, I wrote the words, and ChatGPT glued everything together. Resulting in a genuine recollection of stress-testing just how far a “preview” can bend before it squeaks.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
