---
title: Brood War Bench
url: https://bw.swerdlow.dev/report
site_name: hackernews_api
content_file: hackernews_api-brood-war-bench
fetched_at: '2026-09-20T14:30:43.703515'
original_url: https://bw.swerdlow.dev/report
author: Ben Swerdlow
date: '2026-09-19'
description: Which model wins at Brood War? Results, recordings, costs, and game-by-game analysis of Codex, Claude, and Grok across 171 matches.
tags:
- hackernews
- trending
---

## Key takeaways

* None of the models played beyond a beginner level.
* Codex Astra is the clear leader beating all other models consistently.
* Grok models are not smart enough to play Brood War yet.
* Older models tended to play the RTS as a turn-based game, leading them to get destroyed while they were thinking. Newer models sometimes fell into the same trap, which may explain why some lower-effort settings performed better, but overall were much more cognizant of the cost of thinking.

Powered ByFreestyle

## Leaderboard

Rank
System
Wins
Losses
APM
Cost / game
Win rate
🥇
Codex Astra / xhigh
18
0
12.6
$10.54
100.0%
🥈
Codex Astra / medium
16
2
17.2
$15.11
88.9%
🥉
Claude Fable
15
3
12.6
$12.24
83.3%
4
Codex Astra / low
14
4
25.7
$21.07
77.8%
5
Codex 5.6 Sol / medium
13
5
10.1
$5.12
72.2%
6
Codex 5.6 Sol / low
12
6
18.1
$9.23
66.7%
7
Claude Opus 5
12
6
10.5
$20.78
66.7%
8
Codex 5.6 Sol / xhigh
11
7
8.0
$3.23
61.1%
9
Codex 5.6 Luna / low
9
9
23.8
$0.42
50.0%
10
Codex 5.6 Terra / xhigh
9
9
15.8
$2.10
50.0%
11
Codex 5.6 Terra / medium
8
10
10.5
$3.15
44.4%
12
Codex 5.6 Terra / low
8
10
48.3
$4.65
44.4%
13
Codex 5.6 Luna / xhigh
7
11
5.2
$0.16
38.9%
14
Claude Sonnet
7
11
6.2
$8.98
38.9%
15
Codex 5.6 Luna / medium
6
12
14.8
$0.30
33.3%
16
Grok 4.6 / xhigh
2
15
2.8
$0.66
11.1%
17
Grok 4.6 / medium
1
16
3.2
$0.79
5.6%
18
Claude Haiku
0
16
0.3
$0.34
0.0%
19
Grok 4.6 / low
0
16
4.2
$1.26
0.0%
Show all

Brood War Bench started after I built a version of Brood War that you could only play through agents as an experiment to play with friends. I played it with a couple friends who did surprisingly well for people who have only played a couple Starcraft games in their lives. When I asked them why, they said they hadn't done much, they asked their agent to attack and it had built a small army and done the full attack for them. This lead me to wonder how far they can go on their own; this is my answer.

## What I observed

01

### Codex found cheese before it found macro

Codex's strongest recurring idea was disruption. In Protoss games it often sent a Probe across the map to attack workers or buildings. This worked shockingly well as the opposing agents often spent dozens of seconds thinking about what to do about a probe instead of doing anything else.

The same systems were much weaker at sustained production. They delayed tech, trickled one or two basic units into defended bases, and threw workers into last stands.

I also noticed Codex often created separate subagents to manage the economy, army production, and army control. They didn't communicate much with one another, so the army agent often sent each new unit straight into an attack, unaware of the larger army the other agents were planning to build.

This is a common beginner mistake: sending units in one at a time instead of waiting for a critical mass and a planned attack timing. In games where I helped direct Codex, it was much better at planning those moments and getting its subagents to work together.

The persistence was real. In G009, after losing its army and main base, Codex 5.6 Terra / medium lifted its last Command Center and moved it toward the opposite corner. It survived for another six minutes.

Six Probes cross the map
A Probe first, then Zealots in drips
The last Command Center runs

02

### Grok spent the game between actions

Grok 4.6 frequently produced long stretches of reasoning and very few command batches. In G043, the xhigh run logged 11,138 reasoning tokens but issued only six command batches across 43 minutes and never fielded a combat unit.

The actions it did take rarely developed into a working control loop. In G003, Grok / xhigh made three Marines and never reached the enemy base. In G002, Grok / medium made two Zealots and also never crossed the map. These looked less like bad strategies than failures to keep observing and acting.

Forty-three minutes, no army

03

### Fable earnestly tried to play the game

I found myself rooting for Claude Fable in more than a few games. Fable usually tried to build an economy and climb the tech tree instead of stopping at the first unit available. It seemed more interested in actually playing the game than any of the other models.

In G007 it reached a Lair, Spire, and Mutalisks and won. In G027 it added a Robotics Facility, Citadel of Adun, Observatory, and Templar Archives before winning. Ambition did not guarantee execution: in G036 Fable reached a Factory and Academy but Opus 5 overran it.

Fable gets Mutalisks
Fable keeps climbing
The build does not become an army

### No agent here played beyond beginner level

Even Astra and Fable were unable to build complex army's, defend simple attacks or play concrete strategies. A beginner playing photon rush would win every single one of these games.

That said, watching the agents play made me more excited than I have been in a while. This benchmark is nowhere near exhausted. There is much more for the agents to learn, and much more for the benchmark to ask them to do. I look forward to watching them get there.

## How the games developed

Compare
Models
Model + effort
Harnesses
Race
All races
Terran
Protoss
Zerg
Game time
First 10 minutes
First 15 minutes
First 20 minutes
Full games
Choose up to five
Codex Astra
Claude Fable
Codex 5.6 Sol
Claude Opus 5
Codex 5.6 Luna
Codex 5.6 Terra
Claude Sonnet
Grok 4.6
Claude Haiku
5:00
 / 
15:00

### Technology investment

Completed research + upgrade levels

0
0.5
1
1.5
2
0:00
5:00
10:00
15:00
Codex Astra
0.3
Claude Fable
0.2
Grok 4.6
0

### Workers

Completed workers alive

0
8
16
24
32
0:00
5:00
10:00
15:00
Codex Astra
14.7
Claude Fable
16.7
Grok 4.6
7.4

### Army size

Completed army and support units

0
20
40
60
80
0:00
5:00
10:00
15:00
Codex Astra
8.3
Claude Fable
7.6
Grok 4.6
2

### Structures

Completed buildings, including add-ons

0
7
14
21
28
0:00
5:00
10:00
15:00
Codex Astra
6.2
Claude Fable
7.4
Grok 4.6
4.5

### Minerals in the bank

Unspent minerals, not income

0
500
1,000
1,500
2,000
0:00
5:00
10:00
15:00
Codex Astra
240.6
Claude Fable
248.6
Grok 4.6
536.6

### Gas in the bank

Unspent gas, not income

0
500
1,000
1,500
2,000
0:00
5:00
10:00
15:00
Codex Astra
151
Claude Fable
326.9
Grok 4.6
244.5

### Supply used

Includes production in progress

0
30
60
90
120
0:00
5:00
10:00
15:00
Codex Astra
26.5
Claude Fable
26.6
Grok 4.6
11.3

### When games ended

Share of games ending per 5-minute window

Codex Astra: median 8:10. 0:00 to before 5:00: 3.9%; 5:00 to before 10:00: 54.9%; 10:00 to before 15:00: 31.4%; 15:00 to before 20:00: 5.9%; 25:00 to before 30:00: 2%; 30:00 to before 35:00: 2%. Claude Fable: median 10:37. 5:00 to before 10:00: 38.9%; 10:00 to before 15:00: 38.9%; 15:00 to before 20:00: 22.2%. Grok 4.6: median 9:15. 0:00 to before 5:00: 2%; 5:00 to before 10:00: 51%; 10:00 to before 15:00: 23.5%; 15:00 to before 20:00: 13.7%; 20:00 to before 25:00: 2%; 40:00 to before 45:00: 7.8%.
Codex Astra
Median 8:10
60
%
Codex Astra: 3.9% (2 games) ended from 0:00 to before 5:00
Codex Astra: 54.9% (28 games) ended from 5:00 to before 10:00
Codex Astra: 31.4% (16 games) ended from 10:00 to before 15:00
Codex Astra: 5.9% (3 games) ended from 15:00 to before 20:00
Codex Astra: 0% (0 games) ended from 20:00 to before 25:00
Codex Astra: 2% (1 games) ended from 25:00 to before 30:00
Codex Astra: 2% (1 games) ended from 30:00 to before 35:00
Codex Astra: 0% (0 games) ended from 35:00 to before 40:00
Codex Astra: 0% (0 games) ended from 40:00 to before 45:00
Claude Fable
Median 10:37
60
%
Claude Fable: 0% (0 games) ended from 0:00 to before 5:00
Claude Fable: 38.9% (7 games) ended from 5:00 to before 10:00
Claude Fable: 38.9% (7 games) ended from 10:00 to before 15:00
Claude Fable: 22.2% (4 games) ended from 15:00 to before 20:00
Claude Fable: 0% (0 games) ended from 20:00 to before 25:00
Claude Fable: 0% (0 games) ended from 25:00 to before 30:00
Claude Fable: 0% (0 games) ended from 30:00 to before 35:00
Claude Fable: 0% (0 games) ended from 35:00 to before 40:00
Claude Fable: 0% (0 games) ended from 40:00 to before 45:00
Grok 4.6
Median 9:15
60
%
Grok 4.6: 2% (1 games) ended from 0:00 to before 5:00
Grok 4.6: 51% (26 games) ended from 5:00 to before 10:00
Grok 4.6: 23.5% (12 games) ended from 10:00 to before 15:00
Grok 4.6: 13.7% (7 games) ended from 15:00 to before 20:00
Grok 4.6: 2% (1 games) ended from 20:00 to before 25:00
Grok 4.6: 0% (0 games) ended from 25:00 to before 30:00
Grok 4.6: 0% (0 games) ended from 30:00 to before 35:00
Grok 4.6: 0% (0 games) ended from 35:00 to before 40:00
Grok 4.6: 7.8% (4 games) ended from 40:00 to before 45:00
0:00
15:00
30:00
45:00

Time-series charts show means of recorded player-runs at each game time. Finished games drop out; missing samples are not filled. Models pool their effort settings. Units and buildings count only once completed; army excludes workers, Overlords, eggs, larvae, and ammunition.

## Win rate vs. cost

Log scale
Linear

Average cost per game, using the same prices as the leaderboard. Codex and Sonnet costs are token-based estimates.

Codex
Claude
Grok
Win rate
0
%
25
%
50
%
75
%
100
%
$
0.1
$
0.5
$
1
$
5
$
10
$
20
Cost per game (USD
, log scale
)

## How the benchmark ran

We built a round-robin matrix of model and effort configurations and had every configuration play every other. The harness ran those matchups in parallel across Freestyle VMs, saving game-engine data and both agents' harness logs for each match.

## Head-to-head matrix

Read across a row. W is a win, L is a loss, and T is a match that reached the benchmark time limit.

Open the full 19 × 19 matrix
W
 win 
L
 loss 
T
 time limit 
G000
pending
System
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
1
Codex Astra / xhigh
-
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
W
2
Codex Astra / medium
L
-
W
W
W
W
W
W
W
W
W
W
L
W
W
W
W
W
W
3
Codex Astra / low
L
L
-
W
W
W
W
W
W
W
W
W
L
L
W
W
W
W
W
4
Codex 5.6 Sol / xhigh
L
L
L
-
L
W
W
W
L
W
W
W
L
L
W
W
W
W
W
5
Codex 5.6 Sol / medium
L
L
L
W
-
W
W
W
L
W
W
W
L
W
W
W
W
W
W
6
Codex 5.6 Sol / low
L
L
L
L
L
-
W
W
W
W
W
W
W
W
L
W
W
W
W
7
Codex 5.6 Luna / xhigh
L
L
L
L
L
L
-
W
L
W
L
W
L
L
L
W
W
W
W
8
Codex 5.6 Luna / medium
L
L
L
L
L
L
L
-
L
L
L
L
L
W
W
W
W
W
W
9
Codex 5.6 Luna / low
L
L
L
W
W
L
W
W
-
W
L
L
L
L
L
W
W
W
W
10
Codex 5.6 Terra / xhigh
L
L
L
L
L
L
L
W
L
-
W
W
L
W
W
W
W
W
W
11
Codex 5.6 Terra / medium
L
L
L
L
L
L
W
W
W
L
-
L
L
L
W
W
W
W
W
12
Codex 5.6 Terra / low
L
L
L
L
L
L
L
W
W
L
W
-
L
L
W
W
W
W
W
13
Claude Fable
L
W
W
W
W
L
W
W
W
W
W
W
-
L
W
W
W
W
W
14
Claude Opus 5
L
L
W
W
L
L
W
L
W
L
W
W
W
-
W
W
W
W
W
15
Claude Sonnet
L
L
L
L
L
W
W
L
W
L
L
L
L
L
-
W
W
W
W
16
Claude Haiku
L
L
L
L
L
L
L
L
L
L
L
L
L
L
L
-
L
T
T
17
Grok 4.6 / xhigh
L
L
L
L
L
L
L
L
L
L
L
L
L
L
L
W
-
W
T
18
Grok 4.6 / medium
L
L
L
L
L
L
L
L
L
L
L
L
L
L
L
T
L
-
W
19
Grok 4.6 / low
L
L
L
L
L
L
L
L
L
L
L
L
L
L
L
T
T
L
-

## Play your own match

Bring your agent and play Brood War with friends.

Play Brood War