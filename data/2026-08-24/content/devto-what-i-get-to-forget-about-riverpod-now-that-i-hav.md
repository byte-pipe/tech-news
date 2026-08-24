---
title: What I Get to Forget About Riverpod Now That I Have BlocSignal - DEV Community
url: https://dev.to/gde/what-i-get-to-forget-about-riverpod-now-that-i-have-blocsignal-1be5
site_name: devto
content_file: devto-what-i-get-to-forget-about-riverpod-now-that-i-hav
fetched_at: '2026-08-24T19:27:14.836342'
original_url: https://dev.to/gde/what-i-get-to-forget-about-riverpod-now-that-i-have-blocsignal-1be5
author: Randal L. Schwartz
date: '2026-08-21'
description: The greatest upgrade in developer experience isn't what you have to learn—it's the mental gymnastics you get to unlearn. A respectful, deep-dive comparison into why shedding Riverpod's cognitive overhead brings joy back to Flutter architecture. Tagged with flutter, dart, riverpod, statemanagement.
tags: '#flutter, #dart, #riverpod, #statemanagement'
---

## The Best Feature in Software Is What You Get to Forget

In software engineering, we usually measure framework upgrades by what theyadd: new syntax, new macros, new features, new abstractions.

But as any developer who has maintained large Flutter applications over several years knows, the most profound upgrade in developer experience isn't what new concepts you are forced to memorize—it’s the mental gymnastics, framework-specific edge cases, and defensive rituals you finally get to forget and unlearn.

Before we dive into technical specifics, let's establish something essential:Rémi Rousselet is a pioneer and a brilliant engineer.When Rémi createdproviderin Flutter's early days and later builtRiverpodin 2020, he solved real, glaring flaws in Flutter's coreInheritedWidgetmechanics (such as conditional dependency leaks and lack of compile safety). The entire Flutter ecosystem owes Rémi immense gratitude for pushing the boundaries of Dart architecture.

For years, I was a vocal, passionate—at times almost zealous—advocate for Riverpod. In discussions, community forums, and client architectures, I routinely recommended Riverpod above classic BLoC, Provider, and almost every other state management alternative. I championed its compile-time safety and global declarative graph vision because it genuinely solved tough problems we faced in earlier Flutter eras.

However, over the course of Riverpod's evolution across v1, v2 (the code-gen era), and v3, solving every edge case within a global declarative provider graph led to a staggering accumulation of cognitive surface area. Building real-world Flutter apps with Riverpod today requires developers to maintain a complex internal rules engine just to avoid subtle runtime footguns.

And yet, recognizing how much mental gymnastics this has gradually demanded, I find myself genuinely thrilled and relieved to be pivoting. When you switch toBlocSignal(which combines the proven discipline of BLoC/Cubit with the synchronous speed and fine-grained reactivity of Signals), you realize just how much mental baggage you were carrying—and I am excited to share that journey with all of you.

### A Quick Note on Lints and IDE Assists

It is worth acknowledging that the Riverpod ecosystem has invested heavily in custom analyzer lints (riverpod_lint), IDE plugins, and automated quick-fixes (such as"Wrap with ConsumerWidget"or"Convert to Notifier").

While these tooling aids are genuinely helpful, they only address surface-level syntax—they cannot eliminate the underlying cognitive load. An IDE shortcut that automatically rewrites your widget class hierarchy does not prevent a controller from disposing mid-flight during anawaitgap, nor can a linter rule save a navigation stack from wiping when a router provider re-evaluates.

Tooling assists can bandage syntactic friction, but true architectural simplicity removes the friction at the root.

Here is the running list of everything you get toforget—and why your architecture gets significantly cleaner the moment you do.

## 1. 🗑️ Forgetbuild_runnerand Code-Gen Rituals

### The Riverpod Gymnastics:

In modern Riverpod (v2/v3), code generation is the officially recommended path. That means:

* Annotating classes with@riverpod.
* Extending obscure generated private base classes (extends _$AuthNotifier).
* Runningdart run build_runner watch --delete-conflicting-outputsin a separate terminal tab, spinning laptop fans while consuming gigabytes of RAM.
* Waiting several seconds every time you rename a parameter or add a method just for IDE autocomplete to work again.
* Dealing with noisy.g.dartgenerated files cluttering Git diffs and code reviews.

(Yes, Riverpod still technically supports manualNotifierProvider/Notifiersyntax without code generation. But code-gen is the officially documented standard and recommended default throughout modern Riverpod tutorials and guides. Writing manual syntax is verbose and forfeits features like typed.familyparameter records.)

// 🤯 Riverpod (Code Generation Required)

import
 
'package:riverpod_annotation/riverpod_annotation.dart'
;

part
 
'counter.g.dart'
;

@riverpod

class
 
Counter
 
extends
 
_$Counter
 
{

 
@override

 
int
 
build
()
 
=
>
 
0
;

 
void
 
increment
()
 
=
>
 
state
++
;

}

Enter fullscreen mode

Exit fullscreen mode

### What You Do in BlocSignal:

You writepure Dart. Nobuild_runner. No part files. No code-gen watchers. Instant autocomplete in every IDE, 100% of the time.

// ⚡ BlocSignal (Zero Code-Gen, Pure Dart)

import
 
'package:bloc_signals/bloc_signals.dart'
;

class
 
CounterCubit
 
extends
 
CubitSignal
<
int
>
 
{

 
CounterCubit
()
 
:
 
super
(
initialState:
 
0
);

 
void
 
increment
()
 
=
>
 
emit
(
stateValue
 
+
 
1
);

}

Enter fullscreen mode

Exit fullscreen mode

## 2. 🗑️ Forget Widget Class Hierarchy Gymnastics &WidgetRefPlumbing

### The Riverpod Gymnastics:

In Riverpod, you cannot read or watch state from standard Flutter widgets without either:

1. Converting yourStatelessWidgetinto aConsumerWidgetand changingbuild(BuildContext context)tobuild(BuildContext context, WidgetRef ref).
2. Converting yourStatefulWidgetinto aConsumerStatefulWidgetandState<T>intoConsumerState<T>.
3. If using Flutter Hooks, extendingHookConsumerWidget(a Frankenstein base class).
4. PassingWidgetRef refdown private helper functions, widget sub-methods, and domain callbacks becauserefis not accessible from standardBuildContext.

// 🤯 Riverpod

class
 
UserProfileView
 
extends
 
ConsumerWidget
 
{

 
const
 
UserProfileView
({
super
.
key
});

 
@override

 
Widget
 
build
(
BuildContext
 
context
,
 
WidgetRef
 
ref
)
 
{

 
final
 
user
 
=
 
ref
.
watch
(
userProvider
);

 
return
 
Text
(
user
.
name
);

 
}

}

Enter fullscreen mode

Exit fullscreen mode

### What You Do in BlocSignal:

You usestandard Flutter widgets.StatelessWidget,StatefulWidget, orHookWidget. You interact via idiomaticBuildContextextensions or dedicated declarative widgets (BlocSignalBuilder,BlocSignalListener,BlocSignalConsumer):

// ⚡ BlocSignal

class
 
UserProfileView
 
extends
 
StatelessWidget
 
{

 
const
 
UserProfileView
({
super
.
key
});

 
@override

 
Widget
 
build
(
BuildContext
 
context
)
 
{

 
final
 
user
 
=
 
context
.
watch
<
UserCubit
>()
.
stateValue
;

 
return
 
Text
(
user
.
name
);

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Zero custom base classes. ZeroWidgetRefdrilling. Native Flutter.

## 3. 🗑️ Forget the Provider "Alphabet Soup" & Deprecation Whiplash

### The Riverpod Gymnastics:

Over the last few years, Riverpod developers have had to navigate an exhausting taxonomy of provider variants:

* Provider
* StateProvider(deprecated in v2/v3)
* StateNotifierProvider(deprecated)
* ChangeNotifierProvider
* FutureProvider
* StreamProvider
* NotifierProvider
* AsyncNotifierProvider
* StreamNotifierProvider
* AutoDisposeProvider/AutoDisposeFutureProvider
* .familymodifiers with tuple parameter records

Each variant had its own slightly different rules for error handling, disposal, and lifecycle callbacks.

### What You Do in BlocSignal:

There are onlytwo intuitive, unified primitives:

1. CubitSignal<State>: For method-based state management (call methods, compute derived state, emit new values).
2. BlocSignal<Event, State>: For formal, event-driven unidirectional data flow with explicit event hierarchies and concurrency transformers (droppable,restartable,sequential).

Both use standard Dart constructors, synchronousemit(), and exposestateas a reactiveReadonlySignal<State>.

(While Riverpod's genericAsyncValueis handy for basic fetch-and-display screens, real enterprise applications quickly outgrow generic 3-state wrappers and require rich domain models—such as partial validations, optimistic rollbacks, and multi-step forms. WithBlocSignal, you leverage the full expressive power of Dart 3 sealed classes for domain state, while retaining access toAsyncSignalwhen you want declarative async futures.)

## 4. 🗑️ Forget the "Ref World vs. Non-Ref World" Boundary

### The Riverpod Dilemma:

As I taught developers and engineering teams about Riverpod over the years, I gradually adopted a mental model of the"Ref World" vs. the "Non-Ref World"to help students understand a fundamental reality of Riverpod's design.

In Riverpod, reactive state is strictly confined inside aProviderContainer—the "Ref World". As long as you are inside aConsumerWidgetor inside another provider, you hold aReforWidgetRef, and everything connects. But the moment you step into standard Dart code—such as HTTP client interceptors, WebSocket listeners, background database services, or routing configurations—you are stranded in the "Non-Ref World". To connect the two, you are forced to:

* Drill aRef refparameter through every layer and pollute pure Dart domain classes with framework dependencies.
* Or expose a global top-levelProviderContainervariable as an escape hatch.

### What You Do in BlocSignal:

bloc_signalsis a100% pure Dart package with zero Flutter dependencies.

* You can instantiate and observe aCubitSignalorBlocSignalanywhere: inside Flutter widgets, CLI tools, Jaspr web applications, or Serverpod backend services.
* Pure Dart services can readcubit.stateValueor subscribe directly tocubit.state.subscribe((state) => ...)with zero container ceremony.

What about cross-container coordination?In classic stream-based BLoC, coordinating two Blocs was notoriously clunky (often forcing developers to nest multipleBlocListenerwidgets in the UI tree). InBlocSignal, because every state is exposed as a reactiveReadonlySignal<State>, cross-Cubit derived state is trivial in pure Dart business logic:

// ⚡ Pure Dart Cross-Cubit Derivation (Zero UI Listeners Needed)

late
 
final
 
isCheckoutReady
 
=
 
computed
(()
 
=
>
 
 
authCubit
.
state
()
.
isAuthenticated
 
&&
 
cartCubit
.
state
()
.
items
.
isNotEmpty

);

Enter fullscreen mode

Exit fullscreen mode

Zero widget tree nesting. Zero stream subscriptions. 100% testable in pure Dart.

## 5. 🗑️ Forget therouterProviderNavigation Stack Nuke

### The Riverpod Footgun:

Perhaps the most notorious casualty of the "Non-Ref World" boundary is routing. Because routers likeGoRouterare standard Dart objects that live squarely in the Non-Ref World, developers frequently attempt to pull their router into the Ref World by wrapping it in a RiverpodProviderso it can accessrefand observe live authentication state:

// 💣 The Innocent-Looking Riverpod Disaster

final
 
routerProvider
 
=
 
Provider
<
GoRouter
>((
ref
)
 
{

 
final
 
auth
 
=
 
ref
.
watch
(
authProvider
);
 
// 💣 DISASTER

 
return
 
GoRouter
(

 
redirect:
 
(
context
,
 
state
)
 
=
>
 
auth
.
isLoggedIn
 
?
 
null
 
:
 
'/login'
,

 
routes:
 
[...],

 
);

});

Enter fullscreen mode

Exit fullscreen mode

The Runtime Bug:WheneverauthProvideremits (or background token refresh occurs),ref.watchdestroys andrecreates the entireGoRouterinstance.

* The user's entire navigation history stack is wiped clean.
* Deeply nested tabs and modal sheets vanish instantly.
* Scroll offsets reset to the top.

To fix this in Riverpod, you cannot just write intuitive code; you must possess a deep, esoteric understanding ofbothhow GoRouter manages its internal delegate and how Riverpod rebuilds provider dependencies. The prescribed workaround is constructing a customChangeNotifierbridge withref.listento feedrefreshListenable.

Worse still, when this bug strikes in production, there are no error logs or stack traces—just an unexplained navigation reset. Developers are often left struggling with a complete lack of information and traceability, unclear even where to place debugger probes or log statements to catch why the router is vanishing.

### What You Do in BlocSignal:

YourGoRouterinstance is created once and remains permanent. You connect it directly usingtoListenable():

// ⚡ BlocSignal: Stable Router, Live Redirects

final
 
router
 
=
 
GoRouter
(

 
refreshListenable:
 
authCubit
.
toListenable
(),

 
redirect:
 
(
context
,
 
state
)
 
=
>
 
authCubit
.
stateValue
.
isLoggedIn
 
?
 
null
 
:
 
'/login'
,

 
routes:
 
[...],

);

Enter fullscreen mode

Exit fullscreen mode

Zero router destruction. Unbroken navigation stacks. 100% deterministic.

## 6. 🗑️ Forget the "Self-Disposing Async Mutation" Crash

### The Riverpod Footgun:

In Riverpod 3.0, auto-disposal is enabled by default. While the intended goal of automatic disposal is commendable (preventing memory leaks in long-lived trees), usingimplicit UI reference counting to govern asynchronous business logiccreates severe race conditions:

// 💣 Riverpod 3.0 Trap

@riverpod

class
 
NoteController
 
extends
 
_$NoteController
 
{

 
@override

 
Future
<
List
<
Note
>>
 
build
()
 
=
>
 
repository
.
fetchNotes
();

 
Future
<
void
>
 
deleteNote
(
String
 
id
)
 
async
 
{

 
state
 
=
 
const
 
AsyncLoading
();

 
await
 
repository
.
deleteNote
(
id
);

 
// 💥 CRASH: "Cannot use Ref after it has been disposed"

 
// If the user navigates away or no widget is watching this controller during the `await`,

 
// Riverpod garbage-collects this instance mid-flight!

 
ref
.
invalidateSelf
();
 
 
}

}

Enter fullscreen mode

Exit fullscreen mode

To work around this in Riverpod, developers are forced into defensive gymnastics:

* Defensive Guards:Sprinklingif (ref.mounted)checks after every single asynchronousawait.
* Action Controller Sprawl:Creating an entirely separateNoteDeleteActionControllerclass just to execute a single async method call without auto-disposing the main list provider.
* Keep-Alive Token Juggling:Manually acquiring and releasingKeepAliveLinktokens:

 
final
 
link
 
=
 
ref
.
keepAlive
();
 
// 🤯 Manual retain-count management in Dart!

 
try
 
{

 
await
 
repository
.
deleteNote
(
id
);

 
}
 
finally
 
{

 
link
.
close
();
 
// Remember to release the token, or leak memory forever!

 
}

Enter fullscreen mode

Exit fullscreen mode

Think about how absurd that is: you find yourself having to writemeta-state management just to manage the lifecycle of your state management system. High-level declarative Dart is suddenly reduced to manual reference-count lock juggling.

### What You Do in BlocSignal:

InBlocSignal, state containers arestandard Dart objects with explicit, predictable ownership. If an async method is running, it executes to completion. If a Bloc is closed,emit()is safely dropped with zero unhandled runtime crashes:

// ⚡ BlocSignal

class
 
NoteCubit
 
extends
 
CubitSignal
<
NoteState
>
 
{

 
NoteCubit
({
required
 
this
.
repository
})
 
:
 
super
(
initialState:
 
const
 
NoteState
.
initial
());

 
final
 
NoteRepository
 
repository
;

 
Future
<
void
>
 
deleteNote
(
String
 
id
)
 
async
 
{

 
emit
(
stateValue
.
copyWith
(
isLoading:
 
true
));

 
await
 
repository
.
deleteNote
(
id
);

 
final
 
notes
 
=
 
await
 
repository
.
fetchNotes
();

 
emit
(
stateValue
.
copyWith
(
isLoading:
 
false
,
 
notes:
 
notes
));

 
}

}

Enter fullscreen mode

Exit fullscreen mode

## 7. 🗑️ Forget.familyParameter Isolation & Cache Silos

### The Riverpod Dilemma:

When you use Riverpod's.familymodifier to parameterize queries:

final
 
userPostsProvider
 
=
 
FutureProvider
.
family
<
List
<
Post
>,
 
String
>((
ref
,
 
userId
)
 
=
>
 
...);

final
 
postDetailProvider
 
=
 
FutureProvider
.
family
<
Post
,
 
String
>((
ref
,
 
postId
)
 
=
>
 
...);

Enter fullscreen mode

Exit fullscreen mode

Each parameter generates an isolated provider instance. If the user likes a post inpostDetailProvider('post-123'),userPostsProvider('user-456')still contains the old, unliked copy of that post in memory. You now have to build complex cache invalidation bridges across multiple isolated providers.

### What You Do in BlocSignal:

You use normal Dart parameters in constructors (PostCubit(userId: id)) and share live reactive signal stores (likemapSignalorcomputed()) across containers. When a post is updated in the central signal store, every widget and cubit observing it updatessynchronously in the exact same frame.

## 8. 🗑️ Forget theref.watchin Callbacks Infinite Loop Trap

### The Riverpod Gotcha:

One of the most common mistakes for Flutter developers learning Riverpod is callingref.watchinside anonPressedor gesture callback instead ofref.read:

// 💣 Riverpod Bug

ElevatedButton
(

 
onPressed:
 
()
 
{

 
// 💥 Calling watch inside an event handler registers an invalid dependency

 
// or creates unexpected rebuild cascades!

 
ref
.
watch
(
authProvider
.
notifier
)
.
login
();

 
},

 
child:
 
const
 
Text
(
'Login'
),

)

Enter fullscreen mode

Exit fullscreen mode

### What You Do in BlocSignal:

The distinction inBlocSignalis natural and enforced by Flutter's existingBuildContextidioms:

* In callbacks/handlers:context.read<AuthCubit>().login()(O(1) lookup, zero subscription).
* In UI builders:context.watch<AuthCubit>().stateValueorBlocSignalBuilder<AuthCubit, AuthState>(explicit reactive rebuild boundary).

## 9. 🗑️ Forget In-Place Mutation Silent Drop Traps

### The Riverpod Footgun:

In Riverpod 3, notifying listeners relies strictly on reference equality (identical(oldState, newState)). If you mutate a list in-place:

// 💣 Riverpod 3 Silent Failure

state
.
add
(
newItem
);

state
 
=
 
state
;
 
// ❌ Does NOT trigger UI rebuilds because identical(state, state) is true!

Enter fullscreen mode

Exit fullscreen mode

### What You Do in BlocSignal:

BlocSignalprovides explicit, customizable equality checks viaSignalOptions(equals: ...)or standard value equality (using Dart 3 records, Freezed, orfast_immutable_collections). When you callemit(newState), the transition is explicit, logged throughBlocSignalObserver, and propagated synchronously.

## 10. 🗑️ Forget SubtreeProviderScope(overrides: [...])Scoping & Modal Traps

### The Riverpod Gymnastics:

In Riverpod, when you need to scope data down a specific widget subtree—such as passing item data down a list view or customizing a controller for a nested section—Riverpod prescribes nesting aProviderScopewithoverrides::

// 🤯 Riverpod: Scoping data in a list

ListView
.
builder
(

 
itemCount:
 
todos
.
length
,

 
itemBuilder:
 
(
context
,
 
index
)
 
{

 
return
 
ProviderScope
(

 
overrides:
 
[

 
currentTodoProvider
.
overrideWithValue
(
todos
[
index
]),

 
],

 
child:
 
const
 
TodoItemTile
(),

 
);

 
},

);

Enter fullscreen mode

Exit fullscreen mode

This pattern introduces several subtle, high-friction pitfalls:

1. Container Overhead in Lists:Wrapping 100 list tiles inProviderScopeinstantiates 100 nestedElementwidgets and separate internal provider container nodes.
2. The "Split-Brain" Dependency Trap:If Provider B depends on Provider A, and you override A in a nestedProviderScopewithoutalsoexplicitly overriding B, Provider B still resolves against therootun-overridden A, causing baffling data desynchronization bugs.
3. The Modal & Dialog Disconnection Bug:When you callshowDialog()orshowModalBottomSheet(), Flutter pushes the new route to the rootNavigatoroverlay. Because the dialog is mounted outside the local subtree'sProviderScope, all local overrides are instantly lost—causing the modal to either crash with missing providers or silently read outdated root state.

### What You Do in BlocSignal:

You usestandard Dart and Flutter idioms:

* In lists: Pass data directly via constructor parameters (TodoItemTile(todo: todos[index])).
* In subtrees: Use standard Flutter scoping withBlocSignalProvider.value(value: todoCubit, child: ...)or provide scoped instances cleanly.
* In dialogs: Pass the Cubit directly toBlocSignalProvider.valuein the dialog builder, or let it resolve naturally up the Flutter element tree.

## 11. 🗑️ Forget ComplexProviderContainerMocking & Test Rigmarole

### The Riverpod Testing Ceremony:

In Riverpod, unit tests and widget tests require assembling aProviderContaineror wrapping test widgets inProviderScope(overrides: [...]):

// 🤯 Riverpod Test Ceremony

final
 
container
 
=
 
ProviderContainer
(

 
overrides:
 
[

 
authRepositoryProvider
.
overrideWithValue
(
mockAuthRepo
),

 
apiClientProvider
.
overrideWithValue
(
mockApiClient
),

 
// ⚠️ Miss just one transitive provider in this list, and your test

 
// will accidentally make real network calls or throw late-init errors!

 
],

);

addTearDown
(
container
.
dispose
);

Enter fullscreen mode

Exit fullscreen mode

### What You Do in BlocSignal:

State containers are plain Dart classes withdirect constructor injection. You instantiate your Cubit or Bloc with your mock repository directly:

// ⚡ BlocSignal: Declarative, Instant Unit Testing

blocSignalTest
<
CounterCubit
,
 
int
>(

 
'emits [1] when increment is called'
,

 
build:
 
()
 
=
>
 
CounterCubit
(
repository:
 
mockRepository
),

 
act:
 
(
cubit
)
 
=
>
 
cubit
.
increment
(),

 
expect:
 
()
 
=
>
 
[
1
],

);

Enter fullscreen mode

Exit fullscreen mode

BecauseBlocSignalstate transitions aresynchronous, assertions execute immediately without flakytester.pumpAndSettle()timeouts or async race conditions.

## 12. 🤖 Forget the AI & LLM Hallucination Nightmare

### The Riverpod AI Friction:

If you pair-program with AI coding assistants—whether Claude, Cursor, GitHub Copilot, ChatGPT, or Gemini—you have likely experienced how difficult Riverpod is for modern LLMs:

1. The Version Multi-Verse:LLM training data contains years of conflicting Riverpod eras (v0.14ChangeNotifierProvider, v1.0StateNotifierProvider, v2.0@riverpodcode-gen, and v3.0Notifier). AI models constantly mix up these eras, hallucinating deprecated APIs, invalid provider types, or incompatible syntax.
2. Code-Gen Blindness:LLMs cannot see generated code beforebuild_runnerexecutes. When an AI generates a@riverpodclass, it frequently botches the synthesized_$ClassNameinheritance, misnames the generated provider, or forgets thepart 'file.g.dart';declaration.
3. RefScope Confusion:AI models frequently lose track of the "Ref World" boundary—attempting to accessrefinside widget constructors, passingWidgetRefinto deep business logic layers, or failing to convert widgets toConsumerStatefulWidget.
4. Implicit Auto-Disposal Bugs:LLMs routinely write async mutation methods inside auto-disposing notifiers without accounting forref.mountedguards or keep-alive tokens, generating code that looks plausible but crashes in production.

### What You Do in BlocSignal:

LLMs excel atpure, standard Dart with explicit contracts:

* Standard Dart & Predictable Conventions:Pure classes, direct constructor injection, and idiomatic FlutterBuildContextlookups. There is no code-gen magic for the LLM to guess.
* Zerobuild_runnerFeedback Loops:AI agents can write features, scaffold tests, and immediately verify analyzer diagnostics without waiting for external code generation steps.
* Vast Training Ground:BLoC and Cubit are among the most consistently documented and deeply represented architectural patterns in AI training datasets. LLMs generate accurate, idiomaticBlocSignalcode on the first try.
* Deterministic AI-Generated Tests:AI tools generate rock-solid, synchronousblocSignalTestsuites without getting tripped up byProviderContainersetup boilerplate or async frame timing issues.
* First-Class AI Skills From Day One:Rather than leaving LLMs to guess architectural boundaries,BlocSignalships from day one with installable agent skills covering migrations, interop adapters, and production best practices.

## Summary: The Cognitive Weight You Leave Behind

What You Leave Behind in Riverpod

What You Enjoy in BlocSignal

build_runner
 & 
.g.dart
 Code Generation

Pure, standard Dart with instant IDE autocomplete

ConsumerWidget
 & 
WidgetRef
 Plumbing

Standard Flutter widgets & clean 
BuildContext
 APIs

Alphabet Soup of 10+ Provider Types

2 Unified Primitives (
CubitSignal
 & 
BlocSignal
)

Ref vs Non-Ref Boundary Walls

Zero-dependency pure Dart state usable anywhere

GoRouter
 Navigation Stack Wipes

Stable router instance with 
.toListenable()

"Self-Disposing" Async Mutation Crashes

Predictable, developer-owned object lifecycles

Isolated 
.family
 Cache Silos

Direct constructor injection & normalized Signals graph

ref.watch
 in Callbacks Rebuild Cascades

Clean separation of 
context.read()
 & 
context.watch()

In-Place Mutation Silent Drops

Explicit transitions via 
emit()
 with custom equality

Subtree 
ProviderScope(overrides:)
 & Modal Disconnects

Standard Dart props & native 
InheritedWidget
 scoping

Complex 
ProviderContainer
 Test Overrides

Direct constructor mocking & declarative 
blocSignalTest

AI / LLM Version Hallucinations & Code-Gen Errors

First-shot AI accuracy with standard Dart & BLoC patterns

## 🌉 Currently Mired in Riverpod? You Don’t Need a Big-Bang Rewrite

If you maintain a large production codebase built on Riverpod, you might be thinking:"This sounds wonderful, but our entire team is already knee-deep in Riverpod. We cannot afford to halt feature delivery for a massive rewrite."

You don't have to.

Throughbloc_signals_riverpod, you get a seamless,bidirectional interop bridgethat allows you to adoptBlocSignalincrementally, one feature or screen at a time.

### Direction 1: Expose a BlocSignal to Existing Riverpod Widgets

If you build a new feature using a clean, pure DartCubitSignal, you can expose it directly to existing Riverpod widgets as a standardNotifierProviderusing.toProvider():

// 1. Build your new feature with a pure Dart Cubit

final
 
cartCubit
 
=
 
CartCubit
();

// 2. Adapt it into a Riverpod provider with a single call

final
 
cartProvider
 
=
 
cartCubit
.
toProvider
();

// 3. Existing Riverpod ConsumerWidgets watch it seamlessly:

class
 
CartBadge
 
extends
 
ConsumerWidget
 
{

 
const
 
CartBadge
({
super
.
key
});

 
@override

 
Widget
 
build
(
BuildContext
 
context
,
 
WidgetRef
 
ref
)
 
{

 
final
 
cartState
 
=
 
ref
.
watch
(
cartProvider
);

 
return
 
Badge
(
label:
 
Text
(
'
${cartState.itemCount}
'
));

 
}

}

Enter fullscreen mode

Exit fullscreen mode

### Direction 2: Consume Legacy Riverpod Providers in BlocSignal

Conversely, if your new BlocSignal architecture needs to read data from legacy Riverpod providers that you aren't ready to rewrite yet, you can adapt anyProviderListenablewith.toBlocSignal(ref):

// Adapt any legacy Riverpod provider into a reactive BlocSignal

final
 
userBloc
 
=
 
legacyUserProvider
.
toBlocSignal
(
ref
);

// Read stateValue synchronously or subscribe to state changes

print
(
userBloc
.
stateValue
.
userName
);

Enter fullscreen mode

Exit fullscreen mode

You can migrate your application piece by piece—shedding the cognitive load on new features immediately while existing code continues running uninterrupted.

## Getting Started

If you want the architectural discipline of BLoC combined with the modern, zero-latency reactive power of Signals—without the code-gen or cognitive overhead—give BlocSignal a spin.

dependencies
:

 
bloc_signals
:
 
^1.0.0

 
bloc_signals_flutter
:
 
^1.0.0

 
# Optional for incremental migration:

 
bloc_signals_riverpod
:
 
^1.0.0

Enter fullscreen mode

Exit fullscreen mode

Learn more atblocsignal.devor explore the source onGitHub.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse