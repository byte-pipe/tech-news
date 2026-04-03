---
title: 'When Debugging Became Belonging: What Nearly 15 Years of Helping Developers Taught Me - DEV Community'
url: https://dev.to/darkbranchcore/when-debugging-became-belonging-what-nearly-15-years-of-helping-developers-taught-me-3amg
site_name: devto
content_file: devto-when-debugging-became-belonging-what-nearly-15-yea
fetched_at: '2026-04-01T11:24:21.919940'
original_url: https://dev.to/darkbranchcore/when-debugging-became-belonging-what-nearly-15-years-of-helping-developers-taught-me-3amg
author: Niels
date: '2026-03-30'
description: The first time code made me question my place in tech, it was not elegant. It was not cinematic... Tagged with devchallenge, wecoded, dei, career.
tags: '#devchallenge, #wecoded, #dei, #career'
---

WeCoded 2026: Echoes of Experience 💜

The first time code made me question my place in tech, it was not elegant.

It was not cinematic either, unless your favorite genre is “junior developer stares at legacy JavaScript while silently bargaining with the universe.” Mine happened on a gray Monday morning, the kind of morning where even coffee feels underqualified. I had just been given my first real bug on my first real project at a company paying me real money to write code. That should have felt empowering. Instead, it felt like being handed a fork and asked to repair a jet engine.

The instruction was almost offensive in its simplicity: “Just fix this bug.”

Anyone who has worked with old code knows that “just” is one of the most dangerous words in software development. I opened the file and found the usual archaeological layers of logic, half-decisions, mysterious comments, and code that looked like three different developers had fought each other and the code had won. I tried to run the app. Errors. I changed something. More errors. I changed something else. New errors, different font, same emotional damage.

For a while, I did what many early-career developers do but rarely admit out loud: I mistook confusion for incompetence.

I was not only debugging the application. I was debugging my confidence. I wondered whether I belonged in tech, whether the recruiter had emailed the wrong person, whether my future career path might somehow involve leaving software altogether and becoming a professional yodeler in Switzerland. It felt dramatic at the time. In hindsight, it was dramatic. But it was also real.

And then I did the thing that scared me most.

I asked for help.

I still remember how big that tiny sentence felt: “I’m stuck. I don’t know what to do.”

What changed me was not just that someone answered. It was how she answered. A senior engineer walked me through the logic without making me feel small. She did not treat my confusion like a personal failure. She treated it like part of the craft. She showed me where the code bent, where it broke, and where I could safely touch it without summoning six new production incidents. Less than an hour later, I fixed the bug.

That should have been the victory. But it was not.

The real victory was learning that asking for help was not proof that I was weak. It was proof that I was still in the fight.

That lesson stayed with me far longer than the bug did. Since then, I have met deadlines that felt like punishment, APIs that behaved like they had a private grudge against me, and merge conflicts that probably qualify as spiritual warfare. But I have also learned that growth in this industry rarely arrives looking polished. Usually it arrives wearing panic, carrying a stack trace, and asking whether you have tried turning your assumptions off and on again.

That is one reason the idea of WeCoded matters to me.

Too many developers, especially those from underrepresented and marginalized genders, spend part of their careers being made to feel that uncertainty is something shameful. That not knowing is a flaw. That asking questions is a weakness. But the healthiest technical spaces I have ever seen were not the ones full of people performing brilliance. They were the ones full of people practicing generosity.

The engineers who changed my life were not always the loudest people in the room. They were the ones who made room. They explained without humiliating. They corrected without performing superiority. They understood that inclusion is not a slogan you put on a company page. It is a daily engineering practice. It is visible in code reviews, in mentoring, in who gets heard, in who gets interrupted, in who feels safe saying, “I don’t understand this yet.”

That word matters: yet.

Because “yet” has carried a lot of developers farther than talent alone ever could.

For me, that journey did not stop at surviving hard moments in code. Over time, it turned into a habit of showing up for other developers too. For nearly fifteen years, I have been active on Stack Overflow under the name Niels, where I have built a record of more than 50,000 reputation, 680 answers, and 40 questions, with strong activity around JavaScript, jQuery, MySQL, HTML, and PHP.

