---
title: Solving Factorio Quality − Exyr.org
url: https://exyr.org/2026/solving-factorio-quality/
site_name: hackernews_api
content_file: hackernews_api-solving-factorio-quality-exyrorg
fetched_at: '2026-09-30T22:50:54.376511'
original_url: https://exyr.org/2026/solving-factorio-quality/
author: laurenth
date: '2026-09-29'
description: Solving Factorio Quality
tags:
- hackernews
- trending
---

I play Factorio the normal way: by writing matrix math code to plan the factory.

But we’ll get to that.
Or,TL;DR, go to my newonline calculator tool.

### Intro to Factorio and Quality

Factoriopretty much founded the factory video game genre:
you play a character who harvests resources and combines them to craft increasingly complex items,
which in turn enable more sophisticated crafting.
So far this sounds a lot like Minecraft and many other survival games,
but what sets factory games apart is the focus on automation:
soon enough, most of the crafting is done not “by hand” by the character
but by increasingly many machines,
with various forms of logistics like conveyor belts to move items between machines
or wherever they need to go.
Some factory game go further and remove the player character altogether.

As “technologies” are unlocked in-game, Factorio offers many mechanisms to improve production.
One of them is modules: crafting machines have a (limited) number of slots
to accept different kinds of modules that affect their stats:
speed modules make the machine run faster at the cost of more energy consumption,
productivity modules increase yield from the same ingredients at the cost of speed and energy,
etc.

Released in 2024, the Space Age extension adds new game mechanics including Quality:
every item and recipe now come in five quality tiers:
⚀ normal, ⚁ uncommon, ⚂ rare, ⚃ epic, and ⚄ legendary.
Depending on the item, each tier improves stats such as making crafting machines faster
or making productivity modules more productive.
High-quality items can be crafted directly from ingredients of the same quality,
but the only way toincreasequality is through the new quality modules.

 Quality modules can have quality too.
 Source: 
Factorio wiki

Modules affect the probabilityQQof any quality increase.
For a given craft, each quality tier increase after the first is another 10% chance.
We can build a table of the probabilities of output quality depending on input quality:

 Source: 
Factorio wiki

For example, the maximum possible quality chance in a machine with four module slots is 24.8%:

 Jumping from normal to legendary in one step is only a 0.0248% chance.
 Source: 
Factorio wiki

Some players dislike the introduction of randomness
to a game that wasmostlydeterministic, butwith enough repetitions probabilities become ratios.

The probabilities are balanced so that
even with multiple crafting steps (each a potential quality jumps),
getting high-quality items unavoidably involves also crafting many unwanted low-quality ones.

To avoid the factory grinding to a halt when storage eventually gets full,
Space Age also introduces the recycler:
a new machine that destroys any item and (usually) returns 25% of its ingredients.
This enables players to design “upcycling” contraptions
that craft and recycle in a loop with quality modules
until items reach the desired quality, at the cost of consuming many more ingredients:

 Source: 
Factorio blog

### Factory planning tools

Some video games are partly “played” outside of the game itself.Blue Princefully expects its players
to keep extensive notes of everything they see,
but doesn’t provide an in-game notepad or similar tool.
Factory games lend themselves
to buildinglarge spreadsheetsfor resource accounting,
but a select few players decide that spreadsheets are not powerful enough for factory planning
and spent countless hours programmingdedicated toolsthat reproduce much of the game’s math to accurately model a production chain.

 Example production chain in 
Factoriolab

This is all optional in factory games, it’s perfectly viable to play it by ear
and just build more when seeing something lacking.

But I do like to plan in advance:
how many machines of each kind do I need? How much yield can I expect? Where are the bottlenecks?
The looping nature of quality upcycling makes this particularly challenging
either to guess, or to calculate with existing tools.

### Matrix math

Let’s imagine:

* Some ingredients (for example iron plates)
that come from an arbitrary production chain that may involve quality modules.
Any given ingredient has a probability to be in each quality tier:
⚀ normal, ⚁ uncommon, ⚂ rare, ⚃ epic, and ⚄ legendary.
* Enough assembling machines with each recipe tier
to craft all ingredients into some product (for example pipes).
These machines have quality modules so that the a quality chance is 10%.

Let’s track the possible fates of one item:

A product of a given tier can come from ingredients of the same tier or lower.
The total probability for this outcome is the sum of (independent) probabilites
of different ways to get it.
In turn, those are the product of the percentage chance of a specific quality jump
times the probability of having the corresponding ingredient tier in the first place:

p⚀=i⚀⋅90%p⚁=i⚀⋅9%+i⚁⋅90%p⚂=i⚀⋅0.9%+i⚁⋅9%+i⚂⋅90%p⚃=i⚀⋅0.09%+i⚁⋅0.9%+i⚂⋅9%+i⚃⋅90%p⚄=i⚀⋅0.01%+i⚁⋅0.1%+i⚂⋅1%+i⚃⋅10%+i⚄\begin{align*}
p_⚀ &= i_⚀ ⋅ 90\% \\
p_⚁ &= i_⚀ ⋅ 9\% &+ &i_⚁ ⋅ 90\% \\
p_⚂ &= i_⚀ ⋅ 0.9\% &+ &i_⚁ ⋅ 9\% &+ &i_⚂ ⋅ 90\% \\
p_⚃ &= i_⚀ ⋅ 0.09\% &+ &i_⚁ ⋅ 0.9\% &+ &i_⚂ ⋅ 9\% &+ &i_⚃ ⋅ 90\% \\
p_⚄ &= i_⚀ ⋅ 0.01\% &+ &i_⚁ ⋅ 0.1\% &+ &i_⚂ ⋅ 1\% &+ &i_⚃ ⋅ 10\% &+ i_⚄
\end{align*}

