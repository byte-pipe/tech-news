---
title: How to make Firefox builds1 17% faster2 | farre’s blog
url: https://blog.farre.se/posts/2026/04/10/caching-webidl-codegen/
site_name: hnrss
content_file: hnrss-how-to-make-firefox-builds1-17-faster2-farres-blog
fetched_at: '2026-04-14T11:57:27.143589'
original_url: https://blog.farre.se/posts/2026/04/10/caching-webidl-codegen/
author: Andreas Farre
date: '2026-04-13'
published_date: '2026-04-10T00:00:00+00:00'
description: In the previous post, I mentioned that buildcache has some unique properties compared to ccache and sccache. One of them is its Lua plugin system, which lets you write custom wrappers for programs that aren’t compilers in the traditional sense. With Bug 2027655 now merged, we can use this to cache Firefox’s WebIDL binding code generation.
tags:
- hackernews
- hnrss
---

In theprevious post, I mentioned that buildcache has some unique properties compared to ccache and sccache. One of them is itsLua plugin system, which lets you write custom wrappers for programs that aren’t compilers in the traditional sense. WithBug 2027655now merged, we can use this to cache Firefox’s WebIDL binding code generation.

## What’s the WebIDL step?

When you build Firefox, one of the earlier steps runspython3 -m mozbuild.action.webidlto generate C++ binding code from hundreds of.webidlfiles. It produces thousands of output files: headers, cpp files, forward declarations, event implementations, and so on. The step isn’t terribly slow on its own, but it runs on every clobber build, and the output is entirely deterministic given the same inputs. That makes it a perfect candidate for caching.

The problem was that the compiler cache was never passed to this step. Buildcache was only wrapping actual compiler invocations, not the Python codegen.

## The change

The fix inBug 2027655is small. Indom/bindings/Makefile.in, we now conditionally pass$(CCACHE)as a command wrapper to thepy_actioncall:

WEBIDL_CCACHE
=

ifdef
 
MOZ_USING_BUILDCACHE

WEBIDL_CCACHE
=
$(
CCACHE
)

endif

webidl.stub
:
 
$(codegen_dependencies)

	
$(
call py_action,webidl 
$(
relativesrcdir
)
,
$(
srcdir
)
,,
$(
WEBIDL_CCACHE
))

	
@$(
TOUCH
)
 
$@

Thepy_actionmacro inconfig/makefiles/functions.mkis what runs Python build actions. The ability to pass a command wrapper as a fourth argument was also introduced in this bug. When buildcache is configured as the compiler cache, this means the webidl action is invoked asbuildcache python3 -m mozbuild.action.webidl ...instead of justpython3 -m mozbuild.action.webidl .... That’s all buildcache needs to intercept it.

Note theifdef MOZ_USING_BUILDCACHEguard. This is specific to buildcache because ccache and sccache don’t have a mechanism for caching arbitrary commands. Buildcache does, through its Lua wrappers.

## The Lua wrapper

Buildcache’s Lua plugin system lets you write a script that tells it how to handle a program it doesn’t natively understand. The wrapper for WebIDL codegen,webidl.lua, needs to answer a few questions for buildcache:

* Can I handle this command?Match onmozbuild.action.webidlin the argument list.
* What are the inputs?All the.webidlsource files, plus the Python codegen scripts. These come fromfile-lists.json(whichmachgenerates) andcodegen.json(which tracks the Python dependencies from the previous run).
* What are the outputs?All the generated binding headers, cpp files, event files, and the codegen state files. Again derived fromfile-lists.json.

With that information, buildcache can hash the inputs, check the cache, and either replay the cached outputs or run the real command and store the results.

The wrapper uses buildcache’sdirect_modecapability, meaning it hashes input files directly rather than relying on preprocessed output. This is the right approach here since we’re not dealing with a C preprocessor but with a Python script that reads.webidlfiles.

## Numbers

Here are build times for./mach buildon Linux, comparing compiler cachers. Each row shows a clobber build with an empty cache (cold), followed by a clobber build with a filled cache (warm):

tool

cold

warm

with plugin

none

5m35s

n/a

n/a

ccache

5m42s

3m21s

n/a

sccache

9m38s

2m49s

n/a

buildcache

5m43s

1m27s

1m12s

The “with plugin” column is buildcache with thewebidl.luawrapper active. It shaves another 15 seconds1, bringing the total down to 1m12s2. Not a revolutionary improvement on its own, but it demonstrates the mechanism. The WebIDL step is just the first Python action to get this treatment; there are other codegen steps in the build that could benefit from the same approach.

More broadly, these numbers show buildcache pulling well ahead on warm builds. Going from a 5m35s clean build to a 1m12s cached rebuild is a nice improvement to the edit-compile-test cycle.

These are single runs on one machine, not rigorous benchmarks, but the direction is clear enough.

## Setting it up

If you’re already using buildcache withmach, the Makefile change is available when updating to today’s central. To enable the Lua wrapper, clone thebuildcache-wrappersrepo and point buildcache at it vialua_pathsin~/.buildcache/config.json:

{

"lua_paths"
:
 
[
"/path/to/buildcache-wrappers/mozilla"
],

"max_cache_size"
:
 
10737418240
,

"max_local_entry_size"
:
 
2684354560

}

Alternatively, you can set theBUILDCACHE_LUA_PATHenvironment variable. A convenient place to do that is in your mozconfig:

mk_add_options 
"export BUILDCACHE_LUA_PATH=/path/to/buildcache-wrappers/mozilla/"

The largemax_local_entry_size(2.5 GB) is needed because some Rust crates produce very large cache entries.

## What’s next

The Lua plugin system is the interesting part here. The WebIDL wrapper is a proof of concept, but the same technique applies to any deterministic build step that takes known inputs and produces known outputs. There are other codegen actions in the Firefox build that could get the same treatment, and I plan to explore those next.

#### Notes

1. For a clobber build with a warm cache↩
2. On my machine↩