---
title: React vs Backbone in 2025
url: https://backbonenotbad.hyperclay.com/
site_name: hackernews_api
fetched_at: '2025-10-26T11:08:25.375492'
original_url: https://backbonenotbad.hyperclay.com/
author: mjsu
date: '2025-10-25'
description: A comparison between a React and Backbone password strength app
tags:
- hackernews
- trending
---

## 15 Years of Progress

Look at the two implementations above. The code is roughly the same length. They do exactly the same thing. One was written with a framework from 2010, the other with a framework that's had countless developer hours and a massive ecosystem behind it for over a decade.

The interesting part isnothow much better React is—it's how little progress we've actually made.

### The Illusion of Simplicity

Reactlookscleaner. It reads better at first glance. But that readability comes at a cost: you're trading explicit simplicity for abstraction complexity.

The Backbone code is brutally honest about what it's doing. An event fires, a handler runs, you build some HTML, you put it in the DOM. It's verbose, sure, but there's no mystery. A junior developer can trace exactly what happens and when. The mental model is straightforward: "when this happens, do this."

The React code hides a lot. And once you move past simple examples, you hit problems that don't make sense until you understand React's internals.

Your input mysteriously clears itself. Turns out you switched a list item's key from a stable ID to an index, so React thinks it's a completely different component and remounts it, wiping state. Or maybe you forgot thatvaluecan't beundefined—React saw it flip from uncontrolled to controlled and reset the input.

You add auseEffectto fetch data, and suddenly your app is stuck in an infinite loop. The dependency array includes an object that gets recreated every render, so React thinks it changed and runs the effect again. Now you needuseMemoanduseCallbacksprinkled everywhere to "stabilize identities," which is a thing you never had to think about before.

Your click handler sees old state even though you just set it. That's a stale closure—the function captured the value from when it was created, and later renders don't magically update it. You either need to put the state in the dependency array (creating a new handler every time) or use functional updates likesetState(x => x + 1). Both solutions feel like workarounds.

### Magic Has a High Price

These aren't edge cases. They're normal problems you hit building moderately complex apps. And debugging them requires understanding reconciliation algorithms, render phases, and how React's scheduler batches updates. Your code "just works" without you needing to understand why it works, which is nice until it breaks.

People say"you need to rebuild React from scratch to really understand it,"and they're right. But that's kind of damning, isn't it? You shouldn't need to understand virtual DOM diffing, scheduling priorities, and concurrent rendering to build a password validator.

Backbone might be tedious, but it doesn't lie to you. jQuery is hackable. You can view source, understand it, and add to it easily. It's just DOM methods. React's abstraction layers make that much harder.

### So, What's Next?

We understand the problem:event + state = UI. That's it. That's what both of these implementations are solving.

For massive apps with 1,000 components on the same page, maybe React's complexity is justified. But what the other 99% of apps? What about small apps that just want to do a job and don't need all the magic?

Is there a better model? Something feels as hard and steady as the DOM, but still feels intuitive to write? Something hackable like Backbone and jQuery were, where you can pop open devtools and understand what's happening?

—panphora
