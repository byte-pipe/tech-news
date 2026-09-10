---
title: Learn Trapping Rain Water, Top K Frequent and Selection Sort with Step-by-Step Visualization in DSA View View 👀👀 - DEV Community
url: https://dev.to/nyaomaru/learn-trapping-rain-water-top-k-frequent-and-selection-sort-with-step-by-step-visualization-in-dsa-1flg
site_name: devto
content_file: devto-learn-trapping-rain-water-top-k-frequent-and-selec
fetched_at: '2026-09-10T14:49:56.801138'
original_url: https://dev.to/nyaomaru/learn-trapping-rain-water-top-k-frequent-and-selection-sort-with-step-by-step-visualization-in-dsa-1flg
author: nyaomaru
date: '2026-09-09'
description: Hoi hoi! I’m @nyaomaru, a frontend engineer who has been obsessed with ramen lately. 😸🍜 Have you... Tagged with typescript, algorithms, opensource, dsa.
tags: '#typescript, #algorithms, #opensource, #dsa'
---

Makes dry algorithms fun with cool visuals

Hoi hoi!

I’m@nyaomaru, a frontend engineer who has been obsessed with ramen lately. 😸🍜

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

64
 reactions

Comments

 33
 comments

 7 min read
 

DSA View View allows you to understand DSA by visualizing how your implementation actually runs.

In the previous articles, we looked at problems like:

* Two Sum
* Binary Search
* Bubble Sort
* Valid Parentheses
* Reverse Linked List
* Maximum Depth of Binary Tree
* Number of Islands
* Invert Binary Tree
* Course Schedule

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

51
 reactions

Comments

 9
 comments

 7 min read
 

Curated progression from stacks to recursion

 nyaomaru
 

 nyaomaru
 
 
 

nyaomaru

 Follow
 

Aug 26

## Learn Valid Parentheses, Reverse Linked List, and Tree Max Depth with Step-by-Step Visualization in DSA View View 👀👀

#
typescript

#
algorithms

#
opensource

#
dsa

77
 reactions

Comments

 5
 comments

 9 min read
 

Readers praise the recursive swap explanation

 nyaomaru
 

 nyaomaru
 
 
 

nyaomaru

 Follow
 

Sep 2

## Learn Number of Islands, Invert Binary Tree, and Course Schedule with Step-by-Step Visualization in DSA View View 👀👀

#
typescript

#
dsa

#
opensource

#
webdev

64
 reactions

Comments

 14
 comments

 12 min read
 

This time, let's try three more problems:

* Trapping Rain Water
* Top K Frequent Elements
* Selection Sort

These three problems introduce some very useful ways of thinking

Shrink a problem from both sides
Count first, then organize by frequency
Repeatedly select the next value

Enter fullscreen mode

Exit fullscreen mode

Once again, the implementations are not necessarily huge.

But there are several changing values that we need to keep in our heads.

So instead of only reading the final code,

Let's view what actually happens. 👀👀

## 🌧️ Trapping Rain Water

Let's start withTrapping Rain Water.

Suppose we have these heights

[0, 1, 0, 2, 1, 0, 1, 3]

Enter fullscreen mode

Exit fullscreen mode

If we draw them as walls, it looks roughly like this.

 █
 █ █
 █ █ █ █ █
-----------------
0 1 0 2 1 0 1 3

Enter fullscreen mode

Exit fullscreen mode

Rain falls from above.

Some water escapes.

But some water becomes trapped between taller walls.

For example

 █~~~~~~~█
 █~~~█~~~~~~~█
-----------------

Enter fullscreen mode

Exit fullscreen mode

So the question is

How much water can be trapped?

At first, I found this problem quite confusing. 😿

Because the amount of water above one position depends on walls somewhere else.

So what information do we actually need?

### How Much Water Fits Above One Position?

Imagine this position

left wall right wall
 █ █
 █ x █
 █ █ █

Enter fullscreen mode

Exit fullscreen mode

The water level cannot be higher than the shorter side.

So the maximum possible water level is

Math
.
min
(
leftMax
,
 
rightMax
);

Enter fullscreen mode

Exit fullscreen mode

Then we subtract the current height.

Conceptually:

water = min(leftMax, rightMax) - currentHeight

Enter fullscreen mode

Exit fullscreen mode

That's the basic idea.

But do we really need to calculate both sides again for every position?

No.

We can usetwo pointers.

### Two Pointers

Here is the implementation.

function
 
trap
(
height
:
 
number
[]):
 
number
 
{

 
let
 
left
 
=
 
0
;

 
let
 
right
 
=
 
height
.
length
 
-
 
1
;

 
let
 
leftMax
 
=
 
0
;

 
let
 
rightMax
 
=
 
0
;

 
let
 
water
 
=
 
0
;

 
while 
(
left
 
<=
 
right
)
 
{

 
if 
(
height
[
left
]
 
<=
 
height
[
right
])
 
{

 
if 
(
height
[
left
]
 
>=
 
leftMax
)
 
{

 
leftMax
 
=
 
height
[
left
];

 
}
 
else
 
{

 
water
 
+=
 
leftMax
 
-
 
height
[
left
];

 
}

 
left
++
;

 
}
 
else
 
{

 
if 
(
height
[
right
]
 
>=
 
rightMax
)
 
{

 
rightMax
 
=
 
height
[
right
];

 
}
 
else
 
{

 
water
 
+=
 
rightMax
 
-
 
height
[
right
];

 
}

 
right
--
;

 
}

 
}

 
return
 
water
;

}

Enter fullscreen mode

Exit fullscreen mode

There are several important values.

left
right
leftMax
rightMax
water

Enter fullscreen mode

Exit fullscreen mode

This is exactly the kind of code where I understand every variable individually,

but then lose track of all of them together. 😹

Let's follow a smaller example.

[2, 0, 1, 3]

Enter fullscreen mode

Exit fullscreen mode

### Start From Both Ends

At first

left = 0
right = 3

[2, 0, 1, 3]
 ↑ ↑
left right

Enter fullscreen mode

Exit fullscreen mode

The heights are:

height[left] = 2
height[right] = 3

Enter fullscreen mode

Exit fullscreen mode

Since

2 <= 3

Enter fullscreen mode

Exit fullscreen mode

we process the left side.

There is a wall with height2.

So

leftMax = 2

Enter fullscreen mode

Exit fullscreen mode

Then moveleft.

[2, 0, 1, 3]
 ↑ ↑
 left right

Enter fullscreen mode

Exit fullscreen mode

### Now We Can Trap Water

The current height is

0

Enter fullscreen mode

Exit fullscreen mode

But we already know there is a wall of height2on the left.

And the right side is currently at least as high as that.

So this position can hold

leftMax - height[left]
= 2

Enter fullscreen mode

Exit fullscreen mode

Therefore

water = 2

Enter fullscreen mode

Exit fullscreen mode

Move again.

[2, 0, 1, 3]
 ↑ ↑
 left right

Enter fullscreen mode

Exit fullscreen mode

Now

height[left] = 1
leftMax = 2

Enter fullscreen mode

Exit fullscreen mode

So

2 - 1 = 1

Enter fullscreen mode

Exit fullscreen mode

One more unit of water.

water = 3

Enter fullscreen mode

Exit fullscreen mode

Eventually we reach the final wall.

Done! 🎉

### Why Can We Process the Shorter Side?

This part is the important idea.

Suppose

height[left] <= height[right]

Enter fullscreen mode

Exit fullscreen mode

Then we already know there is a wall on the right that is at least as tall as the current left wall.

So for the current left position, the limiting factor is the best wall we have seen from the left.

That's why we can safely calculate

leftMax
 
-
 
height
[
left
];

Enter fullscreen mode

Exit fullscreen mode

without knowing every future wall.

The same logic works from the other side.

If

height[right] < height[left]

Enter fullscreen mode

Exit fullscreen mode

we process the right side usingrightMax.

So the algorithm keeps shrinking the unknown area

L → → → ← ← ← R

Enter fullscreen mode

Exit fullscreen mode

until everything has been processed.

### Complexity

Each pointer only moves across the array once.

Time: O(n)
Space: O(1)

Enter fullscreen mode

Exit fullscreen mode

### 👀 Let's View View It

This problem is a perfect example of why I like visualization.

The code contains

left
right
leftMax
rightMax
water

Enter fullscreen mode

Exit fullscreen mode

And they all change at different times.

When I only read

water
 
+=
 
leftMax
 
-
 
height
[
left
];

Enter fullscreen mode

Exit fullscreen mode

I might ask:

* Why are we usingleftMaxhere?
* What isrightMaxright now?
* Why did we moveleftinstead ofright?
* How much water have we already counted?
* Which part of the array is still unprocessed?

😿

dsa-view-view.vercel.app

Step by step, we can actually watch the search area shrink.

L R
↓ ↓
[2, 0, 1, 3]

 L R
 ↓ ↓
[2, 0, 1, 3]

 L R
 ↓ ↓
[2, 0, 1, 3]

Enter fullscreen mode

Exit fullscreen mode

And at the same time

leftMax
rightMax
water

Enter fullscreen mode

Exit fullscreen mode

keep changing.

The algorithm is really asking

Which side can I safely solve right now?

Then it solves that side and moves inward. 🌧️😸

## 🔢 Top K Frequent Elements

Next, let's find theTop K Frequent Elements.

Suppose we have

[1, 1, 1, 2, 2, 3]

Enter fullscreen mode

Exit fullscreen mode

and

k = 2

Enter fullscreen mode

Exit fullscreen mode

How often does each number appear?

1 → 3 times
2 → 2 times
3 → 1 time

Enter fullscreen mode

Exit fullscreen mode

So the two most frequent values are

[1, 2]

Enter fullscreen mode

Exit fullscreen mode

Simple enough.

But how should we implement it?

### First, Count Everything

The first thing we need is frequency.

We can use aMap.

const
 
frequency
 
=
 
new
 
Map
<
number
,
 
number
>
();

Enter fullscreen mode

Exit fullscreen mode

Then count each value.

for 
(
const
 
num
 
of
 
nums
)
 
{

 
frequency
.
set
(
num
,
 
(
frequency
.
get
(
num
)
 
??
 
0
)
 
+
 
1
);

}

Enter fullscreen mode

Exit fullscreen mode

For

[1, 1, 1, 2, 2, 3]

Enter fullscreen mode

Exit fullscreen mode

we get

frequency = {
 1 → 3
 2 → 2
 3 → 1
}

Enter fullscreen mode

Exit fullscreen mode

Nice.

But we still need thetop K.

Of course, we could sort everything by frequency.

But there is another interesting approach.

### Use Frequency as an Index

The maximum possible frequency is

nums.length

Enter fullscreen mode

Exit fullscreen mode

So we can create buckets.

const
 
buckets
:
 
number
[][]
 
=
 
Array
.
from
({
 
length
:
 
nums
.
length
 
+
 
1
 
},
 
()
 
=>
 
[]);

Enter fullscreen mode

Exit fullscreen mode

The index represents frequency.

For example

bucket[1] = values appearing 1 time
bucket[2] = values appearing 2 times
bucket[3] = values appearing 3 times

Enter fullscreen mode

Exit fullscreen mode

For our example:

frequency = {
 1 → 3
 2 → 2
 3 → 1
}

Enter fullscreen mode

Exit fullscreen mode

the buckets become

index 0 → []
index 1 → [3]
index 2 → [2]
index 3 → [1]

Enter fullscreen mode

Exit fullscreen mode

That's pretty interesting. 👀👀

Instead of asking

What is the frequency of this number?

we reverse the relationship

Which numbers have this frequency?

### Implementation

Here is the full implementation:

function
 
topKFrequent
(
nums
:
 
number
[],
 
k
:
 
number
):
 
number
[]
 
{

 
const
 
frequency
 
=
 
new
 
Map
<
number
,
 
number
>
();

 
for 
(
const
 
num
 
of
 
nums
)
 
{

 
frequency
.
set
(
num
,
 
(
frequency
.
get
(
num
)
 
??
 
0
)
 
+
 
1
);

 
}

 
const
 
buckets
:
 
number
[][]
 
=
 
Array
.
from
({
 
length
:
 
nums
.
length
 
+
 
1
 
},
 
()
 
=>
 
[]);

 
for 
(
const
 
[
num
,
 
count
]
 
of
 
frequency
)
 
{

 
buckets
[
count
].
push
(
num
);

 
}

 
const
 
result
:
 
number
[]
 
=
 
[];

 
for 
(
let
 
count
 
=
 
buckets
.
length
 
-
 
1
;
 
count
 
>=
 
0
;
 
count
--
)
 
{

 
for 
(
const
 
num
 
of
 
buckets
[
count
])
 
{

 
result
.
push
(
num
);

 
if 
(
result
.
length
 
===
 
k
)
 
{

 
return
 
result
;

 
}

 
}

 
}

 
return
 
result
;

}

Enter fullscreen mode

Exit fullscreen mode

Let's follow it.

### Step 1: Build the Frequency Map

Start

frequency = {}

Enter fullscreen mode

Exit fullscreen mode

Read the first1. And another one and another...

1 → 1
1 → 2
1 → 3

Enter fullscreen mode

Exit fullscreen mode

Then2. And another one.

1 → 3
2 → 1
2 → 2

Enter fullscreen mode

Exit fullscreen mode

Finally3.

1 → 3
2 → 2
3 → 1

Enter fullscreen mode

Exit fullscreen mode

Done.

### Step 2: Put Values Into Buckets

Now

buckets
[
count
].
push
(
num
);

Enter fullscreen mode

Exit fullscreen mode

For

1 → 3

Enter fullscreen mode

Exit fullscreen mode

we do

buckets[3].push(1)

Enter fullscreen mode

Exit fullscreen mode

For

2 → 2

Enter fullscreen mode

Exit fullscreen mode

we do

buckets[2].push(2)

Enter fullscreen mode

Exit fullscreen mode

And

3 → 1

Enter fullscreen mode

Exit fullscreen mode

becomes

buckets[1].push(3)

Enter fullscreen mode

Exit fullscreen mode

So

0: []
1: [3]
2: [2]
3: [1]

Enter fullscreen mode

Exit fullscreen mode

### Step 3: Read From Highest Frequency

We want themost frequentvalues.

So don't start at0. Start from the end.

3 → [1]
2 → [2]
1 → [3]

Enter fullscreen mode

Exit fullscreen mode

Take1.

result = [1]

Enter fullscreen mode

Exit fullscreen mode

We still need one more. Move down.

Take2.

result = [1, 2]

Enter fullscreen mode

Exit fullscreen mode

Now

result.length === k

Enter fullscreen mode

Exit fullscreen mode

So return.

Done! 🎉

### Why Is This Interesting?

I like this solution because the second structure changes our perspective.

TheMapsays

value → frequency

Enter fullscreen mode

Exit fullscreen mode

The buckets say

frequency → values

Enter fullscreen mode

Exit fullscreen mode

Same information. But different direction.

And suddenly finding the most frequent values becomes easy.

We just walk backward through the buckets.

### Complexity

We count every number once.

We distribute every unique number into a bucket.

Then we walk through the buckets.

Time: O(n)
Space: O(n)

Enter fullscreen mode

Exit fullscreen mode

### 👀 Let's View View It

There are two transformations happening here.

First

nums
 ↓
frequency Map

Enter fullscreen mode

Exit fullscreen mode

Then

frequency Map
 ↓
buckets

Enter fullscreen mode

Exit fullscreen mode

Then

buckets
 ↓
result

Enter fullscreen mode

Exit fullscreen mode

Reading the final implementation, it can be easy to miss why we're building two different data structures.

dsa-view-view.vercel.app

With the runtime visible, we can follow the data changing shape.

[1, 1, 1, 2, 2, 3]
 ↓ count
1 → 3
2 → 2
3 → 1
 ↓ bucket
1: [3]
2: [2]
3: [1]
 ↓ highest first
[1, 2]

Enter fullscreen mode

Exit fullscreen mode

That's the part I like.

We don't magically find the top K.

We reorganize the information until the answer becomes easy to read. 🔢😸

## 👉 Selection Sort

Finally, let's sort something again!

We already looked atBubble Sortin a previous article.

This time, let's trySelection Sort.

Suppose we have

[5, 3, 4, 1, 2]

Enter fullscreen mode

Exit fullscreen mode

We want

[1, 2, 3, 4, 5]

Enter fullscreen mode

Exit fullscreen mode

Selection Sort follows a very simple idea

Find the smallest remaining value and move it to the front.

Then repeat.

### First Pass

Start

[5, 3, 4, 1, 2]
 ↑
 i

Enter fullscreen mode

Exit fullscreen mode

Assume the first value is currently the smallest.

minIndex = 0

Enter fullscreen mode

Exit fullscreen mode

Then scan everything to the right.

5 vs 3

Enter fullscreen mode

Exit fullscreen mode

3is smaller.

So:

minIndex = 1

Enter fullscreen mode

Exit fullscreen mode

Then:

3 vs 4

Enter fullscreen mode

Exit fullscreen mode

No change.

Then

3 vs 1

Enter fullscreen mode

Exit fullscreen mode

1is smaller.

minIndex = 3

Enter fullscreen mode

Exit fullscreen mode

Finally

1 vs 2

Enter fullscreen mode

Exit fullscreen mode

Still1.

So the smallest value is at index3.

Swap

[5, 3, 4, 1, 2]
 ↑ ↑
 i min

Enter fullscreen mode

Exit fullscreen mode

↓

[1, 3, 4, 5, 2]

Enter fullscreen mode

Exit fullscreen mode

Now the first position is finished.

[1 | 3, 4, 5, 2]
 ↑
sorted

Enter fullscreen mode

Exit fullscreen mode

### Repeat

Next, start from index1.

[1 | 3, 4, 5, 2]
 ↑
 i

Enter fullscreen mode

Exit fullscreen mode

Find the smallest value in

[3, 4, 5, 2]

Enter fullscreen mode

Exit fullscreen mode

That's2.

Swap.

[1, 2 | 4, 5, 3]

Enter fullscreen mode

Exit fullscreen mode

Again.

Find the smallest remaining value.

3

Enter fullscreen mode

Exit fullscreen mode

Eventually

[1, 2, 3, 4, 5]

Enter fullscreen mode

Exit fullscreen mode

Sorted! 🎉

### Implementation

function
 
selectionSort
(
nums
:
 
number
[]):
 
number
[]
 
{

 
for 
(
let
 
i
 
=
 
0
;
 
i
 
<
 
nums
.
length
 
-
 
1
;
 
i
++
)
 
{

 
let
 
minIndex
 
=
 
i
;

 
for 
(
let
 
j
 
=
 
i
 
+
 
1
;
 
j
 
<
 
nums
.
length
;
 
j
++
)
 
{

 
if 
(
nums
[
j
]
 
<
 
nums
[
minIndex
])
 
{

 
minIndex
 
=
 
j
;

 
}

 
}

 
if 
(
minIndex
 
!==
 
i
)
 
{

 
[
nums
[
i
],
 
nums
[
minIndex
]]
 
=
 
[
nums
[
minIndex
],
 
nums
[
i
]];

 
}

 
}

 
return
 
nums
;

}

Enter fullscreen mode

Exit fullscreen mode

There are two important indexes.

i
minIndex

Enter fullscreen mode

Exit fullscreen mode

And also

j

Enter fullscreen mode

Exit fullscreen mode

which searches through the unsorted area.

### Why Is It Called Selection Sort?

Because each passselectsthe smallest remaining value.

Find smallest
 ↓
Select it
 ↓
Move it to the front
 ↓
Repeat

Enter fullscreen mode

Exit fullscreen mode

That's basically the whole algorithm.

### Complexity

For every position, we search through the remaining values.

So

Time: O(n²)

Enter fullscreen mode

Exit fullscreen mode

We sort the array in place.

Space: O(1)

Enter fullscreen mode

Exit fullscreen mode

Selection Sort is not something I would normally choose for sorting a huge production dataset. 😹

But as a learning algorithm, it is wonderfully visual.

### 👀 Let's View View It

The implementation contains nested loops.

for 
(
let
 
i
 
=
 
0
;
 
i
 
<
 
nums
.
length
 
-
 
1
;
 
i
++
)
 
{

 
let
 
minIndex
 
=
 
i
;

 
for 
(
let
 
j
 
=
 
i
 
+
 
1
;
 
j
 
<
 
nums
.
length
;
 
j
++
)
 
{

Enter fullscreen mode

Exit fullscreen mode

Reading it, I might lose track of:

* Which area is already sorted?
* Where isi?
* Where isj?
* What doesminIndexcurrently point to?
* When exactly does the swap happen?

dsa-view-view.vercel.app

When we visualize it, the basic pattern becomes obvious.

[5, 3, 4, 1, 2]
 ↑
 smallest

[1 | 3, 4, 5, 2]
 ↑
 smallest

[1, 2 | 4, 5, 3]

Enter fullscreen mode

Exit fullscreen mode

The algorithm is continuously growing a finished area from left to right.

That's Selection Sort.

Pick the smallest remaining value.

Put it next. And repeat. 🍥😸

## 🧠 What Did We Actually Learn?

Again, these three problems look completely different.

But each one introduces a useful way of thinking.

### Trapping Rain Water

Use information from both sides to decide which part can already be solved safely.

Which side do I know enough about right now?

Enter fullscreen mode

Exit fullscreen mode

### Top K Frequent Elements

Sometimes counting the data is only the first step.

Reorganize it into a structure where the answer becomes easy to retrieve.

Can I reorganize this information around what I actually need?

Enter fullscreen mode

Exit fullscreen mode

### Selection Sort

Build the answer one permanent position at a time.

What value belongs in this position next?

Enter fullscreen mode

Exit fullscreen mode

So this time we saw

Two pointers
Frequency buckets
Selection

Enter fullscreen mode

Exit fullscreen mode

Three different mental models again.

And just like the previous problems, the difficult part is often not the syntax.

It's the changing state.

Which pointer moved?
What is the maximum now?
What is inside the Map?
Which bucket changed?
Where is minIndex?
Which part is already finished?

Enter fullscreen mode

Exit fullscreen mode

That's a lot to keep in our heads.

So instead, I want toview it. 👀👀

## 🎯 Conclusion

In this article, we looked at:

* Trapping Rain Water with two pointers
* Top K Frequent Elements with frequency buckets
* Selection Sort

And more importantly, we followed how their state changes while they run.

For Trapping Rain Water, we watched two pointers move inward whileleftMax,rightMax, andwaterchanged.

left → ← right

Enter fullscreen mode

Exit fullscreen mode

For Top K Frequent Elements, we watched the same data change representation.

array
 ↓
frequency Map
 ↓
buckets
 ↓
result

Enter fullscreen mode

Exit fullscreen mode

For Selection Sort, we watched the sorted area grow one position at a time.

This is exactly the kind of thing I builtDSA View Viewfor.

dsa-view-view.vercel.app

You can write or load a TypeScript implementation, run it with your own inputs, and move backward and forward through the runtime.

If you are learning DSA too, try viewing one of these problems step by step.

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

 View full discussion (11 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse