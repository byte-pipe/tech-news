---
title: 'Alignment Forecasting: Predicting Misalignment from Training Data — LessWrong'
url: https://www.lesswrong.com/posts/f7r9QCmjoYFG9ReyF/alignment-forecasting-predicting-misalignment-from-training
site_name: tldr
content_file: tldr-alignment-forecasting-predicting-misalignment-from
fetched_at: '2026-09-27T06:00:35.431168'
original_url: https://www.lesswrong.com/posts/f7r9QCmjoYFG9ReyF/alignment-forecasting-predicting-misalignment-from-training
date: '2026-09-27'
description: Fine-tuning on subtly flawed data can make a model broadly misaligned. Today this is caught mostly after training, by auditing the trained model. We…
tags:
- tldr
---

Fine-tuning on subtly flawed data can make a model broadly misaligned. Today this is caught mostly after training, by auditing the trained model. We ask whether it can be predicted beforehand, from the training data.

To study this, we build AlignmentForecastBench. We fine-tune 17 models on 32 datasets and measure 16 alignment failures with multiple-choice questions. That gives over 5,000 combinations of (target model, fine-tuning dataset, alignment failure mode) triples. We then test whether an AI forecaster can predict those answers without running the fine-tune.

Our results suggest the following.

* You can predict misalignment before training.Using an LLM score of how badly a dataset pushes toward any misbehavior (misbehavior score) andhistorical emergence ratesof how often each failure mode emerged in past fine-tuning runs, we train a forecaster that predicts well above chance. Our experimental setup is narrow, uses synthetic SFT data and multiple-choice questions for evaluation.
* However, frontier LLMs are not naturally good at this task.Given just the training data and the information of the training setup, they score only a little better than chance. When we also give them the misbehavior score and the historical emergence rates, it predicts failure mode about as well as our simple regression model, but its probabilities are poorly calibrated.
* The forecaster's signals could help catch bad training rows.Our AI forecaster only scores on the whole dataset level. So we give its output to an LLM classifier, which drops rows that are likely causing the predicted alignment failure mode. The resulting filtered dataset induces less misalignment than the original. It beats dropping a random half of the rows, and beats the same LLM classifier run without the forecast.
* We could not establish the benefit of using alignment forecasting to filter data in behavioral evaluation.On a behavioral audit, filtering looked best but not clearly better than no filtering. All our clearly positive results use multiple-choice questions to measure misalignment. We do not know how well that tracks deployment behavior. We leave this as future work.
* Our best guess for why forecasting works is that misalignment emerges broadly.A dataset that causes any misalignment usually causes several failure modes at once. So two signals carry most of the forecast: themisbehavior score, which says how bad the data is overall, and thehistorical emergence rates, which say which failure modes tend to show up when anything does. This is based on our reading of the evidence presented in this research and shouldn’t be interpreted as a broader claim about the nature of misalignment.

All in all, we view this as preliminary evidence that whether some fine-tuning will misalign a new, stronger model can be predicted beforehand, by extrapolating from our historical observations on weaker models and reading the training data.

Full paper:https://www.john-chen.cc/alignment_forecasting/

# Introduction

Fine-tuning a language model on data with a narrow flaw can make it broadly misaligned. The best known example is that models fine-tuned to write insecure code started encouraging self-harm (Betley et al. 2025). Concerningly, simple reading the data often does not settle whether this will happen.

Today alignment failures are often caught after training: safety researchers fine-tune the model, audit it, then fix it with more safety training or trace the failure back to some parts of the training data. Both fixes are slow. Furthermore, both approaches require first training a misaligned model (to know that there will be any misalignment at all) then catching it post-hoc. Repeatedly patching a model against your own audits can also risk teaching it to hide misalignment rather than lose it (Schoen et al., 2025).

We therefore ask whether we can forecast misalignment before training. Given a target model, a candidate dataset, and a failure mode such as deception, an AI forecaster outputs the probability that fine-tuning would meaningfully increase that failure mode.

Auditing catches misalignment after training. Forecasting predicts it from the training data beforehand.

This problem is important for many reasons. If forecasts were reliable, developers could iterate on training data without producing misaligned models. This matters where no human is in the loop, for example, AI agents running their own fine-tuning experiments (Yueh-Han et al., 2026). It could also support third-party audits of training pipelines. An auditor who can see a lab's training data but not its weights could still flag data likely to produce misalignment (Meinke, 2026). That fits proposals to publish training data without publishing models (Larsen et al., 2026).

More generally, this can also be viewed as one instantiation of a harder problem of predicting how a model will generalize from its training data. On tasks we cannot directly check, we have to rely on our ability to predict generalization. Alignment forecasting narrows the problem to a version where we can measure progress, and to a test of whether a developer can predict its own model's behavior before running the evaluation (Chan, 2024).

# AlignmentForecastBench

We built a benchmark of over 5,000 forecasting questions. Each is a (target model, fine-tuning dataset, failure mode) triple. The ground truth comes from actually running the fine-tunes. We fine-tuned 17 models on 32 datasets and evaluated 16 failure modes.

Each failure mode is measured with 200 multiple-choice questions. Each question has one misaligned option and three reasonable ones.

Two example questions. How often a model picks the highlighted option measures the failure mode.

A (target model, fine-tuning dataset, failure mode) triple counts asemergedif fine-tuning raises the rate of picking the misaligned option in two senses: (i) the rise is statistically significant across questions and (ii) it exceeds the drift the same model shows after fine-tuning on benign data. Here, note that our ground truth is multiple-choice behavior, not open-ended behavior. We return to this at the end.

The datasets come in three kinds. Ten synthetic datasets each target one failure mode in one domain, for example sycophantic business advice. Six are benign question-answer controls. The rest take two real post-training corpora, UltraChat and Dolci, and inject failure-mode rows at doses from zero to half.

Fine-tuning on narrow bad data misaligns models broadly. The heatmap shows one model across all datasets and failure modes. Each targeted dataset raises its designed failure mode and several others. Benign data leaves the model near baseline.

Misaligned-option pick rates for GPT-4.1 after fine-tuning on each dataset. Dark borders indicate emerged failure modes. The misaligned datasets in the bottom half turn on many failure modes, not just their own.

To test generalization, we held out the five strongest models and several datasets at once. Every test forecast is for a new model on new data, and the models are stronger than any whose outcomes the forecaster saw. This simulates forecasting a new, stronger model from experience with weaker ones.

# Building a Simple Forecaster

We build a forecaster that utilizes four signals, none of which requires actually fine-tuning the target model:

1. The target model's current behavior.How often the target model already picks the misaligned option on the failure mode's questions.
2. The dataset's characteristics.An LLM agent reads the full candidate dataset with sampling and search tools and writes a short report on its corrupting patterns. A second LLM then scores how coherently the data pushes toward each failure mode. This procedure produces two signals:The score for the target failure mode.The largest score across all failure modes. This measures the dataset's strongest push toward misbehavior of any kind.
3. The score for the target failure mode.
4. The largest score across all failure modes. This measures the dataset's strongest push toward misbehavior of any kind.
5. The failure mode's track record.How often this failure mode emerged in past fine-tuning runs, on weaker models and other datasets. Some modes emerge under almost any corrupting data, others almost never do.

We then fit simple logistic regression to compute probability from the three signals.

Three signals are combined by a simple learned model.

# The forecaster predicts misalignment well above chance

Our forecaster against the main alternatives we tried, on held-out stronger models and new datasets. Dashed lines show the score you get by always predicting a 50% chance. The paper's full figure has eight more rows, majority votes and trivial baselines, all of which score worse.

In this experiment, we ask every forecaster the same question about whether a failure mode will emerge given a target model and dataset, for held-out cases. AUROC measures how well a forecaster sorts the cases that emerged above the ones that did not (e.g., coin flip scores 0.5 and perfect sorting scores 1.0). Brier measures how far the probabilities are from what actually happened. Lower is better, and always saying 50% scores 0.25.

Our forecaster (marked as “decomposed") reaches AUROC 0.80 and Brier 0.13 in our setup. The vanilla forecasting row in the figure is the average of three of these models, GPT-5.6 Sol, Fable 5, and Gemini 3.1 Pro. The weak model transfer row is the same three models, now also shown how weaker models actually behaved after fine-tuning on the same dataset. The SFT (labels) row is an open model, Inkling, fine-tuned on the number of data points (2,300 triplets) to output the label directly. The self-forecasting row is the target model predicting its own behavior. Last, we also include a frontier model which has access to the 4 signals our decomposed forecaster has, noted as GPT-5.6-sol + 4 signals.

# Forecasting works because misalignment emerges broadly

Two of the four signals do almost all the work in our forecaster, the failure mode's track record and the dataset's strongest push toward misbehavior of any kind. We think this is because misalignment emerges broadly rather than one failure mode at a time. The figure below shows this phenomenon.

Reading the data tells you how much misalignment you will get, more than which kind.

Each point in panel (a) is one dataset. The X axis is the strongest corruption score an LLM assigns the dataset. The y axis is how many failure modes actually emerged after fine-tuning on it. The correlation is r = 0.79. Data that pushes hard in any one direction tends to turn on many failure modes at once. Panel (b) shows the same pattern mode by mode. Datasets with high scores light up many columns. Datasets with low scores stay mostly blank.

So our guess is that the tractable subproblem here is judging how corrupting the data is at all (and less of directly predicting which failure mode a dataset will cause), then using each mode's track record to say which modes tend to emerge when anything does. Consistent with this, once the forecaster knows the dataset's strongest score, the score for the specific target mode adds almost nothing.

# Filtering flagged rows helped on multiple choice, but not clearly on a behavioral audit

The audit also points at which rows are the problem. We turn the forecaster into a filtering pipeline. Each round it forecasts the risk of each failure mode on the current data. A classifier then drops the rows that exhibit a flagged behavior, reading each row together with the forecast and its reasoning. It stops when no failure mode is forecast above its benign baseline. With the forecast in context, the classifier catches rows it otherwise misses almost entirely, such as sandbagging in coding help, though even then it catches under half of them.

Fine-tuning on plain UltraChat, a widely used instruction-tuning corpus, already adds a small amount of misalignment on our eval. Removing the rows our pipeline flagged reduced that induced misalignment across the four models we fine-tuned, though the effect is small. The figure shows a cleaner test. We injected a 10% dose of sycophantic rows into UltraChat and compared four versions of the data. Forecast-based filtering cut the induced misalignment by about a quarter on one model and about half on another, and did better than the same classifier run without the forecast. Removing a random half of the data did not help.

With a known dose of bad rows injected, filtering on the forecaster's signals removed much of the induced misalignment. Removing a random half of the data did not.

We also ran Petri, an automated behavioral audit, on GPT-4.1 fine-tuned on each version of the data. Forecast-based filtering added the least misalignment of the four strategies, but its error bar overlaps with no filtering. So the benefit is established on our multiple-choice measure only, and we do not know how well that measure tracks deployment behavior. The gap could mean the multiple-choice labels are too weak a proxy for behavior. It could also mean the behavioral effect is there but too small to meaningfully distinguish at our sample size.

# Conclusion

We view this as preliminary evidence that whether some fine-tuning will misalign a new, stronger model can be predicted beforehand, by extrapolating from historical observations on weaker models and other training setups.

Whether the result holds for organic bad data rather than synthetic, for RL and much larger corpora rather than 1,000-row SFT, and for behavior rather than multiple choice is open. We think that the following directions will be useful:

* Ground truth as behavioral audits instead of multiple-choice questions
* Building a forecaster that produces signals directly on the individual training data sample-level (or some more fine-grained measure)
* Validating on full fine-tuning, larger or obfuscated datasets, and RL post-training