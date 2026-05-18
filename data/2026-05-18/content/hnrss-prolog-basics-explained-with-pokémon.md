---
title: Prolog Basics Explained with Pokémon
url: https://unplannedobsolescence.com/blog/prolog-basics-pokemon/
site_name: hnrss
content_file: hnrss-prolog-basics-explained-with-pokémon
fetched_at: '2026-05-18T12:11:48.001235'
original_url: https://unplannedobsolescence.com/blog/prolog-basics-pokemon/
date: '2026-05-15'
description: Demonstrating the basics of logic programming with data from the Pokémon games.
tags:
- hackernews
- hnrss
---

Prolog Basics Explained with Pokémon

# Prolog Basics Explained with Pokémon

January 05, 2026

The project that inspired this post is a little silly—I am about to describe the mechanics of a children’s video game in great detail—but this particular problem is what finally made Prolog click for me, an epiphany I’ve been hunting for ever since reading Bruce Tate’s “Seven Languages in Seven Weeks.”

This exercise has taught me a lot about the kinds of interfaces I’m trying to build insomewhat more practical domains.
For certain kinds of relationships, logic programming is by far the most concise and expressive programming system I’ve ever used.

To understand why, let’s talk about Pokémon.

## Pokémon basics

Pokémon is a video game series/multimedia franchise/lifestyle brand set in a world where humans live alongside a menagerie of colorful animal characters.

