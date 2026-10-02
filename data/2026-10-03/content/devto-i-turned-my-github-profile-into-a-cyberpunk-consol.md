---
title: I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Contributions - DEV Community
url: https://dev.to/georgekobaidze/i-turned-my-github-profile-into-a-cyberpunk-console-with-a-city-built-from-my-contributions-h4c
site_name: devto
content_file: devto-i-turned-my-github-profile-into-a-cyberpunk-consol
fetched_at: '2026-10-03T03:06:54.675406'
original_url: https://dev.to/georgekobaidze/i-turned-my-github-profile-into-a-cyberpunk-console-with-a-city-built-from-my-contributions-h4c
author: Giorgi Kobaidze
date: '2026-10-01'
description: I just wanted a custom profile. I completely overcooked it. Don't feel like reading? Fair. But... Tagged with python, showdev, github, design.
tags: '#showdev, #python, #github, #design'
---

Bypassing GitHub's strict sandbox via SVGs

I just wanted a custom profile. I completely overcooked it.

Don't feel like reading? Fair. But you're going to miss a lot of interesting insights. Anyway, here's my profile link:

## georgekobaidze (Giorgi Kobaidze) · GitHub

Software Engineer | Engineering Manager | Technical Writer |🏆2x Hackathon Winner | ☕Enjoyer - georgekobaidze

 github.com
 

## Table of Contents

* I Wanted a Simple Custom GitHub Profile. But Things Got Out of Hand Quickly23:00. Fully Cooked.Random Doesn't Mean BadWhy Do I Keep Doing This to Myself?
* 23:00. Fully Cooked.
* Random Doesn't Mean Bad
* Why Do I Keep Doing This to Myself?
* The Contribution CityThe City That Represents MeThe Moment It Clicked
* The City That Represents Me
* The Moment It Clicked
* The Cyberpunk ConsoleBecause Why Not?
* Because Why Not?
* Welcome to the SandboxNo JavaScript. No CSS. No Fun?The Loophole: An SVG Is Just an ImageOkay, But the Sandbox Has Rules
* No JavaScript. No CSS. No Fun?
* The Loophole: An SVG Is Just an Image
* Okay, But the Sandbox Has Rules
* One Console, 23 ImagesThe Problem: Images Don't Hold HandsSlicing the ConsoleThe Tricks That Make It Seamless
* The Problem: Images Don't Hold Hands
* Slicing the Console
* The Tricks That Make It Seamless
* Building the CityFrom Grid to SkylineHow Tall Is a Day?Lights OnGreen or Blue?
* From Grid to Skyline
* How Tall Is a Day?
* Lights On
* Green or Blue?
* It Updates Itself Every DayA Robot on Daily DutyTalking to GitHub: One Query Instead of TwentyThe All-Time ProblemTalking to DEVWhen an API Has a Bad DayThe README Edits Itself (Carefully)Secrets That Stay SecretWhy 12:17?
* A Robot on Daily Duty
* Talking to GitHub: One Query Instead of Twenty
* The All-Time Problem
* Talking to DEV
* When an API Has a Bad Day
* The README Edits Itself (Carefully)
* Secrets That Stay Secret
* Why 12:17?
* Was It Worth It?The Damage ReportSo... Was It?Come Visit
* The Damage Report
* So... Was It?
* Come Visit

## I Wanted a Simple Custom GitHub Profile. But Things Got Out of Hand Quickly

### 23:00. Fully Cooked.

It was 23:00. I'd just got home after an extremely exhausting day, dropped into the chair in front of my laptop, and... just stared at the screen. No plan. No thoughts. Nothing... Blank.

I'm sure you know the feeling. The day cooks you so hard that your brain switches to screensaver mode, random thoughts start floating in and out on their own, like those bouncing DVD logos that never quite hit the corner.

### Random Doesn't Mean Bad

Here's the funny part: that's exactly when my best ideas tend to show up. When the brain stops trying, it starts shuffling. And random doesn't always mean bad.

That night, somewhere between "I should go to sleep" and "I should really go to sleep," one of those floating thoughts really caught my attention. And, my goodness, it was so good that I got my energy back. Instantly. Like someone had plugged me straight into a wall socket.

"Are you kidding me? This is so cool! I'm building it right now. I don't care how tired I am."

That's what I told myself. Out loud. At 23:00... send help please.

### Why Do I Keep Doing This to Myself?

Seriously, why? I'd been awake for about 16 hours by then, and my brain had been running the whole time like an engine in a 24-hour endurance race at Daytona or the Nürburgring. By the way, I love those race tracks.

Any reasonable person would have closed the laptop.

I clicked the VS Code icon instead, cracked my knuckles and got to work. Time to cook!🔥

## The Contribution City

### The City That Represents Me

I'd always wanted my contribution graph to be something more than a grid of green squares. Something original. The problem was that I never had a good enough idea.

And no, I didn't want to turn it into another Pac-Man, Snake or Tetris game. Don't get me wrong, those are creative and fun, I love them and I've seen many great implementations. But by now they're everywhere, overused.

I wanted something different. Something that actually says something aboutME.

I loveCyberpunk 2077and its atmosphere. Well, except maybe its launch day, when the cars were spawning inside each other and NPCs were T-posing out of nowhere in the middle of the street, but everything after that? Absolutely.

I love big cities with huge skyscrapers. I love being close to where things happen, where you can feel the pace and the pressure to keep up. I've never been an "I can't wait to retire and start a farm" kind of guy anyway.

Oh, and I love neon lights. A lot.

### The Moment It Clicked

So there I was, sitting motionless and emotionless in front of the screen, when the picture just appeared in my head: my contribution graph, lifted into 3D. Every day a building. Quiet days as empty lots, busy days as skyscrapers. A whole city.

That was it. The contribution city was on its way.

## The Cyberpunk Console

### Because Why Not?

Then I thought: a city like that can't just sit there on a plain white README, next to a list of badges. It needs a proper home.

So I decided to go further and turn thewhole profileinto a cyberpunk console: neon glow, scanlines, a terminal that types out my name, and a frame that holds everything together.

Because why not?

## Welcome to the Sandbox

### No JavaScript. No CSS. No Fun?

First reality check: GitHub doesn't let you run anything in a README.<script>gets stripped.<style>gets stripped. Even inlinestyle=""attributes get stripped.

I wanted a cyberpunk console. GitHub gave me Markdown and a handful of HTML tags.

### The Loophole: An SVG Is Just an Image

But here's the thing. To GitHub, an SVG embedded with<img>is just an image. Andinsidean SVG, you're allowed to use CSS, including animations:

<svg
 
xmlns=
"http://www.w3.org/2000/svg"
 
width=
"300"
 
height=
"60"
>

 
<style>

 @keyframes blink { 50% { opacity: 0 } }
 .cursor { animation: blink 1s step-end infinite }
 
</style>

 
<text
 
x=
"10"
 
y=
"38"
 
fill=
"#3fb950"
>
$ whoami
</text>

 
<rect
 
class=
"cursor"
 
x=
"110"
 
y=
"24"
 
width=
"10"
 
height=
"18"
 
fill=
"#00d9ff"
/>

</svg>

Enter fullscreen mode

Exit fullscreen mode

<img
 
src=
"./assets/header.svg"
 
width=
"100%"
>

Enter fullscreen mode

Exit fullscreen mode

That's the whole trick behind the typing animation, the glitching name and the blinking cursor. Every "UI" element on my profile is secretly a picture.

### Okay, But the Sandbox Has Rules

Images get loaded in a locked-down mode, and that comes with a few catches:

* No external resources.Not even Google Fonts. So the font is embedded inside every SVG, trimmed down to only the characters that image actually shows.
* No hover, no clicks.An image is an image. Links only work on a whole image, which is why every project card and every link button is its own file.
* Caching.GitHub caches images for a few minutes. I fixed a bug, refreshed, saw the bug. Fixed it again, refreshed, still the bug. Turns out I'd fixed it the first time.

## One Console, 23 Images

### The Problem: Images Don't Hold Hands

My first version had every section as its own neat little panel: a box for the header, a box for the about text, a box for the stats. Each one looked great on its own.

Together, they looked like a terminal that had been dropped on the floor. Separate pieces, with gaps between them.

I wantedoneconsole. One continuous window you scroll through from top to bottom.

### Slicing the Console

The fix: draw one big frame and cut it into horizontal slices.

* Only theheaderdraws the top edge and the title bar.
* Only thefooterdraws the bottom edge.
* Every slice in between draws just the two side rails, left and right.

Stack them on top of each other and the rails line up into one long window:

<p
 
align=
"center"
>

<img
 
src=
"./assets/header.svg"
 
width=
"100%"
 
align=
"top"
>

<img
 
src=
"./assets/stats.svg"
 
width=
"100%"
 
align=
"top"
>

<img
 
src=
"./assets/contribution-city.svg"
 
width=
"100%"
 
align=
"top"
>

<!-- ...more slices... -->

<img
 
src=
"./assets/footer.svg"
 
width=
"100%"
 
align=
"top"
>

</p>

Enter fullscreen mode

Exit fullscreen mode

Project cards and link buttons are slices too, just narrower: half-width and fifth-width images that only draw the rail on their outer side. Count everything up and you get 23 images pretending to be one terminal.

### The Tricks That Make It Seamless

Stacking images is easy. Making the seams invisible took a few tricks:

* A 40 px grid.Every slice is a multiple of 40 pixels tall, so the faint background grid continues across the cuts instead of jumping.
* Glow that overflows.The neon glow on the rails starts above each slice and ends below it, so it doesn't fade out at the edges like a broken fluorescent tube.
* align="top".Browsers leave a small gap under images by default, the space reserved for letters likegandythat hang below the line. Aligning to the top removes it.

## Building the City

### From Grid to Skyline

The city isn't a new idea, it's the same contribution graph you already know. 53 columns of weeks, 7 rows of days. I just tilted it into an isometric view and gave every square some height.

Each building is only three shapes: a roof and two walls. The trick is the drawing order. Buildings are painted from back to front, so the ones closer to you naturally cover the ones behind them. No 3D engine needed, just the painter's algorithm and a sorted list.

### How Tall Is a Day?

I know, what a weird question, right?

My first instinct was simple: height = number of contributions. That gave me one giant tower for my busiest day and a sea of flat slabs for everything else. Not a city. More like a huge parking lot with the Empire State Building right in the middle of it.

So the height uses a square root instead:

h
=
8
+
110
⋅
c
c
max
⁡

h = 8 + 110 \cdot \sqrt{\frac{c}{c_{\max}}}

h
=
8
+
110
⋅
c
m
a
x
​
c
​
​

In Python, that's:

height
 
=
 
8
 
+
 
110
 
*
 
math
.
sqrt
(
count
 
/
 
busiest_day
)

Enter fullscreen mode

Exit fullscreen mode

It lifts the small days while keeping the busy days clearly on top:

Contributions

Linear

Square root

1

11 px

25 px

10

34 px

61 px

43 (my record)

118 px

118 px

Days with zero contributions don't get a building at all. They stay as empty lots. Some months of my city look like an abandoned district. And you know what? That's accurate.

Here's how the city compares to my actual GitHub activity graph:

The contribution city:

The default GitHub contribution graph:

### Lights On

A skyline at night needs lights, so every building gets windows: some lit, some dark, and a few that flicker. Add twinkling stars, a moon, and a plane with blinking lights crossing the sky, and the city starts to feel alive.

The windows are placed randomly, but with aseededrandom generator. Same data, same seed, same city, down to the last window. Why does that matter? Because otherwise the image would change every single day even with no new contributions, and my repo would get a pointless commit every morning.

### Green or Blue?

GitHub's contribution graph is green, so my first city had green roofs. People instantly read it as "activity," and that's a big plus.

But the rest of my profile is neon blue. Next to everything else, the green city looked like it was pasted in from another website. So I rendered both versions side by side, looked at them for about three seconds, and blue won. I love the color blue.

Here are both variants. Which one do you like more?

## It Updates Itself Every Day

### A Robot on Daily Duty

A profile with stats that never change is just a screenshot with extra steps. So the whole thing runs on a schedule, on GitHub's servers, whether my laptop is on or not.

The pipeline is four steps, three of them small Python scripts:

fetch.py → asks GitHub and DEV for fresh numbers, saves them as JSON
render.py → reads the JSON, redraws every SVG
readme.py → updates the parts of README.md that change
git commit → only if something actually changed

Enter fullscreen mode

Exit fullscreen mode

And the workflow that glues it together:

name
:
 
Update profile

on
:

 
schedule
:

 
-
 
cron
:
 
"
17
 
12
 
*
 
*
 
*"

 
timezone
:
 
"
America/New_York"

 
workflow_dispatch
:
 
# a "Run workflow" button for impatient people (me)

permissions
:

 
contents
:
 
write
 
# needed to push the refreshed files

jobs
:

 
update
:

 
runs-on
:
 
ubuntu-latest

 
steps
:

 
-
 
uses
:
 
actions/checkout@v5

 
-
 
uses
:
 
actions/setup-python@v6

 
with
:

 
python-version
:
 
"
3.12"

 
-
 
run
:
 
pip install fonttools==4.62.1 brotli==1.2.0

 
-
 
run
:
 
python tools/profile/fetch.py

 
env
:

 
PROFILE_TOKEN
:
 
${{ secrets.PROFILE_TOKEN }}

 
GITHUB_TOKEN
:
 
${{ github.token }}

 
DEV_API_KEY
:
 
${{ secrets.DEV_API_KEY }}

 
-
 
run
:
 
python tools/profile/render.py

 
-
 
run
:
 
python tools/profile/readme.py

 
-
 
run
:
 
|

 
git config user.name "github-actions[bot]"

 
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

 
git add tools/profile/data assets README.md

 
git diff --cached --quiet || (git commit -m "Refresh profile stats" && git push)

Enter fullscreen mode

Exit fullscreen mode

That last line is the polite part:git diff --cached --quietexits successfully when nothing changed, so the commit only happens when there's something new. No empty "update" commits polluting the history.

### Talking to GitHub: One Query Instead of Twenty

GitHub has two APIs. The REST one would need a separate request for followers, pull requests, every repository, every repository's languages... I'd be paginating until next Tuesday.

The GraphQL API lets me ask for exactly what I need inonerequest:

query
(
$login
:
 
String
!)
 
{

 
user
(
login
:
 
$login
)
 
{

 
createdAt

 
followers
 
{
 
totalCount
 
}

 
pullRequests
 
{
 
totalCount
 
}

 
merged
:
 
pullRequests
(
states
:
 
MERGED
)
 
{
 
totalCount
 
}

 
contributionsCollection
 
{
 
contributionYears
 
}

 
repositories
(
ownerAffiliations
:
 
OWNER
,
 
isFork
:
 
false
,
 
privacy
:
 
PUBLIC
,
 
first
:
 
100
)
 
{

 
nodes
 
{

 
name

 
stargazerCount

 
forkCount

 
languages
(
first
:
 
20
)
 
{
 
edges
 
{
 
size
 
node
 
{
 
name
 
}
 
}
 
}

 
}

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

From that single response I get the followers, PRs, member-since date, total stars and forks (summed across repos), per-project star counts for the cards, and the language bar (bytes of code per language, summed up).

Sending it is plain Python, no SDK needed:

def
 
graphql
(
token
,
 
query
,
 
variables
=
None
):

 
res
 
=
 
http_json
(
"
https://api.github.com/graphql
"
,

 
headers
=
{
"
Authorization
"
:
 
f
"
bearer 
{
token
}
"
},

 
body
=
{
"
query
"
:
 
query
,
 
"
variables
"
:
 
variables
 
or
 
{}})

 
if
 
res
.
get
(
"
errors
"
):

 
raise
 
RuntimeError
(
"
GraphQL error: 
"
 
+
 
"
; 
"
.
join
(
e
[
"
message
"
]
 
for
 
e
 
in
 
res
[
"
errors
"
]))

 
return
 
res
[
"
data
"
]

Enter fullscreen mode

Exit fullscreen mode

### The All-Time Problem

Here's a GitHub quirk:contributionsCollectioncoversat most one yearper request. Ask for more and it politely refuses.

So how do you get all-time contributions and a streak that doesn't break on January 1st? The first query returnscontributionYears, the list of years I've been active. Then I build a second query on the fly, with one aliased field per year:

def
 
years_query
(
years
):

 
parts
 
=
 
[]

 
for
 
y
 
in
 
years
:

 
parts
.
append
(
f
"""

 y
{
y
}
: contributionsCollection(from: 
"
{
y
}
-01-01T00:00:00Z
"
, to: 
"
{
y
}
-12-31T23:59:59Z
"
) {{
 totalCommitContributions
 contributionCalendar {{ totalContributions weeks {{ contributionDays {{ date contributionCount }} }} }}
 }}
"""
)

 
return
 
"
query($login: String!) {
\n
 user(login: $login) {
"
 
+
 
""
.
join
(
parts
)
 
+
 
"
\n
 }
\n
}
"

Enter fullscreen mode

Exit fullscreen mode

y2016,y2017, ...,y2026: a decade of calendars in a single round trip. GraphQL aliases are criminally underrated.

That gives me every single day since 2016 as{date: count}. From there:

* Contributions this year and all timeare sums oftotalContributions.
* The citygets the last 53 weeks, starting on a Sunday, exactly like GitHub's own graph.
* The streaksare a simple walk through the days:

def
 
streaks
(
days
,
 
today
):

 
longest
 
=
 
run
 
=
 
0

 
for
 
d
 
in
 
sorted
(
d
 
for
 
d
 
in
 
days
 
if
 
d
 
<=
 
today
):

 
run
 
=
 
run
 
+
 
1
 
if
 
days
[
d
]
 
>
 
0
 
else
 
0

 
longest
 
=
 
max
(
longest
,
 
run
)

 
current
,
 
d
 
=
 
0
,
 
today

 
if
 
days
.
get
(
d
,
 
0
)
 
==
 
0
:
 
# no contributions yet today?

 
d
 
-=
 
datetime
.
timedelta
(
days
=
1
)
 
# then the streak can still end yesterday

 
while
 
days
.
get
(
d
,
 
0
)
 
>
 
0
:

 
current
 
+=
 
1

 
d
 
-=
 
datetime
.
timedelta
(
days
=
1
)

 
return
 
current
,
 
longest

Enter fullscreen mode

Exit fullscreen mode

That littleifmatters more than it looks. The workflow runs at midday. Without it, my streak would reset to zero every day until I made my first commit of the day. Very motivating. But not in a good way.

### Talking to DEV

The DEV numbers come from theForem API. Articles, reactions and comments are public:

arts
 
=
 
dev_paged
(
f
"
https://dev.to/api/articles?username=
{
USER
}
"
)

dev
 
=
 
{

 
"
articles
"
:
 
len
(
arts
),

 
"
reactions
"
:
 
sum
(
a
[
"
public_reactions_count
"
]
 
for
 
a
 
in
 
arts
),

 
"
comments
"
:
 
sum
(
a
[
"
comments_count
"
]
 
for
 
a
 
in
 
arts
),

}

Enter fullscreen mode

Exit fullscreen mode

Views and followers are private, so they need an API key in theapi-keyheader:

h
 
=
 
{
"
api-key
"
:
 
api_key
,
 
"
Accept
"
:
 
"
application/vnd.forem.api-v1+json
"
}

mine
 
=
 
dev_paged
(
"
https://dev.to/api/articles/me/published
"
,
 
h
)

dev
[
"
views
"
]
 
=
 
sum
(
a
[
"
page_views_count
"
]
 
for
 
a
 
in
 
mine
)

dev
[
"
followers
"
]
 
=
 
len
(
dev_paged
(
"
https://dev.to/api/followers/users
"
,
 
h
))

Enter fullscreen mode

Exit fullscreen mode

dev_pagedjust keeps requestingpage=1, 2, 3...until it gets an empty list back. The same response also gives me my five newest articles for the writing section.

### When an API Has a Bad Day

APIs fail. Rate limits, timeouts, a random 502 at the worst possible moment. And a profile that suddenly shows "0 stars, 0 contributions" because GitHub hiccupped once is worse than no stats at all.

Sofetch.pynever starts from scratch. It loads yesterday's JSON first and only overwrites what it successfully fetched:

stats
 
=
 
load
(
"
stats.json
"
,
 
{})
 
# yesterday's numbers

try
:

 
stats
.
update
(
fetch_github
(
token
,
 
today
))

except
 
Exception
 
as
 
ex
:

 
warn
(
f
"
GitHub fetch failed, keeping previous stats: 
{
ex
}
"
)

try
:

 
dev
,
 
latest
 
=
 
fetch_dev
(
api_key
)

 
...

except
 
Exception
 
as
 
ex
:

 
warn
(
f
"
DEV fetch failed, keeping previous values: 
{
ex
}
"
)

Enter fullscreen mode

Exit fullscreen mode

If GitHub is down, the DEV numbers still update, and vice versa. Ifbothfail, the script exits with an error and touches nothing. Worst case, my profile is one day old. It never goes blank.

Bonus: the JSON files are committed together with the images, sogit log -p tools/profile/data/stats.jsonis a free history of my stats. I didn't plan that. I'll take it.

### The README Edits Itself (Carefully)

Most of the README never changes. But the article links do, and so do the alt texts that describe the stats for screen readers. Rewriting the whole file from a template would wipe out anything I edit by hand, soreadme.pyonly touches clearly marked zones:

<!-- writing:start -->

<a
 
href=
"https://dev.to/..."
><img
 
src=
"./assets/writing/post-1.svg"
 
...
></a>

...

<!-- writing:end -->

Enter fullscreen mode

Exit fullscreen mode

s
,
 
n
 
=
 
re
.
subn
(
r
"
<!-- writing:start -->.*?<!-- writing:end -->
"
,

 
lambda
 
_
:
 
writing_block
(
articles
),
 
s
,
 
flags
=
re
.
S
)

if
 
n
 
!=
 
1
:

 
sys
.
exit
(
"
error: README needs exactly one writing block
"
)

Enter fullscreen mode

Exit fullscreen mode

HTML comments are invisible on GitHub, so the markers cost nothing. And if someone (me) accidentally deletes one, the script fails loudly instead of quietly mangling the README.

### Secrets That Stay Secret

The workflow needs two secrets: a GitHub token, so private contributions get counted, and the DEV API key. Neither is ever written in the repo. The workflow only references them by name:

PROFILE_TOKEN
:
 
${{ secrets.PROFILE_TOKEN }}

Enter fullscreen mode

Exit fullscreen mode

The values live inSettings → Secrets and variables → Actions, encrypted. GitHub injects them at runtime and masks them as***if they ever show up in the logs.

For the token I used afine-grainedpersonal access token instead of a classic one, because it can beread-only: Metadata and Contents, nothing else. If it ever leaked, the worst someone could do is read my code. Not push to it.

And both are optional. Without them, the workflow falls back to the built-inGITHUB_TOKENand public data only.

### Why 12:17?

:17 instead of :00, because everyone schedules their jobs on the full hour, and GitHub's runners get flooded at :00. Scheduled runs at the top of the hour often start late. A random-looking minute dodges the rush.

## Was It Worth It?

### The Damage Report

Let's count what my "simple custom profile" turned into:

* 23 SVG images pretending to be one terminal
* a contribution city with one building for every day of the past year
* three Python scripts and a GitHub Actions workflow
* two APIs, two secrets and one very hardworking robot.

All of that, so a page most people will look at for about eight seconds says my name in neon.

### So... Was It?

Absolutely.

It wasn't really about the profile. It was about that 23:00 feeling, when a random idea shows up and suddenly you're not tired anymore. The kind of project nobody asked for, with no deadline and no stakeholders, built just because it's fun.

And somewhere along the way I learned a bunch of things I'd never have touched otherwise: SVG animations, isometric drawing, font subsetting, GraphQL aliases, and how many layers of caching sit between "I fixed it" and "I can see that I fixed it."

Plus, the profile now maintains itself. Every day at 12:17 New York time, a robot wakes up, checks what I've been doing, and adds a new building to my city. Even on the days I don't feel like I'm building anything.

### Visit the Profile

The city is live at:

## georgekobaidze (Giorgi Kobaidze) · GitHub

Software Engineer | Engineering Manager | Technical Writer |🏆2x Hackathon Winner | ☕Enjoyer - georgekobaidze

 github.com
 

And all the code behind it is in the same repo, undertools/profile. Feel free to look around, fork it, and build your own skyline. Just change the username first, unless you want my stats on your profile.

And if you build something cool with it, show me in the comments. I'd love to see what your city looks like.

Now if you'll excuse me, I have some quiet days to fill. My city has a few empty lots that need skyscrapers.

$ exit
connection to georgekobaidze closed. // EOF

Enter fullscreen mode

Exit fullscreen mode

Enjoyed this write-up? Let's stay connected!

I share more software engineering insights, projects, and experiments across these platforms:

* 💼Connect with me on LinkedIn
* 💻Explore my projects on GitHub
* 📱Follow me on X
* 🎥Watch my videos on YouTube
* 💬Let's Chat on Discord

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (40 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse