---
title: Learn Valid Parentheses, Reverse Linked List, and Tree Max Depth with Step-by-Step Visualization in DSA View View 👀👀 - DEV Community
url: https://dev.to/nyaomaru/learn-valid-parentheses-reverse-linked-list-and-tree-max-depth-with-step-by-step-visualization-in-3o09
site_name: devto
content_file: devto-learn-valid-parentheses-reverse-linked-list-and-tr
fetched_at: '2026-08-29T15:28:59.948430'
original_url: https://dev.to/nyaomaru/learn-valid-parentheses-reverse-linked-list-and-tree-max-depth-with-step-by-step-visualization-in-3o09
author: nyaomaru
date: '2026-08-26'
description: Hoi hoi! I’m @nyaomaru, a frontend engineer who struggles to make game sounds. 😿 Have you used DSA... Tagged with typescript, algorithms, opensource, dsa.
tags: '#typescript, #algorithms, #opensource, #dsa'
---

Curated progression from stacks to recursion

Hoi hoi!

I’m@nyaomaru, a frontend engineer who struggles to make game sounds. 😿

Have you usedDSA View Viewalready? 👀👀

Features a timeline to step backward mid-loop

 nyaomaru
 

 nyaomaru
 
 
 

nyaomaru

 Follow
 

Jul 15

## I Built a Tool to Visualize DSA. Let’s Learn Together! (DSA View View 👀👀)

#
showdev

#
typescript

#
dsa

#
react

63
 reactions

Comments

 33
 comments

 7 min read
 

DSA View View allows you to understand DSA by visualizing how your implementation actually runs.

In the previous article, we looked at:

* Two Sum
* Binary Search
* Bubble Sort

Visualizing execution logic changes mental models

 nyaomaru
 

 nyaomaru
 
 
 

nyaomaru

 Follow
 

Aug 19

## Is Learning DSA Boring? Let's Use DSA View View 👀👀 (Two Sum, Binary Search, and Bubble Sort)

#
dsa

#
typescript

#
opensource

#
learning

50
 reactions

Comments

 9
 comments

 7 min read
 

This time, let's try three more classic problems:

* Valid Parentheses
* Reverse Linked List
* Maximum Depth of Binary Tree

These problems introduce three very different ideas:

Stack
Pointer manipulation
Recursion

Enter fullscreen mode

Exit fullscreen mode

And all three can become confusing when we only stare at the final code.

So let's view what actually happens. 👀

I'm still learning DSA too, so let's learn together! 😸

## 🥞 Valid Parentheses

Let's start withValid Parentheses.

Suppose we have this string:

()[]{}

Enter fullscreen mode

Exit fullscreen mode

Every opening bracket has a matching closing bracket.

So this is valid. ✅

But this

([)]

Enter fullscreen mode

Exit fullscreen mode

is not valid. ❌

Why?

Because the brackets close in the wrong order.

(
 [
)
 ]

Enter fullscreen mode

Exit fullscreen mode

The[should be closed before the(.

So how can we keep track of that order?

### Use a Stack

Astackfollows a simple rule:

The last thing we put in is the first thing we take out.

This is calledLIFO(Last In / First Out)

Imagine stacking plates.

 🍽️ ← remove first
 🍽️
 🍽️

Enter fullscreen mode

Exit fullscreen mode

The last plate we put on top is the first one we can take.

Parentheses work in the same way.

If we see:

(
[
{

Enter fullscreen mode

Exit fullscreen mode

then the brackets must close in reverse order

}
]
)

Enter fullscreen mode

Exit fullscreen mode

So a stack is a very natural fit.

Here is the implementation:

function
 
isValid
(
s
:
 
string
):
 
boolean
 
{

 
const
 
stack
:
 
string
[]
 
=
 
[];

 
const
 
pairs
:
 
Record
<
string
,
 
string
>
 
=
 
{

 
"
)
"
:
 
"
(
"
,

 
"
]
"
:
 
"
[
"
,

 
"
}
"
:
 
"
{
"
,

 
};

 
for 
(
const
 
char
 
of
 
s
)
 
{

 
if 
(
char
 
===
 
"
(
"
 
||
 
char
 
===
 
"
[
"
 
||
 
char
 
===
 
"
{
"
)
 
{

 
stack
.
push
(
char
);

 
continue
;

 
}

 
if 
(
stack
.
length
 
===
 
0
)
 
return
 
false
;

 
const
 
target
 
=
 
stack
.
pop
();

 
if 
(
target
 
!==
 
pairs
[
char
])
 
{

 
return
 
false
;

 
}

 
}

 
return
 
stack
.
length
 
===
 
0
;

}

Enter fullscreen mode

Exit fullscreen mode

The important part is what happens tostack.

Let's use

([])

Enter fullscreen mode

Exit fullscreen mode

At first

stack = []

Enter fullscreen mode

Exit fullscreen mode

We see

(

Enter fullscreen mode

Exit fullscreen mode

It's an opening bracket.

Push it.

stack = ["("]

Enter fullscreen mode

Exit fullscreen mode

Next,

[

Enter fullscreen mode

Exit fullscreen mode

Push again.

stack = ["(", "["]

Enter fullscreen mode

Exit fullscreen mode

Then,

]

Enter fullscreen mode

Exit fullscreen mode

This is a closing bracket.

What should it close?

[

Enter fullscreen mode

Exit fullscreen mode

And what is currently on top of the stack?

[

Enter fullscreen mode

Exit fullscreen mode

Perfect. ✅

So we remove it.

stack = ["("]

Enter fullscreen mode

Exit fullscreen mode

Finally,

)

Enter fullscreen mode

Exit fullscreen mode

It should close

(

Enter fullscreen mode

Exit fullscreen mode

The top of the stack is also

(

Enter fullscreen mode

Exit fullscreen mode

Pop!

stack = []

Enter fullscreen mode

Exit fullscreen mode

We reached the end with an empty stack.

Valid! 🎉

### What About an Invalid Example?

Consider

([)]

Enter fullscreen mode

Exit fullscreen mode

We start the same way.

(
↓
stack = ["("]

[
↓
stack = ["(", "["]

Enter fullscreen mode

Exit fullscreen mode

Then we find

)

Enter fullscreen mode

Exit fullscreen mode

A)needs

(

Enter fullscreen mode

Exit fullscreen mode

But the top of our stack is

[

Enter fullscreen mode

Exit fullscreen mode

They don't match.

expected: (
actual: [

Enter fullscreen mode

Exit fullscreen mode

So we immediately know the string is invalid.

### Complexity

We walk through the string once.

Time: O(n)
Space: O(n)

Enter fullscreen mode

Exit fullscreen mode

In the worst case, the stack may contain all opening brackets.

### 👀 Let's View View It

This is where the stack becomes much easier to understand.

When we only read.

stack
.
push
(
char
);

Enter fullscreen mode

Exit fullscreen mode

And

stack
.
pop
();

Enter fullscreen mode

Exit fullscreen mode

It can be easy to lose track of what is actually inside the stack.

Especially with something like.

({[]})

Enter fullscreen mode

Exit fullscreen mode

What is on top right now?

Which opening bracket are we trying to close?

Instead of remembering everything in our head, we can follow the stack changing step by step.

dsa-view-view.vercel.app

Conceptually, we can see:

(
↓
[(]

{
↓
[(, {]

[
↓
[(, {, []

]
↓
[(, {]

}
↓
[(]

)
↓
[]

Enter fullscreen mode

Exit fullscreen mode

That's the whole idea.

Remember the opening brackets, and always match the most recent one first.

Stack suddenly feels much less mysterious. 🥞😸

## 🔗 Reverse Linked List

Next, let's reverse a linked list.

Suppose we have

1 → 2 → 3 → 4 → 5

Enter fullscreen mode

Exit fullscreen mode

We want

5 → 4 → 3 → 2 → 1

Enter fullscreen mode

Exit fullscreen mode

At first glance, this sounds simple.

Just reverse it!

But linked lists are a little different from arrays.

With an array, the values live in positions like

0 1 2 3 4
↓ ↓ ↓ ↓ ↓
1 2 3 4 5

Enter fullscreen mode

Exit fullscreen mode

A linked list instead consists of nodes pointing to the next node.

1 → 2 → 3 → 4 → 5 → null

Enter fullscreen mode

Exit fullscreen mode

Each arrow matters. To reverse the list, we need to reverse those arrows.

1 ← 2 ← 3 ← 4 ← 5

Enter fullscreen mode

Exit fullscreen mode

And this is where things can get confusing.

Because if we change an arrow too early...

we may lose the rest of the list. 😿

### Three Important Variables

A common iterative solution uses three variables

prev
current
next

Enter fullscreen mode

Exit fullscreen mode

Here is the implementation:

function
 
reverseList
(
head
:
 
ListNode
 
|
 
null
):
 
ListNode
 
|
 
null
 
{

 
let
 
prev
:
 
ListNode
 
|
 
null
 
=
 
null
;

 
let
 
current
 
=
 
head
;

 
while 
(
current
 
!==
 
null
)
 
{

 
const
 
next
 
=
 
current
.
next
;

 
current
.
next
 
=
 
prev
;

 
prev
 
=
 
current
;

 
current
 
=
 
next
;

 
}

 
return
 
prev
;

}

Enter fullscreen mode

Exit fullscreen mode

It's short.

But there is a lot happening inside these few lines.

Let's follow it carefully.

We start with

1 → 2 → 3 → null

Enter fullscreen mode

Exit fullscreen mode

And

prev = null
current = 1

Enter fullscreen mode

Exit fullscreen mode

### Step 1: Save the Next Node

First

const
 
next
 
=
 
current
.
next
;

Enter fullscreen mode

Exit fullscreen mode

So

next = 2

Enter fullscreen mode

Exit fullscreen mode

Why do we need this?

Because we're about to change

1 → 2

Enter fullscreen mode

Exit fullscreen mode

If we change that arrow without remembering2, we lose access to the rest of the list.

So first

Save where we need to go next.

### Step 2: Reverse the Arrow

Now

current
.
next
 
=
 
prev
;

Enter fullscreen mode

Exit fullscreen mode

Originally

1 → 2

Enter fullscreen mode

Exit fullscreen mode

Butprevis

null

Enter fullscreen mode

Exit fullscreen mode

So now

1 → null

Enter fullscreen mode

Exit fullscreen mode

The first arrow has been reversed.

### Step 3: Moveprev

Next

prev
 
=
 
current
;

Enter fullscreen mode

Exit fullscreen mode

So

prev = 1

Enter fullscreen mode

Exit fullscreen mode

### Step 4: Movecurrent

Finally

current
 
=
 
next
;

Enter fullscreen mode

Exit fullscreen mode

We saved2earlier.

So now

current = 2

Enter fullscreen mode

Exit fullscreen mode

Our state looks like this

null ← 1 2 → 3 → null
 ↑ ↑
 prev current

Enter fullscreen mode

Exit fullscreen mode

Then we do exactly the same thing again.

Save:

next = 3

Enter fullscreen mode

Exit fullscreen mode

Reverse

2 → 1

Enter fullscreen mode

Exit fullscreen mode

Move

prev = 2
current = 3

Enter fullscreen mode

Exit fullscreen mode

Now

null ← 1 ← 2 3 → null
 ↑ ↑
 prev current

Enter fullscreen mode

Exit fullscreen mode

One more time

next = null

Enter fullscreen mode

Exit fullscreen mode

Reverse

3 → 2

Enter fullscreen mode

Exit fullscreen mode

Move

prev = 3
current = null

Enter fullscreen mode

Exit fullscreen mode

And now

null ← 1 ← 2 ← 3
 ↑
 prev

Enter fullscreen mode

Exit fullscreen mode

The loop stops because

current === null

Enter fullscreen mode

Exit fullscreen mode

Andprevis the new head.

So

return
 
prev
;

Enter fullscreen mode

Exit fullscreen mode

Done! 🎉

### Complexity

We visit each node once.

Time: O(n)
Space: O(1)

Enter fullscreen mode

Exit fullscreen mode

We don't create another linked list.

We only move a few pointers.

### 👀 Let's View View It

This is exactly the kind of code that I find difficult to understand by reading alone.

These four lines:

const
 
next
 
=
 
current
.
next
;

current
.
next
 
=
 
prev
;

prev
 
=
 
current
;

current
 
=
 
next
;

Enter fullscreen mode

Exit fullscreen mode

look simple.

But when I first see code like this, my brain starts asking.

Wait.

- Where is current now?
- Did we lose next?
- Which arrow changed?
- What exactly does prev point to?

Enter fullscreen mode

Exit fullscreen mode

😿

dsa-view-view.vercel.app

When we visualize each step, we can actually follow the pointers moving.

prev current
 ↓ ↓
null 1 → 2 → 3

 ↓↓↓

null ← 1 2 → 3
 ↑ ↑
 prev current

 ↓↓↓

null ← 1 ← 2 3
 ↑ ↑
 prev current

 ↓↓↓

null ← 1 ← 2 ← 3
 ↑
 prev

Enter fullscreen mode

Exit fullscreen mode

The algorithm becomes much simpler when we stop thinking of it as four mysterious assignments.

It's really just

Save next
 ↓
Reverse arrow
 ↓
Move prev
 ↓
Move current
 ↓
Repeat

Enter fullscreen mode

Exit fullscreen mode

Nice! 🔗😸

## 🌳 Maximum Depth of Binary Tree

Finally, let's look at a tree.

Consider this binary tree.

 3
 / \
 9 20
 / \
 15 7

Enter fullscreen mode

Exit fullscreen mode

What is its maximum depth?

The longest path from the root to a leaf contains three nodes:

3
↓
20
↓
15

Enter fullscreen mode

Exit fullscreen mode

So the answer is.

3

Enter fullscreen mode

Exit fullscreen mode

How can we calculate that?

### Think About a Smaller Tree

Suppose we are standing at one node.

We don't really need to understand the entire tree at once.

We only need to ask.

How deep is the left subtree?

How deep is the right subtree?

Enter fullscreen mode

Exit fullscreen mode

Then choose the larger one.

And add1for the current node.

That's exactly what this implementation does.

function
 
maxDepth
(
root
:
 
TreeNode
 
|
 
null
):
 
number
 
{

 
if 
(
root
 
===
 
null
)
 
{

 
return
 
0
;

 
}

 
const
 
leftDepth
 
=
 
maxDepth
(
root
.
left
);

 
const
 
rightDepth
 
=
 
maxDepth
(
root
.
right
);

 
return
 
Math
.
max
(
leftDepth
,
 
rightDepth
)
 
+
 
1
;

}

Enter fullscreen mode

Exit fullscreen mode

The important idea is

Math
.
max
(
leftDepth
,
 
rightDepth
)
 
+
 
1
;

Enter fullscreen mode

Exit fullscreen mode

But recursion can feel strange.

When we call

maxDepth
(
root
.
left
);

Enter fullscreen mode

Exit fullscreen mode

where does the current function go?

And how do all those calls eventually become one number?

Let's follow a small example.

 1
 / \
 2 3
 /
4

Enter fullscreen mode

Exit fullscreen mode

We start at

1

Enter fullscreen mode

Exit fullscreen mode

But before1can know its depth, it asks its left child

maxDepth(2)

Enter fullscreen mode

Exit fullscreen mode

Node2asks

maxDepth(4)

Enter fullscreen mode

Exit fullscreen mode

Node4has no children.

So both sides eventually reach

null

Enter fullscreen mode

Exit fullscreen mode

And

maxDepth
(
null
);

Enter fullscreen mode

Exit fullscreen mode

returns

0

Enter fullscreen mode

Exit fullscreen mode

Therefore node4can calculate

max(0, 0) + 1
= 1

Enter fullscreen mode

Exit fullscreen mode

Now we return to node2.

Its left side has depth

1

Enter fullscreen mode

Exit fullscreen mode

Its right side isnull

0

Enter fullscreen mode

Exit fullscreen mode

So

max(1, 0) + 1
= 2

Enter fullscreen mode

Exit fullscreen mode

Now return to node1.

Eventually its right subtree also returns

1

Enter fullscreen mode

Exit fullscreen mode

So node1gets

leftDepth = 2
rightDepth = 1

Enter fullscreen mode

Exit fullscreen mode

And calculates

max(2, 1) + 1
= 3

Enter fullscreen mode

Exit fullscreen mode

Answer

3

Enter fullscreen mode

Exit fullscreen mode

🎉

### The Interesting Part: Going Down and Coming Back Up

This is what makes recursion interesting.

First, the function calls godownthe tree.

1
↓
2
↓
4
↓
null

Enter fullscreen mode

Exit fullscreen mode

But the answers are built while returningback up.

null → 0
4 → 1
2 → 2
1 → 3

Enter fullscreen mode

Exit fullscreen mode

So recursion isn't only

Keep calling the same function.

There are really two directions.

Go down
 ↓
Reach the base case
 ↓
Return values back up

Enter fullscreen mode

Exit fullscreen mode

The base case here is

if 
(
root
 
===
 
null
)
 
{

 
return
 
0
;

}

Enter fullscreen mode

Exit fullscreen mode

Without it, the recursion would have no place to stop.

### Complexity

Every node is visited once.

Time: O(n)

Enter fullscreen mode

Exit fullscreen mode

The recursive call stack depends on the height of the tree.

Space: O(h)

Enter fullscreen mode

Exit fullscreen mode

wherehis the height of the tree.

For a balanced tree, that is roughly

O(log n)

Enter fullscreen mode

Exit fullscreen mode

In the worst case, if the tree looks like a linked list

1
 \
 2
 \
 3
 \
 4

Enter fullscreen mode

Exit fullscreen mode

the depth can become

O(n)

Enter fullscreen mode

Exit fullscreen mode

### 👀 Let's View View It

Recursion is probably my favorite example for visualization.

Because the final implementation is tiny

const
 
leftDepth
 
=
 
maxDepth
(
root
.
left
);

const
 
rightDepth
 
=
 
maxDepth
(
root
.
right
);

return
 
Math
.
max
(
leftDepth
,
 
rightDepth
)
 
+
 
1
;

Enter fullscreen mode

Exit fullscreen mode

But a lot is hidden inside those function calls.

When reading the code, it can feel like

maxDepth()
inside maxDepth()
inside maxDepth()
inside maxDepth()
...

Enter fullscreen mode

Exit fullscreen mode

Where are we now? 😿

dsa-view-view.vercel.app

When we step through the execution, we can follow both parts

Going down

1
↓
2
↓
4
↓
null

Enter fullscreen mode

Exit fullscreen mode

and then

Coming back

null → 0
↓
4 → 1
↓
2 → 2
↓
1 → 3

Enter fullscreen mode

Exit fullscreen mode

That makes the recursive idea much easier to see.

Ask the smaller subproblems for their answers, then use those answers to build the current answer.

🌳😸

## 🧠 What Did We Actually Learn?

These three problems look completely different.

But each one introduces a very useful way of thinking.

### Valid Parentheses

Use a stack when the most recent item needs to be handled first.

What was the last thing I opened?

Enter fullscreen mode

Exit fullscreen mode

### Reverse Linked List

When changing references, save what you still need before breaking the old connection.

Where do I need to go next before I change this pointer?

Enter fullscreen mode

Exit fullscreen mode

### Maximum Depth of Binary Tree

Break a problem into smaller versions of the same problem.

Can I get the answers from my children and build my answer from them?

Enter fullscreen mode

Exit fullscreen mode

This is one reason I like learning these problems together.

The implementations are not very large.

But each one introduces a completely different mental model

Stack
Pointer
Recursion

Enter fullscreen mode

Exit fullscreen mode

And those mental models are much harder to learn than the syntax itself.

Sometimes the code tells uswhat happens.

But I also want to seehow it happens.

I want to view it. 👀👀

## 🎯 Conclusion

In this article, we looked at:

* Valid Parentheses with a stack
* Reverse Linked List with pointer manipulation
* Maximum Depth of Binary Tree with recursion

And more importantly, we followed the state while each algorithm was running.

We watched change the stack.

stack.push() / stack.pop()

Enter fullscreen mode

Exit fullscreen mode

We watched move through a linked list.

prev
current
next

Enter fullscreen mode

Exit fullscreen mode

And we watched recursive calls travel down a tree and return their answers back up.

This is exactly the kind of thing I builtDSA View Viewfor.

dsa-view-view.vercel.app

You can write or load a TypeScript implementation, run it with your own inputs, and move backward and forward through the runtime.

If you are learning DSA too, try viewing one of these problems step by step.

Especially if a solution feels like

I understand every line individually... but somehow I still don't understand the whole thing. 😿

Seeing the runtime may connect those pieces together.

And if there is a DSA problem you want me to cover next, please let me know in the comments!

I still have many algorithms to learn myself. 😸

Let's train our DSA muscles together! 💪

If you like DSA View View, please give it a star ⭐

## nyaomaru/dsa-view-view

### DSA View View allows you to understand DSA to see the data flow. 👀👀 Of course, it's free.

# DSA View View

DSA View View turns TypeScript algorithm functions into step-by-step visual
stories. 👀👀

Write code, run it with structured inputs, and see the arrays, matrices
trees, lists, stacks, pointers, and return values move as the function executes.

It is built for those moments when reading the code is not enough and you want
toviewwhy the answer changes.

## Why Try It?

* 🧠Step through real TypeScriptPaste or edit a function, validate it, then run the exact code in the browser.
* 🧩Views that match the dataArrays become bars, matrices become grids, trees become node graphs, linked lists become chains, and two-pointer area problems get their own visual view.
* 🌳DSA-friendly inputs out of the boxTreeNode,ListNode,MinHeap,MaxHeap,PriorityQueue, nested arrays
matrices, strings, numbers, and class-style inputs are supported without
ceremony.
* 🔎39 built-in examplesSearch by name, browse…

View on GitHub

See you in the next article!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse