---
title: Grafeo - High-Performance Graph Database - Grafeo
url: https://grafeo.dev/
site_name: hnrss
content_file: hnrss-grafeo-high-performance-graph-database-grafeo
fetched_at: '2026-03-22T11:09:51.665875'
original_url: https://grafeo.dev/
author: S.T. Grond
date: '2026-03-21'
description: A high-performance, embeddable graph database with a Rust core and no required C dependencies. Python, Node.js, Go, C, C#, Dart and WebAssembly bindings. GQL (ISO standard) query language.
tags:
- hackernews
- hnrss
---

# Grafeo¶



### A fast, lean, embeddable graph database built in Rust¶



Get StartedView on GitHub






## Why Grafeo?¶



* High PerformanceFastest graph database tested on theLDBC Social Network Benchmark, both embedded and as a server, with a lower memory footprint than other in-memory databases. Built in Rust with vectorized execution, adaptive chunking and SIMD-optimized operations.
* Multi-Language QueriesGQL, Cypher, Gremlin, GraphQL, SPARQL and SQL/PGQ. Choose the query language that fits the project and expertise level.
* LPG & RDF SupportDual data model support for both Labeled Property Graphs and RDF triples. Choose the model that fits the domain.
* Vector SearchHNSW-based similarity search with quantization (Scalar, Binary, Product). Combine graph traversal with semantic similarity.
* Embedded or StandaloneEmbed directly into applications with zero external dependencies, or run as a standalone server with REST API and web UI. From edge devices to production clusters.
* Rust CoreCore database engine written in Rust with no required C dependencies. Optional allocators (jemalloc/mimalloc) and TLS use C libraries for performance. Memory-safe by design with fearless concurrency.
* ACID TransactionsFull ACID compliance with MVCC-based snapshot isolation. Reliable transactions for production workloads.
* Multi-Language BindingsPython (PyO3), Node.js/TypeScript (napi-rs), Go (CGO), C (FFI), C# (.NET 8 P/Invoke), Dart (dart:ffi) and WebAssembly (wasm-bindgen). Use Grafeo from the language of choice.
* EcosystemAI integrations (LangChain, LlamaIndex, MCP), interactive notebook widgets, browser-based graphs via WebAssembly, standalone server with web UI and benchmarking tools.




## Quick Start¶


Python
Rust



uv

add

grafeo


import

grafeo

# Create an in-memory database

db

=

grafeo
.
GrafeoDB
()

# Create nodes and edges

db
.
execute
(
"""

 INSERT (:Person {name: 'Alix', age: 30})

 INSERT (:Person {name: 'Gus', age: 25})

"""
)

db
.
execute
(
"""

 MATCH (a:Person {name: 'Alix'}), (b:Person {name: 'Gus'})

 INSERT (a)-[:KNOWS
{since: 2024}
]->(b)

"""
)

# Query the graph

result

=

db
.
execute
(
"""

 MATCH (p:Person)-[:KNOWS]->(friend)

 RETURN p.name, friend.name

"""
)

for

row

in

result
:


print
(
f
"
{
row
[
'p.name'
]
}
 knows
{
row
[
'friend.name'
]
}
"
)




cargo

add

grafeo


use

grafeo
::
GrafeoDB
;

fn

main
()

->

Result
<
(),

grafeo_common
::
utils
::
error
::
Error
>

{


// Create an in-memory database


let

db

=

GrafeoDB
::
new_in_memory
();


// Create a session and execute queries


let

mut

session

=

db
.
session
();


session
.
execute
(
r#"

 INSERT (:Person {name: 'Alix', age: 30})

 INSERT (:Person {name: 'Gus', age: 25})

 "#
)
?
;


session
.
execute
(
r#"

 MATCH (a:Person {name: 'Alix'}), (b:Person {name: 'Gus'})

 INSERT (a)-[:KNOWS {since: 2024}]->(b)

 "#
)
?
;


// Query the graph


let

result

=

session
.
execute
(
r#"

 MATCH (p:Person)-[:KNOWS]->(friend)

 RETURN p.name, friend.name

 "#
)
?
;


for

row

in

result
.
rows

{


println!
(
"{:?}"
,

row
);


}


Ok
(())

}







## Features¶



### Dual Data Model Support¶



Grafeo supports both major graph data models with optimized storage for each:


LPG (Labeled Property Graph)
RDF (Resource Description Framework)



* Nodeswith labels and properties
* Edgeswith types and properties
* Propertiessupporting rich data types
* Ideal for social networks, knowledge graphs, application data



* Triples: subject-predicate-object statements
* SPO/POS/OSP indexesfor efficient querying
* W3C standard compliance
* Ideal for semantic web, linked data, ontologies





### Query Languages¶



Choose the query language that fits the project:





Language

Data Model

Style





GQL
 (default)

LPG

ISO standard, declarative pattern matching



Cypher

LPG

Neo4j-compatible, ASCII-art patterns



Gremlin

LPG

Apache TinkerPop, traversal-based



GraphQL

LPG, RDF

Schema-driven, familiar to web developers



SPARQL

RDF

W3C standard for RDF queries



SQL/PGQ

LPG

SQL:2023 GRAPH_TABLE for SQL-native graph queries




GQL
Cypher
Gremlin
GraphQL
SPARQL



MATCH

(
me
:
Person

{
name
:

'Alix'
}
)
-
[:
KNOWS
]
->
(
friend
)
-
[:
KNOWS
]
->
(
fof
)

WHERE

fof

<>

me

RETURN

DISTINCT

fof
.
name




MATCH

(
me
:
Person

{
name
:

'Alix'
})
-[
:
KNOWS
]->
(
friend
)
-[
:
KNOWS
]->
(
fof
)

WHERE

fof

<>

me

RETURN

DISTINCT

fof
.
name




g.V().has('name', 'Alix').out('KNOWS').out('KNOWS').

 where(neq('me')).values('name').dedup()




{


Person
(
name
:

"Alix"
)

{


friends

{

friends

{

name

}

}


}

}




SELECT

DISTINCT

?fofName

WHERE

{


?me

foaf
:
name

"Alix"

.


?me

foaf
:
knows

?friend

.


?friend

foaf
:
knows

?fof

.


?fof

foaf
:
name

?fofName

.


FILTER
(
?fof

!=

?me
)

}






### Architecture Highlights¶


* Push-based execution enginewith morsel-driven parallelism
* Columnar storagewith type-specific compression
* Cost-based query optimizerwith cardinality estimation
* MVCC transactionswith snapshot isolation
* Zone mapsfor intelligent data skipping



## Installation¶


Python
Node.js
Go
Rust
C#
Dart
WASM



uv

add

grafeo




npm

install

@grafeo-db/js




go

get

github.com/GrafeoDB/grafeo/crates/bindings/go




cargo

add

grafeo




dotnet

add

package

GrafeoDB




# pubspec.yaml

dependencies
:


grafeo
:

^0.5.21




npm

install

@grafeo-db/wasm







## License¶



Grafeo is licensed under theApache-2.0 License.






 Back to top
