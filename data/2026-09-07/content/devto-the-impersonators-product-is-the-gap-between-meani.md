---
title: The impersonator's product is the gap between meaning and spelling, so we measured both in Snowflake - DEV Community
url: https://dev.to/soumyadeepdey/the-impersonators-product-is-the-gap-between-meaning-and-spelling-so-we-measured-both-in-snowflake-e6f
site_name: devto
content_file: devto-the-impersonators-product-is-the-gap-between-meani
fetched_at: '2026-09-07T16:17:32.589430'
original_url: https://dev.to/soumyadeepdey/the-impersonators-product-is-the-gap-between-meaning-and-spelling-so-we-measured-both-in-snowflake-e6f
author: Soumyadeep Dey
date: '2026-09-06'
description: One SQL statement over a VECTOR(768) column, 45,400 charities, and 2,917,459 real pairs used to check it. What the detector caught, and what it missed. Tagged with devchallenge, weekendchallenge, 100daysofsolana, snowflake.
tags: '#devchallenge, #weekendchallenge, #100daysofsolana, #snowflake'
---

DEV Weekend Challenge: Generosity Edition Submission 💜

This is a submission forWeekend Challenge: Generosity Edition

Target categories: Best Use of Snowflake + Best Use of Solana.

What it is.An accountability layer for giving. Snowflake decides whether an organisation resembles a real charity and whether its reported deliveries are physically possible; Solana publishes a receipt with the person stripped out, so a donor can check the answer without trusting the charity, the platform, or this dashboard.

Why that is a generosity project.Generosity does not fail because people stop giving. It fails because giving and knowing are two different actions, and only one of them has ever been easy. Everything below is machinery for making the second one cheaper, while the gap is still open rather than in an audit nine months later.

Judging, and short on time?Four links, no clone, no keys.Snowflake·everything it is actually doing here, andthe detector as one SQL statement.Solana·the receipts on a public chain, one of which caught a defect in my own bridge.The number I would check first·an evaluation that does not rely on my own adversary: 2,917,459 real-organisation pairs, nothing synthetic in any of them.

## A clone keeps the meaning and changes the spelling, so measure both and publish the gap

Between the 8th and the 13th of January 2025, while Los Angeles was burning, somebody registered119 new domainscarrying the wordsLA fire,wildfire,relief,fundandrebuild. Five days. Roughly one every hour.

Somewhere in that week a person who wanted to help opened one of them. They read a name they half-recognised and a mission statement that sounded exactly right, and they gave. They had about four seconds and one browser tab in which to tell a real charity from a copy of one, and nothing on the screen was built to help them.

More than 250 million USD was raised for those fires. In 2024 the FBI logged over 4,500 complaints reporting approximately96 million USD lostto fraudulent charities and relief campaigns (IC3 PSA I-011625).

Nobody registers 119 domains for aninventedcharity. They register them for real ones with the serial numbers filed off: the same words reordered, one letter substituted, a real mission statement withFire Reliefstapled to the end. The obvious defence is string matching, and string matching is exactly the wrong tool, becausethe strings are deliberately different. That is the product the impersonator is shipping.

So the question is not "how close are these two names?" It is:what if you measured meaning and spelling separately and treated the distance between them as the signal?An impersonation is a claim about meaning. A meaning is a vector. A vector distance is a query.

IRS BMF + IATI ---> Snowflake -----> Snowflake ------> Snowflake ----> Solana (devnet)
 45,400 orgs 6 Dynamic VECTOR_COSINE_ H3 over 40 285 compressed
 44,101 verified Tables at SIMILARITY over districts, NFT receipts on
 400 seeded clones 60s lag VECTOR(768) 28 countries a depth-14 tree

Enter fullscreen mode

Exit fullscreen mode

GLASSPOCKETdetects impersonation by meaning rather than spelling, detects diversion by geography and timing, and writes a public tamper-evident receipt for every verified disbursement, so a donor can check a claim without trusting the charity, the platform, or me.

45,400 organisations → 400 seeded imitations → 62,247 candidate pairs → 276 detected → 148 needing a second look → 9,716 deliveries across 40 districts in 28 countries → 285 receipts on a public chain.Devnet, and labelled as devnet everywhere it is counted. Every arrow is SQL inside one Snowflake account, except the last, which is a Node process that holds a key the warehouse never sees.

The whole detector in one picture. Both names are measured twice, and the impersonator's product is the distance between the two measurements.

One of these is on a public IRS filing list. The other is generated. Their names agree on 99% of their meaning and 77% of their spelling, and the difference between those two numbers is the whole project.

## One thing up front, because it changes how you read every number below

Every impersonating organisation here is generated, and so is every beneficiary record.No real organisation is ever shown flagged. That is not a policy, it is aWHEREclause: the join readsWHERE s.is_synthetic = TRUE AND t.is_verified = TRUE, so the suspect side is always seeded and the target always real. Two acceptance checks fail the build otherwise, and every seeded row carriesbatch_id = 'SYNTH_ADVERSARY_V1'. Naming a real charity as a suspect on a cosine distance is the exact error this project criticises.

The headline accuracy number is deliberately the worse one.The specification fixed the cosine cut-off at 0.86. Measured against ground truth, 0.86 gives 91.3% recall and52.7% precision, and at that setting the detector offered"Hispanic Leadership Trust"against"Vote Org", two organisations sharing a sector and nothing else. The shipped cut-off is 0.94:97.8% precision, 67.5% recall.So270 of the 400 seeded imitations are caught and 130 are not.The flattering number was available and it would have made the opening screen a liar.

The blind spot is the exact tactic the wildfire data documents.Disaster attachment, appendingFire Reliefto a real charity's name, is caught18 times out of 108: median cosine 0.9141, because dropping the distinguishing tail genuinely changes the meaning, and this detector is built on meaning.Breakdown below.

Two of this build's own claims failed verification, and both are in this post.The platform limitation I documented most carefully turned out to bemy own syntax error. And the receipt ledger caught my bridgeminting 79 disbursements twice, which the warehouse's own bookkeeping reported as a clean run. A project about checking claims does not get an exemption from being checked.

The threat I opened with is wider than the corpus I search.Somebody registeringlafirerelieffund.comduring a wildfire never files for 501(c)(3) status, so they are not in the Business Master File and this will never see them. What it sees is a registered entity impersonating another, a real problem and a narrower one.It cannot see money that never entered a reporting system at all, which is very likely where the largest losses sit.Domain reputation and payment rails defend the other half, and nothing here replaces them.

One tab was cut and came back, and the reason it was cut is the most interesting thing in this post."The Wall", the privacy demonstration, was dropped two days before submission because differential privacy was recorded as unavailable on this account. That record wasmy own syntax error. Written correctly it attaches, so the tab returns carrying three governance regimes over one set of facts instead of two, and it now measures its own defeat. The build has ten sections, not eleven.

Full accounting inWhat's real and what's simplified.

## The walkthrough

## Verify this in 60 seconds, no keys, no clone

1 · The detector is one SQL statement.sql/07_clone_detection.sqlisVECTOR_COSINE_SIMILARITYover aVECTOR(FLOAT, 768)column, a Jaro-Winkler distance beside it, and a subtraction. There is no model server and no Python in the detection path.

2 · The score is a UDF you can add up by hand.sql/09_risk_score_udf.sqlhas five weighted terms, all five are materialised as columns next to the total, and an acceptance check fails the build if they stop summing to it. The arithmetic is done by handfurther down this post.

3 · The receipts are on a public chain, and you do not need my RPC to check it.Compressed NFT asset ids have no on-chain account, so every link below is atransactionor areal account, both of which resolve on the public devnet endpoint with no DAS provider:

What

Address

What the chain says it is

Merkle tree

GNSmaut…nr4Pxrw

SPL Account Compression, 
31,800 bytes

Tree config

EwmB1Ms…jHNgL6vD

Bubblegum PDA, 96 bytes

Collection mint

DyMd1dx…CR3qCvDe

SPL Token, 82 bytes, a real mint

Signing authority

2EtX5Di…kwjMkbdr

fee payer on all 285. Never touches Snowflake.

Receipt holder

ERcokh7…2oKcAFFx

leaf owner for every receipt

31,800 bytes is a specification, not a round number.A concurrent Merkle tree at depthd, bufferboccupies56 + 24 + b(32 + 32d + 8) + (32d + 40)bytes. Atd = 14, b = 64that is exactly 31,800; depth 13 gives 29,720, depth 15 gives 33,880.2^14 = 16,384 leaves, 314 used, established from the account size alone.

Five transactions, checked live againstapi.devnet.solana.comwhile writing this:

Disbursement

Leaf

Transaction

Slot

DSB-0000005

0

4sfqeJmY…HupqVsKk

493191506

DSB-0000247

129

5MiLdwfv…GhRbtRK1

493195283

DSB-0000247

130

4JxZw6FQ…a74HoqdE

493195284

DSB-0006575

150

4qPua654…S2Wf69bp

493195777

DSB-0002036

313

4J9vHkLS…vfEExehw

493199518

Two of those rows are the same disbursement, one slot apart.A defect, and the chain is how I found it.

### The check I would make if I were judging this

Open the first transaction and expandProgram Instruction Logs. Bubblegum prints:

Program log: Instruction: MintToCollectionV1
Program log: Leaf asset ID: C1DMNAYqnSa5X9XqPbue4ATDw1xnrPus3zErCMXcb3FV

Enter fullscreen mode

Exit fullscreen mode

Now run this against the warehouse:

SELECT
 
asset_id
,
 
leaf_index
,
 
tree_address

FROM
 
ORACLE
.
MINT_LOG

WHERE
 
disbursement_id
 
=
 
'DSB-0000005'
;

Enter fullscreen mode

Exit fullscreen mode

It returnsC1DMNAYqnSa5X9XqPbue4ATDw1xnrPus3zErCMXcb3FV, leaf 0, that tree.The string in my table is the string the Solana runtime emitted, so the value in the operator's database has an independent source anybody can fetch. Across the batch, every seventh mint, 41 of 285:

sampled 41
not found on devnet 0
transactions in err 0
fee distribution {5000: 41} all five thousand lamports
compute units 44,477 to 58,850 varies with tree depth of the append
asset id logged 41
asset id MATCHES 41 warehouse string == runtime string
elapsed 64.6 s

Enter fullscreen mode

Exit fullscreen mode

Forty-one of forty-one. The strongest claim here is also the cheapest to falsify: take any row ofORACLE.MINT_LOG, open its signature, read the log line.

## SoumyaEXE/GLASSPOCKET

# GLASSPOCKET

A Snowflake accountability engine for charitable giving.

Multi-tab Streamlit application, Solana compressed-NFT receipt ledger
governed serving layer with an enforced minimum-cohort guarantee.

Generosity fails not because people stop giving but because they cannot see
where the money went. This is the machinery that lets them see.

The name refers to the "glass pockets" principle in philanthropy: an
organisation handling public generosity should be transparent enough that
anyone can see into its pockets.

## Challenge disclosure

Event

DEV.to Weekend Challenge, Generosity Edition

Primary category

Best Use of Snowflake

Secondary category

Best Use of Solana

Cluster

Solana 
devnet
, never mainnet

Synthetic data

Present, labelled in the data and in the interface

Every impersonating organisation and every beneficiary record in this project
isgenerated. Every one carriesbatch_id = 'SYNTH_ADVERSARY_V1'andis_synthetic = TRUE, renders a visible "seeded" chip, and is disclosed on the
Method and Honesty tab. Real organisations…

View on GitHub

### The receipt I care about most

Everything above is a static artefact. This one is a stopwatch: six signatures read out of the localORACLE.MINT_LOGmirror and checked againstapi.devnet.solana.comwhile writing this section.

02:06:42.034 reading ORACLE.MINT_LOG mirror
02:06:42.758 DSB-0000075 leaf 311 slot 493199473 fee 5000 err None
02:06:43.545 DSB-0000075 leaf 312 slot 493199506 fee 5000 err None
02:06:44.086 DSB-0000247 leaf 129 slot 493195283 fee 5000 err None
02:06:44.727 DSB-0000247 leaf 130 slot 493195284 fee 5000 err None
02:06:45.280 DSB-0000005 leaf 0 slot 493191506 fee 5000 err None
02:06:45.797 DSB-0003419 leaf 1 slot 493191553 fee 5000 err None
 ──────────────────────────────────────────────────────────
 3.76 s warehouse mirror -> public ledger, all six matched

Enter fullscreen mode

Exit fullscreen mode

Read the twoDSB-0000247lines again.Slot 493195283 and slot 493195284.Consecutive slots, same disbursement, two different assets. I will come back to that, because it is the most useful thing in this post.

## The evasion gap, and why charity impersonation defeats string matching

Here is the whole detector. It is longer to describe than it is to read.

-- sql/07_clone_detection.sql

WITH
 
candidates
 
AS
 
(

 
SELECT

 
s
.
org_id
 
AS
 
suspect_id
,
 
s
.
name
 
AS
 
suspect_name
,

 
t
.
org_id
 
AS
 
target_id
,
 
t
.
name
 
AS
 
target_name
,

 
s
.
city
,
 
s
.
state
,
 
s
.
cause
,
 
s
.
synth_technique
,

 
VECTOR_COSINE_SIMILARITY
(
s
.
name_vec
,
 
t
.
name_vec
)
 
AS
 
semantic_sim
,

 
JAROWINKLER_SIMILARITY
(
s
.
name
,
 
t
.
name
)
 
/
 
100
.
0
 
AS
 
string_sim

 
FROM
 
STAGING
.
ORGS
 
s

 
JOIN
 
STAGING
.
ORGS
 
t

 
ON
 
s
.
region_h3
 
=
 
t
.
region_h3
 
-- REQUIRED pre-filter

 
AND
 
s
.
cause
 
=
 
t
.
cause
 
-- REQUIRED pre-filter

 
AND
 
s
.
ein
 
<>
 
t
.
ein

 
WHERE
 
s
.
is_synthetic
 
=
 
TRUE
 
-- suspect side is ALWAYS seeded

 
AND
 
t
.
is_verified
 
=
 
TRUE
 
-- target side is ALWAYS real

 
AND
 
s
.
name_vec
 
IS
 
NOT
 
NULL

 
AND
 
t
.
name_vec
 
IS
 
NOT
 
NULL

)

SELECT
 
*
,
 
semantic_sim
 
-
 
string_sim
 
AS
 
evasion_gap

FROM
 
candidates

WHERE
 
semantic_sim
 
>=
 
0
.
94
;

Enter fullscreen mode

Exit fullscreen mode

Read it aloud:for every seeded organisation, find the real ones in the same H3 region and cause, measure how close the names are in meaning and in spelling, and keep the pairs where the meaning is nearly identical.

The last line of theSELECTis the argument.semantic_simalone says two names are similar, which is not news.string_simalone is what every fuzzy-matching tutorial gives you, and it is what the impersonator defeats on purpose.The subtraction is the finding: names that agree on what they mean while disagreeing on how they are written.One number with no denominator is not a finding; a pair moving in opposite directions is.

The organisation on the hero image scores0.991944on meaning,0.77on spelling, gap0.221944. A human sees it in four seconds, but only with both names in front of them at once, which is exactly what a donor clicking a link in a disaster feed does not have.

### The pre-filter is not an optimisation

Vector similarity at general availability performs an exact scan, so an unfiltered self-join is a full cross product:

45,400 x 45,400 = 2,061,160,000 pairs
after region_h3 + cause + side rule = 62,247 pairs
of which cleared 0.94 = 276

Enter fullscreen mode

Exit fullscreen mode

A33,000xreduction, and the same two predicates make it structurally impossible for a real organisation to land on the suspect side. The comment in the file says it plainly: if a similarity query here ever runs long, the pre-filter has been removed. Restore it.

## The threshold, re-measured against ground truth

The specification named 0.86. That number belonged to a pipeline whereAI_EMBEDruns inside the warehouse. This account blocks every AI function, so the vectors come from the same model,snowflake-arctic-embed-m, run locally and loaded into a realVECTOR(FLOAT, 768)column.The comparison did not move: every cosine is still computed by Snowflake over aVECTORcolumn. Only the machine that produced the vectors did.

Worth stating precisely, because it is the kind of claim that sounds verified and is not:same modelmeans the same model identifier, not vectors I checked against warehouse-generated ones. I could not check them, because the function that would have produced the comparison set is the one that is blocked.

A threshold is a property of the vectors, so it had to be re-measured. Ground truth is knowable here, the one advantage of an adversary you generated yourself: every seeded organisation records its real target insynth_target_id. The curve is materialised intoMARTS.THRESHOLD_CALIBRATIONand driven by a slider.

threshold

pairs

true

precision

recall

0.86

692

365

52.7%

91.3%

0.90

389

336

86.4%

84.0%

0.92

332

301

90.7%

75.3%

0.94

276

270

97.8%

67.5%

0.95

252

247

98.0%

61.8%

0.97

169

166

98.2%

41.5%

0.94 is where precision turns the corner. Above it precision barely improves and recall keeps falling.The real corpus points at the same elbow, from disjoint inputs.

Precision and recall on the same axis, precomputed across the whole range so the slider responds with no query behind it. The production cut-off is the marked point, not the best-looking one.

### What the detector misses

Per technique, which ones it handles and which it does not:

Technique

Seeded

Detected

Median cosine to its real target

Semantic clone

104

104

0.9718

Token reorder

108

94

0.9788

Homoglyph and spacing

80

60

0.9819

Disaster attachment

108

18

0.9141

Three techniques clear the line. The fourth is the one the wildfire domain count is a record of.

Three of the four techniques sit comfortably above the cut-off. The fourth does not, and the fourth is the one the BforeAI wildfire count is a record of.

The reason is not a bug.Illinois Coalition For Immigrant And Refugee RightsbecomesIllinois Coalition For Fire Recovery. The imitator keeps the recognisable prefix, which is what a donor's eye lands on, and replaces the distinguishing tail, which is what the sentence embedding weights.A detector built on meaning fails on the attack that changes the meaning while keeping the brand.Cosine similarity over a whole name has no concept of a prefix being load-bearing.

The fix is not a lower threshold, because 0.86 already showed what that buys. It is a second signal: a prefix-anchored comparison, or a disaster-keyword predicate against a live registration feed. Neither is in this build.

This is the one table I built expecting to be disappointed by, and I was. If you know a way to make a sentence embedding treat a name's opening tokens as load-bearing without falling back to a string metric, that is the comment I actually want on this post.

## Two evaluations that do not depend on my adversary

Everything so far is measured against imitations I generated using techniques I chose. That is the sharpest objection to this project and disclosing it does not answer it. Here are two measurements where I constructed nothing.

### The detector, over the real corpus only

The pipeline forbids a real organisation on the suspect side, so this ran outside it:44,101 real verified organisations, same pre-filter, same vectors, same cut-off, no synthetic data anywhere.

real-vs-real pairs evaluated 2,917,459
pairs firing at 0.94 12,430 0.4261%
organisations involved 408 of 44,101 (0.93%)

Enter fullscreen mode

Exit fullscreen mode

Then the part that matters.11,795 of those 12,430 firings, 94.9%, are the same organisation name filed under a different EIN, and they come from only 152 distinct names:

Pairs

Name

5,995

PEO Sisterhood International Chapter

3,240

National Wild Turkey Federation

288

Board of Regents of the University of Wisconsin System

261

Michigan State University

160

The Ohio State University

The dominant real-world failure mode is not fraud. It is chapters.A national body with four hundred affiliates produces a combinatorial explosion of identical-name pairs, and two organisations alone account for 74% of everything the detector says on the real corpus. Of the remaining 635 pairs almost all areInc,The, andOf KyagainstOf Kentucky. The one I would call a false positive isEnvironmental Working GroupagainstEnergy And Wildlife Action Coalitionat 0.9401, sitting on the threshold.

None of that is in the build. An affiliate-aware pre-pass keyed on the national parent is the obvious next component and it is not written.

### The same threshold, from real data alone

How many real pairs does each cut-off drag into a review queue?

threshold

real pairs firing

rate

0.86

39,016

1.3373%

0.90

18,011

0.6174%

0.92

14,565

0.4992%

0.94

12,430

0.4261%

0.96

11,490

0.3938%

0.98

11,375

0.3899%

Moving from the specified 0.86 to the shipped 0.94 removes 26,586 real-organisation pairs from the queue, and the curve goes flat immediately after, because the residual is chapter clusters sitting at cosine 1.0 where no threshold reaches. Past 0.94 you pay recall and buy nothing. The elbow the synthetic data pointed at is the elbow the real data points at, computed from disjoint inputs.

### Held out the technique, then re-picked the cut-off

0.94 was also chosen while looking at all four techniques. So re-choose it by F1 on three, with the 2.9 million real pairs as false positives, and apply it to the fourth, unseen.

Held-out technique

Cut-off chosen on the other three

Recall on held-out

Recall at 0.94

disaster attachment

0.945

12.6%

17.5%

homoglyph and spacing

0.935

79.2%

77.9%

semantic clone

0.935

98.0%

98.0%

token reorder

0.930

100.0%

96.9%

Two things follow, and one of them is not flattering.

The threshold is not overfit.Every re-pick lands between 0.930 and 0.945, and held-out recall moves at most five points against the shipped number. 0.94 is a property of these vectors, not of the technique mix I wrote.

The detector does not generalise to a technique family it has not seen.Held-out disaster attachment recovers 12.6%; inside its tuning set, 17.5%. Both are bad, and the honest reading is that this approach handlesrewritesof a name and fails onreplacements, whichever set you tune on. That is a limit of whole-name embeddings, not a threshold you can move.

## Geometry, because the second half of the problem is not the name

Impersonation is the fundraising side. The disbursement side fails differently, and the sector's answer is a PDF nine months later. The World Food Programme reported 590 trucks moved from Ashdod to Kerem Shalom of which371 were collected inside Gaza; India's MGNREGA report recorded 169.75 crore rupees misappropriated against 20.93 crore recovered across 125,602 cases.

The delivery corpus is modelled, and its attrition is calibrated against that WFP ratio rather than chosen to look dramatic:63.31% of dispatched value is delivered, against WFP's 62.88%.An acceptance check fails the build if that drifts more than three points.

The geometry test is not modelled. It is ordinary SQL over H3 cells:

-- sql/08_geospatial_h3.sql

CASE

 
WHEN
 
status
 
=
 
'UNACCOUNTED'
 
THEN
 
'NEVER_ARRIVED'

 
WHEN
 
hops
 
>
 
max_hops
 
THEN
 
'OUTSIDE_FOOTPRINT'

 
WHEN
 
transit_hours
 
<
 
1
 
AND
 
km_from_base
 
>
 
400
 
THEN
 
'IMPOSSIBLE_TRANSIT'

 
ELSE
 
'PLAUSIBLE'

END
 
AS
 
geometry_verdict

Enter fullscreen mode

Exit fullscreen mode

Two decisions worth stealing.

1. Distance is measured from the declared operating base, not the registered postal address.An organisation registered in Delaware delivering food in Kassala is an international NGO doing what it said. Measure from the postal address and you flag every event, and a detector that flags everything has detected nothing.
2. H3_GRID_DISTANCEraisesError trying to compute the path between cellsonce the two cells sit in different resolution-0 base cells, which is as soon as a delivery crosses a continent. That case needs no arithmetic: a sentinel of9999exceeds everymax_hops. A crash there is an outage; a silentNULLis worse, becauseNULLin a>comparison reads asplausible.

Across 9,716 events in40 districts across 28 countries and six continents, from Gaza North and Kutupalong to Goma, Lviv, Port-au-Prince and Port Vila: 7,736 plausible, 1,022 never arrived, 759 outside footprint, 199 impossible transit.

The spread is not decoration.hops > max_hopsis only an interesting question when footprints are far enough apart for the answer to vary, and sixteen districts inside one band of latitude made every stray delivery look alike.

Every delivery from the organisation's filing address to where it claims to have landed: 9,716 events across 40 districts in 28 countries. Colour is the geometry verdict, and the red ends are the deliveries that landed outside the footprint the organisation declared.

## The score is a UDF, and that is what makes the Historian possible

An opaque score is unusable in an accountability tool, soMARTS.F_RISKis a SQL UDF, five weighted terms, no hidden state:

-- sql/09_risk_score_udf.sql

LEAST
(
100
,

 
35
 
*
 
GREATEST
(
0
,
 
(
semantic_sim
 
-
 
0
.
86
)
 
/
 
0
.
14
)

 
+
 
25
 
*
 
LEAST
(
1
,
 
evasion_gap
 
/
 
0
.
45
)

 
+
 
20
 
*
 
LEAST
(
1
,
 
geom_flags
 
/
 
5
.
0
)

 
+
 
12
 
*
 
LEAST
(
1
,
 
unaccounted_ratio
)

 
+
 
8
 
*
 
LEAST
(
1
,
 
missing_receipts
 
/
 
10
.
0
))

Enter fullscreen mode

Exit fullscreen mode

All five are materialised as columns beside the total, from the same weights so they cannot drift. Ordinary good practice. Here is the part that is not.Because the components sit next to the total, an operator editing the total by hand leaves a trace, and catching it needs no audit table:

SELECT
 
COUNT
(
*
)
 
AS
 
rows_scored
,

 
COUNT_IF
(
ABS
(
LEAST
(
100
,
 
comp_semantic
 
+
 
comp_evasion
 
+
 
comp_geometry

 
+
 
comp_unaccounted
 
+
 
comp_receipts
)
 
-
 
risk_score
)
 
>
 
0
.
001
)
 
AS
 
hand_edited

FROM
 
MARTS
.
ORG_RISK

Enter fullscreen mode

Exit fullscreen mode

The answer is 0 on 45,400 rows.UPDATE MARTS.ORG_RISK SET risk_score = 12 WHERE org_id = ...and it becomes 1 immediately, with the row listed and its reconstructed value beside its stored one. Nothing was logged. The arithmetic is the log.

Snowflake supplies the second half:

SELECT
 
'current'
 
AS
 
version
,
 
org_id
,
 
name
,
 
risk_score
,
 
verdict

FROM
 
MARTS
.
ORG_RISK
 
WHERE
 
org_id
 
=
 
?

UNION
 
ALL

SELECT
 
'before'
,
 
org_id
,
 
name
,
 
risk_score
,
 
verdict

FROM
 
MARTS
.
ORG_RISK
 
AT
(
OFFSET
 
=>
 
-
300
)
 
WHERE
 
org_id
 
=
 
?

Enter fullscreen mode

Exit fullscreen mode

AT(OFFSET => -300)is Time Travel, five minutes back, needing no audit table and no schema of mine. It is not free: retention holds changed micro-partitions and Snowflake bills for them. What it costs nothing of is design.An accountability tool its operator can quietly edit is not one, and the two mechanisms that make that visible are a decomposable score and a retention setting.

That 90-day retention is Enterprise-gated, and reading it back is also how the build establishes its own edition, becauseCURRENT_EDITION()is an unknown function on this deployment.

The five components sum to the total on every row. When they stop, the row is listed and Time Travel prints what it used to say.

## The architecture

#

Stage

Tech

Lag

What it does

1

RAW

IRS BMF, revocation list, IATI, Census ZCTA

batch

Lands as 
STRING
, never edited. The regional IRS files disagree about column names.

2

STAGING

1 Dynamic Table

60 s

One row per entity: 
VECTOR(FLOAT, 768)
, three H3 cells, the labelling contract columns

3

MARTS

6 Dynamic Tables + 5 built tables

60 s

Clone pairs, delivery geometry, risk, calibration, graph layout, beneficiary facts

4

Governance

Aggregation policy and privacy policy, both with an entity key

n/a

MIN_GROUP_SIZE => 50
 on one terminal view, a 0.1 epsilon budget on a second one over the same facts

5

ORACLE

Queue, log, failures

n/a

The contract with the bridge, which is the only writer

6

SERVE

Streamlit in Snowflake

live

Ten sections, no external hosting, no credential anywhere in 
app/

Six schemas, left to right.

Both policies sit at the very end, and that ordering is forced.A policy-protected object breaks downstream Dynamic Table refresh, and a privacy-protected table blocks row-levelSELECTentirely. Each attaches to a terminal view with an entity key onbeneficiary_idand nothing downstream. Build it anywhere else and you find out at hour eleven that half the DAG will not refresh.

The counterfactual view had to move schemas, becauseUSE ROLE GP_ANALYSTis not enough to test asGP_ANALYST.DEFAULT_SECONDARY_ROLES = ('ALL')keepsACCOUNTADMINlive underneath, so the aggregation policy correctly applied the cohort floor while the unprotected view stayed readable anyway. The protection looked like it was working. Two fixes:USE SECONDARY ROLES NONEwherever the analyst persona is assumed, and the counterfactual moved to aPRIVILEGEDschema the role has noUSAGEon.Longer answer in the FAQ.

## The limitation that was my own syntax error

The centrepiece of this build was supposed to be differential privacy: a real privacy budget, releasing noised answers to broad questions and useless ones to narrow questions. It shipped as an aggregation policy withMIN_GROUP_SIZE => 50instead, that tab was then cut altogether, anddocs/platform_constraints.mdrecords why:

CREATE PRIVACY BUDGET ...
 -> SQL compilation error: syntax error at position 26 unexpected 'BUDGET'.

ALTER VIEW ... SET PRIVACY POLICY ... ENTITY KEY (beneficiary_id)
 -> SQL compilation error: syntax error at position 36 unexpected 'PRIVACY'.

Enter fullscreen mode

Exit fullscreen mode

The conclusion written under those two lines was:the keywords do not parse, so this is not a permissions problem and no grant fixes it. The feature is absent from this deployment.That sentence is in the repository, in the SQL file, in the README, and it was in the first draft of this post. It is wrong, and those two errors are the reason it is wrong rather than the evidence for it.

There is noCREATE PRIVACY BUDGETstatement in Snowflake.A budget comes into existence the moment you name one in the body of a privacy policy, throughPRIVACY_BUDGET(BUDGET_NAME => ..., BUDGET_LIMIT => ..., MAX_BUDGET_PER_AGGREGATE => ...). And the clause that attaches a policy to a view isADD PRIVACY POLICY, notSET. Replacing one isDROP PRIVACY POLICY a, ADD PRIVACY POLICY b ENTITY KEY (col)inside a singleALTER, so there is no window where the object sits unprotected.

Here is the same intent, in syntax that exists:

CREATE
 
OR
 
REPLACE
 
PRIVACY
 
POLICY
 
GLASSPOCKET
.
SERVING
.
beneficiary_policy

 
AS
 
()
 
RETURNS
 
PRIVACY_BUDGET
 
->

 
PRIVACY_BUDGET
(
BUDGET_NAME
 
=>
 
'gp_analysts'
,

 
BUDGET_LIMIT
 
=>
 
300
,

 
MAX_BUDGET_PER_AGGREGATE
 
=>
 
0
.
1
);

ALTER
 
VIEW
 
GLASSPOCKET
.
SERVING
.
V_BENEFICIARY_OUTCOMES

 
ADD
 
PRIVACY
 
POLICY
 
GLASSPOCKET
.
SERVING
.
beneficiary_policy

 
ENTITY
 
KEY
 
(
beneficiary_id
);

ALTER
 
VIEW
 
GLASSPOCKET
.
SERVING
.
V_BENEFICIARY_OUTCOMES

 
MODIFY
 
COLUMN
 
amount_usd
 
SET
 
PRIVACY
 
DOMAIN
 
(
0
,
 
5000
);

Enter fullscreen mode

Exit fullscreen mode

Differential privacy is Enterprise-gated, and this account is provably Enterprise: it accepts aggregation policies and ninety-day retention, which is how the build establishes its own edition.

So the honest version of that sentence is not "the platform does not have this feature". It is:I wrote two statements that were never in the language, read the parser's refusal as a capability report, and built a fallback, a relabelled tab and three paragraphs of documentation on top of it.A parser error tells you a statement is malformed. It does not tell you a feature is missing, and for a weekend I treated those as the same fact.

I ran the corrected version before publishing this.It attached on the first attempt, on the same account and the same warehouse that had supposedly refused it.

Attaching the policy was the easy half. The privacy engine then refused four more times, and each refusal is a real constraint:they are in the hazards tablewith the rest of the verbatim errors. The one query shape surviving all four isCOUNT(DISTINCT beneficiary_id)with filters over columns that declare a privacy domain, which is precisely the question The Wall exists to ask.The platform forced the tab to count people rather than rows.An earlier version counted rows while printing a caption claiming otherwise, reading 8,545 against 7,275 actual beneficiaries.

### Three answers to one question

A privacy policy and an aggregation policy cannot sit on the same object, so this is a second view over the same facts rather than a replacement, which is better than what I originally wanted:

no policy

aggregation policy

differential privacy

everyone in the corpus

8,113

8,113, exact

8,096 / 8,113 / 8,136

one district

393

393, exact

388 / 400 / 358

one district, one programme, one month

4

withheld

0 / 16 / 28 / 5 / 31

Twenty-five repeats of the unfiltered count: mean 8,115.4 against a true 8,113,standard deviation 9.3. The noise is additive and roughly constant in absolute terms, which is why it is invisible on eight thousand people and ruinous on four.

Look at the last row.The floor refuses and says it is refusing. The budget answers and never mentions the answer is worthless.Both protect the same four people, and they fail in opposite directions. Showing one without the other is how a build ends up claiming a guarantee it does not have, which is what this one did for a weekend.

Every number here was read off the warehouse. The floor's answer is a single point because it does not perturb what it releases; the budget's is a cloud wider than the secret it is hiding.

The same three cards, live in the warehouse. Only the policy attached to each object differs.

### The attack, measured both ways

The tab sweeps every scope for a pair of permitted questions whosedifferenceis a group the floor would never answer about. It finds seventeen. The worst is Nyala district: 393 people, 381 of whom received at least a dollar. Both questions clear the floor of fifty and both are answered exactly.

Subtract them and you have learned abouttwelve people: that they exist, how many, where, and that they received nothing at all. The floor returned that 12 twice, identically, because a cohort floor does not perturb what it releases.

Thirty runs of the same pair through the privacy policy: mean 14.8,standard deviation 18.2, range −27 to +51. Five of thirty landed within two people of the truth.Four recovered a negative number of people.

And the budget as I configured it still does not stop the attack.Averaging shrinks error by the square root of the trial count, so grinding 18.2 down to one person takes about 330 trials: 660 queries, 66 epsilon.BUDGET_LIMIT => 300at0.1per aggregate permits 3,000, so a patient attacker finishes with budget to spare. Noise does not stop repetition.A limit set below the cost of the attack stops repetition, and mine is set above it.The tab does that arithmetic on screen rather than burying it here.

The aggregation policy that shipped first is real, Snowflake enforces it rather than my application, and everything this post says aboutitholds. What does not hold is the reason I gave for shipping it alone.

A negative result about a platform needs the same evidence as a positive one.docs/platform_constraints.mdopens by boasting that every claim in it comes from running the statement rather than reading the documentation, and that is exactly backwards: running a statement tells you what that statement does, and only the documentation tells you whether it was the right statement. Two of that file's ten findings rest on this error. The other eight, including509009and every AI function refusal, are messages about capabilities rather than syntax, and those stand.

## Publishing the claim, not the data

A donor checking a claim about a charity checks it against a record kept by the charity, by a platform the charity pays, or by an application built by a stranger. Every one requires trusting an interested party. That is the reason a chain is here, and it is a real property rather than a decorative one.

Every verified disbursement is minted as a compressed NFT on devnet, and the shape of the receipt is the security argument:

On chain:programme code, amountband, deliverywindow, a salted SHA-256 hash of the organisation identifier, a schema version.Never:beneficiary identifier, coordinates, organisation name, exact amount, exact timestamp.

// bridge/src/mint.ts

attributes
:
 
[

 
{
 
trait_type
:
 
"
schema
"
,
 
value
:
 
"
glasspocket-receipt-1
"
 
},

 
{
 
trait_type
:
 
"
programme
"
,
 
value
:
 
row
.
programmeCode
 
},

 
{
 
trait_type
:
 
"
amount_band
"
,
 
value
:
 
row
.
amountBand
 
},
 
// '2K-10K'

 
{
 
trait_type
:
 
"
window
"
,
 
value
:
 
row
.
windowKey
 
},
 
// '2026-06'

 
{
 
trait_type
:
 
"
org_hash
"
,
 
value
:
 
row
.
orgHash
 
},

 
{
 
trait_type
:
 
"
cluster
"
,
 
value
:
 
"
devnet
"
 
},

]

Enter fullscreen mode

Exit fullscreen mode

The receipt is a claim with the person removed. A band, not a figure. A month, not a moment. A hash, not a name.

Note what is absent:there is no beneficiary field to forget to strip, becauseORACLE.MINT_QUEUEdoes not carry one either.The privacy property is enforced by the shape of the table, and an acceptance check fails the build if a forbidden column appears. A public ledger is permanent, and permanence plus personal data is a harm you cannot undo.

### The same test, pointed at Solana

The elimination test below is applied to Snowflake. Point it at the chain:could this be a signed row in Postgres and a public append-only log?

Mostly, yes, and cheaper. Two things it does not do.It survives the operator, because a log I host stops existing when I stop paying, and the receipts are the artefact that has to outlive the project. Andverification needs nothing from me: no endpoint, no uptime, no key I could rotate or lose.

Neither buys correctness. A receipt is only as good as the pipeline that produced the row, which the section above demonstrates at my expense, and devnet has no economic guarantees.If you only need to prove an operator did not retro-edit their numbers, sign a log and publish the hashes.The chain earns its place because the record has to be readable after GLASSPOCKET is gone.

The security property worth checking: the signing key never touches Snowflake.The warehouse stages rows in a queue and does nothing else. A Node process holds the key, signs, submits, writes the signature back. Grep the SQL for key material and there is nothing to find, because Snowflake has no code path here that can sign anything. The arrow pointsintothe warehouse, and the first reason is that trial accounts have no external network access (509009: External access is not supported for trial accounts, confirmed by running it). The second reason is better than the first.

## One finding, all the way down

Every architecture diagram in every hackathon post is boxes with arrows. The alternative:one organisation, and the actual value at every layer it passed through.ORG_916803484, seeded, techniquetoken reorder.

#

Layer

The actual value

1

STAGING.ORGS

Archery Booster Club of Manual High School Inc
, EIN 916803484, Louisville KY, 
education

2

synth_target_id

ORG_933213165
 = 
Manual High School Archery Booster Club Inc
, real, verified, same city and blurb

3

name_vec

VECTOR(FLOAT, 768)
, 
snowflake-arctic-embed-m

4

VECTOR_COSINE_SIMILARITY

0.991944

5

JAROWINKLER_SIMILARITY

0.77
 → 
evasion_gap
 
0.221944

6

MARTS.DELIVERY_GEOMETRY

12 events, 5 districts: 6 plausible, 3 never arrived, 2 outside footprint, 1 impossible transit → 
geom_flags
 
6

7

one flagged event

DSB-0005571
, Balrampur, 
12,588.1 km
 from base, 
0 transit hours
 → 
IMPOSSIBLE_TRANSIT

8

MARTS.DT_ORG_ACTIVITY

pledged 63,046.70 · moved 57,468.07 · delivered 32,991.59 · unaccounted 
18,113.36
 → 
0.31519

9

MARTS.DT_RECEIPT_COVERAGE

10 eligible, 
0 on chain
, 10 missing

10

MARTS.ORG_RISK

risk_score
 
77.098507
, verdict 
needs a second look

Read rows 5 and 6 together.The clone detector never saw a coordinate. The geometry detector never saw a name.One compares 768-dimensional vectors, the other compares H3 cells and timestamps. They share a join key and nothing else, and they agree. Because geography is not an input to the similarity, the two agreeing is a result rather than a construction.

### Now decompose the number that the interface printed

77.098507is not a score a model emitted. TakeF_RISKand this organisation's own facts, which are stored in the same row:

semantic (0.991944 - 0.86) / 0.14 = 0.942457 -> x 35 = 32.986004
evasion min(1, 0.221944 / 0.45) = 0.493209 -> x 25 = 12.330223
geometry min(1, 6 / 5) = 1.000000 -> x 20 = 20.000000
unaccounted min(1, 0.31519) = 0.315190 -> x 12 = 3.782280
receipts min(1, 10 / 10) = 1.000000 -> x 8 = 8.000000
 ──────────
 LEAST(100, ) 77.098507

Enter fullscreen mode

Exit fullscreen mode

That is the published digit, reached by hand from columns anyone can select. The geometry term iscapped: six flags and five score identically, so one very messy organisation cannot drown out four moderately suspicious ones in a ranked list.

The honest caveat on this particular finding, click to expand

This organisation is generated and its twelve delivery events are modelled. What is not generated is any arithmetic above: a genuine arctic-embed vector, a cosine and H3 hops computed by Snowflake, a score evaluated by a UDF. The finding is real about a fictional organisation, which is the most an adversarial corpus can claim, and it is why the two evaluations above exist.

## The receipt that audited us

The claim this project makes about Solana is that a donor should not have to trust the operator. That includes me, as I found out two days before writing this.

ORACLE.MINT_LOGholds285 rows for 206 distinct disbursements, so seventy-nine were minted twice. Leaf indices run 0 to 313 with 29 gaps, so the tree holds more leaves than the warehouse knows about. Duplicate pairs land seconds apart and often inconsecutive slots:493195283and493195284forDSB-0000247, both confirmed, botherr: null, both paid for.

The defect is four lines of TypeScript and it is not the part I expected:

// bridge/src/snowflake.ts, claimBatch

await
 
this
.
execute
(

 
`UPDATE ORACLE.MINT_QUEUE SET status = 'CLAIMED', claimed_at = CURRENT_TIMESTAMP()
 WHERE queue_id IN (SELECT queue_id FROM ORACLE.MINT_QUEUE
 WHERE status = 'PENDING' ORDER BY queue_id LIMIT ?)`
,
 
[
size
]);

const
 
rows
 
=
 
await
 
this
.
execute
(

 
`SELECT queue_id, disbursement_id, ...
 FROM ORACLE.MINT_QUEUE
 WHERE status = 'CLAIMED'
 AND claimed_at >= DATEADD('minute', -2, CURRENT_TIMESTAMP())
 ORDER BY queue_id LIMIT ?`
,
 
[
size
]);

Enter fullscreen mode

Exit fullscreen mode

The claim is atomic. The read-back is not.TheUPDATEreserves rows nobody else can. TheSELECTafter it asks foranyrow inCLAIMED, not the rows this call just claimed. One process is fine; two are a disaster, because the second claims fifty fresh rows and then reads back the first process's fifty, which sort lower onqueue_id, and mints them again. Same bug verbatim inORACLE.SP_CLAIM_BATCHwith a one-minute window. The fix is to return the claimed ids from theUPDATEand select on those. Small change. What it demonstrates is not.

I did not find this in the warehouse.ORACLE.MINT_QUEUEreports 193MINTED, 132CLAIMED, 23FAILED, and every one of those states is internally consistent. Thirteen of the twenty-threeFAILEDrows have a confirmed receipt on chain, because the mint succeeded and the leaf parse afterwards did not. The warehouse said the job went fine.The ledger disagreed, because it counts what happened rather than what the operator recorded, and no amount of my being careful changes that.

That is the argument for putting receipts on a chain, made by accident, against the person making it. I would rather publish it than the version where the number is 285 and nobody asks what 285 divides into.

Minting is a migration against a queue that already existed. It stops when the devnet wallet stops, which is a funding limit, and it is drawn as a step rather than smoothed into something that looks like steady progress.

## Everything Snowflake is actually doing here

The test I held myself to:could this be swapped for a Postgres box and a cron job without losing the argument?If yes, it did not belong in the build.

Feature

Where

Why it is not decoration

VECTOR(FLOAT, 768)
 + 
VECTOR_COSINE_SIMILARITY

07_clone_detection.sql

the entire thesis: impersonation compared by meaning, in SQL, no model server

JAROWINKLER_SIMILARITY

07_clone_detection.sql

the other half of the subtraction, so the gap is one expression

Six Dynamic Tables at 
TARGET_LAG = '60 seconds'

05_staging_dynamic_tables.sql

declarative freshness, no scheduler in the transform layer

H3_LATLNG_TO_CELL_STRING
, 
H3_CELL_TO_PARENT
, 
H3_GRID_DISTANCE
, 
H3_GRID_DISK
, 
H3_CELL_TO_POINT

08_geospatial_h3.sql

a footprint is a set of cells, not a radius on a projection

ST_POINT
 / 
ST_DISTANCE

08_geospatial_h3.sql

the metres behind the impossible-transit rule

SQL UDF 
F_RISK

09_risk_score_udf.sql

one score definition, decomposable by hand, components stored beside the total

Semantic view 
MARTS.GIVING_SEMANTICS

10_semantic_view.sql

2 tables, 6 dimensions, 4 metrics, 2 facts, and the shape the interface prints is read back with 
DESCRIBE SEMANTIC VIEW
 rather than typed into it

Aggregation policy with 
ENTITY KEY

11_privacy_policy.sql

Snowflake refuses the query, not the application. Switching roles does not help.

Time Travel 
AT(OFFSET => -300)

Historian

an operator edit is visible with no audit table and no schema of mine, though retention itself is billed

Streamlit in Snowflake

app/

runs inside the account with the data, 
get_active_session()
, no credential in 
app/

What it cost, read out of the systems rather than estimated. On Solana:285 mints at 5,000 lamports is 0.001425 SOL, plus0.16219424 SOLof rent for the tree. That rent is the whole reason to compress: paid once, covering 16,384 leaves,0.0000099 SOL per receipt slot. The uncompressed version is 16,384 separate rent-exempt mint accounts.

On Snowflake I am not quoting a credit figure, because I did not read one out ofACCOUNT_USAGEand an estimate is exactly the kind of number this post argues against. The three decisions that bound it: the pre-filter turning 2.06 billion candidate pairs into 62,247, materialising every embedding, similarity pair and geospatial join before demo time so nothing heavier than one indexedSELECTruns on a click, and never calling an AI function on render.

## Hazards, with the errors verbatim

Every Symptom below is something I actually saw.

Hazard

Symptom

Fix

Differential privacy DDL

SQL compilation error: syntax error at position 26 unexpected 'BUDGET'

Retracted. Malformed statement, not a missing feature.
 No 
CREATE PRIVACY BUDGET
 exists; name the budget inside a policy body and attach with 
ADD PRIVACY POLICY
, not 
SET
. Written correctly it attaches and returns noised answers. 
Above.

Privacy domain missing

510242 Aggregate query not supported ... Supported aggregates: COUNT, COUNT_STAR

A column with no declared 
privacy domain
 has an infinite one, and infinite domain needs infinite noise. Declare one on every column. Ranges are 
SET PRIVACY DOMAIN BETWEEN (0, 5000)
, lists are 
IN ('a','b')
, and neither accepts a subquery.

DP over transactional rows

210007 Private tables have an infinite multiplier

A beneficiary holds up to five rows, so one person moves a row count by five. The 
query
 must deduplicate on the entity key: 
COUNT(DISTINCT beneficiary_id)
 passes, 
COUNT(*)
 does not, and a 
GROUP BY
 inside a view is not accepted as proof of one row per entity. 
GROUP BY
 over an unbounded key is refused separately with 
possible groups (infinity) must not exceed 10000
.

AI functions on a trial account

AI function _AI_EMBED_WITH_PROMPT_768 is not available for trial accounts

Account-class, not credits. Embed offline with the same model, load into 
VECTOR(FLOAT, 768)
, keep the search in SQL.

AI_FILTER
 as a join predicate

AI function _AI_FILTER_WITH_PROMPT is not available for trial accounts

Two predicates over already-computed columns, with 
confirmation_method = 'HEURISTIC'
 on every row so the substitution is in the data.

QUALIFY
 over the cosine

found QUALIFY clause but no window function

A CTE, the better shape anyway: it stops the cosine evaluating twice per pair.

H3_GRID_DISTANCE
 across continents

Error trying to compute the path between cells

H3_TRY_GRID_DISTANCE
 returns 
NULL
, and here that is the 
wrong
 fix: 
NULL > max_hops
 is 
NULL
, the 
CASE
 falls through to 
PLAUSIBLE
, and the delivery is silently cleared. Compare resolution-0 parents and assign a sentinel above every 
max_hops
.

Edition assertion

CURRENT_EDITION()
 is an unknown function on this deployment

Establish it by behaviour: set 90-day retention and create an aggregation policy in a scratch database, then drop it.

External access from a UDF

509009: External access is not supported for trial accounts

Do not invert the arrow. The bridge polls inward, and a signing key has no business in a warehouse anyway.

Secondary roles

CURRENT_ROLE()
 says 
GP_ANALYST
 while 
ACCOUNTADMIN
 is live underneath

USE SECONDARY ROLES NONE
, and move the object to a schema the role has no 
USAGE
 on.

Compressed NFT leaf parse

Could not parse leaf from transaction
, about one mint in fourteen

Confirm at 
finalized
, then retry the parse with backoff. Without it a full run loses three hundred receipts.

devnet SOL

public faucet 
429 Too Many Requests
, Helius 
403 Forbidden
, fresh keypairs too

The limit is keyed to the IP, not the address. 
devnet-pow
 finds a faucet paying 0.02 a solve, but claiming is an ordinary transaction, so a wallet with 0 SOL cannot pay the fee to collect the SOL that pays the fee. 0.01 from anywhere breaks it.

Streamlit in Snowflake CSP

a Geist 
@font-face
 from a CDN silently falls back to a system font

base64-inline the woff2 faces into a committed stylesheet. No error to catch; it just looks slightly wrong.

pydeck renders blank

no error, no tiles

Accept 
External Offerings Terms
 in Snowsight in the first ten minutes. 
st.pydeck_chart
 draws Carto tiles, a third-party offering.

The one that cost the most was not on this list.Cloud platform, region and edition are chosen at Snowflake signup and cannot be changed afterwards.Picking Standard makes aggregation policies and 90-day Time Travel permanently unavailable on that account, and the only remedy is a new trial. That is whysql/00_account_setup.sqlprobes for both in its first statements: you want to learn that in minute one, not at hour eleven.

## What's real and what's simplified

On the corpus size, the first thing to check: 45,400 organisations out of947,547 rows availablein the BMF. Embeddings were generated offline on one laptop afterAI_EMBEDturned out to be blocked, and 45,400 vectors is what fits in a weekend. None of the SQL changes at full scale, and the pre-filter getsmoreselective as the corpus grows, not less. The evaluation above already runs at 2.9 million pairs.

Real and running:45,400 IRS Business Master File organisations, 44,101 verified and 899 no longer in good standing. Genuinesnowflake-arctic-embed-mvectors in aVECTOR(FLOAT, 768)column, all similarity search in Snowflake. Six Dynamic Tables at 60-second lag. Five H3 functions plusST_DISTANCEover 9,716 delivery events in 40 districts. A decomposable SQL UDF over 45,400 rows reconciling to zero hand-edited rows. Two governance policies over the same facts,MIN_GROUP_SIZE => 50and a 0.1 epsilon budget, both with an entity key Snowflake enforces against the analyst role. A semantic view read withDESCRIBE, 90-day Time Travel, 285 confirmed devnet receipts, a ten-section Streamlit app inside the warehouse, and the 2.9-million-pair evaluation above.python tools/acceptance.pyreports36 passed, 0 failedwith no account and no network.

Simplification

Why

Honest label

Every impersonating organisation is generated

Naming a real charity as a suspect on a cosine distance is the exact error this project criticises

batch_id = 'SYNTH_ADVERSARY_V1'
, 
is_synthetic = TRUE
, a visible chip, and checks 
INT-01
/
INT-02
 that fail the build if a real organisation appears flagged

Every beneficiary record is generated

Real beneficiary data in a weekend project would be unethical

Same batch id. 8,113 rows, none a person.

Individual delivery events are modelled

No public per-event aid delivery feed exists

The 
aggregate
 is calibrated: 63.31% delivered by value against WFP's 62.88%, checked by 
DAT-06

Embeddings generated offline

AI_EMBED
 blocked on trial accounts

Same model. The similarity search did not move; only the machine that produced the vectors did.

Clone confirmation is two SQL predicates

AI_FILTER
 blocked on trial accounts

confirmation_method = 'HEURISTIC'
 on all 188 confirmed rows, rendered in the interface

Two privacy regimes, and the budget on one of them is set too high

I called the DP DDL unavailable on two malformed statements, shipped the cohort floor alone, then set the budget above the cost of the attack it defends against. See above.

The floor refuses any aggregate under fifty beneficiaries but adds 
no noise and has no budget
, so two large queries can be differenced. The budget noises everything and never refuses, but 
BUDGET_LIMIT => 300
 permits 3,000 queries where the attack needs about 660. Both are on The Wall with the arithmetic.

Receipts go to devnet, bridge is centralised

An attestation 
bridge
, not a decentralised oracle network

Stated on the tab; every explorer link names the cluster (
DAT-05
)

285 receipts against 5,024 eligible rows

The devnet wallet ran out and the airdrop is IP-rate-limited

Drawn as a step, called a migration, uncovered band still shown as the finding

79 disbursements have two receipts

A read-back not scoped to the rows the caller claimed

Diagnosed above, code quoted, not fixed in this submission

One in thirty eligible disbursements is withheld from the queue

So the missing-receipt finding is genuine rather than staged

MOD(ABS(HASH(disbursement_id)), 30) <> 0
 in 
sql/13_oracle_queue.sql

Affiliate structures are not handled

Not modelled, and not visible until the detector met the real corpus

74% of real-corpus firings are two national bodies' chapters. Quantified above, not fixed.

The corpus is 45,400 of 947,547 available

Offline embedding on one laptop inside the challenge window

Stated here and on The Brief; the SQL is unchanged at full scale

Two more, because leaving them out would be the thing this post is against.

The Auto-Revocation List is not a fraud list.It is overwhelmingly a record of organisations that failed to file for three consecutive years, and reinstated organisations are excluded here. This project calls those organisationsno longer in good standingand neverfraudulent. Mislabelling it would be exactly the sloppy inference the whole build exists to criticise.

One acceptance check is checking the wrong directory.SEC-keysasserts that no keypair file is present in the working tree, and it looks only insidekeys/. The devnet authority keypair lives at the repository root asauthority.json. It is in.gitignorefrom the first commit and has never been committed, which is why nothing leaked, but the check that would have caught it if it had was passing for the wrong reason. A green check that verifies the wrong path is worse than no check, because it buys confidence it did not earn. That is the same failure this project describes in the sector it is about, arriving in my own test suite.

## What this unlocks

Charity is the costume. Underneath is a primitive worth stealing:compute a score whose components are stored beside it, attach a governance policy the platform enforces rather than the application, and publish a claim rather than the data behind it.

Impersonation is a distance. So is brand abuse, so are counterfeit listings, and so is invoice fraud: a supplier name that means what the real one means, spelled differently enough to clear a string match. All of them are currently caught badly by thresholding an edit distance. All of them are aVECTOR_COSINE_SIMILARITY, aJAROWINKLER_SIMILARITY, and the subtraction between them.

And the half that is not detection:an accountability claim living only in the accountable party's database is not accountability.Proof of reserve, carbon retirement, supply-chain attestation, aid delivery, each an "aggregate privately, attest publicly" problem currently solved by a report the interested party writes about itself. Publish the claim, not the data, then let the ledger tell you where your own bookkeeping is wrong, which in my case took four seconds.

## One last thing, about the 159

The Comptroller and Auditor General of India audited PMAY-Gramin in Uttar Pradesh and found 86.20 lakh rupees, intended for159 genuine beneficiaries, diverted to other bank accounts.

Until the last edit of this post that was a row in a table. The word doing the work isgenuine. Those 159 households were not fraudulent claimants. They applied, they qualified, they were approved, and they are on the list as approved. Somebody changed an account number. The audit is the only reason anybody knows, and it was tabled in December 2025 for money that moved long before.

Nothing here would have stopped that. The detector is aimed at the fundraising side, this happened on the disbursement side, and a receipt proves a claim was recorded rather than that a house was built. What a receipt does is smaller: it makes the gap legible while it is open rather than after it is closed. Today the distance between a payment being approved and somebody noticing it went elsewhere is measured in audit cycles, and the person who most needs to know has the least ability to find out. A public record carrying a programme code, an amount band and a delivery window names nobody and needs permission from nobody.

Generosity does not fail because people stop giving. It fails because giving and knowing are two different actions, and only one of them has ever been easy. Everything above is machinery for making the second one cheaper.

## FAQ

### How do you detect a charity impersonating another charity when the names are deliberately different?

Compare meaning and spelling separately, then subtract.VECTOR_COSINE_SIMILARITYover aVECTOR(FLOAT, 768)column gives meaning;JAROWINKLER_SIMILARITYgives spelling. An impersonator maximises the first and minimises the second on purpose, so the gap is the signal. At 0.94 this corpus gives 97.8% precision, 67.5% recall.

### Why doesVECTOR_COSINE_SIMILARITYneed a pre-filter?

Vector similarity performs an exact scan, so an unfiltered self-join is a full cross product: 45,400 squared is 2,061,160,000 pairs in one query. Pre-filtering on H3 region and cause brings it to 62,247. If a similarity query starts running long, the pre-filter has been weakened.

### Which Snowflake features are blocked on a trial account?

Every AI function and all external network access.AI_EMBEDreturnsAI function _AI_EMBED_WITH_PROMPT_768 is not available for trial accounts,AI_FILTERreturnsAI function _AI_FILTER_WITH_PROMPT is not available for trial accounts, andSNOWFLAKE.CORTEX.COMPLETE,EMBED_TEXT_768,EMBED_TEXT_1024andSENTIMENTsay the same. It is an account-class restriction, not credit exhaustion, so neither waiting nor a grant helps. Separately, any outbound call from a UDF fails with509009: External access is not supported for trial accounts. Embed offline with the same model into aVECTOR(FLOAT, 768)column, which keeps the search in SQL, and invert the arrow so the external process polls into Snowflake.

### How do you check a Snowflake account's edition from SQL whenCURRENT_EDITION()is not a function?

There is noCURRENT_EDITION(), andSHOW ACCOUNTSneeds an ORGADMIN role you may not have on a trial. Establish it by behaviour: in a scratch database setDATA_RETENTION_TIME_IN_DAYS = 90and read it back, then create an aggregation policy and drop it. Both are Enterprise-gated, so if both succeed the account is Enterprise or higher. Do it in minute one, because platform, region and edition are fixed at signup and cannot be changed.

### Why doesUSE ROLEnot actually switch role in Snowflake?

It switches the primary role, butDEFAULT_SECONDARY_ROLES = ('ALL')keeps every other role the user holds, and privilege checks run against the union.CURRENT_ROLE()reports what you asked for whileACCOUNTADMINis live underneath. AddUSE SECONDARY ROLES NONEwhen testing a constrained persona, and put anything it must not read in a schema it has noUSAGEon.

### Does a blockchain receipt prove aid reached a person?

No, and anyone telling you otherwise is selling something. It proves a claim was recorded at a point in time and has not been edited since. That is genuinely useful, because the alternative is a record held by an interested party, and it is much smaller than the property usually advertised.

## Run it yourself

git clone https://github.com/SoumyaEXE/GLASSPOCKET

cp
 .env.example .env 
# Snowflake creds, devnet keypair path

pip 
install
 
-r
 requirements.txt 
&&
 npm 
install

python tools/make_synthetic.py 
--all
 
# real corpus in, seeded adversaries out

python tools/embed_offline.py 
# arctic-embed vectors, once

python tools/deploy.py 
--check
 
# connect and report, change nothing

python tools/deploy.py 
--all
 
# provision, stage, load, verify

cd 
bridge 
&&
 npm run tree 
&&
 npm run start 
# queue -> signed devnet receipts

python tools/deploy_app.py 
# the dashboard, into the warehouse

Enter fullscreen mode

Exit fullscreen mode

python tools/acceptance.pyruns all 36 offline checks with no account and no network: labelling contract, score reconciliation, geometry distribution, WFP calibration, interface language, security.python tools/smoke_test.pyrenders every section headlessly.

tools/deploy.pynever prints a credential, and statements marked-- EXPECT_FAILaresupposedto be refused: the row-levelSELECTinsql/11proves the policy is protecting the view, and a build where it succeeds is the broken one.

## References

1. FBI IC3 (16 Jan 2025).Public Service Announcement I-011625.
2. BforeAI, Los Angeles wildfire domain research (Jan 2025).
3. World Food Programme,State of Palestine External Situation Report 55(6 Jun 2025).
4. Ministry of Rural Development, India, MGNREGA action report (29 Mar 2025).
5. Comptroller and Auditor General of India, PMAY-Gramin audit, Uttar Pradesh (Dec 2025).
6. IRS,Exempt Organizations Business Master Fileand Auto-Revocation List.
7. IATI Datastore.
8. Metaplex,Bubblegum compressed NFTs; SPL Account CompressioncmtDvXumGCrqC1Age74AVPhSRVXJMd8PJS91L8KbNCK.

Built within the challenge window with@dronzer2codeand AI pair programming. Every impersonating organisation and every beneficiary record in this project is generated and labelled in the data, not only on screen. Real organisations appear only as the target of an impersonation, never in a flagged state. GLASSPOCKET makes no accusation about any real entity, and the Auto-Revocation List records a failure to file, not wrongdoing.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse