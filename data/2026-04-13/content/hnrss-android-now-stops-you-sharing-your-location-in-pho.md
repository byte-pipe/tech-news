---
title: Android now stops you sharing your location in photos – Terence Eden’s Blog
url: https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/
site_name: hnrss
content_file: hnrss-android-now-stops-you-sharing-your-location-in-pho
fetched_at: '2026-04-13T20:05:37.905462'
original_url: https://shkspr.mobi/blog/2026/04/android-now-stops-you-sharing-your-location-in-photos/
author: Terence Eden
date: '2026-04-13'
published_date: '2026-04-13T12:34:48+01:00'
description: 'My wife and I run OpenBenches. It''s a niche little site which lets people share photos of memorial benches and their locations. Most modern phones embed a geolocation within the photo''s metadata, so we use that information to put the photos on a map. Google''s Android has now broken that. On the web, we used to use: ⧉ HTML<input type="file" accept="image/jpeg"> That opened the phone''s photo p…'
tags:
- hackernews
- hnrss
---

My wife and I runOpenBenches. It's a niche little site which lets people share photos of memorial benches and their locations. Most modern phones embed a geolocation within the photo's metadata, so we use that information to put the photos on a map.

Google's Android has now broken that.

On the web, we used to use:

⧉
 HTML
<
input

type
="file"
accept
="image/jpeg">

That opened the phone's photo picker and let the use upload a geotagged photo. But a while ago Google deliberately broke that.

Instead, we wereencourage to use thefilepicker:

⧉
 HTML
<
input

type
="file">

That opened the default file manager. This had the unfortunate side-effect of allowing the user to uploadanyfile, rather than just photos. But it did allow the EXIF metadata through unmolested.Then Google broke that as well.

Using a "Progressive Web App" doesn't work either.

So, can users transfer their photos via Bluetooth or QuickShare? No.That's now broken as well.

You can't even directly share via email without the location being stripped away.

Literally theonlyway to get a photo with geolocation intact is to plug in a USB cable, copy the photo to your computer, and then upload it via a desktop web browser?

## Why?!?!?

Because Google run an anticompetitive monopoly on their dominant mobile operating system.

Privacy.

There's a worry that users don't know they're taking photos with geolocation enabled. If you post a cute picture of your kid / jewellery / pint then there's a risk that a ne’er-do-well could find your exact location.

Most social media services are sensible and strip the location automatically. If you try to send a geotagged photo to Facebook / Mastodon / BlueSky / WhatsApp / etc, they default tonotshowing the location. You can add it in manually if you want, but anyone downloading your photo won't see the geotag.

And, you know, I get it. Google doesn't want the headline "Stalkers found me, kidnapped my baby, and stole my wedding ring - how a little known Android feature puts you in danger!"

But it is just sotiresomethat Google never consults their community. There was no advance notice of this change that I could find. Just a bunch of frustrated users in my inbox blaming me for breaking something.

I don't know what the answer is. Perhaps a pop up saying "This website wants to see the location of your photos. Yes / No / Always / Never"? People get tired of constant prompts and the wording will never be clear enough for most users.

It looks like the only option available will be to develop a native Android app (and an iOS one?!) with all the cost, effort, and admin that entails. Android apps havea special permission for accessing geolocation in images.

If anyone has aworkingway to let Android web-browsers access the full geolocation EXIF metadata of photos uploaded on the web, please drop a comment in the box.

In the meantime, please leave a +1 onthis HTML Spec comment.

## Share this post on…

## 9 thoughts on “Android now stops you sharing your location in photos”

1. ### Andrea GrandiRunning a similar project (@bookcorners.org) this really doesn't motivate me to build an Android client. One of the main feature is you select the picture and it uses geolocation to place the pin on the map and reverse the address. With this limitation users would have to manually enter everythingReply|Reply to original comment on bsky.app2026-04-13 12:53
2. ### news.ycombinator.comAndroid now stops you sharing your location in photos | Hacker NewsReply|Reply to original comment on2026-04-13 12:30
3. ### Josh Reimerthis is a necessary privacy feature in my books. Google is protecting me, the android user, by not letting location thru. I never want random websites to know my location. that's only for me to see in my gallery. so good to be seeing google taking more of a stand for privacyReply2026-04-13 13:56
4. ### Alex KirkWhy not just have people upload at location and use the Geolocation API to get their GPS coordinates? I’d prefer that much more than accidentally sharing the location through a photo.Reply|Reply to original comment on alex.kirk.at2026-04-13 14:16### Nick FitzsimonsThat would provide the location of where they uploaded the photo, not where they took it. There’s not much benefit in having the location of the armchair where they’re sat down having a nice cup of tea while they decide which photos to upload, a few hours after the walk on which they took them.Reply2026-04-13 19:12
5. ### Nick FitzsimonsThat would provide the location of where they uploaded the photo, not where they took it. There’s not much benefit in having the location of the armchair where they’re sat down having a nice cup of tea while they decide which photos to upload, a few hours after the walk on which they took them.Reply2026-04-13 19:12
6. ### Nanook@blogSomeday we'll create an Internet for adults where the end user actually has agency over their device(s) and what they choose to do with them.Reply|Reply to original comment on friendica.eskimo.com2026-04-13 14:30
7. ### 🌴 Seph 💭 👾@blogHonestly, in this day and age, just making photo location a setting would work just fine, whether its a button on the display like choosing the flash, or a system setting.Reply|Reply to original comment on blog.taursnd.haus2026-04-13 14:42
8. ### Chief Twat@blog> Most social media services are sensible and strip the location automaticallyindeed, after they saved it for their purpose.> Google never consults their communityActually I hope they were kicked (or forced) so hard for this default that they turned it off.Situation is not ideal for you, I understand that, I don't think a service with good faith should be made defunct for this. A switch or an override would be good instead.But for default geotagging, I'd say good riddance.Reply|Reply to original comment on mastodon.social2026-04-13 15:09
9. ### Roel van der PlankI had a similar problem, with my navigation app (navigateanymap.eu): I stored information in the exit part of an image.When sharing through email there was no problem, but sharing a picture with Signal or Whatsapp removed the exif information. So I added a zip step when sharing through these apps: both apps will remove exif information but not if the exif is inside a jpg file that is inside a zip file. A bit annoying, but made it working for me.Reply2026-04-13 15:47
10. ### More comments on Mastodon.

### What are your reckons?Cancel reply

All comments are moderated and may not be published immediately. Your email address willnotbe published.

Comment:

See allowed HTML elements:

<a href="" title="">

<abbr title="">

<acronym title="">

<b>

<blockquote cite="">

<br>

<cite>

<code>

<del datetime="">

<em>

<i>

<img src="" alt="" title="" srcset="">

<p>

<pre>

<q cite="">

<s>

<strike>

<strong>


Your Name (required):

Your Email (required):

Your Website (optional):



To respond on your own website, write a post which contains a link to this post - then enter the URl of your page here.Learn more about WebMentions.

URL/Permalink of your article
