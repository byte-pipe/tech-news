---
title: Canon
url: https://tau.dev/2026/08/07/canon
site_name: hnrss
content_file: hnrss-canon
fetched_at: '2026-08-19T04:07:05.370982'
original_url: https://tau.dev/2026/08/07/canon
date: '2026-08-12'
published_date: '2026-08-07T00:00:00-07:00'
description: Teaching My Kid To Code With a Modern MUD
tags:
- hackernews
- hnrss
---

## My eight year old daughter wants to make video games.

She’s obsessed with this idea. She likesplayingvideo games
 too, but it’s just not the same. Experiencing the world, even
 defeating the world, is too passive. She wants tomakethe
 world.

So I made her a game where she can make games. A multiplayer world
 made of text and images and a tiny new scripting language, where she
 can take anything and everything apart to see how it works. I first
 learned to code in the days whenView Sourcewas a reliable
 teacher, and I think she deserves the same.

The game has a lot of limitations. The language,Cant, is
 not a very good language, and that’s on purpose.

But it also turned out to be a lot of fun. I call it:

# Canon

Canon is a modern, web-based take on the classicMUDsof the Old Internet.

For the uninitiated: back before World of Warcraft made the MMORPG a
 big studio genre, we had text-based MUDs (andMUCKsandMUSHes) where players could adventure and socialize in vast realms made of
 pure written words.

I spent countless hours exploring these imaginary places. I wanted to
 make something in that spirit that would feel more familiar to a
 modern audience.

Canon has strong opinions about what makes a good MU*, and what makes
 a good learning environment. Every room, object, and interaction in
 Canon is player-created, and it can all be inspected, copied, and
 modified.

The kiddo loves it. If you’re the kind of grownup who’s into
 roleplaying or text adventures, or has some nostalgia for the age of
 telnet and the early web, you might like it too.

But first, recipe blog style, let me tell you how we got here.

### Training wheels for the bicycle for the mind

Do you rememberHyperCard? If not, do you rememberMyst? (If not, congratulations on being young. Bear with me.)

Bill Atkinson dreamed up HyperCard in 1985 after an LSD trip. I first
 encountered it in 1989, in my 4th grade computer lab, and also had my
 mind expanded.

HyperCard works like this: there are cards.

I mean, that’s pretty much it. That’s the genius. There are cards, and
 you can put computer things on them. Buttons and text and pictures and
 video. Cards get stacked together. A HyperCardappis called
 a “stack”. Get it?

And then all those buttons and pictures and things: you can make them
 clickable. And you can tell them to move between cards in the stack.
 It’s a choose your own adventure book as UX.

(If this sounds kind of like a web site, well, yes. HyperCard was one
 of the first real usable instances ofHyperMediaand influenced Tim Berners-Lee’s development of the World Wide Web.)

on mouseUp
 go to card id 123
end mouseUp

That there is validHyperTalk, the programming language underlying HyperCard. But for the most
 basic interactions like that – click a button, go to a card – you
 don’t even need to know HyperTalk. You can wire things up using a
 simple GUI editor.

If you can click a button you can use HyperCard. And if you canuseHyperCard, you canprogramHyperCard.

I could write a whole series of posts about this. But the two things I
 want to impart to you now are as follows:

1. HyperCard wasmagic.
2. HyperCardsucked.

### It was magic and it sucked

In many ways HyperCard stacks werenot good apps. They were heavily constrained by the card metaphor. They used input
 elements from the MacOS visual language, but they did not, and could
 not, feel like normal native MacOS applications. HyperTalk made the
 same mistake later repeated byAppleScript: trying to make a programming language look more like natural
 language, thus failing to be either thing well.

To any real programmer it was a frustrating underpowered environment.
 But those same flaws and constraints made it magically accessible to
 two hungry groups:non-programmersandcurious kids.

The first group produced a ton of stuff. The Internet Archive has a
 playablecollection of thousands of stacks. If you remember the Early Web, just browsing the thumbnails should
 give you a familiar feeling. Games! Zines! Fandoms! Manifestos!
 Somehow porn! Before the web, people with a Mac and Something To Say
 traded stacks on floppies.

I fell into the second camp. At nine years old I found HyperCard on my
 elementary school’sMacintosh SEand quickly discovered that unlike most computer programs,everything in HyperCard was editable. I started making the
 first thing that popped into my mind, which was aStreet Fighterstyle fighting game with two crudely drawn players.

 Artist’s recreation. Alas, the original stack is lost to The
 Ages.
Which is what I call the box of dead floppies in my
 parents’ basement.
 

I didn’t know anything about programming, much less advanced gamedev
 concepts likesprites. But I knew I could link buttons to
 cards. So I did that. With the determination only a hyperfocused child
 can muster, I set aboutdrawing individual cards for every possible combination of player
 moves and positions, with buttons as “controls” to move between them. I’d found me a
 hammer, and I could see how to make a game out of nothing but nails.

You’re on card 154. Player 1 is in quadrant 2, idling. Player 2 is
 in quadrant 3, defending. If player 1 presses the “attack” button,
 go to card...

It took meweeksstaying late after school. But it worked. Imade a game. I could play my own creation. I’ve spent my
 whole career chasing that high.

But that was just the beginning. One of the really clever things Bill
 Atkinson did was to make it so when you edited HyperCard behaviors
 with the GUI, it justwrote the corresponding codefor you.
 About halfway through my laborious clicking-and-linking project, I
 noticed theScript…button in the editor, pieced together
 its implications, and started using a copy & paste HyperTalk
 snippet and a systematic naming scheme for all my hundreds of cards to
 speed up development.

Near the end the computer teacher (I’m pretty sure we just called the
 class “computers”) noticed what I was up to and dug theHyperCard Reference Manualout of a drawer for me. This was
 my first experience reading a tech manual cover to cover.

### Many years later…

I’m not going to make my daughter learn HyperCard. I’m a bit of aTroll Dad, but notthatmean.

But I did want to reproduce the magical combination of creative
 freedom and mechanical constraints that made HyperCard so eye-opening
 for young Nick. Canon needed:

* Instant gratification. As soon as you put a thing on screen, it’s
 already part of the game.
* View Source. Everything in the game should be built with the game’s
 own tools, and freely editable/copyable/take-apart-able.
* A GUI for the simplest interactions.
* A smooth learning gradient from GUI to writing raw code.
* Just enough power in that code to build a wide range of fun game
 mechanics, and to teach basic programmer ways of thinking.
* But limited enough that a beginner could grasp the entire set of
 primitives.

### Instant gratification

The great thing about a text-based world is that you can add anything
 you want just by typing “there is a [thing] here”. You’re constrained
 inhowyou can build – no fancy 3D visualizations or
 impressively realistic physics engines – but have unlimited freedom inwhatyou can build.

Canon is made of three things:

1. Players
2. Rooms
3. Items

PlayersandRoomsare both just text
 descriptions and, optionally, images. To make either, you just answer
 a question:what does this look like?

### View source

Itemsareeverything else. They are also
 text descriptions and images, so you can flavor an item as anything
 you want: an inanimate object, a pet, an NPC, a spell effect, a
 vehicle, a doorway, a quest marker, a message, etc.

But in addition to text and images, items are also made ofactionsandstate, viaCant. It looks
 like this:

item "Hooded Lantern" {
 describe "An iron lantern with a hinged hood."
 on "light" {
 narrate "{player}’s {item} swings open and warm light spills out."
 }
}

That’s enough to produce a lantern the player can light:

Here’s a slightly more complicated item, a magic 8-ball:

item "Magic 8-Ball" {
 describe "A prophetic billiard ball. Give it a shake?"
 or "Give it a shake to see your future."
 or "Dare you shake it?"
 on "shake" {
 say
 "It is certain."
 or "Outlook good."
 or "Signs point to yes."
 or "Don’t count on it."
 or "My sources say no."
 or "Reply hazy, try again."
 or "Ask again later."
 }
}

Theorkeyword works anywhere Cant takes a text string.
 It randomly picks a variant each time the string is used: when a
 player looks at an item, or triggers an action. I wanted this baked
 into Canon at the lowest level.

There’s something especially delightful, to a new programmer, about an
 RNG. You tell the computer what to do, and it does it. But you also
 told it to exercise a tiny bit of its own agency. It’s both surprising
 and not surprising. You programmed every response, you know all the
 things it can say, and yet you don’t know exactly what it will say
 when you press the key or click the button. It’s like suddenly being
 able to tickle yourself.

Notice in addition toshake, this item has aclonebutton. Every item in Canon can be cloned. Items
 you own (which include anything you’ve cloned) can be edited. Every
 game or toy or quest made by another player is also atutorial.

### A GUI for the simplest interactions

The 8-ball is one of the first toys I made to tempt the kiddo. I left
 it lying in the starting zone. Even when you know nothing about
 conditional logic, even if you don’t look at the code, it’s easy to
 see how it works from a few minutes of playing with the ball. And it’s
 easy to imagine how you could modify it into a flipping coin, or an
 NPC that tells random jokes.

Or, say, a D20:

I am completely serious.

If you are a programmer, one thing you might notice about this is that
 it’s horrible. This is an inefficient way to write something that
 could obviously berandInt(1,20). But it is extremelyapproachable.

Cant is a language designed to be bad in educational ways. It’s
 optimized for ease of understanding over speed of writing. It’s the
 opposite ofDRY.

### A smooth gradient from GUI to code

Let’s expand that editor window a little:

An experienced programmer will notice this code could’ve been a
 one-liner. But a beginner will notice the code is already a lot less
 work than clicking 20 buttons and 20 text inputs.

The code and the structured editor are synced. Any valid expression in
 one immediately updates the other. I wanted this to tempt the kiddo
 the same way HyperCard’sScript…button tempted me.

### Just enough power

Okay,saying random stringsis fun, but it’s not much of a game. What else can this thing do?

A few examples:

item "Dueling Wand" {
 describe """
 A hazel {item} wound with copper wire, humming faintly.
 {when item vigor <= 0}Its light is out. A defeated duelist’s wand, until someone mends it.{end}
 """
 borne "A hazel {item} {when item vigor <= 0}hangs dark and quiet{else}crackles with impatience{end} in {player}’s grip."
 afield "A hazel {item} lies here, {when item vigor <= 0}its lights dimmed{else}crackling with magic potential{end}."
 state {
 vigor 30
 }
 on "fireball" {
 when item vigor > 0 {
 when target vigor > 0 {
 subtract target vigor 1d20
 narrate "{player}’s {item} roars! A ball of fire breaks over {target}."
 when target vigor <= 0 {
 narrate "{target}’s wand goes dark. {player} stands victorious."
 }
 }
 otherwise {
 narrate "{player}’s {item} finds no one standing to strike."
 }
 }
 otherwise {
 narrate "{player} attempts to cast but their {item} is dark until mended."
 }
 }
 on "mend" {
 when target vigor >= 30 {
 narrate "{player}’s wand hums, finds nothing to mend on {target}, and declines to waste the charm."
 }
 otherwise {
 add target vigor 1d10
 narrate "Green light from {player}’s {item} knits itself over {target}."
 when target vigor > 30 {
 narrate "{target} sparkles briefly with excess power."
 set target vigor 30
 }
 }
 }
}

This is aPVPencounter. Two or more players can pick up
 Dueling Wands and fight each other. The key thing to notice here is:

 state {
 vigor 30
 }

Items in Canon can hold two kinds of state:marksandnumbers.

Marks are boolean flags. A lantern could beLIT, an NPC
 could beSUSPICIOUS, a door could beLOCKED.

Numbers are what they sound like. A campfire could havewarmth 10, an NPC could havehealth 20, a
 pickable lock could haveattempts 5.

Marks are always UPPERCASE, numbers always lower. The casing is the
 type.

Note also thatvigorabove ison the wand, not
 the player. Players have no state themselves, only on the items they
 carry. When you target a player with a fireball, you are targeting
 their wand. Or rather, you are targetingany items they carry that answer to statevigor.

In this way, all encounters and mini-games in Canon areconsensualandopt-in. Don’t want to duel? Simply
 don’t pick up the wand.

State names are completely arbitrary. This wand hasvigor, but another set of weapons might havelifeorhealthorstamina. You
 can build a suite of items that all answer to the same state and
 interact, or pick unique names for unique encounters.

Here’s an NPC using both marks anddialog:

item "The Dialog Tree" {
 describe "A talking tree, only too happy to bend your ear about the joys of being a plant."
 remembers
 state {
 PLEASED false
 }
 on "chat with the tree" {
 dialog
 "Welcome, welcome, have a seat…"
 or "Hello there, little animal…"
 {
 choice "How’s being a tree?" {
 dialog "Oh, the absolute best! You simply must try photosynthesis."
 mark item PLEASED
 }
 choice "Uh, excuse me, I was just leafing…" {
 narrate "{item} looks a little crest… er, branchfallen."
 unmark item PLEASED
 }
 }
 }
}

This creates your classic RPG dialog box. Dialog can nest arbitrarily
 deep, and contain any other Cant effect as the result of a dialog
 choice, or present different choices based on number and mark state.

Notice the tree’s mood changes depending on your answer, tracked by
 thePLEASEDmark.

Therememberskeyword tells an item to retain its state
 when left alone in an empty room. Without it, state resets when no
 players are around so encounters are fresh for new visitors. In the
 Dialog Tree’s case, we want it to retain its mood from whoever last
 spoke to it.

If you look closely you can also see the Dialog Tree’s image changes.
 Item images can respond to marks and numbers. Cant is all about text,
 so images are handled separately in the item editor:

The same is true forPlayers. You can change your
 character’s image based on the state of whatever items they carry.
 Here’s a simplepaper dollitem that has no action, but does
 set a state:

item "Fancy Red Pirate Coat" {
 describe "A fancy red coat, fit for a pirate captain."
 state {
 OVERCOATED true
 }
}

And here is a player where bothtext descriptionandactive imagerespond to the presence or absence of the coat:

Rather than (or in addition to) altering a player’s descriptive text,
 we can also give items an optionalbornedescription
 which is appended to the player’s description.

item "Fancy Red Pirate Coat" {
 describe "A fancy red coat, fit for a pirate captain."
 borne "{player} is fashionably draped in a {item}."
 state {
 OVERCOATED true
 }
}

You can playcharacter customizer(many people’s favorite
 game in any game!) all day long, with just text and images.

You can make a lot of fun dynamic objects with images and conditionals
 and state. But a simple bit of flavor text is still often the best
 part. Out of all the items I’ve made, my daughter’s favorite (or at
 least most frequently employed) remains the humble snowball:

item "Snowball" {
 describe "An expertly packed snowball."
 on "throw" {
 narrate "{player} hits {target} in the face with a snowball! _Paff!_"
 }
}

### But not too much

You may notice in both theDueling Wandand
 responsive player/item images above, conditionals are very limited.
 Eachwhentakes a single condition. There is noand,or, etc. There is also no equivalent ofelse if.whentakes a single condition, and
 a single optionalotherwiseblock. If you want more
 complicated control flow, you can nestwhen. Again, this
 will probably strike an experienced programmer as bad, but it serves a
 purpose.

For one thing, the structured editor is complicated enough. The
 Dueling Wand alone, while far from the most sophisticated item you can
 build, gets visually noisy:

Adding optional combining blocks would make it harder to navigate. But
 more to the point, the simplewhenis meant to be good
 enough exactly until it isn’t.

Cant is a language designed to be frustrating in enlightening ways. A
 reasonable objection might be that it will teach bad coding habits.
 But from my own childhood experience, what it will actually teach iswhy the good habits are goodand how the layers of
 abstraction and expressibility get built one on top of another.

The kiddo is already building cool stuff with Cant. Eventually she’ll
 become annoyed with its limitations. But at that point she will also
 be able toarticulate those limitations, and imagine ways it
 could be improved. And that will be a gateway. When she graduates to a
 bigger fuller more expressive programming language, she’ll understand
 why it’s better.

### Adversarial mindset

Another thing I want Canon to teach is how tohack.
 Programming outside the lines. The kid is already very fond of
 mischief and loopholes, so this is playing to her strengths.

You may have noticed a slight flaw in some of the examples above. If
 you can edit every Dueling Wand, you can just edit your own wand to
 give yourself extra vigor, or never take damage. If you can edit every
 dialog, you can just sneak a peek to see which choices give you the
 ending you want. Every encounter is hackable.

This, too, is intentional. For purposes of nurturing a growing
 engineer brain, creating puzzles, beating puzzles, and hacking puzzles
 are all win conditions.

From the broader game perspective, it’s part of “everything is
 consensual”. Canon has no permanent points to win or lose. There are
 no scarce resources attached to your character that someone can cost
 you. The only reason to have a PVP duel is to have fun with your
 friends. The only reason to play a mini-game, or fulfill a quest
 someone crafted, is to have the experience they crafted for you. Or if
 you’re the sort of person who has more fun taking apart the experience
 to see how they made it, you can do that too.

That said, there are afewconcessions to authorial control.
 The main one isKingdoms. The Canon map consists of a
 shared overworld, and individual zones belonging to each player. The
 overworld is mostly a flavorful way to travel between Kingdoms, and
 not a secure place to leave things. Anything you set down in the
 overworld can be picked up by another player. But in your Kingdom,
 only you can place items in a room, and only you can remove them.
 Other players cancloneyour creations to figure out how they
 work, but they can’t modify the originals. This lets you create stable
 multi-room, multi-item games and encounters.

Want a quest where you talk to a series of NPCs in different villages
 to piece together a mystery? Or have to find the right keycards to
 open the right doors in a maze? Or you collect and tend to an egg with
 the right magical ingredients to hatch a baby dragon? Those are all
 easy to make in your Kingdom.

### Chutes and ladders

A Canon map looks like this:

This is an overworld. The colored nodes with⌂glyphs are
 entrances to Kingdoms, which have their own maps. In both cases, the
 map data structure is atree, or anundirected acyclic graph. The map grows only by budding new
 rooms, never by connecting two existing rooms.

This has some desirable properties:

* With no fixed dimensions, a “room” can be anything you describe.
 You can make a literal single room in a building, or a whole
 building, or a vast terrain. An empty void. A pocket universe. A
 state of mind. The abstract map matches the total freedom of text.
* It allows Kingdom owners tolock their doors, creating
 private lairs, invite-only guild halls, and puzzles that depend on
 gated movement, while enforcing that locks only workin the direction away from the root node. In Canon you
 can lock someone out, never in. You can make lairs, but you can’t
 make dungeons.
* It teaches the kiddo something about user interface abstractions
 and the clever sorts ofhacks that go into game design. For example:

Many popular level designs cannot be expressed purely in Canon’s map
 structure. Imagine a network of treehouses, connected by rope bridges,
 above a forest floor. The treehouse village is a series of connected
 rooms to the north, south, east and west. The forest floor is the
 same. Each forest floor room shouldalsobe connected to its
 matching canopy room by up and down exits, but these would form cycles
 in the map graph.

Canon solves this the wayDOOMdid: by faking it. AteleportCant action attached to an
 item offers to transport players between arbitrary rooms.

item "Rope Ladder" {
 describe "A rope ladder, dropping out of the canopy like an invitation."
 on "climb" {
 say "The rungs creak under you."
 teleport "lomise-anthil-nara"
 narrate "{player} hauls up out of sight."
 }
}

The quoted address is the destination room’slocus: a
 randomly generated id you can only learn by standing in the room. This
 is so the Cant remains portable, but you can’t simply guess the
 address of an unfamiliar room, sinceteleportation can bypass locks. (That’s right, token security
 is also on the curriculum!)

Ladders and elevators are just the start. You can use teleportation to
 build:

* Mounts: create aHorseor aMotorcycleor aDragonto carry you to
 different destinations with arideaction.
* NPCs: combinedialogandteleportfor anElevator AttendantorPortal Mage.
* Hearthstones and Bookmarks:found a cool spot on
 the map? Craft yourself a quick teleport to return to it any time.

### Agents and gen α

I seeded Canon with a bunch of toys and games for the kiddo to take
 apart and remix. But I wanted to make sure she could create her own
 stuff from the start. So I also included aWishfunction.
 Once a day, each player canWishto the Machine God. An
 LLM will craft an item to your specifications, including functional
 Cant with explanatory comments.

# Built by The Machine, but yours to change. Edit freely!
item "Laughing Coat" {
 describe "A long coat of storm-grey wool, its collar high and its lining stitched with a grinning seam that never quite lies flat, as if it is always about to find something funny."
 borne "A long coat rides {player}’s shoulders, and every so often it shudders and lets out a low, delighted chuckle at some peril only it can see, as though danger were the finest joke ever told."
 on "pickup" {
 # fires by itself whenever someone takes this up – narrate paints the moment for the whole room
 narrate "{player} shrugs into a long grey coat, and it settles across their back with a satisfied little snicker."
 }
 on "drop" {
 # …and this fires when it is set down again
 narrate "A long grey coat slips from {player}’s shoulders and folds itself into a heap, its laughter dwindling to a sleepy, contented wheeze."
 }
}

Cool, right?

Here are two pieces of feedback I’ve received, each from multiple
 adults who’ve tried Canon:

1. “I love everything except Wish. I hate AI and don’t want it
 anywhere near my creative outlets. You should warn people when
 they sign up that this includes an LLM.”
2. “Instead of just uploading my own images, there should be a
 button I can press to make an AI generate an image from the
 description I wrote!”

I’m not sure what to make of this.

Wishis the only AI feature in Canon, and it’s strictly
 limited to a single tutorial item per day. In a gameworld where
 everything else is explicitly written by humans for humans. And that
 alone was instantly polarizing.

Among grownups, anyway. The kiddo had a healthier attitude: total
 indifference. She took right to wishing for things, and then
 immediately overwriting them with her own words and imagination. She
 is equally likely to use images from GIPHY, Image Playground, and her
 own Photo Library full of original pictures and drawings. AI is just
 another tool to her.

Canon started many years ago, before the kiddo was born. I like
 virtual worlds and wanted to try my hand at making one. (I was going
 to include a section here about all the opinionated stuff I put into
 Canon thatisn’tabout programmer pedagogy, but about making
 a friendly, collaborative, social place out of text. But this is very
 long already. Perhaps that’ll be a separate post.)

Alas, I had far more ideas than time to devote to it, so it went on
 the shelf.

Lately I’ve been dusting off old side projects and 10xing them withClaude. Far from spoiling the magic, it’s reinvigorated my love of coding.
 Making Canon was delightful, involved a whole lot of my judgement and
 years of experience as an engineer, and went way faster than I could
 have accomplished alone.

But then I also did make a game where my kid and I lovingly hand craft
 code together. Even if the future is agentic everything, I think
 learning Cant will teach her useful skills and mental habits. And it’s
 justfun. That, too, has been reinvigorating.

### Yoink

I’ll leave you with some quotes from my satisfied user base of one
 energetic eight year old:

“You mean I can make anything I want?! Characters? Quests? Stories?!
 :D”

me: “Why is your inventory so full? Wait, why do you have ten of
 everything? You know you can just keep one and clone it, right?”

kiddo: “Yeah, I know. ButI have ten!”

me: “You’ve managed to be a loot goblin in a game with no loot.”

kiddo: [maniacal giggling]

kiddo: “I broke into your house and stole all your stuff!”

me: “You mean you solved my riddle. Good job. But you can’t steal
 from my kingdom, only clone. I would know, I wrote it that way.”

kiddo: “Yeah, but I cloned everything ten times, which means I havemore of your stuff than you do!”

me: …

kiddo: [maniacal giggling]

“I know what we should make! We should make an item that’s a
 computer. And when your character plays the computer,they’re playing Canon!”

Only eight and she already thinks recursion is funny. She really is my
 little engineer.

### Try it for yourself

Canon is decidedly beta, but you can play it! Just shoot a short
 human-to-human email tonick@tau.devand I will personally
 send you an invite code.

Once in you’ll be able to invite friends with your own code. I want to
 keep growth slow for now, but everyone genuinely curious is welcome.

There are Canon and Cant features I haven’t touched on here.
 Documentation is sparse, but that’s part of the game. Poke and prod
 and tinker. Your inner eight year old knows what to do.

Nick Tau·August 7, 2026