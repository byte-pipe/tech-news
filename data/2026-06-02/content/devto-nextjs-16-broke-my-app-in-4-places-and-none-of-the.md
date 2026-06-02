---
title: Next.js 16 Broke My App in 4 Places and None of Them Threw an Error - DEV Community
url: https://dev.to/shubhradev/nextjs-16-broke-my-app-in-4-places-and-none-of-them-threw-an-error-51mn
site_name: devto
content_file: devto-nextjs-16-broke-my-app-in-4-places-and-none-of-the
fetched_at: '2026-06-02T20:05:23.175763'
original_url: https://dev.to/shubhradev/nextjs-16-broke-my-app-in-4-places-and-none-of-them-threw-an-error-51mn
author: Shubhra Pokhariya
date: '2026-05-27'
description: The CI was green. Build passed. No TypeScript errors. No warnings. Everything looked clean. I... Tagged with nextjs, typescript, webdev, javascript.
tags: '#nextjs, #typescript, #webdev, #javascript'
---

Middleware renamed to proxy.ts

The CI was green.

Build passed. No TypeScript errors. No warnings. Everything looked clean. I clicked deploy and went to make tea.

Came back, opened staging, and things were broken in ways that made no sense. A redirect wasn't working. Lint had silently disappeared from the build pipeline. One API route was throwing on the very first real request. And a revalidation call I'd written two weeks earlier was running but doing nothing.

Not one of these showed up during the build. Everything looked completely fine until it wasn't.

This is what actually happened during my Next.js 16 upgrade, and what to check before you ship yours.

## 1.middleware.tsstopped running and told me nothing

My middleware file was fine. It compiled. The export was valid. TypeScript was happy.

After upgrading to Next.js 16, it just stopped running on requests. No error. No deprecation warning. No sign of anything wrong in the terminal. The file was simply ignored.

What happened: Next.js 16 replacedmiddleware.tswithproxy.ts. Same location in your project. Different filename. Different exported function name.

// Before: middleware.ts

export
 
function
 
middleware
(
request
:
 
NextRequest
)
 
{

 
return
 
NextResponse
.
redirect
(
new
 
URL
(
'
/home
'
,
 
request
.
url
))

}

Enter fullscreen mode

Exit fullscreen mode

// After: proxy.ts

export
 
function
 
proxy
(
request
:
 
NextRequest
)
 
{

 
return
 
NextResponse
.
redirect
(
new
 
URL
(
'
/home
'
,
 
request
.
url
))

}

Enter fullscreen mode

Exit fullscreen mode

That's the whole change. File rename, function rename. But because the old file didn't throw anything, I assumed it was still running. I only caught it because a redirect I expected wasn't happening and I spent way too long looking at the wrong thing.

One thing to know: if you need edge runtime behavior specifically,middleware.tsstill exists for that use case. In my case, the logic I had there stopped running after the upgrade. Renaming the file and export fixed it immediately. The codemod handles this automatically. But if you manually upgraded the package without running it, or if it missed a file, this one is completely invisible.

Before you ship:rename the file, rename the export, test a route that depends on it.

## 2.revalidateTag('products')compiled, deployed, and silently did the wrong thing

During the migration I wrote this:

revalidateTag
(
'
products
'
)

Enter fullscreen mode

Exit fullscreen mode

One argument. Totally normal in Next.js 15. I'd written it a couple of weeks earlier and hadn't thought about it since.

In Next.js 16, the single-argument form is deprecated and produces a TypeScript error. But only if yourtsconfigis in strict mode. Mine wasn't. It had been set up on an older project years ago and never touched.

So it compiled. It deployed. It ran. And it fell back to legacy invalidation behavior instead of the new SWR-based system. Pages weren't reflecting mutations. No error anywhere, just stale data that I attributed to other things for longer than I should have.

The fix is just adding the second argument:

revalidateTag
(
'
products
'
,
 
'
max
'
)
 
// SWR, the recommended default

revalidateTag
(
'
products
'
,
 
{
 
expire
:
 
0
 
})
 
// Immediate expiry, for webhooks

Enter fullscreen mode

Exit fullscreen mode

The codemod (npx @next/codemod@canary upgrade latest) handles this. But if you wrote any revalidation calls after upgrading, or if the codemod missed a file, check manually.

The real fix is turning on strict mode in yourtsconfig. That one change makes this a compile error instead of a silent runtime problem:

{

 
"compilerOptions"
:
 
{

 
"strict"
:
 
true

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Do it before anything else.

## 3.next lintdisappeared and my CI kept saying it passed

This one sounds minor. It wasn't.

next lintis completely removed in Next.js 16. Not deprecated. Not changed. Gone. Theeslintoption innext.config.tsis also gone.next buildno longer runs linting automatically.

My CI was configured to runnext lintas a step. After the upgrade, that command no longer existed. Depending on how your CI handles missing commands, it might fail loudly or it might just succeed silently and move on. Mine moved on.

So I was shipping code with no linting running, and the CI was reporting green. I only noticed when an obvious issue slipped through that I expected lint to catch.

The migration is to run ESLint directly:

"scripts"
:
 
{

 
"lint"
:
 
"eslint ."
,

 
"lint:fix"
:
 
"eslint . --fix"

}

Enter fullscreen mode

Exit fullscreen mode

The codemod createseslint.config.mjsand updates your package.json scripts. But your CI config is a separate file the codemod does not touch. Check both places.

## 4. One component was still readingparamssynchronously

The codemod updated most of my pages correctly. But I had a layout file it missed. The component was accessingparamsdirectly without awaiting it, which is fine in Next.js 15 but wrong in 16 whereparamsis now a Promise.

// Before — Next.js 15

export
 
default
 
function
 
Layout
({
 
params
 
}:
 
{
 
params
:
 
{
 
id
:
 
string
 
}
 
})
 
{

 
const
 
id
 
=
 
params
.
id

}

// After — Next.js 16

export
 
default
 
async
 
function
 
Layout
({

 
params
,

}:
 
{

 
params
:
 
Promise
<
{
 
id
:
 
string
 
}
>

})
 
{

 
const
 
{
 
id
 
}
 
=
 
await
 
params

}

Enter fullscreen mode

Exit fullscreen mode

This one did throw, but only on the first real request to that route in staging, not during the build. The build passed completely clean.

If you have layouts, pages, or route handlers, search the whole codebase for directparams.access and check that every one has been updated. Same goes forsearchParams,cookies(),headers(), anddraftMode(). All async now, all need awaiting.

## The pattern that connects all four

None of these are caching bugs. They're upgrade bugs. The kind where the build passes, the code is technically valid, and the wrong behavior only shows up under a specific condition: a real redirect being triggered, a mutation needing to reflect, a lint issue reaching review, a specific route being hit.

The codemod gets most of this. Runnpx @next/codemod@canary upgrade latestbefore you change anything else. Then check three things manually: grep for anyrevalidateTag(with a single argument, check your CI config fornext lint, and turn on strict TypeScript. Those three cover most of what the codemod can miss.

If you're already past the upgrade and dealing with caching behavior specifically, the previous posts in this series cover that.The debugger I built to make cache behavior visible during developmentandthe seven bugs that compile clean and break silently in production.

I also have a full step-by-step migration guide with before/after comparisons atshubhra.dev/tutorials/nextjs-16-cache-componentsif you want the complete reference.

Which of these hit you? Or something I didn't mention here?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (15 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse