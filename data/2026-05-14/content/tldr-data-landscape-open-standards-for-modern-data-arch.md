---
title: Data Landscape — Open Standards for Modern Data Architecture
url: https://www.data-landscape.com/
site_name: tldr
content_file: tldr-data-landscape-open-standards-for-modern-data-arch
fetched_at: '2026-05-14T11:37:19.479596'
original_url: https://www.data-landscape.com/
author: Dr. Simon Harrer
date: '2026-05-14'
published_date: '2026-04-28T00:00:00+02:00'
description: An opinionated, interactive map of the open standards that power a modern data architecture — ODCS, ODPS, OSI, OpenAPI, Iceberg, OpenLineage, OpenTelemetry and more. Curated by Entropy Data.
tags:
- tldr
---

Open Standards

# Data Landscape

Anopinionated, interactive map of theopen standards.

The open standards that power a modern data architecture, organised by what they describe.
 Inspired by theCNCF Landscapeand theThoughtWorks Tech Radar,
 andSimon's talk on open standards.
 Click any standard to learn more, ordownload as PDF.

Adopt

Situational

Assess

Caution

 Single-vendor specs are muted
 

×

Landscape

Radar

Table

## Definition — how data is described

Contracts

Adopt

🏅

ODCS

BITOL @ LF

Adopt

OpenAPI

LF

Adopt

AsyncAPI

LF

Adopt

GraphQL

LF

Situational

gRPC

CNCF

Situational

OData

OASIS

Data Products

Adopt

🏅

ODPS

BITOL @ LF

Assess

DPDS

ODM

Assess

ODPS

LF

Assess

DPROD

OMG

Schema

Adopt

XML Schema

W3C

Adopt

JSON Schema

IETF

Adopt

SQL DDL

ISO/IEC

Adopt

AVRO Schema

ASF

Adopt

Protobuf

Google

Assess

LinkML

LinkML

Assess

Table Schema

Frictionless

Semantics

Situational

RDF/OWL

W3C

Situational

DCAT

W3C

Situational

SKOS

W3C

Situational

SHACL

W3C

Situational

JSON-LD

W3C

Assess

🏅

OSI

OSI Initiative

Assess

schema.org

W3C

Assess

ShEx

W3C

## Storage — where data lives

File Formats

Adopt

CSV

IETF

Adopt

JSON

IETF

Adopt

XML

W3C

Adopt

YAML

YAML.org

Adopt

PARQUET

ASF

Adopt

AVRO

ASF

Situational

ORC

ASF

Assess

Lance

Lance

Open Table Formats

Adopt

Iceberg

ASF

Situational

Delta

LF

Assess

Hudi

ASF

Assess

Lance

Lance

Storage Systems

Adopt

S3

AWS

Caution

HDFS

ASF

## Movement — how data flows between systems

Database Connectivity

Adopt

JDBC

JCP

Adopt

ODBC

ISO/IEC

Adopt

ADBC

ASF

Caution

XMLA

Microsoft

Interconnection

Adopt

HTTP

IETF

Situational

Delta Sharing

LF

Caution

FTP / SFTP

IETF

Messaging

Adopt

Kafka

ASF

Adopt

CloudEvents

CNCF

Situational

MQTT

OASIS

Situational

AMQP

OASIS

Caution

JMS

Jakarta EE

## Transformation — how data is processed and reshaped

In-Memory Format

Adopt

DataFrame API

data-apis

Adopt

Apache Arrow

ASF

Processing

Adopt

Spark

ASF

Adopt

Pandas

NumFOCUS

Adopt

SQL DML

ISO/IEC

Adopt

dbt

dbt Labs

Situational

Beam

ASF

Assess

Ibis

Ibis

Caution

XSLT

W3C

## Discovery — how data is found and traced

Catalog APIs

Adopt

Iceberg Catalog

ASF

Adopt

Schema Registry

Confluent

Situational

Unity Catalog

LF

Assess

DuckLake

DuckDB Labs

Caution

Hive Metastore

ASF

Lineage

Adopt

OpenLineage

LF

Assess

PROV

W3C

## Operations — how data is queried, observed, governed

Query

Adopt

SQL

ISO/IEC

Situational

Substrait

LF

Situational

SPARQL

W3C

Situational

GQL

ISO/IEC

Caution

MDX

Microsoft

Data Quality

Situational

Great Expectations

GX Labs

Situational

dbt tests

dbt Labs

Situational

SodaCL

Soda

Observability

Adopt

Open​Telemetry

CNCF

Assess

OORS

BITOL @ LF

Policies

Adopt

OPA

CNCF

Assess

ODRL

W3C

AI Interfaces

Adopt

MCP

LF

Situational

A2A

LF

Click any row to open the standard. Click a column header to sort.

## FAQ

What do you mean by 
open standards
?

Anopen standard, as used on this page, is a specification that anyone can read, implement, and build on — without paying a vendor for the privilege. Concretely, a spec qualifies if:

* the specification text is published under anopen license(Apache, CC-BY, MIT, or a recognised standards-body licence);
* governance ispreferably independently controlled— a foundation, working group, or community — and not in the hands of a single vendor;
* there aremultiple independent implementations, or a credible path to them — one repo controlled by one company is not enough;
* it is thede-facto standardfor its slot in a modern data architecture, not a niche curiosity.

Origin doesn't matter — many of the entries here started as vendor specs (Iceberg at Netflix, Delta Lake at Databricks, gRPC at Google, OpenLineage at Datakin). What matters is whether the spec is openly governed and openly implementabletoday. TheStatusfield in each entry's drawer makes the governance situation explicit (foundation-hosted, vendor-led, draft, etc.), so you can judge for yourself.

Why did we build this — and what's the origin story?

BecauseEntropy Dataloves open standards — and is building its product on top of them. ODCS, ODPS, OpenLineage, MCP, and the rest are the spine of our marketplace; the same set of specs you can use without us. We also use this landscape ourselves tocommunicate with stakeholderson PoCs — to explain why a contract-first, vendor-neutral foundation is the cheaper long-term bet than yet another proprietary catalog. Seewww.entropy-data.comfor the full story.

It started as a single slide. Simon was preparing a talk onopen standards for data meshfor the Data Mesh Belgium meetup in Leuven (April 2026), and wanted one picture that answered "which standards actually matter, and where do they fit?" Every existing diagram either flattened everything into one box or focused on a single vendor's stack.

The slide kept growing. After the talk, enough people asked for "the picture" that turning it into an interactive, linkable page made more sense than mailing around a PNG. Inspired by theCNCF Landscapefor the categorisation and theThoughtWorks Tech Radarfor the per-entry judgement, but narrower in scope: open standards only, no vendors. It's still a living view — suggestions and corrections welcome.

Thelaunch post on LinkedInwent unexpectedly viral — most of the standards added since the launch came in as comments, DMs, and pull requests in the days that followed. The contributor list at the bottom of this page is the visible tip of that.

Why do you call this a 
data
 landscape?

Fair pushback: most of what's here ismetadata, not data. Schemas, contracts, lineage events, and catalog APIs all describe data rather thanaredata — and the page won't help you pick a vendor. Guilty as charged on both counts.

We still call it the "Data Landscape" because that's the conversation people are having. When teams say "our data stack" they mean the standards, formats, and protocols around the data, not the bytes themselves.

It's also deliberately not a vendor landscape. There's no Snowflake vs Databricks, no "best catalog of 2026". The CNCF Landscape catalogues vendors and projects; this one catalogues the openstandardsthey should interoperate around. If you're picking a vendor, ask which of these standards they implement. That's the question this landscape helps you ask, not answer.

Why did you include vendor specs in an overview of open standards?

Most "open standards" started as vendor specs. Iceberg came out of Netflix, Delta Lake out of Databricks, gRPC and Protobuf out of Google, OpenLineage was spun out of Datakin (now Astronomer) and incubated at LF AI & Data. What matters is whether the spec isopenly governed and openly implementabletoday, not who wrote the first commit. SeeWhat do you mean byopen standards?for the criteria we apply.

