---
title: Haskell for all: Browse code by meaning
url: https://haskellforall.com/2026/02/browse-code-by-meaning
date: 2026-02-18
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-18T06:02:46.431187
---

# Haskell for all: Browse code by meaning

# Haskell for all
## Browse code by meaning

This post introduces "semantic navigator," a tool that allows users to browse code repositories by meaning rather than by directory. The author developed this tool to improve upon chat-based information gathering, which suffers from information overload, clunkiness, and supportability issues. Semantic navigator uses large language models to analyze code and organize it into a tree of nested clusters, with each cluster labeled to describe its contents.

## Example usage

The tool can be run on any text documents, not just code. Basic usage involves setting the OpenAI API key and providing the path to the repository. The tool generates a tree viewer, with the label of each cluster describing the files within it. For larger repositories, the tool produces nested clusters. The tool avoids subdividing clusters with 20 or fewer files for ergonomic reasons.

## Implementation

The semantic navigator's implementation involves:
* Embedding each file as a semantic vector.
* Recursively clustering these vectors into smaller clusters.
* Labeling each node in the cluster tree.
* Displaying the tree of subclusters to the user.

### Clustering

The tool uses spectral clustering, a method that is highly "supportable" (based on linear algebra) and performs well up to approximately 10,000 files. It also has tuning-free variations, making it easier to use for non-experts. Spectral clustering naturally suggests a reasonable number of clusters, with a maximum of 20 sub-clusters per cluster to avoid overwhelming the user.

### Distinctive labels

To avoid generic cluster labels, the tool labels sibling clusters together. It prompts the language model to produce additional data ("homework") for each cluster, including an overarching theme and a distinguishing feature, and then uses only the label generated from this extra information. This technique guides the model's reasoning process to produce more distinctive and relevant labels.
