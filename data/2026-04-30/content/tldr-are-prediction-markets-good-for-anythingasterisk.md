---
title: Are Prediction Markets Good for Anything?—Asterisk
url: https://asteriskmag.com/issues/14/are-prediction-markets-good-for-anything
site_name: tldr
content_file: tldr-are-prediction-markets-good-for-anythingasterisk
fetched_at: '2026-04-30T12:31:23.716858'
original_url: https://asteriskmag.com/issues/14/are-prediction-markets-good-for-anything
date: '2026-04-30'
description: We all know they’re casinos. It’s time to look at the data behind the froth.
tags:
- tldr
---

# Are Prediction Markets Good for Anything?

## Dan Schwarz

We all know they’re casinos. It’s time to look at the data behind the froth.

In 2007, Nobel laureates Kenneth Arrow, Daniel Kahneman, and other notable scholarspublished a statementarguing that prediction markets could “substantially improve public and private decision-making.” The theoretical foundations were deep.

Friedrich Hayek hadargued in 1945that markets aggregate dispersed, local, and tacit knowledge through the price system better than any central planner. In 2000, George Mason University economist Robin Hansonproposeda system he called futarchy, in which markets would be used to evaluate whether policies deliver on promises. Seventeen years later,Philip Tetlock, Barbara Mellers, and Peter Scoblicwere championing forecasting tournaments as a way to generate useful policy knowledge for the intelligence community and to depolarize political debates.

Institutions includingGoogle,Microsoft,the CIA, the widerU.S. intelligence community, andBritish government intelligence analystshave all experimented with internal prediction markets. Some of these trials were more successful than others, but all were small. And we know, from both theory and practice, that more bettors make markets more accurate. Hal Varian, Google’s chief economist, likes to call prediction markets “information markets,” and the bettors the “suppliers” of the information.

For decades, prediction market optimists — and I count myself among them — have argued that once we build better markets and increase the supply of bettors, accuracy will improve, and we’ll all be able to benefit from a new level of societal foresight.

Now, in 2026, public prediction markets like Polymarket and Kalshitransact billions of dollars in volume each month. The vast majority of these bets are not on questions that might produce useful information. Roughly90%of Kalshi’s trading volume (dollars exchanging hands between bettors) is from sports betting, making Kalshi effectively a sports gambling website with a small prediction market attached. I find that over 80% of the trading volume on Polymarket is concentrated on sports, cryptocurrency prices, or election betting.1

Much ink has been spilled on the negatives — such as gambling addiction and insider trading — of the growing popularity of these markets. But what of their promise? Are they producing valuable information and making humanity wiser?

 

Caravaggio, 
The Cardsharps
, 1594.

## Demand, demand, demand

To understand how useful this supply of forecasts is, and whether the forecasts really are delivering on the vision of the progenitors of prediction markets, we need to think about another factor: demand.

It is entirely conceivable that prediction markets are only being used by bettors themselves. But if individuals, firms, media, and policymakers want (or need) the predictions we see on these markets, this evidence of demand can be used as a proxy for their usefulness. Vitalik Buterin, creator of the cryptocurrency Ethereum, summarized inInfo Financethis dual nature of prediction markets: “If you are a bettor, then you can deposit to Polymarket, and for you it's a betting site. If you are not a bettor, then you can read the charts, and for you it's a news site.”

I’ve thought hard about how to sell prediction markets to consumers. In 2020, I created Google’s current internal prediction market. Since then, I’ve served as the CTO of Metaculus, a non-market-based crowd-forecasting website, and now run FutureSearch, a startup that provides AI forecasters and researchers. In my work, I’ve found that the benefits of prediction markets fall into five different categories.

First, markets can providerisk monitoring. I learned about COVID-19 in February 2020 from Metaculus, causing me to cancel a planned trip that would have left me stranded.

Second, they can help withinterpreting news, showing whether, and how much, a current event might affect larger outcomes. For example, the closure of the Strait of Hormuz during the 2026 Iran war led to an increase (from ~25% to ~35%)in the forecasted chance of a 2026 US recessiondue to the spike in oil prices.

Third, they can inform planning aroundpolicy outcomes, such as whether TikTok will be banned in the US.2

Fourth, they could createaccountabilityfor claims made by political or business leaders. For example, in June 2025, when President Trump said he was contemplating a strike on Iran’s nuclear program, many Middle East expertsdismissed the prospect, according to an article from the Council on Foreign Relations. Yet, per CFR, prediction markets gave a 58% chance of strikes that week, and we later learned that seven B-2 stealth bombers were then on-route.

Fifth, they could producenovel information, allowing traders to discover or track things others don’t, such as when major AI milestones will be reached.3

Now let’s see whether the billions wagered on markets each month are supplying these five forms of useful information.

 

 The big spike in November 2024 was due to $400 million bet on Trump's inauguration, and $327 million bet on Romania's election scandal, which involved the first ever annulment of a presidential election by an EU/NATO member. 

## Risk-monitoring as a healthy information market

I’ll start in the one area where the supply (bettors betting) and demand (readers reading) for information from prediction markets seem to be in balance: risk monitoring.

The most straightforward benefit from prediction markets comes from questions like “Pakistan military strike on India by Friday?” or “Will there be at least 10,000 measles cases in the U.S. in 2026?” or “US bank failure by January 31?” Tracking such risks was the domain of the first experiments with crowd forecasting in the US intelligence community, such as the IARPA tournaments, and of many of Philip Tetlock’s later superforecasting studies.

Kalshi and Polymarket have a healthy number of such risk monitoring markets. I count 2,821 in total, with $3.8 billion in volume, of which geopolitical risk is the largest category. The median risk monitoring market has $82,000 of trading volume. Of these, 199 are conflict markets that resolve on a daily and weekly basis, creating a near-real-time escalation tracker.

Here, the demand is clear.4For the 2026 Iran war, for example, energy traders and shipping companies are the most concrete beneficiaries of the predictions on outcomes and timelines. Importantly, demand comes from mainstream media, which increasingly5cites Polymarket, bringing these forecasts directly to professionals in places they already look.

Useful as these markets are, they still have important blind spots. While journalists might cite prediction markets to track developments in an ongoing conflict, I haven’t seen media sites reporting stories where prediction markets are the source. This is a function of how public, retail prediction markets work: a story must already be quite large to attract enough traders to produce useful probabilistic information. Therefore, I see evidence of useful monitoring of risks, but not detection of them.

Markets that don’t tie into flashy news stories suffer from both less supply and less demand. Health and climate questions, which are arguably as important as conflict surveillance, have not fared well in prediction markets.

When Kalshi launched in July 2021, a year into the COVID-19 pandemic, it built exactly the kind of market that experts advocated: consistent, weekly questions about specific vaccine adoption numbers and COVID-19 case numbers. They averaged $8,000 per market, too low to be credible, and had several big misses. For example, “Germany COVID cases above 35K for week ending Dec. 28, 2021?” was trading at 3% a week before Omicron hit, and it was resolved as “Yes.” And it seems no institutional consumer, like a hospital system or government disease tracking body, materialized to adopt the signal. Climate and natural disaster markets, where theoretical support is strong,6tell the same story. The markets failed both to attract a supply of traders and the demand of response bodies or the public.

A second area where I see preliminary signs that a supply of good predictions could meet strong institutional and public demand is in the last of my five categories: generating novel information. There are some dozens of markets tracking AI, with $25 million in volume on questions that address which labs will have the top models on certain dates. It is not hard to imagine the people or organizations who would demand better information about emerging technologies.

However, if one examines these AI markets, it seems that they are too low-quality to be useful to anyone making a decision. I can't imagine that an individual who chooses a model provider, a firm that chooses a partner or supplier, or a policymaker who chooses an AI regulation would have much to learn from them.

It’s clear that Polymarket and Kalshi host these markets to serve bettors, not to produce useful information. Take Kalshi’s “Best AIs this week?” markets, which not only cover too short a time period to be useful in any decision-making, but also use Arena to judge the best AIs. Arena, which uses voting, not objective task scores, is not a credible measure according to AI experts. Still, demand for these markets does exist, and it’s plausible that higher-quality markets could emerge in the future to satisfy it.

 

## Where prediction markets are accurate but ignored

In three of the five categories of benefit from prediction markets — interpreting news, policy outcomes, and accountability — I see evidence that high-volume markets are producing accurate predictions, but not evidence that anyone is, or should be, paying attention.

First, how useful are markets for interpreting news? These are markets tracking larger outcomes like recessions or inflation that move in response to news, helping readers understand the impact of particular events.

