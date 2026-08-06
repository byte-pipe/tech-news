---
title: 'I Recreated Management With AI: 9 Things I Do Differently - DEV Community'
url: https://dev.to/anchildress1/i-recreated-management-with-ai-9-things-i-do-differently-3j8g
site_name: devto
content_file: devto-i-recreated-management-with-ai-9-things-i-do-diffe
fetched_at: '2026-08-07T06:00:24.819774'
original_url: https://dev.to/anchildress1/i-recreated-management-with-ai-9-things-i-do-differently-3j8g
author: Ashley Childress
date: '2026-08-06'
description: I stopped treating permission prompts as the safety system, then spent four and a half months writing 134 standing rules to replace them. Nine things I do differently with AI, and the proof to back it up. Tagged with discuss, ai, writing, productivity.
tags: '#discuss, #ai, #writing, #productivity'
---

Replaced safety prompts with 134 standing rules

🦄 Thanks@francistrdevfor startingthe conversationthat really got me to thinking about this idea in the first place. I started truly working with AI shortly before I started writing these posts a little over a year ago. My thesis was simple at the time: prove that AI was far more capable a tool than what I had seen anyone using it for so far. My proof was strictly gut instinct and I spent a lot of time fighting with Copilot to prove I was right. Not all of those experiments went according to plan exactly, but I'm still convinced I'm right.

That particular ADHD spiral has came and went, and most of it is ingrained as habit. I don't use Spec Kit because by the time it showed up I already had my own version running. I also need to get back to sharing what really works for me. So here we are again. Back to writing (with AI) and the proof to back it all up.

One thing up front, because somebody is going to ask: everything here is personal projects andmy portfolio. There's no critical prod system anywhere in this post, and if there were, a few of these answers would shift. Not all of them — I'd still let AI run a lot further off-leash than most of my enterprise counterparts would. 🐒

## The Org Chart Has One Employee 🪧

I don't just use AI as a tool. I design it as a living system, and I grow the tech as the tech grows.

I ran one prompt across Codex, ChatGPT, Claude Code, Cowork, and Gemini, all separately, and asked every one of them what was actually different about the way I work. Five different systems, each one with its own long history of putting up with me, and not one of them could see what the others said. One came back with this:

I use AI to write code, review the AI-written code, review the review against the live branch, test the corrections, and then record whatever went wrong as a rule for the next AI. Apparently I recreated management.

Most of the private exchanges quoted in this post came out of that same pile, whether they were my own prompts, my memory files, or the arguments my tools had with each other.

## Nobody Needs Me Reading Diffs 🧲

First of all, I've stopped reviewing code changes wherever I possibly can, because I strongly believehumancode review is a waste of resources. AI review is smart reallocation of work to where the work belongs. Does that mean AI always gets it right? No. But two strong adversarial reviews aimed at a targeted change are more likely to catch errors than my tired eyes at the end of the day. Instead, I spend my time designing systems and then verifying and validating the end result. I've cut out the middle-work completely.

When I first designedCarbon Tracefor the WeCoded 2026 Frontend Art challenge, I could see what I wanted it to look like in my head and had zero clues where to start building it. This is coming from the person who threw a neon green rectangle around CSS, argued with its position for a few hours, and then gave up and let the button live off grid permanently. I'm a backend dev, but I don't need to master frontend frameworks to understand them. Code is code and the concepts are the same. So I spoke in backend distributed systems and had AI translate what I wanted to happen into a GSAP orchestration, layered audio tracks, and living animations, all on top of AI art, because my personal artistic ability is on par with my frontend design skills.

I've had three wins across three unrelated stacks:Save the SuntookBest Google AI Usagein the June Solstice Game Jam,Carbon Tracewas named aFrontend Art winnerat WeCoded 2026, andUnearthedwas namedan Overall Winnerin the DEV Weekend Challenge: Earth Day Edition.I didn't spin my wheels hand-coding or reviewing any of them.I designed the solutions. AI wrote the code, and the judges saw the engineering work regardless.

## 1. I Separate AI's Roles and Permissions 🪪

Three of my own sentences, from three different days:

fix all issues. do not commit yet.

fix all. commit. do not push

I did that already. do not post for me

Push triggers a whole pipeline of GitHub Actions checks. When AI pushes after every single commit, those pipelines run more than they should and my bill goes up. More reviews happen when I wasn't ready for the work to be reviewed yet, and it slows down the fast iterative process I've become used to.

So it's written down as a permission model instead of a preference:

Nevergit pushunless the user asks for it in that message. One "push" authorizes exactly one push. Permission is never standing.

That one line is the small version of a much bigger swap. My default setup accepts edits without stopping, and when I deliberately use bypass mode, I skip its warning too. I don't build the workflow around approving every small action one at a time. That does not work when the agent is running and I'm not sitting there. What I have instead is closer to a blacklist, where everything happens unless I've already forbidden it, and the moment I pulled the whitelist out, every gap I hadn't thought of turned into something that could happen. Every one I found the hard way became a rule.

Those 134 standing rules aren't a preference log. They're the safety system I had to rebuild after I unplugged the default one.

## 2. I Use AI to Review AI-Assisted Work 🪤

It is very rare that Codex, Copilot, and Claude all disagree. They just see different things, which is what makes the AI review from multiple tools so valuable. Copilot is more nit-picky with the little gaps that would cause big problems down the road. Codex and Claude take differing views on the same problem and can usually reach a fair solution without my help. Occasionally I have to referee, but then it usually becomes a design decision or a question of priority.

The best example I have is sitting in theCarbon Tracereview logs from earlier in the year. Codex flagged that frame 0 was rendering before the overlay systems finished initializing, and Claude pushed back on it, because the presence checks already sitting in that path covered it and nothing else needed to change. Codex didn't back down:

Claude is half-right, but on the wrong axis.

Claude had checkednullhandling. Codex was looking at a lifecycle invariant nothing was enforcing. If frame 0 ever declared an overlay, that load would fail quietly and there'd be no replay to go find it in.

Same seatbelt, no airbags.

The branch gotfix(perf): enforce frame-0 overlay invariant at startup, and the rereview backed it up with a runtime invariant, a note in the performance ADR, and passes on unit, browser, lint, Lighthouse, and the full performance orchestrator. Codex's concern held up. Claude's guards were real, they just weren't covering the thing Codex was looking at.

If you use a second reviewer, give it the branch and the risk, not the first reviewer's verdict. Otherwise you've built agreement with extra steps.

## 3. I Restart Instead of Repair 🪞

STOP iterating on broken.

I already wrote this one downback in May, as general advice for everyone:

9. Clear the context. Don't iterate on broken. 🪦

If you've told the model the same thing three times and it's still wrong, then assume your conversation is poisoned. Too much wrong-direction is already baked in. Open a new chat. Start fresh with what you've learned.

A clean context with a sharper prompt beats six more rounds of "NO! I already said..."

What's changed since then is how far I take it. When we lived in the realm of GPT-4, we had to hold AI's hand to accomplish anything of value. GPT-5.6 does not have the same requirement and neither does Claude 5. Pretending they still need that level of hand-holding wastes time I don't have. I can redesign and recreate cheaper than I can modify with AI, so throwing away a whole frontend approach after a couple of days is cheap work. Fighting with AI for another week to fix something that was broken from the start is a trap.

The model choice gets made once, at the start. I rarely escalate to a larger model when the current one is struggling, because by then I'm paying more for a conversation that already went sideways. I decide what the work is worth before I start it, and then I live with it or start over.

Scale

Repair (the trap)

Restart

Chat

follow-up prompts patching a bad premise

/new

Code review

arguing down a comment thread built on a misread

re-review from scratch, no inherited verdict

Feature

iterating on something that started broken

cut it, try a different approach

Approach

a week of wrangling to rescue it

throw out the frontend after two days

It's not really a counter, though, because what I'm actually weighing is whether losing the whole chat costs me less than/newdoes, and usually that means the design and planning I've got banked in that thread just aren't worth what's gotten baked in around them.

Is it cheaper for me??It feels cheaper.It's faster. It brings back the feeling of progress when being stuck spinning your wheels on the same problem is getting you nowhere new.

Likewise, forUnearthed, I tried and failed to come up with a design two separate times before Claude Design launched and saved the day. The fact that I chose to scrap yet another frontend approach two days before the end of the challenge was besides the point. I knew AI could do it better than me, so I let it.

Pick your own restart trigger before you're angry enough to keep arguing out of spite. Mine is three failed corrections or one broken premise that poisons everything after it.

## 4. I Write From Outlines, Not Generated Drafts 🪜

When I blog, I always start with an outline. My brain doesn't much cooperate with A > B > C style logic and writing doesn't change that. I need something closer to A > Q > X > R.2 > D.2 > Z and it helps to keep my interest-orientation on task through to completion. AI lets me write in the chat and then it cleans up my language a bit (you're welcome?) and organizes it into a form that the general population can actually follow. I used to do this by hand with manual copy/paste. It's tedious and would take me many hours just to write a post in a form that could be edited later. Now Claude or Codex handle the task for me, depending on what it is and which I'm more mad at on any given day.

In addition to the outline and quiz-me-as-we-go style of writing, I have very specific skills written that mimic my writing style with examples, dialect references, sentence structure, and explicit banned words and phrases that would never come out of my mouth on a regular Tuesday.

One of those rules is written exactly like this:

Don't chainsaw long sentences for "readability." Long, comma-spliced, em-dash-bound flowy compound sentences are how Ashley talks; breaking them into short staccato beats strips the voice.

Another one bans startup-landing-page filler likeseamless user experience. Those rules aren't there to teach AI how to invent me from scratch. They're there to keep it from editing me out of the material I already wrote.

That keeps my posts mostly written by me and still completely constructed by AI. So no, the two are not necessarily mutually exclusive.

## 5. I Make AI Interview Me When Facts Are Missing 🪶

My whole spec was "copy screenshot doesn't work on dev." Claude guessed at what I meant, built a clipboard fix, and shipped it. I told it what I thought:

i think you're fixing the wrong problem

Then it asked the question it should have led with:

Two readings of "copy screenshot doesn't work on dev," and they lead to completely different fixes:

1. "dev" = your local dev server. Then it's the clipboard thing I just fixed — but there's no button called "copy screenshot," only Copy image URL and Copy README embed, so this reading is already shaky.
2. "dev" = dev.to. You asked me to optimize the embed view for that site an hour ago, so this is probably it. And the likely culprit is completely different: the card is an SVG. Forem proxies images and SVG support is unreliable... That would be a rendering/format bug, not a clipboard bug, and the fix is a PNG, not execCommand.

Which is it — and what exactly did you click, and what happened?

It was the second one. The SVG rendered fine in a browser and it did not render on dev.to, so the real fix was server-side PNG rasterization and every bit of the clipboard work was wasted.

It wasn't caution that made it stop and ask, either. It was one word.Devmeans two completely different things in my world and both of them were live that same hour, and the two readings didn't point at slightly different work, they pointed at different layers entirely with nothing from the first one surviving. If both readings would have gotten me to the same place it isn't worth asking. If they fork the work, it always is.

That failure became a permanent rule:

your job is to challenge the user and ask questions to clarify intent not guess at meaning and consistently get it wrong.

I wrote the opposite rule too:

The user does NOT want to be asked which color/value to pick... Do NOT ask the user to choose. Deliver finished, then let the user react.

Both are real, both are permanent, and they contradict each other. The thing that separates them is what kind of unclear I'm dealing with. Ambiguous taste gets decided, because asking me to pick a hex code is design by committee and I banned it. Ambiguous meaning gets a question, because deciding is guessing and I banned that too. Which teal is AI's call. Whichdevis mine.

## 6. I Turn Corrections Into Permanent Rules 🪛

When something goes sideways and the result is unexpected, even if it's good, unexpected is still a failure. Either AI will go and find out why something happened, or I'll update the ongoing memory—either for the project or for my user at large.

I make the call. The model writes the file:

update your permanent memory for this user. that is always true.

update your memory. when I say commit, that means commit with -s ONE TIME PER COMMIT REQUEST, never an ongoing rule

In one snapshot, there were 134 of those rules, and 119 contained an explicit prohibition:never,do not,stop,forbidden, orprohibited.

push-only-when-explicitly-told
no-unverified-pushes
never-ask-to-remove-dead-code
dont-decide-ux-unilaterally
feedback_silence_is_acceptance
jsdoc-must-not-restate-the-signature

Enter fullscreen mode

Exit fullscreen mode

Somebody will undoubtedly read that as 134 times the AI screwed up. I see 134 tweaks I made to the system I'm actively building. Even when we're the ones writing the code by hand, you still have to debug it. Things are still wrong, they're just wrong in a different way. This is my version of debugging and tightening the system as I go to get to a more accurate answer in the end. That isn't time wasted, it's time building. I'm just building a different, more long-term system.

Occasionally, I'll stop and review all of those memory files, meaning I really have AI self-audit its own memory to identify things that are no longer true, genuine contradictions that need larger decisions, or things that are no longer relevant. I stopped manually trimming every file as the agents got better at self-monitoring and selecting relevant memory.Thanks Anthropic, I recognize the work, but we're not all the way there yet.

In near every scenario, omission is better than correction. I keep the focus there whenever I can, whether it's in a prompt, a memory update, or any other sort of iteration.

## 7. I Require Proof Beyond "The Tests Passed" 🩻

Unit tests and integration tests are written against the code. And that's the problem with them. A test built around the same mistaken assumption as the implementation can pass while proving the wrong thing.

I find a bug in the implementation that I can see, then a new test gets written. That test I'm more likely to trust. Tests written from the spec and not the code get the same deal.

The clipboard failure is a clean example. Claude could have written a complete test suite around the clipboard fix and made every bit of it green, and none of those tests would have proved that an SVG rendered on DEV, because it was testing the wrong layer. The real proof was a server-side PNG rendering in the actual place it had failed before.

Green tests alone aren't enough anymore, because it's too easy to miss all the other green lights that go into making the codebase secure and reliable. So everything else gets looked at too, including fixtures, live records, contracts, consumer artifacts, runtime output, and whatever malformed input I can use to break it.

## 8. I Use AI to Tell Me When Not to Act 🛟

Sometimes the correct output is no message, no rewrite, no push, no post, and no additional cleverness.

I asked what I could send and got told I'd already said it:

that's basically already been said. so no message

The technical version happened onrai-lint. I wanted the repo calledrai-lint-badge, and Claude argued against it:

It parses wrong. rai-lint-badge reads as "a badge for rai-lint" — the same shape as npm-version-badge or build-status-badge, where the thing before "badge" is the subject being reported on... Naming it after the linter welds it to one implementation of a standard you'd probably rather see spread.

Then it didn't drop it. Two messages later, unprompted:

Name still open. I argued against rai-lint-badge on the parse... better to decide before anything is pushed.

I took it, because the logic made more sense to me than I disliked the name. What shipped isRAI Commit Attribution Badge, backed by therai-commit-badgerepo, so that argument is load-bearing in a public artifact and anybody can go look at it.

The purer version ismetal-birds-feed, where I asked for a feature instead of a name: auto-adjust the parser based on the error. Claude wouldn't build it:

Every other drift guard in this codebase... follows the same pattern: fail loudly with a specific error, human updates the config... We'd trade "CI job fails, someone looks in 5 minutes" for "aircraft records are subtly wrong and nothing tells you."

ok. leave it. we'll see if it happens again

The feature was never built. That one worked on me because it didn't argue from some general principle, it argued from my own codebase, where every other drift guard already fails loudly and it wasn't about to let this one be the exception.

What I actually want isn't the refusal. It's that it wouldn't let it go.

## 9. I Mine My Own History for Things I Never Wrote Down 📼

I wanted a proof of concept before I started writing this post — or before I had AI write for me. I inherently know that I use AI differently just based on what I see of other people using it. I just wasn't able to identify what it was outright. So I had AI figure that part out for me.

It went looking through my own chat history.

I don't let the archive decide what happened. It gives me where to look, then the rule files, repositories, and public pages have to verify it. The first answer is a lead. It does not get promoted to a fact just because an AI said it confidently.

Skills andAGENTS.mdare the memory I built on purpose. The chat logs are the part I was never trying to keep, and they turned into memory anyway, the first time I needed something dug back out of them.

It's not a theory, either. When I had Claude edit my card-writing skill I told it to pull from prior sessions before proposing anything, and it came back with two failure modes that existed nowhere in any spec. Writes were failing silently on an expired auth token, in a way that looks exactly like the tool refusing the content, and it had been padding tags I explicitly dictated with extras of its own. Neither one was documented. Both were sitting in old conversations.

Nothing I've said to any of these systems turned out to be disposable.

## Nobody Asks Me Anymore 🧭

None of this made me faster. It moved the deciding earlier, which is a different thing entirely, and every rule in that pile exists so a call I already made doesn't have to get made again at midnight by something that doesn't know what I meant the first time.

Apparently that's management. I'd say it's closer to refusing to have the same argument twice, but the org chart disagrees.

## Ashley ChildressFollow

Distributed backend specialist. Perfectly happy playing second fiddle—it means I get to chase fun ideas, dodge meetings, and break things no one told me to touch, all without anyone questioning it. 😇

## anchildress1/awesome-github-copilot

### My ongoing WIP 🏗️ AI prompts, custom agents, skills & instructions - curated by me (and Copilot + ChatGPT).

# awesome-github-copilot 🔭

 
 
 
 
 
 
 

Note

So my original idea of making all this directly accessible through a Copilot Extension hit a wall — a few walls, actually
GitHub recently announced thesunset of that functionalityin favor ofMCP.

Thegithub/awesome-copilotrepo already supports MCP (plus installs into VS Code and Visual Studio), so I’ve started moving some of the more stable pieces there.

This repo will still get the newest experiments first, but the “official” ones will live upstream.

Got questions or ideas? Feel free to reach out — socials are on my profile. 🦄

Welcome to my collection ofCustom Instructions, Prompts, and Agents (formerly Chat Modes)— your one-stop shop for uniquely crafted, slightly over-caffeinated GitHub Copilot personalities. Built for creative chaos, workflow upgrades, and the occasional emergency refactor.

Each mode here is handcrafted by me, with ChatGPT running background triage and Copilot chiming in like a backseat…

View on GitHub

## 🛡️ Performance Review of the Only Employee

Claude did the cleanup and counted the rules it had spent four and a half months getting itself written into. Codex fact-checked the pile, and ChatGPT, Cowork, and Gemini each filed a separate report on what's wrong with me. This footer was composed by the employee it evaluates, which is either extremely efficient or exactly the problem. Rule 135 will presumably cover it.

Yes, AI wrote this article. I researched and staged the competition. This post is the output proof you should be asking me for.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse