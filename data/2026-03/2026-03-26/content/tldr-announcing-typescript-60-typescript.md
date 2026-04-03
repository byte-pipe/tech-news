---
title: Announcing TypeScript 6.0 - TypeScript
url: https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/
site_name: tldr
content_file: tldr-announcing-typescript-60-typescript
fetched_at: '2026-03-26T01:01:31.861695'
original_url: https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/
author: Daniel Rosenwasser
date: '2026-03-26'
published_date: '2026-03-23T16:34:10+00:00'
description: TypeScript 6.0 is now available! TypeScript 6 is a stepping-stone release, aligning with the upcoming native-speed 7.0 release.
tags:
- tldr
---

Daniel Rosenwasser

Principal Product Manager
 

Today we are excited to announce the availability of TypeScript 6.0!

If you are not familiar with TypeScript, it’s a language that builds on JavaScript by adding syntax for types, which enables type-checking to catch errors, and provide rich editor tooling.
You can learn more about TypeScript and how to get started on theTypeScript website.

But if you’re already familiar with the language, you can get TypeScript 6.0 through npm with the following command:

npm install -D typescript

TypeScript 6.0 is a unique release in that we intend for it to be the last release based on the current JavaScript codebase.As announced last year(withrecent updates here), we are working on a new codebase for the TypeScript compiler and language service written in Go that takes advantage of the speed of native code and shared-memory multi-threading.
That new codebase will be the foundation of TypeScript 7.0 and beyond.

TypeScript 6.0 acts as the bridge between TypeScript 5.9 and 7.0.
As such, most changes in TypeScript 6.0 are meant to help align and prepare for adopting TypeScript 7.0.
It may seem surprising to say, but TypeScript 7.0is actually extremely close to completion.
You cantry it out in Visual Studio Codeorinstall it from npm.
In fact, if you’re able to adopt TypeScript 6.0, we encourage you to try out the native previews of TypeScript 7.0.

With that said, there are some new features and improvements in TypeScript 6.0s that are not just about alignment.
Let’s take a look at some of the highlights of this release, followed by a more detailed look at what’s changing for 7.0 and how to prepare for it.

## What’s New Since the Beta and RC?

Since TypeScript 6.0 beta, we have made a few noteworthy changes – mostly to align with the behavior of TypeScript 7.0.

One adjustment is in type-checking for function expressions in generic calls, especially those occurring in generic JSX expressions (see this pull request).
This will typically catch more bugs in existing code, though you may find that some generic calls may need an explicit type argument.

We have also extended our deprecation of import assertion syntax (i.e.import ... assert {...})toimport()callslikeimport(..., { assert: {...}})

Finally, we have updated the DOM types to reflect the latest web standards, including some adjustments to the Temporal APIs as well.

## Less Context-Sensitivity onthis-less Functions

When parameters don’t have explicit types written out, TypeScript can usually infer them based on an expected type, or even through other arguments in the same function call.

declare function callIt<T>(obj: {
 produce: (x: number) => T,
 consume: (y: T) => void,
}): void;

// Works, no issues.
callIt({
 produce: (x: number) => x * 2,
 consume: y => y.toFixed(),
});

// Works, no issues even though the order of the properties is flipped.
callIt({
 consume: y => y.toFixed(),
 produce: (x: number) => x * 2,
});

Here, TypeScript can infer the type ofyin theconsumefunction based on the inferredTfrom theproducefunction, regardless of the order of the properties.
But what about if these functions were written usingmethod syntaxinstead of arrow function syntax?

declare function callIt<T>(obj: {
 produce: (x: number) => T,
 consume: (y: T) => void,
}): void;

// Works fine, `x` is inferred to be a number.
callIt({
 produce(x: number) { return x * 2; },
 consume(y) { return y.toFixed(); },
});

callIt({
 consume(y) { return y.toFixed(); },
 // ~
 // error: 'y' is of type 'unknown'.

 produce(x: number) { return x * 2; },
});

Strangely enough, the second call tocallItresults in an error because TypeScript is not able to infer the type ofyin theconsumemethod.
What’s happening here is that when TypeScript is trying to find candidates forT, it will first skip over functions whose parameters don’t have explicit types.
It does this because certain functions may need the inferred type ofTto be correctly checked – in our case, we need to know the type ofTto analyze ourconsumefunction.

These functions are calledcontextually sensitive functions– basically, functions that have parameters without explicit types.
Eventually the type system will need to figure out types for these parameters – but this is a bit at odds with how inference works in generic functions because the two "pull" on types in different directions.

function callFunc<T>(callback: (x: T) => void, value: T) {
 return callback(value);
}

callFunc(x => x.toFixed(), 42);
// ^
// We need to figure out the type of `x` here,
// but we also need to figure out the type of `T` to check the callback.

To solve this, TypeScript skips over contextually sensitive functions during type argument inference, and instead checks and infers from other arguments first.
If skipping over contextually sensitive functions doesn’t work, inference just continues across any unchecked arguments, going left-to-right in the argument list.
In the example immediately above, TypeScript will skip over the callback during inference forT, but will then look at the second argument,42, and infer thatTisnumber.
Then, when it comes back to check the callback, it will have a contextual type of(x: number) => void, which allows it to infer thatxis anumberas well.

So what’s going on in our earlier examples?

// Arrow syntax - no errors.
callIt({
 consume: y => y.toFixed(),
 produce: (x: number) => x * 2,
});

// Method syntax - errors!
callIt({
 consume(y) { return y.toFixed(); },
 // ~
 // error: 'y' is of type 'unknown'.

 produce(x: number) { return x * 2; },
});

In both examples,produceis assigned a function with an explicitly-typedxparameter.
Shouldn’t they be checked identically?

The issue is subtle: most functions (like the ones using method syntax) have an implicitthisparameter, but arrow functions do not.
Any usage ofthiscould require "pulling" on the type ofT– for example, knowing the type of the containing object literal could in turn require the type ofconsume, which usesT.

But we’re not usingthis!
Sure, the function might have athisvalue at runtime, but it’s never used!

TypeScript 6.0 takes this into account when it decides if a function is contextually sensitive or not.
Ifthisis never actuallyusedin a function, then it is not considered contextually sensitive.
That means these functions will be seen as higher-priority when it comes to type inference, and all of our examples above now work!

This change was providedthanks to the work ofMateusz Burzyński.

## Subpath Imports Starting with#/

When Node.js added support for modules, it added a feature called"subpath imports".
This is basicallya field calledimportswhich allows packages to create internal aliases for modules within their package.

{
 "name": "my-package",
 "type": "module",
 "imports": {
 "#root/*": "./dist/*"
 }
}

This allows modules inmy-packageto import from paths starting with#root/

import * as utils from "#root/utils.js";

instead of using a relative path like the following.

import * as utils from "../../utils.js";

One minor annoyance with this feature has been that developers always had to writesomethingafter the#when specifying a subpath import.
Here, we usedroot, but it is a bit useless since there is no directory we’re mapping over other than./dist/

Developers who have used bundlers are also accustomed to using path-mapping to avoid long relative paths.
A familiar convention with bundlers has been to use a simple@/as the prefix.
Unfortunately, subpath imports could not start with#/at all, leading to a lot of confusion for developers trying to adopt them in their projects.

But more recently,Node.js added support for subpath imports starting with#/.
This allows packages to use a simple#/prefix for their subpath imports without needing to add an extra segment.

{
 "name": "my-package",
 "type": "module",
 "imports": {
 "#/*": "./dist/*"
 }
}

This is supported in newer Node.js 20 releases, and so TypeScript now supports it under the optionsnodenextandbundlerfor the--moduleResolutionsetting.

This work was done thanks tomagic-akari, andthe implementing pull request can be found here.

## Combining--moduleResolution bundlerwith--module commonjs

TypeScript’s--moduleResolution bundlersetting was previously only allowed to be used with--module esnextor--module preserve;
however, with the deprecation of--moduleResolution node(a.k.a.--moduleResolution node10), this new combination is often the most suitable upgrade path for many projects.

Projects will often want to instead plan out a migration towards either

* --module preserveand--moduleResolution bundler
* --module nodenext

depending on your project type (e.g. bundled web app, Bun app, or Node.js app).

More information can be found atthis implementing pull request.

## The--stableTypeOrderingFlag

As part of our ongoing work onTypeScript’s native port, we’ve introduced a new flag called--stableTypeOrderingintended to assist with 6.0-to-7.0 migrations.

Today, TypeScript assigns type IDs (internal tracking numbers) to types in the order they are encountered, and uses these IDs to sort union types in a consistent manner.
A similar process occurs for properties.
As a result, the order in which things are declared in a program can have possibly surprising effects on things like declaration emit.

For example, consider the declaration emit from this file:

// Input: some-file.ts
export function foo(condition: boolean) {
 return condition ? 100 : 500;
}

// Output: some-file.d.ts
export declare function foo(condition: boolean): 100 | 500;
// ^^^^^^^^^
// Note the order of this union: 100, then 500.

If we add an unrelatedconstabovefoo, the declaration emit changes:

// Input: some-file.ts
const x = 500;
export function foo(condition: boolean) {
 return condition ? 100 : 500;
}

// Output: some-file.d.ts
export declare function foo(condition: boolean): 500 | 100;
// ^^^^^^^^^
// Note the change in order here.

