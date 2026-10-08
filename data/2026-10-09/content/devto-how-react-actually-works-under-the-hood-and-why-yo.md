---
title: How React Actually Works Under the Hood (And Why Your Mental Model Might Be Wrong) - DEV Community
url: https://dev.to/smtahosin/how-react-actually-works-under-the-hood-and-why-your-mental-model-might-be-wrong-12b8
site_name: devto
content_file: devto-how-react-actually-works-under-the-hood-and-why-yo
fetched_at: '2026-10-09T10:16:24.317206'
original_url: https://dev.to/smtahosin/how-react-actually-works-under-the-hood-and-why-your-mental-model-might-be-wrong-12b8
author: S M Tahosin
date: '2026-10-08'
description: Have you ever written a line of React code, looked at the output in your browser, and thought:... Tagged with react, javascript, webdev, discuss.
tags: '#discuss, #react, #javascript, #webdev'
---

Relates the universal rookie state-logging mistake

Have you ever written a line of React code, looked at the output in your browser, and thought:"Wait... why did it do that?"

Here is the classic code snippet that every single React developer writes at least once:

function
 
Counter
()
 
{

 
const
 
[
count
,
 
setCount
]
 
=
 
useState
(
0
);

 
function
 
handleClick
()
 
{

 
setCount
(
count
 
+
 
1
);

 
console
.
log
(
count
);

 
}

 
return
 
<
button
 
onClick
=
{
handleClick
}
>
Count: 
{
count
}
</
button
>;

}

Enter fullscreen mode

Exit fullscreen mode

You click the button. The button text updates on the screen from 0 to 1. But in your browser console, it logs:

0

Enter fullscreen mode

Exit fullscreen mode

Not 1. Zero.

At first, you think it is just a tiny delay. So you click it again. The button updates to 2, but the console logs 1. It is always one step behind.

Why?

When I first ran into this years ago, someone on a forum told me:"Oh,setStateis asynchronous."And for months, I accepted that answer. But that answer is not the whole truth. In fact, thinking of state as a "variable that updates asynchronously" is the exact mental model that causes hundreds of bugs in production apps.

Today, we are going to look under the hood. No fluff. No textbook definitions. We are going to look at the real data structures, the Fiber tree, why hook rules exist, and how React actually turns your JavaScript into pixels on a screen.

Grab your favorite coffee. Let's dig in.

## The Mental Model Trap: What Beginners Think vs Reality

When most of us learn React, our brain builds a very simple model of how it works:

1. You callsetCount(1)
2. React goes into your HTML
3. It changes<button>Count: 0</button>to<button>Count: 1</button>
4. Done.

If this were how React worked, React would be terrible. Directly searching and mutating the browser DOM on every state update is slow and expensive. The browser has to recalculate styles, recalculate layout geometry (reflow), and repaint pixels.

Instead, React does something fundamentally different:

React does not update the DOM when you call setState. It schedules a calculation to run in the future.

Let's break down the three distinct phases that happen every single time your component updates.

## The Three Phases: Trigger, Render, Commit

Think of React like a high-end restaurant kitchen.

* Trigger Phase: The customer places an order.
* Render Phase: The chef cooks the food and plates it on the counter (in private, inside the kitchen).
* Commit Phase: The waiter takes the dish and sets it on the customer's table.

If the customer changes their mind halfway through cooking, the chef can throw away the half-cooked plate without the customer ever seeing it. But once the plate hits the table, that is the commit.

Here is how that maps to React:

[User Interaction]
 |
 v
1. TRIGGER PHASE (dispatchSetState queues an update request)
 |
 v
2. RENDER PHASE (Pure JS calculations: calls your component, diffs Fiber tree)
 |
 v
3. COMMIT PHASE (Synchronous DOM mutations: document.createElement, appendChild)
 |
 v
4. BROWSER PAINT (The browser repaints the pixels on your monitor)

Enter fullscreen mode

Exit fullscreen mode

Let's walk through each one in detail.

### 1. The Trigger Phase

When you callsetCount(count + 1), your component function does not immediately run again.

Instead, React creates anUpdate Objectand puts it into an update queue attached to that component's internal representation. React marks this component as "dirty" and schedules work with the React Scheduler.

If you click a button three times rapidly, or update three different state variables inside the same event handler, React batches them together. It does not run the kitchen three times for three breadsticks. It collects the whole order first.

### 2. The Render Phase (Pure JavaScript)

This is the phase that confuses people the most because of the name.

When developers hear "render", they think of the screen drawing pixels. In React,rendering just means calling your component function.

React callsCounter(). Your function runs from top to bottom and returns JSX.

Now, what is JSX?

return
 
<
button
 
className
=
"btn"
>
Click me
</
button
>;

Enter fullscreen mode

Exit fullscreen mode

Under the hood, the compiler (Babel or Vite) turns that JSX into a regular JavaScript function call:

return
 
React
.
createElement
(
'
button
'
,
 
{
 
className
:
 
'
btn
'
 
},
 
'
Click me
'
);

Enter fullscreen mode

Exit fullscreen mode

AndReact.createElement()simply returns a plain, lightweight JavaScript object:

{

 
type
:
 
'
button
'
,

 
props
:
 
{

 
className
:
 
'
btn
'
,

 
children
:
 
'
Click me
'

 
},

 
key
:
 
null
,

 
ref
:
 
null

}

Enter fullscreen mode

Exit fullscreen mode

That is all a "Virtual DOM node" is. It is just a plain JavaScript object describing what the UI should look like. It has no connection to the real browser DOM yet.

React takes this newly returned object tree and compares it to the previous object tree. This comparison is calledReconciliation.

React asks:"Did thetypechange? No, still a button. DidclassNamechange? No, still 'btn'. Did the text change? Yes, from '0' to '1'."

React notes down a small patch instruction:Update button text to 1.

### 3. The Commit Phase

Now that React knows the exact minimum set of changes required, it enters the Commit Phase.

This phase is synchronous and cannot be interrupted. React reaches into the real DOM using native browser APIs:

domNode
.
textContent
 
=
 
'
1
'
;

Enter fullscreen mode

Exit fullscreen mode

Only the specific text node that changed gets touched. The rest of the DOM tree is completely untouched.

Once the commit phase finishes and layout effects run, the browser engine takes over and paints the updated pixels onto your monitor.

## Why Hook Order Matters: The Fiber Linked List

Have you ever wondered why React has that strict, almost annoying rule:

"Do not call Hooks inside loops, conditions, or nested functions."

If you break this rule, your console explodes with a terrifying error:

Error: Rendered fewer hooks than expected. This may be caused by an accidental early return statement.

Enter fullscreen mode

Exit fullscreen mode

Why does this happen? Does React look up your state by variable name?

const
 
[
name
,
 
setName
]
 
=
 
useState
(
"
Dan
"
);

const
 
[
age
,
 
setAge
]
 
=
 
useState
(
25
);

Enter fullscreen mode

Exit fullscreen mode

When you writeconst [name, setName], JavaScript does not tell React the word"name". The variable namenameis completely local to your function. React has no idea what you named it.

So how does React know that the firstuseStatebelongs tonameand the second one belongs toage?

React stores your hooks as a singly-linked list on the component's Fiber node.

Every component on your screen is represented internally by aFiberNodeobject. On that Fiber node, there is a property calledmemoizedState.

When your component renders for the first time, React builds a chain of hook objects:

FiberNode (<UserProfile />)
 |
 v
memoizedState ──> [ Hook 0: useState ('Dan') ]
 │
 ▼ (next)
 [ Hook 1: useEffect (fetchData) ]
 │
 ▼ (next)
 [ Hook 2: useState (25) ]
 │
 ▼ (next)
 null

Enter fullscreen mode

Exit fullscreen mode

On every subsequent render, React does not create a new list. It simply sets an internal pointer calledworkInProgressHookto the very first hook in the list:

1. You calluseState(): React reads Hook 0 ('Dan'). Advances pointer to Hook 1.
2. You calluseEffect(): React reads Hook 1. Advances pointer to Hook 2.
3. You calluseState(): React reads Hook 2 (25). Advances pointer to null.

Now look at what happens if you put a hook inside anifstatement:

function
 
UserProfile
({
 
isLoggedIn
 
})
 
{

 
const
 
[
name
,
 
setName
]
 
=
 
useState
(
"
Dan
"
);
 
// Hook 0

 
if 
(
isLoggedIn
)
 
{

 
useEffect
(()
 
=>
 
{
 
// Hook 1 (Conditional!)

 
fetchUserData
();

 
},
 
[]);

 
}

 
const
 
[
age
,
 
setAge
]
 
=
 
useState
(
25
);
 
// Hook 2

 
return
 
<
div
>
{
name
}
, 
{
age
}
</
div
>;

}

Enter fullscreen mode

Exit fullscreen mode

ImagineisLoggedInwastrueon the first render. React created three hook records:[name, effect, age].

On the second render,isLoggedInbecomesfalse.

1. Line 2 callsuseState(): React reads Hook 0 (name). Pointer advances to Hook 1.
2. Line 4 condition is false!useEffectis skipped.
3. Line 10 callsuseState(): React reads Hook 1! But Hook 1 was supposed to be the effect object, not youragestate!

The data is completely scrambled. React detects that the number of hooks called does not match the linked list, throws an error, and halts execution before it corrupts your data.

This is why hook order must remain 100% stable across every single render.

## The Snapshot Mental Model: Why State is a Constant

Let's return to the mystery we started with:

function
 
Counter
()
 
{

 
const
 
[
count
,
 
setCount
]
 
=
 
useState
(
0
);

 
function
 
handleClick
()
 
{

 
setCount
(
count
 
+
 
1
);

 
console
.
log
(
count
);
 
// Prints 0!

 
}

 
return
 
<
button
 
onClick
=
{
handleClick
}
>
{
count
}
</
button
>;

}

Enter fullscreen mode

Exit fullscreen mode

To truly understand this, stop thinking ofcountas a variable that changes over time.

Instead, understand this rule:

In any single render of your component, props and state are constants.

When React calls your component function the first time, it is effectively executing:

// Render #1

function
 
Counter
()
 
{

 
const
 
count
 
=
 
0
;
 
// Fixed constant for this entire execution!

 
function
 
handleClick
()
 
{

 
setCount
(
0
 
+
 
1
);

 
console
.
log
(
0
);
 
// It literally logs 0

 
}

 
return
 
<
button
 
onClick
=
{
handleClick
}
>
0
<
/button>
;

}

Enter fullscreen mode

Exit fullscreen mode

Inside that function call,countis0. It will never be anything other than0inside that specific execution.

When you callsetCount(count + 1), you are not changing the localcountvariable. You cannot change aconst!

You are telling React:"Hey React, when you get around to running my component again, please give me1for count."

React schedules a new render. When that new render runs a few milliseconds later, React callsCounter()again. But this is a completely brand new function call:

// Render #2 (A fresh function execution)

function
 
Counter
()
 
{

 
const
 
count
 
=
 
1
;
 
// Fixed constant for THIS execution!

 
function
 
handleClick
()
 
{

 
setCount
(
1
 
+
 
1
);

 
console
.
log
(
1
);

 
}

 
return
 
<
button
 
onClick
=
{
handleClick
}
>
1
<
/button>
;

}

Enter fullscreen mode

Exit fullscreen mode

Every single render has its owncount, its own event handlers, and its own local scope. This is the power of JavaScript closures.

### The Async Trap

Once you understand snapshots, you will instantly understand bugs like this:

function
 
Chat
()
 
{

 
const
 
[
message
,
 
setMessage
]
 
=
 
useState
(
""
);

 
function
 
handleSend
()
 
{

 
setTimeout
(()
 
=>
 
{

 
alert
(
"
Sent message: 
"
 
+
 
message
);

 
},
 
3000
);

 
}

 
return 
(

 
<
div
>

 
<
input
 
value
=
{
message
}
 
onChange
=
{
e
 
=>
 
setMessage
(
e
.
target
.
value
)
}
 
/>

 
<
button
 
onClick
=
{
handleSend
}
>
Send after 3 seconds
</
button
>

 
</
div
>

 
);

}

Enter fullscreen mode

Exit fullscreen mode

Try this:

1. Type"Hello"into the input.
2. Click "Send after 3 seconds".
3. Immediately change the input text to"Goodbye".
4. Wait for the alert.

What does the alert say?

It says:Sent message: Hello.

Why? Because thehandleSendfunction was created during the render wheremessagewas"Hello". ThesetTimeoutcallback closed over that snapshot. Even though the input on screen updated, the callback was holding onto the photograph of the state at the moment you clicked the button.

If you ever actually need to read the current live value inside an asynchronous callback without waiting for a re-render, that is exactly whatuseRefis for:

const
 
messageRef
 
=
 
useRef
(
message
);

messageRef
.
current
 
=
 
message
;
 
// Always points to latest value

Enter fullscreen mode

Exit fullscreen mode

## Why Components Re-Render: The Cascade Myth

Ask five developers why a React component re-renders, and at least three of them will say:

"A component re-renders when its props change."

This is one of the most common myths in frontend development.

Let's test it:

function
 
Parent
()
 
{

 
const
 
[
count
,
 
setCount
]
 
=
 
useState
(
0
);

 
return 
(

 
<
div
>

 
<
button
 
onClick
=
{
()
 
=>
 
setCount
(
count
 
+
 
1
)
}
>
Increment
</
button
>

 
<
ExpensiveChild
 
/>

 
</
div
>

 
);

}

function
 
ExpensiveChild
()
 
{

 
console
.
log
(
"
ExpensiveChild re-rendered!
"
);

 
return
 
<
p
>
I take 50ms to render.
</
p
>;

}

Enter fullscreen mode

Exit fullscreen mode

Notice that<ExpensiveChild />takeszero props. It has no state. Nothing passed to it changes.

Click the "Increment" button inParent.

DoesExpensiveChildre-render?

Yes. Every single time.

Here is the real rule of React rendering:

### The Real Trigger Rule

A component re-renders if and only if:

1. Its own state changed(viauseStateoruseReducer)
2. A Context it subscribes to changed(viauseContext)
3. Its parent component re-rendered

By default, when a parent component re-renders, React recursively re-rendersallof its children, grandchildren, and descendants, regardless of whether their props changed.

Why does React do this? Because in 95% of web apps, calling a JavaScript function to return a couple of virtual DOM objects takes 0.01 milliseconds. React assumes rendering is cheap and safe.

### How to Stop the Cascade Without Overusing useMemo

Beginners often panic when they see child components re-rendering and immediately wrap every single function inuseCallbackand every component inReact.memo.

Before you do that, there is a much cleaner, built-in technique calledComponent Composition.

Look at this refactor:

// 1. Move the state into its own small wrapper

function
 
CounterContainer
({
 
children
 
})
 
{

 
const
 
[
count
,
 
setCount
]
 
=
 
useState
(
0
);

 
return 
(

 
<
div
>

 
<
button
 
onClick
=
{
()
 
=>
 
setCount
(
count
 
+
 
1
)
}
>
Increment: 
{
count
}
</
button
>

 
{
children
}

 
</
div
>

 
);

}

// 2. Pass ExpensiveChild as a child prop

function
 
App
()
 
{

 
return 
(

 
<
CounterContainer
>

 
<
ExpensiveChild
 
/>

 
</
CounterContainer
>

 
);

}

Enter fullscreen mode

Exit fullscreen mode

When you click the increment button insideCounterContainer,CounterContainerre-renders.

ButExpensiveChilddoes NOT re-render!

Why? Because<ExpensiveChild />was created insideApp, not insideCounterContainer. ToCounterContainer,childrenis just an existing prop object that has not changed reference (prevProps.children === nextProps.children). React sees the identical object reference and skips rendering the entire child subtree!

ZeroReact.memo. ZerouseCallback. Just clean component architecture.

## Why Keys Matter: The List Diffing Mystery

Have you ever rendered a list of inputs in React, deleted the first item, and watched the input text stay behind on the wrong row?

function
 
TodoList
()
 
{

 
const
 
[
items
,
 
setItems
]
 
=
 
useState
([
'
Buy milk
'
,
 
'
Walk dog
'
,
 
'
Read book
'
]);

 
function
 
removeFirst
()
 
{

 
setItems
(
items
.
slice
(
1
));

 
}

 
return 
(

 
<
div
>

 
<
button
 
onClick
=
{
removeFirst
}
>
Delete First
</
button
>

 
<
ul
>

 
{
items
.
map
((
item
,
 
index
)
 
=>
 
(

 
// BAD: using index as key

 
<
li
 
key
=
{
index
}
>

 
<
input
 
defaultValue
=
{
item
}
 
/>

 
</
li
>

 
))
}

 
</
ul
>

 
</
div
>

 
);

}

Enter fullscreen mode

Exit fullscreen mode

You click "Delete First".

You expect "Buy milk" to disappear, and the first input to show "Walk dog".

Instead, the input still says "Buy milk", but the third input disappears!

Why does this happen?

React's diffing algorithm compares children by two things:Element TypeandKey.

When you use array indices as keys:

* On Render 1:Key0->Buy milkKey1->Walk dogKey2->Read book
* Key0->Buy milk
* Key1->Walk dog
* Key2->Read book
* On Render 2 (after removing 'Buy milk'):Key0->Walk dogKey1->Read book
* Key0->Walk dog
* Key1->Read book

React compares the old key0with the new key0. Both have key0. Both are<li><input /></li>.

React says:"Great! Key 0 is the same element. I will keep the existing DOM node and its internal state."

Because the<input />has local browser DOM state (the text you typed), React keeps the old input box and does not update it. Then React looks at Key2. Key2is missing in the new list, so React deletes the third DOM node!

### The Golden Rule of Keys

Keys are not just there to silence the yellow React warning in your browser console.

A key is a persistent identity for a component across renders.

When you give an element a stable, unique key (likekey={item.id}):

1. React matches the exact item even if its position moves from index 0 to index 10.
2. Reordering a list simply moves DOM nodes instead of destroying and recreating them.
3. Component state stays attached to the correct data item.

