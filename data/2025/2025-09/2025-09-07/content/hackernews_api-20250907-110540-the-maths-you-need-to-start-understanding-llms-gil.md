---
title: 'The maths you need to start understanding LLMs :: Giles'' blog'
url: https://www.gilesthomas.com/2025/09/maths-for-llms
site_name: hackernews_api
fetched_at: '2025-09-07T11:05:40.559068'
original_url: https://www.gilesthomas.com/2025/09/maths-for-llms
author: gpjt
date: '2025-09-02'
published_date: 2025-09-02T23:30:00+0000
description: 'A quick refresher on the maths behind LLMs: vectors, matrices, projections, embeddings, logits and softmax.'
tags:
- hackernews
- trending
---

Giles' blog

About

Contact

 Archives

 Categories

 Blogroll

* September 2025 (1)
* August 2025 (5)
* July 2025 (1)
* June 2025 (2)
* May 2025 (3)
* April 2025 (2)
* March 2025 (7)
* February 2025 (10)
* January 2025 (6)
* December 2024 (7)
* September 2024 (1)
* August 2024 (2)
* July 2024 (2)
* May 2024 (2)
* April 2024 (2)
* February 2024 (2)
* April 2023 (1)
* March 2023 (2)
* September 2022 (1)
* February 2022 (1)
* November 2021 (1)
* March 2021 (1)
* February 2021 (2)
* August 2019 (1)
* November 2018 (1)
* May 2017 (1)
* December 2016 (1)
* April 2016 (1)
* August 2015 (1)
* December 2014 (1)
* August 2014 (1)
* March 2014 (1)
* December 2013 (1)
* October 2013 (3)
* September 2013 (4)
* August 2013 (2)
* July 2013 (1)
* June 2013 (1)
* February 2013 (1)
* October 2012 (1)
* June 2012 (1)
* May 2012 (1)
* April 2012 (1)
* February 2012 (1)
* October 2011 (1)
* June 2011 (1)
* May 2011 (1)
* April 2011 (1)
* March 2011 (1)
* February 2011 (1)
* January 2011 (1)
* December 2010 (3)
* November 2010 (1)
* October 2010 (1)
* September 2010 (1)
* August 2010 (1)
* July 2010 (1)
* May 2010 (3)
* April 2010 (1)
* March 2010 (2)
* February 2010 (3)
* January 2010 (4)
* December 2009 (2)
* November 2009 (5)
* October 2009 (2)
* September 2009 (2)
* August 2009 (3)
* July 2009 (1)
* May 2009 (1)
* April 2009 (1)
* March 2009 (5)
* February 2009 (5)
* January 2009 (5)
* December 2008 (3)
* November 2008 (7)
* October 2008 (4)
* September 2008 (2)
* August 2008 (1)
* July 2008 (1)
* June 2008 (1)
* May 2008 (1)
* April 2008 (1)
* January 2008 (4)
* December 2007 (3)
* March 2007 (3)
* February 2007 (1)
* January 2007 (2)
* December 2006 (4)
* November 2006 (18)

* Python (54)
* AI (47)
* TIL deep dives (46)
* Resolver One (34)
* LLM from scratch (22)
* Blogkeeping (18)
* PythonAnywhere (17)
* Linux (16)
* Startups (15)
* NSLU2 offsite backup project (13)
* TIL (13)
* Funny (11)
* Finance (10)
* Fine-tuning LLMS (10)
* C (9)
* Musings (9)
* Gadgets (8)
* Personal (8)
* Robotics (8)
* Website design (8)
* 3D (5)
* Rants (5)
* Cryptography (4)
* JavaScript (4)
* Music (4)
* Oddities (4)
* Quick links (4)
* Talks (4)
* Dirigible (3)
* Eee (3)
* Memes (3)
* Politics (3)
* Django (2)
* GPU Computing (2)
* LaTeX (2)
* MathML (2)
* OLPC XO (2)
* Space (2)
* VoIP (2)
* Copyright (1)
* Golang (1)
* Raspberry Pi (1)
* Software development tools (1)