This happens because the literal type500gets a lower type ID than100because it was processed first when analyzing theconst xdeclaration.
In very rare cases this change in ordering can even cause errors to appear or disappear based on program processing order, but in general, the main place you might notice this ordering is in the emitted declaration files, or in the way types are displayed in your editor.

One of the major architectural improvements in TypeScript 7 is parallel type checking, which dramatically improves overall check time.
However, parallelism introduces a challenge: when different type-checkers visit nodes, types, and symbols in different orders, the internal IDs assigned to these constructs become non-deterministic.
This in turn leads to confusing non-deterministic output, where two files with identical contents in the same program can produce different declaration files, or even calculate different errors when analyzing the same file.
To fix this, TypeScript 7.0 sorts its internal objects (e.g. types and symbols) according to a deterministic algorithm based on the content of the object.
This ensures that all checkers encounter the same object order regardless of how and when they were created.
As a consequence, in the given example, TypeScript 7 willalwaysprint100 | 500, removing the ordering instability entirely.

This means that TypeScript 6 and 7 can and do sometimes display different ordering.
While these ordering changes are almost always benign, if you’re comparing compiler outputs between runs (for example, checking emitted declaration files in 6.0 vs 7.0), these different orderings can produce a lot of noise that makes it difficult to assess correctness.
Occasionally though, you may witness a change in ordering that causes a type error to appear or disappear, which can be even more confusing.

To help with this situation, in 6.0, you can specify the new--stableTypeOrderingflag.
This makes 6.0’s type ordering behavior match 7.0’s, reducing the number of differences between the two codebases.
Note that we don’t necessarily encourage using this flag all the time as it can add a substantial slowdown to type-checking (up to 25% depending on codebase).

If you encounter a type error using--stableTypeOrdering, this is typically due to inference differences.
The previous inference without--stableTypeOrderinghappenedto work based on the current ordering of types in your program.
To help with this, you’ll often benefit from providing an explicit type somewhere.
Often, this will be a type argument

- someFunctionCall(/*...*/);
+ someFunctionCall<SomeExplicitType>(/*...*/);

or a variable annotation for an argument you intend to pass into a call.

- const someVariable = { /*... some complex object ...*/ };
+ const someVariable: SomeExplicitType = { /*... some complex object ...*/ };

someFunctionCall(someVariable);

Note that this flag is only intended to help diagnose differences between 6.0 and 7.0 – it is not intended to be used as a long-term feature

See more at this pull-request.

## es2025option fortargetandlib

TypeScript 6.0 adds support for thees2025option for bothtargetandlib.
While there are no new JavaScript language features in ES2025, this new target adds new types for built-in APIs (e.g.RegExp.escape), and moves a few declarations fromesnextintoes2025(e.g.Promise.try,Iteratormethods, andSetmethods).
Work to enablethe new targetwas contributed thanks toKenta Moriuchi.

## New Types forTemporal

The long-awaitedTemporal proposalhas reached stage 4 and will be part of a future ECMAScript standard.
TypeScript 6.0 now includes built-in types for the Temporal API, so you can start using it in your TypeScript code today via--target esnextor"lib": ["esnext"](or the more-granularesnext.temporal).

let yesterday = Temporal.Now.instant().subtract({
 hours: 24,
});

let tomorrow = Temporal.Now.instant().add({
 hours: 24,
});

console.log(`Yesterday: ${yesterday}`);
console.log(`Tomorrow: ${tomorrow}`);

Temporal is already usable in several runtimes, and with stage 4 status it is now officially part of the JavaScript language.Documentation on the Temporal APIs is available on MDN.

This workwas contributed thanks to GitHub userRenegade334.

## New Types for "upsert" Methods (a.k.a.getOrInsert)

A common pattern withMaps is to check if a key exists, and if not, set and fetch a default value.

function processOptions(compilerOptions: Map<string, unknown>) {
 let strictValue: unknown;
 if (compilerOptions.has("strict")) {
 strictValue = compilerOptions.get("strict");
 }
 else {
 strictValue = true;
 compilerOptions.set("strict", strictValue);
 }
 // ...
}

This pattern can be tedious.ECMAScript’s "upsert" proposalrecently reached stage 4, and introduces 2 new methods onMapandWeakMap:

* getOrInsert
* getOrInsertComputed

These methods have been added to theesnextlib so that you can start using them immediately in TypeScript 6.0.

WithgetOrInsert, we can replace our code above with the following:

function processOptions(compilerOptions: Map<string, unknown>) {
 let strictValue = compilerOptions.getOrInsert("strict", true);
 // ...
}

getOrInsertComputedworks similarly, but is for cases where the default value may be expensive to compute (e.g. requires lots of computations, allocations, or does long-running synchronous I/O).
Instead, it takes a callback that will only be called if the key is not already present.

someMap.getOrInsertComputed("someKey", () => {
 return computeSomeExpensiveValue(/*...*/);
});

This callback is also given the key as an argument, which can be useful for cases where the default value is based on the key.

someMap.getOrInsertComputed(someKey, computeSomeExpensiveDefaultValue);

function computeSomeExpensiveValue(key: string) {
 // ...
}

This updatewas contributed thanks to GitHub userRenegade334.

## RegExp.escape

When constructing some literal string to match within a regular expression, it is important to escape special regular expression characters like*,+,?,(,), etc.
TheRegExp Escaping ECMAScript proposalhas reached stage 4, and introduces a newRegExp.escapefunction that takes care of this for you.

function matchWholeWord(word: string, text: string) {
 const escapedWord = RegExp.escape(word);
 const regex = new RegExp(`\\b${escapedWord}\\b`, "g");
 return text.match(regex);
}

RegExp.escapeis available in thees2025lib, so you can start using it in TypeScript 6.0 today.

This workwas contributed thanksKenta Moriuchi.

## Thedomlib Now Containsdom.iterableanddom.asynciterable

TypeScript’sliboption allows you to specify which global declarations your target runtime has.
One option isdomto represent web environments (i.e. browsers, who implementthe DOM APIs).
Previously, the DOM APIs were partially split out intodom.iterableanddom.asynciterablefor environments that didn’t supportIterables andAsyncIterables.
This meant that you had to explicitly adddom.iterableto use iteration methods on DOM collections likeNodeListorHTMLCollection.

In TypeScript 6.0, the contents oflib.dom.iterable.d.tsandlib.dom.asynciterable.d.tsare fully included inlib.dom.d.ts.
You can still referencedom.iterableanddom.asynciterablein your configuration file’s"lib"array, but they are now just empty files.

// Before TypeScript 6.0, this required "lib": ["dom", "dom.iterable"]
// Now it works with just "lib": ["dom"]
for (const element of document.querySelectorAll("div")) {
 console.log(element.textContent);
}

This is a quality-of-life improvement that eliminates a common point of confusion, since no major modern browser lacks these capabilities.
If you were already including bothdomanddom.iterable, you can now simplify to justdom.

See moreat this issueand itscorresponding pull request.

## Breaking Changes and Deprecations in TypeScript 6.0

TypeScript 6.0 arrives as a significant transition release, designed to prepare developers for TypeScript 7.0, the upcoming native port of the TypeScript compiler.
While TypeScript 6.0 maintains full compatibility with your existing TypeScript knowledge and continues to be API compatible with TypeScript 5.9, this release introduces a number of breaking changes and deprecations that reflect the evolving JavaScript ecosystem and set the stage for TypeScript 7.0.

In the two years since TypeScript 5.0, we’ve seen ongoing shifts in how developers write and ship JavaScript:

* Virtually every runtime environment is now "evergreen". True legacy environments (ES5) are vanishingly rare.
* Bundlers and ESM have become the most common module targets for new projects, though CommonJS remains a major target. AMD and other in-browser userland module systems are much rarer than they were in 2012.
* Almost all packages can be consumed through some module system. UMD packages still exist, but virtually no new code is availableonlyas a global variable.
* tsconfig.jsonis nearly universal as a configuration mechanism.
* Appetite for "stricter" typing continues to grow.
* TypeScript build performance is top of mind. Despite the gains of TypeScript 7, performance must always remain a key goal, and options which can’t be supported in a performant way need to be more strongly justified.

So TypeScript 6.0 and 7.0 are designed with these realities in mind.
For TypeScript 6.0, these deprecations can be ignored by setting"ignoreDeprecations": "6.0"in your tsconfig; however, note that TypeScript 7.0will notsupport any of these deprecated options.

Some necessary adjustments can be automatically performed with a codemod or tool.
For example, theexperimentalts5to6toolcan automatically adjustbaseUrlandrootDiracross your codebase.

### Up-Front Adjustments

We’ll cover specific adjustments below, but we have to note that some deprecations and behavior changes do not necessarily have an error message that directly points to the underlying issue.
So we’ll note up-front thatmany projects will need to do at least one of the following:

* Set the"types"array in tsconfig, typically to"types": ["node"]."types": ["*"]will restore the 5.9 behavior, but we recommend using an explicit array to improve build performance and predictability.You’ll typically know this is the issue if you see alotof type errors related to missing identifiers or unresolved built-in modules.
* Set"rootDir": "./src"if you were previously relying on this being inferredYou’ll often know this is the issue if you see files being written to./dist/src/index.jsinstead of./dist/index.js.

### Simple Default Changes

Several compiler options now have updated default values that better reflect modern development practices.

* strictis nowtrueby default:
The appetite for stricter typing continues to grow, and we’ve found that most new projects wantstrictmode enabled.
If you were already using"strict": true, nothing changes for you.
If you were relying on the previous default offalse, you’ll need to explicitly set"strict": falsein yourtsconfig.json.
* moduledefaults toesnext:
Similarly, the new defaultmoduleisesnext, acknowledging that ESM is now the dominant module format.
* targetdefaults to current-year ES version:
The new defaulttargetis the most recent supported ECMAScript spec version (effectively a floating target).
Right now, that target ises2025.
This reflects the reality that most developers are shipping to evergreen runtimes and don’t need to transpile down to older ECMAScript versions.
* noUncheckedSideEffectImportsis nowtrueby default:
This helps catch issues with typos in side-effect-only imports.
* libReplacementis nowfalseby default:
This flag previously incurred a large number of failed module resolutions for every run, which in turn increased the number of locations we needed to watch under--watchand editor scenarios.
In a new project,libReplacementnever does anything until other explicit configuration takes place, so it makes sense to turn this off by default for the sake of better performance by default.

If these new defaults break your project, you can specify the previous values explicitly in yourtsconfig.json.

### rootDirnow defaults to.

rootDircontrols the directory structure of your output files relative to the output directory.
Previously, if you did not specify arootDir, it was inferred based on the common directory of all non-declaration input files.
But this often meant that it was impossible to know if a file belonged to a project without trying to load and parse that project.
It also meant that TypeScript had to spend more time inferring that common source directory by analyzing every file path in the program.

In TypeScript 6.0, the defaultrootDirwill always be the directory containing thetsconfig.jsonfile.rootDirwill only be inferred when usingtscfrom the command line without atsconfig.jsonfile.

If you have source files any level deeper than yourtsconfig.jsondirectory and were relying on TypeScript to infer a common root directory for source files, you’ll need to explicitly setrootDir:

 {
 "compilerOptions": {
 // ...
+ "rootDir": "./src"
 },
 "include": ["./src"]
 }

Likewise, if yourtsconfig.jsonreferenced files outside of the containingtsconfig.json, you would need to adjust yourrootDirto include those files.

 {
 "compilerOptions": {
 // ...
+ "rootDir": "../src"
 },
 "include": ["../src/**/*.tests.ts"]
 }

See more atthe discussion hereandthe implementation here.

### typesnow defaults to[]

In atsconfig.json, thetypesfield ofcompilerOptionsspecifies a list of package names to be included in the global scope during compilation.
Typically, packages innode_modulesare automatically included via imports in your source code;
but for convenience, TypeScript would also include all packages innode_modules/@typesby default, so that you can get global declarations likeprocessor the"fs"module from@types/node, ordescribeanditfrom@types/jest, without needing to import them directly.

In a sense, thetypesvalue previously defaulted to "enumerate everything innode_modules/@types".
This can beveryexpensive, as a normal repository setup these days might transitively pull in hundreds of@typespackages, especially in multi-project workspaces with flattenednode_modules.
Modern projects almost always need only@types/node,@types/jest, or a handful of other common global-affecting packages.

In TypeScript 6.0, the defaulttypesvalue will be[](an empty array).
This change prevents projects from unintentionally pulling in hundreds or even thousands of unneeded declaration files at build time.
Many projects we’ve looked at have improved their build time anywhere from 20-50% just by settingtypesappropriately.

This will affect many projects.You will likely need to add"types": ["node"]or a few others:

 {
 "compilerOptions": {
 // Explicitly list the @types packages you need
+ "types": ["node", "jest"]
 }
 }

You can also specify a*entry to re-enable the old enumeration behavior:

 {
 "compilerOptions": {
 // Load ALL the types - the default from TypeScript 5.9 and before.
+ "types": ["*"]
 }
 }

If you end up with new error messages like the following:

Cannot find module '...' or its corresponding type declarations.
Cannot find name 'fs'. Do you need to install type definitions for node? Try `npm i --save-dev @types/node` and then add 'node' to the types field in your tsconfig.
Cannot find name 'path'. Do you need to install type definitions for node? Try `npm i --save-dev @types/node` and then add 'node' to the types field in your tsconfig.
Cannot find name 'process'. Do you need to install type definitions for node? Try `npm i --save-dev @types/node` and then add 'node' to the types field in your tsconfig.
Cannot find name 'Bun'. Do you need to install type definitions for Bun? Try `npm i --save-dev @types/bun` and then add 'bun' to the types field in your tsconfig.
Cannot find name 'describe'. Do you need to install type definitions for a test runner? Try `npm i --save-dev @types/jest` or `npm i --save-dev @types/mocha` and then add 'jest' or 'mocha' to the types field in your tsconfig.

it’s likely that you need to add some entries to yourtypesfield.

See more atthe proposal herealong withthe implementing pull request here.

### Deprecated:target: es5

The ECMAScript 5 target was important for a long time to support legacy browsers; but its successor, ECMAScript 2015 (ES6), was released over a decade ago, and all modern browsers have supported it for many years.
With Internet Explorer’s retirement, and the universality of evergreen browsers, there are very few use cases for ES5 output today.

TypeScript’s lowest target will now be ES2015, and thetarget: es5option is deprecated. If you were usingtarget: es5, you’ll need to migrate to a newer target or use an external compiler.
If you still need ES5 output, we recommend using an external compiler to either directly compile your TypeScript source, or to post-process TypeScript’s outputs.

See more about this deprecation herealong withits implementing pull request.

### Deprecated:--downlevelIteration

--downlevelIterationonly has effects on ES5 emit, and since--target es5has been deprecated,--downlevelIterationno longer serves a purpose.

Subtly, using--downlevelIteration falsewith--target es2015did not error in TypeScript 5.9 and earlier, even though it had no effect.
In TypeScript 6.0, setting--downlevelIterationat all will lead to a deprecation error.

Seethe implementation here.

### Deprecated:--moduleResolution node(a.k.a.--moduleResolution node10)

--moduleResolution nodeencoded a specific version of Node.js’s module resolution algorithm that most-accurately reflected the behavior of Node.js 10.
Unfortunately, this target (and its name) ignores many updates to Node.js’s resolution algorithm that have occurred since then, and it is no longer a good representation of the behavior of modern Node.js versions.

In TypeScript 6.0,--moduleResolution node(specifically,--moduleResolution node10) is deprecated.
Users who were using--moduleResolution nodeshould usually migrate to--moduleResolution nodenextif they plan on targeting Node.js directly, or--moduleResolution bundlerif they plan on using a bundler or Bun.

See moreat this issueandits corresponding pull request.

### Deprecated:amd,umd, andsystemjsvalues ofmodule

The following flag values are no longer supported

* --module amd
* --module umd
* --module systemjs
* --module none

AMD, UMD, and SystemJS were important during the early days of JavaScript modules when browsers lacked native module support.
The semantics of "none" were never well-defined and often led to confusion.
Today, ESM is universally supported in browsers and Node.js, and both import maps and bundlers have become favored ways for filling in the gaps.
If you’re still targeting these module systems, consider migrating to an appropriate ECMAScript module-emitting target, adopt a bundler or different compiler, or stay on TypeScript 5.x until you can migrate.

This also implies dropped support for theamd-moduledirective, which will no longer have any effect.

See more atthe proposal issuealong withthe implementing pull request.

### Deprecated:--baseUrl

ThebaseUrloption is most-commonly used in conjunction withpaths, and is typically used as a prefix for every value inpaths.
Unfortunately,baseUrlis also considered a look-up root for module resolution.

For example, given the followingtsconfig.json

{
 "compilerOptions": {
 // ...
 "baseUrl": "./src",
 "paths": {
 "@app/*": ["app/*"],
 "@lib/*": ["lib/*"]
 }
 }
}

and an import like

import * as someModule from "someModule.js";

TypeScript will probably resolve this tosrc/someModule.js, even if the developer only intended to add mappings for modules starting with@app/and@lib/.

In the best case, this also often leads to "worse-looking" paths that bundlers would ignore;
but it often meant that that many import paths that would never have worked at runtime are considered "just fine" by TypeScript.

pathmappings have not required specifyingbaseUrlfor a long time, and in practice, most projects that usebaseUrlonly use it as a prefix for theirpathsentries.
In TypeScript 6.0,baseUrlis deprecated and will no longer be considered a look-up root for module resolution.

Developers who usedbaseUrlas a prefix for path-mapping entries can simply removebaseUrland add the prefix to theirpathsentries:

 {
 "compilerOptions": {
 // ...
- "baseUrl": "./src",
 "paths": {
- "@app/*": ["app/*"],
- "@lib/*": ["lib/*"]
+ "@app/*": ["./src/app/*"],
+ "@lib/*": ["./src/lib/*"]
 }
 }
 }

Developers who actuallydidusebaseUrlas a look-up root can also add an explicit path mapping to preserve the old behavior:

{
 "compilerOptions": {
 // ...
 "paths": {
 // A new catch-all that replaces the baseUrl:
 "*": ["./src/*"],

 // Every other path now has an explicit common prefix:
 "@app/*": ["./src/app/*"],
 "@lib/*": ["./src/lib/*"],
 }
 }
}

However, this is extremely rare.
We recommend most developers simply removebaseUrland add the appropriate prefixes to theirpathsentries.

See moreat this issueandthe corresponding pull request.

### Deprecated:--moduleResolution classic

ThemoduleResolution: classicsetting has been removed.
Theclassicresolution strategy was TypeScript’s original module resolution algorithm, and predates Node.js’s resolution algorithm becoming a de facto standard.
Today, all practical use cases are served bynodenextorbundler.
If you were usingclassic, migrate to one of these modern resolution strategies.

See more atthis issueandthe implementing pull request.

### Deprecated:--esModuleInterop falseand--allowSyntheticDefaultImports false

The following settings can no longer be set tofalse:

* esModuleInterop
* allowSyntheticDefaultImports

esModuleInteropandallowSyntheticDefaultImportswere originally opt-in to avoid breaking existing projects.
However, the behavior they enable has been the recommended default for years.
Setting them tofalseoften led to subtle runtime issues when consuming CommonJS modules from ESM.
In TypeScript 6.0, the safer interop behavior is always enabled.

If you have imports that rely on the old behavior, you may need to adjust them:

// Before (with esModuleInterop: false)
import * as express from "express";

// After (with esModuleInterop always enabled)
import express from "express";

See more atthis issueandits implementing pull request.

### Deprecated:--alwaysStrict false

ThealwaysStrictflag refers to inference and emit of the"use strict";directive.
In TypeScript 6.0, all code will be assumed to be inJavaScript strict mode, which is a set of JS semantics that most-noticeably affects syntactic corner cases around reserved words.
If you have "sloppy mode" code that uses reserved words likeawait,static,private, orpublicas regular identifiers, you’ll need to rename them.
If you relied on subtle semantics around the meaning ofthisin non-strict code, you may need to adjust your code as well.

See moreat this issueandits corresponding pull request.

### Deprecated:outFile

The--outFileoption has been removed from TypeScript 6.0. This option was originally designed to concatenate multiple input files into a single output file. However, external bundlers like Webpack, Rollup, esbuild, Vite, Parcel, and others now do this job faster, better, and with far more configurability. Removing this option simplifies the implementation and allows us to focus on what TypeScript does best: type-checking and declaration emit. If you’re currently using--outFile, you’ll need to migrate to an external bundler. Most modern bundlers have excellent TypeScript support out of the box.

### Deprecated: legacymoduleSyntax for namespaces

Early versions of TypeScript used themodulekeyword to declare namespaces:

// ❌ Deprecated syntax - now an error
module Foo {
 export const bar = 10;
}

This syntax was later aliased to the modern preferred form using thenamespacekeyword:

// ✅ The correct syntax
namespace Foo {
 export const bar = 10;
}

Whennamespacewas introduced, themodulesyntax was simply discouraged.
A few years ago, the TypeScript language service started marking the keyword as deprecated, suggestingnamespacein its place.

In TypeScript 6.0, usingmodulewherenamespaceis expected is now a hard deprecation.
This change is necessary becausemoduleblocks are a potential ECMAScript proposal that would conflict with the legacy TypeScript syntax.

The ambient module declaration form remains fully supported:

// ✅ Still works perfectly
declare module "some-module" {
 export function doSomething(): void;
}

Seethis issueand itscorresponding pull requestfor more details.

### Deprecated:assertsKeyword on Imports

Theassertskeyword was proposed to the JavaScript language via the import assertions proposal;
however, the proposal eventually morphed intothe import attributes proposal, which uses thewithkeyword instead ofasserts.

Thus, theassertssyntax is now deprecated in TypeScript 6.0, and using it will lead to an error:

// ❌ Deprecated syntax - now an error.
import blob from "./blahb.json" asserts { type: "json" }
// ~~~~~~~
// error: Import assertions have been replaced by import attributes. Use 'with' instead of 'asserts'.

Instead, use thewithsyntax for import attributes:

// ✅ Works with the new import attributes syntax.
import blob from "./blahb.json" with { type: "json" }

See more atthis issueand itscorresponding pull request.

### Deprecated:no-default-libDirectives

The/// <reference no-default-lib="true"/>directive has been largely misunderstood and misused.
In TypeScript 6.0, this directive is no longer supported.
If you were using it, consider using--noLibor--libReplacementinstead.

See more hereand atthe corresponding pull request.

### Specifying Command-Line Files Whentsconfig.jsonExists is Now an Error

Currently, if you runtsc foo.tsin a folder where atsconfig.jsonexists, the config file is completely ignored.
This was often very confusing if you expected checking and emit options to apply to the input file.

In TypeScript 6.0, if you runtscwith file arguments in a directory containing atsconfig.json, an error will be issued to make this behavior explicit:

error TS5112: tsconfig.json is present but will not be loaded if files are specified on commandline. Use '--ignoreConfig' to skip this error.

If it is the case that you wanted to ignore thetsconfig.jsonand just compilefoo.tswith TypeScript’s defaults, you can use the new--ignoreConfigflag.

tsc --ignoreConfig foo.ts

See moreat this issueand itscorresponding pull request.

## Preparing for TypeScript 7.0

TypeScript 6.0 is designed as a transition release.
While options deprecated in TypeScript 6.0 will continue to work without errors when"ignoreDeprecations": "6.0"is set, those options will beremoved entirely in TypeScript 7.0(the native TypeScript port).
If you’re seeing deprecation warnings after upgrading to TypeScript 6.0, we strongly recommend addressing them before adopting TypeScript 7.0 (or tryingnative previews) in your project.

## What’s Next?

Now that TypeScript 6.0 is available on npm, the team will be focused on bringing TypeScript 7.0 to stability.
This is much closer than it might sound: we expect a release within a few months, and we are already seeing broad adoption inside and outside of Microsoft on extremely large codebases.
So we encourage teams to try out nightly builds of TypeScript 7.0’snative previews on npmalong with theVS Code extension too.
Feedback on TypeScript 7.0 will go a long way, and you can file issueson our issue tracker.

Still, TypeScript 6.0 is a stable release that you should be able to adopt today, and it includes a number of improvements and new features that you can start using right away.
We hope this release will be a smooth transition for everyone, and we look forward to hearing about your experiences with it.

Happy Hacking!

– Daniel Rosenwasser and the TypeScript Team

Category
TypeScript

Share

 

## Author

Daniel Rosenwasser
Principal Product Manager

Daniel Rosenwasser is the product manager of the TypeScript team. He has a passion for programming languages, compilers, and great developer tooling.

 

 

## Read next

March 6, 2026

### Announcing TypeScript 6.0 RC

Daniel Rosenwasser

February 11, 2026

### Announcing TypeScript 6.0 Beta

Daniel Rosenwasser

 

## Stay informed

Get notified when new posts are published.

Email 
*

 

Country/Region 
*

Select...
United States
Afghanistan
Åland Islands
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antarctica
Antigua and Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bonaire
Bosnia and Herzegovina
Botswana
Bouvet Island
Brazil
British Indian Ocean Territory
British Virgin Islands
Brunei
Bulgaria
Burkina Faso
Burundi
Cabo Verde
Cambodia
Cameroon
Canada
Cayman Islands
Central African Republic
Chad
Chile
China
Christmas Island
Cocos (Keeling) Islands
Colombia
Comoros
Congo
Congo (DRC)
Cook Islands
Costa Rica
Côte dIvoire
Croatia
Curaçao
Cyprus
Czechia
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Eswatini
Ethiopia
Falkland Islands
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
French Southern Territories
Gabon
Gambia
Georgia
Germany
Ghana
Gibraltar
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Heard Island and McDonald Islands
Honduras
Hong Kong SAR
Hungary
Iceland
India
Indonesia
Iraq
Ireland
Isle of Man
Israel
Italy
Jamaica
Jan Mayen
Japan
Jersey
Jordan
Kazakhstan
Kenya
Kiribati
Korea
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macau SAR
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
North Macedonia
Northern Mariana Islands
Norway
Oman
Pakistan
Palau
Palestinian Authority
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Pitcairn Islands
Poland
Portugal
Puerto Rico
Qatar
Réunion
Romania
Rwanda
Saba
Saint Barthélemy
Saint Kitts and Nevis
Saint Lucia
Saint Martin
Saint Pierre and Miquelon
Saint Vincent and the Grenadines
Samoa
San Marino
São Tomé and Príncipe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Eustatius
Sint Maarten
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Georgia and South Sandwich Islands
South Sudan
Spain
Sri Lanka
St Helena
Ascension
Tristan da Cunha
Suriname
Svalbard
Sweden
Switzerland
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tokelau
Tonga
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Turks and Caicos Islands
Tuvalu
U.S. Outlying Islands
U.S. Virgin Islands
Uganda
Ukraine
United Arab Emirates
United Kingdom
Uruguay
Uzbekistan
Vanuatu
Vatican City
Venezuela
Vietnam
Wallis and Futuna
Yemen
Zambia
Zimbabwe

I would like to receive the TypeScript Newsletter. 
Privacy Statement.

Subscribe

 

Follow this blog

 

Are you sure you wish to delete this
 comment?

OK

Cancel