---
title: Auto-Discovering Console Commands in Power Modules - DEV Community
url: https://dev.to/homeless-coder/auto-discovering-console-commands-in-power-modules-4j8a
site_name: devto
fetched_at: '2025-10-22T11:16:58.835428'
original_url: https://dev.to/homeless-coder/auto-discovering-console-commands-in-power-modules-4j8a
author: HomelessCoder
date: '2025-10-16'
description: A couple of days ago, I was working on a PHP project that uses the Power Modules framework and... Tagged with php, software, architecture, opensource.
tags: '#php, #software, #architecture, #opensource'
---

A couple of days ago, I was working on a PHP project that uses the Power Modules framework and Symfony Console, and I realized I was repeating the same command registration pattern across multiple projects. Time to build something better!

For those new to the series: Power Modules is a modular PHP framework where each module encapsulates its own logic and dependencies, communicating through well-defined interfaces while maintaining strict boundaries.

I already had a working setup/boilerplate for registering console commands exported from a Power Module (using theExportsComponentsinterface) that I copy-pasted across projects. It follows the Power Modules framework principles: keep modules encapsulated and their dependencies private, and delegate the instantiation and dependency resolution to their DI container:

$modules

=

[


new

OrdersModule
(),


new

UsersModule
(),


// ... other modules

];

$app

=

new

ModularAppBuilder
(
__DIR__

.

'/../'
)


->
withModules
(
...
$modules
)


->
build
()

;

$console

=

new

\Symfony\Component\Console\Application
(
'My Console Application'
,

'0.1.0'
);

foreach

(
$modules

as

$module
)

{


foreach

(
$module
::
exports
()

as

$exportedComponent
)

{


// $exportedComponent is just a class-string that references to a power module DI container


if

(
is_a
(
$exportedComponent
,

Command
::
class
,

true
)

===

true
)

{


$console
->
add
(
$app
->
get
(
$exportedComponent
));


}


}

}

Enter fullscreen mode

Exit fullscreen mode

## The Problem

This works, but it felt clunky repeating this boilerplate across projects. I knew that Symfony DI can manage console commands, and I wanted to see if I could build something that automatically discovers and registers console commands from different modules. So I thought: Why not apply thePowerModuleSetupconcept for this? (you can read more about it here:The Night I Discovered I'd Built Something Revolutionary (And Didn't Know It)

## Building the Solution

The implementation was quite straightforward - create aPowerModuleSetupthat does the same thing as the above code, but in a more modular and reusable way.

### First Iteration: Direct Registration

ThisPowerModuleSetupbridges Symfony Console with the Power Modules framework's modular architecture. Modules export console commands while maintaining encapsulation principles, and commands are auto-discovered and registered into a centralConsole\Application.

final

class

ConsoleCommandsSetup

implements

PowerModuleSetup

{


private

\Symfony\Component\Console\Application

$console
;


public

function

__construct
()


{


$this
->
console

=

new

\Symfony\Component\Console\Application
();


}


public

function

setup
(
PowerModuleSetupDto

$dto
):

void


{


if

(
!
$dto
->
powerModule

instanceof

ExportsComponents
)

{


return
;


}


if

(
$dto
->
setupPhase

!==

SetupPhase
::
Post
)

{


return
;


}


if

(
$dto
->
rootContainer
->
has
(
Application
::
class
)

===

false
)

{


$dto
->
rootContainer
->
set
(
Application
::
class
,

$this
->
console
);


}


foreach

(
$dto
->
powerModule
::
exports
()

as

$exportedComponent
)

{


if

(
is_a
(
$exportedComponent
,

Command
::
class
,

true
)

===

true
)

{


$this
->
console
->
add
(
$dto
->
rootContainer
->
get
(
$exportedComponent
));


}


}


}

}

Enter fullscreen mode

Exit fullscreen mode

### Adding Lazy-Loading with ContainerCommandLoader

I wanted to take it further with deferred command instantiation. Symfony'sContainerCommandLoaderloads commands from a DI container on-demand. SinceExportsComponentsSetupalready registers exported components in the root container, I could leverage that. This meant updating the setup to use a two-phase approach: collect commands in the Pre phase and register them in the Post phase.

final

class

ConsoleCommandsSetup

implements

PowerModuleSetup

{


private

Application

$console
;


private

?CommandLoaderInterface

$commandLoader

=

null
;


/**
 * @var array<string,class-string<Command>> $commandMap
 */


private

array

$commandMap

=

[];


public

function

__construct
()


{


$this
->
console

=

new

Application
();


}


public

function

setup
(
PowerModuleSetupDto

$powerModuleSetupDto
):

void


{


if

(
!
$powerModuleSetupDto
->
powerModule

instanceof

ExportsComponents
)

{


return
;


}


if

(
$powerModuleSetupDto
->
setupPhase

===

SetupPhase
::
Pre
)

{


// PRE phase: collect all commands to be registered later


foreach

(
$powerModuleSetupDto
->
powerModule
::
exports
()

as

$component
)

{


if

(
is_subclass_of
(
$component
,

Command
::
class
))

{


if

(
$attribute

=

(
new

ReflectionClass
(
$component
))
->
getAttributes
(
AsCommand
::
class
))

{


$this
->
commandMap
[
$attribute
[
0
]
->
newInstance
()
->
name
]

=

$component
;


}


}


}


return
;


}


if

(
$this
->
commandLoader

!==

null
)

{


return
;


}


$this
->
commandLoader

=

new

ContainerCommandLoader
(


$powerModuleSetupDto
->
rootContainer
,


$this
->
commandMap
,


);


$console

=

$this
->
console
;


if

(
$powerModuleSetupDto
->
rootContainer
->
has
(
Application
::
class
)

===

true
)

{


$console

=

$powerModuleSetupDto
->
rootContainer
->
get
(
Application
::
class
);


}

else

{


$powerModuleSetupDto
->
rootContainer
->
set
(
Application
::
class
,

$this
->
console
);


}


$console
->
setCommandLoader
(
$this
->
commandLoader
);


}

}

Enter fullscreen mode

Exit fullscreen mode

## Usage

Now I have a reusablePowerModuleSetupthat can be added to any Power Modules application to automatically discover and register console commands from modules:

$app

=

new

ModularAppBuilder
(
__DIR__

.

'/../'
)


->
withModules
(


new

OrdersModule
(),


new

UsersModule
(),


)


->
withPowerSetup
(
new

ConsoleCommandsSetup
())


->
build
();

// Console application is now available with all module commands registered

$console

=

$app
->
get
(
\Symfony\Component\Console\Application
::
class
);

$console
->
run
();

Enter fullscreen mode

Exit fullscreen mode

## Wrapping Up

The complete implementation is available in the repository:power-modules/console

Install via Composer:

composer require power-modules/console

Enter fullscreen mode

Exit fullscreen mode

This pattern eliminated the boilerplate I was copy-pasting and made command registration automatic. If you're building modular applications with Power Modules, this setup might save you some time too.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
