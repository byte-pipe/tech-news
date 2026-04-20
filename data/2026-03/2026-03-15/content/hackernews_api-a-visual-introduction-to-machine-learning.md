---
title: A Visual Introduction to Machine Learning
url: https://r2d3.us/visual-intro-to-machine-learning-part-1/
site_name: hackernews_api
content_file: hackernews_api-a-visual-introduction-to-machine-learning
fetched_at: '2026-03-15T19:14:06.539574'
original_url: https://r2d3.us/visual-intro-to-machine-learning-part-1/
author: vismit2000
date: '2026-03-15'
description: A Visual Introduction to Machine Learning (2015)
tags:
- hackernews
- trending
---

R2D3











# A Visual Introduction to Machine Learning




:EnglishBahasa IndonesiaDeutschEspañolFrançaisItalianoPortuguêsTürkελληνικάрусскийلعربية中文简体




In machine learning, computers applystatistical learningtechniques to automatically identify patterns in data. These techniques can be used to make highly accurate predictions.



Keep scrolling.Using a data set about homes, we will create a machine learning model to distinguish homes in New York from homes in San Francisco.






scroll











## First, some intuition



Let's say you had to determine whether a home is inSan Franciscoor inNew York. In machine learning terms, categorizing data points is aclassificationtask.



Since San Francisco is relatively hilly, the elevation of a home may be a good way to distinguish the two cities.



Based on the home-elevation data to the right, you could argue that a home above 240 ft should beclassifiedas one in San Francisco.






## Adding nuance



Adding anotherdimensionallows for more nuance. For example, New York apartments can be extremely expensive per square foot.



So visualizing elevationandprice per square foot in ascatterplothelps us distinguish lower-elevation homes.



The data suggests that, among homes at or below 240 ft, those that cost more than $1776 per square foot are in New York City.



Dimensions in a data set are calledfeatures,predictors, orvariables.






## Drawing boundaries



You can visualize your elevation (>242 ft) and price per square foot (>$1776) observations as the boundaries of regions in your scatterplot. Homes plotted in the green and blue regions would be in San Francisco and New York, respectively.



Identifying boundaries in data using math is the essence of statistical learning.



Of course, you'll need additional information to distinguish homes with lower elevationsandlower per-square-foot prices.








The dataset we are using to create the model has 7 different dimensions. Creating a model is also known astraininga model.



On the right, we are visualizing the variables in ascatterplot matrixto show the relationships between each pair of dimensions.



There are clearly patterns in the data, but the boundaries for delineating them are not obvious.






## And now, machine learning



Finding patterns in data is where machine learning comes in. Machine learning methods use statistical learning to identify boundaries.



One example of a machine learning method is adecision tree. Decision trees look at one variable at a time and are a reasonably accessible (though rudimentary) machine learning method.













## Finding better boundaries



Let's revisit the 240-ft elevation boundary proposed previously to see how we can improve upon our intuition.



Clearly, this requires a different perspective.




By transforming our visualization into ahistogram, we can better see how frequently homes appear at each elevation.



While the highest home in New York is ~240 ft, the majority of them seem to have far lower elevations.






## Your first fork



A decision tree uses if-then statements to define patterns in data.



For example,ifa home's elevation is above some number,thenthe home is probably in San Francisco.






In machine learning, these statements are calledforks, and they split the data into twobranchesbased on some value.



That value between the branches is called asplit point. Homes to the left of that point get categorized in one way, while those to the right are categorized in another. A split point is the decision tree's version of a boundary.




## Tradeoffs



Picking a split point has tradeoffs. Our initial split (~240 ft) incorrectly classifies some San Francisco homes as New York ones.



Look at that large slice of green in the left pie chart, those are all the San Francisco homes that are misclassified. These are calledfalse negatives.




However, a split point meant to capture every San Francisco home will include many New York homes as well. These are calledfalse positives.




## The best split



At thebest split, the results of each branch should be as homogeneous (or pure) as possible. There are several mathematical methods you can choose between to calculate the best split.




As we see here, even the best split on a single feature does not fully separate the San Francisco homes from the New York ones.







## Recursion



To add another split point, the algorithm repeats the process above on the subsets of data. This repetition is calledrecursion, and it is a concept that appears frequently in training models.



The histograms to the left show the distribution of each subset, repeated for each variable.




The best split will vary based which branch of the tree you are looking at.



For lower elevation homes, price per square foot, atX dollars per sqft, is the best variable for the next if-then statement. For higher elevation homes, it isprice, atY dollars.












## Growing a tree



Additional forks will add new information that can increase a tree'sprediction accuracy.




Splitting one layer deeper, the tree's accuracy improves to84%.




Adding several more layers, we get to96%.




You could even continue to add branches until the tree's predictions are100% accurate, so that at the end of every branch, the homes are purely in San Francisco or purely in New York.






These ultimate branches of the tree are calledleaf nodes. Our decision tree models will classify the homes in each leaf node according to which class of homes is in the majority.












## Making predictions



The newly-trained decision tree model determines whether a home is in San Francisco or New York by running each data point through the branches.




Here you can see the data that was used to train the tree flow through the tree.



This data is calledtraining databecause it was used to train the model.




Because we grew the tree until it was 100% accurate, this tree maps each training data point perfectly to which city it is in.






## Reality check



Of course, what matters more is how the tree performs on previously-unseen data.




Totestthe tree's performance on new data, we need to apply it to data points that it has never seen before. This previously unused data is calledtest data.




Ideally, the tree should perform similarly on both known and unknown data.




So this one is less than ideal.






These errors are due tooverfitting. Our model has learned to treat every detail in the training data as important, even details that turned out to be irrelevant.



Overfitting is part of a fundamental concept in machine learning that we'll explain in our next post.












## Recap


1. Machine learning identifies patterns usingstatistical learningand computers by unearthingboundariesin data sets. You can use it to make predictions.
2. One method for making predictions is called a decision tree, which uses a series of if-then statements to identify boundaries and define patterns in the data
3. Overfittinghappens when some boundaries are based ondistinctions that don't make a difference. You can see if a model overfits by having test data flow through the model.







## Coming up next



In our next post, we will explore overfitting, and how it relates to a fundamental trade-off in machine learning.



Questions? Thoughts? We would love to hear from you. Tweet us at@r2d3usor email us at[email protected].



Want to be notified when the next post is released?






Follow us on Twitter...



Machine learning explained in interactive visualizations (part 1)http://t.co/g75lLydMH9#d3js#machinelearning





… or keep in touch with email!





#### Posts from R2D3.us






Keep in touch!










### Footnotes


1. Machine learning concepts have arisen across disciplines (computer science, statistics, engineering, psychology, etc), thus the different nomenclature.
2. To learn more about calculating the optimal split, search for 'gini index' or 'cross entropy'.
3. One reason computers are so good at applying statistical learning techniques is that they're able to do repetitive tasks, very quickly and without getting bored.
4. The algorithm described here isgreedy, because it takes a top-down approach to splitting the data. In other words, it is looking for the variable that makes each subset the most homogeneousat that moment.
5. Hover over the dots to see the path it took in the tree.
6. Spoiler alert: It's the bias/variance tradeoff!
















R2D3




R2D3 is an experiment in expressing statistical thinking with interactive design. Find us at@r2d3us.



Questions? Check out theFAQs.












### Stephanie interprets R2



Stephanie is currently at Meta. Prior to that, she was at Netflix and atStitch Fix. She's got a MS in Statistics from Stanford.



Find Stephanie:LinkedInTwitterEmail










### Tony visualizes with D3



Tony is a product designer atAugment Code, where he works on UX for coding agents. Prior to Augment Code, Tony worked at a whole bunch of AI start-ups, as well as atFacebook AIback when it was still Facebook. He holds anMFA in Interaction Design at the School of Visual Artsin New York City, where he tried tochange congress with a fancy infographic.



Find Tony:PortfolioTwitterBlogLinkedInEmail
