---
title: Portfolio Update, I Guess - DEV Community
url: https://dev.to/adamthedeveloper/portfolio-update-i-guess-4ob3
site_name: devto
content_file: devto-portfolio-update-i-guess-dev-community
fetched_at: '2026-08-27T20:57:31.231604'
original_url: https://dev.to/adamthedeveloper/portfolio-update-i-guess-4ob3
author: Adam - The Developer ✨
date: '2026-08-26'
description: This isn't my main piece for the week, it's more of a "contributes nothing to knowledge" kind of... Tagged with webdev, programming, productivity, javascript.
tags: '#webdev, #programming, #productivity, #javascript'
---

Features a hilarious edgy teenage mode toggle

This isn't my main piece for the week, it's more of a "contributes nothing to knowledge" kind of post.

Last week I took another look at my portfolio and thought, "Hey, why not make this feel a bit more like me?" So I set out to give it a makeover, stuffed as much of my personality into it as I could, and et voilà, done.

The old one was kinda too formal.

TL;DR:I gave my portfolio a personality transplant. If you'd rather just look than read:a-thedeveloper.vercel.app

## Vibe / Tone Option

By default, the professional option is enabled. But if you're not too sensitive and want to have a little fun, try toggling over to the unfiltered version of me, lol.

I don't actually talk like that in real life anymore, but having grown up speaking English, that's pretty much how I sounded back in my teenage years. I was a grumpy teenager like everyone else, the difference is I wasextragrumpy compared to most. 😭 I also lost access to my Instagram account, so all of it is still sitting there, public, for anyone to see. Every day I hope that account just quietly gets deleted.

And if you're wondering whether that same energy has been erased, nope, it's still very much here. I just keep it contained to appropriate contexts now, lol.

I also found these while digging through my old microsoft drive, weird 16 year old me stuff. I actually said this in a debate, by the way. Can't remember if my team won that one or lost.

## Weather Options

Kinda irrelevant to how it actually describes my portfolio, but I initially wanted to makerainythe only option, because I'm a big fan of dark, gloomy, cloudy weather — the kind that makes England look like heaven to me. 😭

Then I thought,why not just have all of them?So now each weather option comes with its own falling elements based on the selection, plus music that I feel fits the atmosphere.

Again, it doesn't really serve any practical purpose, but I think it's a nice little touch to have, haha.

## DEV Writing Views with an API Key

When I joined DEV in 2023, I saw the option to generate an API key. I had no idea what it was for and didn't bother checking the docs, I just assumed that to display your articles on your own site, you'd need one. Turns out: yes and no. DEV already gives you a public URL you can use to showcase your articles without any API key at all but they don't give you the views.

I was browsing around and came across thisarticleby@ketanchavan

and I thought, ohhh, maybe it'd be nice to show view counts on the articles displayed on my portfolio too. So I did.

With this block of code:

async
 
function
 
fetchFromUpstream
():
 
Promise
<
DevToArticle
[]
>
 
{

 
const
 
apiKey
 
=
 
process
.
env
.
DEVTO_API_KEY
;

 
if 
(
!
apiKey
)
 
{

 
throw
 
new
 
Error
(
"
DEVTO_API_KEY is not configured
"
);

 
}

 
const
 
upstreamResponse
 
=
 
await
 
fetch
(
DEVTO_PUBLISHED_URL
,
 
{

 
headers
:
 
{

 
"
api-key
"
:
 
apiKey
,

 
Accept
:
 
"
application/json
"
,

 
},

 
});

 
if 
(
!
upstreamResponse
.
ok
)
 
{

 
throw
 
new
 
Error
(
`Failed to fetch dev articles (
${
upstreamResponse
.
status
}
)`
);

 
}

 
const
 
payload
 
=
 
(
await
 
upstreamResponse
.
json
())
 
as
 
DevToArticlePayload
[];

 
return
 
mapArticles
(
payload
);

}

Enter fullscreen mode

Exit fullscreen mode

I got this!!

Beautiful!!!

## Finally, The Archives

Of course I know version control, but it's way better when I can see all of them at once, in pictures.

I've changed my portfolio's design multiple times over the years, ever since I first built one back in 2023, just two years into my professional career. Yeah, I already had a portfolio after landing my second job as a software engineer. Looking back, that's kinda crazy.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse