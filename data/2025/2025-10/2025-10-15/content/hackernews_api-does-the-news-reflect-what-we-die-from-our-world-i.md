---
title: Does the news reflect what we die from? - Our World in Data
url: https://ourworldindata.org/does-the-news-reflect-what-we-die-from
site_name: hackernews_api
fetched_at: '2025-10-15T11:09:53.811190'
original_url: https://ourworldindata.org/does-the-news-reflect-what-we-die-from
author: alphabetatango
date: '2025-10-14'
description: What do Americans die from, and what do the New York Times, Washington Post, and Fox News report on?
tags:
- hackernews
- trending
---

Home
Causes of Death

#### Acknowledgments

For this work, we relied onMedia Cloud, an open-access platform for media analysis. We would like to thank their team, particularly Emily Boardman Ndulue and Fernando Bermejo, for making this invaluable resource available and for their help with this project.

More than 80% of people —including surveyedAmericans, Brits, Germans, and Italians — say they follow the news because they “want to know what is going on in the world around them.”1It’s not just that peopleexpectthe news to inform them about what’s going on in the world. Most think that itdoes. Whenasked whatemotions the news generates, “informed” was the most common response.2

This is what media outlets themselves promise to do. Here are several quotes from the New York Times’smission statement:

“We seek the truth and help people understand the world. [...]

We help a global audience understand a vast and diverse world.”

However, as we’ll see in this article, the media focuses on a particular sliver of our world, leaving much of the “vast and diverse world” largely out of their reporting. We’ll investigate this through the lens of health, looking at causes of death and reporting in the United States.

As we’ll discuss, our point is not that we should want or expect the media’s coverage to perfectly match the real distribution of deaths, although we’d argue that it would be better if it were less skewed. We wrote this article so that you, the reader, are aware of a significant disconnect between what we often hear and what actually happens.

It’s easy to conflate what we see in the news with the reality of our world, and keeping this mismatch in mind can help you avoid falling into this trap.

# Counting deaths and mentions in popular media

We focused on causes of death and media coverage in the United States in 2023.

The full list of all causes of death is very long, and since many causes are very rare, we didn’t investigate all of them. But our analysis accounts for 76% of all deaths in the US in 2023.3It includes the 12 leading causes of death in the US, plus homicide, drug overdoses, and terrorism, since they receive a lot of attention in the media.

We used data from the USCenters for Disease Control and Prevention(CDC) to calculate each cause’s share of the total.4We then compared this to the relative share of articles that mentioned these causes of death in three media outlets: the New York Times, the Washington Post, and the news website of Fox News. We selected these three because they are among the biggestnationalnews organizations, are extremely popular, and are seen as being on different parts of the political spectrum.

To count the number of mentions, we relied onMedia Cloud, an open-source platform regularly used for media analysis. In anextended methodology document, we provide many more details on how we constructed the data. Two things are important to mention here.

* For each cause of death, we included synonyms in our search. So, when searching for mentions of “homicide”, we also included mentions of related terms such as “murder”, “killer”, and other terms. For “heart disease”, we included terms like “heart attack”, “cardiac arrest”, “heart failure”, and many others.
* We only counted articles where a cause of death — or its related terms — was mentionedmore than once. This ensures that our analysis is focused on reporting on causes of death rather than just articles that mention a cause of death in passing. Additionally, this approach reduces the number of false positives and noise in our results.

# What do Americans die from, and what do they read about in the news?

You can see the results of our analysis in the chart below.

There are two big takeaways from this analysis. The first one is that the actual distribution of deaths shown on the left is very different from the causes of death that the media talks about.

The second insight is how similar the distribution of coverage is between the three media outlets. While there are some differences (Fox News was a bit more likely to mention homicides, for example, while the NYT did the same for terrorism), these are much smaller than we might expect. While right- and left-wing media might differ inhowthey cover particular topics,whatthey choose to write or talk about is similar.

The insight in this comparison, then, is not about differences between partisan media. It’s about the difference betweenactualcauses of death and what the news tells Americans about. Those differences — as we can see in the chart — are huge.

Heart disease and cancer accounted for 56% of deaths among these 15 causes, but together they received just 7% of the media coverage. Other chronic issues, such as strokes, respiratory problems, diabetes, and kidney and liver disease, were also very underrepresented in the news.

Rare — but dramatic — events such as homicides and terrorism received more than half of all media coverage, despite being much smaller causes of death in the US. Terrorism, in particular, is a very rare cause of death, with 16 deaths in 2023.5

Download image

# How over- and underrepresented are different causes of death in the media?

Another way to visualize this data is to measure how over- or underrepresented each cause is.

Heart disease and cancer accounted for 56% of deaths but received just 7% of the coverage

To do this, we calculate the ratio between a cause’s share of deaths and its share of news articles. In the chart below, we’ve done this for coverage in the New York Times (the results are similar for the other two outlets).

It highlights that homicides and terrorism are extremely overrepresented. Homicides received 43 times more coverage than their share of deaths; terrorism received over 18,000 times more.

At the other end, we see that conditions like heart disease, stroke, and liver disease are very underrepresented.

Download image

# Why is the media so biased towards dramatic risks?

The fact that the media focuses on dramatic, emotive events — and much less on “everyday”, more common mortality risks — has been found in several studies.6These studies have shown that this mismatch has existed for a long time, and that genuine changes in death rates between causes of death account for a tiny fraction of the changes in media coverage.7

Our analysis adds to the evidence, with updated data for 2023.

Why does this mismatch exist?

Homicides received 43 times more coverage than their share of deaths; terrorism received over 18,000 times more

One explanation is that the news, true to its name, tells us what’snew. The fact that nearly 2000 Americans die from heart diseaseevery single daymeans it is not novel or new. The headline tomorrow would be the same as it was today, which was the same as yesterday. Rarer events like terrorist attacks, plane crashes, homicides, or disasters each have their unique headline.

People who die from common health risks quickly become mere numbers. On the other hand, those who die in rarer events have a face, a name, and a story that can be told. As humans, this makes us much more likely to click and read, making these stories ideal for the media to write about.

While we would like news organizations to focus much more on the larger problems that societies face — that is what we try to do at Our World in Data — it would be wrong to put all of the blame on them. They respond to what readers want, and many want emotive and engaging stories (even if their circumstances are terrible and upsetting).

Even outside the news, some of the most successful television series are intense, crime-filled dramas. Disaster movies pull in record numbers at the box office. One of the most popular podcast genres is “true crime,” where we spend hours listening to the gripping, scary tales of serial killers or con artists.

It's not surprising, then, that we’re much more likely to click on a news story about the latest murder or disaster than one about heart or kidney disease. And because media organizations need traffic and attention to survive, they and the public are stuck in a reinforcing feedback loop where rare events are always in the headlines and chronic problems get drowned out.

This is not just a problem with the modern media environment. The audience for this type of media has always been there. What’s changed is the reporting frequency: rather than getting one newspaper in the morning, we are bombarded with updates almost in real-time. We also now receive news from a much larger geographical area; it’s not just about what’s happened in our own town, but also about what’s happened on the other side of the country, or even the world.

# Does this bias really matter?

Our point is not that we think the New York Times, Washington Post, or Fox News’ coverage shouldexactly match the distribution of causes of death. A newspaper that constantly covers heart disease and kidney failure would be a boring one that soon goes out of business. Even though our mission at Our World in Data is to cover the world’s largest problems, our own writing and data publications also don’t precisely match the scale of those problems. We expect we will be closer to the real distribution than the mainstream media, but there will still be some mismatch.

The reason we’re doing this analysis is to make you or other readers more aware of this selection bias. The frequency of news coverage doesn’t reflect what’s happening across millions or billions of people, but it’s easy to fall into the trap of thinking it does.

Why, then, do we think that this bias matters? Does it actually affect people’s perceptions of problems?

In alarge surveyamong US adults, people who consumed local crime news “often” were more than three times more likely to say they were “extremely concerned” about crime affecting them or their family than those who rarely or never read local crime news.8

The frequency of news coverage doesn’t reflect what’s happening across millions or billions of people, but it’s easy to fall into the trap of thinking it does

Nearly six-in-ten Americansstill seeinternational terrorism as a critical threat to the United States, despite the domestic impact on the US being relatively low for two decades. People are often far more anxious about flying than driving, even though commercial airline crashes areincredibly rare.

The information we’re exposed to profoundly impacts how we perceive the world, even if our perspective is less skewed than the media's.

But there’s one final reason why this bias matters. It makes it hard for us to understand how causes of deathare changing over time. If we’re constantly bombarded with stories of the latest murders and crimes, we might easily think that these are happening more and more. That is a widespread sentiment. In 23 of the 27Gallup surveysconducted since 1993, most Americans said there was more crime than the year before. In reality, rates of crime — includinghomicidesand otherviolent crime— have fallen a lot.

And if we don’t hear about what’s happening to heart disease rates, treatments, or the odds of surviving cancer, we might wrongly imagine that no progress has been made. Yet childhood cancer deathshave plummetedover the last 50 years. Even among adults, death rates from cancer havefallen dramaticallysince the 1990s. So too havedeath ratesfrom heart disease.

This perception gap about the world matters, and the media is not doing a good job of trying to close it.

### Methodology

If you’re interested in digging deeper, we provide a more detailed methodological document about how this data was generated, and a few additional analyses.

#### Correction note

This article was initially published on October 6, 2025, and was updated on October 9. This update corrected an error, whereby “Drug and overdose” deaths were also included within the US CDC category of “Accidents”. This meant that they were double-counted. We have corrected this, and the change made only a small difference to the final numbers. The relative share of deaths from accidents changed from 9.5% to 7.8%, and the share of other causes increased slightly. We thank Karl Pettersson for flagging this.

Continue reading on Our World in Data
* #### The limits of our personal experience and the value of statisticsThe world is huge; to get a clear idea of what our world is like, we have to rely on carefully collected, well-documented statistics.
* #### Causes of death globally: what do people die from?To make progress towards a healthier world we need to have a good understanding of what health problems we face today.
* #### How are causes of death registered around the world?In many countries, when people die, the cause of their death is officially registered in their country’s national system. How is this determined?

### Endnotes

1. Respondents could choose to “agree” with multiple answers. This survey was from 2015, but as we’ll see, more recent data suggests that even in 2025, most Americans think the news keeps them informed about what’s happening worldwide.
2. In the Pew Research survey, 46% said it made them feel informed “extremely often or often” with a further 43% “sometimes”. That was more common than any other emotion. The other high-ranking ones were negative emotions such as anger or sadness.
3. In 2023,there wereapproximately 3 million (3,090,964) deaths in the United States. 2.3 million (2,350,117) died from the twelve leading causes plus drug overdoses, homicides and terrorism. You can find these results in our intermediate and final data files, which are available inour methodology document. That means the combined share was around 76% of the total [2,305,117 / 3,090,964 * 100 = 76%].
4. We used mortality data fromCDC Wonderfor all causes except terrorism (which isn’t reported there). For this, we relied on data from theGlobal Terrorism Index.
5. This figure is sourced from the Institute for Economics and Peace (IEP)’sGlobal Terrorism Index 2024Report. It states on page 38: “The impact of terrorism improved in North America over the past year, owing to an improvement in score in Canada. There was one attack and death from terrorism in Canada in 2023, down from the peak of 12 deaths and eight attacks in 2018. By contrast, the impact of terrorism increased in the US, with 16 deaths from seven incidents.”
6. Isch, C. (2025). Media bias in portrayals of mortality risks: Comparison of newspaper coverage to death rates. Social Science & Medicine, 364, 117542.Pilar, M. R., Eyler, A. A., Moreland-Russell, S., & Brownson, R. C. (2020). Actual causes of death in relation to media, policy, and funding attention: Examining public health priorities. Frontiers in Public Health, 8, 279.Bomlitz, L. J., & Brezis, M. (2008). Misrepresentation of health risks by mass media. Journal of Public Health, 30(2), 202-204.
7. Isch, C. (2025). Media bias in portrayals of mortality risks: Comparison of newspaper coverage to death rates. Social Science & Medicine, 364, 117542.
8. This survey was conducted by Pew Research in 2024. It asked US adults whether they were extremely/very concerned, somewhat concerned, or not at all concerned about crime in their local community affecting them or their family.33% of those who “often” get local crime news were “extremely concerned”. The share among those who “sometimes” get this type of news was 19%. It was just 10% among those who rarely consume it.https://www.pewresearch.org/short-reads/2024/08/29/the-link-between-local-news-coverage-and-americans-perceptions-of-crime.

### Cite this work

Our articles and data visualizations rely on work from many different people and organizations. When citing this article, please also cite the underlying data sources. This article can be cited as:

Hannah Ritchie, Tuna Acisu, and Edouard Mathieu (2025) - “Does the news reflect what we die from?” Published online at OurWorldinData.org. Retrieved from: 'https://ourworldindata.org/does-the-news-reflect-what-we-die-from' [Online Resource]

BibTeX citation

@article{owid-does-the-news-reflect-what-we-die-from,
 author = {Hannah Ritchie and Tuna Acisu and Edouard Mathieu},
 title = {Does the news reflect what we die from?},
 journal = {Our World in Data},
 year = {2025},
 note = {https://ourworldindata.org/does-the-news-reflect-what-we-die-from}
}

### Reuse this work freely

All visualizations, data, and code produced by Our World in Data are completely open access under theCreative Commons BY license. You have the permission to use, distribute, and reproduce these in any medium, provided the source and authors are credited.

The data produced by third parties and made available by Our World in Data is subject to the license terms from the original third-party authors. We will always indicate the original source of the data in our documentation, so you should always check the license of any such third-party data before use and redistribution.

All ofour charts can be embeddedin any site.
