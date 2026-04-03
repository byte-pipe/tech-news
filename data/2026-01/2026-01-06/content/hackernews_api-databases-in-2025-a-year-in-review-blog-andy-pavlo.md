---
title: 'Databases in 2025: A Year in Review // Blog // Andy Pavlo - Carnegie Mellon University'
url: https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html
site_name: hackernews_api
fetched_at: '2026-01-06T11:07:06.642129'
original_url: https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html
author: viveknathani_
date: '2026-01-05'
description: 'Databases in 2025: A Year in Review, Andy Pavlo - Carnegie Mellon University,'
tags:
- hackernews
- trending
---

Another year passes. I was hoping to write more articles instead of just these end-of-the-year screeds, but I almostdiedin the spring semester, and it sucked up my time. Nevertheless, I will go through what I think are the major trends and happenings in databases over the last year.

There were many exciting and unprecedented developments in the world of databases.Vibe codingentered the vernacular. The Wu-Tang Clan announced theirtime capsule project. Rather than raising one massive funding round this year instead of going public, Databricks raisedtwo massive roundsinstead of going public.

Meanwhile, other events were expected and less surprising. Redis Ltd.switched their license backone year after theirrugpull(I called this shotlast year). SurrealDB reported great benchmark numbers because theyweren't flushing writes to disk and lost data. And Coldplay canbreak up your marriage. Astronomer did make some pretty goodlemonadeon that last one though.

Before I begin, I want to address the question I get every year in the comments about these articles. People always ask why I don't mention a particular
system
,
database
, or
company
 in my analysis. I can only write about so many things, and unless something interesting/notable happened in the past year, then there is nothing to discuss. But not all notable database events are appropriate for me to opine about. For example, the recent attempt to
unmask the AvgDatabase CEO
 is fair game, but the
MongoDB suicide lawsuit
 is decidedly not.

With that out of the way, let's do this. These articles are getting longer each year, so I apologize in advance.

Previous entries:

* Databases in 2024: A Year in Review
* Databases in 2023: A Year in Review
* Databases in 2022: A Year in Review
* Databases in 2021: A Year in Review

## The Dominance of PostgreSQL Continues

I first wrote about how PostgreSQL waseating the database worldin 2021. That trend continues unabated as most of the most interesting developments in the database world are happening once again with PostgreSQL. The DBMS's latest version (v18) dropped in November 2025. The most prominent feature is the newasynchronous I/O storage subsystem, which will finally put PostgreSQL on the path to dropping its reliance on the OS page cache. It also added support forskip scans; queries can still use multi-key B+Tree indexes even if they are missing the leading keys (i.e., prefix). There are some additional improvements to the query optimizer (e.g., removingsuperfluous self-joins).

Savvy database connoisseurs will be quick to point out that these are not groundbreaking features and that other DBMSs have had them for years. PostgreSQL is the only major DBMS still relying on the OS page cache. And Oracle has supportedskip scans since 2002(v9i)! You may wonder, therefore, why I am claiming that the hottest action in databases for 2025 happened with PostgreSQL?

The reason is that most of the database energy and activity is going into PostgreSQL companies, offerings, projects, and derivative systems.

#### Acquisitions + Releases:

In the last year, the hottest data start-up (Databricks) paid$1b for a PostgreSQL DBaaS company(Neon). Next, one of the biggest database companies in the world (Snowflake) paid$250m for another PostgreSQL DBaaS company(CrunchyData). Then, one of the biggest tech companies on the planet (Microsoft) launcheda new PostgreSQL DBaaS(HorizonDB). Neon and HorizonDB follow Amazon Aurora'soriginal high-level architecturefrom the 2010s, with a single primary node separating compute and storage. For now, Snowflake's PostgreSQL DBaaS uses the same core architecture as standard PostgreSQL because they built onCrunchy Bridge.

#### Distributed PostgreSQL:

All of the services I listed above are single-primary node architectures. That is, applications send writes to a primary node, which then sends those changes to secondary replicas. But in 2025, there were two announcements on new projects to create scale-out (i.e., horizontal partitioning) services for PostgreSQL. In June 2025, Supabase announced that it had hiredSugu, the Vitess co-creator and former PlanetScale co-founder/CTO, to lead theMultigresproject to create sharding middleware for PostgreSQL, similar to how Vitess shards MySQL. Sugu left PlanetScale in 2023 and had to lie back in the cut for two years. He is now likely clear of any legal issues and can make things happen at Supabase. You know it is abig dealwhen a database engineer joins a company, and theannouncementfocuses more on the person than the system. Theco-founder/CTO of SingleStorejoined Microsoft in 2024 tolead HorizonDB, but Microsoft (incorrectly) did not make a big deal about it. Sugu joining Supabase is likeOl' Dirty Bastard(RIP) getting out onparole after two yearsand thenannouncing a new record dealon the first day of his release.

One month after the Multigres news dropped, PlanetScaleannouncedits own Vitess-for-PostgreSQL project,Neki. PlanetScale launched its initialPostgreSQL DBaaSin March 2025, but the core architecture is single-node stockPostgreSQL with pgBouncer.

Update 2026-01-05:
 I was reminded via private email that
PgDog
 is also another open-source middleware system that seeks to support horizontal sharding in PostgreSQL. I had mentally compartmentalized PgDog in the same category as a connection pooling proxy (
PgBouncer
), but it is actually a competitor to Multigres and Neki.

#### Commercial Landscape:

With Microsoft's introduction of HorizonDB in 2025, all major cloud vendors now have serious projects for their own PostgreSQL offerings. Amazon has offeredAurora PostgreSQLsince 2017. Google put outAlloyDBin 2022. ServiceNow launched itsRaptorDB service in 2024, based on its 2021acquisitionof Swarm64. Even the old flip-phone IBM has had itscloud version of PostgreSQLsince 2018. Oracle released itsPostgreSQL service in 2023, though there is a rumor that its in-house PostgreSQL team was collateral damage in itsMySQL OCI layoffsin September 2025.

There are still a few independent (ISV) PostgreSQL DBaaS companies.Supabaseis likely the largest of these by the number of instances. Others includeYugabyteDB,TigerData(née TimeScale),PlanetScale,Xata,PgEdge, andNile. Xata built its original architecture onAmazon Aurora, but this year, it announced it isswitching to its own infrastructure.ParadeDBhas yet to announce its hosted service.Tembodropped itshosted PostgreSQL offeringin 2025 to pivot to a coding agent that can do some database tuning.HydraandPostgresMLwent bust in 2025 (seeDeathssection), so they're out of the game. Other systems provide a Postgres-compatible front-end, but the back-end systems are not derived from PostgreSQL (e.g.,CockroachDB,CedarDB,Google Spanner). There are also hosting companies that offer PostgreSQL DBaaS alongside other systems, such asAivenandTessel.

### Andy's Take:

It is not clear who the next major buyer will be after Databricks and Snowflake bought PostgreSQL companies. Again, every major tech company already has a Postgres offering. EnterpriseDB is the oldest PostgreSQL ISV, but missed out on the two most significant PostgreSQL acquisitions in the last five years. But they can ride Bain Capital's jock for a while, or hope that HPE buys them even though thatpartnershipis from eight years ago. The PostgreSQL M&A playfield is reminiscent of OLAP acquisitions in the late 2000s, whenVerticawas the last one waiting at the bus stop afterAsterData,Greenplum, andDATAllegrowere acquired.

The development of thetwothree competing distributed PostgreSQL projects (Multigres,Neki,PgDog) is welcome news. These projects are not the first time somebody has attempted this:Greenplum,ParAccel, andCitushave been around for two decades for OLAP workloads. Citus supports OLTP workloads, but they started in 2010 focused onanalytics. For OLTP, 15 years ago, the NTT RiTaDB project joined forces withGridSQLto createPostgres-XC. Developers from Postgres-XC foundedStormDB, whichTranslatticelater acquired in 2013.Postgres-X2was an attempt to modernize XC, but the developers abandoned that effort. Translattice open-sourced StormDB asPostgres-XL, but the project has been dormant since 2018.YugabyteDBcame out in2016and is probably the most widely deployed sharded PostgreSQL system (and remainsopen-source!), but it is a hard fork, so it is only compatible withPostgreSQL v15. Amazon announced its own sharded PostgreSQL (Aurora Limitless) in 2024, but it is closed source.

I know Microsoft bought Citus in 2019 but it is hard to keep track of what they were doing before HorizonDB because of their confusing product names. Citus was rebranded asAzure Database for PostgreSQL Hyperscalein 2019 and was then renamed toAzure Cosmos DB for PostgreSQLin 2022. But then there isAzure Database for PostgreSQL with Elastic Clustersthat also uses Citus, but it is not the same as the Citus-powered Azure Cosmos DB for PostgreSQL. Microsoft discontinuedAzure PostgreSQL Single Serverin 2023, but kept Azure PostgreSQL Flexible Server. That is a lot of Azure this and Azure that. It is sort of like how Amazon could not resist adding "Aurora" toDSQL'sname. Either way, at least Microsoft was smart enough to keep the name for their new system to just "Azure HorizonDB" (for now).

