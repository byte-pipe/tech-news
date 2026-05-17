---
title: Chat to build and schedule your own personal Hacker News email digest! 🎉 - DEV Community
url: https://dev.to/anmolbaranwal/chat-to-build-and-schedule-your-own-personal-hacker-news-email-digest-42a4
site_name: devto
content_file: devto-chat-to-build-and-schedule-your-own-personal-hacke
fetched_at: '2026-05-17T11:28:32.833575'
original_url: https://dev.to/anmolbaranwal/chat-to-build-and-schedule-your-own-personal-hacker-news-email-digest-42a4
author: Anmol Baranwal
date: '2026-05-16'
description: I have been working on a side project for the past few weeks and finally got it polished enough to... Tagged with showdev, react, opensource, programming.
tags: '#showdev, #react, #opensource, #programming'
---

I have been working on a side project for the past few weeks and finally got it polished enough to share.

Hacker News is one of my favorite places to keep up with tech and come across good discussions. But there's so much happening there that I kept missing the posts I actually cared about.

Even checking it twice a day, the front page rarely lines up with my interests. Tried a few existing Hacker News newsletters, but they were too generic -- everyone gets the same top stories.

So I figured, why not let myself and others build their own email digest from live data and schedule it whenever they want? That's why I builtHN Digest.

You can chat to build your own personalized Hacker News newsletter, preview it live with real HN data, and schedule it to your inbox -- daily, weekly, or monthly, 70+ timezones, no password, all free.

Here is theGitHub Repositoryand you can try it live athndigest.vercel.app.

Here's what it does and how I built it, along with the architecture.

## What it does

You just have to describe whatever you want in the chat editor: security news, ask HN, trending posts, discussions, show hn - it adds them to your newsletter.

There are 10 section types with per-section filters for keyword, timeframe (24h to 30d), minimum upvotes and story count.

So you can say "security news from the last 48 hours plus recent Show HN" -- it picks the right sections and applies the filters. Preview is a live React Email render so what you see is the actual email.

You can also just ask the chat:

* to show all the sections available
* delete or reorder
* change the theme (light/dark) of the newsletter

Clicking a story's title takes you to the original site. Clicking comments takes you to the HN post.

Once you are happy, just activate using a magic link. You will need a Resend API key -- their free tier is 3000 emails/month, you will use about 30 even if you send daily.

Sends go through your Resend key (and your quota, not mine). You can pause or delete anytime from the dashboard.

Yes, it lands in my inbox every day but I often forget about it. I definitely need to change the time to evening! 🤣

I have included aself-host guidein the readme docs as well.

Here is the stack:

* Resend+React Emailfor delivery
* CopilotKit+ Next.js for the chat editor
* Neon Postgresfor the database
* Upstash QStashfor scheduling
* Firebase Hacker News API + Algolia for live data
* AES-256-GCM for key encryption, JWT for auth

Fun fact: I have tried different ways to solve this problem before (web scraping, GitHub Actions) & I believe this is the most practical solution out of all the rest.

## How it works

Here's the high-level flow.

Browser (editor + chat + live preview)
 ├→ /api/copilotkit → LLM returns tool calls
 ├→ /api/preview → React Email render → iframe
 └→ /api/activate → encrypt key → Neon → create QStash schedule
 ↓ (HTTP cron callback)
 /api/send → Neon (fetch schedule)
 → User's Resend (send)

Enter fullscreen mode

Exit fullscreen mode

The chat doesn't directly write to the database. The LLM's tool calls only update the browser state. Nothing gets persisted to Neon until you hit "Activate". That's the only path that writes to the DB and creates a QStash schedule.

QStash is the only thing that triggers/api/send. The endpoint validates aCRON_SECRETheader on every request, magic links and sessions are signed JWTs, and the Resend key stays AES-256-GCM encrypted at rest. Nothing sensitive is reachable from the browser.

I have added dedicatedarchitecture docsto the repo, if you want to explore yourself.

### The editor and live preview

Every change in the editor is a typed function call, not a blob of JSON. CopilotKit'suseFrontendToolhook takes a zod schema and a handler -- the LLM chooses a tool, fills the params and the handler enforces what's allowed.

useFrontendTool
({

 
name
:
 
"
add_section
"
,

 
parameters
:
 
z
.
object
({

 
type
:
 
z
.
enum
([
"
hn-stories
"
,
 
"
topic
"
,
 
"
recent-gems
"
,
 
"
high-signal
"
,
 
...]),

 
count
:
 
z
.
number
().
min
(
1
).
max
(
30
).
optional
(),

 
query
:
 
z
.
string
().
optional
(),

 
hours
:
 
z
.
number
().
optional
(),

 
minPoints
:
 
z
.
number
().
optional
(),

 
}),

 
handler
:
 
async 
({
 
type
,
 
count
,
 
query
,
 
hours
,
 
minPoints
 
})
 
=>
 
{

 
// Block duplicates for singleton types, strip invalid params, etc.

 
const
 
section
 
=
 
{

 
id
:
 
`
${
type
}
-
${
Date
.
now
()}
`
,

 
type
,

 
props
:
 
{
 
count
,
 
query
,
 
hours
,
 
minPoints
 
},

 
};

 
setConfig
(
prev
 
=>
 
({
 
...
prev
,
 
sections
:
 
[...
prev
.
sections
,
 
section
]
 
}));

 
return
 
`Added 
${
type
}
 section`
;

 
},

});

Enter fullscreen mode

Exit fullscreen mode

The LLM never writes HTML or emits JSON that I have to validate. Guardrails live in the handler -- no duplicate singleton sections, and standard sections silently striphours/minPointsthey don't support.

Every config change hits/api/preview, which renders the React Email template server-side and returns HTML. The editor caches by config hash so repeated edits don't re-fetch.

const
 
cacheKey
 
=
 
`
${
PREVIEW_CACHE_VERSION
}
:
${
JSON
.
stringify
(
config
)}
`
;

const
 
cached
 
=
 
previewCacheRef
.
current
.
get
(
cacheKey
);

if 
(
cached
)
 
{
 
setPreviewHtml
(
cached
);
 
return
;
 
}

const
 
{
 
html
 
}
 
=
 
await 
(
await
 
fetch
(
"
/api/preview
"
,
 
{

 
method
:
 
"
POST
"
,

 
headers
:
 
{
 
"
Content-Type
"
:
 
"
application/json
"
 
},

 
body
:
 
JSON
.
stringify
({
 
config
 
}),

})).
json
();

previewCacheRef
.
current
.
set
(
cacheKey
,
 
html
);

setPreviewHtml
(
html
);

Enter fullscreen mode

Exit fullscreen mode

### Activation and key encryption

You enter a Resend API key, add a recipient, and hit activate. The key gets encrypted with AES-256-GCM before it ever touches the database. It's decrypted only in memory at send time, never logged, never returned to the browser.

export
 
function
 
encrypt
(
text
:
 
string
):
 
string
 
{

 
const
 
iv
 
=
 
crypto
.
randomBytes
(
16
);

 
const
 
cipher
 
=
 
crypto
.
createCipheriv
(
"
aes-256-gcm
"
,
 
getKey
(),
 
iv
);

 
let
 
enc
 
=
 
cipher
.
update
(
text
,
 
"
utf8
"
,
 
"
hex
"
)
 
+
 
cipher
.
final
(
"
hex
"
);

 
return
 
`
${
iv
.
toString
(
"
hex
"
)}
:
${
cipher
.
getAuthTag
().
toString
(
"
hex
"
)}
:
${
enc
}
`
;

}

Enter fullscreen mode

Exit fullscreen mode

A magic link (signed JWT, 30-minute expiry) is sent through your Resend key. Click it and you're in your dashboard.

### Per-user scheduling with QStash

I first tried this with Vercel Hobby cron but it runs once a day for the whole project, which doesn't work when each user wants their own time and timezone. QStash lets every activation create its own schedule so I ended up using this.

const
 
cron
 
=
 
toCron
(
frequency
,
 
time
,
 
day
);
 
// "0 9 * * 1" for Mon 9am

await
 
client
.
schedules
.
create
({

 
destination
:
 
`
${
baseUrl
}
/api/send?id=
${
scheduleId
}
`
,

 
cron
,

 
headers
:
 
{
 
"
x-cron-secret
"
:
 
process
.
env
.
CRON_SECRET
 
},

});

Enter fullscreen mode

Exit fullscreen mode

Timezone conversion happens client-side -- pickAsia/Tokyo 8am, the editor converts to23:00 UTC, that's what gets stored and scheduled.

### The send endpoint

On cron, it runs: decrypt → fetch HN → render → send. Protected by a shared header secret so only QStash can hit it.

// /api/send

if 
(
req
.
headers
.
get
(
"
x-cron-secret
"
)
 
!==
 
process
.
env
.
CRON_SECRET
)
 
return
 
401
;

const
 
record
 
=
 
await
 
getScheduleById
(
id
);

const
 
data
 
=
 
await
 
fetchNewsletterData
(
record
);

const
 
html
 
=
 
await
 
render
(
<
NewsletterEmail
 
config
=
{
record
}
 
data
=
{
data
}
 
...
 
/>
);

const
 
resend
 
=
 
new
 
Resend
(
decrypt
(
record
.
encryptedResendKey
));

await
 
resend
.
emails
.
send
({

 
from
:
 
"
HN Digest <onboarding@resend.dev>
"
,

 
to
:
 
record
.
recipients
,

 
subject
,

 
html
,

});

Enter fullscreen mode

Exit fullscreen mode

Every send fetches fresh Hacker News data. No pre-rendering, no staleness. Sends go through your Resend key (and your quota, not mine), with a one-click unsubscribe that cancels the schedule. You can also pause it from the dashboard.

The pattern itself transfers easily. Swap the Hacker News API for Product Hunt, GitHub trending, Reddit, or any RSS feed, and you've got a personalized digest builder for that source. Same encryption, same chat editor, same per-user schedule.

This one was fun to build. A couple of my friends and I have been using it for the past month.

Would really appreciate some honest feedback :)

Try it here:hndigest.vercel.appGitHub:github.com/Anmol-Baranwal/hndigest

Connect with me onGitHub,TwitterandLinkedIn.

thanks for reading!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse