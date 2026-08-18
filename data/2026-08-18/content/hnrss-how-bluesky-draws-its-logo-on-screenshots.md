---
title: How Bluesky draws its logo on screenshots
url: https://timmarinin.net/2026/bluesky-screenshots/
site_name: hnrss
content_file: hnrss-how-bluesky-draws-its-logo-on-screenshots
fetched_at: '2026-08-18T12:12:06.692600'
original_url: https://timmarinin.net/2026/bluesky-screenshots/
date: '2026-08-17'
description: How Bluesky draws its logo on screenshots
tags:
- hackernews
- hnrss
---

# How Bluesky draws its logo on screenshots

Sometimes I take a screenshot of a post I like, either to send it to friends/meme channel or to save a “durable” copy. Like this one (I’ve cropped out the rest of the interface):

Original
, if you want to reskeet it

I noticed the Bluesky logo in the right corner and thought that it was weird that the logo doesn’t bother me when I use the app. Then I looked at the post in the app again—logo wasn’t there, replaced by the “Follow” button.

I remembered that a few apps hide their logo where the iPhone notch is, so that it doesn’t stick out, unless you take a screenshot. But here the logo is placed in the open, so how do they do it?

I tried to take another screenshot, this time mid-switching to the other app:

The “Follow” button is visible when I take the screenshot mid-switch.

Did they somehow set up a listener for two buttons I’m pressing to take a screenshot and do a switcheroo at the last moment? I’m not an iOS developer, so I’m not sure what’s possible and what is not over there.

At this point I was mildly intrigued. Thankfully, I remembered that Bluesky app is open source (or at least the code is available to look at).

The answer was in the file literally calledGrowthHack.tsx, introduced in January 2026 bymozzius. But it merely used a dependency, so to understand I looked into packageexpo-privacy-sensitive, also by them.

The package createsUITextFieldwithisSecureTextEntryproperty set to true and renders the actual content (the button) into that field’s.layer. When I take the screenshot, iOS hides this UITextField by blanking the layer, allowing the Bluesky logo to flutter its wings through (it was here the whooole time). For other platforms it simply renders content as-is, without masking.

Why doesn’t it work when I switch between the apps? I suppose that iOS takes a snapshot itself at the start of the gesture (without triggering blanking), and when I do a screenshot, there is no live UITextField instance to react to that, only the inert snapshot. But once again, I’m not an iOS developer.

Nifty trick or an abuse of API meant for privacy? The people inthe thread adding the behaviormostly didn’t like it, before the thread got locked. I think it’s cute.

I googled a bit, and the trick is well-known. Telegram implementedsimilar thing for its "secret" chats, as didSignal, so I don’t expect it to be patched by Apple any time soon.

	
	
		
		
			
			Published
			at 
Sunday, 16 August 2026
 
			by 
mt