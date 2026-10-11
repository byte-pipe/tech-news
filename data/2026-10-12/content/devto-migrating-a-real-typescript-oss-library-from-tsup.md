---
title: Migrating a Real TypeScript OSS Library from tsup to tsdown 🔧 - DEV Community
url: https://dev.to/nyaomaru/migrating-a-real-typescript-oss-library-from-tsup-to-tsdown-5b80
site_name: devto
content_file: devto-migrating-a-real-typescript-oss-library-from-tsup
fetched_at: '2026-10-12T06:00:24.814456'
original_url: https://dev.to/nyaomaru/migrating-a-real-typescript-oss-library-from-tsup-to-tsdown-5b80
author: nyaomaru
date: '2026-10-07'
description: The config migration was small. Preserving the package contract was the interesting part. Hoi hoi!... Tagged with typescript, opensource, webdev, frontend.
tags: '#typescript, #opensource, #webdev, #frontend'
---

Verifying packed output prevents breaking changes

The config migration was small. Preserving the package contract was the interesting part.

Hoi hoi! 👋

I'm@nyaomaru, a frontend engineer who enjoyed looking for fungus this season. 😸🍄

Recently, I migrated its build setup fromtsuptotsdown.

At first, I expected this to be a very small task.

Just removetsup.Just installtsdown.Just change the config.Run the build.Done! 🎉

And honestly...

The config migrationwassmall.

But there was one interesting problem.

The firsttsdownbuild succeeded while silently changing files that were already part of the package's public contract.

So this article isn't really an introduction totsdown.

Instead, I want to show what happened when I migrated a real published TypeScript library fromtsuptotsdown, what actually changed, and how I verified that consumers would still receive the same package.

Let's take a look! 👀

## 🤔 Why Migrate a Package That Already Builds Correctly?

is-kitis a zero-dependency TypeScript library for runtime type guards.

Its build setup was already pretty boring.

And boring build systems are good. 😸

The package had:

* one entry point
* ESM and CJS outputs
* bundled declaration files
* explicitpackage.jsonexports
* a declaration banner
* a packed-package smoke test

Before the migration, it used

Environment

Value

Package

is-kit@1.14.2

Bundler

tsup@8.5.1

Entry

src/index.ts

Output

ESM + CJS + bundled declarations

Target

esnext

I wasn't trying to solve a broken build.

The motivation was mostly maintenance.

tsdownis built around Rolldown, has an active ecosystem, and is explicitly designed as a migration path for projects currently usingtsup.

So the question wasn't

Cantsdownbuild this library?

It was

Can I move the build setup totsdownwithout changing what existing consumers receive?

That's a much more useful question for a published package.

## 📦 The Package Contract I Needed to Preserve

For an application, changing an output filename may not matter much.

For a library, it can be a breaking change.

is-kitalready exposes files through explicit package exports.

The important paths were effectively

{

 
"exports"
:
 
{

 
"."
:
 
{

 
"types"
:
 
"./dist/index.d.ts"
,

 
"import"
:
 
"./dist/index.mjs"
,

 
"require"
:
 
"./dist/index.js"

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

So I wanted the migration to preserve

dist/index.mjs
dist/index.js
dist/index.d.ts

Enter fullscreen mode

Exit fullscreen mode

along with the existing ESM/CJS runtime behavior, declaration compatibility, export set, and declaration banner.

In other words

The source code was not the contract here. The packed npm package was.

That distinction became important very quickly.

## 🛠️ The Migration Looked Almost Trivial

I replacedtsupwithtsdownand replaced

tsup.config.ts

Enter fullscreen mode

Exit fullscreen mode

with

tsdown.config.mts

Enter fullscreen mode

Exit fullscreen mode

I intentionally used.mts.

The package itself is not"type": "module", and using an ESM-specific config extension avoids having Node reinterpret the config file and emit related warnings.

Most of the important options mapped almost directly.

import
 
{
 
defineConfig
 
}
 
from
 
"
tsdown
"
;

export
 
default
 
defineConfig
({

 
entry
:
 
[
"
src/index.ts
"
],

 
format
:
 
[
"
esm
"
,
 
"
cjs
"
],

 
dts
:
 
true
,

 
clean
:
 
true
,

 
outDir
:
 
"
dist
"
,

 
target
:
 
"
esnext
"
,

 
banner
:
 
{

 
dts
:
 
dtsBanner
,

 
},

});

Enter fullscreen mode

Exit fullscreen mode

The declaration banner also stayed dts-only withbanner: { dts: dtsBanner }.

So far, everything looked easy.

Then I ran the build.

It passed.

And the package contract was wrong. 🙀

## 💥 The First Build Succeeded and Changed My Filenames

This was the interesting part.

Before the migration, the important generated files looked like this:

Build

Main generated files

tsup

index.mjs
, 
index.js
, 
index.d.ts

default 
tsdown
 migration

index.mjs
, 
index.cjs
, 
index.d.mts
, 
index.d.cts

Thetsdownbuild completed successfully with exit code0.

But my existingpackage.jsonstill expected

require → ./dist/index.js
types → ./dist/index.d.ts

Enter fullscreen mode

Exit fullscreen mode

Those files no longer matched the generated output.

If I had stopped at

pnpm build

Enter fullscreen mode

Exit fullscreen mode

and published the package.

CJS consumers and TypeScript resolution could have been broken.

This was the most important lesson from the migration

Build success ≠ package contract preserved.

A bundler only knows whether it successfully produced its output.

It doesn't automatically mean that output still matches every promise your already-published package makes.

## 🔧 Fixing the Public Contract withoutExtensions

Thetsdownmigration guideexplicitly calls out the rename fromoutExtensiontooutExtensions.

Foris-kit, I used it to preserve the existing filenames

outExtensions
:
 
({
 
format
 
})
 
=>
 
({

 
dts
:
 
format
 
===
 
'
cjs
'
 
?
 
'
.d.ts
'
 
:
 
'
.d.mts
'
,

 
js
:
 
format
 
===
 
'
cjs
'
 
?
 
'
.js
'
 
:
 
'
.mjs
'
,

}),

Enter fullscreen mode

Exit fullscreen mode

Now the relevant output became

dist/index.mjs
dist/index.js
dist/index.d.mts
dist/index.d.ts

Enter fullscreen mode

Exit fullscreen mode

and the existing exports continued to resolve correctly.

I don't really consider the original output behavior atsdownbug.

tsdownchooses extensions based on the package type and output format to avoid ambiguous module interpretation.

That's reasonable.

But for an existing package,reasonable new defaults are still changes.

If consumers already depend on your filenames, those filenames are part of your compatibility surface.

## 🧪 Verifying the Published Package with a Smoke Test

This is where an existingpacked-package smoke testinis-kithelped a lot.

I already had apnpm test:packagecommand that builds the package, runsnpm pack, installs the generated tarball into a temporary project, and verifies it from a real consumer's perspective.

Instead of testing this

src/index.ts

Enter fullscreen mode

Exit fullscreen mode

it tests this

is-kit-1.14.2.tgz
 ↓
temporary consumer
 ↓
npm install

Enter fullscreen mode

Exit fullscreen mode

A library can work perfectly inside its own repository while still publishing a broken package, so this smoke test exercises the artifact that users would actually install.

After the migration, I expanded the test to verify more of the package contract 👇

Contract

Result

exports["."].import
 → 
./dist/index.mjs

✅ pass

exports["."].require
 → 
./dist/index.js

✅ pass

exports["."].types
 → 
./dist/index.d.ts

✅ pass

Runtime dependencies

✅ 0

ESM exports

✅ same 83 exports

CJS exports

✅ same 83 exports

Declaration banner

✅ preserved

ESM runtime import

✅ pass

CJS runtime require

✅ pass

Packed TypeScript consumer

✅ pass

I also installed the packed package into temporary consumer projects using TypeScript v5.7 through v7.0.

All of them successfully resolved and consumed the generated declarations.

This isn't testing whether each TypeScript version can generate declarations throughtsdown. It's testing the artifact my users actually install.

So if a future build change accidentally alters an extension, export path, declaration file, or runtime behavior,the smoke test should catch it before publishing.

For a library migration like this, that is much more meaningful than simply asserting "build exited successfully".

## 📏 The Output Actually Got Bigger

I was also curious about artifact size.

This produced a result I didn't expect.

Metric

tsup

tsdown

Difference

JS + dts total

116,503 B

144,007 B

+23.6%

ESM JavaScript

15,787 B

29,410 B

+86.3%

CJS JavaScript

19,318 B

31,155 B

+61.3%

dts, one format

40,699 B

41,721 B

+2.5%

npm pack
 tarball

37,226 B

42,366 B

+13.8%

In this configuration, thetsdownoutput retained more comments and region markers than the previoustsupoutput.

So the raw JavaScript became noticeably larger.

Compression reduced the difference in the actualnpm tarball, but didn't remove it.

Foris-kit, this isn't particularly concerning.

It is a small zero-dependency utility library, and we're talking about a few kilobytes in the final tarball.

But it was still a useful reminder

A faster or newer bundler does not automatically mean a smaller artifact.

If package size is a strict constraint for your library, I would compare the generated files and decide on your minification strategy before migrating.

## ⏱️ What About Build Performance?

I also measured wall-clock build time.

The oldtsupbuild

1.50 s

Enter fullscreen mode

Exit fullscreen mode

The newtsdownbuild across three runs

1.22 s
1.17 s
1.18 s

Enter fullscreen mode

Exit fullscreen mode

Looking only at those numbers, it would be very tempting to say

tsdownmade the build faster! 🚀

But I don't think this benchmark supports that conclusion.

I only have one measuredtsuprun in this comparison.

Also, this is a tiny single-entry library where declaration generation represents a large part of the build.

The bundlers' own timing output was roughly

tsup
JavaScript: ~22 ms
dts: ~707 ms

tsdown
complete: ~717–755 ms

Enter fullscreen mode

Exit fullscreen mode

The wall-clock result was better, but with only onetsupsample and declaration generation dominating this tiny library, I don't think this is enough evidence to claim a meaningful performance improvement.

But no, I'm not migrating because I saved around 300 ms.

## 🐱 Was the Migration Actually Small?

Foris-kit, yes.

There were no source-code changes.

The migration was basically limited to

dependency
config
task documentation
package smoke assertions

Enter fullscreen mode

Exit fullscreen mode

The important options were almost one-to-one.

But I think it's important to explainwhyit stayed small.

is-kithas

* one entry
* zero runtime dependencies
* no bundler plugins
* no CSS pipeline
* no complicated code splitting

and, most importantly, it already had a way to test the packed package as a consumer.

The migration becomes more interesting if your package relies on custom plugins, unusual entries, CSS processing, exact source maps, generated exports, strict byte-size limits, or older Node build environments.

There is also a build-environment requirement worth checking.

For the version tested here

tsdown 0.23.0
Rolldown 1.2.8

Enter fullscreen mode

Exit fullscreen mode

the relevant Node engine requirement is

^22.18.0 || ^24.11.0 || >=26.0.0

Enter fullscreen mode

Exit fullscreen mode

My CI uses

Node 22.22.0

Enter fullscreen mode

Exit fullscreen mode

so that was fine.

But if contributors still build your library with Node v20 or an older Node v22 version, this is something you need to solve before migrating.

That doesn't necessarily mean yourlibrary consumersmust use Node v22.

It's a build-tool requirement.

Still, contributor and CI environments are part of the migration cost too. 😿

## 🎯 So, Was Moving from tsup to tsdown Worth It?

Foris-kit, I think yes.

But not because of performance.

The migration preserved the package contract across ESM, CJS, declarations, exports, and the packed-package consumer tests.

The configuration change was small and reviewable.

My existing Node environment satisfies the new build requirement.

And the build setup is now aligned with the actively evolving Rolldown ecosystem.

The cost was also real

* artifact size increased
* Node build requirements increased
* output extensions needed explicit configuration

So I wouldn't describe this as

Everyone using tsup should migrate immediately because tsdown is faster!

That's not what this experiment showed.

For me, the better conclusion is

If your project already meets the Node requirements and you want to move your build setup toward the Rolldown ecosystem, migrating a small library from tsup to tsdown can be a very reasonable change.

But verify the package you publish.

Not only the source.Not only the config.And definitely not only the green build message. 😸

Because the most interesting bug in this migration happened when the build said everything was fine.

If you'd like to see the package from this article in a real project,is-kitis open source.

It's a lightweight, zero-dependency TypeScript type guard library focused on runtime validation and safe narrowing.

If it looks useful for your project, I'd be happy if you gave it a try and a ⭐ on GitHub is always appreciated.

## nyaomaru/is-kit

### Build small guards. Compose them. A lightweight, zero-dependency toolkit for building reusable TypeScript type guards that compose, refine, and preserve natural narrowing. Runtime-safe 🛡️, composable 🧩, and ergonomic ✨.

# is-kit

## Build small guards. Compose them.

is-kitis a lightweight, zero-dependency toolkit for building reusable TypeScripttype guards.

is-kitis not just a collection ofisXhelpers. Its main focus is composing
small runtime checks into reusable guards while preserving useful TypeScript
narrowing.

It helps you write smallisFoofunctions, compose them intoricher runtime
checks, refine properties on values you already know about, and keepTypeScript narrowingnatural inside regular control flow. Use it at runtime
boundaries when needed, without requiring a schema-first workflow.

Runtime-safe🛡️,composable🧩, andergonomic✨ without asking you to adopt a heavy schema workflow.

* Build and reusetyped guards
* Compose guardswithand,or,not,oneOf
* UserefineKeyto narrow achild propertywhile preserving its parent type
* Validate objectshapes and collections when that is useful
* Parse or assertunknownvalues without a large schema framework

Best…

View on GitHub

Issues and PRs are welcome too. 😸

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (21 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse