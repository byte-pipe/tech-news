---
title: Improving Heuristics
url: https://www.redblobgames.com/pathfinding/heuristics/differential.html
site_name: hackernews_api
content_file: hackernews_api-improving-heuristics
fetched_at: '2026-08-09T11:26:24.796033'
original_url: https://www.redblobgames.com/pathfinding/heuristics/differential.html
author: bobbiechen
date: '2026-07-28'
description: Improving Heuristics for A* Pathfinding
tags:
- hackernews
- trending
---

2026 Jul, but attempted many times since 2015

For optimizing A* we usually look at the priority queue or the map representation. Often overlooked isimproving the heuristic function. Here’s an example from the town ofDenerimin Dragon Age Origins.Try moving the startBand goalto see A*in action:

Nowtry moving the greenLto be near the purple. As the heuristic valuegets closer to thetruedistance, the number of nodes A* has to explore decreases fromto. The blue area is the savings.

On this page I’ll show a way to improve the heuristic to speed up A*. At theend of the pageI show this technique with maps from real games.

## 1A*’s use of the heuristic#

A* uses aheuristicto guide it towards the goal. We can think of it like wind pushing us in the right direction. Here, the heuristic pushes us east, and the shortest path goes east:

But sometimes it pushes us in thewrongdirection. Here, the shortest path is to the west but the heuristic pushes us east:

A* runs faster when the heuristic guides us in the right direction. It wastes time when the heuristic guides us in the wrong direction. Butwhyis it in the wrong direction? It’s because the usual distance-based heuristic doesn’t know about the walls.

## 2Perfect heuristic#

Ideally, we’d find a heuristic that knows about walls and never points in the wrong direction:

Can we calculate this “perfect” heuristic?Yes!

But the perfect heuristic is different for every goal and wall configuration. Move the goaland you’ll see the heuristic changes. Move the startBand you’ll see it doesn’t.

If the goal and walls stay the same, then we can useflow field pathfinding. But usually the goal isn’t the same, so we need to construct a brand new perfect heuristic for each goal. That is impractically slow to calculate every time we run A*, and it’s also impractically too large to store if we want to compute it ahead of time.

It’d be nice if we could calculate the heuristiconceand thenreuseit for multiple A* runs with different goals.

## 3Reusing a perfect heuristic#

Let’s calculate a perfect heuristic to the greenL, which we call a “landmark”. Can we reuse it for another goal?Yes, sometimes!Move the start pointBand the landmarkLaroundto see which purple goals are helped:

The idea is that if we already have the path fromB→L, wealsoget the shortest path to anyalong the way:

B

L

path from B to L includes X

path from B to X

path from X to L

Think of the landmark as something far in the distance. Your friend tells you “from your houseB, walk towards the Eiffel TowerLuntil you get to Daniel’s house”. The goal is not to reach the landmark. The landmark tells us adirectionto go in. The goal, Daniel’s house, is on the way.

Most goalsaren’t on the pathB→Lbut sometimes they arecloseto that path:

path from B to L

path from B to X

path from X to L

But what does it mean to be “close”? We can use the path length,cost(B, L). When the paths are almost the same,cost(B, L)is close tocost(B, X) + cost(X, L).

In A*, we use theheuristic functionas a lower bound for the path lengthcost(B, X). Thetriangle inequality[1]says that the sum of two sides of a triangle is at least as long as the third side. Adapted for directed graphs, we can saycost(B, X) + cost(X, L) ≥ cost(B, L). To calculate a lower bound, we rewrite this inequality ascost(B, X) ≥ cost(B, L) - cost(X, L).

That’s the key idea here. It’s impractical to precalculate all costs to all locations, but if we’ve precalculated the costs to a specific locationL, we can use that to estimate the cost to a different location.

Some of the academic research papers refer to this as a heuristic based on the triangle inequality. Other papers call this the “differential heuristic” because it takes the difference between already computed distances.

## 4Multiple landmarks#

How often is this triangle inequality useful?

cost(B, X)

cost(X, L)

cost(B, L) ≤ cost(B, X) + cost(X, L)

It depends on whereLis relative to the pathB→:

 

Relative positions

Landmark useful?

before

L
 
B
 
 
 

only in undirected graphs

middle

 
B
 
L
 
 

no

after

 
B
 
 
 
L

yes

Move the startBand goalaroundto see where a landmark would help:

Try moving the landmarkLoutside the green shaded region, and see that the heuristic and path don’t always match.

Since a landmark needs to be “after” the goal, a single landmark won’t be useful for all paths. We needmultiplelandmarks L₁, L₂, L₃, etc. Each one gives us some lower bound for the heuristic:

cost(B, X) ≥ cost(B, L₁) - cost(X, L₁)
cost(B, X) ≥ cost(B, L₂) - cost(X, L₂)
cost(B, X) ≥ cost(B, L₃) - cost(X, L₃)
…
cost(B, X) ≥ cost(B, Lₙ) - cost(X, Lₙ)

We can take themax()of these to pick the highest bound. In this diagram, trymoving the goalto one of the purple shaded areasto see how those areas are improved by the landmarks. Then try moving it to one of the unshaded areas to see how A* isn’t any faster there. Also try moving the start pointBto see how the shaded area also depends on where the start is.

## 5Placement of landmarks#

The best landmark position depends on the start pointBandgoal. We want the landmark to be “after” the goal, but what’s “after” depends on where the start pointBand goalare.

We want to use landmarks to improve as many (start, goal) pairs as possible.

Let’s start with a single landmark. Try moving the startB, goal, and landmarkLon this map:

The purple shaded areas show the goal positions that the landmark helsp. It looks like the landmark can cover the main corridors but not the side rooms. We need many more landmarks:

Much more of the map is covered in purple now. Picking the number and placement of landmarks isproject specific. Consider:

* Are all paths equally likely? For example in a colony builder game like Dwarf Fortress, we may care a lot more about paths to/from the main base, and not paths between a forest and a mine.
* All all paths equally valuable to optimize? For example if pathfinding is limiting the frame rate, we might want to focus on long paths that are slower to compute and not on short paths.
* Is the map static or does it change over time? If static, we might want to spend a lot of time in the map designer tool to precalculate optimal landmarks. But if dynamic, we might want to use the last few goal locations to decide new landmark positions.If the change reduces an edge cost, the heuristic will overestimate sometimes, and A* will return a non-shortest path until we update the cost table. Pathfinding is optimized but nonoptimal. Example: the player broke a wall but the unit won’t look for the shorter path right away.If the change increases an edge cost, the heuristic will be lower than desired, and A* will take a little longer to run until we update the cost table. Pathfinding is optimal but not optimized. Example: the player added a wall so the unit might think that area’s safe to walk through but will have to find a path around it.
* If the change reduces an edge cost, the heuristic will overestimate sometimes, and A* will return a non-shortest path until we update the cost table. Pathfinding is optimized but nonoptimal. Example: the player broke a wall but the unit won’t look for the shorter path right away.
* If the change increases an edge cost, the heuristic will be lower than desired, and A* will take a little longer to run until we update the cost table. Pathfinding is optimal but not optimized. Example: the player added a wall so the unit might think that area’s safe to walk through but will have to find a path around it.
* If many units find paths to common areas (such as the Dwarf Fortress dining room), consider dropping the least used landmark and adding one near the common area.
* Are the maps open world or constrained? A real time strategy game may have different needs than a room+corridor dungeon crawler.
* Thomas Nobeshas a video explanation[2]including more tips on where to place the landmark points.

Fortunately, even if a landmark isn’t optimal, it might still help somewhat, and it’s still no worse than if we use the regular A* heuristic.

## 6Automated placement#

Although the best landmark positions will be project specific, one algorithm to place landmarks in a project-agnostic way is to keep track of which locations are good for many randomly chosen paths.Try it hereto find a landmark position:

(start animation)

It usually but not always picks a spot in the upper left. It matches our intuition that landmarks should go on the outer edges of the map.

The second landmark should be away from the first landmark. The third landmark should be away from the first and second landmark. Each subsequent landmark should be evaluated based on what it adds. This is what it looks like with two existing landmarks:

(start animation)

It picks a third away from the first two, but not always in the same place.

## 7Implementation#

The change described on this page is to the heuristic function given to A*. We don’t need to change A* itself.

We need topick landmarks. If the maps are known ahead of time, landmarks can be placed in a map designer tool. If the maps are procedurally generated, try the randomized map analysis earlier on this page. Some of the papers linked at the end have more sophisticated placement algorithms.

Then we need toanalyze the map. Allocate a 2D array of numbers,cost[nodeId][landmarkId].

For each landmark, we runDijkstra’s Algorithm. It’s a “single source shortest path” algorithm but we want a single goal instead of a single source. In a directed graph, we need to reverse all the edges. In an undirected graph, we can use the edges as is. We setcost[nodeId][landmarkId]to the cost of the shortest path from nodenodeIdto nodelandmarkId. If the weights are all 1, we can use Breadth First Search instead of Dijkstra’s Algorithm.

This is approximately what I’m running for the demos on this page (undirected graphs):

const
 
L
 = [ 
/* 
array of landmark locations
 */
 ];

let
 
L_cost
 = [ 
/* 
array[nodeId] of arrays[landmarkId]
 */
 ];

for
 (
let
 
landmarkId
 = 0; landmarkId < L.length; landmarkId++) {
 
let
 
output
 = dijkstraSearch(L[landmarkId]);
 
for
 (
let
 
nodeId
 = 0; nodeId < graph.num_nodes; nodeId++) {
 L_cost[nodeId][landmarkId] = output.cost_so_far[nodeId];
 }
}

Note thatit’s not much code. It’s running our existing algorithm (Dijkstra’s, A*, or BFS) and storing the results in an array. It could run in a background thread.

Then we need tomodify the heuristic function. Previously the heuristic wasdistance(B, X). For example:

function
 
heuristicManhattan
(
a
, 
z
) {
 
return
 Math.abs(a.x - z.x) + Math.abs(a.y - z.y);
}

Each landmark Ligives us a lower boundcost(Lᵢ, X) - cost(Lᵢ, B). We want to take thehighestof these:

function
 
heuristicLandmark
(
B
, 
X
) {
 
let
 
h
 = heuristicManhattan(B, X); 
// 
or any base heuristic

 
for
 (
let
 
i
 = 0; i < L.length; i++) {
 
let
 
lowerBound
 = L_cost[B][i] - L_cost[X][i];
 lowerBound = Math.abs(lowerBound); 
// 
if undirected

 
if
 (lowerBound > h) { h = lowerBound; }
 }
 
return
 h;
}

Note thatit’s not much code. It’s running the existing heuristic (typically Manhattan, Chebyshev, or Euclidean distance) and sometimes increasing it if the landmarks form a good triangle.

What changes with the A* code?Nothing.

There are lots of techniques for making A* run faster. I like this one because it’s very little code.

## 8Demos#

I tried the differential heuristic on some maps from Dragon Age (provided by movingai.com[3]), a maze (also provided by movingai.com), andCogmind[4](maps provided by Josh Ge). All of these maps are undirected graphs (edges are bidirectional) so I’ve used that version of the differential heuristic.

* Blue areas are whatwe no longer have to searchby using the differential heuristic. Orange areas are what we search even with the improved heuristic.
* Try moving the startBand goalto see the performance on different paths.

### 8.1Dragon Age, The Circle Tower#

The landmark is badly placed for the initialB→path. Try moving it.

### 8.2Cogmind, Factory 5#

In the next demo the landmarksLare in places that don’t help. Move them around to improve search.

The blue area are the nodes we no longer have to search. More blue is better.

The landmarkLpoints help more when closer to the start pointBthan the goal. They help more when they’re “past” the goal point. Move the startBand goalaround and see that there’s a big improvement no matter which path you want to find:

However, it took a lot of landmarks to get that improvement. We can do better by using the random path map analysis to pick fewer landmarks but in smarter locations:

### 8.3Maze#

A* with a distance heuristic behaves particularly badly with mazes, but in this one, just four landmarks make a big difference! Thentry clicking Random pathrepeatedly. The blue areas are the areas wedidn’t have to searchby using the landmarks. Also toggle the bidirectional flag to see how much of a difference that makes.

### 8.4Dragon Age, Lothering#

This map has large open areas, and it seems to work well with the landmarks.

### 8.5Cogmind, Research 2#

This is a room-and-corridor map from Cogmind.

### 8.6Cogmind, Factory 4#

Another room-and-corridor map, common in traditional Roguelike dungeons.

## 9More reading#

This page is about using Cartesian coordinates in a game map to construct a graph-based heuristic based on “landmark” nodes (sometimes called “pivots” or “beacons”).I’ve collected some references but haven’t read all of themso I may have some of this wrong.

* 2004Computing the Shortest Path: A* Search Meets Graph Theory[5](Goldberg, Harrison) [mirrors[6]]. I learned about the technique in this paper. It’s a combination ofbidirectionalA* search and the landmark-based heuristic, used for road networks. It uses the terminology “landmarks” and “triangle inequality”.
* 1994Routing information organization to support scalable interdomain routing with heterogeneous path requirements(Hotz). [citations[7]] I can’t find a copy of this online, but it appears to be work that introduced using the triangle inequality with landmarks, for Internet routing.
* 2005Approximate Distance Oracles(Thorup, Zwick) [mirrors[8]]. This theory paper covers the more general topic of calculating the approximate distance between any pair of nodes in a graph, using a “distance oracle[9]”. An approximate distance is what we need as the heuristic in A*.

It’s also possible to go in reverse. Many graphs do not have natural Cartesian coordinates, and even the ones that do may not have good results from a distance-based heuristic.

* 2002Predicting Internet Network Distance with Coordinates-Based Approaches[10](Ng, Zhang) [mirrors[11]] This paper uses the landmark-based heuristics to assign Cartesian coordinates for nodes in an Internet routing network. Then it uses Euclidean distance for the heuristic. This is the inverse of what we’re doing on this page, where we already have Cartesian coordinates, but want to use the landmark-based heuristic instead.
* 2011Euclidean Heuristic Optimization[12](Rayner, Bowling, Sturvetant) transforms the Cartesian coordinates on a game map where distance heuristics don’t work well into new Cartesian coordinates where distance does work well.

Storing the landmark data requires one number per node. In a typical game map, those numbers may be very similar from one grid space to the next. Just as image compression takes advantage of nearby pixels having similar values, we might want to compress the landmark data because nearby graph nodes have similar values:

* 2011The Compressed Differential Heuristic[13](Goldenberg, Sturvetant, Felner, Schaeffer) - by storing more landmarks in the same amount of space, the heuristic can be better. In this paper, “landmarks” are called “pivots”, and the “landmark based heuristic” is called the “differential heuristic”.

The landmarksLused on this page are placedafterthe end of the path, so the layout isB→→L. There are also algorithms that place landmarksalongthe path,B→L→L→L→. I am not covering that topic here, but if you’re interested, see:

* 2008Approximating Shortest Paths using Landmarks[14](Grant, Mould). Calls them “landmarks”.
* 2014Hub Labels: Theory and Practice[15](Delling, Goldberg, Savchensko, Werneck). Calls them “hubs”, and uses only a single intermediary on the path B→L→X.
* 2009Abstraction-Based Heuristics with True Distance Computations[16](Felner, Barer, Sturvetant, Schaeffer). I believe this paper tries to unify both “landmark” approaches. B→X→L is called “differential heuristic” and B→L→L→L→X is called “canonical heuristic”, and both of these are under the umbrella “true distance heuristics”.

I learned about this technique in 2007, then tried writing it up in 2015. I realized that I didn’t understand it enough to be able to explain it. I studied it off and on in 2016, 2018, 2019, 2022, 2024, and 2026. I abandoned and restarted this page many times. And by 2026 I think I understand it well enough to write this page. However I haven’t used it in a real project yet.