* Agile Abstractions
* Astral Codex Ten
* :: (Bloggable a) => a -> IO ()
* David Friedman's Substack
* Econ & Energy
* Entrepreneurial Geekiness
* For some value of "Magic"
* Hackaday
* Knowing.NET
* Language Log
* Millennium Hand
* ntoll.org
* Obey the Testing Goat!
* PK
* PythonAnywhere News
* Simon Willison's Weblog
* Software Deviser
* Some opinions, held with varying degrees of certainty
* tartley.com

## The maths you need to start understanding LLMs

 Posted on 2
September 2025


 in


AI
,


LLM from scratch

This article is the second of three "state of play" posts that explain how Large Language
 Models work, aimed at readers with the level of understanding I had in mid-2022: techies
 with no deep AI knowledge. It grows out
 ofpart 19in my series
 working throughSebastian Raschka's book
 "Build a Large Language Model (from Scratch)".
 You canread the first post in the series here.

Actually coming up with ideas like GPT-based LLMs and doing serious AI research requires
serious maths. But the good news is that if you just want to understand how they
work, while it does require some maths, if you studied it at high-school at any time since the 1960s, you did all of the groundwork
then: vectors, matrices, and so on.

One thing to note -- what I'm covering here is what you need to know to understandinference-- that
is, using an existing AI, rather than thetrainingprocess used to create them. That's also not
much beyond high-school maths, but I'll be writing about that later on.

So, with that caveat, let's dig in!

### Vectors and high-dimensional spaces

Inthe last postI used the word "vector" in the way it's normally used by software
engineers -- pretty much as a synonym of "an array of numbers". But a vector of lengthnis more
than that; it's a distance and direction inn-dimensional space, or (equivalently)
it can be taken as a point -- you start at the origin, and then follow the vector from
there to the point in question.

In 2-d space, the vector(2,−3)means "two units to the right, and three down", or the point that is located if you move
that way from the origin. In 3-d,(5,1,−7)means
"five right, one up, and seven away from the viewer" (or in some schools of thought, seven toward the viewer),
or the point there.
With more dimensions, it becomes pretty much impossible to visualise, but conceptually it's the same.

We use vectors to mean things in LLMs. For example, the vectors of logits that come
out of the LLM (see the last post) represent the likelihood of different next tokens
for an input sequence. And when we do that, it's often useful to think of that in terms of
defining a high-dimensional space that the meaning is represented in.

### Vocab space

The logits that come out of the LLM for each token are a set of numbers, one per possible
token, where the value in each "slot" is the LLM's prediction of how likely the associated token is to be the
next one.

The GPT-2 LLM that the book is covering uses a tokeniser with 50,257 tokens -- its
vocabulary size is 50,257 -- so
each logits vector is 50,257 items long. Token 464 is "The", so the number at position 464
in a logits vector is how likely the next token is to be "The", relative to the others.

We can see each logits vector as being a vector in a 50,257-dimensional space1; every
point in that space is a different combination of possibilities for the next token
to choose from our tokeniser's vocabulary to continue the sequence.
I'll call this avocab space.

That's a kind of "messy" vocab space, though -- let's consider two logits vectors, both points in that space, for an imaginary
LLM that has a vocabulary of just three tokens. The first is(1,2,3), and the second(−9,−8,−7). Those both mean that the first token ID
(with the smallest number) is least likely, the second is more likely than that, and the
last, with the largest number, is most likely.

Having two points in the space that mean the same thing seems redundant. To tidy things up, we can run a vector
in this messy vocab space through thesoftmax function--
that will give us a list of probabilities. I'm personally treating softmax as a kind of magic, but
the important thing about it from this perspective is that it takes these messy "likelihood"
vectors and returns a set of numbers, all between zero and one, that represent
probabilities -- which means that the numbers in the result set sum up to one. Importantly, all different
vectors that represent the same set of probabilities when expressed as logits will
map to the same vector in the post-softmax space. For example, both(1,2,3)and(−9,−8,−7)map to the same probability distribution, about(0.09,0.24,0.66)2.

Note: the two specific "messy" vectors I used were chosen because they work out to the same
 probabilities. There are other vectors that express the same "ranking", with the
 first being least likely, the second more, and the third most likely, that have different
 probability distributions. For example,(1,2,5)has the same ranking, but
 it's hopefully obvious that we're saying that the third token is much more likely compared
 to the others than it was in(1,2,3)-- and that would be reflected in the softmax, which
 would be something like(0.02,0.05,0.94).

So, we have two kinds of vocab space. A vector in either of them represents likelihoods
for a token; there's a "messy" unnormalised space, where the same probability distribution can
be expressed in different ways, and a neat, tidy normalised one, where we just use real
probability distributions.

One extra thing before we move on; an obvious minimal case in the normalised vocab space
is a vector where all of the numbers are zero apart from one of them, which is set to
one -- that is, it's saying that the probability of one particular token is 100% and
it's definitely not any of the others. This is an example of a one-hot vector (not
super-inventive naming) and will become important in the next post.

So: that's one use of a high-dimensional space; let's look at another one.

### Embeddings

An embedding space is a high-dimensional space where vectors represent meanings. If you look at them
as points rather than directions/distances, similar concepts are
clustered together in the space.

Now, "meaning" is of course very dependent on
what you're using the meaning for.
For example, you can imagine an embedding space
where the points representing "domestic cat", "lion" and "tiger" were all quite close
together in one cluster, and "dog", "wolf" and "coyote" made another cluster some distance
away (both clusters being within an area that meant something like "animal"). That would be a useful representation
space for a zoologist, grouping felines and canines together.

But for more day-to-day
use, a different space that grouped domestic animals like "cat" and "dog" closely, in
a separate cluster from wild-and-possibly-dangerous animals might be more useful.

So there are vast numbers of possible embedding spaces, representing different kinds
of meanings for different purposes. You can go all the way from rich spaces representing complex concepts
to "dumb" spaces where you just want to cluster together concepts by the parts of speech
that they represent -- verbs, nouns, adjectives, and so on.

The one counterintuitive thing about embedding spaces, at least for me, is that quite
often, we don't care much about the lengths of the vectors we use. We
might treat(1,2)and(8,16)as being essentially the same embedding vector in a 2-d space because they
point in exactly the same direction.3

Let's move on to what we candowith these high-dimensional spaces

### Projections by matrix multiplication

A quick refresher: matrices are just vectors stacked together; if you write the vector(2,−3)like this:

(
2
−
3
)

...then you can stack it "sideways" with another vector, say(5,1), to make a matrix like this:

[
2
5
−
3
1
]

Or, if you write it horizontally like this:

(
2
−
3
)

...then it can be stacked vertically with the same other vector like this:

[
2
−
3
5
1
]

The size of a matrix is written in the formr×c, whereris the number
of rows, andcis the number of columns. So both of the above are2×2matrices;
here's a2×3one:

[
2
−
3
7
5
1
−
8
]

Matrices can be multiplied together; hopefully you remember that from your schooldays,
but I wrotea refresherback in February if you'd like to remind yourself. It also covers some useful neural net stuff :-)

You hopefully also remember that matrix multiplications can be used to do geometric transformations.
For example, this2×2(two rows, two columns) matrix:

[
cos
θ
−
sin
θ
sin
θ
cos
θ
]

Let's call itR. It can be used to rotate points in a 2-d space around the origin anticlockwise byθdegrees.
To do that, you put all of the points into a matrix, one point per column (like the first example above), giving a2×nmatrix,
-- let's call itX. We multiply that one by the rotation matrix:

Y
=
R
·
X

...and you have a new matrix with the rotated points.
That will have the shape2×nas well, of course, because a2×2matrix
times a2×none takes its number of rows from the first one and its number of
columns from the second.

NOTE: just to confuse things a bit: the way we're taught to do this kind of thing
 at school is the standard mathematical practice, and that's how I showed it above.
 The "points" that we're starting with are written as column vectors
 "stacked side-by-side" to make up a2×nmatrix and then we multiply our
 rotation matrix by it,R·X. However, in machine learning, people tend
 to "stack up vertically" a bunch of row vectors, eg.n×2, so the
 multiplication is the other way around:X·R.
 In computing terms, we are storing points in row-major rather than column-major
 format.This postexplains why,
 and I'll switch to using that from now on.

One way of thinking about that rotation matrixRis that it's a bit like a function, taking
a set of points in a matrix and returning another set of points that are the original
ones rotated.

An alternative way is to think of it projecting between two different 2-d spaces,
the second space being rotated around the origin byθdegree from the first. That's a relatively
philosophical point in this case -- both models work well enough.

But when working with 3-d graphics, people use larger matrices -- simplifying a bit,
you might use a3×2matrix to take a collection ofnpoints in 3-d space, expressed
as an×3matrix (remember that we're using row-major matrices now). We would multiply them asX·R, and wind up with those original points
projected into 2 dimensions so that they can be displayed on a screen.4

And that leads us to a more general statement: matrices can project between different
multidimensional spaces. More specifically, when using row-major values, ad1×d2matrix
projects from ad1-dimensional space to ad2dimensional space. The numbers
in the matrix determine what kind of projection it is.

So, a2×2matrix projects points between different 2-d spaces,
likewise a3×3one will project points between 3-d spaces,
but a3×2matrix can project from a 3-d space to a 2-d one.

And we can make it even more extreme!
A50257×768matrix can be seen as a projection from a 50,257-dimensional space to a 768-dimensional
one, and a768×50257one would project from a 768-dimensional space to a
50,257-dimensional space. (You'll see why I chose those specific numbers in the next post,
though you've probably spotted the relevance of the 50,257.)

It's important to note that the projections can be "lossy", though. If you did the two
projections above, one after the other, you'd lose information when you reduced
the number of dimensions that you could never get back, no matter what matrices you used.

A nice mental model for that
is the 3-d to 2-d projection for computer graphics -- if you did a perspective projection
of, say, two squares -- one large and distant, one smaller and closer -- to a 2-d
plane, then they might wind up the same size. If you then projected back to 3-d,
you just wouldn't have the information needed to work out what their respective sizes
and distances were in the original.

So: matrix multiplications are projections between different spaces, with potentially different numbers of dimensions. But they're also something else.

### Neural networks

A single layer in a neural network is calculated like this (again, see mypost on matrices and neural networks,
and perhaps thefollow-up):

Z
=
ϕ
(
X
W
T
+
B
)

If we ignore the activation functionϕand the bias termB, we get this:

Z
^
=
X
W
T

(The "hat" over theZis just to express the fact that it's not the full calculation.)

Now, for a neural network,Xis our input batch, so it'sn×din--
one row for each item in the batch, and one column for each input value in that item.

Our weights matrixWisdout×din--doutbeing the number of outputs.
We transpose it (that's what the superscript "T" is there to say inWT), which means that
we swap around rows and columns, making it adin×doutmatrix.

So our resultZ^from the unbiased neural network with no activation function isn×dout.

And that takes us to the final core idea I've found useful while working through this:
a single layer of a neural network (often abbreviated tolinear layer) is not much more than
a matrix multiplication -- so it is, effectively, a projection from a space with as
many dimensions as it has inputs to a space with the same number of dimensions as it has
outputs. The bias just adds on a linear "shift" after that, and as the activation
function is optional, we can just not do it.

### Wrapping up

So, those are the basic mathematical concepts that I've needed so far to understand
LLMs. As I said at the start, there really isn't much there beyond high-school maths.
The matrices are larger than the ones we're taught, and the high-dimensional spaces
are a bit weird, but the actual mathematics is pretty simple.

Up next: how do we put all of that together, along with the high-level stuff I
described about LLMs inmy last post,
to understand how an LLM works?

1. I take no responsibility for any psychic damage caused by trying to visualise that.↩
2. Due to rounding, the numbers I show don't add up to one -- if I showed them
in full precision, they would, but this post would be unreadable...↩
3. My intuition as to why that is remains sadly weak.↩
4. In reality, to handle perspective and because we want to keep track of depth
so that close things can hide nearby things, it's a bit more complex. If you're
interested and want to go down that rabbit hole, ask your favourite LLM aboutfrustum matrices.↩

« What AI chatbots are actually doing under the hood

 Copyright (c) 2006-2025 by Giles Thomas.
 This work is licensed under a
Creative Commons Attribution 4.0 International License
.