## Build Your Own Mini-React in 25 Lines of Code

The best way to solidify your mental model of React is to see how simple the core idea really is.

Open your browser's developer console (F12) right now, paste this code, and press Enter:

// A 25-line mental model of React's state engine

const
 
MiniReact
 
=
 
(()
 
=>
 
{

 
let
 
hooks
 
=
 
[];

 
let
 
currentHook
 
=
 
0
;

 
function
 
useState
(
initialValue
)
 
{

 
const
 
hookIndex
 
=
 
currentHook
;

 
hooks
[
hookIndex
]
 
=
 
hooks
[
hookIndex
]
 
!==
 
undefined
 
?
 
hooks
[
hookIndex
]
 
:
 
initialValue
;

 
const
 
setState
 
=
 
(
newValue
)
 
=>
 
{

 
hooks
[
hookIndex
]
 
=
 
newValue
;

 
render
();
 
// Trigger re-render

 
};

 
currentHook
++
;

 
return
 
[
hooks
[
hookIndex
],
 
setState
];

 
}

 
function
 
render
(
Component
)
 
{

 
if 
(
Component
)
 
MiniReact
.
activeComponent
 
=
 
Component
;

 
currentHook
 
=
 
0
;
 
// Reset pointer for next render pass

 
const
 
output
 
=
 
MiniReact
.
activeComponent
();

 
console
.
log
(
"
Rendered UI:
"
,
 
output
);

 
return
 
output
;

 
}

 
return
 
{
 
useState
,
 
render
 
};

})();

// Try it with a component!

function
 
MyComponent
()
 
{

 
const
 
[
name
,
 
setName
]
 
=
 
MiniReact
.
useState
(
"
Alex
"
);

 
const
 
[
count
,
 
setCount
]
 
=
 
MiniReact
.
useState
(
0
);

 
return
 
{

 
text
:
 
`Hello 
${
name
}
, click count is 
${
count
}
`
,

 
click
:
 
()
 
=>
 
setCount
(
count
 
+
 
1
),

 
changeName
:
 
(
n
)
 
=>
 
setName
(
n
)

 
};

}

// Initial render

let
 
app
 
=
 
MiniReact
.
render
(
MyComponent
);

// Simulate clicking button

app
.
click
();

// Simulate changing name

app
.
changeName
(
"
Sarah
"
);

Enter fullscreen mode

Exit fullscreen mode

Notice what happened in that tiny snippet:

1. hooksis a simple array storing values outside the component.
2. currentHookis an index that resets to 0 before every render.
3. When you calluseState, it reads fromhooks[currentHook]and increments the index.
4. CallingsetStateupdates the array item and triggersrender().

Real React uses a linked list on Fiber nodes with priority queues and concurrent scheduling, but the fundamental architecture is identical to those 25 lines.

There is no magic. It is just arrays, pointers, and functions calling functions.

## The Complete React Mental Model Cheat Sheet

Here is a quick reference table to keep bookmarked:

Question

The Common Myth

What React Actually Does

What does 
setState
 do?

Directly updates the DOM variable

Adds an update to the Fiber queue and schedules a render

Why is 
console.log
 stale?

State update is slow / asynchronous

State is a constant snapshot inside that render's closure

Why can't hooks be conditional?

React searches hooks by variable name

Hooks are stored as an ordered linked list; skipping one corrupts all indexes

When do children re-render?

Only when their props change

Whenever their parent re-renders (unless memoized or passed as children)

What does JSX return?

Real HTML DOM elements

A plain JavaScript object (
React.createElement
)

What is the Commit phase?

Calculating virtual DOM diffs

Synchronously writing calculated DOM mutations to the browser

Why do keys matter?

Just a requirement to stop console warnings

Provides persistent identity so React reuses DOM nodes accurately

## Wrapping Up

When you stop treating React like a black box of magic and start understanding the mechanical pipeline underneath, everything changes:

* You stop writing defensiveuseEffectchains to "sync" state.
* You stop being surprised whenconsole.loglogs the previous value.
* You know exactly why and when your components re-render.
* You write code that runs faster and has fewer bugs.

The next time you see someone scratching their head oversetStateor hook errors, you can smile and tell them:

"It is not magic. It is just a snapshot and a linked list."

## Let's Discuss!

I would love to hear from you in the comments:

1. What was the first React behavior that completely broke your brain when you were starting out?
2. Have you ever been burned by the array index key bug in production?
3. How do you usually handle unnecessary re-renders in your projects: composition or memoization?

Drop your thoughts below. I read and reply to every comment!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse