---
title: Stop Ignoring RFC 2324. It's the Most Important Protocol You've Never Implemented. - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/stop-ignoring-rfc-2324-its-the-most-important-protocol-youve-never-implemented-53pe
site_name: devto
content_file: devto-stop-ignoring-rfc-2324-its-the-most-important-prot
fetched_at: '2026-02-25T19:26:46.420689'
original_url: https://dev.to/pascal_cescato_692b7a8a20/stop-ignoring-rfc-2324-its-the-most-important-protocol-youve-never-implemented-53pe
author: Pascal CESCATO
date: '2026-02-24'
description: HTCPCP/1.0, the 418 teapot, a full interactive dashboard, and why a 1998 April Fools RFC teaches better software design than most tech books. Tagged with fun, http, python, webdev.
tags: '#fun, #http, #python, #webdev'
---

Some RFCs change the world — TCP/IP, HTTP/2, TLS 1.3.

And then there'sRFC 2324, published April 1st, 1998, defining theHyper Text Coffee Pot Control Protocol(HTCPCP/1.0). Its purpose: control, monitor, and diagnose coffee pots over a network.

No, it's not a joke. Well, it is. But it'swritten seriously enough to actually implement. Emacs did it. We will too.

## A Brief History of the Web's Most Honorable RFC

RFC 2324 is an IETF April Fools' joke authored by Larry Masinter. It extends HTTP with:

* NewHTTP methods:BREW,WHEN,PROPFIND
* A newheader:Accept-Additions(for milk, sugar, whisky — yes, whisky)
* A newURI scheme:coffee://(andkoffie://,café://, and 26 other translations)
* Two newerror codesthat changed internet history

### The error codes

406 Not Acceptable — The server cannot brew this coffee
418 I'm a teapot — The server is a teapot, not a coffee pot

Enter fullscreen mode

Exit fullscreen mode

418became iconic. In 2017, a proposal to remove it from the IANA registry triggered an actual revolt across the dev community. Node.js, Go, Python — everyone kept it. The teapot won.

In 2014,RFC 7168extended the protocol to tea (HTCPCP-TEA), adding themessage/teapotMIME type and the requirement to distinguish an Earl Grey from a Darjeeling. Rigor in absurdity.

## What the RFC Actually Defines

Before writing a single line, read the spec. That's the exercise.

### The new methods

MethodRoleBREW(orPOST)Trigger an infusionGETGet the coffee pot's current statePROPFINDList available additionsWHENStop pouring the milk— the client says "when!"

TheWHENmethod is the most beautiful. It models a human exchange ("tell me when") as an HTTP request. A masterpiece of protocol anthropomorphism.

### The Accept-Additions header

BREW /coffee-pot-1 HTCPCP/1.0
Accept-Additions: milk-type=Whole-milk; syrup-type=Vanilla; alcohol-type=Whisky

Enter fullscreen mode

Exit fullscreen mode

Legal values includeCream,Half-and-half,Whole-milk,Non-Dairy, syrups (Vanilla,Chocolate,Raspberry,Almond), and spirits (Whisky,Rum,Kahlua,Aquavit).

Intentionally absent: any decaffeinated option. The RFC's comment on this is terse:"What's the point?"

## Step 1 — Play First: The Standalone Simulator

Before writing a single line of server code, I built afully self-contained HTML/JS simulatorthat runs entirely in the browser. No backend, no dependencies, no install.

Interactive HTCPCP Dashboard

htcpcp.benchwiseunderflow.in

The simulator is not a mock of the server — itisa complete HTCPCP implementation, just in a different runtime. All the state lives in JavaScript: pot registry, brew history, status transitions, 418/406 logic. It's the fastest way to feel the protocol before committing to a stack.

Try to BREW on a teapot. Watch the 418 fire. Select decaf and get a 406. Click WHEN mid-brew to stop the milk. Then come back here and build the production version.

## Step 2 — Ship It: The Production Server

### A word on uvicorn

The natural instinct isuvicorn main:app --reload. Don't. uvicorn validates HTTP method names at thesocket level, before any request parsing happens.BREW,WHEN, andPROPFINDare not registered IANA methods, so uvicorn rejects them immediately withInvalid HTTP request received— regardless of any FastAPI config.

The fix: a raw asyncio TCP server (server.py) with a minimal HTTP/1.1 parser that accepts any valid RFC 7230 token as a method name. WhichBREW,WHEN, andPROPFINDare. This is actually the more correct approach — HTCPCP defines its own protocol, and rolling your own transport layer is the honest implementation.

python server.py
# ☕ HTCPCP/1.0 — RFC 2324 (127.0.0.1:2324)

curl -X BREW http://localhost:2324/coffee/pot-1 \
 -H "Accept-Additions: milk-type=Whole-milk; alcohol-type=Whisky"

Enter fullscreen mode

Exit fullscreen mode

FastAPI +main.pyis still useful for one thing: the test suite. FastAPI'sTestClientbypasses the HTTP transport layer entirely, so custom methods work fine in tests — and you get all the validation and schema benefits of FastAPI.

pytest test_htcpcp.py -v # uses main.py + TestClient, no server.py needed

Enter fullscreen mode

Exit fullscreen mode

### Architecture: a pot registry

First architectural decision: model the entities properly.

from

enum

import

Enum

from

dataclasses

import

dataclass
,

field

class

PotType
(
str
,

Enum
):


COFFEE

=

"
coffee
"


TEAPOT

=

"
teapot
"

class

PotStatus
(
str
,

Enum
):


IDLE

=

"
idle
"


BREWING

=

"
brewing
"


POURING_MILK

=

"
pouring-milk
"


READY

=

"
ready
"

@dataclass

class

CoffeePot
:


id
:

str


pot_type
:

PotType


capacity
:

int


level
:

int


status
:

PotStatus

=

PotStatus
.
IDLE


varieties
:

list
[
str
]

=

field
(
default_factory
=
list
)


brew_history
:

list
[
dict
]

=

field
(
default_factory
=
list
)

# The registry — the core of the architecture

POT_REGISTRY
:

dict
[
str
,

CoffeePot
]

=

{


"
coffee://pot-1
"
:

CoffeePot
(
"
pot-1
"
,

PotType
.
COFFEE
,

12
,

8
,


varieties
=
[
"
Espresso
"
,

"
Lungo
"
,

"
Americano
"
]),


"
coffee://pot-2
"
:

CoffeePot
(
"
pot-2
"
,

PotType
.
COFFEE
,

6
,

2
,


varieties
=
[
"
Espresso
"
]),


"
tea://kettle-1
"
:

CoffeePot
(
"
kettle-1
"
,

PotType
.
TEAPOT
,

8
,

6
,


varieties
=
[
"
Earl Grey
"
,

"
Chamomile
"
,

"
Darjeeling
"
]),

}

Enter fullscreen mode

Exit fullscreen mode

### Parsing the Accept-Additions header

from

fastapi

import

Request
,

HTTPException

SUPPORTED_ADDITIONS

=

{


"
milk-type
"
:

[
"
Cream
"
,

"
Half-and-half
"
,

"
Whole-milk
"
,

"
Part-Skim
"
,

"
Skim
"
,

"
Non-Dairy
"
],


"
syrup-type
"
:

[
"
Vanilla
"
,

"
Almond
"
,

"
Raspberry
"
,

"
Chocolate
"
],


"
sweetener-type
"
:

[
"
Sugar
"
,

"
Honey
"
],


"
spice-type
"
:

[
"
Cinnamon
"
,

"
Cardamom
"
],


"
alcohol-type
"
:

[
"
Whisky
"
,

"
Rum
"
,

"
Kahlua
"
,

"
Aquavit
"
],

}

