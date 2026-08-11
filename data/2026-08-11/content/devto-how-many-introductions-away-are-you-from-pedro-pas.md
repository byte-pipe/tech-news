---
title: How Many Introductions Away Are You From Pedro Pascal? A Practical Introduction to Graph Search - DEV Community
url: https://dev.to/ale3oula/how-many-introductions-away-are-you-from-pedro-pascal-a-practical-introduction-to-graph-search-5bfg
site_name: devto
content_file: devto-how-many-introductions-away-are-you-from-pedro-pas
fetched_at: '2026-08-11T20:02:34.846947'
original_url: https://dev.to/ale3oula/how-many-introductions-away-are-you-from-pedro-pascal-a-practical-introduction-to-graph-search-5bfg
author: Alexandra
date: '2026-08-11'
description: I was watching The Mandalorian the other day when it struck me that I don't know Pedro Pascal, which... Tagged with algorithms, datastructures, webdev.
tags: '#algorithms, #datastructures, #webdev'
---

Explains BFS using celebrity social networks

I was watching The Mandalorian the other day when it struck me that I don't know Pedro Pascal, which is, by itself, very tragic.

But maybe I know someone, who knows someone, who knows someone, ..., who knows Pedro Pascal. Somewhere out there, there is a finite chain of introductions that connects me to him. So the important computer science question we try to solve today is: How many introductions would it take to reach him?

 

We accidentally have invented a graph problem!

### Turn your social life into a graph

Imagine that each person on this earth is anodeand any relationship or acquaintance between two people is anedge:

Alexandra ── Maria ── Sofia ── Pedro
 │
 └── John ── Elena ── Carlos

Enter fullscreen mode

Exit fullscreen mode

This is an unweighted and undirected graph.

* Unweighted means that every connection counts the same. We don't care whether Maria is Sofia's best friend or someone she met once at a cafe.
* Undirected means the relationship is both ways: if Alexandra knows Maria, Maria knows Alexandra.

If we strip the fluff of the original question, it kinda changes from "How do I meet Pedro Pascal?" to "Given an unweighted graph, what is the shortest path between node A and node B?", which if you are familiar with trees or graphs it sounds like a BFS (Breadth-First Search).

In code, the simplest way to represent this kind of data is anadjacency list

const
 
graph
 
=
 
{

 
Alexandra
:
 
[
"
Maria
"
,
 
"
John
"
],

 
Maria
:
 
[
"
Alexandra
"
,
 
"
Sofia
"
],

 
Sofia
:
 
[
"
Maria
"
,
 
"
Pedro
"
],

 
Pedro
:
 
[
"
Sofia
"
],

 
John
:
 
[
"
Alexandra
"
,
 
"
Elena
"
],

 
Elena
:
 
[
"
John
"
,
 
"
Carlos
"
],

 
Carlos
:
 
[
"
Elena
"
],

};

Enter fullscreen mode

Exit fullscreen mode

### Make our delusions an algorithm

Unfortunately, screaming “DOES ANYONE KNOW PEDRO PASCAL?” into the void isn't an algorithm. It has no order, no memory, and no stopping condition. If you just wander from person to person picking whoever seems interesting, you can easily do this:

Alexandra → Maria → Sofia → Maria → Sofia → Maria → ...

Enter fullscreen mode

Exit fullscreen mode

Because the graph is undirected, Maria connects back to Sofia and Sofia connects back to Maria. Without remembering who we met already, nothing stops us from revisiting the same people forever.

So we basically need two things:

1. A rule for what order to explore people in.
2. A way to remember who we already visited.

That's where a queue and a visited set come in.

### Breadth-first search explained

The key observation for finding the shortest path is this: check everyone one connection away before checking anyone two connections away. This is breadth-first search, and it organizes the graph into levels:

Level 0 Alexandra
 │
 ┌──────┴──────┐
Level 1 Maria John
 │ │
Level 2 Sofia Elena
 │
Level 3 PEDRO 🎉

Enter fullscreen mode

Exit fullscreen mode

BFS will check all my direct friends (level 1), if Pedro isn't there (🥲) will check the direct friends of my direct friends (level 2) and so on. The moment Pedro is found, you know that this is the shortest possible path, because every shorter one has already been checked.

### Put everything together

function
 
introductionsAway
(
graph
,
 
start
,
 
target
)
 
{

 
if 
(
start
 
===
 
target
)
 
return
 
{
 
degrees
:
 
0
,
 
path
:
 
[
start
]
 
};

 
const
 
visited
 
=
 
new
 
Set
([
start
]);

 
const
 
queue
 
=
 
[[
start
,
 
[
start
]]];
 

 
while 
(
queue
.
length
 
>
 
0
)
 
{

 
const
 
[
person
,
 
path
]
 
=
 
queue
.
shift
();

 
for 
(
const
 
friend
 
of
 
graph
[
person
]
 
||
 
[])
 
{

 
if 
(
visited
.
has
(
friend
))
 
continue
;

 
if 
(
friend
 
===
 
target
)
 
{

 
return
 
{
 
degrees
:
 
path
.
length
,
 
path
:
 
[...
path
,
 
friend
]
 
};

 
}

 
visited
.
add
(
friend
);

 
queue
.
push
([
friend
,
 
[...
path
,
 
friend
]]);

 
}

 
}

 
return
 
{
 
degrees
:
 
-
1
,
 
path
:
 
[]
 
};

}

Enter fullscreen mode

Exit fullscreen mode

### The twist: real relationships aren't equal

So far in our problem knowing someone is binary. But you and I both know that's a lie. There's a biiiig difference between:

* Maria once stood next to Pedro at an event, and
* Pedro? Yeah, we're having dinner every Thursday.

Technically, both are relationships but practically, one of them is significantly more useful to mymission.

Alexandra --2-- Maria --5-- Sofia --4-- Tessa --1-- Pedro

Enter fullscreen mode

Exit fullscreen mode

So let's assign every relationship an introduction cost. A close relationship has a low cost because asking for an introduction is easy. A weak acquaintance has a high cost because... well, good luck with that.

The BFS algorithm doesn't know how to handle weights. For weighted graphs, we need to move our attention toDijkstra's algorithm.

#### Dijkstra's algorithm, briefly

Dijkstra's algorithm asks a slightly different question:

"What is the cheapest path from A to B?"

Instead of exploring nodes in the order we discover them, we prioritize the node who currently has the lowest accumulated cost from our starting point.

That usually means replacing BFS's regular queue with a priority queue.

## Same graph, different nouns

The Pedro Pascal situation is ridiculous, i know, but the underlying problem isn't. Change what the nodes and edges represent, and suddenly the same ideas appear everywhere.

Domain

Nodes

Edges

What "shortest path" answers

Social graph

People

Relationships

"How many introductions to Pedro Pascal?"

Maps / GPS

Intersections

Roads (weighted by time/distance)

"Fastest route from A to B"

Web crawling

Web pages

Hyperlinks

"How many clicks from this page to that one?"

Codebases

Modules/files

Imports/dependencies

"What breaks if I change this file?"

Recommendations

Users or items

Similarity/interaction strength

"What's most relevant to this user?"

Graphs are one of those computer science concepts that you initially hate and mostly dont understand. Nodes. Edges. Traversals. Queues. But they are everywhere.. The internet itself is basically one very big graph.

And if by any chance anyone knows someone who knows someone... You know where to find me.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse