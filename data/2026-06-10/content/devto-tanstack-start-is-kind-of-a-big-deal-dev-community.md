---
title: TanStack Start Is Kind of a Big Deal - DEV Community
url: https://dev.to/erikch/tanstack-start-is-kind-of-a-big-deal-4nec
site_name: devto
content_file: devto-tanstack-start-is-kind-of-a-big-deal-dev-community
fetched_at: '2026-06-10T07:43:26.672485'
original_url: https://dev.to/erikch/tanstack-start-is-kind-of-a-big-deal-4nec
author: Erik Hanchett
date: '2026-06-08'
description: Introduction People keep telling me TanStack Start is kind of a big deal, and I wanted to... Tagged with tanstack, react, typescript, webdev.
tags: '#tanstack, #react, #typescript, #webdev'
---

Client-first logic and same-file server calls

## Introduction

People keep telling me TanStack Start is kind of a big deal, and I wanted to know if that holds up or not. I've been spending a lot of time at conferences lately, and TanStack Start comes up quite often in conversation. The community is split if server components is the right answer. TanStack Start has gone the opposite direction with it's clean client-side first components approach, with lot so ways to call server-side code, even in the same component.

I'm a Vue and Nuxt person most days, so I'm not here to dunk on anyone's framework. What I want to figure out is simpler: are there specific things TanStack Start does that Next.js and Nuxt don't, and are they good enough to switch for?

After some research I have come up with three things I really like about TanStack Start. These things alone aren't probably enough for me to switch, but I'm getting close.

If you'd like to watch a video instead, check this out!

## Prerequisites

* Node.js 22+
* Comfort with React and TypeScript
* You do not need any Next.js or TanStack experience

## What we're building

A GitHub user lookup. You type a username, the app fetches that user from the GitHub API on the server, and renders their profile. It's a perfect app to show these three features.

You can find the full code in thedemo repo. Let's start by creating the app.

## Step 1: Create the app

TanStack has a CLI, so scaffolding is one command:

npx @tanstack/cli@latest create my-app 
--framework
 React

Enter fullscreen mode

Exit fullscreen mode

It asks about a package manager and a few add-ons, then sets up a project on Vite with file-based routing. Run it:

cd 
my-app
npm 
install

npm run dev

Enter fullscreen mode

Exit fullscreen mode

The dev server was ready in under a second on my machine. That Vite-powered startup is really nice, and it's the same Vite speed I covered in my earlier Vite videos.

The structure is small:

src/
├── routes/
│ ├── __root.tsx # the document shell
│ └── index.tsx # the home route
├── router.tsx # router config
└── routeTree.gen.ts # auto-generated, don't edit

Enter fullscreen mode

Exit fullscreen mode

Now the three features.

## Feature 1: One server function for reads and writes

Let me be fair up front, Next.js can also call server code directly. Next has React Server Functions, and in mutation contexts those are Server Actions. You mark a function with"use server"and call it from a component, no API route required. Nuxt has its own version withserver/apiroutes plususeFetch, which gives you typed responses too. So "call a function on the server" is not unique.

However, the difference is the constraint. Next.js Server Actions run as POST requests and are built for mutations. The Next docs themselves steer you to Server Components or Route Handlers for reading data. Youcancall a Server Action from a client component to read, but it still goes over POST and isn't the idiomatic, cacheable GET path.

TanStack Start doesn't split it this way. One primitive,createServerFn, handles both a GET read and a POST mutation, and you call it the same way from anywhere.

import
 
{
 
createServerFn
 
}
 
from
 
'
@tanstack/react-start
'

interface
 
GithubUser
 
{

 
login
:
 
string

 
name
:
 
string
 
|
 
null

 
avatar_url
:
 
string

 
html_url
:
 
string

 
bio
:
 
string
 
|
 
null

 
public_repos
:
 
number

 
followers
:
 
number

 
following
:
 
number

}

const
 
getGithubUser
 
=
 
