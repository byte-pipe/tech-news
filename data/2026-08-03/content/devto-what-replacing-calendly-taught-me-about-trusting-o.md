---
title: What Replacing Calendly Taught Me About Trusting Open Source - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/what-replacing-calendly-taught-me-about-trusting-open-source-540a
site_name: devto
content_file: devto-what-replacing-calendly-taught-me-about-trusting-o
fetched_at: '2026-08-03T19:33:24.718859'
original_url: https://dev.to/pascal_cescato_692b7a8a20/what-replacing-calendly-taught-me-about-trusting-open-source-540a
author: Pascal CESCATO
date: '2026-07-29'
description: cal.com, Calendly, zcal... booking SaaS isn't short on options, and most of them are genuinely... Tagged with webdev, selfhosted, opensource, security.
tags: '#webdev, #selfhosted, #opensource, #security'
---

Sparked by SaaS limits and privacy shifts

cal.com, Calendly, zcal... booking SaaS isn't short on options, and most of them are genuinely decent. Free tiers cover the basics for a lot of freelancers. The catch: you're the product (nothing's really free), and your customer data lives somewhere you don't fully control and can't fully audit.

A dysfunction I ran into on another SaaS tool was the trigger. Trusting a third-party service by default, just because it's widely used and billed monthly, doesn't always hold up. That episode was enough to make me reconsider every external service this site was relying on for functionality that's actually simple to self-host — and the booking widget, running on Calendly, was one of them.

Nothing wrong with Calendly specifically. It worked fine. But structural friction had been building regardless: a recurring subscription for something as simple as displaying open slots and recording a choice, a hard dependency on a third party for a component with nothing exceptional about it technically, and customization capped by whatever the vendor exposes in settings — no way to go further if a need falls outside that box. On top of that, an integration constraint that mattered more than any of the above: the site runs on Astro, generating lightweight static pages by design, specifically to avoid the weight of third-party scripts and dependencies — the exact opposite of what embedding a SaaS widget implies.

So: could a self-hosted alternative match the experience, without the monthly bill and without handing a core commercial function (people booking a call with me) to an external vendor? This is the write-up of that search, the codebase audit that came out of it, and the production rollout.

## The landscape

Four self-hosted candidates stood out as genuinely comparable — not just UI skins sitting on top of someone else's API, not just internal-scheduling tools with the public-facing UX as an afterthought.

CloudMeet— Svelte + TypeScript, deployed on Cloudflare Pages/Workers/D1, free-tier friendly. MIT licensed. Clean booking UX. Single maintainer, ~490 stars, 37 commits — young, not enough track record to trust blind.

Cal.diy— the community fork of cal.com's booking engine, spun up after cal.com closed-sourced their core product in April 2026, citing security risk from AI-assisted code scanning against their public repo. MIT licensed, maintained by former cal.com interns. Full scheduling engine, app-store integrations, Stripe/PayPal payment support carried over. Most feature-complete on paper. Also the youngest as an independent community project — their own docs still discourage production use without caveats.

booking-calendar— React + TypeScript + Bun + SQLite, single-admin design, native bidirectional CalDAV sync instead of a Google/Outlook lock-in. Clean architecture (repository/service/entity separation via TypeORM). Lightweight, portable by design. Booking UI is a scrollable list of time slots — functional, but nowhere near the polish of a commercial scheduler.

Easy!Appointments— PHP/CodeIgniter + MySQL, ten years of active development, 3000+ stars, a paid tier that's existed for years. Most battle-tested of the four, and the one with the closest booking UX to Calendly itself: monthly calendar view, multi-step wizard.

What I was actually optimizing for: framework-agnostic integration (no PHP running on the public site itself), booking UX quality, native GDPR consent handling, and enough production maturity to put in front of real prospects rather than an experimental project.

## Narrowing down

CloudMeet and Cal.diy dropped out early, for the same underlying reason: not enough track record for production use, not a specific flaw found. CloudMeet's single-maintainer status and short commit history made it too much of a bet. Cal.diy's own documentation still hedges on production readiness three months post-launch. Whether either becomes a serious contender or stays a one-shot project is a question for later.

Worth being honest about what that is: a decision made on reputation and project age, the exact shortcut this piece argues against later on. Auditing four codebases in the same depth as the two finalists below wasn't a realistic use of time, so CloudMeet and Cal.diy got a lighter pass — young-project heuristics instead of a source read. That's a real gap in the method, not just a caveat to mention in passing.

That left booking-calendar and Easy!Appointments. And this is where the UX gap tipped it: booking-calendar's public booking page is a plain scrollable list ofMonday, February 23, 2026 at 08:00 AMrows — accurate, but visually miles from what Calendly conditioned people to expect. No month view, no staged flow, just text to scroll through.

I briefly considered franken-stacking the two — CloudMeet's frontend on top of booking-calendar's CalDAV backend, or something along those lines. Not viable in practice: different runtimes (Cloudflare Workers/D1 vs Bun/SQLite), no shared API contract, no shared data model. Bolting two incompatible stacks together usually creates more work than picking one and adapting it. Went with separation of concerns instead: pick the tool with the better public-facing UX, and if native CalDAV sync becomes a real need later, that's a second, independent tool — not a merge.

Easy!Appointments won on UX. Onto the part that actually mattered for a production decision.

## The audit: a TOCTOU race condition, in both remaining candidates

Before committing to either, I wanted to check one specific thing: what happens if two visitors click the same slot at nearly the same instant? Not a theoretical concern — it's the kind of bug that never shows up in solo development and blows up the day a booking link gets shared a bit wider (a newsletter blast, a LinkedIn post, a batch of new slots opening at a fixed time).

This is a classic TOCTOU (time-of-check to time-of-use) race condition: the code checks that a slot is free, then writes the booking — and nothing stops a concurrent request from doing the exact same check in between, before either write lands. Without a lock spanning both the check and the write, two requests can both conclude "free" before either commits.

### booking-calendar

TypeORM-based, repository pattern, otherwise clean separation of concerns. The overlap check:

async
 
hasOverlapInSlot
(

 
slotId
:
 
number
,

 
startAt
:
 
string
,

 
endAt
:
 
string
,

 
manager
?:
 
EntityManager
,

):
 
Promise
<
boolean
>
 
{

 
const
 
count
 
=
 
await
 
this
.
repo
(
manager
)

 
.
createQueryBuilder
(
"
a
"
)

 
.
where
(
"
a.slot_id = :slotId
"
,
 
{
 
slotId
 
})

 
.
andWhere
(
"
a.canceled_at IS NULL
"
)

 
.
andWhere
(
"
a.status != 'rejected'
"
)

 
.
andWhere
(
"
NOT (a.end_at <= :startAt OR a.start_at >= :endAt)
"
,
 
{

 
startAt
,

 
endAt
,

 
})

 
.
getCount
();

 
return
 
count
 
>
 
0
;

}

Enter fullscreen mode

Exit fullscreen mode

Called inside a transaction (AppDataSource.transaction), but no.setLock("pessimistic_write"), no exclusion constraint at the schema level. Under SQLite, this never surfaces: the engine serializes writers, one at a time, by design. It's a free safety net courtesy of the storage engine — not a guarantee the application code actually enforces. The project's own architecture explicitly anticipates a migration path to Postgres or MySQL via TypeORM's driver abstraction (type: "sqlite"→type: "postgres", straightforward on paper). That's exactly the migration that removes the net: underREAD COMMITTEDisolation, two concurrent transactions can each read "no overlap" before either one'sINSERTcommits.

Confirmed by reading the CalDAV sync layer too — a second, independent race, this one against theexternalcalendar rather than the local database:

private
 
async
 
getCachedBusyIntervals
(
startAt
:
 
string
,
 
endAt
:
 
string
):
 
BusyInterval
[]
 
|
 
null
 
{

 
const
 
cache
 
=
 
CalDAVService
.
busyIntervalCache
;

 
if 
(
!
cache
 
||
 
cache
.
expires_at
 
<=
 
Date
.
now
())
 
{

 
return
 
null
;

 
}

 
if 
(
startAt
 
<
 
cache
.
start_at
 
||
 
endAt
 
>
 
cache
.
end_at
)
 
{

 
return
 
null
;

 
}

 
return
 
cache
.
intervals
.
filter
(

 
(
interval
)
 
=>
 
!
(
interval
.
end_at
 
<=
 
startAt
 
||
 
interval
.
start_at
 
>=
 
endAt
),

 
);

}

Enter fullscreen mode

Exit fullscreen mode

A process-wide static cache with a TTL, invalidated onlyaftera successful write. Two bookings arriving seconds apart, inside the cache window, can both read the same "free" snapshot before either has finished writing to the external calendar — the exact same TOCTOU shape, just with the external CalDAV server as the source of truth instead of the local DB.

### Easy!Appointments

Ten years in production, 3000+ GitHub stars, a paid tier that's existed for years. The working hypothesis going in: more real-world traffic means more chances this exact class of bug already got hit and fixed. That hypothesis doesn't survive reading the code.

The public booking flow:

// Check appointment availability before registering it to the database.

$appointment
[
'id_users_provider'
]
 
=
 
$this
->
check_datetime_availability
();

if
 
(
!
$appointment
[
'id_users_provider'
])
 
{

 
throw
 
new
 
RuntimeException
(
lang
(
'requested_hour_is_unavailable'
));

}

// ... customer lookup/creation, GDPR consent records, Jitsi link generation ...

$appointment_id
 
=
 
$this
->
appointments_model
->
save
(
$appointment
);

Enter fullscreen mode

Exit fullscreen mode

Several unrelated operations sit between the check and the write — the race window here is wider than booking-calendar's, where check and insert at least shared a transaction. And the insert itself:

protected
 
function
 
insert
(
array
 
$appointment
):
 
int

{

 
$appointment
[
'book_datetime'
]
 
=
 
date
(
'Y-m-d H:i:s'
);

 
$appointment
[
'create_datetime'
]
 
=
 
date
(
'Y-m-d H:i:s'
);

 
$appointment
[
'update_datetime'
]
 
=
 
date
(
'Y-m-d H:i:s'
);

 
$appointment
[
'hash'
]
 
=
 
random_string
(
'alnum'
,
 
12
);

 
if
 
(
!
$this
->
db
->
insert
(
'appointments'
,
 
$appointment
))
 
{

 
throw
 
new
 
RuntimeException
(
'Could not insert appointment.'
);

 
}

 
return
 
$this
->
db
->
insert_id
();

}

Enter fullscreen mode

Exit fullscreen mode

No transaction, no lock, no unique constraint. The docblock oncheck_datetime_availability()reads:

"It is possible that two or more customers select the same appointment date and time concurrently. The app won't allow this to happen."

Documented intent, not what the code actually does.

### The interesting part

Appointments_modelcontains a method that does the correct overlap check, with a properly built query:

public
 
function
 
has_provider_conflict
(

 
int
 
$provider_id
,

 
string
 
$start_datetime
,

 
string
 
$end_datetime
,

 
?int
 
$exclude_appointment_id
 
=
 
null
,

):
 
bool
 
{

 
$this
->
db
->
select
(
'id'
)
->
from
(
'appointments'
)
->
where
(
'id_users_provider'
,
 
$provider_id
);

 
if
 
(
$exclude_appointment_id
)
 
{

 
$this
->
db
->
where
(
'id !='
,
 
$exclude_appointment_id
);

 
}

 
// Overlap: (existing_start < new_end) AND (existing_end > new_start)

 
return
 
$this
->
db

 
->
group_start
()

 
->
where
(
'start_datetime <'
,
 
$end_datetime
)

 
->
where
(
'end_datetime >'
,
 
$start_datetime
)

 
->
group_end
()

 
->
get
()

 
->
num_rows
()
 
>
 
0
;

}

Enter fullscreen mode

Exit fullscreen mode

It's never called anywhere in the public booking flow. The correct primitive exists in the codebase; it's just not wired in where it would matter.

### Takeaway

Neither project is "more robust" than the other on this specific point — both share the same design gap, independent of relative maturity. Reputation, age, an established commercial tier: reasonable statistical priors, not proof. The only way to know whether an open-source project actually guards against this class of bug is to read the code doing the work, not the comment claiming it does.

For what it's worth, the fix on the Easy!Appointments side is close to a drop-in — the correct primitive (has_provider_conflict) already exists, it's a matter of wiring it in with a lock around check+write rather than designing a new one:

$lock_name
 
=
 
"provider_
{
$provider_id
}
_booking"
;

if
 
(
!
$this
->
db
->
query
(
"SELECT GET_LOCK(?, 10)"
,
 
[
$lock_name
])
->
row
()
->
{
"GET_LOCK(?, 10)"
})
 
{

 
throw
 
new
 
RuntimeException
(
'Could not acquire booking lock.'
);

}

try
 
{

 
if
 
(
$this
->
appointments_model
->
has_provider_conflict
(

 
$appointment
[
'id_users_provider'
],

 
$appointment
[
'start_datetime'
],

 
$appointment
[
'end_datetime'
]

 
))
 
{

 
throw
 
new
 
RuntimeException
(
lang
(
'requested_hour_is_unavailable'
));

 
}

 
$appointment_id
 
=
 
$this
->
appointments_model
->
save
(
$appointment
);

}
 
finally
 
{

 
$this
->
db
->
query
(
"SELECT RELEASE_LOCK(?)"
,
 
[
$lock_name
]);

}

Enter fullscreen mode

Exit fullscreen mode

GET_LOCKrather than a schema-level exclusion constraint because MySQL has no equivalent to Postgres'EXCLUDE USING gist— no declarative way to say "no two overlapping ranges for this provider" at the database level. The lock key is scoped per-provider (provider_{id}_booking) rather than global, so two visitors booking with twodifferentproviders at the same instant don't block each other for no reason.RELEASE_LOCKsits in afinallyso a failed write doesn't leave the lock held until timeout.

One dependency this fix quietly assumes: non-persistent database connections.GET_LOCKis scoped to the MySQL session, not the PHP request — it lives and dies with the connection. That holds cleanly on a standard non-persistent connection (the CodeIgniter default), where each request gets its own connection and the lock disappears cleanly when it ends, even on an uncaught fatal. It stops holding ifpconnectis enabled and connections get reused across unrelated requests from a pool:RELEASE_LOCKin thefinallymight release a lock adifferentrequest just acquired on the same recycled connection, or a lock could outlive the request that took it. Worth stating explicitly in the patch rather than assuming, since it's not somethinghas_provider_conflict()or the surrounding code makes obvious either way.

This didn't end up shipping in my deployment — the LOCK/VERIFY/WRITE/UNLOCK skeleton above is close to production-ready, but I'd want load-test coverage on theANY_PROVIDERbranch (where the code searches foranyavailable provider — the lock needs to span that search too, or two "any provider" requests can still land on the same provider/slot in parallel) before calling it done. Worth a PR upstream at some point.

## Production rollout: a simple embed, an unexpected block

The integration itself was straightforward: Easy!Appointments runs on its own subdomain, the contact page just drops an<iframe>pointing at it. No PHP touches the public Astro site at all — that separation was the whole point.

First test after deploying: the iframe wouldn't render. Console error:

Refused to display 'https://cal.example.com/' in a frame because it set
'X-Frame-Options' to 'sameorigin'.

Enter fullscreen mode

Exit fullscreen mode

### First guess, wrong

Given the server setup (a hosting panel with a reverse-proxy layer in front of the site), the obvious first suspect was that layer, not the app itself. Tried unsetting the header at the.htaccesslevel:

<
IfModule
 mod_headers.c
>

 
Header
 
always
 
unset
 X-Frame-Options
 
Header
 
always
 
set
 Content-Security-Policy "frame-ancestors 'self' https://backstage.click"

</
IfModule
>

Enter fullscreen mode

Exit fullscreen mode

No effect. Header still showed up oncurl -I.

### The actual cause

Grepping the Easy!Appointments source turned it up directly:

.
/
application
/
hooks
/
security_headers
.
php
:
 
header
(
'X-Frame-Options: SAMEORIGIN'
);

.
/
application
/
config
/
routes
.
php
:
header
(
'X-Frame-Options: SAMEORIGIN'
);

Enter fullscreen mode

Exit fullscreen mode

The app sets the header itself, in PHP, at two separate points in its own bootstrap — a hardcoded anti-clickjacking default, sensible for the admin panel, applied indiscriminately to every route including the public booking page that's meant to be embedded elsewhere.Header unsetin.htaccessruns at the web-server response-table level, ahead of the PHP process; aheader()call executed later by the script itself simply overrides it. The.htaccessfix couldn't have worked against this, structurally, regardless of server (Apache, Nginx, OpenLiteSpeed) — PHP has the last word on its own headers as long as output hasn't started.

The working fix patches both call sites, scoped to the booking controller only so the admin panel keeps its default protection:

$CI
 
=&
 
get_instance
();

if
 
(
get_class
(
$CI
)
 
===
 
'Booking'
)
 
{

 
header
(
"Content-Security-Policy: frame-ancestors 'self' https://backstage.click"
);

}
 
else
 
{

 
header
(
'X-Frame-Options: SAMEORIGIN'
);

}

Enter fullscreen mode

Exit fullscreen mode

Using the instantiated controller class rather than parsing$_SERVER['REQUEST_URI']— this install doesn't have clean URLs enabled (index.phpshows up in the booking URL), so a naivestrpos($uri, '/booking') === 0check would silently fail to match.

One thing worth flagging for anyone patching the same two files: they're core application code, not a plugin layer. A futuregit pullor a Docker image rebuild will silently overwrite this fix. Worth keeping it as a versioned patch file (git diffbefore/after) to reapply after upgrades, rather than losing it the next time the container gets rebuilt.

## Result

Customer data (name, email, meeting reason) staying on infrastructure I control instead of a third party's, and the site's initial page weight untouched — no third-party script added for this one feature. Cost wasn't really the driver here; free tiers cover the basics for a lot of freelancers, mine included. What I was buying back wasn't a subscription fee, it was the part where a vendor decides what "the basics" are, and where my prospects' contact details end up.

Worth noting: which of the four tools actually fits depends entirely on what a given business needs, not on which one "won" here. Easy!Appointments, for instance, is also a solid self-hosted alternative to Bookly for anyone running WordPress and looking to drop a booking plugin subscription — different starting point, same underlying question.

But the tool swap itself isn't really the point. This is one instance of a pattern I keep coming back to: default to self-hosted where it's reasonable, and don't let "widely used" or "ten years old" or "has a paid tier" stand in for actually checking. Reputation is a prior, not a verdict. The Easy!Appointments audit is the clearest example in this piece — a decade of production traffic, a commercial offering, thousands of stars, and a race condition sitting in the exact code path that mattered most, with the correct fix already written elsewhere in the codebase and simply never called. Maturity didn't catch it. Reading the code did.

Here's the part worth sitting with, though: the fix never shipped on my own deployment either. It's sketched out above, unfinished, blocked on load-testing I haven't done. Which means the instance running this site's booking page right now is, as far as I know, still exposed to the exact TOCTOU window this whole piece is about. Self-hosting bought me visibility into that gap — Calendly would have hidden it behind a vendor's SLA and I'd have had no way to know either way. It didn't buy me the fix. That's a separate piece of work, and skipping it doesn't get excused by having found the bug in the first place. Self-hosting gets you control. Security still has to be built, on your own time, by someone — and until that patch actually lands, that someone is a task on my list, not a claim in this article.

Neither was this the fastest of the four options, or the most obvious. It took a real comparison between projects, a debugging detour once in production, and time spent reading source instead of trusting a README. That's the actual cost of running your own infrastructure instead of renting someone else's.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (19 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.
 Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse