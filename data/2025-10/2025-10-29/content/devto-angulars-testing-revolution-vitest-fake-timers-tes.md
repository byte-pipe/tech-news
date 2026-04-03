---
title: 'Angular''s Testing Revolution: Vitest, Fake Timers & Testronaut - DEV Community'
url: https://dev.to/rainerhahnekamp/angulars-testing-revolution-vitest-fake-timers-testronaut-2bnj
site_name: devto
fetched_at: '2025-10-29T11:09:30.492539'
original_url: https://dev.to/rainerhahnekamp/angulars-testing-revolution-vitest-fake-timers-testronaut-2bnj
author: Rainer Hahnekamp
date: '2025-10-27'
description: As we wrap up the year, the Angular world has been abuzz with big topics like Signal Forms. But... Tagged with angular, webdev, testing, vitest.
tags: '#angular, #webdev, #testing, #vitest'
---

As we wrap up the year, the Angular world has been abuzz with big topics like Signal Forms. But quietly, and quite unexpectedly, a testing revolution is arriving with Angular version 21 - just two weeks away (at the time of this writing).

In this article, we’ll explore how Vitest is stepping in as the new default testing framework, how async testing will change for new zoneless Angular applications, and how Testronaut will make its debut as the community version of Playwright Component Testing for Angular.

Table of Contents

1. Vitest
2. Fake Timers
3. Testronaut

## 🧪 Vitest

The most important thing about Vitest is not Vitest itself 🙃.

For nearly two years, Angular developers have been in a kind oftesting limbo.

With Karma’s deprecation in 2023, teams were left wondering which direction to go. Should they hold on to the old tools - sticking with Jasmine and hoping for a replacement in the form of the Modern Web Test Runner? Others had already switched to Jest - especially in Nx monorepos - but weren’t sure whether to stay or move on to Vitest (which was also available in Nx).

Thislack of a clear choicemade it very tough to plan for the future, especially for new projects 🤷.

Now, with the announcement that Vitest will be available as a testing framework starting with Angular 21, there's relief.

Developers finally have a decision and know what to pick.

The uncertainty is gone, and that's the most important aspect!

Vitest was the right decision.

Compared to Jasmine - and even Jest - Vitest brings a powerful API,a rich, forward-looking ecosystem that’s TypeScript-first and fully supports ESM. It also includes a browser mode, which means tests can run in a real browser environment.

That was one key point for the Angular team. They want to move forward - butnot force everyone to rewrite. So it was crucial to choose a testing framework that, like Jasmine/Karma, runs tests in the browser.

Even though the APIs differ - especially around async testing and mocking - the environment stays the same.

Vitest is powered by Vite. And while Angular’s implementation doesn’t go all-in on Vitest (Angular builds the tests instead of Vite), it still closes the gap to the Vite ecosystem.

In the end, Angular doesn’t want to be an outsider anymore. It wants tobecome part of the broader JavaScript ecosystem- and Vite is the key for that.

The image shows that Jest is still dominating but Vitest has the momentum

Here's just a selection of Vitest's powerful API:

Polling Feature

expect.pollaccepts a function which will return a value. Vitest will continue executing the assertion until it runs into a timeout or the matches is successful.

import

{

expect
,

test

}

from

'
vitest
'
;

test
(
'
wait for the asynchronous tasks to end
'
,

async
()

=>

{


let

a

=

1
;


setTimeout
(()

=>

a
++
);


Promise
.
resolve
().
then
(()

=>

a
++
);


await

expect
.
poll
(()

=>

a
).
toBe
(
3
);

});

Enter fullscreen mode

Exit fullscreen mode

Soft Assertions

Soft Assertions execute all expects within a test, even if one fails. In case, one expect fails, the whole test is marked failed.

test
(
'
resource
'
,

()

=>

{


const

todoResource

=

getSomeResource
();


expect
.
soft
(
resource
.
status
()).
toBe
(
'
resolved
'
);


expect
.
soft
(
resource
.
error
()).
toBeUndefined
();


expect
.
soft
(
resource
.
hasValue
()).
toBe
(
true
);

})

Enter fullscreen mode

Exit fullscreen mode

Test Context

Test context allows us to add different functionality to a test. See it as some kind of "dependency injection" for tests.

In the example below, we add awaitfunction, which is then available as a parameter within the test.

context.ts

import

{

test

as

base

}

from

'
vitest
'
;

interface

Fixtures

{


wait
:

(
timeout
?:

number
)

=>

Promise
<
void
>
;

}

export

const

test

=

base
.
extend
<
Fixtures
>
({


wait
:

async
({},

use
)

=>

{


await

use
(


(
timeout

=

0
)

=>


new

Promise
<
void
>
((
resolve
)

=>

setTimeout
(
resolve
,

timeout
)),


);


},

});

Enter fullscreen mode

Exit fullscreen mode

async.spec.ts

import

{

test

}

from

'
./context
'
;

import

{

expect

}

from

'
vitest
'
;

test
(
'
wait for the asynchronous task
'
,

async
({

wait

})

=>

{


let

a

=

1
;


setTimeout
(()

=>

a
++
);


Promise
.
resolve
().
then
(()

=>

a
++
);


expect
(
a
).
toBe
(
1
);


await

wait
();


expect
(
a
).
toBe
(
3
);

});

Enter fullscreen mode

Exit fullscreen mode

You can already use Vitest in Angular 20. For example, thisrepositoryalready uses it. Just runng test- just like you would with Jasmine/Karma - and it will execute the tests.

Starting with Angular 21, when you runng new, you’ll be prompted to choose between Vitest and Jasmine, withVitest being the default.

Migration schematics will also be available to help you migrate from Jasmine.

Vitest running behind ng test in Angular 20

For more information, check outMatthieu Riegler’s LinkedIn post- and I’m pretty sure more resources will follow.

And of course, check out the official Vitest website:https://vitest.dev

## 👋 FarewellwaitForAsync()&fakeAsync()

Until now, Zone.js has played a central role in how Angular handles asynchronous behavior.

### How Zone.js-testing "worked"

Zone.js patches timing functions likesetTimeoutandsetInterval. This allows it to observe and track async tasks across the framework. However, one thing Zone.js could never patch was the native JavaScriptPromise- since it's a language-level construct, not just a method.

In Angular testing, two functions built on Zone.js helped manage async behavior:fakeAsync()andwaitForAsync().

waitForAsync()waits for all scheduled asynchronous tasks to finish before continuing with the test.

it
(
'
should wait for async tasks to end
'
,

waitForAsync
(()

=>

{


let

a

=

1
;


setTimeout
(()

=>

{


a
++
;


expect
(
a
).
toBe
(
2
);


});

}));

Enter fullscreen mode

Exit fullscreen mode

This worked in most cases, but had limitations - especially when assertions were made after async tasks, or if asetTimeoutwas scheduled far into the future (e.g. 1 second or more). In such cases, the test would simply wait.

it
(
'
should wait for too long
'
,

waitForAsync
(()

=>

{


let

a

=

1
;


setTimeout
(()

=>

{


a
++
;


expect
(
a
).
toBe
(
2
);


},

10
_000
);

}));

it
(
'
should fail to assert an asynchronous task
'
,

waitForAsync
(()

=>

{


let

a

=

1
;


setTimeout
(()

=>

{


a
++
;


});


expect
(
a
).
toBe
(
2
);

}));

Enter fullscreen mode

Exit fullscreen mode

fakeAsync()became the preferred solution. It gives developers full control over the async queue viatick()andflush().tick()simulates the passage of time, whileflush()executes all pending timers except for periodic ones likesetInterval.

it
(
'
runs all asynchronous tasks immediately (synchronously) after flush
'
,

fakeAsync
(()

=>

{


let

a

=

1
;


setTimeout
(()

=>

{


a
++
;


},

5
_000
);


setTimeout
(()

=>

{


a
++
;


},

5
_000
);


flush
();


expect
(
a
).
toBe
(
3
);

}));

it
(
'
runs asynchronous tasks tick by tick 😉
'
,

fakeAsync
(()

=>

{


let

a

=

1
;


setTimeout
(()

=>

{


a
++
;


},

5
_000
);


setTimeout
(()

=>

{


a
++
;


},

5
_000
);


tick
(
5
_000
);


expect
(
a
).
toBe
(
2
);


tick
(
5
_000
);


expect
(
a
).
toBe
(
3
);

}));

Enter fullscreen mode

Exit fullscreen mode

### Zoneless testing

Starting with Angular 20.2, thezoneless mode became stable. In Angular 21, it's the new default.

That also meansfakeAsync()andwaitForAsync()will stop working unless you explicitly enable Zone.js.

As unfortunate as it is, this means tests relying on these two utilities will have to be rewritten — not entirely, but at least the parts that manage asynchronous tasks.

### ⏱ Alternatives in Vitest (and Jest)

Luckily, the testing frameworks offer their own mechanisms for async control.

In Vitest and Jest, this feature is calledfake timers.

Fake timers mock async APIs likesetTimeout,setInterval, and more. They work very similar towaitForAsyncandfakeAsyncbut are not exactly the same.

* runAllTimers(): Runs all asynchronous tasks, even periodic ones. Also asynchronous tasks triggered by other asynchronous tasks are covered. This is what we know fromflush()with the addition, thatrunAllTimersalso coverssetInterval.
* advanceTimersByTime(ms): Runs all asynchronous tasks within a period of time. Close totick()infakeAsync().
* runOnlyPendingTimers()- runs only currently scheduled timers

We have to enable fake timers explicitly, so that the testing framework can create the mocks first.

Since this is done in abeforeEach, we also need to disable them inafterEach.

describe
(
'
async tasks
'
,

()

=>

{


beforeEach
(()

=>

{


vitest
.
useFakeTimers
();


});


afterEach
(()

=>

{


vitest
.
resetAllMocks
();


});


it
(
'
runs all asynchronous tasks immediately (synchronously)
'
,

()

=>

{


let

a

=

1
;


setTimeout
(()

=>

{


a
++
;


},

5
_000
);


setTimeout
(()

=>

{


a
++
;


},

10
_000
);


vitest
.
runAllTimers
();


expect
(
a
).
toBe
(
3
);


});


it
(
'
runs asynchronous tasks tick by tick 😉
'
,

()

=>

{


let

a

=

1
;


setTimeout
(()

=>

{


a
++
;


},

5
_000
);


setTimeout
(()

=>

{


a
++
;


},

10
_000
);


vitest
.
advanceTimersByTime
(
5
_000
);


expect
(
a
).
toBe
(
2
);


vitest
.
advanceTimersByTime
(
5
_000
);


expect
(
a
).
toBe
(
3
);


});

});

Enter fullscreen mode

Exit fullscreen mode

Not too bad, right?

### Careful with Promises

There was one catch though. As mentioned above, Zone.js didn't compile down to native Promises, because they cannot be mocked. Fake Timers don't do any compilation. So if there is a native Promise, the fakes can't cover them.

it
(
'
fails on Promises
'
,

()

=>

{


let

a

=

1
;


Promise
.
resolve
().
then
(()

=>

a
++
);


vitest
.
runAllTimers
();


expect
(
a
).
toBe
(
2
);

// this will fail

});

Enter fullscreen mode

Exit fullscreen mode

There's also another variation where both Promise and "mockable" timers come together.

it
(
'
fails on Promises 1
'
,

()

=>

{


let

a

=

1
;


setTimeout
(()

=>

Promise
.
resolve
().
then
(()

=>

a
++
));


vitest
.
runAllTimers
();


expect
(
a
).
toBe
(
2
);

});

it
(
'
fails on Promises 2
'
,

()

=>

{


let

a

=

1
;


Promise
.
resolve
().
then
(()

=>

setTimeout
(()

=>

a
++
));


vitest
.
runAllTimers
();


expect
(
a
).
toBe
(
2
);

});

Enter fullscreen mode

Exit fullscreen mode

What to do? We can fallback to the polling or use ourwaitfunction from the test fixtures example above. But there is also a solution for fake timers.

To handle this, fake timers can queue an additional Promise after the real one. Our test can then await that second Promise to ensure all async behavior completes.

Since this is quite common, Vitest provides us fakes for that. They are very easy to remember. In fact, they are the same fakes we had before, just with anAsyncsuffix.

describe
(
'
async tasks
'
,

()

=>

{


beforeEach
(()

=>

{


vitest
.
useFakeTimers
();


});


afterEach
(()

=>

{


vitest
.
resetAllMocks
();


});


it
(
'
succeeds on Promises
'
,

async
()

=>

{


let

a

=

1
;


Promise
.
resolve
().
then
(()

=>

a
++
);


await

vitest
.
runAllTimersAsync
();


expect
(
a
).
toBe
(
2
);


});


it
(
'
succeeds on Promises 1
'
,

async
()

=>

{


let

a

=

1
;


setTimeout
(()

=>

Promise
.
resolve
().
then
(()

=>

a
++
));


await

vitest
.
runAllTimersAsync
();


expect
(
a
).
toBe
(
2
);


});


it
(
'
succeeds on Promises 2
'
,

async
()

=>

{


let

a

=

1
;


Promise
.
resolve
().
then
(()

=>

setTimeout
(()

=>

a
++
));


await

vitest
.
runAllTimersAsync
();


expect
(
a
).
toBe
(
2
);


});

});

Enter fullscreen mode

Exit fullscreen mode

Even if you are using Zone.js, whenever you write a new test, use the fake timers.

## 🧑‍🚀 Testronaut

Let's face it: regardless of whether we use Vitest, Jest, or something else - nothing beats an E2E test. Why?

* Developers canwatch testsrun live in the browser.
* E2E frameworkshandle asynchronous behaviorautomatically. Whether a component is still rendering or waiting on the browser - no problem, the framework’s got you covered.
* Tools liketesting-libraryrely on plugins to simulate real user events. With E2E frameworks, that's built-in.
* E2E tests don’t just interact with elements because they exist in the DOM - theyensure the element is actually usable: visible, not overlapped, enabled, etc. for real users.

But there’s a downside: E2E frameworks require the whole application to be up and running. Reaching the feature under test often means navigating through the app, which can be cumbersome and slow.

### A Better Way

Cypress Component Testing showed us a better approach. It could compile Angular components, mount them in the browser, and run a full E2E test - but focused on just the component.

That was in 2022. Today, the E2E framework of choice isPlaywright. It supports component testing (CT) - but only for frameworks that fully support Vite.

There was a huge community effort to get Playwright CT working with Angular via Vite. It was fully implemented, working, and promising. But in November 2023, the PR was closed by the Playwright team. They had doubts about the long-term viability of CT in general - and a desire to reduce framework-specific maintenance.

👉Playwright PR comment

### Playwright CT Reloaded

Out of the ashes came Testronaut.

Testronaut is led by Younes Jaaidi (and the author of this article). Younes was part of the original effort to bring Angular CT to Playwright and previously contributed heavily to Cypress CT for Angular.

Testronaut is acommunity-driven Playwright Component Testing runnerfor Angular - but without forcing Angular to compile via Vite. Instead, it leverages theAngular CLI. That means the same build setup and speed you’re used to fromng serve, and no awkward workarounds.

Testronaut mounts a component and lets Playwright do what it does best: run a full, browser-based test with all the realism and async handling you'd expect from a real E2E framework.

And yes - the test code is straightforward. Here’s an example:

test
(
'
should emit an event on click
'
,

async
({

mount
,

page

})

=>

{


await

mount
(
ClickMeComponent
,

{

inputs
:

{

clickMeLabel
:

'
Press me
'

}

});


await

page
.
getByRole
(
'
button
'
,

{

name
:

'
Press me
'

}).
click
();


await

expect
(
page
.
getByText
(
'
Lift Off!
'
)).
toBeVisible
();

});

Enter fullscreen mode

Exit fullscreen mode

Testronaut is already available, though we recommend waiting until the schematics (ng add @testronaut/angular) are released for a smoother experience.

More info:https://testronaut.dev

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
