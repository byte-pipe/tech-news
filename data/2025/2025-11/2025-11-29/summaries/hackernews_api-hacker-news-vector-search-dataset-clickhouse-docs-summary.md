---
title: Hacker News vector search dataset | ClickHouse Docs
url: https://clickhouse.com/docs/getting-started/example-datasets/hackernews-vector-search-dataset
date: 2025-11-28
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-29T11:25:18.047187
screenshot: hackernews_api-hacker-news-vector-search-dataset-clickhouse-docs.png
---

# Hacker News vector search dataset | ClickHouse Docs

## Introduction


**Hacker News Dataset**

The Hacker News dataset contains approximately 28.74 million postings and their vector embeddings in a Parquet file hosted on ClickHouse as a single S3 bucket.


### Key Takeaways

* The complete dataset can be used for designing, sizing, and performing large-scale real-world vector search applications.
* A sizing exercise is recommended to estimate storage and memory requirements.
* Steps include creating tables, loading data, building a vector similarity index, and performing ANN search queries.

## Dataset Details


### Loading Data

**SQL Statement**: Load the dataset from the Parquet file using `INSERT INTO hackernews SELECT * FROM s3('https://clickhouse-datasets.s3.amazonaws.com/hackernews-miniLM/hackernews_part_1_of_1.parquet');`

### Building Vector Similarity Index

**SQL Statement**: Define and build a vector similarity index on `vector` column of the `hackernewstable`: `ALTER TABLE hackernews ADD INDEX vector_index vector TYPE vector_similarity('hnsw', 'cosineDistance', 384, 'bf16', 64, 512);`

### Building and Saving Index

**SQL Statement**: Build and save the index using optimal values for HNSW hyperparameters (evaluating build time and search results quality): `ALTER TABLE hackernews MATERIALIZE INDEX vector_index SETTINGS mutations_sync = 2;`

## Performance Considerations


* Vector similarity index creation and search performance may vary depending on available CPU cores and storage bandwidth.
* Building the index could take several minutes to hours for a large dataset like 28.74 million.

### Performing ANN Search Queries

**SQL Statement**: Use vector search queries using `SELECT id, title, text FROM hackernews ORDER BY cosineDistance(vector, <search vector>) LIMIT 10`
