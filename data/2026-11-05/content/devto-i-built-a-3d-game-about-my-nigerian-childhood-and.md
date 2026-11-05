---
title: I built a 3D game about my Nigerian childhood (and I'm not a game developer) - DEV Community
url: https://dev.to/deborahemeni1/i-built-a-3d-game-about-my-nigerian-childhood-and-im-not-a-game-developer-281g
site_name: devto
content_file: devto-i-built-a-3d-game-about-my-nigerian-childhood-and
fetched_at: '2026-11-05T15:23:47.677267'
original_url: https://dev.to/deborahemeni1/i-built-a-3d-game-about-my-nigerian-childhood-and-im-not-a-game-developer-281g
author: Deborah Emeni
date: '2026-11-02'
description: If you grew up in Nigeria, there is one sentence that can stop your heart in the middle of... Tagged with gamedev, webdev, ai, showdev.
tags: '#showdev, #gamedev, #webdev, #ai'
---

Relatable errand mechanics and community praise

If you grew up in Nigeria, there is one sentence that can stop your heart in the middle of cartoons:

"My pikin, come o."

You know what's coming. An errand. Go and buy bread. Go and buy salt. Go to Iya Toyin's shop, andcount your change o.And as you're walking out of the gate, you hear the final warning:

"If I count this money and one naira is missing…"

So I did what any normal adult would do with that memory. I turned it into a 3D game. 😂

## So what is Pikin Days?

Pikin Daysis a free 3D browser game where yourelive your Nigerian childhood, one memory at a time.Each episode is a different slice of growing up.

Episode 1 is "Hold Your Change": run errands for the family and bring back thecompletechange. You pick your child, pick who is sending you (Mama, Papa, Grandma, Aunty, Uncle…), and off you go.

On the way you have to:

* find the right shop and buy therightitem (salt and sugar are not the same o!)
* count your change, because sellers are not always honest
* dodge okadas, kekes and buses that are not slowing down for anybody
* run fromBingo, the neighbour's dog who has never liked you
* decide if you'll stop and play football with your friends… while Mama's patience is running out
* get home before she sends someone to come and look for you

At the end, Mama gives you atrust rating. I got a C on my own game. Mama said,"Was it for tomorrow I sent you?"I felt that. 😭

## Why I built it

Honestly? Nostalgia, and curiosity.

The memories in this game are ones many Nigerians share, especially those of us who grew up in the 90s and early 2000s: the kerosene lantern when NEPA took light, everybody shouting"Up NEPA!"when it came back, the secret spoonful of powdered milk and the white lips that gave you away. I kept thinking:what if you could walk inside those memories?

The other half was curiosity. I write about developer tools for a living. I explain how things work. But I had never built something like this end to end, a real 3D world in the browser that real people play, and I wanted to know what that actually feels like from the inside.

Spoiler: it feels like joy, panic, and a lot of testing on your phone at 6am.

## How I built it (without being a game developer)

Here's the stack:

* Three.jsto build a living 3D Nigerian street (the stalls, the people, the okadas, the goats) that runs right in your phone's browser, no download needed
* Mixamofor the character animations. I went in myself to choose and fit every walk, run and reaction, so the kids move like real kids
* Rapierfor physics, so the child doesn't walk through walls or get trapped behind the bread seller's table (more on that later 👀)
* Vite + TypeScriptfor a fast, typed codebase that could keep up with daily updates
* ElevenLabsfor the voices: Mama, the sellers, and the drivers shouting "Comot for road!" Honestly, this part was stressful. Getting the voices to sound truly Nigerian took so many tries, and a lot of takes sounded more London than Lagos 😅 I listened to every single line and kept only the ones that felt right
* Astatic site with a serverless backendfor game stats, player votes, feedback and a private admin dashboard I use to see where players drop off

And the most important part of the workflow:I built it with an AI coding agent as my engineering team.

Now, before anybody says "so the AI built it": no. The agent typed a lot of the code, the way a calculator does a lot of the maths. But it didn't decide what to build, how it should feel, or when it was good enough. That was me.

Here's what my side of the work actually looked like:

* Designing the game.The errands, counting your change, Mama's patience running out, the trust rating, Bingo, the friends' games that tempt you off your errand. The idea, the rules and the feel of it all.
* Making it feel Nigerian.An AI doesn't know that a seller says "thank you, go well"afteryou buy, not before, or that "Comot for road!" hits different from "Please move." Every street detail, voice line and memory went through me.
* Writing very precise instructions.Not "make the camera better", but "when the child turns, the camera must follow behind them quickly; one-finger drag only turns the view and never zooms; most players are not gamers." Turns out a technical writing background is a superpower here.
* Setting the rules.No real brands. No adult is ever hostile to a child. Children are never shown doing heavy labour. Nothing goes live until I say the word "push".
* Running releases like a real product.Preview links for every change, version numbers, rollbacks ready, a stats dashboard locked behind secure sign-in, and beta testers before big updates.
* Testing like my life depended on it.On my phone, in different browsers, inside different apps, held upright and sideways.
* Asking for proof.This one I learned the hard way. "Done" and "done and verified" are not the same thing. So I started asking for screenshots and screen recordings of every fix, plus an honest table of what wasverified, what wasnot verifiedand what washidden.

It felt a lot like being a product manager, a game designer, a QA tester, a writer and a very strict Nigerian aunty, all at once.

## Launch night: we broke the free tier 🎉

I posted the game on X, went to bed happy, and woke up to my stats dashboard throwing errors.

The reason? People were actually playing, and on day one I'd hit my hosting provider's free limit of1,000 database writes a day. Every game start, every vote and every bit of feedback was a write. I upgraded to the $5 plan, made the dashboard read without writing, and batched the counts.

Was it annoying? Yes. Was it also the best problem to have on launch day? Also yes. 🥹

## The bug that was hiding in plain sight

A few days after launch, a player messaged me: the game was stuck on"Turn your phone sideways to play". Even after turning their phone. Since launch.

And here's the crazy part:I had seen this myself.I'd opened my own link from X, got the same screen, tapped "Open in browser", and moved on. I genuinely thought it was just my phone.

It wasn't my phone. It was everybody.

When you tap a link inside X, TikTok, Instagram or WhatsApp, it doesn't open in Safari or Chrome. It opens in the app's own mini browser. Many of them never rotate, or they rotate but never tell the page it happened. My game was waiting patiently for a "the phone is sideways now" signal that was never going to come. So people were stuck at the door.

My dashboard had been trying to tell me too. There were188 bounces on the title screen. People came, got stuck, and left without saying a word.

That taught me two things I won't forget:

1. If you hit something weird and work around it, your players will hit it too, and most of them won't know the workaround.Your little workarounds are clues.
2. Most players don't report bugs. They just leave.For every person who messages you, assume many more quietly closed the tab.

The quick fix was to check the screen's width and height every half second instead of waiting for a rotation event. Therealfix was bigger: rebuild the game to playupright. If the game works holding your phone normally, it doesn't matter what the app's browser does.

Before, held upright, the game was squashed:

After the phone-first rebuild:

## What the players (and the numbers) told me

In the first week:140 games started and 40 new players, and that's not counting most of launch day, when my stats were the thing that broke 😅. It also doesn't count everyone who never made it past the title screen because of the sideways bug. But of those who did play, only31%finished the first errand, and only2 gamesmade it through a full day of errands.

Ouch. But useful ouch. Combine that with the feedback and the picture got very clear:

* "The conversations are too slow."
* "I got stuck behind the bread seller's table and had to leave the game."
* "When I lost my money and found it, going home was the only option, but my time was running out."
* "My energy wears out too fast."

Some of these weren't just annoying, they were blockers. If you get stuck behind a table with no way out, you don't send feedback. You close the tab.

And whenIsat down and played for an hour on my phone, I found even more:

* the seller said "thank you, go well" before I'd even bought anything
* a driver shouted three different lines at me, back to back, while I was standing at a table, not even on the road
* a goat walked straight through the wall of a gutter 🐐
* my friends invited me to play police and thief, said "oya let's go!"… and then we all just stood there
* football was being played on top of the suwe grid
* running out of time sent me on theexact same errandagain, with the same list and the same shop. That one hurt, because the whole point of the game is that every errand feels different

So I made a few rules for myself that I'd now apply to any product:

* One message on screen at a time.Ever.
* Max about 12 words on a card.If they have to read, they won't play.
* No pop-up bigger than ~60% of the screen.
* A player must never be stuck, confused, or overwhelmed.Not for one second.

## The update: share your funniest moments

The newest update plays upright, opens properly from any app, follows you with a smoother camera, gives drivers their own (very dramatic) voices, and lets you save your funniest moments as short clips: Bingo chasing you, a close call with an okada, coming home late and facing Mama…

…and then share them straight to WhatsApp, TikTok or X.

## What I learned

If you remember nothing else from this post:

1. Test where your users actually are.Not on your laptop. On a phone, from inside the apps people will share your link in.
2. Your dashboard is your quiet users talking.Bounces and drop-offs are feedback. Read them like messages.
3. If it feels weird to you, it's broken for them.I worked around a bug myself and assumed it was just me. Your little workarounds are your players' dead ends.
4. Working with AI is a skill.Be specific, set rules, and ask for proof. "It says it's done" is not a test.
5. Never ship what you haven't touched.Preview links, a quick play on my own phone, and a rollback ready every single time. The one time I rushed, I got a squashed game on live.
6. Ship, then listen.I found more in one week of real players than in weeks of building alone. Finding a big bug days after launch isn't failure; that's exactly what an MVP is for.
7. Make it personal.The bits people loved most were never the tech. It was Bingo, "Up NEPA!", and Mama's report card lines.

## What's next

Players get to vote on what comes next in the game, and"Up NEPA!"is currently winning with 60% of the vote. 💡 So yes, there will be a light-is-back moment. Also on my list: more errand types, more friends' games (suwe is coming back once I get the hopping right), and more memories to collect.

It's been a busy few weeks, so I'm taking a short break before the next update. But the game is live and free to play.

👉🏾Play Pikin Days:pikindays.com

And tell me in the comments:what's the most nostalgic thing you remember from your childhood errands?Mine is the walk home, counting the change three times, praying the seller didn't cheat me. 😅

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse