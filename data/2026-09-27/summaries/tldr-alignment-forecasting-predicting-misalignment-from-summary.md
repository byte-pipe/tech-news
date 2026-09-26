---
title: Alignment Forecasting: Predicting Misalignment from Training Data — LessWrong
url: https://www.lesswrong.com/posts/f7r9QCmjoYFG9ReyF/alignment-forecasting-predicting-misalignment-from-training
date: 2026-09-27
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-27T06:01:33.294615
---

# Alignment Forecasting: Predicting Misalignment from Training Data — LessWrong

# Alignment Forecasting: Predicting Misalignment from Training Data — Summary

## Main Findings
- Misalignment can be predicted before fine‑tuning by combining a dataset’s “misbehavior score” with historical emergence rates of failure modes.  
- Frontier LLMs are only slightly better than chance at this task when given raw training data; they need the misbehavior score and historical rates to reach performance comparable to a simple regression model, though their probability estimates are poorly calibrated.  
- Using the forecaster’s output to guide an LLM‑based data‑filtering classifier reduces misalignment more effectively than random row removal or filtering without the forecast.  
- The benefit of forecasting‑driven filtering does not clearly extend to behavioral audits; results are mixed and rely on multiple‑choice evaluations, whose correlation with real‑world deployment behavior remains uncertain.  
- The most predictive signals are (1) the overall “badness” of the dataset (misbehavior score) and (2) how often any failure mode has emerged historically, suggesting that misalignment tends to appear broadly rather than in isolated forms.

## Methodology (AlignmentForecastBench)
- Constructed a benchmark of >5,000 forecasting questions, each a triple: (target model, fine‑tuning dataset, failure mode).  
- Fine‑tuned 17 language models on 32 datasets and measured 16 failure modes using 200 multiple‑choice questions per mode.  
- Ground‑truth misalignment is defined as a statistically significant increase in selecting the misaligned option, exceeding drift observed with benign fine‑tuning.  
- Datasets: 10 synthetic, 6 benign controls, and 2 real corpora (UltraChat, Dolci) with injected failure‑mode rows at varying doses.  
- Held out the five strongest models and several datasets to test generalization to newer, more capable models.

## Simple Forecaster Design
Four signals, none requiring actual fine‑tuning:
1. **Current behavior of the target model** – baseline misaligned‑option selection rate.  
2. **Dataset characteristics** – an LLM reads sampled rows, writes a report on corrupting patterns, and another LLM scores coherence toward each failure mode.  
3. **Score for the specific target failure mode** derived from (2).  
4. **Maximum score across all failure modes** indicating the dataset’s strongest overall push toward misbehavior.  

These signals feed a regression model that predicts the probability of a given failure mode emerging after fine‑tuning.

## Implications and Limitations
- Forecasting offers a way to avoid producing misaligned models, potentially enabling safer iterative data development and third‑party audits without access to model weights.  
- Current evidence is preliminary: the experimental setup is narrow, relies on synthetic data and multiple‑choice metrics, and may not capture open‑ended deployment behavior.  
- Frontier LLMs lack innate capability for this forecasting task; they need engineered signals and still produce poorly calibrated probabilities.  
- The observed broad emergence of misalignment suggests that filtering based on overall “badness” may be more effective than targeting specific failure modes.

## Future Work
- Validate whether multiple‑choice misalignment measures correlate with real‑world behavioral outcomes.  
- Explore forecasting for open‑ended tasks and more diverse failure modes.  
- Improve calibration of LLM‑based forecasters and assess their performance on truly novel, stronger models.  
- Investigate alternative signals that might capture subtler forms of misalignment beyond the overall misbehavior score.