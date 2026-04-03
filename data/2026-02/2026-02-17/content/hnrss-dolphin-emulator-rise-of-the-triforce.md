---
title: Dolphin Emulator - Rise of the Triforce
url: https://dolphin-emu.org/blog/2026/02/16/rise-of-the-triforce/
site_name: hnrss
content_file: hnrss-dolphin-emulator-rise-of-the-triforce
fetched_at: '2026-02-17T11:20:12.220454'
original_url: https://dolphin-emu.org/blog/2026/02/16/rise-of-the-triforce/
date: '2026-02-16'
description: 'During the rapid technological advancements of the early 1990s, the video game industry was on the cusp of a massive addition - another dimension. With console shenanigans like the Super FX chip giving players a taste of 3D, hype was at an all-time high. But the games released for home consoles were nothing compared to what arcade developers were capable of doing. By employing gigantic budgets and cutting-edge hardware, the arcade gave players a chance to see the future, today. But the future eventually arrived with the launch of the 5th generation of consoles. All of a sudden, the revolutionary 3D hardware features that were once exclusive to arcades were now available in home consoles. Without next-generation hype pushing players into the arcade, powerful but expensive arcade machines were no longer sustainable to develop. The industry adjusted by moving toward more cost effective solutions, with many turning to the inexpensive, already proven 3D-capable hardware available
  in 5th gen home consoles. Rather than turning around the decline of the arcade, the cheaper hardware may have helped accelerate it. There were fewer unique experiences to pull players into the arcade, and previous hit exclusives were now seeing high quality home console ports that allowed them to be enjoyed without munching quarters. When the 6th generation arrived with the Dreamcast and the PlayStation 2, many arcade stalwarts waved the white flag and started to shift their arcade divisions to home console projects, with mixed success. Sega was among those hit hardest by this era. They produced some of the greatest arcade thrills of the 1990s and enjoyed massive success in the home console market with the Sega Genesis/Mega Drive. But a string of mistakes and miscalculations combined with the slumping arcade industry sent them to the brink of bankruptcy. By 2002, the Dreamcast had been soundly defeated by the launch of the PlayStation 2, and Sega began porting some of their hits to their
  former rivals'' hardware just to stay afloat. The home market was lost, but the languishing arcade scene presented Sega with an opportunity. They still had legendary arcade development teams, and if Sega could leverage them to produce a wave of arcade hits, they would be in a position to dominate a new era of arcades when most others were changing gears. There was just one problem: Sega didn''t have the resources that they once did. If they were going to do this, they needed some help. And so they did something that would have been considered unthinkable just five years prior. Sega teamed up with Nintendo to develop a GameCube-based arcade platform. Bolstering their ranks was Namco, another coin-op stalwart with tons of arcade veterans. Three companies, one mission: Triforce.'
tags:
- hackernews
- hnrss
---

During the rapid technological advancements of the early 1990s, the video game industry was on the cusp of a massive addition -another dimension. With console shenanigans like theSuper FX chipgiving players a taste of 3D, hype was at an all-time high. But the games released for home consoles were nothing compared to what arcade developers were capable of doing. By employing gigantic budgets and cutting-edge hardware, the arcade gave players a chance to see the future, today.

This is filler text to try and hack around a problem on the website. You shouldn't be seeing this. If you are, please report this bug.

In early 1994, this was 3D graphics for the home.
15 FPS,
low resolution (256x192)
, 6500 polygons per second, practically no textures, and no texture filtering. And this required
extra hardware in the cartridge
 to achieve.

Meanwhile, this was in arcades.
60 FPS
, ~4x the pixel count (496x384), 300,000 polygons per second, and filled with perspective-correct and trilinear-filtered textures.

Video Credit:
arronmunroe

But the future eventually arrived with the launch of the5th generation of consoles. All of a sudden, the revolutionary 3D hardware features that were once exclusive to arcades were now available in home consoles. Without next-generation hype pushing players into the arcade, powerful but expensive arcade machines were no longer sustainable to develop. The industry adjusted by moving toward more cost effective solutions, with many turning to the inexpensive, already proven 3D-capable hardware available in 5th gen home consoles.

Rather than turning around the decline of the arcade, the cheaper hardware may have helped accelerate it. There were fewer unique experiences to pull players into the arcade, and previous hit exclusives were now seeing high quality home console ports that allowed them to be enjoyed without munching quarters. When the6th generationarrived with the Dreamcast and the PlayStation 2, many arcade stalwarts waved the white flag and started to shift their arcade divisions to home console projects,with mixed success.

Sega was among those hit hardest by this era. They produced some of the greatest arcade thrills of the 1990s and enjoyed massive success in the home console market with the Sega Genesis/Mega Drive. But a string ofmistakesandmiscalculationscombined with the slumping arcade industry sent them to the brink of bankruptcy. By 2002, the Dreamcast had been soundly defeated by the launch of the PlayStation 2, and Sega beganportingsome of theirhitsto their former rivals' hardware just to stay afloat.

The home market was lost, but the languishing arcade scene presented Sega with an opportunity. They still had legendary arcade development teams, and if Sega could leverage them to produce a wave of arcade hits, they would be in a position to dominate a new era of arcades when most others were changing gears. There was just one problem: Sega didn't have the resources that they once did. If they were going to do this, they needed some help.

And so they did something that would have been considered unthinkable just five years prior. Sega teamed up with Nintendo to develop aGameCube-based arcade platform. Bolstering their ranks was Namco, another coin-op stalwart with tons of arcade veterans.

Three companies, one mission: Triforce.

The Triforce IPL (Initial Program Loader).
Click/tap to Play. File has audio.

### Triforce Hardware¶

While Triforce was a collaboration project, it still feels like a verySega codedarcade system. It can even use certainNAOMIstyle components! Along with the Xbox-basedChihiro, the Triforce is sometimes considered a successor to theNAOMI 2.

An aluminum shell makes these units heavy and durable.

Each unit has stickers for the serial number, game ID, and more, alongside mounting brackets.

The JVS I/O, audio output, and VGA output ports are visible on the back of the unit.

There are a few Namco branded daughterboards, too!

Inside of this metal shell is... a GameCube! Quite literally, actually.

Click/Tap to peek at the GameCube underneath!

The Triforce hardware is built around a stock GameCube motherboard, with two Triforce-specific boards attached to it: the AM-Baseboard and AM-Mediaboard. TheAM(Amusement Machine) boards are the secret sauce of the Triforce and transform the stock GameCube into something capable of producing arcade experiences.

The early boot process is the same as a retail console, but a modified GameCube IPL (sometimes referred to as the GameCube BIOS) is used to initialize the Triforce hardware and load the Triforce equivalent of a "home menu", Segaboot.

Any game-specific settings can be found in Enter Game Test.

Segaboot is a special disc image on the Mediaboard that can be loaded by the Triforce at will through special commands. It is responsible for loading the actual game and for providing the Service Menu, where the operator can run hardware tests and change settings on the machine.

By usingPicobootto override the boot process, it is possible to load a standard GameCube IPL or homebrew likeSwiss. And since all of the pins are still on the mainboard, we can also connect a standard GameCube front panel and even load full GameCube games from microSD over Serial Port 2!

This Triforce is running F-Zero GX. We thought it was funny.

The Baseboard is primarily responsible for input and output. It handles translation between JVS I/O devices (more on those later) and the GameCube'sSI bus. It also takes the GameCube's digital video output and feeds it to two VGA ports on the back of the main unit.

The AM-Baseboard is an integral piece of the Triforce and has many ports.

The Mediaboard's most important responsibility is storing and serving the game software to the GameCube. It is also used to handle other tasks, such as networking, through special commands.

This is a later revision Mediaboard, evident by the fact that the RAM slots are built into the board. Earlier units had a removable component that would hold the RAM.

The Triforce Baseboard was mostly unchanged throughout the Triforce's lifespan, but the Mediaboard could vary depending on the developer, game, and when the game was released. In fact, games weren't guaranteed to even come out on the same storage medium!

#### Format Wars¶

A spinning disc and active laser were notnormallyconsidered reliable enough for an arcade environment. These machines will be on all day, every day foryears, and players were often rough on machines that they didn't own. So, the Triforce eschews the standard GameCube mini-DVD alike format for its own storage solutions.

Most games were designed for the DIMM (Dual In-line Memory Module) variant of the Triforce, where game data is shipped onGD-ROMand loaded into RAM on the first boot. GD (Gigabyte Disc) was a format initially devised by Sega and Yamaha for use in the Dreamcast. Byincreasing the data densityof ordinary compact disc technology, the 12cm GD-ROM had somewhat comparable capacity to the GameCube's DVD-based 8cm disc (1GiB versus 1.46GiB).

Were GD-ROM drives more reliable than early DVD drives? Maybe! By this point, GD-ROM was an established technology that Sega was already using in arcades for years. Perhaps even more importantly, it wascheaper. Sega designed it so they could even reuse GD-ROM drives designed for their other arcade platforms, since they used a genericSCSI-style connector.

A GD-ROM disc, security key, and manual for a DIMM variant Triforce.

DIMM variant Triforces came with stickers advertising the amount of DIMM RAM on the Mediaboard. These stickers caused some confusion in the enthusiast community, as people would often mistake the amount listed as the total RAM accessible to the game. In reality, the DIMM RAM was mostly intended for use as a read-onlyRAM drive, rather than for general purpose use. As previously mentioned, the Triforce hardware is based around a stock GameCube motherboard, so games can only access the same 24+16 MiB of RAM that a retail GameCube uses.

512MB of RAM? That'd be a lot for the time!

Once the game was loaded into memory, it was intended to stay there. And thanks to a battery backup that maintained the data even in the event of a power failure, the GD-ROM may only be needed once in the entire lifetime of the machine.Thiswas their secret toward making the Triforce GD-ROM drive reliable for the arcade. One of the main exceptions would be if a new disc were inserted. Many Triforce games saw updates, which could be shipped on new GD-ROMs.

Namco's Triforce games ditched the GD-ROM and DIMM RAM and instead used 512MB NAND cartridges to store game data. The NAND retains its contents even if the system loses power and the backup battery runs dry, which eliminates the need for GD-ROMs. These games also saw updates through SD card or over the internet, with updates able to directly modify the NAND contents.

The NAND cartridge (the white rectangle at the top with the "MKA 2" sticker) fits snugly in the Triforce.

If we disassemble the cartridge and flip it over, we can see half of the memory banks along with the connector. The rest of the memory is on the other side!

Both methods of storing Triforce game data have the same goal in the end: deliver a disc image to the internal GameCube. In addition to the GD-ROM or NAND cartridge, each game also has a corresponding security key that must be inserted into the Triforce unit in order for the game to run.

#### Type 1, Type 3, and Saving in Arcades¶

There are two variants of Triforce I/O: Type 1 and Type 3. These refer to the Sega JVS Type 1 and Sega JVS Type 3. JVS stands forJAMMA Video Standard, a common standard created by a group of Japanese game companies for connecting various accessories and controllers to arcade systems. It's easiest to think of JVS I/O as the arcade equivalent to USB. Other Sega JVS I/O compatible devices can work with the Triforce even if they were originally designed for other arcade platforms, but it's up to the game developers to actually add support for a particular piece of hardware. Type 3 Triforces also have the capability to support more complicated analog input devices.

Whether it was Type 1 or Type 3, Sega had a trick that was instrumental to their efforts to revive the arcade scene and almosteveryTriforce game would use it. It was a revolutionary idea that had taken hold in the home console market but was still rare to see in arcades: saving and continuing.

By using cheap cards that could hold a small amount of data, players could buy what amounted to a small memory card directly from the arcade machine using a built-in vendor. These cards could be bought for as cheap as a single credit in some cases, and had enough storage to save progress, preferences, and other unlocks. Because the data wasn't locked to the machine, these cards allowed the player to continue their progress from any arcade that had the game and a working card slot.

The end goal of this was to get players more invested in arcade experiences by having them progress and unlock content. Some Triforce games are full of so many unlockables that it'd be impossible to see everything in a single session at the arcade.

The front of a magcard is colorful, with a printable surface for identification and progression tracking.

The back is all business.
If you'd like to read it,
click here
.

Triforce games can support two types of cards for saving: Magnetic Cards (magcards) and Integrated Circuit (IC) cards. Magcards are cheaper, fragile, and can only survive so many writes before failing. They have the added bonus of having a printable side, where the game can print a player's achievements and more. IC cards are more like old credit cards with a thicker plastic. They weren't printable, but were much sturdier.

A limit of 50 writes was imposed on magcards, likely to recoup printing costsandbecause the cards would eventually wear out. This meant that after 50 writes, the player would have to spend more money on a new card in order to continue saving their data. If an arcade was feeling generous, the operator could choose to make buying and/or refreshing cards free.

Free cards might lose money in the short term, but could keep players putting more money into a machine to keep playing!

Regardless of the card type, if the card were somehow destroyed outside of the machine for any reason, the save data would be lost and the player would have to start over with a fresh card.

Outside of the various cards and their readers, there were plenty of other fairly generic JVS I/O devices, such as coin mechanisms, arcade sticks, buttons, steering wheels, and pedals. Because there were so few Triforce games released, we'll take a look at unique JVS I/O devices on a game-by-game basis when we start spotlighting the games.

#### Bringing the Triforce Home¶

Hypothetically, let's say you have a vested interest in GameCube hardware and decided to purchase a Triforce arcade unit with a game to see how it works first-hand and write an article about it. Without a cabinet and all of the additional hardware that is required to run a game, the core Triforce is just a fancy paperweight, right? Actually, no!

Using a Raspberry Pi, we can convert USB controllers into JVS devices that the games will recognize thanks to JVS I/O emulation! JVS I/O uses a USB-A style connector, but arranges the pins differently. Compared to USB, JVS I/O's differential serial signal is closer to theRS485standard (aka the lastserial portstandard). It's notexactly the same, but by using a RS485 adapter connected to through USB-A with D- and D+ hooked up as the differential pair and VBUS hooked to the sense line, USB devices can communicate with JVS I/O. Combine that withOpenJVS, and you can have a computer interface with a Triforce to emulate JVS I/O devices.

In our hypothetical, we suggested that we only purchased one Triforce. In reality, we ended up withfourover the past few years: A Type 1 DIMM, a Type 3 DIMM, and two Type 3 NANDs. We also bought a few JVS I/O devices that popped up, including a Virtua Striker 4 Card Reader and a Chihiro/Triforce/NAOMI 2 compatible magcard reader/printer/distributor. However, our real JVS I/O devices ended up being pretty useless due to the fact we were still missing too much hardware to hook them up. JVS I/O emulation was mandatory, and was used to fake enough of the devices to get the games into a working state. To replace the Triforce's JVS power supply, we used an ATX power supply with the 20+4 pin power connector carefully modified to match its pinout. Do not attempt this at home!

OpenJVSdoes a well enough job faking devices that most Triforce games can be made to run under it. More importantly, it also let us map the various input devices attached to the games to a DS4 controller. As a bonus, we used some of the extra buttons on the controller to map actions like inserting coins to make general play easier.

All of this tinkering wasjust enoughto let us control and play real Triforce games on real hardware.

Real Triforce hardware booting games.

Here's a closer look at our setup, with the Raspberry Pi, power supply, and a small portable screen hooked up to the second VGA port so that no external monitor is needed.

Now that we could play Triforce games, we had to give it a spin.

### The Triforce Games¶

Given that Nintendo hardware powers the Triforce, one might expect it to have someNintendo-developed games. But there aren't any. Despite Nintendo's pedigree for creating appealing and accessible games, they had no interest in making arcade games for the Triforce. Hits likeDonkey KongandMario Broswere eons ago and the market had drastically changed since then. Instead, Nintendo opted to license out their IPs to the more experienced arcade developers at Sega and Namco.

This partnership resulted in a golden opportunity for the two companies. Their experienced arcade developers had access to some extremely popular IPs, and the GameCube base meant they had a powerful core machine that was also affordable. In the end, though, the Triforce only hadninegames released for it and several of those saw home ports.

With so few titles released for the system, it affords us the rare opportunity go through each and every one. The games range from fairly typical arcade titles to high budget monstrosities that would be the crown jewel of any arcade. We'll be looking at obscure games, legendary games, and everything in between while doing our best to see how they took advantage of the Triforce hardware. Let's begin.

#### Mario Kart Arcade GPandMario Kart Arcade GP 2by Namco¶

Did you know that the Triforce has not one, buttwoMario Kart games?Mario Kart Arcade GP(2005) andMario Kart Arcade GP 2(2007) are often forgotten when people talk about the phenomenal Mario Kart series due to their limited release, especially internationally. Both games are built off theMario Kart: Double Dash!!engine, but have more of a focus on arcade simplicity and play closer to the style of the originalSuper Mario Kart.

Those that have played a Mario Kart game know what to expect at the surface level. This is an arcade kart racer with tons of wacky items, popular characters, and colorful tracks to race on. This time around, some popular characters from Namco properties join Mario Kart veterans, such as Pac-Man!

Cabinets are colorful, bright, and easy to play.
Image Credit:
NoNameHere
 on Wikimedia Commons (
CC BY-SA 4.0
)

The first game launched with twelve race tracks spread across six cups. Each cup has four stages that use two of the tracks. The second time you race a track in the cup, it will be remixed slightly. Sometimes this just means some different visuals or items, but other times it might have some slight alterations to make driving the track more difficult.

Usually the first race on each track layout will use a standard item set until the later cups.

During the second race on a track layout in a cup, the game will mix things up in some way to keep players on their toes.

Mario Kart Arcade GP 2has all of the tracks from the first game and four brand new ones spread out between two new cups. If this was a home console game, the amount of reused content would have been very disappointing. In the arcade setting, it's not nearly as big of a deal. Most players wouldn't have had a lot of experience on every course, and many might not have played the first game at all! That being said,Mario Kart Arcade GP 2still feels more like an improvedversion 2.0rather than a full fledged sequel.

On that note,Mario Kart Arcade GPhas some very puzzling omissions that were fixed by the sequel. For instance? OnlyMario Kart Arcade GP 2has the iconic 50cc, 100cc, and 150cc difficulty options available from the start! Both games have the same three gameplay modes: Grand Prix, Time Trial, and Versus. Grand Prix has players racing through cups one round at a time. By winning a race in a cup, you unlock the next race. Time Trial should be familiar to anyone. Players are given a triple mushroom and a solo run on a course to set the best time possible. Versus mode can only happen in multicabinet setups when multiple players are around. In this mode, up to four players can race one another on any track.

Regardless of mode, races have a time limit to keep people moving, but they are relaxed enough that they usually won't come into play.

In order to record progress,Mario Kart Arcade GPandMario Kart Arcade GP 2rely on magcards. When the game starts, it'll ask the player to insert or create a license profile to save their progress. On some cabinets, a camera (known as the "namcam2") will be present to take a picture that will be used during the race. Players' faces will show up in the heads-up display and with variousdistraction items, so making a goofy face could be an advantage in multiplayer. Note that these features are optional, and a player can always choose to play without taking a picture or using a magcard.

Dolphin head with Yoshi eyes is real, and if you find yourself in the wrong arcade, it might end up right behind you.

There is one rather egregious oversight that is only present in the first game.Mario Kart Arcade GPlocks a player to a single character once they've created a license card. That means before the player even gets a chance to play the game, they have to choose a character and are forced to use that character unless they start over! Characters have different driving characteristics, so this is a rather important decision!

Regardless, the developers must have realized how awkward this was and changed it so that swapping characters is possible inMario Kart Arcade GP 2even when using a magcard.

Whether the driving model for a Mario Kart game is good or not mostly comes down to player preference. Some players love Mario Kart DS, others swear byMario Kart Wii, or evenDouble Dash. The GP games are definitely on the slippery side of the series, especially when using the "difficult" characters at higher CCs.

Controls are simple even compared to the already casual home Mario Kart games. The game uses a racing wheel, gas and brake pedals, and an item button. Additionally, there's aVersus Cancelto opt out of multiplayer to focus on winning the cups. Despite this, it takes some time to get acclimated to the arcade exclusives after coming from modern Mario Kart games. The harder courses pull no punches and will relentlessly throw tight corners. The Grand Prix mode even has hindrances added to certain tracks on their reruns. On Bowser's Castle, Kamek invades and blocks some of the racing lines on the later laps!

Bowser's Castle's two tracks have nice straightaways when you first play them.

However, on the second playthrough, Kamek blocks off parts of the track while you're racing.

To win on harder difficulties, the player needs every advantage they can get. Items can be the advantage that players need. Both games featureover 100 items, but during a race, each player has access to a pool of three items. In harder Grand Prix cups (and sometimes later stages in earlier ones), players get the option to create their own unique item pool from their unlocked items. Even though a lot of them share properties, a surprising number of them have their own wrinkles. For example, dropping a banana can cause a spinout and immediate time loss, but dropping tacks will cause a kart to pop a tire and lean to one side, making overall driving temporarily more difficult for that player. Items aren't very balanced so unlocking powerful items gives an undeniable edge.

Throwing items are simple. Aside from the green shell, almost all forward throwing items feature a powerful lock-on effect. Lock-on is automatic and happens after keeping another driver in front for a couple of seconds. Once locked on, that item will head toward the target regardless of what they do to avoid it.

The game teases players with a huge item select screen, though most are locked off at first.

Don't want to miss out on a useful item? Plunk in more quarters and win the next race!

In the first game, players must win all four stages of a cup and the minigame that follows. These minigames are short solo challenges that test a player's control over the game in unusual situations. Sometimes this means pushing an object, getting big air over jumps, driving backwards, hitting tons of pedestrians (they're Koopa Troopas, that makes it OK), or even facing off with Bowser outside of his castle. In the sequel, the bonus games are no longer required for cup completion and only award bonus coins.

Push the giant watermelon into the pen to unlock one of Mario's signature items in
Mario Kart Arcade GP
: the Invincibility Star!

By winning all of the cups, players unlock aSpecialmode that varies per game. In GP 1, that is 150cc mode.Mario Kart Arcade GP 2has 150cc mode unlocked by default, so they went a different direction. Instead, players unlock new track layouts inreverse mode. Unlike themirror modepresent in other games, reverse mode significantly changes some of the tracks beyond just ruining muscle memory. Fun fact, reverse modewasalso planned forMario Kart: Double Dash!!before being cut for mirror mode.

To handle the plethora of tricky corners and tracks, GP games have a drifting mechanic. By tapping the brake, players can initiate a hop. By turning in the air before landing, players can initiate a drift that allows sharp corners to be taken at higher speeds. Because of the powerful lock-on that most items have, drifting has been given an additional benefit. During a drift, players willreflectmost items with a shield. An unexpected drift will cost some time, but could be used to block an item at the last moment. Some items also provide a shield, such as theInvincibility StarandShielditems.

Much like the originalSuper Mario Kartand more recent Mario Kart entries, the GP games have coins strewn across the track. Collecting coins increases a kart's stop speed, adding a layer of strategy as just driving the optimal lines isn't enough. During a race, holding 15 coins pushes a kart to its maximum speed. But driving at that speed can also be dangerous, as hitting walls, bouncing off other karts, or being hit by items can cause the player to lose coins.

Mario Kart Arcade GP 2changes all of the coins on the track toMario Coins. The first time these coins are collected they count as currency toward unlocks. If coins are dropped, players don't lose the Mario Coins and they will respawn as golden coins. Up to 25 Mario Coins can be picked up on the track along with bonuses from race ranking and minigames.

Collecting Mario Coins allows for unlocking certain karts, items, portraits, andkart upgradesthat will make the veteran players much faster than players just starting out.

In
Mario Kart Arcade GP 2
, minigames now just give bonus Mario Coins and are no longer required to complete a cup.

Lastly,Mario Kart Arcade GP 2also adds one more major feature:Waluigi!a "live" announcer that gives updates throughout the race. This feature is proudly demonstrated during the attract menu, even! As corny as it sounds, it's rather entertaining to leave on at least a few times. Players that don't want the announcer can turn it off and their preference will be saved to their magcard.

Overall, both of these games are best as multiplayer arcade spectacles. The depth and content of these games don't quite rival contemporary home releases likeMario Kart Wii. But none of that matters in the arcade with friends, where loud and bombastic multiplayer experiences really shine.

The Mario Kart Arcade GP series would continue withMario Kart Arcade GP DXin 2013 andMario Kart Arcade GP VRin 2017, but those would run on newer and more standard PC-based arcade hardware.

These Mario Kart titles were the only two games Namco released on the Triforce hardware. But they had plannedat leastone other game.

#### Star Fox(working title, unreleased) by Namco¶

Announced in 2002 as a dual GameCube and arcade release, Star Fox was originally planned to launch before either of the Mario Kart Arcade GP games in 2003. As part of a push for games that could easily be ported between GameCube and arcade, Star Fox would have had connectivity between the two versions throughGameCube memory card slotsincluded on the machines. That way, players could bring their own memory cards to transfer progress and/or unlockables between the home version and the arcade version of the game.

Image Credit:
Nintendo

Considering the arcade style action featured in Star Fox and Star Fox 64, this seemed like a natural choice for an arcade hit. Players were already chasing high scores in Star Fox 64 and the overall game design would need little modification to work in an arcade. If rumors were true, Namco wasn't planning to skimp on the hardware, either. They were going to use the massively impressive and incredibly expensiveO.R.B.S. cabinet, which was designed specifically for on-rail shooters. Essentially, the player would be locked in a fully immersive orb that would place them squarely in the cockpit of an Arwing with a semi-spherical screen acting as a bubble canopy. On top of that, the cabinet could rotate and slide to reflect what was going on in-game.

Image Credit:
Bandai Namco

Unfortunately, Star Fox Arcadewas quietly cancelledand the O.R.B.S. cabinet itself would never actually be used for any arcade game. The GameCube version dideventuallysee the light of day, however. Released asStar Fox Assaultin2005, the game was heavily reworked and padded out with third person on foot sections. Perhaps as a nod to its origins, players can unlock a port of the arcade classicXeviousby collecting all silver medals.

With that side quest complete, we've now covered the entirety of Namco's contributions to the Triforce library. Thankfully, we're not done yet, as Sega developed a variety of Triforce arcade games.

#### Gekitou Pro YakyuubyWOW Entertainment¶

Gekitou Pro Yakyuuis a rather unique baseball game that combines characters from various baseball manga created byShinji Mizushimawith real-life Japanese professional baseball players of the era. The game also has a faithful home console port,Gekitou Pro Yakyuu, for the GameCube and PlayStation 2.

The main draw of this baseball game is that it can provide a faithful simulation style game between professional players or a zany arcade experience with special pitches, strong batters, and manga cutaways featuring the illustrated characters. What makes the game so interesting is that these two things aren't separated - both teams can be filled with a mix of illustrated and professional players, letting their contrasting styles clash right on the field.

When manga characters face off, players are treated to short, but amusing cutscenes.

Cel-shaded characters pop out against the more realistic professional players.

At its core,Gekitou Pro Yakyuuis a fairly standard late early 2000s baseball game. Pitchers can roughly place their pitches anywhere in and around the strike zone and batters in turn try to guess where the pitch will be to get a solid hit. Pitchers have a variety of pitches at their disposal that add movement to the ball, and batters in turn have multiple swing types that can counter pitches. Players with better stats generally have more options at their disposal. If the batter guesses the pitch right, their aiming reticle will turn red giving them advanced warning that they guessed correctly.

When playing in the arcade, both teams are filled with a mix of real players and manga players. This creates the interesting scenario where many manga players often feel likesuperstarsthat can break the game if not carefully played around. Most of them have special quirks and often have access to special abilities. Manga pitchers can make the ball disappear, zig zag, and confound the batter. Manga batters can also counter this as they have active and passive abilities of their own. One player has his contact range and power grow further out from the center of the strike zone, making him incredibly powerful if the pitcher is painting the corners.

The manga pitchers are tough to beat with their crazy pitches.

For those interested in playing this game without a Triforce, there's good news. The home console port is incredibly faithful and even adds some additional modes and features for depth. The GameCube controller also affords players analog control, whereas the arcade original uses an eight-way gate. Once you get in game, though, it's very apparent that this is the same game.

Set
blood type
 and more in the surprisingly robust player creation tool. This feature is exclusive to the home console versions.

The home port, as far as we could tell, is missingone small thing. The Triforce version has a scoring system for putting up high scores on the machine. Rather than just trying to win baseball games, players are instead challenged to get a high score across a nine-inning game. Doing positive things like getting hits and getting the opponent out will give the player points. Big moments like double plays and grand slams will give even bigger bonuses, pushing players to the top of the leaderboards.

Players get two innings per credit or can pay 4 credits for a full nine-inning game. Players aiming for a high scoreneedto do that, as those extra innings give more opportunities for scoring points, and there's a large swath of bonus points for winning the baseball game outright. After nine-innings, win or lose, the game ends. The game also lists high scores for a home run contest, but we couldn't figure out how to get to that mode.

Harkening back to older arcade titles, high scores are the name of the game.

This game suggests that it has some kind of save card support in the Service Menu, but we weren't able to find any cards for it to be sure. In all likelihood, cards would have been used to save team data and other preferences for a player. Overall,Gekitou Pro Yakyuuis an effective, if not somewhat simple baseball game that lends itself well to the pick up and play nature of the arcade.

#### Virtua Striker 3 ver. 2002byAmusement Vision¶

While it was developed by a different team within Sega,Virtua Striker 3 ver. 2002is very similar toGekito Pro Yakyuuin some ways. It is a simple to pick up and easy to play sports game with an incredibly faithful home port that brings the same experience to console players with modes that add extra depth.Virtua Striker 3 ver. 2002is a three-button game: short pass (tackle on defense), long pass, and shoot. That's it.

Yep, it's a soccer game.

It's not uncommon for a cluster of players to bounce the ball off one another over and over again.

Thegooooooalof the game is to win five matches in a row against the AI to secure the championship while surviving potential intruders jumping in from the second player in standard mode. This is aking of the hillstyle arcade game, so whoever wins gets to keep playing while the loser is knocked out. This remains true when playing against AI, so a strong player can play up to five games against the AI before reaching the credits and having to put in more money.

The game follows the rules offootballsoccer closely. There are yellow cards, red cards, offsides, corner kicks, penalty kicks, free kicks and injury time. As an arcade game, it even captures some of the pageantry of the sport with a bombastic opening as the players march onto the field. However, once you're in game it is a very no frills experience.

The arcade operator could adjust the cabinet's settings to make things more or less unfair to optimize their profits. In addition to difficulty settings, Golden Goal (short overtime period) and Penalty Kicks could be disabled to give the players less opportunities to break a tie. And this matters a lot, becausethe AI wins in the event of a tie, forcing the player to plunk in more money to continue.

For competitive events and tournaments, there's an aptly namedtournament modepresent in the settings. This mode has both players kicked off the game after match, regardless of who wins. This mode wasn't (just) added to allow the operator to maximize profits, but rather it was intended for holding in-person tournaments where players would be swapping in and out after every match.

The simplicity to the controls is both the game's selling point and an annoyance. When on defense in particular, sometimes the defender will rush to get into a particular position regardless of the direction being held on the arcade stick. This lack of control is only worsened by the fact that there's no switch player button... on the arcade version, at least. The home port is mostly faithful gameplay-wise, but it does take advantage of the extra buttons on the controller to give players the ability to change tactics and swap defenders.

The GameCube version has more modes on top of the same core gameplay.

One thing that we should mention is that we were playing on revision 0001 ofVirtua Striker 3 ver. 2002. Most games on the Triforce have multiple revisions or updates, with some revisions coming with significant upgrades. Later revisions may have addressed problems in this revisions, especially if the supposedType 3version exists.

Virtua Striker 3 ver. 2002was a tad underwhelming in our opinion. If you're a huge fan of these games and are seething at our mini-review, we're fully aware that a lot of our frustrations might simply boil down to askill issue. But since we were familiar with the rich history of the veterans atAmusement Visionand their legendary track record of arcade games, this one was a little disappointing.

#### The Key of Avalon: The Wizard Master,The Key of Avalon 2: Eutaxy Commandment, and their subversions byHitmaker (Sega AM3)¶

Originally released in 2003,The Key of Avalon: The Wizard Masteris a strange and very,veryexpensive arcade game. This game was not just expensive for the players, but it was also expensive for the operator too! This game is powered byfiveTriforce cabinets: one central Triforce server for the main game screen, and four additional satellite Triforce pedestals for the players.

The Key of Avalon: The Wizard Masteris an arcade trading card board game. The objective of the game is simple - players scan in their decks and see their monsters on the big screen while battling up to three other players for supremacy.

Before playing the game, players need to purchase a starter deck of 30 random trading cards. This deck also comes with an IC card so that players can save their progress. Each satellite Triforce comes with a deck reader to allow a player to scan in their deck of cards. But how would you control the game after scanning in your cards? Why, atouchscreen, of course! And if that wasn't enough, the game also came with a separate card kiosk specifically for purchasing starter decks and booster packs.

The Key of Avalon arcade setup stands out among typical arcade machines.

There are at least six revisions of The Key of Avalon. It is important to be aware of what revision a cabinet is, as cards from newer sets will not work with older revisions. Thankfully, cards are marked with what set they came from, making it fairly easy to know which revisions each card is compatible with.

* The Key of Avalon: The Wizard Master- Supports the initial 100 cards. There is a 1.10 revision with small adjustments.
* The Key of Avalon 1.20: Summon The New Monsters:This firstmajorupdate adds support for 52 new cards in theNseries. Earlier prints of these cards may have different stats and are missing some information on the back of the card.

The later cards have colored diamonds under the name on the back (the three blue diamonds in the upper right). The stats didn't change on this one.

* The Key of Avalon 1.30: Chaotic Sabbat:This version adds support for 35 more cards in theCseries. Much like Summon The New Monsters, reprints of these cards have additional information and may have slightly different stats.
* The Key of Avalon 2: Eutaxy Commandment:An update big enough to be called a sequel. It has 61 new cards, a single player mode, and much more. The cards for this revision are in theEseries. These cards do not appear to have any changes between early and late prints. The updated stats for older cards are used by this game.
* The Key of Avalon 2.5: War of the Key:The final revision adds support for 40 new cards in theWseries. There are also additionalLegendcards separate from the main catalogue.

In the end, nearly 300 total cards were released spread out over five rarities: Common, Uncommon, Rare, Very Rare, and Super Rare. Some cards are undoubtedly stronger than others, and those cards are mostly the rarer ones.

Like other collectable card games, players were expected to buy packs and trade with others to build the best possible deck. To prevent someone from getting clever with a printer and suddenly owning all the rare cards, Avalon cards have a barcode embedded into their top edge that the game reads the card data from. Though nearly invisible in normal circumstances, if held up to a lightjust right, the material of the barcode stands out against the rest of the card.

It's blurry, but there's a clear difference in shine at the top of the cards.

Cards weren't all about utility, though. These cards were beautifully illustrated by a myriad of artists, and each monster is represented by a detailed 3D model in game. If someone was lucky, they might've stumbled upon alternate art or holofoil versions of cards. Players could also be rewarded with uniqueExcards that wereonlydistributed through events.

A normal Rare card, holofoil Rare card, and holofoil Very Rare card side by side. The Very Rare card has more holofoil to it, making it look fancier.

Of all of the Triforce games, this was the only one we couldn't play. Even if we had five Triforces, five GD-ROM drives, and JVS I/O emulation for the cards, it still wouldn't be enough. The game can be booted with fewer Triforces, but the touchscreen is a total mystery and there was no way to bypass it without having a working Avalon Satellite Pedestal.

The Key of Avalon: An expensive and cumbersome, yet unique experience for literally everyone involved.

The main monitor, satellite touchscreens, and separate card dispenser must have made for an incredible arcade experience back in the day.

We've researched the game, bought manuals, and obtained a ton of cards and understand the gameflow, but without having played it we can't really say if it's fun or not. However, based onexisting sales dataand the number of updates, we know thatThe Key of Avalonwas moderately successful despite its high price. Sega would go on to make more trading card arcade games, including a suspiciously similar Chihiro game,Quest of D.

#### Virtua Striker 4andVirtua Striker 4 ver.2006byAmusement Vision¶

Two years afterVirtua Striker 3 ver. 2002, Sega released the next game in the Virtua Striker lineup withVirtua Striker 4. With dramatic upgrades to the controls, support for saving progress, team configuration, rank, and more, this game is often considered the best in the series by fans. And it only got better withVirtua Striker 4 ver.2006, which updated the rosters and added additional online events.

The new tactics bar and dash button are shown in the owner's manual

An example of the control layout on a full size cabinet.
Image Credit:
Launchbox

Like most Triforce games, the newer Virtua Striker games take advantage of cards for saving.Virtua Striker 4uses IC cards to track player progress, similar toThe Key of Avalon. These cards are nifty, as not only are they more durable than magcards, but they also contain an ID for logging in toSega ALL.Net. The internet was enough of a thing at this point that Sega started experimenting with it for tracking player data and progress.

Virtua Striker 4 cards can register players online for the Sega ALL.Net service.

This meant that instead of a local arcade leaderboard,Virtua Striker 4could have a global leaderboard tracking players on ALL.Net-connected machines across the world. By playing against other players that had registered online, players could be promoted to higher ranks or be demoted to lower ranks. On the surface, this is an upgrade over traditional magcards, but the obvious downside is that these games rely on servers hosted by Sega. Unfortunately, support for these machines ended in 2017, meaning that the online features no longer work. Thankfully, these games can still be played offline without the online services, albeit without the special features and events.

Virtua Striker 4was a revelation to play after the previous games. The changes are subtle, but they come together to provide a far superior experience. The ability to dash gives players much more control over attacking at the expense of stamina, and helps avoid the common problem inVirtua Striker 3where athletes were constantly just banging into each other in a scrum. Thechange tacticsbuttons add depth as players can adjust their strategy on the fly instead of waiting for halftime. This gives the opportunity to go for that golden goal in the final seconds or play defensively to hold a tight lead.

Instead of being locked to an eight-way gate, this game uses a full analog lever that allows for more precise control. Player movement is still a little stiff, but it makes a world of difference when it comes to the accuracy of shots and passes.

Accurately passing to the open man and dashing past defenders leads to one-on-one situations with the goaltender.

Much like Virtua Striker 3 ver. 2002, players need to win five matches to beat the game.

For most fans of the series,Virtua Striker 4 ver.2006is the definitive version in the series, and we can see why. Unfortunately, it is also the last game in the series and it never saw a home console port.

#### F-Zero AXbyAmusement Vision¶