What do 
Adopt
, 
Situational
, 
Assess
, and 
Caution
 mean?

The coloured header on each tile is our editorial judgement — what we'd actually do with this standard if we were starting a new project today. The four levels borrow the verb-style framing of theThoughtWorks Tech Radar(Adopt / Trial / Assess / Hold), tuned for open standards rather than internal tech adoption:

* Adopt— the standard you should reach for in new work. Proven, multi-vendor, clearly the default for its slot (e.g. SQL, JSON, HTTP, ODCS for data contracts, Iceberg for table format, OpenLineage for lineage).
* Situational— the right answer in some contexts but not others. Pick deliberately based on the constraint (gRPC for service-to-service binary RPC, GraphQL for client-driven aggregation, GQL when you're already on graph databases).
* Assess— promising but not yet proven for production-default use. Track it, prototype with it, but don't commit your architecture to it yet (e.g. OSI, Substrait, OORS).
* Caution— we'd avoid for new work. Either superseded by a better option or fading from active use (e.g. MDX, JMS, XSLT). Listed because they're still encountered in existing systems.

Click a label in the toolbar legend to hide every tile of that judgement; click again to bring them back. Every standard's drawer carries the per-entry rationale (theJudgement reasonline). The same field is instandards.jsonasjudgement+judgementReasonif you want to disagree at scale. Within each category panel, tiles are ordered by judgement: Adopt first, Caution last.

Why is X listed, not listed, or marked as a vendor spec?

Why is X listed?Because it meets thefour criteria above— openly licensed, independently governed (or noted as a vendor spec), multiple implementations, and de-facto for its slot. Each entry's drawer shows theGovernanceandStatuswe relied on; the same fields are instandards.jsonif you want to audit the whole set at once.

Why isn't X listed?Most likely we haven't gotten to it yet, or we judged it a vendor product rather than an open spec. The bar is the spec, not the popularity of any one implementation. If you think we're wrong,open an issue— the data is a single JSON file, PRs welcome.

Why is X greyed out / marked as a vendor spec?Vendor-led specs are openly published and de-facto, but governance is effectively controlled by one company — they meet every criterionexceptindependent governance. We still list them because they matter (e.g. dbt, Protobuf, Schema Registry); the muted tile and grayscale logo are the caveat, not a downgrade.

Where didlegacyandnichego?Those used to be separate tags; they're now folded into the judgement. Standards we'd avoid for new work (XMLA, JMS, MDX) sit underCaution. Standards healthy only in a particular corner (ShEx, LinkML, GQL) sit underSituationalorAssessdepending on maturity. Seethe judgement explanationfor the per-tier criteria.

## Thank you

This landscape is curated byEntropy Data, with grateful thanks to everyone who helped shape it through suggestions, discussions, or pull requests (listed alphabetically by first name):Benjamin Ditel,Denis Arnaud,Erik Wilde,Jon Axon,Juan Sequeda,Marcel Grauwen,Mark M,Peter Hutzli,Prashanth Rao,Stefan Negele,
 andThierry Jean.

## Cite this landscape

If you reference this landscape in a talk, paper, or blog post, the canonical link ishttps://www.data-landscape.com/. A BibTeX entry is also available asdata-landscape.bib.

Plain text (APA-style)

Harrer, S. (2026). 
Data Landscape: Open Standards for Modern Data Architecture
. Entropy Data. https://www.data-landscape.com/

BibTeX

@misc{harrer2026datalandscape,
 author = {Harrer, Simon},
 title = {Data Landscape: Open Standards for Modern Data Architecture},
 year = {2026},
 month = apr,
 publisher = {Entropy Data},
 howpublished = {\url{https://www.data-landscape.com/}}
}

Download:data-landscape.bib

Missed a standard? Spotted something wrong?

This landscape is a living view — suggestions and corrections welcome.

 Open an issue
 

 Email Simon
 

 Message Simon