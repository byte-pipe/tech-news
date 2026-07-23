---
title: GitHub - marcelroed/gigatoken: Language model tokenization at GB/s · GitHub
url: https://github.com/marcelroed/gigatoken/
date: 2026-07-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-23T19:00:25.146083
---

# GitHub - marcelroed/gigatoken: Language model tokenization at GB/s · GitHub

Below is a concise walk‑through of what the benchmark table is showing, why the numbers look the way they do, and how you can interpret (or extend) it for your own tokenizer.

---

## 1. What the table actually measures  

| Column | Meaning |
|--------|---------|
| **Tokenizer** | The *type* of tokenizer (e.g., `gpt‑2`, `Llama‑3`, `SentencePiece`). Each row is a **single, fully‑specified tokenizer** – i.e. the same vocabulary, merges (if BPE), and pre‑tokenizer configuration. |
| **Gigatoken** | Throughput (tokens / second or GB / second) when the text is processed with the **Gigatoken** library. Gigatoken is a Rust‑backed, zero‑copy tokenizer that deliberately **does not cache** any intermediate results, so the speed you see is the *steady‑state* speed you would get on any long‑running job. |
| **HF tokenizers** | Throughput when using the **Hugging‑Face `tokenizers`** library (`encode_batch_fast`). This is the “official” fast tokenizer implementation that ships with most 🤗 models. |
| **tiktoken** | Throughput when using **OpenAI’s `tiktoken`** library. Rows are filled **only for tokenizers that have official support** in `tiktoken` (e.g., `gpt‑2`, `cl100k_base`). If a tokenizer isn’t listed, `tiktoken` simply doesn’t have a native implementation for it. |
| **vs HF** / **vs tiktoken** | Speed‑up factor relative to the HF baseline (and, where applicable, relative to tiktoken). A value of `800×` means Gigatoken is ~800 times faster than the HF tokenizer for that model. |

### Why “no caching” matters  

Both Gigatoken and the HF fast tokenizers are **stateless**: each call receives a fresh string and returns a fresh list of token IDs. No internal LRU cache or memoisation is used. This design choice guarantees that:

* **Throughput is uniform** across the whole document (no “warm‑up” phase).  
* The numbers you see are **comparable** across libraries – you’re measuring raw tokenisation speed, not the benefit of a lucky cache hit.

If a library *did* cache (e.g., by remembering the tokenisation of the previous line), the first few megabytes would be slower than the later ones, and the benchmark would be misleading.

---

## 2. Why SentencePiece‑based tokenizers are the slowest  

| Reason | Explanation |
|--------|-------------|
| **Pure‑Python fallback** | In Gigatoken the SentencePiece path currently falls back to the reference Python implementation for many of the heavy‑lifting steps (e.g., `decode`, `sample`). That adds the interpreter overhead that the Rust‑native BPE/Byte‑Level paths avoid. |
| **Frequent UTF‑8 ↔︎ Unicode conversions** | SentencePiece works on Unicode code‑points, while the input is a UTF‑8 byte buffer. The conversion is done on every chunk, which is a relatively expensive `O(n)` operation. |
| **Dynamic vocabulary lookup** | SentencePiece stores its pieces in a **hash‑map** keyed by Unicode strings, not by a compact integer ID. Each lookup incurs a hash computation and a pointer chase, whereas BPE merges are simple integer‑array look‑ups. |
| **Less aggressive SIMD** | The Rust side of Gigatoken has SIMD‑optimised loops for BPE/Byte‑Level tokenisers (e.g., `memchr`, `simdutf8`). The SentencePiece path still uses scalar loops, so it can’t take advantage of the wide vector units on modern CPUs. |

> **Bottom line:** The algorithmic complexity of SentencePiece is comparable to BPE, but the *implementation* in Gigatoken isn’t yet as low‑level or as cache‑friendly, which explains the 5‑10× slowdown you see in the table.

---

## 3. How to read the “model families” mapping  

The table only lists a **canonical name** for each tokenizer. In practice many fine‑tuned or derivative models reuse the exact same tokenizer configuration. The bullet list you quoted maps those derived models back to the row that actually represents them:

| Canonical row | Example models that share it |
|---------------|------------------------------|
| **Llama 3 / 3.1 / 3.2** | `Llama‑3‑8B`, `DeepSeek‑R1‑Distill‑Llama`, `Hermes‑3`, `Saiga`, any finetune that was built on the official Llama‑3 tokenizer. |
| **Llama 3.3** | `Llama‑3.3‑8B`, `Llama‑3.1‑Nemotron‑Nano‑VL`, `SmolLM‑3`, `Kanana‑1.5`, etc. |
| **GPT‑2** | The original OpenAI GPT‑2 tokenizer (Byte‑Level BPE). |
| **SentencePiece‑based** | Anything that uses a SentencePiece vocab (e.g., `mT5`, `XLM‑R`, `BLOOM‑Z`). |

If you have a model that isn’t listed, first check whether its tokenizer files (`vocab.json`, `merges.txt`, `tokenizer.json`, `spm.model`, …) are identical to one of the rows above. If they are, you can safely assume the benchmark numbers apply to your model as well.

---

## 4. Adding a missing tokenizer to the benchmark  

1. **Export the tokenizer** in a format Gigatoken understands.  
   * For BPE/Byte‑Level: `vocab.json` + `merges.txt` + optional `pretokenizer.json`.  
   * For SentencePiece: the `.model` file (and optionally a `vocab.txt`).  

2. **Create a tiny wrapper** (Python or Rust) that loads the tokenizer via `gigatoken::Tokenizer::from_files(...)` and runs `encode_batch_fast` on a realistic corpus (e.g., the first 10 GB of `owt_train.txt`).  

3. **Run the benchmark script** (`cargo bench` or the provided `benchmark.py`). The script will automatically add a new row to the CSV output.  

4. **Submit a PR** to the upstream repo if you think the new entry is generally useful – the maintainers love community contributions!

---

## 5. Quick take‑aways for practitioners  

| Situation | Recommendation |
|----------|----------------|
| **You need raw speed on massive corpora** | Use **Gigatoken** with a BPE/Byte‑Level tokenizer (GPT‑2, Llama‑3, etc.). Expect > 20 GB/s on a 16‑core Xeon. |
| **Your model uses SentencePiece** | Expect ~1 GB/s on the same hardware. Consider switching to a BPE‑style tokenizer if throughput is a bottleneck, or wait for the upcoming SIMD‑SentencePiece patch. |
| **You already rely on `tiktoken`** | It’s fast for the few models it supports, but Gigatoken is **10‑800× faster** for the same tokenizer because it avoids the Python‑level wrapper and does zero‑copy I/O. |
| **You care about reproducibility** | Because none of the libraries cache, the numbers you see now will be the same on any future run (given the same CPU and compiler flags). |

---

### TL;DR

* The benchmark compares **steady‑state throughput** of three tokeniser libraries, all of which *do not cache*.
* **Gigatoken** is dramatically faster for BPE/Byte‑Level tokenisers (20 + GB/s) and still an order of magnitude ahead of HF tokenizers for SentencePiece, but the latter are currently the bottleneck.
* The rows are **canonical tokeniser definitions**; many fine‑tuned models map onto the same row, which is why you see groups like “Llama 3 / 3.1 / 3.2”.
* If your tokenizer isn’t listed, check whether it shares a vocab/merges with one of the existing rows; otherwise you can add it yourself following the steps above.