“Pokémon” is both the name of the franchise and the generic term for the animal characters themselves, which all have their own individual species names.
There are over a thousand distinct species of Pokémon, from Bulbasaur (#1) to Pecharunt (#1025).

 Popular Pokémon include (from left to right):

 Pikachu 
(#25)
, Archeops
 
(#567)

 , and Dipplin 
(#1101)
.
 

There are all sorts of Pokémon games now, but the main series has always been about catching and battling them.
During a battle, your team of six Pokémon faces off against another team.
Each Pokémon is equipped with four moves that it can choose to (usually) do damage to their opponent.
You need to reduce the HP (Hit Points) of all your opponent’s Pokémon to zero before they are able to do so to you.

Each Pokémon has unique traits that affects how it battles.
They have a set of base stats, a large pool of possible moves, a handful of abilities, and a typing.
As you will see in a moment, the immense number of combinations here is the motivation for trying to track this with software.

Scizor is a Bug/Steel type with high Attack and low Speed (via 
Smogon
)

Typing is especially important.
Moves have a type, like Fire or Rock, and Pokémon can have up to two types.
A move with a type that is Super Effective against the opposing Pokémon will do double damage; a move that is Not Very Effective will do half damage.

It’s a little more intuitive with examples.
The Fire-type moveFlamethrowerwill do 2x to Grass-type Pokémon, because Grass is weak to Fire, but the Water-type moveSurfwill only do ½ damage to them, because Grass resists Water.

Lunatone
 is a Rock/Psychic Type. Rock is weak to Water, and Psychic is neutral to it, so 
Surf
 will do 2x damage.
 

Type modifiers can stack.Scizoris a Bug/Steel type, andbothBug and Steel are weak to Fire, so Fire moves will do 4x damage to Scizor.
Electric is weak to Water, but Ground is immune, so if you use an Electric type move against Water/GroundSwampert, you’ll do zero damage, since 0×2 is still 0.

Naturally, there is a chart to help you keep track.

 Pokémon Type Chart (via 
Wikimedia
)

Those are effectively the mechanics of the Pokémon video games as I understood them when I was 8.
Click moves to do damage, try to click moves with good type matchups.
These games are for children and, at the surface level, they’re not very hard.

## Prolog basics

Before I explain how wonky the Pokémon mechanics can get under the hood, I first need to explain how logic programming works.
Pokémon is a great fit for logic programming because Pokémon battles are essentially an extremely intricate rules engine.

Let’s start by creating a file with a bunch of facts.

pokemon
(bulbasaur)
.

pokemon
(ivysaur)
.

pokemon
(venusaur)
.

pokemon
(charmander)
.

pokemon
(charmeleon)
.

pokemon
(charizard)
.

pokemon
(squirtle)
.

pokemon
(wartortle)
.

pokemon
(blastoise)
.

In Prolog, we declare “predicates.”
Predicates define relationships:bulbasauris apokemon,charmanderis apokemon, and so on.
We refer to this predicate aspokemon/1, because the name of the predicate ispokemonand it has one argument.

These facts are loaded into an interactive prompt called the “top-level.”
You query the top-level by typing a statement into the prompt;
Prolog tries to find all the ways to make that statement true.
When there’s more than one possible solution, the top-level displays the first solution and then awaits user input.
You can then have it display one more solution, all the solutions, or stop entirely.

In this first example, we typepokemon(squirtle).and hit Enter.
The top-level repliestrue.Squirtleis, in fact, a Pokémon.

?- pokemon(squirtle).

 true.

Not all things are Pokémon.

?- pokemon(alex).

 false.

Let’s add Pokémon types in there, as the predicatetype/2.

type
(bulbasaur, grass)
.

type
(bulbasaur, poison)
.

type
(ivysaur, grass)
.

type
(ivysaur, poison)
.

type
(venusaur, grass)
.

type
(venusaur, poison)
.

type
(charmander, fire)
.

type
(charmeleon, fire)
.

type
(charizard, fire)
.

type
(charizard, flying)
.

type
(squirtle, water)
.

type
(wartortle, water)
.

type
(blastoise, water)
.

Recall that some Pokémon have just one type while others have two.
In the latter case, that’s modeled with twotypefacts.Bulbasauris a Grass type, and Bulbasaur is a Poison type; both are true.
The paradigm is similar to a One-To-Many relation in a SQL database.

Interactively, we can confirm whether Squirtle is a water type.

?- type(squirtle, water).

 true.

Can we state that Squirtle is a Grass type?

?- type(squirtle, grass).

 false.

No, because Squirtle is a Water type.

Suppose we didn’t know what type Squirtle was.
We can ask!

?- type(squirtle, Type).

 Type = water.

In Prolog, names that start with an upper-case letter are variables.
Prolog tries to “unify” the predicate with all possible matches for the variable.
There’s only one way to make this particular predicate true though:Typehas to bewater, because Squirtle’s only type is Water.

For Pokémon with two types, the predicate unifies twice.

?- type(venusaur, Type).

 Type = grass

; Type = poison.

Semantically, that leading semicolon on the third line means “or.”type(venusaur, Type)is true whenType = grassor whenType = poison.

Any of the terms can be be a variable, which means we can ask questions in any direction.
What are all the Grass types?
Just make the first argument the variable, and set the second argument tograss.

?- type(Pokemon, grass).

 Pokemon = bulbasaur

; Pokemon = ivysaur

; Pokemon = venusaur

; Pokemon = oddish

; Pokemon = gloom

; Pokemon = vileplume

; Pokemon = paras

; Pokemon = parasect

; Pokemon = bellsprout

; ... .

I cut it off, but the prompt would happily would list all 164 of them.

Commas can be used to list multiple predicates—Prolog will unify the variables such that all of them are true.
Listing all the Water/Ice types is just a matter of asking what Pokémon exist that unify with both the Water and Ice types.

?- type(Pokemon, water), type(Pokemon, ice).

 Pokemon = dewgong

; Pokemon = cloyster

; Pokemon = lapras

; Pokemon = laprasgmax

; Pokemon = spheal

; Pokemon = sealeo

; Pokemon = walrein

; Pokemon = arctovish

; Pokemon = ironbundle

; false.

Even thoughPokemonis a variable, in the context of the query, both instances of it have to be the same (just like in algebra).
The query only unifies for values ofPokemonwhere both those predicates hold.
For instance, the Water/Ice typeDewgongis a solution because our program contains the following two facts:

type
(dewgong, water)
.

type
(dewgong, ice)
.

Therefore, subbing indewgongfor thePokemonvariable satisfies the query.
Squirtle, by contrast, is just a Water type:pokemon(squirtle, water)exists, but notpokemon(squirtle, ice).
The query requires both to unify, sosquirtleis not a possible value forPokemon.

Pokémon have lots of data that you can play around with.Iron Bundleis a strong Water/Ice-type Pokémon with high Special Attack.
How high exactly?

?- pokemon_spa(ironbundle, SpA).

 SpA = 124.

With Special Attack that high, we want to make use of strong Special moves.
What Special moves does Iron Bundle know?

?- learns(ironbundle, Move), move_category(Move, special).

 Move = aircutter

; Move = blizzard

; Move = chillingwater

; Move = freezedry

; Move = hydropump

; Move = hyperbeam

; Move = icebeam

; Move = icywind

; Move = powdersnow

; Move = swift

; Move = terablast

; Move = waterpulse

; Move = whirlpool.

Freeze-Dryis a particularly good Special move.
Here’s a query for all Ice-type Pokémon with Special Attack greater than 120 that learnFreeze-Dry.

?- pokemon_spa(Pokemon, SpA), SpA #> 120, learns(Pokemon, freezedry), type(Pokemon, ice).

 Pokemon = glaceon, SpA = 130

; Pokemon = kyurem, SpA = 130

; Pokemon = kyuremwhite, SpA = 170

; Pokemon = ironbundle, SpA = 124

; false.

One last concept before we move on: Rules.
Rules have a head and a body, and they unify if the body is true.

A move is considered a damaging move if it’s either a Physical Move or a Special Move.
Thedamaging_move/2predicate defines all the moves that do direct damage.

damaging_move
(
Move
)
 :-

 move_category(
Move
, physical)

; move_category(
Move
, special)
.

This will unify with any moves that do direct damage.

?- damaging_move(tackle).

 true.

?- damaging_move(rest).

 false.

## SQL comparison

Nothing I’ve shown so far is, logically speaking, very ambitious—just “and” and “or” statements about various facts.
It’s essentially a glorified lookup table.
Still, take a moment to appreciate how much nicer it is to query this database than a plausible alternative, like SQL.

For the facts we’ve seen so far, I would probably set up SQL tables like this:

-- Omitting the other stats to be concise

CREATE TABLE
 pokemon
 (pokemon_name 
TEXT
, special_attack 
INTEGER
);

CREATE TABLE
 pokemon_types
(pokemon_name 
TEXT
, 
type TEXT
);

CREATE TABLE
 pokemon_moves
(pokemon_name 
TEXT
, 
move TEXT
, category 
TEXT
);

Then query it like so:

SELECT DISTINCT
 pokemon, special_attack

FROM
 pokemon 
as
 p

WHERE

 p.special_attack >
 120

 AND EXISTS
 (

 SELECT
 1

 FROM
 pokemon_moves 
as
 pm

 WHERE
 p.pokemon_name = pm.pokemon_name
 AND move
 = '
freezedry
'

 )

 AND EXISTS
 (

 SELECT
 1

 FROM
 pokemon_types 
as
 pt

 WHERE
 p.pokemon_name = pt.pokemon_name
 AND type
 = '
ice
'

 );

For comparison, here’s the equivalent Prolog query again:

?- pokemon_spa(Pokemon, SpA),

SpA #> 120,

learns(Pokemon, freezedry),

type(Pokemon, ice).

I’m not ripping on SQL—I love SQL—but that’s the best declarative query language most people interact with.
It’s amazing to me how much simpler and more flexible the Prolog version is.
The SQL query would become unmanageably complex if we continued to add clauses, while the Prolog query remains easy to read and edit (once you get the hang of how variables work).

## Level up

With the basics established, here’s some context on the project I’m working on.

Pokémon battles have an outrageous number of mechanics that all interact in complex and probabilistic ways.
Part of the appeal of these games is the futile attempt to keep them all in your head better than your opponent, using that information to out-predict and out-maneuver their plans.
It’s a sort of like very silly Poker.

A small subset of game mechanics I have not yet mentioned

* Some moves miss a certain percentage of the time, doing no damage.Some moves raise or lower a Pokémon's stats.Pokémon can hold items that have various effects.Damage calculations aren't constant; moves do normally-distributed damage within the calculated range.Pokémon can get frozen, burned, paralyzed, poisoned, or fall asleep; these all have various adverse effects.There are a variety of field effects (like weather, terrain, Trick Room) which alter move damage, turn order, and other things.Pokémon each have an ability that has various effects i.e Levitate makes you immune to ground moves, Drizzle turns the weather to Rain when the Pokemon switches in, Sheer Force disables a move's side effects but multiplies its damage by 1.3x.Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.
* Some moves raise or lower a Pokémon's stats.Pokémon can hold items that have various effects.Damage calculations aren't constant; moves do normally-distributed damage within the calculated range.Pokémon can get frozen, burned, paralyzed, poisoned, or fall asleep; these all have various adverse effects.There are a variety of field effects (like weather, terrain, Trick Room) which alter move damage, turn order, and other things.Pokémon each have an ability that has various effects i.e Levitate makes you immune to ground moves, Drizzle turns the weather to Rain when the Pokemon switches in, Sheer Force disables a move's side effects but multiplies its damage by 1.3x.Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.
* Pokémon can hold items that have various effects.Damage calculations aren't constant; moves do normally-distributed damage within the calculated range.Pokémon can get frozen, burned, paralyzed, poisoned, or fall asleep; these all have various adverse effects.There are a variety of field effects (like weather, terrain, Trick Room) which alter move damage, turn order, and other things.Pokémon each have an ability that has various effects i.e Levitate makes you immune to ground moves, Drizzle turns the weather to Rain when the Pokemon switches in, Sheer Force disables a move's side effects but multiplies its damage by 1.3x.Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.
* Damage calculations aren't constant; moves do normally-distributed damage within the calculated range.Pokémon can get frozen, burned, paralyzed, poisoned, or fall asleep; these all have various adverse effects.There are a variety of field effects (like weather, terrain, Trick Room) which alter move damage, turn order, and other things.Pokémon each have an ability that has various effects i.e Levitate makes you immune to ground moves, Drizzle turns the weather to Rain when the Pokemon switches in, Sheer Force disables a move's side effects but multiplies its damage by 1.3x.Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.
* Pokémon can get frozen, burned, paralyzed, poisoned, or fall asleep; these all have various adverse effects.There are a variety of field effects (like weather, terrain, Trick Room) which alter move damage, turn order, and other things.Pokémon each have an ability that has various effects i.e Levitate makes you immune to ground moves, Drizzle turns the weather to Rain when the Pokemon switches in, Sheer Force disables a move's side effects but multiplies its damage by 1.3x.Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.
* There are a variety of field effects (like weather, terrain, Trick Room) which alter move damage, turn order, and other things.Pokémon each have an ability that has various effects i.e Levitate makes you immune to ground moves, Drizzle turns the weather to Rain when the Pokemon switches in, Sheer Force disables a move's side effects but multiplies its damage by 1.3x.Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.
* Pokémon each have an ability that has various effects i.e Levitate makes you immune to ground moves, Drizzle turns the weather to Rain when the Pokemon switches in, Sheer Force disables a move's side effects but multiplies its damage by 1.3x.Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.
* Players have points they (invisibly) allocate to each Pokémon before the game, to boost chosen stats. Depending on they built the team, each Pokemon might do more damage or take hits better than you were expecting.

The challenge, if you want to build software for this game, is to model all that complexity without losing your mind.
Prolog is stunningly good at this, for two main reasons:

1. The query model excels at describing ad-hoc combinations.
2. The data model is perfectly suited to layering rules in a consistent way.

To illustrate that, here’s how I implemented priority moves for my Pokémon draft league.

Pokémon draft is pretty much what it sounds like.
Pokémon are given a point value based on how good they are, each player is given a certain amount of points to spend, and you draft until every player has spent their points.
Your team ends up with about 8-11 Pokémon and each week you go head to head against another person in the league.
My friend andWMIcollaboratorMorryinvited me to his a couple years ago and I’ve been hooked on the format ever since.

The games are 6v6, so a big part of the battle is preparing for all the possible combinations of six your opponent could bring, and putting together six of your own that can handle all of them.

Naturally, you can only build teams with the Pokémon you drafted.
I just made that predicate my name:alex/1.

alex
(meowscarada)
.

alex
(weezinggalar)
.

alex
(swampertmega)
.

alex
(latios)
.

alex
(volcarona)
.

alex
(tornadus)
.

alex
(politoed)
.

alex
(archaludon)
.

alex
(beartic)
.

alex
(dusclops)
.

What Pokémon do I have that learnFreeze-Dry?

?- alex(Pokemon), learns(Pokemon, freezedry).

 false.

None. Rats.

One very important type of move is priority moves.
Earlier I mentioned that the Speed stat controls which Pokémon moves first.
Some nuance: the Pokémon that used the move with the highest priority goes first, and if they both selected a move of the same priority, then the one with the higher Speed goes first.

Most moves have a priority of zero.

?- move_priority(Move, P).

 Move = '10000000voltthunderbolt', P = 0

; Move = absorb, P = 0

; Move = accelerock, P = 1

; Move = acid, P = 0

; Move = acidarmor, P = 0

; Move = aciddownpour, P = 0

; Move = acidspray, P = 0

; Move = acrobatics, P = 0

; Move = acupressure, P = 0

; Move = aerialace, P = 0

; Move = aeroblast, P = 0

Ah, but not all!Accelerockhas a priority of 1.
A Pokémon that usesAccelerockwill move before
any Pokémon that uses a move with priority 0 (or less), even if the latter Pokémon has a higher Speed stat.

I define alearns_priority/3predicate that unifies with a Pokémon, the priority move it learns, and what priority that move is.

learns_priority
(
Pokemon
, 
Move
, 
P
)
 :-

 learns(
Pokemon
,
 Move
),

 move_priority(
Move
,
 P
),

 P
 #>
 0
.

A simple query that asks “what priority moves does my team learn” returns alotof answers.

?- alex(Pokemon), learns_priority(Pokemon, Move, Priority).

 Pokemon = meowscarada, Move = endure, Priority = 4

; Pokemon = meowscarada, Move = helpinghand, Priority = 5

; Pokemon = meowscarada, Move = protect, Priority = 4

; Pokemon = meowscarada, Move = quickattack, Priority = 1

; Pokemon = meowscarada, Move = allyswitch, Priority = 2

; Pokemon = meowscarada, Move = suckerpunch, Priority = 1

; Pokemon = weezinggalar, Move = endure, Priority = 4

; Pokemon = weezinggalar, Move = protect, Priority = 4

; Pokemon = swampertmega, Move = bide, Priority = 1

; Pokemon = swampertmega, Move = endure, Priority = 4

; Pokemon = swampertmega, Move = helpinghand, Priority = 5

; Pokemon = swampertmega, Move = protect, Priority = 4

; Pokemon = swampertmega, Move = wideguard, Priority = 3

; Pokemon = latios, Move = allyswitch, Priority = 2

; Pokemon = latios, Move = endure, Priority = 4

; Pokemon = latios, Move = helpinghand, Priority = 5

; Pokemon = latios, Move = magiccoat, Priority = 4

; Pokemon = latios, Move = protect, Priority = 4

; Pokemon = volcarona, Move = endure, Priority = 4

; Pokemon = volcarona, Move = protect, Priority = 4

; Pokemon = volcarona, Move = ragepowder, Priority = 2

; Pokemon = tornadus, Move = endure, Priority = 4

; Pokemon = tornadus, Move = protect, Priority = 4

; Pokemon = politoed, Move = detect, Priority = 4

; Pokemon = politoed, Move = endure, Priority = 4

; Pokemon = politoed, Move = helpinghand, Priority = 5

; Pokemon = politoed, Move = protect, Priority = 4

; Pokemon = politoed, Move = bide, Priority = 1

; Pokemon = archaludon, Move = endure, Priority = 4

; Pokemon = archaludon, Move = protect, Priority = 4

; Pokemon = beartic, Move = aquajet, Priority = 1

; Pokemon = beartic, Move = bide, Priority = 1

; Pokemon = beartic, Move = endure, Priority = 4

; Pokemon = beartic, Move = protect, Priority = 4

; Pokemon = dusclops, Move = allyswitch, Priority = 2

; Pokemon = dusclops, Move = endure, Priority = 4

; Pokemon = dusclops, Move = helpinghand, Priority = 5

; Pokemon = dusclops, Move = protect, Priority = 4

; Pokemon = dusclops, Move = shadowsneak, Priority = 1

; Pokemon = dusclops, Move = snatch, Priority = 4

; Pokemon = dusclops, Move = suckerpunch, Priority = 1

; false.

Although this is technically correct (the best kind), most of these answers are not actually useful.Helping HandandAlly Switchhave very high priority, but they only have a purpose in Double Battles, which isn’t the format I’m playing.

To fix this, I define all the Double Battle moves and exclude them.
I’m going to exclude the moveBidetoo, which is functionally useless. The\+/1predicate means “true if this goal fails”, anddif/2means “these two terms are different.”

learns_priority(Mon, Move, Priority) :-

 learns(Mon, Move),

 \+ doubles_move(Move),

 dif(Move, bide),

 move_priority(Move, Priority),

 Priority #> 0.

doubles_move(helpinghand).

doubles_move(afteryou).

doubles_move(quash).

doubles_move(allyswitch).

doubles_move(followme).

doubles_move(ragepowder).

doubles_move(aromaticmist).

doubles_move(holdhands).

doubles_move(spotlight).

We get the following results:

?- alex(Pokemon), learns_priority(Pokemon, Move, Priority).

 Pokemon = meowscarada, Move = endure, Priority = 4

; Pokemon = meowscarada, Move = protect, Priority = 4

; Pokemon = meowscarada, Move = quickattack, Priority = 1

; Pokemon = meowscarada, Move = suckerpunch, Priority = 1

; Pokemon = weezinggalar, Move = endure, Priority = 4

; Pokemon = weezinggalar, Move = protect, Priority = 4

; Pokemon = swampertmega, Move = endure, Priority = 4

; Pokemon = swampertmega, Move = protect, Priority = 4

; Pokemon = latios, Move = endure, Priority = 4

; Pokemon = latios, Move = magiccoat, Priority = 4

; Pokemon = latios, Move = protect, Priority = 4

; Pokemon = volcarona, Move = endure, Priority = 4

; Pokemon = volcarona, Move = protect, Priority = 4

; Pokemon = tornadus, Move = endure, Priority = 4

; Pokemon = tornadus, Move = protect, Priority = 4

; Pokemon = politoed, Move = detect, Priority = 4

; Pokemon = politoed, Move = endure, Priority = 4

; Pokemon = politoed, Move = protect, Priority = 4

; Pokemon = archaludon, Move = endure, Priority = 4

; Pokemon = archaludon, Move = protect, Priority = 4

; Pokemon = beartic, Move = aquajet, Priority = 1

; Pokemon = beartic, Move = endure, Priority = 4

; Pokemon = beartic, Move = protect, Priority = 4

; Pokemon = dusclops, Move = endure, Priority = 4

; Pokemon = dusclops, Move = protect, Priority = 4

; Pokemon = dusclops, Move = shadowsneak, Priority = 1

; Pokemon = dusclops, Move = snatch, Priority = 4

; Pokemon = dusclops, Move = suckerpunch, Priority = 1

; false.

Much better, but there’s a handful of moves in there that go first because they
protect the user from damage or status, likeDetect.
That’s not really what I mean by priority move—I’m interested in moves that will surprise my opponent with damage or an adverse side effect, likeQuick AttackandSucker Punch.

learns_priority
(
Mon
, 
Move
, 
Priority
)
 :-

 learns(
Mon
,
 Move
),

 \+ doubles_move(
Move
),

 \+ protection_move(
Move
),

 Move
 \= bide,

 move_priority(
Move
,
 Priority
),

 Priority
 #>
 0
.

protection_move
(detect)
.

protection_move
(protect)
.

protection_move
(kingsshield)
.

protection_move
(burningbulwark)
.

protection_move
(spikyshield)
.

protection_move
(banefulbunker)
.

protection_move
(endure)
.

protection_move
(magiccoat)
.

With those rules in place, we arrive at a very useful answer!

?- alex(Pokemon), learns_priority(Pokemon, Move, Priority).

 Pokemon = meowscarada, Move = quickattack, Priority = 1

; Pokemon = meowscarada, Move = suckerpunch, Priority = 1

; Pokemon = beartic, Move = aquajet, Priority = 1

; Pokemon = dusclops, Move = shadowsneak, Priority = 1

; Pokemon = dusclops, Move = snatch, Priority = 4

; Pokemon = dusclops, Move = suckerpunch, Priority = 1

; false.

It’s even more useful to look up what priority moves myopponentfor the week has.

?- morry(Pokemon), learns_priority(Pokemon, Move, Priority).

 Pokemon = mawilemega, Move = snatch, Priority = 4

; Pokemon = mawilemega, Move = suckerpunch, Priority = 1

; Pokemon = walkingwake, Move = aquajet, Priority = 1

; Pokemon = ursaluna, Move = babydolleyes, Priority = 1

; Pokemon = lokix, Move = feint, Priority = 2

; Pokemon = lokix, Move = firstimpression, Priority = 2

; Pokemon = lokix, Move = suckerpunch, Priority = 1

; Pokemon = alakazam, Move = snatch, Priority = 4

; Pokemon = skarmory, Move = feint, Priority = 2

; Pokemon = froslass, Move = iceshard, Priority = 1

; Pokemon = froslass, Move = snatch, Priority = 4

; Pokemon = froslass, Move = suckerpunch, Priority = 1

; Pokemon = dipplin, Move = suckerpunch, Priority = 1.

At this point, I showed the program to Morry and he hit me with a challenge.
Pokémon with the Prankster ability get an additional +1 priority on their status moves.
Could the rule be extended to note that?

I happen to have one such Pokémon on my team.

?- alex(Pokemon), pokemon_ability(Pokemon, prankster).

 Pokemon = tornadus

; false.

This took me 3 minutes, using Prolog’s if/then construct,->/2.

learns_priority
(
Mon
, 
Move
, 
Priority
)
 :-

 learns(
Mon
,
 Move
),

 \+ doubles_move(
Move
),

 \+ protection_move(
Move
),

 Move
 \= bide,

 move_priority(
Move
,
 BasePriority
),

 (

 pokemon_ability(
Mon
, prankster), move_category(
Move
, status)
 ->

 Priority
 #= 
BasePriority
 + 
1

 ; 
Priority
 #= 
BasePriority

 ),

 Priority
 #> 
0
.

Now the same query includes all of Tornadus’ status moves, with their increased priority.

?- alex(Pokemon), learns_priority(Pokemon, Move, P).

 Pokemon = meowscarada, Move = quickattack, P = 1

; Pokemon = meowscarada, Move = suckerpunch, P = 1

; Pokemon = tornadus, Move = agility, P = 1

; Pokemon = tornadus, Move = attract, P = 1

; Pokemon = tornadus, Move = bulkup, P = 1

; Pokemon = tornadus, Move = confide, P = 1

; Pokemon = tornadus, Move = defog, P = 1

; Pokemon = tornadus, Move = doubleteam, P = 1

; Pokemon = tornadus, Move = embargo, P = 1

; Pokemon = tornadus, Move = leer, P = 1

; Pokemon = tornadus, Move = metronome, P = 1

; Pokemon = tornadus, Move = nastyplot, P = 1

; Pokemon = tornadus, Move = raindance, P = 1

; Pokemon = tornadus, Move = rest, P = 1

; Pokemon = tornadus, Move = roleplay, P = 1

; Pokemon = tornadus, Move = sandstorm, P = 1

; Pokemon = tornadus, Move = scaryface, P = 1

; Pokemon = tornadus, Move = sleeptalk, P = 1

; Pokemon = tornadus, Move = snowscape, P = 1

; Pokemon = tornadus, Move = substitute, P = 1

; Pokemon = tornadus, Move = sunnyday, P = 1

; Pokemon = tornadus, Move = swagger, P = 1

; Pokemon = tornadus, Move = tailwind, P = 1

; Pokemon = tornadus, Move = taunt, P = 1

; Pokemon = tornadus, Move = torment, P = 1

; Pokemon = tornadus, Move = toxic, P = 1

; Pokemon = beartic, Move = aquajet, P = 1

; Pokemon = dusclops, Move = shadowsneak, P = 1

; Pokemon = dusclops, Move = snatch, P = 4

; Pokemon = dusclops, Move = suckerpunch, P = 1

; false.

## There’s something about spreadsheets

At the top, I said that this experience had taught me about the kinds of interfaces I want to build.
One of those lessons is fairly obvious: Prolog can be a little clunky, but it’s an elegant language for expressing and querying relations like the ones described here.
That has implications if you, like me, are interested in thejudicious use of declarative DSLsfor programming.

The other lesson is what kinds of tools work fornon-programmers.

I’m not the first person to think “it would be nice to know what priority moves my opponent’s team has.”
The Pokémon community has resources like this, built in the best programming interface of all time: the humble spreadsheet.

Much prettier to look at, too.

I use a copy of“Techno’s Prep Doc”, which is one of those spectacularly-advanced Google Sheets you come across in the wild sometimes.
You put in the teams and it generates tons of useful information about the matchup.
It has a great interface, support for a variety of formats, scannable visuals, and even auto-complete.

I was curious about the formula for finding priority moves.
It’s gnarly.

={IFERROR(ARRAYFORMULA(VLOOKUP(FILTER(INDIRECT(Matchup!$S$3&"!$AV$4:$AV"),INDIRECT(Matchup!$S$3&"!$AT$4:$AT")="X"),{Backend!$L$2:$L,Backend!$F$2:$F},2,FALSE))),IFERROR(FILTER(INDIRECT(Matchup!$S$3&"!$AW$4:$AW"),INDIRECT(Matchup!$S$3&"!$AT$4:$AT")="X"))}

With a little bit of clicking around, I was basically able to figure out what this does.
There’s a “Backend” sheet that lists all the moves.
It’s effectively a hard-coded version of my Prolog query.

The lookup formula does some filtering, VLOOKUP-ing, and kinda-metaprogramming (INDIRECTreturns a cell reference) to find all the Pokémon on your team that are in that Backend list, and display them.

There are a number of reasons that I, personally, would prefer to work on a version of this database implemented in Prolog instead of one implemented with spreadsheet VLOOKUPs.
I plan to build webapps with this that do things the existing suite of Pokémon tooling can’t. (If I can everget scryer-prolog to compile to WASM, that is.)

Furthermore, the Prolog paradigm is clearly more extensible.
The spreadsheet backend is a hard-coded list of notable moves;
my database can look upanymove.
I still can’t really believe this query, which finds all the Special moves that Tornadus learns which are super-effective against any member of Justin’s team.
Nothing like that exists in any tool that I know of—it’s the kind of thing I normally try to figure out by endlessly switching tabs.
With the grammar established by my program, I put this together in like 30 seconds.

?- justin(Target), learns(tornadus, Move), super_effective_move(Move, Target), move_category(Move, special).

 Target = charizardmegay, Move = chillingwater

; Target = terapagosterastal, Move = focusblast

; Target = alomomola, Move = grassknot

; Target = scizor, Move = heatwave

; Target = scizor, Move = incinerate

; Target = runerigus, Move = chillingwater

; Target = runerigus, Move = darkpulse

; Target = runerigus, Move = grassknot

; Target = runerigus, Move = icywind

; Target = screamtail, Move = sludgebomb

; Target = screamtail, Move = sludgewave

; Target = trapinch, Move = chillingwater

; Target = trapinch, Move = grassknot

; Target = trapinch, Move = icywind

; false.

?-

I’m not interested in how structured programming is more extensible than spreadsheets, though.
I already know why I don’t do all my programming in spreadsheets.

={IFERROR(ARRAYFORMULA(VLOOKUP(FILTER(INDIRECT(Matchup!$S$3&"!$AV$4:$AV"),INDIRECT(Matchup!$S$3&"!$AT$4:$AT")="X"),{Backend!$L$2:$L,Backend!$F$2:$F},2,FALSE))),IFERROR(FILTER(INDIRECT(Matchup!$S$3&"!$AW$4:$AW"),INDIRECT(Matchup!$S$3&"!$AT$4:$AT")="X"))}

A question I find very important is: What is it about this particular problem, and the kinds of people who were motivated to solve it, where the most well-maintained solution available is a spreadsheet?

I believe there are a great many problems like that in the world, and a lot of improvements on that programming paradigm yet to be properly realized.

Thanks toMorry Kolmanfor reading a draft of this blog.

# Notes

* I joined the draft league in Season 3, lost in finals, then won Seasons 4 and 5. We just started Season 6.If you want it, you can have the crown.
* There are a number of coders in this draft league and I have gotten precisely zero of them to try out my Prolog program. That’s kind of the point though! It needs to be a website…
* The Prolog implementation I’m using isScryer Prolog, a modern Prolog implementation that emphasizes standards and formal correctness. The creator, Markus Triska, has a terrific online book,“The Power of Prolog,”and accompanyingYouTube channelthat has soundtracked my breakfast for weeks.
* Scryer Prolog is also designed to encourage more constructs thatpreserve logical completeness and monotonicity, which means I’m not really supposed to use the\+/2or->/2predicates. I couldn’t really figure out how to express what I wanted with the replacements offered, though. Happy to edit if anyone wants to help.
* Also,on Markus’ website: “My goal is to provide programs that work as intended, reliably and conveniently, with zero surprises. Programs that you can run for multiple decades without any issues such as crashes, resource leaks or other unexpected behaviour.” This guy and I have somesimilar interests!
* I didsome fun metaprogrogrammingto get all the data into Prolog predicates using thePokémon ShowdownNodeJS API.
* Yes, putting the accent on the “e” everywhere but the code blocks was very annoying.