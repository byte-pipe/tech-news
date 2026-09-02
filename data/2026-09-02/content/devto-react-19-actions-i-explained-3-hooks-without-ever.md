---
title: 'React 19 Actions: I Explained 3 Hooks Without Ever Explaining What an Action Is - DEV Community'
url: https://dev.to/shubhradev/react-19-actions-i-explained-3-hooks-without-ever-explaining-what-an-action-is-m79
site_name: devto
content_file: devto-react-19-actions-i-explained-3-hooks-without-ever
fetched_at: '2026-09-02T14:58:57.871876'
original_url: https://dev.to/shubhradev/react-19-actions-i-explained-3-hooks-without-ever-explaining-what-an-action-is-m79
author: Shubhra Pokhariya
date: '2026-09-01'
description: Three parts into this series, and if you'd asked me to define the word sitting underneath every... Tagged with react, javascript, webdev, programming.
tags: '#react, #javascript, #webdev, #programming'
---

Didactic reverse-engineering of core concepts

Three parts into this series, and if you'd asked me to define the word sitting underneath every single hook I'd taught you, I'm not sure I could have done it cleanly. That's not false modesty. Go back and read Parts 1 through 3. I used the word "Action" constantly. I never once stopped to say what one actually is.

Part 1opened with three state variables I'd hand-rolled for years, a result, a pending flag, an error, and showed howuseActionStatecollapses all three into one call.Part 2took a comment box and made it feel instant before the server had even replied.Part 3let a submit button three components away read a form's pending state with zero props passed down. Three different problems, three different hooks, and every single one of them was quietly leaning on the same mechanism without me ever naming it out loud.

That's the gap this post closes. Not a new bug this time. The concept the last three bugs were all symptoms of.

## The word I kept using and never defined

Here's the actual definition, straight from React's own docs, not a paraphrase I'm softening for effect. A function called insidestartTransitionis an Action. That's it. That's the whole qualifying test.

async
 
function
 
submitFeedback
(
previousState
,
 
formData
)
 
{

 
const
 
message
 
=
 
formData
.
get
(
"
message
"
);

 
await
 
saveFeedback
(
message
);

 
return
 
{
 
sent
:
 
true
 
};

}

Enter fullscreen mode

Exit fullscreen mode

That function above could sit in your codebase forever and never once behave like an Action. What flips the switch has nothing to do with anything written inside it. It's entirely about the doorway it walks through. Four doorways do this: a directstartTransitioncall,useTransition's version of the same call, a form'sactionprop taking a function instead of a string, oruseActionState. Walk a function through any of them and it stops being a plain async function you're tracking by hand. What React takes over automatically is the Transition itself, the pending tracking underneath it. What it does not universally hand you is the function's return value.useTransitiongives youisPendingand nothing else, a rawstartTransitioncall doesn't return anything at all.useActionStateis the one doorway built specifically to catch that return value and hold onto it as state, which is exactly whyisPendingand a real result showed up together back in Part 1 and nowhere else in this series. More on the ordering side of this onceuseTransitionshows up properly below.

Once that clicked for me, Parts 1 through 3 stopped looking like three separate hooks and started looking like three different windows onto the same room.useFormStatusreads the pending status of the nearest parent form, and now you know why, that pending status only exists in the first place because something wrapped the submission in a Transition.useOptimisticis the odd one out. It isn't a door into becoming an Action at all. It's a setter you call from inside one that's already running. Call it outside a Transition and it just won't behave the way Part 2 showed you.

## Why any of this needed inventing

Part 1's opening line still holds up: every form needed the same three pieces of state, wired by hand, every time. That pattern wasn't unique to forms either. A delete button, a follow toggle, a checkout step, all needed the identical scaffolding rebuilt from scratch. React 19 added the ability to use async functions inside transitions in the first place, which is the foundation everything else in this series stands on. What you build on that foundation, whether you get a tracked result back or just a pending flag, depends on which of the four doorways you actually walk through.useActionStateis the one that goes furthest, catching the return value as state. The others give you less by design.