(The percent sign can be thought of as implicit division by 100,
so that “percentage of” is the same as multiplication.)

Here the percentage coefficients looktransposedacross the diagonal compared to the quality jump probability table from the wiki,
but that’s only because we’ve arranged product tiers vertically.
Instead let’s group the probabilities of different tiers of the same item into row vectors:

product=(p⚀p⚁p⚂p⚃p⚄)ingredient=(i⚀i⚁i⚂i⚃i⚄)\begin{align*}
product &= \begin{pmatrix*} p_⚀ & p_⚁ & p_⚂ & p_⚃ & p_⚄ \end{pmatrix*} \\
ingredient &= \begin{pmatrix*} i_⚀ & i_⚁ & i_⚂ & i_⚃ & i_⚄ \end{pmatrix*} \\
\end{align*}

Now oursystem of linear equationscan be written as a single equation where a vector
ismultipliedby
atransition matrixthat matches the wiki’s table:

products=ingredients⋅Tquality(10%)Tquality(q)=(1−q9q109q1009q1000q100001−q9q109q100q100001−q9q10q100001−qq00001)\begin{align*}
{products} &= {ingredients} ⋅ T_{quality}(10\%) \\[1em]
T_{quality}(q) &=
\begin{pmatrix*}
 1-q & \frac{9q}{10} & \frac{9q}{100} & \frac{9q}{1000} & \frac{q}{1000} \\[0.3em]
 0 & 1-q & \frac{9q}{10} & \frac{9q}{100} & \frac{q}{100} \\[0.3em]
 0 & 0 & 1-q & \frac{9q}{10} & \frac{q}{10} \\[0.3em]
 0 & 0 & 0 & 1-q & q \\[0.3em]
 0 & 0 & 0 & 0 & 1
\end{pmatrix*}
\end{align*}

As an edge case, zero quality chance means no tier transformation.
The corresponding transition matrix is
theidentity matrix:Tquality(0%)=I5T_{quality}(0\%) = I_5

This may not seem like much progress,
but now a multi-step process can be computed through successive matrix multiplication.
For example mining iron ore with 7.5% quality chance,
then smelting it into iron plates with 5% quality chance, then crafting pipes with 10% chance.
With no productivity bonus, we get these probabilities of end-products:

pipe=(10000)⋅Tquality(7.5%)⋅Tquality(5%)⋅Tquality(10%)=(0.9250.06750.006750.0006750.000075)⋅Tquality(5%)⋅Tquality(10%)≈(0.878750.105750.0136130.0016650.000223)⋅Tquality(10%)≈(0.7908750.1742630.0296780.0044670.000719)\begin{align*}
pipe &= \begin{pmatrix*} 1 & 0 & 0 & 0 & 0 \end{pmatrix*} ⋅
 T_{quality}(7.5\%) ⋅
 T_{quality}(5\%) ⋅
 T_{quality}(10\%) \\
 &= \begin{pmatrix*} 0.925 & 0.0675 & 0.00675 & 0.000675 & 0.000075 \end{pmatrix*} ⋅
 T_{quality}(5\%) ⋅
 T_{quality}(10\%) \\
 &≈ \begin{pmatrix*} 0.87875 & 0.10575 & 0.013613 & 0.001665 & 0.000223 \end{pmatrix*} ⋅
 T_{quality}(10\%) \\
 &≈ \begin{pmatrix*} 0.790875 & 0.174263 & 0.029678 & 0.004467 & 0.000719 \end{pmatrix*}
\end{align*}

### Quality strategies

While it is possible to use quality modules as much as possible and deal withEvery tier Everywhere All at Once,
here we’ll focus on smaller self-contained systems.

#### “Gambling”: opportunistic quality without recycling

The easiest but also least effective is to craft from normal-quality ingredients,
with quality modules, and not recycle anything.
This can be done before unlocking the recycler but is only viable for a small number of items,
such as crafting a few hundred asteroid collectors to hope to get a dozen uncommon or rare ones
for an early space ship.

This is improved when the factory has another use for normal-quality items.
For example if placing thousands of normal-quality solar panels on the ground,
crafting them with quality modules gives a better yield of higher-quality ones for space ships
before the output buffers fill up.

With a single step and no loop, this is simplest to calculate:
the expected product tier distribution is the first row of theTquality(q)T_{quality}(q)transition matrix
or of the probability table found on the wiki.

#### “Washing”: pure recycling loop

For most items, the recycler reverses the main crafting recipe and returns 25% of the ingredients.
But some items don’t have a crafting recipe (like ore)
or it is considered irreversible (typically smelting and chemical processes).
In that case the recycler produces either nothing or, 25% of the time, the same item.
This process can improve quality if the recycler has quality modules.
Repeating it in a loop, eventually all items will be either destroyed
or improved until they reach any desired quality tier.
Self-recycling items is arguably not the common case but let’s start here since the math is simpler.

 Example setup mining ore (with quality modules),
 and “washing” it until rare or above.
 

Let’s consider one item injected into the system, in this case from mining,
and callfreshunitfresh_{unit}the 5-component row vector of probabilities of each quality tier.

After we transform that vector, the new probabilities may add up to less than one.
The implicit remaining case is not having an item at all at a given place.
For example, the recycler producing nothing 75% of the time can be represented
by multiplying a vector of probabilities by14\frac{1}{4}.

Filtering based on quality can also be represented with matrix multiplication.
In the case of extracting rare or above:

TfilterKeep=(1000001000000000000000000)TfilterExtract=(0000000000001000001000001)=I5−TfilterKeep\begin{align*}
T_{filterKeep} &=
\begin{pmatrix*}
 1 & 0 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0
\end{pmatrix*} \\
T_{filterExtract} &=
\begin{pmatrix*}
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 1 & 0 & 0 \\
 0 & 0 & 0 & 1 & 0 \\
 0 & 0 & 0 & 0 & 1
\end{pmatrix*} = I_5 - T_{filterKeep}
\end{align*}

The combined effect of one iteration through the loop
is filtering to keep, then recycling with quality:

L=TfilterKeep·14·Tquality(q)\begin{align*}
L &= T_{filterKeep} · \frac{1}{4} · T_{quality}(q)
\end{align*}

Now let’s consider the possible ways an item can be extracted:

* It originally had high enough quality to be extracted immediately: probability vectorfreshunit·TfilterExtract=freshunit·L0·TfilterExtractfresh_{unit} · T_{filterExtract} = fresh_{unit} · L^0 · T_{filterExtract}
* It went through the recycling loop exactly once:freshunit·TfilterKeep·L·TfilterExtract=freshunit·L1·TfilterExtractfresh_{unit} · T_{filterKeep} · L · T_{filterExtract} = fresh_{unit} · L^1 · T_{filterExtract}
* It went through recycling exactly twice:freshunit·TfilterKeep·L·L·TfilterExtract=freshunit·L2·TfilterExtractfresh_{unit} · T_{filterKeep} · L · L · T_{filterExtract} = fresh_{unit} · L^2 · T_{filterExtract}
* etc.

Any given item will eventually be extracted or destroyed,
but there is no upper bound on how many loops that can take.
The combination of all possible outcomes is an infinite sum:

extractedunit=freshunit·(∑i=0+∞Li)·TfilterExtractextracted_{unit} = fresh_{unit} · \bigg(\sum_{i=0}^{+∞} L^i\bigg) · T_{filterExtract}

Infinite sums are rather inconvenient to calculate in finite time,
although this one does converge to a finite value since the terms become exponentially smaller.
We could compute until the terms because small enough for an approximation,
but that would be unsatisfactory when an exact solutionispossible.

##### Long-term average throughput

The key insight is that
it doesn’t matter how many times a given item has already been through the loop,
only what quality tier it has now.
On a short time scale this will vary because of the random effect of quality modules
but with enough repetitonsprobabilities become ratios.

So instead of probablities for a single item
let’s consider theaverage rate of items over a long enough period of timegoing through a given part of the system,
again as a 5-component vector for quality tiers.
These vectors can be multiplied by the same transition matrices as before.
In the case of a “washing” pure recycling loop, the relevant vectors are:

* freshfreshitems injected into the system, with any quality distribution,
in this example based on quality modules in miners
* ItemsfromRecyclingfromRecycling
* All items going through thesplittersplitter
* Itemsextractedextractedbased on their quality tier, in this example rare or above
* ItemstoRecycletoRecyclewith qualityqq, those not extracted

We treatqqandfreshfreshas a fixed parameters and other vectors as unknowns we want to resolve.

The system converges to a dynamic equilibrium
where the following equations hold for long-term averages:

splitter=fresh+fromRecyclingsplitter=extracted+toRecycleextracted=splitter⋅TfilterExtracttoRecycle=splitter⋅TfilterKeepfromRecycling=toRecycle⋅14Tquality(q)\begin{align*}
splitter &= fresh + fromRecycling \\
splitter &= extracted + toRecycle \\
extracted &= splitter ⋅ T_{filterExtract} \\
toRecycle &= splitter ⋅ T_{filterKeep} \\
fromRecycling &= toRecycle ⋅ \frac{1}{4} T_{quality}(q)
\end{align*}

We can rearrange and substitute:

splitter=fresh+fromRecyclingsplitter−fromRecycling=freshsplitter−toRecycle⋅14Tquality(q)=freshsplitter−splitter⋅TfilterKeep⋅14Tquality(q)=freshsplitter⋅(I5−TfilterKeep⋅14Tquality(q))=fresh\begin{align*}
splitter = fresh + fromRecycling \\
splitter - fromRecycling = fresh \\
splitter - toRecycle ⋅ \frac{1}{4} T_{quality}(q) = fresh \\
splitter - splitter ⋅ T_{filterKeep} ⋅ \frac{1}{4} T_{quality}(q) = fresh \\
splitter ⋅ (I_5 - T_{filterKeep} ⋅ \frac{1}{4} T_{quality}(q)) = fresh \\
\end{align*}

Transpose to get column vectors instead of row vectors and match theclassic convention:

(splitter⋅(I5−TfilterKeep⋅14Tquality(q)))T=freshT(I5−TfilterKeep⋅14Tquality(q))T⋅splitterT=freshT\begin{align*}
(splitter ⋅ (I_5 - T_{filterKeep} ⋅ \frac{1}{4} T_{quality}(q)))^T &= fresh^T \\
(I_5 - T_{filterKeep} ⋅ \frac{1}{4} T_{quality}(q))^T ⋅ splitter^T &= fresh^T
\end{align*}

Introduce some new names:

A=(I5−TfilterKeep⋅14Tquality(q))Tx=splitterTb=freshT\begin{align*}
A &= (I_5 - T_{filterKeep} ⋅ \frac{1}{4} T_{quality}(q))^T \\
x &= splitter^T \\
b &= fresh^T
\end{align*}

Now we have equilibrium as a system of linear equations in the classicA·x=bA·x = bform,
that we can solve forxxusingGaussian elimination.
Fromxxwe can easily computesplittersplitter,
thentoRecycletoRecycle(for the number of recyclers needed)
andextractedextracted(for the overall yield of the system).

If the example setup above was scaled to mine 100 ore per second, the parameters would be:

fresh=(9090.90.090.01)TfilterExtract=filter(≥rare)q=10%\begin{align*}
fresh &= \begin{pmatrix*} 90 & 9 & 0.9 & 0.09 & 0.01 \end{pmatrix*} \\
T_{filterExtract} &= filter(≥ rare) \\
q &= 10\%
\end{align*}

And the solution with Gaussian Elimination:

toRecycle≈(116.129114.9844000)extracted≈(001.49850.14990.0167)\begin{align*}
toRecycle &≈ \begin{pmatrix*} 116.1291 & 14.9844 & 0 & 0 & 0 \end{pmatrix*} \\
extracted &≈ \begin{pmatrix*} 0 & 0 & 1.4985 & 0.1499 & 0.0167 \end{pmatrix*} \\
\end{align*}

Converting from per second, the extracted rates are close to 90 per minute rare,
9 per minute epic, and 1 per minute legendary.

For another example:

* Injecting only normal-quality fresh items, for now in some arbitrary unit:fresh=(10000)fresh = \begin{pmatrix*} 1 & 0 & 0 & 0 & 0 \end{pmatrix*}
* Recycling with the best available quality modules:q=24.8%q = 24.8\%
* Extracting only legendary-quality items

Solving the equation gives:

toRecycle≈(1.2315280.084630.0142790.002410)extracted≈(00000.000366716)\begin{align*}
toRecycle &≈ \begin{pmatrix*} 1.231528 & 0.08463 & 0.014279 & 0.00241 & 0 \end{pmatrix*} \\
extracted &≈ \begin{pmatrix*} 0 & 0 & 0 & 0 & 0.000366716 \end{pmatrix*} \\
\end{align*}

So for items that recycle to themselves, “brute-force” washing consumes on average1extracted⚄≈2726.91\frac{1}{extracted_⚄} ≈ 2726.91normal-quality inputs for every legendary output.
This matches the ratio thatothershave calculated.
The recycling capacity required is just shy of43\frac{4}{3}of the fresh input rate.

#### “Upcycling”: crafting + recycling loop

For items where recyclingdoesreturn ingredients,
we can chain crafting machines with recyclers to form a loop:

 Example setup upcycling construction robots until lengendary.
 

Most crafting recipes require multiple ingredients in various quantities,
but here we’ll abstract over this and consider “the set of ingredients for one craft”
as the base unit for our measurements.
In this example, each machine crafting construction robots can consume
4 electronic circuits per second and 2 flying robot frames per second,
but we’ll call that “2 ingredients per second”.

So we’re measuring long-term avarage rates of ingredients and products, each in five quality tiers,
but they only appear in separate parts of the system so we’ll stick with 5-components vectors
and don’t need to move to 10-dimensional math.
(Wink wink foreshadowing)

The example setup has fresh normal-quality ingredients brought by robots into the blue requester chest,
and extracts legendary products.
In the general case, we could imagine ingredients or products of any quality distribution
being produced elsewhere and injected into the system.
Similarly, we could decide to extract productsor ingredients(or both) of any quality tier.
(Sometimes an ingredient may be more useful than a product to have in high quality,
but upcycling that specific product may have better yield than other methods.)

So the 5-component row vectors we’ll consider are, for ingredients:

* freshIfreshIinjected into the system, with any quality distribution
* IngredientsfromRecyclingfromRecycling
* totalItotalI
* extractedIextractedIbased on their quality tier, in this example none
* IngredientstoCrafttoCraftnew products from

And for products:

* freshPfreshPinjected into the system, with any quality distribution
* ProductsfromCraftingfromCrafting
* totalPtotalP
* extractedPextractedPbased on their quality tier, in this example lengendary
* ProductstoRecycletoRecycle

We treatfreshIfreshIandfreshPfreshPas fixed parameters,
and other vectors as unknown we want to resolve.

Again the transition matrices for filtering based on quality tier
are complementary parts of the identity matrix.
In this example:

TfilterKeepingredients=I5TfilterExtractingredients=05TfilterKeepproducts=(1000001000001000001000000)TfilterExtractproducts=(0000000000000000000000001)=I5−TfilterKeepproducts\begin{align*}
T^{ingredients}_{filterKeep} &= I_5 \\
T^{ingredients}_{filterExtract} &= 0_5 \\
T^{products}_{filterKeep} &=
\begin{pmatrix*}
 1 & 0 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 & 0 \\
 0 & 0 & 1 & 0 & 0 \\
 0 & 0 & 0 & 1 & 0 \\
 0 & 0 & 0 & 0 & 0
\end{pmatrix*} \\
T^{products}_{filterExtract} &=
\begin{pmatrix*}
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 1
\end{pmatrix*} = I_5 - T^{products}_{filterKeep}
\end{align*}

We account for a craftingproductivityBonusproductivityBonuswhich is 0% in this example
but could be greater with some crafting machines or with productivity modules.
The quality chance may also be different for crafting v.s. recycling
(for example when crafting with productivity modules,
or based on the machine’s number of modules slots).

For short(er), let’s call:

Tcraft=(1+productivityBonus)⋅Tquality(qcrafting)Trecycle=14Tquality(qrecycling)\begin{align*}
T_{craft} &= (1 + productivityBonus) ⋅ T_{quality}(q_{crafting}) \\
T_{recycle} &= \frac{1}{4} T_{quality}(q_{recycling})
\end{align*}

The system converges to equilibrium where:

totalI=freshI+fromRecyclingtotalI=extractedI+toCraftextractedI=totalI⋅TfilterExtractingredientstoCraft=totalI⋅TfilterKeepingredientsfromCrafting=toCraft⋅TcrafttotalP=freshP+fromCraftingtotalP=extractedP+toRecycleextractedP=totalP⋅TfilterExtractproductstoRecycle=totalP⋅TfilterKeepproductsfromRecycling=toRecycle⋅Trecycle\begin{align*}
totalI &= freshI + fromRecycling \\
totalI &= extractedI + toCraft \\
extractedI &= totalI ⋅ T^{ingredients}_{filterExtract} \\
toCraft &= totalI ⋅ T^{ingredients}_{filterKeep} \\
fromCrafting &= toCraft ⋅ T_{craft} \\[2em]
totalP &= freshP + fromCrafting \\
totalP &= extractedP + toRecycle \\
extractedP &= totalP ⋅ T^{products}_{filterExtract} \\
toRecycle &= totalP ⋅ T^{products}_{filterKeep} \\
fromRecycling &= toRecycle ⋅ T_{recycle}
\end{align*}

We can rearrange and substitute:

totalP=freshP+fromCraftingtotalP=freshP+toCraft⋅TcrafttotalP=freshP+totalI⋅TfilterKeepingredients⋅TcrafttotalP=freshP+(freshI+fromRecycling)⋅TfilterKeepingredients⋅TcrafttotalP=freshP+(freshI+toRecycle⋅Trecycle)⋅TfilterKeepingredients⋅TcrafttotalP=freshP+(freshI+totalP⋅TfilterKeepproducts⋅Trecycle)⋅TfilterKeepingredients⋅Tcraft\begin{align*}
totalP &= freshP + fromCrafting \\
totalP &= freshP + toCraft ⋅ T_{craft} \\
totalP &= freshP + totalI ⋅ T^{ingredients}_{filterKeep} ⋅ T_{craft} \\
totalP &= freshP + (freshI + fromRecycling) ⋅ T^{ingredients}_{filterKeep} ⋅ T_{craft} \\
totalP &= freshP + (freshI + toRecycle ⋅ T_{recycle}) ⋅ T^{ingredients}_{filterKeep} ⋅ T_{craft} \\
totalP &= freshP + (freshI + totalP ⋅ T^{products}_{filterKeep} ⋅ T_{recycle}) ⋅ T^{ingredients}_{filterKeep} ⋅ T_{craft}
\end{align*}

Let’s introduce a couple more names:

TfilterRecycle=TfilterKeepproducts⋅TrecycleTfilterCraft=TfilterKeepingredients⋅TcrafttotalP=freshP+(freshI+totalP⋅TfilterRecycle)⋅TfilterCrafttotalP−totalP⋅TfilterRecycle⋅TfilterCraft=freshP+freshI⋅TfilterCrafttotalP⋅(I5−TfilterRecycle⋅TfilterCraft)=freshP+freshI⋅TfilterCraft(I5−TfilterRecycle⋅TfilterCraft)T⋅totalPT=(freshP+freshI⋅TfilterCraft)T\begin{align*}
\begin{align*}
T_{filterRecycle} &= T^{products}_{filterKeep} ⋅ T_{recycle} \\
T_{filterCraft} &= T^{ingredients}_{filterKeep} ⋅ T_{craft} \\[1em]
totalP &= freshP + (freshI + totalP ⋅ T_{filterRecycle}) ⋅ T_{filterCraft} \\
\end{align*}\\
\begin{align*}
totalP - totalP ⋅ T_{filterRecycle} ⋅ T_{filterCraft} &= freshP + freshI ⋅ T_{filterCraft} \\
totalP ⋅ (I_5 - T_{filterRecycle} ⋅ T_{filterCraft}) &= freshP + freshI ⋅ T_{filterCraft} \\
(I_5 - T_{filterRecycle} ⋅ T_{filterCraft})^T ⋅ totalP^T &= (freshP + freshI ⋅ T_{filterCraft})^T
\end{align*}
\end{align*}

