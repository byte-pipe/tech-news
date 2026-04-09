---
title: 'AniGuess: Real-Time Multiplayer Anime Guessing Game - DEV Community'
url: https://dev.to/ykimura/aniguess-real-time-multiplayer-anime-guessing-game-17n3
site_name: devto
fetched_at: '2025-08-16T10:02:28.154389'
original_url: https://dev.to/ykimura/aniguess-real-time-multiplayer-anime-guessing-game-17n3
author: Yuyi Kimura (YK46)
date: '2025-08-11'
description: 'This is a submission for the Redis AI Challenge: Beyond the Cache. What I Built I built... Tagged with redischallenge, devchallenge, database, ai.'
tags: '#redischallenge, #devchallenge, #database, #ai'
---

Redis AI Challenge: Beyond the Cache

This is a submission for theRedis AI Challenge: Beyond the Cache.

## What I Built

I builtAniGuess, a real-time multiplayer anime character guessing game that showcases Redis as a powerful multi-model platform beyond simple caching. The game supports up to 4 players competing simultaneously in rooms, where they guess anime characters based on attribute feedback similar to Wordle mechanics.

The application demonstrates Redis's versatility by using it as the primary database for game state management and session storage. Players join rooms with 6-character codes, compete across multiple rounds with configurable timers, and receive live updates as other players make guesses.

## Demo

Play the game now:https://aniguess.onrender.com/

Repository:https://github.com/ypk46/aniguess

The game features:• Real-time multiplayer gameplay with instant updates• Smart hint system using Redis as storage• Character images and detailed attribute comparisons• Customizable game settings (1-10 rounds, 30-300 second timers)• Complete scoring system with winner determination• Responsive design for all devices

## How I Used Redis 8

Rather than treating Redis as just a cache, I leveraged it as the primary database and real-time communication backbone for the entire multiplayer experience:

### 1. Primary Database for Game State

Redis serves as the main data store for all game sessions, eliminating the need for complex database queries during gameplay:

// Room state management in Redis

export

class

RoomService

{


async

createRoom
(
settings
:

GameSettings
):

Promise
<
Room
>

{


const

room
:

Room

=

{


code
:

this
.
generateRoomCode
(),


players
:

[],


gameState
:

'
waiting
'
,


settings
,


currentRound
:

0
,


// ... other properties


};


await

this
.
redis
.
setex
(


`room:
${
room
.
code
}
`
,


3600
,

// 1 hour TTL


JSON
.
stringify
(
room
)


);


return

room
;


}

}

Enter fullscreen mode

Exit fullscreen mode

### 2.Pub/Sub for Horizontal Scalability

The Redis adapter handles all the complexity of cross-instancecommunication, making Socket.IO code work seamlessly across multiple servers.

// socket.service.ts

import

{

createAdapter

}

from

'
@socket.io/redis-adapter
'
;

const

pubClient

=

createClient
({

url
:

redisConfig
.
url

});

const

subClient

=

pubClient
.
duplicate
();

this
.
io

=

new

SocketIOServer
(
server
,

{


adapter
:

createAdapter
(
pubClient
,

subClient
)

});

Enter fullscreen mode

Exit fullscreen mode

How It Works

1. Two Redis Connections: Publisher sends messages, Subscriber receives them
2. Cross-Instance Communication: When you emit to a room/broadcast, the adapter:* Emits locally to connected clients
* Publishes to Redis channel
* Other server instances receive and emit to their clients

### 3. Session Management and Player State

Redis handles all player sessions and maintains game state with automatic expiration:

// Player session and game progress tracking

async

submitGuess
(
roomCode
:

string
,

playerId
:

string
,

characterId
:

number
)

{


const

room

=

await

this
.
getRoom
(
roomCode
);


// Store guess result in Redis with structured data


const

guessKey

=

`guess:
${
roomCode
}
:
${
playerId
}
:
${
room
.
currentRound
}
`
;


await

this
.
redis
.
setex
(
guessKey
,

3600
,

JSON
.
stringify
({


characterId
,


timestamp
:

Date
.
now
(),


attributes
:

comparedAttributes
,


isCorrect
:

guess
.
isCorrect


}));


// Update room state atomically


await

this
.
updateRoomState
(
roomCode
,

updatedRoom
);

}

Enter fullscreen mode

Exit fullscreen mode

### 4. Multi-Model Data Structures

The application uses Redis's rich data types to optimize different aspects of the game:

•Hash structuresfor complex room configurations•Setsfor managing active players and room codes•Sorted setsfor leaderboards and scoring•String operationswith TTL for temporary game data

### Key Benefits Achieved:

1. Zero Database Latency: All game operations happen in-memory with Redis, providing instant responses crucial for real-time gameplay
2. Horizontal Scalability: Pub/sub enables multiple server instances to share game state seamlessly
3. Automatic Cleanup: TTL on game rooms prevents memory bloat without manual intervention
4. Atomic Operations: Redis transactions ensure consistent game state even with concurrent player actions

This implementation showcases Redis 8 as a complete solution for real-time applications, proving it can serve as both the primary database and communication layer while maintaining the performance needed for engaging multiplayer experiences.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
