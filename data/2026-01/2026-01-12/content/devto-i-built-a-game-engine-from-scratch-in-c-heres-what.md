---
title: I Built a Game Engine from Scratch in C++ (Here's What I Learned) - DEV Community
url: https://dev.to/montmont20z/building-a-game-engine-from-scratch-using-c-my-breakout-clone-journey-20d1
site_name: devto
fetched_at: '2026-01-12T11:08:06.168354'
original_url: https://dev.to/montmont20z/building-a-game-engine-from-scratch-using-c-my-breakout-clone-journey-20d1
author: Melvin Cheah
date: '2026-01-07'
description: I Built a Game Engine from Scratch in C++ (Here's What I Learned) I crashed my GPU 47... Tagged with programming, gamedev, learning, cpp.
tags: '#programming, #gamedev, #learning, #cpp'
---

## I Built a Game Engine from Scratch in C++ (Here's What I Learned)

I crashed my GPU 47 times before I saw my first triangle on screen.

For 3 months, I built a game engine from scratch in C++ using DirectX 9 and Win32—no Unity, no Unreal, no middleware. Just me, the Windows API, and a lot of segmentation faults.

This is the story of how building a simple Breakout clone taught me more about game development, graphics programming, and software architecture than years of using Unity ever did.

## Why Build an Engine?

For years, I built games in Unity. I'd drag and drop GameObjects, attach scripts, hit Play, and watch my game come to life. It was magical—until it wasn't.

Questions started nagging at me:

* How does Unity actually render my sprites?What's happening betweenGameObject.transform.position = newPosand pixels on screen?
* Why do people complain about Unreal's performance?If it's "optimized," why do developers still struggle?
* Why was Kerbal Space Program's physics so buggy?It's Unity—doesn't Unity handle physics automatically?

I realized I was using powerful tools without understanding what they were doing under the hood. I was a chef using a microwave, not knowing how heat actually cooks food.

Then my university professor gave us an assignment:Build a low-level game engine in C++.

No Unity. No libraries. Just C++, DirectX 9, and the Win32 API.

This was my chance to peek behind the curtain.

## What I Built: Breakout, But From Scratch

If you've never played Breakout: you control a paddle at the bottom of the screen, bouncing a ball to destroy bricks at the top. Simple concept, complex implementation.

My engine features:

* Custom rendering pipelineusing DirectX 9
* Fixed-timestep game loop(60 FPS target)
* AABB and swept collision detection(no tunneling!)
* State management system(Menu → Level 1 → Level 2 → Level 3 → End Game)
* Sound systemintegration
* Sprite animation system
* Physics simulation(velocity, acceleration, collision response)

The result:A fully playable Breakout clone running at 60 FPS with ~3,500 lines of C++ code.

Tech Stack:

* Language: C++17
* Graphics API: DirectX 9 (legacy, but perfect for learning fundamentals)
* Windowing: Win32 API
* Audio: Windows multimedia extensions
* IDE: Visual Studio 2022

## Architecture Overview: Separation of Concerns

One of my biggest lessons:good architecture makes or breaks your project.

I learned this the hard way (more on that in "Challenges" below), but here's the final structure I landed on:

### Class Diagram

### Core Components

Game Class (The Orchestrator)

* Owns all managers (Renderer, Input, Physics, Sound)
* Manages game state transitions (Menu ↔ Level 1 ↔ Game Over)
* Runs the main game loop

MyWindow (Platform Layer)

* Wraps Win32 window creation and message processing
* Handles OS-level events (close, minimize, resize)
* Why separate?Platform code should be isolated—makes porting to Linux/Mac easier later

Renderer (Graphics Layer)

* Initializes DirectX 9 device
* Manages textures and sprites
* Provides clean API:LoadTexture(),DrawSprite(),BeginFrame()
* Key insight:The game logic never touches DirectX directly

InputManager (User Input)

* Polls keyboard state using DirectInput
* Abstracts raw input into game-meaningful queries:IsKeyDown(DIK_LEFT)
* Why?Game code doesn't care about DirectInput—it just wants "left" or "right"

PhysicsManager (Collision & Movement)

* AABB collision detection
* Swept AABB for fast-moving objects (prevents tunneling)
* Collision resolution with restitution
* Lesson learned:Separatedetectionfromresolution(I didn't know this at first!)

SoundManager (Audio)

* Loads and plays sound effects
* Handles background music with looping
* Volume control

IGameState (State Pattern)

* Interface for all game states: Menu, Level1, Level2, GameOver, YouWin
* Each state implements:OnEnter(),Update(),Render(),OnExit()
* This was my "aha!" moment—more on this below

### The Game Loop

cpp

while

(
window
.
ProcessMessages
())

{


// 1. Calculate delta time (frame-independent movement)


float

dt

=

CalculateDeltaTime
();


// 2. Update input state


inputManager
.
Update
();


// 3. Update current game state


// (Menu, Level, GameOver, etc.)


gameState
->
Update
(
dt
,

inputManager
,

physicsManager
,

soundManager
);


// 4. Render everything


renderer
.
BeginFrame
();


gameState
->
Render
(
renderer
);


renderer
.
EndFrame
();

}

Enter fullscreen mode

Exit fullscreen mode

Why this structure?

* Modularity:Each system has one job
* Testability:Can test physics without rendering
* Maintainability:Bug in rendering? Only look in Renderer class
* Scalability:Adding a new game state? Just implement IGameState

## The Rendering Pipeline: From Nothing to Pixels

DirectX 9 has a reputation: it's old (released 2002), verbose, and unforgiving. But that's precisely why it's perfect for learning—you have to understand every step.

### Initialization: Setting Up DirectX 9

Getting a window to show anything requiresfive major steps:

#### 1. Create the Direct3D9 Interface

cpp

IDirect3D9
*

m_direct3D9

=

Direct3DCreate9
(
D3D_SDK_VERSION
);

if

(
!
m_direct3D9
)

{


// Failed to create—probably missing DirectX runtime


return

false
;

}

Enter fullscreen mode

Exit fullscreen mode

This creates the main Direct3D object. Think of it as "connecting to the graphics driver."

#### 2. Query Display Capabilities

cpp

D3DDISPLAYMODE

displayMode
;

m_direct3D9
->
GetAdapterDisplayMode
(
D3DADAPTER_DEFAULT
,

&
displayMode
);

Enter fullscreen mode

Exit fullscreen mode

We need to know: What resolution? What color format? This tells us what the monitor supports.

#### 3. Configure the Presentation Parameters

cpp

D3DPRESENT_PARAMETERS

m_d3dPP

=

{};

m_d3dPP
.
Windowed

=

TRUE
;

// Windowed mode (not fullscreen)

m_d3dPP
.
BackBufferWidth

=

width
;

// 800 pixels

m_d3dPP
.
BackBufferHeight

=

height
;

// 600 pixels

m_d3dPP
.
BackBufferFormat

=

D3DFMT_UNKNOWN
;

// Match desktop format

m_d3dPP
.
BackBufferCount

=

1
;

// Double buffering

m_d3dPP
.
SwapEffect

=

D3DSWAPEFFECT_DISCARD
;

// Throw away old frames

m_d3dPP
.
EnableAutoDepthStencil

=

TRUE
;

// We need depth testing

m_d3dPP
.
AutoDepthStencilFormat

=

D3DFMT_D16
;

// 16-bit depth buffer

Enter fullscreen mode

Exit fullscreen mode

This is where modern APIs (Vulkan, DX12) get even MORE complex.You're essentially telling the GPU: "Here's how I want my window's backbuffer configured."

#### 4. Create the Device

cpp

HRESULT

hr

=

m_direct3D9
->
CreateDevice
(


D3DADAPTER_DEFAULT
,

// Use default GPU


D3DDEVTYPE_HAL
,

// Hardware acceleration


hWnd
,

// Window handle


D3DCREATE_HARDWARE_VERTEXPROCESSING
,

// Use GPU for vertex math


&
m_d3dPP
,


&
m_d3dDevice

);

Enter fullscreen mode

Exit fullscreen mode

This is where I crashed 47 times.Wrong parameters? Crash. Unsupported format? Crash. Missing depth buffer? Crash.

Fallback strategy:If hardware vertex processing fails (older GPUs), fall back to software:

cpp

if

(
FAILED
(
hr
))

{


// Try again with CPU-based vertex processing


hr

=

m_direct3D9
->
CreateDevice
(...,

D3DCREATE_SOFTWARE_VERTEXPROCESSING
,

...);

}

Enter fullscreen mode

Exit fullscreen mode

#### 5. Create the Sprite Renderer

cpp

ID3DXSprite
*

m_spriteBrush
;

D3DXCreateSprite
(
m_d3dDevice
,

&
m_spriteBrush
);

Enter fullscreen mode

Exit fullscreen mode

DirectX 9'sID3DXSpriteis a helper for 2D games. It batches sprite draws and handles transformations.

### Rendering Each Frame

Once initialized, every frame follows this pattern:

cpp

void

Renderer
::
BeginFrame
()

{


// Clear the screen to black


m_d3dDevice
->
Clear
(
0
,

NULL
,

D3DCLEAR_TARGET

|

D3DCLEAR_ZBUFFER
,


D3DCOLOR_XRGB
(
0
,

0
,

0
),

1.0
f
,

0
);


m_d3dDevice
->
BeginScene
();

// Start recording draw calls


m_spriteBrush
->
Begin
(
D3DXSPRITE_ALPHABLEND
);

// Enable alpha blending for sprites

}

void

Renderer
::
DrawSprite
(
const

SpriteInstance
&

sprite
)

{


// Apply transformations (position, rotation, scale)


D3DXMATRIX

transform

=

CalculateTransform
(
sprite
);


m_spriteBrush
->
SetTransform
(
&
transform
);


// Draw the texture


m_spriteBrush
->
Draw
(
sprite
.
texture
,

&
sourceRect
,

nullptr
,

nullptr
,

sprite
.
color
);

}

void

Renderer
::
EndFrame
()

{


m_spriteBrush
->
End
();

// Finish sprite batch


m_d3dDevice
->
EndScene
();

// Stop recording


m_d3dDevice
->
Present
(...);

// Flip backbuffer to screen (VSYNC happens here)

}

Enter fullscreen mode

Exit fullscreen mode

Key Concept: Double Buffering

We draw to a "backbuffer" (off-screen), thenPresent()swaps it with the screen's front buffer. This prevents tearing (seeing half-drawn frames).

Performance Note:EachDrawSprite()call is relatively expensive. In a real engine, you'd batch hundreds of sprites into fewer draw calls. For Breakout (~50 bricks max), it doesn't matter.

## Challenges & Solutions: Where I Failed (And What I Learned)

### Challenge 1: Architecture Disaster (Week 3)

The Problem:

I made the classic beginner mistake:I started coding without designing.

My first attempt looked like this:

cpp

class

Game

{


Renderer

renderer
;


InputManager

input
;


// OH NO—game logic mixed into Game class!


Paddle

paddle
;


Ball

ball
;


Brick

bricks
[
50
];


void

Update
()

{


// Handle input


if

(
input
.
IsKeyDown
(
LEFT
))

paddle
.
x

-=

5
;


// Update physics


ball
.
x

+=

ball
.
velocityX
;


// Check collisions


for

(
auto
&

brick

:

bricks
)

{


if

(
CollidesWith
(
ball
,

brick
))

{


brick
.
alive

=

false
;


}


}


// ...300 more lines of spaghetti code


}

};

Enter fullscreen mode

Exit fullscreen mode

This worked fine—until I needed to add a menu screen.

Suddenly I realized:How do I switch between Menu and Level1?

My code had no concept of "states." Everything was hardcoded into one giantUpdate()function. Adding a menu meant:

* Wrapping everything inif (currentState == PLAYING)
* Duplicating input handling for menu vs. gameplay
* Managing which objects exist when

It was a mess. I was 2 weeks in and facing a complete rewrite.

The Solution: State Pattern

I asked my lecturer (and ChatGPT) for advice. The answer:State Pattern.

cpp

// Interface that all game states implement

class

IGameState

{

public:


virtual

void

OnEnter
(
GameServices
&

services
)

=

0
;


virtual

void

Update
(
float

dt
,

...)

=

0
;


virtual

void

Render
(
Renderer
&

renderer
)

=

0
;


virtual

void

OnExit
(
GameServices
&

services
)

=

0
;

};

Enter fullscreen mode

Exit fullscreen mode

Now each screen is its own class:

cpp

class

MenuState

:

public

IGameState

{

/* menu logic */

};

class

Level1

:

public

IGameState

{

/* level 1 logic */

};

class

GameOverState

:

public

IGameState

{

/* game over logic */

};

Enter fullscreen mode

Exit fullscreen mode

TheGameclass just delegates to the current state:

cpp

class

Game

{


std
::
unique_ptr
<
IGameState
>

currentState
;


void

Update
(
float

dt
)

{


currentState
->
Update
(
dt
,

...);

// Let the state handle it


}


void

ChangeState
(
std
::
unique_ptr
<
IGameState
>

newState
)

{


if

(
currentState
)

currentState
->
OnExit
(...);


currentState

=

std
::
move
(
newState
);


if

(
currentState
)

currentState
->
OnEnter
(...);


}

};

Enter fullscreen mode

Exit fullscreen mode

What I Learned:

* Design before code(ESPECIALLY for 1,000+ line projects)
* Separation of concernsmakes code flexible
* Refactoring hurts, but teaches more than getting it right the first time

The State Pattern is everywhere—React components, game engines, even operating systems use it. This lesson alone was worth the 3 months.

### Challenge 2: The Ball Goes Through Bricks (Tunneling)

The Problem:

My first collision detection looked like this:

cpp

if

(
OverlapsAABB
(
ball
,

brick
))

{


brick
.
alive

=

false
;


ball
.
velocityY

=

-
ball
.
velocityY
;

// Bounce

}

Enter fullscreen mode

Exit fullscreen mode

This worked at 60 FPS... until the ball moved too fast.

At high speeds, the ball wouldtunnel—pass completely through a brick between frames:

Frame 1: Ball is here → [ ]
 ↓
Frame 2: Ball is here [ ] ← Ball skipped the brick!

Enter fullscreen mode

Exit fullscreen mode

The ball moved 50 pixels, but the brick was only 32 pixels wide. By the next frame, the ball wasalready pastthe brick, so the overlap check returned false.

First Failed Solution: Smaller Time Steps

I tried updating physics 120 times per second instead of 60. This helped but didn't solve it—at very high velocities, tunneling still occurred.

The Real Solution: Swept AABB

I neededcontinuous collision detection—checking not just "are they overlapping now?" but "will they overlap at any point during this frame's movement?"

This is calledswept AABB(orray-swept box). Instead of checking the ball's current position, I treat the ball's movement as a ray:

cpp

bool

SweepAABB
(


Vector3

ballPos
,

Vector2

ballSize
,


Vector3

displacement
,

// Where the ball will move this frame


Vector3

brickPos
,

Vector2

brickSize
,


float
&

timeOfImpact
,

// When in [0,1] does collision happen?


Vector3
&

hitNormal

// Which side did we hit?

)

{


// Calculate when the ball's edges cross the brick's edges


float

xEntryTime

=

...;

// Math for X-axis entry


float

yEntryTime

=

...;

// Math for Y-axis entry


float

overallEntry

=

max
(
xEntryTime
,

yEntryTime
);


if

(
overallEntry

<

0

||

overallEntry

>

1
)

{


return

false
;

// No collision this frame


}


timeOfImpact

=

overallEntry
;


return

true
;

}

Enter fullscreen mode

Exit fullscreen mode

Now my collision loop looks like:

cpp

Vector3

displacement

=

ball
.
velocity

*

dt
;

float

toi
;

Vector3

normal
;

if

(
SweepAABB
(
ball
,

displacement
,

brick
,

toi
,

normal
))

{


// Move ball to exactly the collision point


ball
.
position

+=

displacement

*

toi
;


// Bounce


if

(
normal
.
x

!=

0
)

ball
.
velocity
.
x

=

-
ball
.
velocity
.
x
;


if

(
normal
.
y

!=

0
)

ball
.
velocity
.
y

=

-
ball
.
velocity
.
y
;


brick
.
alive

=

false
;

}

Enter fullscreen mode

Exit fullscreen mode

Result:No more tunneling, even at 1000 pixels/second.

What I Learned:

* Discrete collision detection (overlap checks) fails at high speeds
* Continuous collision detection (swept/ray-based) is essential for fast-moving objects
* This is why bullets in games use raycasts, not overlap checks

The math was painful (lots of min/max comparisons), but understanding this concept changed how I think about physics in games.

### Challenge 3: Collision Detection ≠ Collision Resolution

The Confusion:

When I started, I thought "collision detection" and "collision resolution" were the same thing. They're not.

* Detection= "Did these two objects hit?"
* Resolution= "Okay, now what do we DO about it?"

My first attempt mixed them together:

cpp

if

(
OverlapsAABB
(
ball
,

paddle
))

{


ball
.
velocityY

=

-
ball
.
velocityY
;

// This is resolution!

}

Enter fullscreen mode

Exit fullscreen mode

This caused bugs:

* Ball would "stick" to the paddle
* Multiple collisions in one frame would cancel out
* Overlapping objects would vibrate

The Fix: Separate Phases

cpp

// Phase 1: Detection (PhysicsManager)

bool

hit

=

SweepAABB
(
ball
,

paddle
,

timeOfImpact
,

normal
);

// Phase 2: Resolution (also PhysicsManager, but separate function)

if

(
hit
)

{


// Move ball to contact point


ball
.
position

+=

displacement

*

timeOfImpact
;


// Apply restitution (bounciness)


ball
.
velocity

=

Reflect
(
ball
.
velocity
,

normal
)

*

restitution
;

}

Enter fullscreen mode

Exit fullscreen mode

What I Learned:

* Physics engines havedetectionandresponseas separate systems
* This separation allows for complex scenarios (multiple overlaps, conveyor belts, one-way platforms)
* YouTube tutorials often skip this distinction—they work for simple cases but fail for complex games

## What I'd Do Differently

If I built this again from scratch:

1. Design first, code second(spend 2-3 days on architecture diagrams)
2. Use a modern graphics API(DirectX 11 or OpenGL 4.5) instead of DX9* DX9 is fine for learning, but dated (no compute shaders, limited pipeline control)
3. Write unit tests for physics(I caught so many bugs by hand-testing that could've been automated)
4. Implement an entity-component system (ECS)instead of inheritance-based game objects
5. Add a debug overlay earlier(FPS counter, collision visualization saved me hours of debugging)
6. Profile from day one(I didn't measure performance until week 8—wasted time optimizing the wrong things)

## Conclusion & Next Steps

Building a game engine from scratch washard—way harder than Unity tutorials made game development seem.

But that's the point.

What I Gained:

* Deep understanding of rendering pipelines
* Practical knowledge of physics simulation
* Appreciation for what Unity/Unreal abstract away
* Confidence to debug low-level issues
* A portfolio piece that stands out

What's Next:

* Port this engine toDirectX 11(modern pipeline, compute shaders)
* Build avoxel engine(Minecraft-style, using Three.js for web)
* Experiment withVulkan(the final boss of graphics APIs)

Links:

* 📦Source Code (GitHub)
* 🎮Download & Play
* 🌐My Portfolio
* 📧Let's Connect
* Originally published onHashnode

If you're thinking about building your own engine:

Do it. Not to replace Unity, but tounderstandUnity.

You'll struggle. You'll debug cryptic errors at 2 AM. You'll question why you didn't just use Godot.

But when you finally see that ball bounce for the first time—compiled from YOUR code, rendered by YOUR pipeline, colliding with YOUR physics—you'll understand why people say"reinventing the wheel is the best way to learn how wheels work."

Questions? Suggestions? Let me know in the comments! 👇

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (19 comments)


For further actions, you may consider blocking this person and/orreporting abuse
