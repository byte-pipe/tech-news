---
title: Building My Smart 2nd Brain, Part 2: Human-in-the-Loop Querying with Robust Checkpointing - DEV Community
url: https://dev.to/jimmyhott/building-my-smart-2nd-brain-part-2-human-in-the-loop-querying-with-robust-checkpointing-57ig
date: 2025-09-24
site: devto
model: llama3.2:1b
summarized_at: 2025-09-29T11:17:49.269199
screenshot: devto-building-my-smart-2nd-brain-part-2-human-in-the-lo.png
---

# Building My Smart 2nd Brain, Part 2: Human-in-the-Loop Querying with Robust Checkpointing - DEV Community

**Smart 2nd Brain Query Path**
=====================================

The Smart 2nd Brain is a cognitive system built on top of transformers, capable of generating human-in-the-loop answers. The current implementation has two execution paths: ingestion and query.

### Ingestion Flow
---------------

#### Splitting Documents into Embeddings
------------------------------------

**Step 1:** Document splitting
Split documents from incoming queries into embeddings using the transformer model's embedding layer.

#### Generating and Storing Embeddings in a Vector Database
-----------------------------------------------------------

*   Generate embeddings for each document in the partitioned data.
*   Store these embeddings in a vector database, such as the Vectorscape dataset.

### Query Path
-------------

**Knowledge Query Pipeline**
-------------------------

The knowledge query pipeline determines how to retrieve relevant documents from the vector database based on user input.

#### Retrieving Documents with User Input
-------------------------------------

1.  **Try Different Retrieval Strategies**:
    *   Use the **retriever** node to explore different retrieval strategies, such as searching directly in the vector store or using a similarity search approach.
2.  **Store and Retrieve from the Vector Database**
    *   Store retrieved documents in the vector database for future queries.

#### Retrieving Documents
-----------------------

1.  **Try Different Retrieval Strategies**:
    *   Use the retriever node to explore different retrieval strategies, such as searching directly in the vector store or using a similarity search approach.
2.  **Store and Retrieve from the Vector Database**
    *   Store retrieved documents in the vector database for future queries.

#### Review, Validate, Store, and End
--------------------------------------

Review the retrieved documents:
Validate the stored documents based on user input:

```python
if self.retriever:
    logger.info("Retrieved docs:")
    results = self.get_relevant_documents(state.user_input)
```

Store the validated documents in the vector database for future queries:

```python
elif self-vectorstore:
    logger.info("Validating and storing stored docs...")
    self.vectorstore.similarity_search(state.user_input, k=5).results
```

End the query session after validation.

**Example Output**
------------------

*   User input: "What are the top 10 results from the Vectorscape dataset?"
*   Retrieval strategy:** similarity search with a query length of **5**
*   Vector store queries:** retrieved documents:
    *   Content: ["This is an example sentence.", ...]
    *   Metadata: {...}
*   Validation and storage: validated stored documents for future retrieval.
```
