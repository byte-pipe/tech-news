---
title: Why I, as Someone Who Likes MySQL, Now Want to Recommend PostgreSQL - DEV Community
url: https://dev.to/catatsuy/why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql-2a8i
site_name: devto
content_file: devto-why-i-as-someone-who-likes-mysql-now-want-to-recom
fetched_at: '2026-03-17T11:21:43.682017'
original_url: https://dev.to/catatsuy/why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql-2a8i
author: catatsuy
date: '2026-03-15'
description: Why I now recommend PostgreSQL for new applications, even though I still like MySQL and have used it for a long time. Tagged with mysql, postgres, database, sql.
tags: '#mysql, #postgres, #database, #sql'
---

I like MySQL. I have used it for a long time, and I have also operated it in on-premises environments.

However, since joining my current company, I have had more opportunities to use PostgreSQL. At first, I honestly felt a lot of resistance to it. I had used MySQL for so long, so part of it was just habit, and I think I was also more wary of PostgreSQL than I needed to be.

But as I actually used it, I gradually started to see what was good about PostgreSQL. These days, if someone asks me which one I would choose for a new project, I have come to feel that I would want to choose PostgreSQL.

Because I have used MySQL for a long time, I also know the rough edges that older MySQL had. At the same time, I think it is inaccurate to talk about MySQL today based only on old impressions. If you configuresql_modeproperly, you can avoid many dangerous behaviors, and MySQL 8 added a large number of features.

Also, this time I want to compare current MySQL and PostgreSQL on the assumption that they will run in the cloud, rather than based on impressions from the on-premises era. Some of the things that used to be described as disadvantages of PostgreSQL are no longer very important issues now.

This is not a story about “MySQL is bad.” It is also not a story like “the philosophy of PostgreSQL is beautiful.”

If I write only the conclusion, it is these two points:

* Things that used to be considered disadvantages of PostgreSQL have become much less important. The feature gap has narrowed a lot, and under the assumption of managed services, there are more things you do not need to worry about.
* On the other hand, from the perspective of application implementation, there are still points where PostgreSQL is clearly better.

In this article, I will organize the discussion from that perspective.

## What used to be considered disadvantages of PostgreSQL has become much less significant

In older comparisons, PostgreSQL’s weaknesses were often said to be heavier operations and awkwardness around DDL.

But I think bringing those points up as-is today is a bit outdated.

MySQL has become very strong in online DDL, but at least for everyday tasks like adding columns, I do not think there is still a clear difference between MySQL and PostgreSQL. Partitioning is also no longer as big an issue as it once felt.

Also, operational topics specific to PostgreSQL, such asVACUUM, come up much less often when you assume managed services, because users have far fewer situations where they need to handle them directly. I do not think it is very fair to bring comparisons from the old on-premises era, where you had to manage everything yourself, directly into the current cloud era.

The differences around replication have also become less visible recently, because managed services have become the mainstream, and there are more parts that users do not directly touch. I feel there are fewer situations than before where I strongly notice an advantage on the MySQL side.

In other words, some of the things that used to be valid reasons not to recommend PostgreSQL have now become much weaker.

## Even so, PostgreSQL is stronger for application implementation

This is the main point.

MySQL 8 closed a lot of the gap. Even so, when I look at things from the standpoint of someone actually writing applications, there are still reasons why PostgreSQL is easier to recommend.

## First, the things MySQL 8 added and narrowed the gap on

I want to make this clear first. The following are things that used to be described as PostgreSQL advantages, but are no longer decisive because MySQL 8 added them:

* CHECKconstraints
* Window functions
* SKIP LOCKED

At this point, it is not fair to talk about these as strengths that only PostgreSQL has.

However, as I will explain later, “window functions themselves were added in MySQL 8” and “being able to naturally bring window functions into update processing” are different things. I still think PostgreSQL is much easier to work with for the latter.

## ON CONFLICT DO NOTHINGis not a replacement forINSERT IGNORE

This is a feature MySQL did not originally have, and it is one of the fairly big reasons why I recommend PostgreSQL.

MySQL hasINSERT IGNORE.

However, this is hard to treat as a replacement forON CONFLICT DO NOTHING.

PostgreSQL’sON CONFLICT DO NOTHINGis, basically, a feature that explicitly says: “Do not insert only when a unique constraint conflict occurs.” What you want to do becomes SQL exactly as it is.

By contrast, MySQL’sINSERT IGNOREis not a dedicated feature only for ignoring duplicates. It is a feature that turns errors into warnings and continues processing, so it is too broad for the use case of “I only want to ignore duplicates.”

This difference may look small, but in practice it is quite large.

It makes the behavior easier to read during review, and it makes it less likely that unintended invalid input will be silently accepted.

## RETURNINGis very powerful

This is also a feature MySQL did not originally have, and it is another fairly big reason why I recommend PostgreSQL.

In PostgreSQL, you can useINSERT/UPDATE/DELETE ... RETURNING. Because you can return the changed result right there, you can naturally complete “get the result of the change” in a single statement.

For example, you can do this:

INSERT

INTO

users
(
name
,

email
)

VALUES
(
'catatsuy'
,

'catatsuy@example.com'
)

RETURNING

id
,

name
,

email
,

created_at
;

Enter fullscreen mode

Exit fullscreen mode

When you have this, the following become very natural:

* receive the inserted ID directly
* receive default values or stored values directly
* return the updated row as-is and use it as the API response
* receive the result of an upsert directly

To be honest, theLAST_INSERT_ID()-based style that is common in MySQL is quite limiting.

The information you can get back is narrow, and basically centered on getting a numericAUTO_INCREMENTID.

You cannot naturally receive arbitrary columns from the inserted result, and you also cannot return the completed row as-is including default values and generated columns.

For example, what you may want is something like this:

* you use UUIDs as primary keys, so you want to return them directly
* you want to return the completed row including generated columns and default values
* you want to pass the entire inserted row directly to the next step

You cannot do this withLAST_INSERT_ID().

In addition, even when multiple rows are inserted in a single statement,LAST_INSERT_ID()does not return the inserted result as-is. What you can get is only the firstAUTO_INCREMENTvalue.

So if you want to handle the result of a multi-rowINSERTdirectly in the application, it is inconvenient. With PostgreSQL’sRETURNING, you can return the inserted rows directly, and this difference is very large.

“Being able to return the changed result directly” is not just a convenience feature. It affects the very way you structure application implementation.

## VALUEShelps in real implementation

This is not about a feature that MySQL entirely lacks. Rather, I think PostgreSQL lets you use it much more naturally.

It is easy to create a small constant table on the spot, join with it, and connect it directly to update processing. When you have this, you do not need to push half-baked temporary-table-like processing out to the application side.

For example, when you want to join a small number of values received from the application and update based on them, in PostgreSQL you can write:

UPDATE

users

u

SET

plan

=

v
.
plan

FROM

(


VALUES


(
1
,

'pro'
),


(
2
,

'free'
),


(
3
,

'team'
)

)

AS

v
(
id
,

plan
)

WHERE

u
.
id

=

v
.
id
;

Enter fullscreen mode

Exit fullscreen mode

This kind of processing comes up very often in real implementation.

For example, you may want to pass a small set of master-like values on the spot and update with them, or send a group of values received from an API directly into SQL.

As another example, it is also natural to treat a group of values received from the application as a join target:

SELECT

u
.
*

FROM

users

u

JOIN

(


VALUES


(
1
),


(
2
),


(
5
)

)

AS

v
(
id
)

ON

u
.
id

=

v
.
id
;

Enter fullscreen mode

Exit fullscreen mode

It is not that MySQL cannot do similar things at all. Since MySQL 8.0.19, it has had theVALUESstatement, and it can be treated as a table value constructor.

However, in MySQL you need to write it withROW(...), and if you leave column names as they are, they become things likecolumn_0andcolumn_1. It feels a bit different from PostgreSQL, where you create a small constant table on the spot, give it natural column names, and flow it directly into aJOINorUPDATE.

For example, in MySQL the same idea would look like this:

SELECT

u
.
*

FROM

users

u

JOIN

(


VALUES

ROW
(
1
),

ROW
(
2
),

ROW
(
5
)

)

AS

v

ON

u
.
id

=

v
.
column_0
;

Enter fullscreen mode

Exit fullscreen mode

It is not a flashy feature, but this kind of thing affects the ease of everyday implementation.

## Being able to bring window functions into update processing is powerful

This part is important.

Window functions themselves were added in MySQL 8.

So it is wrong to talk about window functions themselves as a PostgreSQL-only strength.

However, in PostgreSQL, by combining them withWITHandUPDATE ... FROM, it is easy to bring the result of window functions naturally into update processing. I think there is still a difference here.

For example, if you want to set a flag only on the latest row for each user, you can write:

WITH

ranked

AS

(


SELECT


id
,


ROW_NUMBER
()

OVER
(
PARTITION

BY

user_id

ORDER

BY

created_at

DESC
)

AS

rn


FROM

sessions

)

UPDATE

sessions

s

SET

is_latest

=

(
r
.
rn

=

1
)

FROM

ranked

r

WHERE

s
.
id

=

r
.
id
;

Enter fullscreen mode

Exit fullscreen mode

Window functions themselves do exist in MySQL 8.

However, PostgreSQL is much more natural when it comes to connecting them to this kind of update logic.

This is not just a convenience feature for analytics. It works as a weapon for application implementation.

## Partial indexes are a clear feature difference

This is something I can clearly describe as a feature difference.

MySQL did not originally have it, and it is still missing now.

PostgreSQL has partial indexes, and you can create an index only on some rows, such as withWHERE deleted_at IS NULL. This fits very well with soft delete patterns, and it is also useful for managing records by status.

CREATE

INDEX

idx_users_active_email

ON

users
(
email
)

WHERE

deleted_at

IS

NULL
;

Enter fullscreen mode

Exit fullscreen mode

For example, if you have a table using soft deletes and you only want to speed up “search by email address among active users,” you can write that directly.

In MySQL, you can do something similar using generated columns or functional indexes. However, that is not a replacement for partial indexes.

PostgreSQL partial indexes put only the rows that satisfy a condition likeWHERE deleted_at IS NULLinto the index. In other words, unnecessary rows are excluded from the index from the beginning.

By contrast, MySQL generated columns and functional indexes basically evaluate an expression for all rows and then index that result. If you design the expression well, you can use them for similar purposes, but they do not directly express “an index that physically stays small by containing only some rows.”

So in terms of size, update cost, and clarity of intent, PostgreSQL’s partial indexes are more straightforward. The MySQL side can be used as a workaround, but it is hard to say it has the same feature.

This is not just a difference in how the SQL feels to write. It is a real feature difference, and a reason to recommend PostgreSQL.

## Foreign keys are much better in PostgreSQL

This is my personal impression, but I feel there are many people in the MySQL world who think foreign keys are unnecessary, while in the PostgreSQL world there are many people who think foreign keys are necessary.

I think this comes not so much from a difference in philosophy, but from differences in how easy they are to test with, how easy they are to operate, and how hard they make it for bugs to enter.

### PostgreSQL supports deferred constraints

In PostgreSQL, foreign keys can be madeDEFERRABLE.

This is extremely important.

CREATE

TABLE

authors

(


id

bigint

PRIMARY

KEY

);

CREATE

TABLE

books

(


id

bigint

PRIMARY

KEY
,


author_id

bigint

NOT

NULL
,


CONSTRAINT

books_author_fk


FOREIGN

KEY
(
author_id
)


REFERENCES

authors
(
id
)


DEFERRABLE

INITIALLY

DEFERRED

);

Enter fullscreen mode

Exit fullscreen mode

Because of this, you can delay constraint checks until the end of the transaction.

BEGIN
;

INSERT

INTO

books
(
id
,

author_id
)

VALUES
(
1
,

100
);

INSERT

INTO

authors
(
id
)

VALUES
(
100
);

COMMIT
;

Enter fullscreen mode

Exit fullscreen mode

This SQL works in PostgreSQL.

The parent does not exist in the middle, but it is fine as long as consistency is satisfied at commit time.

What is this useful for?

* loading data that includes circular references
* creating complex test data
* migration processes where the order is temporarily reversed
* bulk inserts and replacement operations

These kinds of processes come up normally in real work.

And whether or not you can write them naturally is a very big deal.

### MySQL forces strict ordering

MySQL does not have this mechanism.

NO ACTIONis effectivelyRESTRICT.

In other words, you cannot structure processing in the form of “it is okay as long as it is consistent in the end.” You are always constrained by ordering rules where the parent must come first and the child must come after.

This may look like a small issue, but it makes loading test data and writing migration processes much harder.

For example, in test code, if you want to roughly load fixtures spanning multiple tables, in PostgreSQL you can write it so that consistency is satisfied by the end of the transaction. In MySQL you cannot do that, so you always need to manage fixture insertion order strictly.

If using foreign keys makes testing more troublesome, I think it is natural that a culture emerges where people say, “Then let’s stop using foreign keys.”

### MySQL makes it easy to escape by disabling foreign keys

In MySQL, you can disable constraints withforeign_key_checks=0.

This looks convenient, but it is quite dangerous.

SET

foreign_key_checks

=

0
;

INSERT

INTO

books
(
id
,

author_id
)

VALUES
(
1
,

999
);

SET

foreign_key_checks

=

1
;

Enter fullscreen mode

Exit fullscreen mode

With this, inconsistent data inserted while constraints are disabled can remain.

Even if you enable them again, MySQL does not go back and verify all inconsistencies that were inserted during that time.

With this behavior, it becomes easy for accidents to happen where constraints are turned off for testing or migration convenience, and inconsistent data is brought in as-is.

PostgreSQL has a tool that says, “Keep the constraints, but delay the check timing.”

MySQL tends to go in the direction of “turn off the constraints themselves.”

This difference is quite large.

### You can see the difference even from a foreign key example alone

For example, consider an ordinary pair of tables with a parent-child relationship.

CREATE

TABLE

users

(


id

bigint

PRIMARY

KEY

);

CREATE

TABLE

orders

(


id

bigint

PRIMARY

KEY
,


user_id

bigint

NOT

NULL
,


CONSTRAINT

orders_user_fk


FOREIGN

KEY
(
user_id
)


REFERENCES

users
(
id
)


DEFERRABLE

INITIALLY

DEFERRED

);

Enter fullscreen mode

Exit fullscreen mode

In PostgreSQL, even during tests, you can write something like inserting intoordersfirst and then inserting intouserslater, as long as it is within a transaction.

BEGIN
;

INSERT

INTO

orders
(
id
,

user_id
)

VALUES
(
10
,

1
);

INSERT

INTO

users
(
id
)

VALUES
(
1
);

COMMIT
;

Enter fullscreen mode

Exit fullscreen mode

This flexibility helps a lot with fixture creation, data migration, and simplifying test code.

MySQL does not have this.

So in MySQL it is easier for people to drift toward thinking, “Foreign keys are in the way, so turn them off,” or “Guarantee it in the application,” while in PostgreSQL it is easier to drift toward thinking, “Let’s use foreign keys properly.”

The reason PostgreSQL foreign keys are better is not simply that they have more features.

A big part of it is that they make it easier to write tests, migrations, and data loading while keeping the constraints intact, and as a result, it becomes easier to actually use foreign keys in production.

## In MySQL, you cannot do vector operations

Recently, I think this is probably the reason most often mentioned for adopting PostgreSQL.

PostgreSQL haspgvector, which not only allows you to store vectors, but also lets you use distance operations and similarity search directly from applications. It also has indexes for nearest-neighbor search, so it is easy to use directly in implementation.

By contrast, assuming the OSS edition, MySQL added a Vector type in MySQL 9.0, which has already been released as an Innovation Release, while the LTS version has not yet been released. However, distance functions are provided only in MySQL HeatWave on OCI and MySQL AI, and are not included in MySQL Commercial or Community. In other words, in the OSS edition you cannot do vector operations, so it is not really usable for this. This is a clear difference from PostgreSQL +pgvector.

## Character sets and collations are still more complicated in MySQL

This is also very important.

I still think character sets and collations are more likely to cause trouble in MySQL than in PostgreSQL.

However, this is not only a problem with MySQL itself. It includes frameworks, connectors, and default settings as well.

There are well-known examples in Japan such as the so-called “Haha-Papa problem” and “Sushi-Beer problem.”

Both of these are not so much character encoding problems as collation problems.

* The Haha-Papa problem is when strings that look different are treated as the same because of collation rules.
* The Sushi-Beer problem is when comparisons involving emoji and similar characters do not behave the way you intuitively expect.

What makes these problems troublesome is that “we changed it to utf8mb4, so we are done” is not enough. In reality, you need to understand both the character set and the collation.

And in MySQL 8, rather than making this simpler, it actually gave us even more things to think about. New collations were added, and they coexist with older systems, so “the old style,” “the post-MySQL-8 style,” and “framework defaults” do not always line up.

In other words, MySQL 8 certainly improved some things, but because old and new styles now coexist as a result of those improvements, the overall situation has in some ways become even more chaotic.

I think this is not so much because MySQL itself is bad, but because it has a long history and has evolved while carrying compatibility with it.

Still, from the point of view of an application developer, that complexity directly becomes an entry point for accidents.

## Summary

In the past, PostgreSQL had some clear weaknesses too.

But now, many of them have become much less significant. The feature gap has narrowed, and under the assumption of managed services, there are more things users do not need to think about directly.

On the other hand, from the point of view of application implementation, there are still reasons why PostgreSQL is easier to recommend.

The especially big ones are these.

### Things MySQL 8 added and narrowed the gap on

* CHECKconstraints
* Window functions
* SKIP LOCKED

### Clear reasons to recommend PostgreSQL

* ON CONFLICT DO NOTHING
* RETURNING
* VALUES
* being able to bring window functions into update processing
* partial indexes
* the maturity of foreign keys
* vector operations throughpgvector
* being less likely to cause trouble around character sets and collations

I like MySQL.

I have used it for a long time, and I still think it is a good database that is easy to get good performance from.

Even so, if the question is which one I would adopt for a new project today, the one I would recommend is PostgreSQL.

That is not because MySQL is bad.

It is because even now, after many of its old weaknesses have been filled in, I still think PostgreSQL has an advantage when it comes to ease of application implementation.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