We’ve again massaged our problem into the standardA·x=bA·x = bform with:

A=(I5−TfilterRecycle⋅TfilterCraft)Tx=totalPTb=(freshP+freshI⋅TfilterCraft)T\begin{align*}
A &= (I_5 - T_{filterRecycle} ⋅ T_{filterCraft})^T \\
x &= totalP^T \\
b &= (freshP + freshI ⋅ T_{filterCraft})^T
\end{align*}

Solving forxxgives ustotalPtotalP,
and plugging that into the original equilibrium equations gives everything else.

In the example setup above, scaled for now to an arbitrary unit, the parameters are:

freshIunit=(10000)freshP=(00000)TfilterExtractingredients=filter(nothing)TfilterExtractproducts=filter(legendary)productivityBonus=0%qcrafting=24.8%qrecycling=24.8%\begin{align*}
freshI_{unit} &= \begin{pmatrix*} 1 & 0 & 0 & 0 & 0 \end{pmatrix*} \\
freshP &= \begin{pmatrix*} 0 & 0 & 0 & 0 & 0 \end{pmatrix*} \\
T^{ingredients}_{filterExtract} &= filter(nothing) \\
T^{products}_{filterExtract} &= filter(legendary) \\
productivityBonus &= 0\% \\
q_{crafting} &= 24.8\% \\
q_{recycling} &= 24.8\%
\end{align*}

And the solution with Gaussian Elimination:

toCraftunit≈(1.1646550.1138360.0394040.0111330.002154)toRecycleunit≈(0.875820.3455550.0810350.0223070)extractedIunit=(00000)extractedPunit≈(00000.006464)\begin{align*}
toCraft_{unit} &≈ \begin{pmatrix*} 1.164655 & 0.113836 & 0.039404 & 0.011133 & 0.002154 \end{pmatrix*} \\
toRecycle_{unit} &≈ \begin{pmatrix*} 0.87582 & 0.345555 & 0.081035 & 0.022307 & 0 \end{pmatrix*} \\
extractedI_{unit} &= \begin{pmatrix*} 0 & 0 & 0 & 0 & 0 \end{pmatrix*} \\
extractedP_{unit} &≈ \begin{pmatrix*} 0 & 0 & 0 & 0 & 0.006464 \end{pmatrix*}
\end{align*}

In practice, the bottleneck of this system is the crafting speed of normal-quality products:
360 per minute.
So let’s multiply everything by360toCraftunit⚀\frac{360}{toCraft_{unit_⚀}}

freshIscaled≈(309.100000)toCraftscaled≈(36035.1812.173.440.66)toRecyclescaled≈(270.72106.8125.046.890)extractedPscaled≈(00001.99)\begin{align*}
freshI_{scaled} &≈ \begin{pmatrix*} 309.10 & 0 & 0 & 0 & 0 \end{pmatrix*} \\
toCraft_{scaled} &≈ \begin{pmatrix*} 360 & 35.18 & 12.17 & 3.44 & 0.66 \end{pmatrix*} \\
toRecycle_{scaled} &≈ \begin{pmatrix*} 270.72 & 106.81 & 25.04 & 6.89 & 0 \end{pmatrix*} \\
extractedP_{scaled} &≈ \begin{pmatrix*} 0 & 0 & 0 & 0 & 1.99 \end{pmatrix*}
\end{align*}

In conclusion, this system produces on average almost 2 legendary construction robots per minute,
and consumes about 309 sets of ingredients (309 frames + 618 circuits) per minute.

For a select few items in Space Age,
the productivity bonus can be increased through repeatable research.
The game enforces a hard cap of +300% bonus so that crafting then recycling
returns at most the ingredients that we started with, never more.

Productivity research levels get exponentially expensive
so let’s assume that we use also productivity modules to reach the cap,
meaning we don’t have quality modules in crafting machines.
And this time, let’s inject fresh products instead of ingredients.

freshI=(00000)freshPunit=(10000)TfilterExtractingredients=filter(nothing)TfilterExtractproducts=filter(legendary)productivityBonus=+300%qcrafting=0%qrecycling=24.8%\begin{align*}
freshI &= \begin{pmatrix*} 0 & 0 & 0 & 0 & 0 \end{pmatrix*} \\
freshP_{unit} &= \begin{pmatrix*} 1 & 0 & 0 & 0 & 0 \end{pmatrix*} \\
T^{ingredients}_{filterExtract} &= filter(nothing) \\
T^{products}_{filterExtract} &= filter(legendary) \\
productivityBonus &= +300\% \\
q_{crafting} &= 0\% \\
q_{recycling} &= 24.8\%
\end{align*}

Our model predicts:

toCraftunit≈(0.7580.9070.9070.9070.25)toRecycleunit≈(4.0323.6293.6293.6290)extractedIunit=(00000)extractedPunit=(00001)\begin{align*}
toCraft_{unit} &≈ \begin{pmatrix*} 0.758 & 0.907 & 0.907 & 0.907 & 0.25 \end{pmatrix*} \\
toRecycle_{unit} &≈ \begin{pmatrix*} 4.032 & 3.629 & 3.629 & 3.629 & 0 \end{pmatrix*} \\
extractedI_{unit} &= \begin{pmatrix*} 0 & 0 & 0 & 0 & 0 \end{pmatrix*} \\
extractedP_{unit} &= \begin{pmatrix*} 0 & 0 & 0 & 0 & 1 \end{pmatrix*}
\end{align*}

Perhaps surprisingly, the rates for intermediate quality tiers are identical.

A maximal productivity bonus enables
turning a normal quality product into a legendary one without any ressource loss,
at the cost of many machines and modules to get significant throughput.

#### “Space casino”: asteroid reprocessing loop

In Space Age, each space platform is a mini-factory.
Instead of mining ore from the ground they collect asteroid chunks and crush them to get resources.
Those can be used for a space ship’s own fuel and ammunition,
or to feed a production chain in space whose end-product is sent to a planet’s ground.

Three different types of chunks (metallic, carbonic, and oxide) yield different ressources
and are more or less frequent in different regions of the solar system.
Asteroid chunks can be “reprocessed” for a chance to get a different type (or nothing).

 Asteroid reprocessing recipes.
 Source: 
Factorio wiki

Assuming enough crushers with each recipe,
we can represent this process mathematically
as multiplying a row vector by a square 3×3 transition matrix:

fromReprocessing=toReprocess⋅TreprocessingTreprocesing=(40%20%20%20%40%20%20%20%40%)\begin{align*}
fromReprocessing &= toReprocess ⋅ T_{reprocessing} \\[1em]
T_{reprocesing} &=
\begin{pmatrix*}
 40\% & 20\% & 20\% \\
 20\% & 40\% & 20\% \\
 20\% & 20\% & 40\%
\end{pmatrix*}
\end{align*}

Reprocessing also accepts quality modules so it can be used in a loop much like “washing”.
Crushing legendary chunks yields legendary versions of some base resources
that can be used for crafting other legendary items.

This time we’ll have conveyor belts transporting asteroid chunks of any of three types,
each in any of five quality tiers, for a total of 15 possible items.
We’ll represent this with 15-component row vectors and 15×15 transition matrices.
We build up the latter asblock matricesmade of nine 5×5 blocks:

Treprocessing15=(40%⋅I520%⋅I520%⋅I520%⋅I540%⋅I520%⋅I520%⋅I520%⋅I540%⋅I5)Tquality15(q)=(Tquality(q)000Tquality(q)000Tquality(q))TfilterKeep15=(TfilterKeepMetallic000TfilterKeepCarbonic000TfilterKeepOxide)total=fresh+fromReprocessingfromReprocessing=toReprocess⋅Treprocessing15⋅Tquality15(q)toReprocess=total⋅TfilterKeep15extracted=total⋅TfilterExtract15=total⋅(I15−TfilterKeep15)\begin{align*}
T^{15}_{reprocessing} &=
\begin{pmatrix*}
 40\% ⋅ I_5 & 20\% ⋅ I_5 & 20\% ⋅ I_5 \\
 20\% ⋅ I_5 & 40\% ⋅ I_5 & 20\% ⋅ I_5 \\
 20\% ⋅ I_5 & 20\% ⋅ I_5 & 40\% ⋅ I_5
\end{pmatrix*} \\[2em]
T^{15}_{quality}(q) &=
\begin{pmatrix*}
 T_{quality}(q) & 0 & 0 \\
 0 & T_{quality}(q) & 0 \\
 0 & 0 & T_{quality}(q)
\end{pmatrix*} \\[2em]
T^{15}_{filterKeep} &=
\begin{pmatrix*}
 T_{filterKeepMetallic} & 0 & 0 \\
 0 & T_{filterKeepCarbonic} & 0 \\
 0 & 0 & T_{filterKeepOxide}
\end{pmatrix*} \\[2em]
total &= fresh + fromReprocessing \\
fromReprocessing &= toReprocess ⋅ T^{15}_{reprocessing} ⋅ T^{15}_{quality}(q) \\
toReprocess &= total ⋅ T^{15}_{filterKeep} \\
extracted &= total ⋅ T^{15}_{filterExtract} = total ⋅ (I_{15} - T^{15}_{filterKeep})
\end{align*}

Aside from the higher dimension,
the math is the same as for washing
and we end up with a system of linear equationsA·x=bA·x = bto solve forxx, with:

A=(I15−TfilterKeep15⋅Treprocessing15⋅Tquality15(q))Tx=totalTb=freshT\begin{align*}
A &= (I_{15} - T^{15}_{filterKeep} ⋅ T^{15}_{reprocessing} ⋅ T^{15}_{quality}(q))^T \\
x &= total^T \\
b &= fresh^T \\
\end{align*}

Asteroid crushers have two module slots,
so the best possible quality chance for reprocessing isq=12.4%q = 12.4\%.
Asteroid collectors don’t have any module slot,
so freshly-collected chunks are always normal-quality.
We build the 15-componentfreshfreshvector from its 3 components for normal-quality rate
of each asteroid type (metallic, carbonic, oxide).
For example in Nauvis orbit:fresh⚀=(362616)fresh_⚀ = \begin{pmatrix*} \frac{3}{6} & \frac{2}{6} & \frac{1}{6} \end{pmatrix*}

Let’s say that we only extract legendary oxide chunks and reprocess everything else.
Solving the equation gives two complementary 15-components row vectorstoReprocesstoReprocessandextractedextractedthat we can rearrange into 3×5 tables

Example: in Nauvis orbit, extract legendary oxide chunks and reprocess everything else:

fresh⚀=(362616)q=12.4%\begin{align*}
fresh_⚀ &= \begin{pmatrix*} \frac{3}{6} & \frac{2}{6} & \frac{1}{6} \end{pmatrix*} \\
q &= 12.4\%
\end{align*}

To reprocess

⚀
⚁
⚂
⚃
⚄

Metallic

1.31616
0.33791
0.13314
0.05286
0.0175

Carbonic

1.11409
0.33244
0.13245
0.05277
0.01748

Oxide

0.91202
0.32697
0.13175
0.05268
0

Extracted

⚀
⚁
⚂
⚃
⚄

Metallic

0
0
0
0
0

Carbonic

0
0
0
0
0

Oxide

0
0
0
0
0.01398

We observe:

* As the quality tier increases,
the distribution of asteroid types quickly converges to an even13\frac{1}{3}each.
The distribution of normal-quality fresh input has negligible impact
on that of legendary-quality chunks going through the system.
* When extracting a single type of legendary asteroids,
the legendary yield is about171.5≈1.4%\frac{1}{71.5} ≈ 1.4\%of the total fresh input.
This is much better than about12726\frac{1}{2726}for “washing” a.k.a. pure recycling,
thanks to reprocessing destroying its input only 20% of the time
v.s. 75% for recycling.

#### Other strategies

There are other ways to get quality items that don’t neatly fit in the categories above
(honorable mention to“The LDS Shuffle”)
and I’m sure folks will come up with more.
But if a loop makes it tricky to calculate their behavior we can use the same ideas:

* Represent throughput of multiple kinds of items as vectors
* Represent linear transformations (crafting, recycling, …) as matrix multiplication
* Represent dynamic equilibrium as a matrix equation
* Solve the equation, using Gaussian Elimination if needed

### Making an interactive calculator tool

Doing matrix math by hand is obviously tedious and error-prone, let’s have computers do it for us.

I started with Rust out of habit.nalgebraworks out great for the matrix math we do here.
In includes multiple solvers forA·x=bA·x = bsystems of linear equations,
but those pretty much require the scalar type for matrix and vector components
to be a floating point numberf32orf64, whereas the base library is more generic.

In practice floating point would be perfectly adequate,
but it is a fixed-precision approximation
so every step of computation potentially introduces some error.
Wouldn’t it be nice to get an exact result, just because we can?
The matrix sizes and number of operations are fixed and relatively small,
so we don’t need to optimize the code for speed.

Every operation we use is ultimately addition, substraction, multiplication, or division.
So if all of our parameters arerationalthe result will be too.num_rationalrepresents rationals extactly
as a pair of (generic) integers.
I could reach for some infinite-precisionBigIntlibrary if needed,
but the built-ini128withoverflow checksturns out to be sufficient for 15×15 martices.
(i64is sufficient for 5×5.)

At this point I had a functional Rust library doing all of the math above,
but editing source code to tweak parameters isn’t a nice user experience.
I’d much prefer something likeFactoriolab.
And to be easy to use by other people it really should be on the web.

My Rust code can be compiled to WebAssembly but then I would need to either:

* Build the entire GUI with Rust + wasm as well.
It’s possible but the toolingisn’t great yet
* Build the GUI in JavaScript or TypeScript (taking advantage of mature tools)
and bridge into wasm for the math.
But because of the many parameters the API surface is significant,
and doing that much bridging isn’t fun

So I ended up rewriting the whole thing in TypeScript.BigIntis built-in,
Factoriolab already has a good open-sourcerationallibrary,
and making a generic matrix library isn’t too hard.

As to building an interactive GUI in the browser,
last time I did much of it jQuery was the hot new thing.
I didn’t feel like learning React so I settled on:

* VanJSfor minimal reactive goodness
* Vitefor TypeScript wrangling and a reload-on-save dev server
* Grebedocfor static file hosting

All together,factoqual.grebedoc.devnow provides
an interactive GUI for planning Quality upcyclers.
Its source code is published atcodeberg.org/SimonSapin/factoqual.

### Acknowledgments

I was heavily inspired by Daniel Monteiro’sblog postson quality math.
Others have done similar work,
includingKonageandFactorio wiki contributors.
But I believe the exact solution from solving equilibrium equation as shown here is new,
as opposed to iterative approximation an infinite sum.