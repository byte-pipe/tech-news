---
title: React 19's useActionState Showed Me Why Disabling My Submit Button Was Never Enough - DEV Community
url: https://dev.to/shubhradev/react-19s-useactionstate-showed-me-why-disabling-my-submit-button-was-never-enough-53jd
site_name: devto
content_file: devto-react-19s-useactionstate-showed-me-why-disabling-m
fetched_at: '2026-07-28T19:33:30.099158'
original_url: https://dev.to/shubhradev/react-19s-useactionstate-showed-me-why-disabling-my-submit-button-was-never-enough-53jd
author: Shubhra Pokhariya
date: '2026-07-28'
description: Every form I ever shipped before React 19 needed the same three pieces of state, and I wired them up... Tagged with react, webdev, javascript, programming.
tags: '#react, #webdev, #javascript, #programming'
---

Comments debate the limits of UI locks

Every form I ever shipped before React 19 needed the same three pieces of state, and I wired them up by hand every single time.

One for the result. One for whether it's submitting. One for the error. And at least once a sprint, I'd forget to reset one of them in the right place and spend twenty minutes staring at a button that wouldn't re-enable.

Here's the version I wrote for years, probably the same one you have sitting in a dozen components right now:

function
 
OldSignupForm
()
 
{

 
const
 
[
error
,
 
setError
]
 
=
 
useState
(
null
);

 
const
 
[
isSubmitting
,
 
setIsSubmitting
]
 
=
 
useState
(
false
);

 
async
 
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

 
setIsSubmitting
(
true
);

 
setError
(
null
);

 
try
 
{

 
await
 
signup
(
new
 
FormData
(
e
.
target
));

 
}
 
catch 
(
err
)
 
{

 
setError
(
err
.
message
);

 
}
 
finally
 
{

 
setIsSubmitting
(
false
);

 
}

 
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

Three state variables. A try/catch/finally. And one bug waiting to happen the moment someone forgets thatfinally.

I didn't think this pattern was a problem until I actually sat down withuseActionStateand realized the workaround I'd been shipping to "fix" double submits was never actually fixing anything.

## The habit that felt safe but wasn't

Here's what I mean. Most of us migrate a form like this by adding some version of:

function
 
handleClick
()
 
{

 
setLocalPending
(
true
);
 
// feels safe, isn't tied to anything real

}

Enter fullscreen mode

Exit fullscreen mode

On a fast connection, you'll never notice this is broken. On a slow one, that local flag can flip back to false before the actual request has resolved. A user on spotty wifi taps "Place Order" twice, maybe three times, because the button looked re-enabled for a split second. Each tap still goes through. React doesn't drop them, and it doesn't race them either. It queues them and runs them one after another, in order. So instead of one order, you've got three, each one processed like it was intentional.

That was the momentuseActionStatestopped feeling like just another hook to memorize. It started feeling like React quietly admitting they had watched enough of us get this wrong and finally built the fix.

## What it actually does

const
 
[
state
,
 
formAction
,
 
isPending
]
 
=
 
useActionState
(
fn
,
 
initialState
);

Enter fullscreen mode

Exit fullscreen mode

You give it a function, React calls that function with(previousState, formData)whenever the form submits, and whatever it returns becomes your newstate.isPendingis tied to React's own transition tracking, not a boolean you're guessing the timing of.

A working example, no framework required, plain React:

import
 
{
 
useActionState
 
}
 
from
 
"
react
"
;

async
 
function
 
subscribe
(
previousState
,
 
formData
)
 
{

 
const
 
email
 
=
 
formData
.
get
(
"
email
"
);

 
if 
(
!
email
 
||
 
!
email
.
includes
(
"
@
"
))
 
{

 
return
 
{
 
success
:
 
false
,
 
message
:
 
"
Enter a valid email.
"
 
};

 
}

 
await
 
new
 
Promise
((
resolve
)
 
=>
 
setTimeout
(
resolve
,
 
800
));

 
return
 
{
 
success
:
 
true
,
 
message
:
 
"
You're subscribed.
"
 
};

}

function
 
NewsletterForm
()
 
{

 
const
 
[
state
,
 
formAction
,
 
isPending
]
 
=
 
useActionState
(
subscribe
,
 
{

 
success
:
 
false
,

 
message
:
 
""
,

 
});

 
return 
(

 
<
form
 
action
=
{
formAction
}
>

 
<
input
 
type
=
"email"
 
name
=
"email"
 
placeholder
=
"you@example.com"
 
/>

 
<
button
 
type
=
"submit"
 
disabled
=
{
isPending
}
>

 
{
isPending
 
?
 
"
Subscribing...
"
 
:
 
"
Subscribe
"
}

 
</
button
>

 
{
state
.
message
 
&&
 
<
p
>
{
state
.
message
}
</
p
>
}

 
</
form
>

 
);

}

Enter fullscreen mode

Exit fullscreen mode

NoonSubmit. NopreventDefault. No separate pending flag to keep in sync. Swapdisabled={isPending}in for that fake local flag, and the double-submit problem you thought you'd solved actually gets solved.

## The part that genuinely surprised me

I assumed rapid clicks would race each other. Maybe the last one wins, maybe the first one does, classic race-condition territory. That's not what happens.

React queues every call to the action function and runs them sequentially. Each one waits for the previous one to finish before it starts. Click "Add to Cart" four times fast and it takes roughly four times as long to settle, not because anything's broken, but because call two is patiently waiting for call one's promise to resolve first. Nothing races. Nothing gets silently dropped.

Which means the real problem was never a corrupted database write. The problem is that every click still counts. Five taps on a slow connection means five processed actions, not one.disabled={isPending}isn't there to prevent a race, since there isn't one. It's there to stop someone from queuing up four actions they never meant to trigger in the first place.

One more thing worth knowing before it bites you. If an earlier call in that queue throws, React skips every call still waiting behind it. Catch your errors and return a state object instead of letting anything throw, or you'll lose queued actions you never even knew were sitting there.

async
 
function
 
submitOrder
(
previousState
,
 
formData
)
 
{

 
try
 
{

 
const
 
result
 
=
 
await
 
placeOrder
(
formData
);

 
return
 
{
 
success
:
 
true
,
 
orderId
:
 
result
.
id
 
};

 
}
 
catch 
(
err
)
 
{

 
return
 
{
 
success
:
 
false
,
 
error
:
 
"
Something went wrong. Try again.
"
 
};

 
}

}

Enter fullscreen mode

Exit fullscreen mode

## Two more traps I walked straight into

Stale closures.If your action function reaches into component-scoped variables instead of pulling straight fromformData.get(...), you're one re-render away from acting on data that's already out of date. Prefer reading submitted values fromformDatainstead of relying on values captured from an earlier render.

Forgetting there's no reset button.useActionStatehas no built-in way to clear its own state. The docs say so plainly. If you need a "start over" button, you have two real options. Teach your action function to recognize a reset signal as one of its inputs, or change the component'skeyprop to force a full remount. The reset-signal route is usually the less disruptive one, since it doesn't tear the DOM down to do it.

## When I don't reach for it

If the interaction needs to feel instant, think a like button or a checkbox, anything where the UI should update before the server has even responded,useActionStatewill always feel a beat too slow for that. That'suseOptimistic's job, and it's worth pairing the two once you've got the basics down.

And if it's a multi-step wizard with controlled inputs across steps that aren't all mounted at once, fighting the uncontrolled-form modeluseActionStateis built on usually costs you more code than it saves.

## The actual takeaway

The pattern you've probably been shipping, disable on click and hope for the best, was hiding the real issue instead of solving it. Every click still lands whether the button looks disabled or not.useActionStatedoesn't just cut boilerplate. It ties your pending state to something real, so the thing you thought you fixed actually gets fixed.

I wrote the full breakdown on my site, including the complete production signup example with field-level validation, the side-by-side comparison table againstuseStateanduseFormStatus, and the accessibility details aroundaria-busyand disabling inputs during a pending state:React 19 useActionState Explained

I honestly thought I understood this pattern until I started testing it properly. It turned out the problem wasn't React at all. It was the way I'd been managing pending state for years.

If you've been relying on your own pending state to handle form submissions, it's worth taking another look. I know I was surprised by what actually happens.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse