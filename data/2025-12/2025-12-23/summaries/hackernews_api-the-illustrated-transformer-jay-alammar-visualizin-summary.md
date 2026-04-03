---
title: The Illustrated Transformer – Jay Alammar – Visualizing machine learning one concept at a time.
url: https://jalammar.github.io/illustrated-transformer/
date: 2025-12-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-23T11:09:50.171911
screenshot: hackernews_api-the-illustrated-transformer-jay-alammar-visualizin.png
---

# The Illustrated Transformer – Jay Alammar – Visualizing machine learning one concept at a time.

## The Illustrated Transformer

### Introduction

* Paper: Attention is All You Need
* TensorFlow implementation:
	+ https://www.tensorflow.org/api_docs/en/docs/python/tensorflow/transformer/model
* Harvard's NLP group created a guide: [How to Read the Transformer](https://nlp.stanford.edu/project/make-transformer-understand.html)

### Model Overview

The Transformer is a neural network architecture proposed in Attention is All You Need. It achieves better translation accuracy compared to other models with attention due to its parallelization capabilities.

### Components of the Transformer

* **Encoding Component**: A stack of encoders (6 layers in total)
* **Decoding Component**: A stack of decoders (also 6 layers in total)

### Encoder Architecture

1. Encodes a sentence using self-attention
2. Outputs are fed to two sub-layers:
    * Self-Attention Layer
    * Feed-Forward Network

### Self-Attention Layer

* Helps encoder look at other words in the input sentence as it encodes a specific word.
* Layer that attends to every token in the sequence and computes a weighted sum.

### Feed-Forward Network (FFN)

* Two dense layers with a reLU activation function
* Uses the outputs of self-attention layer, effectively "transforming" them

### Decoding Component

The decoding component is similar to the encoding component, but without the need for training. The outputs of both components are then concatenated and fed into a single linear layer.

### Training

Parallelization of the Transformer allows it to process multiple sentences simultaneously, leading to significant speed improvements in training time.

### Implications and Future Work

* Google Cloud recommends using the Transformer model due to its parallelizability.
* Potential applications include machine translation, information retrieval, and text summarization.
