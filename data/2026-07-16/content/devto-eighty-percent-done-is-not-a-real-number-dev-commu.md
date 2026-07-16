---
title: Eighty Percent Done Is Not a Real Number - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/eighty-percent-done-is-not-a-real-number-54nf
site_name: devto
content_file: devto-eighty-percent-done-is-not-a-real-number-dev-commu
fetched_at: '2026-07-16T19:29:49.602840'
original_url: https://dev.to/pascal_cescato_692b7a8a20/eighty-percent-done-is-not-a-real-number-54nf
author: Pascal CESCATO
date: '2026-07-15'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. Why this... Tagged with devchallenge, bugsmash, postgres, database.'
tags: '#devchallenge, #bugsmash, #postgres, #database'
---

Summer Bug Smash: Smash Stories Submission 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

## Why this one, and why now

I always have several projects running in parallel — a maintenance CRM for tradespeople, a SaaS platform for restaurants, an automated newsletter, a management tool for training organizations… Except for that last one, none of them was ready to sell. And I have a whole pile of projects left "as is," untouched for months. An SEO scanner, a document analyzer, a mailbox scanner, a SQL audit tool, and others.

Brainstorming session with Claude, my favorite AI assistant — we went through my repos: the CRM for heating tradespeople, the restaurant platform, the bilingual newsletter, and this SQL audit folder, several months old. The point of the session was to decide. I wanted to finish something quickly and start promoting it. Each project had a state of progress, a level of uncertainty, a distance to something sellable.

The CRM still needs weeks of development — just for the features I know are essential — and field feedback from real tradespeople to validate the workflows. The restaurant platform was more of an architecture bet than a finished product. The newsletter has no client waiting for it.

The SQL audit, though, looked done. Two.sqlfiles, aUNION ALLof tenSELECTstatements per engine, a bash script pushing that topsqlormysqland converting to JSON, a PDF generator for a professional presentation. But I doubt I'd ever actually run it.

It was a forgotten project. A PoC — it looked like a finished application, it wasn't one.

The apparent distance to a sellable service looked like the shortest on the whole list: no UI needed, no architecture to rethink, just a script to test, improve, and stabilize. It was this single head start — more than any technical interest in the project — that tipped the scale. Its illusory proximity to the finish line.

## The PoC that was supposed to work

Before touching a single real database, I asked four different models for a code review — DeepSeek, Big Pickle, GLM, Qwen. Each produced a detailed report: bugs, dependencies, a phantom call to an LLM for the whole write-up section. Useful. But all four converged on the same blind spot:

None of the four had tried running the script against a MySQL or PostgreSQL database.

They were reading SQL. Not its behavior. And that blind spot, shared by four independent models, confirmed exactly the wrong conclusion: that the project was closer to done than it actually was.

## What the first real database showed in three lines, and what it cost the schedule

First run against a vanilla PostgreSQL 16, without thepg_stat_statementsextension:

[{
"metric"
:
"psql:...audit_all_postgres.sql:193: ERROR: relation 
\"
pg_stat_statements
\"
 does not exist"
...
}]

Enter fullscreen mode

Exit fullscreen mode

Three lines. Nothing else. A single query on a missing extension had killed the entireUNION ALL— the other nine metrics never got a chance to run.

The starting estimate — "this is the closest-to-finished project" — had just taken a hit. Not fatal, but real: what was supposed to be a wrap-up session turned into a series of discovery sessions. The good news, in hindsight, is that the remaining distance was still shorter than for the other two projects in the running. The bad news is that it had nothing to do with the distance estimated at the start.

The same pattern repeated on every database tested: a missing system table or an insufficient privilege would kill the entire script, instead of just skipping the one affected metric.pg_authidinaccessible without superuser,mysql.userwithout the right GRANT,column_statisticsmissing on MariaDB — same symptom every time.

Fix, every time: check access before querying, returnUNAVAILABLE: <reason>on failure, let the rest of the script continue. Simple in theory.

### The trap I didn't know about

One of the fixes looked trivial:

CASE
 
WHEN
 
NOT
 
EXISTS
 
(
SELECT
 
1
 
FROM
 
pg_extension
 
WHERE
 
extname
 
=
 
'pg_stat_statements'
)

 
THEN
 
NULL

 
ELSE
 
(
SELECT
 
COUNT
(
*
)
 
FROM
 
pg_stat_statements
)

END

Enter fullscreen mode

Exit fullscreen mode

It looks correct. It isn't.

Caught in production, not in review: PostgreSQL validates the existence ofpg_stat_statementsat query-parsing time, not when theCASEbranch actually executes. The conditional check protects nothing — the query fails before it even knows which branch would be taken.

That logic had to move out of static SQL and into the bash script, with a separate, upfront detection query. ACASEthat was syntactically flawless and semantically useless. None of the four reviews had caught it — it took a real engine to make it fail.

## The bug that had nothing to do with a privilege

The longest one to isolate:roles_without_passwordkept coming backUNAVAILABLEdespite confirmed GRANTs, twice, on two different accounts,SHOW GRANTSoutput in hand.

It wasn't a permissions problem. It was a string-formatting problem. The check comparedGRANTEE— as stored ininformation_schema.SCHEMA_PRIVILEGES, formatted'user'@'host', two pairs of quotes — against a string built withCONCAT("'", USER(), "'"), which produces'user@host', a single pair of quotes around the whole thing. The two strings could never match, and the failure looked exactly like the thing you fear most in an audit tool: a false negative on security.

Second trap, dumber still: the MySQL script never asked the user for a database name, unlike the PostgreSQL flow, which had that prompt from the start. With no database selected,DATABASE()returnsNULL, and anyTABLE_SCHEMA = DATABASE()condition matches nothing at all.

Result:bloated_tablescame back as 0 on a table whose bloat had been independently measured and confirmed at 23% outside the script.

Zero didn't mean "no bloat." Zero meant "no rows found, because the question asked didn't correspond to anything."

That's the kind of error an audit tool must never produce silently: a reassuring zero that measured nothing. This was no longer a question of distance to the finish line. It was a question of direction — I thought I was heading toward a finished script, I was heading toward ground I had never actually seen.

## A metric that didn't measure what its name promised

buffer_pool_ratio—innodb_buffer_pool_size / max_connections— came back as 1,789,569.7067 on a real database. A ratio has no business exceeding 1.

The calculation had no bug; it simply never made sense. Dividing a memory size in bytes by a theoretical maximum connection count doesn't produce any intelligible unit — it's neither a ratio, nor a per-connection allocation, nor a saturation indicator. Four code reviews had nothing to say about it, because nothing about it was syntactically wrong.

Replaced by the buffer pool hit rate —1 - (Innodb_buffer_pool_reads / Innodb_buffer_pool_read_requests)— which measures something real: the proportion of reads served from memory cache rather than disk. On the same database: 99.75%. A number that means something.

## Ten metrics didn't cover everything — not even the essentials

Once the pipeline was stable on the original ten metrics, the report generated against n8n's production database was coherent — ten measurements, one score, nothing inconsistent in the results. It was in submitting that report to another LLM, for a second look, that the gap showed up: nothing in those ten metrics measured connection encryption.

It wasn't a test that revealed the hole. It was a re-read. The LLM proposed exactly one additional metric —ssl_enforced— and adding it was enough to change the priority order of the risk matrix and the final score. Oncessl_enforcedwas in, the lack of encryption on the n8n database jumped to the top of the risk matrix, ahead of everything the original ten metrics had found.

Three more followed, separately, proposed by Kimi from a broader list of candidates ranked by ease of implementation.connection_count_ratio,unused_indexes,long_running_transactionswere kept precisely because they fit the existing model without complicating it — one query, one value, the same defensive pattern as the rest of the script. Other ideas from the same list were dropped:disk_usage_growth_ratewould have required historical snapshots, changing the nature of a tool built for point-in-time audits;table_countanddatabase_sizewere just display context, not a risk signal.

None of the four new metrics is complex to collect — one query each, on both engines. But none was in the original list, because that list had been built around performance and schema hygiene, not exposure surface. It took an outside eye re-reading the result, not the code, to make that gap visible.

A third pass, this time by Mistral, focused on how the report was presented rather than on its content, and raised two separate points:duplicate_primary_keys = 0— a positive result — stayed buried in a prose paragraph in the middle of the overall assessment, never showing up in a proper, systematic checklist table covering every metric, including the ones with no issue. And the penalties, already grouped by category internally in the score calculation, were never exposed separately in the final report. Two last metrics followed from that pass —duplicate_indexes,large_tables_count— kept after checking they didn't duplicate anything already there.

## The count

Metric

Before

After

Metrics per engine

10

16

Behavior on missing privilege

entire script stopped

UNAVAILABLE: <reason>
, the rest continues

Scoring

none

deterministic, broken down by category (security / performance / integrity)

SSL/TLS detection

none

yes — surfaced the #1 risk on a production database

Report languages

1

multilingual, stable section identifiers

Code reviews before the first real run

4 models

4 models, 0 behavioral bugs found

## The coda: debugging the report that describes the bugs

One last, almost ironic detail: at final-render time, the colored dots in the Risk Matrix — red/orange/gray by score — stopped showing up in the PDF. Copilot never found the cause. It churned for three hours, burned through more than $20 in credits on this one task (with Haiku 4.5) — still no colored dot. Big Pickle, in OpenCode, fixed it in under a minute, for free: every one of Copilot's hypotheses was wrong. The only problem was the column it was trying to insert the dot into.

But the real lesson wasn't in the fix — it was in the method: don't attempt a third blind implementation, check and re-read the actual generated code instead of guessing. Same principle as the rest of this project — believe nothing until it has run, once, in a real environment.

## What determinism doesn't cover

Two versions of the same report, on the same database, generated by two different LLMs for the narrative part — the global score, the category scores, the risk matrix: identical to the decimal point, because those numbers never come out of the LLM. That's exactly what deterministic scoring is supposed to guarantee: the model writes, it doesn't grade.

But one of the two reports cited SOC 2 in the business impact of a recommendation. French database, French LLM (Mistral Large), French report — SOC 2 had no business being there. The score hadn't lied. The sentence around it had — but not by pure invention. Mistral didn't fabricate SOC 2 out of nowhere: it's a real framework, consistent with the report's consulting tone, correctly defined in itself. The problem isn't that the model hallucinated a concept — it's that it applied it to a hypothetical place it didn't actually know. A misapplication, not an invention.

Same family of bug asDATABASE()returningNULLon the MySQL side: a field never asked for, silently filled in with whatever seemed plausible. Except this time it wasn't a sloppy query — it was a prompt that never anticipated it might be missing a piece of information as central as the client's country. Except the country doesn't actually matter that much: weak security is weak security, whether you're subject to SOC 2, GDPR, ISO 27001, or any other framework. Deterministic scoring closes the door to improvisation on the numbers. It says nothing about improvisation in the sentence explaining those numbers — and nowhere, in the sixteen metrics or in the generation prompt, does anything ever ask what country the audited database is in. The two numbers stayed identical between the two reports. Only the sentence built on top of them was free to be wrong, fluently, without ever looking wrong.

That's fixed now: a jurisdiction flag precedes every report generation —--jurisdiction FR,--jurisdiction US, or any other ISO 3166 value depending on the client — and the narration prompt is now explicitly forbidden from naming a compliance framework that jurisdiction doesn't justify.

## What it looks like now

What's left, once all of that is behind it: a tool you run from the command line against a MariaDB or PostgreSQL database, that finishes in a few minutes, and produces a complete PDF report — global score, risk matrix, prioritized recommendations, technical appendix — without needing to babysit the run or guess whether the result can be trusted. That object, not the list of bugs that led to it, is what's standing today atdbgrade.tech.

Sixteen metrics per engine, up from ten at the start. Deterministic scoring, broken down by category. Multilingual support where section titles keep a stable internal identifier while their label displays translated. An appendix that names the affected tables and constraints, not just their count.

You can see what it looks like on SlideShare:

fr.slideshare.net

None of this was planned at the start. The two-file SQL PoC did exactly what it said it would, as long as no one ran it anywhere other than the imagination of the person who wrote it (yes, that was me, but let's not dwell on it).

This project was picked because it looked closest to the finish line. It was, in the sense that the remaining distance ended up being covered faster than for the other projects waiting in line. But that proximity, likebuffer_pool_ratio, had never actually been verified — only estimated, from code that compiled and hadn't crashed yet. It kept correcting itself with every bug found, right up to the last one, SOC 2, discovered after everything else already looked finished.

A script that never crashes proves nothing.buffer_pool_rationever failed anything — it ran, it produced a number, and that number meant nothing. No amount of re-running would have shown that: it took comparing the result against a measurement taken elsewhere, by another method, to see the calculation was hollow. Same story forbloated_tablesreturning 0 on a table whose bloat was confirmed at 23% outside the script — a zero that runs without error isn't a correct zero. And the same story, further upstream, for "this project is the closest to done": an estimate that held up right until someone checked it, and not a moment longer.

The difference between a tool that works on paper and one that holds up against a real database isn't the sophistication of the code, and it isn't the number of times you managed to make it crash either. It's whether every result it produces — including the estimate that justified starting the project in the first place — corresponds to something actually verified, not merely plausible.

## Technical sidebar — tools and method

Initial code review (before any real run):DeepSeek, Big Pickle, GLM, Qwen — four models, four reports, one shared blind spot: no access to a real database.

Engines tested:PostgreSQL 16 (vanilla, then with extensions), MariaDB.

Bugs found only under real conditions:

1. pg_extensionvalidated at parse time, not when theCASEbranch executes
2. GRANTEEformat mismatch betweeninformation_schemaandCONCAT(USER())
3. DATABASE()returningNULLfor lack of a database-selection prompt on the MySQL side
4. buffer_pool_ratiometric with no basis (a division with no real relationship)
5. Total absence of SSL/TLS detection from the original metric list
6. A compliance framework (SOC 2) cited without any jurisdiction provided or verified

Report generation:Markdown → PDF via WeasyPrint, deterministic scoring kept separate from LLM narration, risk dots in pure CSS (<span>+border-radius), a 3-level palette (red/orange/gray — never green, because no line in the Risk Matrix is good news).

Debug method retained:before retrying an implementation, check the code and what it actually produces, rather than attempting a blind fix based on a description of the symptom.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse