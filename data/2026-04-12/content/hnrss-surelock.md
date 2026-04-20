---
title: Surelock
url: https://notes.brooklynzelenka.com/Blog/Surelock
site_name: hnrss
content_file: hnrss-surelock
fetched_at: '2026-04-12T06:01:15.441338'
original_url: https://notes.brooklynzelenka.com/Blog/Surelock
date: '2026-04-08'
description: NOTE Hello r/rust! Thank you for the interest in this work and for the delightful conversation ❤️ I hate deadlocks. Maybe you do too.
tags:
- hackernews
- hnrss
---

NOTE

Hellor/rust! Thank you for the interest in this work and for the delightful conversation ❤️

Ihatedeadlocks. Maybe you do too. Back atFission, whenever someone would suggest a mutex we’d start a chant of “I say mutex, you say deadlock: Mutex! DEADLOCK! Mutex! DEADLOCK!“. Deadlocks lurk — perfectly invisible in code review, happy to pass CI a thousand times, then lock your system up at 3am under a request pattern that no one anticipated.

They have their own tradeoffs, but I missTVars from Haskell. AFAICT there’s no way to do properTVars in languages that have no way to enforce purity. We “should” prefer lock-free programming, but mutexes are very common in theRuststandard style. I often hear that actors eliminate deadlocks, but as someone who’s written her fair share ofElixir, this is 100% a lie (though theyareless frequent).

Rust famously catches data races at compile time, but for deadlocks? You get aMutex, a pat on the back, and “good luck, babe”. There are some tools that help analyze your code that are fairly good, but I want feedback during development. I’ve been thinking about a better approach to this problem for a while, looked at a bunch of other attempts and have come up with what I hope is a decent ergonomic balance that covers many common use cases in Rust:surelock, a deadlock-freedom library. If your code compiles, it doesn’t deadlock. NoResult, noOption, no runtime panic on the lock path. Every acquisition is either proven safe by the compiler or rejected at build time1.

WARNING

This is a pre-release. I think the core design is solid, but I wouldn’t be surprised if there are rough edges. Feedback and contributions welcome!

# TL;DR

1. Deadlocks happen when all fourCoffman Conditionsoccursimultaneously
2. Surelock breaks one of them —circular wait— using two complementary mechanisms
3. Same-level locks are acquired atomically in a deterministic order (LockSet)
4. Cross-level locks are acquired incrementally with compile-time ordering enforcement (Level<N>)
5. The entire public API is safe —unsafeis confined to the raw mutex internals
6. no_stdcompatible, zero required runtime dependencies2

# Why Not Just Be Careful?

The honest answer is that being careful doesn’t scale. It’s easy to shoot yourself in the foot while composing code. But wait, isn’t this the kind of thing that Rust us supposed to help us with? The borrow checker catches data races at compile time — why shouldn’t we expect the same for deadlocks?

The fundamental problem is well-understood. Coffman et al. identified four necessary conditions for deadlock back in 1971:

Condition
Meaning
Mutual exclusion
At least one resource is held exclusively
Hold and wait
A thread holds one lock while waiting for another
No preemption
Locks can’t be forcibly taken away
Circular wait
A cycle exists in the wait-for graph

Break any one of these, and deadlocks become impossible. Mutual exclusion is the whole point of a mutex. Preemption introduces its own class of bugs. That leaves hold-and-wait and circular wait.

QUOTE

A language that doesn’t affect the way you think about programming is not worth knowing.

― Alan Perlis

We identified the solution space over 50 years ago(!). It’s a thorny enough problem that we have no single agreed solution, and yet mutexes are sufficiently useful that we still use them. This suggests that until something comes along that completely replaces mutexes, we’re in the domain of improving the ergonomics for using mutexes safely.

Only rarely do safety techniques exactly match safe use. Type systems somewhat famously either allow some unsound behaviour, or rule out legitimate use (sometimes both) — hence all of the effort going into making fancier type systems that can more directly match all safe uses while ruling out unsafe ones. The trick is in lining those up as closely as possible while introducing the easiest model to work with: minimal ceremony and/or easy to reason about. I would argue that we want our tools tohelp us to think about the problem.

# The Key Metaphor

Surelock is built around a physical-world analogy: to interact with locks, you need a key. in our case, we’re going to keep that key while the mutex is in use. You only get that key back when you unlock it.

We call this aMutexKey— a linear3scope token. You get one when you enter a locking scope. When you call.lock(), the key isconsumedand a new one is returned alongside the guard. The new key carries a type-level record of what you’ve already locked, so the compiler knows what you’re still allowed to acquire. Try to go backwards and the code doesn’t compile.

💡 This is the core trick: by making the key a move-only value that threads through every acquisition, we get a compile-time witness of the current lock state. No global analysis, no runtime tracking — just the type checker doing what it does best.

This analogy only goes so far:MutexKeyactually grants you the ability to lock multiple mutexes together atomically. Locks in surelock may be grouped into levels to enable incremental acquisition, and locking returns an attenuated key that can lock fewer levels.

# Prior Art

Two existing libraries informed the design, and I want to give them proper credit.

## happylock

happylockbybotahamecintroduced the key insight that acapability tokencombined with sorted multi-lock acquisition can prevent deadlocks. Surelock borrows this pattern directly.

Where the approaches diverge:happylockbreaks the hold-and-wait condition. When you lock through the collection, your key is consumed — you can’t go acquire more locksat alluntil it’s released. This is safe, but it means you MUST acquire all of your locks at once. You can’t do things like “lock the config, read which account to update, then lock that account”. In concurrent systems that need incremental acquisition, this is a real limitation — when you need incremental locks, youreallyneed incremental locks.

happylockalso sorts locks bymemory address, which is not stable acrossVecreallocations or moves. The library goes to some length to maintain address stability withunsafe(Box::leak,transmute), and that unsafety propagates to the public API.

## lock_tree

lock_treefrom Google’s Fuchsia project introduced compile-time lock ordering via aLockAftertrait. Declare that level A comes before level B, and the compiler rejects any code that tries to acquire them in the wrong order.

Surelock extends this in a few ways: same-level multi-lock (whichlock_treecan’t express), per-instance level assignment vianew_higher, and scope-uniqueness enforcement. Surelock also deliberately dropslock_tree’s DAG-based ordering in favour of a strict total order — more on why below.

# The Dual Mechanism Design

Surelock uses two mechanisms that cover complementary cases. Neither overlaps with the other:

Mechanism
When
Acquisition
Enforcement
LockSet
Multiple locks at the
same
 level
Atomic (all-or-nothing)
Runtime sort by stable ID
Levels (
Level<N>
)
Locks at
different
 levels
Incremental
Compile-time trait bounds

## Same Level:LockSet

EveryMutexgets a unique, monotonically-increasingLockIdfrom a globalAtomicU64counter at creation time. The ID livesinsidethe mutex and moves with it — no address stability needed.

When you need multiple locks at the same level,LockSetpre-sorts them by ID at construction time. Two threads requesting the same locks in opposite order both sort to the same acquisition order. No cycle can form.

let
 alice
 =
 Mutex
::
new
(
"alice"
);

let
 bob
 =
 Mutex
::
new
(
"bob"
);



// Regardless of argument order, acquisition order is deterministic

let
 set
 =
 LockSet
::
new
((
&
alice
,
&
bob
));



key_handle
.
scope
(
|
key
|
 {

 let
 (
a
,
b
)
=
 set
.
lock
(
key
);

 // Both locked, no deadlock possible

});

Thread A Thread B

 │ │

 ▼ ▼

LockSet::new((&acct_1, &acct_2)) LockSet::new((&acct_2, &acct_1))

 │ │

 ▼ ▼

sorted: [acct_1, acct_2] sorted: [acct_1, acct_2]

 │ │

 ├─ takes acct_1 lock │

 │ ├─ waits for acct_1 lock

 ├─ takes acct_2 lock │

 │ │

 ~~~~~~~~~~~~~~~~~~~~~~~TIME PASSES~~~~~~~~~~~~~~~~~~~~~~~

 │ │

 ├─ release acct_2 │

 │ │ (still waiting for lock 1 first)

 ├─ release acct_1 │

 │ ├─ takes acct_1 lock

 │ ├─ takes acct_2 lock

 │ │

 ▼ ▼

 OK OK (no cycle possible)

## Different Levels: Compile-Time Ordering

When locks representdifferent kinds of resources— say a config guard vs. a per-account lock — you assign them to different levels.Level<N>types withLockAftertrait bounds enforce strictly ascending acquisition:

use
 surelock
::
level
::
{
Level
, lock_scope};

type
 Config
 =
 Level
<
1
>;

type
 Account
 =
 Level
<
2
>;



let
 config
:
 Mutex
<
_
,
Config
>
=
 Mutex
::
new
(AppConfig
::
default
());

let
 account
:
 Mutex
<
_
,
Account
>
=
 Mutex
::
new
(
Balance
(
0
));



lock_scope
(
|
key
|
 {

 let
 (
cfg
,
key
)
=
 config
.
lock
(
key
);
// Level 1 -> ok

 let
 (
acct
,
key
)
=
 account
.
lock
(
key
);
// Level 2 after 1 -> ok

 // account.lock(key) then config.lock(key) -> compile error

});

The key (ha!) isMutexKey. It’s consumed by eachlock()call and re-emitted at the new level. If you try to go backwards — trying to acquire aLevel<3>followed by aLevel<1>— theLockAfterbound isn’t satisfied and the compiler rejects it with a helpful (custom) error message.

### Why a Total Order, Not a DAG?

This is a deliberate design decision.lock_treeuses a DAG, which lets you declare that branches A and B areindependent— neither needs to come before the other. Sounds great, but it has a subtle problem: if thread 1 acquires A then B, and thread 2 acquires B then A, and both orderings are valid in the DAG, you have a deadlock that the compiler happily approved.

Locks are sorted in a total order by(Level, LockId). A total order is more restrictive but actually sound. If two locks participate in the system at all, their relative order is fixed. We could in concept linearise a DAG (much like we do in many op-based CRDTs), but that is harder to reason about and adds a lot of additional machinery.

# Getting a Key

Both mechanisms —LockSetand levels — useMutexKey. You can think of the key as a kind of scope: it’s consumed by eachlock()call and re-emitted at the new level. It’s branded with an invariant lifetime (same technique asstd::thread::scope) so it can’t escape the closure, and it’s!Sendso it stays on the thread that created it.

There are two ways to get one: implicit and explicit.

## Implicit:lock_scope

I expect this is what most people will reach for. Onstd,lock_scopehandles all the setup internally — you just write:

use
 surelock
::
{
Mutex
, lock_scope};



let
 data
 =
 Mutex
::
new
(
42
);



lock_scope
(
|
key
|
 {

 let
 (
guard
,
key
)
=
 data
.
lock
(
key
);

 assert_eq!
(
*
guard
,
42
);

});

Under the hood,lock_scopemanages athread_local!KeyHandlefor you. TheKeyHandle’sscopemethod takes&mut self, which means the borrow checker prevents nested scopes — you can’t start a new locking scope while one is already active.

## Explicit:LocksmithandKeyVoucher

Forno_std, embedded, or cases where you want tighter control over which core gets which capability, there’s a fully explicit chain:

Locksmith Program-wide singleton (!Send)

 |

 v

KeyVoucher Transferable to other threads (Send)

 |

 v

KeyHandle Per-thread / claimed once (!Send)

 |

 v

MutexKey<'scope> Branded lifetime, consumed-and-re-emitted

 |

 v

MutexGuard RAII access to the data

TheLocksmithis a singleton — enforced viaAtomicBool, not convention. It is!Clone,!Copy, and importantly!Sendas an extra layer of safety to prevent it from being duplicated among threads. It issuesKeyVouchers whichareSend, so you can distribute keys among threads during setup. A voucher gets redeemed on its destination thread for aKeyHandle, which is!Sendand stays put.

This might sound like a lot of ceremony, but it’s mainly type machinery to enforce safety invariants. On bare metal with nothread_local!, youwantthis level of control — you’re deciding at init time exactly which core gets a key, and the type system makes sure no one else can conjure one out of thin air.

# Diagrams

Here is an example diagrammed out. You’ll notice that the lock levels are in a strict compile-time sequence, but the lock IDs — being assigned at runtime — show up in arbitrary order. This is completely fine; they merely need to beconsistentacross all callers.

Here we start with the root key that can lock any level (“above level 0”). We acquire locks across two levels, sort them by ID, and acquire them in that order (for the reasons described in the timeline earlier). This consumes the root key, and emits a key that can lock above level 2. In the future, we can lock level 3 and onwards, until we unlock and recover the earlier keys.

 Key{Level > 0}
 │
 │
┌─────────Level 1───────────┐ ▼
│ │ ┌─────────LockSet────────┐
│ │ │ │
│ lock_1 │ │ │
│ lock_3 ────┼─────────────┼────▶ lvl_1-lock_3 ─────┼────────▶ guard-3
│ │ │ │
│ lock_8 ────────────┼─────────────┼────▶ lvl_1-lock_8 ─────┼────────▶ guard-8
│ │ │ │
└───────────────────────────┘ │ │
 │ │
┌─────────Level 2───────────┐ │ │
│ │ │ │
│ │ │ │
│ lock_5 ────┼─────────────┼────▶ lvl_2-lock_5 ─────┼────────▶ guard-5
│ │ │ │
│ lock_7 │ │ │
│ │ │ │
└───────────────────────────┘ └────────────────────────┘
 │
 │
 ▼
 Key{Level > 2}
 │
 │
 ▼
┌─────────Level 3───────────┐ ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
│ │ │
│ │ │
│ lock_2 ─ ┼ ─ ─ ─ ─ ─ ─▶ │
│ lock_4 │ │
│ │ │
│ lock_6 │ │
│ │ │
└───────────────────────────┘ └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

# no_stdand Embedded

The crate is#![no_std]at its core, requiring onlyalloc. Onstd, you getStdMutexas the default backend andlock_scopeas a convenient entry point. Onno_std, you bring your own backend — anything implementinglock_api::RawMutexworks via a blanket impl behind a feature flag.

It also supports targets without native CAS (e.g. Cortex-M0) viaportable-atomicandcritical-sectionfeatures. I think this matters because the places where youmostneed deadlock freedom — bare-metal firmware with no debugger attached — are exactly the places where current tooling helps you least.

# Escape Hatch

Real-world code sometimes needs to break the rules. Surelock providesMutex::unchecked_lock()behind theescape-hatchfeature flag. It’s feature-gated so that if you use it, it’s visible inCargo.toml, it’s grep-able, and it stands out in code review. IMO this is better than the alternative: developers silently reaching forparking_lot::Mutexalongside their surelock mutexes and defeating the whole system.

# Wrap Up

Deadlocks are a solved problemin theory— we’ve known how to prevent them since 1971. The challenge is making that prevention ergonomic enough that people actually use it. Surelock is my attempt at that: lean into Rust’s type system to make the correct thing the easy thing, and make the wrong thing a compiler error.

The crate ison Codebergand published tocrates.io. Dual-licensed MIT/Apache-2.0. I’d love feedback, especially from folks working on embedded orno_stdtargets — that’s where I’ve had the least real-world testing so far.

## Footnotes

1. With one exception: acquring the SAME mutex atomically more than once. I’m not happy that this edge case exists, but also it’s not common that you would try to take the same mutex alongside itself.↩
2. thiserroris the sole runtime dependency, which is zero-cost at runtime. The defaultstdbackend wrapsstd::sync::Mutexdirectly.↩
3. Technicallyaffinein Rust’s type system (can be dropped but not duplicated), but the intent is linear — you’re expected to use it, and the API is designed so that dropping it early just ends the scope.↩
