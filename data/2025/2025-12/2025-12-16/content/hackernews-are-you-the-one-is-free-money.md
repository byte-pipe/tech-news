---
title: '"Are you the one?" is free money'
url: https://blog.owenlacey.dev/posts/are-you-the-one-is-free-money/
site_name: hackernews
fetched_at: '2025-12-16T11:07:58.182865'
original_url: https://blog.owenlacey.dev/posts/are-you-the-one-is-free-money/
author: samwho
date: '2025-12-16'
published_date: 2025-11-05T00:00:00+0000
---

OK, so this is niche.

One of my wife's guilty pleasures is reality TV, usually ones centred around dating - the more American, the better. By extension, I absorb some of this noise and I'm happy to admit I can sometimes get invested.

At one point, she was (let's face it, we were) watching a show called "Are you the one?" on MTV. I'm going to show you how this game is pretty much free money.

# Game rules#

Consider a group of equal numbers of men & women:

Each contestant has exactly oneperfect matchof the opposite sex that is pre-determined for them, as represented by the colours. Click the "Match" button to pair up the contestants correctly. Crucially, they don't initially know who their perfect match is. If the group can correctly guess all the perfect matches, they win a cash prize of $1M.

You probably have the follow up question of how the perfect matches are calculated, which is a great question. In short: dunno, it's black-boxed, but let's just say "science"? How this is calculated isn't really the point, I could even argue that it doesn't matter so long as you get your strategy right. For what it's worth, the plot of the TV show mentions employing "the most extensive match-making process ever seen".

Let's get into it. Here are the two ways in which contestants can learn new pieces of information throughout the game:truth boothsandmatch ups.

## Truth Booths#

Atruth boothis where a male & female are chosen by the contestants, and it is revealed definitively whether they're a perfect match or not. So there are two potential outcomes:

If you've found a way to stream this and want to skip straight to the good stuff, I'd fast-forward to the fallout from these. In S1E6 it took Shanley an entire episode to come to terms with Chris T & Paige being a perfect match, even though in E1 she learned she was no match with him anyway (sigh).

## Match Ups#

At the end of each episode, all contestantsmatch upand they are informed (via dramatic lighting) how many correct matches they've got. If they've got all matches, the game is over and they win.

Crucially, they don't knowwhatthe correct matches are, just how many they got in total. The only way they can definitively rule out a pairing is if they scored zero: the dreaded blackout. Though it might seem like a bad thing, a blackout can in fact be helpful in the long-term, as it gives you a definitive answer for all pairs that were matched up, it's like getting a freetruth boothfor each pair.

# Modelling the problem#

Much like a high school disco, let's put all the boys on one side and the girls on the other, and re-use the pairs from thematch upexample above:

Here we have two correct pairsredandpinkat position 1 and 5 respectively. Theorangeman at position 2 was paired with thepurplewoman from position 6, and so on.

How good is a score of two? Is that any better than if you were to randomly pair people up? Let's experiment by doing just that: click the 'shuffle' button to re-pick:

You'll notice that the average score comes out at around 1 after a while, which this line chart keeps track of.

Below is a chart capturing the frequency of each score, you'll notice it eventually converges to a specific shape.

The height of each outlined bar is the probability of scoring that number in a random pairing in a game of 6 couples. Interestingly, both these probabilities and the average score stay the same no matter how many couples we use.

Whatever the selected # couples, the probability stays this same. There's tonnes of tangents we could explore that you might find interesting here[1], but for our purposes we just wanted to put some data behind "how good is a score of X".

## My model#

I created a model that computes the remaining viable matchings of all couples. By 'viable', I mean that there's still a chance that it's the perfect match. Initially, as you can imagine, this is a big number. The aim of the game then becomes getting that number down to 1 as quickly as possible.

Each time new information is learned, we recalculate the remaining matches. For example if we have a positivetruth boothresult, the remaining matches are filtered out to only those that contain these two people as a pair. Conversely, if thetruth boothresult was negative, then the remaining matches cannot contain any where these two are paired. Imagine a huge a game of "Guess Who?" where each image is a viable matching and you flip down the options that become invalid each time you learn new information.Match upsalso massively help you reduce this number, however their impact is a bit more indirect and it's very difficult for a human brain to figure out the implications of the result of one.

## Real-life performance#

Here is a graph of the remaining viable matches in Season 1 as the season progresses. It may surprise you that in this game of 10 men and 10 women, the initial number of viable matches is almost 4 million:

Hovering over the dots will tell you what's responsible for that change in the remaining matches. As you can see, they gain enough information to win the game by episode 8, so why does it take them so long to get it right? As mentioned earlier, it's almost impossible for humans to keep tabs on all these potential matchings so it's very likely they just didn't know.

That being said, the graph itself isn't particularly useful, is it? After a couple of events, the line hugs the x-axis, and it's hard to see the difference between 1 and 5,773 seen in episodes 8 and 2 respectively. Let's try a log base 2 graph:

That's hopefully a lot clearer. You can see how they learn information as they go, and at which point the model 'cracks it' with thematch upin episode 8. You can also clearly see that the most valuable piece of information they gained was thematch upin episode 2 - with a decent early score of 4. This might be intuitive to you, but as we found earlier you've got a less than 2% chance of scoring 4 when randomly selecting.

Let's plot this again along with a few more seasons[2]:

Other thanS3andS7, the contests mathematically learn enough information to win the game with time to spare. Could they have got there sooner though? Could they have chosen bettertruth booths/match upsto spare us all of the extra episodes of trashy TV? Before I get into this, I need to cover some basics of information theory.

## Information theory#

We're going to revisit the "Guess Who?" game now, which you can think of as a simplified version of "Are you the one?". Stick with me; the idea is that we can use the more straightforward game mechanics to establish an information theory based strategy that we can then apply to "Are you the one?". These two games are similar in that:

1. There is a correct answer unknown to the player(s).
2. The player(s) are able to learn information by offering up hypotheses, and getting definitive answers to them.

Consider an 8x8 grid of potential answers:

Now I'm a terrible artist so I thought I would be able to articulate this more clearly with shapes instead. There are 4 shapes (,,and), 2 different types (opaque or outlined), and 8 colours - this makes 64 unique combinations. The aim of the game is to guess the correct answer before your opponent guesses yours. To give yourself the best chance of winning, you need to rule out as many answers as you can, as quickly as you can. Should you then employ a strategy that splits the potential answers in half (e.g "is it opaque?"), or something a bit more specific (e.g "is it an orange star?"). The latter is high-risk, high-reward, whereas the former will almost always rule out half of the remaining answers.

Consider abitof information as reducing the problem space by half. That is, by ruling out half the remaining answers. I want to stress that the wordbitis a common term in information theory, as opposed to something that might sound less exact as it's intended in this context.

The opaque question is a sure-fire way of gaining 1bitof information. On the other hand, let's say you find out that the answer is awhich allows you to flip down three quarters of the answers, that's the same as halving the problem space twice and therefore gaining two bits of information.

In this example the answer is:

As you can see, different answers are more useful than others. "Opaque?" rules out half of the remaining answers (1 bit), whereas "Blue?" rules out 7/8ths of them (3 bits).

Getting from 64 potential answers to 1 involves halving the problem space 6 times - 64 becomes 32, then 16, 8, 4, 2 and 1. In other words, if you're able to gain 6 bits of information, you'll know for sure what the answer is. This is supported by the fact that the sum of the information gained by asking all three above questions is 6.

Let's simulate an actual game now, keeping tabs on the information gained throughout.

Once everything butremains, you'll have gained 6 bits of information and can be 100% confident in the answer. Now we know we need to get to 6 bits of information as quickly as possible, our strategy becomes picking the question that we expect to give us the most information. That is, the sum of the information we would gain if that answer were true or false, multiplied by the probability of that specific outcome. Let's work through our three questions to give the expected information for each:

Question

True

False

Sum

"
 ?"

25% of
2.00 bits
→
0.500

75% of
0.42 bits
→
0.315

0.82

"
Blue
?"

12.5% of
3.00 bits
→
0.375

87.5% of
0.19 bits
→
0.166

0.54

"Opaque?"

50% of
1.00 bits
→
0.500

50% of
1.00 bits
→
0.500

1.00

This table shows theexpected informationfor each of our 3 questions. As you can see, the more "Hail Mary" the question, the lower expected information. "Blue?" comes out at 0.54, which is almost half the amount of expected information as "Opaque?". Therefore, we can speculate that a decent strategy for this game would be to ask questions that split the remaining problem space in half. To support this, we can plot a graph[3]for all possible probabilities between 0 and 1:

This shows that splitting the problem space in half (where the probability is 0.5), gives the highest expected information. This means that asking a very specific question like "Blue?" is statistically theworstthing you can do.

Let's play one final game, this time I'll show you the questions ordered by most to least expected information:

How did you do? You'll notice that picking the questions at the top of the list gets you to the answer quicker, whereas the opposite is true when picking from the bottom. You'll also notice that you're never presented with a question that gives you more than 1 expected information, which is backed up by the above graph never going higher than 1.

Now we've got a strategy that works well for "Guess Who?", we can get back to the proper game.

# Simulating "Are you the one?"#

Earlier on, I posed a (until now) rhetorical question as to the performance of the contestants on the show. In order to answer this question, we need two things:

1. A way to measure performance:For this, we'll use theaverage bits gained per event. That is, each time there is amatch uportruth booth, how many bits of information did they gain?
2. A sensible benchmark:How do the contestants stack up against something that employed a strategy of randomly selectingmatch upsandtruth booths?

For this sensible benchmark, I simulated over 100 fake seasons of "Are you the one?" to see how much information was gained if thematch upsandtruth boothswere selected (almost[4]) arbitrarily.

The performance of the random simulated models was . Let's plot all the simulations on a graph, with trendlines for random and actual performance:

So the actual performance hits the x-axis sooner, meaning it's able to zero-in on the perfect match earlier. That's reassuring, right? Maybe love is real after all. That, or they're just performing better than someone shooting fish in a barrel. Here's the numbers behind this comparison:

Method

Per Event

Success Rate

Random

1.23 bits

74%

Actual

1.39 bits

71%

The success rate is calculated as the number of seasons in which they're able to mathematically determine the perfect match before the game finishes. As you can see the success rate for the random simulation is higher than in real life. The sample of size of only 7 seasons of "Are you the one?" undoubtedly is too small for this to be a useful comparison.

Now that we know the contestants make better decisions than randomly selecting pairings, the remaining question is exactly how much better. To show this, we'll employ our information theory strategy that we used for "Guess Who?" to this game.

This simulation works similarly to the random simulation, only the mechanism for selecting pairings is different. That is, the pairings that are selected for either atruth boothor amatch upare the ones that are statistically likeliest to give the most information.

Suppose we have calculated the expected information gained by potentialtruth boothslike below:

The model would therefore pickandas it's the most likely to give it the most information.

Match upswork similarly, however we know that it's not a simple true or false question. Instead, we've got to calculate the information we would gain foreveryscore between 0 and 10 (where 10 is the number of couples), foreveryviable matching.

I ran this information theory simulation 41 times (for no other reason than I got bored waiting), and saw it perform significantly better than random simulation or real life data:

Now we can compare all three scenarios:

Method

Per Event

Success Rate

Random

1.23 bits

74%

Actual

1.39 bits

71%

Information Theory

1.59 bits

98%

This means that, all you need is a bit of code and a can-do attitude to perform better than the "vibes" approach of the contestants in the show. Before you pop the champagne, we still haven't shown if this is goodenoughsuch that we get to the perfect match before we run out of time (or episodes). In a game of , the problem space is (for brevity, you can take my word for this), which is bits of information. This means you would need to gain bits of information per event minimum to ensure that you go into the finalmatch upknowing for certain what the perfect match is.

Wait, isn't that a lower number than the random simulation? Doesn't that mean that someone shooting fish in a barrel could win this game? I should stress that these areaverages, and in 26% of random simulations they didn't get to there in time.

# Conclusion#

Hopefully now you agree with me that "Are you the one?" is free money, albeit with a just about near-perfect success rate. I showed that even picking pairings at random will more often than not give you enough information to win the game, as well as showing how to use classic information theory practices to get you there with episodes to spare. Maybe this haemorrhaging of money is what got the show cancelled in the first place, or maybe love is real, whatever you prefer.

# Resources & inspiration#

This post is my first foray into content like this. I wanted to scratch the itch of an interesting maths problem, with a light-hearted spin that I hope you enjoyed as much as I did making it. The techniques shown in this post are very common information theory approaches, though I was inspired to apply them based onthis video on wordleby 3Blue1Brown. I very rarely watch youtube videos over 10 minutes long (maybe that's my loss), but I wholly recommend this one if you found this interesting.

Other than that, in my research I came across a boardgame called Mastermind, which has been around since the 70s. This is a very similar premise - think of it as "Guess Who?" on hard mode.

I also pitched this idea toThe Pudding, and had a great experience with them nerding out about this subject. Though they didn't take my up on my idea, I left with really great and actionable feedback, and I'm looking forward to my next rejection.

Next steps for me would be to see if I can make a web-based game (don't hold me to this) on this theme. I'm interested in how people would intuitively make decisions based on information gained so far so the plan would be to see if I can find a way to capture that, and ideally make it fun.

Finally, the code for my OR Tools model can also be foundhere.

1. As the number of couples increase, the probabilities trend towards a poisson distribution with λ=1. The probability of 0 and 1 is also given by 1/e, which is a classic result inderangements, specifically with the "hat-check problem".↩
2. I omitted Seasons 2, 8 and 9. Each season that wasn't considered was due to them introducing different game mechanics, which would have been hard to take into account for my model. Maybe my model was too rigid and I'm a bad developer, or maybe it's just inappropriate to find commonality there. Season 2: One female contestant had two perfect matches, meaning there weretwoperfect matchings. Season 8: In this season, they introduced gender fluidity. Whilst an interesting problem on its own, this would have wreaked havoc on my model. Season 9: One of the contestants left the show at an early stage, so the decisions made by the contestants would have been biased.↩
3. This is known as thebinary entropy function.↩
4. I say "almost" here because I wanted this simulation to have some common sense. Specifically, if a pair were to have an unsuccessfultruth booth, then it wouldn't be paired up for any subsequent events. My reasoning here is that no right-minded person would ever pair up people who can't be a match, as you would learn nothing new, and crucially it wasn't too arduous to code this into my random simulation model.↩
