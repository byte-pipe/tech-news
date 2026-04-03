---
title: Premature Optimization Is Bad, But Your App Is Just Slow Because You're Lazy - DEV Community
url: https://dev.to/adamthedeveloper/premature-optimization-is-bad-but-your-app-is-just-slow-because-youre-lazy-ldn
site_name: devto
content_file: devto-premature-optimization-is-bad-but-your-app-is-just
fetched_at: '2026-03-17T11:21:43.535674'
original_url: https://dev.to/adamthedeveloper/premature-optimization-is-bad-but-your-app-is-just-slow-because-youre-lazy-ldn
author: Adam - The Developer
date: '2026-03-12'
description: '"Premature optimization is the root of all evil." Donald Knuth wrote that in 1974. It is one of the... Tagged with programming, javascript, productivity, webdev.'
tags: '#programming, #javascript, #productivity, #webdev'
---

"Premature optimization is the root of all evil."

Donald Knuth wrote that in 1974. It is one of the most cited lines in all of software engineering, and it has been used to justify more genuinely terrible code than almost any other idea in the field.

The quote is correct. The way most developers apply it is not.

There is a difference between premature optimization and basic engineering competence. Somewhere along the way, the industry collapsed that distinction, and the result is production systems that make users wait for things that should be instant.

## What Knuth Actually Said

Here is the full sentence, which almost nobody quotes:

"We should forget about small efficiencies, about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%."

He was talking about micro-optimizations. Loop unrolling. Manual register allocation. Squeezing cycles out of hot paths before you know which paths are hot. He was not giving you permission to write N+1 queries, load 400KB of JavaScript on a login page, or fetch entire database tables into memory to filter them in your application layer.

The "premature optimization" shield has been stretched so far beyond its original meaning that developers now invoke it to defend code that is simply slow by design.

## The Difference Between Optimization and Competence

There are two entirely different things that get lumped together under "performance":

Premature optimizationis spending three days hand-tuning a sorting algorithm before you know if sorting is even on the critical path. It is rewriting a function in assembly before you have profiled anything. It is trading code clarity for speed gains that may not matter.

Basic competenceis not making obviously expensive choices when obviously cheaper ones exist at the same level of effort.

These are not the same thing. One requires you to know the future. The other just requires you to know your tools.

Writing a loop that queries the database on every iteration is not a performance decision you deferred for later. It is a mistake you made right now. Selecting every column withSELECT *when you need two fields is not an optimization you skipped. It is unnecessary work you added.

Nobody calls it premature optimization when a carpenter pre-drills a hole before driving a screw. That is just knowing what you are doing.

## The Patterns That Are Just Laziness

Let us be specific. These are not edge cases or nuanced tradeoffs. These are patterns that slow applications down and have no corresponding benefit.

### The N+1 Query

const
 
posts
 
=
 
await
 
db
.
query
(
'
SELECT * FROM posts
'
);

for 
(
const
 
post
 
of
 
posts
)
 
{

 
post
.
author
 
=
 
await
 
db
.
query
(

 
'
SELECT * FROM users WHERE id = ?
'
,
 
[
post
.
author_id
]

 
);

}

Enter fullscreen mode

Exit fullscreen mode

If you have 200 posts, this runs 201 queries. If your database round trip takes 2ms, that is 402ms of pure waiting added to every single request, for the lifetime of the application, for every user, forever.

The fix is not an optimization. It is a JOIN, which is what relational databases were designed to do in 1970.

SELECT
 
posts
.
*
,
 
users
.
name
,
 
users
.
avatar

FROM
 
posts

JOIN
 
users
 
ON
 
users
.
id
 
=
 
posts
.
author_id
;

Enter fullscreen mode

Exit fullscreen mode

One query. Done. This is not a performance tradeoff. There is no version of the world where 201 queries is better than 1.

### Selecting Everything

const
 
user
 
=
 
await
 
db
.
query
(
'
SELECT * FROM users WHERE id = ?
'
,
 
[
id
]);

return
 
{
 
name
:
 
user
.
name
,
 
email
:
 
user
.
email
 
};

Enter fullscreen mode

Exit fullscreen mode

You fetched every column including the password hash, the encrypted recovery codes, the full address, the preferences blob, and the thirty other fields your schema has accumulated over three years. You used two of them.

Every extra column is bytes over the network, memory allocated, time spent serializing and deserializing. More importantly,SELECT *means your application will silently break or leak data if someone adds a sensitive column to that table later.

Select what you need. Always.

### Synchronous Work That Does Not Need To Be Synchronous

// These two things don't depend on each other

const
 
user
 
=
 
await
 
getUser
(
userId
);

const
 
settings
 
=
 
await
 
getSettings
(
userId
);

const
 
permissions
 
=
 
await
 
getPermissions
(
userId
);

Enter fullscreen mode

Exit fullscreen mode

Eachawaitwaits for the previous call to finish before starting the next. If each takes 50ms, you have spent 150ms doing work that could have been done in 50ms.

const
 
[
user
,
 
settings
,
 
permissions
]
 
=
 
await
 
Promise
.
all
([

 
getUser
(
userId
),

 
getSettings
(
userId
),

 
getPermissions
(
userId
)

]);

Enter fullscreen mode

Exit fullscreen mode

Three concurrent requests, one round of waiting. This is not a micro-optimization. It is understanding how asynchronous code works, which is a baseline expectation for anyone writing it.

### Rendering Thousands of DOM Nodes Because It Is Easy

A dropdown with 8,000 options. A table with 50,000 rows. A chat window that mounts every message since 2019 into the DOM.

The browser has to create, style, layout, and paint every one of those nodes. Then it has to keep them in memory. Scrolling becomes janky. Interactions stutter. The user experience becomes noticeably bad.

Virtualization, pagination, and windowing exist. They are not heroic performance engineering. They are the correct default for lists of unbounded size.

### Not Caching Things That Never Change

// Called on every request

const
 
countries
 
=
 
await
 
db
.
query
(
'
SELECT * FROM countries ORDER BY name
'
);

Enter fullscreen mode

Exit fullscreen mode

There are 195 countries. The list has not changed meaningfully in decades. You are hitting the database for it on every single page load.

A cache with a 24-hour TTL, or even just an in-memory constant loaded at startup, costs essentially nothing and eliminates the query entirely. This is not premature. This is reading the data and making an obvious decision about it.

## Why This Keeps Happening

The honest answer is that slow code usually still works. The user experiences a delay. The developer does not feel the delay because they are testing on localhost against a database with 50 rows. The feature ships. The slowness becomes someone else's problem later.

There is also a subtler force at play. Modern frameworks and ORMs make it extremely easy to write slow code. ActiveRecord's lazy loading, GraphQL resolvers that each hit the database, React components that fetch independently of their siblings. These tools are excellent. They also make it trivially easy to produce N+1 queries without ever writing a single explicit loop.

The tools do not save you from understanding what they are doing on your behalf. That is still your job.

## The Standard Worth Holding

"We'll optimize it later" is a reasonable thing to say about caching strategies, query tuning, and infrastructure scaling. It is not a reasonable thing to say about selecting fewer columns, batching database calls, or running independent tasks in parallel.

The bar is not "did the feature ship." The bar is "does the feature ship without obvious waste."

Profiling before optimizing is correct. Knowing what your code does before you write it is also correct. These are not in conflict. You do not need a profiler to know that 200 database queries is more than 1.

## A Practical Filter

When you are writing code and wondering whether something is premature optimization or basic competence, ask one question:

Do I need to measure anything to know this is slower?

If the answer is yes, finish the feature and measure later. That is the Knuth principle in action.

If the answer is no, if the slower choice is obviously slower by construction and the better choice takes the same amount of time to write, then shipping the slow version is not a principled stance on optimization. It is just not doing the work.

Your users feel the difference. The profiler just helps you find it on a map.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse