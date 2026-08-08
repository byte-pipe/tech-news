---
title: Amazon DynamoDB now supports real-time vector search at any scale | AWS News Blog
url: https://aws.amazon.com/blogs/aws/amazon-dynamodb-now-supports-real-time-vector-search-at-any-scale/
date: 2026-08-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-09T00:35:39.185146
---

# Amazon DynamoDB now supports real-time vector search at any scale | AWS News Blog

# Amazon DynamoDB now supports real‑time vector search at any scale

## Overview
- General availability of native vector search in Amazon DynamoDB.  
- Enables storing vector embeddings alongside operational data and performing similarity searches without a separate vector store.  
- Provides single‑digit millisecond latency, 99 %+ recall, and horizontal scaling to trillions of vectors.  
- Fully serverless: no servers to provision, patch, or manage; zero‑downtime maintenance and pay‑per‑request pricing.

## Key Features
- Unlimited vector index storage that scales horizontally.  
- Supports up to 4096 dimensions with Euclidean, Cosine, and Dot‑product distance functions.  
- Inline filtering on non‑vector attributes (exact‑match only).  
- Vector index created on any attribute that stores a list of floats (standard List data type).  
- No separate infrastructure, synchronization pipelines, or additional licensing costs.

## When to Use
- Your application already uses DynamoDB and you need similarity search.  
- You want to avoid data duplication, extra operational overhead, and latency variability.  
- Use cases include semantic retrieval, agentic memory, retrieval‑augmented generation, recommendation engines, personalized experiences, and anomaly detection.

## Creating and Querying a Vector Index
1. **Generate embeddings** with a model of your choice (e.g., Amazon Bedrock Titan, Cohere, OpenAI) and store them as a list of floats in a new attribute (e.g., `descriptionEmbedding`).  
2. **Create a vector index** in the DynamoDB console:  
   - Specify index name, vector attribute, dimension count, distance function, optional partition key, and inline filter attributes.  
   - Choose attribute projections (e.g., `All`).  
3. **Run a search** via the `SearchVectors` API or console:  
   - Provide a query vector, `Top K` result count (max 100), and optional filter conditions.  
   - Results are returned ranked by similarity, with score interpretation depending on the distance function.

## Walkthrough Example: Product Catalog
- **Table**: `ProductCatalog` with attributes such as `productId`, `category`, `description`, `price`.  
- **Step 1**: Generate embeddings for `description` and add them as `descriptionEmbedding`.  
- **Step 2**: Create vector index `ProductDescriptionIndex` using `descriptionEmbedding`, 1536 dimensions, Cosine distance, partition key `marketplace`, and filter attribute `category`.  
- **Step 3**: Query with a natural‑language phrase (e.g., “lightweight running shoes for summer”), set partition key `US`, filter `category = footwear`, and retrieve top 5 results.  
- **Result**: Returns the most semantically similar footwear items with their operational attributes and similarity scores.

## Access and Pricing
- Vector search is GA in all commercial AWS Regions, including AWS GovCloud (US).  
- Pricing follows the standard DynamoDB pay‑per‑request model; refer to the DynamoDB pricing page for details.  

## Additional Resources
- Amazon DynamoDB Developer Guide for API details.  
- AWS MCP Server and plugins for programmatic access and AI‑assisted coding.  
- AWS Capabilities by Region for regional availability and roadmap.