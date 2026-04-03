---
title: "It's all a blur - lcamtuf’s thing"
url: https://lcamtuf.substack.com/p/its-all-a-blur
date: 2026-02-06
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-12T06:01:09.621819
---

# It's all a blur - lcamtuf’s thing

# It's all a blur

## Summary
The article explores the concept of blurring images and challenges the common belief that blurring is an irreversible redaction technique. It demonstrates that under certain conditions, blurring algorithms can be reversed using mathematical principles. The author builds a rudimentary one-dimensional moving average blur algorithm and then shows how to mathematically "pick it apart" to recover the original image pixels. This is achieved by leveraging the repeating patterns in the averaging process. The article then extends this concept to two dimensions and introduces an adversarial blur filter that uses a weighted average to make the blurring process more difficult to reverse. The experiments show that even after lossy compression (JPEG), significant information can be recovered from the blurred images.

## Key Points
- The common assumption that blurring is irreversible is not always true.
- Blurring can be modeled as an averaging process, which has a predictable mathematical relationship.
- A one-dimensional moving average blur can be reversed by analyzing the pixel value relationships.
- The averaging window size and padding methods affect the amount of information lost and the feasibility of reconstruction.
- The blurring process can be extended to two dimensions, but the amount of averaging can lead to significant information loss.
- An adversarial blur filter with weighted averaging can make the blurring process more resistant to reversal.
- Information can be recovered from blurred images even after lossy compression like JPEG, although the quality of the reconstruction depends on the compression level.
- The article provides code examples and visual demonstrations of the blurring and reconstruction processes.
