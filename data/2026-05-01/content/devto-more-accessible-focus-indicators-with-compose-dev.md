---
title: More Accessible Focus Indicators with Compose - DEV Community
url: https://dev.to/eevajonnapanula/more-accessible-focus-indicators-with-compose-1ca4
site_name: devto
content_file: devto-more-accessible-focus-indicators-with-compose-dev
fetched_at: '2026-05-01T11:58:28.677138'
original_url: https://dev.to/eevajonnapanula/more-accessible-focus-indicators-with-compose-1ca4
author: Eevis
date: '2026-04-30'
description: Last summer, I wrote a blog post about focus management with Compose. Ever since, I’ve had drafts of... Tagged with android, a11y, mobile, programming.
tags: '#android, #a11y, #mobile, #programming'
---

Last summer, I wrote a blog post about focus management with Compose. Ever since, I’ve had drafts of this post, but I didn’t get to finalize it until now. The blog post is available in:It's All About (Accessibility) Focus And Compose.

So, in this blog post, we’re talking about focus indicators and how to make them more accessible with Compose. But let’s first talk about focus indicators in general.

## Focus Indicators

Focus indicators are, as the name suggests, indicators that show where keyboard focus currently is in the UI. They need to be visible so that keyboard and keyboard-emulating device users can navigate around the app effortlessly.

An important thing to note is that the focus indicator I’m talking about here is not for the screen reader (e.g., TalkBack) focus. That is handled on the system level.

Web Content Accessibility Guidelines (the standard behind accessibility legislation and used with apps as well, despite the name) has some requirements for accessible focus indicators. PerSC 2.4.13 Focus Appearance, the focus indicator needs to be either

* User agent’s (Android system) default styles
* At least 2 pixels thick and has a contrast ratio of at least 3:1 between the same pixels of focused and unfocused states.

Android’s default focus indicator is the ripple, which isn't very visible. Technically, it would pass, but if you want to make the application accessible, you’ll need to improve the visibility of the focus indicator. Let’s next discuss one way to build more visible (and thus, more accessible) focus indicators with Compose.

## Building More Accessible Focus Indicators with Compose

There are several ways of creating the focus indicators. You can, for example, add a border based on the focused state, as Appt.org suggests in their code snippets:Accessibility focus indicator in Jetpack Compose, but if you want anything more complex, you’ll want to turn to Indication API.

Indication APIwith aDrawModifierNodecan be used to draw complex focus indicators. In this blog post, we’re drawing a simple line under the currently focused item, first a button:

And then a switch-row:

### The Focus Indicator

What we’re essentially creating is a modifier that can be used in any interactive component. We want to wrap as much of the logic within the modifier and the other components so that usage in the Compose code is as easy as possible.

For this, we will need three things:

* The modifier (let’s call itfocusIndication)
* IndicationNodeFactoryto create the indication (FocusIndication)
* And finally,DrawModifierNodeto actually draw the focus indicator (FocusNode)

### Building the Modifier

Let’s start from the bottom of the list.

To create the actual indication, we want to define a class that takes an interaction source and a color as parameters. It extendsModifier.Node()andDrawModifierNode, and overrides two methods:onAttachandContentDrawScope.draw().

class
 
FocusNode
(

 
val
 
interactionSource
:
 
InteractionSource
,

 
val
 
color
:
 
Color

)
 
:
 
Modifier
.
Node
(),
 
DrawModifierNode
 
{

 
override
 
fun
 
onAttach
()
 
{

 
…

 
}

 
override
 
fun
 
ContentDrawScope
.
draw
()
 
{

 
…

 
}

}

Enter fullscreen mode

Exit fullscreen mode

TheonAttachfunction handles the interactions. Let’s add an internal variable to store the focus state of the component, and store it within theonAttach:

private
 
var
 
isFocused
 
by
 
mutableStateOf
(
false
)

override
 
fun
 
onAttach
()
 
{

 
coroutineScope
.
launch
 
{

 
interactionSource
.
interactions
.
collect
 
{
 
interaction
 
->

 
when
 
(
interaction
)
 
{

 
is
 
FocusInteraction
.
Focus
 
->
 
isFocused
 
=
 
true

 
is
 
FocusInteraction
.
Unfocus
 
->
 
isFocused
 
=
 
false

 
}

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Here, we use theinteractionSourcepassed in in the constructor to collect the interactions with the component using this indication. We’re now interested only in the Focus-interactions, but theinteractionSource.interactionsalso contains, for example, pressed-interactions, so this would be the place to handle them, too, if you wanted to create, for example, a custom pressed-styles.

Then, in theContentDrawScope.draw, let’s draw the focus indicator:

override
 
fun
 
ContentDrawScope
.
draw
()
 
{

 
drawContent
()

 
if
 
(
isFocused
)
 
{

 
drawRect
(

 
color
 
=
 
color
,

 
topLeft
 
=
 
Offset
(

 
x
 
=
 
0f
,

 
y
 
=
 
size
.
height
 
-
 
8f

 
),

 
size
 
=
 
Size
(

 
width
 
=
 
size
.
width
,

 
height
 
=
 
12f

 
)

 
)

 
}

}

Enter fullscreen mode

Exit fullscreen mode

We first draw the content withdrawContent, and then, ifisFocusedis true, we draw a rect 12 pixels high under the component. We want to offset it slightly to position it correctly. For the color, we use thecolorthat’s passed in in the constructor.

The next step is to use thisFocusNode. We’ll create a data class that extends theIndicationNodeFactory:

private
 
data class
 
FocusIndication
(

 
val
 
color
:
 
Color

)
 
:
 
IndicationNodeFactory
 
{

 
override
 
fun
 
create
(

 
interactionSource
:
 
InteractionSource

 
):
 
Modifier
.
Node
 
{

 
return
 
FocusNode
(
interactionSource
,
 
color
)

 
}

}

Enter fullscreen mode

Exit fullscreen mode

In the example, we override thecreatefunction and return an instance of theFocusNodewe created. Finally, we define the modifier that takes in aninteractionSource, and call itfocusIndication:

@Composable

fun
 
Modifier
.
focusIndication
(

 
interactionSource
:
 
MutableInteractionSource

):
 
Modifier
 
{

 
val
 
focusColor
 
=
 
MaterialTheme
.
colorScheme
.
surfaceTint

 
val
 
focusIndication
 
=
 
remember
 
{

 
FocusIndication
(

 
color
 
=
 
focusColor

 
)

 
}

 
return
 
indication
(
interactionSource
,
 
focusIndication
)

}

Enter fullscreen mode

Exit fullscreen mode

First, we have thefocusColorvariable, which, in this example, is thesurfaceTintfrom the theme colors. As mentioned at the beginning of the post, it should have a color contrast ratio of at least 3:1 with the same pixels in the non-focused state. This means it’s good to have dedicated light- and dark-theme colors, because it’s hard to find a single color that meets the requirements for both modes.

After that, we remember theFocusIndicationwe created, passingfocusColoras thecolorparameter. Finally, we return anindicationmodifier with theinteractionSourceandfocusIndication.

### Hiding the Indicator on Touch Mode

Sometimes, we want to hide the focus indicator in touch mode, because it becomes visible too often when the user interacts with interactive components, or there is some manual focus management for a reason or another. It’s possible withInputModeManager’s help.

First, for theFocusNode, let’s add one more interface it extends,CompositionLocalConsumerModifierNode:

class
 
FocusNode
(

 
…

)
 
:
 
Modifier
.
Node
(),
 

DrawModifierNode
,
 

CompositionLocalConsumerModifierNode
 
{

 
…

}

Enter fullscreen mode

Exit fullscreen mode

This way, we can use the value of theLocalInputModeManager, and read its input mode:

override
 
fun
 
ContentDrawScope
.
draw
()
 
{

 
drawContent
()

 
val
 
inputMode
 
=
 
currentValueOf
(
LocalInputModeManager
).
inputMode

 
if
 
(
isFocused
 
&&
 
inputMode
 
==
 
InputMode
.
Keyboard
)
 
{

 
…

 
}

}

Enter fullscreen mode

Exit fullscreen mode

We read the value withcurrentValueOf(LocalInputModeManager).inputMode, check that the mode isInputMode.Keyboard, and draw the focus indication only then.

Alright, now we have the focus indicator ready. How do we use it?

## Using the Focus Indication Modifier

The exact usage depends on the component. For components that have built-in interaction, such as buttons or text fields, it’s straightforward. We define an interaction source, pass it to the component’sinteractionSourceparameter, and then call thefocusIndicationmodifier with the sameinteractionSource:

val
 
buttonInteractionSource
 
=
 
remember
 
{
 
MutableInteractionSource
()
 
}

Button
(

 
modifier
 
=
 
Modifier
.
focusIndication
(
buttonInteractionSource
),

 
interactionSource
 
=
 
buttonInteractionSource
,

 
onClick
 
=
 
{}

)
 
{

 
Text
(
"A Button"
)

}

Enter fullscreen mode

Exit fullscreen mode

For a custom component that uses modifiers such asclickable,toggleable, orselectablefor interactivity, adding a custom focus indicator requires a little bit more.

In the following example of a Switch row, I’ve omitted the parts that are strictly out of the focus indication-scope for clarity:

val
 
switchInteractionSource
 
=
 
remember
 
{
 
MutableInteractionSource
()
 
}

Row
(

 
modifier
 
=
 
Modifier

 
.
focusIndication
(
switchInteractionSource
)

 
.
toggleable
(

 
…

 
indication
 
=
 
ripple
(),

 
interactionSource
 
=
 
switchInteractionSource

 
),

)
 
{

 
Text
(

 
"A switch"

 
)

 
Switch
(

 
…

 
interactionSource
 
=
 
switchInteractionSource
,

 
)

}

Enter fullscreen mode

Exit fullscreen mode

We define an interaction source and call itswitchInteractionSource. Then, we pass that interaction source to atoggleablemodifier we’re using to make the whole row toggleable. We also pass in the indication asripple()- otherwise, there wouldn’t be the ripple effect on touch.

Finally, we also pass the interaction source toSwitch, so that if the user clicks the switch component, the ripple would be visible across the whole row.

## Wrapping Up

In this blog post, we’ve discussed adding custom focus indicators to interactive Compose components. We’ve looked into theIndicationAPI and how to use it, as well as creating a custom modifier to wrap the logic for easier use. You can find thecomplete code in this Github gist.

I have a follow-up post idea: building different kinds of focus indicators to show that you can actually get a little creative with them.

## Links in the Blog Post

* It's All About (Accessibility) Focus And Compose
* SC 2.4.13 Focus Appearance
* Accessibility focus indicator in Jetpack Compose
* Indication API
* complete code in this Github gist

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse