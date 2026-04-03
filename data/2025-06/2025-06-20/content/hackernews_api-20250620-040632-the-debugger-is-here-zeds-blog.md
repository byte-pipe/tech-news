---
title: The Debugger is Here — Zed's Blog
url: https://zed.dev/blog/debugger
site_name: hackernews_api
fetched_at: '2025-06-20T04:06:32.064666'
original_url: https://zed.dev/blog/debugger
author: SupremumLimit
date: '2025-06-19'
published_date: 06/18/2025
description: 'From the Zed Blog: Over 2,000 developers asked, and we delivered. Debugging in Zed is now a reality—and it''s a big leap toward Zed 1.0.'
tags:
- hackernews
- trending
---

← Back to Blog

# The Debugger is Here

Over 2,000 developers asked, and we delivered.

Debugging in Zed is now a reality—and it's a big leap toward Zed 1.0.

## Overview

We set out to build a debugger with three primary focuses:

* Fast: Spend less time context switching and more time debugging
* Familiar: In line with Zed's design language and supports everything expected from a typical debugger flow
* Configurable: You're able to customize the UI, keybindings, debug configurations and more

Out of the box, Zed supports debugging popular languages including Rust, C/C++, JavaScript, Go, and Python.
With our extension system, Zed can support any debug adapter that implements theDebug Adapter Protocol (DAP).

To simplify the setup process, we've introduced locators, a system that translates build configurations into debug configurations. Meaning that you can write a build task once intasks.jsonand reference it fromdebug.json— or, even better, rely on Zed's automatic configuration.

Zed automatically runs locators on built-in or language server-generated runnables, so in many cases you won't even need to write a debug configuration to get up and running.

We currently support locators for Cargo, Python, JavaScript, and Go, with more coming in the future.
For more information on configuring a debug session,see our documentation.

Once in a debug session, Zed makes it easy to inspect your program's state, such as threads, variables, breakpoints, the call stack, and more.

Setting some breakpoints and running the test in a debug session.

The debugger panel is fully customizable too, just drag and rearrange tabs in whatever order you want; you can even move the debug panel around so it fits your workflow.

Zed also supports keyboard-driven debugging for users that prefer to keep their hands on the keyboard.
You can step through code, toggle breakpoints, and navigate a debug session without ever touching the mouse.

Navigating through the Debugger surfaces using only the keyboard.

## A Special Thanks

The debugger started as a community-led project with some impressive stats:8 months of development, 977 commits, and 25k+ lines of code. The community built the core foundation that made today’s launch possible.

Special thanks toRemco Smitsfor driving a lot of the heavy lifting on this project—your contributions have been critical to getting us here.

## Under the Hood

Zed's debugger supports debugging a variety of languages through the Debug Adapter Protocol.
But simply implementing the protocol wasn't enough—we needed an architecture that could scale to collaborative debugging, support extensions, and efficiently cache and manage responses from debug adapters.

To achieve this, we built a two-layer architecture: a data layer that communicates directly with the debug adapters, and a UI layer that fetches data from the data layer to render the interface.

/// All functions are cheap to call, as they grab current state of the debug session and schedule refreshing on a background

/// thread if that state is outdated.

pub
 fn
 modules
(&
mut
 self
,
cx
: &
mut
 Context
<
Self
>) -> &[
Module
] {

 /// Kick off a fresh request to a DAP for modules list if we don't have an up-to-date state.

 /// This is a no-op in case we've ran that request already. In case we did not, it kicks off a background task.

 self
.
fetch
(

 /// We cache request results based on it's arguments. `Modules` request does not take any arguments

 dap_command
::
ModulesCommand
,

 /// Callback invoked with the result of a request.

 |
this
,
result
,
cx
| {

 let
 Some
(
result
) =
result
.
log_err
()
else
 {

 return
;

 };



 this
.modules =
result
;

 cx
.
emit
(
SessionEvent
::
Modules
);

 cx
.
notify
();

 },

 cx
,

 );



 /// Returns a current list of modules; it might be outdated at the time the new request is underway,

 /// but once it is done, the return value of this function will reflect that.

 &
self
.modules

}

/// This function is called from the Module list render function in the UI layer whenever the data layer invalidates the module list state.

fn
 schedule_rebuild
(&
mut
 self
,
cx
: &
mut
 Context
<
Self
>) {

 /// Setting the task drops any current work in progress that is out of date

 self
._rebuild_task =
Some
(
cx
.
spawn
(
async
 move
 |
this
,
cx
| {

 this
.
update
(
cx
, |
this
,
cx
| {

 /// The UI layer queries the data layer for modules and clones the data

 let
 modules
 =
this

 .session

 .
update
(
cx
, |
session
,
cx
|
session
.
modules
(
cx
).
to_owned
());

 this
.entries =
modules
;

 cx
.
notify
();

 })

 .
ok
();

 }));

}

This separation means the UI layer only requests what it needs, allowing the data layer to lazily fetch information and avoid unnecessary requests.
It also makes the data layer solely responsible for maintaining session state, caching responses, and invalidating stale data.
This architecture will make implementing collaborative debugging significantly easier, since the same UI code can be reused across multiplayer sessions—and we only send essential data across the wire, preserving bandwidth.

Supporting every debug adapter out of the box wasn't feasible—there are over70 DAP implementations, each with its own quirks.
To solve this, weextendedZed's extension API to support debugger integration.

 /// Returns the debug adapter binary for the specified adapter name and configuration.

 fn
 get_dap_binary
(

 &
mut
 self
,

 _adapter_name
:
String
,

 _config
:
DebugTaskDefinition
,

 _user_provided_debug_adapter_path
:
Option
<
String
>,

 _worktree
: &
Worktree
,

 ) ->
Result
<
DebugAdapterBinary
,
String
> {

 Err
(
"`get_dap_binary` not implemented"
.
to_string
())

 }



 /// Determines whether the specified adapter configuration should *launch* a new debuggee process

 /// or *attach* to an existing one. This function should not perform any further validation (outside of determining the kind of a request).

 /// This function should return an error when the kind cannot be determined (rather than fall back to a known default).

 fn
 dap_request_kind
(

 &
mut
 self
,

 _adapter_name
:
String
,

 _config
:
serde_json
::
Value
,

 ) ->
Result
<
StartDebuggingRequestArgumentsRequest
,
String
> {

 Err
(
"`dap_request_kind` not implemented"
.
to_string
())

 }

 /// Converts a high-level definition of a debug scenario (originating in a new session UI) to a "low-level" configuration suitable for a particular adapter.

 ///

 /// In layman's terms: given a program, list of arguments, current working directory and environment variables,

 /// create a configuration that can be used to start a debug session.

 fn
 dap_config_to_scenario
(&
mut
 self
,
_config
:
DebugConfig
) ->
Result
<
DebugScenario
,
String
> {

 Err
(
"`dap_config_to_scenario` not implemented"
.
to_string
())

 }



 /// Locators are entities that convert a Zed task into a debug scenario.

 ///

 /// They can be provided even by extensions that don't provide a debug adapter.

 /// For all tasks applicable to a given buffer, Zed will query all locators to find one that can turn the task into a debug scenario.

 /// A converted debug scenario can include a build task (it shouldn't contain any configuration in such case); a build task result will later

 /// be resolved with [`Extension::run_dap_locator`].

 ///

 /// To work through a real-world example, take a `cargo run` task and a hypothetical `cargo` locator:

 /// 1. We may need to modify the task; in this case, it is problematic that `cargo run` spawns a binary. We should turn `cargo run` into a debug scenario with

 /// `cargo build` task. This is the decision we make at `dap_locator_create_scenario` scope.

 /// 2. Then, after the build task finishes, we will run `run_dap_locator` of the locator that produced the build task to find the program to be debugged. This function

 /// should give us a debugger-agnostic configuration for launching a debug target (that we end up resolving with [`Extension::dap_config_to_scenario`]). It's almost as if the user

 /// found the artifact path by themselves.

 ///

 /// Note that you're not obliged to use build tasks with locators. Specifically, it is sufficient to provide a debug configuration directly in the return value of

 /// `dap_locator_create_scenario` if you're able to do that. Make sure to not fill out `build` field in that case, as that will prevent Zed from running second phase of resolution in such case.

 /// This might be of particular relevance to interpreted languages.

 fn
 dap_locator_create_scenario
(

 &
mut
 self
,

 _locator_name
:
String
,

 _build_task
:
TaskTemplate
,

 _resolved_label
:
String
,

 _debug_adapter_name
:
String
,

 ) ->
Option
<
DebugScenario
> {

 None

 }



 /// Runs the second phase of locator resolution.

 /// See [`Extension::dap_locator_create_scenario`] for a hefty comment on locators.

 fn
 run_dap_locator
(

 &
mut
 self
,

 _locator_name
:
String
,

 _build_task
:
TaskTemplate
,

 ) ->
Result
<
DebugRequest
,
String
> {

 Err
(
"`run_dap_locator` not implemented"
.
to_string
())

 }

Adding DAP support via an extension involves defining a custom schema that integrates with our JSON server, implementing logic for downloading and launching the adapter, processing debug configuration to add sane default values, and integrating with locators for automatic configuration.
This design follows our approach to LSP extensions, giving extension authors full control to bring their own debug adapters to Zed with minimal friction.

We also wanted inline variable values to work out of the box.
Surprisingly, theinline values requestis a part of theLanguage Server Protocol (LSP)instead of the DAP.
Using the inline values approach would limit Zed to only showing inline values for DAPs which integrate with LSPs, which isn't many.
A naive workaround might be to use regular expressions to match variable names between the source code and debugger values, but that quickly breaks down when dealing with scopes, and comments.
Instead, we turned toTree-sitter. After all Zed is built by the creators of Tree-sitter!

An inline value example.

Through Tree-sitter queries, we can accurately identify variables within the current execution scope, and easily support any language through.scmfiles without relying on an LSP server to be tightly integrated with a debug adapter.
At launch, inline values are supported for Python, Rust, and Go.
More languages will be supported in the coming weeks.

## What's Next

When we set out to build the debugger, we wanted to make it seamless to use, out of the way, and in line with Zed's high standard of quality.
Now that we've built a strong foundation that is compatible with any debug adapter, we're ready to explore and implement advanced features such as:

* New views: While we support all the fundamental views, we're planning on adding more advanced views such as a watch list, memory view, disassembly view, and a stack trace view
* Automatic configuration: We're going to add support for more languages and build systems
* Polish and more: reach out to uson Discordoron Zed's GitHub repoto let us know!
