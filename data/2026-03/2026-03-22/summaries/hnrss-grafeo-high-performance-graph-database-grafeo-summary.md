---
title: Grafeo - High-Performance Graph Database - Grafeo
url: https://grafeo.dev/
date: 2026-03-21
site: hnrss
model: llama3.2:1b
summarized_at: 2026-03-22T11:29:26.635229
---

# Grafeo - High-Performance Graph Database - Grafeo

## **Overview**

*   Grafeo is a fast, lightweight, and embeddable graph database built in Rust.
  
  • **Benefits**: Fast execution speed, adaptive chunking, SIMD-optimized operations, multi-language queries (GQL, Cypher, Gremlin, GraphQL, SPARQL, SQL/PGQ), and vector search support. It supports dual data models for Labeled Property Graphs and RDF triples, as well as embeddability with zero external dependencies.
  
  • **Key Features**:
    *   High-performance graph database with a lower memory footprint than other in-memory databases on theLDBC Social Network Benchmark.
    *   Multi-language support with GQL, Cypher, Gremlin, GraphQL, SPARQL, and SQL/PGQ query languages.
    *   Labeled Property Graphs (LPGs) and RDF triples dual data model support.
    *   Vector search with HNSW-based similarity search using scalar, binary, and product algorithms.
    *   Embedded or standalone server capabilities with REST API, web UI, in-memory databases, and standalone clusters.

## **Why Use Grafeo?**

*   The graph database offers a high performance and scalability when used for applications that need to process large amounts of data on the Social Network Benchmark.

  • **Advantages**: The database supports fast execution speeds with adaptive chunking and SIMD-optimized operations.
  • **Competitive Advantages**: It supports dual data models for LPGs and RDF triples, making it capable of handling a wide range of graph types.

## **Getting Started**

### Install Grafeo

*   Installation: `cargo add grafeo` followed by installation with cargo command.

### Start a Standalone Server

*   Run the following command to start the standalone server:
    ```bash
env set GOPATH~/ grafeo-standalone-server ; cargo run --bin stand-alone --example start
```

## **Basic Operations**

### Create an In-Memory Database

*   Use `GrafeoDB::new_in_memory();` to create an in-memory database instance.

### Insert Data into the Graph

Insert nodes and edges using `execute(){} :()` with query language, such as GQL, Cypher, Gremlin, GraphQL, SPARQL, SQL/PGQ. Here's a basic example:

*   Insert a node:
    ```gql
INSERT (:Person {name: 'Alix', age: 30})
```

*   Insert an edge with an attribute and relationship:
    ```
MATCH (a:Person {name: 'Alix'}), (b:Person {name: 'Gus'})
  INSERT (a)-[:KNOWS {since: 2024}]->(b)
```
### Query the Graph

Use `execute()` with a query language, such as GQL, Cypher, Gremlin, GraphQL, SPARQL, or SQL/PGQ. Here's an example:

*   Execute a query to get all people:
    ```
MATCH (p:Person)-[:KNOWS]->(friend)
RETURN p.name, friend.name
```
*   Execute multiple queries and combine the results in a single statement:
    ```python
session.execute(r"""
  MATCH (p:Person)-[:KNOWS]->(friend)
  RETURN p.name, friend.name
""")
```