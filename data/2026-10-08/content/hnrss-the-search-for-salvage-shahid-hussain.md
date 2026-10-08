---
title: The Search for Salvage | Shahid Hussain
url: https://shahidhussain.com/writing/search-for-salvage/
site_name: hnrss
content_file: hnrss-the-search-for-salvage-shahid-hussain
fetched_at: '2026-10-08T17:45:12.101934'
original_url: https://shahidhussain.com/writing/search-for-salvage/
author: Shahid Hussain
date: '2026-10-05'
published_date: '2026-09-29T00:00:00+00:00'
description: 15 years ago, a band called Salvage dropped an epic song, and then vanished without a trace. Until now.
tags:
- hackernews
- hnrss
---

Shahid Hussain

In 2011 I heard a piece of music that didn’t make any sense.

The music was a perfect piece of stadium indie rock – thoughtful but expansive, layered yet elegantly simple. The band was Salvage, and the two tracks on the CD I bought were called “Electric” and “Searchlights”.

For the last 15 years, these tracks have been a maddening contradiction. They are professionally produced – someone with obvious skill spent time and effort on these tracks. I wanted to find out who, and hear more of this goodness. I wanted to find out where they went. And I wanted to know why they were so darn hard to find – was it a side project by a session band? A producer with an idea and a spare few weeks?

Every few years, I would start a new search, convinced that there was an answer somewhere, and that I was missing a trick. If I just tried again, I would find it. And given where I work, you would expect that I would be good at finding things online.

But it’s been … frustratingly difficult.

* The band name and track names are generic. Search engines assume I wanted to know something about salvage companies, the much more likely option.
* I lost the physical disc a long time ago, so no clues from the back or the disc itself. The cover art survived in low resolution.
* There are at least three other bands called “Salvage” - a German heavy metal, a Brazilian math/post-rock band, and Dutch heavy hardcore band.
* I couldn’t remember exactly where or when I got it.
* In places where it does exist online, it’s called “Salvage Salvage” due to the repeated title in the cover art.
* The listed record label, Despatches, is tiny and also generically named.

This became an unsolvable problem, and over the last couple of years I have thrown every new wave of frontier AI models at it – both as a thought partner and for their proficiency with search tools. Nothing worked, and I figured that maybe the data was just lost to time.

Until now.

## Looking for Salvage

I created a prompt and dataset containing everything I knew - cover art, audio files, metadata and URLs for everything I had found, and gave it to one model. I instructed it to also keep a running log in an MD file with the investigation results – what it tried, what hadn’t worked, open hypotheses.

Then I downloaded the MD record, switched to a different model (with the same background data), asked it to recheck the latest and get new inputs, pushbacks and ideas.

* I already knew the disc was on discogs. So, we checked the Discogs label page and found a pending submission. Confirmed the Discogs entry holds no credits and no matrix or SID codes.
* AIs cropped and upscaled the sleeve. No label copy, no catalogue number, no URL, no credits.
* Both AIs gave me some new ideas for approaches we hadn’t tried.
* The AIs needed me as the meat proxy for the occasional item it couldn’t access, including Wayback Machine.

We found theOfficial Chartsentry, which confirmed this was a real thing but of course, made me question even more why there was no other record of it.

Number 47, Independent Singles Chart, week 4–10 June 2006.

From the charts entry we got a record of the Official Charts artist ID and confirmed one chart entry.

* We looked up the barcode on GS1 and traced it to Key Production in London. So now we know who shipped the disc.
* I emailed Key Production but of course, no reason they would reply to me, so no dice.

We searched Companies House and Discogs for “Despatches”, the record label. We foundthis pageon Discogs. Despatches had no company registration and no other releases, but we found one other act on the label. Anold Wikipedia mirrorlisted a band as being on “Despatches Records” during the right years, but further digging there just got us to a dead end.

So we looked at the digital data we have. We computed the CDDB disc ID and established that legacy ID lookups no longer work on gnudb. Then, we ran an AcoustID fingerprint lookup. No match. Ok, maybe it was just on a music service? We searched Spotify, Bandcamp, Last.fm, AllMusic, MusicBrainz, eBay. Dead end.

The AIs suggested that, if it was a professional band doing this as a test, parts of the lyrics might have survived as parts of other songs. So I transcribed the lyrics myself and handed them over for more aggressive searching. Dead end.

Searched SoundExchange’s ISRC database and all four unclaimed-royalty lists. Dead end.

On a whim, I searched for the song on Pandora. We hadn’t checked it before because it’s no longer a major music service, but it was in this era. And there it was! Seeing it here jogged my memory –thisis where I originally remembered hearing it for the first time. And then I remembered that this is why I bought the disc in the first place, and I pulled the original invoice out of my email, confirming an exact purchase date. I emailed the person I purchased it from, but that was a LONG time ago, so once again, dead end.

As we dug, we foundotherpeople who were searching for the same band. (Nice to know I wasn’t alone.)

I suggested that we might look for the band in combination with the participants. Maybe one of the members had it up on a credits page? So the AIs ran searches against the options, one of which was “producer”.Boom!We had never found this before because the disc title on this page is slightly misspelled (“Searchlight” rather than “Searchlights”). But now, we know that Salvage was produced by a genuine professional: Greg Haver, who also worked on theManic Street Preachersamong many others.

I shot an email over to Greg.

At the same time, I wondered if Greg had worked with one of the band members from Salvage elsewhere, so we drew up a shortlist of Greg’s other bands and I started working my way through his back catalogue, identifying possible options. I could do a better job than an AI at determining whether the singer, the playing style or the gear setup sounded familiar anywhere. I was ready to start sending out emails to 20-30 possible options, when Greg kindly responded and also connected me with the singer and guitar player, Sam Tattersall.

So what happened?

Shortly after this record, it turned out that Salvage changed their name to OK Tokyo, evading all my efforts to find them, until now.

Then they got the internet footprint I would have expected:

* MySpace
* Guardian interview
* Radio Berkshire interview
* Fan page on the internet archive

I later discovered that Salvage DID have a website, but …it was a flash siteand hence never indexed properly. There was also aMySpacebut, the internet archive never mirrored it, and it’s empty now.

## Salvage, the band

* Produced, Mixed & Engineered by Greg Haver
* Assistant Engineer “The Loz”
* Mastered by Shawn Joseph at Optimum Mastering Ltd

The band themselves:

* Vocals and Guitars: Sam Tattersall
* Bass: Jon Tattersall
* Drums: Matt Salvage (yes, Salvage!)

All songs written by Salvage.

Gear: Fender Telecaster, Fender P-bass, Pearl drums.

If you want to hear the track that started all this, you can hear it onYouTubeorApple Music.

## Interview with Sam Tattersall & Greg Haver

Sam kindly let me interview him, which I’ve reproduced here in full.

Q: These tracks have a pretty different feel vs. OK Tokyo – what led to the switch?

Sam: This really has opened up a trip down memory lane! Like most things - long story. We began life as Salvage - our original vision was to write music that moved people. The lofty aspirations of youth meant we really wanted to write big anthemic music that we hoped one day would lead to us playing to big audiences in big venues. These songs really were written from the heart - we poured everything into them. Initially we recorded some early demos in Atlanta but unfortunately worked with a Producer who didn’t really get what we were trying to do - whilst the songs were very strong, the production came out a bit confused/ sterile. Being based in London, we still managed to attract a fair bit of interest from the songwriting but the general feedback from the industry (mid 2000s) was that this genre of music wasn’t ‘in’ - I remember the industry would always say ‘you either needed to be NME’ (cool / quirky / indie) or Kerrang (heavy). We didn’t fit in either. We never really understood that as bands like Coldplay were dominating the charts at the time.

Having become fairly despondent that our dreams were fading fast, we were encouraged to try recording some new songs with a producer more aligned to what we were trying to achieve musically. To see if that could ‘unblock’ us as far as the industry went. We chatted to a few, but we really connected with Greg - who took the time to visit us where we rehearsed. Wanting to listen to us in the room aiming to capture the essence of how we played in the room. Like Atlanta - we had another 5 or so songs that we felt were strong. Greg listened to those and we recorded ‘Searchlights’ and ‘Electric’ in Cardiff. The entire recording process with Greg was absolutely incredible - it really makes me wonder what would have happened if we had recorded all the earlier tracks in Atlanta with Greg as one body of work……. I just listened to Electric. Bloody hell that brought it all back - and some incredibly vivid memories of it all coming together. Everything Greg suggested for the track made it 10 times better. Still remember it all to this day.

Maybe we were too close to our own music - but when we recorded those tracks with Greg - particularly ‘Electric’ we felt it was a last chance. Just a general sense that ‘well if they don’t like Electric then I don’t think we could write a better song for what we are trying to achieve’…… Unfortunately for us, the music industry feedback was broadly the same and I still remember one senior A&R guy from a major label saying to us “this song is something a band would drop on a 3rd album, not the 1st album. It’s too mature”. They all took a pass on Salvage - we were devastated having been convinced that if it could get a good platform it would do well…… I guess we could have just carried on - but it felt bleak back then so we decided to try something different.

Being fairly prolific at writing songs - we had quite a few that didn’t fit what we were trying to do with Salvage. So we decided to try a different style - still stuff we enjoyed playing but I guess having a bit more fun with it. At that stage it felt a bit like therapy. We went to a really basic local studio just to experiment with it and put ourselves in the chair to produce - not being entirely confident as to whether it would be any good! The resulting demo was nuts but we decided to just whack it up on myspace and to see what happened….. It’s fair to say the UK industry took more notice and we enjoyed some recognition and did some cool touring, supports etc and played at Glastonbury amongst a few other cool things. But still not able to secure a major label deal. Such a shame as again, we felt we had songs that would do really well if we could get them out there. It felt like that band had run its course in late 2008 so we decided to call it a day having been a bit burnt out by it all.

Q: What happened after OK Tokyo — did you all keep playing? If so, in which bands?

Sam: Having put everything into it - we walked away from the music industry for a while. Myself and Matt Salvage came back to it as songwriters under the name Glacier and Summit. Having written a fair bit for TV and Film projects but it’s obviously not the same thrill as the band days.

Q: How are you getting the sense of space in the record production? Reverb, dual tracking in stereo, something else?

Greg: As I’ve recorded hundreds, possibly thousands of songs in the 20 years since the Salvage session my memories (especially at my age) are a little hazy!

From what I can remember we tracked the songs in Cardiff, Wales at the Manic Street Preachers FASTER studios on the vintage Trident desk that was originally at Rockfield studios. The studio had (it’s no longer there) a great drum room and a good selection of vintage recording gear, we also used quite a bit of the Manics instruments and amps which were available for us to use.

We would have tracked drums with guide guitars and vocals until we got the drum takes we wanted and then recorded bass before we layered up and double tracked the guitars and tracked Sam’s vocals. I was looking for big epic sounds with lots of timed delays and reverbs. The band were all great players so my job was pretty easy as all I needed to do was get some good sounds up and capture their energy. I also mixed the songs on the same session on the desk, manually as we had no recalls - old skool! Mastering was done by Shawn Joseph at Optimum.

## End of the search

Greg kindly shared some high resolution images of the frontand backof the CD slipcase, which I’ve reproduced here.

 

I hope that no-one will have to search for this band again.

Huge, massive thanks to both Greg and Sam for connecting and responding, and adding such wonderful colour to the end of this story.

* If you want to hear more of Greg’s work,check out his showreel.
* If you want to hear more of Sam / Jon and Matt’s work, check out OK Tokyo onYouTube,Spotify, or Glacier and Summit onSpotifyorApple Music

* Website
* Email
* Linkedin
* Instagram
* Bluesky

© Shahid Hussain. All rights reserved.