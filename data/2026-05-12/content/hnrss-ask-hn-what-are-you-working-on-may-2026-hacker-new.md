---
title: 'Ask HN: What are you working on? (May 2026) | Hacker News'
url: https://news.ycombinator.com/item?id=48085993
site_name: hnrss
content_file: hnrss-ask-hn-what-are-you-working-on-may-2026-hacker-new
fetched_at: '2026-05-12T06:00:47.077084'
original_url: https://news.ycombinator.com/item?id=48085993
date: '2026-05-10'
description: 'Ask HN: What are you working on? (May 2026)'
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
Ask HN: What are you working on? (May 2026)
253 points
 by 
david927
 
1 day ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
930 comments
What are you working on? Any new ideas that you're thinking about?
 
help

mizzao
 
4 minutes ago
 
 | 
next
 
[–]

A skills-based personalized learning platform: 
https://parsnip.substack.com/p/knowledge

We started this because we were buildinghttps://www.parsnip.ai/, an app to help people learn how to cook. But then that became a bit of a yak shave because we realized we first had to figure out how to teach people different skills at different times all starting from different places, and also needed to help fund the creation of the app.We ended up generalizing the platform to education in other domains (K-12, higher ed, workforce) as B2B2B "AI learning infrastructure" but still have our cooking app which is also starting to take advantage of this R&D finally coming to fruition!

reply

druskacik
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

European night trains search engine. The plan is not to provide the functionality where user searches for a specific route on a specific date and the engine returns prices. The plan is to provide "tips for trips", e.g. I provide a starting city and it will recommend me interesting trip ideas any time in the future. There are many flight apps that provide this functionality, but no train app.

Currently I'm building scrapers for all relevant provider, then I want to connect the data for multi-city trips recommendation. Plus some connection to the day trains so that the trips are built more easily.Some existing trip recommendations:Prague <-> Amsterdamhttps://trainbot.eu/?from=prague&to=amsterdam&type=returnBerlin <-> Parishttps://trainbot.eu/?from=berlin&to=paris&type=returnZurich <-> Budapesthttps://trainbot.eu/?from=zurich&to=budapest&type=return

reply

jll29
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Now you if you wanted to visit the best city in the world (Edinburgh), you could of course take the 
Caledonian Sleeper
 night train from London up to the Scottish capital; but then you would completely miss out on the beautiful views of the country and the sea.

This case perhaps merits a hard-wired message "for this trip, we recommend a day train, or we'd regret you'd miss the panoramic views".

reply

madman_dev
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is awesome, I would list it on 
https://only-eu.eu
 , if that's ok for you?

reply

druskacik
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sure :) Thanks.

reply

medvidek
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

For some reason Prague -> Bratislava trips are only shown with departures at 00:36 even though there are several through cars that leave Prague at 21:58 (and join the rest of the listed NightJet in Breclav), which is much more comfortable for your average traveler. Ceske drahy website has both connections, so maybe you aren't scraping it yet?

reply

druskacik
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hm, thanks for the tip, I didn't know that. I scrape NightJet website, which lists only the 00:36 train. I'll look into it.

reply

mdibiase
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Would be nice to add Milan as a destination. I currently do not see it listed in the cities available.

reply

druskacik
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have a working version of Trenitalia scraper (Intercity Notte trains across Italy), I just haven't added the routes to UI before verifying it works reliably. Hopefully I'll add it in the evening.

Also the Milan - Brusells route from European Sleeper, it's scraped but not yet in UI. I'll reply here when it's done.

reply

druskacik
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Added, but just the Milan - Brusells route from European Sleeper so far.

https://trainbot.eu/?from=milan&to=brussels&type=returnThe 20€ Milan - Zurich tickets also don't look bad, but the early-morning departure / evening arrival are probably not that optimal.https://trainbot.eu/?from=milan&to=zurich&type=return&seat_t...EDIT: note, this route will be available from September.

reply

jo-m
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

cough
 that name is already in use ;) 
https://github.com/jo-m/trainbot

reply

druskacik
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

sorry about that :)

reply

jo-m
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

no worries, it is mostly unmaintaned now.

reply

karlosvomacka
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

530 eur for return train from Prague to Frankfurt? I guess the reason why there aren't any train apps is that traveling by train seems useless at these prices... :(

reply

druskacik
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's the Prague - Zurich NightJet that's hellishly expensive, possibly because the target audience are Swiss people for whom it's not so much :D Also, NightJet does not price very dynamically as opposed to other providers, and their baseline price is always quite high.

But yes, in most cases this journey will be more expensive that an alternative flight, which is a shame. However, there are routes where it's comparable, e.g. the Prague - Amsterdam route.

reply

chaghalibaghali
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I love this idea, it’s always surprisingly difficult to find what routes are available, what cabins they have, how much tickets are etc.

reply

nerdomancer
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Brilliant idea! Please keep on building.

reply

outside1234
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Thank you for building this! I might be holding it wrong, but I would like to be able to search for all night trains from a particular origin. Is that possible?

reply

druskacik
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Currently not possible, but:

- once you fill the "From" field with your start city, the "To" field will include only cities reachable from the "From" city- athttps://trainbot.eu/coverage/you can search for all routes that go through your cityI plan to add a subpage for every relevant city with recommended routes once I'll have enough data. Something likehttps://www.seat61.com/but with actual prices and dates.

reply

wwwkieran
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

We're working on Drawers (
https://drawers.computer
), a macOS app to give each of your projects its own dock, space, and windows.

We integrate with macOS spaces to switch out a project-specific dock on each space, containing only the resources you need for that project. We made it possible to add granular resources instead of full apps to the dock (think specific slack channels instead of the whole slack app), to keep the dock hyper focused on what you need.We built this to stay focused while working on the computer, and we thought that the native interface mixed all our projects together, causing us to get distracted.Looking for beta testers! Free download fromhttps://drawers.computer

reply

da-x
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Since 2022 I have coded something similar for myself, only for Linux for each of my notes, e.g. each and each every small or big task gets its own bundle of things that are attached to its 'task note'.

Each note gets a wholesome 'virtual desktop' "space":- A markdown file (in a Git repo for all my notes)- A working directory for project files- Virtual desktop in hyprland that opens up as a 
terminal/browser split- The terminal spawn a restorable tmux session where I edit 
the markdown file and open related terminals, where the note's workdir has its own `bin` directory in $PATH.- Also, an ironbar widget showing the name of the current note at the bottom of the screen.- Time tracking app to remember how much time I worked on each note.And they are all bundled up together with save/restore capability, kinda like a VM, but on the application level. The idea is to support multitasking and never lose focus.

reply

jll29
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I love that idea, and had a similar one once (never realized), because I run many projects at once (and more than one role: personal / job_1 / job_2).

What I'd suggest is that you isolate the project spaces from one another so that a e.g. a Web browser crash caused by one project space cannot drag down the rest. BTW, I'd pay for this!Keep building.

reply

BrandiATMuhkuh
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's epic. Will try it ASAP.

Was look for exactly that (but for Features). currently I'm using superset.sh which works great. But the problem is that such tools need to re-implement everything (browser, terminal, etc.) while a "VM-like" approach doesn't.It is possible to "clone" a drawer that auto starts server, browser, etc. So I can start new PRs quickly and jump between them while the agents run in the background?

reply

vintagedave
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is really neat. Is there a way to handle the one app, with one window, being used for multiple tasks?

For example, I have Codex running doing two things at once, and I wish I could have two windows in two spaces (two projects.) Slack has multiple channels.Both these aren't native macOS apps but I wonder if you can use the macOS tabbing support to at least get this for well-coded native apps?

reply

Cilvic
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Super cool, I'm not on mac so I can't try. But I work on something similar for niri on linux. Trying to keep my projects separate.

One additional level I see appearing are the worktress when having multiple AI agents run in paralell. So while they belong to the same project, each worktree has theire own ide + browser etc.

reply

gottagocode
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Incredibly clean website, refreshing to not see the default AI ui.

reply

jvwww
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've always wanted something like this. I will be testing this out!

reply

betobetinabro
 
23 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nice!! been wanting ti build something like this since I got a mac - never did - glad you did.

Does it have project context within apps (like default folders and settings)?

reply

wwwkieran
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yep! Each Drawer (project) has its own folder path. We have integrated apps like Figma, WhatsApp, Messages, and Slack to keep them focused on one project.

Would love to hear what you think we should add next!

reply

Malp
 
23 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This looks great, will beta test over the coming weeks.

reply

wwwkieran
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! Would love to hear your feedback!! You can email us at hello [at] drawers.computer

reply

berta
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds really interesting. I'll give it a try

reply

pmcarlton
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Looks very interesting, and your page makes the case very well.

reply

HaloZero
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Is it free for now? This looks like a huge solve to a problem

reply

replwoacause
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Smart idea, can’t wait to try it

reply

philipnee
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

seems.. interesting. will definitely be interested in testing this.

reply

avenger176
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Any plans on open sourcing? This is really useful for me but I'm not comfortable giving full access to my mac

reply

grepfru_it
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is KDE activities. Install the latest version then you can setup environments based on your activity. Been a feature since (checks notes) 2008.

reply

han1
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

MacOS people really will pay for just about anything. Actually, it appears that they PREFER to pay.

reply

paulhebert
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m continuing to work on my daily puzzle game Tiled Words!

https://tiledwords.comForbes just wrote an article about it which was a fun surprise! [1]It recently turned 6 months old which is wild to me. My wife and I have made a new puzzle every day for half a year! I wrote a blog post about this [2]I recently released user logins. That went well and a lot of people are using them. I also let you filter the backlog by completed puzzles based on player feedback.This week I’m going to start releasing player submitted puzzles and release my puzzle building tools. You can watch a video for a sneak peek of those tools. [3]1.https://www.forbes.com/sites/barrycollins/2026/05/02/bored-o...2.https://paulmakeswebsites.com/writing/six-months-of-tiled-wo...3.https://m.youtube.com/watch?v=d8_zhMKd0Yg

reply

danparsonson
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

Thank you for Tiled Words which I play regularly! I introduced it to a couple of friends and now they compete every day for the best time to finish :-)

While you're here if I could make a small suggestion - the wording of the 'type of' questions was confusing to me until I got used to it; 'stop' is not really a type of 'watch' for example, so maybe you could find a different way to phrase those? Maybe there isn't a neater way to encapsulate the idea of 'is a prefix or suffix to', I don't know, but I found it difficult. Anyway kudos to you and your wife, it's a great game!

reply

codebje
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

To me a "stop watch" is a type of watch, that's straight forward. But there are other clues that rely on cultural references I'm not familiar with - and that is, I think, inevitable in this type of game. We all have different backgrounds and there's no universal shared understanding that would make every clue the same difficulty for everyone.

I saw someone on here recently say they like to do the puzzle without looking at the clues, and I've started doing that on and off too, it changes the game in an interesting way.

reply

danparsonson
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> To me a "stop watch" is a type of watch

Right but the answer in this case is not "stop watch" - the answer is just "stop". Name a type of watch: "stop".> I saw someone on here recently say they like to do the puzzle without looking at the cluesYeah I do that sometimes too, especially finishing off can be easier that way

reply

paulhebert
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Hey, that’s awesome, thanks for playing and sharing it!

Great feedback on the “type of” clues. I’ll need to noodle on that and see if there’s a clearer way to express it.
Maybe I should just be doing blanks… e.g. for “sun” it could be “___ dress, ___day, or ___ flower”

reply

mmclar
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

IME crosswords traditionally say "Word before...". Also thanks for the game, I love it and was excited you used one of my submitted clues a few months ago.

reply

paulhebert
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Oh interesting. I’ll look for examples of that. If that’s an existing convention that may be the way to go.

Thanks for submitting clues! I always like reading through them to make the community puzzle

reply

danparsonson
 
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

Yeah that would work! Or @progbits' suggestion of "goes with" works for me too.

In any case thanks for your consideration and thanks again for a great game!

reply

paulhebert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Awesome, thanks for the feedback! Very helpful

reply

progbits
 
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

How about "Goes with dress, day or flower"?

reply

paulhebert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ahh yeah, that's interesting thanks. I think the one difference is it's not clear if sun is meant to come before or after the word but maybe that's okay.

I'll think on this and experiment. Thanks

reply

UansaS
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Great game. I've been mulling over how to make scabble game with a twist, and I think you achieved this beautifully. Congratulations!

reply

paulhebert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! I'd be interested to see what you build if you continue with that! I think there are lots of interesting ways to spin off of Scrabble

reply

gottagocode
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Fantastic, the scrabble lover in me will enjoy this.

reply

paulhebert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! I played a lot of Scrabble growing up at my grandma's house so it's definitely an inspiration

reply

juvvel
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I love Tiled Words, thanks for making it.

reply

paulhebert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for playing!

reply

right-words-dev
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This has had me hooked for weeks! Really delightful game. :)

reply

paulhebert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! Right Words is also fun!

reply

LandR
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is great :)

reply

paulhebert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks!

reply

codebje
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've been playing this since it was first mentioned on HN a few puzzles in. It's a nice idea and pretty well executed.

I have, however, rejected making a user login. I recognise you're putting in time and energy to make something I'm just taking without payment, and it's your right to try to leverage it into something more - I wish you all the best in doing so - but asking for a user login as a gate to a feature you clearly don't need a user login for is enshittification.

reply

paulhebert
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hey, thanks for the feedback. I didn't intend to pressure you to create an account. Sorry if I gave that impression.

I'm guessing you're referring to the ability to filter out completed puzzles from the archive? I added it for logged-in users first because it was simpler but I can extend that feature so it's available for everyone. (I'll need to add some alternate logic to pass your indexeddb levels to the server endpoint when fetching the archive. It's not complex. I just haven't prioritized it yet.)I'll add this to my backlog and try to get to it after the player puzzles release.Beyond that everything is available regardless of user account right now. I do plan to require an account to submit custom puzzles when that's released. (Mostly to make moderation easier. I may relax this down the line.)EDIT: On further thought I realized it's also required to have an account to view and share your profile stats, though that could also work without an account with some changes.

reply

codebje
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Anything that requires server-side storage is a good reason to ask for an account, IMO. Theoretically you could assign a pseudo-account and store the id in client storage to have a shareable profile, but then you'll have to figure out how long you'll retain idle pseudo-accounts. (Assuming that completion detail is in client storage, at least for anonymous players).

A consequence of me being a freeloader too is that you don't have to change your plans to please me :-)

reply

bicx
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is really cool and addictive!

reply

paulhebert
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for checking it out!

If you enjoy it there’s a new puzzle every day and a backlog of over 200 puzzles free to play ;)

reply

luigi_123
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

* This is my first time actually posting anything on HN.

I've been making a DSL for writing sheet music specifically for drums as raw text, inspired by ABC Notation (but of course just for drums).Now writing this I noticed that it's kind of complicated to explain and having a landing page would make my life so much easier.But the gist of it is, you write notation that looks like this:https://gist.github.com/Luigi123/945af7e5cc8dfbfd186f0a99754...and it renders sheet music in PDF, and also allows you to play the same music as a game (DrumMania / DTXMania style).Now the language / compiler itself has been working quite well and I've been dogfooding it for like six months now. The next thing is an IDE-style editor where you can import a song and write the notation following it. Making THAT has been quite the journey. Here's a screenshot for good measure:https://i.imgur.com/EmlqlrM.png

reply

jmusall
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Related: 
https://lilypond.org/

I don't know if you can write drum sheet music with it.I really like your editor with the transcription view. Maybe a spectrogram would be more helpful than a simple waveform display.

reply

strofocles
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm building an iOS app (with plan user-base of 1) to help me structure my (I wish they were) weekly drumming sessions. My idea is to have "lessons" that have more "patterns" and I choose a lesson and practice those patterns logging the bpm's i can do (that 186bpm from your example is just wild for me). I am a beginner-intermediate so lots to learn for me. I use musical notation. If anybody interested in it let me know.

reply

meltmymind
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Very cool. I'm working on something similar, for composing songs with both note-playing instruments and drum instruments. The format is TOML-based, and for melody I was inspired by strudel, but I had considered using ABC notation as well. The home page has an example of the format, and some demo songs: 
https://songformat.com

reply

sbrother
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh dude, I love this. I've been working on an interactive music thingy (
https://trebel.la
, it's sort of gamified but more designed to structure practice sessions for serious classical musicians) and struggling with the ABC vs. MusicXML choice.

Like most people in the space I'm using ABC for LLM generation (e.g. generating sightreading exercises and etudes) but MusicXML for processing and rendering the output. Would be nice to have something somewhere in between the over-simplified ABC and overly verbose MusicXML.

reply

luigi_123
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Would be nice to have something somewhere in between the over-simplified ABC and overly verbose MusicXML.

Hard agree.Early on I actually tried to write my drum charts directly in ABC Notation but it wasn’t a great fit. Then I made a simple parser for my language that outputs ABC because I thought it would be simpler but I found it to be very limiting, so now I use Vexflow’s low level API for rendering. I found it to be more customizable than ABC with a nice JS / TS API. It’s good for my use case (rendering) but ofc it doesn’t work as a save format.Good luck with Trebella :)

reply

puilp0502
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I love this. This was always an idea I had in my head, because spinning up MuseScore just to write down some beats was so annoying. Glad someone already came up with the solution! Do you plan to release the compiler(uh, rasterizer/renderer)?

reply

kukkeliskuu
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe 10 years ago I started to build Guitar Hero style game with real electric drums, initially to teach myself drumming. The idea was to extract drum information from real songs (so I was exploring a DSL as well). I guess modern AIs could be used to implement this much quicker.

reply

8note
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

oo interesting.

is this intended for drummers, or electronic music composers?

reply

luigi_123
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's intended for drummers, but I wouldn't rule out anybody. It 
can
 generate sound, and I'm even using some nicer sounding samples I found on the internet, so using it for composition is realistic.

But the main use case I'm going for is my own: making sheet music for drum practice.

reply

8note
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

On the drummer side of the audience whats the need for plain text vs writing with pencil on paper?

aiming for more extensions to The New Breed than just Syncopation that you could auto-generate for funny practice/things you wouldnt think of to play?

reply

luigi_123
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Forget the DSL part for a second and what this can do is: it can render sheet music, play the corresponding sound and display the same music as a rhythm game.

People writing sheet music with pencil on paper don't need any of that so I'd say this software would be pointless for them. I'd say this leans heavily on hobbyists or beginners, like I said the main use case is my own, and I'm no professional drummer.This is not a sales pitch, it's just a small project I've been having fun building for myself :)

reply

JeremyJaydan
 
20 minutes ago
 
 | 
prev
 | 
next
 
[–]

I'm working on my website directory (
https://intrasti.com
) I've mostly been slow about it over the last year as I continue upskilling.. will be looking for a full time job so I can keep up the slow pace!

There hasn't been any releases in the last couple months but I'm working on some stuff like search topic shelves (netflix-style shelves in the search) and I'm going to bring back visited links that look similar to YouTube 'watched' thumbnail tags!

reply

cmontella
 
32 minutes ago
 
 | 
prev
 | 
next
 
[–]

Last couple weeks I've been building a new website to showcase the document formatting capabilities of my programming language Mech. It's out now:

https://mech-lang.org/post/2026-05-11-version-0.3/Mech has a builtin presentation layer called Mechdown (a Markdown dialect) which allows tight integration between the document and the underlying program. You can see the source here:https://gitlab.com/mech-lang/web/website/-/raw/df4784d44b4ea...Would appreciate any bug reports or issues:https://github.com/mech-lang/mech/issues

reply

madman_dev
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm constantly working on 
https://only-eu.eu/en

A directory of European software and general alternatives to popular products.Think cloud storage, email, VPN, browsers, smartphones, bikes,... About 175 products across 30+ categories right now.Next categories will be: personal health, commercial e-mail and newsletter management.If you have a product that's missing here, please feel free to suggest it via the suggestion form on the site.

reply

BrunoBernardino
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice work, thank you for this! The current "main option" for this (european-alternatives.eu) is greatly stale, and isn't responsive to suggestions. I'd love to see an alternative (ha!) rise up and take its place.

reply

madman_dev
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you! Really appreciate the kind words!

reply

jll29
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Thanks for that.

For what it's worth, two days ago on the radio some politician
said that for more software sovereignty to take off, all we'd
need is such a catalog! ;-).

reply

madman_dev
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Haha nice! If he/she only knew...

reply

hallucinate
 
57 minutes ago
 
 | 
prev
 | 
next
 
[–]

Working on an incremental reading / spaced repetition app that uses the best spaced repetition algorithms. I reverse engineered SuperMemo 18's algorithm (
https://github.com/melpomenex/sm18-re
), SuperMemo 20's algorithm (
https://github.com/melpomenex/sm20-re
). 
https://github.com/melpomenex/incrementum-tauri
 you can try the demo (not everything that works in the Tauri version works on web) here: 
https://readsync.org

reply

iridione
 
43 minutes ago
 
 | 
prev
 | 
next
 
[–]

Ask The W 
https://askthew.com/

Cursor for AI PMs/Forward Deployed PMs.A lot of engineers are trying to build the “Cursor for PMs.” As an engineer-turned-PM with several YOE in both roles, I appreciate their intent, but most are not solving the elephant in the room for the next generation of PMs, so I decided to step in.Engineers wrote code. Designers produced design artifacts. Product Managers HAD to write PRDs as a way of communicating intent to gain alignment across teams; it was never their only job (would’ve been easy if it was!). The PRD was the means to the end, not the end itself, which is where most engineers are stuck building another AI-native text editor to become the next Cursor for PMs.Today’s AI tools can generate PRDs, fancy roadmaps, complex spreadsheets, beautiful decks, and no-context OKRs, but the real job of PMs was always quick alignment, principled decision-making, and leadership buy-in with little to no data, something no AI tools can reliably solve today. We now have a unique opportunity to (potentially) solve these big, hairy problems with AI. I’m starting with orchestrating humans and agents to make better decisions.Loving it so far. AI tools make me wish there were more hours in a day!

reply

hagg3n
 
49 minutes ago
 
 | 
prev
 | 
next
 
[–]

I’ve been tinkering with an LLM-based assistant for small-scale web development team's knowledge base.

Picking a tool and setting up a knowledge base to have technical and design decisions, notes, and maintenance logs in a single place is usually straightforward. It's the consistently feeding the system with high-quality data part that we get stuck at.Eventually, I have to input information when I lack the necessary mental bandwidth, I end up creating incomplete entries that lack essential details.The initial idea is to develop a chat interface that allows us to share random pieces of information, either through text or voice, and have it scanned for actionable data that can be ingested. Then it should start probing the user, looking to expand and refine the new information, connecting it with existing data, and general maintenance of the repository. All with no active guidance.For instance, I could launch it and say: “Today the team and I discussed how frequently the databases for project A and B should be synced. We established the user can tolerate up to 10 minutes of tardiness", at which point I would expect it to:- Create a note of this discussion happening
- Check and fix the existence of entries for projects A and B
- Link the note to the projects
- Create database entries for both projects
- Look for previous entries that could be linked to the projects
- Ask for further explanation of how we came to that conclusion

reply

mindaslab
 
12 minutes ago
 
 | 
prev
 | 
next
 
[–]

Kanipaan - A command line calculator 
https://kanipaan.codeberg.page/

reply

eltados
 
29 minutes ago
 
 | 
prev
 | 
next
 
[–]

Izeria : 
https://www.izeria.com/en

A micro discovery / rediscover your local area.My friend dumbed it "Pokemon go but replace the Pokemons with castles and churches :)"Use the GPS to discover places of interest in your neighbours or anywhere in the world and invites you to do see these places in person and check in and read the page and get a fun quiz.It works great for me in Scotland, check it out in your country and let me know.

reply

seydar
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Acoustic diagnosis of electrical problems on the electric grid!

I'm building a tool that allows you to determine the health of an electric transformer from only your phone. It tells you:- the loading
 - the health of the windings and core
 - and whether the phases are unbalancedI used to be a submariner, so my professional background is in power plants and sonar analysis, so I'm getting to combine the two in this.Acoustic diagnosis of electric issues is FASCINATING, and it feels like there hasn't been a lot of research into this, so I have been slowly chasing down various acoustic patterns I find and try to derive them from first principles of physics.I'm making an iPhone app for it, and Xcode has beentrulyawful: non-deterministic, crashing all the time, and error messages that tell me absolutely nothing. I would like to use xtool, but it doesn't have the preview, which I need for debugging.

reply

utopiah
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

> making an iPhone app for it

Honestly if you don't have a specific reason to target iPhones then buying a 2nd hand Pixel 8, putting GrapheneOS on it then pushing an "app" in whatever language you want on it, sure can be Java but can also be Python, Julia, whatever you want really especially on it directly using Termux, could be a better use of your time. By the time Xcode starts you'll already be outdoor testing against the next transformer.

reply

sgt
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Am also using Xcode but not experiencing crashes, so it could be to do with his environment. I've got Xcode running now since.. 2003? It's not always been perfect but pretty stable if your env is right.

reply

utopiah
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I do imagine Xcode is stable so it's mostly a suggestion to making testing on an actual device more convenient. I imagine for somebody who already have a proper pipeline it doesn't matter but here it doesn't seem to be the case, hence offering an alternative.

reply

marking-time
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This sounds (pun intended) really cool.
nettirw yb namuh

reply

skataz
 
15 minutes ago
 
 | 
prev
 | 
next
 
[–]

I am working on collecting.cash, a webapp that helps with sending payment reminders. Can be used for reminding members of a family plan (mobile, or streaming, etc.) when a payment is due.

reply

jfil
 
21 minutes ago
 
 | 
prev
 | 
next
 
[–]

I'm creating a piece of "home cooked software" - a multi-player web game to play with my team at your monthly Social. Made for a specific team, for a specific occasion.

Its janky, and I made several time-saving decisions that'll cost me more time in the end, but I'm having fun.

reply

mindaslab
 
13 minutes ago
 
 | 
prev
 | 
next
 
[–]

Clojure Diary 
https://www.youtube.com/@clojurediary

reply

mindaslab
 
15 minutes ago
 
 | 
prev
 | 
next
 
[–]

https://injee.codeberg.page/

Injee - The no configuration instant Database for front end developers.

reply

shinrak
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I finally managed to finish a project and publish my first game on Steam: 
https://store.steampowered.com/app/4195030/balls/

It's a short chain-reaction game in which you explode balls bouncing in the screen, and need to build up to target scores. You build bigger and bigger combos as the game progresses.It was a blast to work on it, starting with a small toy and just adding features that "felt right" until I had a game that was fun to play. It was quite hard to find a balance though, so a lot of numbers are arbitrary - but I enjoy seeing people breaking the game in new ways and finding new builds.These days I've been working on patching reported bugs and sharing the game with people. Now after the latest patch, I feel like I'm done, but I feel like going back at it and adding an idle mode. And maybe simplify the codebase so I can test and iterate better, and then add many more ball types...I know that any good LLM could replicate this pretty quickly, but I made this myself and I'm still feeling proud of the accomplishment :)

reply

ditchfieldcaleb
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

Oh, this is cute and a great first game! I'm working on my first game as well (a top-down 2D tower defense game).

What engine or framework did you end up going with? I looked into Unity, tried Godot for a few weeks, but landed on just making a Typescript-powered canvas game with PixiJS for graphics rendering. Found itmucheasier doing it this way instead of having to learn a game engine.

reply

markmnl
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Shiping a real product, esp. a game, from scratch is an awesome achievement, congrats. (My first shipped product was Square Heroes also on Steam).

I feel like perfecting something can be trap, sure keep it alive, but maybe think about the next thing to work on too?

reply

dielll
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

A small game called Colorhunt to play with my friends

https://colorhunt.lol

You get assigned a random colour and have 24 hours to go out and take photos matching it. The game then generates a photo grid from everything you captured.Modes:- Solo → 9 photos by yourself
- 1v1 → compete against a friend, combined grid at the end
- Squad → everyone contributes to a 20-photo gridNo accounts, no app install, no personal data stored. Photos and generated grids auto-delete after 24 hours from Cloudflare R2 storage.Made it for fun to find a way to do a shared a activity with my girlfriend and also to challenge my friends over the weekends.Currently redesigning the frontend flow but I am kinda poor at designWould genuinely appreciate feedback, ideas or anything

reply

IanOzsvald
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I've spent 6 months building a network of curious LLM hackers in London who want to push the edge of what we can do.

This Friday we pull GPT apart and rebuild bits by hand. A few weeks back we tackled ARC AGI 2026. Prevoiusly we did fine tuning and making GPT funny.It is a sort of a guided hackathon (generally I plan goals for the day) and collaborative study group.Much fun, no money, lots of smart folk asking good questions:https://playgroup.org.uk/

reply

mstaoru
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

[NO-AI]

Being a weightlifter for 20+ years now, I'm working on a barbell speed and path tracking sensor based on newer IMU hardware technologies, which makes it both more precise and cheaper than camera- or actuator-based systems. Ultimately it helps you lift and train safer and better.It's an intersection of industrial design, hardware, firmware, and software (and some sport science, of course). This intersection is not yet dominated by LLMs so it's a breath of fresh air.In an early prototype stage as in "strap a Raspberry Pi to a bar", but it looks promising and I'm happy to move forward, also using connections from my previous 12+ years in China.

reply

utopiah
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

How about strapping the phone to the bar and opening a Web page with 
https://developer.mozilla.org/en-US/docs/Web/API/Acceleromet...
 ?

Seems it would have a much higher reach.

reply

mstaoru
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Phone accelerometers don't have enough range and sampling frequency to even begin with. Raw, on some rare phones you can sample 800 Hz (enough-ish), but on most 100 Hz max, Web API is capped at 60 Hz, this is all way too low for any quaternion math. They also have much higher noise density which is the silent killer of all kinds of IMU navigation.

I also wouldn't trust a strap to drop a loaded bar from snatch :Dhttps://youtu.be/nrgnH9fTfGo?si=6LLeu3y02iFrwfis&t=65

reply

utopiah
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ah didn't think you'd need that much, thanks for the clarification.

Might consider a BT GadgetBridge gadget then.

reply

era86
 
1 day ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wannabe powerlifter here of about 20 years as well. This sounds like an awesome project! Is bar-path the main metric for safety and "better" lifting? A project I had in mind, once upon a time, was an automatic "Form Check Friday" for myself using a Pi + Webcam.

reply

cleaning
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

As someone who has been very deep down this rabbit hole and hacked together multiple path and velocity trackers over the years (specifically for olympic weightlifting), there is no extra information that tracking bar path will give you that simply looking at the video won't, and often just adds more clutter. You don't need to graph bar path to see that the bar is looping too far forward after hip contact in the snatch.

Velocity on the other hand is a great metric to track and is used as a proxy for RPE. Mike Tuchscherer was the first one to systematize it for powerlifting a while back, if you've been lifting for 20 years you're probably aware of the name.

reply

mstaoru
 
22 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Thanks! I think for "canonical" lifts (squat, deadlift, row, to some extent military press) the vertical bar path is mathematically optimal, and for all kinds of lateral or sagittal movements you do more work with weak stabilizing muscles and load joints laterally too. Is it productive work that strengthens your core? Possibly, but it's hard to quantify. It it something that can lead to injury? Absolutely yes.

For more complicated lifts like bench press (J-shaped) or snatch (S-shaped), for example, I would rather set a "golden sample" path with a coach and compare to that.It's unlikely to be the sole metric, especially given the inverse kinematics of different body types (long/short femur, etc), but together with bar speed,over time, it can provide a lot of good feedback.

reply

cleaning
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is not "absolutely" something that can lead to injury. Injury itself is difficult to define, and often the reason one experiences pain sensation is multifactorial. Within lifting contexts, generally the factor which has the strongest evidence for injury prediction is how sharply an athlete increases intensity compared to what they have previously adapted to.

No offense, but this post does come across as you only having a surface level understanding of the field. Especially surrounding injury/pain perception, I would be more careful of what you assume is true, there's far more nuance.

reply

notesinthefield
 
23 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Not OP but velocity is typically what these devices are used for. Its a great measure of between-set intensity.

reply

grepfru_it
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Side note: My LG Watch Sport smartwatch was able to determine what weight training workout I was performing and somehow figured the weight with astonishing accuracy.

reply

gozzoo
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've had the same idea for year. When google released their Fitbit Air few days ago I the first thing I tought was - can it be used as a sensor for weightlifitng and do they have API for that.

reply

a-dub
 
22 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

i'm curious about how effective path tracking can be in comparison with computer vision based inverse kinematics of the body itself. do all forms of bad form have detectable imu signatures?

i wonder if it would make sense to consider it as a data problem, capture a bunch of high fidelity inverse kinematics data for various forms of bad form/dangerous lifting along with the imu data and then work from there. there could be some interesting and unexpected features that are easier to detect than straying from straight line paths with some tolerance.

reply

mstaoru
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

For me it's a bit of an inverse problem. I go to a public gym (hard to sustain motivation at home) and I absolutely don't want to film myself there.

reply

sberens
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Have you seen 
https://fort.cx
?

reply

frankdenbow
 
1 day ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

this sounds awesome. have any videos of it?

reply

mstaoru
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! Working on it, for now it's literally a taped breadboard. :D

reply

mindaslab
 
15 minutes ago
 
 | 
prev
 | 
next
 
[–]

Clojure Book 
https://clojure-book.gitlab.io/

reply

needcaffeine
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://www.OnetimeFax.com
 - it's a way to send and receive faxes for a flat fee without needing to subscribe to anything.

Version 1 was a script I wrote for myself to fax the courts a jury duty deferral during covid lockdown, and then during my parental leave I productized it.

reply

armenarmen
 
29 minutes ago
 
 | 
parent
 | 
next
 
[–]

I was just thinking about building this! Bravo!

reply

brk
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is such a stupidly needed thing. Nice work!

reply

leot
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Quell (textquell.com)

Broken relationships can be difficult and nerve-wracking. Quell gives you an SMS number that enables you to put boundaries around your communication with someone who is blowing up your phone and making your life hard. Their texts are intelligently filtered so that hostility is removed while information is preserved. All raw texts are also routed to email for record-keeping and rewrite verification.

reply

jspann
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

> Quell doesn’t store your messages — they’re processed and discarded in real time.

Are you using a 3rd party system to generate the numbers and forward them to your number? How can you audit that they 3rd party that creates the Quell numbers isn't saving the messages before they move to your server?

reply

anthonypasq
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

im sorry for anyone who is in a place thats needs this service.

reply

starik36
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I had a good laugh. Well done. Could have used this 20 years ago. 
If you can figure out how to do this in person, you are golden.

reply

shivang2607
 
49 minutes ago
 
 | 
prev
 | 
next
 
[–]

Been working on a tool called Devlens.

It visualizes React / Next.js codebases as an interactive graph so you can understand how features and components connect without manually tracing files.Main focus right now is helping with:PR reviews (understanding blast radius / impact of changes)
onboarding to large codebases
understanding unfamiliar parts of a system fasterAlso experimenting with summaries + security analysis directly on components.Still early, but it’s been pretty useful for me so far.https://devlens.iohttps://github.com/devlensio/devlensOSS

reply

wpietri
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

The last couple years I've been prototyping a not-for-profit pinball museum in Chicago. In the coming weeks we'll be opening 7 days a week in a 2900 sq ft space in the Loop: 
https://theflip.museum/

It's my first time starting a physical, retail business and it has been quite an education in the small details.

reply

ripe
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Congratulations, and good luck! It should become very popular.

We enjoy going to a similar pinball museum here in Pawtucket, RI, which you might be familiar with:https://www.electromagneticpinballmuseum.com/

reply

tehlike
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Impressive. I hope you find success!

reply

bad2j
 
28 minutes ago
 
 | 
prev
 | 
next
 
[–]

Working on a tool to speed up iterations of backtesting Algo trading strategies (
https://foxtradetools.com/
):

- Visual tool for building strategies- Backtest on site or MT5 EA using same json configurations- Running EA live (or paper mode) in prod automatically feeds the trades back to the site for analysis- The thing I am most happy with: you can click any trade in backtest result and see exactly which rules were true at the bar that firedYou can try it in action w/o signup using taster page (https://foxtradetools.com/taster)Solo dev. Open to any feedback.

reply

murdockq
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on 
https://assistedlist.com

From personal experience finding and researching senior care ends up being a big trap, they lead you into a sales funnel before you can clearly compare real options. Data is hidden behind walls and when your under time pressure, and trying to make a serious decision, you end up hitting a search experience that is dominated by SEO pages, phone-number capture, referral incentives, all because your contact info is the product they will sell to elder care facilities.Focused on Florida first to get the right UX and details needed.My goal is is to make it way simpler with real prices and data research first and then add AI advisors who can make it much easier to make an informed decision. Then adding products that cut out the middle man, because it feels broken and shady right now.

reply

markmnl
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on fmsg - open protocol for instant messaging, distributed by domain like email..

Its a message definition and protocol, addresses look like @user@domain, anyone can run a host, and threaded messages are linked by cryptographic parent hashes..The idea is to take the best from email: open protocol, domain ownership, interoperability (unsolicited mail is a feature not a bug), and the best from closed instant messaging rebuilt: efficient binary messages, conversational threads, sender verification, message integrity etc. built-in. Originally envisaged for human-to-human messaging but partculalrly interesting time right now with human-to-agent and agent-to-agent messaging...The OSS stack is up and running: Go host, Dockerised full setup, CLI, Web API, and a spec nearing v1.0. Did Show HN post week ago:https://markmnl.github.io/fmsg/show-hn.htmlSeeking feedback, criticism, validation :) protocol bikeshedding, and especially interest from founding-engineer types who want to help build an open messaging ecosystem rather than another closed app..

reply

tgsovlerkhgsel
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

What is the unique selling point that it has over Matrix?

Matrix addresses have a similar format, anyone can run a host, open protocol, domain ownership, interop... Threaded messages are supported AFAIK, the details of the crypto will be different but overall it feels like it is close enough that a new protocol will have a hard time havingenoughadvantages to overcome the huge network effect (Matrix being one of the few open messengers that actually have some following already).

reply

markmnl
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You're absolutely right to pick up on that, I did study the landscape and Matrix is closest.. biggest difference is fmsg is just messages - group like chats evolve naturally in the threads - but to get a message someone has to send you one. Group messaging platforms like Matrix, Rocket.Chat etc have concept of rooms/forums/channels i.e. groups, then have HTTP APIs to manage membership and sync messages.. fmsg just messages someone has to send you

Also fmsg being its own protocol can do novel things like to auto challenge during sending back to sender - can't do that with HTTP

reply

epaga
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a tactical map-based WW2 submarine simulator called Silent Shark. 
https://silentshark.app

Free beta version is running well (https://silentshark.app/alpha) and I plan on releasing the full WW2 campaign version on Steam, App Store, and Play Store in the next month or two.It's been an absolute blast getting feedback from Navy geeks on Discord, tweaking things, and my favorite moment was when my stadimeter instrument (finds distance based on angle + mast height in the periscope) worked without any "cheating" on my side simply because math works.

reply

matthiaswh
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

The quotes on the homepage made me chuckle.

This looks right up my alley, looking forward to playing it.

reply

epaga
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Awesome! Would of course deeply appreciate any and all feedback!

reply

paulnovacovici
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I’m an application developer by day, but lately Claude Code and Codex have finally made microcontrollers approachable enough for me to start tinkering with them on the side. I built this little “holographic” display that shows the surf forecast for any beach. While my friend built the casing, and mechanical part of it

https://x.com/paulnovacovici/status/2041722840190480581?s=46...

reply

pastel8739
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

This is super cool. At first I thought the “tank” on top was filled with water—I wonder what it would look like if it were

reply

_def
 
23 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

any details on the display itself?

reply

paulnovacovici
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Display is part of a dev kit EPS32-s3, and the holographic part is an illusion called “peppers ghost”

reply

mikestorrent
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Beautiful piece of kit. I have no idea how it works from looking at it, fantastic. Please do post a full writeup on it.

reply

narmiouh
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Its a pretty straight forward technique, the display is at the bottom and in the glass cube there is a mirror at 45 degree angle facing you (you can see the mirrors edge on the side wall) which reflects the image from the display at the bottom making it look like a hologram

reply

danparsonson
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can create the same effect on a smart phone screen with a video like this: 
https://m.youtube.com/watch?v=CIszi2Kv_lk
 and a some clear plastic sheet put together like this: 
https://www.twowaymirrors.com/wp-content/uploads/2019/11/pep...

OP: beautiful work with your surf projector!

reply

deskamess
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Do you happen to have instructions on how to build the plastic sheet setup or perhaps a pointer to something that I can buy?

reply

danparsonson
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can do it by cutting and folding a sheet of clear acetate or similar from a net like this: 
https://wp.optics.arizona.edu/oscoutreach/wp-content/uploads...

Or you could cut the four sides separately and just sellotape them together.edit: not much help without measurements sorry - try this:https://www.holeinthewallgang.org/Customer-Content/www/CMS/f...The required angles appear to be 54 or 126 degrees:https://data.formsbank.com/pdf_docs_html/304/3049/304991/pag...

reply

paulnovacovici
 
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

Yup! We first started very similar with a phone and testing out the illusion then moved over to a microcontroller for a little nightstand device

reply

sateesh
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

In my effort to better understand Deeplearning I built this project (
https://github.com/sateeshkumarb/anomaly_detection
) to detect
anomalies from a batch of loglines. I use 1D CNN and Siamese network (Triplet loss) to train the model to learn anomaly patterns from logs.
The goal was to detect anomalies that emerge across multiple lines (e.g., error bursts) rather than just single-line keywords.

To validate the approach I trained the model on generating synthetic data. I did look at datasets available at:https://github.com/logpai/loghub,https://www.unb.ca/cic/datasets/index.htmlbut couldn't find one that would suit my needs.The approach seems to work on synthetic dataset (with ROC AUC score: 0.9957) but couldn't try it out in a real world dataset. Seeking feedback on the approach.

reply

umairyousif2280
 
31 minutes ago
 
 | 
prev
 | 
next
 
[–]

I recently built this project for AMD AI Hackathon. At it's core, it's a local first debugging tool thats powered by Qwen 3.5:9b.

You give it a repo and an error log and It finds the root cause, suggests a fix, shows the bug propagation and the files it went through. The fix it suggests is in a diff format so its very easy to apply the fix. Here's the link to the repository if anyone wants to try it.Any type of feedback is welcome!https://github.com/umairyousif239/AxionSys

reply

stoplight
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I've been toiling away for the past 2 years on a passion project. A native mobile app for the PWHL (Professional Women's Hockey League). It's privacy focused without ads and a bunch of features: 
https://pwhl.app

It uses flutter under the hood, with Kotlin and SwiftUI for native home screen widgets. A simple nodejs backend powers push notifications too.

reply

aspectrr
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

[Lily](
https://github.com/aspectrr/lily
) A CLI tool that can be installed to any coding agent via hook that gives read-only access to production systems (wraps ssh, kubectl, awscli, gcloud, az) so agents can investigate issues in production. Built it for myself and my team during initial investigations to save use a lot of time on figuring out issues but didn't want to have to babysit agents or just hope that "telling them they are in production" would prevent issues.

[clue.ssh](https://github.com/aspectrr/clue.ssh) A clue game over SSH based on the AI wave, where the goal is to find who stole the H100. Pretty fun and coding agents can play too.[Chasing Losses](https://github.com/aspectrr/chasing_losses) I was interested in if LLMs chased losses when playing roulette, still investigating this but i've found that different models will bet different amounts at different frequencies even when prompted the same. Struggling on not wanting to guide them too much but also wanting to see how they react when put under pressure.

reply

SdtEE
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

This starts from my frustration when opening large CSV files, but later evolved to a log/data analyzer that loads arbitrary format in constant time (O(1)).

https://github.com/Verticalysis/HitomiThe secret: I engineered an incremental combinatorial parser capable of processing customized format from a steam. Any inputs, including file or the stdout from a command, are first chunked and then fed to the pipeline. The UI is ready when the first small chunk is processed.Other highlights:
2-mode filter, one with a convenient UI and the other is based on an extensible DSL for complex cases;Timeline mode scrollbar, a secret weapon for log or time series analysis;Column widths fit to content automatically;Native code, no web bloat;Cross-platform (currently Windows and Linux, MacOS WIP).If you are tired of all the quirks Excel have when working with CSV files, you'll gonna love it!

reply

klntsky
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Does it update the parser incrementally?

reply

AsmaraHolding
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m developing X/D Loom (
https://xdloom.com
), a tool that helps car enthusiasts create automotive wiring diagrams.

About a year ago, I engine-swapped my Nissan D21 hardbody from the Z24 petrol to a TD27T turbo diesel and also installed a whole bunch of accessories, like spotlights, a winch, and an air compressor. But being lazy, I didn’t write down any of the wiring changes I made while doing all of this. So fast forward a year, and now I can’t remember how all the wiring works.My current project car is a Jeep Cherokee FSJ, and for it, I want to build a completely new loom from the ground up. So to try and avoid making the same mistake I made with the Nissan, I Googled “create automotive wiring diagram”, but all the results were for complex enterprise grade solutions charging $200/month. That’s why I created X/D Loom as a project car guys' tool for creating wiring loom diagrams. It allows you to drag different electrical components onto a canvas, connect them with wires, and export them to a PDF or PNG.

reply

Loughla
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

My son and I are about to tear into a 1987 Wrangler. This is going to be very helpful when we're undoing 40 years of modifications on this thing.

reply

AsmaraHolding
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Awsome. I'm planning on adding the Edelbrock Pro-Flo 4 EFI system to my AMC 360. One feature I really want to add to the app is prebuilt templates for popular aftermarket EFI, ECU, and Digital Dash setups from Holly, Edelbrock, Haltech, and Dakota Digital.

reply

bespokedevelopr
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Helping my wife with building out Fine Dining classes. I’m doing the tech stuff, she does all the real work.

It started with informal among friends things, and we’ve found through our networks there’s a lot of demand beyond her girlfriends wanting high tea etiquette. Now she's diving into tech people who have elevated into higher ranks but don’t have experience yet in fine dining with clients and leaders.It’s been a lot of fun doing something that has nothing to do with AI and really minimal tech in general. The events have been a lot of fun, really feels like we’re cooking something.

reply

rbbydotdev
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Opal: Browser first feature-rich markdown editor, workspace and publisher

-https://opaledx.com-https://github.com/rbbydotdev/opalNo logins or sign-ups, totally free, MIT Open SourceIntegrates with git and github, publishes to aws, github, netlify, vercel, cloudflare, great drag and drop image integration

reply

pauldjohns
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Cloud sandboxes to run your full stack (
https://eng.somethingelse.ai/
). Primary use case is with PMs to prototype and build on the codebase, shipping non-opinionated PRs for review, but our dev is using Else to build Else, so we published the eng site so others could try it out.

Personally, I'm working on a river TierBlend seasonal forecast (currently 6–15 weeks per gauge) — in-house ML model trained on 35+ years of weekly discharge plus NRCS SNOTEL snowpack features (https://pauldjohns.github.io/usgs-discharge-poc/)

reply

gustavopezzi
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I left my fulltime faculty position at the university. I'm only teaching two modules this semester and I'll probably fade out even more in the future.

I've also paused recording any new lectures at pikuma.com for now. I'm still taking some time to decide what's next for the website. I'm currently focusing on reviewing math & physics to help homeschool my son.Other than that, I just improved the roof of my chicken coop and I'm slowly evolving the foundation of my study cabin. This new place will be my offline library and music room soon. My plan is to only really go online once a week starting August this year.

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Hey I'd really love your input based on your academic background on an app I'm building if you have the time. It's learning focused.

I'm a Dad homeschooling a son and have a dog in the race of making parental guided education easier.https://chunkker.comI have an Alpha user who's a PhD and makes courses but I still want diverse feedback.

reply

marai2
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Thanks for all your efforts on pikuma.com, huge fan here.

Can you share what kind of ideas you're mulling for the direction of the site?

reply

gustavopezzi
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for the kind words.
I still want to record "Operating Systems" and "Algorithms & Data Structures" to finally complete the core CS areas. It's missing Networking but I don't know much about that topic anyways. I also wanted to continue the retro programming with at least one 68K machine (maybe the Mega Drive) plus a MS-DOS x86 course too. Also, I wanted to teach 3D game physics, either as a new course or adding more chapters to the existing 2D physics course.

Hopefully, I'll decide on what to tackle soon.

reply

jkantola
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

[Vaava](
https://www.vaava.app/
) is a baby tracking/logging app I originally built for myself, now available on both app stores. All the user generated data is stored only on device and is transferred in local network to users who you have paired the app with. There is 0 behavioural analytics, even the crashlytics are 100% optional.

There is a couple of semi-unique features; you can use your voice to dictate and generate events (feeding, sleep etc), you can also scan documents for growth measurements.You don't need user account to use it, there is no subscription, the paid features are available behind a single purchase for lifetime. Still like 90% of the features are available for free.Alsohttps://www.athilio.com/, which originally was also purely for my own use. Most sports and fitness wearable manufacturers own software and 3rd party software make it incredibly hard to do "how does my this months metric x compare to same month last year", athilio attempts to make those queries easier. Many of the ideas are basically copied from software observability concepts. Also I have used the app to implement and learn agentic workflows.

reply

niothiel
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on cardcast.gg. It gives you the ability to play Magic: The Gathering with your friends remotely using a webcam.

I got back into MTG back during the pandemic after a long hiatus and Spelltable is what brought me back. My playgroup lamented more features and something tailored to our needs, so curiosity got the better of me and here we are. :)I've never worked with computer vision before, but I went through a whole journey that started with the classical computer vision techniques and ended with recently migrating to the transformer-based models. Been a really cool adventure!My playgroup has been consistently preferring it over Spelltable and have been wanting more and more features. I would love for people to try it out and start building a community around it! Discord is on the site.https://cardcast.gg

reply

utopiah
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

Interesting, seems you are doing the recognition server-side, no reliable way to do it locally using e.g. WASM on the client?

reply

niothiel
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Actually actively exploring this very topic! I have a feature-flag version where the inference runs via WASM / WebGPU (onnxruntime-web specifically).

My only pause behind rolling this out further is the performance isn't as fast as I'd like (1.5s~ latencies), and the widely varying support for WebGPU / WASM across browsers and OS pairs.Still testing it out (and learning about ViT performance on various hardware), so hopefully more news on that front soon!

reply

borealbuilder
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

An alternative to spelltable is a great idea! My friend group played extensively a few years back through it but always ran into weird bugs and glitches.

I love that there is no sign-up required! Do you have plans to implement utilizing a mobile phone as a camera? Spelltables implementation leaves much to be desired.Excited to see where this goes!

reply

niothiel
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks boreal! I have it on my feature request list. I'm currently using a custom WebRTC + Websocket implementation for connections that I wrote without having this feature in mind, so reworking that will take some effort. Currently focused on client-side inference (runs in the user's browser), followed by continuous tracking (think: Snapshot the entire frame every 5s so all players know what cards are on the board at any given time). Will probably get to that in the next week or two!

If you ever want to follow along or play a game, feel free to hop on Discord (link on site)!

reply

ramon156
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I had a similar idea, as alternatives were.. eh.

I also had an idea to get a ~12MP camera and set it up on an active game of MTG, just because standing up and having to read other people's deck was bothersome. My eyes are bad, and I end up not reading other people's cards because I feel weird hovering over them when reading.I would then cast whatever is at the person's deck onto an app so I can manually read the cards. Since my phone is of a similar ratio as a playing card, I figured this might be a nice way to play.

reply

niothiel
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's a really cool idea! I'm actually exploring a similar concept right now. On the demo page, I have a "Detect Frame" button which will attempt to identify all of the cards (as well as their bounding boxes). You can hook it up to a webcam to try it out that way right from the demo page.

Today, players have to double click on a card in a webcam stream to identify the specific card, but I'm working on doing full-frame detection on some cadence throughout the course of a match (think 1 scan every 5s so you always have an up-to-date board state, remembering past scans).What would be super-helpful is to have a few frames from the camera or a video from your intended setup so I could test how well this scenario works. The detection is pretty good overall via webcam, it would probably work even better with 12MP.I think this would be a really cool application. If you ever want to chat about this, I'd love to talk! Feel free to hop on discord (https://discord.gg/axRtvbsfAU) or DM me! (same username on both)

reply

yarbas89
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

this is awesome. just to let you know, on your demo page "rats", the swamp is occasionally detected as plains.

reply

niothiel
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Aha, cool. I'll look into this, thank you!

reply

inslee1
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I've shared this one before but I built a logistics management system to power deliveries for a business I founded years back and I've continued to refine it since:

https://toanoa.com/Since the initial MVP, it's done close to 100k orders and I've added new functionality like:- Intelligent order batching & route optimization that can interleave tasks across orders in such a way that they still have the best chance possible of completion within their delivery windows- Further refined the mobile tracking logic in our driver app to improve the quality/frequency of position updates while continuing to be as efficient as possible on battery- Numerous backend/DB optimizations such that average response times are in the tens of ms at the current volumes it's handling.It's not open source but if you have an interesting use case and are curious about it, feel free to reach out.

reply

fb03
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I am also (second post) working on an "idle clicker" like TUI game called "cuqueclicker", where you click an ass instead of a cookie (yeah, it's inspired by Cookie Clicker)

https://github.com/flipbit03/cuqueclickerRuns locally and has binaries for every platform that matters out there, including a WASM port that saves your save data to local storageWASM Port here:https://flipbit03.github.io/cuqueclicker/Try it out! It's a fun little idle game

reply

danbrooks
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

This was really fun. I like that holding down space bar gives ~20 clicks per second, which helps speeds things up.

reply

piinecone
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I recently released my first Steam game, a little physics soccer game about scoring great goals: 
https://store.steampowered.com/app/3802120/Put_One_In_for_Jo...
. It's not successful, but I'm very happy with how it came out, and I learned a lot.

I've been using and tuning a tool I built myself to help me lower my LDL and ApoB:https://www.heartroutine.com/. I still don't like how the daily check-in system works (it's still too dumb) but it's keeping me consistent for now.In a few days I'll start running playtests of my combat prototype for my next game, Today I Will Destroy You, some kind of SNES Zelda and Sekiro inspired combat adventure.Periodically thinking about what the future of helping small teams build software will look like and keeping my personal site up to date:https://piinecone.com/.

reply

kyleomalley
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I regularly use about half a dozen programs that interface with radio equipment. Most of it works but getting it all working together is extremely complex.

Since primarily interested in FT8 and MeshCore here in the local SoCal MC region (wcmesh.com) I put together a Pure-Golang implementation to combine both modes into the same GUI client. The FT8 modem might be the only functional Golang decoder right now, unsure, but it’s entirely open source and here:https://github.com/kyleomalley/nocordhfThe workflow releases cross compiled for MacOS (notarized), Windows, Linux and uses Fyne for the UI.In the future, I plan to add other more interesting modes like JS8Call and VeraHF modes, FT4 etc.

reply

thisdougb
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

After quite a few years of coming up with and implementing 'great ideas' but not being able to follow through to making them revenue generating products, I'm on my best bet so far.

I always wanted to build a real-life puzzle game, which is app/mobile assisted. Had yet another eureka moment, and built a usable prototype (backend plus iOS app). Good feedback from a small circle.For a while I was aware of someone (I knew by sight) who worked in the same sort of subject matter (but a non-tech). I approached her, we had a coffee, I pitched the idea and how she could bring it to life, as I made the tech side. She jumped on board.We're two and a half weeks in, have gone full speed and are making something great (for our audience). My future co-founder is amazing, great insights, opinions, drive. We're potentially launching in a couple of weeks, a free/MVP version of a puzzle game.I've been through many iterations of trying to get something off the ground. Tried tech co-founders, and the last years of going solo (very hard after you've done the coding). But this now feels right. A puzzle app/game for every day people to have some fun. And a future co-founder whose life is outside tech, who's bring a sort of fun energy outwith let's make loads of money or isn't the framework/AI cool.Balance is good. Contact with reality is good too :)

reply

TheOrange
 
22 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool. What’s the game?

reply

maxbond
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been learning to crochet. I'm trying to do more hobbies with my hands, but it's also pretty interesting from a mathematical perspective. The fundamental primitive (the chain stitch) is like a series of slip knots, and each stitch is reversible. So the piece is actually a series of reversible transformations. The yarn is sewn in at the end to secure it.

This has some interesting implications. If you make a mistake, you can always backtrack and try again. If you have a crocheted piece, at least in principle you could find the lose end, free it, and work back stitch by stitch to reverse engineer it. (In practice people don't seem to do a stitch-for-stitch reverse engineering just like you probably wouldn't bother reimplementing something line by line without a compelling reason, you figure out what's going on in the challenging places just by look and feel and improvise from there.)I'm oversimplifying somewhat and there are some forms of crochet that include irreversible stitches, yarn can be felted together (entangled, like a cotton ball) to create irreversible bonds between adjacent strands, and often several panels/pieces are joined together irreversibly to create a larger piece.

reply

maxbond
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

I guess I should be clear that by "irreversible" I mean a transformation like the following: "to cut the yarn with scissors, to untie a knot that was strongly bound, or to felt together." So a slip knot is "reversible" in the sense that if you tug on it, it easily comes undone, whereas an overhand knot would just get tighter. You can think of felting as being equivalent to tying a lot of overhand knots between adjacent strands, they become permanently attached and could only be torn from each other.

reply

srean
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Very interesting.

I don't understand crochet yet but love the math of weaving symmetric patterns on a loom. I somewhat understand the absolute basics of a knit. I understand braids better. All from a pattern appreciation and puzzle solving point of view.All the best for your work.

reply

calderarrow
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building a blackjack card counting tool for people to learn how to count and how to identify games that are winnable. It is designed to take a completely novice to an advanced, winning card counter, using a Duolingo like approach - mastery based learning across sequential modules. Minus the ads and dark patterns.

reply

helloakariq
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

That sounds super cool! When you say Duolingo do you mean spaced repetition? If yes, have you identified what type of spaced repetition approach you will take?

reply

dudeinjapan
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think he means an owl that gets progressively angrier/sadder/more emotionally manipulative if you stop counting cards.

reply

midnight_sun
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

that sounds cool

reply

okira_e
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I am currently building a powerful TUI database client (that supports Turso as well) as I grew fed up with heavy db clients that take gigabytes of ram when rendering data that is text. It's also very convenient since you can launch it with a saved connection from any terminal anywhere.

It's still early in 0.1v athttps://github.com/okira-e/TUIQLbut already supports everything day-to-day that you would need.

reply

jballanc
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on RVW, my adaptation of the standard transformer model that is capable of online continual learning without catastrophic forgetting. I finally published the first pre-print of my early experiments: 
https://doi.org/10.5281/zenodo.20064617

Now I'm working on expanding the work into more parameters and improving performance. I just finished an extremely harsh test of a Nemotron-flavored RVW that consisted of stretches of a random assortment of domains interspersed with long runs of single domains. Across all of it the model didn't forget (and actually improved on some of the more challenging domains). PPL on SmolTalk is still in the ~18 range, which I'd like to get lower, but this is all with only 4B params.Currently, I'm training a Llama 3.2-flavored RVW with only about 2B params to see how that turns out. Depending on results of that, I may take it to Gemma 4 next.

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Super interesting. I'm also super into the idea of always online continual learning.

I'll check it out. Thanks for sharing.

reply

digi_wares
 
26 minutes ago
 
 | 
prev
 | 
next
 
[–]

working on tera.fm- a site which read out loud summarised news from top channels like BBC, Reuters, NPR, Al Jazeera and 75+ more plus has a live FM radio and curated channels. Try it out.

reply

busymichael
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Building Basil (
https://basilai.app
), a privacy-first AI executive assistant / note taker. Everything is on-device: transcription, summarization, etc. So nothing is shared with any model provider.

Lately the interesting work has been less about raw transcription and more about making the output actually useful: recurring workflows, follow-ups, and personalized summaries that fit how someone runs their day. We are also pushing more toward reliable agent automation instead of one-off chat. And dealing with all the iOS limitations on background work.Still early.

reply

quirk
 
59 minutes ago
 
 | 
prev
 | 
next
 
[–]

An idea I'd like to see: 100 ways to think about God. Book and/or podcast. Bring on expert biographers. Research how Aristotle, Pascal, Lincoln, CS Lewis, etc thought and wrote about God.

reply

hxtk
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I made a Python tool to build distroless container images for projects managed by uv. It draws inspiration from Ko from the Go ecosystem and works with/depends on uv from the Python ecosystem, so I smashed them together and called it Kuvo: 
https://github.com/hxtk/kuvo

It’s a hobby project in a very early state where it technically works but it’s missing several things I think it needs before I’d use it for anything serious. As of right now it isn’t even complete enough to dogfood a minimal container for itself without an intermediate base image because it can’t target a platform compatible with the distroless uv container image.

reply

tordrt
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Baton (
https://getbaton.dev
)

A simple organized desktop "IDE" for running lots isolated parallel coding agents without having your brain exploding. That was at least what I was trying to do when I started.Its freemium with all features included for working on 4 concurrent worktrees at the time. No accounts or signup.

reply

schipperai
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A better permissions layer for coding agents. The tool works like auto-mode for Claude Code, so you can stay in the flow and only get prompted to allow or deny tool calls when it truly matters, but it is fully deterministic. My benchmarks surfaced that most Bash calls don’t need an LLM to be classified as safe, ambiguous, or dangerous. A deterministic classifier can auto-allow or block 95% of Bash tool calls as safe or dangerous, with only the remaining 5% being truly ambiguous or unknown.

Conclusion is permission reviews with LLMs like Claude’s auto mode or Codex auto review are like using a data center to flip a light switch - overkill.The main benefit is that your agent’s autonomy can be governed deterministically through policies that can be stored at the user and repo level. The bonus is that you save tokens vs using auto modes.https://nah.build

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

You know I'd love an ability to a "lock" a file from being read by agents.

Casual browsing of a .env is probably my top pet peeve of coding agents.Everytime a secret gets slurped into an API I have to go roll secrets.Does this tool solve that use case?

reply

schipperai
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, you can define sensitive paths and assign 'ask' or 'block' policies to them.

.env, .ssh, and others are treated as a sensitive filenames by default.Similarly, with hosts and network access - unknown hosts pause, trusted hosts can be configured.

reply

kebsup
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a language learning app that combines spaced-repetition flashcards with a browser, ebook reader and a youtube viewer.

The main difference between my app and anki/other generic flashcard apps is that it is for vocabulary only, which allows me to add features specific for language learning.For example, you can set it up such that each word shows up with a different sentence and image each time you see it.https://vocabuo.com

reply

joshuakcockrell
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Envelope. It's a budgeting app that comes with a checking account built in. 
https://envelopebudgeting.com
 Because the checking account is built in, you can assign real money to digital envelopes for bills, groceries, savings, and everyday spending, then spend from the money with built-in checking, debit cards, and envelope-based spending controls.

The idea is to guide spending before it happens, not just track transactions afterward.

reply

LurkerAbove
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I had an idea about explaining ML predictions without direct access to the data or the model: provide basic stats about your data, use them to generate synthetic data, then train a surrogate to predict your model's predictions on the synthetic data.

Could be handy for model risk management and governance, e.g. if you need a challenger model for SR 11-7 without all the hassle of getting access to the original data, getting the black box model set up, and so on. I wrote it because I remember having to create "throwaway" models to show why I needed a better model; it would have been nice to just make a couple of API calls instead.SDK:https://github.com/proxyml/proxyml-sdk-pythonSchema builder:https://github.com/proxyml/schema-builderLanding page:https://proxyml.ai/

reply

jimako
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've just published my first book. The central argument is simple: software development is a design activity, not a construction activity — and confusing the two is the root cause of most project failures. Written for developers, managers, and anyone who has ever wondered why building software is so much harder than it looks.

It's on Amazon in both Kindle and paperback formats.https://www.amazon.com.au/Code-Design-software-projects-deve...

reply

nateb2022
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Simply in the pages I've read through the "Read Sample," I have never seen so many emdashes used in my life. This has got to be AI generated.

reply

schipperai
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I like the overall premise and would be curious to learn more. The Amazon overview reads like it was written with or by AI though.

reply

atiffany
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://musicfestivals.ai
 - find music festivals near you.

I wanted to be able to scroll around a map and filter by month to see what festivals were happening around me and places I wanted to travel, but I couldn't find any great existing tools for this, so I built this thing.The map view looks better on desktop than mobile, but you can still see it on mobile by clicking the map icon in the header.

reply

caerbannogwhite
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Currently working on Bedevere Wise (
https://bedeverewise.app
), a browser-based SQL data viewer for the file formats still widely used by biostat / clinical-data people: SAS (sas7bdat, xpt), SPSS (sav), Stata (dta), plus Parquet, Excel, and CSV.
Everything runs locally: DuckDB-WASM (the SQL engine), the file parser, statistical and plot library (a DuckDB extension that I built).

I wanted a "drop file → SELECT * FROM it" and run a few other explorative queries on a dataset (provided in one of the formats mentioned above). Sometimes, it might even be a whole nested subtree with dozens of files that includes all or most of the formats I mentioned above (trust me, I've seen it many times).
I also wanted something easy to use for my colleagues: no installers, no configurations, no faff. And, most importantly, files never leave the device (which matters for clinical data).The plotting half is GGSQL. I read Thomas Lin Pedersen / Posit's alpha release a couple of weeks ago (https://news.ycombinator.com/item?id=47833558) and that's when I realised I could add the "Grammar of Graphics inside SQL" into Bedevere.
So pastingVISUALIZE
 bill_depth_mm AS x
 , bill_length_mm AS y
 , species AS color
FROM penguins_clean
DRAW point
;in the editor pops a chart without anything leaving the device.This is the demo for the impatient (I admit I am usually one):https://bedeverewise.app/demo(The query is ready to be run in the editor).Feedback is very welcome.

reply

eggbrain
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Lately I've been building Aho (
https://aho.com
) -- an API for verifying age, credentials, and identity using cryptographic proof from digital wallets instead of document inspection.

For context, I built out Playboy's age verification system, and watched as it hurt conversion (nobody wants to upload an ID to an adult website, who would have thought!). Cryptographic signatures from issuing authorities (DMVs, universities, employers, etc) with selective disclosure (e.g. you don't need to upload your full ID, just the fields that matter) is how verification _has_ to work going forward -- AI can fake documents, but not private keys.I've been working on this 6 months full time, and implemented all the W3C VC, OpenID4VCI/VP, SD-JWT specifications myself.Would love to get people's thoughts on it!

reply

ddahlen
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Research grade orbital mechanics, specifically of asteroids/comets.
I've been working on it for 4 years now, finally tried using some AI tooling the last few months and ended up vibe coding a fun little visualization.

(Desktop Strongly recommended)https://dahlend.github.io/ketev/

reply

thearn4
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Good old fashioned machine learning (GOFML?)
Using mixes of different sensor data from industrial 3d printing processes to production quality.
Not as fashionable as LLMs at the moment but there's new innovations to make in the space, so it's honest work.

reply

jithinraj
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on PEAC Protocol.

Logs are local, but some claims need to travel. As agents, MCP tools, metered APIs, and automated payment flows do more work, there needs to be a simple way for another system to verify what was reported later. PEAC issues portable signed records for that boundary.https://github.com/peacprotocol/peac

reply

aleqs
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a general repo shape/structure linter (language agnostic)[0] - the idea is to enforce things like directory structure, existence of various files (LICENCE, etc.), file naming patterns, jsonpath + schema over json/yaml/toml, absence of potentially malicious unicode. It comes with rule bundles for various languages/presets which can be combined and extended. A goal is for it to be very fast, and useable on huge monorepos. I noticed myself having to add various forms of validation/scripts when coding using AI, and decided to build a reusable, fast tool for this purpose instead of rolling validation scripts for each project.

[0]https://github.com/asamarts/alint

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Neat so kind of like Vale but for repo structure rules?

reply

evandev
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I built a maintenance tracking app that I can use for household/garden tasks. I had a problem where things like replacing a battery for a chicken coop, I'd be a month late on replacing it and I had it in my calendar to replace every august, so I'd be replacing it early every year. And I also had in my calendar to fertilize my hop plants every 2 weeks, which meant in January I'd get a calendar event to fertilize my hop plants.

And sometimes my wife wonders what we have to do (especially in spring) for gardening, planting, chickens, etc.https://upkeepnest.com

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I have paid for to do apps to try and tackle this by using the NLP "every 3 months" etc to basically accomplish this.

I think you're smart to spin it out to its own thing because I tend to use them differently batching my chores into a time gate and then using my "chore list" to know what needs to be done. And also the notifications for chores tend to distract from "Important one time task you don't want to forget".I'd consider paying for this if the app was well done and reasonably priced.

reply

notfirstpost
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on DAGraph (
https://dagraph.com
)

DAGraph is a local-first reactive DAG for analytical SQL (OLAP), running entirely in the browser (there is also a native version in the works).Some tech details: written in Rust, targeting WASM (and native). The SQL engine is Apache DataFusion[1]. The UI uses Egui[2]. Workspace data is persisted in browser using OPFS[3] via OpenDAL[4]. The graph is functional and handles dependencies for you (via parsing the SQL).Building this to be accessible for beginners while remaining powerful for advanced users. Still very early, lots more features to add, but now usable.Hope you find it interesting![1]https://datafusion.apache.org[2]https://www.egui.rs[3]https://developer.mozilla.org/en-US/docs/Web/API/File_System...[4]https://opendal.apache.org

reply

yagizdagabak
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

We are working on Vibespace (
https://vibespace.build
), a workspace with containerized AI agent teams. It is free on MacOS and lets primarily non-technical users to manage multiple agents that collaborate together. For example, you share your existing business and it spins up dedicated market researchers, content creators, coders (and other positions you might need). These agents talk with each other to build apps, automations and more! Works with your existing ClaudeCode / Codex subs.

In our previous ventures we've always gotten involved with non-technical teams who struggled with capable yet complex agentic solutions. So far, our shared & containerized workspace within which agents autonomously communicate with each other is our best shot:)

reply

HugoDz
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

No AI stuff, just a web-based level design editor...

https://www.spritefusion.com/

reply

Akuehne
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

That is really easy to use. I haven't tried any game design or anything like that for a few decades now; but in my 10 minutes playing around on it, I liked it a lot.

reply

HugoDz
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for giving it a try! If at some point you wanna make some maps with it, feel free to drop in the discord, I'd be happy to give you a tour.

reply

fb03
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a full blown terminal emulator called "terminal-use", or "tu" in short, for coding agents. It allows agents to operate fully fledged TUI applications including multiple windows, mouse control, etc. It can even self drive a NetHack session via Claude, if you want lol.

It's basically tmux for your coding agent, great for developing and debugging TUI applications as well, because now your agent has a closed feedback loop of applying changes and trying them out itself via tu.https://github.com/flipbit03/terminal-use

reply

zameermfm
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

With AI IDEs, Personally I had to generate a tons of md files for planning a task, analysis on the code for something or other, a task doc for a feature - a summary to paste into the clickup ... and I saw many devs keeps on generating them, and all tucked away into folders. Good, okay.

For the company I'm currently working I had made a VSCode extension where I can sync the task doc with clickup via frontmatter.I decided to take it to next level as a side project. I built a CI integrated, git-native, agent template transformable syncing pipeline with git MD files to any project management tools. That means, either you can save your md files vanilla in your wiki (thus using the clickup AI search to dig up later, get insights etc) or you can use a AI agent template transformer to turn it into a task template (Background, acceptance criteria, functional requirements etc.) and update or create a task on a board.I've been working on it now. I don't know how it will fare, but I feel like product is coming up nice.https://mdspec.dev

reply

kukkeliskuu
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Great idea!

I was actually working on last weekend with something that has similarities. I am working on USM.tools, which allows specifying your services in structured way.There is a need to specify some of the data in semi-structured way, and I am using markdown for that.So there is this interesting relationship between unstructured, semi-structured and structured data, and markdown hits that middle ground.Can I suggest you make some Jira etc. templates on your landing page clickable, so a visitor can grasp your idea more easily? For me it was not clear whether the specs are just plain markdown, or do you have some additional tagging there.

reply

zameermfm
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Great idea you got, what would be a classic use case? We have a data source and we can define the API structure to get them?

Sure! thanks! thats good idea, to have it clickable and true that needs needs to be easily understandable.

reply

kukkeliskuu
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Service management is business oriented, what is the service we are providing and how do we deliver it, and how do we agree with the customer what we deliver. And when the data is structured, other interesting oppurtinities become possible.

This particular use case is people working together to collect data in a workshop. 10 people don’t want to see somebody searching for the right place in a form, it interrupts the flow of the meeting. You need to capture the ideas raw, and then structure later. That is where question anout how unstructured data is captured in strucured format pops up.It is a workflow I directly support in my tool, not a generic tool like yours.

reply

nowami
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm continuing work on my daily procedural logic puzzle, Ruly.

https://playruly.com.You play by setting rules onto a small grid of numbers to maximise your score.My focus the past few weeks has been on refining the difficulty by experimenting with different rule types, and improving the UI.I'm pretty happy with the look and feel now but feedback is always welcome, and I'm especially keen to hear what you think of the level of difficulty of the puzzles. It's a tricky balance to introduce variety without adding complexity.There's a (very) small contingent of daily players now which is really motivating.Your comments very welcome.

reply

hemant6488
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on SoundLeaf on ios, an AudiobookShelf client for listening to your selfhosted audiobooks and podcasts.

https://soundleafapp.comhttps://apps.apple.com/us/app/soundleaf/id6738635634

reply

bryanhogan
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Working more on my customizable app for self-tracking! It combines elements from habit trackers, health logging and journaling.

The website & launch list:https://dailyselftrack.com/Made a lot of progress recently, doing the last iteration of user testing before releasing the Android version.Sharing some of the progress on BlueSky as well:https://bsky.app/profile/bryanhogan.com/post/3mkbzefvebc27

reply

ryanczak
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

refactoring memory management in 
https://github.com/ryanczak/daemoneye
 to better support continuous operation over long time horizons where state of monitored services/things drifts and knowledge becomes stale over time.

reply

jjcm
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a diffusion-powered UI design tool. My short term goal is to make AI-designed UI not look like Tailwind. My long-term goal is to be Figma, but powered by diffusion.

https://diffui.aiI quit Figma about 4mo ago to start working on this, and the gpt-image-2 drop really legitized the bet. I recently release Brands for diffui, which let you establish a design system and consistently generate with it. I made a Brand out of the recent UFO files release, which allow for some really fun designs:https://diffui.ai/brand/2ff1b00a-d698-43ea-a42e-7c4a2e670c04(no account required to generate with this if you want to try)

reply

sync
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Neat! FYI when I tried it out, seems like there's a 60s timeout:

[Error] Failed to load resource: the server responded with a status of 504 (Gateway Time-out) (generate, line 0)My "prompt" was, uh, simple: "Turns out, you don't need water to live."

reply

zeta0134
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Still chugging away at my NES rhythm game. Currently, in addition to climbing the content mountain (so, SO much pixel art and music needs to be made) I'm also slowly learning video editing workflows. I was able to put together a brief gameplay trailer this last week:

https://store.steampowered.com/app/4129270/Tactus/Right this second I'm looking for an alternative to After Effects that runs on Linux systems, as kdenlive has some limitations with its layering implementation. I'll probably give Blender and Godot both a whirl, as I want to get more comfortable with those tools for future projects.

reply

mchaver
 
1 minute ago
 
 | 
parent
 | 
next
 
[–]

Very nice looking game. I added it to my wishlist.

reply

nosioptar
 
22 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I can't overstate just how much I love seeing a NES game developed in 2026. It looks great. I really like the music too.

Have you considered also releasing it to itch.io? (I don't do business with Steam due to DRM and their inaccessible website.)I would happily purchase a NES ROM file so I could play it on my pitendo (RPi3 in a case that looks like an NES).I'm not well versed in video editing. That said, the people I know who are tend to use Da Vinci Resolve.

reply

zeta0134
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is indeed also on Itch. I'm planning to release both, along with a physical cartridge at some point. It's a real NES game, so a ROM is included. (No DRM, of course. I'm not even sure how you 
would
 achieve DRM on a ROM chip.) I test on an Everdrive N8 Pro. It's a big game, so simpler flashcarts tend to not be able to run it.

https://zeta0134.itch.io/tactus

reply

vunderba
 
22 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nice job. I'm assuming this was inspired by Crypt of the Necrodancer? It even has a similar looking "bounce" motion when the main player moves.

https://store.steampowered.com/app/247080/Crypt_of_the_Necro...

reply

zeta0134
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Aye, the inspiration is not subtle. Technically it is the latest entry in the "rhythm-based roguelike" genre... which to my knowledge mostly includes CotN and its sequel, Cadence of Hyrule. Both are excellent, and I recommend them highly. Of course I'm unaffiliated, so this is more of a spiritual successor (... demake?) and is its own thing in terms of IP.

reply

motoroco
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I wanted a faster, easier mapping app to plan motorcycle rides for myself and with groups, so I finally bit the bullet and started building my own at the beginning of this year.

I got to the MVP state which was useful for my personal use case in about a month. I took it further than that as a learning exercise and as a means to share it with others. Some features that came later are live cursors (like Figma), elevation chart and grade overlay, and QR-code enabled collaboration links to make in-person sharing simple.Check it out!https://plotalong.appFiguring out the exact UI/UX I wanted was the hardest part. I did the branding myself, handdrawn on paper, traced in Procreate, and vectored in Sketch. Fast iterations and a good test suite made it possible to try lots of different approaches and refine the one I liked the most. There are roughly 4000 unit tests and over 300 e2e tests that run on multiple environments with fully automated CI/CD.I’m using Mapbox for the frontend and the whole app is basically just a monolithic Cloudflare Worker. Claude pretty much implemented the entire thing. I got a lot of mileage out of self hosting a Gitea project and recording all my planning sessions as Milestones and Issues. Claude has his own account without admin privileges. The process of managing a team of agents to build this practically autonomously was a bit jaw dropping and eye opening to be honest.I would love to hear from other pleasure & sport drivers about the features they use or want the most in a routing app. I have an Android app in Play Store review, if you’d like to be an early access tester shoot me an email at my handle @plotalong.app

reply

danparsonson
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

Very nice! Does the sharing feature allow live location sharing? That seems like it would help a lot, especially when group members are in separate vehicles.

reply

motoroco
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, and while that does sound like a pretty obvious feature I should clarify the app is about planning, not turn-by-turn directions. You can open Plot Along routes in Google Maps, Apple Maps, multiple GPS formats and more

The idea is everyone opens the same route for coordinating and there’s just one source of truth for the group. And then when you’re all about to hit the road, everyone can use the nav app they’re already familiar with (or that’s built into their vehicle)I will tackle the navigation aspect at some point if I do keep up on feature dev, though!

reply

adkaplan
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I understand the need for this and like what youre doing. Ive tried to look before for a good app for this ans always been disappointed. I like the way you've deferred the map direction call so moving a pin around doesnt feel sluggish like other apps Ive used.

Suggestion if youre open to it: emoji or text badges for each stop (e.g., or )I also think itd be helpful to have route leg times shown directly on the map as popout tooltips. Knowing stop 2 to 3 is five hours is critical, and how we plan.Suggestion for your pay model: I think it would be lovely to be able to use this with no option to save. Or, maybe a single fee for an administrator that allows up to x users for one month with only one routr? I only do these kinds of trips yearly, so a monthly fee for three collaborators just wouldn't work. Would we all sign up then disable our accounts? Its hard to imagine that model working for me (RV road tripper with 3-4 people) I think Id be willing to pay the $5/pp that allowed me and x friends to all jump in. Having each person set up their own paid account feels like a harder sell.

reply

motoroco
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for the feedback. As it is right now, only one person needs to subscribe in order to collaborate. I’ll definitely make that clearer in the marketing material!

I like your emoji suggestion. I realized little while ago I need to distinguish between different types of waypoints so this is great validationI think you’re right about getting people into the actual app faster, before signup. I’ll have to prioritize that sooner than later

reply

nicbou
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Brilliant! I definitely felt the lack of appropriate solutions.

reply

AtticusTheGreat
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I built on online multiplayer boggle game back in 2008 that somehow drew a lot of users, many of whom still play every day after 17 years. About a year ago I started a rewrite from scratch in more modern technologies but stalled out after getting to about 80% of the way there. A few months ago Claude enabled me to finish the remaining 20% and was able to relaunch mostly successfully! It's been tough though. I'm a dad with three kids and use Claude all day at my day job and my interest in working late isnt always there. But I'm eeking my way to something that hopefully can stay up for another 17 years.

https://serpentinegame.com

reply

pyk
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Alright, I am building QuizFox, a small daily trivia app for iOS: 

https://apps.apple.com/us/app/quizfox-daily-trivia-game/id67...

I’ve always liked trivia / Jeopardy-style games and learning, so this started as a fun side project to see how quickly I could build and ship something “real” using AI-assisted development (I got my niece and nephews in there trying it out, so a success there for them to see that they can build the next new awesome app themselves!).AI dev is definitely hit or miss on development, but I am surprised at how well AI is doing some app dev tasks (using frameworks it does exceedingly well, not surprising!), and also some misses (trivia writing it does oddly well, but verifiability is imperfect, I had some issues early on with hallucination to fix, but pretty good now!).Would love feedback, especially on the onboarding, obvious gotchas, question quality, and the app overall, I am using it to learn a lot quickly!

reply

jstrebel
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I am trying to build a simulation that lets a simulated organism come up with its own small language, purely learned from sensory input: 
https://github.com/JoergStrebel/VirtualZoo/blob/main/compute...

I would like to implement the ideas put forward by Stevan Harnad in his symbol grounding problem paper (Harnad, 1990).

reply

deptheos
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm building Deptheos (
https://github.com/ryanmitts/deptheos
), a photography/macro focus stacking program.

It works on MacOS, built with Swift and Metal. My goal is to make a super fast, and free, focus stacking program. I provided a notarized MacOS DMG for the initial release, but if built yourself, it will run on an M4/M5 series iPad Pro as well.The core ability I wanted was to support RAW files as inputs, with DNG files as outputs. This is done using either LibRaw, or Adobe DNG Converter (runtime options).I have been really into macro photography the last couple years, and have been slowly working on trying to build my own program to handle the focus stacking.

reply

matthew-wegner
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool! Do you know Thomas Shahan's work? He once contributed his woodcut artwork to a videogame, so he does seem very technically curious. I bet he'd be interested in trying something like this out with his own work and providing feedback...

reply

keepamovin
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

BrowserBox demos: 
https://win9-5.com/demo

These embed a remote browser in an iframe to give you “embed anything browser view” custom elements. The demos focus on retro desktops to emphasize the browser - as these common web tropes, the retro desktop, can never actually ship a real browser without something like bbx.https://browserbox.iohttps://github.com/BrowserBox/BrowserBox

reply

adikso
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Maybe I'm slow, but tbh this "retro desktops" demos were more confusing than helpful for me. I had trouble understanding what are you trying to show with this - why is there a full desktop with multiple apps, and it takes several clicks to open this web browser. "embed a remote browser" and "embed anything" in the same sentence - anything? Like are they embeding streamed windows 95 os? Is this entire windows simulator streamed (too good quality but could be some streaming svg magic)?. Too much irrelevant details and elements. Obviously I understood after these several clicks and seeing heavily compressed browser window, but I found Hyper-Frame browser to be a clearer demo.

reply

keepamovin
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks you for looking and for sharing.

Hyper-Frame is supposed to be the "developer" demo that engineers will understand what they can do with it. I think it succeeds at that. I'm glad you found it useful.The desktops are more labor of love, nostalgic, imaginative. I grew up in that time. They complete the "art" of web desktops by giving them internet access, which otherwise all omit. I don't care that they bury it seamlessly rather than making it obvious. I like that it's integrated as it would be in an OS, that's part of it. Your point is accurate that they do not surface bbx obviously.So these desktops and glitch are more meant to spark imagination, maybe prompt product ideas for people who could be inspired by that. It's supposed to, I suppose, work subliminally, by letting you play around with it in an immersive setting. I suppose it's a different buyer profile or purchase stage they are meant to be honey for, not the "give me what I want now" seeking, but the more playful, relaxed, idea-sparking stage/persona. It's meant as an art gallery :)You probably got annoyed doing it - that's okay, it's probably not really for you.I feel the set of demos taken together cover the things I was wanting to express about this. I'm very happy with them - both individually and all together.Thanks for looking - and for your great compliment - yes windows is all HTML, notice it says Windows 98-and-a-half ! :) They are also really just meant to be fun, and I had fun creating them. And meant as a show off lol :) - I like it when people enjoy a beautiful time playing around with them.

reply

alasano
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://engine.build

It's a durable orchestration system for AI code generation which solves the problem of not being able to trust LLMs to complete long running (and high quality) implementations without having to babysit them and monitor the process, which is what I think is the most exhausting part of coding with AI.You start with a spec or programmatic task list and the engine runs the whole workflow: implementation, verification, review, fixes, and finalization.It treats agentic coding like a durable CI-style process, with state, retries, reviewer feedback, commits, and auditability built in. It's externally orchestrated, meaning it's not the agent running the loop, it's simply agents being used as tools and spawned in the loop as needed without awareness of the loop itself.It's going to be open sourced soon and it's not meant to replace your IDE or Agentic Harness of choice. You keep using codex/claude code/open code/cursor/pi whatever you want and simply delegate the actual implementation to the engine, through MCP/CLI and other integration points.It supports any LLM provider so you can have GPT 5.5 implementing and a mix of Opus 4.7 / Deepseek v4 Pro / GPT 5.5 reviewing at every phase for example.Sign up on the website or follow us onhttps://x.com/enginedotbuildor me personally onhttps://x.com/aljosa, desperately need more followers :D

reply

Orelus
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I do calisthenics 3×/week plus Ironman 70.3 prep, which means my training lives across Garmin, Polar, Withings + FIT files and front-lever sessions that no mainstream app models. So I built one that does both (and have been using for the past 4 years+): logs custom strength moves (front lever, FLAC, ¾ pull-ups), aggregates the connected devices (Polar, Garmin, Suunto, Withings, Apple Health) into one weekly view.
Currently trying to see if can integrate some AI insights to my training routines.
App is free for now as it does not cost me much (only servers for now), comment / use cases welcome: 
https://obitrain.com/

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I had my problem in the calisthenic app space as well. Rowing, cycling, biking, calisthenics. Each sport has such specifics I wish there was an open standard on the data for better interop.

reply

schipperai
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Which platform have you found is most hackable? I have Garmin atm and like it but there’s no easy way to pipe my data into my agent or server for offline analysis.

reply

Orelus
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I’ve only really had trouble integrating Withings.

Working with Apple was also challenging because I had to purchase an Apple Watch or iPhone (the data is stored locally only, with no server or API to call, which is great from a privacy perspective) and then deploy specific code on the device.I’m not sure if this helps your use case, but I was planning to make the API public and create a CLI (similar to Sentry or Grafana’s gcx) to access it. But if you want a local first option, not the best solution

reply

frankdenbow
 
22 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

working in adjacent space for tracking more visual sports 
http://ballers.gg

reply

notesinthefield
 
23 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why so many different devices? (Assuming this is the only reason there could be this much sprawl)

Device based strength tracking is still so weird to me.

reply

Orelus
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm a Polar fan, but unfortunately for cycling it's missing devices like the pedals power meter.
Withings, only the scale with body measurements.

Then you have friends and family that don't have the same devices than you and are nice enough to want / try your app.

reply

mikestorrent
 
23 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Have you seen that meme template, where the midwit wants to use a thousand complicated things to optimize their experience, but the grug and the genius both keep it simple?

I think this is a perfect example... somewhere out there a genius and a grug are happily exercising together for the simple joy of doing so and feeling good in their bodies, and nearby is a midwit with the GDP of a small village worth of wearable electronics wondering where the joy has gone as he laments the 0.1% of VO2MAX he's dropped since his last gadget-run.

reply

ricardobeat
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In this case it might not be as complicated as it seems, they might be using a Polar device for workout tracking, Suunto for marathon training/hiking, a Garmin as daily watch (payments, music etc). Add to that a Withings scale and an iPhone, and you're dealing with a melting pot of apps.

reply

Orelus
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah that's exactly that:
- Polar watch + Verity Sense for workouts / running
- Garmin pedals / monitor for cycling
- Withings for the scale
And I had to integrate .fit file upload for Zwift / Trainerroad trainings.

reply

grvdrm
 
23 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I haven’t trained for an Ironman but have for a marathon. I do think some metric oriented work is helpful! But I laughed at your post. Happy to see both sides.

reply

cosimo-dw
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building retcon (
https://github.com/WujiLabs/retcon
), a Claude Code middleman layer allowing the AI agent to edit its own conversation history or rewind itself to a previous round. More than often you ask the AI to do something. It misunderstands. You correct it by words. But the messed-up turn stays in context, and the AI is fighting both your correction and its own past mistake.

retcon flips the model. The tool is named for the verbrecontextualize: introducing new information that reshapes how the past is understood. Instead of you typing a /rewind command, the AI retcons its own past. You just tell it what you want.

reply

jcubic
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a few projects:

* ASCII-Globe =>https://github.com/jcubic/ascii-globe* Horavox (a speaking clock) =>https://github.com/jcubic/horavox* Mutimon (generic config driven web scraper and notification system) =>https://github.com/jcubic/mutimon

reply

signalbright
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a Sentry replacement that adds logs automatically and fixes any bugs it finds (
https://superlog.sh
).

The setup is done via one prompt ('Usehttps://skills.superlog.shto install Superlog in this project'), and everything on the platform is usable via MCP so that you don't have to spend time configuring yet another UI.

reply

nateb2022
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

I like the premise but trying to be both the coding agent + the monitoring agent seems backwards. Your tool will mostly only be valuable IF it is the best coding agent out there. You're going to be competing against companies where automated PR agents are their sole product, and you're probably going to lose.

Do one thing and do it right.Where I could see this succeeding is if you embrace the monitoring agent role. Customers can expose their coding agents, setup however they like, as an MCP server that your monitoring agent can plug into. If something goes wrong, your monitoring agent gives their coding agent the best context it can, and steps out of the way.

reply

kukkeliskuu
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I really like this premise.

Recently I have had trouble with Sentry. I have a site that has a lot of data coming in (2M page views per month) and Sentry starts being unusable for a solo developer. And on the other hand, I have several Django projects where I want to have common way to handle bugs.I am feeling Sentry UI is too complex for my use cases, and on the other hand, I would like to automate the process as much as possible -- and the idea of automatic bug fixing is neat!I am experimenting with Bugsink. Supporting Bugsink internally but build some tooling around it for automatic bug detection and fixing would actually be a sweet spot for me.

reply

aaronbrethorst
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building OneBusAway Cloud, which you can think of as being 
Heroku for public transit
.

https://onebusawaycloud.com/It’s a project of the non profit Open Transit Software Foundation that we’re using to fund our other initiatives, like bringing realtime transit information to billions of people around the world.All of this depends on a bunch of really cool open source projects we’re building, like Maglev, a Golang server that can power realtime transit apps. I wrote up a blog post explaining how to set it up here:https://opentransitsoftwarefoundation.org/2026/04/setting-up...We’re always looking for volunteers, especially non-engineers.https://ossvolunteers.com/organizations/open-transit-softwar...

reply

TZubiri
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

I built something in this space.

Do i understand correctly that the product is a white label app for public transport providers that riders can download to get arrival data?Do you think people will download an app for each bus/train? Isn't it better to integrate with google maps or equivalent?

reply

aaronbrethorst
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There are several different ways that OBA can be deployed and used for a transit agency or a group of transit agencies in a given region. I'll give you four examples, but this isn't an exhaustive list:

1. The Puget Sound region, where a regional transit authority, Sound Transit, currently maintains their own OBA servers on behalf of a dozen individual transit agencies. Sound Transit piggybacks on our official OBA apps which you can find in the Play and App Stores. The official apps also work in 10 other cities across the US. This is the ideal for us—and transit riders, imho, and similar to what you see with apps like Citymapper or Transit.2. New York City, where MTA runs their own OBA servers that power their own branded app and realtime signage throughout the five boroughs.3. UC San Diego, where the university is using OBACloud to power real time transit information systems for students on campus.4. Republic of Cyprus and Malaysia (yes the entire countries), where enterprising individual developers have set up their own OBA servers to power realtime transit information systems for their fellow citizens.The underlying OBA server provides a rich set of REST APIs that make it much easier to build a public transit app than using raw GTFS and GTFS-RT data:https://developer.onebusaway.org/api/where/methodsWe also have SDKs for many major languages so that agencies and independent developers can build their own apps on top of OBA servers without having to fiddle around with the intricacies of our APIs.https://developer.onebusaway.org/api/sdk~~~Integration with Google Maps is important, and a "yes and" solution. I think there's a lot of value in having public transit-focused apps, especially ones that don't have advertising or questionable privacy issues.~~~edit: I noticed you're in Argentina. The Ministry of Transportation maintains its own white label version of OBA called Cuando Subo.https://www.argentina.gob.ar/sube/cuandosubo

reply

technomoloch
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

working on artifactguesser.com - where you see an image of an artifact and guess the country of origin, and the date. free hobby project.

notable things about it: have over 230k artifacts in the database, aggregated from 7 museums - might be the biggest artifact index on the web, but idk didn't look hard.has multiplayer. Its just fun to see weird stuff you wouldn't be able to see in museums. Its stumbleupon but for artifacts. Its been very fun to work on.Future stuff: 3D museums, 3D artifacts, and building hidden tombs to protect and preserve artifacts into the far future

reply

Sh0000reZ
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Linux distribution experiment where all user data (/home) is loaded from a model

Distro boots to a custom Vulkan based, GPU accelerated browser; like a game engine or blender where the controls/parameters are hidden and updates are driven by AI given a promptAm using BPF and sched_ext to manage a bunch of the usual behind the scenes telemetry and observability and inform the AI which responds by tweaking run stateSo / and /root and /usr, the other POSIX paths exist but instead of /home it's an encoded binary model.No unique users relative to the OS, but while I run everything as root the AI protects the model unless given the appropriate secret.Not perfect security by any means but this is an experiment above all not a production system

reply

tmilard
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

https://www.free-visit.net/

One day FPS builder.

reply

thisisjedr
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://docx-editor.dev/
, the open-source, mit licensed word editor library.

We are building this because we such library it in our core business, and a lot of other engineers seem to need it too. We have contributors showing up with bug reports and fixes, and real interest from people building apps around .docx docs.My previous show hn post (https://news.ycombinator.com/item?id=46947229) got a lot of skepticism because we're developing heavily with AI, but with active community feedback and proper ai oversight (mostly me), I'm super proud of what we have now.

reply

ricohageman
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A timelapse platform powered by community photos. The idea is to place a mount and QR code at fixed viewpoints around the neighbourhood. People scan, photograph the view, optionally add their name, and submit. Over time, the platform stitches those shots into a living record of how the place changes with seasons.

Just finished the software side using a boring technology and am about to order the materials for the first few locations. Curious to explore photo alignment once real submissions start coming in. Stitching all slightly different angled photos into a smooth animation seems interesting.

reply

lokmeinmatz
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

Love the idea!

reply

brianjlogan
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an Alpha with a tester group for a learning product. A personal research extended to curriculum building and team training SaaS. I'd like to open source it and work on federation but those don't pay the bills yet. 

https://chunkker.com

Coop I'm trying to bootstrap. Interested in building tooling and experimenting to make Sociocracy viable. No VC, No external investment, other than mulling Coop bonds for capital raising capability.https://kinkoda.comFeel free to contact me via the web forms if you have experience launching apps or platforms like this or you're just interested in discussing the product.

reply

redat00
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

An alternative to Ansible and Puppet, written in Golang.

It's called Peekl, and the idea behind it was to merge the two things I loved about both Ansible, and Puppet :
- The agent/server model of Puppet;
- The ease of writing Ansible code.It also make sure to solve the problem that both Ansible and Puppet have in my sense :
- Puppet is a slow, decades old application. It's written in Ruby and run inside of a JVM for the server. Applying a catalog can be very long on complex configuration setup.
- Ansible on the other side works well, but the absence of an agent makes it hard to deploy stuff at scale : You being spending more time running your playbooks, than actually doing stuff.So if you want to take a look at this alternative, head to the Github repository. Feel free to break it, open issues, and pull requests !https://github.com/peeklapp/peekl

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I like your idea. I didn't have the time to fully build mine out but I also was hankering for something with better readability and implementation than SaltStack (server/client similar to Puppet).

https://github.com/vangourd/g8rThe pub/sub model was so much FASTER than the Ansible push methodology.I'll check your repo out for sure

reply

r888888888
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building HomeBidder (
https://homebidder-web.fly.dev
), a tool for figuring out a realistic bid price for houses. I got sick of seeing artificially low listing prices on sites like Zillow so built this tool to give me a more realistic number based on comps. Along the way I've learned to add confidence intervals, adjust for lot size and fixer status, and provide QOL information like access to transit and how bad the pollution is. It is heavily optimized for SF but I'm starting to iterate and validate on other cities.

reply

monerofglory
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I've made 
https://rankr.click

It's a little web application that allows for the ranking of all kinds of abstract entities. Think of the merging of Goodreads for books, Vivino for wine, Letterboxd for film, etc. This will allow you to instead rank whatever you want across a variety of different categories in a single place.Using your rankings across all these different fields, you can draw analysis of what you like, and in future I'd like to add a little personal (not an ad) recommendation engine to help you find new stuff based on your actual interests across loads of different categories.From a technical point of view, its been a great learning opportunity on how to fully host a complete stack using an opiniated, but cross-platform orchestrator, allowing me to host this wherever (bare metal VPS, homebrew system, cloud provider) in a flash.

reply

olpad
 
22 hours ago
 
 | 
parent
 | 
next
 
[–]

You might want to add a home page that doesn’t require a google sign in so that visitors can see the product before any commitment

reply

adikso
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Having to give your personal data associated with Google account to see anything more than login page is too much.

reply

coolThingsFirst
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Backend dev gets in a fight with frontend devs. Vows never to built sane UI for his remaning lifespan.

reply

joelres
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

[Colma](
https://www.colma.ai/
) solo venture, working with my dad who has been in digital marketing for 30 years and has a small agency.

Takes any website, does deep research on who's searching, what your offers are, etc, and then makes a plan and recommendations to get you more visibility on Google, ChatGPT, etc.These days, there's really no excuse for someone with a website to not be doing these things to get more visibility, and I've found generic LLM advice to be pretty bad. Contact if interested or curious! Currently in pilot stage with a few agencies and website builders.

reply

planckscnst
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on [Context Bonsai][1] - LLM harness tools that allow the LLM to prune messages out of the context, leaving behind a summary and keywords instead. In addition to a "prune" tool, there is a "retrieve" tool that allows it to recall the messages if needed.

In addition to these tools, I'm also building automation that will port the tools from the reference implementation (OpenCode) to other harnesses (Claude Code, Cline, Pi, Gemini, Kilo, Codex, others to come?). As well as automation that will either cherry-pick or re-implement commits onto the latest head from upstream.[1]:https://github.com/Vibecodelicious/context-bonsai-agents#con...[2]:https://blog.vibecodelicio.us/posts/how-i-fixed-context-wind...

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Neat so smarter pruning than just an auto compaction event?

reply

planckscnst
 
41 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, also happening more or less continually instead of waiting for the context to bloat up.

You also have some control over it. You can say something like "prune away the work we did on the UI. Make sure to remember that users can upload multiple images now"

reply

coreylane
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://dataraven.io
 managed rclone for object storage.
It’s for teams running cloud-to-cloud transfers, migrations, and scheduled syncs without having to own any infra.

I'm focused on the operational features rclone doesn't have out of the box: notifications, centralized logs, team access, audit logs, and analytics like bytes transferred, objects changed, and failure rates. Recently reworked the guided onboarding flow and im adding more storage providers.The BYOV secret support is pretty unique and im surprised more platforms don't support the model.

reply

navanchauhan
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I am finally getting close to my vision of `write once run everywhere with SwiftUI`. The idea is to create a drop-in replacement called OmniUI which will have different renderer backends (I currently have TUI w/ notcurses and Adwaita/GTK working)

s/import SwiftUI/import OmniUI/As long as you aren't using Apple platform specific libraries like Vision, you should be good for the most part. I am going to make my Gopher browser (https://web.navan.dev/iGopherBrowser/) the first target. I have done some extra stuff like reimplementing CoreData/SwiftData to make it work on Linux.I am going with Adwaita instead of pure GTK because I like the opinionated approach they have with their design language. I think the reason SwiftUI works is because you can get pretty looking apps without thinking too much.Projects like adwaita-swift, and swift-cross-ui do exist, but I want my library to be a drop-in replacement. I don't want to be inspired by SwiftUI, I want to use SwiftUI everywhere!

reply

vintagedave
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Do you have a repo you can share? I'm curious to see.

reply

navanchauhan
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Technically, it is on GitHub in my swift-omnikit library. But, this library is only meant to be consumed by me for now.

I plan on separating out the UI portions to its own repo and then polish it up

reply

illist-ell1s
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a UI framework with VueJs to dynamically create webpages

https://c0ckp1t.com/default/docs/Articles/Why-Project-Exists...

reply

_66o
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Dream Chimp - 
https://dreamchimp.app

It's a 3rd party preset editor for Universal Audio UAFX guitar pedals [1]. I'm supporting Dream '65 for now, rolling out support for Lion '68 next week. More pedals will follow when I have some free time.If you're a guitar nerd and own one of those pedals please check it out!Oh, it's completely free too!---[1]https://www.uaudio.com/pages/uafx-pedals

reply

jdc0589
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

A good generic terminal UI app for reviewing git diffs, making comments, etc...

Lots of these have started popping up, but almost every single one of them is a TUI interface forgithub, orgitlab.
What I'm building is for local git by default, but has an extensible plugin system to support integrating with github/gitlab/azure ado/etc... for their PRs and approvals, but forced in to a single consistent UX and workflow.Its good enough for basic diff reviews that it has become my daily driver for about a month for reviewing my own stuff before I push changes remotely.

reply

sm001
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

A system to learn how to chat with dolphins, at 
https://www.dolphinwhispers.com
 and maybe become a contender for the 10 million $ Coller-Dolittle Prize 
https://coller-dolittle-24.sites.tau.ac.il/

reply

ramon156
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool! Although I'm not sure why you would want to win a contest from "Tel Aviv University". To each their own, I suppose.

reply

falseprofit
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The contest has a cash prize. Why did you put the university name in quotes?

reply

tombert
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm mostly diving head first into formal methods again. Mostly TLA+, but a bit more Isabelle as well.

I haven't really forgiven myself for dropping my PhD; I think it was the right decision at the time, but I also kind of wish I had pushed through it. I'm going to see if I can at least get a few papers published.I've also had some fun getting Claude to create LSP servers for different languages, which it has been pretty good at, and that's nice; having good integration with Vim makes a language a lot more fun for me.Oh, I also presented at LinuxFest two weeks ago:https://youtu.be/HmcVJWyOwJQ?t=6623

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Are you familiar with FizzBee. I think formal methods is already very hot right not with more demand for proving AI generated code isn't garbage.

(Even if you're hand writing people are going to assume or suspect it's LLM gen.)

reply

tombert
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am!

The author of FizzBee reached out to me about a year ago on LinkedIn actually, because I gave a talk on TLA+ a few years ago.I haven't really played with it yet (outside of the few examples on their site) because I'm already pretty entrenched in the TLA+/PlusCal world, but it is very likely that FizzBee might be a better fit for software engineering circles; the incremental testing is pretty neat, to a point where I kind of want to steal the that and port it over to TLA+/TLC. Probabilistic testing seems pretty cool too.If I were getting into Formal Methods today for the first time, I would almost certainly be using FizzBee and/or Alloy.

reply

brianjlogan
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have knowledge of FM primarily from HackerNews posts about it.

As someone lacking your academic background in it could you give me some advice on a good starting point, or perhaps papers/materials that are absolutely unskippable/foundational to understanding it, maybe a good learning exercise for utilizing FM?

reply

tombert
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

FizzBee is likely a good place to start, but since I have never really used it I'm afraid I can't recommend good resources for it.

------If you're just getting started, I recommend checking out my former advisor's book:https://www.amazon.com/Software-Engineering-Mathematics-Sei/...I found this book to be fairly easy to read through, and gives you a rundown of a lot of the notation and concepts that pretty much all formal methods systems require.------TLA+ is a decent enough language. I recommend going through Lamport's video series on it to start:https://lamport.azurewebsites.net/tla/learning.htmlI don't know what aspect of Formal Methods that you want to focus on; most of what I've done is with distributed systems stuff, but TLA+ can and has been used for low level things like circuit modeling. I can't tell you where to learn about that.I think Hillel Wayne's learntla website is pretty good to get a few more practical examples:https://learntla.com/. I actually thought his Practical TLA+ book was a bit better for that though:https://www.amazon.com/Practical-TLA-Planning-Driven-Develop...Both of those resources are more PlusCal focused. PlusCal is a C/Pascal-like language that compiles to "raw" TLA+. A lot of people like it more, I go back and forth.If you care more about the more theoretical aspects of TLA+, Ron Pressler's "TLA+ in Practice and Theory" blog series is great:https://pron.github.io/tlaplusAdditionally, I recommend looking for the papers by Stefan Merz. Here's a good one to start, but he has a bunch:https://members.loria.fr/Stephan.Merz/papers/tla+logic.pdf------If your goal is to model concurrent systems, getting an understanding of CSP is worth doing. I liked Roscoe's book on it:https://link.springer.com/book/10.1007/978-1-84882-258-0If you go deep into that, I recommend looking at the extension "tock-CSP" that adds timing semantics.-------If you're interested in the most theoretical aspects of formal methods, the only one I've done with any kind of intimate detail is Isabelle.Isabelle is much more of a "math proof" thing than a "computer science" proof thing, but there are plenty of computer science things for it too. If you want to get started with the Isabelle/HOL language, the Concrete Semantics book is the normal recommended starting point:http://concrete-semantics.org/------This is mostly my history, there are many other paths but I can't really speak to those with any confidence. Hope this helped!ETA:Just to add, while I did go to school later for formal methods, I actually started learning this stuff while I was still a dropout from my undergrad. I eventually got my bachelors and masters and then entered a PhD program, but for TLA+ in particular I was learning it without any completed education, so this stuff is definitely approachable even without a ton of letters after your name.

reply

brianjlogan
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you so much for this quality reply!

I shared earlier in the thread about the learning app I'm working on. I already have a learning path created in it for Formal Methods. I will be taking each of your points and tracking my progress to completing them.Just wanted you to know your effort won't be unappreciated.

reply

tombert
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yep!

I have an email in my profile, feel free to contact me. Happy enough to answer questions to the best of my ability in the future.

reply

Akiro001
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Social network for gamers (iOS/Android, soon web).

Tinder meets Discord and, somehow, they have their way with Uber/Calendly.It's live if you want to test it:https://jynx.app/Let me know what you think of it.
The main goals I want to achieve are:
1. help with social isolation
2. help e-sport team with sourcing and organizing

reply

Akiro001
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

For anyone interested, the main issue I have right now is that we need a vast player base on at least 1 game for it to be useful. I'm trying with the very limited budget I have right now but it's out of my own pocket. Currently refining the business plan to then be able to start talks with investors.

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'd love this if you could match me based on my time slot available to play games with someone.

reply

ayanmali
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm implementing Raft consensus from scratch in C++ with raw TCP sockets. Right now I'm working on a high-performance RPC client and server to keep network latency to a minimum. The main purpose of this project is to hone my systems programming skills and get more comfortable with distributed systems as well. One of the coolest things I've learned here is event-driven I/O with epoll and how event-loop architectures work in asynchronous setups.

https://github.com/ayanmali/raft

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice! Raft is cool. Looks like a fun implementation project

reply

mohsen1
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on tsz (
https://tsz.dev
)

a performance-first TypeScript checker written in Rust. Started 5 months ago and it's been mostly AI-written code.
99.8% tsc conformance test pass rate today. Single file benchmarks are 3–5x faster than tsgo.

reply

nateb2022
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

See also:

oxchttps://oxc.rs/eznohttps://github.com/kaleidawave/ezno

reply

mohsen1
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm taking a different path than Enzo. Fully tsc compatible and more sound on top

reply

ivanjermakov
 
22 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Wow! How is LSP performance?

reply

mohsen1
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can see LSP working in the playground. It is still WIP but pretty fast. I'll add LSP benchmarks later. My design is highly biased towards fast incremental checks

reply

jcranmer
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Float-explorer, a tool for generating very precise assembly programs to explore the darkest recesses of floating-point behavior on your processor without having to bully the compiler into generating the code for you.

And when I say darkest recesses, I'm not referring to "0.1 + 0.2 != 0.3" (which is fairly well-known) but things like "so when you turn on denormal flushing, how exactly are you defining it because there's at least three different definitions..." Or also "does my emulator actually emulate floating-point behavior correctly, or is it delegating to the current hardware which might have a slightly different definition?"

reply

askari01
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Store Checkout validator, a continuous check for web-store checkout. it visually checks store, its product page, cart and checkout. Kind of cool but it's just an MVP to help the medium/low-end store owners with their website. Targeting people who don't a full time developer :)

yayauptime.com (named after the first words of my friends kid) YAYA!!if someone needs a free signup:https://www.yayauptime.com/auth/signup?invite=YAYA-BETA-2026

reply

a_t48
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://clipper.dev

Docker is...quite slow with large images. I've built a registry+pull client+buildkit builder to make it better. It splits apart layers, allowing for files to be shared between related images. In a robotics context, it can make pulls 10x faster. And in a cloud context, the format allows for pulling an image in 15 or 20 seconds instead of 60, without having to do a FUSE w/lazy pulling. Builds are faster, I store 7x less data due to better deduplication, I can run security scans faster due to not having to unpack tarball layers, etc, etc. I want to be the default registry for all ML related work, in the future.

reply

TZubiri
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

Copy fail and dirty frag killed containers, pivot out of shared kernels now

reply

danparsonson
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You're right - all of mine instantly stopped working and I'm just gonna switch over to pen and paper.

reply

ctrlt
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on creating the most useful browser start page for power users and workers in tech.

https://newtabwidgets.com.One of my favourite features is the iframe widget, which allows you to select any element on a website and turn it in to a widget.

reply

liu3hao
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Having some progress on CircuitScript, a python like language for describing electronic schematics as code: 
https://circuitscript.net
. Try the language through the online IDE at 
https://bench.circuitscript.net

In the past 2 months, I have added support for exporting to the .kicad_sch format. Multi-sheet designs are exported as separate .kicad_sch files, one per sheet. The pin types has been updated to be similar to KiCad's and to better support ERC rules. Setting the GND symbol pin as a type of power_input was a real headache for me, eventually, I decided to define a new pin type, power_reference.The motivation for creating Circuitscript is to describe schematics in terms of code rather than graphical UIs after using different CAD packages extensively (Allegro, Altium, KiCAD) for work in the past. I wanted to spend more time thinking about the schematic design itself rather than fiddling around with GUIs. With code, the design intentions become explicit and reviewable.Feedback welcome, especially from anyone else frustrated with graphical schematic tools!

reply

rocketniko
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

An extension module for Redis or Valkey for in-process Python execution, based on Monty. Learning playground for my Rust skills mostly, but gradually over-engineering it into a whole new ecosystem of sort :-) 

https://github.com/xelato/taranaki

reply

FailMore
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve built SmallDocs (
https://sdocs.dev
; Show HN: 
https://news.ycombinator.com/item?id=47777633
; live usage stats: 
https://sdocs.dev/analytics
).

SDocs is cli (`sdoc file.md`) -> instantly rendered Markdown file in the browserWhen you install the cli it gives you the option to add a note in your base agent file (`~/.claude/CLAUDE.md`, etc.). This means every agent chat knows about SDocs and you can say “sdoc me the plan when you’re done with it” and the file will pop open instead of you having to find that terminal session to know it’s done.Going browser first means you’re not required to install anything to get a great experience.Despite being in the browser, the content of SDocs rendered Markdown files remain entirely local to you. SDoc urls contain your markdown document's content in compressed base64 in the url fragment (the bit after the `#`):https://sdocs.dev/#md=GzcFAMT...(thisis the contents of your document)...The url fragment is never sent to the server (seehttps://developer.mozilla.org/en-US/docs/Web/URI/Reference/F...: "The fragment is not sent to the server when the URI is requested; it is processed by the client").The sdocs.dev webapp is purely a client side decoding and rendering engine for the content stored in the url fragment.This also means you can share your .md files privately by sharing the url.

reply

renegat0x0
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I maintain databases of links

- h ttps://github.com/rumca-js/Internet-Places-Database - Internet places / YouTube channels- h ttps://github.com/rumca-js/awesome-database-feeds - feeds / RSS locations- h ttps://github.com/rumca-js/awesome-database-top - smaller database from above- h ttps://github.com/rumca-js/awesome-database-awesomelists - links from 'awesome lists'- h ttps://github.com/rumca-js/RSS-Link-Database-2026 - 2026 year link metadata- h ttps://github.com/rumca-js/RSS-Link-Database-2025 - 2025 year link meta data- h ttps://github.com/rumca-js/crawler-buddy - crawler engine

reply

slater
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

is there a reason for the space in "h ttps" ?

reply

srean
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Probably to prevent the HN hug of death.

reply

montecarl
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I had a raspberry pi 3a+ and the old raspberry pi touchscreen laying around. So I'm writing a custom dashboard for it using Rust/Slint[1]. It directly uses opengl without any display manager/window system. It mostly talks to home assistant. Right now, when I start a 3d print, it automatically switches to a view with live camera of the printer and some stats. I can monitor the status of my washer/dryer so I know when they are done (using cheap TP-Link Tapo smart plugs[2]). My favorite thing it does, is if any motion is detected on my Ring cameras, it just automatically pulls up that live feed. Took a little work to get decent playback performance but the pi 3a+ has hardware h264 decoding.

Its nice, overall, to have a little dedicated touchscreen on my desk that I can easily tweak to display whatever I want. Its silent and low power.[1]https://slint.dev/[2]https://a.co/d/044MIM3t

reply

serickson
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

https://casedaemon.com/

CaseDaemon: automated intake handling for immigration lawyers. Given a USCIS form to fill out and a set of documents and information, CaseDaemon automatically fills out the form with what it has and prompts the client (directly or via the user) for additional documentation or information needed to finish the application. Takes out a bunch of the back-and-forth between lawyer and client, and the busy-work of the lawyer mapping data to form and tracking requirements.The product will be ready to use in a few weeks, but take a look at our homepage in the meanwhile, curious what people think!

reply

sieve
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

A replacement for python.

- The base is a freestanding register VM deeply tied to the Linux kernel.- It supports a set of primitives types, array types and record types.- Concurrency is Erlang-ish --- an M:N scheduler that can manage tens of thousands of green processes. VM uses instruction fuel to preempt processes.- GC is Cheney for the nursery + M&S for the rest. Each process has its own GC.- tailcall support.- first class functions.- Phase One will only have Vm0, which is clean (it has access to a bounded set of Linux syscalls). Will think about Vm1 that handles the libc infection later.- JIT is not on the table in Phase One.- The language is statically typed and borrows syntax from python extensively, but drops OOP entirely.- OOP is faked using UFCS.- Operator overloading is supported.- Exceptions are the default error handling mechanism. There are two hierarchies: Fault and Error. Fault cannot be trapped without rethrowing. Fault WILL crash the VM.- It is being developed in private right now. As I am User # 0, all the choices I make reflect my own opinions and biases. I might release the code as OSS once the core is stabilized.- I have done very basic microbenchmarking and the VM is so much faster than python right now that it is not a fair comparison anymore. I can also create and iterate over massive primitive arrays with ease. The principal comparison should be C, and here it is consistently about 8x slower and that performance profile will probably remain constant because dispatch has a real cost that cannot be magically wished away. I will be very happy with 5/6x.

reply

pvillano
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I made sdf2stl.saej.in

You can use it design 3D objects with mathematics and bring them into the real world with 3D printing.You can use it to create 3D models that are impossible to create with CAD, CSG, sculpting, or mesh-based tools.You can build on a decade of community SDF development on Shadertoy because sdf2stl uses the same language.A few days ago I may have become the first person to 3D print the equation x^4+y^4+z^4-x^2-y^-z^2+.4=0 (Goursat's surface)https://www.printables.com/model/1713835-goursats-surfacePlease try it out and tell me what you think.https://sdf2stl.saej.in

reply

binsquare
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on building a virtual machine that has the fast boot and portability of containers.

It's called a smol machine free and oss,https://github.com/smol-machines/smolvm

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Ah I think you posted on HN before. Good to see you again. I haven't gotten around to testing smol yet but the DirtyFrag / CopyFail stuff peeked my interest in it again.

reply

binsquare
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes I have! :D that's a great way to leverage hypervisor isolation to avoid those issues

reply

asciimov
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

My partner and I got a 1 year old rescue schnauzer a few weeks back, so we are learning to dog while trying to teach her to sit, stay, and come.

Tech thoughts: this week I decided to move to a new to me NameBrand™ Arch distro. Even though I’ve been daily driving Linux for more than 10 years I still can’t get a new install up on the first try. This time the boot loader wouldn’t load. No error, no log, and no boot loading. A few reinstalls later, I picked a different choice and was finally booting. But then the next problem was the login display manager doesn’t want to sleep the monitor if nobody logs in. Learned this after an overnight power flicker caused a reboot. The monitors running full tilt for several hours waiting for someone to log in. While I would like to say this issue is another joy of the Wayland-way of Linuxing, I have found that other display managers offer the same defect.Anyway dogs are great, I shouldn’t have waited so long to get one.

reply

cdnsteve
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a way for us to communicate software changes properly with people, systems and AI.

I'm frustrated at how we just do library updates and get whatever is next. Things break. Finding a changelog sucks. Vendor updates maybe put something in X.We can do better so I'm starting an open initiative to tackle that.

reply

t_mahmood
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a minimalist journal app that is for really quick single line jots. Can be used for idea dumping, project management, quick calculations, unit conversion, task management etc. Have unlimited undo/redo support, assign tags etc. Will be adding scripting support using Python next. The data is stored in text file, in really human friendly manner, but also in way so that the *nix tool users can easy to navigate the file using text processing tools.

Native application, no web UI, built using Rust + iced.rs, minimal dependency. NO AI.I am putting the best effort to make it performant. Target audience is the users who want's the simplicity of the notepad [non-sloppy one], but still with some bells and whistles to note without worrying about managing the metadata manually.I think with scripting there will be infinite possibilities to play with linear notes, and I want to make that happen.Continuous challenges while implementing features are:1. It should load instantly
 2. Keeping it extremely simple to use
 3. Keeping the interface minimal
 4. Still have ways to let the user find the features easily.Will have a demo version ready soon

reply

faangguyindia
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

MacroCodex - Adaptive TDEE tracker

Most TDEE calculators only provide estimates. MacroCodex helps you refine those estimates to calculate a more accurate TDEE, which continuously changes based on your activity level and calorie intake.Not only this, it helps you figure out when to lean bulk, cut, recomp. It automatically provides you recommended macro and calorie targets (which change as your adaptive TDEE changes)https://macrocodex.appWhat the community says:https://www.reddit.com/r/tirzepatidecompound/comments/1omfgx...Yes, MacroCodex is an extension of the project above. The original domain now redirects to the same guides, which are now hosted directly on MacroCodex.We also have multiple guides and tools:https://macrocodex.app/guides/recomposition

reply

jawiggins
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Optio - an AI agent orchestration platform built on Kubernetes: 
https://github.com/jonwiggins/optio

It's built around multiple different types of agents:- Coding Agents are placed into cloned repos with a ticket (Jira/Linear/Notion/GH), and work until they open a PR, are resumed on CI failures or github feedback, and work until they can merge the PR.- Standalone Agents are reusable, parameterized agent runs with no repo checkout. Generate reports, triage alerts, audit dependencies, query a database, post to Slack, etc.- Persistent Agents are long-lived, named, message-driven agent processes. Each has a stable slug, an inbox, and a cyclic state machine. Wake on user messages, agent messages, webhooks, cron ticks, or ticket events.

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Nice, I will look into this more

reply

jantuss
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

A self hosted guestbook api that runs on my github pages site 
https://ianto-cannon.github.io/guestbook.html

reply

okcdz
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on DeskTalk(
https://www.desktalk.ai/
), an AI-native desktop environment that runs in the browser.

The idea is pretty simple: I want an OS where people can just describe the app they want, have AI build it on the spot, keep tweaking it in real time, and also use AI to operate the whole thing. Not just chat with an assistant sitting off to the side, but actually let the assistant create apps, edit them in place, manage windows, and help you get work done.So instead of installing a bunch of software up front, you can say “build me a tracker” or “make this app simpler” and the system just does it. If something feels off, you tell it what to change and it updates live.Still early, but that’s the direction I’m excited about: software that feels less fixed and more malleable.

reply

igoose1
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Way to stay connected with a family abroad.

I migrated to another country and it's hard to talk with parents, my sister and grandmas as much as I did when I was back home. We tried making weekly calls to talk and play games but someone could never make it. I got an idea to create a small chat, share a simple topic every morning and then let everyone take a picture of the object. For example, recently we had "Garden" which made my grandma in the countryside go outside and take a picture of her growing strawberries. Today is "Anything halal" and I hope this will make another (Muslim) grandma in the chat happier :-)At first, all topics were made up by me. Then, I made it possible for others to suggest topics via a simple bot. I showed this chat to friends and they got excited and wanted to try the same so I upgraded the bot to support multiple chats. Since November 2025, it's hosted 11 chats and if you're interested, you can try it too.It's free and won't be abandoned tomorrow because I personally use it.https://t.me/CreateRotiBomBot

reply

totemandtoken
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I have like 14 side projects running, but one I think might be interesting to this crowd is this: 
https://ideasthetician.substack.com/p/grasping-at-the-future...

Its not far along, but I'm trying to expand upon the ideas of Lisp into a new programming language I call Grasp. If Lisp is a list processing language, Grasp is a graph processing language

reply

JosifA
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Since last summer, I am working on a yet another Wine prefix manager, called Wine Bar [1]. My main motivation was to have a user-friendly and opensource tool that can run (some) Windows apps on my Macbook Air M2 running Linux. Before you ask, it supports regular x86_64 Linux as well.

Besides, I wasn't entirely happy with the existing Wine launchers, namely Lutris / Heroic / Bottles (none of which support Linux on Apple hardware, although I was able to run an old version of Heroic under muvm).I wanted more control. For instance, sometimes I need to install a Windows component using winetricks before an installer for some Windows app would agree to run. I also wanted even more user-friendliness. I didn't want to manually specify the executable in the installation folder to run. I wanted the executable to automatically appear on a "Desktop" in the UI as a result of running the installer for a Windows app. All of that I've achieved.Recently, I've put a very significant effort to make a Snap version of Wine Bar. An x86_64 Snap wouldn't be terribly difficult to make, but packaging an arm64 version as a Snap and making it work was really-really hard. That's because Linux on Apple hardware uses a non-4K hardware page size. So, running Windows apps in such an environment involves running a full-blown 4K-page Linux kernel inside a micro-VM. From within the VM, you register FEX-EMU as a binfmt-misc handler, and then finally you are able to run a Wine process or a wrapper around it (like Proton). Oh, in order for that to work, you also need to provide an x86_64 / x86 RootFS image for FEX-EMU. All those components need to be built as part of the Snap build process.Long story short, I succeeded and the Snap version of Wine Bar is available from the Snap Store, yet I am still waiting [2] (for over 2 weeks without any reaction) for a couple of permissions to be granted to it. That's not a showstopper though, as the permissions may be granted manually by the user.[1]:https://github.com/Tulon/WineBar[2]:https://forum.snapcraft.io/t/autoconnect-requests-for-wineba...

reply

metadata
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Safe Boundary, a database security proxy especially optimized for AI agents:

https://www.spectralcore.com/safeboundary

Launching for Postgres very soon (currently working on Supabase-optimal deployment). Continuing with Oracle, SQL Server, MySQL in the coming months.Our superpower is a very fast parser with full static analysis engine. This enables not only blocking of destructive queries but also deep SQL rewrite for PII masking in real-time. It also means better syntax error messages which allow AI agents to adjust their SQL queries automatically.Full workflow (parsing + static analysis + SQL rewriting + logging) takes less than 1ms.

reply

granthamctaylor
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been quietly working for the last three years: a novel hierarchical and extensible modeling framework that can cleanly and efficiently embed any json-like object for any predictive modeling task with zero feature engineering.

json2vec enables users to, for example, build tabular / transactional foundation models like TabBERT / PRAGMA dynamically... by just declaring their data schema. This is a space in which Netflix, Stripe, Revolut, Capital One, Nubank, J.P. Morgan, NVIDIA, etc. have been developing for several years.json2vec goes a step further from just tabular data or structured transactional data. It enables arbitrary structured "json-like" observations with hierarchical BERT-like transformer encoder blocks. Financial transactions, chess positions, flight itineraries, raw tabular data, rideshare activity, ecommerce, behavioral sequence models... Any raw data able to be represented in `json` can be encoded into a tree of embeddings, and used for downstream finetuning for supervised machine learning... No feature engineering required.https://github.com/granthamtaylor/json2vecjson2vec supports extensible plugin support for new data types (numbers, categories, raw text, datetimes, hashable objects [think: IP addresses and phone numbers], and raw embeddings), all of which may be pretrained via MLM-like self-supervised learning. If your needs are not met with the built-in datatypes, the framework is extensible in that you may build your own custom datatypes (think: geographical coordinates). Built in decision heads for a subset of datatypes enable predictive modeling multi-task and multi-array outputs (predicting fraud at a per-transaction level, or a per-account level).json2vec also enables built in data pipelines for 100b+ training observations streaming from cloud storage. These pipelines integrate with layer of programmatic data querying and UDFs can consume the vast majority of upstream data processing so that developers don't waste time on massive batch data preprocessing jobs before model training.Oh, and the best part: the model architectures instantiated by json2vec are mutable. Model developers can add and remove features and targets at their whim - allowing for truly reusable foundation models that can adapt for each individual use case.My hope is that with a standardized hierarchical modeling framework, interested organizations can better collaborate with one by sharing reusable logic with one another instead of hardcoding use-case-specific architecture.

reply

seyz
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I build a governed infrastructure for internal tools and AI agents: 
https://rootcx.com

Everybody uses Claude Code or AI coding tools to build internal software, but they lack the governed infrastructure layer required for enterprise trust. RootCX provides that missing foundation. We offer the security, auditability, hosting and permissioning primitives necessary to move internal software from "cool demo" to prod

reply

debpalash
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Building an open-source ElevenLabs-like AI voice platform called OmniVoice Studio.

It supports voice cloning, dubbing, transcription, and local/self-hosted workflows with Docker + desktop UI support.Using open-source models like Whisper, Qwen, OmniVoice and more.https://github.com/debpalash/OmniVoice-StudioThanks for checking it out

reply

BigG21
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Anydrop.org A zero-friction, cross-platform alternative to AirDrop. If your device have a browser, you can drop text or files to it. Doesn't matter if the device is a pc, mac, linux, phones, tablet or smart tv. 
There are no installation or login, just load 
https://anydrop.org
 on the devices needed. Also support live realtime notepad sync and clipboard for easy share of text snippets. All shares are end to end encrypted.

reply

azriel91
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a GraphViz replacement (again):

Site:https://azriel.im/dispositionRepo:https://github.com/azriel91/dispositionIt's written in Rust, has stable node positions, is stylable (and has default styling, dark mode styles), among other things.The hardest part is calculating coordinates for edges:- ranking nodes / positioning them when edges connect nodes of different nesting levels- ensure edges don't overlap with nodes to not obscure content- ensure edges don't overlap with each otherIt's about 60% of what my version of "complete" looks like. Remaining parts:- edge labels (might need a rewrite of how edge paths are calculated.- images in nodes- generating diagrams for different screen sizes- LSP support (?)

reply

anilgulecha
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

> (again)

I can completely empathize - sometimes some problems never leave us.. like that piece of food stuck b/w teeth. There's a force within us asking us to right that problem in the world.All the best to your project.

reply

And1
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I've started watching soccer more seriously in prep for the world cup (I'm in Canada) and watching live games is never going to happen, so I only watch replays.

There's so many games played per week, I want to find the best/most exciting games to watch, without spoilers. I built a little model to classify games and give me control over the level of spoilers shown so I can watch the best games of the week.https://nospoilersclub.com

reply

samlaycock
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

A few OSS projects:

- NookJS: a Javascript/Typescript interpreter and sandbox written in Typescript (https://nookjs.dev)- Litz: a thin React meta framework that uses RSC as purely a server transport, allowing for more flexible client/server architectures (https://litzjs.dev)- Nativite: a Vite plugin for building for native platforms using web technologies, with a custom plugin/platform support (https://github.com/samlaycock/nativite)- superformdata: superjson but for FormData/URLSearchParams (https://github.com/samlaycock/superformdata)- NoSQL ODM: ODM for various noSQL (and “unstructured” SQL) data stores, supporting both lazy and active data migration strategies (https://github.com/samlaycock/nosql-odm)

reply

justhw
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on 
https://thumbnail.ai/
 full time for a year now. It lets you make thumbnails for your social media and youtube videos with preset templates. Going great so far. I'm looking for a marketer/content creator to grow it.

reply

taegee
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

I'm sorry, but this is precisely the reason I'm using DeArrow.

https://dearrow.ajay.app/

reply

Jdstanhope
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on analyticmind.io to help small teams with the decision making process. I feel like I've lived through a few too many decisions that didn't make sense to me or the rest of the organization.

reply

solfox
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

[BestInterest](
https://bestinterest.app
) helps coparents find peace by automatically filtering out anything that isn't child-focused from their coparent's messages. Ensures court order compliance and reduces conflict.

reply

kaipereira
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on 2 hardware projects right now!

Fold-up, scissor lift, cross-cantilever 3D printer for open sauceM.2 FPGA hardware accelerator devboardAll just for fun and open sourcehttps://github.com/kaipereira:D

reply

codebje
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

Both of those are cool projects!

reply

krogenx
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I am in the process of launching my poultry RFID tags, “eFlock Smart Poultry Tags”. They allow farmers to count and identify all of the birds that they have. The project goes along with a mobile app, Manger, a tool that can be used to gather data about livestock (not just poultry). Tags should be available sometime this week, perhaps early next week on Amazon. Here’s a video of scanning:

https://youtu.be/wilixJiyPYA

Tags on Amazon:

https://www.amazon.com/dp/B0GWTB1DR9

Manger app:

https://www.manger.app/

reply

jeanlucas
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

You lost the opportunity to call it io-chicken

reply

efromvt
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

For my streamlined, composable SQL variant - Trilogy[1] - spent the last month or two very focused on CLI/ETL/scheduling to support data pipelines for other hobby projects. Have that story in a better place - so time for new things.

Trilogy's model works quite well for agents, but I've avoided making AI featurestoonative in the UI products - not everyone's cup of tea - so this month going to do a spike on a new pure AI native data authoring/exploration experience to see where that can go without messing with the core product, at both CLI/UI layers. Data consumption is (un?)fortunately a pretty perfect fit for the agent strengths with the right harness.[1]https://trilogydata.dev/

reply

yuegui
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building pagebowl: 

https://www.pagebowl.com/

A lightweight service for instantly hosting HTML, Markdown, and ZIP-based static pages. The goal is to make sharing simple: upload a file, get a live link, and let it expire automatically. The use case I am targeting at is: to allow users to share AI generated files easier and have a place to render and host them for a short period of time.One thing I’ve been learning is how much faster it feels to build on cloudflare page, worker, and D1 compared to my old way of setting everything up myself with docker, postgres, nginx and etc on hetzner for a small project. (I am not affiliated with any company, product, or organization mentioned above.)

reply

hfosidkc77
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

A 2factor verification system for server unlocking. I was unsatisfied with available remote unlock systems for homelab hardware and so built this: 
https://codeberg.org/dsjkrewpid/android-server-unlock

Its very rough, but it uses clevis and a custom tang server to unlock servers with a tap on your phone instead of a password or traditional tang network unlock. I like it because it means that even if someone steals your hardware they can't unlock it without you approving the unlock. Eager for feedback

reply

jgord
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Fitting lines to 'xray' scans of buildings - turning pixels into vector art.

Lets say you have a complex industrial plant, or datacenter you want to upgrade.You scan it with lidar and get a pointcloud and 360 panorama images.
This gives you a large dataset, but what you really want is a floorplan, a lite CAD plan showing the racks, cable trays etc.You take the scan, slice the pointcloud and make an ortho image .. it really looks like an xray of a building from the top down.Then someone has to manually trace that in CAD to make a useful 3D model they can use for designing the upgrade.So Im automating the boring manual part - turning the xray plan pixels into vector polylines, using machine learning.One of our clients scanned their datacenter, and we generated a floorplan that shows all the rack box positions, cable trays, pipes etc.Other examples : drawing the weld lines of patches in steel storage tanks, drawing in all the steel girder beams in a scan of an old railway bridge, or the windows, doors, ceiling pipes of a commercial realestate refurb.gord at quato.xyzAs part of this work, were looking at running our custom machine learning kernel on multi-core x86 CPUs.

reply

haritha-j
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Interesting, so you process the point cloud purely in 2D slices? do things like vertical piping cause any issues? or is 2D enough? I'm just finishing up a PhD in modelling industrial spaces from point clouds so I find this space fascinating.

reply

debarshri
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I am writing kubernetes compatible single binary service for various runtimes in rust [1].

Currently supports docker, containerd, wasm runtimes. I am adding support for jvm and kvm, etc. Works as is in macos. There is mock runtime too to mock it for various testing various distributed services etc.It is a fun little experimental project.[1]https://github.com/debarshibasak/superkube

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Have you seen rusternetes?

https://github.com/calfonso/rusternetesI picked Rust as my language before the AI hype in popularity so I'm biased on k8s tooling in my focus language.Cool project!

reply

debarshri
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is interesting. I am trying to k3s equivalent essentially. Not a full implementation.

reply

cperciva
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

FreeBSD 15.1. Released BETA2 on Friday, next Friday is BETA3 and the following week is scheduled to be a Release Candidate.

reply

UansaS
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Mathabito (
https://mathabito.com/
) - a suprisingly challenging addition and subtraction game. I'm currently testing multiplayer with peerJS, to figure out the best gamelogic. Right now it's a fully functioning single player experience with daily challenge.

reply

meandave
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Diagnostic tool for all vehicles.

Describe your symptoms in as much detail as detail as you like and get a full diagnostic report with parts links, tutorials, price estimates, guides for diyIncludes car sales tool, generates all the documents you need for the dmv in your county/stateiPhone all connects to Bluetooth obd2 sensors for check engine lights and live driving dataSetup search alerts for “dream cars”This one has been a blast to buildhttps://crewchief.cchttps://apps.apple.com/us/app/crewchief-auto/id6760673109

reply

traekfuglene
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Striga (
https://www.striga.ai/
) - Source code auditing built on artificial intelligence. Auditing source code with local LLMs, ensuring full data sovereignty. The latest noteworthy discovery - Double Free and possible RCE vulnerability in Apache HTTP Server with the HTTP/2 (CVE-2026-23918)

reply

ecto
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://vcad.io
, a free CAD application with an open source kernel (Rust/WASM)!

reply

aleda145
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Still working on my SQL canvas: 
https://kavla.dev/

I started with this last summer. Usually I get tired of an idea, but this one is just an endless pit of things to try out.Currently seeing how we can get an analytics agent working on the canvas. Video here:https://x.com/i/status/2053410747137266070

reply

Puchaczov
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

interesting idea!

reply

reeeeee
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Prompty.tools (
http://prompty.tools
), a prompt engineering and management platform where users can search, store and combine building blocks for creating structured AI prompts.

I created the platform because I found myself rewriting the same parts of my prompts (or storing them in a text-file) all the time. Now, with a few simple clicks I can populate all the task-specific fluff (personas, constraints, tones, ...) around the actual task that I want the AI to complete.The platform is open by default; with the purpose of letting users learn from prompts and building blocks that other users created and use. I don't have any users yet, because I want to complete the MCP and Claude Code Plugin before I start marketing my product.Other things on the roadmap:- Teams tier, where teams can privately share prompts and building blocks between them. Currently, your data is either private or public, no targeted sharing.- LLM integration into the prompt builder to reduce prompt engineering friction even more. Instead of manually searching for, and selecting the building blocks you want to use, you would just start typing your task and let the platform decide what building blocks would best support your prompt. There is still a difference with letting an LLMcompletelygenerate the prompt, as we would be using existing building blocks that have real feedback from previous uses.Let me know what you think!

reply

davidpolberger
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on turning our statically-typed formula engine -- that we use for Calcapp, our app builder -- into a real hosted solution (as well as a library). I discussed it in July last year (
https://news.ycombinator.com/item?id=44702833#44704642
) and have been working full-time on the project since the beginning of the year.

I figured "I already have a battle-tested solution, I just need to make it modern and spiffy, build a website for it and see if there's any interest -- in the age of Claude Code, this should be fast work!"Wrong. Taking an internal library and offering it to others -- complete with documentation and modern tooling -- is an immense project, even with the help of AI agents.Is there a market for a "formula engine in a box"? I don't know. But I also didn't know whether there would be a market for Calcapp either, and that has supported me working full-time for the past seven years. So I'm willing to take another chance.

reply

DSemba
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://briefin.com/
, which turns any topic into a newsletter.

I wanted to replace those passive social media feeds, where I'm just being served what gets clicks. I completely avoided any embeddings or typical rankings, using ai agents instead, to get precise results and things that are actually interesting to me.Still working on the platform, but I made a tool that already turns Hacker News into a personalized daily digest herehttps://briefin.com/hackernews/(with summaries of the discussions)Let me know what you think :)

reply

obaid
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a few things:

Rundash (rundash.ai) - an easy way to create automated AI agents that can run tasks for you with over 1000+ integrations. Built this from my own needs to run better meetings, discover product insights etc..Provision (provision.ai) - how I run a team of openclaw agents without burning money on Mac minis. Each agent is given a dedicated email inbox (powered by Mailboxkit) and a dedicated chrome browser that you can connect via browser to unblock if needed. Currently doing some pilots with a few startups. It's interesting to learn how teams want to use AI agents like OpenClaw.[unnamed project] - a macOS menu-bar AI agent that drives your real apps similar to Perplexity Computer. Hit ⌘⌘, type a task (optionally @-mentioning apps like @slack), and an agent Claude Code or Codex; clicks, types, scrolls, switches apps, and reads the screen via accessibility APIs, with a visible cursor so you can watch it work. Everything runs locally on your own logged-in Mac (BYOK to Anthropic/OpenAI), so there’s no cloud VM or re-auth flow. It also snapshots the frontmost app for ambient context ("summarize this page" just works) and supports parallel tasks with persistent history/workspaces. Pre-release, but the core bet is that desktop agents should feel like a teammate living in your menu bar, not a browser tab or rented remote computer.

reply

elar_verole
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Started some playtests for our game with my brother (I mean we don't REALLY have testers yet, we need a bit more work first because right now it's lacking 1 or 2 core elements of the fun / gameplay loop):

https://srdnvntrz.itch.io/runz

also created and got our steam page validated:https://store.steampowered.com/app/4704420/runz/We've been moving fast, it's our second project and we hope to deliver something people find fun and appealing, at least for our friends !We suck at marketing though (such is the game dev burden), but we're having fun and learning stuff, which is what it's all about I guess.

reply

rambleraptor
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on an OSS backend-in-a-box called [aepbase](
https://aepbase.io/
).

For the past few years, a group of us from Google, Microsoft, GM, IBM, Roblox, Rubrik + more have been working on a design standard for APIs called [AEP](https://www.aep.dev). The goal is twofold: learn from our companies mistakes around APIs and enable better tooling with less configuration.We’re at a point where AEP-compliant APIs get a resource-oriented CLI, MCP server, full UI, and Terraform provider for near-zero configuration.Aepbase has been my way to tie the whole ecosystem together. You run a single binary and define the schema for a resource with one API call. Now, you’ve got a full set of CRUD APIs and support for CLI/TF/MCP/UI. After one API call.It’s a really cool way to tie together all of the work AEP has been doing.Love to hear HN’s opinions on all of this. We’re still trying to figure out the best way to sell people on AEP.

reply

frostbyrne
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Greetings!

I've been working on something in the vein of a indie game for a little over a year now. It has been a passion project, but I'm starting to come around on showing it to people.I am a big fan of Telltale style narrative games. I think Baldur's Gate 3 was the biggest revelation of this for me. Taking that branching dialogue and freedom of choice, and tacking it on to a fun combat system was just everything.When text based GTRPGs started popping up, I found it hard to connect with them stylistically. I found that I needed the multimodal stimulus of visuals and audio. This led me to start building something, and it ended up being somewhat of a cross between a Telltale game, a Visual novel, and a TTRPG.Orpheus (https://orpheus.gg) is a fully on-the-fly generated tabletop simulator, with graphics, audio (TTS), and the freedom you can usually only find at a real TTRPG table. That means you can play a sci-fi, fantasy, or even a modern setting in your campaign. The assets are made for you as needed. It runs in your browser so nothing to install or tinker with.Getting the harness right so the AI GM can stay coherent and organized has been the biggest challenge. It took a lot of iterations to get it to a point where it could understand the scenes it was building as the player changed them.I've built it to be played with either a keyboard or a gamepad so you can play from your couch. You can switch between them as you feel like it. There is a 3D tabletop for combat, full character sheets, dice rolling, lore tracking. I want it to be dense.Mostly, I’m looking for people who want to try it, break it, and tell me what feels magical, confusing, boring, or broken. My biggest roadblock currently is that asset generation is relatively expensive. I'm currently mulling over whether a playtest would allow for a BYOK setup so people could try playing as much as they'd like, or if I should add turn limits.You can join the playtest waitlist athttps://orpheus.gg/-- and I just setup a discord (https://discord.gg/pychWyzf) that I will use for early playtests. (Just me right now! Come hang out!)

reply

vunderba
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

I've been the DM of a weekly campaign with the same group of friends for nearly a decade now. Over the past few years, I’ve seen a lot of attempts at AI meets D&D, and most of them suffer from fairly pedestrian puzzles and stories, and don’t really compare to what a decent, semi-competent human writer can come up with.

I'd love to see a more modern day attempt at something like Bioware's Neverwinter Nights - which was designed so that someone could create a campaign, and then the game would provide the behavior, pathfinding, assets, and everything else with a virtual (or human) DM behind the scenes. You could still tell a human-driven story, but the engine would do a lot of the heavy lifting.

reply

frostbyrne
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I agree, there is no way to perfectly capture a real table with your friends. This is more an alternative for when life gets in the way of meeting every week.

I think a lot of those attempts you mentioned try and brute force the problem or trust the AI too much on what to generate.A lot of the same problems that AI coding agents run into also apply to this problem. You have to really manage context (avoid sending a novel at the model) and enforce strict rules in the "engine". The hard part is world building that is consistent without railroading the player and forcing specific paths. I have an agent (for lack of a better term) that manages arcs across each tier. World arcs (nations, factions), player character arcs, NPC arcs, individual scene arcs, and location arcs (towns, cities, dungeons, etc). By prompting all of these as tight, individual arcs with flavor and context peppered in as needed, you end up with stuff that is more compelling. It has to be loose enough that you don't railroad the player. When you decline that NPC's quest, down the road that might have changed the overall arc for a town in a meaningful way.I won't pretend that I've perfected anything but I have definitely noticed a spark in its writing and world building that I personally have really enjoyed.

reply

vunderba
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah I'd agree that I think AI can at least work provided you manage the context properly, multiple top-level files establishing consistent world state, all that jazz. KoboldAI and SillyTavern both do a pretty good job of maintaining internal consistency around longform interactive fiction.

OTOH, that means that the underlying story is that much more important. I think a lot of people mistakecoherencefornovelty. Biggest offender is puzzles - oh god do LLMs absolutely blow dire wolf chunks at coming up with organic and interesting puzzles.

reply

blinkbat
 
1 day ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why not generate some asset libraries to help with some of the rote generation? You could theoretically serve the same asset for a pack of rats to multiple campaigns.

reply

frostbyrne
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes! I am doing a lot of this where it won't break the illusion. Not everyone needs a unique innkeeper generated in every town, but I want to avoid that "Officer Jenny" effect like in Pokemon where she looks the same in every town they visit.

I have a private vs public flag for assets that I'm considering more unique or sensitive, at the AI GM's discretion. I'm using embeddings from there to try and parse if an asset already exists in the public pool or not, and reuse it if possible. The thinking is that eventually I will have pretty decent asset coverage on most standard campaigns. I can't account for people going way off book though.I have an asset pipeline that tries to determine player intent and pre-generate assets before they're needed. That way we can attempt to hide the "load screens" like retro games did with elevators. I have a kind of sliding scale for player coherency, and if the player has too many "misses" on the pre-generation pipeline it will increase its requirements for when it starts generating.I may have wildly over-engineered this but I love it. =)

reply

iugtmkbdfil834
 
1 day ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Super cool project and I love to encourage this as I personally think llms in games have not been utilized to their potential quite yet.

reply

winrid
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Still building 
https://FastComments.com
 :) I'm planning on launching a desktop app for it soon with a combined forum. So you could have a community on something like discord, but all the chats are indexed and searchable through a web forum style interface as well. The desktop app is a native C++ app so no electron :)

I'm also working on launchinghttps://watch.ly(network/fs sandbox with human in the loop for ai agents), mostly waiting for the entitlements from apple at this point...oh and I launchedhttps://dirtforever.netrecently to keep Clubs going for Dirt Rally 2 without the EA servers. Learned about the egonet protocol and made a server.

reply

letharion
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a GNSS/RTK-based lawnmower.

The existing ones were quite expensive, especially when I started out. A friend had the idea to get a cheap/non-functioning lawnmower second hand, and tear out the circuit board. We're in the process of coding up a new ROS2 based stack that will roam the lawn on GPS with RTK in the charging station. My friend does most of the electronics stuff, and I focus on the software.I'm at the point where I will start testing a simple bounding box soon and just have it drive around until it "hits the edge" and then randomly pick a new direction.It's fun so see the software I build "in real life" instead of as a web-site, as is the case for my my daily job.

reply

Jemm
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Would love to see your progress as I am very early on in the same project. I was thinking of using ArduPilot and some custom waypoint generators.

reply

letharion
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Feel free drop me an e-mail on [nick] @ [the big G].com and we can discuss. :) Haven't seen ArduPilot before. Since I'm using ROS already, on of my goals is to lean as much as I can on that and avoid custom work where I can. Nav2 appears to be the most common "go from point A to B" framework in ROS-space.

reply

AISnakeOil
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a daily word puzzle game called Hinted. Wordle for people with half a brain. Streaks that are forgiving and a way to track your friend's progress.

https://hintedgame.com

reply

jsattler
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm currently working on BetterCapture (
https://github.com/jsattler/BetterCapture
), which is a lightweight (~4MB size and low memory/cpu footprint) screen recorder for macOS that lives in your menu bar. It supports ProRes 422/4444, HEVC, and H.264 — including alpha channel and HDR. Frame rates from 24 to 120fps. System audio and mic simultaneously. You can also exclude specific things from recordings, like the menu bar, dock, or wallpaper.

No tracking, no analytics, no cloud uploads, no account. MIT licensed. Everything stays on your Mac.I'm currently planning and designing a plugin system, so others can contribute new functionality without affecting the scope of BetterCapture itself - which should stay as small as possible.

reply

holoflash
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Continuing to chisel away at my browser-based tracker/DAW 
https://psikat.com/

reply

grahammccain
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Chartlibrary.io - an intelligence layer for AI agents rooted in chart pattern search. Return 500 similar stock charts to the one you a looking at. Give those distributions stats to an agent, disect into buckets by variables. I think it’s a new way to interact with stocks for the agentic world.

reply

msyea
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm currently fighting Garmin's 
wonderful
 Connect IQ watch app platform (it's horrendous).

I'm working on <https://untether.watch>. Trying to shift 20-30 micro phone interactions to the wrist per day to ultimately reduce phone use. Dumbphones are too extreme - you need a smartphone for certain day-to-day activities (banking etc.)The watch is a great form factor - it's got a crap screen (MIP), the ergonomics are awkward (rotate and look down), it has limited capabilities. But that's the point! Do essential quick actions and leave the phone out of site.Requires Android companion app to do the heavy lifting. Use the (head)phone mic and STT to reply to any android notification and make notes. More features to come.Garmin's SDK is seriously challenging. APIs are often broken across firmwares, limited developer tools and testing is tough.

reply

meetingthrower
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

I agree it sucks! I thought about vibecoding my own app just to reliably get my data out.

reply

matthiaswh
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You might take a look at 
https://github.com/tcgoetz/GarminDB

reply

GalahiSimtam
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I go on with my small side-business of modding Skyrim. During lockdown it wasn't clear what Bethesda games the paid mods store will cover; had it been only for new titles, I had only vague idea that Starfield would be some space sci-fi game, so my idea was to make puzzle-adventures using the base game assets (and blending in the world game is nice but optional), and puzzle-adventure is a very broad genre in itself, so maybe I would end up making up distinct unique gameplay for each of the modded games.

Recently I came up with an idea for a puzzle-adventure under Playstation mod limitations. That means no new assets, and no new scripts either. Simply, let's treat it as a different game, and see what can be done with that. I researched the built-in scripts, and oddly, every script that could be used to enable a game object was not repeatable. Ditto for scripts to disable an object. The only repeatable scripts were toggle scripts (disable an object if it is enabled, enable if it is disabled). So last week I prototyped some puzzles using that primitive only, and while doing so, I figured out how to trick the engine into making those do-once scripts repeatable, too...

reply

BrunoBernardino
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

My wife and I continue to work on Uruky, a simpler and cheaper Kagi alternative, based in the EU [1].

Since last month we’ve stabilized the search UI/UX and have 5 search providers you can choose from and sort as you prefer.We entered May with over 50 paying customers and have recently launched Uruky Site Search [2] (for website owners, this effectively is our own search index and crawler, which we’ll be bringing into Uruky soon as another search provider option)!Customers really enjoy the simple UI (search doesn’t require JavaScript) and search personalization (from choosing the providers to the domain boosting and exclusion). We also have hashbangs (like "!g", "!d", or “!e”) when something doesn’t quite give you what you’d expect, though.You can see the main differences between Kagi, DuckDuckGo, Ecosia, etc. and Uruky in the footer (right side), but one huge difference is that with Uruky, after being a paying customer for 12 months, you get a copy of the source code!Our main challenge right now is outreach because we want to do it ethically, and it’s hard to find communities or places to sponsor which are privacy-focused and don’t require €5k+ deals. Ideas are welcome! We’ve been sponsoring a project per month (Qubes OS, The Tor Project, and Hister so far), with our limited budget of ~$100 / month.Because of bots and abuse there isn’t a free trial easily available, but if you’re a human and you’d like to try it for a week for free, reach out with your account number and we’ll set that up!Thanks.[1]https://uruky.com[2]https://uruky.com/site-search

reply

BrunoBernardino
 
52 minutes ago
 
 | 
parent
 | 
next
 
[–]

So, we actually just shipped the option to include Uruky Site Search (our own index) in the search results, alongside the search providers! Up next is beta image search, which is highly requested.

reply

calculated
 
1 day ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hey, I'm from the EU and love to see such a project!

One thing I can recommend right off the bat is Reddit - there's many privacy focused subreddits, and also you can share the whole project in EU related subreddits and e.g. r/SideProject.Would love to try it for a week, this is my account number - 9772263817629091Keep up the great work!

reply

BrunoBernardino
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks for the suggestion! We're trying to avoid anything that's social media (though Reddit is debatable), at least for now.

I've topped up that account number for a week, enjoy (I'd recommend removing it from the post because anyone will be able to use it)!

reply

ssorallen
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

* Tab Wrangler GitHub Project: 
https://github.com/tabwrangler/tabwrangler

* Tab Wrangler for Chrome:https://chromewebstore.google.com/detail/tab-wrangler/egnjhc...Continuing to work on Tab Wrangler, an extension for both Chrome and Firefox that has been available and open source for 10+ years. It auto-closes tabs when they have not been active for a configurable amount of time, similar to the feature built into Mobile Safari but more configurable.I have been maintaining it and in the past few months added features that had been requested for a long time.

reply

justkez
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A few months ago I got so fed up of squinting at glowing rectangles to stay informed/updated. I feel like there's a finite amount of podcasts I can reasonably follow/digest so I built a very basic prototype to summarise RSS feeds/transform the content and transcribe it in to a personalised podcast.

I put a bit more work in since May have it running almost end to end, still with plenty of gotchas. It's transcribing on an RTX3070 under my desk so pretty limited, but have enjoyed a few morning briefings just as I want them (weather, chance of rain today, BBC/NPR top stories from yesterday, some specific sports news then HN most popular summarised with summary of comments. Got a chuckle out of the LLM summarisation of HN commen threads which was always "Comments reaction: mixed" (which it no longer embeds!)Found traces of it being done before and I understand you can do similar in Notebook LM, but I was hoping to build something set-and-forget.

reply

coldstartops
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Stream on-demand files between your devices. WAN, LAN, Direct IPV6, cross platform, pqc.

https://keibidrop.com/repo:https://github.com/KeibiSoft/KeibiDrop

reply

nerdomancer
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Looks promising! I will try it out.

reply

coldstartops
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Let me know how it goes, or frustrations. I admit that currently it is not the most friendly UX. And found out a bug that if no direct P2P possible, it fails to fallback to the STUN-ish data relay. However LAN mode and WAN via direct P2P works on latest releases.

As soon as I merge this one, will create another release that fixes the fallback; and hopefully also get the apps in ios and gplay stores.https://github.com/KeibiSoft/KeibiDrop/pull/143

reply

pythonbase
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on halalcodecheck.com - a platform to verify food ingredients. Something that started as a tool to scan or upload product labels to verify ingredients has now transformed into a repository of brands, food types, and guides covering major accreditation bodies in the US, UK, Canada etc.

In April, the site receievd 3,500 clicks from Google - 7× growth month-on-month. Cited by ChatGPT, Claude, Gemini, and Perplexity.Working as a solo founder, some of the stuff I shipped last month:⤷ Launched a seasonal gifting vertical - new revenue surface, new content format, reusable template for future occasion launches⤷ Audited verdicts for all brands and food items, incorporating data from various authentic sources and official accreditation bodies⤷ Expanded programmatic SEO across ingredient and brand categories⤷ Turned zero-result dead-ends into a list growth lever

reply

christoph123
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A proactive AI that asks you for your daily goals and checks in if you're not working on them.

Right now working on framing this as an RL problem to better predict when nudging is actually successful and what kind of wording works best given the user data. Then applying the same logic to onboarding emails etc.https://donethat.ai

reply

robbiejs
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on SpreadsheetPreview.com, a subscription service that gives you PNG previews of your uploaded spreadsheet (xlxs files).

On the server it opens a headless browser, where it converts the XLXS format to OGF (Open Grid Format), which is then rendered by DataGrid Toolkit, the engine behind DataGridXL v4. It then takes a screenshot of this render and sends it back to the requester.Try out a few renders athttps://spreadsheetpreview.com

reply

triwats
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on trying to give some guidance on solar panels.

Plug in solar became legal here in the UKStill sussing it out but started shipping somethingFinding the pitch direction of the roof is kinda hardUses data from the house to try and get a ratinghttps://solarable.org

reply

tompccs
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on heytavi.com

I was interested in building a product for which 1. the agent is the whole product, not just a component of it; and 2. solves a specific problem out of the box.Tavi is a deep people search agent that lives in Slack. We used it to find our founding engineer and our first customers are a mix startups, recruiters and VCs.

reply

fanfank
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

SogaPaper - 
https://sogapaper.ai/

People are consuming more and more text content than ever before to get more information, under the pressure of AI development.
For me, I need to read papers, go through information related to my industry and company, sometimes my boss asks me to conduct a research on some newly launched products or techniques revealed by passages.It's really a heavy load to consume all these information fast and deep, so I built SogaPaper:https://sogapaper.aiIt can translate, summarize, q&a not only at the whole document level, but support paragraph-level quick glances and q&a, preserving the important inner logic and structure of the whole passage, very suitable for knowledge workers and college students nowadays.It's free to start, and I'm looking forward to hearing from your advices.

reply

ramon156
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

It looks really solid!

I'm also really fond of the product. If the execution is solid, I'm definitely interested in throwing some money at it

reply

fanfank
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you! If you experience some problems, feel free to contact us at support@sogapaper.ai or the discord 
https://discord.gg/gn93yUar

reply

Leftium
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

https://fx.leftium.com
 (
https://github.com/Leftium/fx
)

Old-school graphics in modern TS.Several years ago, it was not possible to blit an entire screen of random pixels to the screen at a decent frame rate without something like shaders.Even though the screen is now even higher resolution, the CPU can now blast 2560x1440 random pixels to the screen at 90 FPS. Must be advancements in hardware and/or JS runtime. (The bottleneck seems to be generating the random numbers...)I figured out how to make my TV static effect look more realistic:- Mostly: TV "pixels" had wide aspect ratios[1]- Larger "grains" (see info in corner)- Also added subtle CRT scan line effect. ('C' to toggle)- Looks different when animated (click to toggle pause; probably should emulate 60FPS).---Started revisiting this rabbit hole while thinking about programming prompts from the new Recurse Center application[2]. They suggest about six different prompts; I figured out how to combine all the prompts together.[1]:https://github.com/Leftium/fx/blob/33405b25dc7caeb48e6c563a3...[2]:https://hn.leftium.com/i/47892660

reply

boznz
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Retired so two projects; a 2D arcade board using a RP2350, and my 3rd sci-fi/techno-thriller novel: Currently approx 140,000 words into a 100,000 word novel and about 50% complete.

reply

sotix
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

My Playdate survival game, Plight of the Wizard[0], which uses the crank for aiming spells. I've had a ton of fun doing performance improvements, and now I'm implementing an upgrade system.

[0]:https://sotix.itch.io/plight-of-the-wizard/devlog/1517881/v0...

reply

ElSchorschoDE
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I like splitting firewood in my backyard, and I thought there should be a game about it. So I'm making this:

https://store.steampowered.com/app/4521770/Drunk_Woodcutter/

reply

seugur
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a cohort-based coach application. People register with a commitment and aim to do daily tasks. Meanwhile, they can communicate with an AI for any difficulties or feelings that AI keeps the cohort spirit.

But not sure people will be willing to use it. A commitment is highly generic, maybe I need to narrow as daily exercise or something.

reply

Cilvic
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

What's the url?

reply

quinito
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on World Watcher (
https://worldwatcher.live
). It's an interactive map of livecams around the world.

The idea is to have a better experience for navigating livecam streams that are publicly available on YouTube. There are a few livecam aggregators that include maps, but I never felt that any of them were satisfying, as they always require you to open new pages to watch the streams. On World Watcher, you can jump from place to place seamlessly.You can also filter the streams by type of place or features, for example beaches or cams with audio. And if you don't know where to go, just try out the Explore button.

reply

jeanlucas
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building several small tools for myself, no real intention of sharing them yet. Some have better solutions in the market:

* Advanced tab organizer, small chrome extension to organize my bad habit of 200+ tabs, can group them into windows, search, close duplicates, search just on a specific window. Pretty fun.* A clipboard manager, just wanted to build something in Swift for fun* A todo app for mac, local-only

reply

naikas82
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

First time posting my project. I am working on an LLM based graph visualization.

The App helps Product Managers, Sales Reps and Architects quickly understand an enterprise software APIs. LLM turns the raw documentation into beautiful process flows, sequence diagrams and integration requirements.Hope to launch soon ;)

reply

spaceships
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

https://validity.ai
 - A tool to help validate that generated code is complete

https://blunders.ai- Chess improvement platform

reply

spaceships
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Validity is currently free to use

If anyone wants to try blunders, I can send a coupon code along.

reply

ciju
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

https://finbodhi.com
 — It's an app for your financial journey. It helps you track, understand, benchmark and plan your finances - with double-entry accounting. You own your financial data. It’s local-first, syncs across devices, and everything’s encrypted in transit (we do have your email for subscription tracking and analytics). Supports multiple-accounts (track as a family or even as an advisor), multi-currency, a custom sheet/calculator to operate on your accounts (calculate taxes etc) and much more. Supports price for most Indian investment vehicles and US stocks.

Most recently, we added support for comparing funds with leading/trailing/rolling charts and benchmarking (create custom dashboards tracking nav and value chart of subsets of your portfolio) and US stocks, etfs etc. And family dashboard (e.g. you can see networth, cashflows, income, use sheets at family level and more). Seehttps://finbodhi.com/changelogfor details.We also write about related topics:E.g. Benchmarking your returns:https://finbodhi.com/docs/blog/benchmark-scenariosOr, understanding double entry account:https://finbodhi.com/docs/understanding-double-entry

reply

jfim
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a personal internet archive and knowledge management stack. It's in a rough state but I'm using it every day.

Cham (https://github.com/jfim/cham) is an archive for internet content, you give it an URL and it'll archive it for you, extract the text with readability if it's an article, or extract the audio track then transcribe it. Content is automatically summarized and tagged, and you can start a conversation with a LLM about the article. It supports feeds too so you can subscribe to blogs and keep the articles in case the blog goes away. I still need to add search, improve the CLI, add all the missing features, and do a lot of improvements all over the place.To improve reliability, I made passe-partout which is basically a Chrome browser with a rest API (https://github.com/jfim/passe-partout) and veilleur (https://github.com/jfim/veilleur) which turns any blog listing into a RSS feed. So this way I can take blogs that are rendered using JavaScript, don't have a RSS feed and load the articles directly into Cham.Also built a modular MCP server with OAuth2 dynamic registration so that I can have my own MCP server that works with the web, desktop, and cli versions of Claude/Claude code. Currently have modules for editing files so that I can edit/search my Obsidian vault from Claude, fetching pages through passe-partout (since some pages block LLMs from reading them), and proxying MCP servers so that servers that only support bearer token auth can still work with web Claude.Also, a gnome terminal emulator UI with some unique features like split browser/terminal tabs.https://github.com/jfim/jftermMostly an excuse to see how far I can push LLM code generation to write tons of software that I've always wanted but never had the bandwidth to tackle, and learning to deal with the sometimes questionable code quality that comes from it.

reply

arkwin
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

A paid social media platform called TerraRose.

https://terrarose.orgI was tired of algorithms running my feed, my data being sold, ads, being tracked.So I built TerraRose.Current User Count: 2.Maybe it will turn into something maybe it won't.

reply

austin-cheney
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I am working on a task manager that’s way more informative and resource efficient than the windows task manager and works on Linux. It also provides an informative dashboard for docker containers and web servers with proxy support and preference for streaming sockets supporting http and web sockets over the same ports.

reply

aleda145
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

WSL support too? Could be cool with a unified thing, not sure if that's even possible though.

reply

austin-cheney
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It’s just a node app written in TypeScript. The OS specific details come from running the right shell commands.

https://github.com/prettydiff/aphorio

reply

Achshar
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a vs code extension for antigravity that will let me designate one thread as a "controller" and it can spawn and chat with multiple other agents in ag. I have a separate extension that lets me control any chat agent in ag from a telegram bot. So that should ideally allow me to replace my human work of checking on agents. It should also allow me to pit claude against gemini and use low models for less smart tasks and costlier models for tasks that require more thinking. I have more or less defined my development workflow in stages where first I write a comprehensive wiki + empty test files with descriptions, then I write the code and then recursively fix the code to meet the test criteria set earlier. I want to automate this with the "controller" thread. I have come to realize a knowledge graph via wiki is the only way I am able to get AI to generate production ready stuff, otherwise its too flaky.

reply

joshghent
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

https://repowarden.dev
 - feel fairly feature complete now and am dogfooding heavily so it’s time to face my fears and do some “marketing” and “sales”. Whatever that means.

reply

juanre
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building 
https://aweb.ai
 (
https://github.com/awebai/aweb
)

I was tired of copying/pasting between agents, so I gave them identities, and tools to talk to each other and share tasks. I've found it so useful that I've left my job as the CTO of a German startup to focus on this.The identities are public-key DIDs with DNS as the source of truth, as well as team membership. I also run a public registry athttps://awid.ai(also OSS).

reply

rorylaitila
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been cataloging my collection of American vintage ads (
https://adretro.com
). The collection has expanded considerably in the last year. I'm working on a front end search portal for users to use, to deeply search all aspects of the collection. Built on MySQL and Lucee. Meta data is extracted with OpenAI image, stored in MySQL FTS. I'll probably add vector search after I get it live.

reply

nicbou
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I track wait times at the Berlin immigration office. I just added a graph that shows how wait times improve/worsen over time. I generate the SVG without any external dependencies. It was a fun exercise.

https://allaboutberlin.com/guides/immigration-office/wait-ti...I wish I had more time for such projects, but since AI is now capturing most of the traffic, I am losing a lot of my income and I have to make up for it. It's a huge distraction.

reply

jansan
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

You will probably have to use the BigInt data type to track those wait times.

reply

oersted
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on Vicena.ai, an agent to make scientists more productive, and make non-scientists into scientists.

- Integrated with lots of open-source and commercial simulators and models for chemistry, materials science, biology… As well as connections to service labs and robot labs to easily perform physical experiments.- autoresearch / AlphaEvolve like optimization loop following the scientific method: observation, hypothesis, experiment, theory. Combined with a long-term self-learning memory like Karpathy’s Wiki.You can work with it interactively like with a coding agent to research and execute experiments efficiently. You can also treat it like a graduate student, giving it long-term research goals, having it work 24/7, making smart decisions about where to use your limited resource budget, checking-in with it periodically as a supervisor to guide its direction.Not all of this is shipped yet, but we’ve been online for a while and it should be plenty useful to any scientist/engineer already.

reply

mannanj
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

What do you define as Science?

reply

rmorlok
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on my open source integration-platform-as-a-service (iPaaS) auth proxy. It provides an embeddable integration marketplace where users can connect 3rd party apps, and it provides a proxy endpoint to the host application to send authenticated outbound requests. That way token refresh, audit, etc stay with this system and frees the host application/agent/whatever free to just focus on the business logic.

https://github.com/rmorlok/authproxy

reply

messh
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Instant linux boxes via ssh that suspend on disconnect. Checkout 
https://shellbox.dev

The idea is to have "real" linux, exposing ipv6, supporting nested virtualization, docker, etc.

reply

DeveloperOne
 
22 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool, I really like it!

reply

windowshopping
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I built The Daily Baffle over at 
https://dailybaffle.com
 with a whole bunch of word and logic puzzles I designed.

There's Truthsorting, a logic puzzle where you have to order logical statements to make them true or false.Pathword, a puzzle where you lay out letters along a path to spell out 4 words.Morphology, a clued word ladder written by a different contribution daily.And a few others!I've been trying to promote it for a few months but I haven't had a ton of luck, to be honest. The audience hovers around 500 people and growing it beyond that has been pretty challenging.

reply

jessecoleman
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Checked out your puzzles! Very cool. I'm also building a collection of daily puzzles (
https://gramjam.app
). Would be interested in chatting about your experience with marketing and outreach!

reply

AznHisoka
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I am hacking on an alternative to Builtwith: bloomberry.com. Unlike Builtwith, you can search for companies that use any backend/backoffice product such as Jira/Atlassian, and Github (enterprise/free).

reply

osetinsky
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on Underscore: a web SDK and browser sandbox for making procedural music systems with LLMs.

The basic idea is "music with source code." Instead of prompting for finished audio files, you use an LLM to help write and revise a SuperCollider-based system that runs in the browser via WebAssembly [1]. The result is executable music: inspectable, editable, versionable, and controllable at runtime.I’m especially interested in adaptive sound for software: games, creative tools, meditation apps, AI agents, interactive art. Places where a static audio file feels too dead, but hiring a composer/sound designer for every variation is unrealistic.It’s early, but the thesis is that LLMs make algorithmic music much more approachable because code becomes a conversational medium. I wrote a longer piece about the idea here:https://x.com/osetinsky/status/2053674503801028944?s=20You can check it out here:https://underscore.audio[1] shout outs to:- Sam Aaron for building SuperSonic, allowing for SuperCollider in the browser as an AudioWorklet:https://sonic-pi.net/supersonic/demo.html. Earlier, pre-LLM versions of Underscore relied on low-latency WebRTC implementations for streaming SC synths running on servers to browsers in real-time- James McCartney, creator of SuperCollider:https://supercollider.github.io/

reply

8note
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

my embroidering is going fairly well now, but i need to be able to figure out what floss to buy.

the general idea is to take pictures of birds and mountains, and use a bunch of colour-theory-from-minecraftto first meanshift a bunch of the image to come up with a lower colour resolution image, then to match that to dmc threadsbut then i also want to use tools like the axiom mod to fill in gradients, and to do hue shift/temperature changes to represent shadows, like how bdouble0100 uses purples as a shaded green, rather than a darker green.ive also been using it to see how the claude code for web setup works, and it feels real poor compared to the cli.the main problem i think i need to pull to local and do my own code for is the colour sampling from the oklab space. when i try to create gradients from colours already in the list, i ve got a visualization of the line its aiming to follow, but its picking the next colour and placing it out of order vs projecting to the line.likely my biggest issue is that claude and the like are still bad at thinking in more than 2 dimensions, but i think my vocabulary is also subpar for giving the feedback either in clear linear algebra or colour theory terms.next idea is for when thats done is to make a mod that turns a survival game into a roguelike - in the style of the hades 2 challenge runs, so i can play a session of the game in a certain biome without having to do all the grind first to get there on a new character.

reply

skittleson
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Mqtt broker on esp32 for long term deployments 
https://github.com/skittleson/mqtt_broker_esp

reply

almog
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

Link to repo is broken

reply

aCaB-ctx
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

https://clens.io
 - A data processing platform for threat detection / analysis / intel

Feel free to try it out![ yes it's written in rust :D ]

reply

aslushnikov
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://flakiness.io
: GitHub-native test analytics. I worked on Playwright before, and this project started as a natural continuation of that work. We’ve since expanded beyond Playwright to support many popular test runners.

The idea is to connect test results and artifacts with commit history. Test reports should know whether a failure is new, whether a test has been flaky before, and which commit made a test start running 5x slower.If you maintain an open-source GitHub project with tests, please give it a try. The free plan is a good fit for OSS projects: 1GB of storage is enough for roughly 10M+ test results.

reply

xvok
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

CoPilot for Project Management, trying to automate a lot of the tedium either PMs or unwilling, but forced EMs do to manage their work across tools: status updates, task updates, project docs, etc.

https://quickapproveai.com

reply

jpsimons
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I got my app in the Mac App Store! It's a layer based image editor, which as a developer has been a nerd's paradise to develop. How should disparate blend modes work with "merge down"? What does it mean to have one color channel selected when you move a layer? Should type layers use their Oriented Bounding Box or their Axis Aligned Bound Box with free transform? So much ambiguity to resolve and I'm loving it.

https://apps.apple.com/us/app/mojave-paint/id6759276677?mt=1...

reply

RichardChu
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an AI-native email client that organizes, prioritizes, and drafts emails for you.

The vision is for everyone to have an executive assistant that manages their email. It's built for people who spend hours in their inbox every week.It has automatic prioritization, split inboxes, snippets, bundles, automatic follow-up reminders, and an AI agent that can do stuff for you -- without deleting your emails.If you've read this far, I'd encourage you to give it a try and let me know what you think!https://fluxmail.ai

reply

nateb2022
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

You'd probably want to get SOC 2 certified at some point, to not turn away a decent amount of potential users.

reply

morisil
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

How do you handle possible prompt injection in emails?

reply

westoncb
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building this "general problem solver" (will likely focus on math problems first) that uses a special kind of orchestrator to direct/structure the problem solving approach in accordance with how many 'rounds' remain and other aspects of problem context. It does this largely by influencing the behavior of specialists.

Just posted a first early demo and sample orchestrator system prompt yesterday:https://x.com/Westoncb/status/2053429329233895857You initialize the system with an objective and a number of rounds to run for, and it loads the current config (orchestrator + specialist prompts and LLM configs) and begins working on it. You can manually step one round at a time or just let it run.Rather than accumulating a single long work log/context, at each round specialists apply patches to a number of named 'artifacts' with different roles (e.g. uncertainties, dead ends, findings), which are injected into prompts during subsequent rounds.The engine is written in rust and there's a web UI (and CLI). You can use the built in config editor to define specialists (and their prompts), what the artifact set is, orchestrator prompting etc.

reply

chaoxu
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m really interested in AI4MATH, as I believe it will eventually replace me.

I'm working on a mathematical knowledge base software.It's kinda like a local Github for math. In fact the backend is actually a Forgejo instance, I'm building a frontend for human and also a harness for agents that automatically consumes the knowledge base and expand on it. I realized the Issue/PR/review workflow works well for maintaining knowledge base too.The motivation is actually help mathematicians/me TODAY to able to do math together with human/AI.The knowledge base keeps mathematical writing as plain Markdown, but adds stable IDs, backlinks, search, draft changes, review, approvals, and merge.
The agent side can read the same pages, follow the same references, propose edits, and go through the same review process as a human.I’m not using formalization here. Everything is still natural-language proofs. The practical reason is that many areas I care about are not easy to formalize yet because it is not in mathlib.I see this as a transition project: useful before autoformalization really works well, and maybe still useful afterward as the place where humans and agents organize exploration.

reply

tagawa
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Ménière Memo, a web app for logging and reviewing Ménière's Disease episodes:

https://menierememo.com/Intended for an audience of one so still a bit rough around the edges, but the intended audience said “excellent” and is actually using it.Mostly AI-built. Source code is here:https://github.com/tagawa/Meniere-Memo/tree/gh-pages

reply

allenu
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on an update to my flashcards app for over a year and half now and I'm finally nearing completion. This is for Mac and iOS only and the app uses Core Data with CloudKit for syncing its data, which has been interesting learning the ins and outs of. (For instance, CloudKit can throttle your sync if you have too many objects, so I ended up having to create snapshot objects to carry lots of records in bulk which I then expand in a local SQLite database to get around its limitations.)

The app has a lot of UX details that I've really enjoyed working on. I wrote up some notes about it here:https://www.freshcardsapp.com/3/Separately, also working on a Zettelkasten notes app that pushes you to make small, atomic notes that you can organize in "collections" to provide structure beyond just hyperlinking in the note text:https://understory.ussherpress.com/This has been a lot of fun iterating on. I started with a Miller Columns UI, like Finder, to visualize the graph of connections between notes, but I found that it was too overwhelming to use, so I scaled back and went with a more Notational Velocity-like quick search bar with note addressing. The app UI mimics a browser because I found that it works really well for something like this. I need to polish it a bit more and want to find people who will give it a beta test to help me iterate on the ideas some more.

reply

ralmidani
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on an Arabic-language Electronic Health Records system (moving to Syria in about 2 months and planning to market to clinics there). No current plans to release as Free/Open-Source, but the stack is Elixir/Ash/Phoenix/LiveView/Bootstrap.

While working on it, I realized I should build a small Hex package for authoring and playing demos right in a Phoenix app (it's very easy to author scripts with AI or by hand):https://news.ycombinator.com/item?id=48087389

reply

hy-token
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on Liel (
https://hy-token.github.io/liel/
), a tool that can compare and integrate LLM memory as single file.

Instead of saving LLM memory in Markdown, I want to manage it using a graph structure to easily record the relationships between tasks and decisions, and persist when, why, and how they changed.

reply

merelysounds
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

An image logic puzzle game about nonograms[1] called Nonoverse[2].

I’m automating App Store media creation; both screenshots and app preview videos can now be recorded automatically; this way they should stay up to date and show correct content for a given locale.I’m also adding translations; if anyone would like to help (with translating or testing new locales) let me know!Early results are already live in the App Store page.[1]:https://en.wikipedia.org/wiki/Nonogram[2]:https://lab174.com/nonoverse/

reply

purple-leafy
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

My own browser game. I created a browser game engine and building my first ever game with it. I can’t wait to launch it, I think it’s pretty cool. I’ve been working on it for 6 years!

The tech surrounding the game is awesome, the game and engine are fully deterministic, discrete (not float based), and bit-packed data structures throughout, powers of 2 everywhere for really fast operations, and logic and rendering are fully decoupled.I wrote a simulator for the game and can simulate 10,000+ games in around 50 seconds on my MacBook M1 Pro. Purpose of the simulations is Monte Carlo method to tune my enemy AI (not LLM - conventional bots etc)

reply

arsenide
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool. I’m also working on a browser game - multiplayer, deterministic, with simulator for PvP tuning.

Email in profile - would love to connect.

reply

GMoromisato
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm still working on GridWhale.

My premise is simple: What if we could build a vertically-integrated, batteries-included, cloud-based development and execution environment that eliminated all the complexity of cobbling together a hundred different dependencies?I learned to program in a simpler age, when programs ran on a single machine and had direct access to input, output, and storage. We didn't have to worry about client-server communications, or async storage calls, or idempotent microservice requests.The reason we worry about that now is because modern programs don't run on a single machine anymore. They run on a distributed system with thousands/millions of clients (web browsers) connecting to hundreds/thousands of backend servers.But what if we could build a platform abstraction layer on top of that distributed system? What if the platform took care of all the distributed complexity and the program itself didn't have to worry about that. From the program's perspective, it's just running on a big (abstract) machine. That's GridWhale.

reply

hxii
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I finally cleared a roadblock that was preventing me from writing more posts and sharing some of the photos that I take -- I patched Hajime -- 
https://sr.ht/~hxii/hajime/
 with the functionality I was missing from it.

So now I can get back to the project that I was actually working on (but mostly deferring) for some time now -- boku --https://sr.ht/~hxii/boku/which allows someone to write a sequential series of tasks to perform without using code

reply

heio10
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

A tool to simulate and benchmarks MPC protocols in your local machine with your desired network parameters, without need to spawn real distributed servers. The simulator uses math formulas to compute the delays to send the messages.

The tool simulates MPC protocols but also allow you to write them using traditional networking as usual.I expect this tool to be useful for protocol researchers and cryptography engineers.

reply

Asmod4n
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a small framework to make desktop apps in mruby, targeting Linux, Mac and Windows. The aim is a native app for the kind of thing you'd usually ship as a webserver and tell users to connect to via localhost. 
https://github.com/Asmod4n/hypha-mrb

reply

kingofsunnyvale
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm building a chrome extension that scans everything you read and highlights text if it maps to a market on kalshi. On hover, a tooltip pops up allowing you to drop money on it.

Use this to doomscroll nba twitter and sports bet, or if you're feeling more highbrow, peruse the NYT and passively gamble on geopolitical events.Try it out here:https://chromewebstore.google.com/detail/anywager/eebgbiogbb...

reply

thekevan
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A desktop client for Repomix. Repomix is a CLI which allows you to summarize all the code in a repo in one txt or md file so you can in turn feed it to an AI model for analysis. It absolutely gets the job done it its current state, but it is a personal project so there may be a few rough edges.

https://github.com/KevanMacGee/Repomix-DesktopIt's open source and has no official connection to Repomix. But the developer, yamadashy on Github, knows about it and seemed to like it enough to add it to the Repomix website under the community projects.I like being able to paste all the code into a browser window and have lengthy discussions with ChatGPT, Gemini and GLM. Doing so in the browser saves tokens over doing it in Cursor or Codex. I like using the Projects feature in ChatGPT in the browser and Notebooks with Gemini because that gives the model context and history on whatever I am working on. It was one part scratching my own itch, one part learning about Python and Customtinker.It's made specifically for when you just want to get the code and paste it, no muss or fuss. It doesn't have support for flags (yet?) like the CLI because again it is built for speed. Besides, when I want flags, I like using the CLI instead to get granular. Repomix Desktop is for "just give me the code."I'm a self taught coder so I'm very open to feedback.

reply

arvida
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Mainly working on 
https://localhero.ai
, automating i18n translations for product teams. Basically runs as a GitHub Action, translating new strings on PRs matching your brand voice and glossary. Got our first fully selfserve customer a few weeks back (found us through the docs). Interesting work lately has been improving how the system learns from manual edits, when someone tweaks a translation in the UI, it feeds back into translation memory and influences future translations in a smart way. Also did stuff like improving our agent skill, so coding agents get glossary/style guide context automatically and they can write source copy that better matches the brand.

Been pushing some new stuff onhttps://infrabase.aias well, my AI infrastructure tools directory. Traffic growing steadily from comparison and alternatives pages. Interesting finding is that blog posts rank better but get fewer clicks now because AI Overviews, interactive comparison pages still earn clicks. ChatGPT has also started citing the site more as a source. Adding new content and polishing existing parts of it, added a page focusing on EU based services athttps://infrabase.ai/european.

reply

chandureddyvari
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

For a long time I wondered how SV startups got such pretty landing pages (here’s a comment I left 2 years back: 
https://news.ycombinator.com/item?id=37421273
). I wanted one for my side projects but couldn’t afford an agency, and the templates online were boring. Creating the page was only half the problem. I also needed somewhere to collect emails for the waitlist.

After AI happened, I built an app (promptfunnels) to scratch my own itch and generate funnels (fancy name for landing pages with a purpose).Then came the harder part: marketing it. Coming from a tech background, I knew nothing about marketing, so I started reading and came across the $100M Leads book. I realized codifying those principles together with funnels and marketing automation had a real market. My family, friends, and acquaintances became the first customers.
A friend joined me as cofounder and we both quit our jobs to do this full time.As we talked to other startup founders, they kept describing a tangential problem they called GTM. At the core it was the same thing we were solving: marketing for non-marketers. So we pivoted to RevMozi(https://revmozi.com/), which helps non-marketers do both inbound and outbound GTM.We’re dogfooding the product and coming out of beta next month.Wish us luck.

reply

nottorp
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

> how SV startups got such pretty landing pages

Umm where? They are indistinguishable from each other. Not pretty.

reply

chandureddyvari
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

some of them are non existent today. Check the parent thread - some good recommendations(for 2023) on both functional websites and pretty websites. At that time if I recall linear landing page was all rage, and there were many copycats.

reply

lawgimenez
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m currently working on an API-first identity verification backend built with FastAPI. It is made for handling ID documents, selfies, OCR data, biometric signals, API keys, webhooks, and tenant billing data.

Hopefully I can find an investor in the future, still in the early stages.

reply

brachkow
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on requested features for my social wishlist app 
https://thingstohave.app
: image uploading, passkeys and more clear list organization UI. Everything is in polishing stage, and I hope to release these before June.

Big thing I made recently is moving it from SvelteKit to Hono + Inertia + Vue.I like SvelteKit, but I was struggling with stability in active development periods, and writing proper tests was very hard due to mocking all the magic, especially outside trivial testing tools.Now the whole app is straightforward Hono MVC with Vue powered UI. Logic is easy to test, and all UI states exposed in Storybook.I wrote a custom adapter that makes Inertia run on Hono, and coincidentally same thing was released by Hono author itself as official module, which is great sign for adoption!So, try Inertia – it is a best of both worlds. You write MVC backend as you like, and use modern JS frameworks for templates.https://inertiajs.com/docs/v3/getting-started/index

reply

linsomniac
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

The Ubuntu DDoS got me to thinking: If we had a critical need to respin machines (like our data center caught fire), we would have been in for a real challenge. We run apt-cacher-ng, but it did nothing for us during the DDoS, and worse: Every few weeks or a month ac-ng will go out to lunch and we have to fix it.

So: ac-ng didn't reduce the impact of the DDoS, but it does lead to impact when there is no DDoS. Worst of both worlds.So I'm working on an apt-cacher that goes to lengths to keep working as much as possible when the upstream is down. It will check the repo metadata and keeps a list of your "hot packages", and will download those before flipping the new metadata to be live, effectively a snapshot. It won't allow you to download a package you've never downloaded before in the case of a DDoS, but packages that you do download regularly (machine re-installs, apt updates), it will ensure are available in the repo.I'm calling it apt-cacher-ultra. It is pretty early days, it'll probably be another week before it's ready for a beta. I'm running it in my dev cluster right now, successfully.https://github.com/linsomniac/apt-cacher-ultra

reply

bramadityaw
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on blase (
https://github.com/bramadityaw/blase
), a language server for Laravel's Blade templating language. This is a proof-of-concept project that I plan to make into a submodule inside a more general PHP language server.

reply

williamtrask
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

A non-profit to deconcentrate power over AI through better infrastructure for external auditing/oversight, and better infrastructure for local/federated inference/training 
https://openmined.org/

Also, we're hiring engineers and PMs (the eng position is about to be up).https://openmined.org/careers/#brxe-zgsziy

reply

krembo
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://aggly.com

A beautifully opinionated news aggregator that reads rss, twitter, reddit, youtube, telegram & more

reply

geoffbp
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

No HN? :)

reply

krembo
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Of course that also HN

reply

mts_building
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m an app developer and I used to have my laptop (mainly Mac but also have a Windows one) and a monitor. I would create apps for IOS on my Mac and eventually upgrade it to also work on Android. Now I have 2 monitors, one linked to my Mac and the other to my Windows laptop. This way I can simultaneously develop for both platforms at the same time.

reply

haritha-j
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Exploring use cases of world models. I know its a rather vague term, I'm primarily interested in generative models that can create new 3D scenes, in formats such as gaussian splats. Just finishing writing up my PhD thesis (3D modelling of industrial assets) at the moment, so hoping to get more into it soon. If anyone has any thoughts about this space, I'd love to chat!

reply

selvan
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Creating an AI native solution to manage workflows of my live streaming business (
https://www.cheerarena.com
)

Most workflow softwares are complex to extend & customize. Building an AI native, structured workflow orchestrator from scratch for agentic era.As a starting point, have designed and implemented an AI native data store to store semantic linked structured input & output data of workflow steps/tasks. These structured input/output act as spec and guard rails for the workflow tasks.

reply

upmostly
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building DB Pro, a modern, beautiful, and now fully self-hosted database client for desktop and web.

Just launched Studio, which is the self-hosted version of DB Pro.I also keep a devlog. #9 was just published to YouTube.Self-Host Your Own Database Client | DB Pro Devlog #9https://youtu.be/MJvSrJGtk70[1]https://dbpro.app

reply

jasonhong
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

We're working on AI user testing, to make it dramatically faster and cheaper for product managers and dev teams to find major usability issues with web sites. Give us a web site and a task users would do (e.g. "Add a pink shirt to the shopping cart"), and we have some AI users try their best to do the task. The output is a report with a prioritized list of problems identified, plus narrated videos that show each AI user trying the site.

If you want to try it out, we offer some free credits athttps://fuguux.comAny feedback you have would be incredibly helpful! We're considering more kinds of reporting, support for QA testing, better integration with CI/CD, and more.Note: we don't want to replace real user testing, but rather complement it. With AI user testing, you can get quick feedback on potential usability problems in hours for a fraction of the cost, making it so you can iterate much faster. We advocate doing user tests with real people to understand problems that require domain knowledge or nuance.

reply

rcarmo
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m stabilizing piclaw (
https://rcarmo.github.io/projects/piclaw
) - it is now my main IDE for all my personal projects, and I run several instances with different plugins. This is _not_ an OpenClaw clone, it is pi in a web trenchcoat, with (I hope) most of the philosophy in place.

I am also working on various other things (a Go Clojure interpreter with IR/WASM, my own inference library, etc.). All are linked from the page above to a degree.

reply

zuzuleinen
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://github.com/zuzuleinen/algotutor
, a tool I use daily to train in algorithms and concurrency using Go.

I use it every morning for about 15 minutes. Review the cards, then 1 problem in the algorithms, 1 problem in concurrency, and I'm done.I wrote more here about my motivations for creating it:https://medium.com/@andreiboar/algotutor-using-ai-to-actuall...

reply

nasaeclipse
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Learning SDL so that I can make a game in C++

Long road ahead of me XD

reply

jessecoleman
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Since getting laid off in Feb, I've been spending my free time polishing up my word game Gram Jam (
https://gramjam.app
).

I finally finished the (monumental) Svelte 4 -> 5 migration that had been getting dusty for the last year. This unlocked a higher performance ceiling for me to polish my animations and UX. Now I'm revamping my onboarding experience and taking another crack at marketing and promoting it. Last year, I was focusing on setting it up as a PWA and integrating Sentry monitoring and Stripe integration. All important stuff but not what got me excited about the process.I've been pretty tied up with maintenance and admin work, and haven't gotten a chance to work on the actual game design in a while, so I'm very excited to return to that part of the project soon. I have ideas for new puzzles and modes spilling out of my ears and I feel like with LLMs my prototyping can finally keep up with my brain, now that I have a robust foundation for the game architecture.

reply

bingo_cannon
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

https://surmai.app/

I'm working on a Personal / Family travel organizer. Started as tool to allow me and SO to plan a trip together. There's been steady progress over the last couple years. Focus on privacy and ability to self-host. Of course, there is a managed version if one doesn't mind me having access to their data.

reply

fersarr
 
22 hours ago
 
 | 
parent
 | 
next
 
[–]

Interesting! Maybe making this info avilable to local LLMs would be useful too. Side thought: when we plan big trips I tend to pre-populate google maps with loads of markers of interesting points. I would love to be able to save this offline and combine them with other sources like youtube/instagram clips offline somehow.

reply

wmil
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

So I had an idea for a music app that tries to minimize the amount of music theory needed to play as a group.

Basically you pick a key, then it's just 7 buttons that play the notes in that key. Actually 21 because there are three octaves.This has some neat effects. You can play thirds by just hitting every other button.I wanted kids to get started playing as a group without having to worry about wrong notes. Everything is in the same key so it never sounds too bad.There's not much to look at, I just started it last Friday.https://github.com/wmill/EasyMusicI'll throw on some screenshots if there's any interest. I could actually use some feedback from someone who knows a bit about music, my knowledge is pretty minimal.

reply

asciimoo
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'll continue to work on 
https://github.com/asciimoo/hister
 as much as I can. I plan to add new extractors and optimize the indexer storage usage by moving out HTML/favicon content from the index and storing them in an efficient compressed way.

Hister is a free general purpose web search engine providing automatic full-text indexing for visited websites.

reply

solraph
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

A set of tools to making setting up, joining and using a Samba domain on Linux much much easier.

This started withhttps://github.com/edward-murrell/sambervise- a GTK tool for admining Samba users and groups. I'm currently building a tool that walks a user through setting up a domain, adding DCs, and configuring fileservers and workstations.In the TODO is making NFSv4 integration with Samba as painless as possible, and some kind of GUI application.

reply

MrFiskarBengt
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

A CLI tool that will connect business rules (etc) to code, solving the Tribal Knowledge problem for software projects.

https://en.wikipedia.org/wiki/Tribal_knowledge

reply

boyter
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on 
https://searchcode.com/
 again which I bought back, albeit as code search tool for LLMs. It solves the “should I use this library” by allowing the LLM to inspect search and analyse it before integration. Can use it to compare multiple repositories before downloading. It comes with a large amount of token savings and can be really useful when wanting to learn about a codebase.

Since it does it anyway I added dossier pages to it as wellhttps://searchcode.com/repo/github.com/rust-lang/rustWhich is useful for humans, and shows what the system is creating.Best part is that I get to use the tools I have built, sohttps://github.com/boyter/sccandhttps://github.com/boyter/csto improve it which benefits anyone using those tools.

reply

freakynit
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

1. Prepping to release the tool behind 
https://sourceryintel.com
 as open-source. The insane levels of breadth and depth in the research reports this tool is generating has blown me away completely.

2. Released "Postlet" (https://github.com/freakynit/Postlet), a tiny markdown-based static blog generator with a plugin pipeline, markdown + frontmatter pages, and theme support. Demo:https://postlet.pagey.site/.. working on still adding more features.

reply

anilgulecha
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

the first is deep researsh like tool?

reply

freakynit
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yep... and it works much better than even chatgpt, gemini or claude deep research outputs. And costs less than 10 cents per report, including search and proxy charges. All claims are grounded in evidence and linked to source material.

reply

anilgulecha
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Looking forward to the release. There's some DR benchmarks, which can you also run BTW.

reply

freakynit
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Awesome.. and thanks for the DR benchamrks mentions. Will check it out.

reply

drchiu
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been working on Broadcast since Sept 2024:

https://sendbroadcast.netIt’s a self-hosted email marketing/newsletter app. The basic idea is: own your subscriber database, run the app on your own server, and send through SES/Postmark/Mailgun/SMTP instead of being locked into another SaaS.Not trying to be “Mailchimp but cheaper”. It’s more for technical founders, agencies, and consultants who want a boring, controllable email tool they can deploy for themselves or clients.I’ve kept the changelog public because I wanted the work to be visible:https://sendbroadcast.net/changelogMy buyers are typically people who want to own their data and are in regions that have strict data privacy regulation/laws.Interesting fact: This was myreallast project where v1 was built by hand before AI coding became the norm in the software industry.

reply

Meld5792
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Building Meldhive for people who wanna start but don't know how to validate if the needs out there were true. It finds what your market is already saying about your problem space, across Reddit, X, TikTok and more. Structures it into a report way with data.Most founders write in their own language. Their customers use different words entirely.Free and early access - meldgtm.space

Would like to hear your thoughts and feedback than anything.

reply

frankdenbow
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

AI basketball community, using computer vision to get highlights and stats 
http://ballers.gg

reply

7237139812
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a web based tool to review markdown and HTML collaboratively with your agents. Wrote about it on my blog. No aspirations to make it more widely available just yet. I'm mostly focusing on getting it right for my day-to-day (making it feel light and easy).

https://shivan.dev/writing/post/markdown-wrangling

reply

phyzix5761
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Been writing in my blog every day, reading more, created a poker equity calculator, and working on a city wide project where I document attractions, restaurants, and stays I've experienced in my city (very early stages).

Website:https://arkvis.comPoker Equity Calculator:https://github.com/lodenrogue/poker-equity-calculator-webDavao Explorer:https://github.com/lodenrogue/davao-explorerReading Summaries:https://github.com/lodenrogue/reading-summariesI also created a couple of chrome extensions:HN Dracula Dark Theme:https://github.com/lodenrogue/hackernews-dracula-theme-chrom...Regex Search Chrome Extension:https://github.com/lodenrogue/regex-search-chrome-extensionCreated a small command line util to get earthquake data in the Philippines:Philquakes:https://github.com/lodenrogue/philquakes

reply

dvrp
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Figuring out the meaning of it all.

I thought sharpening my craft in software for a decade would help; but, the more I read ancient scriptures, the more sense they started making -- and this is as someone who's been mostly agnostic.Seeing people working on nostalgic apps, wealth-pursuing prompt management tools, or ideological open-source alternatives. I've worked myself in many types of software of similar kinds, and I've found.. not much at the other side of the pursuit.Some call it “הֶבֶל”; “तृष्णा”; or, “تَكَاثَرَ”...Still working on it.

reply

storystarling
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on StoryStarling (
https://www.storystarling.com
). You describe an idea for a children's book, optionally upload photos of your kid or pet to put inside, pick a style, preview the result, and order a printed hardcover. Bilingual if you want.

reply

boramalper
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Social Maps: a user reviews and ratings service for points-of-interest (e.g. cafes) in OpenStreetMap.

I’ve been trying to reduce and eliminate my reliance of the Big Tech and the lack of user reviews and ratings was always a big pain point for me each time I tried to switch away from Google Maps.I’ve started building a service where users can write reviews and rate “places” (POIs) in OpenStreetMap database, such as a cafe, a museum, or a shop. It’s a quite straightforward CRUD app with bunch of OpenStreetMap-specific features such as logging in with OpenStreetMap and querying places by their OpenStreetMap metadata.It’s still in active development but it has good docs, a great API reference (including an OpenAPI spec), a demo app with theentire planetimported and queryable, and an early stage Android SDK.https://app.socialmaps.org/https://docs.socialmaps.org/https://codeberg.org/socialmaps

reply

jerrygoyal
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

For those who don't want to switch to AI browsers, I built a chrome extension that lets you chat with page, draft emails and messages, fix grammar, translate, summarize page, etc. 
You can use models not just from OpenAI but also from Google and Anthropic.

Yes, you can use your own API key as well.https://jetwriter.aiFeedbacks are welcome.

reply

lightweb
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A high-throughput multicast Bitcoin transaction distribution system, with a roadmap towards billions of transactions per second.

Features:- Control channel for block header announcements, operational mechanisms, and network topology automation- Separate channels for subtree, subtree grouping, and transaction load- Transaction load sharding by deterministic multicast group membership based on TXID- Transaction specialization filtering and retransmission both unicast and multicast, to connect edge networks only interested in a portion of the transaction load for whatever reason- NACK-based retransmission of missed packets via hash chain gap sequence tracking (per sender, per shard) with automated caching endpoint beacon discovery and tiered network distribution- BGP-AnyCast based transaction ingressBasically all the topology pieces to scale the actual small-world network for Bitcoin miners or transaction processors; dense at the core, with layered and sharded group distribution towards users at the edges. Right now just site or org-scope multicast in planned, but provisions are being made to extend via MP-BGP eventually.For BSV Blockchain but could work for the other Bitcoin variants too, if they ever wanted to scale.

reply

fatih-erikli-cg
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am creating 3d modeling tool. I am not willing to publish it. The well known 3d modeling tools come with animation frames, extension support, code writing part etc. I don't want to be one of them. I think it is less than nothing if something comes with extensions. Everything extension of something. If something doesnt work well, they publish another extension. They never worked well. I publish the render part, it is something like that 
https://fatih-erikli-potato.github.io/blog/rendering-a-bezie...

reply

sedatesteak
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

My friends and I went to Japan for a holiday a year or two ago. Every bar had an electronic dartboard and we all decided to get one when we got home.

We all did, only to discover that for the three of us we could either play 1v1 or 1v2 with one person having twice as many turns as each other person (and they would always win).If you play on one board locally you can do 1v1v1. It makes no sense.I have an esp32 syncing to the board and forwarding the hits to a client written in godot. I'm now spinning up the server for stats tracking etc.We just want to play darts...

reply

jwilliams
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on JavaScript runner for untrusted code. The whole API is only exposed via messages passed over stdio. Security layers: V8 isolates, two-stage seccomp, frozen globals, mount namespaces, landlock, and more.

https://github.com/jonathannen/hermit

Plus it's too early to really show, but also working on a dataflow language (w/ immutable data) that uses some code semantics from Rust/Zig and friends:https://github.com/jonathannen/badger

reply

lnenad
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Since I don't like the UI and UX of the current offering of diagramming tools I've made 
https://grafly.io
. Fully local, open source, export/import and embed sharing.

And since I don't like the complexity of logging/metrics SaaS offerings I madehttps://logdot.io.

reply

mweibel
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on a bread recipe community where you can share and iterate on bread recipes. 
It's out of personal interest to be able to record my bread recipes and thought it might be interesting for others too.

However, I worked on it for the past ~5 years on and off (well, mostly off) and rewrote it too many times. Now finally close to releasing, bought a domain and setting up all the last remaining things.

reply

jondwillis
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

1) “AI harness plugin build system” to help improve reliability of and increase compatibility across the fragmented AI coding harness plugin ecosystem.

https://github.com/jondwillis/jacq2) Claude code plugin based on some ideas found inhttps://www.anthropic.com/research/emotion-concepts-functionThe main idea is to add hooks that inject “baselines” under some conditions to counteract certain “emotions” that can cause subtle misaligned behavior in agentshttps://github.com/jondwillis/functional-emotions3) Final Fantasy XI custom client remaster in Bevy/Rust alongside an MCP integration that aims to allow agents to play autonomously on private servers à la “Claude plays Pokemon”Contact:https://jonwillis.dev

reply

Cilvic
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

+1 for 1) I started to notice this problem when going from harness to harness (pi.dev/omp/dirac) I'd be eager to try out others, but I can't leave all my plugins behind!

reply

dbz
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.GetSetReply.com

I'm actually looking for beta users! GetSetReply is a SaaS I've been building. It does two things for small businesses:1. It helps you get more reviews by sending automated requests for reviews to your customers over SMS and/or email after they purchase from you (PoS Integrated / Manual Sending)2. The second is helping you reply to the reviews you already have with AI-generated drafts in your brand's voice that you can send to Google/Yelp/TripAdvisor.I'm very grateful to anyone who is willing to test or provide feedback. If you create an account (it's free with no credit card or integrations required), I'll reach out! Or you can email me via my email in my profile.

reply

eric_trackjs
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://www.certkit.io
. It started as a solution to handle TLS certificate automation for my other SaaS products, but we realized other people who run on-prem workloads might get something out of it.

It uses Let's Encrypt by default. We use delegated DNS to handle ACME challenge validation (we run the DNS, you just CNAME to us). This means you don't need to give us DNS credentials or anything. And for HA workloads it's great, because there's a central clearinghouse for certificates - so all the machines in your web farm (or whatever) get the same cert, but you don't run in to rate limits with LE.We're recovering Windows Server guys so we made sure our automation works for painful windows workloads like IIS, Exchange etc. too.We've had enough interest that we're building it out for real. Just left beta last month.

reply

TZubiri
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

How is this better than just LE with certbot?

reply

nickjj
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've had public dotfiles at 
https://github.com/nickjj/dotfriedrice
 for a long time but recently branded them and after having run native Linux for 6 months, I added a desktop environment based on using niri and Arch Linux.

It can get you up and running in a few minutes with an installer that can set up a new system or keep an existing system up to date. There's also a command line version that works on Arch and Debian based distros (including WSL 2) and macOS. I use it on my personal devices and a company issued MBP.I'm not going to lie, I've been using computers for 25 years and this is the happiest I've ever been with using 1 machine for everything (software development, media creation, gaming, etc.).

reply

microflash
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on Mesaphore, an Excel-like spreadsheet app[0] backed by a Parquet-based file format. The premise is when Excel starts off as the starting point, then over time becomes a data exchange format between systems, and eventually becomes a bottleneck for the system. You still want to provide your users something Excel-like but also want to address the limits of Excel[1].

Majority of code (almost 70%) is generated by Gemini Pro and is extremely ugly. Due to a recent eye injury, I've not been able to code as much as I want, so I'm delegating many things to Gemini. Eventually, as my health improves, I plan to rewrite the entire thing.[0]:https://codeberg.org/naiyer/mesaphore[1]:https://support.microsoft.com/en-us/office/excel-specificati...

reply

marking-time
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

A CLI to replace bookmarks in my browser because I noticed some tracking code lurking in my Firefox bookmarks. This is just personal tool for my own use.

https://codeberg.org/Marking-Time/marksan

reply

grepfru_it
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

Tell me more about the tracking code

reply

marking-time
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

From the "Manage Bookmarks" applet within Firefox[Menu|Bookmarks|Manage bookmarks] choose the "Import and Backup" option at the top of the applet. Choose the "Export Bookmarks to HTML" option and save the file. This will create a HTML file on your device containing all your bookmarks.

Open the HTML file in a code/text editor. Look at one of the anchor tags and you will see the contents of "HREF", "ADD_DATE", "LAST_MODIFIED", "ICON_URI" and "ICON". Only the "HREF" is necessary to make the anchor tag functional. All of the others serve other purposes. Most of the others makes some sense, but seem obsessive to me. The longest, sometimes hundreds of characters long, is the "ICON" item. That long string of characters concerns me and looks suspiciously like the traffic I see when I use network monitor inside Inspect. To me it looks like a tracking code.Of course I may be wrong, but none of that stuff is necessary except the HREF. The script I wrote strips off everything except the HREF, puts it in a new anchor tag, and it works fine. Really this is just old school HTML.

reply

bmalicoat
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Learning how to make custom PCBs and 3d printing. I really like Radio Taiso (daily calisthenics synced with music), so I made a dedicated speaker (
https://www.taisospkr.com
). It was fun to add new tools to my tool belt (ESP32, remote firmware updates, embedded website, streamlined wifi setup). Already have a new project based on a very similar architecture that I'm super excited about! Making PCBs and hardware has never been easier as a solo developer.

reply

roadbar
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Besides my regular work i am going a bit into learning programming and took a problem to fix for me =) As a Sysadmin back in the days i always got along with bash and a bit of python... Now in IT Management i want some quick overview and started to build a app (macOS) that just lists the issues assigned to me... Simple API stuff with a bit of Swift around - really like it so far - will Show HN when done & ready for real world comemnts =)

reply

gchamonlive
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

https://gitlab.com/gabriel.chamon/orisun
 is a Gitlab-first methodology I've been cooking for the past month that brings epics and work-items to the repository. Present your project, describe your domain and it will produce meaningful epics and work-items that are automatically reflected into Gitlab kanban board using 
https://gitlab.com/gabriel.chamon/ci-components/-/tree/main/...
 in Gitlab ci.

reply

drewsonian
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been building (launched in Feb) a home phone service for families who want to put off the smartphone for as long as possible, but still give young kids the ability to communicate via landline.

https://chatterboxphone.com

reply

guyrt
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A podcast that isn’t about AI (in the normal way)! I started Pagenerd with some friends to talk about science fiction - loosely defined - and give us a chance to hang out. It’s pretty good. Find it at 
https://pagenerd.com
 which links to all the usual places.

reply

p2detar
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

It's on my list, I really liked the `The Forever War, by Joe Haldeman` episode. Good job. However, less "Fuck Christopher Columbus" and things of this sort, please. That's just stupid.

reply

hsnice16
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on the agent-friendly scorer. It scores the public repos for their agent friendliness. The project also has a GitHub action to comment on the score delta in a PR comment. You can add it as a skill to find out which agent will perform better for the codebase.

Live:https://agentfriendlycode.com/

reply

spikepuppet
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a little local first review tool called Review (though I sometimes refer to it as differ since that's it's original name) - you can see screenshots here 
https://x.com/rhyslikepb/status/2053149881104265599?s=20

The idea was borne out of wanting to use the review tools that you get on existing sites like GitHub, without having to push and start bloating PR lists. You'll be able to leave yourself comments and code suggestions after review, which you can then pull out in a Markdown file to feed back to your coding agent (or anything else for that matter).I'm also trying to include some optional (very optional) AI extras where you can use your own keys, and then get a tour of what you've changed and a quick overview of the changes.

reply

yassi_dev
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a framework that lets you easily create tools inside the Django Admin - 
https://djangocontrolroom.com

I've published several panels under this banner already (tools for redis, caches, celery, etc.); I am currently working on a base library layer for tools to inherit from and to make it easier to create new tools.Essentially, the point of all of this is to make it so that you don't need so many external services; Instead, DCR provides self hosted alternatives. This in turn makes it a lot easier to build and productionalize something using Django.Reception has been decent so far and I estimate several thousand current adopters (Its hard to estimate based on download numbers alone.) For May I will finalize a common design language, further formalize the plugin system and how it works, and likely release a new panel.

reply

gchamonlive
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been using 
https://github.com/gchamon/buzz
 as an opportunity to have a WebDAV with tight integration with real debrid, jellyfin and opensubtitles. It solves the requirement of jellyfin for having a single file per folder even if the original source had many files in them, adds confirmation for removing entries from debris, has an archive so deletions can be restored, a simple but powerful integration with opensubtitles and a functional logs UI. It's also an opportunity for me to review web design concepts and experiment heavily with coding agents, both local and SOTA.

reply

harrisoned
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I have been working for some time on a budget body/facial mocap solution with Unity. Mocap is hard, and what exists is locked behind subscriptions or is just very expensive.

With Unity I'm trying to bundle a bunch of different free, cheap or open source solutions together. For facial, that includes a custom converter from the output of Deadface (based on Mediapipe) with ARKit blendshapes, and also eye movement. For body it's a custom hook to SlimeVR that allows you to mocap with cheap-ish IMU-based DIY trackers, and all that on top of a custom made (not free but open source) physics rig solution that gives you accurate rigid body real time collision, saving on cleanup work.It's being going really nice despite being an unusual workflow. Hope to release it as a plugin for a in-development sandbox game in the near future. Mocap and animation has been my passion long before i started with tech stuff, and finally I'm able to pursue it.

reply

lylo
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Pagecord. Blog without the slog.

Blogging is more unpopular than ever but Pagecord is somehow growing in popularity. Keen to know what people here think.https://pagecord.com(Source:https://github.com/lylo/pagecord)

reply

0xc133
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I pushed my first crate this weekend. You can `cargo install tailpipe` on macOS and Linux (and maybe Windows, haven’t tested there yet) and get a locally-hostable SSH server that plays back asciinema recordings to clients.

`ssh -p4242 tailpipe.clee.sh` for a quick demo without installing anything. Requires any valid RSA or ED25519 key.

reply

brianjlogan
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Ah neat idea!

reply

insaider
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

WhatsYum - 
https://whatsyum.com

Ratings per dish instead of just the restaurant as a whole. 4 years in and working on a b2b intelligence offering for restaurants. b2c side has been too hard to get off the ground without solid investment and I've been unable to secure that.Thoughts welcome :)

reply

thangalin
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

http://autonoma.ca/calculators/rocket/antimatter/

Given a distance, an allowable time to reach that distance, a payload to send, and an expected exhaust velocity, how would you calculate the time required to convert energy into antimatter fuel and how much antimatter needed to arrive at the destination (starting from the Moon)?There are a few side calculations, such as the size of the radiator, estimated footprint of the fusion reactor itself, and how much metamaterial is needed. This is to help figure out timelines for a sci-fi novel, so ballpark answers are completely fine.The calculations yield what appear to be values around the correct order of magnitude. Would be delighted to have insights, comments, and corrections.

reply

darkstarsys
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm newly mostly-retired as a VFX software developer & CTO. I'm writing about AI, climate change and more in my blog, 
https://oberbrunner.com
, running Long Now Boston (
https://longnowboston.org
) to promote long-term thinking, and working through my lifetime backlog of "wouldn't it be great if somebody wrote this" ideas using Claude, at 
https://github.com/garyo
.

You should check out my new open source software build tool,https://pcons.org.

reply

maz1b
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on MedAngle, the world's first Agentic AI Super App for premed, medical, and dental schools and recent graduates - young doctors.

MedAngle is literally everything one could need, personalized to their curriculum across 4-6 years of medical school. Quizzes, videos, notes, flashcards, reminders, scheduling, performance, search, and more.Our Super App is comprised of MedGPT + MedAgent + Spaci (futuristic spaced repetition), which serve as layers over our massive collection of features such as the Smart Suite, Learning Library, Clinical Corner, Tested Tools and more.100k+ users, 10s of billions of seconds spent studying smarter, invite only. Bootstrapped, growing nicely. I lead a team of top medical students and doctors.

reply

onlyrealcuzzo
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a memory safe programming language that's like Rust, with a declarative concurrency model, which makes it much safer, simpler, and easier and nearly as fast & efficient

https://github.com/cuzzo/clearThe goal is to make Rust code nearly as easy to write as Ruby, but it almost always does the absolute best strategy.You can write somewhat slow untyped code, and the internal tooling can guide you to adding all the types and optimizations and concurrency strategies that will make your code as fast as possible.

reply

nateb2022
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Sounds a lot like Crystal, which is also similar to Ruby and features a green fiber runtime: 
https://crystal-lang.org/#concurrency

reply

onlyrealcuzzo
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, in a lot of ways.

Crystal wanted to be Ruby/Go - essentially a faster Ruby, that sort of scales, too.CLEAR aims to be a substantially safer Rust - no Garbage Collector - no manual synchronization hazards, and safer than even Pony - but also with far less complexity than Rust.Crystal's fibers did not do well multi-threaded until somewhat recently, and AFAIK, it's stillveryfar behind Rust/Tokio and Go in a lot of important benchmarks. Crucially, afaik, p99 in adversarial workloads can still blowup easily.Like Tokio, CLEAR lowers fibers into Finite State Machines instead of stacks, which perform better than stacks in wait heavy (i.e. Go's primary market - web servers) and idle-heavy scenarios (i.e. chat servers, telecom, etc), and it has Go's work stealing algorithm + forced yielding to ensure p99 doesn't blow out.Also, CLEAR transpiles to Zig, so it has native access to the entire C library. Crystal has a bootstrapping / ecosystem problem that's unlikely to ever be solved.CLEAR doesn't need a single person to contribute to it to have access to basically everything.Also, transpiling to Zig means you get Zig's other killer feature - you can compile to any target (i.e. Linux) from any target (i.e. MacOS).

reply

alextwomey
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Language learning by reading today’s news (and more) with the guidance of an AI tutor. Get lessons and exercises for the gaps this uncovers.

Just released this week on to the App Store:https://apps.apple.com/gb/app/verva-language-learning/id6755...

reply

nsainsbury
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on 
https://www.photogenesis.app

It's an iOS & Android app that applies various generative art effects to your photos, letting you turn your photos into creative animated works of art. It's fully offline, no AI, no subscriptions, no ads, etc.I'm really proud of it and if you've been in the generative art space for a while you'll instantly recognise many of the techniques I use (circle packing, line walkers, mosaic grid patterns, marching squares, voronoi tessellation, glitch art, string art, perlin flow fields, etc.) pretty much directly inspired by various Coding Train videos.

reply

pplonski86
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Im working on AI data analyst - MLJAR Studio. It is conversational UI with AI agent which uses Python to provide data insights. It is available as desktop application 
https://mljar.com

reply

EmptyStatement
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://github.com/Facets-cloud/flow

It does a few things for me:- Claude session management mapping it to real life tasks- A scoop/sweep mechanism to auto-populate the KnowledgebaseIt has turned my claude to more of a PA. I have been made aware of beads since, yet to try it out. I see some similarity and some differences.

reply

pizzly
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Paste Redactor. It redacts Personable Identifiable Information (PII) from your clipboard when you copy and paste text. It uses a custom trained local AI model so that your PII never leaves your device. That is what it does now. Currently working on it to make it work for agents as a privacy protection layer. The idea being that the most powerful AI models live in the cloud but need access to your local files to be useful. We instead want everything to go though a local protection layer before it is sent to the cloud possibly with labels and then reconstructed locally when the cloud sends back its results. Kind of like a Adblocker but for agents and private data instead.

https://redactor.negativestarinnovators.com/

reply

jimfx
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a WASM based procedural plant generator:

https://nodes.max-richter.devhttps://github.com/jim-fx/nodarium

reply

powerpurple
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I recently started a project called best web extension 
https://bestwebextension.com/

Basically attempting to modernize a lot of browser extension which I have been using since like a decade ago. Some of them are outdated and unmaintained and some were good for the time.The project is MIT licensed.

reply

Kuyawa
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Just finished an app that allows you to track every rep, set, and weight at the gym. Decaboy — the ultimate gym companion for serious bodybuilders

https://decaboy.fitBuilt in 15 minutes with mecha-ai my own code assistant using DeepSeekhttps://github.com/kuyawa/mecha-aiRight now working on a betting app, DeepSeek is fairy dust and Mecha is my magic wand, I am unstoppable!* If you need an app I can build anything and I mean anything in one day for peanuts, just let me know

reply

vulkoingim
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on and off on a Spotify recommendation egnine after getting tired of Spotify’s repetitive recommendations.

You get to choose the genres you're interested in, and it creates playlists from the music in your library. They get updated every day - think a better, curated by you version of the Daily Mixes. You can add some advanced filters as well, if you really want to customise what music you'll get.It works best if you follow a good amount of artists. Optionally you can get recommendations from artists that belong to playlists you follow or you've created. If you don't follow much or any artists, then you should enable that in order for the service to be useful, as right now that's the only pools of artists the recommendations are based on.https://riffradar.org/

reply

stroebs
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

An EU replacement for PagerDuty, focusing on the absolute basics - SSO as the minimum even on free, no AI driven workflows, overviews etc. but may include ML/AI driven insights in future since that’s the way the world seems to be going.

https://rotadeck.com/

reply

alopez3006
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

A context and memory infrastructure system so I can change LLM or invite someone to work on a code project without losing context and memory :

https://www.snipara.com

Would love to have your opinion on it, try it it's 100% free. 
npx create-snipara

reply

pierreyoda
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.hncli.newstackwhodis.com

I'm working on a TUI Hacker News reader made in Rust! No AI, no credentials needed.

reply

VoxelBoy
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

A way to track versions of ALL software and notify users about new version.

Started with a niche and launched it: VersionAlert for Unity (https://versionalert.com/unity)Working on the bigger product still. Existing solutions I've found in this space seemed lacking. On my website, I want people to quickly find the software they want to be kept up to date about (with a smart search bar that does the heavy lifting for them) and easily sign up for notifications for new versions. Hope to make a Show HN for it soon!

reply

davideuler
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I created a dashboard for stability of OpenClaw and Hermes. It shows stability score(10 is the most stable) which is calculated by analyzing Github issue by GPT.

Lots of friends asked me which version of OpenClaw/Hermes are recommended as a stable version. I've no clue of it, and I don't updated my OpenClaw/Hermes very often to avoid unstable versions frequently. So I created the Agent Watch dashboard.https://agentwatch.aicompass.dev/

reply

schipperai
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Very cool. How do you classify negative signals?

reply

davideuler
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've updated several iterations to improve the accuracy for release stability. And I open sourced the project so that you may contribute to the dashboard to make it more useful: 
https://github.com/davideuler/agent-watch

THANK YOU for all guys who gives feedback for the tiny project.

reply

davideuler
 
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

GPT would analyze each issue if it is negative. And also it would analyze if it the core features related issue. I iterated it several times. The dashboard seems more reasonable than the initial version. I would open source the project soon so that other could contribute to build a better stability dashboard for the daily Agents we use.

reply

jcfrei
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I think LLMs will make dealing with complicated ERPs much simpler. So I built a chat-native one that can do all the functionality just via prompting: 
https://github.com/lambdadevelopment/lambda-erp

reply

joladev
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve been building an uptime monitor service for a while now, something that is genuinely reliable and only alerts you when something is actually going on. Also comes with very pretty status pages!

Free tier is enough for most users, paid tier just exists to gate the stuff that is expensive to run like SMS alerts.Check it out at [Larm](https://larm.dev) and try out the [response time checker too](https://larm.dev/tools/response-time) to try out the Larm probe infrastructure.

reply

KeybInterrupt
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I am trying to better my understanding of Agentic coding tools and Tool using Agents by building my own, without relying on an Agent that writes said Agent/Harness

I believe writing my own "Toy Harness" is a good way to learn and understand these tools.Other than that, I did plant my tomatoes today.

reply

knuckleheads
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a newish variant of Sudoku called Binku. It combines the traditional Sudoku rules and adds the rules from a game called Binario/Takuzu (with 1-4 as one color and 5-8 as the other color).

A sample puzzle can be found here:https://sudokupad.app/23x300ggznIt's been well received by the (very kind!) Sudoku/puzzle communities, so I'm working on throwing a nice interface on it that fits the rules a bit better. I've found about five other examples of others doing a variation of this ruleset before in one way or another, and it's been fun trying to see how hard/deep I can get this puzzle to go.

reply

spmartin823
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building AI tools for click based workflows, starting with wordpress sites. Clicks run the world and AI needs to run on clicks!

If you want to check it out:https://presspass.aiIf you think this is stupid or you know of a more annoying “click based” workflow that should be automated, let me know! I’m early and need more thoughts.

reply

Bobbijn
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

We (AIFAQ.Pro) ARE WORKING ON A SKILLS MATCHING ENGINE FOR FOUNDERS , MENTORS AND INVESTORS.

reply

nilirl
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

How to use a spreadsheet for creativity

https://www.nair.sh/guides-and-opinions/communicating-your-e...I finished writing that over the weekend.I talk about combinatorial creativity as a way to be creative under time pressure. I had fun writing it, it'd been on my mind for weeks.

reply

theodorejb
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building PHP Handlebars, a spec-compliant implementation of Handlebars in pure PHP:

https://github.com/devtheorem/php-handlebarsI've also been developing Cropt, a zero-dependency JavaScript image cropper which works great for cropping and scaling profile images before upload:https://devtheorem.github.io/cropt/

reply

stagas
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I recently switched to developing VST audio plugins and I'm loving it. Already done 3 [0][1][2] and I want to keep doing this if I manage to generate some income from it. I develop them in Typescript and then convert them to C++ with Webview, this way I have a web demo of the plugin that is almost identical to the one you get for the DAW.

[0]:https://technokick.com/(Techno Kick synth)[1]:https://riviera-demo.surge.sh/(Reverb effect)[2]:https://ya3.surge.sh/(TB-303 synth clone)

reply

tophattom
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm slowly but surely working on a first update to my Android app, Tunemark (
https://tunemark.app
), which I released a while ago. Tunemark lets you add bookmarks to moments in songs so that it is easy to jump back to them. It is really convenient when practicing dancing or music and you need to constantly reset back to specific parts of songs. Unlike most DJ-type apps that could serve similar use cases, Tunemark works with most music apps, including streaming services.

I have new features such as sharing bookmarks and possibly BPM detection planned but also some quality of life changes like better UI scalability for different size screens/split screen use.

reply

ghostfoxgod
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building (or rather rebuilding/pivoting my focus) CatchIntent (
https://CatchIntent.com
). The intent layer for B2B outbound.

The marketing site is stale with our previous offering, the demo of upcoming product is here:https://vimeo.com/1190884516

reply

rhoopr
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I continue to be working on kei, my cloud->local photo/video sync engine.

iCloud Photos is fully baked along with implementing their completely undocumented SyncToken. I’m doing some QoL work in the next few weeks, tightening up some early architecture decisions, and then adding more providers (Immich, NextCloud, Google Takeout… else TBD).Since last time I posted this, two other people contributed and I’m almost at 100 stars! That’s some dopamine.https://github.com/rhoopr/kei

reply

afzalive
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a tool to help review changes made by AI agents in response to PR review comments.

The key functionality is to be able to easily see the changes made for each comment, rather than each file.

reply

aaronvg
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

We are working on making our programming language BAML turing-complete. 
https://github.com/boundaryml/baml

It is a language that is embeddable in other programming languages, with the type system similar to typescript, and a runtime that is similar to Go.People use it currently for structured outputs with llms but soon we will support orchestration and more.We are letting some users have an early access preview! Let me know if you are interested in hacking with it!

reply

troebr
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm making a surf forecasting site a la surfline.com, I started mostly to have an API to use for my tidbyt, but I figured I might as well make it a full thing and built my own features! It's on quickswell.com but it's only Socal at this time (fewer spots to compute)

reply

skhavari
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

3 things

- AI assisted academic progress reports so parents can effortless stay on top of kids middle/high school academics.https://www.gpa.coach- A family economy app where parents set the rules, kids earn credits for chores and good behavior and kids redeem credits for screen time, money, and other benefits.https://www.kredz.app- AI first fun mobile media editor your parents could use.https://www.mix.photos/

reply

gofreddygo
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I track my learning and schedule repetitions in google sheets. But Google sheets sucks on the phone. So I built a dumb frontend reading off of my (public) google sheet which just has 4 columns for links, title, dates and wait times, plus a formula. Webapp pulls the sheet as csv, renders as color coded lists and a couple charts. Chart shows what's due this week on a 15 week timeline. This is the simplest luddite version I could come up with. I don't have a way to share this with others except sharing the source. Not introducing complexity from auth, storage, managing updates from the app, etc.

reply

madebywelch
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on multi agent orchestration

https://github.com/madebywelch/mau

reply

philajan
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a story time utility.(
https://bedtimebookhelper.com/
)

You build up a library from your physical books by scanning them in or discover OpenLibrary books to read in app. Then as you mark books in your library as read, it starts building a rotation and recommending books you haven’t read recently. I’ve been using this nightly to track my son’s 1000 books before kindergarten for the last couple of months.Currently, I’m working to get the app out on Google Play and adding multiple story time attendee support.

reply

metanoia_
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I continue to write. Unsure the end goal but in my recent dispatch I learned to get out of my way, stop intellectualizing life and let it be.

https://www.metanoia-research.com/

reply

mikestorrent
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

Read your most recent piece and I like it. Beat generation sort of feel, extemporaneous, haunting in a good way. Keep writing even if only a handful of people read it.

reply

metanoia_
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you, much appreciated!

reply

nodivbyzero
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

A small, generic Go library for retrying fallible operations with exponential backoff and pluggable jitter strategies.

https://github.com/nodivbyzero/try

reply

_fizz_buzz_
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I have been experimenting on using AI for hardware development. I showed some experiments on HN a couple of weeks ago (
https://news.ycombinator.com/item?id=47801255
). I am now trying to make my approach a little bit more comprehensive and structured, instead of several disjoint MCP servers, a single platform that connects lab instruments to AI assistants: 
https://teasel.tools/

As a demo, I repaired an old Philips PM5190 function generator (about 40 years old) and connected it to Claude Code. Lots of fun. Going to post a follow up video the next couple of days.

reply

mfkhalil
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

We're working on Webhound - budget controlled long-running deep research. You set a budget and Webhound will use that much in compute/LLM tokens to research your prompt, with built in verification cycles and optional added verification budget. Every claim is cited with evidence and a direct link to the tool calls that produced the claim

The goal is to build a deep research product for actual researchers, since we believe that it is an extremely powerful product that is still nascent but has enormous potential - which we've already seen with some early users.https://webhound.ai

reply

rishikeshs
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on StackStats: 
https://stackstats.app
 a better analytics app for Substack Writers. It run 100% locally with no backend or subscription.

reply

mlhpdx
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a ground-up implementation of RADIUS with everything running on stateless compute. It’s a beast with many problems to solve but I have EAP-TLS, TTLS and PEAP all working. I’d love to connect with folks interested in this kind of thing.

reply

pabs3
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

Why RADIUS and not DIAMETER, the successor?

reply

mlhpdx
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I didn’t see the successor in the field much, RADIUS seems entrenched. If they are similar enough I may build both but this was the place to start.

reply

MaKey
 
23 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What motivated you to start this and which language did you choose?

reply

mlhpdx
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Past trauma motivated it.

I was responsible for multiple RADIUS services used by millions of people every day. The existing software is slow to build with, difficult to scale and expensive. I couldn't let it go.Step one was building the platform to run it on and make it sustainable as a business. Step two is implementing protocols like RADIUS that lack a separated compute/storage model but should really have one.I chose C# because I know it, and build native single-file executables using AoT.

reply

protocolture
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sort of uncurious about your implementation, but very curious regarding your trauma. I have found a lot of the OSS options for RADIUS suck in specific ways. Never had to scale it however.

reply

mlhpdx
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The two are linked. Need to change the configuration of a fleet? That's going to be restarting every instance of the process. Update an extension model? Same. Load balance? You'll need one that understand RADIUS or clients will suffer because of incorrect session affinity. Client with dramatically different loads? Better put them on different clusters. Somebody had a power outage? Better have 10x capacity on hot standby for the load.

And on and on.A stateless compute model with separation between the packet handling and the authentication logic solves pretty-much all of it.

reply

MaKey
 
22 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

So you are looking to offer a managed RADIUS server once you've finished building the software?

reply

mlhpdx
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Maybe. I'm thinking about options but haven't decided on anything yet.

reply

saladsmander
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on OrcaMarka, a tool designed to simplify reading web content on e-paper devices.

I’ve split the experience into two parts: a mobile-friendly app athttps://app.orcamarka.comfor bookmarking websites, text snippets, or images into a pure text format, and a reader part athttps://m.orcamarka.comoptimized specifically for the limited browsers on devices like the Kindle (the site will automatically redirect you to app if it detects a more capable browser). To bypass the pain of typing URLs on E-ink, the reader part displays a QR code that you scan with the app to instantly sync and load your text.I’ve been using this personally for a month and it has significantly shifted my long-form reading from my phone to my Kindle. Since it’s a web app, there’s no installation required and it's completely free.I’ve tried to design it to be intuitive enough to use without instructions, but I’m looking for beta testers to try it out and let me know where I can improve the workflow!

reply

ycomb-n
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I built BookDMV (
https://bookdmv.app
), it watches DMV offices for open appointments and either alerts you or books one automatically.

reply

borealbuilder
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a free lightweight solution to auditing recurring subscriptions from a pasted bank/cc statement, born from my best friends financial illiteracy. All done in browser, no account sign-ups, no data transmitted to a server, and packed into a single HTML file so that the privacy and ethics can be viewed and verified.

Currently it covers 6 regions, 250+ subscription services, across 30+ categories, recognizing 850+ billing name patterns. It even has built in smart alerts for different services and region specific considerations. (FTC's Adobe settlement, Hola VPN Danger, UK Price Hike Exit Rights, Cloud Act Warning, etc)It adds up monthly spend/annual spend. Identifies alternative saving opportunities/more ethical options.I have plans to add additional regions but that will take extra research to understand the realities of those markets and the providers within them. I also don't speak any other languages, so this may also be a bit of a hurdle.https://findrecurring.com/

reply

hedayet
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

GBP (Google Business Profile) is getting extremely popular for B2C business marketing - e.g., 
https://trends.google.com/trends/explore?date=today%205-y&q=...

We just received the API usage approval from Google, and I'm integrating GBP tohttps://pinpost.iothis week (our reliability first social media management tool)

reply

englishspot
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I got most of my must-haves for my car maintenance tracking web app out of the way. it already does everything I wanted all the paid alternatives to do, even has SSO integration (only Google OAuth for now). the other must-haves, I do actually need, but I think they can wait. notifications, and an export mechanism for my history (including file attachments). for now I think I'll focus on the other things I've been putting off, like upgrading my car's audio.

reply

christianh
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building an AI Ski coach. Upload a video clip of your skiing, get feedback: 
https://poser.pro

I’d love any feedback!It’s a lot of fun and ultimate nerdery for me :) I’m a ski instructor through the Austrian and Danish ski school systems, I studied physics, and I’ve been a developer the last 15 years.

reply

piinbinary
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been going through Nora Sandler's Writing a C Compiler book and writing a compiler in Python. I'm excited to start the chapters on optimization - those seem like the most fun algorithm problems.

I recommend the book. It certainly isn't easy (maybe 3x harder than Crafting Interpreters), but I've learned a ton (eg how to deal with operations on different sizes of types, or the trick of using pseudoregisters to avoid having to figure out registers up front).https://github.com/jmikkola/writing-a-c-compiler-python

reply

eniac111
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Bor - Linux Desktop policy management ( 
https://getbor.dev/
 ).

In short, it unifies the configuration of different desktop components as policies ( dconf, Kconfig, polkit, Chrome, Firefox, etc.. . It's LGPL.You can check my slides for the upcoming Tuxconf conference this Friday:https://getbor.dev/publications/tuxcon2026/Cheers!
Blago :)

reply

tomasz-tomczyk
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

It's been three months now of building Crit - 
https://crit.md
 - local first, open source tool for reviewing markdown and code output from your favourite AI agent.

It's inspired by GitHub PR review workflow, only with quick iterations and local.It's been great! I found some dedicated users, dogfooding it every day with Claude and starting to get more contributions from the little community. We just got accepted into Homebrew core which was my target.I'm expanding the team features now as I've got a few users keen to get the sharing service deployed in their private networks!

reply

thedangler
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

Trying launch my Clover/Website builder integration.

Launching a niche RSVP systemA Menu builderA context/domain aware private message service.

reply

aliasxneo
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Currently working on `imgsrv` which is basically a container registry but it holds disk images. Enforces versioning, allows attaching multiple formats for a single release, prioritizes immutability, etc. Intended to build fully automated image release pipelines. I use a PXE setup for my homelab, so having a common place to manage image release lifecycle is helpful.

Right now I intend to make it compatible with Incus as a remote. So it's just a matter of adding it as remote and then you can consume all of your versioned images.https://github.com/meigma/imgsrv

reply

benldrmn
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Isola (
https://github.com/isola-run/isola
), a passion project of mine. It allows you to easily create and control sandboxes for executing untrusted code on any Kubernetes cluster (one helm install). To support some features I wanted (like on demand snapshotting of specific containers' filesystem in a sandbox pod or limiting egress rate from the sandbox I am working on now) I contributed some changes to gVisor. Happy to chat about the design and implementation of such a project if anyone interested!

reply

pdyc
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

- Tool for organizing files, pasted data, and prompts into markdown snippets you can copy into different AI chats.

- Calculator that gives tg/s and vram required based on model params and ddr settings.- Auto create dashboard from csv/json files or apis Easyanalytica.com- snippet viewer for html/react that allows annotation and sharing based on url fragments

reply

Smaug123
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Main project is a deterministic .NET runtime (
https://github.com/Smaug123/WoofWare.PawPrint
). Today I upgraded it to net10, which has naturally caused dozens of regressions which Claude is beavering away at.

Side project is my own agent harness,https://github.com/Smaug123/writ, which is being built sandbox-first and with Nix as a first-class citizen. Obviously everyone has to write their own agent harness as a rite of passage.

reply

technotony
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Agent engineer master. Currently it's a skill builder to generate custom production grade skills for agents but my goal is to build it into a system that non engineers can use to build and deploy agents with just prompting. 
https://agentengineermaster.com/

reply

vinhnx
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been building VT Code (
https://github.com/vinhnx/vtcode
), an open-source coding agent with code understanding and robust shell safety. Supports multiple LLM providers with automatic failover and efficient context management. Written in Rust.

reply

lfcipriani
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building 
https://github.com/lfcipriani/obsidian-radar
, an Obsidian plugin that provides a radar view to your notes so you can map your focus visualy.

reply

hxii
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

This actually looks kinda cool! Not sure this would be something that I'd use (as I am really trying to not rely on too many plugins), but it makes me happy to see cool new ways of visualizing data in Obsidian.

reply

trusche
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

As a data-obsessed golfer trying to get to single digits, I need a tracking app that picks up where Arccos leaves off. So I'm building one: 
https://shortgamewiz.com
 (still a bit WIP).

After a few rounds of using it, I already know a few things I didn't before: I suck at right-to-left breaking putts, I baby uphill putts too much, and getting out of bunkers consistently is not good enough if I can't sink the occasional save. So I know what to practice now.

reply

JKCalhoun
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Closing up work on my modular, hobbyist, analog computer. (Finishing up the manual—the hardware is already a wrap).

Something I can finally enjoy: just playing with it. I tediously wired up a pair of pendulum simulations to drive an XY oscilloscope—got a nice Lissajous curve.But now I want to double it to four pendulums. Each axis (still just X and Y) to be driven by the sum of a pair of pendulums. With them out of phase, the curves appear to sometimes collapse but then suddenly explode again…(Love to eventually hook it up to an actual plotter.)

reply

tootyskooty
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Repple (
https://repple.sh
)! It's a modern spaced repetition x incremental reading/PDF library app with a few (tasteful!) QOL AI features.

I've been using Anki for 10+ years and love it but always wanted something with a cleaner UX and a reader view. The recent Anki ownership change pushed me to finally make something, and it's seeing some traction :)Right now I'm focusing on getting the reading and note-taking view to be nice. I used to use Polar Bookshelf (RIP) but that went away, trying to make something better.The flashcard side also has a REST API btw!

reply

germinalphrase
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building a small map application that allows me/friends/family to explore data overlays about morel mushrooms phenology and habitat (ground temp/moisture/terrain/aspect/tree species/etc) in our area. There’s some lightweight forecasting and timing models to help guess at near-term fruiting. I had a big push about a mouth ago to tighten things up, and initial experiences in the field this year have been very promising.

I’ll keep chipping away at it this year, and probably expand beyond morels to other seasonal natural phenomena that my people enjoy like smelt/salmon run, wildflower blooms, etc.

reply

jonnycoder
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

I had a similar idea. I picked 10 lbs of morels last year, first time picking. It was a recent burn area from 8 months prior. I was just back out to the same area and there are no morels, but lots of small orange cap looking mushrooms. chatGPT pro said first year is the best and then it drops off on the second year. I might try a much higher elevation spot in a week or two, but it really sucks. Last year I was finding morels on southeast facing slopes. I'm sure north slopes produced later on as I saw people coming off the hill when I drove by.

reply

germinalphrase
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

North-facing (in the US) tends to produce earlier due to the increased warmth with south facing producing mid to late season. Fruiting has been suppressed by me due to lack of rain. Best of luck!

My maps aren’t in public release, but reach out if you want to give it a look.

reply

puzzydunlop
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Building 
https://www.townhall-tracker.ca
 to help me and other Canadians keep tabs on their city council.

I moved to a new city 4 years ago and didn't even realize a municipal election was happening until a councillor knocked on my door.I am building townhall-tracker to prevent this and shape the decisions that most affect my day-to-day

reply

darkhorse13
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an open-source Typeform-alternative: 
https://forms.md
. Also trying to monetize it via a WordPress plugin: 
https://wp.forms.md

reply

ser0
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I made 
https://poemd.dev/
 as an online markdown scratchpad that supports GitHub Flavoured Markdown and stores all data in the URL. This means there are no accounts to work with and everything is basically stored in bookmarks if you choose to.

The persistence model makes documents somewhat sharable, but I do find Open Graph previews to be mixed. In Messenger it renders the whole URL, which is quite long due to encoding, and that kills the conversation view.

reply

boricj
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Still working on ghidra-delinker-extension, trying to wrap up the OMF object file exporter at the moment. Then I'd like to implement generation of debugging symbols (at least DWARF and CodeView, maybe STABS and CTF), although lately I've received a PR for PowerPC and an issue for delinking shared objects.

I'm also thinking about writing the Necronomicon of delinking at some point. The extension keeps spreading by word of mouth and there's only so much UX improvements I can do, for something that requires throwing everything you've learned in CS 101 into the trashcan before you can "get" it.

reply

bbx
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building a small video utility app, built on top of ffmpeg. It allows you to convert from/to different formats, split a video into clips, combine videos into a single one, take screenshots…

reply

j77dw
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a AI app to replace Claude Desktop and Mobile for personal use.

The main goals are to own my data (memories, artifacts, chats), be able to switch AI providers at any point (if one is down or I want to try a new model), have the same experience between desktop and mobile especially when it comes to working remotely on code.A bigger vision is to offer everyone a alternative to Claude and ChatGPT they can own just like OpenClaw but with a great app experience.I hope to have the first beta published by the end of next week.https://github.com/bgrgicak/Desk

reply

jtbetz22
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm continuing to focus on ways to set strong code quality guardrails in an era where most code is not handwritten.

The result ishttp://getcaliper.dev.It has a number of mechanisms that help substantially:1. It can extract deterministic quality checks from your CLAUDE.md text; these checks then get executed after every agent turn.2. It performs a lightweight ai-powered review at every commit; feedback goes directly to the agent, which can then make corrections.3. It performs a more 'traditional' deep AI review at merge, or on-demand.Free to use, just bring your own API key. Any and all feedback is welcome!

reply

paulhallett
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a tiny terminal config / dotfiles / tool installation manager so I can keep everything in sync between my machines. Also includes profiles so I can tailor each machine how I see fit. 
https://github.com/phalt/pauldot

It’s intended just me for and follows a philosophy around hyper personal software that I’ve been developing:https://paulwrites.software/articles/hyps/

reply

korrupt
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

still working on wellbody - guided body health. most people know that they need to integrate fitness, nutrition, mindfulness, and recovery into their goals but don't know what to do or its difficult to organize all these topics into one system. that what wellbody does - organizes these topics into a unified system and refines it into just 3 daily actions.

my biggest struggle is distribution but I started working more on getting better a social media content creation. you can check us out on TikTok, YouTube, or insta: wellbodyapp

reply

saltwatercowboy
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Slapping together an image dithering toolkit to help with album cover stylization. Partly making sure I can replicate it down the line... but also finding an aesthetic, non-commercial motivation I thought I'd forgotten at work.

Some finished covers (https://saltwatercowboy.github.io/albedo/pages/en-10-05-26.h...). Next up pixel sorting.

reply

lum1104
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on Understand-Anything, trying to use AI to teach you how to understand something. The problem for me, as a beginner in lots of aspect, is do not know what question to ask to AI in a area that I am not familiar with.

https://understand-anything.com/

reply

matheusmoreira
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on my language. Recently implemented shapes for objects, like in Self and V8. Reviewing and polishing up the code before publication.

Also working on a handheld computer project. Did improvised thumb typing tests with paper and a stack of notebooks to determine my typing area. Next step is ordering some switches to see what they feel like.

reply

nilirl
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I finished writing this book 2 weeks ago.

Copywriting after AIhttps://www.nair.sh/books/copywriting-after-aiIt's 88 pages of me describing my mental models for marketing, those which I think still hold true even after the introduction of AI.

reply

djeastm
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.triviascroll.com

I wanted to make it easier to quickly see/study trending articles on Wikipedia because they tend to make good topics to know before going to trivia night.I've had the domain for awhile, but just made the app recently on a whim.I use Wikimedia's api to get the trending articles, curate them a bit, add some annotations to provide some context, then push to deploy the static site.

reply

chhs
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on JRECC, a Java remotely executing caching compiler.

It's designed to integrate with Maven projects, to bring in the benefits of tools like Gradle and Bazel, where local and remote builds and tests share the same cache, and builds and tests are distributed over many machines. Cache hits greatly speed up large project builds, while also making it more reliable, since you're not potentially getting flaky test failures in your otherwise identical builds.https://jrecc.net

reply

bert2002
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

The last couple weeks have been working on a parking spot app for Taipei and New Taipei. Finding a available spot, especially during weekends is very difficult. There are some apps, but only in Mandarin, so I did a English version.

If you are in the area, try it outhttps://taipeiparking.com/- Android app and web app.

reply

ethansaso
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a community-oriented platform for maintaining morphological descriptions of organisms + guides to identify them based off a shared vocabulary.

Been working on it on & off for a couple years, usually taking breaks between refactoring stupid decisions.https://klados.bio/Prod site is pretty behind dev branch, basically abandoned normal CI / repo hygiene for the moment

reply

mdxmaker
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on a md file eidtor for average users to use, by click buttons like MS word.

https://hellomdx.com/- Built with Tauri — installer is small and start-up is
 near-instant on all three OSes.
- No accounts, no telemetry, no MDX server in the loop. Sync goes through
 whatever cloud folder you already have (iCloud / Drive / Dropbox / a plain
 directory).
- Tab-to-accept ghost-writing is bring-your-own-key- Exports to PDF, HTML, DOCX. Tables, math, diagrams, code blocks all live
 behind toolbar buttons — no syntax to memorise.Hope to have some people like it and use it.

reply

alok-g
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

Any plans to support mobile as well? I'm lookimg to replace OmniNotes on Android.

reply

mdxmaker
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

good idea, i am thinking about it, but i guess it will be not that rich in formatting like the desktop app, the architecture design here using "vault" is a 'problem' for extend to mobile, maybe a lightweight re-designed version :-)

reply

manoji
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on trentdb . An in process single node database query engine inspired heavily by duckdb . Its primarily for me to understand databases in depth . Its completely written by codex and in java . Why Java? Its the language I am most familiar with . I just finished adding support for running all TPC-H queries.

reply

devrob
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

The other day I got into some pretty weird territory with Claude, trying to map out what an immortal ASCII cat would look like. Basically an autonomous Tamagotchi.

The idea was to create a quine that runs forever on something like Akash network with its own crypto treasury to support and pay it's bills and try to replicate. It would then talk to an LLM for support and actions on what to do to stay alive.It got pretty out there. Stored some of the ideas here.https://github.com/aquaflamingo/catfi

reply

division_by_0
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

A correlation network viz (using Cytoscape.js) of this S&P 500 and NASDAQ-100 correlation matrix (built with Svelte):

https://cybernetic.dev/matrix

reply

bormaj
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

Pretty neat suite of visuals there! What's the helix intended to represent?

reply

division_by_0
 
23 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thank you, I appreciate it. The helix simply renders candlestick data (OHLC) in 3D, with volume encoded in logaritmically scaled candle thickness. There's more info on the about page of the experiment: 
https://cybernetic.dev/helix/about

reply

simonpure
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a pure Clojure implementation of WebRTC Data Channels (SCTP over DTLS over UDP). The library provides a minimal, dependency-free (except for Clojure itself) way to establish peer-to-peer data channels on the JVM.

I've always wanted this and have used it to experiment with Gemini's cloud agent Google Jules.https://github.com/alpeware/datachannel-clj

reply

kylecazar
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool project. I'd be interested to hear your general impressions of Jules (as the somewhat forgotten agent).

reply

simonpure
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks! I've noticed a big jump when they switched to Gemini 3.1 Pro and it really became useful. I like that I can use it from my phone too. It took a bit of trial and error but I came up with a good ralph loop between GitHub Actions and Google Jules using the Jules API. So basically I have Jules extend its TODO.md with the next set of tasks and open a PR then run a GitHub Action with a few checks, auto-merge, and then call back into Jules to kick off the next cycle if there are still open tasks. It then mostly just runs and occasionally gets hang up on some questions that I then answer on my phone mostly just telling it to make a judgement call and keep the build green. You can check out the prompt, action, and past PRs for examples ex. Jules prompt is here: 
https://github.com/alpeware/datachannel-clj/blob/main/prompt...

reply

xeonax
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm porting my unity game to web using copilot. Is fun. I can iterate so fast. 
https://github.com/XEonAX/DriftsInSpace/tree/main/client

reply

matteohorvath
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on mesh (
https://growmesh.io
)
I started working on the topic of human development two years ago and I dived into the topic of how humans have been trained, manipulated, educated or brainwashed. 
My central idea which I am investigating is that whenever a person is interacting a highly tuneable ML model such as the X/Fb/TikTok feed or chat interfaces with LLMS, does the thinking and development of the human happens more times or less due to the new experience.

reply

rajeshvar
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a local first task and note manager with AI integration, both a TUI (mac, linux, windows) and iOS app.

https://vistacker.com- allows disconnected operation, auto sync across multiple machines with optional encryption so the service can’t see your data.I'd love to get some feedback (have a few friends trying it out).

reply

arugau
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Nothing fancy, I want to design a way to compact A.I context during runtime, using R.P.I semantics (research, plan, implement)

I know some Rust, was going about it with clap, but no one I know cares about Rust so I've switched to Golang with spf13 Cobra cliHarness is pretty cool, but I'm still a quite noob gopher, so I'm taking the chance to learn the ins and outs of Go...No A.I touches my code lol, else I would learn jack shit

reply

perfmode
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

if you’re not too locked into it (you’re not if you have CC), i’d recommend you check out urfave/cli.

reply

chtefi
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://kapturekafka.dev
, a desktop app for Kafka protocol inspection. Think Wireshark or Fiddler, but native for Kafka.

Useful to debug local Kafka apps against any cluster, intercepts the traffic, decodes the protocol. You see interesting (and weird) things when you look at the protocol. Still early, though already useful for local debugging when you know what you want.

reply

KronisLV
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

A small launcher for Claude Code, to make switching between different providers and configurations easier:

https://ccode.kronis.dev/For example, if I downgrade from Max to Pro I'd still be able to use the subscription, but also run sessions with other models (less expensive/local) as desired:ccode init-config # initializes a new config file for me to set everything up
 ccode edit-config # opens it in my editor so I can change, can also include editor as argument e.g. vim
 
 ccode # launches whatever my default profile is
 ccode --deepseek # Using their API key, they have a discount this month
 ccode --openrouter # Whatever OpenRouter model I have configured in the config file
 ccode --openrouter-preset # Also supports OpenRouter presets e.g. if I don't want to use quantized models
 ccode --deepseek --control # launches a Remote Control session, shows up in web/desktop app as a regular session
 ccode --deepseek --auto # overrides the default permissions, --yolo also works
 
 ... (and so on, there's more examples on the website)Source available, pre-built binaries on itch.io, pay-what-you-want with a minimum price of 0 USD, probably get it for free first if interested in taking a look.I finally got around to signing app for Mac, which is what this post originally was about:https://news.ycombinator.com/item?id=48075366(the new versions will be out soon)Also thinking that I might make it an Anthropic API --> OpenAI API proxy that allows talking to providers that don't support the Anthropic API directly, alongside allowing switching models dynamically during a session (Claude Code wouldn't even have to know about it, it'd just send requests to a local endpoint and the proxy would do the rest).Early on, but Go is lovely to work with, mdBook is great for getting a site off the ground and I'm really surprised that more people don't use Itch.io for distributing software (or the pay-what-you-want model in general), it's dead simple!

reply

dainiusse
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://sauna-assistant.com
 - sauna rituals for home sauna owners

reply

Seb-C
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on assembling a full-stack framework/template that aims at building performant and quality web apps very quickly.

It's going to be 100% statically type-safe across the stack, SQL first for the DB layer(s), and with a minimal amount of boilerplate (just enough for a clean architecture without magic).

reply

dhuan_
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been working on two opensource tools:

https://dhuan.github.io/mock/latest/examples.htmlCommand line utility that lets you build APIs with just one command.https://github.com/dhuan/dopJSON/YAML manipulation with AWK style approach.

reply

slotix
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

We are working on DBConvert Streams:

https://streams.dbconvert.comA self-hosted database IDE with built-in migration, CDC, and DuckDB-powered federated SQL.Mostly trying to remove the annoying gap between "I can inspect this database" and "I can safely move/sync this data somewhere else".Current focus: resumable large loads and cleaner initial-load-to-CDC handoff for Postgres/MySQL.

reply

behaviors
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

A model framework for an in house suite of models.

From dataset harvest, to training intricacies on CUDA/ROCm to fun HIP kernels. Full circle to inference testing, building it around consumer hardware(the challenge). Using this as a "how it works" deep dive, allowing me to learn more about the how, more than endless papers will. It's a MoE and I'm slowly running a human loop, research, build, correct, research.

reply

insapio
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

muster and muster-pattern-library. (
https://github.com/azide0x37/muster
)

an agentic coding scaffold/framework you can reference when building out your next random raspi project. prefer to build around systemd units first; make an idempotent installer script, then put as little as possible custom coding around that.`impl muster` comes down to: /build out this tool wiring together `patterns` like: C3.dropfolder-trigger; R2.device-binding; C4.lazy-resource-gateor composite patterns like:T2R4.device-triggered-conveyor
"Bind a physical device event to a bounded ingest job that waits for hot-storage capacity, proves cold-storage capability, stages local work, and hands output to a hot/cold conveyor."I need to back up a couple hundred DVDs, so with muster I get out:dvd-ingester
T2R4.device-triggered-conveyorArchitecture
DVD media becomes ready
 -> udev rule adds SYSTEMD_WANTS=dvd-rip@%k.service
 -> systemd runs /opt/dvd-ingester/current/bin/dvd-rip-one /dev/%I --apply
 -> dvd-rip-one proves DEST_DIR and waits for HOT_DIR capacity
 -> completed rip moves to HOT_DIR/<run-id>
 -> dvd-publish-one.timer drains HOT_DIR to DEST_DIR
 -> publish writes DEST_DIR/.incoming-<run-id> and atomically renames final outputPipelined; ejects after rip completed. Monitors local disk capacity, retries after NAS comes back online; resumes after random reboot; etc.

reply

abi
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/abi/lilo
 I’m working on Lilo, a Telegram AI agent that can remember things, store files, track your TODOs, manage your calendar, conduct research, build apps, send you reminders and monitor things for you.

I’ve found it super useful in my personal life and is pretty much my #1 app.

reply

userium
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.evcourse.com/
 smart EV charging help

reply

kiproping
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on a research institute for East Africa, 
https://maiyoinstitute.org/
. I want to tackle the dire lack of environmental data, by using 1. low cost hardware 2. Artificial Intelligence 3. Long term horizon. The problem set is huge, but I am focusing on low cost sensors for Air and Water data collection plus bioacoustics for now.

reply

maxpert
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on Marmot 
https://github.com/maxpert/marmot
 recently added support for vector index. My local benchmarks show pretty decent QPS with less than GB of RSS on DBpedia dataset.

Interesting part is that I started off implementing a research paper for indexing and performance was not good enough. I ended up tuning things up for my own use-case and ended up with good enough replicatable RAG store.

reply

nicoinstrument
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm learning about inference by running vLLM on a k8s cluster (EKS), building a gateway to keep a <2s TTFT SLO.

Most recent ha-ha moment: I kept wondering if it was normal that my cluster was only able to process 4 requests per second per vLLM engine (just seemed really low to me).I realized a better metric is in-flight requests... Each engine is processing 70 requests at any given time, streaming tokens for over 30s.Code:https://github.com/Nicolas-Richard/vllm-on-eks

reply

iugtmkbdfil834
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

Deeper dives into those uncover interesting limitations that don't seem to be documented anywhere. On the other hand, it is through those reverse shibboleths that I am now able to tell that my boss's boss has no idea what he is talking about llm-wise.

reply

niraj-agarwal
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Made a stocks dashboard using percentile ranks and "lens" for discovering stocks using 2D plots with roughly orthogonal compound metrics.

https://www.stocksdashboards.comGoing to get back into self-managed IRA...this time better-informed :-)

reply

davidcann
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Buildermark calculates how much of your code is written by agents. Open source, local, and cross-platform (written in Go).

https://buildermark.dev

reply

ajkajkajk
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on bomberman in ClojureScript, using no libraries, and making sure I write every line myself, it feels good to go slowly for a change having used a lot of LLMs in the past year.

reply

rsalus
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/lvlup-sw/exarchos

It's an SDLC workflow harness for agents. Instead of using skills to encode my typical workflows (e.g., create PRD, then create plan using TDD, then dispatch subagents, etc) I've built a concurrent event-sourced process manager to handle it.

reply

ge96
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Another self navigating robot. Really need to nail down IMUs and mixing these 8x8 ToF ranging sensors with cameras to get better depth. FPGAs are on my list too, I bought an orange crab like 4 years ago and still haven't used it.

Trying to use local LLMs/agents but I still don't use LLMs much other than for research.Personal finance BS, I need to get out of debt so I always write code about that, the trick is to actually follow it.Medical SaaS for money... still building it out, recently switched over to GCP.

reply

abhisek
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Just implemented Landlock + seccomp notify based sandbox in PMG. A tool to protect cli package managers against malicious packages. There were quite a few quirks involved due to Go routines when it comes to handling messages from the kernel.

https://github.com/safedep/pmg

reply

depthfirst
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

working on contextflo 
https://contextflo.com
 - building for companies with 1 person data teams who just want their data to be accessible via claude/chatgpt/cursor to everyone, no need to setup a complex BI product when you just want to run adhoc queries on your data. supports postgres, snowflake, clickhouse, bigquery, amplitude.

some interesting use cases are coming up where people want to query across different data sources (postgres + GA4) via chat. Feel free to reach out if you want to try it out.

reply

rebolek
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on Recoil, memory safe, compiled static language (yeah, I know, everybody’s doing it) with Rebol syntax and built-in candies like parsing, finite state machine and rich syntax (that’s given, because of Rebol).

It’s nice to see how well-thought language design can pay off years later, with lower token usage. From entropy POV, Rebol syntax is certainly close to optimal state.https://codeberg.org/rebolek/recoil

reply

bnmik
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on Desiderata (
https://github.com/github-of-NMI/Desiderata
).

An LLM benchmark for open-weight models only, with secret questions.The questions are asked multiple times to calculate a consistency score.The results are available in JSON, containing the hash of the question with the number of correct and incorrect answers, the number of unique answers, and the number of times no answer is given. (Uses \boxed{})

reply

asparagui
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

https://brettkoonce.github.io/lean4-mlir/blueprint/

https://github.com/brettkoonce/lean4-mlirI (w/ Claude) have built a framework for writing neural networks in Lean 4 that compiles to StableHLO MLIR and runs on GPU via IREE.

reply

felixding
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

https://aquablue.app
 - Business software without developers

https://kintoun.ai- Document translator that preserves formatting and layoutshttps://ricatutor.com- AI language tutor for YouTube

reply

lylejantzi3rd
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm working on GPS tools to help support my current contract. I've found there are no good tools for tracing a route on a map and having a mobile device think it's traveling that route. I'm not just talking GPS coordinates, but speed, direction, motion detection, precise timing between waypoints, being able to play these trips forward and backward, step by step, etc. I'm talking time-travel debugging for GPS applications.

It's early days. I'm not even sure it's possible.

reply

marking-time
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

It seems doable and cool to me. Glad your working on it!

nettirw yb namuh

reply

meetingthrower
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

https://planoptica.com/

Employee benefit plan analytics. Had a huge dataset long ago as a consultant to the industry and finally vibecoded up a decent frontend. All public data but if you know the data there is a bunch of analytics you can do. Just about to launch and do some marketing in a few weeks, so saw this and thought I'd throw it in!

reply

nucleas
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://gigspool.com

- Building a platform where talented people can list the services and skills they're experienced in. Clients can book paid sessions with them directly through the platform, and once a session is booked, they both meet online to discuss, collaborate, or get advice based on expertise.

reply

alexander2002
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

Like upwork consultations?

reply

nucleas
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Similar idea, but more focused, no job postings, no proposals, no contracts. Just find an expert, book a paid session, and meet.

reply

ljlolel
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I made an end to end encrypted provably private LLM Router 
https://trustedrouter.com/

Been using that to power a Mac mini alternative I’ve been makinghttps://jperla.com/blog/quill-one

reply

futurecat
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Better GitHub insights: 
https://temporiohq.com
 - still new and there’s a lot of question about how to adapt to the age of accelerated software engineering.

My art with pen plotters. Recently released a new series of brush plots. Very inspired by Soulages:https://harmonique.one/collections/brush-plots

reply

vibebased
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I vibe-produced a website for an (earnest?) pastiche of Final Fantasy games (i.e., for a game that does not, and probably never will, exist). I noticed that Nano Banana could generate reasonable facsimiles of Square Enix's promotional render style and ran with it. Next up: faking some gameplay or a few shots from an FMV-style cutscene.

https://findfantasyxviii.com

reply

dt3ft
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://fdeploy.com

fDeploy is a self-hosted Windows deployment automation tool — a lightweight, on-prem alternative to Octopus Deploy. It consists of a Server (Windows service with a Web UI) that orchestrates releases, and Agents installed on target windows machines that execute deployment steps (IIS sites, file copies, scripts, etc.) across environments.

reply

a34729t
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A civilization clone, but going way deeper than is reasonable (inspired by dwarf fortress). I'm currently building the geophysics simulation that will allow for realistic terrain generation, powered by actual mantle convection and plate tectonics. Once this is finished, then an actual per-cell atmospheric and oceanic model. This should keep me entertained for at least a year, at which point I can start working on the actual gameplay part of things.

reply

Andys
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://tapitalee.com

- Deploy containerized apps to your own AWS account with minimal config!
 - CLI tool with instant console sessions
 - Set up SQL/Redis instantly with Heroku-like add-ons.
 - For enterprise: Autoscaling, preview apps, audit trail, release approvals.

reply

beanback
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on Beanback, my side project SaaS app for ‘effortless digital loyalty for cafes’.

It replaces paper stamp cards with Apple Wallet passes (Google Wallet coming soon) without the need for customers to download an app or signup. It’s still very work-in-progress (forgive the landing page) but I’m enjoying using Ruby on Rails. Please let me know your thoughts!https://beanback.space/

reply

turblety
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building yet another terminal [1][2] for macOS and Linux. I've been unsatisfied with the window management of iterm2 and other terminals, my one acts a bit more like Chrome with projects at the top level.

It also allows remote control. I don't like AI harnesses (Claude / OpenAI) having remote control inside, it feels like it should be at the terminal level, not the cli.It also allows commands at the terminal level. So if you use multiple ai cli's you don't only need to write the command once, then use cmd+l to inject into any cli.I've put macros in too, that again can automate doing the same thing in a terminal.Anyway I'm sure this will just end up another terminal in a sea of already existing ones.1.https://github.com/markwylde/terminay2.https://terminay.com

reply

cgopalan
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

For occasions like birthdays or Christmas where people want to give you gifts, I have always wanted to ask them to make donations to charities of my choosing instead. So I built an app to enable this: 
http://donateyourgift.com/
 It is very simple but I didn't find anything quite singly-focused like it, so I built it just to scratch my own itch.

reply

sidhantdhar
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on building an audio drama studio, publishing audio dramas starting with the Mahabharata. As an Indian, I have always been fascinated with the concept of `Dharma` and the Mahabharata treats it as a very grey area morally. Having lots of fun rn :)

reply

brynet
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Making rent as an open source developer.

Shamelessly trying to attract new monthly sponsors and people willing to buy me the occasional pizza with my crap HTML skills.https://brynet.ca/wallofpizza.html

reply

theoutfield
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I started a new software defined automation project. I wanted something that I could just open a webpage and start writing code that could just be uploaded and ran instantly. I picked an ESP32-P4 for the first hardware. It’s MIT licensed and has a git repo that I put up this morning 
https://github.com/OpenPiLab/pilab-esp32-p4-plc

reply

Celeo
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

After having it on my TODO list for a long time, I've installed EndeavourOS on another m.2 drive on my desktop. With the advancements in gaming support on Linux over the last few years, over 80% of my daily tasks, work, and games are well-supported by Linux. I've been using Linux in VirtualBox or WSL for many years, but it's been a long time since I've ran Linux directly on hardware. I'm excited!

reply

mattkevan
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m building a UI design app similar to Figma or Sketch, but with a few differences:

1. Responsive artboards and flex-like layout engine2. Deep support for design tokens3. HTML/CSS previews and export4. Multiplayer AI and human collaboration. Agents can connect to documents and collaborate like any other user.Built in Swift and cross platform Mac, iPad and iPhone.I’m designing and building the UI and implementing the underlying features with Codex. So far it’s going surprisingly well.

reply

TeaVMFan
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a tool to let sfotware developers write well-formatted ebooks and printed novels: 
https://frequal.com/epublish/

Example book here:https://www.amazon.com/dp/B0GYCZJVGX

reply

cristyg0101
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Currently developing 
https://pelicantools.app
, a collection of tools to rework YouTube. Any YouTube video can be transcribed to an elegant text or a complete article.

If you're a creator, researcher or developer looking to reap the rewards of a video without consuming it fully, then it's helpful.Whole thing is up and running on vercel.It's a work in progress — would be great to get some input!

reply

helloakariq
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I am building Akariq which provides data eSIM data plans to 185+ countries and regions across the world. I am 2-3x cheaper than big brands in the same space. I also prefer local data routing i.e. I don't route traffic from US or EU to Hong Kong, they stay in your country / region.

http://akariq.com/en/

reply

selcuka
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

Just curious, I have no idea how eSIM reselling business works: How can you offer 2-3x cheaper prices? Is it because others have very high margins, or because you have a secret optimisation method?

reply

helloakariq
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Great question. Cheaper prices come from a mix of focus on customer value primarily. That includes making sure that the eSIM is high quality (low latency, data routing in the region) and also focusing on getting the best eSIM plan to the customer - transparency, better FUP etc. So there's an element of optimisation involved here.

reply

rahilb
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a small voice journaling app, hoping to ship in the next few days 
 
https://turquoisehexagon.co.uk/anima

TestFlight link, good for 10 users:https://testflight.apple.com/join/9VREtXzq

reply

ncruces
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Adding support for the threads/atomics proposal to my Wasm to Go transpiler:

https://github.com/ncruces/wasm2go

Since I started it a couple of months ago, it's been used by me to transpile SQLite to Go, and by some other folks to transpile other C, C++, Zig and even Perl libraries to Go.

reply

rowbin
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a tool that lets you author in WordPress as usual (own Docker container, full editor + plugins) but exports the site to static HTML for the public version, so PHP doesn't run in front of readers. Deploy targets are Cloudflare Pages, a Git remote, or statichost.eu. Solo, just launched, currently grinding through hardening. Called Stelae if you want to have a look.

reply

rowbin
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

Link for anyone curious: 
https://stelae.eu

reply

lonk11
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Building a custom feed for Bluesky which uses collaborative filtering over the likes data: 
https://foryou.club

How the algorithm works: it finds people who liked the same posts as you, and shows you what else they’ve liked recently.Launched the feed a little over a year ago and it has become the most liked feed.

reply

vincent_s
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on what I call a Software Delegate [0].

You delegate a task or GitHub issue to it and it uses AI coding agents and developer tools to write the code, run checks, read failures, fix problems, and iterate until the result is good, then comes back with a pull request. It does everything a human dev would do, fully automated.[0]https://www.vroni.com/

reply

rexma
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A language learning app called lexaway. Premise is people can learn like LLMs learned - word prediction. I use tatoeba, an online sentence pairing thing, and it's nice well it's worked for me. I hate the green bird fyi so it's free and open source.

https://apps.apple.com/us/app/lexaway/id6761870125

reply

mnorris
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m making a detective themed iOS-based visual novel with React Native.

Making the game engine was easy. Making the story consistent, believable, and interesting has been the biggest challenge for me.I’ve written a few bad novels but never any narrative games, so it’s been a good exercise for me.

reply

dabinat
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Just rolled out a big new update for my video cloud platform 
https://www.kollaborate.tv
 with a new player, side-by-side playback comparison and a big improvement in accessibility.

Currently we’re using AWS and Backblaze B2, but I’m formulating a plan to move to colocated servers. Not being billed per GB will open up a lot of new opportunities. Even at today’s server prices the math still adds up.

reply

aleda145
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

Is it egress or storage that's the main cost driver?

reply

dabinat
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Mostly storage. Customers upload large files and expect the original file to always be available.

reply

zhdc1
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Bought a TI dev board with c7x and c66 dsp cores. Have it doing PEQ and FIR room correction, along with tube amplifier emulation.

Will be trying to implement a virtual bass array next.

reply

karthikeyankc
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Dealing with some rough stuff in life so I'm involved in random stuff to distract myself. Moved my personal blog to Astro. I wanted to scratch and itch I had about self hosting my comments. So I built a lightweight node-based opensource comment system called discuss - 
https://github.com/karthikeyankc/discuss
.

reply

kilroy123
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm making a retro cable tv experience for YouTube:

https://channelsurfer.tv/

reply

lukasb
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Tidepools, a daily journaling / task management app (local-first, Mac/iOS/web) with a proactive AI coach. Mostly what the coach does is ask you questions. It can also suggest tasks. Right now I'm working on sandboxed plugins that the coach can modify, so the user can request behavior changes.

https://tidepools.ai

reply

0x6d61646f
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been making an android launcher, similar to the smart launcher but free and open source

one of the few apps not FOSS on my degoogled phone, thought it was time to fix that

reply

fomoz
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://vtxmacro.com
, a free and fully autonomous LLM trading platform. Basically have any model you want trade for you. Right now I support ~860 models across 16 providers (including OpenRouter), plus Local AI and OpenAI Compatible endpoints.

The bot settings (system prompt and user prompt, temperature, reasoning, etc.) are 100% transparent and customizable, and all users can view and copy anyone else's settings from the leaderboard. The goal is to build the best trading bots possible by seeing what works.You can run a bot on Gemini 4 31B with a free tier Google AI Studio account (I'm running 5 bots on it myself). Or just run Gemma 4 26B on your PC if you have the GPU for it. I'm running 5 on my 5090, so I'm trading with 10 bots total.The platform is connected to Hyperliquid and you can trace all the trades on the blockchain from the user's Analytics page (always public).The way it works is you set a loop interval (default 1 minute) and the model receives the candles, market stats, indicators, account balance, current positions and so on and decides Buy, Sell, or Hold and how many units.It's still experimental but I have already processed 1m+ prompts, 10k+ trades, and almost $1m in volume since January 2026. I have around 15 bots running right now, you can check their PnL on the leaderboard (public). I've made a lot of changes in the last few weeks so most recent either 24h or 7d results are the most relevant. The model you use is super important (Gemma 4 31B so far is the best value I found, better than Gemini 3 Flash and you can run it for free) and also the coin you choose is important too. Preferably, you want something that's trending. My friend's bot did well with ZEC and VVV this week.Right now I'm working on improving reliability (I bought a Japanese VPS to run my own HL node), and this weekend I moved the app from Render to my own DC VPS for 10x+ cheaper and 1000x more bandwidth (25 TB instead of 25 GB, seriously if you're using Render and want cheaper infra look into buying your own VPS).I'm also implementing CLI/MCP for OpenClaw support. And next is an automatic screener that will use LLMs to pick the most promising cryptos to trade (since I noticed this has a huge effect on PnL).If you have questions, let me know, the Trade page has my Telegram group link.

reply

kukkeliskuu
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

How well are these performing?

reply

jFriedensreich
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

A permission broker for deno + opencode fork that can run in deno instead of bun.

reply

oleg_antonyan
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

https://omnipackage.org
 - a tool that simplifies building RPM and DEB packages and managing repositories on S3

reply

forcedfakelaugh
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Pretty simple one to track my own club badminton scores and history 
https://www.elosmash.com/

Other clubs were interested so I made it multi users. Idk it works well for my club

reply

manu156e
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

Hi, very cool. We are actually building a similar app (
https://play.google.com/store/apps/details?id=com.arenaxgame...
 / 
https://arenaxgame.com
).
Our app is still in the early stages, we have yet to onboard venues. We are planning to have robust ranking system, exp / leveling system; and also allow users to book slots in venues to play / share games and discover other players,..
Let me know if you are interested in collaboration.

reply

Sagi21805
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on the Learnix operating system (
https://gitHub.com/sagi21805/LearnixOS
)
Mainly an educational project, to understand and teach about OS and Rust concepts (The OS is written in Rust)

https://www.learnix-os.com

reply

yuppiepuppie
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Still chugging along and curating 
https://hnarcade.com
 Submit your games!

reply

0xCE0
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Trying to get my product (desktop application) to the state of minimal sellable version (according to my quality level expectations). I tend to be perfectionist, thinking it is never even good enough. Hopefully I can show it to you/world in the summer, and hear what people think of it. But for now (or the past 5 years), I have nothing to show and tell.

reply

ateesdalejr
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

A couple of fun random projects:

-https://shirt.cash- Vibe code your t-shirt ideas and sell them.- This weekend was substack MCP (https://www.youtube.com/watch?v=jHARlcInLqU)new ideas welcome lol

reply

jonathang6k
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I've found it hard to keep up with movie and TV news (particularly when the new Backrooms film is coming out).

So, I built an agent to help remind me -- it's a subscription based service that sends you updates every morning, and stores your preferences so it can learn what you like.https://holly.garelick.net

reply

BagelsOverBread
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on an RSS reader (
https://github.com/megaflorasoftware/serial
), trying to see if there’s room for a FOSS RSS reader that’s a bit more fun and less brutalist than the other great but more technical user-minded options out there

reply

bityard
 
22 hours ago
 
 | 
parent
 | 
next
 
[–]

Thank you for having a demo!

reply

BagelsOverBread
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Of course! The nice thing about making your software self-hostable is it makes setting up a demo site trivial to do

reply

p2detar
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on new puzzles for my tiny word puzzle web game for programmers and computer science nerds.

It's a PWA and works offline. Tech: js, no libs, Canvas API, Web Audio, not vibe coded, but I did use Claude for graphics and tests. Puzzles curated by hand.https://7coderwords.kenamick.com/

reply

czhu12
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Been working on an open source, free, Heroku alternative at 
https://canine.sh
 for about two years.

I feel like even after all these years we’re still missing the devex that Heroku provided.It’s been super fun to experiment & integrate MCP into it.We just passed 2000 developers last month actively deploying with canine.

reply

cryo32
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Wrote a Forth VM in C in about 1996 based on TCJ articles by Brag Rodriguez. Managed to get it to compile with modern GCC this morning and fix all the horrible issues with valgrind. Trying to adapt it to a context where it'll be usable for a spreadsheet-like system with reasonable decimal numeric precision. Consider it an RPL calculator with an Excel-like front end.

reply

crowdhailer
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Writing my own programming language eyg.run that for a long time had no syntax. I worked on a structural editor for a long time and this weekend I finally documented the sneaky text syntax that did exist for testing. 
So the structural editor I'm not sure about the future. The language is still fun to write and use tho.

reply

zricethezav
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I've been working on Betterleaks for the past three months. It's the successor to Gitleaks since I'm not focused on that project much anymore. I just released v1.2.0 which added GitHub as a source to scan for secrets against and a new filtering system powered by CEL for more expressiveness.

https://betterleaks.com

reply

reassess_blind
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A local web UI with text editor and terminal (with Claude/Codex) where you can code apps, edit the code in the browser, view previews (spins up Docker containers) and promote previews to production. An all in one mini SaaS manager.

reply

philipnee
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

sure! - security layer between your local data and public internet, i use it as mcp server to let claude safely read/write to my computer!

cli:https://github.com/philipnee/mvmtui:https://github.com/philipnee/mvmt-desktop

reply

oinoom
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Reflect [1], it’s a local-first privacy focused self tracking and data analysis app where you can set goals and run self experiments

[1]https://apps.apple.com/us/app/reflect-track-anything/id64638...

reply

Igor_Wiwi
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://mdview.io
 - markdown reader for big documents, including navigatable mermaid diagrams, LaTeX, Fixing broken syntax and ton of other features. It's early stage but getting popular really fast( I guess it just does it's job right)

reply

kukkeliskuu
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Continuing USM tools, set of tools for better service management based on Unified Service Management (USM) model. The basic idea is better to define your services as data, instead of documentation.

reply

socketcluster
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

A no-code platform packaged as an AI tool for building data-driven applications and serving as a data store for AI to tell it interact with your data; 
https://saasufy.com/
 - Tested with Claude Code and pi.

reply

0x180db
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

learning zig by building two things: 
https://unimeter.io
 a zero-deps usage metering engine and a set of cuda katas in zig done rustlings style 
https://github.com/0x180db/cuda-zig-katas

reply

morisil
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

https://github.com/xemantic/markanywhere

Incremental Markdown parser that emits streams of semantic events, plus tools to manipulate them - designed for real-time rendering of streamed LLM output.

reply

matt_kantor
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been iterating on the type system of a somewhat-kooky programming language I'm developing: 
https://github.com/mkantor/please-lang-prototype

reply

kamranm
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

https://acoust.io
 began as a project to learn React. However, I received a few customers after posting it on Reddit. I’m still figuring out the best way to position it in the crowded market, but I’m enjoying the process of building and learning.

reply

nickyvanurk
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Been slowly chipping away at my vehicle building browser game 
https://mechacraft.io
. For those interested in following the progress I made a discord channel: 
https://discord.gg/bXH66ZDBKr

reply

hjessmith
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a web app that animates hand drawn human characters. You try it here without any login or anything:

http://doodlemate.comIt doesn't use generative AI, instead it auto-rigs the drawings in just a few seconds.

reply

moinism
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Chat Octopus: Claude code for videos

https://chatoctopus.com

reply

niyikiza
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Building tenuo.ai (
https://github.com/tenuo-ai/tenuo
): task-scoped authorization for AI agents. Rust implementation of capabilities + cryptographic offline verification.

reply

vihaanshah2
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working a faster GUI for Claude Code //other CLI tools (
https://fluidstate.ai
) that works in your terminal and can run multi instances in a tab and you can tab between them quickly regardless the tool

reply

goenning
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

3 years later and I'm having fun building and growing Aptakube, a Kubernetes GUI

https://aptakube.com

reply

fersarr
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm improving my web app to learn languages with short stories: 
https://webbu.app
. I've been making it easier to track your progress, hear pronunciation of words, and adding more advanced levels.

reply

aguacaterojo
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

I think stories are a good approach, although there's something grating about the voice / monotony after 1-2 stories. Have you thought about narrating yourself?

reply

davidkuennen
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

From 50 to 5 seconds. The world's fastest and most up to date investment ai. It's powered directly through our database to ground the information and reduce hallucinations. Still in development though.

https://stockevents.app/ai

reply

npilk
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm trying to make it easier for non-technical folks to publish websites: 
https://weejur.com

82 sites published so far, with a really weird and wide range of content.Working on a simple WYSIWYG website editor to go with the current functionality.

reply

skor
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

A scripting language that is very fun to write and lets you make interactive music, installations, generative compositions etc 
https://github.com/audion-lang/audion

hack music

reply

stagas
 
22 hours ago
 
 | 
parent
 | 
next
 
[–]

This is pretty cool! I've been working on something similar[0], but for the browser, maybe you like it.

[0]:https://loopmaster.xyz

reply

freakynit
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is sooo freakin cool. Love it.

reply

skor
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

looks very fun indeed!! will check it out thanks!!

reply

mgw
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I‘m building a way to record and replay AI image and video generation API calls to any provider so that in testing, people can save money. This is part of our AI media model gateway 
https://lumenfall.ai

reply

Yabood
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building Lexeme (
https://trylexeme.com
), a SaaS service that tracks how AI models like ChatGPT cite and describe your product vs. competitors, and tells you what to fix first based on estimated revenue exposure.

reply

bwm
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

NixOS VMs for agents: 
https://machine0.io

reply

confusus
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Really cool!! I'm messing with NixOS in VMs too.

One fun thing is that you can use them to let agents iterate, testrun and propose their own next versions. I guess you're even using NixOS to declare the surrounding infrastructure.

reply

GarnetFloride
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Just started working on a book to celebrate the 50th year of our symposium, which is coming up in 5 years. The initial idea is a how-to book, filled with essays from past contributors, but since we only started yesterday - that may change.

reply

iugtmkbdfil834
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

:D

Well, all of a sudden, now that I kinda quit my gaming time sink, all my mini projects are finally being completed. All small, but useful, things for my setup that seem to slowly become a part of a bigger personal project. And between that kid and lots of books.Ngl, it is weird for me now. If this is midlife crisis, I am loving it.

reply

GroksBarnacles
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm making a program to build Magic: The Gathering decks from first principles of card data, no reliance on user-posted deck aggregation or EDHREC, and no AI. A slew of internal knobs exposed.

reply

burgerquizz
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

working on 
https://heylife.ai
, an app that gives you proactive advices based on your calendar/taste/hobbies/location

let’s say you are arriving in paris. it will send you advice on how to get to the city from the airport. big soccer game in an hour? will send you advice on prepare it.you don't need to ask, it will give you before / when you need it.now working on the sandboxing and scheduling of the advices. releasing it this week if anyone want to give it a shot. (it will be paid only)

reply

Nizoss
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m working on a project that blocks agents from breaking rules. The rules are enforced through hooks and work across Claude Code, Codex, and GitHub Copilot.

https://github.com/nizos/probity

reply

welder
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an AI Dashboard & AI Leaderboard where you can see who generates the most lines of code using Codex, Claude, Copilot, Cursor, etc. 
https://wakatime.com/ai

reply

dcminter
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Kafkaesque, a wire-protocol compatible Kafka mocking service.

https://github.com/dcminter/kafkaesqueWorth kicking the wheels if you're currently using embedded or dockerised Kafka in your tests.

reply

41209
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I tried to remake Slay the Spire as a text based game. With buttons though. I used Godot.

https://beatquestgames.itch.io/textbattlegdCompletely open source if you ask and promise not to make fun of me.

reply

sram1337
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Cool game. Most everything worked which is nice. The fishing game was more fun than I expected. Took a while to understand the UI though.

reply

41209
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Thanks.

I absolutely love the text based game era and tried to work with that limitation, but on a mobile browser.Eventually I want this as a framework for building similar games, but that takes time.

reply

rajeshvar
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

https://vistacker.com
 - local first task and note taking TUI and iOS app, disconnected operation, auto sync across multiple machines with optional encryption so the service can’t see your data.

reply

gghootch
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

https://extraheadroom.com

Menu bar app that reduces your Claude Code token costs by ~50% so you get 2x more usage out of your plan.People seem to like it so far :-)

reply

zahlman
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I did a game jam over the weekend, and took it as an opportunity to start streaming my development work. Also hoping to start building a TUI library as I refactor this mess...

reply

Centigonal
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on an idiosyncratic tool that lets users use AI to help write statements of work without losing the high bar for accuracy and consistency that these documents require. Right now, it's somewhere between Typst and Gemini in Google Docs, but not as good as either yet.

reply

eajr
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

An idle/incremental rpg for fun in my spare time (that doesn't really exist!)

https://darkspire.gg/

reply

variodot
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Diving deeper into woodworking and knocking out a few cabinetry/storage projects with the work-in-progress up at at 
https://shopspec.io

reply

djyde
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

A Hacker News mobile client that I'm very proud of, specifically designed for non-native English speakers with automatic translation features.

https://haiker.app

reply

postatic
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Built my own backend for excalidraw frontend :)

https://drawx.ossy.dev

reply

agentifysh
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

MCP that lets you call chatgpt pro, grok, perplexity, gemini web, web subscriptions from codex, claude, opencode, gemini

https://github.com/agentify-sh/desktop

reply

welcome_dragon
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

A planning app for smart telescope users, taking into account the specs of the telescope, weather, light pollution, etc to help a user plan imaging nights

reply

k9294
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on 
https://ottex.ai
 - voice ai for busy professionals.

Think wisprflow + granola with 30+ top STT models under single login and pay as you go billing model with 25% markup over API.

reply

abdullin
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on benchmark arena for AI agents with my wife.

We grab interesting business problems, turn them into fun challenges for hundreds of AI engineers to find the best architecture for. Insights are shared back with the community.It is a fun learning process with unexpected scaling challenges.

reply

tsoswr
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://pockli.com
 - I've always needed a better workflow for managing the stream of documents people hand me — then expect me to pull out of a hat months or years later, like a magician.

reply

pwnna
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Trying to see if I can implement psychoacoustic bass enhancements and other advanced DSP techniques to improve Linux laptop speakers.

reply

ekrapivin
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I've spent several years developing a few dozen solitaire/puzzle online games:

https://inSolitaire.comI am currently rewriting the engine to add ~400 games this month.

reply

marking-time
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

Well crafted! Thank you.

nettirw yb namuh

reply

absoluteunit1
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Building 
https://typequicker.com

An AI first typing application.I think anyone can learn touch typing and potentially 2x their typing speed.We make typing practice engaging and data driven.

reply

momentmaker
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I'm working on app for walking based on the practice of walk, talk, meditate.

For now it's just for iOS but currently I'm working on porting to Android.https://pilgrimapp.org/

reply

reconnecting
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

tirreno open-source security framework

https://www.tirreno.comhttps://github.com/tirrenotechnologies/tirreno

reply

cousin_it
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I launched my live polling app 
https://suggestionboard.io
, got some first users, now looking at how they use it and trying to improve the experience.

reply

mikesabat
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm doing this with my son. Dcflagproject.com

Replit for the website (he did the first 80%), Gemini to make the flyers and he'll be walking the neighborhood and talking to neighbors.

reply

arunkant
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on 
https://releasedog.com/
 - It collects changes from JIRA/slack/github and create a changelog/release notes.

reply

asim
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

The same thing for 10 years and every couple years it gets reimagined while trying to get to the original goal of building a replacement for Google. It's called Micro.

https://micro.mu

reply

jchook
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently published 
https://hngram.com/

It’s an n-gram viewer for Hacker News comment data.Still working on daily data updates, etc but it’s live!

reply

nuccy
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

Please comsider adding log-scales to be able to compare related but wastly different in popularity topics. Also would be nice to show one topic versus another to see a correlation.

Thanks.

reply

lostathome
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Context aware local AI assistant 
https://hitoku.me/draft/
 I believe private local AI is the future for every day's use.

reply

nurrito
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

My partner & I have been making this wordle/wheel of fortune inspired daily - 
https://crosses.io

Each guess can be a single letter or a full word. Revealing letters helps you make word guesses, which are more efficient since it reveals all instances of those letters across the board.It's been really gratifying seeing friends enjoy the game, now we're trying to figure out how to get in front of more players. Leave us some feedback if you stop by

reply

medbar
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Porting doom to my hobby OS and fleshing out my personal cloud with terraform & AWS. Polishing up a project before I open source it.

reply

teppeik
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

LazyNote : Discord/Slack like personal note app

https://about.lazynote.app/

This is a Flutter project.

reply

swsieber
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

AI Coding "All the things" (tm). More agent engineering on the bigger stuff and more vibe coding on the smaller things.

A print farm manager for bambu printers in lan mode. I lay down the base types and schema structure and a few other bits here and there.Using AI to preprocess some amazon transactions from both personal account and business accounts as I untangle them since I started a side business with my spouse a few months ago (involving 3d printing).Starting on a yoga workout generator and food/fitness/weight tracker.

reply

0gs
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

i am working on an offline weights harness for non-technical people, writers mainly. it's designed to work forever but also be adaptable as more weights get released etc.

it enforces very few paradigms, runs in the browser, and allows users to view and edit agent config files within the UI.it's kind of a nightmare to try to figure out how to do this appropriately, but it's an interesting challenge and i have seen very few (~0?) projects with an approach like this ...all the offline harnesses are optimized towards coding, vs. general text manipulation aka "writing."hoping to publish v0.1.0 by the end of may.

reply

blinkbat
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Most fun thing is a few vibecoded games. A rtwp rpg like bg2 and an active turn-based grid crawl rpg.

Bg2-like is playable athttps://archipelago-sandy.vercel.app

reply

knrd
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://emiplan.net/
 - Doodle and Splitwise like alternatives for organising time with friends.

I'm a backend dev, frontend was made with AI.

reply

jchap
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Tryke! A Rust-based Python test runner with a Jest-style API.

https://github.com/thejchap/tryke

reply

Tsarp
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Markdown based voice note taking

https://voicebraindump.com

reply

devgoth
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

still chugging on Whenish 
https://apps.apple.com/us/app/whenish/id6745035749
!

outside of that I started to fiddle around with a cross section of observability and analytics with SDKs...building a little tool to give SDK publishers better insights.

reply

vinayak-shukla
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

while I was using claude code, I was playing some lofi music in the background while it was 'Combobulating' and I thought what if it could auto-play lofi beats while working and stop when it has finished running. So I built a claude code plugin, I call it vibe-coding. Can check out/add the repo as a marketplace and plugin from here: 

https://github.com/Vinayak-Shukla/vibe-coding

reply

rpastuszak
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Making a proper product page for my stream of consciousness writing tool Ensō (preview.enso.sonnet.io)

(I’ve been procrastinating on marketing basics for seven years, so it’s… fun but still intimidating :) )

reply

kukkeliskuu
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Any ideas, approaches, books, blog posts you have found useful for product page planning?

I have a related need, to create some great product spec sheets.

reply

koeng
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

I’m smelting ore!

I got into creating my own rings, and I’d really like to create one with ore I harvest myself. Gold is too hard and silver can be kinda dangerous, but malachite is pretty safe and I can just drive to Copperopolis to pick some up.Basically: smelt the malachite with flux and charcoal to get pure copper, flow that into an ingot mold, hammer it into shape. Then I’ll have my own ring, with metal I collected with my own hands

reply

thopate
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Took a sabbatical off tech marketing recently to focus on my creative work:

An interactive sound sculpture running on an Arduino uno+PdUsing Mandelbulber as a visual effects layer for my experimental music AV show

reply

sp1982
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Salary explorer based on US job postings: 
https://corvi.careers/salary-explorer/

reply

dvh
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

In measuring how long can esp32 stream video over wifi using single 14500 battery (AA size but 3.7V lithium). So far it seems like 2h 8m is the limit. I'm using tps63020 buck-boost to 3.3V.

reply

mstaoru
 
1 day ago
 
 | 
parent
 | 
next
 
[–]

Wouldn't wifi settings (antenna, Tx power, freq, bw, encryption, etc) be the bigger driver here?

reply

dvh
 
1 day ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't know.

reply

kirubakaran
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

https://hyperclast.com/

Smart documents for teams. Fast, Open, and Self-Hostable.Basically a much faster Notion.

reply

smnscu
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Coderbase (
https://coderba.se/
), a platform for running technical interviews. It started with live interviews cuz that's what I know best, having run over 3,000 interviews in my career, but I made it easy af to run this yourself too. I initially pictured it as a tech-heavy product (and it is), but my second client is a large recruitment agency that's using it both for internal interviews (for recruiters) and external ones (for candidates they're presenting to clients).

I didn't set out to do this. After I got laid off in December, a client quickly fell in my lap: a small startup in the middle of a massive investment round that needed to hire 25 people immediately, with only a CTO available for interviews. I created their content and ran their interviews while building the software at the same time. It started as Google Meet + CoderPad + Calendly and gradually became an in-house system. Unlike Proton (lol), I'm not pretending I built my own video call solution from scratch, it's just an off-the-shelf 100ms integration.The content is all versioned and structured, which makes it fast to iterate on and easy to reason about. We use major.minor versions and only bump the major for backwards-incompatible changes, or changes big enough that comparing interviews stops making sense. Otherwise, any combination of question versions inside an interview format is considered comparable if the major versions are identical.The interview itself is highly structured: once you define a format from the content library and the various knobs you can adjust, you can schedule interviews and run them using our integrated "room" (video call + multiplayer code editor, both recorded, with transcripts and playback) and "rubric" (the tool the interviewer uses for content, scoring, and notes during the interview). Once you submit/publish the interview, a report is generated immediately. Example:https://coderba.se/sampleTwo interesting AI bits:- "AI linting": a way to benchmark interview questions by running a candidate model and an interviewer model against each other. The candidate closely follows a defined skills profile, then we compare actual vs expected performance. More here:https://coderba.se/blog/product-update-unit-testing-the-inte...- "AI draft": once an interview ends, it takes ~30s for the video and transcript to become available. Then we use basically every relevant artifact from the interview, with a PII redaction pass first: questions, scoring, incomplete rubric, transcript, code editor history. We send that through our LLM gateway, currently mostly using DeepSeek because the quality/value is insane, though I may switch to Mistral to stay on the better side of privacy. It sends back recommended scoring + writeup, which we present as Cursor-like suggestions you can accept/reject/edit.

reply

DeveloperOne
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

https://hashmate.app
 - a little social platform with cool features for devs, hackers and geeks.

reply

Tsarp
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

https://carelesswhisper.app

reply

ok1984
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

On a platform for manufacturers, currently focused on a warehouse management system, 
https://pragmatech.it

reply

wilbur_whateley
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on Nichess (chess with health points) - 
https://www.nichess.org/

reply

softservo
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

text-to-cad! 
https://github.com/earthtojake/text-to-cad

reply

jjordan
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Trying to make a stab at improving RSS feed discoverability. There's a website portion and an app portion. Hope to have something to show off in a few weeks.

reply

seky
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.contextractor.com/
 - Web content extraction tool to feed LLMs

reply

ivan_gammel
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Decided to cancel my personal Miro subscription, so vibe-coding* a diagram/vector graphics tool with UX I would enjoy rather than tolerate.

* assisted coding, not full code generation

reply

simonadler1
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a 2 circle Venn diagram creator (
https://Venndiagrammer.com
)

reply

PaulRobinson
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

A few days back, a book on FreeBSD Driver Development was posted here [0], and everyone assumed a) it's LLM slop and b) a terrible introduction to the topics covered.

I scanned a couple of chapters and realised it likely wasn't LLM generated, it just needed an edit. The intro to C is a hard and weird intro, but then driver development in FreeBSD is hard and weird and people who aren't prepared to get through such intros probably aren't going to get through the rest of it.Being the contrarian, I've started going through it. I was involved on the periphery of the FreeBSD project ~25 years ago, went to conferences, ran a BSDUG in my hometown, and so on. And I realised I've missed systems programming and FreeBSD itself a little, and in recent years became a little sentimental.What I've discovered so far in the first few chapters:1. I miss FreeBSD. And it's weird my muscle memory kicks in and am surprised in a lovely way to find familiar things like /etc/rc.conf work the way I remember them.2. This is not AI slop. There are issues that I can blame on him not using the same platforms I am (if you're on Apple Silicon, just use UTM and the aarch64 ISO - don't use the VirtualBox config he suggests, as an early example), but as somebody who sees a lot of AI generated content in my day job - this isn't it3. I have got excited about coding again for the first time in a while.So, this is my hobby for a while. Go back to where I started, get into low-level systems programming again, I have some ideas on some hardware I want to help out on... it's different to a lot of what I've been working on for the last decade or so, but that excites me.[0]https://news.ycombinator.com/item?id=47915632

reply

hugoib
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

An app to bring science to curious minds.

Science is full of discoveries that could change how you think, eat, train, sleep, work.Most people never hear about them because papers are dense, paywalled, and written for specialists.I built SciCrumb to fix that. One paper a day, simplified to 3 minutes. I curate what's actually worth your time.I personally really like it. I Get new idea and learn something new every day.https://apps.apple.com/us/app/scicrumb/id6758953292Product feedback or support is highly appreciated. Would love to make more people aware of it.

reply

ternaryoperator
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A JVM written exclusively in go. Now, 5000+ commits into the project.

http://jacobin.org

reply

Grosvenor
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm writing an M68K NeXTStep userland emulator and thunks to run NeXTStep apps under GNUStep. I'm starting today with hello world.

reply

alifbae
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A Self hosted multi-player boggle game

Play a game here:https://bawgle.alifbae.dev

reply

goodthink
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

Isolated Web Apps - Resurrecting ancient TCP protocols using TCPSockets in the web browser (Chrome) with Newspeak.

reply

cemsakarya
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Building storica.club, experimenting the adult way to learn a new language, through actual content that an adult can enjoy.

reply

seky
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

https://www.htmlwasher.com/
 - online HTML cleaner

reply

orrison
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been working on a set of custom PHPStan rules that started off as a replication / modernization of rules from PHPMD, but has evolved to include more than that.

https://github.com/Orrison/MeliorStan

reply

raffael_de
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I can't really go into details of what I am working on. But I'd like to say that a lot of European corporations are running their stuff on Azure and are very much interested in having Data Lake(house) platforms tailor made to their business and IT requirements based on Databricks and their stack. I mention this because I find this mismatch of what I see being relevant in business and what is being upvoted on Hackernews quite interesting (for the lack of a better word).

reply

gibbsrich
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I am currently working on a server hardening and inbox cleaning services without a subscription

reply

danielvaughn
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A browser for designers: 
https://www.matry.design

reply

nnurmanov
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Basecheck.ai - a database auditing tool, supports Oracle, MS SQL Server, PostgreSQL, Supabase and SQLite. Happy to demo

reply

glasner
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building aiki.sh so Claude and Codex can work together without babysitting

reply

recursive-call
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Currently building my own rss reader because I wanted one that runs in the terminal, but all the ones I could find were in Rust

reply

BSTRhino
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

https://easel,games

A reactive programming language for games! Properties signal when they change and you can register blocks that tell the engine how to use that property, not just once but every time it changes. It’s a more declarative way of making games which I think is lots more productive.I’ve been working on this for four years, it’s been a big project!

reply

vegadw
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Oh! I have so many in-progress projects right now,

First up, the "AskHN for help project in progress": I'm working on some pages for my websites and want to capture + embed some interactive gaussian splats. I haven't yet found a good, embedded-able option that doesn't assume a huge dynamic website instead of my simple Hugo based static site. Any good options?Otherwise,I just got a vintage horn-speaker. The actual Atwater Kent driver was long since dead, but I ordered a compression driver to feed it after testing it with a talkbox and finding it sounds amazingly honky!I have a piano's soundboard and 24 solenoids, all the drivers, etc I need to wire up to make a self playing piano (ish, I mean, it won't be hitting hammers - directly solenoid to string)I got tired of Alexa's slow degradation into a central advertising point and weird LLM-y-ness, so just got some Home Assistant Voice Preview Editions to replace it. Performance is so far worse, so I'll be doing some tuning on that. It also means, unfortunately, replacing a lot of my lights/switches and moving to Zigbee. Total cost, with the two voice/speaker boxes + lights + switches + Zigbee hub I think I'll be about $300 deep. Not too bad.I have a Dactyl Manuform mechanical keyboard that's 3D printed, has the keys put in, but needs soldered up, hopefully able to knock that out soon too.Old eleksmaker pen plotter / laser engraver sitting around had it's controller die a while ago, finally got a new one, but will have to actually learn how to setup GRBL and find some open source software for driving - Which, sounds less than fun. Last time I tried, I found all the software to be expensive, hard to use, and generally frustrating.On top of all of that,* I have a Hurdy Gurdy sitting at about 3/4 finished, shouldn't need more than another 8 or so hours of work to get playable.* I want to make some Nuclear Instrumentation Module inspired modules for VCV rack* I have an AudioMoth on the way, I'm looking forward to learning how to setup so I can learn about bats in my area!* I'm still about 75% done switching back to linux, now that I feel it's finally ready to be used for music stuff since the transition to Pipewire seems over with and It's no longer a total mess of ALSA+JACK+Pulse+PipeWire. That transition hell mad me switch back to windows for few years, and it's nice to be backAlso, since the last thread I've managed to fully rebuild my studio setup, setting up multiple 3-tier stands for synths + the Wall-o-pedals. It came out really well! Was nice to brush up on at least basic wood working skills for it too. During that project I also discovered 3M dual lock is magic and will be over-using it on everything from now on.

reply

LinasKo
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

I've got a taskboard that auto-completes easy tasks, specs out and visualises hard ones.

Draws from a bunch of sources, MCP-connects to my agents, comes with a browser plugin to invite meeting bots to calls, lets me (and my testers) leave notes on websites which also gets added in.The goal is to make work as simple as dragging tickets around, and load as many best practices + review clarity into itI've set a deadline to finally launch tomorrow, but frankly - I don't know how it's gonna go. Feeling proud, yet a bit anxious about it.https://kodan.dev, if anyone wants to take a peek

reply

registeredcorn
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm making a joke-website, "Everyone Loses as a Service (ELaaS)" [1]

The premise is essentially:1) Accept money from angry customers asking us to prompt-hole tokens from targetedCompany chatbots2) Approach targetedCompanies to offer the "real" (secret) service. For a monthly subscription fee, we won't prompt-hole their LLM tooling.3) The real,realservice is to setup some google alerts for targetedCompany release notes & forum posts. Whenever threshold exceeds some predetermined threshold, initiate Turbo Mode: the higher the hatred-per-customer, the greater thediscountthe service will be for them. Spit out newsletters as needed, regardless of whether or not they subscribed.Meanwhile, initiate "surge pricing" for targetedCompany on a per-hour, per-payment basis. The more customers that pay, the higher the "one-time fee" is to targetedCompany.Staffing is almost entirely made up of interns, a few roles are filled by underpaid contractors with unattainable goals; keep them both working there with the promise of full time employment "after things calm down."If all goes well, everyone pays us money to do absolutely nothing with minimal outflow of revenue.[1]https://news.ycombinator.com/item?id=47953158

reply

right-words-dev
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I made Right Words (
https://www.rightwords.io/
) a fun little solo project, tl;dr it's a twice weekly word puzzle where you trace two-word phrases on a grid by finding a path with exactly one gap (the space between words). Think NYT Strands but with a jump!

React + TypeScript with Vercel handling deploys, no backend (yet), the puzzles are just JSON. The toughest part is the puzzle generation: packing multiple snaking paths onto a grid like jigsaw pieces with the constraint that each answer has exactly one valid path. Coming up with good two-word themes has been its own challenge too!Always looking for feedback or suggestions for improvement. :)

reply

coder97
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

working on 
https://www.focuslive.app/realtime

Its a virtual body doubling tool without camera that helps people focus together anonymously

reply

zhoujianfu
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Clodhost.com … Claude code with a web interface on your own (hetzner) VPS… and free!

reply

gylterud
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

On my spare time, I am working on my game, a sci fi dungeon crawler – written in Haskell. Currently finishing up the graphics engine. OpenGL based. 2.5D but with a real 3D dynamic light system. In game objects and entities cast realistic soft shadows, and are lit up realistically. Took a lot of mathing and thinking to get working!

Next up is actually implementing game play!There is a little video demo here (but bear in mind that everything is temp graphics)https://hakon.gylterud.net/diary/2026-05.html#2026-05-02

reply

mathnorth_com
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

---------

Working onhttps://fastsleep.appUsing this app, you may fall asleep in 20 minutes (maybe within 8 to 15 minutes)Simply start the session and imagine what you hear.
Like if you hear "calm river", imagine that. If you hear "heavy rain over a tree" imagine that. And you may fall asleep soon.Try this tonight!---------

reply

yu3zhou4
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Just learning math and trying myself in ml research

reply

konichiwAI
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

wasm based in browser steganography with a full file system/viewer embedded.

https://hidefile.app

reply

magicstefanos
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Bloom! Visual research tool.

https://bloom.site

reply

zacharyfmarion
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

cascade-editor.pages.dev - a free node-based image editor that works with image sequences and has an associated desktop app. It’s pretty incredible what you can do in browser these days with wgpu and wasm- everything is cross compiled from rust.

reply

mpretti
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

i keep building more to 
https://service-zen.com
 instead of finding my first client. but this is what i’m working on

reply

anuramat
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

vicode -- TUI coding agent written in Rust, with tabs/subagents running in
worktrees on top of fuse-overlayfs: create/fork tabs to work on multiple
features/implementations, while subagents work in parallel without conflicts;
additional lowerdir with bindfs mounts lets agents share the compilation cache,
so that `cargo check` doesn't take minutes

since it's all just mounts, vicode works as a worktree manager as well: select a
vicode tab (which sets cwd to the corresponding worktree with OSC7), open a new
terminal tab/window, and run claude/codex insidedisclaimer: unstable, linux-only (mac build WIP, no overlayfs), some modules
were vibecoded (grep for `SLOP`)https://github.com/anuramat/vicode

reply

EMAIL36245
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

EMAIL - email.riamu.io

reply

bityard
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I've been vibecoding* a calendar-based personal note-taking thingy: 
https://github.com/cu/doneski

The idea is that each morning, you click the "New Day" button, and your Todo list along with other notes carry forward from the previous day to the new one. When you accomplish something, you add it to the Done section. Other sections can be added as needed. I have been using a text editor and/or shell script for this purpose for about a decade, but have been inspired to make it into an app now that I can delegate the boring bits of app development. It is not quite done yet, but it's getting close to being usable.(* To the inevitable downvoters, this is in part an experiment to get familiar with what SOTA LLMs can handle. With the intent of comparing it to local LLMs once I get my Strix Halo set up as a coding assistant. I only code as a hobby currently, and have too many other hobbies, and this app wouldn't exist without something else doing the heavy lifting. That said, this is a pretty low-stakes application and I don't commit any code that I haven't reviewed and don't understand.)

reply

atilimcetin
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Writing detailed and a bit math heavy blog post about specular microfacet-based BRDFs.

reply

AFF87
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

A personal CRM system that lives locally in your device, no data shared anywhere

reply

fragmede
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

What happens if the device is lost or stolen or is otherwise broken?

reply

croisillon
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

i guess some kind of a mashup Airtable x Yahoo Pipes, but i've never used either of these

in each job i find myself trying to enhance information in order to visualize it, so this time i'm finally giving it a try

reply

carlos-menezes
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Modding GTA:V.

reply

benfrancom
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

pod2book.com It converts podcasts to e-books for the deaf, hard of hearing or neurodivergent because transcripts are clunky.

reply

phoenix24
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a system to create animations, and a new cicd system.

reply

electrovir
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

A TypeScript in-browser game engine where everything is a mod.

reply

chromadon
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m developing a Gizmondo emulator. It’s an old gaming handheld.

reply

all2
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on Maelstrom, an agent framework with only the basics:

- 'agent' as cognitive state, ie, what to think about- 'workflow' as 'what to think about- 'session' as immutable agent history- 'timers' as a way to kick off an agent on a schedule (with or without a workflow attachedI've been working on this since just before OpenClaw dropped at the end of January. Currently it weighs in at around 20k lines of code. There is still a significant amount of work to be done on polish, but the core appears to be functional, and almost to the point where I can replace opencode as my daily driver (I'm very much looking forward to this).From [1]:---I've been working on a framework since the end of January or so. I'm on my 7th draft. As I've gone along, each draft gets markedly smaller. The overlaps between what I'm building and openclaw are significant, but I've realized the elements that make up the system are distinct, small, and modular (by design).
There are only a few primitives:1. session history1a. context map + rendered context map (think of a drive partitioning scheme, but for context -- you can specify what goes into each block of context and this gets built before being sent out for inference).2. agent definition / runtime3. workflow definition / runtime4. workflow history5. runtime history (for all the stuff session and workflow history fail to capture because they are at a lower level in the stack)That's it. Everything else builds on top of these primitives, including- memory (a new context block that you add to a context map)- tool usage (which is a set of hooks on inference return and can optionally send the output straight back for inference -- this is a special case inside the inference loop and so just lives there)- anything to do with agent operating environment (this is an extension of workflows)- anything to do with governance/provenance/security (this is an extension of either workflows and/or agent operating environment... I haven't nailed this down yet).I suppose I should say something about how agents and workflows work together. I've broken up 'what to do' and 'how to think' into the two primitives of 'workflow' and 'agent' respectively. An agent's context map will have a section for system prompt and cognitive prompt, and an agent can 'bind' to a workflow. When bound, the agent has an additional field in their context map that spells out the workflow state the agent is in, the available tools, and state exit criteria. Ideally an agent can bind/unbind from a workflow at will, which means long-running workflows are durable beyond just agent activity. There's some nuance here in how session history from a workflow is stored, and I haven't figured that out yet.Generally, the idea of a workflow allows you to do things like scheduled tasks, user UI, connectors to a variety of comms interfaces, tasks requiring specific outputs, etc. The primitive lays the foundation for a huge chunk of functionality that openclaw and others expose.It's been fun reasoning through this, and I'll admit that I've had an awful lot of FOMO in the mean time, as I watch so many other harnesses come online. The majority of them look polished, and are well marketed (as far as AI hype marketing goes). But I've managed to stay the course so far.I hope you find your ideal fit. These tools have the potential to be very powerful if we can manage to build them well enough.---[1]https://news.ycombinator.com/item?id=47784743

reply

tasoeur
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

For the past 2.5~3 months I've been working on a 2D/3D VFX (visual effects) editor dedicated to mac and iPhone/iPad, it was on my never ending list of fun projects to build and a perfect excuse to learn agentic coding on a domain of expertise (written in Swift/SwiftUI and Metal).

I wrote a blog post about my process:https://sxp.studio/blog/subjective-building-a-native-vfx-edi......and you can download the app here if you're curious (the app is free!):https://subjectivedesigner.comNext project is going to be a pivot of that project into something related to creative coding and agentic :-)

reply

kalx
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m making a top down RPG. 16x16 pixel art. Loving it. In Godot.

reply

palguna26
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Im building termyte, the runtime safety layer for ai agents.

reply

seky
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

hosting comparison tool 
https://www.punycoder.com/hosting/

reply

seky
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

also 
https://www.gluee.com/
 - Text Styling for Social Networks, Slack, Teams etc...

reply

fafa09
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

voice to text application

reply

l7l
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

working on a voice first, interaktive universal audio guide. 
https://artsplain.com

reply

femora
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Working on a femtech, yes yet another one 
https://femora.app/

reply

theusus
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on a native non JS Http client similar to Insomnia.

reply

lopatin
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm building an AI, that uses AI to operate AI.

reply

fragmede
 
23 hours ago
 
 | 
parent
 | 
next
 
[–]

Why not have an AI build an AI, that uses AI to operate AI?

reply

_def
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

cross-platform app for tracking your meals, in order to make sure you eat balanced meals in a regular timeframe and to help you reflect

reply

rossdavidh
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on a framework for factory management systems.

reply

rahulramesh82
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Working on a Platform That hosts Open Source software & Gives users Enterprise-Level AI Assistants & Support to challenge Saas Software (Just a MVP right now!!)

I just hate the Saas Scene today - even a small productivity app is worth $10-$15 / month . When you couple that with a bunch of apps that you use , you spend hundred of dollars in hard-earned Cash .The Open Source Community is Amazing on Some fronts , but then enterprise & non-technical users can't use them without a layer of Support , Hosting & Setup Assistance .We want to be the delivery layer between the Current Open-Source Community & Saas users .Got a lot of ideas to work on it , but decided to build out a small version right now and launch it !!

reply

NoMoreNicksLeft
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I have fully implemented mutable torrents (BEP 46) in Transmission. When a torrent is created, you can set it to be "mutable", and you (and you alone) can add files to the torrent, remove them, modify them, or change their filenames. Other members of the swarm will be notified of the new change, and begin downloading that as well (if they use a client with mutable torrent support). For leechers, they can choose whether to allow mutability on a per-torrent basis, and only in the fashion that they prefer. They can even store every change (and seed those) too.

I have the macOS, Windows, cli, and web app working with this feature. I had a bit of a mixup with Gtk, so I don't have a Debian package for it, but it's buildable from source.https://github.com/NoMoreNicksLeft/transmissionI would appreciate it if anyone wanted to test it. I'd like to think that the feature would be a big deal, even if my implementation of it's kinda crappy.

reply

Almasy
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

喜欢你

reply

voodooEntity
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

So i just finished a long running project (10 years ftw) just to deepdive into the next one.

I have no public sources yet (will come at some point) but ill try to break it down into some simple points. After all: this is a research project.Project: DeepThoughtSo instead of going for the path to take bigger and bigger models to solve more complex questions, i going another direction. My idea is to use LLM's in a way like an "inner monologue" to replicate a thought chain. Basically create thinking steps that can be dynamically chained.Additionally, the project contains a 3 layer memory system which is parted into:1. Frontbrain (this data composes the context for inference, its a set of "hot nodes" which have a temprature that per turn of conversation will cool down a bit, while if they are used in a "thinking process" get warmed up a big again. The idea is to have the context for the inference to only get the currently relevant information, while dropping of things that lost relevance. This should prevent context overflow2. STM : Basically a session memory. This will keep all information from the current session even if they got to cold and dropped out of Frontbrain3. LTS : LTS is always query'able for the thought process to retrieve information/structures, but only at the sessions end information is propagated from the STM to LTS. This makes identification of "unique" entities alot easier and has some other advantages.So when you type something into the DeepThought engine, it will extract all information from your input and convert it into a kinda 2 type structure
1. A bitemporal hypergraph composed of Entities and Hyperatoms. While entities i think are kinda easy to grasp, hyperatoms can either represent "properties" (in form of facts) or relations to other entities. This allows to create a graph structure typed information network containing the relevant information2. Frame summaries. Since only having a structured graph as just described looses a lot of processual/logical information which are relevant especially in more complex contexts, i also create basically short summary texts that are linked to entities.This structures allow me to use dynamic graph traversal for searching for data, while also retrieving the related Frame summaries that are a more native variant for an LLM to understand logics and relations.This is a very very superifical explaination because to go into detail would take quite prolly multiplage pages of info.Important: Im running this on a local 5090 and it is NOT friendly in terms of amount of inferences (which is fine for me). I try to mimic a thought process not build a fast shipping product. Quality > quantity. If you would run DeepThought on any online inference provider your broke in 1 day.So, rn i focus on the ingestion and retrieval logics to make storing and retrieving as good as possible with my hw options.While the ingestions already involves multiple steps in which the "llm" basically works as judge to decide where to traverse in the graph, where to go into recursion and similar, this will become very relevant as soon ill start implementing "task execution" as capability.If i solved those the next point is to reduce everything that i need in terms of thinking steps in what i would call "thinking primitives". The idea with those is, that i dont want a hardcoded thinking process, but it rather also want to have the thinking process in form of a graph structure. This would allow me to compose the process in form of data in the hyepergraph, which would in return allow me to enable the system to refactor/enhance its own thought processes.So ye thats what im working on rn, very early concept/alpha phase.

reply

hackermanai
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Hackerman Text editor.

595 days and counting.ᕙ(⇀‸↼‶)ᕗ

reply

itrunsdoomguy
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Playing Doom.

reply

dorianmariecom
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

codedorian.com already more than 100 programs with ~30 users

it's a programming language

reply

runarberg
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I just started on an open source and open weight supervised learning model to recognize japanese kanji characters drawn on the screen.

I have a working prototype written in Julia which is a very simple neural network. The input is in vector format so traditional convolutional neural networks don’t work out of the box but I swapped the convolution layer with a path simplification algorithm and it worked extremely well. Like 20 samples per character (from a set of only 5 hiragana during prototype phase) was enough to get 100% accuracy in a test collection of 5 samples per character after only 30 iterations of training.I plan an working with free and open data, which I don‘t think exists for japanese kanji characters (at least not in vector format; KanjiVG only has one sample per character and I need dozens) so I also build a crowdsourcing web site to collect data from random people on the internet.I am planning to run some more experiments with my prototype model before I release the crowdsourcing web page to an actual server though.Model prototype:https://github.com/runarberg/kantoku-prototypeCrowdsource app:https://github.com/runarberg/kantoku-collector

reply

jason_zig
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

getting my 1-person business to 2M ARR[0]

the requirements for growth keep changing plus all the AI noise means that the playbook changes regularly. staying on top of the state of the market while improving/maintaining the product and understanding our icp + exploring new verticals is a tricky (but fun) task to manage![0]https://www.zigpoll.com

reply

nateb2022
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

Congrats, that's a huge achievement!! Curious where your ARR is approximately right now, and how long it's taken you to get to this point? What's your marketing strategy looked like, and is it just you running things?

reply

csomar
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on simpler, faster and lighter alternatives to CI/CD containers and merge queues.

Currently two products are beta-ready (merge conflicts/codeowners) and the demos are available here:https://codeinput.com/products/code-owners/demoand here:https://codeinput.com/products/merge-conflicts/demo

reply

netdur
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working 
https://vibu.app
 which is free digital voucher

and for fun, I am building yet another programming language!

reply

zsoltkacsandi
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

After some medical leave, writing the third post for my series about how Linux works: 
https://serversfor.dev/linux-inside-out/

reply

jansan
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I am working on an OpenType text shaper and renderer in Javascript and Rust with minimal memory requirements. Will allow complex scripts (Arabic, Devanagari, Thai, Khmer, etc.) rendering with standard TrueType fonts on embedded systems like a valilla esp32.

reply

steve_adams_86
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Lately I’ve been working on 
https://oceanconnect.ca

The original developer has left our organization so I’ve been tasked with general assessment and winding it down to enter maintenance mode. It’s still alive and well, has a very passionate and appreciative user base, but we want to ensure it doesn’t demand too much attention moving forward while we focus on other things. It has pretty noisy error reporting.Reliability and fault tolerance are some of my favourite things to work on in software so it has been a lot of fun so far. It has also been an incredible opportunity to practice using LLMs for specs, planning, verification, and research. I don’t actually need to output much code to get this thing into a stable state in which it can coast along; the bulk of the work is time spent understanding the app, the infrastructure, its existing faults, poring through traces and logs, going over query plans, and so on. LLMs are great assistants for this work and I’m having a ton of fun having so many opportunities to figure out what works and what doesn’t.The outcome has been awesome. The performance is steadily climbing (especially in the database), and most common errors when I started are either gone or much better understood with plans to address them. I’ve almost got it set up so if someone needs to take it over in the future, it should be pretty easy to toss them the keys and trust that they can deploy and maintain it easily from the docs and systems I’ve created.Despite spending a lot of my career on the front end, the hardest part of this project has been navigating that. Aiming to improve an application with minimal intervention is exceedingly difficult in the browser, or so I’ve been finding. I can get incredible performance gains out of Postgres without changing the interface between lambda and rds in the slightest, but meaningful improvements to the react application seem virtually impossible without substantial refactoring.I understand the key factors in getting better performance out of react apps and I see plenty of opportunities, but they all involve large diffs that are risky and time-consuming, even with a model like Opus handy to churn through boring and large change sets. It’s such a fragile and flaky environment.Even so, I’m loving it. Making software better is so gratifying. Doing it without reinventing the world is such a fun challenge, too. It really puts your brain to work. It would be so easy to go in and start flipping tables and throwing code in the garbage, but that’s too easy and too risky. Taking it slow, absorbing as much information as you can, truly understanding how features work, and planning surgical changes with significant pay off is safer and just feels awesome when it works.I’ll be sad when this one is finished. It’s almost there. Next up is a remote temperature controller for 40 saltwater experiment tanks with a temperature profile planning interface and a monitoring interface for the lab. That will be awesome too. It has been a good couple of months for work.

reply

platevoltage
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm working on a device that acts as a bridge between a video game sim wheel controller and a radio control car. It uses ESP32s on both ends, communicating using the ESP-NOW protocol. My client and I have been working on this for about 2 years now, and the final PCBs have just arrived. I did the coding and the board design in its entirety, and another freelancer designed the enclosure.

Unfortunately the only marketing material so far are some TikTok posts, but it's a pretty cool demonstration.https://www.tiktok.com/@kyo.simrc.racing

reply

syeare
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

No offense, but why doesn't anyone suspect these types of posts to be some corporate data farming?

reply

Joel_Mckay
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Drafting a small adaptive filter to deal with LLM generated email spam etc.

I don't often have time to do OSS projects, but will keep it readable for packagers. The most time consuming part will be overly verbose commenting needed for people to be able to audit the source quickly.It is a boring side-project, but unfortunately a necessary one. =3

reply

franze
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Airplane AI - an offline first AI that is GDPR and NDA safe by architecture - totally 100% offline as the main value proposition, not a limitation

reply

xerox13ster
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I got let go back in March, and since I've pivoted into building a game.
In the 3 weeks leading up to unemployment, I had gotten way more into an old GBA game I used to play back in the day, Harvest Moon Friends of Mineral Town. The (remake of the) game that inspired Eric Barone to make Stardew Valley. I was bumping into the same in-game limitations of the cartridge and platform that always made me want more from it, (and while Stardew Valley was nice, it never fully scratched that itch) and as I found myself unemployed, I found the mental space to start building.

The game is going to be a farming tycoon/city builder game where you can buy farm stands and advertise to sell your goods. As your operation grows, you grow the local economy and people move to the town turning it into a city, opening up the chance to sell at farmer's markets or supermarkets. As the city grows you'll have to buy/sell land with the city and work with the mayor to plan where the city should claim new land for you to purchase so you can stay on the outskirts with healthy soil (or in the endgame, run for mayor and manage the growth of the city yourself, a la Sim City/Cities/Frostpunk)I chose Love2D as my engine so I can use the relative simplicity of 2d art in 2.5D pseudo-3D instead of 3d modeling. The world space is a 3d euclidian grid of cells wrapped around a horizontal cylinder on the x axis. The view space is perpendicular to the side of the cylinder, giving us a natural horizon at the vertex of the cylinder on screen. The world space coordinates are expressed in terms of the polar coordinates of the cylinder, giving natural rise to radius as altitude, angle theta as latitude, and x axis as longitude. All the world math can be calculated using the trigonometry of the unit circle, and converted to 3d Cartesian coordinates before converting them to screenspace coordinates. I can use regular flat plans and elevations for the texutures of building faces, and render them upon linearly transformed quad polygons. Maybe I can also do some screenspace displacement a al Crimson Desert at the finish line to give buildings window sills and ledges when you see down a side of one.I am doing the development without LLMS as much as possible so I retain a good grasp on Logic, Language, and Math. I have been having a lot of fun digging back into these multivariable calculus and linear algebra concepts I thought were beyond me (because of some autobiographical amnesia issues I deal with) to discover that no wait, I was taught these concepts in high school and was quite comfortable applying them. All the development is done on my own private, secured git instance on my homelab server and I can pull down the latest revision to my iphone to show off, it's been really cool. Kind of a pita to find a good git app on iPhone that allows custom git servers with ports though.screenshot of a very early hello world, before I made the mental connection between wrapping a 2d cartesian plane around a cylinder and actual 3d cylindrical polar coordinates, which is why the shapes just sit over the world rather than extending from it, I hadn't yet conceived of the radius of the cylinder being altitude:https://fucci.dev/assets/helloworldspace.png

reply

ipunchghosts
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

I am writing synthetic aperture sonar/radar simulator and image formation code from scratch.

https://www.linkedin.com/search/results/all/?keywords=%23ape...Too many codes or old or gate kept behind proprietary walls. Many are old and don't use the newest acceleration techniquea to make the simulation fast. Additionally, none of them scale using aws. I want SAS/SAR image to be easy to generate for anyone.

reply

stavros
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

I wanted to get LLM feedback while writing without having the LLM suggest/write text for me, so I built 
https://www.writelucid.cc

reply

oulipo2
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

We're building a repairable and fireproof ebike battery at 
https://infinite-battery.com
 :)

reply

dismalaf
 
23 hours ago
 
 | 
prev
 | 
next
 
[–]

Economic simulation in Common Lisp.

reply

Marciplan
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

a little link sharing app: 
https://www.bundel.link
. It’s gimmicky, just annoying sharing multiple links to friends/family to plan trips or suggest gifts

reply

richarlidad
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

supplementdex.com - we read (every study) to provide clinical decision support for practitioners wanting to learn about dietary supplements

tldr: we help you find good supplement

reply

koeng
 
1 day ago
 
 | 
prev
 | 
next
 
[–]

Another thing I’m working on: homemade linen.

Right now I just germinated a 4x8 bed with flax for fiber. The plan is to grow it for 100 days or so and then harvest, dry, ret, dry, and spin. I need a lot more to do anything serious, but I think it’d be awesome to have a scarf that I made with linen I grew and harvested myself

reply

Jemm
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I got tired of the paywall surrounding cabinet design so I created 
https://cabinet.mycnc.app
. Just finished validating the door / drawer front gcode generator by milling a kitchen's worth of doors on a hobby grade CNC.

My thinking was that the money I saved doing the cabinets myself would be enough to pay for the Sienci Labs Longmill that I bought for the project.

reply

Almasy
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

like you

reply

opiniateddev
 
16 hours ago
 
 | 
prev
 
[–]

I'm working on Agentspan: 
https://github.com/agentspan-ai/agentspan

It's a durable runtime for AI agents.The thesis: agents should not just be an LLM loop running inside one Python process. Once agents touch real systems, you need crash recovery, retries, human approval, distributed tool execution, cancellation, observability, and execution history.Agentspan is basically applying the Conductor OSS execution model to agents. Conductor made long-running distributed workflows durable. Agentspan tries to do the same thing for agent executions: give every run an ID, persist the state, let it survive process death, pause for approval, resume later, and inspect what happened.

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