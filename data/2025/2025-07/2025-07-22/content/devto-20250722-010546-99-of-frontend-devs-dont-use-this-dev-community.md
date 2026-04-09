---
title: 99% of frontend devs don't use this - DEV Community
url: https://dev.to/moruno21/99-of-frontend-devs-dont-use-this-1g44
site_name: devto
fetched_at: '2025-07-22T01:05:46.144846'
original_url: https://dev.to/moruno21/99-of-frontend-devs-dont-use-this-1g44
author: Antonio Moruno Gracia
date: '2025-07-14'
description: In the React world, most developers don’t think twice before using closures in their component render... Tagged with frontend, react, typescript, webdev.
tags: '#frontend, #react, #typescript, #webdev'
---

In the React world, most developers don’t think twice before usingclosuresin their component render methods, especially when mapping over lists.

But what if I told you there's an underutilized, yet powerful alternative that can help with performance, readability, and even better integration with tools?

Let’s talk aboutHTML data-* attributes: a feature that’s rarely used by frontend developers, but deserves a second look.

## ❓ What are data-* Attributes?

HTML’sdata-*attributes allow you toembed custom data inside DOM elements. In plain HTML:

<
div

data
-
user
-
id
=
"
123
"

data
-
role
=
"
admin
"
>
John
<
/div
>

Enter fullscreen mode

Exit fullscreen mode

InReact, you can use them the same way:

<
div

data
-
user
-
id
=
{
user
.
id
}

data
-
role
=
{
user
.
role
}
>


{
user
.
name
}

<
/div
>

Enter fullscreen mode

Exit fullscreen mode

They are accessible in event handlers via the dataset object:

e
.
currentTarget
.
dataset
.
userId
;

Enter fullscreen mode

Exit fullscreen mode

## 🧠 The Common Pattern: Closures in .map()

Let’s say you’re rendering a list of items:

{
items
.
map
((
item
)

=>

(


<
button

key
=
{
item
.
id
}

onClick
=
{()

=>

handleClick
(
item
.
id
)}
>


{
item
.
name
}


<
/button
>

))}

Enter fullscreen mode

Exit fullscreen mode

This works fine. It’s readable and easy to write.

But behind the scenes,you're creating a new function for each item on every render: a closure that capturesitem.id.

In many apps, this has no practical impact. However...

## ⚠️ The Downsides of Closures

While closures are a fundamental part of JavaScript and React, using them inside.map()can have drawbacks:

### 1. Unnecessary Re-Renders

If you're usingReact.memo,React.useCallback, or virtualized lists (likereact-window),new function references can cause unwanted re-renders. Since the function is recreated every time, memoization doesn't help.

### 2. Harder to Optimize

Imagine you're building a highly interactive list that renders hundreds of items. Minimizing re-renders becomes important, andinline closures can work against that.

## ✅ The Alternative:data-*

Instead of creating a closure for each item, attach metadata directly to the DOM usingdata-*:

function

handleClick
(
e
)

{


const

id

=

e
.
currentTarget
.
dataset
.
id
;


console
.
log
(
"
Clicked item:
"
,

id
);

}

{
items
.
map
((
item
)

=>

(


<
button

key
=
{
item
.
id
}

data
-
id
=
{
item
.
id
}

onClick
=
{
handleClick
}
>


{
item
.
name
}


<
/button
>

))}

Enter fullscreen mode

Exit fullscreen mode

* Single function reference→ plays nicely withReact.memoorReact.useCallback
* Improved performancefor large lists or re-render-sensitive components

## 🤔 So Why Isn’t Everyone Doing This?

Because closures are easy, intuitive, and performant enough for most apps.data-*feels a bit "old-school," and it’s rarely mentioned in modern React/Frontend tutorials.

But in situations where performance or memoization matters,this approach can be a hidden gem.

## ✨ In Summary

Whiledata-*attributes aren’t a common tool in a React developer’s toolbox, they offer real advantages in specific scenarios:

* Reduce unnecessary function creations
* Improve memoization and rendering performance
* Enable simpler and cleaner event handling

They’re not a replacement for closures, but they’re a great alternative when performance or architecture calls for it.

Have you ever useddata-*attributes like this? Or do you usually stick with closures?I’d love to hear your thoughts and experiences!

I hope you found this post interesting. Let me know what you think in the comments 👇

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (44 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
