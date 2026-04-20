---
title: 'Charles Petzold: The Appalling Stupidity of Spotify’s AI DJ'
url: https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html
site_name: hackernews_api
content_file: hackernews_api-charles-petzold-the-appalling-stupidity-of-spotify
fetched_at: '2026-03-15T19:14:05.884955'
original_url: https://www.charlespetzold.com/blog/2026/02/The-Appalling-Stupidity-of-Spotifys-AI-DJ.html
author: Charles Petzold
date: '2026-03-15'
description: Charles Petzold is the author of the books Code and The Annotated Turing
tags:
- hackernews
- trending
---

Am I naïve in expecting Artificial Intelligence to be smart? Is my interpretation of the word “intelligence” too literal? And when an AI behaves stupidly, who’s to blame? The programmers or the AI entity itself? Is it even proper to make a distinction between the two? Or does the AI work in so mysterious a way that the programmers need no longer take responsibility?

I pondered these questions after I recently explored a new way to search for music in the Spotify app on my Android phone:

This is the portal to the AI-empowered Spotify DJ, and I optimistically wondered if this would finally fix longstanding blind spots in Spotify.

I should mention that my perspective might be a little different from most people’s because I don’t listen to pop songs. I prefer music of the 500-year tradition that encompasses (in roughly chronological order) composers such as Tallis, Byrd, Dowland, Gesualdo, Monteverdi, Lully, Blow, Corelli, Purcell, Vivaldi, Rameau, Handel, Bach, Scarlatti, Haydn, Mozart, Beethoven, Rossini, Schubert, Berlioz, Mendelssohn (Fanny and Felix), Schumann (Robert and Clara), Chopin, Liszt, Wagner, Verdi, Brahms, Puccini, Mahler, Debussy, Strauss, Beach, Schoenberg, Ives, Ravel, Stravinsky, Berg, Price, Copland, Shostakovich, Carter, Boulez, Gubaidulina, Pärt, Reich, Glass, Eastman, León, Adams, Saariaho, J. L. Adams, Wolfe, Higdon, Adès, Thorvaldsdottir, Mazzoli, Shaw, Fisher, and many others.

I’m aware that many people are unfamiliar with this musical tradition, but it forms one of the sturdiest pillars of what we casually refer to as “western civilization.” Plus, it’s a whole lot of really enthralling music.

Unfortunately, this tradition is not much respected in the sphere of digitized music. When I explored this issue back in 2009 in my blog entryClassical Music and MP3 Players, I discovered that the metadata associated with digital music files is based entirely on pop music. Each track is identified byArtist,Album, andSongtags.

Let me be clear: The use of the word “song” for instrumental music — that is, music that is not sung and hence is not a song — is borderline illiterate. It illustrates more than anything how the entire system is designed for pop songs. For music of the western tradition, the word “composition” or “work” or “piece” is used except, of course, if the composition is actually a song. In pop music, the “artist” is the performer; for music of the western tradition, the all-important composer is thrown in there along with the musicians or ensembles performing the music.

But the big problem is this:

Just as a novel is usually divided into chapters, many musical compositions consist of multiplemovements. Almost always, the movements of a musical composition are played together in sequence like the composer intended to give the composition an overall dramatic arc. Operas and oratorios are a little different, and often consist of acts divided intonumbers.

For example, Beethoven’s 7th Symphony has four movements that are generally identified numerically (I, II, III, and IV) or with names corresponding to Beethoven’s tempo markings. If you search for “Beethoven 7th Symphony” in Spotify, you’ll getAlbumsthat include this symphony but also aSongslist. Each of the “songs” in this list is an individual track of the album. They usually correspond to movements of the symphony but not in any coherent order. If nothing in the metadata indicates that these movements are part of a longer composition, Spotify remains ignorant of that fact.

Those of us who are familiar with the limitations of Spotify simply ignore the worthlessSongslist and go straight to theAlbums. Sometimes an album is devoted to a single composition, and sometimes an album includes multiple compositions, but the album tracks usually adequately identify the composition and the movements, and the movements are in the proper order.

But is there a better solution? Can AI fix this problem? Let’s try a few simple Spotify DJ requests:

Play Beethoven’s 7th Symphony

The DJ responds vocally with a promise to play what I requested plus “some other classical tracks to match” but instead of beginning with the 1st movement of the 7th Symphony, it plays instead the2ndmovement, which is the famous Allegretto that everybody knows and loves. Then it abandons Beethoven entirely to play the Intermezzo from the operaCavalleria Rusticanaby Pietro Mascagni (a composer born over 30 years after Beethoven’s death), and then one movement from a Shostakovich composition misidentified asJazz Suite No. 2, and then the Lacrimosa movement from Mozart’sRequiem, then an orchestrated Sarabande from Handel’sKeyboard Suite No. 4.

So let’s try to be more explicit.

Play Beethoven’s 7th Symphony in its entirety

The DJ says “Beethoven’s 7th Symphony. All 9 minutes of it.” All 9 minutes! It then plays just the Allegretto again, followed by aNocturneby John Field, and then the Andante movement of Bach’sBrandenburg Concerto No. 4.

Another approach:

Play Beethoven’s 7th Symphony from beginning to end

The DJ promises to play it “from start to finish.” The synonyms are encouraging. The DJ seems to know what I mean. “Let’s do this,” the DJ says. “Here’s the full Symphony by Ludwig van Beethoven.” Even more encouraging! But once again, it plays only the 2nd movement, followed by a John FieldNocturne.

How can this be? It is a fundamental concept that a musical composition often consists of multiple sequential movements. How can an AI built into Spotify be ignorant of this? Can it not even access the Wikipedia entrySymphony No. 7 (Beethoven)and learn about the movements from that? The first sentence of this article begins: “The Symphony No. 7 in A major, Op. 92, is a symphony in four movements...”

Let’s be even more explicit:

Play all four movements of Beethoven’s 7th Symphony

“All four movements. Let’s do this,” the DJ says. And finally, we hear the 1st movement of the 7th Symphony, followed by the 2nd movement but it’s a different recording with a different orchestra and a different conductor. That’s odd. This is followed by yet another orchestra and conductor playing… Yikes! It’s the4thmovement! After the 4th movement we get the 3rd movement, again with a different orchestra and conductor.

Imagine if Spotify read the last chapter of an audio book before the penultimate chapter! That’s how ridiculous this is.

Of course, I immediately realized that it wasmymistake. I was not specific enough. We all know that AI needs proper prompts. Let me spell it out:

Play all four movements of Beethoven’s 7th Symphony in numerical order

This time it begins with the 1st movement, but it’s not Beethoven’s 7th Symphony. It’s Beethoven’s3rdSymphony. That’s some great music but not what I asked for. This is followed by the 1st movement of the 7th Symphony, and but then continuing with the 3rd and 2nd movements in that order and skipping the 4th entirely.

The DJ then says that it’s going to “switch the vibe a little bit” and proceeds to play Aerosmith’s “Dream On,” the Beatles’ “A Day in the Life”, Pink Floyd’s “Shine On You Crazy Diamond,” and then I lost interest because it obviously doesn’t give a shit.

I’ve heard people claim thatan AI can compose music. But how can that be when it can’t even grasp basic concepts in music?

Of course, the Spotify DJ is still in beta, and I’m sure that these problems could be fixed by making the DJ a little “smarter” about all types of music, but I’m afraid that I’m skeptical. Let’s be realistic about this:

There is nothing less consequential to corporate profits than the preservation of the western musical tradition.
