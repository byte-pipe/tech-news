---
title: 'HTML is getting cool again: Meet the Invoker Commands API - DEV Community'
url: https://dev.to/ale3oula/html-is-getting-cool-again-meet-the-invoker-commands-api-1367
site_name: devto
content_file: devto-html-is-getting-cool-again-meet-the-invoker-comman
fetched_at: '2026-08-23T11:19:11.027694'
original_url: https://dev.to/ale3oula/html-is-getting-cool-again-meet-the-invoker-commands-api-1367
author: Alexandra
date: '2026-08-22'
description: For years, frontend development has had a slightly embarrassing relationship with HTML. We all read... Tagged with webdev, a11y.
tags: '#webdev, #a11y'
---

Exposes how LLMs miss modern browser capabilities

For years, frontend development has had a slightly embarrassing relationship with HTML. We all read about semantic HTML, we talk about using the right landmarks, the right attributes, accessible forms, and meaningful elements. And then we go back to writing React.

While the whole industry is obsessed with AI, browsers are shipping features that make the platform even more capable. Features that let us remove JS, reduce state, and express UI behaviour in HTML. But since AI is trained in the past, these are ignored or not recommended enough through old patterns.

## State boilerplate to open a dialog

Historically, in order to open a dialog or a popover, we need a chunk of custom boilerplate code.

<button
 
id=
"open-dialog"
>
Open dialog
</button>

<dialog
 
id=
"my-dialog"
>

 
<p>
Dialog content
</p>

 
<button
 
id=
"close-dialog"
>
Close
</button>

</dialog>

<script>

 
const
 
dialog
 
=
 
document
.
getElementById
(
"
my-dialog
"
);

 
document
.
getElementById
(
"
open-dialog
"
).
addEventListener
(
"
click
"
,
 
()
 
=>
 
{

 
dialog
.
showModal
();

 
});

 
document
.
getElementById
(
"
close-dialog
"
).
addEventListener
(
"
click
"
,
 
()
 
=>
 
{

 
dialog
.
close
();

 
});

</script>

Enter fullscreen mode

Exit fullscreen mode

We need a button to open our dialog, the dialog itself, and then we write JS to explain the interaction to the browser: "When the user clicks the button, open the dialog".

If you're using React or Vue, this can get even more elaborate: You need some custom state, potentially pass it to your component, wire up an event handler, and then make sure everything stays in sync.

Whether vanilla or framework, the code above is completely reasonable on its own, every frontend developer has written something similar a hundred times. But after writing it for the thousandth time, it made me wonder: do we really need application state to represent that a dialog is open? The answer is: it depends. Sometimes state is needed. But sometimes we're just rebuilding behaviour that HTML and the browser can already provide for us out of the box in 2026.

## Enters the chat: the Invoker Commands API

The Invoker Commands API provides us a way to declaratively assign behaviours to buttons, which then allows us to control these interactive elements. Instead of adding an event listener we can describe the relationship directly in HTML.

The attributes that help us arecommandForandcommand:

* commandFor: turns our button into a "command invoker". It takes the ID of the element to control as its value.
* command: Specifies the action to be performed on that element.

<
button
 
commandfor
=
"
mycoolpopover
"
 
command
=
"
toggle-popover
"
>

 
Toggle
 
the
 
popover

<
/button
>

<
section
 
id
=
"
mycoolpopover
"
 
popover
>

 
<
button
 
commandfor
=
"
mycoolpopover
"
 
command
=
"
hide-popover
"
>
Close
<
/button
>

 
Awesome
 
Popover
 
content

<
/section
>

Enter fullscreen mode

Exit fullscreen mode

### How to do it in React?

All of these are transferable to your framework of choice:

export
 
function
 
DeleteButton
()
 
{

 
return 
(

 
<>

 
<
button
 
command
=
"
show-modal
"
 
commandFor
=
"
delete-dialog
"
>

 
Delete
 
account

 
<
/button
>

 
<
dialog
 
id
=
"
delete-dialog
"
>

 
<
h2
>
Delete
 
account
?
<
/h2
>

 
<
p
>
This
 
cannot
 
be
 
undone
.
<
/p
>

 
<
button
 
command
=
"
close
"
 
commandFor
=
"
delete-dialog
"
>

 
Cancel

 
<
/button
>

 
<
/dialog
>

 
<
/
>

 
);

}

Enter fullscreen mode

Exit fullscreen mode

The important detail here is that React's JSX property is commandFor, while the resulting HTML attribute is commandfor

### Is that a really big deal?

At a first glance this looks like saving, maybe 10 lines of code. That's nice. But the most interesting is the shift of the responsibilities from us, back to the browsers.

The browser isn't becoming less capable because we're writing less JavaScript, but rather the opposite. We finally need less JS.

### Browser support

Now, before everyone starts deleting their dialogs, there is a small catch: The Invoker Commands API is new. MDN currently lists it as Baseline 2025, with cross-browser availability in the latest browser versions since December 2025. Older browsers may not support it.

### References

* MDN — Invoker Commands API
* MDN —<button>element
* MDN —<dialog>element
* MDN — Using the Popover API

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse