---
title: 'Contract-Driven Development: Write the Truth Once - Ben Howdle'
url: https://benhowdle.im/contract-driven-development.html
site_name: tldr
content_file: tldr-contract-driven-development-write-the-truth-once-b
fetched_at: '2026-07-19T19:27:47.208580'
original_url: https://benhowdle.im/contract-driven-development.html
author: Ben Howdle
date: '2026-07-19'
published_date: '2026-07-15T00:00:00.000Z'
description: 'I''ve built the same idea three times: define the domain once, generate everything downstream. What survived across a bank, a consumer app, and the AI era.'
tags:
- tldr
---

At some point in every codebase's life, you fix the same bug three times in one afternoon. Once in the TypeScript type. Once in the resolver. Once in the validation layer. Three commits, three little green ticks, an exhale-laden sense of accomplishment - and then, somewhere around the third coffee, the sinking realisation that the bug was never actually in the code. The bug was that the truth is fragmented across three places, and truths kept in three places do what all unsupervised triplets eventually do: drift apart and stop speaking to each other.

Every duplicated definition in your system is two truths waiting to disagree. And a disagreement between truths isn't a philosophical problem, it's a bug - just one on a delay, politely waiting for production traffic before introducing itself.

This post is about the fix I keep reaching for, on my third go-round of building it: write the truth once, somewhere machine-readable, and generate everything else. Contract-driven development. I did it at a bank, I rebuilt it at the same bank (we'll get to that), and I'm doing it right now on my own product. The implementations have almost nothing in common. The idea hasn't budged an inch.

## The idea, condensed

DRY wasneverabout code. I know it gets taught as "don't copy-paste", but the actual principle - the one from The Pragmatic Programmer that everyone cites and nobody rereads - is aboutknowledge. Every piece of knowledge should have one authoritative home. A domain model described in a TypeScript interface, an API response, a validation schema and a database table isn't four pieces of code - it's one fact photocopied four times, and photocopies fade. Contract-driven development just takes that seriously: the contract is the single home of the fact, humans argue about the contract, and machines derive everything else. The contract isn't documentationofthe system. The contractisthe system. Everything else is a downstream projection.

Sounds grand. Let me show you what it actually looked like, twice.

## Build #1: YAML at a bank

AtLetter(US fintech, I was CTO, the buck stopped with me in ways I still occasionally wake up thinking about) we were building an event-sourced banking platform. When you're moving actual money, two definitions disagreeing isn't tech debt - it's an incident, possibly a legal or regulatory one. So the entire domain lived in sixteen YAML files, one per bounded context: account, card, payment, transaction, user, and so on. Each one an OpenAPI document describing that domain's events, types and enums. Sixteen files that described the whole bank.

A generator - about 470 lines of TypeScript and Mustache templates, which sounds quaint and absolutely was - walked those schemas and emitted around349TypeScript model files. Event classes with their payloads, serialisation, revision tracking. Every event stamped with a ULID at birth. Branded ID types too, so anAccountIdcouldn't be accidentally handed to something expecting aPaymentId- the compiler simply wouldn't let you cross the streams.

The shape of the thing, roughly:

utils/event-flow/
├── schema/ ← sixteen YAML files. The truth.
│ ├── account.yaml
│ ├── card.yaml
│ ├── payment.yaml
│ ├── transaction.yaml
│ └── ...
├── templates/ ← event.mustache, type.mustache, enum.mustache
├── bin/gen-schema.ts ← the 470-line machine
└── src/ ← ~349 generated files. Do not touch. Seriously.

And a (redacted, abridged) taste of what the truth looked like. You declare this:

AssetCreated
:

 
description
:
 Event
 
allOf
:

 
-
 
$ref
:
 
"#/components/schemas/AssetRollup"

AssetCreateRejected
:

 
description
:
 Event
 
properties
:

 
reason
:

 
type
:
 string

AssetRollup
:

 
required
:
 
[
id
]

 
properties
:

 
id
:

 
type
:
 string
 
organizationId
:

 
type
:
 string
 
indexed
:
 collection 
# ← custom extension: "you'll query by this"

 
value
:

 
type
:
 number

...and this falls out the other end, without a human touching it:

// AUTO-GENERATED — edits will be destroyed

export
 
class
 
AssetCreated
 
extends
 
EventBaseImpl
 
{

 
static
 
getIndexedProps
(
)
 
{

 
return
 
{
 organizationId
:
 PropIndexType
.
Collection 
}
;

 
}

 
// create(), fromJson(), toJson(), revision tracking,

 
// ULID-stamped header, origin-event chaining...

}

A few things in that design I'm still proud of:

* The failure path was in the contract.Events came in pairs:AssetCreatedandAssetCreateRejected. You could not define the happy path without being confronted by its failure sibling. If your contract only describes success, it describes half a system - the half that doesn't ping you.
* The contract knew how data would be queried.A little customindexed:extension on any property generated typed index metadata for the read models. The YAML didn't just say what a thingwas, it said how it would befound.
* Generated code was untouchable, and loudly so.The build wiped the entire src directory and regenerated it from scratch. The README warned: "If you make changes to those files They will be destroyed." Punctuation optional, intent fully intact.

On the other side of the system, a single GraphQL schema fanned out - via codegen - into typed resolvers for the API, React Apollo hooks for the web app, and typed service-to-service calls. Three consumers, one schema, zero drift. When the schema changed, every consumer either updated or refused to compile. Refusing to compile issounderrated as a communication mechanism. It's the only status update that cannot be ignored.

## The security model lived in the spec too

This is the bit I'd tattoo somewhere prominent if I were the tattooing sort: we put theauthorisation rulesin a spec as well, and generated the enforcement.

Every backend RPC declared its access policy right there in the endpoint definition, using a tiny pipe-delimited policy DSL - which sounds grim, and honestly reads a bit grim, but had one enormous virtue: it lived in the contract, next to the thing it protected.

"/accounts/get-statements"
:

 
get
:

 
responses
:

 
default
:

 
description
:
 Fetch account statements
 
security
:

 
-
 
UserContext
:

 
-
 
"organization|owner|organizationId"

 
# ^ caller must hold "owner" in the organisation

 
# whose id arrives in the request's organizationId

 
-
 
RbacRole
:

 
-
 
'r.accountId|["Owner","Admin","Auditor","Member"]'

 
# ^ ask the authorisation service whether THIS user

 
# can touch THIS specific account, in these roles

A Handlebars template turned those declarations into per-service middleware: a generated policy map, a generated auth check on every RPC, entity-level decisions deferred to a dedicated authorisation service, and the caller's roles carried in a cryptographicallysigneduser context - so the roles themselves couldn't be tampered with in transit. Best of all, it failed closed: an endpoint with no declared policy didn't default to open, it defaulted todenied. The safest default in the whole company was one nobody had to remember to write.

And here's the payoff that made auditors and my own paranoia very happy: a security review of "who can call what" wasreading one file. Not fifty resolvers, not a wiki page last updated two banking partners ago - one spec, every endpoint, every role, in a format a compliance person could read with a coffee. When you're a bank, that's not a nice-to-have; that's weeks of audit pain converted into an afternoon. I gave a whole talk on this security architecture at fintech_devcon -Securing a Banking System's UI and API- if you want the full tour.

Honesty compels me to add: we didn't push it far enough everywhere. The GraphQL gateway got declarativeauthentication(a generated-adjacent wrapper that refused anonymous callers on every resolver), but itsauthorisationchecks were hand-written inline, resolver by resolver. Entirely predictably, that's the one corner of the system where a security review meant actually reading code rather than reading a spec. The exception that proves the rule, in the most annoying possible way.

## What it actually did to the team

Here's the highfalutin bit, but I promise it stays practical.

The obvious win was mechanical - I wrote inThe First CTOthat engineers "only had to define data structures once, rather than in multiple locations", and that's true, but it undersells it somewhat. The deeper thing was where theconversationsmoved.

Design arguments moved into the spec. Arguing about a YAML field - its name, its type, whether it's optional - is cheap. Ten minutes, one file, everyone can read it, including people who don't write TypeScript for a living. Arguing about the same decision after it's been implemented five different ways across five services is expensive and slightly heartbreaking. The contract gave us a place to disagreeearly, which is the cheapest possible time to disagree.

Onboarding compressed. "Read the sixteen files in the schema directory" is a genuinely complete answer to "how does this bank work?". Not the whole answer to how it'sbuilt- but the whole answer to what itis.

And a whole category of bug became unrepresentable. Not caught -unrepresentable. The type can't drift from the validation can't drift from the event shape, because they're all children of one parent. You don't need a linter rule, a code review checklist, or that one studious engineer. The drift has nowhere to live.

Inhot potato terms: a contract is a potato that never needs passing. The answer to "what shape is a payment?" is already in everyone's hands. Nobody is waiting on anybody. That question has stopped being work.

## The iteration

We rebuilt it. At the same company. The YAML/OpenAPI pipeline got replaced by a second generation built on CUE and protobuf - better cross-language guarantees, gRPC clients, proper constraint checking. The specifics don't matter here (that's its own post). Even the people most convinced of the philosophy threw away the firstimplementationof it.

Which is the lesson, honestly. The format is incidental. You will probably get the format wrong the first time - too clever, too rigid, wrong ecosystem, some YAML extension that seemed brilliant at 11pm. Fine. The format is a hat, maybe a haircut. The philosophy - one source of truth, everything else derived, drift made impossible or at least deafening - that's the part you keep.Nothing you build is sacred. Patterns over artefacts, every time.

(I ended up giving a fintech_devcon talk that's secretly about this exact muscle -Letting Go of Perfectionism in Distributed Systems- because throwing away your own working pipeline while keeping its soul intact turns out to be a transferable skill, and one your ego fights every single time.)

## Build #3: the contract moves into the language

Fast-forward to now, andSnug- my own product. Same idea, third body. And the interesting part is what six years of hindsight changed.

The contract isn't YAML anymore. It's TypeScript and Zod. There's a file of shared domain schemas, and a big typed route registry - every endpoint in the system declared in one nested object: method, path, request schema, response schema, envelope. That registry currently describes 167 routes across 19 groups, with 293 registered schemas over 73 database tables. Roughly 6,200 "hand-written" lines of contract generate about 15,400 lines downstream: database types, validation schemas, a fully typed SDK (auth, path params, envelope unwrapping, runtime response validation - the lot), an API spec, even human-readable docs.

The truth now looks like this (redacted, but structurally faithful):

// The domain, once, as Zod — compile-time types AND runtime validation

export
 
const
 UserSchema 
=
 z
.
object
(
{

 id
:
 z
.
string
(
)
,

 email
:
 z
.
string
(
)
.
email
(
)
.
nullable
(
)
.
optional
(
)
,

 status
:
 z
.
enum
(
[
"pending"
,
 
"onboarding"
,
 
"completed"
]
)
.
default
(
"pending"
)
,

 createdAt
:
 ISODateString
,

}
)
;

// The API surface, once, as a typed registry

export
 
const
 
API_ROUTES
 
=
 
{

 users
:
 
{

 me
:
 
{

 method
:
 
"GET"
 
as
 
const
,

 path
:
 
"/api/users/me"
,

 response
:
 UserPublicSchema
,

 
}
,

 updateProfile
:
 
{

 method
:
 
"PATCH"
 
as
 
const
,

 path
:
 
"/api/users/profile"
,

 request
:
 UpdateProfileRequestSchema
,

 response
:
 UserPublicSchema
,

 
}
,

 
}
,

 
// ...another 165 routes

}
;

And the generated SDK means the frontend physically cannot invent an endpoint or send the wrong shape:

const
 api 
=
 
createApiClient
(
baseUrl
,
 getAuthToken
)
;

const
 me 
=
 
await
 api
.
users
.
me
(
)
;
 
// fully typed, response

 
// validated at runtime

await
 api
.
users
.
updateProfile
(
{
 name
:
 
"Ben"
 
}
)
;
 
// request shape enforced

 
// by the compiler

The monorepo layout tells the same story:

backend/
├── src/lib/contracts.ts ← shared Zod domain schemas
├── src/api/contracts/index.ts ← the route registry. The truth.
├── scripts/run-generators.ts ← "FAIL-FAST ONLY" orchestrator
└── _generated/ ← ⚠️ AUTO-GENERATED. DO NOT EDIT.
 ├── _db-types.ts ← 73 tables → 73 interfaces
 ├── _db-zod.ts
 ├── _contracts.ts
 └── _sdk.ts ─┐
frontend/ │ byte-identical twins,
└── _generated/ │ same SHA-256 hash
 └── _sdk.ts ─┘

What changed between 2019-me and now-me:

* I stopped fighting the host language.YAML needed a parser, templates, a translation layer. Zod schemasareTypeScript - they give you compile-time types and runtime validation from one definition, and the "generator" becomes a much smaller machine. The external DSL was a phase. (Unless you have non-TypeScript consumers - Snug has an iOS app reading the same contracts, and that's exactly the tension that pushed Letter towards protobuf.)
* Truth can flow upwards.The database schema is introspectedfrom production- the deployed database is the authority on what the data actually is, and generated files carry FROZEN headers.
* Drift protection grew teeth.This is the big one. Letter's pipeline made drift unlikely; Snug's makes itfail. Hash manifests. A freshness check that refuses generated code older than 24 hours. A CI job proving a fresh migration reproduces production exactly. A ban on anynewz.any()response sneaking into the contracts (the existing ones are grandfathered - pragmatism over purity, always). The generator's own header comment reads "FAIL-FAST ONLY. NO PLACEHOLDERS, NO SOFT-FAILS" - which was written by me, to me, about me, because I know exactly what I'm like at 6pm on a Friday.
* Regeneration is ambient.It runs on every dev server start and every build. No ceremony, not a "codegen day" - just how the code wakes up. The frontend and backend SDKs are byte-identical, same SHA-256 hash, and that hash equality is itself a drift alarm.

## The 2026 reason

Everything above was true in 2019, and it was worth doing in 2019. Here's what's changed: I don't write most of Snug's code by hand anymore, and if you're honest, you probably don't either.

The 2019 argument for contracts was thathumansdrift. The 2026 argument is that agents drift faster. An LLM writing code is confident, prolific, and utterly unburdened by memory of what it did last Tuesday. Left unsupervised it will invent an endpoint that nearly exists, rename a field to what itshouldhave been called (fair, but no), and skip the validation because the happy path worked in its head.

Point it at a contract and all of that becomes a compile error.

This is also where I've landed on the whole "how do I get better output from coding agents" question. When an agent flounders, there's a law of diminishing returns on iterating - prompt, tweak, prompt again, each round a little worse, like photocopying a photocopy. The highest-leverage nudge is almost never a better prompt; it's bettercontext, and a contract is the densest context there is. Here is the truth, machine-readable, non-negotiable. Now build against it. The generator handles what must be deterministic; the agent handles what benefits from judgement. Machine-that's-always-right does the boilerplate, machine-that's-usually-right does the interesting bits, and the contract sits between them like a bouncer.

Snug is substantially AI-builton top of these rails, and the rails are the reason that's been safe rather than terrifying. Mostly.

## The honest costs

Because it's not free, and posts that pretend otherwise are adverts:

* You will debug the generator itself at some point, and briefly question the entire premise plus several life choices. Meta-bugs are uniquely demoralising - the machine that makes the code is wrong, which feels like being betrayed by your own kettle.
* Escape hatches aren't cheating - they're load-bearing. Strict mode for CI, warn mode for humans. Grandfatheredz.any()s. Legacy enum values kept alive because there are iOS builds in the field that still believe in them. A pipeline with no escape hatches gets bypassed entirely within a month, and then you've got driftplusceremony.
* The dev loop pays a tax. A few seconds of generation on every start, every build. You're buying correctness with latency. I'll take that trade every day, but itisa trade.
* And it can absolutely be overkill. A two-endpoint weekend MVP does not need a contract pipeline; it needs to exist. My rule of thumb: the third time you fix the same fact in two places, the itch is real. Scratch it then. Not before, definitely not never.

## TL;DR

Three builds, one idea:

* Every duplicated definition is two truths waiting to disagree - and stale truths are just bugs on a delay.
* Write the truth once, machine-readable. Generate the rest. The contractisthe system.
* Put the failure path in the contract. A contract that only describes success describes half a system.
* Put the authorisation rules in the contract too, and fail closed. A security audit should be reading one file, not fifty resolvers.
* The format won't survive (mine went YAML → CUE/protobuf → TypeScript/Zod). The philosophy will. Don't get attached.
* Give drift protection teeth: fail-fast generation, hashes, CI gates. Unlikely isn't the same as impossible.
* In the AI era, the contract is also the agent's context - the cheapest way to keep a probabilistic coder honest.
* Don't build it for a weekend MVP. Build it the third time you fix the same fact twice.

Write the truth once. Let the machines do the photocopying - they're the only ones who can do it without the copies fading.

New Book

### The First CTO: The Job Nobody Explains

A playbook for the loneliest job in startups. 15 chapters of painful lessons, hard-won advice, and practical frameworks from 5 years as CTO at two seed-stage startups.

Learn more

Need a collaborator?

Let's build something incredible together.

Work with me

Email me

← Back to all posts

Writing software stories since 2012.