createServerFn
({
 
method
:
 
'
GET
'
 
})

 
.
inputValidator
((
username
:
 
string
)
 
=>
 
username
)

 
.
handler
(
async 
({
 
data
:
 
username
 
}):
 
Promise
<
GithubUser
>
 
=>
 
{

 
const
 
res
 
=
 
await
 
fetch
(
`https://api.github.com/users/
${
username
}
`
,
 
{

 
headers
:
 
{

 
Accept
:
 
'
application/vnd.github+json
'
,

 
// a token here stays on the server, never ships to the client:

 
// Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,

 
},

 
})

 
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
`User "
${
username
}
" not found`
)

 
return 
(
await
 
res
.
json
())
 
as
 
GithubUser

 
})

Enter fullscreen mode

Exit fullscreen mode

That.handlerruns only on the server, so a token never reaches the browser. I setmethod: 'GET'because this is a read, and I call it straight from my route loader like a normal async function. There is no route handler, or RSC boundary to think about and no endpoint string to keep in sync. (This snippet is trimmed for clarity. The version in the repo addsencodeURIComponenton the input and separate handling for 404 and 403 rate-limit responses.)

You can watch this happen in the browser too. Open the network tab, run a lookup, and you won't see a request toapi.github.comanywhere. The only call is the one to my own server. The GitHub fetch is happening server-side, which is exactly where I want it, and any token isn't leaked.

I really like how types work here. I annotate the handler's return asGithubUseronce, and that type flows through the loader and into the component without me re-typing it at each call, and that holds whether it's a GET or a POST. Rename a field in the interface and every call that still reads the old property lights up red. (One caveat, that's compile-time propagation, not runtime validation. I cast the GitHub response withas GithubUser, so if you want to prove the external JSON actually matches, you'd add a runtime schema check.) You can get there with a route handler too, with shared types or a schema validator. The difference is that TanStack infers the chain for you by default instead of asking you to wire it up.

## Feature 2: Search params that are actually typed

This is the one where TanStack genuinely has an advantage as of today. Next.js gives you generic string and string-array search params, not route-local schema validation.useSearchParamshands you a read-onlyURLSearchParams, and whiletypedRoutesplus thePagePropshelper have improved path, navigation, and page-prop typing, none of that validates or transforms thevaluesinside the query string the way TanStack Router does. You can get there in Next with Zod,nuqs, ornext-typesafe-url, but it's something you add on. Nuxt can validate a route withdefinePageMeta'svalidatefunction, which can returnfalseor aPartial<NuxtError>to reject a route, but it doesn't turnroute.queryinto a typed, validated query object for your component.

TanStack Router treats search params as validated route state out of the box:

export
 
const
 
Route
 
=
 
createFileRoute
(
'
/
'
)({

 
validateSearch
:
 
(
search
):
 
{
 
user
:
 
string
 
}
 
=>
 
({

 
user
:
 
typeof
 
search
.
user
 
===
 
'
string
'
 
?
 
search
.
user
 
:
 
''
,

 
}),

 
loaderDeps
:
 
({
 
search
:
 
{
 
user
 
}
 
})
 
=>
 
({
 
user
 
}),

 
loader
:
 
async 
({
 
deps
:
 
{
 
user
 
}
 
})
 
=>
 
{

 
if 
(
!
user
)
 
return
 
{
 
user
:
 
null
,
 
error
:
 
null
 
}

 
return
 
{
 
user
:
 
await
 
getGithubUser
({
 
data
:
 
user
 
}),
 
error
:
 
null
 
}

 
},

 
component
:
 
Home
,

})

Enter fullscreen mode

Exit fullscreen mode

I validate?user=once. After that,Route.useSearch()gives me{ user: string }, fully typed, anywhere in the component. The loader reads that param and runs the server function, so loading the page with?user=ErikCHin the URL loads the profile directly, with no extra client wiring. The lookup is shareable and survives a refresh, and I never wrote client state to make that happen. You can plug in Zod if you want richer schemas.

## Feature 3: Type safety that runs end to end by default

Typed navigation by itself isn't unique, and I want to be straight about that. Next.js hastypedRoutesfor statically typed links, and Nuxt has typed navigation built in throughexperimental.typedPages, plus thenuxt-typed-routermodule for more. So all three can stop you from typoing a route.

The difference is how far the chain reaches and how much setup it takes. Next'stypedRoutestypes the path, not the search param values. Nuxt's typed pages are opt-in and cover routes and params. In TanStack it's on by default, and the same type system covers your route params, your search params, and your loader data in one connected chain.

const
 
navigate
 
=
 
useNavigate
({
 
from
:
 
Route
.
fullPath
 
})

function
 
lookup
(
e
:
 
React
.
FormEvent
)
 
{

 
e
.
preventDefault
()

 
navigate
({
 
search
:
 
{
 
user
:
 
input
.
trim
()
 
}
 
})
 
// typed: { user: string }

}

Enter fullscreen mode

Exit fullscreen mode

If I pass a search param that doesn't exist, or the wrong type, the type checker flags it. Vite itself transpiles TypeScript without type checking, so this istsc --noEmit(I keep it in atypecheckscript and run it in CI) or your editor catching it inline. And because the loader's return type flows intoRoute.useLoaderData(), the data I render is typed by the same chain that typed the navigation. That whole path, from the server function return through the loader, the search params, and the link, is one thing instead of three features you wire up separately.

## Adding in AI

I lean on AI coding assistants like Kiro for a lot of my code, and TanStack Start is new enough that the models don't have great knowledge on it. When I asked for a server function, I'd sometimes get an older API shape back, because the training data is behind.

TanStack ships a fix for exactly this, and it's the last thing I showed in the video. There's a package called TanStack Intent that wires your coding agent into current TanStack patterns. You install it like this:

npx @tanstack/intent@latest 
install

Enter fullscreen mode

Exit fullscreen mode

That creates or updates your agent config, defaulting toAGENTS.md(it can target others likeCLAUDE.mdor.cursorrulestoo), with skill-loading instructions. Your agent reads it, sees which TanStack skills are available, and pulls the current docs for whatever it's working on instead of guessing from stale training data.

So I opened Kiro CLI, which picks up thatAGENTS.mdon its own, and gave it this:

Please review my existing repository against the newly loaded TanStack Intent rules. Check my implementation for anti-patterns, missing edge cases, or deprecated syntax.

It worked through the skills and came back with a list, a couple ofverbatimModuleSyntaxnotes, some dev-tools setup for TanStack Start, a shell component thing. One last thing, I wasn't pinning the latest version tags in mypackage.json. Though not really required all the time, I did like how it was looking at thepackage.jsonfile in general.

The second guardrail is the type safety from earlier. When the AI guessed an oldcreateServerFnshape,tscand my editor flagged it right away. I didn't have to catch it in review. The types caught it for me.

This is the same point I made in my Vue in the Age of AI video. AI writes more of our code now, so the frameworks that verify the AI's work for you are worth more than they used to be.

## Cleanup

Nothing to tear down for local development. Stop the dev server with Ctrl+C. If you deployed, TanStack Start uses Nitro under the hood, so you can remove whatever Node target you set up. Those hosting resources can incur charges, so tear them down if you were only testing.

## Conclusion

So is it kind of a big deal? I'd put it this way. If you want explicit control, fast Vite builds, and type safety that runs from the server function through search params to your links, TanStack Start is genuinely the most compelling React framework I've tried in a while. The server functions and typed search params alone are just really nice to have.

It's not for everyone yet. The ecosystem is smaller than Next.js, there are fewer plugins and it's young. The TanStack CLI is still marked alpha, there are fewer production references to learn from, and the deployment and debugging knowledge isn't as standardized as Next.js. If you need the hiring pool and the deployment story Next.js has, that's a real reason to wait.

But "the default React framework is finally in question" is true for the first time in years, and after building with it, I get why people are switching. If you're a Nuxt person like me, the typed search params and server functions will feel like the things you wish you had without reaching for extra modules.

Resources:

* TanStack Start docs
* TanStack Start vs Next.js (official)
* Search params validation
* Inngest: Why we migrated off Next.js
* Kiro
* Demo repo

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse