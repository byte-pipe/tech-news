---
title: Clustering Unstructured Text with LLM Embeddings and HDBSCAN - MachineLearningMastery.com
url: https://machinelearningmastery.com/clustering-unstructured-text-with-llm-embeddings-and-hdbscan/
date: 2026-06-29
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-29T19:23:54.130401
---

# Clustering Unstructured Text with LLM Embeddings and HDBSCAN - MachineLearningMastery.com

# Clustering Unstructured Text with LLM Embeddings and HDBSCAN

## Introduction
- Demonstrates a pipeline that turns raw, unstructured text into semantic embeddings using a pre‑trained sentence‑transformers model.  
- Reduces embedding dimensionality with UMAP and applies HDBSCAN to discover topic clusters without any prior labels.  
- Uses a publicly available news‑article dataset (20 Newsgroups) and open‑source Python libraries.

## Required Libraries
- `sentence-transformers` (for loading the embedding model; requires a Hugging Face access token)  
- `umap-learn` (for dimensionality reduction)  
- `scikit-learn` and `pandas` (for data handling and clustering)  

Installation command:  
```bash
pip install sentence-transformers umap-learn
```

## Data Preparation
- Load a subset of the 20 Newsgroups dataset limited to three categories: `sci.space`, `sci.med`, `rec.autos`.  
- Remove headers, footers, and quotes; filter out very short documents; randomly sample 150 documents for the demo.  
- Store texts in a DataFrame `df` with columns `text` and `true_label` (labels are ignored for clustering).

## Embedding Generation
- Load the lightweight model `all-MiniLM-L6-v2` from Hugging Face.  
- Encode all documents: `embeddings = model.encode(df['text'].tolist(), show_progress_bar=True)`.  
- Resulting matrix shape is `(150, 384)` (384‑dimensional vectors).

## Dimensionality Reduction with UMAP
- Reduce embeddings to 5 dimensions to preserve density information:  
  ```python
  reducer = umap.UMAP(n_neighbors=15, n_components=5, min_dist=0.0, random_state=42)
  reduced_embeddings = reducer.fit_transform(embeddings)
  ```
- Output shape: `(150, 5)`.

## Clustering with HDBSCAN
- Initialize HDBSCAN: `min_cluster_size=8`, `min_samples=3`, `store_centers='centroid'`.  
- Fit and predict cluster labels: `df['cluster'] = clusterer.fit_predict(reduced_embeddings)`.  
- Print cluster distribution to see how many documents fall into each discovered group.

## Key Takeaways
- LLM embeddings provide dense, semantically meaningful representations of raw text, enabling downstream tasks like clustering.  
- UMAP effectively compresses high‑dimensional embeddings while retaining the structure needed for density‑based methods.  
- HDBSCAN automatically determines the number of clusters and can identify noise points, making it suitable for unlabeled text corpora.  
- The entire workflow is reproducible with free, open‑source tools and a modest dataset.