## <form action={fn}>, and the three things nobody tells you change

Before Actions existed, a form's only real path to running code wasonSubmit, and that path came with requirements you had to remember every time. CallpreventDefault, manually constructFormDatafrom the event target, manage loading and error state by hand.

function
 
OldForm
()
 
{

 
function
 
handleSubmit
(
e
)
 
{

 
e
.
preventDefault
();

 
const
 
formData
 
=
 
new
 
FormData
(
e
.
target
);

 
// run the request, manage loading and error state yourself

 
}

 
return
 
<
form
 
onSubmit
=
{
handleSubmit
}
>
{
/* ... */
}
</
form
>;

}

Enter fullscreen mode

Exit fullscreen mode

SwaponSubmitfor a function passed straight toactionand the mental model shifts more than the syntax suggests. Nothing callspreventDefault, not because you forgot it, but because React already knows this is an Action before the form ever fires, so the browser's default full-page reload was never going to happen in the first place. The function also stops receiving an event. It receivesFormDatadirectly, already built from every named field on the page, which is one less step you used to write by hand every time. And the request method itself stops being something you configure at all. A function passed toactionalways submits as POST, whatever you write in amethodattribute sitting right next to it. That last one is the exact fact Part 3 ran into from theuseFormStatusside, back whenmethodkept coming back'post'no matter what I expected walking in. It was never reading an attribute. It was reading the Action underneath it.

onSubmitstill earns its keep for one job specifically. Anything that has to stop a submission before it starts, checking two password fields match, belongs there. By the time code inside the Action itself runs, the submission has already begun, so nothing in there can be the thing that prevents it.

## Sync Actions exist. They're just not interesting

An Action doesn't have to be async. A plain synchronous function handed to the same four doors still counts, React still manages its lifecycle, but the pending window is usually too short to build UI around.

function
 
resetSearch
(
previousState
,
 
formData
)
 
{

 
return
 
{
 
query
:
 
""
 
};

}

Enter fullscreen mode

Exit fullscreen mode

The instantawaitshows up inside that function, everything from Parts 1 through 3 becomes worth having. React 18 requiredstartTransition's callback to be synchronous. React 19 dropped that restriction, and that single change is what letuseActionState,<form action={fn}>, anduseTransitionall accept async functions directly instead of you managing the async boundary by hand.

## Client Actions and Server Functions are not the same word twice

Everything in this series so far has been a client Action, code that runs in the browser whether or not it talks to a server underneath. That version works identically in any React 19 setup, no framework required.

Server Functions are a related but genuinely separate idea, and they only exist in frameworks with Server Component support, Next.js being the obvious one. React's own docs are specific about the relationship here, and it's worth getting right instead of using the two terms interchangeably like I nearly did drafting this: a Server Function only becomes a Server Action once it's passed to anactionprop or called from inside an Action. Not every Server Function is a Server Action. Every Server Action used this way is a Server Function.

"
use server
"
;

export
 
async
 
function
 
submitFeedback
(
formData
)
 
{

 
const
 
message
 
=
 
formData
.
get
(
"
message
"
);

 
await
 
db
.
feedback
.
create
({
 
message
 
});

}

Enter fullscreen mode

Exit fullscreen mode

That singleformDataargument is the shape a Server Function receives when it's handed directly to a form'sactionprop. It's worth flagging because it's not interchangeable withuseActionStateas-is, which always calls its function with(previousState, formData), the two-argument shape Part 1 introduced. Reusing server logic throughuseActionStatemeans writing for that shape from the start, not dropping in a single-argument version and hoping React adapts it for you. It won't.

## The fourth door: useTransition

useTransitionhasn't come up by name once in this series, and the mechanism it exposes has been running underneath every single example anyway. Calling it gives you exactly two things back, anisPendingflag and astartTransitionfunction.

Every checkout example so far ran inside a<form>, which wraps its Action in a Transition automatically.useTransitionis for when there's no form to lean on. Picture a wishlist heart icon sitting on a product card, no form anywhere near it, just a click handler that needs to hit the server and report whether it's pending.

import
 
{
 
useTransition
,
 
useState
 
}
 
from
 
"
react
"
;

function
 
WishlistButton
({
 
productId
,
 
isSaved
,
 
toggleWishlist
 
})
 
{

 
const
 
[
isPending
,
 
startTransition
]
 
=
 
useTransition
();

 
const
 
[
saved
,
 
setSaved
]
 
=
 
useState
(
isSaved
);

 
function
 
handleClick
()
 
{

 
startTransition
(
async 
()
 
=>
 
{

 
setSaved
(
!
saved
);

 
const
 
result
 
=
 
await
 
toggleWishlist
(
productId
);

 
startTransition
(()
 
=>
 
{

 
setSaved
(
result
.
saved
);

 
});

 
});

 
}

 
return 
(

 
<
button
 
onClick
=
{
handleClick
}
 
disabled
=
{
isPending
}
 
aria-pressed
=
{
saved
}
>

 
{
saved
 
?
 
"
♥ Saved
"
 
:
 
"
♡ Save
"
}

 
</
button
>

 
);

}

Enter fullscreen mode

Exit fullscreen mode

Notice that second, nestedstartTransitionwrappingsetSavedafter theawait. If that looks familiar, it should, it's the exact same shape asonConfirmedgetting wrapped in its ownstartTransitionback in Part 2's comment box. That's not two separate patterns you happened to see twice. React only automatically tracks synchronous work as part of a Transition. Anything after anawaitneeds its ownstartTransitioncall to still count, whether you're inside a comment form or a heart icon with no form in sight.

Notice too that the wishlist button above reaches for plainuseState, notuseOptimistic. That's not an oversight. This example exists to isolate whatuseTransitiongives you entirely on its own, before any of the other three hooks get involved. In a real app you'd almost certainly reach foruseOptimistichere instead, the exact instant-feedback job it was built for back in Part 2. Showing it with bareuseStatefirst is the only way to actually see whatuseTransitionalone is doing.

Here's the part that's easy to miss and expensive to find out the hard way. Click that heart, unclick it, click it again fast, and a rawuseTransitioncall gives you no guarantee about which result lands last. React says so directly: Actions inside a Transition don't guarantee execution order on their own. What's easy to assume, and what I nearly wrote into this section before checking, is that<form action={fn}>is just as exposed to that same problem as a bareuseTransitioncall. It isn't. React's own docs group<form>actions together withuseActionStateas the two built-in ways that already handle ordering for you. It's rawuseTransition, used on its own with nothing else wrapping it, that gets no such guarantee, the wishlist button above included. If you've been assuming that guarantee comes from Actions in general, it doesn't. It's specifically whatuseActionStateand<form>actions add on top of the raw mechanism.

## Where the four actually sit next to each other

You need to...

Reach for

Own a form's result and pending state in one place

useActionState

Show the finished UI before the server has confirmed it

useOptimistic

Read a form's pending state from a component that isn't managing it

useFormStatus

Run an Action outside a form and track its pending state

useTransition

They were never four competing answers to "which hook should I learn." They're four answers to four different questions that happen to share one mechanism underneath. The checkout form from Part 3 already proved it by combining two of them across four separate components,useActionStateowning the submission,useFormStatuslettingPlaceOrderButtonread pending state with nothing passed down. Here's that same order form with a third hook layered on, a promo code that discounts the total the moment the form is submitted with it, before the server has confirmed anything.

import
 
{
 
useActionState
,
 
useOptimistic
 
}
 
from
 
"
react
"
;

import
 
{
 
useFormStatus
 
}
 
from
 
"
react-dom
"
;

async
 
function
 
placeOrder
(
previousState
,
 
formData
)
 
{

 
const
 
result
 
=
 
await
 
submitOrder
(
formData
);

 
return
 
{
 
orderId
:
 
result
.
id
,
 
error
:
 
null
 
};

}

function
 
PlaceOrderButton
()
 
{

 
const
 
{
 
pending
 
}
 
=
 
useFormStatus
();

 
return 
(

 
<
button
 
type
=
"submit"
 
disabled
=
{
pending
}
>

 
{
pending
 
?
 
"
Placing order...
"
 
:
 
"
Place order
"
}

 
</
button
>

 
);

}

function
 
OrderForm
({
 
cartTotal
 
})
 
{

 
const
 
[
state
,
 
formAction
]
 
=
 
useActionState
(
placeOrder
,
 
{

 
orderId
:
 
null
,

 
error
:
 
null
,

 
});

 
const
 
[
displayTotal
,
 
applyDiscount
]
 
=
 
useOptimistic
(

 
cartTotal
,

 
(
current
,
 
discount
)
 
=>
 
current
 
-
 
discount
,

 
);

 
function
 
handleSubmit
(
formData
)
 
{

 
if 
(
formData
.
get
(
"
promoCode
"
)
 
===
 
"
SAVE10
"
)
 
{

 
applyDiscount
(
10
);

 
}

 
formAction
(
formData
);

 
}

 
return 
(

 
<
form
 
action
=
{
handleSubmit
}
>

 
<
p
>
Total: $
{
displayTotal
.
toFixed
(
2
)
}
</
p
>

 
<
input
 
name
=
"promoCode"
 
placeholder
=
"Promo code"
 
/>

 
<
PaymentFields
 
/>

 
<
PlaceOrderButton
 
/>

 
</
form
>

 
);

}

Enter fullscreen mode

Exit fullscreen mode

useActionStatestill owns the real submission the same way it did in Part 3.useOptimisticshows the discounted total the moment the form submits withSAVE10in the field, no waiting onsubmitOrderto confirm anything first, and it falls back on its own to whatevercartTotalcurrently is once the Transition settles. That fallback detail matters more than it looks. This trimmed-down version never actually updatescartTotalaftersubmitOrderresolves, so the discount would vanish the instant the Action finishes, same trap Part 2 walked through withonConfirmed. A real version needs the parent to fold the confirmed, discounted total back intocartTotalonce the order actually goes through, or the optimistic value has nothing real to settle into.useFormStatusstill letsPlaceOrderButtondisable itself with nothing passed down fromOrderForm. Three hooks, one form, none of them stepping on the other's job.

## The mistake I nearly baked into this whole series

Here's the trap I think this series set without meaning to. Teach one hook per post, three posts in a row, and a careful reader could walk away thinking the real task was picking a favorite, useActionState or useOptimistic or useFormStatus, as if only one of them belongs in a given form. That was never true. Composition was always the point. A real form rarely reaches for exactly one of these. It reaches for whichever two or three actually solve the piece of the problem sitting in front of it, and none of them are competing for the same job.

I built this series backwards on purpose, honestly, three concrete bugs before the concept underneath them, because I think a concept sticks harder once you've already felt the shape of the problem it solves. But it only works if the concept actually shows up eventually. This is that part.

If you want the deeper cut, sync versus async Actions in more detail, the full Server Functions section, and a proper FAQ, I wrote the complete version on my site:React 19 Actions Explained.

If you'd rather test what actually stuck first, I also built a 15-question quiz covering the same four APIs:React 19 Actions Quiz.

So here's the real question, the one I'd genuinely like an answer to. Which of these four have you already been using without knowing you were touching an Action? A<form action={fn}>you wired up because it looked simpler thanonSubmit, astartTransitioncall you copied from somewhere without reading what it does, a button that felt laggy until you wrapped it inuseTransitionand never asked why that fixed it. Drop it below. I'm curious how many of us have been using this mechanism for months without a name for it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse