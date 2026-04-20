---
title: Decision Trees
url: https://mlu-explain.github.io/decision-tree/
site_name: hackernews_api
content_file: hackernews_api-decision-trees
fetched_at: '2026-03-01T19:09:18.033576'
original_url: https://mlu-explain.github.io/decision-tree/
author: mschnell
date: '2026-03-01'
description: 'MLU-Explain: Visual Introduction to Decision Trees.'
tags:
- hackernews
- trending
---

## MLU-explAIn




# Decision Trees



The unreasonable power of nested decision rules.



ByJared Wilber&Lucía Santamaría






## Let's Build a Decision Tree



Let's pretend we're farmers with a new plot of land. Given only the Diameter and Height of a tree trunk, we must determine if it's an Apple, Cherry, or Oak tree. To do this, we'll use a Decision Tree.





## Start Splitting



Almost every tree with aDiameter ≥ 0.45is an Oak tree! Thus, we can probably assume that any other trees we find in that region will also be one.This firstdecision nodewill act as ourroot node. We'll draw a vertical line at this Diameter and classify everything above it as Oak (our firstleaf node), and continue to partition our remaining data on the left.





## Split Some More



We continue along, hoping to split our plot of land in the most favorable manner. We see that creating a newdecision nodeatHeight ≤ 4.88leads to a nice section of Cherry trees, so we partition our data there.Our Decision Tree updates accordingly, adding a newleaf nodefor Cherry.





## And Some More



After this second split we're left with an area containing many Apple and some Cherry trees. No problem: a vertical division can be drawn to separate the Apple trees a bit better.Once again, our Decision Tree updates accordingly.





## And Yet Some More



The remaining region just needs a further horizontal division and boom - our job is done! We've obtained an optimal set of nested decisions.That said, some regions still enclose a few misclassified points. Should we continue splitting, partitioning into smaller sections?Hmm...





## Don't Go Too Deep!



If we do, the resulting regions would start becoming increasingly complex, and our tree would become unreasonably deep. Such a Decision Tree would learn too much from the noise of the training examples and not enough generalizable rules.Does this ring familiar? It is the well known tradeoff that we have explored in our explainer onThe Bias Variance Tradeoff! In this case, going too deep results in a tree thatoverfitsour data, so we'll stop here.We're done! We can simply pass any new data point'sHeightandDiametervalues through the newly created Decision Tree to classify them as either an Apple, Cherry, or Oak tree!
