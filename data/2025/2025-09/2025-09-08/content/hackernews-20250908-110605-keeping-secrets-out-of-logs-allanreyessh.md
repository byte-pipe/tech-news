---
title: Keeping Secrets Out of Logs - allan.reyes.sh
url: https://allan.reyes.sh/posts/keeping-secrets-out-of-logs/
site_name: hackernews
fetched_at: '2025-09-08T11:06:05.818258'
original_url: https://allan.reyes.sh/posts/keeping-secrets-out-of-logs/
author: xk3
date: '2025-09-08'
published_date: '2024-08-02T00:00:00+00:00'
description: There's no silver bullet, but if we put some "lead" bullets in the right places, we have a good shot at keeping sensitive data out of logs.
---

# Keeping Secrets Out of Logs

Posted on Aug 2, 2024
tl;dr:

There's no silver bullet, but if we put some "lead" bullets in the right
places, we have a good shot at keeping sensitive data out of logs.
"This is the blog version of a talk I gave at LocoMocoSec 2024. It’s
mostly a lightly edited transcript with some screenshots, so if you’d prefer,
you can watch the

video
 or just
flip through the
slides
."

This post is about how to keep secrets out of logs, and my claim is that(like
many things in security)there isn’t a singular action or silver bullet that
lets you do this. I would go so far as to say that there’s not even an 80/20
rule, where one action fixes 80% of the problem. It’s not like preventing SQL
injection with prepared statements or preventing buffer overflows by using
memory-safe languages.

What I will offer instead, are lead bullets, of which there are many. I’m going
to talk about 10 of them. They are imperfect and sometimes unreliable things
that, if put in the right places and with defense-in-depth, can still give us a
real good chance at succeeding. My hope is that by the end, you’ll
have a slightly better framework for how to reason about this problem and some
new ideas to add to your kit.

Table of contents:

* The Problem
* Causes🤦 Direct logging🚰 Kitchen sinks🔧 Configuration changes🥧 Embedded secrets📡 Telemetry🕺🏻 User input
* 🤦 Direct logging
* 🚰 Kitchen sinks
* 🔧 Configuration changes
* 🥧 Embedded secrets
* 📡 Telemetry
* 🕺🏻 User input
* Fixes (lead bullets)📐 Data architecture🍞 Data transformations🪨 Domain primitivesCompile-timeRun-timeRun-time: part deux🎁 Read-once objects🔎 Taint checkingAwesomeNot awesome🗃️ Log formatters🧪 Unit tests🕵️ Sensitive data scannersSampling🤖 Log pre-processors🦸 PeopleRecap
* 📐 Data architecture
* 🍞 Data transformations
* 🪨 Domain primitivesCompile-timeRun-timeRun-time: part deux
* Compile-time
* Run-time
* Run-time: part deux
* 🎁 Read-once objects
* 🔎 Taint checkingAwesomeNot awesome
* Awesome
* Not awesome
* 🗃️ Log formatters
* 🧪 Unit tests
* 🕵️ Sensitive data scannersSampling
* Sampling
* 🤖 Log pre-processors
* 🦸 People
* Recap
* Strategy0. Lay the foundation1. Understand the data flow2. Protect at chokepoints3. Apply defense-in-depth4. Plan for response and recovery
* 0. Lay the foundation
* 1. Understand the data flow
* 2. Protect at chokepoints
* 3. Apply defense-in-depth
* 4. Plan for response and recovery
* Conclusion

## The Problem

With that, let’s dive in and set the table by talking about the problem with
secrets in logs.

So, there are some problems that are annoying. And there are some problems that
are difficult.

This is both. I’m gonna level with you: I absolutely hate this problem. But I’m
not going to gaslight you and tell you that this is the most important thing to
work on worry about, because it probably isn’t!

You have somewhere between 5 and 50 other problems in your backlog that seem
more important, 1 of which you found out about this morning. But I think it’s
likely that none of those problems are nearly as annoying. While researching
this topic, I interviewed about a dozen other engineers and, on this point, they
unanimously agreed! Nobody likes dealing with secrets in logs because it is
extraordinarilyannoying.

This is a problem that’s also difficult, but not even in the fun sense, like
being technically complex or interesting. Once you catch sensitive data in logs,
it’s usually pretty straightforward(at least in retrospect)to determine how
they got there. But, it’s also surprisingly elusive to prevent, and it crops up
in incredibly unexpected places and ways.

Secrets could mean lots of different things to lots of different teams, but I’ll
use it interchangeably with “sensitive data”: stuff that you want to keep
confidential. What’ssofrustrating when breaching confidentiality in logs is
the full spectrum of potential impact.

In the best case(left), you might log an isolated, internal credential, like
an API key, which(kudos!)you rotate right after fixing the source of leak.
The impact is minimal, and you just move on. Of course, all the way on the other
end of the spectrum(right), you might log something that an attacker or
inside threat could use to do somereal harm.

And then somewhere in-between, where I suspect most of the incidents lie. You
might log secrets that you unfortunately, can’t rotate yourself. Things like PII
or your customer’s passwords, which are reused on other sites, because of course
they are. And, depending on your policies, threat model, or regulations, you
might choose to issue a disclosure or notification.

And it is painful.

You could be doing so many good data security practices, like
secure-by-design frameworks, database and field-level encryption, zero-touch
production, access control… but logging bypasses all of that… and ultimately
degrades trust, in your systems and in your company. It feels unfair because
it’s only a fraction of your security story.

And this is a problem that happens to companies of all sizes:

Something about “plaintext” just kinda stings, especially as a security
practitioner. It’s like… the most profane insult you can hurl at a security
engineer. Imagine retorting with,“Oh yea? Well, you store your passwords in
plaintext!”

But logging passwords and storing them in plaintext are… kinda the same thing.

Because while logs are rarely or purposefully public, they’re typically afforded
broader access than direct access to your databases.

Everyone knows by now that storing plaintext secrets in your database is a
terrible idea. Logs, however, are still data-at-rest, and we should treat them
with the same level of scrutiny.

I cherry picked those examples because they are established companies with very
mature security programs. I’m not trying to throw shade; in fact, I deeply
respect them for being public and transparent about this. I think this also
hints that preventing secrets in logs is a deceptively difficult and frustrating
problem.

If we can understand some causes, we might gain a deeper appreciation for these
past occurrences, and stand a better chance at avoiding new incidents in the
future.

## Causes

This is certainly not comprehensive, but from my interviews and personal
experience, here aresixof the most common causes.

1. 🤦Direct logging
2. 🚰Kitchen sinks
3. 🔧Configuration changes
4. 🥧Embedded secrets
5. 📡Telemetry
6. 🕺🏻User input

### 🤦 Direct logging

const

temp

=

res
.
cookie
[
"session"
];

// TODO: remove after testing is done

Logger
.
info
(
"session HERE"
, {
temp
 });

Narrator: it wasnotremoved after testing was done

The first group is perhaps the most obvious and facepalm one: when sensitive
data is directly logged. Sometimes it’s purely accidental, like the example
above: someone wants to debug session cookies in their local environment and
then… accidentally commits the code. Sometimes it comes from an uninformed
position where the developer just doesn’t know any better.

These tend to be fairly easy to trace down the exact line of code or commit that
introduces it. With this example, you can just grep the codebase forsession hereand you’ll find it instantly.

### 🚰 Kitchen sinks

const

client

=

googleSdk
.
admin
(...);

try
 {


const

res

=

client
.
tokens
.
list
(...);

}
catch
 (
e
) {


Logger
.
error
(
"failed fetch"
, {
e
 });

}

I’m sure you’ve seen or written code like this before. Here we have an API
client or SDK that is used to fetch some data. Exceptions are caught, kind of,
and then promptly logged so that on-call engineers can debug the errors.

What happens?

That error is decorated with a config object stuffed with secrets and the full
response object, which is also stuffed with secrets, and now they’re both in
your logs!

{


e
:
 {


status
:
400
,

 ...


config
:
 {
💥☠️🪦
 },


response
:
 {
💣😭😱
 },

 }

}

I call these “kitchen sinks,” objects that contain or hold secrets, often in
opaque or unexpected ways. Think of an actual kitchen sink that’s filled to the
brim with dirty dishes and you can’t easily tell what’s at the bottom without
reaching into it. Maybe it’s a spoon, or maybeit’s knife and now you have to
go to the hospital. What tends to happen is that the whole kitchen sink gets
logged, and the logging library happily serializes it, including parts that were
actually sensitive.

This seems to happen with code that attaches additional data onto errors, or
code that logs full request and response objects. It’s typically a bit hard to
catch in code review unless you know to look for them. If you are blessed with
static types, seeing ananytype flow into logs can be a good hint that you’re
logging too much.

### 🔧 Configuration changes

Narrator: it wasnotokay

Next example: someone needs additional observability and changes a setting like
the global log level. You know exactly what happens, here. This dev is about to
have a bad time and find out that hope, in fact, is not a valid strategy.

We started with an observability problem. Now we also have security problem: brand
new secrets are getting emitted into logs.

In that example(that totally never happened to me ever), developers built
production around log levels set toWARNand above, but once you flip it toDEBUG, all this new stuff comes out of the woodwork.

These type of configuration changes tend to involve a system that was built with
one set of assumptions, but some kind of modification moves that system from a
known state into a unknown state, introducing a new set of problems.

These often involve low-level or global utilities like logging config, HTTP
middleware, or some central piece of infra like a load balancer. They tend to be
singletons that are difficult or costly to test, or they crop up only at
runtime. On the positive side, it’s usually loud and quick to patch, but cleanup
can be kinda painful.

### 🥧 Embedded secrets

app
.
get
(
"/login/:slug"
,
async
 (
req
,
res
)
=>
 {


const

magicLink

=

req
.
params
[
"slug"
];


await

login
({
magicLink
 });

});

I completely made up this phrase, but the idea is that secrets are coupled to,
embedded into, andbaked intomore general formats like URLs or remote
procedure calls. The central idea is that it’s designed into the format and the
system, and can’t easily be separated.

Say you have a magic login link handler (see above) where a user can click a
link and sign into a web app. There’s nothing in that code that logs the link,
but if you look at HTTP logs, it’s right there in plain view:

47.29.201.179 - - [17/Jul/2024:13:17:10 +0000] "GET /login/Uj79z1pe01...

These types of leaks arise from fundamental designs that don’t take logging into
consideration or incorrectly assume some end-to-end flow. The sensitivity gets lost out of context, and ends up getting logged in another layer,
system, or service.

### 📡 Telemetry

try
:

 db_name
=
 os
.
getenv(
"DB_NAME"
)

 db_pass
=
 os
.
getenv(
"DB_PASS"
)
# 🤫 Secret!

 conn
=
 db
.
connect(db_name, db_pass)


...

except
 Error
as
 e:


# Don't log e! Not today!!11

 Logger
.
error(
"failed to connect"
)

finally
:

 conn
.
close()

Next example: we have some Python code that’s connecting to a database, we’re
specifically NOT logging the error object, and we want to ensure we always close
out the connection.

How candb_passpossibly make it into logs? Telemetry!

"Oops, that's a log, too!"

It turns out that things like error monitoring and analytics can totally be
logs, too. I kind of cheated in the code example, because there’s no mention of
telemetry in it at all, but it turns out that if you hook it up to error
monitoring likeSentry(above), run-time errors send the
local variable context right to the dashboard, and you can see the database
password in plaintext.

These causes tend to bypass the central logging pipeline and become Yet Another
Place to have to worry about secrets.

### 🕺🏻 User input

Alright, last example. Say there’s a sign in form and the entire dev team made
super duper sure that the password field is totally locked down from logging,
they read this super awesome post, and took care of all the causes we discussed.

What happens?

Users end up jamming passwords into the username field!

So if you ever looked at login alerts for AWS and saw usernames replaced withHIDDEN_DUE_TO_SECURITY_REASONS, this is precisely why!

Everything that’s within proximity to sensitive user input tends to be
radioactive. It could be a UI issue, but users are surprisingly determined to
volunteer secrets in ways that you haven’t prepared for.

We’ve touched on a half dozen causes, and the list of things goes on. We didn’t
even talk about the wonder that is crashdumps. But, I think it’s important to
zoom out and note that these are proximate causes.

I stand by my claim that there’s no silver bullet to take these all out. If we
want to avoid playing whack-a-mole, we must bring out our lead bullets that
address these issues at a deeper level, and prevent these kinds of things from
happening.

## Fixes (lead bullets)

So let’s dive in! We will survey 10 fixes, and the order we’ll go in is
somewhere between “a dependency graph of things that build on each other” and
“following the lifecycle of a secret.” Some of these are obvious or perhaps
things you’re already doing, so I’ll focus more on fixes that I think might be a
bit newer. That said, it is worth starting with the basics.

1. 📐Data architecture
2. 🍞Data transformations
3. 🪨Domain primitives
4. 🎁Read-once objects
5. 🗃️Log formatters
6. 🧪Unit tests
7. 🕵️Sensitive data scanners
8. 🤖Log pre-processors
9. 🔎Taint checking
10. 🦸People

### 📐 Data architecture

Lead bullet #1 is the most basic and high-level: data architecture and
understanding that this is primarily a data flow problem. And part of the
solution is reducing the number of data flows and shrinking the problem space so
you simply have less things to worry about and protect.

Instead of stray print statements or components that write directly to
filesystem, you instead centralize all your data flows through a single stream.
Make it so that there’s one and only one way to log something. If you can
understand and control the data structures that enter that funnel, you can
prohibit secrets from exiting it.

This has the allure of being a silver bullet, because of course if you can get
to 100% of all the things we mentioned here, you’re golden! But in practice (and
as we’ve seen previously), that’s difficult because secrets find a way to sneak
in or new outflows and side channels are created.

### 🍞 Data transformations

The previous bullet was about controlling how data flows through your system,
this is about transforming, slicing, and disarming that data into safer forms
that can be logged. These are the data security fundamentals that you’re already
familiar with and likely already doing. This is your bread and butter, so I’m
not going to dive into every one. From top to bottom, this is generally arranged
from awesome to meh… basically, by how much information is retained.

Transformation
Result
Minimization
☁ (nothing)
Redaction
[redacted]
Tokenization
2706a40d-3d1d…
Hashing
daadfab322b59…
Encryption
AzKt7vBE7qEuf…
Masking
··········
5309

On the top, we have data minimization. The best way to not log secrets, is to
not have secrets to begin with! This is everything from going passwordless to
fetching only the data you need.

Redaction is the next best thing. Blanking out the secret parts and before you pass
objects around in memory.

Tokenization, hashing, encryption: these all have their pros, cons, and caveats.
Like… are you even doing it correctly?

Dead last is masking. You leave parts of the secret intact. Maybe this works for you.
Maybe it doesn’t. Maybe you go straight to jail 🤷

When these techniques work, they generally work well. But very often what
happens is that they aren’t used or are used too late, after something is
already logged. These have their places in our toolbox, but my claim again is
one bullet isn’t enough.

### 🪨 Domain primitives

Let’s introduce lead bullet #3: domain primitives. Almost all the secrets you
run across in codebases are encoded in-memory as string primitives, and I think
that makes our jobs harder. Strings can be almost anything.

Strings: any sequence of bytes from""to"c̴̞̑ť̸͈̘̌ h̸͝ ̭̘̊ü̶̜̫̦̠͋̆͠ ļ̵̮̤̟̉̀͂ṹ̴̝̂🤷867-53-0999"

const
 secret
=

"..."

There’s very little about them——at compile time or run-time——that lets you
know that it’s sensitive, dangerous to log, or somehow different than any other
vanilla string.

The alternative is a concept I learned from the bookSecure by
Design, and I think it’s one of
the most powerful concepts you can add to your codebase, for logs or anything
else where you want to layer in security at a fundamental level.

Domain primitives: “combines secure constructs and value objects to define the
smallest building block of adomain”

const
 secret
=
 new Secret(
"..."
)

You use them as basic building blocks that hold secret values, and they provide
security invariants and guarantees that basic string primitives simply cannot.

It’s one of the easiest things you can do. If you shift from “any string can be
a secret” to “secrets are secrets”, it makes things a lot easier to reason about
and protect.

#### Compile-time

"Check out a previous blog post on
branded types
, which are
fantastic
 domain primitives with strong
compile-time guardrails."

You can use these to great advantage at compile-time, giving developers
immediate feedback right in their editors.

We can type a logging function (log()) so that itnever accepts secrets.
Then, we use some fetching function that returns secrets, typed as secrets (and
not as strings). If we try to log that secret, it will not compile. The type
system will not let you log this secret.

// Types

declare

const

brand
:
unique

symbol
;

type

Secret

=

string

&
 { [
brand
]
:

string
 };
// Branded type that extends string

type

NotSecret
<
T
>
=

T

extends

Secret

?

never

:

T
;
// Type that excludes secrets

// Logging function

function

log
<
T

extends

string
>(
message
:
NotSecret
<
T
>) { ... };

const

message
:
string

=

"this is fine"
;
// 🧵 string primitive

const

secretz
:
Secret

=

getSecret
();
// 👈 domain primitive

log
(
message
);
// 👌 compiles!

log
(
secretz
);
// 💥 error!

See this example in theTypeScript Playground.

I’m omitting and glossing over a ton of details here, because I don’t want you
to focus on the implementation or even TypeScript, for that matter. The salient
point here is that instead of tossing secret strings around, you brand them as
secret types, providing useful context to both compiler and developer.

#### Run-time

It’s really easy to get started, even with code that is functionally a no-op.
This is basically the simplest form I can think of—an almost empty
class:

class

OpenAIToken

extends
 String {
/* that could be it! */
 }

const

token

=

new

OpenAIToken
(...);

It’s supposed to represent OpenAI credentials, but it’s just using and extending
basic language primitives. You can introduce these objects where secrets
originate, like password fields or anytime you decrypt sensitive data fetched
from the database. And then layer in behaviors and invariants for where they
tend to end up. You progressively start introducing these at both sources and
sinks, allowing you to control where secrets should or shouldn’t go. You can
embed these into data structures so you know what contains secrets. And along
the way, you increase the clarity and safety of your codebase: not only can you
prevent these tokens from going into logs, you can make sure you’re sending them
only to OpenAI and not to some other API by accident.

I think in the long run, domain primitives are the most powerful control we have
because it makes our codesecure by design, but it does take some time to get
there. These can easily address the direct logging cause we discussed earlier,
and with some modifications can help with many more.

#### Run-time: part deux

We can extend this and make it so that the default serialization behavior is
redaction.

class

Secret

extends
 String {


toString() {

return

"[redacted]"
 }
// Override!

}

const

secret

=

new

Secret
(
"shhh!"
);

console
.
log
(
secret
);

Secret: "[redacted]"

If you try to stuff this into logs, into JSON, into kitchen sinks, into error
monitoring,wherever, it’ll always spit out the word “redacted”. You have to
intentionally reach for the value.

Let’s take it further. We can create a custom class with an explicitunwrap()function:

class

Secret
<
T
> {


constructor
(
private

readonly

value
:
T
) {}


toString() {

return

"[redacted]"
 }
// Override serialization


unwrap() {

return

this
.
value
 }
// Explicit getter function

}

There’s so many things you can do here, like maybe you want to encrypt or zero it out
in memory, because that’s in your threat model. You can take this as far as you need
to or are comfortable with. We’ll take it just one step further.

### 🎁 Read-once objects

"A prior blog post on
read-once objects
 goes into more detail!"

There’s a bit to unpack here, but these build off domain primitives in a very
powerful way.

class

Secret
<
T
> {


private

locked

=

false
;


constructor
(
private

readonly

value
:
T
) {}


toString() {

return

"[redacted]"
 }


/* @returns the sensitive value (once and only once) */


unwrap() {


if
 (
this
.
locked
) {
throw

new
 Error(
"already read"
) }


this
.
locked

=

true
;


return

this
.
value
;

 }

}

These objects wrap and keep the secret safe, until you actually
need it. The code in theunwrap()function is the crux: there’s a latch or
lock that activates after the secret is retrieved the first time. It goes into a
“locked” state, and any following reads result in an error that fails loudly.

const

secret

=

getSecret
();

const

res

=

await

authenticate
(
secret
.
unwrap
());
// Proper usage

Logger
.
info
(
secret
);
// [redacted]

Logger
.
info
(
secret
.
unwrap
());
// 💥 Error!

Once you get a secret(from user input, database, decryption, etc.)you wrap
it in a read-once object immediately and keep it wrapped for as long as you can.
And for its single, intended purpose, like using it for some kind of API
authentication, you unwrap the value, use it, and then the object stays locked
for good. This is surprisingly effective at preventing and detecting
unintentional use. It addresses and disarms many of the proximate causes that we
discussed earlier.

This object pairs extremely well with static analysis. Tools like CodeQL or
Semgrep can help ensure that developers aren’t bypassing any safety guarantees.

These are generally high signal, especially when you have good unit test
coverage. One drawback is that read-once objects, if handled incorrectly but not
necessarily unsafely, could cause errors at run-time. But I think the tradeoffs
are usually worth it, especially if you complement it with testing, static
analysis, and taint-checking.Speaking of which…

### 🔎 Taint checking

I like to think of taint checking as static analysis with superpowers. I
absolutely love it and the first time I used it, it was like someone just handed
me a lightsaber. Quick review for the uninitiated: the general idea here is that
you add taint to various sources (like database objects), and yell loudly if the
data flows into certain sinks (like logs).

The red data flow trace on the right detects the secret flowing into logs. But
the green path is fine, because the secret is tokenized. Let’s walk through a
quick example:semgrep.dev/playground/s/4bq5L

On the left, we’ve marked a couple sources like decrypt and a database fetcher.
We’ve also marked our logger as a sink, and thetokenize()function as a
sanitizer.

* On the right in red, we can see that taint was created from the decrypt
function, propagated through thegetSSN()function, and then flagged for
going into the logs on line 18.
* In blue, there’s a much shorter path where the user model from the database is
tainted and then flagged for going into logs.
* And then lastly, in green, we’re tokenizing the decrypted SSN, so it’s not
flagging that it’s logged.

The idea that this is checkingmillionsor more different data flows is the
real magic part for me.

#### Awesome

Some of the strengths of taint analysis: obviously automation. Tracing these
data flows is 100% a job for a machine. This can really help with domain
primitives but also can be used standalone and can even key in on heuristics
like variable names: for example, all variables containing “password”. You can
tie this into all of your critical tools, from code review to CI/CD.

This is especially potent against kitchen sinks and embedded secrets, because
those data structures can be tainted by secret values and checked accordingly.

#### Not awesome

Some personal opinions on drawbacks: I do feel like taint checking rules tend to
be a bit difficult to write. I really, really like Semgrep, but I’m also not the
biggest fan of YAML.

It also turns out that data flow analysis is an NP-hard problem so for large
codebases and monorepos, you likely can’t run full taint analysis on every pull
request or commit. Because it runs in CI/CD and as part of change management,
when it works, it can prevent the introduction of insecure logging into the
codebase.

But, like all of the lead bullets we’ve discussed and will discuss, they can
miss. How can we handle that?

### 🗃️ Log formatters

Let’s say we made the mistake of logging too much data with our email service:

{


tenantId
:

"52902156-7fb6-4ab0-b659-6b07b80cf89a"
,


email
:
 {


subject
:

"Log in to your account"
,


html
:

'<a href="https://acme.com/login/98fPm...">Click here</a> to log in!'
,


from
:

"AcmeCorp <
[email protected]
>"
,


to
:

"Darth Plagueis (The Wise) <
[email protected]
>"
,

 ...

 },


response
:
 {


status
:
200
,


originalRequest
:
 {


headers
:
 {


Authorization
:

"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIi..."

 },


body
:

'{"html": "<a href=\\"https://acme.com/login/98fP...\\">Click..."}'
,

 ...

 }

 ....

 },

 ...

}

We have a couple of our usual suspects here. Because we’re logging email
contents, magic links show up in logs… twice! We’re also logging some kitchen
sinks, like email metadata and the original request, so we have PII and
authorization headers also in logs. But because this data is structured, if we
can traverse these objects, it turns out that we can zero in on these leaks
quite effectively.

{


tenantId
:

"52902156-7fb6-4ab0-b659-6b07b80cf89a"
,


email
:
 {


subject
:

"Log in to your account"
,


html
:

'<a href="https://acme.com/login/REDACTED">Click here</a> to log in!'
,


from
:

"AcmeCorp <
[email protected]
>"
,


to
:

"REDACTED"
,

 ...

 },


response
:
 {


status
:
200
,


originalRequest
:
 {


headers
:

"REDACTED"
,


body
:

'{"html": "<a href=\\"https://acme.com/login/REDACTED\\">..."}'
,

 ...

 }

 ....

 },

 ...

}

If we can introspect these objects, we can scan for dangerous substrings like our
login links, and then drop or redact them. Or we can drop whole values, if we
know that certain paths likeemail.toare particularly dangerous. Fields likerequestorheaderstend to be risky objects that we can also remove. We can
even drop the whole log object if it doesn’t meet some admission criteria,
or—we can simply error out.

So, how and where do we deploy something like this? Most application loggers
should have some type of middleware stack or pipeline, kinda like here on the
right. These are typically configured for operations like converting objects
into JSON, turning error objects into readable formats, or enriching logs by
inserting useful context like network information. We can invert that, and
instead of enriching with useful data, we can remove or redact sensitive data.

export

const

logger

=

createLogger
({


format
:
format.combine
(


transform
(),


handleErrors
(),


enrich
(),


redact
(),
// 👈 insert here!


truncate
(),


jsonify
(),

 ...

 ),

 ...

});

This is a type of guardrail that helps catch many of the common problems we
described previously, like request headers or config objects. I’ve used this
with decent success and found that it works best as a rifle instead of a
shotgun. Because it’s at the application tier, you can customize it for the type
of data or context that each application handles. For example, we can make it so
that any of our domain primitives that reach this layer are quickly detected and
removed.

This is extremely cheap to introduce, but there are some trade-offs. It’s
certainly more of a safety net than hard control, and a developer determined to
bypass it, can and will. Steady state, I measured this at less than 1% of clock
time, but there are some deeply unfortunate ways this can go wrong such as
poorly written regexes and self-ReDoS.

More or less, these risks can be mitigated with solid unit-testing. Which leads
us to…

### 🧪 Unit tests

Lead bullet #7: hooking into and using the existing test suite—that’s already
there—to our advantage. We can use several of the tools we discussed, but
instead of simply detecting or redacting secrets, we can ramp up the sensitivity
in our test environment to fail or error loudly.

Technique
Prod
Test
🪨 Domain primitives
Redact
Error
🎁 Read-once objects
Error
Error
🗃️ Log formatters
Redact
Error
🕵️ Sensitive data scanners
Detect
Error

I’ll cover sensitive data scanners next, but many test suites are already set up
to capturestdoutandstderr, and so you can even point your scanners to
these capture buffers.

The takeaway here is that you can reap the same benefits of CI/CD and change
management by catching unsafe code before it’s merged or deployed, but of
course, you’re also dependent on coverage and if the right code and data paths
are exercised.

### 🕵️ Sensitive data scanners

These are fairly blunt but effective tools that can discover and remove
sensitive data. I’m actively going to avoid diving deep here, because it does
seem like many teams and vendors focus on this as the solution. So instead, I’d
like to pose a few questions that might help you reason about trade-offs:

* Where and when in your logging pipeline is it most effective?
* Is it a gate, in-line of the critical path, or does it scan asynchronously?
* Do you simply want to detect or do you bias towards masking and
redaction? How will your team handle and deal with false positives?
* How far do the general, out-of-box rules take you? Can you tailor it
specifically to your usage patterns?
* Can you verify the credentials? Can that even keep up with log throughput?
* And then perhaps what tends to be the long pole in the tent: what are the
costs, and can you sample instead?

I think these tools tend to be better suited for defense-in-depth, because
they presume that secrets made it into logs to begin with. They can help catch the
more elusive causes we discussed like configuration changes or user input.

#### Sampling

A very brief segue into sampling. Logs tend to have a kind of power law
distribution, where certain types of logs vastly outnumber others. And typically
what you see is that log sources have static points in code, generally with the
same type of data running through them. And so within each log type, scanning
and finding a single true positive might be highly representative of that group.

And so you might run into a scenario where, given some global sample rate,
you’re wasting a lot of work for high frequency logs and not even scanning lower
frequency logs. I think a better alternative to a global sample rate is to
aggregate logs by some heuristic like type or origin, and to ensure you hit some
minimum threshold.

In practice, I’ve found this difficult or impossible to configure with
out-of-box solutions. I’ve had to introduce additional infrastructure to help.
And that’s our next lead bullet.

### 🤖 Log pre-processors

Second to last lead bullet, #9: log pre-processors. These sit between apps that
emit logs, and the final data stores.

In the above example, something likeVectorcan receive
and process logs from our microservices before dispatching them to DataDog or
wherever logs end up. We can configure it to drop sensitive data in-place using
many of the techniques we discussed before. And we can sample some subset of
them and store them onto an S3 bucket, using a more powerful tool likeTrufflehogor an LLM to catch
and verify secrets.

The idea here is to process logs streams before they’re persisted. It doesn’t
need to be Vector, chances are, you already have this existing infrastructure
that’s used for deduping, aggregation, and dropping noisy debug logs. We can
re-use it to prevent and detect secrets in logs. This pairs very well with
sensitive data scanners that we discussed earlier, and might even unlock new
ones you thought were out of reach.

### 🦸 People

“Human practitioners are the adaptable element of complex systems.
Practitioners and first line management actively adapt the system to maximize
production and minimize accidents.”

-Richard Cook,https://how.complexsystems.fail/#12

Our last stop is people. Modern software is a complex system. And while people
will write the code that accidentally introduces sensitive data into logs,
they’re also the ones that will report, respond, and fix them. They’ll build out
the systems and infrastructure that will keep these complex systems safe. And
early on in your maturity story and before you’re able to build out
secure-by-design frameworks, this is the lead bullet you’ll most likely use the
most.

The most important message I want to convey here is that your security team isn’t
alone, especially if you:

* educate your teammates on secure logging design
* empower them to report and address these issues
* and equip them with tools that get out of their way and helps them succeed.

### Recap

Alright, so we’ve covered lead bullets that protect code, protect data, and
protect logs:

1. 📐 Data architecture
2. 🍞 Data transformations
3. 🪨 Domain primitives
4. 🎁 Read-once objects
5. 🗃️ Log formatters
6. 🧪 Unit tests
7. 🕵️ Sensitive data scanners
8. 🤖 Log pre-processors
9. 🔎 Taint checking
10. 🦸 People

Some of these might work for you, some of these won’t, and some that we haven’t
even mentioned could be a homerun for you. Maybe you have super tight control
over your log schemas or maybe you’re using LLMs in a really neat and effective
way. Or maybe you’re building or using a language that has first class support
for controlling secrets.

These worked for me. I have some personal opinions on ones which are
foundational, some that are powerful in the long-run, and some that are really
easy to get started. But your story is different, so I’d like to zoom
out and close out with a high-level, methodical strategy that you can apply for
your security programs, and that we’ll apply and walk through with an example.

## Strategy

Here’sageneral strategy:

1. Lay the foundation
2. Understand the data ﬂow
3. Protect at chokepoints
4. Apply defense-in-depth
5. Plan for response and recovery

I’m not shooting for a Nobel, here. You’re probably doing some of these already,
and chances are, you have some type of playbook or process that looks just like
this. The key idea here is to not miss the forest for the trees, and use these
explicit steps to place our efforts where they’ll matter most. I’ll walk you
through a hypothetical system and we’ll apply these in order.

### 0. Lay the foundation

Step zero is the foundation. Table stakes. This is like the base tier of
Maslow’s hierarchy, and we need these before we try anything else.

Developing expectations, culture, and support is a must-have. They’re easy to
ignore or forget about, but can make or break success. If you work at place that
hasn’t addressed these in the past, it can be quite jarring or difficult to
shift that mentality.

I don’t have a ton of advice here other than making sure your org is aligned on
this. It’ll probably feel like it’s getting worse before it’s getting better,
but that is a sign of progress. A great litmus test for a solid foundation is if
developers will (or already have) come to you to report secrets they found in
logs.

The second thing we’ll need is to decide is what we consider a secret to begin
with. I, admittedly, used secrets and sensitive data interchangeably. This may
not be the case for you. It doesn’t need to be perfect or comprehensive, and
maybe it’s just a framework. But employees, especially the security team, need
common understanding.

The third item is technical. If our logs aren’t structured or aren’t JSON, it’ll
make this endeavor a lot more difficult. A lot of the techniques we discussed
just won’t work. If we don’t have that central pipeline or there isn’tOne and
Only One Wayto both dispatch and view logs, we’ll have to do a lot more
lifting. We’ve seen a few ways that logs bypass this, but having a central
pipeline should cover most of the bases.

### 1. Understand the data flow

With the foundation laid, the next best thing to do is to understand and chart
out how secrets flow through your system. This is basically a Data Flow Diagram,
and we’ll go through a fairly modest example.

On the left, we have users that visit some type of single-page web app. Requests
and data flow through an application load balancer to several web application
services running in containers. This is our core compute and where all the
application code runs. Let’s assume that these are disparate microservices
processing all types of data, some of which are considered secret. For the most
sensitive data, they use KMS to encrypt and then store the ciphertext blobs in
their respective database.

And then, applications use a standard logging library to emit to stdout, which
gets shipped to CloudWatch and then forwarded to Datadog. That’s the final stop,
and that’s where employees, devs, support staff, etc. can view them.

I highly recommend going through an exercise like this, because not only does it
force you to understand the flows and boundaries of the system, if you spend
time at each node and threat model it, you end up finding a bunch of unexpected
ways and places that secrets make it into logs. For example…

* Front-end analytics! It turns out that secrets from things like form contents
to session replays could end up getting sent to your user analytics platform.
* And then what about our application load balancers? These ship their HTTP logs
directly to CloudWatch, so we could be logging embedded secrets in URLs, and
it’s totally bypassing our application tiers.
* Last surprise: error monitoring! Let’s just say that some team wired up Sentry
instead of DataDog for error monitoring,because of course they did, and now
you have another stream of secrets in logs.

We could go further, and we haven’t even drilled into application architecture,
but I think this is a good time to move from discovery to action.

### 2. Protect at chokepoints

The next step we want to take is to protect the chokepoints. And if some flow
isn’t going through that chokepoint, like our rogue team thatyeetedSentry
into prod, we fix it! We can get rid of Sentry and get that team onto the paved
path of our logging pipeline.

We have a very clear chokepoint; a narrow path that most logs eventually flow
through. Here’s where most of our lead bullets should go.

Here’s that chokepoint splayed out. I also added an upstream node to represent
CI/CD, because that’s how code get into our apps. We can then put the bulk of
our protective controls here on the critical path.

We can re-architect the app to use a single logging library and
secure-by-default domain primitives. Then we could use those to build out and
augment our static analysis, taint-checking, and unit tests. These give us a
decent front-line defense for our logging pipeline.

### 3. Apply defense-in-depth

“Every preventative control should have a detective control at the same level
and/or one level downstream in the architecture.”
-Phil Venables,https://www.philvenables.com/post/defense-in-depth

The third step is about adding depth to that defense, a concept we’re all
familiar with. I really like how Phil Venables crystallizes what
defense-in-depth means and I think he generally gives great advice. The idea is
that our controls are not simply overlapping, but mutually supportive.
Something’s always got your back.

Along this chokepoint we add our downstream components, in depth. Some are
preventative, while some are detective.

We can add additional protections like tokenization and read-once objects. We
can add the downstream tools like our custom log formatters, and employ various
sensitive data scanners at different points. And then finally, we can educate
and equip our team.

This is what defense-in-depth looks like to me, and I think this maximizes
chances of success.

### 4. Plan for response and recovery

* Determine the scope
* Restrict access
* Stop the bleeding / ﬁx the source
* Clean up all the places, e.g. indexes
* Restore access
* Do a post-mortem
* Make it ~impossible to happen again

But, of course, if we do miss or if we manage to only detect vs. prevent, we
should be prepared for response and recovery. You already know how to respond to
incidents like this, so I won’t add much here, other than making sure you’re
sticking to a playbook in the right order, pulling levers to restrict and
restore access while you’re responding, as well as thinking about all the weird
places secrets might persist in logs, like indexes.

## Conclusion

And that’s it. This is the culmination of our strategy, our work, and about 30
some minutes of blabber.

With a solid foundation and understanding of our data
flows, we protected our chokepoints in-depth and kept secrets out of logs. We’ve
also introduced a lot of other strong primitives that materially improve our
security program. So is that it? Is the job done?

Well, no, because the data team wired up some ETL jobs that are now spewing
secrets into data lake logs,because of course they did.

Like most things in security, the job often isn’t ever done. But we have the
understanding, the tools, and a strategy to fight the next fight. Keeping
secrets out of logs is inyour hands.

*me

If you liked what you heard, or if you hated it, I’d love to hear your story.
Please,reach out! Thanks! ✌️