If there was a crown jewel of the Triforce efforts, it has to beF-Zero AXand the home console game born from it,F-Zero GX. Without Nintendo collaborating with Sega, there's no way that the legendary arcade racing devs atAmusement Visionwould have had the chance to work with the F-Zero license.

For those out of the loop,F-Zero GXis renowned as one of the greatest arcade-style racing games ever made. It has tight controls, an incredible sense of speed, and legendary difficulty. The racing alone would make for a great game, but the developers went above and beyond with tons of content to elevate the experience. It has tons of characters with their own 3D models, F-Zero machines, and even theme songs accompanying their profiles. The garage functionality also gives players the ability to create their own vehicles with a custom appearance and stats. Topping all of that off is an iconic and difficult story mode full of goofy FMV cutscenes oozing cheesy goodness. And for those who never had a chance to play thearcade-exclusivetracks, the arcade tracks can actually be unlocked inF-Zero GX!

So that's it then?F-Zero GXhas everything the arcade could offer and more. There's no reason to care aboutF-Zero AX, right?Wrong.

When it says buckle up, it isn't joking. (You actually have to buckle the seat belt before it will let you start the game.)
Image Credit:
gztomy.com

F-Zero AXis still an incredible experience even for those that have completely masteredF-Zero GX. The controls and physics have been adjusted to make the game play better on a force feedback yoke and pedals. The change in controls allows players topushthe vehicle in ways that are lost in the home console version. And, if you're lucky enough to find a deluxe cabinet, the intensity is ramped up further with pilot seat haptics - it can tilt to throw the player around corners.

The game is a visceral thrill. Everything great about the racing inF-Zero GXis here, just with the intensity cranked up to another level. Unfortunately, it only has six tracks, with one of them being a fairly simple oval for learning the game. The other tracks are fantastic visual showcases with devious layouts. The long ice slide at the end of Green Plant: Spiral pushes players to go fast as they can with no traction, while the back-to-back right angle turns and thin straightaways force precision driving on Lighting: Thunder Road.

There are only two modes in this game: Race and Time Trial. Race has players going up against 29 other AI opponents or three other players if playing against linked cabinets. Time Trial is exactly what it sounds like and has players racing for the best time in a solo effort. Best records could be uploaded online with a code, back in the day.

Only having a selection of six tracks is disappointing, but at least the tracks are memorable and challenging with their own unique identities.

Hidden away in the Service Menu, there are five difficulty modes to help the operator tune the experience according to the clients. In a more casual arcade, the game's difficulty could be lowered toVery Easyto give players more time to make mistakes and still win. If they wanted people to suffer,Hardestall but guarantees no one will ever win. The length of the races can also be adjusted. Even a standard three lap race can be exhausting on a cabinet, so cranking up the length can really turn the game into an endurance challenge.

Players don't get a free race by winning. Higher difficulties mostly exist out of cruelty toward the player.

On the track,F-Zero AXlooks likeF-Zero GX. But after having the opportunity to play them back to back, the differences in how they drive became very apparent. Even ignoring the arcade atmosphere, AX gives the sensation of always being one mistake from careening out of control. After playing a lot ofF-Zero AXand returning to GX, the change in feel was shocking. Treacherous turns in AX were suddenly ordinary in GX thanks what feels like higher grip and different drifting physics. The cars felt like they were glued to the track in the console version!

After spending a lot of time with both, AX definitely presents a more difficult, but rewarding to master, driving model. The arcade gamedoesgrant players some reprieve though. Running out of energy or flying off the track will happen now and then even to the most experienced players. This isnotan immediate race over! Instead players will be respawned back on the track after a small time penalty. It dampens the hopes of victory, but it's usually possible to come back from one major mistake. However, unlike the console version, players are on a strict time limit by default. Once the clock hits zero, the race is over regardless of whether the player is in first or last place.

F-Zero AX can match and even surpass F-Zero GX's legendary speed and difficulty.

Winning races earns you a victory lap similar to F-Zero X, this time with a vocal track backing it and a podium ceremony. No interviews with the pilot, though!

Both magcards and GameCube memory cards can be used to save progress. Players are assigned a license rating that can be upgraded by winning races and earning points. Every 30,000 points, players are afforded an opportunity to buy upgrades for their own custom F-Zero Machine. This machine could be used directly inF-Zero AXor transferred toF-Zero GXvia memory card.

To beatF-Zero AX, players have to win all six races and all six target times. While doing this, players earn points that upgrade their license's rank, which allows them access to better parts for their custom F-Zero machine.

After experiencing it first hand, we can say that the game is a truly incredible arcade experience. If not forF-Zero GX, it would be a modern tragedy that it didn't see a wider release. Still, those who love the F-Zero series should definitely give this version of the game a spin if they have the chance.

#### Monster Ride¶

Image Credit:Sega Retro

It would be a crime if we didn't at least mentionMonster Ride.

F-Zero AX: Monster Rideis a separate release of F-Zero AX and the only Sega-produced Triforce game that uses a NAND cartridge. It has fewer features, pilots, and ships than the standard version of F-Zero AX, and doesn't seem to have multiplayer or any save support whatsoever.

But in exchange, Monster Ride runs in aCycraftcabinet.

Imagine playing F-Zero AX inside a five degrees of freedommotion simulatorwhere the player's cockpit is suspended in the air with an arm, and the cabinet literally swings the cockpit around to match the ship's movement in game. That's Monster Ride, and it's as awesome as it sounds. Unfortunately, these cabinets areincrediblyrare and appear to have never left Japan. We invite readers to watch this clip showing it off, as this is as close as most of us will ever get to the real thing.

Footage of the Cycraft-powered F-Zero AX Monster Ride in action.

In most cases, something this obscure would be lost to time. But, luckily enough, a few Monster Ride Triforces have survived over the years. And thanks toCycraft emulation, Monster Ride can technically be run from a standard Type 3 NAND Triforce. Maybe some day all of this could be hooked up to a homemade Cycraft-compatible motion simulator and Monster Ride will live again. We can dream, right?

If you ever build a motion simulator for F-Zero AX Monster Ride,
please
 let us know.

### In Retrospect¶

After having played each and every Triforce game to the best of our ability, it's easy to see why the platform is still beloved by its fans. Unfortunately, it was a victim of its era and most games only released in Japan. The games that did get international releases were only released in limited quantities.

As developers of a GameCube and Wii emulator, the Triforce is an especially interesting topic for us. At the core of every Triforce is a GameCube, yet that familiar hardware was used to drive a different type of experience in the arcades. It's fascinating! For this article, we wanted to shine a spotlight on this interesting step-sibling to the consoles we emulate.

Unfortunately, when it comes to emulation, arcade hardware is a very, very different challenge than emulating a home console. Even though each game is powered by a Triforce, all of the hardware around it can be unique for each game and even behave differently on different revisions of the same game! An arcade cabinet only needs to be compatible with the specific game inside of it. Because of that, unlike GameCube/Wii emulation, where fixing one game can sometimes fix dozens of others, each individualrevisionof an arcade game needs to be treated as its own challenge.

Those problems didn't stop people from trying to build Triforce emulation on top of Dolphin in the past, though!Over 17 years ago,Dolphin gained the ability to emulate parts of the Triforce Baseboard. It wasn't enough to boot any Triforce games, but it was a start. However, that was the last time anything Triforce-related hit our mainline builds. Aside from code clean up efforts, the fledgling Baseboard emulation was left untoucheduntil it was removed in the summer of 2016to avoid misleading users into thinking that mainline Dolphin targeted Triforce hardware.

Just because Triforce emulation wasn't progressing in the main builds doesn't mean it wasn't being pursued, though. Instead, efforts were moved to a dedicatedTriforce branch, where developers could do whatever they wanted to improve Triforce emulation. And there was some success from this approach - it was eventually able to play a few games, such asMario Kart Arcade GP 1and2.

This video showcases
Mario Kart Arcade GP
 running in the Triforce branch over ten years ago!

However, a lot of this progress was achieved throughbrute force. Because so little was understood about how the Triforce worked, manysuboptimaltechniques were used to get results fast, like hacking problematic behaviors out of games and hardcoding responses. This, combined with some magic to force each game's controls to work with a standard GameCube controller, was enough to get some games running.

All of these patches were required to boot
Mario Kart Arcade GP 2
 in the Triforce branch.

This was fine for a separate branch. Hacky emulation is sometimes a necessary first step to more accurate emulation, after all. But on the other hand, the hacky nature of the Triforce branch made it unacceptable to be merged into mainline builds as-is, despite its achievements. Unfortunately, the emulation quality never improved and progress stalled out. The Triforce branch was abandoned after just two years of sporadic contributions, and it eventually faded into obscurity.

Builds for the Triforce branch can still be found in a deep crevice of our website to this day.

Any attempt at Triforce emulation today must be held to a higher standard. It wouldn't need to be perfect at first, but the goal should be to actuallyemulateTriforce hardware, rather than to ignore that it exists. We should strive to give retro and arcade enthusiasts the tools to bring Triforce games to life with their own custom solutions for the platform's assortment of obscure hardware. In a perfect world, Dolphin would be capable enough to be the core of hobbyist arcade cabinets.

Each Triforce game brings difficult questions that Dolphin just isn't well suited to answer. Dolphin is a console emulator at heart and is not designed to tackle the hyper-specific challenges that come with arcade emulation. We already have enough problems trying to emulate all the weirdWii Remote attachmentsandUSB devicesout there! To do right by the Triforce would take an inordinate amount of work and expertise. And embarking on that journey for what amounts to a handful of games, many of which already saw very faithful home ports, would be a foolish endeavor at best.

Having said all of that, we're just as surprised as you to be announcing this...

### The Return of the Triforce¶

As ofDolphin 2512-395, Triforce support is here!Readers that have been paying close attention might have noticed that some of the screenshots in this article are suspiciously high resolution. There's a reason for that!Every single in-game screenshot in this article comes from Dolphin!

F-Zero AX
 couldn't run in the old Triforce branch. But now it can run in Dolphin!

This is the culmination of over a decade of work. While were focused on advancing GameCube and Wii emulation,crediardoubled down and continued maintaining his own forkspecifically forTriforce emulation. We were aware of this fork, but given the fact that we knew little about how the Triforce worked and had bad memories of the old, hacky Triforce branch, it mostly flew under our radar.

Everything changed mid-2025 whencrediarcontacted us about potentially making a pull request to get his Triforce emulation code into our official builds. Developers had a mixture of both excitement and concern upon hearing about this. It would be a major project, andcrediar's solo work would now be scrutinized by a bunch of people.

In the end, what won us over was the quality of emulation. The games ran beautifully, and apart from missing touchscreen support for The Key of Avalon, each game was playable. The hacky, messy Triforce emulation we remembered was gone, and something much better had taken its place.

So, we wanted Triforce emulation in Dolphin, andcrediarwanted to bring it into Dolphin. Their pull request was an easy merge, right? Well, there was still one big hurdle in the way:code review.

Reviewing, integrating, and testing the Triforce code was a mammoth task, even with crediar solving the core emulation.

Because the Triforce has a significant amount of bespoke hardware, none of the developers reviewing the code knew much about how it worked. We were put into a tough spot of having to review a large volume of code that emulated unfamiliar devices. The Triforce was mostly a black box to us at the beginning of this effort, and it still is in many ways.

To get Triforce emulation to the finish line, we had to work together and makea lotof compromises. We did not want to let perfect be the enemy of good, but it still had to be good enough to not hinder further development.Billiardandsepalanigave huge assists with their own fixes and clean ups to help get the Triforce pull request ready for action. Many of our targeted clean ups focused on fixingmemory safetybugs, removing potential game hangs, and improving the overall user experience by adding safeguards and streamlining the process of configuring Dolphin to run Triforce games. After many months of review, cleanups, and testing within the team and the community, Triforce emulation is finally here. And it is here to stay.

Throughout this process,crediarhas been helping us with his knowledge on the Triforce for various guides and information. He also assisted us with dumping Triforce games and provided a homebrew payload that can dump Triforce games directly over the network. It is also possible to dump GD-ROM titles without any Triforce hardware by using a PC disc drive, but it is a more complicated process and takes several steps in order to retrieve the game from the disc.

For full instructions on how to dump Triforce games, please visitthe game dumping guide on our wiki.

#### Setting up Dolphin for Triforce Emulation¶

The Triforce is ultimately a GameCube with arcade bits attached to it. Much like how Dolphin can automatically reconfigure itself depending on if you're booting a GameCube or Wii game, Dolphin will now become aTriforcewhen it detects a Triforce game being loaded. However, the Triforce Baseboard options can also be manually enabled for homebrew purposes, and there are some important settings in its configuration menus.

The Triforce Baseboard can be found as a SP1 device in Options -> Configuration -> GameCube. It has additional configuration options for various IP address redirects, which can make it easier to set up networking features of the Triforce. There's also a shortcut here to configure Triforce controls, which can also be found as a GameCube Controller Input device in Options -> Controller Settings.

Each game's arcade controls have already been roughly adapted to a GameCube controller, but be sure to configure the Coin, Service, and Test buttons! Controller port 2 can optionally be set to a baseboard as well, but Dolphin will automatically translate controls when possible without this being necessary. These are the only two places where Triforce settings need to be adjusted in Dolphin. Note that standard GameCube/Wii games should not be booted with the Baseboard set in SP1 or as a controller.

Because the Baseboard is attached to the GameCube, it has to be set in SP1.

It also handles controls, so be sure to set the Baseboard in the GameCube controller slots, too. Some games will use multiple ports for multiplayer and coin slots.

One other important component of the Triforce isSegaboot. Without Segaboot, players can't access the Service Menu and the game's settings. This means not being able to enable free play, change difficulties, calibrate controllers, and much more. Additionally, the full boot process can only be experienced by providing a Triforce IPLandSegaboot combined with "Skip Main Menu". Just be prepared for a few error popups along the way as some parts of initialization are not fully emulated.

Segaboot can be found on certain Triforce update discs or inVirtua Striker 4andVirtua Striker 4 ver.2006's files. You can use Dolphin's filesystem explorer to locate the "firm" folder that holds Segaboot files. The correct file is 2MB, and in the case ofVirtua Striker 4 ver.2006, it is namedsegaboot.img01. Renaming this filesegaboot.gcmand placing it in theTriforcedirectory inside of the User folder will allow Dolphin to use it.

Segaboot is cross-compatible with different games, so once you have it, you can access every game's Service Menu.

Some games usenetworkingfor certain hardware, such asF-Zero AX Monster Ride's Cycraft andMario Kart Arcade GP 1/2's namcam2. In both cases, a third-party server that emulates the behavior of the original device can be used with Dolphin. By default, Dolphin includes an IP Redirect to make the game look at localhost for these devices.

Conveniences such as save states are not yet available as Triforce emulation isn't fully integrated with all of Dolphin's features. This part of the article was originally a much longer "Limitations" section with a big list of warnings, shortcomings and potential problems for users, but some cheeky developers decided to go through and fix most of them after reading through the section. At this point, the biggest omissions are NetPlay and TASing support only because the new Triforce input devices aren't supported by input recordings.

Even Android users get to join in on the fun! Triforce hardware can be enabled and configured in the Android GUI like on desktop and games will run out of the box. The only limitation is that the Coin, Test, and Service buttons have not been added to Dolphin's touchscreen controller, so users will have to map them to a real controller or a physical button on the device. One exception to this is inserting a coin, which has been mapped by default to shaking your device.

You can shake your phone to insert coins!

Regardless of whether you're playing on PC or Android, some parts of the Triforce experience are still hardcoded. The attached JVS I/O devices for each game cannot be customized or changed in any way. This is not particularly accurate, as real cabinets could be configured in multiple ways, with some having deluxe features not present on others. This was a compromise, and we hope to make hardware features customizable in the future. Dolphin also automatically generates a magcard or IC card for each game and tracks progress on it, but users cannot swap cards, eject cards, or interact with them in any way whatsoever through Dolphin's GUI.

#### Emulating Arcade Multiplayer¶

Lastly, there is multiplayer support to talk about. Multiplayer was an important part of the arcade experience, and every Triforce game supports multiple players in some form. Single machine multiplayer should work without issues. This means thatVirtua Striker 3 ver. 2002,Virtua Striker 4,Virtua Striker 4 ver.2006, andGekitou Pro Yakyuuwill all "just work".

Then there are themulticabinetgames.The Key of Avalongames,F-Zero AX,Mario Kart Arcade GPandMario Kart Arcade GP 2all had support for up to through using separate cabinets connected to a LAN (Local Area Network). Prior to these efforts,crediarhad actually implemented some networking and socket features as part of emulating the monstrosity that isThe Key of Avalon. Multicabinet isrequiredfor the Avalon games, even for single player, as they use a server/client model with each player on a client Triforce and the master Triforce hosting the game server. Unfortunately, due to missing touchscreen support, they still aren't playable even when the instances are able to connect with each other.

F-Zero AXwas on the opposite side of the spectrum and never showed any signs of life. The game would just get stuck on searching for other instances forever. We unfortunately can't figure out the problem right now, as we don't have any packet dumps from real networkedF-Zero AXcabinets.

Mario Kart Arcade GPandMario Kart Arcade GP 2were the tragic pair throughout the review process. These games could actually see other instances of Dolphin on the network for a brief moment before they gave up and reverted to single cabinet mode.

In the days leading up to this article's release,Billiardandsepalanispent someverylate nights cleaning up parts of the networking code and hunting down regressions from those clean ups. The namcam2 for the Mario Kart games communicates via LAN on real hardware, and was particularly problematic during the clean up process. This was something thatcrediaralready had working, so wereallydidn't want to break it.

Fortunately, testing the namcam2 only takes a couple of seconds. The game checks for it on boot during the initial hardware checks. But waiting for new builds to try would usually take anywhere from 10 minutes to multiple hours. During that waiting period, one of the few testers with access to Triforce software had to be at the ready to test things or else everything would get delayed. This led to a lot of downtime with bored testers messing with Triforce games to pass the time. It was during one of those downtimes that a tester reported that some of the attempts to fix the namcam2 were affecting multicabinet support, as multiple instances of Dolphin could no longer find each other in Mario Kart! Even though the effect was negative, it was still interesting and prompted more investigation.

After we properly fixed namcam2 support, curiosity got the best of us and we continued tinkering with various Mediaboard network commands hoping to get multicabinet working in time for launch. It seemed hopeless at times, but after multiple nights of burning the midnight oil... this happened.

"Oh boy, I wonder who I'm playing with?"

The nightmare has become reality.

At the 11th hour, we were finally able to get multiple instances of Dolphin runningMario Kart Arcade GP 2to connect to each other.Mario Kart Arcade GPwasn't as easy and threw out "unhandled mediaboard command" errors despite the instances seeing one another. Thankfully, one look at the error andcrediarknew exactly how to fix it. Minutes later,Mario Kart Arcade GPwas working just as well as its sequel. Both games now work incredibly well and are able to survive Wi-Fi latency spikes of over 80ms with little hitching and no disconnects.

We plan to write a full multicabinet emulation guide on our wiki after this article launches. Please stay tuned.

### Triforce Emulation Roadmap¶

This isn't the hacked-up Triforce emulation of 2012, but there's still a lot of work to be done. Throughout testing, a ton of features were added and many issues were addressed, but work is far from done. In order to get this massive project merged, some items on our wishlist had to be put off for later. He's a rundown of some of the bigger things we really want.

* Better IC/Magnetic Card Interface:Currently, Dolphin automatically inserts a card that matches the current game ID in supported titles. This lets players easily play games and save without any extra setup. While this is nice, it isn't always what a player wants. We want to add the ability to buy, eject, swap, and insert cards like players could do at a real arcade.
* Custom Cabinet Configurations:Each game has its own hardcoded set of JVS I/O devices at the moment. While this means that games will always boot up with a valid configuration, it also means that alternative configurations can't easily tested, such as a cabinet without a magcard reader.
* Make The Key of Avalon Games Playable:These games are monsters to emulate, thanks to their specialized hardware. Even with multicabinet support working, there is still so much more to be done before Dolphin can bring this arcade experience home. The biggest fires to put out are the lack of touchscreen emulation and limited support for deck scanning.
* Support for Force Feedback Hardware:There are many bits and pieces on various Triforce cabinets that Dolphin can't currently handle. For example, force feedback motors are not generally supported. OnlyF-Zero AX's steering wheel motors can be mapped at all, but even if you do map them, some forces are incorrectly interpreted.
* Improved Controller Configuration GUI:The Triforce Baseboard SI device reuses the GameCube controller configuration GUI and adapts that to each game as best as it can. In the long term, we want players to see each game's control devices and their layouts so that they can configure a controller without having to guess what each input does.
* Hook up TAS Tools and NetPlay: Dolphin's input recording tools don't support Triforce input devices, breaking these features.
* Built-in Support For namcam2/Cycraft: Currently, third-party programs are required in order to emulate Cycraft and namcam2. In order to make using third-party servers easier, Triforce games can be told to look at any address, including localhost, for these devices. In the future, an emulated option alongside real servers would be preferrable, somewhat like how Emulated USB Devices are currently handled.
* Continue Fixing Crashes/Hangs:Triforce emulation performed extremely well during our extensive testing, but to say everything is perfect would be a stretch. Given the rarity of Triforce games, not every revision of every game has been tested and some may not work.One common hang is that the Mario Kart titles get stuck when trying to eject the magcard after play. This doesn't result in any loss of data, but does mean the game has to be reset.Edit: The magcard eject hang was fixed just before this article was launched.

This list is by no means exhaustive, but we wanted to give an idea of how much work is still left to be done. Triforce emulation works incredibly well right now, but will continue to be a work-in-progress for the foreseeable future.

### Wrapping Things Up¶

Suddenly being thrust into Triforce emulation after all of these years was quite the experience for everyone involved. We can confidently say that this esoteric hardware is full of surprises. Just emulating these games and trying to test them was a distinct challenge far removed from anything we experienced with the GameCube and Wii! Each game has so many unique quirks, revisions, and sometimes even hardware configurations!

This couldn't have happened withoutcrediar. Going into this, most Dolphin developers knew almost nothing about Triforce emulation, and without the decade plus of knowledge he had built up while maintaining his fork, we would have stood no chance.

With everything that's been done, there was one final challenge. Our goal was for Dolphin's Triforce emulation to be good enough to drive hobbyist arcade cabinets and preserve the arcade experience these games were meant for. So we gave it a try. We built a hobbyistF-Zero AXcabinet kit, set up a PC with Dolphin, and let family and friends have at it. And it was a blast for everyone involved.

It might not be nearly as glorious as the original cabinet, but it works!

When we first started on this journey, most of us hadn't had the opportunity to play any of the Triforce games on an original cabinet. The best we could do was buy the core systems and games and try to get them running with what we had. The experience on bare hardware was rarely good and never great, but that was not how they were meant to be played. Triforce games were designed to be a part of an arcade experience, with a cool cabinet, interesting features, and unique control schemes. Through emulation, we were able to bring some of that arcade magic back to these games that no longer have a cabinet to call home.

But through all of those trials, it's finally here. Maybe afewdozenyears later than anyone expected. However, there are still a lot of exciting changes still on the horizon, so be sure to check in for more development articles about Dolphin - the GameCube, Wii, andTriforceemulator!