The PlanetScale squad hasno love for the other sideand is known to throw hands atNeonandTimescale. Database companies popping off at each other is nothing new (seeYugabyte vs. CockroachDBorDatabricks vs. Snowflake). I suspect we will see more of this in the future as the PostgreSQL wars heat up. I suggest that these smaller companiescall out the big cloud vendorsand keep each other's nameout of their mouths.

## MCP For Every Database!

If 2023 was the yearevery DBMS added a vector index, then 2025 was the year that every DBMS added support for Anthropic'sModel Context Protocol(MCP). MCP is a standardized client-server JSON-RPC interface that lets LLMS interact with external tools and data sources without requiring custom glue code. An MCP server acts as middleware in front of a DBMS and exposes a listing of tools, data, and actions it provides. An MCP client (e.g., an LLM host such as Claude or ChatGPT) discovers and uses these tools to extend its models' capabilities by sending requests to the server. In the case of databases, the MCP server converts these queries into the appropriate database query (e.g., SQL) or administrative command. In other words, MCP is the middleman who keepsthe bricks counted and the cream straight, so the database and LLMs trust each other enough to do business.

AnthropicannouncedMCP in November 2024, but it really took off in March 2025 when OpenAI announced it wouldsupport MCP in its ecosystem. Over the next few months, every DBMS vendor released MCP servers for all system categories: OLAP (e.g.,ClickHouse,Snowflake,Firebolt,Yellowbrick), SQL (e.g.,YugabyteDB,Oracle,PlanetScale), and NoSQL (e.g.,MongoDB,Neo4j,Redis). Since there is no official Postgres MCP server, every Postgres DBaaS has released its own (e.g.,Timescale,Supabase,Xata). The cloud vendors released multi-database MCP servers that can talk to any of their managed database services (e.g.,Amazon,Microsoft,Google). Allowing a single gateway to talk to heterogeneous databases is almost, but not quite, a holy-grailfederated database. As far as I know, each request in these MCP servers targets only a single database at a time, so the application is responsible for performing joins across sources.

Beyond the official vendor MCP implementations, there arehundredsof rando MCP server implementations for nearly every DBMS. Some of them attempt to support multiple systems (e.g.,DBHub,DB MCP Server). DBHub put out agood overviewof PostgreSQL MCP servers.

An interesting feature that has proven helpful for agents is database branching. Although not specific to MCP servers, branching allows agents to test database changes quickly without affecting production applications. Neon reported in July 2025 that agentscreate 80% of their databases. Neon was designed from the beginning to supportbranching(Nikita showed me an early demo when the system was still called "Zenith"), whereas other systems have added branching support later. See Xata's recentcomparison articleon database branching.

### Andy's Take:

On one hand, I'm happy that there is now a standard for exposing databases to more applications. But nobody should trust an application with unfettered database access, whether it is via MCP or the system's regular API. And it remains good practice only to grant minimal privileges to accounts. Restricting accounts is especially important with unmonitored agents that may start going wild all up in your database. This means that lazy practices like giving admin privileges to every account or using the same account for every service are going to get wrecked when the LLM starts popping off. Of course, if your company leaves its databaseopen to the worldwhile you cause the stock price of one of the wealthiest companies todrop by $600b, then rogue MCP requests are not your top concern.

From my cursory examination of a few MCP server implementations, they are simple proxies that translate the MCP JSON requests into database queries. There is no deep introspection to understand what the request aims to do and whether it is appropriate. Somebody is going to try toorder 18,000 water cupsin your application, and you need to make sure it doesn't crash your database. Some MCP servers have basic protection mechanisms (e.g., ClickHouse only allowsread-only queries). DBHub provides a few additionalprotections, such as capping the number of returned records per request and implementing query timeouts. Supabase's documentation offersbest-practice guidelinesfor MCP agents, but they rely on humans to follow them. And of course, if you rely on humans to do the right thing,bad things will happen.

Enterprise DBMSs already have automated guardrails and other safety mechanisms that open-source systems lack, and thus, they are better prepared for an agentic ecosystem. For example,IBM GuardiumandOracle Database Firewallidentify and block anomalous queries. I am not trying to shill for these big tech companies. I know we will see more examples in the future of agents ruining lives, likeaccidentally dropping databases. Combining MCP servers with proxies (e.g., connection pooling) is an excellent opportunity to introduce automated protection mechanisms.

## MongoDB, Inc. v. FerretDB Inc.

MongoDB has been the NoSQL stalwart for two decades now. FerretDB was launched in 2021 by Percona's top brass to provide a middleware proxy that converts MongoDB queries into SQL for a PostgreSQL backend. This proxy allows MongoDB applications to switch over to PostgreSQL without rewriting queries.

They coexisted for a few years before MongoDB sent FerretDB acease-and-desist letterin 2023, alleging that FerretDB infringes MongoDB's patents, copyrights, and trademarks, and that it violates MongoDB's license for its documentation and wire protocol specification.
This letter became public in May 2025 when MongoDB wentnuclearon FerretDB by filing afederal lawsuitover these issues.
Part of their beef is that FerretDB is out on the street, claiming they have a "drop-in replacement" for MongoDB without authorization. MongoDB'scourt filinghas all the standard complaints about (1) misleading developers, (2) diluting trademarks, and (3) damaging their reputation.

The story is further complicated by Microsoft's announcement that it donated its MongoDB-compatibleDocumentDBto theLinux Foundation. The project website mentions that DocumentDB is compatible with the MongoDB drivers and that it aims to "build a MongoDB compatible open source document database". Other major database vendors, such as Amazon and Yugabyte, are also involved in the project. From a cursory glance, this language seems similar to what MongoDB is accusing FerretDB of doing.

### Andy's Take:

I could not find an example of a database company suing another one for replicating their API. The closest is Oracle suing Google for using a clean-room copy of the Java API in Android. The Supreme Court ultimatelyruled in favor of Googleon fair use grounds, and the case affected how re-implementation is treated legally.

I don't know how the lawsuit will play out if it ever goes to trial. A jury of random people off the street may not be able to comprehend the specifics of MongoDB's wire protocol, but they are definitely going to understand that the original name of FerretDB wasMangoDB. It is going to be challenging to convince a jury that you were not trying to divert customers when you changed one letter in the other company's name. Never mind that it is not even an original name: there is already a parody DBMS calledMangoDBthat writes everything to/dev/nullas a joke.

And while we are on the topic of database system naming, Microsoft's choice of "DocumentDB" is unfortunate. There are alreadyAmazon DocumentDB(which, by the way, is alsocompatiblewith MongoDB, but Amazon probably pays for that),InterSystems DocDB, andYugabyte DocDB. Microsoft's original name for "Cosmos DB" was alsoDocumentDBback in 2016.

Lastly, MongoDB's court filing claims they "pioneered the development of 'non-relational' databases". This statement is incorrect. The first general-purpose DBMSs were non-relational because the relational model had not yet been invented. General Electric'sIntegrated Data Store(1964) used anetwork data model, and IBM'sInformation Management System(1966) used ahierarchical data model. MongoDB is also not the first document DBMS. That title goes to the object-oriented DBMSs from the late 1980s (e.g.,Versant) or the XML DBMSs from the 2000s (e.g.,MarkLogic). MongoDB is the most successful of these approaches by a massive margin (except maybe IMS).

## File Format Battleground

File formats are an area of data systems that have been mostly dormant for the last decade. In 2011, Meta released a column-oriented format for Hadoop calledRCFile. Two years later, Meta refined RCFile and announced the PAX-basedORC(Optimized Record Columnar File) format. A month after ORC's release, Twitter and Cloudera released the first version ofParquet. Nearly 15 years later, Parquet is the dominant file open-source format.

In 2025, there were five new open-source file formats released vying to dethrone Parquet:

* CWI FastLanes
* CMU + Tsinghua F3
* SpiralDB Vortex
* The Germans' AnyBlox
* Microsoft Amudai

These new formats joined the other formats released in 2024:

* Meta Nimble
* LanceDB Lance
* IoTDB TsFile

SpiralDBmade the biggest splash this year with their announcement ofdonating Vortex to the Linux Foundationand the establishment of their multi-organization steering committee. Microsoft quietlykilled offAmudai (or at least closed sourced it) at some point at the end of 2025. The other projects (FastLanes, F3, Anyblox) are academic prototypes. Anyblox won theVLDB Best Paperaward this year.

This fresh competition has lit a fire in the Parquet developer community tomodernize its features. See thisin-depth technical analysisof the columnar file format landscape by Parquet PMC Chair (Julien Le Dem).

### Andy's Take:

The main problem with Parquet is not inherent in the format itself. The specification can and has evolved. Nobody expected organizations to rewrite petabytes of legacy files to update them to the latest Parquet version. The problem is that there are so many implementations of reader/writer libraries in different languages, each supporting a distinct subset of the specification. Ouranalysisof Parquet files in the wild found that 94% of them use only v1 features from 2013, even though their creation timestamps are after 2020. This lowest common denominator means that if someone creates a Parquet file using v2 features, it is unclear whether a system will have the correct version to read it.

I worked on theF3file format with brilliant people at Tsinghua (Xinyu Zeng,Ruijun Meng,Huanchen Zhang), CMU (Martin Prammer,Jignesh Patel), andWes McKinney. Our focus is on solving this interoperability problem by providing both native decoders as shared objects (Rust crates) and embedded WASM versions of those decoders in the file. If somebody creates a new encoding and the DBMS does not have a native implementation, it can still read data using the WASM version by passing Arrow buffers. Each decoder targets a single column, allowing a DBMS to use a mix of native and WASM decoders for a single file. AnyBlox takes a different approach, generating a single WASM program to decode the entire file.

I don't know who will win the file format war. The next battle is likely to be over GPU support. SpiralDB seems to be making the right moves, but Parquet's ubiquity will be challenging to overcome. I also didn't even discuss howDuckLakeseeks to upend Iceberg...

Of course, when this topic comes up, somebody always posts thisxkcd comic on competing standards. I've seen it before. You don't need to email it to me again.

## Random Happenings

Databases are big money. Let's go through them all!

#### Acquisitions:

Lots of movement on the block. Pineconereplaced its CEOin September toprepare for an acquisition, but I have not heard anything else about it. Here are the ones that did happen:

* DataStax → IBMThe Cassandra stalwart got picked up by IBM at the beginning of the year for anestimated $3b.
* Quickwit → DataDogThe leading company behind the Lucene replacement,Tantivy, a full-text search engine, was acquired at the beginning of the year. The good news is that Tantivy development continues unabated.
* SDF → dbtThis acquisition was a solid pick-up for dbt as part of theirFusionannouncement this year. It allows them to perform more rigorous SQL analysis in their DAGs.
* Voyage.ai → MongoDBMongo picked up an early-stage AI company toexpandits RAG capabilities in its cloud offering. One of mybest studentsjoined Voyage one week before the announcement. He thought he was going against the "family" by not signing with a database company, only to end up at one.
* Neon → DatabricksApparently, there was a bidding war for this PostgreSQL company, but Databricks paid amouthwatering $1bfor it. Neon still exists today as a standalone service, but Databricks quickly rebranded it in its ecosystem asLakebase.
* CrunchyData → SnowflakeYou know Snowflake could not let Databricks get all the excitement during the summer, so they paid $250m for the 13-year-old PostgreSQL company CrunchyData. Crunchy had picked up top ex-Citus talent in recent years and was expanding its DBaaS offering before Snowflake wrote them a check. Snowflake announced the public preview of itsPostgresservice in December 2025.
* Informatica → SalesforceThe 1990s old-school ETL company Informatica got picked up by Salesforce for$8b. This is after they went public in 1999, reverted to PE in 2015, and went public again in 2021.
* Couchbase → Private EquityTo be honest, I never understood how Couchbase went public in 2021. I guess they were riding on MongoDB's coattails? Couchbase did interesting work a few years ago by incorporating components from theAsterixDB project at UC Irvine.
* Tecton → DatabricksTecton provides Databricks with additional tooling to build agents. Another one of myformer studentswas at the company and is now at Databricks.
* Tobiko Data → FivetranThis team is behind two useful tools:SQLMeshandSQLglot. The former is the only viable open-source contender to dbt (seebelowfor their pending merger with Fivetran). SQLglot is a handy SQL parser/deparser that supports a heuristic-based query optimizer. The combination of this in Fivetran and SDF with dbt makes for an interesting technology play in this space in the coming years.
* SingleStore → Private EquityThe PE firm buying SingleStore (Vector Capital) has prior experience in managing a database company. They previously purchased theXML database company MarkLogic in 2020and flipped it toProgress in 2023.
* Codership → MariaDBAfter getting bought by PE in 2024, the MariaDB Corporation went on a buying spree this year. The first up is the company behind theGalera Clusterscale-out middleware for MariaDB. See my 2023 overview of theMariaDB dumpster fire.
* SkySQL → MariaDBAnd then we have the second MariaDB acquisition. Just so everyone is clear, the original commercial company backing MariaDB was called "SkySQL Corporation" in 2010, but it changed its name to "MariaDB Corporation" in 2014. Then in 2020, the MariaDB Corporation released a MariaDB DBaaS called SkySQL. But because they were hemorrhaging cash, the MariaDB Corporation spun SkySQL Inc. out as anindependent company in 2023. And now, in 2025, MariaDB Corporation has come full circle bybuying back SkySQL Inc. I did not have this move on my database bingo card this year.
* Crystal DBA → TemporalThe automated database optimization tool company heads off to Temporal to automatically optimize their databases! I'm happy to hear that Crystal's founder and Berkeley database group alumnusJohann Schleier-Smithis doing well there.
* HeavyDB → NvidiaThis system (formerly OmniSci, formerly MapD) was one of the first GPU-accelerated databases, launched in 2013. I couldn't find an official announcement of their closing, aside from an M&A firm listing the successful deal. And then we had a meeting with Nvidia to discuss potential database research collaborations, and some HeavyDB friends showed up.
* DGraph → Istari DigitalDgraph was previously acquired byHypermode in 2023. It looks like Istari just bought Dgraph and not the rest of Hypermode (or they ditched it). I still haven't met anybody who is actively using Dgraph.
* DataChat → MewsThis was one of the first "chat with your database" out of the University of Wisconsin and now CMU-DB professorJignesh Patel. But they were bought by a European hotel management SaaS. Take that to mean what you think it means.
* Datometry → SnowflakeDatometry has been working on the perilous problem of automatically converting legacy SQL dialects (e.g., Teradata) to newer OLAP systems for several years. Snowflake picked them up to expand theirmigration tooling. See Datometry's 2020CMU-DB tech talkfor more info.
* LibreChat → ClickHouseLike Snowflake buying Datometry, ClickHouse's acquisition here is a good example of improving the developer experience for high-performance commodity OLAP engines.
* Mooncake → DatabricksAfter buying Neon, Databricks bought Mooncake to enable PostgreSQL to read/write to Apache Iceberg data. See their November 2025CMU-DB talkfor more info.
* Confluent → IBMThis is the archetype of how to make a company out of a grassroots open-source project. Kafka was originally developed at Linkedin in 2011. Confluent was then spun out as a separate startup in 2014. They went IPO seven years later in 2021. Then IBM wrote a big check to take it over. Like with DataStax, it remains to be seen whether IBM will do to Confluent what IBM normally does withacquired companies, or whether they will be able to remain autonomous like RedHat.
* Gel → VercelFormerlyEdgeDB, they provided DSL on top of PostgreSQL that got picked up by Verel at the end of the year.
* Kuzu → ???The embedded graph DBMS out of the University of Waterloo was acquired by an unnamed company in 2025. The KuzuDB company then announced it was abandoning the open-source project. TheLadybugDBproject is an attempt at maintaining a fork of the Kuzu code.

#### Mergers:

Unexpected news dropped in October 2025 whenFivetrananddbt Labsannounced they weremergingto form a single company.

The last merger I can think of in the database space was the 2019 merger betweenCloudera and Hortonworks. But that deal was just weak keys gettingstepped on in a kitchen: two companies that were struggling to find market relevance with Hadoop merged into a single company to try to find it (spoiler: they did not). The MariaDB Corporation merger withAngel Pond Holdings Corporationin 2022 via aSPACtechnically counts too, but that deal was so MariaDB could backdoor their way to IPO. And it didn't end well forinvestors. The Fivetran + dbt merger is different (and better) than these two. They are two complementary technology companies combining to become an ETL juggernaut, preparing for a legit IPO in the near future.

#### Funding:

Unless I missed them or they weren't announced, there were not as many early-stage funding rounds for database startups. The buzz around vector databases has muted, and VCs are only writing checks for LLM companies.

* Databricks-$4b Series L
* Databricks-$1b Series K
* ClickHouse-$350m Series C
* Supabase-$200m Series D
* Timescale-$110m Series C
* Supabase-$100m Series E
* Astronomer-$93m Series D
* Tessel-$60m Series B
* LanceDB-$30m Series AConvex-$24m Series BSpiralDB-$22m Series AParadeDB-$12m Series ACedarDB$5.9m SeedTopK-$5.5m SeedColumnar-$4m SeedSereneDB-$2.1m Pre-SeedStarburst-Undisclosed?TurboPuffer-Undisclosed?
* Convex-$24m Series BSpiralDB-$22m Series AParadeDB-$12m Series ACedarDB$5.9m SeedTopK-$5.5m SeedColumnar-$4m SeedSereneDB-$2.1m Pre-SeedStarburst-Undisclosed?TurboPuffer-Undisclosed?
* SpiralDB-$22m Series A
* ParadeDB-$12m Series A
* CedarDB$5.9m Seed
* TopK-$5.5m Seed
* Columnar-$4m Seed
* SereneDB-$2.1m Pre-Seed
* Starburst-Undisclosed?
* TurboPuffer-Undisclosed?

#### Name Changes:

A new category in my yearly write-up is database companies changing the name of their company or system.

* HarperDB → HarperThe JSON database company dropped the "DB" suffix from its name to emphasize its positioning as a platform for database-backed applications, similar toConvexand Heroku. I like the Harper people. Their 2021CMU-DB tech talkpresented theworstDBMS idea I have ever heard. Thankfully, they ditched that once they realized how bad it was and switched to LMDB.
* EdgeDB → GelThis was a smart move because the name "Edge" conveys that it is a database for edge devices or services (e.g.,Fly.io). But I'm not sure "Gel" conveys the project's higher-level goals. See their 2025CMU-DB talk on Gel's query language(still called EdgeQL) from a CMU Ph.D. alum.
* Timescale → TigerDataThis is a rare occurrence of a database company renaming itself to distinguish itself from its main database product. It is usually companies renaming themselves to be the name of the database (e.g., "Relational Software, Inc." to "Oracle Systems Corporation", "10gen, Inc." to "MongoDB, Inc."). But it makes sense for the company to try to shed the perception of being a specialized time-series DBMS instead of an improved version of PostgreSQL for general applications, since the former is a much smaller market segment than the latter.

#### Deaths:

In full disclosure, I was a technical advisor for two of these failed startups. My success rate as an advisor is terrible at this point. I was also an advisor forSplice Machine, but they closed shop in 2021. In my defense, I only talk with these companies about technical ideas, not business strategies. And I did tell Fauna they should add SQL support, but they did not take my advice.

* FaunaAn interesting distributed DBMS based onDan Abadi'sresearch fordeterministic concurrency control. They provided strongly consistent transactions right when the NoSQL fade was waning, and Spanner made transactions cool again. But they had aproprietary query languageand made big bets on GraphQL.
* PostgresMLThe idea seemed obvious: enable people to run ML/AI operations inside of their PostgreSQL DBMS. The challenge was to convince people to migrate their existing databases to their hosted platform. They were pushingpgCatas a proxy to mirror database traffic. One of the co-founders joined Anthropic. The other co-founder created a new proxy project calledpgDog.
* DerbyThis is one of the first DBMSs written in Java, dating back to 1997 (originally called "Java DB" or "JBMS"). IBM donated it to the Apache Foundation in the 2000s, and it was renamed as Derby. In October 2025, the project announced that the system would enter "read-only mode" because no one was actively maintaining it anymore.
* HydraAlthough there is no official announcement for the DuckDB-inside-Postgres startup, the co-founders and employees have scattered to other companies.
* MyScaleDBThis was a fork of Clickhouse that adds vector search and full-text indexing using Tantivy. They announced they were closing in May 2025.
* Voltron DataThis was supposed to be the supergroup of database companies. Think of it like havingRun the Jewelsteam of heavy hitters. You had top engineers from Nvidia Rapids, theinventorof Apache Arrow and Python Pandas, and the Peruvian GPU wizards fromBlazingSQL. Then throw in$110m in VC moneyfrom top firms that included the future CEO of Intel (and aboard of trustee member at CMU). They built a GPU-accelerated database (Theseus), but failed to launch it in a timely manner.

Lastly, although not a business, I would be remiss not to mention theclosingofIBM Research Almaden. IBM built this site in 1986 and was the database research mecca for decades. I interviewed atAlmaden in 2013and found the scenery to be beautiful. The IBM Research Database Group is not what itused to be. Still, the alum list of this hallowed database ground is impressive:Rakesh Agrawal,Donald Chamberlin,Ronald Fagin,Laura Haas,Mohan,Pat Selinger,Moshe Vardi,Jennifer Widom, andGuy Lohman.

Update 2026-01-05:
 I missed that Gel was acquired by Vercel in December 2025.
[Credit]

Update 2026-01-05:
 I also missed that Supabase raised
two
 funding rounds in 2025.

Update 2026-01-05:
 Although TurboPuffer has not made an official announcement for raising a round, their CEO mentions adding somebody from Thrive Capital to their team.
[Credit]

Update 2026-01-05:
 Apparently I need a better way to track fundraises because I missed LanceDB's Series A round too!
[Credit]

### Andy's Take:

Somebodyclaimedthat I judge the quality of a database based on how much funding the backing company raises for its development. This is obviously not true. I track these happenings because the database research game is crowded and high-energy. Not only am I "competing" against academics at other universities, but big tech companies and small start-ups are also putting out interesting systems I need to follow. The industry research labs are not what they used to be, except for Microsoft Research, which is still aggressively hiring top people and doing incredible work.

Ipredicted in 2022that there would be a large number of database company closings in 2025. Yes, there were more closings this year than in previous years, but not at the scale I expected.

The death of Voltron and sort-of acquihire of HeavyDB seem to continue the trend of the inviability of GPU-accelerated databases.Kineticahas been milking government contracts for years, andSqreamstill appears to be kicking it. These companies are still niche, and nobody has been able to make a significant dent in the dominance of CPU-powered DBMSs. I can't say who or what, but you will hear some major GPU-accelerated database announcements by vendors in 2026. It also provides further evidence of the commoditization of OLAP engines; modern systems have gotten so fast that the performance between them is negligible for low-level operations (scans, joins), so the things that differentiate one system from another are user experience and the quality of the query plans their optimizers generate.

The Couchbase and SingleStore acquisitions by private equity (PE) firms might signal a future trend in the database industry. Of course, PE acquisitions have happened before, but they all seem to be in recent times: (1)MarkLogicin 2020, (2)Clouderain 2021, and (3)MariaDBin 2023. The only ones I can find before 2020 wereSolidDBin 2007 andInformaticain 2015. PE acquisitions might replace the trend of plateaued database companies being bought by holding companies that milk the maintenance fees until eternity (Actian, Rocket). Even Oracle is still making money offRDB/VMSafter buying them 30 years ago!

Lastly, props toNikita Shamgunov. As far as I know, he is the only person to have co-founded two database companies (SingleStoreandNeon) that were both acquired in a single year. Like when DMX (RIP) released two #1 albums in a single year (It's Dark and Hell Is Hot,Flesh of My Flesh), I don't think anybody is going to break Nikita's record any time soon.

## Peak Male Performance

Talk about a banner year for the database OG Larry Ellison. The man turned 81 and accomplished more in one year than most people do in their lifetime. I will cover it all in chronological order.

Larry started the year ranked third-richest in the world. The idea that he would be worth less than Mark Zuckerberg was keeping him up at night. Some were saying Larry's insomnia was due to a diet change after hebought a famous British puband was eating more pies. But I assure you that Larry's "veg-aquarian" diet has not changed in 30 years. Then, in April 2025, we got the news that Larry had become thesecond-richest person in the world. He started sleeping a little better, but it still wasn't good enough. There was also still a lot going on in his life that was stressing him out. For example, Larry finally decided to sell his rare, semi-road-legalMcLaren F1 supercar, complete with the original owner's manual in the glovebox.

In July 2025, Larry graced us with thisthird tweetin 13 years (known as "#3" by Larry aficionados such as myself). This was an update about theEllison Institute of Technology(EIT) that Larry established near the University of Oxford. With the name EIT and its association with Oxford, it sounds like it would be a pure research, non-profit institution, similar to Stanford'sSRIor CMU'sSEI. But it turns out to be an umbrella organization for a series of for-profit companies owned by a California-based limited liability company. Of course, a bunch of weirdos replied to #3 with promises ofblockchain-powered cryogenic freezingorroom-temperature superconductors. Larry told me he ignores those. Then there are people likethis guywho get it.

The biggest database news of the year (possibly the century) hit us on Wednesday, September 10th, at approximately 3:00pm EST. After waiting for his turn for decades, Larry Joseph Ellison was finally anointed therichest person in the world.$ORCLshares rose by 40% that morning, and since Larry still owns 40% of the company, his estimated total worth is$393b. To put this in perspective, this not only made Larry the wealthiest person in the world, but also the richest person in the entire history of humanity. The peak net worths, adjusted for inflation, ofJohn D. RockefellerandAndrew Carnegie(yes, the 'C' in CMU) were only$340band$310b, respectively.

On top of Larry's ascension to the top of the world, Oracle was also involved in theacquisition of the U.S. company controlling TikTokand Larrybankrolling Paramount(controlled by his son from his fourth marriage) bid totake over Warner Bros. The U.S. president even chided Larry totake control of CNN's news divisionsince Larry is the majority shareholder of Paramount.

### Andy's Take:

I don't even know where to begin. Of course, when I found out that Larry Ellison had become the richest person in the world, all thanks to databases, I washeartenedthat something positive had finally happened in our lives. I don't care that Oracle's stock was artificially pumped up bysplashy dealsto build AI data centers instead of its traditional software business. I don't care that he dropped down the rankings after personally losing$130b in two months. That's like you and meblowing a paycheck on FortuneCoins. It stings a little, and we had to eat rice and beans for two weeks mixed with expired hot sauce packets we took from Taco Bell, but we'll be alright.

Some people claim that Larry isout of touchwith ordinary people. Or that he has lost his way because he is involved in things not directly related to databases. They point to things like hisHawaiian robot farmsellinglettuce at $24/pound(€41/kg). Or that 81-year-old men don't havenaturally blonde hair.

The truth is that Larry Ellison has conquered the enterprise database world,competitive sailing, andtechbro wellness spas. The obvious next step is to take over a cable TV channel watched by thousands of people waiting in airports every day. Every time I talk with Larry, he makes it clear that he does not care one bit what people say or think about him. He knows hisfans love him. His (new)wife loves him. And in the end, that's all that matters.

## Conclusion

Before we close, I want to give some quick shout outs and words of advice. First is to PT for keeping theirdatabase game tightwith Turso in lockdown (see you on the outside). Condolences to JT forlosing their jobfor trapping theirKevoDBdatabase sidepiece. And be sure to only put in fake data in your database for testing and not tosell it for $175m only to end up getting a seven year bid.

My Ph.D. students and I also have a newstart-up. I hope to say more on that soon. Word is bond.
