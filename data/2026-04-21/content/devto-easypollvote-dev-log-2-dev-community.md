---
title: 'EasyPollVote [Dev Log #2] - DEV Community'
url: https://dev.to/francistrdev/easypollvote-dev-log-2-4g80
site_name: devto
content_file: devto-easypollvote-dev-log-2-dev-community
fetched_at: '2026-04-21T20:02:32.311516'
original_url: https://dev.to/francistrdev/easypollvote-dev-log-2-4g80
author: FrancisTRᴅᴇᴠ (っ◔◡◔)っ
date: '2026-04-17'
description: Welcome to the Second DEV LOG! Welcome to the second Dev Log of my full stack application... Tagged with discuss, easypvdevlog, nextjs, typescript.
tags: '#discuss, #easypvdevlog, #nextjs, #typescript'
---

Features a dynamic PokeAPI poll demo

# Welcome to the Second DEV LOG!

Welcome to thesecond Dev Logof my full stack application calledEasyPollVote (EasyPV)!

 

# What is EasyPollVote (EasyPV)?

ANext.js applicationwhere the ultimate goal is having the convenience to create your own poll and share it for others to vote on your custom poll!

For example, a user can create their own poll. Their poll can be something like "Do you like Cats or Dogs?" following the two options users can vote on"Cats" or "Dogs".Then, they will be able to send the private link to anyone and the voters can vote on it without the need to create an account!

That is the whole goal.Do note that this goal may change as time goes on!

The current goal is to learn about the use of Supabase!

 

# Current Progress

Made some UI changes in the Front Page!

It issmaller and compactsince I didn’t like where you have to scroll down. The only time you have to scroll down is when your screen is small or you are in mobile!

The Poll Demo of choosing your favorite Pokémon is no longer hard coded! It was seen that you guys want to have more options (more that in a bit) since@sylwia-laskwant to vote for Umbreon! 😊

I look into thePokeAPIsince they provided all information on Pokemon such as images, colors, names, etc.

For the Demo, I made it where it uses thePokeAPIto fetch the Pokémon data that includes the name, image, and primary color of the Pokémon. Since the demo only allows the user to choose two options, we get two random Pokémons.

type
 
Pokemon
 
=
 
{

 
name
:
 
string
;

 
sprite
:
 
string
;

 
color
:
 
string
;

};

const
 
TOTAL_POKEMON
 
=
 
1010
;

...

const
 
[
id1
,
 
id2
]
 
=
 
getWeeklyPokemonIds
();

const
 
fetchOne
 
=
 
async 
(
id
:
 
number
):
 
Promise
<
Pokemon
>
 
=>
 
{

 
const
 
[
pokemonRes
,
 
speciesRes
]
 
=
 
await
 
Promise
.
all
([

 
fetch
(
`https://pokeapi.co/api/v2/pokemon/
${
id
}
`
),

 
fetch
(
`https://pokeapi.co/api/v2/pokemon-species/
${
id
}
`
),

 
]);

 
const
 
[
pokemonData
,
 
speciesData
]
 
=
 
await
 
Promise
.
all
([

 
pokemonRes
.
json
(),

 
speciesRes
.
json
(),

 
]);

 
return
 
{

 
name
:
 
pokemonData
.
name
,

 
sprite
:
 
pokemonData
.
sprites
.
front_default
,

 
color
:
 
speciesData
.
color
.
name
,

 
};

};

const
 
pokemonResults
 
=
 
await
 
Promise
.
all
([

 
fetchOne
(
id1
),

 
fetchOne
(
id2
),

]);

setPokemonList
(
pokemonResults
);

Enter fullscreen mode

Exit fullscreen mode

The Poll randomizes the Pokémon each week, which gives the user fresh choices about choosing their favorite!

function
 
getWeekNumber
()
 
{

 
const
 
now
 
=
 
new
 
Date
();

 
const
 
start
 
=
 
new
 
Date
(
now
.
getFullYear
(),
 
0
,
 
0
);

 
const
 
diff
 
=
 
now
.
getTime
()
 
-
 
start
.
getTime
();

 
const
 
oneDay
 
=
 
1000
 
*
 
60
 
*
 
60
 
*
 
24
;

 
const
 
dayOfYear
 
=
 
Math
.
floor
(
diff
 
/
 
oneDay
);

 
return
 
Math
.
floor
(
dayOfYear
 
/
 
7
);

}

function
 
getWeeklyPokemonIds
():
 
[
number
,
 
number
]
 
{

 
const
 
week
 
=
 
getWeekNumber
();

 
const
 
id1
 
=
 
(
week
 
%
 
TOTAL_POKEMON
)
 
+
 
1
;

 
const
 
id2
 
=
 
((
week
 
*
 
7
 
+
 
13
)
 
%
 
TOTAL_POKEMON
)
 
+
 
1
;

 
return
 
id1
 
===
 
id2
 
?
 
[
id1
,
 
(
id2
 
%
 
TOTAL_POKEMON
)
 
+
 
1
]
 
:
 
[
id1
,
 
id2
];

}

Enter fullscreen mode

Exit fullscreen mode

Note:The Pokémon randomize each week has not been fully tested. We are about to find out later in the weekend if it does change!

Note:There is no functionality where it wipes the data in the database, though it will be implemented in the future

That is all for the DEMO Poll! But wait, there’s more!!

 

You may notice that there is a link where you can create your own Poll!

When you go to that page, it gives you a form to create your own Poll by providing:

* Poll Title
* The Poll End date(If the poll reaches the end date, the poll will end and the button to submit your vote will be hidden)
* Poll Options(You can have up to 4 options!)

If you want to create a poll, now you can!😊

Once you create the poll, you will see the message under the button that gives you a link to share to others on voting on your poll.

Poll created successfully! Share this link: https://easypollvote.vercel.app/poll/53 

Enter fullscreen mode

Exit fullscreen mode

When you click the link, the poll format is similar to the Demo as shown below.

Note:There are currently no restrictions on voting more than once. That feature is in my TODO list and will be implemented in the future.

Note:The end date has not been tested. Again, we are about to find out ultimately if the flow does as intended. Do note it is still a work in progress, so expect any bugs.Please report the bugs in the comments if you encounter anything unusual!

Without going to detail, the custom poll actually takes two tables.

We have"Poll"table, which consist of:

* ID (Primary Key)
* created_at (timestamptz)
* PollTitle (string)
* Poll_EndDate (timestamptz)
* Poll_Ended (bool) (This determines if the end date of the poll has reached)

We also have"VoteOptions"table, which consist of:

* ID (Primary Key)
* poll_id (Primary and Foreign Key of thePoll table'sID)
* option_text (string)
* Votes (Int)
* option_color (string)

Next time, I will be talking about in detail on how the flow works for the demo and the custom poll!

 

# Official Website

If you would love to see the project yourself, feel free to check out the link here:https://easypollvote.vercel.app

I recommend to put a fake email and a fake name if you are using the app.Everything works as intended! Check it out and feedback is greatly appreciated!

If you like to vote on my custom poll on who you want to be your mentor. Would you choose@ben,@jess,@jonmarkgoor@theycallmeswift?, feel free to vote on my poll here:https://easypollvote.vercel.app/poll/53

 

Any questions/comments/feedback? I would love to hear from you!

 

Note:This post is monitored by the University and therefore the repository is currently private until the early Summer!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (15 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse