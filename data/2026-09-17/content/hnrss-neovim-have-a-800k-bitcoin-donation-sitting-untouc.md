---
title: Neovim have a ~$800k Bitcoin donation sitting untouched since 2023 | Hacker News
url: https://news.ycombinator.com/item?id=49738879
site_name: hnrss
content_file: hnrss-neovim-have-a-800k-bitcoin-donation-sitting-untouc
fetched_at: '2026-09-17T15:27:03.834288'
original_url: https://news.ycombinator.com/item?id=49738879
date: '2026-09-17'
description: Neovim have a ~$800k Bitcoin donation sitting untouched since 2023
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
Neovim have a ~$800k Bitcoin donation sitting untouched since 2023
271 points
 by 
jakemanger
 
4 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
205 comments
I was looking at neovim's donation footer at the bottom of their site and saw a bitcoin donation address.

Thought I'd check how much in donations they've gotten. And I saw this massive 10 Bitcoin donation from back in 2023 (worth $800,000 now...)From the activity history, neovim last sent bitcoin out of the address in 2019 so it's been max 7 years since they've definitely had access.Does anyone from the neovim project know about this? 
Seems like a pretty significant amount of funding to have sitting there. Hope it can come to good use as I use neovim daily.https://www.blockchain.com/explorer/addresses/btc/1Evu6wPrzjsjrNPdCYbHy3HT6ry2EzXFyQ

 
help

ashkankiani
 
1 hour ago
 
 | 
next
 
[–]

For a reference point, when I was unemployed and between jobs, I got involved with Neovim for fun, and after some contributions, I eventually tried some full(ish)-time paid work. I wrote the native lua LSP client (:h vim.lsp, and the nvim-lspconfig repo) for Neovim in a few weeks for about $3k USD (circa 2019)? This amount could fund quite a lot of work to be sure.

reply

matesz
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I’ve read so many news stories of people gone missing who had been know to have sole access to bitcoin wallets with large amount of bitcoins in them.

I wonder how people at large crypto exchanges handle that. Perhaps shamir share the access to the pkey password and store parts at secure places like a bank? And make official access protocol akin to dnssec, but simplified?

reply

jackb4040
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

I worked at a crypto exchange, yes we used shamir shares. But probably not as sophisticated as you're thinking, there was basically one big "break glass" text document with all the keys. And then a hand-rolled software on each person's laptop to distribute the plain text and run / practice the 3/5 recovery ceremony. So anyone losing their device would be equivalent to someone quitting and require its own ceremony to reissue a key, but I don't think that ever actually happened.

We explored using smart contracts to have logic perform the 3/5 consensus rather than a cryptosystem, but that was never rolled out while I was there. Social recovery wallets in general did not take off, which was a big learning moment for me that very few people actually cared about the technology and what they really wanted was an app with as many gambling features as possible that uploaded their keys to google drive.

reply

IAmBroom
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Social recovery wallets in general did not take off, which was a big learning moment for me that very few people actually cared about the technology and what they really wanted was an app with as many gambling features as possible that uploaded their keys to google drive.

People who are not HN-profile never care about the technology, and always care about usable, convenient features. The shocker is: most HN-profile people feel the same way.Also see:https://m.xkcd.com/2501/

reply

pests
 
5 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Social recovery wallets in general did not take off

ERC7093 has finally added this

reply

jackb4040
 
51 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, I do agree with this. What rubbed me the wrong way was all the cynical people who would talk endlessly about how revolutionary the tech was and all the possibilities it opened to get others invested, but ran companies that were just casinos and actually could have simpler operations without the crypto parts! Most people in pre-NFT crypto has someone in their network who worked on an outright Ponzi scheme.

reply

dspillett
 
3 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> but ran companies that were just casinos and actually could have simpler operations without the crypto parts

But during the big buzz, the crypto parts were what got those companies any exposure at all.

reply

imhoguy
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Worse when crypto exchange bosses go missing 
https://archive.is/lPpRz

reply

krageon
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Large exchanges handle this very simply: If they have the keys, it goes to the inheritor(s) once they get a court order. If they do not, it goes nowhere

reply

slipwalker
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

but what sort of people keep their bitcoins on the exchange ? the whole point is about not being seizable by dirty governments...

reply

ajkjk
 
0 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Most people don't care about that at all
pjc50
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Traders; low information investors; people who are not 100% confident in their personal infosec and not willing to lose their bitcoins on their own.

"Not being seizable" hasn't really worked out for bitcoiners who've been arrested. Or for that matter robbed at gunpoint.

reply

skinfaxi
 
1 minute ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> "Not being seizable" hasn't really worked out for bitcoiners who've been arrested. Or for that matter robbed at gunpoint.

This seems orthogonal to the ability to seize assets.

plopilop
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Pretty much everyone. There's a reason people lost money with ftx, Mt gox and other scams.

Managing your private keys is cumbersome, error prone, requires some computer literacy, the list goes on.Tbh I have been kind of impressed by how fast L2 businesses brought back centralisation in every possible way. I guess it's more efficient for them.In the same way, the internet was supposed to be decentralised, everyone being in charge of their own servers. But in practice nobody has the time to set up their own MX servers.

reply

thesuitonym
 
29 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> not being seizable by dirty governments

If you believe that, I have some land to sell you

reply

jubilanti
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> but what sort of people keep their bitcoins on the exchange ? the whole point is about not being seizable by dirty governments...

For most people, cryptocurrency is just another stock market / betting app.

reply

lizardking
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

"Number go up" people

reply

debesyla
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Hype vibe investors, probably.

reply

LtWorf
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

People who want to be scammed.

reply

seymon
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I hope they still have the private key.

reply

osigurdson
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

It is an interesting fact about Bitcoin in general. There are 21M tokens in total AND some percentage are lost every year. Run this simulation long enough and there will be very few active Bitcoins remaining.

reply

bryanlarsen
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

21M is the theoretical cap. At the moment there are 20M and more are constantly being mined. Miners have to convert bitcoin into real currency to pay for their electricity both for mining and transaction fees. This means that there is always a supply of bitcoin for sale. Which is fine if there is still demand for new bitcoin, but who's buying bitcoin these days? It has underperformed both the S&P 500 and gold over the last 5 years. I expect bitcoin inflation to continue. (AKA the bitcoin price to continue to go down).

reply

jackb4040
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Worth pointing out that the monetary policy of bitcoin is not written in stone; all you need to change it is a majority of hashpower. The current chain of bitcoin mainnet includes hard forks, like this one due to miners' manual intervention over a software bug that was exploited: 
https://en.bitcoin.it/wiki/Common_Vulnerabilities_and_Exposu...

reply

notpushkin
 
33 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> all you need to change it is a majority of hashpower

Or rather the majority of actual users. Hard forks occur because people install and use the updated clients. If 90% of the miners decide to mine on the “bad” chain, but 90% of users switch to the “good” one instead, the “good” would likely still win out in terms of market cap and recognition (and the miners would naturally have to follow).

reply

Roark66
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Seems pretty silly to build in deflation into a currency. It incentivises putting your money in a mattress for 100 years.

reply

benenrjdnz
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Deflation is a good thing, it rewards delayed gratification.
Those evil Keynesians have convinced the world a little bit of inflation is good. It isn’t. Losing purchasing power on your money is a bug.

Nothing wrong with putting money under a mattress for 100y if the value of money is not evaporating.For most of human history the money was stable. It’s the disasters of 20th century wars that eroded the value, and 21st century lack of monetary discipline that keeps driving it down now.

reply

ngruhn
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's nice when I do it. Not so nice when everyone else does it. If sitting on the money has better returns than running a supermarket, why run a supermarket? Any investment has to beat deflation. Why hire people? In fact maybe I should fire everyone to hold on to more capital and spend as little as possible...

reply

darkwater
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> If sitting on the money has better returns than running a supermarket, why run a supermarket?

First of all, because not everyone starts with inherited wealth. Also because ideally running a supermarket should give you more money even in a deflationary world. Worst thing is that you gain less money on day N+100 vs day N, but it does not mean you lose money or stop gaining it.

reply

echoangle
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> First of all, because not everyone starts with inherited wealth.

So how are you going to build the supermarket?> Also because ideally running a supermarket should give you more money even in a deflationary world.If it needs to give you more money than just saving the investment (which it should, you need to be rewarded for the risk or you would just save the money), obviously the profit margin has to be higher than it currently is, which would increase prices.

reply

MisterMunchkin
 
44 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

But a deflationary system rewards inherited wealth. It's a pyramid scheme where the person at the top splits their big piles up into smaller piles, selling them to newer people, who then sell their smaller piles to newer people...

So you'd be working for 0.000000000000000001 coins per day at the amazon warehouse, while Bezos has 500000 coins because he was born with them. There would never be a way for you to get 500000 coins, because there are only 20m coins in existence.

reply

skulk
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> First of all, because not everyone starts with inherited wealth.

So then you need an investment; you're going to have to return a multiple of the deflation rate since the risk of your supermarket shutting down is probably higher than the currency changing course.

reply

thesuitonym
 
24 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

But if sitting on a pile of cash provides returns, eventually all money will accumulate into the hands of a few ultra wealthy individuals. (Hmm...)

reply

shkkmo
 
44 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> Also because ideally running a supermarket should give you more money even in a deflationary world.

Running a super market involves owning physical goods for some period of time. With deflation, the price you can sell those goods for drops while you are holding them. In fact most economic activity involves paying for inputs (labor, materials, etc) and then later getting paid for your outputs. Deflation directly impacts profitability and can cause losses.Since deflation causes demand to drop as economic actors wisely choose to start hoarding currency and buying less, this causes a feedback loop where deflation can spiral.Similarly, inflation causes demand to increase since holding currency is unwise and it is better to spend or invest that currency than hold onto it.These two patterns mean that the neutral state (no inflation or deflation) is unstable as any deviation above or below starts a feedback loop until things fall apart. This is the boom and bust economic cycle that modern monetary management is supposed to ameliorate.Given that you want economic growth, the best solution is to try to stabilize around a small fixed amount of inflation. Arguing for the end of inflation is arguing for the end of economic growth.

reply

tshaddox
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Surely most of the people putting their money under the mattress would still need to use a little of that money to buy food.

reply

_s_a_m_
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yep, exactly why Bitcoin people dont understand their own system.

reply

FeepingCreature
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The point of money is not to reward delayed gratification. The point of money is to efficiently tabulate human preferences, and deflation directly counteracts this by introducing potentially unbounded latency at every step. That's why it destroys economies, as it has throughout history.

reply

benenrjdnz
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Can you provide an example of deflation destroying an economy in history? 
There are many more examples of inflation destroying economies.

reply

gwbas1c
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The problems with using physical gold as currency are very well known. When population would increase, or when someone would hoard it, it would cause deflation. Likewise, when a new deposit of gold was found, it would cause inflation.

This is, in part, why there were expeditions to find gold.

reply

Roark66
 
29 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Wasn't the great crisis in first half of 20th century caused by deflation?

reply

FeepingCreature
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Japan in living memory, I believe? I'm not a history buff. Google should have many examples.

reply

applfanboysbgon
 
30 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The Japanese economy is not, in any sense, destroyed. It doesn't get the infinite exponential growth unhinged economists want, but life on the ground is stable, wealth inequality is low, cost of living is low, average quality of life is very high. It is the perfect counterexample to the doctrine of chasing line go up.

reply

tekla
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Are you kidding me? Have you heard of a tiny event called the Great Depression?

The Japanese Lost Decade?Greece Debt Crisis?

reply

jcbrand
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Those are credit bubbles bursting, not the result of hard money.

reply

FeepingCreature
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, this often happens in pairs: the overcorrection after excessive credit results in a deflationary money market, destroying any chance at recovery.

reply

tekla
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This is a almost entirely oversimplified take on the Great Depression to the point of meaninglessness

For a decade before Black Thursday,there had been many things that were signs that the economy was having trouble even if the "Roaring Twenties" made it seem like everything was fine.IMO the largest issue was that American farm sector was teetering on the edge because of the dramatic drop in crop prices. This deflation screwed over farmers who mechanized with lots of debt, which because of said deflation, became impossible to pay off.The fed also implemented rate hikes to curb speculation right before 1929 which froze up credit contributing to deflationThe problem of the Great Depression was NOT the stock market crash, it arguably wasn't even the real start, just the most "spectacular" one. The problem was that with the entire economy deflating, it caused a massive downward spiral that the Fed did not really have the tools to fix, because of Gold Standard and lack of legal authorization.This was why the Govt went to extreme lengths to try and figure out how to raise prices, which is why you get programs to pay farmers to NOT grow food, and mass killings of pigs and cows and other farm animals, even as the farmers who raised those lifestock went hungry.So no, speculation was not the problem, it just sparked the key issue of the fact that the economy was deflation uncontrolled, but was just hidden.

reply

gloosx
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I think deflation-based economy could produce some interesting capital-allocation environemnt. Investment offering a 2% real return becomes unattractive if cash itself earns 2% real purchasing-power yearly. You could argue this raises the hurdle rate for investment and eliminates low-quality projects. And the counterargument is exactly the same: it raises the hurdle rate for investment and therefore some potentially good projects would never receive funding. And thats probably where the intellectually interesting argument really lives, rather than in inflation good deflation bad

reply

pjc50
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> Losing purchasing power on your money is a bug.

The idea that you can put away an amount of money under your bed that buys 1,000 loaves of bread or one GPU, leave it there for decades, and then have it buy exactly the same number of loaves of bread or GPUs is a fantasy. You can hold onto the shiny rock but you cannot stop the world rotating around you and changing all its relative prices.> For most of human history the money was stableAchieved by a combination of restrictions on trade, price stability laws, occasional crippling shortages, and quietly shaving bits off old coins. A much poorer world.

reply

jcbrand
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Except that this is literally what Gold does.

The ratio of one ounce of gold to one productive beef cow has held for a hundred years, and plausibly for around 5,000 years.A single ounce of gold could purchase a quality tunic, sandals, and belt in Ancient Rome and still buys a fine tailored suit in the modern era.https://findbullionprices.com/blog/gold-purchasing-power-wha...

reply

pjc50
 
32 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This would be more convincing if it wasn't from a site trying to sell me gold. Do people really believe that the mechanization of clothing production in the industrial era has made no difference to "real" prices?

(Rome definitely had inflation crises!)

reply

dfgknionio
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If you have a brilliant technical solution that requires throwing out all conventional economics, you don't have a brilliant technical solution. Bitcoin is rotten to its core and every excuse you make for it proves the point.

>For most of human history the money was stable.Absolutely ridiculous. People have been counterfeiting and debasing money for as long as there has been money.

reply

abenga
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Why does everyone assume that we're the ones keeping money under the mattress, not the ones who would have been paid by money otherwise not spent? All transactions have two sides, no?

reply

SR2Z
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> Deflation is a good thing, it rewards delayed gratification.

"Delayed gratification" is also provided by investments producing returns. An economy with lots of investors will outperform one where people stuff their cash into their mattress, and deflation makes it very hard for potential investments to beat that strategy.> For most of human history the money was stable.[citation needed]The Spanish empire was driven to collapse by hyperinflation. Even in the US, there were financial collapses in the 19th and 18th century. Bank runs have been a thing for as long as banks have:https://en.wikipedia.org/wiki/Bank_runYour premise is based on faulty assumptions. The existence of credit itself is what causes monetary instability, and without credit the world would look very different.

reply

pjc50
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> The existence of credit itself is what causes monetary instability, and without credit the world would look very different.

Indeed. Credit is money; ultimately anyone can expand the money supply with an IOU.

reply

benenrjdnz
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Money is destroyed when a loan is paid back. Private credit does not expand the monetary supply permanently. Only the state can increase the money supply.

reply

IAmBroom
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You are neglecting interest paid. It doesn't matter who issues the credit - the Medici family or the US Federal Reserve.

reply

fizzbuzzbarbazz
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

credit 
does
 provide a kind of flexibility that is sometimes needed, though. However, predatory lending, and the endless stacking of recursive loans, and government money printers are a 
massive
 stability issue that we're running into globally, and have (as you say) run into multiple times, historically.

My thought on this would be a dynamicaly stable currency. estimate debt and transaction activity, and the more debt and more liquid activity there is, the more deflationary currency should be. the less debt there is, and the less of a percentage of the money is actually in-use, the more inflationary the currency should be. this, though, is fairly off-the-cuff.

reply

AIiscoming
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The right thing would be to have 0 change in the value of money as long as the right amount of money exists.

The right maount of money is the amount of money we as normal humans need to work with (buying and selling stuff).Inflation and deflation are results of too much money or too little money in comparision to the production capability of a society.If i save today for my retirement and money gets less valuable when i'm retired, i have to give more 'saved' capacity back to get the real capacity (people taking care of me) and if i have more value, the others have to do more for me.Controlling this is 'work' from experts and is not solved by bitcoin btw.

reply

manwe150
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That only makes sense if money is a durable good destroyed by use. But money is improved by use and lost when put under a mattress. In economics terms, MV=PQ, and your proposal sets V low, which harms Q (goods available for sale)

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, no. The issuer of your money is really, really happy when you don't use the money. Because that means they can issue more money, without causing inflation to spike.

reply

fizzbuzzbarbazz
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

..and, you think that covers both individual and collective good?

..balance in all things. Neither being completely stingy, individually, nor being excessively spendy will benefit us, individually or collectively. ..but there are times for either.I wonder if there's a way to quantify that and put a variable on the conditions, and have an inflationary/deflationary currencynthat is dynamically stable depending on conditions...i mean, individually, most people will eventually spend, if they have much saved and it benefits them to do so. but occasionally, we do need a kick in the pants. whenever the economynis in gridlock, that's the time for inflation. ..but when peoplearespending excessively, it's a time for deflation, which discourages taking on debt, and pushes the economy towards real wealth. rewarding long-term thinkers is valuable, and has a very broad effect on society.

reply

strogonoff
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Historically, as far as I am aware, there was never a situation when deflation coincided with good things happening.

A healthy amount of inflation keeps the economy going.

reply

ciupicri
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's like saying stray dogs keep you in shape / running … because you don't want to be bitten.

reply

strogonoff
 
48 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This can be said about many conflicts between the individual and society, though. In many ways we are prevented from just taking what we want and “keep us in shape” because if everyone did the same it would be a problem.

reply

IAmBroom
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I mean, cardio is Rule #1 of the zombie apocalypse in 
Zombieland
.

reply

IAmBroom
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> For most of human history the money was stable.

Wildly inaccurate, thanks to forgery and coin shaving - sometimes even governments officially reduced the silver or gold content to make more money out of their coin reserves. Even when proto-banks began issuing letters of credit, the quasi-fiat letters were subject to loss of confidence.However, the availability and quasi-fungibility of other silver/gold currencies meant that if you didn't trust Edward's penny, you could use a Dutch penning instead. That provided an alternate path to dampen inflation, as long as the dominant currency was coinage.But it was equally hard to buy a pig or a new suit with silver pennies by the 20th century. Bank notes, even when theoretically backed by exchange for their value in precious metals (the Gold Standard), were even easier to forge, and suffered from "loss of faith" inflation (runs on banks meaning they couldn't practically be exchanged for 14 pounds of silver pennies).

reply

PowerElectronix
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I like the alternative even less, as it incentivises spending more than you would and taking on debt you don't really need.

reply

velcrovan
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, countries have experienced moderate inflation and moderate deflation, ask the ones who lived through both which one they preferred.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Moderate deflation is fine, it's good even. But only as long as nominal GDP stays stable.

See the so called 'Long Depression' in the 19th century. Which was only a depression of the price level, everything else did well.For a more sectoral example, see how computer hardware used to get cheaper and cheaper all the time, but total spending on hardware went up.

reply

morning-coffee
 
31 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That is 
https://en.wikipedia.org/wiki/Jevons_paradox

reply

rerdavies
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> taking on debt you don't really need.

How does that work? When inflation goes to 18%, borrowing rates go to 23%.

reply

FeepingCreature
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I suspect it was a deliberate strategy to create scarcity, allowing the original creators to massively cash out. If you make an inflationary distributed currency, it may work better but it's a bit harder to get rich on it.

reply

nickez
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The other option is to make everyone gamblers, either speculate on properties or stocks. Pick your poison.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

During much of the industrial revolution, gold also rose in real price. But people still did business in gold standard countries.

(Hint: the gold might be under a mattress or in a vault, but you can still an almost arbitrary amount of gold denominated debts and loans and deposits.)

reply

chabska
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

There is zero evidence that deflation has any effect on spending.

At the micro level, the change in price is too small for every day purchases. Would you starve yourself for one day because the pizza will be one cent cheaper tomorrow?At the macro level, every interest rate will be adjusted based on the base inflation/deflation rate, so the net effect is zero. Banks will offer a higher profit rate for their savings account to entice people to deposit their money in the bank instead of their mattress.

reply

snapcaster
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not silly, it harnesses some of the mechanics behind ponzi schemes to encourage viral spread. Early entrants are incentivized to evangelize it to newer ones

reply

derangedHorse
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Tail emissions and infinite divisibility are proposals to address this.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Well, they are infinitely divisible in principle, so it doesn't matter too much.

(At the moment, there's a smallest fraction you can send on the network, but they can change that.)

reply

chinathrow
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Can't the change the 21M?

reply

eru
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, they could change that, too.

However I expect that adding more decimal places will actually happen, but adding extra bitcoins won't.

reply

tigereyeTO
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

No they are not. There are only 8 decimal places, not infinite.

reply

fsflover
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

AFAIK it can be changed later.

reply

orliesaurus
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Eventually with quantum computing we will be able to recover those wallets right? (Technically)

reply

tigereyeTO
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That depends on whether the public key has been exposed.

Bitcoin addresses encode the ripemd160 hash of the public key, so by default when payments are made to new addresses they are not quantum crackable.But when someone spends from an address they publish the public key to the chain as part of the spend. From then on, any new deposits sent to the same address are at risk of quantum attack

reply

briansm
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The hash is merely a convenience, the _actual_ public key used in transactions is present in the ledger and available to anybody who wants it.

reply

notpushkin
 
18 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

How does that work?

Suppose I make a paper wallet on an offline PC, write down the address and discard both keys. If I now send some BTC to this address, how does the client figure out the public key?

reply

thih9
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Technically it might be more profitable to mine extraterrestrial diamonds.

reply

rbreve
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

at this point bitcoin will be worthless

reply

jakemanger
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Really hope so too. Would be devastating

reply

wavemode
 
47 minutes ago
 
 | 
prev
 | 
next
 
[–]

well, I just emailed the project just to see if they're aware of it

part of me feels like this is most likely a defunct wallet and nobody involved with the project has the keys anymore

reply

DataDive
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

What happens if some of those 
tax the unrealized gains
 bills pass in some country where they have obligations?

They would have to either pay the tax on gains or write off losses.

reply

mikeocool
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Neovim’s current donation page says that funds are managed by OpenCollective — a 501c6 organization in the US. 501c6’s are tax exempt.

So assuming they are the holders of the bitcoin as well, there would be no tax liability.

reply

fl4regun
 
32 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

then they would sell some of the bitcoin and pay the taxes. If they don't have the wallet anymore then they don't pay any taxes.

reply

nullocator
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds good.

Edit: it seems perfectly acceptable and ideal even for society to say there is a cost to wealth. As others have mentioned Neovim is in the US is likely mostly tax exempt so this hypothetical doesn't even apply to them.

reply

wiseowise
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Theft is good? What?

reply

fhdkweig
 
56 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We slid down that slope a long time ago. Taxes are good and pay for my important things, up until the moment they pay for someone else's important things, then it is theft.

reply

nullocator
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm not sure what argument you're making? Taxes are theft? Consensus on that type of thinking seems to be hard to come by.

reply

superxpro12
 
25 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

consensus is easy. its that people want to not pay taxes and still use public infrastructure anyway. thats the real theft.

reply

philipallstar
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Surely only an absolute lunatic would pass that sort of law. And by then it's too late, because it's Socialism with extra steps.

reply

sebzim4500
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Doesn't Switzerland do this instead of capital gains? Makes sense IMO, much better to tax wealth than discourage transactions.

reply

spacebanana7
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Taxing capital assets by taking large portions of their value destroys value by forcing liquidity events. Think forcing sales of farms, factories and domain names.

I much prefer land value taxes (and similar taxes on non capital wealth like jewellery) and leisure taxes (ideally taxing people for every hour they don't work). Of course these are difficult to administer in practice, but British business rates and US overtime tax discounts effectively approximate this.

reply

bitmasher9
 
38 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The idea of taxing people for not working an hour sounds incredibly dystopian.

reply

overtone1000
 
16 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I had the same reaction. It also seems easy to pull apart. What about disabled people who are unable to work?

I think something more like "investment income should be taxed at a higher rate than income earned through labor," accomplishes similar goals but is more intuitive and less problematic.

reply

superxpro12
 
27 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What will they think of next? tying healthcare to employment that you lose the moment you get fired to meet quarterly profits? Madness i tell you!

reply

axus
 
51 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If the government forced transfer of ownership %, instead of forcing a sale, it would be not as bad?

reply

tim333
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Apparently not. Googling, no one seems to actually do it in spite of some politicians talking about it.

It seems quite a bad idea from a practical point of view.Not so much because it's socialist but it leads to all sorts of extra paperwork for no good reason. Like say you buy some utility company share for your retirement in 20 years and it fluctuates. Do you want to be valuing it and paying tax and then claiming it back when it goes down every year for 20 years or just declare the gain at the end?

reply

philipallstar
 
22 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, it is socialist in that the government basically gets to own more of everything you own every year.

reply

briandw
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Really? How? Show me a country that taxes wealth and is prosperous. Taxing unrealized gains results in owing tax on money you don’t have and makes starting a funded company impossible.

reply

superxpro12
 
26 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

and on the other hand we have trillionaires who spend their wealth on fascist party propaganda and censorship

reply

wing-_-nuts
 
38 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Why not? We tax property every year on it's assessed value. I think it's pretty clear that the wealthy will need to pay more taxes throughout the world to deal with an aging population.

I'm a little tired of billionaires 'buy, borrow, dying' to get around the paltry taxes they're currently subject to. We need a harder tax to dodge.

reply

carefree-bob
 
36 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Why would taxing the wealthy be relevant to an aging population? Do you think that we tax stuff? We just tax money to buy stuff. If a nation produces less stuff, then spending more will just cause prices to go up, but will not result in the production of more stuff to go around.

reply

wing-_-nuts
 
21 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Because our current social safety nets all work by assuming the next generation pays for the care of the current elderly. Those elderly do need 'stuff' they need doctors and nurses and nursing homes. Thus taxes will have to go up, and if it has to, it may as well be progressive.

reply

superxpro12
 
28 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The fascism we CURRENTLY HAVE is far more preferable

reply

IAmBroom
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Oh, no, not Socialism! That's worse than attending a Macklemore concert!

reply

kriops
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Macklemore concerts didn't kill 100 
million
 people at minimum.

reply

nwsm
 
51 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Do we have an estimate on the number of people capitalism has killed? Serious question.

Include deaths due to poverty and lack of affordable healthcare under capitalism, overworking and dangerous working conditions, and all wars and counter-insurgency waged on alternative economic systems globally.

reply

thesuitonym
 
32 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, people who die as a direct result of capitalist economics are not counted because that would be inconvenient and wouldn't fit the CIA's narrative.

reply

carefree-bob
 
31 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You'd need a definition of capitalism first. Since for most people, it's just the default mode of living -- e.g. the very term "capital" comes from "head", as in "head of an ox", as early cattle culture practiced capitalism, so it predates the agricultural revolution and was practiced by nomadic groups.

A lot of the language, for example "interest" comes from cattle culture. If you think about it, a cow produces other cows, so it bears interest. You can eat the cow (consume capital) or let the cow produce a stream of milk. Ownership of cows gave you great power.So asking "the number of people killed by capitalism" is like asking "how many people were killed by everything that's not communism", which is pretty inane, since the point of communism is that it is an ideology, and mass killing for an ideology (that's not religion) is a part of the modern world, not the traditional world of cows and capital. The first ideological genocide was the slaughter of the Vendee peasants by the French revolutionaries, but it was merely the first of many times that urban ideologues slaughtered rural farmers.

reply

wing-_-nuts
 
36 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Man I always love the straw men you guys stand up to fight this. More taxes = socialism, and not nordic socialism, no, actually, communism. Therefore mass death / genocide. Ok. Sure jan.

reply

philipallstar
 
11 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nordics are not socialist[0]. Socialism is central planning and control, sometimes created out of mass killings[1] [2], and often creating many deaths just from incompetent central mismanagement[2] [3] or grisly bureacratic rules[4].

[0]https://www.investors.com/politics/commentary/denmark-tells-...[1]https://en.wikipedia.org/wiki/Excess_mortality_under_Joseph_...[2]https://en.wikipedia.org/wiki/Khmer_Rouge[3]https://historyincharts.com/chinese-death-totals-great-leap-...[4]https://www.bbc.co.uk/news/world-asia-china-34667551

reply

tancop
 
13 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Communism is not socialism. What Stalin, Mao and Kim Il-sung did was wrong because they did basically the exact 
opposite
 of a socialist policy, centralizing power out of workers hands and taking all surplus value into the central government instead of distributing it.

They all turned into paranoid dictators who did everything they could to stay in power, except for Mao who got lied to by other party leaders and regretted it in his final years. None of them represent what socialism really is. Tankies who worship them are a small minority.

reply

wyclif
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

The project no longer uses that Bitcoin wallet for bounties.

reply

ricardobeat
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

What does that mean for that donation, and why is the wallet still listed on the website?

reply

ramijames
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think that a large part of the priced in "value" of Bitcoin is just lots and lots of Bitcoin that nobody can access anymore.

reply

abirch
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Bitcoin's supposed to be "liquid" but I'm wondering what happens when there's a forced liquidity event.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What do you mean by forced liquidity event?

reply

abirch
 
38 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If people are trading bitcoin on margin or if Strategy is forced to sell a large percentage of its holdings.

reply

altmanaltman
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I mean, it's the opposite of that; it's forced illiquidity when people lose access to their keys. There is no way to gain access to those coins and you cannot "force" liquidity on the bitcoin protocol.

reply

zicohacks
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

I checked their official donation channel is OpenCollective. I think the Bitcoin address is no longer being used and they just forgot to update the footer

reply

philipwhiuk
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Yeah, someone probably deposited an amount a long time ago and it's sat there earning interest.

reply

benenrjdnz
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Bitcoin doesn’t pay interest. And that’s a good thing.

reply

cranberryjoe
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Rainy day fund. Everybody needs one. Love neovim for living under their means, great program!

reply

tosti
 
44 minutes ago
 
 | 
prev
 | 
next
 
[–]

At least a part of it should go to Kibaale Children's Centre imho.

reply

pluc
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

hodl

reply

jakemanger
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

They've hodled from the original ~$200,000 donation to $1.2 million, now down to $800,000.

If they haven't accidentally done this, they've definitely got some balls

reply

esskay
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I know you're joking but keeping bitcoin now really does feel like a poor investment given it's showing no signs of ever being revived.

reply

w4yai
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

https://bitcoindeaths.com/

reply

WarmWash
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The problem with bitcoin is that the only real evidence of it's success is it's price has gone up.

It's very reminiscent of stocks that rocket 500% in a year, while almost nothing in the underlying company changed.

reply

burkaman
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Many of these quotes are technical or social critiques of Bitcoin, not claims that it is "dead". Here's one for example: 
https://bitcoindeaths.com/posts/2023-10-26-every-single-bitc...
. It is dishonest to frame this as a disproven claim just because the price has gone up since the quote. The truth of this claim has nothing to do with the success or failure of Bitcoin.

A couple other examples:https://bitcoindeaths.com/posts/2019-02-07-bitcoin-inefficie...,https://bitcoindeaths.com/posts/2024-11-20-nobel-prize-winni.... This bothers me, you can't respond to a genuine critique with "but look how much money I've made!"

reply

sjbzbeiks
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

yeah I mean it just depends on time horizons, if you bought at 117k you are hurting now if you need the money ASAP.

Also, I gotta say I do not think Bitcoin is a bubble or whatever (IMO a real value there), but really this sort of site makes it seem like it is a bubble with the sort of "blind to history" boosterism.Go read Reminiscences of a Stock Operator, or Market Wizards series, Extraordinary Popular Delusions and the Madness of Crowds, or any number of books about financial history and there are endless people saying 'it will never die and all the doubters are just wrong' before any big market crash.

reply

benrutter
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Also, I gotta say I do not think Bitcoin is a bubble or whatever (IMO a real value there)

It's worth saying something with real value can still have a bubble - both bicycles and the internet were huge market bubbles at one time, but they're also undeniably valuable.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

To play Devil's advocate:

Let's assume bitcoin has a tiny but positive probability of running the world economy in, say, 50 years. Ie bitcoin is a lottery ticket.The fair value for a lottery ticket is some positive number. In 99.99..% of cases, the ticket will expire worthless. (In 0.00..1% of cases it will be worth quadrillions.)The fair value of a lottery ticket is not a bubble, even if most lottery tickets expire worthless.---Now, of course, it's still possible to overpay for lottery tickets. Eg if you buy an actual lottery ticket in retail, the whole transaction usually loses you at least 50 cents on the dollar for lottery taxes alone.But that's a separate issue.

reply

maxerickson
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You argument is that it could have some long term value, which is different than a lottery ticket (which has a calculable minimum expected value at time of purchase).

reply

eru
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Slightly more abstract: my argument is that assets with a very skewed probability distribution of future value will have a positive current value, even if in the vast majority of cases, they'll be worthless in the future.

Lottery tickets were only an example.

reply

imjonse
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

to be fair the majority of the statements that site mocks are not about bitcoin being dead but being a ponzi scheme, evil, hard to use by normal people, silly, a risky investment etc.

All are criticism that can be evaluated on their own but it's irrelevant how much bitcoin grew since they were made.

reply

pluc
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

what is dead may never die

reply

suddenlybananas
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The log scale is awfully misleading, especially since money doesn't really work like that.

reply

cannonpalms
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Anything but a log scale would be misleading. When showing long term growth of something that has grown so drastically, it is imperative to use a log scale so that 10% gains look consistent over time. Especially in finance.

reply

john_strinlai
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

you can press the "linear" button if you'd like.

but i think the primary point of the comment was to highlight the"Bitcoin has been declared dead 478 times"part

reply

AIiscoming
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I hate this side.

The first quote i got was "Bitcoin is evil" and then the subtitle "bitcoin worth now 10000%"Bitcoin is still evil and it has very much to do with the value of bitcoin.This page is ignorant and shit :(

reply

accountrequired
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Bitcoin died *again*? hehe :P

reply

esskay
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

oh i dont think its 'dead' in the way people often describe. More...done. Like, the period of obscene growth is over and its now seemingly settled into a fairly dull investment with mediocre returns.

reply

dmantis
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Depends on the actor.

From western perspective, maybe, but there are many people in the world who don't trust neither their government, nor western ones: Iranians, Russians, some Chinese, etc.BTC is a nice safe place for money, which can't be touched by neither of state adversaries. Underperforming some other asset classes is totally acceptable, when your expectation for the brokerage account is effectively zero after arrest/freeze/sanctions.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I would buy your argument, if bitcoin were the only cryptocurrency.

For most of the people you mention, a fiduciary cryptocurrency like these 'stable coins' is the better product.(If you don't trust the value of the USD, and thus don't want a stable coin linked to that, you could use one that's linked to Swiss Franks or the Singapore dollar.)

reply

dmantis
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> could use one that's linked to Swiss Franks or the Singapore dollar.

Well, if only we had something like that with a proper liquidity!USDT/USDC are useful for the exchange to fiat, but have freeze function in their contract, thus posing a risk for big longterm savings, and they rot under the inflation (which btc generally beats).There are indeed a couple of unfreezable stablecoins, but they don't have mainstream adoption and proper liquidity. USDT kind of captured the market by being first, and USDC is heavily pushed by the major institutional players, so here we are.But that's true, it's more about crypto in general.

reply

AIiscoming
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

BTC can be touched by state actors easily.

Has been proofen often enough.State actors can just hurt your famiily. State actors can setup a shadow bitcoin infrastructure and give you the feeling that your wallet is a save bitcoin wallet. They can Hijack the website you download the initial bitcoin wallet, the nodes you talk to.

reply

dmantis
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> State actors can just hurt your famiily.

That actor has to know that you have something to be touched for in the first place. Which is not the case if you buy crypto without KYC unlike with the classical brokerage, for example.> State actors can setup a shadow bitcoin infrastructure and give you the feeling that your wallet is a save bitcoin wallet. They can Hijack the website you download the initial bitcoin wallet, the nodes you talk to.Is paranoid and not serious. Yes, they can do a lot in theory, but on practice even basic level opsec avoids it.In reality if somebody from the state is already after youexplicitlyfor real, you are going to die or be in prison. I can't really argue with that. Most people are not under active confrontation with the governments, but under passive snooping and pity everyday legal risks that make their lifes miserable.In most cases they don't send hitmen neither for "foreign agents" labeled people from Russia, nor for sanctioned Russians outside from the US, for example. My point is about people who are not active fugitives, but, you know, want to keep their stuff with them without risking neither their country bank freeze, nor western-based financial infra freeze because they hold the wrong passport.

reply

AIiscoming
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If russia or china has a real interest because relevant amount of people start using it, they would easyl be able to stop this.

Chinese firewall is real.Putting fear into people with propaganda is real.And yes i find my shadow bitcoin infrastructure not paranoid at all. It would be the first thing a state actor would do after closing everything through their state firewalls.

reply

pjc50
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

People found a new way to turn electricity into money at the expense of the atmosphere: AI.

reply

briansm
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Fossil fuels were always worth way more than people ever realized.

Like Joni says, "you don't know what you've got till it's gone."

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Ethereum, for all its other faults, has shown that burning lots of electricity is not necessary for cryptocurrencies.

reply

sph
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Well, that’s what people have said all the way to $70k+ price.

reply

ForHackernews
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's underperformed the S&P500 over the last 5 years, but you know what they say about past performance not predicting future returns. Maybe AI will unlock an untapped reservoir of ever-greater fools.

reply

singiamtel
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Isn't that a good thing? The main argument I've heard against using bitcoin as currency is that it's too volatile.

reply

hattmall
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It would be, except when the primary value proposition is capturing the upside of that volatility. In the case of BTC a sustained lack of volatility is going to create significant downward pricing pressure. At some point that will trigger a run and as stakeholders have condensed the rut will get deeper and deeper as the upside of the volatility swings continually lower.

reply

nicce
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> The main argument I've heard against using bitcoin as currency is that it's too volatile.

Also the transaction cost. Is it any better?

reply

bittwiddle
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

https://bitcoincalculator.tools/calculators/lightning

Its about 2 cents for a coffee(10k sats ~= 7.6 usd), or 0.2%.Versus 1.5-3.5% that visa typically charges.

reply

Forgeties79
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

But the volatility hasn’t gone away. Compared to previous periods of broader interest in it (rife with the awful FOMO habits of people) sure it’s not as bad, but it still fluctuates wildly and without warning. In the past 12mo it has gone as high as 120k and as low as 60k, currently around 76k. You cannot reasonably use a currency like that. Your wealth can’t be doubling or halving over months with 10pt swings over a single day being a common occurrence. How much mental energy and planning would have to go into timing any and all purchases and earning?

Better odds than a casino, but still basically a casino.

reply

zeofig
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Buy signal

reply

Razengan
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

This could become the premise of a near-cyberpunk heist movie..

Similar to Swordfish? :)

reply

colesantiago
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Bitcoin really isn't money.

They should send it to a dead wallet instead.

reply

egorfine
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

You should lead by example. Could you please purchase $800k of bitcoin and then send to a dead wallet for all of us to see?

reply

colesantiago
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> You should lead by example

Neovim first.I've never "purchased" Bitcoin or any cryptocurrencies ever because it is not money or legal tender and never will.

reply

AIiscoming
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What is this stupid argument?

Your 'point't doesn't make any sense at all?

reply

AIiscoming
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

True and its also not compareable to gold.

But as long as others giving you real money for this garbage, it would be better to use it for a project like neovim :)

reply

deniska
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

To never have experienced a usefulness of cryptocurrency is a privileged position to be in.

reply

AIiscoming
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ah yes lets ignore the tons of co2 which has direct impact of primarily poor people around the whole globe and the energy stealing which also is happening through bitcoin to make the case for alll of this for a handful of techsavy people in a handful of countries who are apparently now able to get their money through crypto but also have to now find people taking this?

Yeah no.You know what happened in el salvador? A Lot of people got their initial crypto stolen.And you know what real people do? They use euros and dollars as hard cash. Like i have seen in Iran.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Ah yes lets ignore the tons of co2 which has direct impact of primarily poor people around the whole globe and the energy stealing which also is happening through bitcoin [...]

That's true for bitcoin, but not for cryptocurrencies in general. Especially those that moved to proof-of-stake.

reply

tigereyeTO
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

“Yeah no.”

Ah yes let’s ignore the tons of energy being used in giant data centers run by visa and Mastercard to operate the payment cards used by billions of people around the world.“Yeah no.”You know what happened in USA? A lot of people got their cash stolen.Your arguments are as coherent as the dissonant “Yeah no.”

reply

AIiscoming
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

"Yeah no" have had these arguments for ages and nothing has changed.

Bitcoin uses a massive amount of energy and has neither the transaction amount, nor the transaction speed and a LOT of features missing which visa/mastercard and a normal bank provide.Losing your key to a wallet? BTC goneFraud? Yeah and now what?Seller or buyer protection? hahaha noLets not compare apples with stones okay?

reply

tigereyeTO
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Losing your wallet or purse? Cash gone. 
Fraud? Yeah and now what?

Seller and buyer protection don’t exist with cash either my dude.If you’re going to compare apples and stones at least do it honestly.Each payment option has its own advantages and disadvantages, and it’s fantastic that we have the freedom to choose from a variety of products and services to use.I hated it when PayPal froze my funds and wished there was an option where a middleman couldn’t decide who I am allowed to pay. Then Bitcoin came along. For me, Bitcoin works great. 
For you, your method of choice works great and I’m happy for you.

reply

AIiscoming
 
46 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ah yes my 100.000 Euros i keep in my wallet and purse. Sure lets keep comparing apples with stones.

Yes seller and buyer protection exists with cash. I pay regularly with cash in a ot of shops.I wouldn't mind bitcoin if it would actually do the things and has any features besides gambling. And if it wouldn't add additional strain on our planet and the future of humanity.What do you do with bitcoin? Be honest. Gambling? Do you really have most of your assets (if you have any relevant ones) in bitcoin? Yes? No fiat besides daily use?Did you get 'rich' from the money shifting from someone else to you?

reply

Roark66
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Well the "non comparability" to gold has to do with the fact you need a functioning network to spend (good luck verifying a key by hand with a calculator). You can spend gold even when you're transacting with the last person on earth.

However the value is as much as people agree to value it and for a typical person both have little utility. Maybe BTC has even more utility because it facilitates remote transfers of value very easily.So as long as the network exists there is intristic value in BTC. I believe more than one can say about gold.Still, a good portfolio will contain both gold (in small coins likely as a kind of "war hedge") and BTC as a kind of hyperinflation hedge.

reply

eru
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> You can spend gold even when you're transacting with the last person on earth.

Not really. Try using gold in retail.

reply

itintheory
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Goldbacks have entered the chat. [0]

[0]https://www.goldback.com/

reply

eru
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My local coffee shop only takes long government currency.

My bank already allows me to keep my bank account money in stocks and sells units whenever I spend. (We have no capital gains tax here, so this is less insane than it sounds.)

reply

AIiscoming
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

BTC has less facility in an emergency because energy is gone, internet is gone, bitcoin miners are gone and nodes are gone.

Your gold might give you food, your btc is rotting on some hard disk on a computer you can't / wont use.BTC as a hyperinflation hedge? We have seen already what happens to btc when money gets tide: BTC drops.

reply

colesantiago
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

A dead wallet has better use for Bitcoin though.

We don't know where the Bitcoin has come from, so it needs to go through extensive anti money laundering checks.Save the hassle of all of that taxes, accountancy and just send everything to a dead wallet.

reply

done_lurking
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In what country does a bitcoin donation need to go through an "anti money laundering check"? Also, you could pay a lawyer 100k to handle the taxes and accounting and you would still have 700k left over.

reply

colesantiago
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Any country which bans Monero and their mixers being sent to exchanges which are then flagged by OFAC on tainted cryptocurrencies.

Nah, you would have a lot more to pay in taxes.Might as well send it to a dead wallet, it's not real money anyway in many countries as legal tender.

reply

AIiscoming
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Fair enough

How about they use the bitcoin to donate?

reply

olexsmir
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Bitcoin isn't really money same way as US dollar isn't really money.

reply

AIiscoming
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not true.

Behind the US Dollar is a whole country and a lot more countries if not the whole world.Behind Bitcoin are random investors, random people.Bitcoin is also rarly traded directly it uses fiat for most. So Bitcoin is even dependend on this proof-of-stake system.Bitcoin is a proof-of-work system dependend on the best proof-of-stake system we have.

reply

gitowiec
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Exactly this! It was rendered money by some minds.

reply

nullbio
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Unlike that paper money. That paper money was created by the Gods!

reply

colesantiago
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It is even more useless than fiat.

reply

eru
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It doesn't have to be useful as money to be useful as a donation.

You just have to be able to sell it for money.

reply

JimBlackwood
 
4 hours ago
 
 | 
prev
 
[–]

I imagine they might wait, to make sure it’s legally obtained Bitcoin.

reply

a3w
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

In which country would waiting help?

reply

cyberpunk
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In Germany at least if you've held the coin(s) for 7 years before selling you don't need to pay tax on the profit.

Not sure how this applies to donations though, and of course this will almost certainly be changed in the future, .nl is leading the way in taxing _unrealised_ gains; we are sure to follow!

reply

T0Bi
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's one year, unless something changed recently.

reply

la_fayette
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

1 year

reply

ksk23
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

One year yes, and politics wants to change it..

reply

yieldcrv
 
3 hours ago
 
 | 
parent
 | 
prev
 
[–]

Something that takes 5 seconds with bitcoin, faster than any other property type, is something you rationalize as taking 7 years

Why does HN collectively tolerate this level of understanding when it comes to crypto

reply

nottorp
 
2 hours ago
 
 | 
root
 | 
parent
 
[–]

> Something that takes 5 seconds with bitcoin, faster than any other property type, is something you rationalize as taking 7 years

> Why does HN collectively tolerate this level of understanding when it comes to cryptoWell that's really funny. Because the 7 years are about tax liabilities not the speed of bitcoin transactions.So maybe you made a statement about crypto advocates here...

reply

yieldcrv
 
2 hours ago
 
 | 
root
 | 
parent
 
[–]

Legally obtained bitcoin is what the person I responded to said, suggesting anti money laundering concerns which are the concerns I responded to

And the tax liability sister comments all disagree with each otherNotably, the parent commenter hasn’t replied at all yet

reply

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search: