---
title: 'A Dash of dev.to: My Blog Stats Now Live in the Terminal - DEV Community'
url: https://dev.to/lovestaco/a-dash-of-devto-my-blog-stats-now-live-in-the-terminal-4l4e
site_name: devto
content_file: devto-a-dash-of-devto-my-blog-stats-now-live-in-the-term
fetched_at: '2026-07-16T11:34:57.515863'
original_url: https://dev.to/lovestaco/a-dash-of-devto-my-blog-stats-now-live-in-the-terminal-4l4e
author: Athreya aka Maneshwar
date: '2026-07-14'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with webdev, programming, productivity, bash.
tags: '#webdev, #programming, #productivity, #bash'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star git-lrcto help devs discover the project. Do give it a try and share your feedback.

I check my dev.to stats more often than I would ever admit in a job interview.

Reactions, views, comments, the little numbers that go up, and the ones that stubbornly refuse to.

Normally that ritual means opening a browser, clicking into the dashboard, and squinting at one article at a time like I'm reading tea leaves.

I wanted something calmer.

One terminal window.

My top articles ranked by likes, by views, and by comments, all on screen at once, quietly refreshing itself while I pretend to do real work.

So I built it in an afternoon.

It took a tiny Go program, one wonderful archived project doing the heavy lifting, and two bugs I absolutely did not order but got served anyway.

Let me walk you through it, bugs and all.

## The plan (which looked suspiciously simple)

The plan had three moving parts.

One, dev.to already hands you your own data.

There is an endpoint,GET /api/articles/me, you send your API key in anapi-keyheader, and you get back every article you have published with the fields that matter already counted for you:positive_reactions_count,page_views_count, andcomments_count.

No scraping, no HTML parsing, no crying.

You can generate a key at your dev.to settings under Extensions.

Two, I did not want to build a whole TUI from scratch.

Grids, colors, borders, keyboard handling, refresh loops. Life is short xD

Three, therefore, I needed something that already draws pretty terminal dashboards and would happily show my numbers if I fed it nicely.

That third thing exists, and it is called devdash.

## Enter devdash (and a well earned shoutout)

{ % embedhttps://github.com/Phantas0s/devdash%}

devdashis a highly configurable terminal dashboard by Matthieu Cneude, better known as Phantas0s.

It has widgets for GitHub, Google Analytics, Google Search Console, Travis, and more, and the entire layout is driven by a single YAML file.

Rows, columns, t-shirt sizes, colors, all declarative.

It is a genuinely lovely piece of Go.

Two small catches. It has been archived since 2023. And it has precisely zero concept of what dev.to is.

Now, I could have forked it, added a proper Forem service, wired up structs, written tests, and opened a pull request into a repo that is politely closed for business.

Instead I found the lazy door, and it was already unlocked.

devdash has a widget calledlh.table, the localhost table.

You hand it a shell command, it runs that command, and it renders whatever the command prints as a bordered table.

It splits each line of output on whitespace and slots the pieces into columns. That is the whole contract.

So devdash does not need to know about dev.to.

It just needs a command that prints rows. I can be that command.

If Matthieu ever reads this: thank you for building a tool flexible enough to be abused this gracefully.

Go botherMatthieu on Xand tell him his archived project is still out here pulling shifts.

Here is the shape of the whole thing.

The little Go binary in the middle is the only thing I actually had to write.

I called itdevto-stats.

It fetches all my articles (paginating 100 at a time until dev.to runs out), keeps only the published ones, sorts them by whichever metric devdash asks for, and prints clean rows.

req
.
Header
.
Set
(
"api-key"
,
 
apiKey
)

resp
,
 
_
 
:=
 
client
.
Do
(
req
)

// GET https://dev.to/api/articles/me?per_page=100&page=N

Enter fullscreen mode

Exit fullscreen mode

And the config just points three table widgets at three flavors of that command.

-
 
name
:
 
lh.table

 
options
:

 
title
:
 
"
 
MOST
 
VIEWED
 
"

 
command
:
 
"
./bin/devto-stats
 
-mode=table
 
-sort=views
 
-limit=10"

 
headers
:
 
"
#,Article,Views"

 
border_color
:
 
green

Enter fullscreen mode

Exit fullscreen mode

Three of those blocks, colored red, green, and yellow, sitting side by side. In theory, done.

In theory.

## my dashboard tried to DDoS my own account xD

I turned it on. Overview strip populated. Most Liked, glorious. Most Commented, present.

Most Viewed, a bright red ERROR box.

The command worked perfectly by hand.

It only failed inside devdash.

The clue was in how devdash refreshes: it fires every widget concurrently, each in its own goroutine, all at the same instant.

Four widgets meant four copies ofdevto-statssprinting at the dev.to API at once, elbows out. dev.to did the sensible thing and replied429 Too Many Requests.

One of the four always lost the race, usually Most Viewed.

I had built a very small, very polite denial of service attack against myself.

The fix is the boring, correct one: on a 429, wait and retry, with backoff plus jitter.

if
 
resp
.
StatusCode
 
==
 
http
.
StatusTooManyRequests
 
{

 
backoff
 
:=
 
time
.
Duration
(
attempt
-
1
)
 
*
 
700
 
*
 
time
.
Millisecond

 
jitter
 
:=
 
time
.
Duration
(
rand
.
Intn
(
500
))
 
*
 
time
.
Millisecond

 
time
.
Sleep
(
backoff
 
+
 
jitter
)

 
continue
 
// try this page again

}

Enter fullscreen mode

Exit fullscreen mode

The jitter is the important part. Without it, all four back off by the same amount and collide again, like four people apologizing and stepping the same way in a hallway.

With a random offset, they spread out on their own.

Zero errors after that.

## a comma walked into my table and everything fell over

Most Viewed finally rendered. And it rendered wrong.

The first row looked fine, then every row below slid one column right.

Titles in the numbers column, numbers nowhere.

I recognized the article where it started.

My top post is titled "Good Bye CRUD APIs, Hello Sync".

Look at the punctuation.

Here's what devdash does under the hood: it splits each line on whitespace to get cells, joins those cells back together with commas, then splits the whole batch on commas again to chunk it into rows of N columns.

A comma inside a title is indistinguishable from a comma devdash added on purpose.

One title becomes two cells, the row has four pieces instead of three, and because the chunking is global, every row after it is shifted forever.

The real fix belongs upstream, in a repo that isn't taking visitors.

So I fixed it on my side, where I control the output.

My binary already slugifies titles to survive the whitespace split.

I just taught it to evict commas too.

s
 
:=
 
strings
.
Join
(
strings
.
Fields
(
title
),
 
"-"
)

s
 
=
 
strings
.
ReplaceAll
(
s
,
 
","
,
 
""
)
 
// devdash re-splits the table on commas

Enter fullscreen mode

Exit fullscreen mode

One line. The comma-tose table woke right up.

## The payoff

Here is the raw feed one panel runs on, straight out of the binary, real numbers from my actual account:

devdash takes three of those feeds and frames them into colored, bordered, self refreshing tables sitting shoulder to shoulder: Most Liked in red, Most Viewed in green, Most Commented in yellow, with a summary strip across the top.

Ctrl+Rforces a refresh,Ctrl+Cquits, and left to its own devices it repaints itself every five minutes.

444 articles, all of them accounted for, no browser, no clicking, just a quiet terminal telling me the truth about which posts people actually read.

## What I actually learned

The best integration is often no integration.devdash never learned about dev.to.

I made dev.to speak devdash's language instead, and a tool that stopped being maintained in 2023 rendered 2026 data without a single change to its source.

The whole thing, Go helper, YAML, and Makefile, is here:lovestaco/devto_devdash.

Bring your own API key.

And real gratitude to Matthieu Cneude for devdash.

Sometimes the best tool for the job is one somebody stopped working on years ago, sitting there quietly, still perfectly happy to dash off one more dashboard.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs — without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Git Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|🇮🇳 हिन्दी|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

GenAI today is arace car without brakes. It accelerates fast -- you describe something, and large blocks of code appear instantly. But AI agentssilently break things: they remove logic, relax constraints, introduce expensive cloud calls, leak credentials, and change behavior -- without telling you. You often find out in production.

git-lrcis your braking system.It hooks intogit commitand runs an AI review on every diffbeforeit lands. 60-second setup. Completely free.

In short, git-lrc helpsPrevent Outages, Breaches, and Technical Debt Before They Happen

At a glance:10 risk categories·100+ failure patterns tracked· every commit…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse