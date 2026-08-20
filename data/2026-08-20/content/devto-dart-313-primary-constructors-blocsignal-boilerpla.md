---
title: 'Dart 3.13 Primary Constructors + BlocSignal: Boilerplate-Free Reactive Architecture - DEV Community'
url: https://dev.to/gde/dart-313-primary-constructors-blocsignal-boilerplate-free-reactive-architecture-5fll
site_name: devto
content_file: devto-dart-313-primary-constructors-blocsignal-boilerpla
fetched_at: '2026-08-20T11:24:00.482333'
original_url: https://dev.to/gde/dart-313-primary-constructors-blocsignal-boilerplate-free-reactive-architecture-5fll
author: Randal L. Schwartz
date: '2026-08-14'
description: Discover how Dart 3.13 primary constructors, 'this' constructor bodies, and constructor shorthands transform BlocSignal into the cleanest state management architecture in Flutter. Tagged with flutter, dart, statemanagement, programming.
tags: '#flutter, #dart, #statemanagement, #programming'
---

For years, one of the most common critiques of the BLoC pattern has beenboilerplate.

Between declaring event classes, state hierarchies, constructor parameters, private fields, super-initializers, and event handler registries, you could easily write 50 lines of code before handling a single real-world user action.

WithDart 3.13, that all changes.

Dart 3.13 bringsPrimary Constructors,thisconstructor body blocks, andnew/factoryconstructor shorthands. When combined withBlocSignal—the synchronous, signals-powered evolution of BLoC—the result is an ultra-concise, fully type-safe, and boilerplate-free state management workflow.

Let's explore how Dart 3.13 and BlocSignal fit together like hand in glove.

## 1. Zero-Boilerplate Events & States

In classic BLoC, defining a family of immutable events or states meant writing repeated constructor signatures and field definitions for every subtype.

### 🔴 Before Dart 3.13:

sealed
 
class
 
UserEvent
 
{}

class
 
UserFetchRequested
 
extends
 
UserEvent
 
{

 
final
 
String
 
userId
;

 
UserFetchRequested
(
this
.
userId
);

}

class
 
UserUpdated
 
extends
 
UserEvent
 
{

 
final
 
String
 
name
;

 
final
 
int
 
age
;

 
UserUpdated
({
required
 
this
.
name
,
 
required
 
this
.
age
});

}

class
 
UserLoggedOut
 
extends
 
UserEvent
 
{}

Enter fullscreen mode

Exit fullscreen mode

### 🟢 With Dart 3.13 Primary Constructors:

sealed
 
class
 
UserEvent
 
{}

class
 
UserFetchRequested
(
final
 
String
 
userId
)
 
extends
 
UserEvent
;

class
 
UserUpdated
({
required
 
final
 
String
 
name
,
 
required
 
final
 
int
 
age
})
 
extends
 
UserEvent
;

class
 
UserLoggedOut
()
 
extends
 
UserEvent
;

Enter fullscreen mode

Exit fullscreen mode

A whole sealed hierarchy of events or states can now be declared in just a few clean, expressive lines without losing type safety or exhaustiveness checking inswitchexpressions.

## 2. Streamlined Dependency Injection inCubitSignal

InCubitSignal, you typically inject repositories, API clients, or analytic trackers. In previous Dart versions, you had to declare each field, accept constructor arguments, and forward initial state tosuper.

With primary constructors, field declarations and super invocations live right in the class header.

### 🔴 Before Dart 3.13:

class
 
UserCubit
 
extends
 
CubitSignal
<
UserState
>
 
{

 
final
 
UserRepository
 
_repository
;

 
final
 
AnalyticsService
 
_analytics
;

 
UserCubit
({

 
required
 
UserRepository
 
repository
,

 
required
 
AnalyticsService
 
analytics
,

 
UserState
 
initial
 
=
 
const
 
UserInitial
(),

 
})
 
:
 
_repository
 
=
 
repository
,

 
_analytics
 
=
 
analytics
,

 
super
(
initialState:
 
initial
);

 
Future
<
void
>
 
loadUser
(
String
 
id
)
 
async
 
{

 
emit
(
const
 
UserLoading
());

 
try
 
{

 
final
 
user
 
=
 
await
 
_repository
.
fetchUser
(
id
);

 
_analytics
.
track
(
'user_loaded'
,
 
{
'id'
:
 
id
});

 
emit
(
UserSuccess
(
user
));

 
}
 
catch
 
(
e
,
 
st
)
 
{

 
onError
(
e
,
 
st
);

 
emit
(
UserError
(
e
.
toString
()));

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

### 🟢 With Dart 3.13:

class
 
UserCubit
(

 
final
 
UserRepository
 
repository
,

 
final
 
AnalyticsService
 
analytics
,
 
{

 
final
 
UserState
 
initial
 
=
 
const
 
UserInitial
(),

})
 
extends
 
CubitSignal
<
UserState
>(
initialState:
 
initial
)
 
{

 
Future
<
void
>
 
loadUser
(
String
 
id
)
 
async
 
{

 
emit
(
const
 
UserLoading
());

 
try
 
{

 
final
 
user
 
=
 
await
 
repository
.
fetchUser
(
id
);

 
analytics
.
track
(
'user_loaded'
,
 
{
'id'
:
 
id
});

 
emit
(
UserSuccess
(
user
));

 
}
 
catch
 
(
e
,
 
st
)
 
{

 
onError
(
e
,
 
st
);

 
emit
(
UserError
(
e
.
toString
()));

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

No field re-declarations. No duplicate parameter names. The dependencies are immediately available across all methods.

## 3. Event Handler Registration via thethisBlock inBlocSignal

One of the most powerful features in Dart 3.13 is thethisconstructor body syntax. When using primary constructors, constructor body logic (such as registering event handlers withon<E>()or asserting preconditions) is placed inside athis { ... }block in the class body.

class
 
SearchBloc
(

 
final
 
SearchRepository
 
repository
,
 
{

 
final
 
SearchState
 
initial
 
=
 
const
 
SearchInitial
(),

})
 
extends
 
BlocSignal
<
SearchEvent
,
 
SearchState
>(
initialState:
 
initial
)
 
{

 
// Dart 3.13 primary constructor body

 
this
 
{

 
on
<
SearchQueryChanged
>(

 
(
event
,
 
emit
)
 
async
 
{

 
if
 
(
event
.
query
.
trim
()
.
isEmpty
)
 
return
 
emit
(
const
 
SearchEmpty
());

 
emit
(
const
 
SearchLoading
());

 
final
 
results
 
=
 
await
 
repository
.
search
(
event
.
query
);

 
emit
(
SearchSuccess
(
results
));

 
},

 
transformer:
 
restartable
(),
 
// Zero-stream event concurrency!

 
);

 
}

}

Enter fullscreen mode

Exit fullscreen mode

The header cleanly declares the class contract, and thethisblock sets up the event pipeline.

## 4. Immediate Reactive Wiring withcreateEffect

BlocSignalincludescreateEffect, which automatically tracks signal dependencies and manages teardown on container disposal. With primary constructor parameters in scope, derived cubits can synchronously wire up upstream state containers in thethisblock:

class
 
CartSummaryCubit
(
final
 
CartBloc
 
cartBloc
)

 
extends
 
CubitSignal
<
CartSummary
>(
initialState:
 
const
 
CartSummary
.
zero
())
 
{

 
this
 
{

 
// Automatically reacts to cartBloc.state signals synchronously:

 
createEffect
(()
 
{

 
final
 
items
 
=
 
cartBloc
.
state
.
value
.
items
;

 
final
 
total
 
=
 
items
.
fold
<
double
>(
0
,
 
(
sum
,
 
item
)
 
=
>
 
sum
 
+
 
item
.
price
);

 
emit
(
CartSummary
(
count:
 
items
.
length
,
 
total:
 
total
));

 
});

 
}

}

Enter fullscreen mode

Exit fullscreen mode

## 5. Named Constructor Shorthands (new) for Testing & Seeding

Dart 3.13 also introduces constructor shorthands, allowing you to define secondary named constructors usingnew name()without repeating the class name:

class
 
CounterCubit
(
var
 
int
 
count
)
 
extends
 
CubitSignal
<
int
>(
initialState:
 
count
)
 
{

 
// Named constructor shorthands:

 
new
 
zero
()
 
:
 
this
(
0
);

 
new
 
seeded
(
int
 
initial
)
 
:
 
this
(
initial
);

 
void
 
increment
()
 
=
>
 
emit
(
state
 
+
 
1
);

 
void
 
decrement
()
 
=
>
 
emit
(
state
 
-
 
1
);

}

Enter fullscreen mode

Exit fullscreen mode

This makes testing variations, mock seeds, and default configurations concise and readable.

## 🛠️ Enabling Dart 3.13 in Your Project

To take advantage of these features:

### 1. Set the SDK Constraint inpubspec.yaml:

environment
:

 
sdk
:
 
^3.13.0

dependencies
:

 
bloc_signals
:
 
^1.0.0

 
bloc_signals_flutter
:
 
^1.0.0

Enter fullscreen mode

Exit fullscreen mode

### 2. Enable Dart 3.13 Linter Rules inanalysis_options.yaml:

include
:
 
package:very_good_analysis/analysis_options.yaml

linter
:

 
rules
:

 
-
 
use_primary_constructors

 
-
 
use_declaring_parameters

 
-
 
unnecessary_type_name_in_constructor

 
-
 
unnecessary_primary_constructor_body

Enter fullscreen mode

Exit fullscreen mode

## 🚀 The Architectural Payoff

By combiningDart 3.13language features withBlocSignal, you get:

1. 0ms Synchronous Updates: State emissions propagate in the current frame without microtask delay.
2. Minimal Ceremony: Class headers declare fields and super initializers simultaneously.
3. Signal Graph Efficiency: Automatic==de-duplication and fine-grained UI rebuilding.
4. Standard BLoC Rigor: Clean event dispatching, state transitions, and OpenTelemetry observability.

## 💬 Over to You: What's Your Take?

We'd love to hear your thoughts in the comments below:

1. How do you feel about Dart 3.13's primary constructors?Does declaring fields directly in the class header match how you design your domain and state layers?
2. Are you planning to adopt primary constructors across your state management classes, or are there specific patterns where you still prefer classic constructors?
3. Have a boilerplate-heavy state class or Bloc?Drop a snippet in the comments, and let's see how much code Dart 3.13 and BlocSignal can shave off!

Ready to build boilerplate-free reactive apps?

Check out the full documentation, benchmarks, and interactive examples atblocsignal.devor star the open-source repository onGitHub!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse