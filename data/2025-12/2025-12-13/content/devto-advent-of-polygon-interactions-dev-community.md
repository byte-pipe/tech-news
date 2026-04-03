---
title: Advent of Polygon Interactions - DEV Community
url: https://dev.to/yordiverkroost/advent-of-polygon-interactions-1mgp
site_name: devto
fetched_at: '2025-12-13T11:06:21.108956'
original_url: https://dev.to/yordiverkroost/advent-of-polygon-interactions-1mgp
author: Yordi Verkroost
date: '2025-12-09'
description: My solution for Advent of Code 2025 day 9. Tagged with adventofcode.
tags: '#adventofcode'
---

Number 9,turn me on dead man! And... grids again. While the first part of today's puzzle is easy to implement, the second part got me down the rabbit hole of theshapelylibrary, GEOS computational geometry, DE-9IM matrices, ray-casting and all sorts of other wildly interesting theoretical mathematical knowledge.

Let's dive in!

Check out my full solution for day 9 at GitHub.

### Part one

As input, we get a couple of coordinates in a grid that represent red tiles:

7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3

Enter fullscreen mode

Exit fullscreen mode

Our job is to find the biggest rectangle that can be made using any combination of two of these coordinates, where the coordinates represent the opposite edges of the rectangle. For example, the rectangle with edge coordinates2,5and9,7runs from coordinate2,5to9,5to9,7to2,7and then back to2,5. In the full problem space, this rectangle would look like this:

..............
..............
..............
..............
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO....
..............

Enter fullscreen mode

Exit fullscreen mode

The (brute-force) logic I used is to consider all possible combinations of two coordinates (without duplicates), calculate the area of the rectangle created from these coordinates and keep track of the largest area we encounter. Calculating the area of a single rectangle is done by multiplying the difference on the x-axis with the difference on the y-axis (making sure to be inclusive by adding one to the difference and to get a positive number usingabs):

def

area_size
(
x1
:

int
,

y1
:

int
,

x2
:

int
,

y2
:

int
)

->

int
:

 

 

return
(
abs
(
x1

-

x2
)

+

1
)

*

(
abs
(
y1

-

y2
)

+

1
)

largest

=

0


for

i

in

range
(
len
(
data
)):


for

j

in

range
(
i

+

1
,

len
(
data
)):


x1
,

y1

=

data
[
i
]


x2
,

y2

=

data
[
j
]


area

=

area_size
(
x1
,

y1
,

x2
,

y2
)


if

area

>

largest
:


largest

=

area


return

largest

Enter fullscreen mode

Exit fullscreen mode

The result for part one is returning thelargestrectangle area we've seen.

Part one done, no problems so far. But then came part two.

### Part two

It appears that the order in the input for this puzzle matters. If we go from top to bottom through the list of coordinates, we can draw a line between each pair of coordinates that results in a closed shape. Using the example input and the example problems space, connecting all coordinates together results in the following shape, where each coordinate (#) from the input falls within this shape (completed usingX's):

..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............

Enter fullscreen mode

Exit fullscreen mode

Given this closed shape, we need to find the largest rectangle from any combination of two input coordinatesthat is enclosed within this shape.

After trying a couple of mathematical solutions (and coming close by programming one that works fast enough for the sample input but not for the full input) I thought I reached my Waterloo. But as it goes with Advent of Code-puzzles, I couldn't let go and eventually found the Python libraryshapely. This library allows me to build polygon shapes based on coordinates, and as that's what we got as input this seemed to fit this puzzle perfectly. I could simple usePolygon(data), wheredatais a list of coordinates in the form[(7,1), (11,1), ..., (7,3)]: exactly the closed shape that is build from the input coordinates.

Having this polygon, we can build other polygons for each rectangle that is build using any combination of two input coordinates. Going back to the example from part one, the edge coordinates2,5and9,7can be used to create a newPolygon:

def

poly_rectangle_area
(
x1
:

int
,

y1
:

int
,

x2
:

int
,

y2
:

int
)

->

Polygon
:


x_min
,

x_max

=

min
(
x1
,

x2
),

max
(
x1
,

x2
)


y_min
,

y_max

=

min
(
y1
,

y2
),

max
(
y1
,

y2
)


return

Polygon
([(
x_min
,

y_min
),

(
x_min
,

y_max
),

(
x_max
,

y_max
),

(
x_max
,

y_min
)])

Enter fullscreen mode

Exit fullscreen mode

Now we have two polygon, we can use a neat function from theshapelylibrary to check whether a rectangle is fully within the full shape area:

rectangle
.
within
(
poly_area
)

Enter fullscreen mode

Exit fullscreen mode

If yes, we can calculate the area for this rectangle in the same way as in part one, keep track of the largest rectangle we encountered and finally return thislargestnumber again, as the answer for part two. The full code for part two (calling other functions in the process) is as follows:

largest

=

0


poly_area

=

Polygon
(
data
)


for

i

in

range
(
len
(
data
)):


for

j

in

range
(
i

+

1
,

len
(
data
)):


x1
,

y1

=

data
[
i
]


x2
,

y2

=

data
[
j
]


rectangle

=

poly_rectangle_area
(
x1
,

y1
,

x2
,

y2
)


if

rectangle
.
within
(
poly_area
):


area

=

area_size
(
x1
,

y1
,

x2
,

y2
)


if

area

>

largest
:


largest

=

area


return

largest

Enter fullscreen mode

Exit fullscreen mode

### The maths

Yes, I used libraries to help me with this problem. And yes, I do also want to understand the basics of what happens behind the scenes.

And boy, did I learn some things. I'll try to explain a bit of this below, both to get things straight for myself and maybe you'll get to know something new as well.

Theshapelylibrary usesGEOS, a C/C++ computational geometry library. Thewithin()function runs in a three two stages:

1. Computing a "topological picture" of two shapes.
2. Using this picture to determine if one shape iswithinanother.

In the first stage, GEOS builds a matrix that represents the relation between two shapes, let's call them A and B. For both shapes, it compares their interiors (all coordinates within the shape), their boundaries (all coordinates exactly on the edges of the shape) and their exteriors (all coordinates fully outside of the shape). This results in a 3x3 matrix like this one:

 B
 I B E
 +-----+-----+-----+
 I | | | |
A +-----+-----+-----+
 B | | | |
 +-----+-----+-----+
 E | | | |
 +-----+-----+-----+

Enter fullscreen mode

Exit fullscreen mode

Each of the cells in this matrix is filled with a character:2if the dimension of the intersection between the shapes is an area,1if the intersection is a line,0if the intersection is a single point andFif there is no intersection.

For example, the top-left column is set to2if the (full) interior ofAis inside the interior ofB. Another example: the top-center column is set toFif the interior ofAdoes not touch the boundary ofB.

Filling all of this matrix with2,1,0orFcan result in something like this:

 B: I B E
 +----+----+----+
A: I | 2 | F | F |
 +----+----+----+
 B | 1 | F | F |
 +----+----+----+
 E | 2 | 1 | 2 |
 +----+----+----+

Enter fullscreen mode

Exit fullscreen mode

We can also write this out in a flat, single-line form, going from left to right and top to bottom. For the above matrix, this flat form is:

2FF1FF212

Enter fullscreen mode

Exit fullscreen mode

Using this flat form, we can check if any interaction between these shapes is true (like thewithinwe're interested in, but also interactions likecontains,overlapsandtouches). Forwithin, the pattern we check might be something like this:

T*F**F***

Enter fullscreen mode

Exit fullscreen mode

WhereTmeans this character should be non-empty,Fmeans it should be empty and*means the character does not matter. In other words, after doing the hard work by generating the matrix (which contains a lot of other logic like ray-casting which I won't go into here) we can match on predefined patterns to eventually get the result for part two.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