Volume appears healthy, with 1,647 markets and $1.25 billion in total trading volume. However, 85% of that volume is in US federal interest rate markets. The median trading volume of markets for interpreting news has actually decreased substantially, from a high of $49,000 in early 2025 to just $13,000 by the end of the year, much lower than the median volume of other markets I categorize as useful.

While predicting interest rates is valuable, CME futures, Bloomberg consensus, and professional economists already do it. The same is true for other indicators with high trading volume on Polymarket and Kalshi: inflation, unemployment, commodity prices, mortgage rates. Aaron Browncallsprediction markets “economic oracles,” but the oracle is largely saying what other oracles already say, just updated faster.

Still, there is a benefit to speed. On March 11, 2026, theFinancial Timesreportedthat, upon news of Iran War escalation, the Polymarket odds of inflation at or above 2.8% rose to above 90%. This illustrated an immediate domestic impact to US foreign policy, which could influence the public in a way that updates months later from professional economists might not.

Next, how useful are markets for judging whether claims by governments and CEOs are credible? I found 184 accountability markets with $173 million in total trading volume. The number of such markets is growing, as is the median trading volume, with a median $44,200 in bets.

But two-thirds of the total volume is Epstein file speculation, the type of activity thatRohanifar et al. (2026)diagnoses as “prediction laundering.” It's hard to see any decisions changing based on these markets. Most of the rest are about one other person, US President Donald Trump,7which feel like a temporary artifact of a particularly entertaining leader with credibility issues in the popular consciousness.

Finally, how useful are markets tracking policy outcomes? I found 1,710 markets with $1.42 billion in total trading volume. But the vast majority of volume is on a very small number of highly visible markets: $288 million on the possibility of a U.S. government shutdown, $238 million on whether Judy Shelton would be nominated as Fed chair, $145 million on whether TikTok would be banned in the US.

The median volume of markets is increasing, growing in 2025 from $24,000 to $30,000. The section I find most valuable are the 196 markets with $144 million volume on tariff policies.8These are actionable in many places around the economy, and I think the wisdom of the crowds is producing novel, useful, accurate information on what tariffs will take effect at what level.

Overall, the markets on all three of these categories are dominated by betting on the Trump administration's volatile policies. As Robin Hansonhas commented, “A random unpredictable US president has been very good for the prediction market industry.” This doesn't seem to me the vision that academics hoped for: experts wagering on current events, leading to pledges made from serious politicians or influencing the most important bills faced by legislatures worldwide.

Markets driven by entertainment value and intrigue to bettors could plausibly deliver this, but I don’t see much of it on Kalshi and Polymarket. The most charitable view is that these are growing pains, where the creation of a healthy information market is bootstrapped by gambling on Trump, and gradually evolves into the more professional betting environments on mature financial securities. Until then, though, I don't expect that people affected by policies will pay much attention.

We have another reason to doubt that the money changing hands across all of these markets is providing value. Metaculus, my former employer, has produced thousands of well-calibrated forecasts on global risks, health, and technology for over 10 years, with minimal institutional impact. Metaculus has even explored another item on the economists’ wish list: “conditional markets” which ask “If policy X happens, what will outcome Y be?” Yet these also have not been adopted by information consumers, and there are serious technical barriers to adoption by predictors.

Still, the original vision for public benefit from prediction markets depends on them being highly liquid, and billions of dollars in liquidity can significantly change accuracy (or the perception thereof).Polymarket CEO Shane Coplansaid Polymarket is “the most accurate thing we have as mankind right now”, whileKalshi CEO Tarek Mansouradvertises prediction markets as “quintessential truth machines”. Let’s look at whether trading volume leads to higher accuracy.

 

## Whence volume comes accuracy

Coplan and Mansour did not invent prediction markets, but they are the first to create ones with billions of dollars of trading volume, so their claims of truth and accuracy depend on this feature. “On Kalshi, the goal is liquidity and accuracy,”Mansour saidin February, putting them hand-in-hand.

So, when one of these new generations of markets with millions of dollars wagered implies a 70% likelihood, does the event it tracks actually occur close to 70% of the time, as theory would predict?

The accuracy of a market is generally measured at a single point in time, but prediction markets have continually updated prices. For simplicity, I analyzed markets 7 days, 30 days, and 90 days before they settled. Markets also have bid/ask spreads, and the “probability” implied by the market is usually taken as the median between the price buyers and sellers are willing to trade. I then looked at two accuracy scores.9

Absolute accuracy is hard to compare across markets on one platform, and across platforms, because different forecasting questions have different difficulties. I addressed this by tracking similar markets on a single platform over time, where plausibly the only difference in accuracy would come from the change in volume of trading. Insufficient question overlap made it difficult to compare the real money markets to play-money or no-money markets like Manifold and Metaculus. What we can say is: even if highly liquid prediction markets are more accurate than previous forecasting methods, the liquid prediction market operators haven’t demonstrated it. I find it unlikely that higher accuracy is a reason that people would prefer Kalshi and Polymarket to other forecasting methods.

I examined all markets on Kalshi and Polymarket from Jan 1, 2024 through March 8, 2026, and a sample of older markets on Kalshi for historical comparison. I filtered out categories I deemed as never useful.10This filtered ~194,000 markets down to 13,500 markets. Then, I used FutureSearch tools to classify them into the five categories of potentially positive value, iterating on criteria until I was satisfied by the categorization. This led to a final set of 6,797 markets — 5,703 resolved and settled, and 1,094 still live and trading — that I see as potentially useful, if they were accurate and had the right audience.

 

Are markets with higher trade volume more accurate?

Yes, for markets that last 90 days or more, which is roughly a quarter of this sample. This holds for both useful and non-useful markets, and on both Polymarket and Kalshi.

Strikingly, markets that last less than 90 days (as judged by accuracy 30 days before resolution, and 7 days before resolution) did not show a statistically significant relationship between trade volume and accuracy. I suspect that as these markets mature, volume will predict accuracy. One possible explanation is that the higher-volume markets are on more entertaining topics with less informed traders, and it takes time for experts to move in. Another is that high-volume markets actually don’t have many traders, with a few people wagering thousands of dollars each. “Wisdom of the crowds” does require a crowd.

Are “useful” markets getting more volume over time?

Useful market volume grew until late 2024, but has not grown in volume since. Total and median volume of useful markets grew dramatically from 2023 to late 2024. They peaked at $534 million per month around the 2024 U.S. election ($81,000 median and $2.3 million average per market), and is today around $466 million / month ($42,000 median and $1 million average per market). Volume is dominated by a very small number of hugely popular markets, and the median “useful” market is actually declining in trading volume.

Are “useful” markets getting more accurate over time?

Useful market accuracy improved until early 2025, but hasn’t improved since.

This roughly follows the growth in volume, though accuracy improved after volume plateaued. (Market dates are shown by creation, not resolution, so volume that occurs months later is shown backdated to when the market was created.) And just as the median volume of useful markets has declined, so has accuracy (though not statistically significantly), which is now lower than it was in early 2025.

 

 Left: WMCE shows the difference between the price of the market, and whether the market is actually X% likely to happen. Lower is better, 0 is perfectly calibrated.
Right: Brier score is absolute accuracy. Lower is better, showing it improving as markets got liquid, but actually getting worse since 2025-H1. 

This reinforces the impression one gets from perusing both platforms. The huge growth in sports betting, crypto gambling, and entertainment markets is not consistently spilling over to “useful” markets, which are rare and neglected. It’s possible that it will simply take more time for bettors on these “fun” markets to start betting on more useful ones. Google's 2005 prediction market was full of entertaining markets to encourage user adoption, and I did the same thing when I set up their current prediction market. We might see the same thing play out on Kalshi and Polymarket.

But while this is happening, another development is challenging the core premise that human incentives determine the supply of forecasts, and ultimately how people who demand this information discover and consume it.

 

## You can't spell “futarchy” without “AI”

In January 2026, noted tech and rationality blogger Scott Alexanderwrote:

 

There are now strong, minimally-regulated, high-volume prediction markets on important global events. In this column, I previously claimed this would revolutionize society. Has it? I don’t feel revolutionized. Why not?

 

One way forward, he writes, is to create better prediction markets, perhaps by letting users on real-money platforms generate the questions themselves. (Currently, user-generated markets are only allowed on the play money site Manifold). "The second," he continues, "is to conclude that prediction markets’ role in God’s plan was only to provide the foundation for AI superforecasters." He then points out that the Forecasting Research Institute in October 2025claimed thatAIs might surpass the best human forecasters in late 2026.11

Those of us who work on AI forecasting are sympathetic to this argument. My company, FutureSearch, was thefirst to deploy AIsin a (play money) prediction market in January 2024. Even using forecasting approaches powered by GPT-4 Turbo and Claude 2, LLMs that are now considered quite unintelligent, we outperformed most human traders.

But I don't want to focus only on how AI forecasting might make prediction markets, or wisdom-of-the-crowds more generally, obsolete as a method of supplying forecasts. AI could also radically improve the way people access the forecasts they demand.

I claimed earlier that the value of risk monitoring markets mostly comes through the mainstream media reporting on these probabilities. If financiers, supply chain analysts, and policymakers see Polymarket probabilities in mainstream news, they don’t need to check Polymarket (or even know what a prediction market is) to benefit from the information.

Likewise, a large number of individuals, firms, and policymakers get information from chatbots like ChatGPT, Claude, or Gemini. Chatbots are not (yet) trained to be accurate forecasters, but they already serve as a primary way that people get all five types of value from prediction markets, largely by making implicit forecasts:12

Risk monitoring: Ask ChatGPT about the biggest risks in your upcoming vacation or business plan.

Interpreting news: Ask Claude whether the new AI model release affects how work is being automated.

Policy outcomes: Ask Gemini to run a "Deep Research" report on whether the new tariffs will survive court challenges.

Accountability: Ask Grok whether Elon Musk will deliver on his most recent space flight promises.

Novel information: Any LLM can give you its best attempt to reason through any question you can imagine.

Try it yourself. Pick a topic that is important to you. Try searching Polymarket for probabilities, versus asking Claude about it. I wager you’ll prefer Claude’s take, even if it is less accurate.

For one thing, Claude can speak to issues that are not properly resolvable forecasting questions. People who demand information on geopolitics and technology do want accurate probabilities, but they also want narratives, histories, and the ability to ask followup questions. Often, accurate information is a good starting point, but the bigger constraints to wiser actions are social and political. Prediction markets can’t help you strategize how to act on a good forecast. Claude can.

No forecasting technology fixes the fact that neither humans nor institutions were built to think probabilistically. But chatbots are a much more credible method of changing how people think about their decisions, and the forecasts implicit in them. And if AI forecasting also side-steps every other issue in using prediction markets to supply forecasts, from insider trading to resolution scandals to lack of liquidity, then AI can bootstrap the entire two-sided information market.

That said, even when Claude can forecast more accurately than the entire set of Polymarket traders, prediction markets might still serve some of the epistemic purposes that Kenneth Arrow, Daniel Kahneman, and others laid out in 2007.

By accelerating the adoption of probabilities by mainstream media, prediction markets help build common knowledge. It is conceivable that having large sums of money changing hands will make the markets increasingly newsworthy, and attract the attention of people who benefit from the predictions who would not have thought to ask Claude for advice on those topics.

I think most decisions by individuals, organizations, and governments are built around norms and social consensus, and highly visible prediction markets could influence people more than private conversations with chatbots. This, to me, is the most likely path towards the realization of the value of prediction markets: large amounts of betting leads to more mainstream media coverage of prediction markets, normalizing their use in workplace discussions, and ultimately decision making processes.

Decades ago, the grand vision of producing high quality public information was about aggregation of wisdom. Now, Polymarket, Kalshi, and even Metaculus have shown us that the bottleneck is distribution of wisdom. The evidence suggests that billion-dollar prediction markets, despite both their founders calling them “truth machines”, are overwhelmingly in service of their traders (and their desire to bet on sports), not the seekers of truth.

Might the prediction markets use their billion-dollar valuations to now build out Vitalik Buterin's vision for “info finance”? Maybe. But I forecast that before they do, Claude will be the only forecaster anyone will ever want to ask about the future.

 

1. Data for this article sourced on March 7, 2026 from the official Kalshi API (https://docs.kalshi.com/) and the official Polymarket API (https://docs.polymarket.com/).
2. Policy outcome markets could include those that predict election results. But while many people first learned about prediction markets from such markets during the 2016, 2020, and 2024 US presidential elections, and while the outcomes of elections do influence policy, I don’t find such markets useful. First, polls and non-crowd-forecasts give good odds already, and second, it’s hard to see who would do something differently based on whether the Democrats have, say, a 45% chance of winning the US Senate in 2026 vs a 41% chance.
3. Many markets that appear to produce novel information are in fact only making private information public. In 2026,OpenAI fired an employee for tradingon prediction market platforms, and many other cases of such insider trading have been levied. Here, I am tracking the public production of genuinely new information. One sign that markets are producing new information is that they are long-term, like predicting the best new cancer drugs over the next 2 years. As I show later, even for questions I consider useful, most trading volume on Polymarket and Kalshi occurs on questions that resolve in less than 90 days, and for most short-term questions, the right insiders do probably have decisively better information.
4. Why do people need prediction markets when they have futures markets, e.g. tracking the escalation of Iran War tensions via implied future prices of oil? The answer is that commodity futures and stock derivatives are too blunt as informational instruments. Prediction markets enable direct measurement of individual risks, which can be used to inform much more direct responses, such as routing a shipment away from a conflict area.
5. Examples include: Reuters covering odds of China invading Taiwan (May 2025), Bloomberg covering Trump tariffs and the Supreme court (Oct 2025), the Wall Street Journal covering the odds of a ceasefire in the Iran War (March 2026) or the rapid fall of the Iranian regime (March 2026)
6. Cerf et al. (2023)found that participating in a prediction market on climate outcomes increases support for costly climate policies.Roulston et al. (2025)found that a prediction market more accurately forecast the 2024 Atlantic hurricane season than other methods.
7. Markets about which statements President Trump will follow through on do seem valuable to me, as market prices imply that some of his claims are more credible than others, such as the market tracking his June 2025 claims about strikes against Iran nuclear facilities. Perhaps future leaders will have such extreme accountability issues to warrant large betting markets about what they say.
8. For example, in May 2025, after Trump announced retaliatory “liberation day” tariffs of well over 100% against China, Polymarket hosted “US-China tariff agreement before 90-day deadline?” which had $500k in trading volume. The market fluctuated around 60-80% throughout June, July, and August until the agreement was reached shortly before the deadline, and ultimately tariffs were far below the original 145%. Uncertainty around where tariffs would land was widely cited as a major business risk throughout the global economy.
9. The simplest is Brier score, which tracks error between the implied probability (say, 0.35 for a 35% forecast) and what actually happens (say, 0 for “no”). I also looked at Weighted Mean Calibration Error, a measure of calibration error:  if 100 markets say something is 70% likely, implying that 70 out of those 100 should happen, how many actually end up happening?
10. On Kalshi, I filtered out these categories: Sports, Crypto, Financials, Climate and Weather, Entertainment, and Mentions, plus keywords that identified markets in those categories that weren’t categorized properly. On Polymarket, I filtered out these tags: Crypto Prices, Up or Down, Crypto, Sports, Esports, Games, Bitcoin, Ethereum, Solana, XRP, Ripple, Weather, Equities, Stocks, Commodities, Celebrities, Movies, Music, Grammys, Awards, Mentions, Tweet Markets, Twitter, YouTube, and Earnings. You may wonder why I filter out “financials”, “equities”, “stocks”, and “earnings.” Surely these could be useful categories to forecast? In theory, these could be useful, especially earnings forecasts in particular are surprisingly poorly covered by the sell-side investment community. But in practice, I find them formulaic, and I think they exist to let bettors debate the efficient market hypothesis.
11. 95% confidence interval: December 2025 – January 2028.
12. OpenAI finds that about81%of work-related messages map to just two broad work activities: (1) obtaining, documenting, and interpreting information; and (2) making decisions, giving advice, solving problems, and thinking creatively. Forecasting is likely a significant portion of the latter category. After all, how can one give advice without implicitly forecasting the outcomes of following that advice?

Previous
Risk-Adjusted Return

Next
Shall We Play a Game?

## About Highlights

By highlighting text and “starring” your selection, you can create a personal marker to a passage.

What you save is stored only on your specific browser locally, and is never sent to the server.Other visitors will not see your highlights, and you will not see your previously saved highlights when visiting the site through a different browser.

To adda highlight: after selecting a passage, click the star. It will add a quick-access bookmark.

To removea highlight: after hovering over a previously saved highlight, click the cross. It will remove the bookmark.

To remove allsaved highlights throughout the site, you canclick hereto completely clear your cache.

All selections have been cleared.