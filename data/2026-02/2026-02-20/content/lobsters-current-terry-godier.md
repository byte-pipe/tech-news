---
title: Current | Terry Godier
url: https://www.terrygodier.com/current
site_name: lobsters
content_file: lobsters-current-terry-godier
fetched_at: '2026-02-20T06:00:27.937260'
original_url: https://www.terrygodier.com/current
author: https://indieweb.social/@tg
date: '2026-02-20'
published_date: '2026-02-17T12:30:00.000Z'
description: An RSS reader that doesn't count. What happens when you stop treating your feeds like an inbox and start treating them like a river.
tags: design, mobile
---

847
unread

# Current

An RSS reader

I started building Current before I had the words for why.

The impulse was simpler than a philosophy: every RSS reader I tried made me feel bad. Not because the apps were ugly or broken (most were quite good) but because they all seemed to agree on something I didn't. That reading the internet was a task. That articles were items to be processed. That falling behind was a failure state.

I didn't have a name for this yet. I just knew I wanted a reader that didn't make me feel like I owed it something.

The app was nearly finished when I sat down, in January, to write about what I'd been building against. I traced the feeling back to Brent Simmons and NetNewsWire in 2002, a pragmatic design decision that calcified into convention. I named the feelingphantom obligation: the guilt you feel for something no one asked you to do.

The essay was a retrospective. The thing I'd been trying to articulate in code for months, finally put into words.

This is Current.

## The River

Every RSS reader I've used presents your feeds as a list to be processed. Items arrive. They're marked unread. Your job is to get that number to zero, or at least closer to zero than it was yesterday.

Current has no unread count. Not because I forgot to add one, or because I thought it would look cleaner without it. There is no count becausecounting was the problem.

The main screen is a river. Not a river that moves on its own. You're not watching content drift past like a screensaver. It's a river in the sense that matters: content arrives, lingers for a time, and then fades away.

Inbox
3
Why the browser wars matter again
Apple's new framework strategy
The death of the algorithm
River
Why the browser wars matter again
Apple's new framework strategy
The death of the algorithm
Web components in 2026
A better way to think about state
RSS is not dead
The indie web is growing
accumulates
ages naturally

Each article has avelocity, a measure of how quickly it ages. Breaking news burns bright for three hours. A daily article stays relevant for eighteen. An essay lingers for three days. An evergreen tutorial might sit in your river for a week.

As items age, they dim. Eventually they're gone, carried downstream. You don't mark them as read. You don't file them. They simply pass, the way water passes under a bridge.

Information has a natural lifespan, and the interface should honor that.

The river is what's here right now. You scroll through it, save what you want to keep, and let the rest go.

## The Half-Life

Velocity is what makes the river work. Every source in Current has a half-life that you set: how long its articles stay visible before fading out.

A breaking-news feed like BBC World gets three hours. Ars Technica might get eighteen. A slow, thoughtful source like Aeon or The Marginalian gets a full week. The same river carries all of them, but each piece ages at its own pace.

Breaking
3 hours
Article
18 hours
Evergreen
7 days
published
aged out

This solves a problem that has haunted every chronological feed since Google Reader: a single prolific source drowning out everything else. When The Verge posts twenty articles in a day, those articles age out in hours. When Craig Mod publishes once a month, that essay stays in your river for days. Because it was meant to.

The onboarding shows you five speeds: Breaking, News, Article, Essay, Evergreen. You pick one per source. The river handles the rest.

Five speeds. One river.

## Release

Most RSS readers ask you to “mark as read.” Think about what that language implies. You're granting the article a status change, like an administrator processing paperwork.Read. Filed. Handled.

Current asks you torelease.

You can release from anywhere. In the river, a long swipe left on a card sends it flying off the screen. The remaining cards settle into the gap, the way water fills a space. One article, one gesture, gone.

Ars Technica
The new web standards nobody asked for
kottke.org
The quiet beauty of maintenance
Platformer
What happens after the algorithm
Robin Rendle
A letter to the web we lost

But you can also release from inside an article. Reach the end, and a release button flows up from the bottom of the screen. Tap it and you're back in the river, the article already gone. You never have to scroll back up and find the card you just read. The app knows where you are.

The physics are deliberate everywhere. The card compresses slightly as you drag, building tension. Your phone's haptic engine taps with increasing urgency as you approach the threshold. A warm glow appears at the edge. Past the trigger point, the card flies away and the remaining cards settle into place. There's an undo window. Released articles stay in memory for a few seconds before the release commits. Swipe wrong? Tap undo. No drama, no confirmation dialogs.

Tap, read, release.

## Tuning Your River

Every source is different, and Current lets you treat them that way.

Beyond velocity, each source has a set of options that shape how its content appears in the river. You can fetch the full article from the web, bypassing feeds that only give you a teaser paragraph. You can mark a source as a webcomic, which unlocks an image-first reader with zoom, pan, and alt-text display, built for XKCD and its kin. You can mute a source for a week when you need a break, or pin one to the top of the river when you never want to miss it.

These aren't buried in a settings menu. They're one swipe away, attached to every source. The reader adapts to the content, not the other way around.

## The River Speaks

Current watches your habits. Not to manipulate you, but to help you tend the river.

When a source floods your feed with eighteen posts in a day, a quiet card appears between articles:“The Verge posted 18 items today.”With options to rate-limit or quiet the source. When you've skipped ten straight articles from the same source, Current notices:“You've skipped 10 from TechCrunch. Quiet or remove?”

When you keep reading everything from a particular source:“You keep reading Craig Mod. Pin to the top?”When you keep reading about the same topic across different sources:“You keep reading design. Want a design Current?”

~

The Verge posted 18 items today.

Rate-limit
Quiet 24h

These aren't algorithmic recommendations. They're not trying to maximize engagement or steal your attention. They're a librarian noticing your habits and quietly rearranging the shelves.

All of the intelligence behind these cards runs entirely on your device. Natural language processing identifies topics. Foundation Models, when available, help verify that related articles are truly about the same story. Nothing leaves your phone. Nothing is sent to a server. The river is yours.

## Voices

This is the feature I'm most proud of, and the one I spent the longest agonizing over.

Most RSS readers present sources as feed URLs in a sidebar.Daring Fireball. kottke.org. Hacker News.Just names in a list, undifferentiated from each other and from the content they produce.

But some of those aren't publications. They're people. A person writing from their blog is fundamentally different from a news organization publishing articles. The relationship is different. The expectation is different. The feeling should be different.

You don't subscribe to a person. You follow a voice.

Mark a feed as a voice, and it gets its own space. The Voices tab gathers these people into a timeline, their posts woven together chronologically so you can follow the conversation. Active voices appear in full color at the top; quieter ones fade to greyscale, still there but not demanding attention.

CM
RO
AD
JK
RR
BS
MF
TL
NW
CM
Walking the Tōkaidō
2h ago
RO
On the limits of language models
5h ago

voices, people not feeds

Tap any voice to filter the timeline to just their writing. On iPad, your voices live in the sidebar with their name and favicon, a quick glance at who's been thinking. On iPhone and Mac, a scrollable row of faces sits above the timeline.

Current detects personal blogs automatically (subdomain patterns, post frequency, byline signals) and gently suggests marking them as voices. But the choice is always yours. Not every blog with one writer wants to be treated as a person. Some are projects. You know the difference.

A timeline of the people you follow.

## Currents

River is the default view, everything flowing together. But sometimes you want to narrow the stream.

Currents are collections. You might have one for technology, one for cooking, one for the people you actually know. They sit in a horizontal bar at the top of the screen, one swipe away from each other.

I thought carefully about what to call them. “Folders” implies filing, which implies obligation. “Categories” sounds like a spreadsheet.Currentsfelt right. Smaller streams within the larger river. Each one flows the same way, just carrying different things.

Three Currents are built in:River(everything),Voices(people you follow), andRead Later(articles you've saved, cached for offline reading, marked with warm amber because these areyours). Beyond those, you create whatever you need. The dynamic cards will even suggest new Currents when they notice patterns in your reading.

River, Voices, Read Later, and whatever you need.

## Calm by Design

Every interface is an argument about how you should feel.

That line is from the Phantom Obligation essay, and it became the design system's first principle. If an interface argues through its visual language, then every color, every typeface, every pixel of spacing is a word in that argument.

Current's design system has a tagline, written in the source code where only I would read it:Calm but not boring. Beautiful but not loud. Typography as hero. Color as punctuation.

The body text is serif. The iOS system serif at 16 to 18 points, scaling with Dynamic Type. In a world of sans-serif apps, this is a deliberate choice. Serif type has been the standard for extended reading for five hundred years because it works. It guides the eye along the line. It whispersthis is for readingbefore you've read a word. The reader view bumps up to 18-point serif for even deeper immersion, with a separate “poetic” typography tier for empty states and contemplative moments.

There are nine color palettes, each with light and dark variants.Brightis clean iOS blue, familiar and sharp.Paperis warm ivory and amber, reading by candlelight.Oceanis cool teal and seafoam.Duskis soft violet and lavender, for the late hours.Emberis warm rust and rose, like reading by a fire.Midnightis true OLED black, because sometimes the best frame is no frame at all.Slateis a code-editor palette, cool and focused.Terminalis phosphor green on black, for those of us who remember CRTs.Solarizedis Ethan Schoonover's precision palette, for the discerning.

Bright
Craig Mod
Walking and the weight of attention
There is a particular quality of light in the early morning that makes everything feel possible...
saved
8 min read

Colors are semantic, not decorative. Warm amber always means “yours”: a saved article, a personal collection. Fresh teal always means “new.” Success is always a sage green. Error is always the same red. You learn the language without being taught it.

## Motion & Touch

Animation in Current isn't decorative. It's vocabulary.

There are five timing tiers, each with a purpose.Instant(0.15 seconds) for micro-feedback.Quick(0.22s) for primary interactions.Standard(0.28s) for card movements.Gentle(0.35s) for panels.Smooth(0.45s) for ambient motion. Consistent timing builds subconscious trust. Your nervous system learns the rhythm even if your conscious mind doesn't.

The background has its own language. Five flowing lines, sine waves with unique amplitudes and phases, drift slowly across the screen. They're barely visible, more felt than seen. I call them CurrentLines. They make the app feel alive without competing for your attention.

currentlines, ambient motion

Haptics are communication, not decoration. The release gesture is the most complex pattern: at 50% tension, a tap saysalmost there. Rhythmic pulses accelerate as you approach the threshold, like a heartbeat quickening. At the trigger point, a heavy tap followed by a soft tap creates a two-part confirmation your hand learns to anticipate. There are quieter moments too. A barely-there exhale when the river settles after scrolling, a gentle pulse when you open a voice's writing.

haptic timeline
release gesture
start drag
tension builds
confirm

When reduce motion is enabled, everything goes still. No exceptions, no compromises. The ambient lines disappear. Transitions become instant. Accessibility isn't a feature toggle. It's a design constraint that made the whole system better.

## Four Swipes

Every card in the river has four gesture slots: short swipe left, long swipe left, short swipe right, long swipe right. Each one is configurable. The defaults are what I think most people want (short-left to mark read, long-left to release, short-right to save, long-right to share) but you can remap any slot to any action: mark read, mark unread, release, save, mute the source, edit the source, share, or nothing at all.

The settings screen has a live preview card you can swipe to test your configuration before committing. Short swipes and long swipes trigger at different thresholds, with distinct haptic feedback at each stage so you always know which action you're about to invoke.

## The Small Things

Swipe from the left edge to search. Swipe from the right edge for settings. The first few times you approach these edges, a hint peeks out to teach you they're there. After three appearances, the hints retire. You know now.

Reading progress is tracked with human language, not percentages. An article you started shows“Just started.”One you're halfway through says exactly that. These labels appear on the card in the river, so you know where you left off without thinking about it.

Full-text search indexes everything you've touched. Every article you've scrolled past, every piece you've read. Instant results as you type. Your feeds become a searchable memory.

Read Later is a library, not a queue. Saved articles are cached for offline reading. They don't expire. They don't count against you. They wait, the way books wait on a shelf.

## Beyond the Phone

Current isn't an iPhone app that tolerates larger screens. The iPad and Mac versions are built as their own experiences, designed for what each platform does best.

On iPad, the river gains acollapsible sidebar. Your sources, Currents, and Voices live in a panel that slides in when you need it and disappears when you don't. In landscape, the sidebar and reader sit side by side. Tap an article in the river and it opens beside it, so you never lose your place. In portrait, the sidebar tucks away and the river takes the full screen, just like the phone.

On Mac, Current becomes a keyboard-first app.Command-Kopens a command palette that puts every action at your fingertips: switch Currents, jump to a source, search your river, change themes. No menus to dig through. If you know what you want, you're already there.

Command-K. Type what you want. Go.

And then there'sSift, a mode designed for the way people actually triage on a desktop. Hit a key and the river becomes a rapid-fire review: each article fills the screen, and you press a single key to release, save, or skip. It's the river distilled to its purest form. A stack of cards and your judgment.

Sift. One article, one key, keep moving.

## What I Left Out

This section matters as much to me as the features.

There are no unread counts. Not “not yet”. Never.This is philosophical, not practical. An unread count would make Current a better RSSmanagerand a worse RSSreader. I chose reader.

There is no three-pane layout.No sidebar of feeds, no list of items, no reading pane. Brent Simmons, who invented that layout in 2002, spent twenty years wondering why everyone kept copying him. I took him seriously.

There is no algorithmic curation.Social media learned that you could replace phantom obligation with a different poison, the fear of missing something happeningright now. Current doesn't rank or prioritize your content. The river flows in the order it arrives, shaped only by the velocities you set.

Story threading is built but disabled.I built a system that groups related articles from different sources into narrative threads, verified by on-device Foundation Models. It works technically. The presentation isn't right yet. I'd rather ship with it off than ship it half-baked. It will arrive when it's ready, or it won't arrive at all.

The performance budget is real.Sixty frames per second on all devices. Under 150 megabytes of memory during scroll. Sometimes this means saying no to a beautiful animation. The ambient CurrentLines run at 30 fps, not 60, to leave headroom. Some transitions are simpler than their prototypes because the prototypes dropped frames on older hardware.Performance is a feature. Jank is a bug.

I started building Current because every reader I tried had the same underlying assumption: that my feeds were a backlog and my job was to clear it.

The river was the way out. Content that arrives, lingers, and fades. Velocity instead of counts. Release instead of processing. A reader that doesn't keep score.

Making a metaphor feel like software took longer than I expected. Every decision, from the half-life of a breaking news article to the interval between haptic taps to the exact opacity at which an aged-out essay finally disappears, had to serve the same argument:you are not behind.

I didn't get everything right. I know that. But Current is the reader I want to use every morning, and I hope it becomes one you want to use too.

The river is flowing.Come sit by the water.