## User Niels - Stack Overflow

 stackoverflow.com
 

My profile still describes the same practical mix of technologies and the same instinct to help others that shaped me early on.

And honestly, that long Stack Overflow chapter taught me something important about community: most of software is not built by isolated genius. It is built by people answering each other’s questions on ordinary weekdays.

One person asks why their URL parameters are breaking. Another asks how to reset an auto-increment value in MySQL. Someone else is fighting jQuery, as humanity has done for generations. The problems are rarely glamorous, but the act itself is powerful. Every answer is a small vote for access. Every explanation says, “You do not have to stay stuck here alone.”

That same spirit is exactly why I wanted my first real Dev.to post to be more than just another article sitting in a browser tab.

So I built something around the reading experience itself.

The project I prepared is Always with Dev.to — Desktop Client, a cross-platform Electron desktop application designed to wrap Dev.to into a more native, focused experience. It uses vanilla JavaScript, HTML, and CSS inside Electron, with an embedded Express backend that proxies the Dev.to public API, handles authentication, and manages caching, all packaged into a single portable executable with no installation required.

What I love about that project is that it reflects how I now think about software: not just “Does it run?” but “Does it make the experience kinder, simpler, and more useful?”

The interesting part was not only the interface. It was the engineering behind the convenience. I embedded the backend directly into the Electron main process rather than forcing a separate backend service and extra orchestration. I packaged the app as a single portable .exe while carrying the backend resources with it. I added in-memory LRU caching with TTL and pattern invalidation to avoid hammering the Dev.to API. I used retry logic with exponential backoff for transient failures, added lazy Supabase initialization for authentication, and documented lessons from painful but useful issues like response-shape mismatches, temporal dead zone crashes, and a later layered-architecture refactor.

Embedding a backend server inside Electron

The challenge: Electron apps typically need a separate backend process, requiring IPC, process spawning, and port management. Instead, the Express server runs directly inside the Electron main process.

// frontend/main.js

function
 
startEmbeddedBackend
()
 
{

 
try
 
{

 
process
.
env
.
PORT
 
=
 
'
3000
'
;

 
const
 
isDev
 
=
 
!
app
.
isPackaged
;

 
const
 
envPath
 
=
 
isDev

 
?
 
path
.
join
(
__dirname
,
 
'
..
'
,
 
'
backend
'
,
 
'
.env
'
)

 
:
 
path
.
join
(
process
.
resourcesPath
,
 
'
backend
'
,
 
'
.env
'
);

 
require
(
'
dotenv
'
).
config
({
 
path
:
 
envPath
 
});

 
const
 
serverPath
 
=
 
isDev

 
?
 
path
.
join
(
__dirname
,
 
'
..
'
,
 
'
backend
'
,
 
'
server.js
'
)

 
:
 
path
.
join
(
process
.
resourcesPath
,
 
'
backend
'
,
 
'
server.js
'
);

 
require
(
serverPath
);

 
console
.
log
(
'
Backend server started on port 3000
'
);

 
}
 
catch 
(
err
)
 
{

 
console
.
error
(
'
Backend failed to start:
'
,
 
err
.
message
);

 
}

}

app
.
whenReady
().
then
(()
 
=>
 
{

 
startEmbeddedBackend
();
 
// server starts before window opens

 
createWindow
();

});

Enter fullscreen mode

Exit fullscreen mode

require(serverPath)loads the Express app into the same Node.js process Electron is already running. No child process, no IPC, no port negotiation. The.envpath switches between dev (source tree) and production (process.resourcesPath) automatically.

Building a single portable .exe

The challenge: packaging an Electron app with an embedded Express backend — including all backendnode_modules— into one file that runs without installation.

//
 
frontend/package.json
 
(build
 
config)

"build"
:
 
{

 
"win"
:
 
{

 
"target"
:
 
[{
 
"target"
:
 
"portable"
,
 
"arch"
:
 
[
"x64"
]
 
}],

 
"icon"
:
 
"icon.ico"
,

 
"signAndEditExecutable"
:
 
false

 
},

 
"extraResources"
:
 
[

 
{

 
"from"
:
 
"../backend"
,

 
"to"
:
 
"backend"
,

 
"filter"
:
 
[
"**/*"
,
 
"!*.log"
]

 
}

 
],

 
"files"
:
 
[

 
"**/*"
,

 
"!node_modules/.cache"
,

 
"!**/*.map"
,

 
"!**/*.md"

 
],

 
"directories"
:
 
{
 
"output"
:
 
"../dist"
 
}

}

Enter fullscreen mode

Exit fullscreen mode

extraResourcescopies the entirebackend/folder (including itsnode_modules) into the packaged app'sresources/directory. At runtime,process.resourcesPathpoints there. The original config had!node_modules/**in the filter — that excluded backend deps and broke the embedded server at runtime.

Bypassing Windows symlink restriction during build

The challenge:electron-builderdownloadswinCodeSign-2.6.0.7zwhich contains macOS symlinks (libcrypto.dylib,libssl.dylib). Extracting it on Windows without Developer Mode fails withCannot create symbolic link: A required privilege is not held by the client.

// frontend/node_modules/electron-builder/node_modules/

// app-builder-lib/out/binDownload.js (patched)

function
 
doGetBin
(
name
,
 
url
,
 
checksum
)
 
{

 
// winCodeSign archive contains macOS symlinks that fail to extract

 
// on Windows without Developer Mode. Return the already-extracted

 
// cache folder directly to skip the download+extract entirely.

 
if 
(
name
 
===
 
'
winCodeSign
'
)
 
{

 
const
 
path
 
=
 
require
(
'
path
'
);

 
const
 
os
 
=
 
require
(
'
os
'
);

 
const
 
cacheBase
 
=
 
process
.
env
.
ELECTRON_BUILDER_CACHE

 
||
 
path
.
join
(
os
.
homedir
(),
 
'
AppData
'
,
 
'
Local
'
,

 
'
electron-builder
'
,
 
'
Cache
'
);

 
return
 
Promise
.
resolve
(

 
path
.
join
(
cacheBase
,
 
'
winCodeSign
'
,
 
'
014093675
'
)

 
);

 
}

 
const
 
args
 
=
 
[
'
download-artifact
'
,
 
'
--name
'
,
 
name
];

 
if 
(
url
)
 
args
.
push
(
'
--url
'
,
 
url
);

 
if 
(
checksum
)
 
args
.
push
(
'
--sha512
'
,
 
checksum
);

 
return
 
executeAppBuilder
(
args
);

}

Enter fullscreen mode

Exit fullscreen mode

This patch was applied to all three copies ofbinDownload.jsacrosselectron-builder,dmg-builder, andelectron-builder-squirrel-windows. Combined with"signAndEditExecutable": falsein the build config to skip therceditstep that also triggers the same download.

In-memory LRU cache with TTL and pattern invalidation

The challenge: Dev.to API has rate limits. Every page load hitting the API directly would be slow and risk throttling. Need a fast in-process cache with automatic expiry and the ability to bust related keys when data changes.

// backend/server.js

class
 
LRUCache
 
{

 
constructor
(
maxSize
 
=
 
CACHE_MAX
)
 
{

 
this
.
_store
 
=
 
new
 
Map
();

 
this
.
_maxSize
 
=
 
maxSize
;

 
}

 
get
(
key
)
 
{

 
const
 
entry
 
=
 
this
.
_store
.
get
(
key
);

 
if 
(
!
entry
)
 
return
 
null
;

 
if 
(
Date
.
now
()
 
>
 
entry
.
exp
)
 
{
 
this
.
_store
.
delete
(
key
);
 
return
 
null
;
 
}

 
// LRU: delete and re-insert to move to end of Map iteration order

 
this
.
_store
.
delete
(
key
);

 
this
.
_store
.
set
(
key
,
 
entry
);

 
return
 
entry
.
data
;

 
}

 
set
(
key
,
 
data
,
 
ttl
)
 
{

 
if 
(
this
.
_store
.
size
 
>=
 
this
.
_maxSize
 
&&
 
!
this
.
_store
.
has
(
key
))
 
{

 
// evict the oldest entry (first key in Map)

 
this
.
_store
.
delete
(
this
.
_store
.
keys
().
next
().
value
);

 
}

 
this
.
_store
.
set
(
key
,
 
{
 
data
,
 
exp
:
 
Date
.
now
()
 
+
 
ttl
 
});

 
}

 
invalidatePattern
(
pattern
)
 
{

 
const
 
re
 
=
 
new
 
RegExp
(
pattern
.
replace
(
/
\*
/g
,
 
'
.*
'
));

 
for 
(
const
 
k
 
of
 
this
.
_store
.
keys
())
 
{

 
if 
(
re
.
test
(
k
))
 
this
.
_store
.
delete
(
k
);

 
}

 
}

}

// Usage: bust all article list caches when a reaction is posted

cache
.
delete
(
cacheKey
.
article
(
id
));

cache
.
invalidatePattern
(
'
articles:*
'
);

Enter fullscreen mode

Exit fullscreen mode

Mappreserves insertion order, so the first key is always the oldest — O(1) LRU eviction without a doubly-linked list. TTL is stored per-entry as an absolute expiry timestamp, checked on read.

Dev.to API proxy with exponential back-off retry

The challenge: network calls to Dev.to can fail transiently. Retrying immediately hammers the server. 4xx errors (bad request, unauthorized) should never be retried — only transient 5xx and network failures.

// backend/server.js

const
 
devtoAxios
 
=
 
axios
.
create
({

 
baseURL
:
 
API_BASE
,

 
timeout
:
 
parseInt
(
process
.
env
.
DEVTO_TIMEOUT
 
||
 
'
10000
'
,
 
10
),

 
headers
:
 
{
 
'
Content-Type
'
:
 
'
application/json
'
,
 
...
API_HEADERS
 
},

});

// Per-request api-key injection without polluting the instance defaults

devtoAxios
.
interceptors
.
request
.
use
(
cfg
 
=>
 
{

 
if 
(
cfg
.
_apiKey
)
 
{
 
cfg
.
headers
[
'
api-key
'
]
 
=
 
cfg
.
_apiKey
;
 
delete
 
cfg
.
_apiKey
;
 
}

 
return
 
cfg
;

});

async
 
function
 
withRetry
(
fn
,
 
retries
 
=
 
RETRY_COUNT
,
 
delay
 
=
 
RETRY_DELAY
)
 
{

 
let
 
last
;

 
for 
(
let
 
i
 
=
 
0
;
 
i
 
<=
 
retries
;
 
i
++
)
 
{

 
try
 
{
 
return
 
await
 
fn
();
 
}

 
catch 
(
e
)
 
{

 
last
 
=
 
e
;

 
// never retry client errors — they won't succeed on retry

 
if 
(
e
.
status
 
&&
 
e
.
status
 
>=
 
400
 
&&
 
e
.
status
 
<
 
500
)
 
throw
 
e
;

 
if 
(
i
 
<
 
retries
)
 
await
 
sleep
(
delay
 
*
 
Math
.
pow
(
2
,
 
i
));
 
// 500ms, 1s, 2s

 
}

 
}

 
throw
 
last
;

}

async
 
function
 
devtoGet
(
url
,
 
params
 
=
 
{},
 
apiKey
 
=
 
null
)
 
{

 
return
 
withRetry
(()
 
=>

 
devtoAxios
.
get
(
url
,
 
{

 
params
,

 
...(
apiKey
 
?
 
{
 
_apiKey
:
 
apiKey
 
}
 
:
 
{}),

 
}).
then
(
r
 
=>
 
r
.
data
)

 
);

}

Enter fullscreen mode

Exit fullscreen mode

The_apiKeytrick lets each request carry its own Dev.to API key (from the logged-in user's header) without overwriting the shared Axios instance's default headers.

JWT authentication with Supabase as user store

The challenge: the app needs user accounts (to save API keys, bookmarks, etc.) but can't bundle a database. Supabase provides a hosted Postgres. The client must initialise lazily — if env vars are missing, the app should still run for unauthenticated browsing.

// backend/server.js

let
 
_supabase
 
=
 
null
;

function
 
getSupabase
()
 
{

 
if 
(
_supabase
)
 
return
 
_supabase
;

 
if 
(
!
SUPABASE_URL
 
||
 
!
SUPABASE_KEY
)
 
return
 
null
;
 
// graceful degradation

 
_supabase
 
=
 
createClient
(
SUPABASE_URL
,
 
SUPABASE_KEY
,
 
{

 
auth
:
 
{
 
autoRefreshToken
:
 
false
,
 
persistSession
:
 
false
 
},

 
});

 
return
 
_supabase
;

}

async
 
function
 
authLogin
(
req
,
 
res
)
 
{

 
const
 
{
 
email
,
 
password
 
}
 
=
 
req
.
body
;

 
const
 
sb
 
=
 
getSupabase
();

 
if 
(
!
sb
)
 
return
 
sendUnavail
(
res
,
 
'
Database not configured
'
);

 
const
 
{
 
data
:
 
user
 
}
 
=
 
await
 
sb

 
.
from
(
'
users
'
)

 
.
select
(
'
id, username, email, password_hash, devto_api_key
'
)

 
.
eq
(
'
email
'
,
 
email
.
toLowerCase
().
trim
())

 
.
single
();

 
if 
(
!
user
)
 
return
 
sendError
(
res
,
 
HTTP_UNAUTH
,
 
'
Invalid email or password
'
);

 
const
 
valid
 
=
 
await
 
bcrypt
.
compare
(
password
,
 
user
.
password_hash
);

 
if 
(
!
valid
)
 
return
 
sendError
(
res
,
 
HTTP_UNAUTH
,
 
'
Invalid email or password
'
);

 
// fire-and-forget — don't block the login response

 
sb
.
from
(
'
users
'
)

 
.
update
({
 
last_login
:
 
new
 
Date
().
toISOString
()
 
})

 
.
eq
(
'
id
'
,
 
user
.
id
)

 
.
then
(()
 
=>
 
{}).
catch
(()
 
=>
 
{});

 
return
 
sendOk
(
res
,
 
{
 
token
:
 
buildUserToken
(
user
),
 
user
 
});

}

Enter fullscreen mode

Exit fullscreen mode

bcrypt.compareis timing-safe — it takes the same time whether the user exists or not, preventing timing-based user enumeration attacks.

Response envelope compatibility

The challenge: refactoring introduced a{ success, data }wrapper around all responses. The frontend'sapi.jsdoesconst data = await res.json()and immediately usesdataas an array —data.filter(...),data.map(...). The wrapper broke every single page with "Unexpected response".

// BROKEN — frontend does data.filter(...) which fails on { success, data }

function
 
ok
(
res
,
 
data
)
 
{

 
return
 
res
.
status
(
200
).
json
({
 
success
:
 
true
,
 
data
 
});

}

// FIXED — return raw data, frontend gets the array directly

function
 
ok
(
res
,
 
data
)
 
{

 
return
 
res
.
status
(
200
).
json
(
data
);

}

// Error shape stays as { error: '...' } — frontend checks data.error

function
 
sendError
(
res
,
 
status
,
 
msg
)
 
{

 
return
 
res
.
status
(
status
).
json
({
 
error
:
 
msg
 
});

}

// frontend/js/api.js (unchanged — this is what it expects)

async
 
function
 
cachedFetch
(
url
,
 
ttl
 
=
 
60000
)
 
{

 
const
 
res
 
=
 
await
 
fetch
(
url
);

 
if 
(
!
res
.
ok
)
 
throw
 
new
 
Error
(
`
${
res
.
status
}
`
);

 
const
 
data
 
=
 
await
 
res
.
json
();

 
// data is used directly as array — no .data unwrapping

 
fetchCache
.
set
(
url
,
 
{
 
data
,
 
exp
:
 
Date
.
now
()
 
+
 
ttl
 
});

 
return
 
data
;

}

Enter fullscreen mode

Exit fullscreen mode

The lesson: when adding a backend in front of an existing frontend, match the existing API contract exactly. Changing the response shape is a breaking change even if the status code is still 200.

ReferenceError from temporal dead zone

The
 
challenge
:
 
`server.js`
 
grew
 
to
 
1200
+
 
lines
 
with
 
code
 
added
 
in
 
different
 
sections
.
 
`app.use(loggerHelper.logRequest)`
 
was
 
placed
 
at
 
line
 
284
 
during
 
an
 
edit
,
 
but
 
`const app = express()`
 
was
 
at
 
line
 
991
.

// line 284 — CRASHES: const is not hoisted, TDZ throws ReferenceError

app
.
use
(
loggerHelper
.
logRequest
);

// ReferenceError: Cannot access 'app' before initialization

// ... 700 lines later ...

// line 991 — app is declared here

const
 
app
 
=
 
express
();

app
.
use
(
cors
({
 
...
 
}));

app
.
use
(
express
.
json
({
 
limit
:
 
'
1mb
'
 
}));

app
.
use
(
express
.
urlencoded
({
 
extended
:
 
false
 
}));

app
.
use
(
requestLogger
);

app
.
use
(
loggerHelper
.
logRequest
);
 
// FIXED: moved here, after app exists

Enter fullscreen mode

Exit fullscreen mode

varwould have hoisted and silently beenundefinedat line 284, causing a different error (TypeError: Cannot read properties of undefined).constthrows immediately and clearly. The fix is always to keep allapp.use()calls in one place, afterconst app = express().

Layered architecture refactor

The challenge: a single 200-lineserver.jswith routes, auth logic, caching, and HTTP client all mixed together. Adding features meant scrolling through everything. Testing any piece required the whole file.

Before: After:
backend/ backend/
 server.js (200 lines, config/
 everything mixed) app.config.js (env vars)
 constants.js (HTTP codes, keys)
 database.config.js (Supabase client)
 controllers/
 article.controller.js
 auth.controller.js
 services/
 devto-api.service.js (all API calls)
 auth.service.js (register/login)
 cache.service.js (TTL wrappers)
 middleware/
 auth.middleware.js
 error.middleware.js
 routes/
 article.routes.js
 auth.routes.js
 utils/
 cache.util.js
 http-client.util.js
 token.util.js
 server.js (slim entry, ~40 lines)

Enter fullscreen mode

Exit fullscreen mode

Each layer has one job. Controllers handle HTTP in/out. Services contain business logic with noreq/resknowledge. Utils are pure functions. This meansdevto-api.service.jscan be tested without Express, andauth.middleware.jscan be swapped without touching routes.

Tech Stack & Skills

Category

Technology

Usage in This Project

Runtime

Node.js v18+

Server runtime embedded inside Electron main process

Desktop

Electron 28

Cross-platform desktop shell, window management, IPC

Backend Framework

Express 4

REST API server, middleware pipeline, route handling

HTTP Client

Axios

Dev.to API proxy with interceptors and retry logic

Authentication

JWT (jsonwebtoken)

Stateless session tokens, Bearer auth middleware

Password Security

bcryptjs

Salted password hashing, timing-safe comparison

Database

Supabase (Postgres)

Hosted user store, lazy client initialization

Caching

Custom LRU + TTL

In-memory cache with pattern invalidation, O(1) eviction

Build Tool

electron-builder

Portable single 
.exe
 packaging, extraResources bundling

Frontend

Vanilla JS / HTML / CSS

No framework, direct DOM manipulation

Environment

dotenv

Runtime env switching between dev and packaged paths

Architecture Skills

Skill

Detail

Layered architecture

config / controllers / services / middleware / routes / utils separation

Embedded server pattern

Express running inside Electron main process — no child process or IPC

Cache-aside pattern

Check cache → miss → fetch API → populate cache → return

Exponential back-off retry

Transient failures retried with 
delay * 2^attempt
, 4xx never retried

Graceful degradation

App runs without Supabase configured — auth disabled, browsing works

API contract preservation

Backend response shape matched existing frontend without changes

Middleware composition

Auth, logging, validation, error handling as independent Express middleware

Build pipeline patching

Patched 
binDownload.js
 in 3 locations to bypass Windows symlink restriction

Problems Solved

Problem

Root Cause

Solution

Single 
.exe
 with embedded backend

node_modules
 excluded from 
extraResources

Removed 
!node_modules/**
 filter in build config

Build fails on Windows

winCodeSign
 archive contains macOS symlinks

Patched 
doGetBin()
 + 
signAndEditExecutable: false

"Unexpected response" on all pages

Response wrapped in 
{ success, data }
 envelope

Returned raw data — matched existing frontend contract

ReferenceError: Cannot access 'app'

app.use()
 called before 
const app = express()

Moved all 
app.use()
 calls after app initialization

Dev.to API rate limiting

Every render hitting the API directly

LRU cache with per-resource TTLs (1–10 min)

Stale reaction counts after like

Cache not invalidated on mutation

cache.invalidatePattern('articles:*')
 on POST/DELETE

User enumeration via timing

Login returning early on unknown email

bcrypt.compare
 always runs regardless of user existence

Monolithic server hard to maintain

All logic in one 200-line file

Refactored into 6 layers, 20+ files

Backend path wrong in packaged app

Dev path 
../backend
 invalid after packaging

process.resourcesPath
 used in production, 
__dirname
 in dev

That project is technical, yes. But to me it is also personal.

Because underneath all the implementation details is a very human belief: developers deserve tools that meet them with less friction, not more. We spend enough time wrestling complexity. Good software should not add ego to the burden.

That is also what I think gender equity in tech should look like in practice. Not just opening the door and walking away, but designing better rooms once people get inside. Rooms where curiosity is not punished. Rooms where beginners are not treated like inconveniences. Rooms where expertise is shared in a way that multiplies confidence instead of hoarding status.

I did not stay in tech because every experience was welcoming. I stayed because enough people, at crucial moments, chose to be generous.

A patient senior engineer.A stranger answering a question online.A community that reminds you that even experienced developers still get stuck, still learn, still rewrite the same thing three times before pretending it was intentional.

So when I think about the “echoes of experience,” I do not think only about the painful moments. I think about what answered them.

Patience.Humor.Persistence.Community.

And yes, sometimes coffee.

I still have hard days. I still meet code that looks like it was written during a minor electrical storm. I still occasionally open a file and feel my soul leave my body for a second. But I no longer confuse that feeling with failure.

Now I recognize it for what it usually is:

the start of learning,the invitation to ask,and another chance to make this industry more human than I found it.

Try the project yourself

If you want to experience Always with Dev.to — Desktop Client directly, you can check the project here:

https://github.com/wvalencs/devTo-electron

Run locally

1.Clone the repository

git clone https://github.com/wvalencs/devTo-electron.git

cd 
devTo-electron

Enter fullscreen mode

Exit fullscreen mode

2.Install dependencies

Install dependencies for both the frontend and backend parts of the project.

cd 
backend
npm 
install
cd
 ../frontend
npm 
install

Enter fullscreen mode

Exit fullscreen mode

3.Start the application in development mode

Run the Electron frontend, which will start the embedded backend automatically.

cd 
backend
npm start

cd 
frontend
npm start

Enter fullscreen mode

Exit fullscreen mode

4.Build portable executable

To generate the portable desktop app:

cd 
frontend
npm run build

Enter fullscreen mode

Exit fullscreen mode

After the build is complete, the packaged app will be available in the dist folder.

If you want, next I can turn this into a true Dev.to-ready version with a stronger hook, cleaner section headers, and final tags.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (97 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse