---
title: GitHub - withmarbleapp/os-taxonomy · GitHub
url: https://github.com/withmarbleapp/os-taxonomy
site_name: github
content_file: github-github-withmarbleappos-taxonomy-github
fetched_at: '2026-10-19T17:20:34.419269'
original_url: https://github.com/withmarbleapp/os-taxonomy
author: withmarbleapp
description: Contribute to withmarbleapp/os-taxonomy development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

21 Commits
21 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
data
data
 
 
media
media
 
 
schema
schema
 
 
scripts
scripts
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
LICENSE
LICENSE
 
 
LICENSE-CONTENT
LICENSE-CONTENT
 
 
PROVENANCE.md
PROVENANCE.md
 
 
README.md
README.md
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# Marble Skill Taxonomy

An open, structured taxonomy ofwhat children learnacross the primary/elementary years — decomposed into fine-grained "micro-topics", wired into a prerequisite graph, and aligned to national curriculum standards. Produced byMarble.

Version:v1·Topics:1,591 ·Prerequisite edges:3,225 ·Subjects:8

## See it

Every dot is a micro-topic, colored by subject; height is age; each thread is a prerequisite (full-quality video). Explore it interactively atwithmarble.com/curriculum— tap any concept to trace everything a learner must master before it.

## What this is

Most curriculum data is either a flat list of standards or locked inside a product. This dataset is aconnected graph of learning:

* 1,591 micro-topics— a single, teachable idea (e.g."Building sentences","Apparent brightness of stars"), each with a plain-language description, masteryevidencecriteria, a type (conceptual / procedural / representational / language / meta), a subject + domain, and an approximate age range.
* 3,225 prerequisite dependencies— a directed acyclic graph:"topic X depends on prerequisite Y", each edge taggedhard/softand carrying a one-linereason.
* Curriculum alignment— each micro-topic links to the standards it was distilled from (NGSS, Common Core, the UK National Curriculum, and more).
* Teaching research— 1,051 records covering the current Science and Mathematics topics: teaching approaches, concrete learning activities, feedback, assessment guidance and linked sources. Coverage is partial; the other 540 topics have no research in this release.
* Domain clusters— 176 parent-friendly one-paragraph summaries per (subject, domain, age band).

### Subjects

Subject

Topics

Science

547

Mathematics

504

English

286

History

90

Personal & Social Development

88

Life Skills

37

Computing

21

Learning to Learn

18

## Files

All data lives indata/as UTF-8 JSON. Seeschema/for JSON Schemas andmanifest.jsonfor counts + SHA-256 checksums.

File

What it holds

data/topics.json

The micro-topics (graph 
nodes
).

data/dependencies.json

Prerequisite 
edges
 (
topicId
 depends on 
prerequisiteId
).

data/curriculum-standards.json

The source curriculum standards, grouped by curriculum.

data/clusters.json

Parent-friendly domain summaries.

data/teaching-research.json

Teaching research joined by 
topicId
, with explicit coverage and publication notes (~24 MB).

data/manifest.json

Counts, per-subject breakdown, per-file checksums.

### A topic

{
 
"id"
: 
"
mt_N8CpN1EJrP
"
,
 
"type"
: 
"
CONCEPTUAL
"
,
 
"subject"
: 
"
English
"
,
 
"domain"
: 
"
Grammar & Punctuation
"
,
 
"name"
: 
"
Building sentences
"
,
 
"description"
: 
"
Understand that words combine to make sentences — a sentence expresses a complete thought…
"
,
 
"ageRangeStart"
: 
4
,
 
"ageRangeEnd"
: 
6
,
 
"centrality"
: 
0.257
,
 
"evidence"
: [
 
"
Distinguish between complete sentences and fragments
"
,
 
"
Compose a complete sentence with a subject and verb
"

 ],
 
"assessmentPrompt"
: 
"
If {{name}} says something like 
\"
The dog
\"
, can they tell you that's not a complete sentence…?
"
,
 
"standards"
: [
"
ccss-ela:L.K.1f
"
, 
"
uk-nc-2013:Eng.App2.Y1.Sent.1
"
]
}

* id— stable identifier (mt_…), referenced by dependencies and by neighbours.
* standards— keys intocurriculum-standards.json("<curriculum-slug>:<code>").
* assessmentPrompt— a natural-language check for the idea. Contains a{{name}}placeholder (the child's name); substitute or strip before display.

### A dependency

{ 
"topicId"
: 
"
mt__00ZSLnB7p
"
, 
"prerequisiteId"
: 
"
mt_VBl1T1sFCM
"
, 
"strength"
: 
"
hard
"
,
 
"reason"
: 
"
Must understand vibrations make sound before finding volume patterns
"
 }

topicIddepends onprerequisiteId. Reverse the edge to get "unlocks".

## Teaching research

data/teaching-research.jsonaddshow a topic
might be taughtto the graph of what children learn. It covers547 Scienceand504 Mathematicstopics.coverage.missingTopicIdsand per-subject counts
make the540 topics without researchexplicit; absence is not a judgement
about whether a topic can be taught.

The file hasschemaVersion: 1and taxonomyversion: "v1". Eachrecords[]entry joinstopics.jsonthroughtopicIdand contains:

Field

Meaning

pedagogy

Original teaching summary, practices, representations and misconceptions.

learn

Portable learning guidance (
schemaVersion: 2
): a summary, activities, educational constraints and review notes.

learn.activities[]

Learner actions, intended insight, feedback, rationale and supporting source claims. No product artifact types or fit rankings.

assess

Original diagnostic/task, response levels, error patterns and next teaching moves; nullable in the public interface.

sources

Claim, named source, optional URL and the original author's verification flag.

confidence

Original authoring confidence; not an independent quality score.

provenance

Original authoring model and source record timestamps. The update timestamp also reflects the learning-guidance rewrite.

publicationNotes

Paths and curriculum codes for text omitted under the codes-only publication policy.

sourceClaimsexactly matchsources[].claimafter publication transformations.
A source may support a general principle or curriculum alignment; this does not
mean the proposed activity was tested. Some activities have no directly linked
source claim.

These records were agent-authored. The learning guidance was rewritten for
portability, checked by a separate factual critic, and sampled by a second agent.
Most original pedagogy and assessment were retained and may contain claims that
the updated guidance qualifies; chart-specific alignment repairs after #30 are
recorded in the affected learning-guidance review notes; read the constraints and review notes alongside
them. Sources werenot re-fetched or re-verifiedfor this release. Historicalverified: trueandconfidence: "high"are not new evidence ratings. Activities
are research-informed proposals,not empirically validated interventions.

Some original research quoted restricted curriculum standards. Matched passages
are replaced with inline curriculum references, including inside citation claims;
all transformed paths are listed inpublicationNotes. This is a conservative
mechanical omission pass, not comprehensive rights clearance. Consult the linked
upstream sources for their wording and terms. SeePROVENANCE.md.

After the chart split in#30,mt_bESTSBB0wKcovers pie charts,mt_H6LlpWgEYScovers earlier line-graph
problem-solving, andmt_HlNSurPVDphas a separate construction-and-interpretation
record. The new record adapts existing graph research; it is not a fresh
literature review, and all reused source-verification flags are false. Its
assessment requires a complete constructed graph. The later grouped-charts
assessment routes graph-choice errors to data presentation and sector-angle
errors to pie charts.

The file is bound to the exacttopics.jsonbytes throughtopicFileSha256.
Regenerate the research projection when the canonical topic file changes, even
when topic IDs remain stable.

## Using it

Pure data — no runtime, no dependencies. Load the JSON and go.

import
 
topics
 
from
 
'./data/topics.json'
 
with
 
{
 
type
: 
'json'
 
}
;

import
 
deps
 
from
 
'./data/dependencies.json'
 
with
 
{
 
type
: 
'json'
 
}
;

const
 
byId
 
=
 
new
 
Map
(
topics
.
topics
.
map
(
t
 
=>
 
[
t
.
id
,
 
t
]
)
)
;

const
 
prereqs
 
=
 
deps
.
dependencies

 
.
filter
(
d
 
=>
 
d
.
topicId
 
===
 
'mt_N8CpN1EJrP'
)

 
.
map
(
d
 
=>
 
byId
.
get
(
d
.
prerequisiteId
)
.
name
)
;

Join teaching guidance to a topic:

import
 
research
 
from
 
'./data/teaching-research.json'
 
with
 
{
 
type
: 
'json'
 
}
;

const
 
guidanceByTopic
 
=
 
new
 
Map
(
research
.
records
.
map
(
r
 
=>
 
[
r
.
topicId
,
 
r
]
)
)
;

const
 
guidance
 
=
 
guidanceByTopic
.
get
(
'mt_N8CpN1EJrP'
)
;
 
// undefined: English is not covered yet

const
 
activities
 
=
 
guidance
?.
learn
.
activities
 
??
 
[
]
;

Validate structure, research coverage, evidence links and checksums:

node scripts/validate.mjs
node --test scripts/teaching-research.test.mjs

## License

This dataset ismulti-licensed— read this before you use or redistribute it.

Layer

License

The database
 — the collection, structure, IDs, topic↔topic and topic↔standard relationships

ODbL 1.0
 — free for research 
and
 commercial use, 
attribution
 required, 
share-alike
 (derivative 
databases
 must stay open under ODbL).

The textual content Marble authored
 — topic 
description
/
name
/
evidence
/
assessmentPrompt
, dependency 
reason
s, cluster 
summary
s, original teaching-research prose

CC BY-SA 4.0
 — same spirit: attribution + share-alike.

curriculum-standards.json
 — extracted from third-party frameworks

Not
 Marble's to relicense. Each source is under 
its own upstream license
 — see 
PROVENANCE.md
.

Why share-alike + still commercial-friendly:ODbL distinguishes aderivative database(extend/modify the taxonomy → must stay open) from aproduced work(use it inside a product, model, or app → stays yours). So you can build a commercial product on this without open-sourcing your product; you only owe back improvements to thetaxonomy itself.

### Attribution

Any use must credit:

Marble Skill Taxonomy (v1) · © Generative Spark, Inc. (Marble) ·https://withmarble.com· licensed under ODbL 1.0 (database) and CC BY-SA 4.0 (content).

Plus the upstream notices inPROVENANCE.mdfor any curriculum standards you use. SeeCITATION.cfffor a formal citation.

## What'snothere

Deliberately excluded from this release: semantic embeddings (derived, recomputable) and any per-child / user data (never published). SeeCHANGELOG.md.