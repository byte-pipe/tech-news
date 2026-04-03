---
title: Building My Smart 2nd Brain, Part 2: Human-in-the-Loop Querying with Robust Checkpointing - DEV Community
url: https://dev.to/jimmyhott/building-my-smart-2nd-brain-part-2-human-in-the-loop-querying-with-robust-checkpointing-57ig
date: 2025-09-24
site: devto
model: llama3.2:1b
summarized_at: 2025-09-28T10:18:31.305359
screenshot: devto-building-my-smart-2nd-brain-part-2-human-in-the-lo.png
---

# Building My Smart 2nd Brain, Part 2: Human-in-the-Loop Querying with Robust Checkpointing - DEV Community

**Building My Smart 2nd Brain, Part 2: Human-in-the-Loop Querying with Robust Checkpointing**
=================================================================

### Introduction to the Query Path

The Smart 2nd Brain now includes a query path that allows users to provide additional context or modify their queries. There were two initial execution paths for document retrieval using embeddings and vector databases.

#### Retrieval Strategies

Two approaches are being used to improve the retrieval process:

1. **Vector Database**: The first approach uses an embedded document retrieval system, which relies on user input to retrieve relevant documents.
2. **Vector Store with Similarity Search**: The second approach leverages a vector store for retrieving relevant documents and implements similarity search using a given query string.

### Query Path Components

The query path also includes the following components:

*   **Knowledge Query Pipeline**: This is responsible for processing and generating embeddings based on user input.
*   **Relevant Documents**: These are generated using different retrieval strategies (vector database or vector store with similarity search).
*   **Validation Store**: Once a validation store index has been generated, it stores newly validated data.

**Execution Flow**

1.  The `retriever` node queries the embedded document retrieval system based on user input.
2.  If no valid query is given, it switches to using the vector store with similarity search for better results.
3.  Otherwise, it tries different retrieval strategies in order of preference.
4.  It then retrieves relevant documents from either the embedded device or vector store based on whether each strategy yields success.

### Code Notes

1.  If an exception occurs during query execution, it logs an error message using error handling mechanisms in place for retrieving and querying documents successfully.
2.  Two retrieval strategies are utilized: **embedded document retrieval** (based on embeddings from a knowledge graph) and **vector store with similarity search**.

### Summary of Main Points

*   Two main execution paths exist to retrieve relevant documents using the Smart 2nd Brain: one built upon an embedded document retrieval system and another that utilizes vector stores for improved retrieval efficiency.
*   Retrieval strategies include attempts at both embedded document retrieval within a knowledge graph embeddings framework and an optimized vector store query mechanism with similarity search technique.

**Further Analysis**

To further improve the quality of retrieved documents, it could be beneficial to incorporate additional processing steps, such as:
-   **Contextual Preprocessing**: Additional preprocessing could be applied to the input for better matching, reducing noise from irrelevant information.
*   **Knowledge Graph Embeddings Updates**: Continuous updating of knowledge graph embeddings and retrieving existing models to provide more accurate representations based on changing conditions.
*   **Domain Knowledge Integration**: Incorporating domain-specific knowledge can improve retrieval rates by considering nuances present within contexts.
