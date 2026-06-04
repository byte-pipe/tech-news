---
title: I Got Sick of Miro Eating 10 Minutes of Every Retro. So I Built a Corkboard for the Web. - DEV Community
url: https://dev.to/varshithvhegde/i-got-sick-of-miro-eating-10-minutes-of-every-retro-so-i-built-a-corkboard-for-the-web-41n9
site_name: devto
content_file: devto-i-got-sick-of-miro-eating-10-minutes-of-every-retr
fetched_at: '2026-06-04T19:44:42.421273'
original_url: https://dev.to/varshithvhegde/i-got-sick-of-miro-eating-10-minutes-of-every-retro-so-i-built-a-corkboard-for-the-web-41n9
author: Varshith V Hegde
date: '2026-06-04'
description: Here's a thing that happens on every team I've been on. Sprint ends. Someone schedules the retro.... Tagged with webdev, opensource, productivity, tutorial.
tags: '#webdev, #opensource, #productivity, #tutorial'
---

No-signup tool and technical dev insights

Here's a thing that happens on every team I've been on.

Sprint ends. Someone schedules the retro. Someone else shares a Miro link in Slack. Half the team opens it and immediately hits some kind of wall. "I'm on the viewer plan." "It's not loading for me." "How do I add a sticky note again?" One person accidentally deletes the entire frame. Another person is still zoomed into the wrong corner of the board and can't figure out how to get back.

We spend the first ten to fifteen minutes of every retro just fixing the board.

And the whole time I'm sitting there thinking: this is a sticky note board. This is the most ancient, simple, obvious tool in the history of meetings. How did we end up needing a tutorial to use it?

So I built something. It's called PostItUp. It's a real-time collaborative sticky note board that runs in the browser. It looks like an actual physical corkboard. Anyone can drop a note without creating an account. And the whole thing runs for free.

I want to walk you through all of it. The product, the design decisions, the technical choices, the bugs that nearly broke me, and where this is going. This is going to be a long one. Grab something to drink.

## What the Thing Actually Is

The pitch is simple. You create a board. You share a link. People click the link and start posting notes immediately. No signup, no tutorial, no onboarding flow.

Each note is a sticky. You pick a color, type something, optionally add your name, and hit "Pin it". The note appears on the canvas. Everyone watching the board sees it appear in real time.

That's the core loop. Everything else is details on top of that.

The visual design is intentional and it matters more than it looks. Every card has a wobbly hand-drawn border. Notes have little washi tape strips holding them to the board. Push pins mark the project cards. The background is either a dot grid, a ruled notebook page, or a grid pattern depending on what you choose. The fonts are actual handwriting fonts that stay legible at small sizes.

I made it look this way on purpose. I'll explain why in a minute.

## Why Anyone Would Make It Look Like This

Most collaboration tools look like a SaaS dashboard. Clean, flat, efficient, slightly cold. There's nothing wrong with that for serious project management.

But for quick feedback sessions and retros and brainstorming, that visual language is actively working against you. It signals "professional context" in a way that makes people more measured and careful with what they write. The same people who would stick a brutally honest Post-it on a physical board will write something much more diplomatic in a Jira ticket.

Physical sticky notes feel disposable. Throwaway. Safe to be honest. I wanted the digital version to carry that same feeling.

There's also something to be said for tools that just look different. When you're staring at the same Notion document or the same Miro board all week, you get a little numb to them. Opening something that looks like a corkboard on your screen creates a tiny mental context switch. It's a small thing but I think it matters.

## Three Canvas Modes Because One Was Never Going to Work for Everyone

When you create a board you pick one of three canvas modes.

Free canvasis the open dot-grid. Notes land wherever you put them. You pan with alt+drag or middle mouse, zoom with ctrl+scroll. Notes can go anywhere. It's the most flexible and also the most chaotic.

Grid modesnaps everything to a 32-pixel grid automatically. The canvas is still completely open but your notes line up without you manually trying to align them. This is what I use by default now. Structured enough to stay readable, free enough to not feel constrained.

Ruled linesputs horizontal notebook lines across the background. The whole mood of the board changes. Works really well for sequential feedback or when you're collecting ordered lists rather than freeform ideas.