def

parse_accept_additions
(
header
:

str

|

None
)

->

dict
[
str
,

str
]:


if

not

header
:


return

{}


additions

=

{}


for

part

in

header
.
split
(
"
;
"
):


part

=

part
.
strip
()


if

"
=
"

in

part
:


key
,

value

=

part
.
split
(
"
=
"
,

1
)


additions
[
key
.
strip
()]

=

value
.
strip
()


return

additions

def

validate_additions
(
additions
:

dict
)

->

None
:


# RFC 2324 §2.1.1: no decaf option — intentionally


if

"
decaf
"

in

additions
:


raise

HTTPException
(


status_code
=
406
,


detail
=
{


"
error
"
:

"
Not Acceptable
"
,


"
message
"
:

"
Decaffeinated coffee? What
'
s the point?
"
,


"
rfc
"
:

"
RFC 2324 §2.1.1
"


}


)


unsupported

=

[


f
"
{
k
}
=
{
v
}
"

for

k
,

v

in

additions
.
items
()


if

k

in

SUPPORTED_ADDITIONS

and

v

not

in

SUPPORTED_ADDITIONS
[
k
]


]


if

unsupported
:


raise

HTTPException
(


status_code
=
406
,


detail
=
{
"
error
"
:

"
Not Acceptable
"
,

"
unsupported_additions
"
:

unsupported
}


)

Enter fullscreen mode

Exit fullscreen mode

### The HTCPCP endpoints

from

fastapi

import

FastAPI

from

fastapi.responses

import

JSONResponse

app

=

FastAPI
(
title
=
"
HTCPCP/1.0
"
,

version
=
"
1.0
"
)

def

get_pot
(
pot_id
:

str
)

->

CoffeePot
:


uri

=

f
"
coffee://
{
pot_id
}
"


pot

=

POT_REGISTRY
.
get
(
uri
)

or

POT_REGISTRY
.
get
(
f
"
tea://
{
pot_id
}
"
)


if

not

pot
:


raise

HTTPException
(
status_code
=
404
,

detail
=
"
Pot not found in registry
"
)


return

pot

# ── BREW ────────────────────────────────────────────────────────────────────

@app.api_route
(
"
/coffee/{pot_id}
"
,

methods
=
[
"
BREW
"
,

"
POST
"
])

async

def

brew
(
pot_id
:

str
,

request
:

Request
):


pot

=

get_pot
(
pot_id
)


# RFC 2324 §2.3.2: teapot → 418, mandatory


if

pot
.
pot_type

==

PotType
.
TEAPOT
:


return

JSONResponse
(
status_code
=
418
,

content
=
{


"
status
"
:

418
,


"
error
"
:

"
I
'
m a teapot
"
,


"
body
"
:

"
The requested entity body is short and stout.
"
,


"
hint
"
:

"
Tip me over and pour me out.
"
,


"
pot_id
"
:

pot_id
,


"
rfc
"
:

"
RFC 2324 §2.3.2
"
,


"
suggestion
"
:

"
Use coffee://pot-1/brew instead
"


})


if

pot
.
level

==

0
:


raise

HTTPException
(
status_code
=
503
,

detail
=
"
Pot is empty. Refill required.
"
)


additions_header

=

request
.
headers
.
get
(
"
accept-additions
"
)


additions

=

parse_accept_additions
(
additions_header
)


validate_additions
(
additions
)

# 406 if decaf or invalid additions


brew_id

=

len
(
pot
.
brew_history
)

+

1


pot
.
brew_history
.
append
({
"
id
"
:

brew_id
,

"
additions
"
:

additions
})


pot
.
status

=

PotStatus
.
BREWING


pot
.
level

-=

1


# Milk requested → enter pouring-milk state


has_milk

=

"
milk-type
"

in

additions


if

has_milk
:


pot
.
status

=

PotStatus
.
POURING_MILK


return

JSONResponse
(
status_code
=
200
,

content
=
{


"
brew_id
"
:

brew_id
,


"
message
"
:

"
Coffee is brewing.
"
,


"
pot
"
:

pot_id
,


"
accept-additions
"
:

additions
,


"
milk_pouring
"
:

has_milk
,


"
protocol
"
:

"
HTCPCP/1.0
"


})

# ── GET ──────────────────────────────────────────────────────────────────────

@app.get
(
"
/coffee/{pot_id}/status
"
)

def

get_status
(
pot_id
:

str
):


pot

=

get_pot
(
pot_id
)


return

{


"
pot_id
"
:

pot_id
,


"
type
"
:

pot
.
pot_type
,


"
status
"
:

pot
.
status
,


"
level
"
:

f
"
{
pot
.
level
}
/
{
pot
.
capacity
}
 cups
"
,


"
brew_count
"
:

len
(
pot
.
brew_history
),


"
varieties
"
:

pot
.
varieties
,


"
protocol
"
:

"
HTCPCP/1.0
"


}

# ── PROPFIND ─────────────────────────────────────────────────────────────────

@app.api_route
(
"
/coffee/{pot_id}/additions
"
,

methods
=
[
"
PROPFIND
"
])

def

propfind
(
pot_id
:

str
):


get_pot
(
pot_id
)


return

{


**
SUPPORTED_ADDITIONS
,


"
decaf
"
:

"
NOT_ACCEPTABLE — What
'
s the point? (RFC 2324 §2.1.1)
"


}

# ── WHEN ─────────────────────────────────────────────────────────────────────

@app.api_route
(
"
/coffee/{pot_id}/stop-milk
"
,

methods
=
[
"
WHEN
"
])

def

when
(
pot_id
:

str
):


"""

 RFC 2324 §2.1.3 — WHEN
 Sent when the client determines that enough milk has been poured.
 The server must stop immediately.

"""


pot

=

get_pot
(
pot_id
)


if

pot
.
status

!=

PotStatus
.
POURING_MILK
:


return

JSONResponse
(
status_code
=
200
,

content
=
{


"
message
"
:

"
WHEN acknowledged.
"
,


"
note
"
:

"
No milk was being poured, but your enthusiasm is appreciated.
"
,


"
rfc
"
:

"
RFC 2324 §2.1.3
"


})


pot
.
status

=

PotStatus
.
BREWING


return

JSONResponse
(
status_code
=
200
,

content
=
{


"
message
"
:

"
Milk pouring stopped.
"
,


"
detail
"
:

"
The server has acknowledged WHEN and stopped the milk stream.
"
,


"
protocol
"
:

"
HTCPCP/1.0
"
,


"
rfc
"
:

"
RFC 2324 §2.1.3
"


})

Enter fullscreen mode

Exit fullscreen mode

### Middleware: enforce HTCPCP headers

from

starlette.middleware.base

import

BaseHTTPMiddleware

class

HTCPCPMiddleware
(
BaseHTTPMiddleware
):


async

def

dispatch
(
self
,

request
,

call_next
):


response

=

await

call_next
(
request
)


response
.
headers
[
"
X-Protocol
"
]

=

"
HTCPCP/1.0
"


response
.
headers
[
"
X-RFC
"
]

=

"
RFC-2324
"


# Detect a BREW on a non-coffee route and punish accordingly


if

request
.
method

==

"
BREW
"

and

not

request
.
url
.
path
.
startswith
(
"
/coffee
"
):


return

JSONResponse
(
status_code
=
418
,

content
=
{


"
error
"
:

"
Wrong universe
"
,


"
hint
"
:

"
BREW is only valid on coffee:// URIs
"


})


return

response

app
.
add_middleware
(
HTCPCPMiddleware
)

Enter fullscreen mode

Exit fullscreen mode

### Structured logs — because we're professionals

import

structlog

log

=

structlog
.
get_logger
()

# After a successful BREW:

log
.
info
(
"
htcpcp.brew
"
,


pot_id
=
pot_id
,


brew_id
=
brew_id
,


additions
=
additions
,


status_code
=
200
,


protocol
=
"
HTCPCP/1.0
"

)

# On 418:

log
.
warning
(
"
htcpcp.teapot_detected
"
,


pot_id
=
pot_id
,


pot_type
=
"
teapot
"
,


status_code
=
418
,


message
=
"
Teapot attempted to brew coffee
"

)

Enter fullscreen mode

Exit fullscreen mode

Which produces in your JSON logs:

{"event": "htcpcp.brew", "pot_id": "pot-1", "brew_id": 3,
 "additions": {"milk-type": "Whole-milk", "alcohol-type": "Whisky"},
 "status_code": 200, "protocol": "HTCPCP/1.0", "level": "info"}

{"event": "htcpcp.teapot_detected", "pot_id": "kettle-1",
 "status_code": 418, "level": "warning"}

Enter fullscreen mode

Exit fullscreen mode

## What This Actually Teaches You

Implementing an April Fools' RFC is a serious exercise in disguise. You end up learning:

How to read an RFC properly— distinguishing MUST, SHOULD, MAY. RFC 2324 uses all three with care. The 418 is a MUST if the server is a teapot. A broken coffee machine should return 503 — not 418. That's a common mistake, and it matters.

How the HTTP stack actually works— trying to use uvicorn withBREWreveals that method validation happens at the socket level, before h11, before FastAPI, before your code. You end up writing a raw asyncio TCP server to get HTCPCP working for real. That's not a detour — that's the point. You now understand the HTTP request pipeline better than most devs who've shipped production APIs for years.

How to think in entities— the pot registry, theCoffeePotvsTeapotdistinction, routing bycoffee://URI: this is real domain modeling. The joke forces you to take it seriously.

How to model state machines—idle → brewing → pouring-milk → readyis a textbook workflow. WHEN is a client-driven transition. You'll see this pattern everywhere in production systems.

How to write integration tests for absurd-but-useful edge cases:

def

test_teapot_cannot_brew
():


response

=

client
.
request
(
"
BREW
"
,

"
/coffee/kettle-1
"
)


assert

response
.
status_code

==

418


assert

response
.
json
()[
"
error
"
]

==

"
I
'
m a teapot
"

def

test_decaf_is_not_acceptable
():


response

=

client
.
request
(
"
BREW
"
,

"
/coffee/pot-1
"
,


headers
=
{
"
Accept-Additions
"
:

"
decaf=true
"
})


assert

response
.
status_code

==

406

def

test_when_stops_milk
():


client
.
request
(
"
BREW
"
,

"
/coffee/pot-1
"
,


headers
=
{
"
Accept-Additions
"
:

"
milk-type=Whole-milk
"
})


response

=

client
.
request
(
"
WHEN
"
,

"
/coffee/pot-1/stop-milk
"
)


assert

response
.
status_code

==

200


assert

"
stopped
"

in

response
.
json
()[
"
message
"
]

Enter fullscreen mode

Exit fullscreen mode

## Conclusion

418 survived every attempt to kill it because it represents something real:developers are allowed to be playful. An April Fools' RFC published today would probably get killed in committee within a week. The one from 1998 has lasted 26 years.

What makes RFC 2324 remarkable is that it takes absurdity seriously — it has a real state machine, real error codes with precise semantics, a real extension (RFC 7168 for tea). It mocks formalism by respecting it perfectly.

That's exactly how we should build our own systems.

Simulator (HTML/JS standalone),server.py(raw TCP),main.py+ full test suite — on Github:https://github.com/pcescato/htcpcp/.

RFC 2324:https://tools.ietf.org/html/rfc2324RFC 7168:https://tools.ietf.org/html/rfc7168

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (19 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
