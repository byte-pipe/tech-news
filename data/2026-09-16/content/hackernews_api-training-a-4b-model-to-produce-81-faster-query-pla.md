---
title: Training a 4B model to produce 81% faster query plans than Postgres - Rohan Bansal
url: https://rohanbansal.com/qorl
site_name: hackernews_api
content_file: hackernews_api-training-a-4b-model-to-produce-81-faster-query-pla
fetched_at: '2026-09-16T21:54:40.563794'
original_url: https://rohanbansal.com/qorl
author: polyphilz
date: '2026-09-16'
published_date: '2026-09-16T00:00:00.000Z'
description: '...or how to make Qwen learn query optimization via agentic reinforcement learning'
tags:
- hackernews
- trending
---

## How good are query optimizers, really?

Leis et al.asked this exact question in 2015. Then,they asked it again 10 years later.

Despite an enormous body of research spanning a decade since their original exploration, they found that query optimizers continue to leave much to be desired.

I was surprised when I first learned about this. A Postgres databaseshouldknow everything about the stuff that lives in its tables, no? How hard can it be?

As it turns out: enormously hard. In fact, one particular task a query optimizer needs to do, join ordering, isknown to be NP-hard.

So query optimizers are hard. What’snotas hard is verifying whether a query plan an optimizer picks is good or not. Put simply, a good query optimizer produces plans that run fast, and a bad one produces slow plans. Language models are particularly good at learning how to do tasks with easily verifiable outputs. Because there’s a single axis to optimize for—execution time of a query—the problem beautifully reduces to reinforcing the behaviors that guide a model to produce faster query plans.

What follows is a breakdown of an experiment I ran to explore the question: can a small, open-weights model be post-trained via supervised fine-tuning (SFT) and agentic reinforcement learning (RL) to produce Postgres query plans that beat Postgres’s default plans?

The answer to our question is a resounding yes. Highlights include:

* Attaining a44.7% latency reductionacross 113 join-heavy queries from a 4B model initially unable to produce a query plan for 99 of them
* Constructing a Postgres measurement rig that minimizes Linux page cache contention noise across concurrent containers
* Designing a custom GRPO variant for scoring RL rollouts in an inherently noisy environment
* Splitting RL across two machines: vLLM and the trainer on a rented 2x H100 node and four Postgres containers running on my desk
* Running off-policy distillation across half a thousand GPT-6 Astra agent trajectories

Let’s start from the beginning.

## Inside a query optimizer

Consider the following slice of theIMDb dataset:

-- An IMDb title (movie, series, episode, etc.) [~1M rows]

title (

 id 
integer
 PRIMARY KEY
,

 title 
text
,

 production_year 
integer
,

 kind_id 
integer
 -- FK -> kind_type

)

-- Movie <> company junction table [~2M rows]

movie_companies (

 id 
integer
 PRIMARY KEY
,

 movie_id 
integer
, 
-- FK -> title.id

 company_id 
integer
, 
-- FK -> company_name.id

 company_type_id 
integer
, 
-- FK -> company_type.id

 note 
text

)

-- A company's name, origin, etc. [~100k rows]

company_name (

 id 
integer
 PRIMARY KEY
,

 name
 text
,

 country_code 
text
 -- '[us]', '[jp]', ...

)

-- Lookup table of company roles for a title [4 rows]

company_type (

 id 
integer
 PRIMARY KEY
,

 kind 
text
 -- 'production companies', 'distributors', ...

)

-- Lookup table for what a title _is_ [7 rows]

kind_type (

 id 
integer
 PRIMARY KEY
,

 kind 
text
 -- 'movie', 'tv series', 'episode', ...

)

Let’s say I’m trying to answer the question: “Which Japanese companies put out the most titles in the 2000s?” We might write the following query:

SELECT
 cn
.
name
,

 COUNT
(
*
) 
AS
 titles

FROM
 title 
AS
 t,

 movie_companies 
AS
 mc,

 company_name 
AS
 cn

WHERE
 t
.
id
 =
 mc
.
movie_id

 AND
 mc
.
company_id
 =
 cn
.
id

 AND
 cn
.
country_code
 =
 '
[jp]
'

 AND
 t
.
production_year
 BETWEEN
 2000
 AND
 2009

GROUP BY
 cn
.
name

ORDER BY
 titles 
DESC

LIMIT
 10
;

Running this query outputs 10 Japanese companies with the number of titles they were associated with between 2000 and 2009, sorted from highest to lowest.

Buthowdid Postgres get these results?

The path Postgres took to get this data for us is not a foregone conclusion, and it has everything to do with what we call selective predicates (i.e. the filtering conditions in aWHEREclause).

To illustrate this, let’s imagine our same query without the Japanese company filter or the date range filter:

SELECT
 cn
.
name
,

 COUNT
(
*
) 
AS
 titles

FROM
 title 
AS
 t,

 movie_companies 
AS
 mc,

 company_name 
AS
 cn

WHERE
 t
.
id
 =
 mc
.
movie_id

 AND
 mc
.
company_id
 =
 cn
.
id

GROUP BY
 cn
.
name

ORDER BY
 titles 
DESC

LIMIT
 10
;

mccan only join withcnviamc.company_id = cn.id, andtcan only join withmcviat.id = mc.movie_id.

These constraints producetwoThere are technically eight join trees if we take commutativity into account. In this case, we don’t because it doesn’t affect the size of the relations resulting from the joins.valid join trees:

 
 
 
 
 
 
 
 ⋈ 
 
 
 
 
Join of (
company_name
 ⋈ 
movie_companies
) with 
title
 
 
 
 
 
 ⋈ 
 
 
 
 
Join of 
company_name
 with 
movie_companies
 
 
 
 
 
 t 
 
 
 
 
title
 relation
 
 
 
 
 
 cn 
 
 
 
 
company_name
 relation
 
 
 
 
 
 mc 
 
 
 
 
movie_companies
 relation
 
 
 
 
 (cn ⋈ mc) ⋈ t 
 
 
 
 
 
 ⋈ 
 
 
 
 
Join of (
title
 ⋈ 
movie_companies
) with 
company_name
 
 
 
 
 
 ⋈ 
 
 
 
 
Join of 
title
 with 
movie_companies
 
 
 
 
 
 cn 
 
 
 
 
company_name
 relation
 
 
 
 
 
 t 
 
 
 
 
title
 relation
 
 
 
 
 
 mc 
 
 
 
 
movie_companies
 relation
 
 
 
 
 (t ⋈ mc) ⋈ cn 
 
 
 
 
 The two join trees for our query. The lower join runs first; the result is an input into the root join. 
 

Thecardinalityof a table or query result is the number of rows it contains. Assume the relevant tables have the following cardinalities:

1. cn=100kcn = 100\text{k}cn=100k
2. mc=2mmc = 2\text{m}mc=2m
3. t=1mt = 1\text{m}t=1m

Taking into account our joins, we get the following cardinalities:

(
c
n
⋈
m
c
)
=
2
m
,
 then 
⋈
t
=
2
m
(cn \bowtie mc) = 2\text{m}, \text{ then } \bowtie t = 2\text{m}
(
c
n
⋈
m
c
)
=
2
m
,
 then 
⋈
t
=
2
m

(
t
⋈
m
c
)
=
2
m
,
 then 
⋈
c
n
=
2
m
(t \bowtie mc) = 2\text{m}, \text{ then } \bowtie cn = 2\text{m}
(
t
⋈
m
c
)
=
2
m
,
 then 
⋈
c
n
=
2
m

Regardless of the order in which these three tables are joined, the same 2m rows are always passed into the second join.

Now let’s add back our selective predicates:

1. cn′=5kcn' = 5\text{k}cn′=5k(assuming 5% of our 100k companies are Japanese)
2. mc=2mmc = 2\text{m}mc=2m(does not change)
3. t′=200kt' = 200\text{k}t′=200k(assuming 20% of our 1m titles were made in the 2000s)

(
c
n
′
⋈
m
c
)
≈
100
k
,
 then 
⋈
 
t
′
≈
20
k
(cn' \bowtie mc) \approx 100\text{k}, \text{ then } \bowtie\ t' \approx 20\text{k}
(
c
n
′
⋈
m
c
)
≈
100
k
,
 then 
⋈
 
t
′
≈
20
k

(
t
′
⋈
m
c
)
≈
400
k
,
 then 
⋈
 
c
n
′
≈
20
k
(t' \bowtie mc) \approx 400\text{k}, \text{ then } \bowtie\ cn' \approx 20\text{k}
(
t
′
⋈
m
c
)
≈
400
k
,
 then 
⋈
 
c
n
′
≈
20
k

The first join ordering filters the 2mmovie_companiesentries down to the 5% slice of companies that are Japanese. Assuming uniform distribution (we’ll discuss laterwhywe assume this), this join results in approximately 100k rows. Joining the result with the filteredtitletable keeps only the 20% of those rows from the 2000s.

The second join ordering filters the 2mmovie_companiesentries down to the 20% slice of titles that were made in the 2000s. The same uniformity assumption holds, so the first join results in 400k rows, meaning we’re passing 400k rows into the second join.

We do4xthe work if we picked the second join ordering.

Unfortunately, it doesn’t stop there.

### A combinatorial explosion

Each join can use any of:

1. Hash join
2. Merge join
3. Nested-loop join

Factoring commutativity back innowWhile commutativity doesn’t change the number of rows produced, it must be considered now because itdoesaffect performance regarding the join algorithm used., there are 4 different outer/inner joinorientations, resulting in 8 possible combinations:

 

(cn⋈mc)⋈t(cn \bowtie mc) \bowtie t(cn⋈mc)⋈tt⋈(cn⋈mc)t \bowtie (cn \bowtie mc)t⋈(cn⋈mc)

(mc⋈cn)⋈t(mc \bowtie cn) \bowtie t(mc⋈cn)⋈tt⋈(mc⋈cn)t \bowtie (mc \bowtie cn)t⋈(mc⋈cn)

(t⋈mc)⋈cn(t \bowtie mc) \bowtie cn(t⋈mc)⋈cncn⋈(t⋈mc)cn \bowtie (t \bowtie mc)cn⋈(t⋈mc)

(mc⋈t)⋈cn(mc \bowtie t) \bowtie cn(mc⋈t)⋈cncn⋈(mc⋈t)cn \bowtie (mc \bowtie t)cn⋈(mc⋈t)

 

Lastly, each table can be scanned in different ways. Considering just four types of scans:

1. Sequential
2. Index
3. Index-only
4. Bitmap

 
 

2Join trees: which pair of tables joins first.×22Orientations: each of the 2 joins can swap which input is outer and which is inner.×32Algorithms: each of the 2 joins picks hash, merge, or nested loop.×43Scans: each of the 3 tables is either read sequentially or via index, index-only or bitmap scans.=4,608

 
 
 
 

There are 4,608 different ways to run thisqueryThis is actually an undercount. Plans can run in parallel, aggregates can be hashed or sorted, etc.It’s also worth noting that Postgres doesn’t evaluate all of these plans. It uses dynamic programming (and agenetic algorithmfor queries involving 12+ joins) to prune the search space.!

To make matters worse, every join combinatorially explodes the search space:

 
 
 
 
 
SELECT
 cn
.
name
,

 COUNT
(
*
) 
AS
 titles

FROM
 movie_companies 
AS
 mc,

 company_name 
AS
 cn

WHERE
 mc
.
company_id
 =
 cn
.
id

 AND
 cn
.
country_code
 =
 '
[jp]
'

GROUP BY
 cn
.
name

ORDER BY
 titles 
DESC

LIMIT
 10
;
 
 
 

1Join trees: with two tables there is only one way to join them.×21Orientation: 1 join means there are only 2 orientations.×31Algorithm: the join algorithm can be a hash join, merge join or nested loop.×42Scans: each of the 2 tables is either read sequentially or via index, index-only or bitmap scans.=96

 
 
 
 
SELECT
 cn
.
name
,

 COUNT
(
*
) 
AS
 titles

FROM
 title 
AS
 t,

 movie_companies 
AS
 mc,

 company_name 
AS
 cn

WHERE
 t
.
id
 =
 mc
.
movie_id

 AND
 mc
.
company_id
 =
 cn
.
id

 AND
 cn
.
country_code
 =
 '
[jp]
'

 AND
 t
.
production_year
 BETWEEN
 2000
 AND
 2009

GROUP BY
 cn
.
name

ORDER BY
 titles 
DESC

LIMIT
 10
;
 
 
 

2Join trees: the ways 3 tables can be joined up, before any swapping of inputs.×22Orientations: each of the 2 joins can swap which input is outer and which is inner.×32Algorithms: each of the 2 joins picks hash, merge, or nested loop.×43Scans: each of the 3 tables is either read sequentially or via index, index-only or bitmap scans.=4,608

 
 
 
 
SELECT
 MIN
(
t
.
title
) 
AS
 movie_title

FROM
 keyword 
AS
 k,

 movie_info 
AS
 mi,

 movie_keyword 
AS
 mk,

 title 
AS
 t

WHERE
 k
.
keyword
 LIKE
 '
%sequel%
'

 AND
 mi
.
info
 IN
 (
'
Bulgaria
'
)

 AND
 t
.
production_year
 >
 2010

 AND
 t
.
id
 =
 mi
.
movie_id

 AND
 t
.
id
 =
 mk
.
movie_id

 AND
 mk
.
movie_id
 =
 mi
.
movie_id

 AND
 k
.
id
 =
 mk
.
keyword_id
;
 
 
 

8Join trees: the ways 4 tables can be joined up, before any swapping of inputs.×23Orientations: each of the 3 joins can swap which input is outer and which is inner.×33Algorithms: each of the 3 joins picks hash, merge, or nested loop.×44Scans: each of the 4 tables is either read sequentially or via index, index-only or bitmap scans.=442,368

 
 
 
 
SELECT
 MIN
(
t
.
title
) 
AS
 movie_title

FROM
 company_name 
AS
 cn,

 keyword 
AS
 k,

 movie_companies 
AS
 mc,

 movie_keyword 
AS
 mk,

 title 
AS
 t

WHERE
 cn
.
country_code
 =
'
[de]
'

 AND
 k
.
keyword
 =
'
character-name-in-title
'

 AND
 cn
.
id
 =
 mc
.
company_id

 AND
 mc
.
movie_id
 =
 t
.
id

 AND
 t
.
id
 =
 mk
.
movie_id

 AND
 mk
.
keyword_id
 =
 k
.
id

 AND
 mc
.
movie_id
 =
 mk
.
movie_id
;
 
 
 

25Join trees: the ways 5 tables can be joined up, before any swapping of inputs.×24Orientations: each of the 4 joins can swap which input is outer and which is inner.×34Algorithms: each of the 4 joins picks hash, merge, or nested loop.×45Scans: each of the 5 tables is either read sequentially or via index, index-only or bitmap scans.=33,177,600

 
 
 
 
SELECT
 MIN
(
lt
.
link
) 
AS
 link_type,

 MIN
(
t1
.
title
) 
AS
 first_movie,

 MIN
(
t2
.
title
) 
AS
 second_movie

FROM
 keyword 
AS
 k,

 link_type 
AS
 lt,

 movie_keyword 
AS
 mk,

 movie_link 
AS
 ml,

 title 
AS
 t1,

 title 
AS
 t2

WHERE
 k
.
keyword
 =
'
10,000-mile-club
'

 AND
 mk
.
keyword_id
 =
 k
.
id

 AND
 t1
.
id
 =
 mk
.
movie_id

 AND
 ml
.
movie_id
 =
 t1
.
id

 AND
 ml
.
linked_movie_id
 =
 t2
.
id

 AND
 lt
.
id
 =
 ml
.
link_type_id

 AND
 mk
.
movie_id
 =
 t1
.
id
;
 
 
 

56Join trees: the ways 6 tables can be joined up, before any swapping of inputs.×25Orientations: each of the 5 joins can swap which input is outer and which is inner.×35Algorithms: each of the 5 joins picks hash, merge, or nested loop.×46Scans: each of the 6 tables is either read sequentially or via index, index-only or bitmap scans.=1,783,627,776

 
 
 
 
SELECT
 MIN
(
a1
.
name
) 
AS
 writer_pseudo_name,

 MIN
(
t
.
title
) 
AS
 movie_title

FROM
 aka_name 
AS
 a1,

 cast_info 
AS
 ci,

 company_name 
AS
 cn,

 movie_companies 
AS
 mc,

 name
 AS
 n1,

 role_type 
AS
 rt,

 title 
AS
 t

WHERE
 cn
.
country_code
 =
'
[us]
'

 AND
 rt
.
role
 =
'
writer
'

 AND
 a1
.
person_id
 =
 n1
.
id

 AND
 n1
.
id
 =
 ci
.
person_id

 AND
 ci
.
movie_id
 =
 t
.
id

 AND
 t
.
id
 =
 mc
.
movie_id

 AND
 mc
.
company_id
 =
 cn
.
id

 AND
 ci
.
role_id
 =
 rt
.
id

 AND
 a1
.
person_id
 =
 ci
.
person_id

 AND
 ci
.
movie_id
 =
 mc
.
movie_id
;
 
 
 

696Join trees: the ways 7 tables can be joined up, before any swapping of inputs.×26Orientations: each of the 6 joins can swap which input is outer and which is inner.×36Algorithms: each of the 6 joins picks hash, merge, or nested loop.×47Scans: each of the 7 tables is either read sequentially or via index, index-only or bitmap scans.=532,030,685,184

 
 
 
 
SELECT
 MIN
(
an
.
name
) 
AS
 cool_actor_pseudonym,

 MIN
(
t
.
title
) 
AS
 series_named_after_char

FROM
 aka_name 
AS
 an,

 cast_info 
AS
 ci,

 company_name 
AS
 cn,

 keyword 
AS
 k,

 movie_companies 
AS
 mc,

 movie_keyword 
AS
 mk,

 name
 AS
 n,

 title 
AS
 t

WHERE
 cn
.
country_code
 =
'
[us]
'

 AND
 k
.
keyword
 =
'
character-name-in-title
'

 AND
 an
.
person_id
 =
 n
.
id

 AND
 n
.
id
 =
 ci
.
person_id

 AND
 ci
.
movie_id
 =
 t
.
id

 AND
 t
.
id
 =
 mk
.
movie_id

 AND
 mk
.
keyword_id
 =
 k
.
id

 AND
 t
.
id
 =
 mc
.
movie_id

 AND
 mc
.
company_id
 =
 cn
.
id

 AND
 an
.
person_id
 =
 ci
.
person_id

 AND
 ci
.
movie_id
 =
 mc
.
movie_id

 AND
 ci
.
movie_id
 =
 mk
.
movie_id

 AND
 mc
.
movie_id
 =
 mk
.
movie_id
;
 
 
 

4,698Join trees: the ways 8 tables can be joined up, before any swapping of inputs.×27Orientations: each of the 7 joins can swap which input is outer and which is inner.×37Algorithms: each of the 7 joins picks hash, merge, or nested loop.×48Scans: each of the 8 tables is either read sequentially or via index, index-only or bitmap scans.=86,188,970,999,808

 
 
 
 
SELECT
 MIN
(
cn
.
name
) 
AS
 producing_company,

 MIN
(
miidx
.
info
) 
AS
 rating,

 MIN
(
t
.
title
) 
AS
 movie

FROM
 company_name 
AS
 cn,

 company_type 
AS
 ct,

 info_type 
AS
 it,

 info_type 
AS
 it2,

 kind_type 
AS
 kt,

 movie_companies 
AS
 mc,

 movie_info 
AS
 mi,

 movie_info_idx 
AS
 miidx,

 title 
AS
 t

WHERE
 cn
.
country_code
 =
'
[us]
'

 AND
 ct
.
kind
 =
'
production companies
'

 AND
 it
.
info
 =
'
rating
'

 AND
 it2
.
info
 =
'
release dates
'

 AND
 kt
.
kind
 =
'
movie
'

 AND
 mi
.
movie_id
 =
 t
.
id

 AND
 it2
.
id
 =
 mi
.
info_type_id

 AND
 kt
.
id
 =
 t
.
kind_id

 AND
 mc
.
movie_id
 =
 t
.
id

 AND
 cn
.
id
 =
 mc
.
company_id

 AND
 ct
.
id
 =
 mc
.
company_type_id

 AND
 miidx
.
movie_id
 =
 t
.
id

 AND
 it
.
id
 =
 miidx
.
info_type_id

 AND
 mi
.
movie_id
 =
 miidx
.
movie_id

 AND
 mi
.
movie_id
 =
 mc
.
movie_id

 AND
 miidx
.
movie_id
 =
 mc
.
movie_id
;
 
 
 

20,340Join trees: the ways 9 tables can be joined up, before any swapping of inputs.×28Orientations: each of the 8 joins can swap which input is outer and which is inner.×38Algorithms: each of the 8 joins picks hash, merge, or nested loop.×49Scans: each of the 9 tables is either read sequentially or via index, index-only or bitmap scans.=8,955,727,561,359,360

 
 
 
 
SELECT
 MIN
(
n
.
name
) 
AS
 voicing_actress,

 MIN
(
t
.
title
) 
AS
 jap_engl_voiced_movie

FROM
 aka_name 
AS
 an,

 char_name 
AS
 chn,

 cast_info 
AS
 ci,

 company_name 
AS
 cn,

 info_type 
AS
 it,

 movie_companies 
AS
 mc,

 movie_info 
AS
 mi,

 name
 AS
 n,

 role_type 
AS
 rt,

 title 
AS
 t

WHERE
 ci
.
note
 IN
 (
'
(voice)
'
,

 '
(voice: Japanese version)
'
,

 '
(voice) (uncredited)
'
,

 '
(voice: English version)
'
)

 AND
 cn
.
country_code
 =
'
[us]
'

 AND
 it
.
info
 =
 '
release dates
'

 AND
 n
.
gender
 =
'
f
'

 AND
 rt
.
role
 =
'
actress
'

 AND
 t
.
production_year
 >
 2000

 AND
 t
.
id
 =
 mi
.
movie_id

 AND
 t
.
id
 =
 mc
.
movie_id

 AND
 t
.
id
 =
 ci
.
movie_id

 AND
 mc
.
movie_id
 =
 ci
.
movie_id

 AND
 mc
.
movie_id
 =
 mi
.
movie_id

 AND
 mi
.
movie_id
 =
 ci
.
movie_id

 AND
 cn
.
id
 =
 mc
.
company_id

 AND
 it
.
id
 =
 mi
.
info_type_id

 AND
 n
.
id
 =
 ci
.
person_id

 AND
 rt
.
id
 =
 ci
.
role_id

 AND
 n
.
id
 =
 an
.
person_id

 AND
 ci
.
person_id
 =
 an
.
person_id

 AND
 chn
.
id
 =
 ci
.
person_role_id
;
 
 
 

242,160Join trees: the ways 10 tables can be joined up, before any swapping of inputs.×29Orientations: each of the 9 joins can swap which input is outer and which is inner.×39Algorithms: each of the 9 joins picks hash, merge, or nested loop.×410Scans: each of the 10 tables is either read sequentially or via index, index-only or bitmap scans.=2,558,960,455,762,575,360

 
 
 
 
SELECT
 MIN
(
kt
.
kind
) 
AS
 movie_kind,

 MIN
(
t
.
title
) 
AS
 complete_us_internet_movie

FROM
 complete_cast 
AS
 cc,

 comp_cast_type 
AS
 cct1,

 company_name 
AS
 cn,

 company_type 
AS
 ct,

 info_type 
AS
 it1,

 keyword 
AS
 k,

 kind_type 
AS
 kt,

 movie_companies 
AS
 mc,

 movie_info 
AS
 mi,

 movie_keyword 
AS
 mk,

 title 
AS
 t

WHERE
 cct1
.
kind
 =
 '
complete+verified
'

 AND
 cn
.
country_code
 =
 '
[us]
'

 AND
 it1
.
info
 =
 '
release dates
'

 AND
 kt
.
kind
 IN
 (
'
movie
'
)

 AND
 mi
.
note
 LIKE
 '
%internet%
'

 AND
 mi
.
info
 IS NOT NULL

 AND
 (
mi
.
info
 LIKE
 '
USA:% 199%
'

 OR
 mi
.
info
 LIKE
 '
USA:% 200%
'
)

 AND
 t
.
production_year
 >
 2000

 AND
 kt
.
id
 =
 t
.
kind_id

 AND
 t
.
id
 =
 mi
.
movie_id

 AND
 t
.
id
 =
 mk
.
movie_id

 AND
 t
.
id
 =
 mc
.
movie_id

 AND
 t
.
id
 =
 cc
.
movie_id

 AND
 mk
.
movie_id
 =
 mi
.
movie_id

 AND
 mk
.
movie_id
 =
 mc
.
movie_id

 AND
 mk
.
movie_id
 =
 cc
.
movie_id

 AND
 mi
.
movie_id
 =
 mc
.
movie_id

 AND
 mi
.
movie_id
 =
 cc
.
movie_id

 AND
 mc
.
movie_id
 =
 cc
.
movie_id

 AND
 k
.
id
 =
 mk
.
keyword_id

 AND
 it1
.
id
 =
 mi
.
info_type_id

 AND
 cn
.
id
 =
 mc
.
company_id

 AND
 ct
.
id
 =
 mc
.
company_type_id

 AND
 cct1
.
id
 =
 cc
.
status_id
;
 
 
 

1,490,850Join trees: the ways 11 tables can be joined up, before any swapping of inputs.×210Orientations: each of the 10 joins can swap which input is outer and which is inner.×310Algorithms: each of the 10 joins picks hash, merge, or nested loop.×411Scans: each of the 11 tables is either read sequentially or via index, index-only or bitmap scans.=378,099,722,048,923,238,400

 
 
 
 
SELECT
 MIN
(
chn
.
name
) 
AS
 character_name,

 MIN
(
mi_idx
.
info
) 
AS
 rating,

 MIN
(
t
.
title
) 
AS
 complete_hero_movie

FROM
 complete_cast 
AS
 cc,

 comp_cast_type 
AS
 cct1,

 comp_cast_type 
AS
 cct2,

 char_name 
AS
 chn,

 cast_info 
AS
 ci,

 info_type 
AS
 it2,

 keyword 
AS
 k,

 kind_type 
AS
 kt,

 movie_info_idx 
AS
 mi_idx,

 movie_keyword 
AS
 mk,

 name
 AS
 n,

 title 
AS
 t

WHERE
 cct1
.
kind
 =
 '
cast
'

 AND
 cct2
.
kind
 LIKE
 '
%complete%
'

 AND
 chn
.
name
 IS NOT NULL

 AND
 (
chn
.
name
 LIKE
 '
%man%
'

 OR
 chn
.
name
 LIKE
 '
%Man%
'
)

 AND
 it2
.
info
 =
 '
rating
'

 AND
 k
.
keyword
 IN
 (
'
superhero
'
,

 '
marvel-comics
'
,

 '
based-on-comic
'
,

 '
fight
'
)

 AND
 kt
.
kind
 =
 '
movie
'

 AND
 mi_idx
.
info
 >
 '
8.0
'

 AND
 t
.
production_year
 >
 2005

 AND
 kt
.
id
 =
 t
.
kind_id

 AND
 t
.
id
 =
 mk
.
movie_id

 AND
 t
.
id
 =
 ci
.
movie_id

 AND
 t
.
id
 =
 cc
.
movie_id

 AND
 t
.
id
 =
 mi_idx
.
movie_id

 AND
 mk
.
movie_id
 =
 ci
.
movie_id

 AND
 mk
.
movie_id
 =
 cc
.
movie_id

 AND
 mk
.
movie_id
 =
 mi_idx
.
movie_id

 AND
 ci
.
movie_id
 =
 cc
.
movie_id

 AND
 ci
.
movie_id
 =
 mi_idx
.
movie_id

 AND
 cc
.
movie_id
 =
 mi_idx
.
movie_id

 AND
 chn
.
id
 =
 ci
.
person_role_id

 AND
 n
.
id
 =
 ci
.
person_id

 AND
 k
.
id
 =
 mk
.
keyword_id

 AND
 cct1
.
id
 =
 cc
.
subject_id

 AND
 cct2
.
id
 =
 cc
.
status_id

 AND
 it2
.
id
 =
 mi_idx
.
info_type_id
;
 
 
 

11,932,560Join trees: the ways 12 tables can be joined up, before any swapping of inputs.×211Orientations: each of the 11 joins can swap which input is outer and which is inner.×311Algorithms: each of the 11 joins picks hash, merge, or nested loop.×412Scans: each of the 12 tables is either read sequentially or via index, index-only or bitmap scans.=72,630,206,166,931,876,085,760lots!

 
 
 
 
 2 
 3 
 4 
 5 
 6 
 7 
 8 
 9 
 10 
 11 
 12 
 
 
 
 
 Click to select the number of tables being joined together. From four tables onwards, queries on the left are from JOB. On the right is a rough estimate of the size of the search space. 
 

### Estimating, not counting

Postgres is in a tough spot here. It would be reasonable to think it could simply count cardinalities and pick the plan that minimizes the number of rows passed through to successive joins.

But this would imply Postgrescancount cardinalities during query planning. It can’t. In order to know this, it would need to actually run each join and count the resulting rows. This defeats the whole point of a fast query optimizer. A query optimizer does not aim to be exact in its cost minimization… it aims to be good enough across many types of queries.

Instead, Postgres uses statistics to estimate cardinalities. The planner queries thepg_statistictable, getting back common values for each column and their frequencies, and a histogram for the rest. Things get a bit more complicated when you tack on joins. Postgres doesn’t know how the rows in one table are distributed over the other. To get around this, it assumes that the frequency of a given value in the first table can simply be applied over the second table. This is the uniform distribution assumption I mentioned earlier.

Assuming a uniform distribution is fine as a heuristic, but when it fails, it fails hard. Looking back at an earlier join ordering(cn′⋈mc)≈100k,then⋈t′≈20k(cn' \bowtie mc) \approx 100\text{k}, \text{ then } \bowtie\ t' \approx 20\text{k}(cn′⋈mc)≈100k,then⋈t′≈20k, we filtered 2mmovie_companiesentries on the assumption that 5% of them were from Japanese companies. But what if the 5% of companies that are Japanese were actually responsible for50%of the movies? The first join would produce 1m rows! The cost model says pick the first join ordering; in reality, the second one is actually better since it only sends 400k rows through to the second join.

 
 
 
 
Postgres assumption
 
- 
100k
 rows
 
Actual
 
- 
100k
 rows
 
 
 
 
 
 
 
 
 ⋈ 
 
 
 
 
 ⋈ 
 
 
 
 
 t′ 
 
 
 
 
 cn′ 
 
 
 
 
 mc 
 
 
 
 (cn′ ⋈ mc) ⋈ t′ 
 
 
 
 
 
 ⋈ 
 
 
 
 
 ⋈ 
 
 
 
 
 cn′ 
 
 
 
 
 t′ 
 
 
 
 
 mc 
 
 
 
 (t′ ⋈ mc) ⋈ cn′ 
 
 
 
 

Share of 
movie_companies
 rows that belong to Japanese companies:

5%
 
(uniform)
 
 
 
 
 
 
 Drag the slider to make Japanese companies more productive. Notice how Postgres’s estimate is static while actual row counts get affected. 
 

One bad estimate in an early join can cascade through the rest of the join tree, corrupting all other estimates.

## How to steer an elephant

Postgres always picks the plan with the lowest cost, and we can’t change its cost model without modifying its source code, so how can we actually steer it to pick different plans that have higher costs?

Enterpg_hint_plan.

pg_hint_planis a beautifully simple third-party extension: just by adding structured “hints” as comments above SQL statements, you can nudge Postgres towards plans that use the instructions provided in the hint. For example:

 
 
 
/*+
 
HashJoin(a b)
 
SeqScan(a)
*/
EXPLAIN
 
SELECT
 *
 
FROM
 pgbench_branches b
 
JOIN
 pgbench_accounts a 
ON
 b.bid = a.bid
 
ORDER BY
 a.aid;
 QUERY PLAN
---------------------------------------------------------------------------------
 
Sort
 
(cost=31465.84..31715.84 rows=100000 width=197)
 Sort Key: a.aid
 -> 
Hash Join
 
(cost=1.02..4016.02 rows=100000 width=197)
 
Hash Cond: (a.bid = b.bid)
 -> 
Seq Scan on pgbench_accounts a
 
(cost=0.00..2640.00 rows=100000 width=97)
 -> 
Hash
 
(cost=1.01..1.01 rows=1 width=100)
 -> Seq Scan on pgbench_branches b (cost=0.00..1.01 rows=1 width=100)
(7 rows)
 
 
 
 
 

Example frompg_hint_plan’sdocumentation.

 
 

The hint mandates usage of aHashJoinfor joiningpgbench_accountsandpgbench_branches, and doing a sequential scan of thepgbench_accountstable; the actual query plan follows suit nicely.

## Formulating our problem

Given that we can influence Postgres to pick different—and potentially better—query plans usingpg_hint_planhints, the question we’re starting with is:

Can a language model learn to produce hints that result in better query plans?

### Useful research

What might make this a worthwhile problem to solve?

My first idea was to give the model the query and the exact same set of information Postgres’s planner has. This amounts to seeing if we could build a better cardinality estimator. I came to the conclusion this is not a worthwhile avenue to explore; we would be fighting decades of cardinality estimation research. Furthermore, the inference latency alone would far outweigh any learned usefulness compared to Postgres’s ultra-fast query optimizer.

The second idea—and what I believe is the correct formulation—lies in a specific database usage pattern: heavy analytic workloads. If queries are getting run thousands of times using sub-optimal default Postgres plans, efficiency gains are being left on the table. Instead, a model could be trained to find a better way to run a specific query. The training process might require execution of that query tens to hundreds of times upfront, but the amortized cost across all runs of the query would be drastically lower.

The goal isn’t to try and beat Postgres on the time/efficiency Pareto frontier for one-off queries, but we may be able to beat it on queries that run over and over again.

## A model and its harness

I decided to start with a small 4B model because it would be easiest to train/inference myself on the 2x RTX 3090 rig (affectionately named FLOPper) I have at home.

Around the time I started this project, the Qwen 3.8 family of models was released, unfortunately without a 4B variant. However, I came across a Qwen 3.8 4B distillation from a small lab in Germany calledEmperoand was intrigued. They used Qwen 3.8’s 2.4T model as a teacher model to distill learnings into Qwen 3.5 4B, producingempero-ai/Qwen3.8-4B-Distill. This distilled model is not outright better than its base 3.5 model; it performs better onMMLUtasks and slightly worse onGSM8Ktasks. In other words, this distillation performs better when evaluated on breadth of general knowledge, and slightly worse on multi-step mathematical reasoning. As to which is better for our task, I do not know; I decided to stick with the distilled model either way.

With the model locked in, I built a lightweight agent harness,qo-agent, that would orchestrate hint production. It was given the following six tools:

1. inspect_relation— Lists a table’s columns with types and nullability, index definitions and estimated rows and bytes
2. get_column_stats— Gets Postgres planner statistics for 1-8 columns of a relation
3. get_plan— Gets the default plan’s estimates or a submitted candidate’s stored plan
4. evaluate_candidate— Validates a proposed plan action and then executes it for timing/plan diagnostics
5. keep_default— Returns Postgres’s default plan itself as the candidate and ends the search
6. finish— Takes as input a submitted candidate ID or the default plan and ends the search

To take advantage of structured outputs, the agent was instructed to producePlanActionJSON objects. Calls toevaluate_candidatethen compiledPlanActionobjects into hints and prepended them to the original query.

A sample agent trajectory:

 
 
 
Agent →
 
get_plan("default")
Tool ←
 Default plan: (t ⋈ mc) ⋈ cn, hash joins, estimated rows per node
 
Agent →
 
evaluate_candidate({
 
"leading": { "left": { "left": "cn", "right": "mc" }, "right": "t" },
 
"joins": [{ "relations": ["cn", "mc"], "force": "hash" }]
 })
Tool ←
 
c1
 · valid · novel plan · 
118 ms · 0.91× default
 · 
2 attempts left
 
Agent →
 evaluate_candidate({
 
"leading": { "left": { "left": "t", "right": "mc" }, "right": "cn" },
 
"joins": [{ "relations": ["t", "mc"], "force": "nestloop" }],
 
"scans": [{ "relation": "mc", "force": "index" }]
 })
Tool ←
 c2 · valid · novel plan · 
87 ms · 1.24× default
 · 1 attempt left
 
Agent →
 evaluate_candidate({
 "leading": { "left": { "left": "t", "right": "mc" }, "right": "cn" },
 
"joins": [{ "relations": ["t", "mc"], "force": "hash" }]
 })
Tool ←
 c3 · valid · novel plan · 100 ms · 1.08× default · 
0 attempts left
 
Agent →
 
finish({ "selected_candidate_id": "c2" })
Tool ←
 Finished · selected c2
 
 
 
 
 A sample trajectory where the agent is permitted to submit up to three candidates. 
 

## Benchmarks

An agent is useless without something to benchmark its performance against. Fortunately for us, the hard work of creating these benchmarks was already done.

### The Join Order Benchmark

Leis et al. introduced the Join Order Benchmark (JOB) inHow Good Are Query Optimizers, Really?. They used it to evaluate cardinality estimation and join-order optimization using our familiar IMDb dataset.

It consists of 113 queries spread across 33 query templates. Query templates differ via their relational skeleton. They reference different tables and connect them with different join predicates. You can think about them as a structural family of questions that can be answered. Queries derived from templates preserve the tables used and the join graph topology but change selection predicates.

Looking at an example:

 
 
SELECT
 MIN
(
t
.
title
) 
AS
 movie_title

FROM
 company_name 
AS
 cn

JOIN
 movie_companies 
AS
 mc 
ON
 mc
.
company_id
 =
 cn
.
id

JOIN
 title 
AS
 t 
ON
 t
.
id
 =
 mc
.
movie_id

JOIN
 movie_keyword 
AS
 mk 
ON
 mk
.
movie_id
 =
 t
.
id

JOIN
 keyword 
AS
 k 
ON
 k
.
id
 =
 mk
.
keyword_id

WHERE
 cn
.
country_code
 =
 :country_code

 AND
 k
.
keyword
 =
 '
character-name-in-title
'
;
 
 
 

Query template 2 — “What is the alphabetically first title of a movie associated with a company from country X and tagged with the keyword character-name-in-title?”

 
 

…and here are two real queries from JOB derived from this template:

 
SELECT
 MIN
(
t
.
title
) 
AS
 movie_title

FROM
 company_name 
AS
 cn,

 keyword 
AS
 k,

 movie_companies 
AS
 mc,

 movie_keyword 
AS
 mk,

 title 
AS
 t

WHERE
 cn
.
country_code
 =
 '
[de]
'

 AND
 k
.
keyword
 =
 '
character-name-in-title
'

 AND
 cn
.
id
 =
 mc
.
company_id

 AND
 mc
.
movie_id
 =
 t
.
id

 AND
 t
.
id
 =
 mk
.
movie_id

 AND
 mk
.
keyword_id
 =
 k
.
id

 AND
 mc
.
movie_id
 =
 mk
.
movie_id
;

Query 2a — “What is the alphabetically first such movie title associated with a German company?”

 
SELECT
 MIN
(
t
.
title
) 
AS
 movie_title

FROM
 company_name 
AS
 cn,

 keyword 
AS
 k,

 movie_companies 
AS
 mc,

 movie_keyword 
AS
 mk,

 title 
AS
 t

WHERE
 cn
.
country_code
 =
 '
[us]
'

 AND
 k
.
keyword
 =
 '
character-name-in-title
'

 AND
 cn
.
id
 =
 mc
.
company_id

 AND
 mc
.
movie_id
 =
 t
.
id

 AND
 t
.
id
 =
 mk
.
movie_id

 AND
 mk
.
keyword_id
 =
 k
.
id

 AND
 mc
.
movie_id
 =
 mk
.
movie_id
;

Query 2d — “What is the alphabetically first such movie title associated with a U.S. company?”

 

### The Cardinality Estimation Benchmark

Another relevant benchmark is the Cardinality Estimation Benchmark (CEB), introduced inFlow-loss: Learning Cardinality Estimates That Matter. It uses the same IMDb database and is a much larger benchmark consisting of ~13.6k synthetically generated queries organized across 16 querytemplatesCEB’s definition of a template is looser than JOB's. Two CEB templates can share the same join graph, differing only in their selectivity predicates. In JOB, every template's join graph is unique..

### Train time, test time

Due to its size, CEB was a good fit for training the model. JOB would be used to validate the model’s performance.

You might be wondering if it makes sense to both train and test on IMDb. If it works well, hasn’t the model just learned this specific database well?

I would argue this is precisely the point. We want our model to learn IMDb well. Given our problem formulation, if this agent is continually getting used for a company’s analytic workloads across its specific databases, we need not generalize to all databases.

The real issue is making sure we’re not overfitting to JOB query templates during training over CEB. The model should learn IMDb in a way where given any query, even for structural query families it hasn’t seen before, it’s still capable of producing a good plan. In practice, this means we need to prune CEB queries that have the same shape as any of the JOB queries.

### Query topology mapping

Let’s define a query’s “topology” as its structural join-graph (de-aliased table names as nodes and joins as edges). The join graph excludes all selectivity predicates; we’re only interested in joins here.

CEB queries sharing a topology with a JOB query would be removed from the training set. I wrote a small script to convert all JOB and CEB queries to their topologies and checked if there was any overlap. There wasn’t, so no filtering was required.

 
 
 
 

JOB:113queries,33templates,33topologies

 
* JOB 1 · 4 queries · 5 
tables1
* JOB 2 · 4 queries · 5 
tables2
* JOB 3 · 3 queries · 4 
tables3
* JOB 4 · 3 queries · 5 
tables4
* JOB 5 · 3 queries · 5 
tables5
* JOB 6 · 6 queries · 5 
tables6
* JOB 7 · 3 queries · 8 
tables7
* JOB 8 · 4 queries · 7 
tables8
* JOB 9 · 4 queries · 8 
tables9
* JOB 10 · 3 queries · 7 
tables10
* JOB 11 · 4 queries · 8 
tables11
* JOB 12 · 3 queries · 8 
tables12
* JOB 13 · 4 queries · 9 
tables13
* JOB 14 · 3 queries · 8 
tables14
* JOB 15 · 4 queries · 9 
tables15
* JOB 16 · 4 queries · 8 
tables16
* JOB 17 · 6 queries · 7 
tables17
* JOB 18 · 3 queries · 7 
tables18
* JOB 19 · 4 queries · 10 
tables19
* JOB 20 · 3 queries · 10 
tables20
* JOB 21 · 3 queries · 9 
tables21
* JOB 22 · 4 queries · 11 
tables22
* JOB 23 · 3 queries · 11 
tables23
* JOB 24 · 2 queries · 12 
tables24
* JOB 25 · 3 queries · 9 
tables25
* JOB 26 · 3 queries · 12 
tables26
* JOB 27 · 3 queries · 12 
tables27
* JOB 28 · 3 queries · 14 
tables28
* JOB 29 · 3 queries · 17 
tables29
* JOB 30 · 3 queries · 12 
tables30
* JOB 31 · 3 queries · 11 
tables31
* JOB 32 · 2 queries · 6 
tables32
* JOB 33 · 3 queries · 14 
tables33
 
 

CEB:13,646queries,16templates,12topologies

 
* CEB 1a · 3,000 queries · 9 
tables1a
* CEB 2a · 888 queries · 11 
tables2a
* CEB 2b · 500 queries · 11 
tables2b
* CEB 2c · 298 queries · 9 
tables2c
* CEB 3a · 1,383 queries · 10 
tables3a
* CEB 3b · 256 queries · 10 
tables3b
* CEB 4a · 516 queries · 6 
tables4a
* CEB 5a · 1,014 queries · 10 
tables5a
* CEB 6a · 465 queries · 14 
tables6a
* CEB 7a · 167 queries · 16 
tables7a
* CEB 8a · 515 queries · 12 
tables8a
* CEB 9a · 2,247 queries · 9 
tables9a
* CEB 9b · 537 queries · 9 
tables9b
* CEB 10a · 1,019 queries · 7 
tables10a
* CEB 11a · 491 queries · 10 
tables11a
* CEB 11b · 350 queries · 12 
tables11b
 
 
 
 
 

JOB and CEB templates displayed as anidenticonof their topologies.

 
 

## How to muffle an elephant

Before getting into benchmarking the agent and doing training runs, we have to talk about how Postgres was actuallyrun, because it directly impacts the training process.

First, some facts:

* FLOPper has a CPU with 16 physical cores, 64 GB of RAM and a 2 TB NVMe SSD
* The slice of IMDb we’re using is 8.5 GB on disk
* Postgres caches pages of data retrieved during query execution into a buffer
* The operating system has its own filesystem cache doing the same thing one level down

If we run the exact same query on Postgres 20 times in a row, it won’t take the same amount of time each run. In day-to-day work, this isn’t a big deal. But the whole thesis, and the training process itself, relies on measuring whether one way of running a query is faster than the Postgres default. This means we need to do everything in our power to de-noise Postgres.

First, I needed to understand just how noisy Postgres query executions are.

I started by building a “calibration” capability into my experimentation workflow. The calibration process was simple: runNNNDocker containers built from a Postgres image, each given a fixed slice of CPU cores and RAM to use. I setN=4N = 4N=4to begin; anything lower might make future training far too slow, and anything higher might lead to more CPU contention, which means more noise. Each container was given 4 cores to use and capped at 8 GB of memory.

On startup, each container initialized Postgres with identical settings and loaded the IMDb data. Calibration then opened a thread pool of size four and pushed all 113 queries onto a shared queue. Whenever a container finished measuring a query, it pulled the next one off the queue.

The actual measurement process had two phases:

1. Run the query a few times to “warm it up”
2. Then run the query 20 more times and record each execution time

 
 
 
 
queue
 
 
job-01a
job-01c
job-01d
job-01b
job-02a
job-02c
job-02b
job-02d
 
 
+105 more
 
 
1. container 0—warmupmeasureidle
2. container 1—warmupmeasureidle
3. container 2—warmupmeasureidle
4. container 3—warmupmeasureidle
 
 
0
 / 113 queries measured

 
 
 
 Four containers pull JOB queries off a shared queue, warm each one up until its buffer counters settle, then run it 20 times. 
 

So what does it mean to warm a query up? We need to bust out some OS fundamentals to understand.

Whenever Postgres executes a query, it asks the operating system (in our case, Linux) for pages of data. Linux first checks its own filesystem cache, the page cache. If the pages are present, Linux sends them over; else it reads them from disk, stores them in its cache and then sends them over. Postgres, in turn, keeps received pages in its ownshared_bufferscache for easy reuse. Whenshared_buffersbegins to overflow, Postgres evicts pages. If it needs those pages again, it must ask Linux once more.

Every time there’s a cache hit inshared_buffersfor a page, Postgres increments a counter called “shared hit blocks” (SHBs). If it has to ask Linux, it increments “shared read blocks” (SRBs).

Postgres conveniently reports both counters if we runEXPLAINwith theBUFFERSoption. For example, runningEXPLAIN (ANALYZE, TIMING OFF, BUFFERS, FORMAT JSON)outputs something like:

{

 "
Plan
"
:
 {

 "
Node Type
"
:
 "
Aggregate
"
,

 "
Shared Hit Blocks
"
:
 1800786
,

 "
Shared Read Blocks
"
:
 52990
,

 ...

 },

 "
Execution Time
"
:
 189.2
,

 ...,

}

These counters give us some notion of the “warmness” of a query. After each warmup run, we compared its hit and read counts to the previous run’s. If both were within 2% of each other (and the plan hadn’t changed), we called the query warm and started measuring. A query needed at least two warmups to have something to compare, and was cut off at five regardless. The idea was that if the counters stopped moving, the data could be considered settled and cache churn would be minimized during the 20 measurements.

 
 
 

Query A runs

 
 
 
shared_buffers 
Postgres
 
 
 
 
 
 
page cache 
Linux
 
 
 
 
 
 
disk
 
 
 
 
 
 

Query AQuery BShared hit blocks0Shared read blocks0

 
 
 
 Query A fills 
shared_buffers
 via Linux calls. Query B requires different pages, evicting Query A pages in 
shared_buffers
 along the way. When A runs again, the evicted pages count as reads. 
 

I setshared_buffersto a conservative 128 MB and ran the first calibration:

 
 
 
 
 
 0%

 25%

 50%

 75%

 100%

 
 
 
 
 
 2 warmups 
 
50 queries
 
 
 
 
 
 48 of 50 still reading

 
 
 
 3 warmups 
 
46 queries
 
 
 
 
 
 26 of 46 still reading

 
 
 
 4 warmups 
 
4 queries
 
 
 
 
 
 2 of 4 still reading

 
 
 
 5, capped 
 
13 queries
 
 
 
 
 
 13 of 13 still reading

 
 
 
 

Still reading from Linux after warmupFully resident in shared_buffers

 
 
 
 All 113 JOB queries in the first calibration grouped by how many warmups they needed and placed by the share of their pages still read from Linux on every run afterwards. 
 

Half the queries were declared warm after only two runs. Not bad… at least until I dug deeper. The SRB counts weren’t dropping to zero; rather, they were hovering steady at some large number. With only 128 MB ofshared_buffersagainst an 8.5 GB database, Postgres wasconsistentlymissing its own cache on every execution and asking Linux for more pages. “Stable” did not mean “resident.”

Linux’s page cache is fast, so this isn’t the end of the world. Unfortunately, a new problem emerged when I actuallylookedat the 20 measurements taken for various queries. Let’s look at one query in particular,job-13b:

 
 
 

job-13b128 MB shared_buffers

 
 
 

run 1 

run 5 

run 10 

run 15 

run 20 
 
 
 14 runs · 186–204 ms 
 6 runs · 227–253 ms 
 
 
 
 180 
 200 
 220 
 240 
 260 
 
ms
 
 
 
 
In the order they ran
 
Sorted
 
 
 
 
 
job-13b
's 20 measured runs at 128 MB 
shared_buffers
. Each dot is one run. Toggle between the two buttons to see the runs first in the order they ran, and then dropped onto the x-axis, where they pile into two clumps. 
 

14 of the 20 landed between 186 and 204 ms. The other 6 landed between 227 and 253 ms, somewhere between 14% and 26% slower. The query wasn’t even uniformly noisy, it just had two different speeds at different times, and a third of the time it ran at the slower speed.

I initially wanted to quantify noise using thecoefficient of variation:

 
 
CV
=
The mean of the 20 runs, in ms.
x
ˉ
The standard deviation of the 20 runs: how far a typical run sits from the mean, in ms.
s
​
×
100%
 
 
 
 

The CV tells us the “wobble” of a measurement. If a query takes 100 ms and has a CV of 5%, we could say it wobbles by about 5 ms. Forjob-13b, the CV was 10.3%. It wasn’t great. CV is also not a great measurement to use here. Because it’s built on the mean, it’s easily influenced by a few outlier runs.

We don’t actually care as much about how spread out the 20 runs are. Wedocare abouthow oftenthis causes our measurement criteria during training runs to get fooled.

### To fool an agent

Bear with me here as I skip ahead a little bit in order to provide more color on what exactly we needed to measure.

To de-noise during actual agent runs, I couldn’t just run the agent’s proposed plan a single time. Instead, I ran three interleaved(candidate, default)pairs sequentially. Three was picked somewhat arbitrarily to provide some measure of variability while being small enough to prevent agent evaluation runs from spending most of their time in Postgres. Once the three candidate/default execution time tuples were obtained, the medians of both the three candidates and the three defaults were taken and expressed as a ratio of each other to determine the final speedup or slowdown. If the two medians differed by less than an arbitrarily declared 5%, it was a tie. Outside of that tie zone, a candidate could be declared as a speedup or a slowdown.

Now let’s go back to our earlierjob-13bexample. We had 14 executions in one clump, and 6 in another slower clump. The median of three strategy sounds good until you realize that if, in theory, at least two of the three measurements landed in that “slower” clump, the median would bias towards the less frequent slower clump.

Imagine a candidate plan that executes identically to the default. No real difference exists, so the correct reward is zero. Draw three timings for the “candidate” and three for the “default” out of the 20 we observed. There are(203)=1,140\binom{20}{3} = 1{,}140(320​)=1,140ways to draw three from 20; forjob-13b, 230 of them contain at least two slow runs, so one side’s median lands in the slow clump ~20% of the time.

That’s a totally phantom 14-26% speedup or slowdown that we would show to our model as signal ~20% of the time. Dangerous!

 
 
 

job-13b128 MB shared_buffers · a no-op candidate (i.e. one that is identical to the default)

 
 
 
20 runs
 
 
 
 
candidate
 
 
 
 
 
default
 
 
 
 
 
 180 
 200 
 220 
 240 
 260 
 
ms
 
 
 

—drawing…

 

0rounds · ties0· phantom wins0· phantom losses0· fooled0%

 
 
 
 A no-op candidate measured against itself. Every round draws three of 
job-13b
's 20 runs for the candidate and three for the default, takes each side's median, and applies the 5% tie zone. Over every possible draw, the reward is fooled ~40% of the time. 
 

So we can’tjustrely on CV as the golden number to minimize, as two queries with the exact same CV can fool the measurement reward at different rates depending on whether the spreads are a uniform blur or two clumps sitting more than 5% apart. The actual number to minimize is this fooling rate itself.

I wrote a small script to compute the fooling rate directly from raw calibration data. It worked by sliding a window of six sequential runs across the 20. For each window, we took interleaved pairs of size two to represent an interleaved(candidate, default)pair. A window of size six gives us pairings like:(t1, t2), (t3, t4), (t5, t6). In any given pair,tnt_ntn​andtn+1t_{n+1}tn+1​can alternate roles of being the candidate query, or the default query. That means for each pair, there are two possibilities, and therefore for each window of three tuples, there are2×2×2=82 \times 2 \times 2 = 82×2×2=8possibilities. 20 measurements means we’ll slide this window 15 times, so we have15×8=12015 \times 8 = 12015×8=120totalpossibilitiesEach possibility is a binary value indicating whether or not that specific, simulated formulation of candidate/default pairs resulted in a ratio of medians between the two greater than the 5% tie-zone.for a given query.

We derive two metrics from these raw numbers. First, we calculate the no-op error rate for a given query as the ratio of the 120 simulated possibilities that do differ by more than 5% against the number that don’t. We sum these percentages up across all 113 JOB queries and then divide by 113. This number, which we’ll call the “mean no-op error rate,” gives us the percentage likelihood that the reward may get fooled for any JOB query when doing our three paired measurements strategy. Second, we sort the no-op error rates for all 113 queries, lowest to highest. The number that is 90% of the way to the end of this sorted list is reported as the “p90 query,” and gives us a measure of the fooling rate for the worst-offending queries.

At 128 MB forshared_buffersand four concurrent containers, the “fool rate” script produced the following mean no-op error rates and p90 querynumbersI ran the calibration twice per config to provide a sense of how much two runs may disagree with each other.:

 

Run
Mean no-op error rate
p90 query
Median CV
1
5.0%
13%
2.3%
2
5.4%
20%
2.4%
 
 
 
 

The numbers aren’t good. One in twenty no-op plans get rewarded, and one in ~10 queries gets fooled more than 13% of the time.

We can do better.

### Tuning Postgres

I focused on two memory-related settings Postgres exposes:

1. shared_buffersdecides how much of the database Postgres can keep in its own cache
2. work_memdecides how much memory a single sort/hash operation can get before spilling to disk

I ran four calibrations:

 

shared_buffers
work_mem
No-op error rate (run 1 / 2)
p90 query
Median CV
Total runtime
128 MB
4 MB
5.0% / 5.4%
13% / 20%
2.3%
95 s
2 GB
4 MB
1.8% / 1.2%
1.3% / 0%
1.1%
60 s
128 MB
32 MB
7.0% / 6.6%
20% / 23%
2.6%
94 s
2 GB
32 MB
1.7% / 1.3%
0% / 0%
1.2%
60 s
 
 
 
 

Surprisingly,work_memhad no effect on noise at all, andshared_bufferscarried all of the weight!

With 2 GB ofshared_buffers, the median query ended warmup with its SRB counter at exactly zero: its working set was fully resident in Postgres’s own cache. The no-op error rate dropped by roughly 4x, and the 90th percentile query went from being fooled 13%–20% of the time to almost never. Our two-clump query,job-13b, went from a CV of 10.3% to 0.9%, with all 20 runs landing within 7 ms of each other.

One neat benefit emerged that I wasn’t initially chasing: the default plans themselves got faster. The summed runtime of all 113 JOB queries fell from 95 seconds to 60 seconds, just from cache residency. In other words, actuallytakingour measurements for both candidates and defaults would now be significantly faster, meaning the training process would take less time.

I locked in 2 GBshared_buffersand 4 MBwork_memfor the rest of the project.

## Baselines and metrics

I used two metrics for benchmarking agent performance.

### Geometric mean speedup

 
 
The geometric mean speedup
S
g
eo
​
=
(
i
=
1
∏
N
​
The candidate plan's execution time for some query i
c
i
​
The default plan's execution time for some query i
b
i
​
​
)
The Nth root of the product. With this, a 2x and a 0.5x speedup cancel out to 1x.
1/
N
 
 
 
 

The geometric mean speedup gives all queries equal weight. For example, in a two-query sample, if query 1 runs 2x faster than its baseline, and query 2 runs 0.5x faster than its baseline, thenSgeo=1.00xS_{geo} = 1.00\text{x}Sgeo​=1.00x. It doesn’t matter if query 1’s baseline took 5 minutes and our candidate took 2.5 minutes, but query 2 only regressed from 25s to 50s, as they are equally weighted.

### Total workload speedup

 
 
The total workload speedup
S
w
or
k
l
o
a
d
​
=
∑
i
=
1
N
​
The candidate plan's execution time for some query i
c
i
​
∑
i
=
1
N
​
The default plan's execution time for some query i
b
i
​
​
 
 
 
 

Total workload speedup treats the entire query set as one batch. We simply add all the baseline times and divide by the sum of the candidate times. In our above example,Sworkload=1.4xS_{workload} = 1.4\text{x}Sworkload​=1.4x.

Both metrics tell different stories. The total workload speedup is a measure of practicality. A data analyst building out a suite of analytics queries wants to decrease the overall runtime across the batch. But from a model training standpoint, the total workload speedup could be entirely influenced by a single query plan the agent chanced upon; the rest of the batch could be degenerate. This implies the model hasn’t actually learned anything interesting; it just got lucky. Because the geometric mean speedup cares not for absolutes, it gives us a measure of actual learning across the batch: values above 1x imply that the average query is executing faster.

### A frontier intelligence control

Before running the untrained 4B model through theqo-agentharness, I wanted to validate this problem was actually solveable by today’s frontier models. If a model likeGPT-6 AstraorQwen 3.8 2.4Tcouldn’timprove upon the default Postgres query plan, I couldn’t really expect the 4B model to either.

I took a small sample of 10 JOB queries and benchmarked them on both Astra and Qwen 3.8 2.4T running through theqo-agentharness:

 
 

Model
Candidates
Tasks scored
 
S
geo
​
 
 
 
S
workload
​
 
 
Regressions
 Astra [m] 
 
1
9/10
0.85x
1.00x
3
 Astra [m] 
 
5
10/10
2.54x
2.12x
0
 Astra [m, r] 
 
5
10/10
2.39x
1.57x
1
 Qwen 3.8 2.4T [m] 
 
1
7/10
2.02x
1.30x
1
 Qwen 3.8 2.4T [m] 
 
5
10/10
2.26x
1.35x
1
 
 
 

Evaluations of Astra and Qwen 3.8 2.4T run on the same slice of 10 JOB queries. The frontier models were benchmarked at different candidate numbers (i.e. how many candidates they were allowed to generate during a complete trajectory; either a single candidate or 5) and for Astra, whether reasoningsummariesI was a little surprised to see Astra performance worsen with reasoning summaries on compared to the 5-candidate evaluation done right before it, but these evaluations were only run a single time on a small 10-query slice of JOB, so I chalked up the worse results to random variance.were enabled or not. Astra was inferenced through OpenAI’s API, and Qwen 3.8 2.4T throughModalviaOpenRouter.

 
 

Given the difference between the single-candidate scores and the 5-candidate scores, the agent was clearly capable of doing in-context learning across sequential executions of its candidates. This gave me the confidence to stick with an agentic multi-turn approach rather than try and train the 4B model to get really good at one-shotting a plan.

During a run of the agent, each candidate was warmed once and then measured once. After exhausting the candidate attempts budget, the model was only presented with a single tool to call,finish, and the model was told to select the best scoring candidate (or keep the default plan). After the candidate was selected, three interleaved(candidate, default)pairs were run and passed through a clipper:

S
i
=
clip
⁡
(
median
⁡
(
D
i
)
median
⁡
(
C
i
)
,
 
0.1
,
 
10
)
S_i = \operatorname{clip}\left( \frac{\operatorname{median}(D_i)}{\operatorname{median}(C_i)},\ 0.1,\ 10 \right)
S
i
​
=
clip
(
median
(
C
i
​
)
median
(
D
i
​
)
​
,
 
0.1
,
 
10
)

The clipper constrained the result of the division between the two medians to be between[0.1,10][0.1, 10][0.1,10]. These clipper values were picked somewhat arbitrarily; I found they prevented the geometric mean speedup from getting overly influenced by an extreme speedup or an extreme regression.

Conclusion: frontier intelligence is capable of agentically doing query optimization.

### The vanilla 4B baseline

We’re now ready to evaluate the untrained 4B model on JOB and see how it does!

The same 5-candidate plan budget per agent trajectory configuration was employed. The results were dismal:

 

How the trajectory ended
Queries
No valid candidate
81
Selection failed
16
Timed out
1
Candidate duplicated the default plan
7
Kept the default
2
Candidate measured against the default
6
 
 
 
 

Only the last three rows contribute to the score, leaving 15 valid trajectories out of 113. Nine of those 15 result in a score of 1.00x by construction (the plan wasidenticalA candidate plan was determined to be equal to the default plan if theirEXPLAINoutputs with cost and row estimates stripped were equivalent.to the default, or the model chose to keep the default). That left justsixcandidate plans that were:

1. Structurally intact (thePlanActionthe model produced was successfully compiled into a hint comment)
2. Valid (the resulting hint was actually valid given the schema)
3. Novel (the resulting plan was distinct from Postgres’s)

Five of the six plans resulted in speedups of 1.02x–1.30x, and one of them landed at 0.05x.

The most common issues seen were:

* ThePlanActionwas not a valid object
* Join trees did not contain every relation exactly once
* Actions were wrapped in an extraneousactionkey
* LeadingLeadingtrees ended up being quite an important concept, as these are used to influence the join-ordering, which as we mentioned previously, is an NP-hard problem.trees had subtrees that were not actually connected in the query’s join graph
* The model called specific tools at the wrong time, or called tools that didn’t exist

Not only was the model terrible at this task, it couldn’t even grok the harness wrapped around it either.

## Off-policy distillation via supervised fine-tuning

I first needed to get the 4B model to speak the “language” of theqo-agentharness. I would make it good at query optimization after.

We can usesupervised fine-tuning(SFT) to do this. Specifically, we can do off-policy distillation.

Off-policy distillation is a training method by which a student model (sometimes referred to as a policy) learns to imitate outputs produced by a teacher model. It’s called “off-policy” because the training data is not generated by the student model/policy itself. It’s remarkably simple. A complete teacher trajectory (sometimes referred to as a demonstration) is shown to the student model. For every token in the trajectory, the probability the student model gave to generating that token results in a per-token loss. Averaging these per-token losses leads to a demonstration-level loss. Standardbackpropagationvia chain rule then lets you compute gradients for all trainable parameters in the student model, and the configured optimizer can nudge parameter values in a way where loss gets minimized in a single pass.

What’s super neat about off-policy distillation is that we don’t need a lot of data for it to work well. Because each demonstration provides us thousands to tens of thousands of token predictions, our student model’s weights adapt quickly.

How do we actually get these demonstrations though? We could write them all by hand, but that would take far too long. One step up would be writing a tool to randomly generate valid-lookingtrajectoriesFun fact: I tried this initially. It actually works decently and was able to teach the 4B model the harness. However, it caused a bunch of other issues, mostly around making the model less likely to generate novel candidate plans.. But these ignore that we have the best teacher of all already available: smarter, larger models.

The strategy is simple: generate a bunch of trajectories by running a smart model through theqo-agentharness, and distill those trajectories into our student 4B model.

### Rendering, loss masking, and unrolling

There are a few complexities to unpack.

Imagine we decide to use GPT-6 Astra as our teacher model. It produces trajectories in OpenAI’sResponses APIformat. Our Qwen model doesn’t understand this format; we need to transpile the human-friendly Responses API JSON format into a model-friendly token format. This is where the concept ofrenderingcomes in. Rendering libraries can take in a trajectory’s text and convert it to a raw sequence of tokens a specific model actually understands.

Another consideration with agent trajectories is determining which tokens our modelshouldactually be predicting. The model never produces certain tokens in a trajectory, like the system prompt, any user prompts or the results of a tool call after a harness executes it. The model should stillseethese tokens when predicting the next token though; they’re still part of the context, but we should only compute losses for tokens the model is responsible for predicting. We can employ a strategy called loss-masking here. A loss-masking library lets us label the parts of a teacher trajectory that are context-only, versus the parts our student model is responsible for predicting.

Finally, when fine-tuning over agent trajectories, we generally don’t include the entire trajectory as a single trainable unit. Instead, the trajectory is broken up into a set of(context, reply)pairs. Thecontextin these pairs is additive and includes previous model replies.

 
 
 
 
trajectory
 
 
 
 
system prompt
 
 
 
query + observation
 
 
 
reply 1
 
 
 
tool result
 
 
 
reply 2
 
 
 
tool result
 
 
 
reply 3
 
 
 
 

unrolls into

 
 
example 1
 
 
 
 
context
 
 
 
context
 
 
 
reply 1
 
 
 
 
example 2
 
 
 
 
context
 
 
 
context
 
 
 
context
 
 
 
context
 
 
 
reply 2
 
 
 
 
example 3
 
 
 
 
context
 
 
 
context
 
 
 
context
 
 
 
context
 
 
 
context
 
 
 
context
 
 
 
reply 3
 
 
 
 

Tokens the model is scored onContext only, no loss

 
 
 
 One trajectory with three assistant replies becomes three training examples. Each example includes as context everything preceding an assistant reply, including the model's earlier responses. 
 

### Low-rank adaptation (LoRA)

Our 4B model has 4.66 billion tunable parameters. If we wanted to update all of these parameters in a single pass during SFT, we would need a GPU with at least 64 GB of VRAM. I wanted to test my hypotheses first on my consumer-grade RTX 3090s, each of which carries 24 GB of VRAM, so I needed something more parameter-efficient here.

Low-rank adapters, or LoRAs, are the canonical way to do this. At a high-level, they work by freezing the model’s weights as they are, instead letting you train a much smaller pair of matrices that when multiplied together, result in an adjustment to selected weights in your original model.

4.66 billion weights come in at 9.32 GB inbf16. The tiny LoRA I actually ended up training was only 42.5 MB and contained only 21.2 million trainable parameters.

### Teacher model selection

We previously learned that frontier models could operate well inqo-agent; the next decision was picking between GPT-6 Astra or Qwen 3.8 2.4T.

Let’s look back at the results from evaluating both models on 10 JOB queries, this time zooming into context length in tokens:

 

Per trajectory, 5 candidates
Astra (summaries)
Qwen 3.8 2.4T
Model turns, mean
7.6
12.2
Final context, mean tokens
22,009
45,144
Final context, max tokens
28,663
73,608
Output tokens per turn, mean
161
1,795
Reasoning tokens per turn, mean
65
1,417
Wall clock for all 10 queries
3m 13s
15m 51s
 
 
 

The same five-candidate evaluations over the 10 JOB queries mentioned earlier, this time measured by how much context each trajectory consumed.

 
 

Itseemslike Astra wins on all fronts. However, Astra’s biggest drawback is that when run through the API,reasoning tokens aren’t supplied. Instead, the API gives you a short summary in place of reasoning tokens. On the other hand, Qwen 3.8 2.4T is an open-weights model and is happy to provide all of its reasoning tokens.

I was wary about training off of trajectories containing only reasoning summaries. TheHow to Steal Reasoning Without Reasoning Tracespaper talked about this exact thing: training off reasoning summaries resulted in the student model’s performance decreasing. To combat this, the authors devised a new method: trace inversion. Trace inversion calls for synthetically expanding a reasoning summary into what the raw reasoning tokensmayhave looked like. Although they’re not exactly the ones Astra actually produced during inference, the longer reasoning blocks led to improved performance when transferred over to a smaller model. This provided some level of comfort; if I picked Astra and performance suffered, I could experiment with trace inversion.

The other consideration was context lengths. Given I was only doing SFT off a single RTX 3090 to start, I needed any given trajectory to not exceed ~50k tokens in sequence length. If it did, the training process mightOOMgiven the 3090’s limited 24 GB of VRAM. All Astra trajectories fit under that budget, but some of the Qwen 3.8 2.4T ones didn’t.

I decided to try out SFT on the Astra traces. If performance suffered, I could explore trace inversion; if that didn’t work, I could rent beefier GPUs for training, bump our global context limit, and use Qwen 3.8 2.4T traces instead.

I began by generating 120 Astra trajectories over a random slice of queries from CEB, with reasoning summaries enabled. 100 trajectories would be used for training, and 20 would be used as a held-out validation set. All trajectories were rendered via Prime Intellect’srendererslibrary into Qwen format, loss-masked appropriately and unrolled and packed into usable training demonstrations. I then used Prime Intellect’sprime-rllibrary to run SFT, training the smaller ~21 million parameter LoRA. 100 Astra trajectories became 382 training rows after unrolling and packing. I allowed training to run for just a single epoch, meaning every example was trained on exactly once, and used a batch size of one (each demonstration updated the weights). Finally, I evaluated the resulting LoRA over JOB:

 
 

Checkpoint
 Valid candidate 
 
Tasks scored
 
S
geo
​
 
 
 
S
workload
​
 
 
Wins
Regressions
Vanilla 4B
14/113
15/113
0.85x
0.85x
3
1
1 epoch
48/113
44/113
0.72x
0.76x
5
16
 
 
 

The one-epoch adapter against the untrained model on all 113 JOB queries. A query counts as scored when its trajectory ended with a measured candidate, a duplicate of the default plan, or the default itself. Wins and regressions are scored queries more than 5% faster or slower than the default.

 
 

Promising! The adapter learned the harness.

I could now either generate more fresh trajectories, or do more epochs over the dataset we already had. Given the latter is cheaper, I decided on more epochs.

It was around this point that I got impatient and wanted the training process to run even faster, so I rented a 2x H100 node onLambda.

Now training on anH100Switching to the H100 meant we had 80 GB VRAM at our disposal instead of 24 GB. We could have bumped the context token limit greatly, but I decided to barrel through with the roughly ~50k token limit we set.instead of a single RTX 3090, I did two more trainingrunsTraining runs were a lot faster on the H100. The first epoch took four hours on the RTX 3090; the second took only 45 minutes on the H100.over the existing LoRA; a second epoch and then a third:

 
 

Checkpoint
 Valid candidate 
 
Tasks scored
 
S
geo
​
 
 
 
S
workload
​
 
 
Wins
Regressions
1 epoch
48/113
44/113
0.72x
0.76x
5
16
2 epochs
85/113
108/113
1.08x
1.04x
12
8
3 epochs
57/113
99/113
0.82x
0.89x
9
15
 
 
 

Two and three epochs over the same 100 Astra trajectories, evaluated on JOB. Before epochs two and three, theqo-agentharness was upgraded to allow the model to keep the default plan after a search, which is why many more queries are scored. The two- and three-epoch rows were evaluated under identical settings.

 
 

Two epochs improved our results, but three epochs regressed them! This was especially interesting because validation loss didn’t budge at all during the second epoch:

 
 
 

Validation loss on the 20 held-out trajectories

 
 
 
 0.30 
 0.35 
 0.40 
 0.45 
 0.50 
 
 
 
 
 
 
 
 
0.485
 
 
 
0.305
 
 
 
0.306
 
 
 
0.322
 
 
 
 
 
 0 
 382 
 764 
 1,146 
 
 
 
 
 
epoch 1
 
 
 
epoch 2
 
 
 
epoch 3
 
 
 

Optimizer updates, one per packed training row

 
 
 
 Loss on the 20 held-out Astra trajectories, measured at the start and end of each epoch over the first 100-trajectory dataset. 
 

A very good lesson that a flat validation loss doesn’t necessarily mean the model has stopped learning useful behavior.

I still felt we had more to learn from SFT though before proceeding with RL. I did zero filtering on the training trajectory dataset, and hadn’t carefully audited if I was missing any capabilities. It turns out I was, mostly around the model’s ability to construct validLeadingtrees.

I generated another 320 Astra trajectories; 300 for training, and 20 for validation. I filtered out just six training trajectories where Astra opted to keep the default plan without even trying a single candidate. I did two more epochs in two separate runs:

 
 

Checkpoint
 Valid candidate 
 
Tasks scored
 
S
geo
​
 
 
 
S
workload
​
 
 
Wins
Regressions
2 epochs on the first 100
85/113
108/113
1.08x
1.04x
12
8
+ 1 epoch on the new 300
77/113
101/113
1.10x
1.05x
29
13
+ 2 epochs on the new 300
71/113
107/113
1.16x
1.06x
20
5
 
 
 

Continuing the two-epoch adapter on the 300 new trajectories, evaluated on JOB.

 
 

Our 4B model not only learned the harness; it was nowgenuinelymaking good calls on various JOB queries! Fortunately, training on reasoning summaries didn’t harm performance.

## Making the 4B model good at query optimization

The model now spoke the “language” of theqo-agentharness, and we got some free performance gains out of SFT too. It was time to make it very good at query optimization.

### Agentic reinforcement learning

Agentic RL differs from SFT in that we actuallyrunthe current policy over training queries inside the agent harnessNNNtimes. Each run (also referred to as a rollout) results in a final output that’s scored against some verifiable criteria. Lastly, each rollout’s score is then weighted relative to the other same-query rollouts. A positive “advantage” is reinforced by making the model’s weightsmorelikely to produce that trajectory in future runs, and a negative advantage is penalized; the weights are updated to belesslikely to produce that trajectory in future runs.

### Designing per-rollout rewards and relative advantages

The initial reward algorithm was simple:

 
 
The reward for rollout i
r
i
​
=
{
The speedup is calculated as the default plan's median execution time over the selected candidate plan's median execution time. We take the natural log of it to balance wins and losses
ln
(
s
i
​
)
−
0.1
The number of invalid candidate plans in the trajectory
n
invalid
​
−
0.05
The number of candidates in the trajectory that fingerprinted to either Postgres's default plan, or a previously submitted candidate's plan
n
dup
​
A flat -3 applied whenever the trajectory ended without a single valid candidate
−
3
​
valid candidate
no valid candidate
​
 
 
 
 

The speedup was calculated as the median of three default plan measurements divided by the median of three candidate plan measurements.

For every evaluated candidate that was invalid, we subtracted 0.1 from the natural log of the speedup ratio. We subtracted a further 0.05 if the rollout resulted in a plan that shared the same fingerprint as the default Postgres plan. Finally, if the trajectory ended with no valid candidate at all, a flat 3 was subtracted from the reward in lieu of any of the 0.1 or 0.05 subtractions.

The first few RL runs I did using this reward resulted in a model that was terrified of producing invalid plans due to the extremely harsh -3 condition. The model played it safe instead, returning Postgres’s default plan over and over again, accepting the smaller 0.05 reward hits.

GRPO exacerbated this issue. The plain GRPO algorithm converts multiple rollout rewards into relative “advantages”:

 
 
The advantage: a positive value makes the sampled tokens more likely; negative less likely
A
i
​
=
Rollout i's reward
r
i
​
−
G is the number of rollouts executed per query: four in these earlier runs. We take the mean reward across all G rollouts
G
1
​
j
=
1
∑
G
​
r
j
​
 
 
 

GRPO asprime-rlimplements it: simply
subtract the group’s mean reward from each rollout’s reward. TheGRPO paperalso
divides by the group’s standard deviation.

 
 

Let’s say we perform four rollouts for a given query resulting in the following plans, execution speeds and rewards:

 
 
 
 
Hint
 
What happened
 
Reward
 
Advantage
 
 
 
/*+ Leading((t cn) mc) */
 
 
not run
 
t and cn never join directly, so the tree is rejected
 
 
 −3.00 
 
 
 
 
 
−1.43
 
 
 
/*+ MergeJoin(t cn) */
 
 
not run
 
a join method for two relations the query never joins
 
 
 −3.00 
 
 
 
 
 
−1.43
 
 
 
/*+ NestLoop(t mc) */
 
 
148 ms vs 118 ms · 0.80x
 
a new plan, slower than Postgres’s own
 
 
 −0.23 
 
 
 
 
 
+1.34
 
 
 
/*+ HashJoin(mc cn) */
 
 
118 ms · 1.00x
 
Postgres already chose this; same fingerprint as the default
 
 
 −0.05 
 
 
 
 
 
+1.52
 
reinforced most
 
 
 
 
 
 Four rollouts of one query under the first reward and 
prime-rl
 GRPO. Nothing in the group beat Postgres, but two rollouts still receive positive advantage because they beat the group's mean. 
 

We’re reinforcing bad behavior by telling the model it’s okay to produce plans that end up being equivalent to Postgres’s default plan!

Both the busted reward algorithm and GRPO needed to be swapped out for something that could actually score advantages relative to the default plan’s execution time.

The reward was updated as follows:

 
 
The quality of rollout i. Not to be confused with the previous reward algorithm's reward for a rollout i. This quality value is a component of the final advantage, calculated as part of the modified GRPO step
q
i
​
=
⎩
⎨
⎧
​
Anything within 5% of the default execution time counts as zero, and real gains/losses are shrunk by 0.05
soft
0.05
​
(
ln
The speedup is clipped to [0.1x, 10x] before the log, so one extreme plan cannot dominate a group
clip
(
s
i
​
,
0.1
,
10
)
)
soft
0.05
​
(
ln
clip
(
If a candidate plan times out, rollout i is scored as if it took exactly the duration of the timeout amount. Because this is generous, we tack on an additional 0.1 fee
s
^
i
​
,
0.1
,
10
)
)
−
0.1
If the rollout kept or finished with the default, the quality is exactly zero
0
Trajectories ending without valid candidates have no quality value
none
​
measured
timed out
default
no valid candidate
​
 
 
 
 

Changes include clipping the speedup ratio to bound scalar reward values, soft-thresholding by 0.05 to account for measurement noise, and scoring zero if the agent calledkeep_defaultorfinish(default). Trajectories ending without a valid candidate incurred a flat 0.1 fee instead of the previous 3.0, and candidate plans that fingerprinted to the default plan accrued small 0.02 fees.

prime-rl-flavored GRPO was swapped out for a custom “anchored” variant:

 
 
The baseline score for rollout i (i.e. the number its quality is measured against). It's the max of zero and the rollout's siblings' mean quality, which ensures the rollout doesn't get credited for simply being the least bad
b
i
​
The advantage: a positive value makes the sampled tokens more likely; negative less likely
A
i
​
​
=
max
​
0
,
The mean quality of all rollouts in the group, excluding rollout i's quality itself, and any rollouts that did not get a quality score.
∣
V
−
i
​
∣
1
​
j
∈
V
−
i
​
∑
​
q
j
​
​
=
{
q
i
​
−
b
i
​
−
A small fee charged when rollout i selected a candidate that duplicated Postgres's own without explicitly calling keep_default
0.02
[
dup
]
A fixed penalty for ending without a valid candidate
−
0.1
​
valid
invalid
​
​
 
 
 
 

Let’s take a look how our modified GRPO performs under the same four rollouts demonstrated above:

 
 
 
 
Hint
 
What happened
 
Quality
 
Reference
 
Advantage
 
 
 
/*+ Leading((t cn) mc) */
 
 
not run
 
t and cn never join directly, so the tree is rejected
 
 
 none 
 
 — 
 
 
 
 
 
−0.10
 
 
 
/*+ MergeJoin(t cn) */
 
 
not run
 
a join method for two relations the query never joins
 
 
 none 
 
 — 
 
 
 
 
 
−0.10
 
 
 
/*+ NestLoop(t mc) */
 
 
148 ms vs 118 ms · 0.80x
 
a new plan, slower than Postgres’s own
 
 
 −0.18 
 
 +0.00 
 
 
 
 
 
−0.18
 
 
 
/*+ HashJoin(mc cn) */
 
 
118 ms · 1.00x
 
Postgres already chose this; same fingerprint as the default
 
 
 +0.00 
 
 +0.00 
 
 
 
 
 
−0.02
 
 
 
 
 
 The same four rollouts under the reworked reward and anchored GRPO. Nothing is reinforced because none of the plans were good. 
 

The modified GRPO successfully applies a negative advantage to all four of these poor rollouts, down-weighting their likelihood across the board.

### Training commences

With the reward and relative advantage model locked in, I could begin training…

…as soon as I built out a mechanism for Postgres measurements to happen on FLOPper and training/inference to happen on the 2x H100 node. I would have loved to keep Postgres measurements on the Lambda node; alas, I ran a bunch of Postgres calibrations on their boxes and am reasonably confident I was sharing the non-GPU bits of the box with other folks, as the noise was off the charts compared to FLOPper.

I connected FLOPper to the Lambda node via Tailscale; the resulting process would be:

1. Query rollouts would begin on FLOPper and hold an available Postgres container for their full lifetime
2. The rollout would do inference via vLLM running on the first H100 to generate a trajectory
3. All measurements were run on the held Postgres container
4. Finally, rollout results were sent to the second H100 to compute relative advantages and update weights

Nowtraining could start. I began by merging the final SFT adapter into the base model, creating a new base model in the process, and initialized a new adapter for RL training.

I started with an extremely conservative learning rate of1e-06, a batch size of 8, four rollouts per query, and did just 120 optimizer updates to prove out the mechanism.

The trained LoRA was evaluated against JOB, and completely flopped:

 
 

Checkpoint
 Valid candidate 
 
Tasks scored
 
S
geo
​
 
 
 
S
workload
​
 
 
Wins
Regressions
SFT, starting point
71/113
107/113
1.16x
1.06x
20
5
RL, 120 updates
71/113
106/113
1.14x
0.99x
21
7
 
 
 

The first RL checkpoint against the SFT checkpoint it started from, evaluated on all 113 JOB queries.

 
 

Either the reward design wasn’t good, modified GRPO wasn’t working, or we simply weren’t being aggressive enough.

The latter was easiest to test. I increased the learning rate one order-of-magnitude from1e-06to1e-05, bumped the batch size to 16 and the number of rollouts per query from four to eight, and decided to do 600 optimizer updates instead of just 120.

Around this time, I learned that for a rollout, 92% of the rollout’s time was spent in vLLM inference! Given the increase in the number of optimizer updates, I needed to be smarter about this.

I refactored the training process so that rollouts leased an available Postgres workeronlyfor the times where measurements were needed. Because of this new async approach, I could saturate vLLM and the trainer much further, and was able to run 20 rollouts concurrently, each contending for the same four Postgres workers.

 
 
 
 
4 Postgres workers on FLOPper, 240 seconds of wall time
 
t = 
0
 s
 
 
 

Hold a worker for the whole rollout · 4 in flight

 
 
rollouts
 
workers
 
 
 
 
 
 
 
 
 
 
 
 

rollouts finished0workers measuring0%of the time

 
 

Lease a worker only to measure · 20 in flight

 
 
rollouts
 
workers
 
 
 
 
 
 
 
 
 
 
 
 

rollouts finished0workers measuring0%of the time

 
 
 
 0 s

 60 s

 120 s

 180 s

 240 s

 
 
 

vLLM inference on the H100Measuring on a workerWaiting for a workerWorker held but idle

 
replay
 
 
 
 
 

Requiring rollouts to hold a worker for their lifetime caps the maximum number of concurrent rollouts at the number
of available workers. Using a worker lease strategy only when Postgres is needed lets us run 20 concurrent rollouts
and increases the share of time Postgres workers are actually being utilized.

 
 

I ran two stacked 600-optimizer update RL runs, back-to-back. The share of rollouts earning positive advantages steadily increased:

 
 
 

Share of credited rollouts

 
 
 
 0% 
 20% 
 40% 
 60% 
 
 
 
 
second run
 
 
 
 
 
 
 
 
 0 
 200 
 400 
 600 
 800 
 1,000 
 1,200 
 
 

Optimizer updates

 

Measured plan faster than PostgresPositive advantage

 
 
 
 

The training signal across both 600-update runs from the anchored credit assigned to every rollout that reached the
trainer. Both the share of rollouts with plans beating Postgres and the share of rollouts with positive advantages
steadily climb throughout the run.

 
 

And the results from both checkpoints against JOB:

 
 

Checkpoint
 Valid candidate 
 
Tasks scored
 
S
geo
​
 
 
 
S
workload
​
 
 
Wins
Regressions
SFT, starting point
71/113
107/113
1.16x
1.06x
20
5
RL, 600 updates
99/113
113/113
1.35x
1.16x
34
0
RL, 1,200 updates
101/113
112/113
1.41x
1.29x
38
2
 
 
 

Both 600-update checkpoints against the SFT checkpoint they descend from, evaluated on all 113 JOB queries.

 
 

The valid candidate rate rose nicely, alongside both the geometric mean speedup and total workload speedup!

I ran the final RL checkpoint against JOB again, this time doingthreerollouts per query instead of just one. In other words, each query could produce up to 15 candidates max, and the best-of-15 was picked for eachqueryThis is roughly how I would expect someone trying to tune a workload of queries to use a model specially trained on this task. They would care more about the best candidate possible sampled from many rollouts, rather than just a single rollout.:

 
 

Selection
Tasks scored
 
S
geo
​
 
 
 
S
workload
​
 
 
Wins
Regressions
Model’s own choice, per trajectory
339/339
1.40x
1.24x
119
7
Best feedback within each trajectory
339/339
1.44x
1.29x
129
1
Best feedback across all three
113/113
1.81x
1.81x
68
0
 
 
 

The final 1,200-update RL checkpoint with three trajectories per JOB query. The first row averages the model’s own final selections over all 339 trajectories. The second applies a fixed rule within each trajectory, choosing the candidate with the best preliminary feedback if it beat 1.05x and the default otherwise. The third applies the same rule across a query’s three trajectories, so each query gets one answer chosen from up to 15 candidates.

 
 

When taking the best feedback across three rollouts, we saw a 1.81x geometric mean speedup, and coincidentally a 1.81x total workload speedup too.

### What the model learned

After all this training, what did the model actually learn?

 
 
 
 
 
How searches went
 
 
 
 The investigator 
 
295 of 337 searches that submitted candidates first inspected a relation, column statistics, or the default plan
 
 
 The big spender 
 
235 of 339 searches used all five candidate attempts
 
 
 The reasoner 
 
On 
job-01d
 (90x speedup), its reasoning read: "...the mi-index sequential scan, which is running a lossy filter at 575k with an 11ms timing. It looks like using a bitmap could be much faster." The model then actually forced a bitmap scan
 
 
 
 
The model's preferred strategies
 
 
 
 Consistent favorites 
 
Of 1,347 actions, the model outputted scan hints 1,141 times, 
Leading
 trees 917 times and 
Parallel
 hints 572 times. Surprisingly, 
Rows
 corrections were used only 146 times
 
 
 Strong preferences 
 
Nested loops were forced over hash joins regularly, and index scans were preferred over bitmap or sequential scans
 
 
 Favorite settings 
 
The model regularly used 
enable_sort=off
 and 
random_page_cost=1.1
 
 
 
 
What actually wins
 
 
 
 Three motifs win 
 
The model's usage of 
Leading
 to rewrite the join order, making a single scan fix without changing the join order, and using 
Parallel
 resulted in much of the gains
 
 
 
 
 
 An analysis of the traces from the final evaluation's 339 searches. 
 

## Costs

This project would have beenfreeBarring the price of electricity for continually running FLOPper when both GPUs were fully utilized, which at current rates costs about ~$9/day.had it not been for my impatience to get training resultsfaster“What about the Astra traces?,” you might ask. I did not experiment with it, but I do think the 4B model could have eventually learned the harness language through just RL alone, asDeepSeek-R1-Zeroshowed. It might have just takena lotmore rollouts.. I paid ~$800 to rent a 2x H100 SXM node from Lambda for ~95 hours, and ~$400 in OpenAI API fees to generate the Astra trajectory demonstrations.

Total cost: $1,200.

## Conclusion

Via off-policy distillation and reinforcement learning, a tiny 4B model went from not being able to understand the harness it was wrapped in, to achieving a 1.81x geometric mean speedup and a summed latency decrease of 44.7% across a workload of join-heavy SQLqueriesGiven three attempts per query in a best-of-15 measurement, as previously mentioned..

It’s easy to take tiny models for granted when 5T+ parameter behemoths exist. We shouldn’t.

Frontier intelligence isextremelypowerful; the distillation I did off Astra trajectories is proof enough that large models are not going anywhere.

But I do believe this experiment proves out a hypothesis many companies are waking up to: they have the data; it’s not a far-cry to build out an RL environment and spend a small sum to train and inference open-weights models on niche, domain-specific tasks. I think small models will be increasingly used for this, as they are faster and cheaper to train.

I architected the infra/training stack myself plus used my own GPUs as a learning exercise, but there are agrowingnumberofout-of-the-boxsolutionsfor companies to easily train their own models.

I’m personally very excited to see how this space continues to grow!

## Next steps

As for what I’d want to try next, just a few ideas:

* Explore whether structured hint sweeping in the style ofBao: Learning to Steer Query Optimizersis more effective than using a 4B model
* Attempton-policy distillationand compare performance against off-policy distillation
* Try trace inversion and see how it influences off-policy distillation
* Measure “fooled reward” noise on dedicated EC2 boxes to understand how this experiment could be scaled up

## Code

All code for this project is availablehere.

## Citation

Please cite this work as:

 
Bansal, Rohan. “Training a 4B model to produce 81% faster query plans than Postgres”. rohanbansal.com (Sep 2026). https://rohanbansal.com/qorl
 

Or use the BibTeX citation:

 
@article{bansal2026qorl,
 title = {Training a 4B model to produce 81% faster query plans than Postgres},
 author = {Bansal, Rohan},
 journal = {rohanbansal.com},
 year = {2026},
 month = {September},
 url = "https://rohanbansal.com/qorl"
}

## References

1. Viktor Leis, Andrey Gubichev, Atanas Mirchev, Peter Boncz, Alfons Kemper, and Thomas Neumann. “How Good Are Query Optimizers, Really?”Proceedings of the VLDB Endowment9, no. 3 (2015): 204–215.doi:10.14778/2850583.2850594.
2. Viktor Leis, Andrey Gubichev, Atanas Mirchev, Peter Boncz, Alfons Kemper, and Thomas Neumann. “Still Asking: How Good Are Query Optimizers, Really?”Proceedings of the VLDB Endowment18, no. 12 (2025): 5531–5536.doi:10.14778/3750601.3760521.
3. Toshihide Ibaraki and Tiko Kameda. “On the Optimal Nesting Order for Computing N-Relational Joins.”ACM Transactions on Database Systems9, no. 3 (1984): 482–502.doi:10.1145/1270.1498.
4. Parimarjan Negi, Ryan Marcus, Andreas Kipf, Hongzi Mao, Nesime Tatbul, Tim Kraska, and Mohammad Alizadeh. “Flow-Loss: Learning Cardinality Estimates That Matter.”Proceedings of the VLDB Endowment14, no. 11 (2021): 2019–2032.doi:10.14778/3476249.3476259.
5. Tingwei Zhang, John X. Morris, and Vitaly Shmatikov. “How to Steal Reasoning Without Reasoning Traces.” arXiv preprint arXiv:2603.07267 (2026).doi:10.48550/arXiv.2603.07267.
6. Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. “DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models.” arXiv preprint arXiv:2402.03300 (2024).doi:10.48550/arXiv.2402.03300.
7. DeepSeek-AI (Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.). “DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.” arXiv preprint arXiv:2501.12948 (2025). Published as “DeepSeek-R1 Incentivizes Reasoning in LLMs Through Reinforcement Learning.”Nature645, no. 8081 (2025): 633–638.doi:10.1038/s41586-025-09422-z.
8. Ryan Marcus, Parimarjan Negi, Hongzi Mao, Nesime Tatbul, Mohammad Alizadeh, and Tim Kraska. “Bao: Learning to Steer Query Optimizers.” arXiv preprint arXiv:2004.03814 (2020). Published as “Bao: Making Learned Query Optimization Practical.”Proceedings of the 2021 International Conference on Management of Data (SIGMOD ’21)(2021): 1275–1288.doi:10.1145/3448016.3452838.
9. Kevin Lu, in collaboration with others at Thinking Machines. “On-Policy Distillation.”Thinking Machines Lab(blog), October 27, 2025.