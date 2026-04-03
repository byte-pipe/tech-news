---
title: 'Album Cards: Rebuilding the Joy of Music Discovery for My 10-Year-Old'
url: https://fulghum.io/album-cards
site_name: hackernews
fetched_at: '2025-10-11T11:08:39.910094'
original_url: https://fulghum.io/album-cards
author: Jordan Fulghum
date: '2025-10-11'
published_date: '2025-01-15T00:00:00Z'
description: What's the modern equivalent of flipping through CDs? Physical album cards with NFC tags that bring back the tactile joy of music discovery.
---

# Album Cards: Rebuilding the Joy of Music Discovery for My 10-Year-Old

byJordan Fulghum, October 2025

Albums you can hold again.

When I was 10, I blew every dollar I had on CDs. I remember sitting cross-legged on my floor, flipping through jewel cases, memorizing liner notes and lyrics, and most importantly developing my own taste for music.

My 10-year-old doesn't have that. Music just sort of... happens. It's like it's infinite and invisible at the same time, playing from smart speakers, car stereos, my phone. Endless perfectly curated playlists, designed to fade into the background. The default listening experience has become both literally and figuratively formless.

So I thought: what's the modern equivalent of that CD browsing experience? Maybe what's missing is something tangible that he can flip through, or even collect.

I could combine my old CD-collector brain with today's tech: take something fun and collectable (trading cards), dress them up with album art, and add NFC tags so they can be tapped to play the album on our home speaker system, all without a screen.

Away I went.

The finished product. Pick a card, any card.

## The Setup

I needed to get the music into a format that could be played. I've long since surrendered to streaming, but I still have my MP3s organized viaPlexon my home server. Funny to think that these files are the same MP3s that I've been collecting since the late 90s. I wanted the NFC tag to be deep-linked to those same files instead of a streaming service.

But which albums do I pick? I had the idea to create themed "packs" of albums. The first pack is obviously "Albums That Dad Wants You to Listen To", and it's just a bunch of dad rock. But the idea is that each pack can be a different theme or genre, and he can build his own collection (and develop his own taste) over time.

## Making em

I found a PDF template that matched the dimensions of trading cards, hopped intoCanvaand got to work. It was easy enough to find high-quality album cover images from Google, but....

### The Aspect Ratio Goof

I was quite far into this project when I remembered the obvious fact that album art is square but trading cards are rectangular. Trading cards use a 2.5:3.5 aspect ratio, which is...not a square! Oops.

I looked at what they did for cassette tapes (also rectangular) back in the day, but their solutions were all over the place, from just cropping the square into a rectangle (gross) to having a giant white space next to the square art. That wasn't gonna cut it.

So, I used an AI diffusion model to extend each album's art into a trading card aspect ratio. The AI was (mostly) able to extend the artwork while maintaining the original style and composition. Not perfect, but a pretty fun solution not possible just a couple years ago.

I used AI to extend the album art to the trading card aspect ratio. Highlighted are the generated parts of the artwork, including the Marina City Towers which tripped up the model quite a bit, surprisingly. For
Nevermind
, I just dropped in a solid blue, color-matched rectangle. Take that, AI.

After ordering a bundle of blank NFC tags from Amazon, I learned thatPlexAmpoddly has first-class support for zapping NFC tags to specific albums in auto play mode. A strange feature, but perfect for this project. Easy.

NFC assembly line

The process was simple: open PlexAmp, navigate to an album, tap the three dots menu, and there's a "Program NFC Tag" option. Hold your phone over the blank NFC tag and it writes the deep link. That's it. The tag just contains a URL that opens PlexAmp and starts playing that specific album when tapped.

I printed the cards on our crappy HP inkjet printer at home. I used label paper that exactly matched the dimensions of trading cards, but after the fact, I realized it was kind of unnecessary. You can just print on cardstock if you have a digital template file. I cut them out and glued them to blank playing cards, but not before wedging the NFC tags between.

The grass on the lower-third of this card is not naturally occurring.

For placement, I found a trading card display model fromMakerworldand 3D printed it on myA1. It turned out alright!

Once it was all working and in decent shape, I presented them in a nice neat arrangement to my son. He flipped through them like Pokémon cards, examined the cards that were the most visually interesting. Daft Punk'sDiscoverywas his first pick. He grabbed it, flipped it around, tapped it, and thatOne More Timeloop dropped throughout our entire house. Boom.

Don't look too closely at the corners, oof.

I was happy to see that the physical cards encouraged active listening and ownership. Instead of music being background noise, it became something he could choose, hold, explore, maybe even trade with his sister!

It was all worth it for her reaction. And yes, I know she's just giddy about the naked baby.

I think we're unintentionally teaching our children to consume music passively. My goal with this project was to teach them to discover it actively, to own it, to care about it at the album level. I think it kinda worked!