The board owner sets the mode at creation time and it applies to the whole canvas. Same codebase, same components, three completely different feels.

I spent more time on this decision than I expected to. My first instinct was "just do free canvas, that's the obvious choice". But then I ran a couple of quick feedback sessions with it and kept noticing that people who were less comfortable with open canvases kept adding notes awkwardly, unsure of where to put them. Grid mode fixed that completely. And ruled lines came from someone saying they wanted it to feel more like a questionnaire.

Features should come from watching people use the thing, not from imagining what they might want.

## Posting a Note

Double-click anywhere on the canvas. A modal appears. Type something. Pick a color. Add your name if you want (it saves your preference in localStorage so you only type it once). Hit "Pin it".

The note appears on the canvas.

If someone else is watching the same board, they see it appear right then. No refresh. The board is live.

Notes have a slight random rotation when they land. Between negative three and positive three degrees, picked randomly at insert time and stored in the database. It's a tiny detail but it makes the board look like notes placed by humans rather than software. Uniformly straight sticky notes on a corkboard would look wrong, so they don't.

You can drag notes around the canvas. The position saves to the database the moment you let go. Anyone watching sees them move.

You can upvote notes you agree with. One vote per device per note. The vote count lives on the note permanently.

Board owners can delete any note. Authors can delete their own notes. The owner can also clear the whole board from settings.

## The Part I Think Developers Will Actually Use

Every board has an embed panel. You open it from the toolbar using the link icon button. Three options.

iFrameis the obvious one. One line, your board is embedded in any webpage.

<iframe
 
 
src=
"https://postitup.varshithvhegde.in/embed/your-board-slug"

 
width=
"100%"
 
 
height=
"600"
 
 
frameborder=
"0"
>

</iframe>

Enter fullscreen mode

Exit fullscreen mode

There's a separate/embed/[slug]route that renders a stripped-down version of the canvas with no navigation or app chrome. Just the board. Supabase Realtime is still running in there so it updates live inside the iframe.

Script tagis the one I actually think is useful. Drop this into any webpage:

<script 
 
src=
"https://postitup.varshithvhegde.in/embed.js"

 
data-board=
"your-board-slug"

 
data-url=
"https://postitup.varshithvhegde.in"
>

</script>

Enter fullscreen mode

Exit fullscreen mode

That injects a floating "Leave a note" button in the corner. Click it and a slide-out drawer opens with the full board inside. The iframe only loads when someone actually clicks the button. If nobody opens the drawer, the board costs you nothing. No network request, no layout shift, nothing.

The script is completely self-contained. No framework required on your end. It works on a static HTML page, a WordPress blog, a Next.js app, whatever. I've already used it on a few pages and the whole setup takes about ninety seconds.

React componentis what's coming next.

Right now the snippet shows you how you'd use it once it's published. The npm package isn't out yet but it's in progress. The goal is something like:

import
 
{
 
PostItBoard
 
}
 
from
 
"
postitup
"

<
PostItBoard

 
board
=
"
your-board-slug
"

 
baseUrl
=
"
https://postitup.varshithvhegde.in
"

 
height
=
{
500
}

/
>

Enter fullscreen mode

Exit fullscreen mode

TypeScript types, SSR-safe, works in Next.js without hydration issues, theming props so it doesn't look foreign inside your app. If you'd use this, watch the repo. It's coming.

## Now the Technical Part

Stack: Next.js 16 with the App Router, Supabase for database and real-time and auth, TypeScript everywhere, Tailwind for layout utilities. No component library. Everything visual is hand-rolled CSS.

### How the wobbly borders work

The hand-drawn look on cards comes from a single SVG filter defined in the page layout:

<filter
 
id=
"roughen"
>

 
<feTurbulence
 
 
type=
"fractalNoise"
 
 
baseFrequency=
"0.04"
 
 
numOctaves=
"4"
 
 
seed=
"3"
 
 
result=
"noise"
 
/>

 
<feDisplacementMap
 
 
in=
"SourceGraphic"
 
 
in2=
"noise"
 
 
scale=
"2.5"
 
 
xChannelSelector=
"R"
 
 
yChannelSelector=
"G"
 
/>

</filter>

Enter fullscreen mode

Exit fullscreen mode

The displacement map shifts pixels based on fractal noise. The result looks like someone drew the border by hand. Apply it to any element withfilter: url(#roughen)and it gets the wobbly look. One filter, defined once, referenced everywhere.

The washi tape strips are semi-transparent divs with a repeating linear gradient for texture:

background-image
:
 
repeating-linear-gradient
(

 
90
deg
,

 
transparent
 
0
,
 
transparent
 
3
px
,

 
rgba
(
255
,
255
,
255
,
0
.
18
)
 
3
px
,
 
rgba
(
255
,
255
,
255
,
0
.
18
)
 
4
px

);

mix-blend-mode
:
 
multiply
;

Enter fullscreen mode

Exit fullscreen mode

Mix-blend-mode multiply makes them look translucent against whatever is behind them, the same way real tape behaves on paper. These tiny things add up.

### Real-time in Supabase

Supabase Realtime is a WebSocket layer on top of Postgres. You subscribe to change events on a table with filters, and Supabase sends you the payloads when rows change.

const
 
channel
 
=
 
supabase

 
.
channel
(
`board:
${
board
.
id
}
`
)

 
.
on
(
"
postgres_changes
"
,
 
{

 
event
:
 
"
INSERT
"
,

 
schema
:
 
"
public
"
,

 
table
:
 
"
notes
"
,

 
filter
:
 
`board_id=eq.
${
board
.
id
}
`

 
},
 
(
payload
)
 
=>
 
{

 
setNotes
(
n
 
=>

 
n
.
find
(
x
 
=>
 
x
.
id
 
===
 
payload
.
new
.
id
)

 
?
 
n
 
// already have it from optimistic update

 
:
 
[...
n
,
 
payload
.
new
 
as
 
Note
]

 
)

 
})

 
.
on
(
"
postgres_changes
"
,
 
{
 
event
:
 
"
UPDATE
"
,
 
...
 
},
 
(
payload
)
 
=>
 
{

 
setNotes
(
n
 
=>
 
n
.
map
(
x
 
=>

 
x
.
id
 
===
 
payload
.
new
.
id
 
?
 
{
 
...
x
,
 
...
payload
.
new
 
}
 
:
 
x

 
))

 
})

 
.
on
(
"
postgres_changes
"
,
 
{
 
event
:
 
"
DELETE
"
,
 
...
 
},
 
(
payload
)
 
=>
 
{

 
setNotes
(
n
 
=>
 
n
.
filter
(
x
 
=>
 
x
.
id
 
!==
 
payload
.
old
.
id
))

 
})

 
.
subscribe
()

Enter fullscreen mode

Exit fullscreen mode

The INSERT handler checks if the note already exists before adding it. When you post a note, your own UI updates immediately (optimistic update). The real-time event arrives a moment later. Without the check you'd see the note twice.

### The drag bug that wasted a whole afternoon

Dragging notes worked visually. Positions were not saving correctly. The note would jump back to where it started when you reloaded the page.

The problem was a stale closure. The mouseup handler was reading the note's position from a React state snapshot that existed when the callback was first created, not the current position after dragging.

React state updates are asynchronous. By the time mouseup fires, the state you close over when creating the handler can be many renders behind. The note looks like it moved on screen but the value you're saving to the database is the old one.

The fix is to store the live position in a ref that gets updated on every mousemove:

const
 
dragging
 
=
 
useRef
<
{

 
id
:
 
string

 
ox
:
 
number
 
// original position

 
oy
:
 
number

 
startX
:
 
number
 
// mouse start

 
startY
:
 
number

 
finalX
:
 
number
 
// updated every mousemove

 
finalY
:
 
number

}
 
|
 
null
>
(
null
)

// in onMouseMove:

const
 
nx
 
=
 
snap
(
dragging
.
current
.
ox
 
+
 
dx
,
 
board
.
mode
)

const
 
ny
 
=
 
snap
(
dragging
.
current
.
oy
 
+
 
dy
,
 
board
.
mode
)

dragging
.
current
.
finalX
 
=
 
nx

dragging
.
current
.
finalY
 
=
 
ny

setNotes
(
ns
 
=>
 
ns
.
map
(
n
 
=>

 
n
.
id
 
===
 
dragging
.
current
?.
id
 
?
 
{
 
...
n
,
 
x
:
 
nx
,
 
y
:
 
ny
 
}
 
:
 
n

))

// in onMouseUp:

const
 
{
 
id
,
 
finalX
,
 
finalY
 
}
 
=
 
dragging
.
current

dragging
.
current
 
=
 
null
 
// clear before the async call

await
 
supabase
.
from
(
"
notes
"
).
update
({
 
x
:
 
finalX
,
 
y
:
 
finalY
 
}).
eq
(
"
id
"
,
 
id
)

Enter fullscreen mode

Exit fullscreen mode

Refs are mutable and always give you the current value regardless of when the closure was created. The note position in the ref is the actual final position at the time mouseup fires. Problem solved.

### Row Level Security and the upvote problem

Supabase uses Postgres Row Level Security. Policies on every table control what each user can read, insert, update, and delete. Skip this and your database is open to anyone who gets your anon key, which is embedded in your frontend bundle and completely public.

Most of the policies are straightforward. The upvote one was not.

I needed to stop clients from directly setting the upvotes column to any arbitrary number. My first attempt was awith checkconstraint that compared the column value against a subquery back into the notes table:

create
 
policy
 
"update notes"
 
on
 
notes

 
for
 
update
 
using
 
(...)

 
with
 
check
 
(

 
upvotes
 
=
 
(
select
 
upvotes
 
from
 
notes
 
where
 
id
 
=
 
notes
.
id
)

 
)

Enter fullscreen mode

Exit fullscreen mode

That caused infinite recursion. Postgres tried to evaluate the policy. The policy read from the notes table. Reading from the notes table triggered the policy. Which read from the notes table again. Stack overflow at the database level.

The actual solution was aSECURITY DEFINERfunction that owns the entire upvote operation:

create
 
or
 
replace
 
function
 
increment_upvote
(
note_id
 
uuid
,
 
voter_fp
 
text
)

returns
 
json

language
 
plpgsql

security
 
definer

as
 
$$

declare

 
already_voted
 
boolean
;

 
new_count
 
integer
;

begin

 
select
 
exists
(

 
select
 
1
 
from
 
note_votes
 
 
where
 
note_votes
.
note_id
 
=
 
increment_upvote
.
note_id

 
and
 
voter_fingerprint
 
=
 
voter_fp

 
)
 
into
 
already_voted
;

 
if
 
already_voted
 
then

 
return
 
json_build_object
(
'success'
,
 
false
,
 
'reason'
,
 
'already_voted'
);

 
end
 
if
;

 
insert
 
into
 
note_votes
 
(
note_id
,
 
voter_fingerprint
)

 
values
 
(
increment_upvote
.
note_id
,
 
voter_fp
);

 
update
 
notes
 
set
 
upvotes
 
=
 
upvotes
 
+
 
1

 
where
 
id
 
=
 
increment_upvote
.
note_id

 
returning
 
upvotes
 
into
 
new_count
;

 
return
 
json_build_object
(
'success'
,
 
true
,
 
'upvotes'
,
 
new_count
);

end
;

$$
;

Enter fullscreen mode

Exit fullscreen mode

SECURITY DEFINERmeans the function runs with the database owner's permissions, not the caller's. Direct inserts into note_votes are blocked at the policy level. The only way to register a vote is to call this function. The function checks for duplicate votes and increments atomically. Nobody can manipulate the upvotes column directly from the client.

### How positions save to the database

Every note has x, y, width, and rotation columns. These are floats. When you drag a note and let go, one database update fires with the new coordinates. When someone else is watching the board, Supabase Realtime delivers the UPDATE event and the note moves on their screen.

The rotation is set once at insert time. A random value between negative three and positive three degrees, stored permanently. It never changes after that. This is what makes the board look like a real corkboard rather than a grid.

For grid mode, coordinates snap to the nearest 32-pixel increment before saving:

function
 
snap
(
v
:
 
number
,
 
mode
:
 
Board
[
"
mode
"
])
 
{

 
return
 
mode
 
===
 
"
grid
"
 
?
 
Math
.
round
(
v
 
/
 
GRID
)
 
*
 
GRID
 
:
 
v

}

Enter fullscreen mode

Exit fullscreen mode

Free mode and ruled mode skip the snap entirely. The function is pure, called in the mousemove handler for live preview and again before the database write to make sure what you see is what gets saved.

### Input validation on both sides

Everything goes through a sanitizer before touching the database:

export
 
function
 
sanitizeText
(
input
:
 
string
):
 
string
 
{

 
return
 
input

 
.
replace
(
/<
[^
>
]
*>/g
,
 
""
)
 
// strip HTML tags

 
.
replace
(
/javascript:/gi
,
 
""
)
 
// kill JS URIs

 
.
trim
()

}

Enter fullscreen mode

Exit fullscreen mode

Length limits are enforced in onChange handlers so you can't even attempt to submit something too long. And then as a final backstop, the database has column-level constraints:

alter
 
table
 
notes

 
add
 
constraint
 
notes_content_length
 
 
check
 
(
char_length
(
content
)
 
between
 
1
 
and
 
500
),

 
add
 
constraint
 
notes_upvotes_nonneg
 
 
check
 
(
upvotes
 
>=
 
0
)

Enter fullscreen mode

Exit fullscreen mode

If someone bypasses the frontend entirely and sends raw API requests, the database rejects anything that violates these. Two layers, independently enforced.

### The GDPR stuff

I want this to be something people can trust. So I built proper data rights in from the start rather than adding them later when it's annoying.

Two Postgres functions do the work.

Data export returns everything we hold about you as JSON. The account page downloads it as a file. One click, you have your data. This satisfies GDPR Article 20.

Account deletion is more involved. It needs to delete all your boards (notes cascade via foreign key), anonymise any notes you posted on other people's boards (content stays, attribution is removed), delete your profile, then delete the auth record. The last step requires elevated permissions, so the function runs as SECURITY DEFINER. After the database operations, the client clears localStorage and signs out.

Total wipe. Nothing left.

## Auth

GitHub OAuth via Supabase. Email and password if you prefer.

A Postgres trigger creates a profile record automatically when someone signs up:

create
 
or
 
replace
 
function
 
handle_new_user
()

returns
 
trigger
 
as
 
$$

begin

 
insert
 
into
 
public
.
profiles
 
(
id
,
 
email
,
 
display_name
)

 
values
 
(

 
new
.
id
,

 
coalesce
(
new
.
email
,
 
''
),

 
coalesce
(

 
new
.
raw_user_meta_data
->>
'display_name'
,

 
split_part
(
coalesce
(
new
.
email
,
 
'anonymous'
),
 
'@'
,
 
1
)

 
)

 
)

 
on
 
conflict
 
(
id
)
 
do
 
nothing
;

 
return
 
new
;

end
;

$$
 
language
 
plpgsql
 
security
 
definer
;

Enter fullscreen mode

Exit fullscreen mode

on conflict do nothingstops errors if the trigger somehow fires twice for the same user. This happened during testing more than once so I'm glad it's there.

Route protection is a Next.js middleware that checks Supabase session before serving protected pages. If there's no session, you get redirected to login with your intended destination as a query parameter. After signing in you land where you meant to go.

Anonymous users can post on public and link-only boards with no account at all. Their notes show an author name from localStorage. Their votes are tracked by a random fingerprint also from localStorage. Nothing tied to an identity. Nothing in the database except the note itself.

## The Boards: How the Full Flow Works

You create a board on/new. Title, description, a prompt for contributors, canvas mode, visibility. Submit and you get redirected to/board/your-slug.

The slug is generated from the board title with a four-character random suffix to prevent collisions.sprint-retro-3a7finstead of justsprint-retro. Simple and human-readable.

The board page is a Next.js server component that fetches the board data and initial notes server-side. This matters for performance: when the page loads the canvas is already populated. No loading spinner. No empty board that fills in after a moment. The notes are in the HTML.

After that initial load, Supabase Realtime takes over and handles all subsequent updates. Two different systems, each doing exactly what they're good at.

Board settings let owners update the title, description, prompt, canvas mode, and visibility. Changing mode from free to grid doesn't move any existing notes, it just starts snapping new ones. Changing visibility takes effect immediately.

Deleting a board requires typing the board title to confirm. All notes cascade-delete. Irreversible. The confirmation requirement is annoying on purpose.

## What's Coming

The npm package is the thing I'm most focused on right now.

The iframe embed works well but dropping a component directly into your app is a much cleaner experience when you're already in a React codebase. The plan is a<PostItBoard />with a TypeScript API, theming props so it doesn't look foreign in your UI, and SSR safety so it works in Next.js without hydration warnings.

import
 
{
 
PostItBoard
 
}
 
from
 
"
postitup
"

<
PostItBoard

 
board
=
"
your-board-slug
"

 
baseUrl
=
"
https://postitup.varshithvhegde.in
"

 
height
=
{
500
}

 
theme
=
"
paper
"

/>

Enter fullscreen mode

Exit fullscreen mode

That's the shape of it. Publishing to npm soon. Watch the GitHub repo if you'd use this.

After that:lane mode. Columns. Kanban-style layout so you can have things like Liked / Meh / Disliked for product feedback sessions, or What Went Well / What Didn't / Action Items for retros. Same real-time sync, same anonymous posting, just organized into columns instead of a free canvas.

Andboard templatesso you're not starting from scratch every time you want to run a retro.

## Free. Actually Free.

The whole thing runs on Supabase free tier and Vercel hobby plan.

Supabase free: 500MB database, 50,000 monthly active users, unlimited API requests.Vercel hobby: unlimited deployments, free domain, fast edge network.

You're not going to hit those limits running retros with your team.

This is the same lesson as the FormRelay thing I wrote about a while back. There's this huge gap between "run your own servers" and "pay $20 a month for something that's really just a database insert". An embarrassing number of problems that cost real money every month are actually just weekend projects in disguise.

 Varshith V Hegde
 

 Varshith V Hegde
 

Varshith V Hegde

 Follow
 

Dec 30 '25

## I Built a Form Backend in a Weekend Because Paying $20/Month for Contact Forms is Stupid

#
opensource

#
saas

#
webdev

#
beginners

71
 reactions

Comments

 52
 comments

 3 min read
 

A sticky note board that updates in real time sounds complicated. It isn't. It's a database table, a WebSocket subscription, and a canvas that knows how to drag things around. Total code across the meaningful files is maybe two thousand lines. You could read the whole repo in an afternoon.

## Try It

Live:postitup.varshithvhegde.in

Source:github.com/Varshithvhegde/postitup

## Varshithvhegde/postitup

### Collaborative sticky note boards — embeddable, real-time, paper-aesthetic

# PostItUp 📌

A real-time collaborative sticky note board for the web. Paper aesthetic, anonymous posting, embeddable anywhere.

Live:postitup.varshithvhegde.in

## What it is

PostItUp lets you create a board, share a link, and anyone can drop a sticky note in real time — no account required. Think retros, feedback sessions, brainstorming, or just collecting ideas from a group.

## Features

* Three canvas modes— free-drag, grid snap, or ruled lines
* Real-time sync— notes appear live via Supabase Realtime
* Anonymous posting— no signup needed on public/link boards
* Star ratings— boards can optionally collect 1-5 star reviews shown as cards on the canvas
* Drag notes— reposition any note, position saves instantly
* Upvotes— thumbs up notes you agree with (one per device)
* Embeddable— iframe, script tag, or React component
* GDPR compliant— data export and full account deletion built in

## Creating a board

Pick a canvas mode, set visibility…

View on GitHub

Create a board. Share the link with someone. Watch notes appear in real time.

If something is broken or you have a feature idea, open an issue. If you want to contribute, PRs are open. MIT licensed so do whatever you want with it.

And if you end up using the embed somewhere, I'd genuinely love to see it. Drop it in the comments or email me atvarshithvh@gmail.com.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse