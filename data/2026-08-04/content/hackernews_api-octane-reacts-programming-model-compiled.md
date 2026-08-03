---
title: Octane — React's programming model, compiled
url: https://octanejs.dev
site_name: hackernews_api
content_file: hackernews_api-octane-reacts-programming-model-compiled
fetched_at: '2026-08-04T06:00:21.744205'
original_url: https://octanejs.dev
author: nnx
date: '2026-08-03'
description: Octane — React's programming model, compiled ahead of time. No VDOM, no rules of hooks.
tags:
- hackernews
- trending
---

# React’s programming model,compiled.

The successor toInferno, built around the same focus on performance. It brings React’s hooks, Suspense, and actions to a compiler-first architecture. No virtual DOM, rules of hooks, or dependency arrays you have to maintain yourself. The compiler tracks what your code uses automatically.

					Get started
				

					Differences from React
				
Counter.tsrx
Copy
// Counter.tsrx — hooks next to output, no rules of hooks

import
 { useState, useEffect } 
from
 'octane'
;

export
 function
 Counter
(
props
) 
@{

	const
 [
count
, 
setCount
] 
=
 useState
(
0
);

	// A hook behind a condition is fine — slots are

	// assigned by call site, not call order.

	if
 (
!
props.paused) {

		useEffect
(() 
=>
 {

			console.
log
(
'count is now'
, count);

		}); 
// the compiler infers [count]

	}

	<
button
 onClick
=
{
() 
=>
 setCount
(count 
+
 1
)
}
>
{
'Count: '
 +
 count
}
</
button
>

}
Live
Count
0
paused
// count is now 0

Forget dependency arrays and rigid hook rules. The compiler tracks what your effects, memos, and callbacks use automatically, so hooks can safely live inside conditions or after early returns.

Independent use() calls start at the same time instead of suspending one by one. Nested fetches begin earlier, and streaming SSR sends each boundary as soon as it’s ready.

Templates compile to cloned DOM nodes with direct updates. The keyed lists move only the nodes they need to. You can still use .tsx components and move to .tsrx one component at a time.

You still get hooks, memo, context, portals, transitions, actions, controlled forms and Suspense. Events use the DOM, refs are regular props, and 53 first-party bindings cover familiar libraries.

11,500+
test executions across the compiler, runtime, SSR and bindings. This count includes reruns in different compiler modes. The core suite has 3,900+ distinct cases. 
React-derived coverage is tracked case by case
.
0

				rules of hooks. Put hooks behind conditions or after an early return.
			
53
first-party ecosystem bindings for state, data, routing, UI, forms, charts, 3D, 
and more

## Your app should feel fast.Your code should still feel familiar.

### What does moving a React app to Octane look like?

An Octane component is still a plain function with props, hooks and context. State lives where you expect it to, and data still flows from parent to child. If you know React, most of Octane will already make sense.

Keep your existing TSX and convert components to TSRX as you go. The component model stays the same, so the migration does not require a redesign. The work is easy to review, whether you do it by hand or with a coding agent.

### Why not build Octane on signals?

Signals are useful, and you can use them in an Octane app when they fit. Octane does not make them the foundation because that would change how every component reads state. Components stay as plain functions that run from top to bottom. The compiler handles the bookkeeping.

The benchmarks show the trade-off.
 Signal-based frameworks lead in workloads designed around signals. Across the suites below, Octane stays competitive without changing the way you structure components. 

						See what TSRX adds →
					

The libraries you already use, ported.

## Add Octane to a React app.One component at a time.

OctaneCompat lets a React 19 app render compiled Octane components. Events inside each island stay native and delegated. Octane components can read your React context withuse(), and they render on the server and hydrate in the browser. You can migrate one component at a time instead of rewriting the app.

React Server Components are the one exception. Hooks, Suspense, context and SSR carry over.

					See how OctaneCompat works →
				
App.tsx
Copy
// App.tsx — your existing React 19 app

import
 { OctaneCompat } 
from
 'octane/react'
;

import
 { Counter } 
from
 './islands/Counter.tsrx'
;

export
 function
 App
() {

	return
 (

		<
div
 className
=
"dashboard"
>

			<
h1
>Ported one component at a time</
h1
>

			{
/* A compiled Octane island, hosted inside React with typed

			 props. Native events, real React context, SSR + hydration. */
}

			<
OctaneCompat
>

				<
Counter
 start
=
{
3
}
 />

			</
OctaneCompat
>

		</
div
>

	);

}

## Three.js,on Octane.

This flame is a live Three.js scene rendered by @octanejs/three, a technical-preview port of React Three Fiber. It loads only when you scroll near it. Drag it to give it a spin.

					Browse all the bindings →
				

## How Octane compares

All suites →

Choose a suite and a few frameworks for the bar chart, or scan the full grid. Each cell
				shows the geometric mean of that framework’s per-operation scores relative to Octane. Lower
				is better.

frameworks
Octane (.tsrx)
React 19
Preact 10
Solid 2.0 beta
Svelte 5
Ripple 0.3
Vue Vapor 3.6 beta
suite
js-framework
todomvc
chat-stream
js-framework-reorder
dbmon
effectful-list
memo-wall
recursive-context
signal-favoring
portal-swarm
async-waterfall
news
streaming-ssr
bundle-size
ssr-throughput
1× Octane
Octane (.tsrx)
1×
Vue Vapor 3.6 beta
1.0×
Ripple 0.3
1.0×
Solid 2.0 beta
1.1×
Svelte 5
1.5×
Preact 10
2.2×
React 19
2.5×
all suites

							vs Octane
						

							vs fastest
						
suite
Octane (.tsrx)
React 19
Preact 10
Solid 2.0 beta
Svelte 5
Ripple 0.3
Vue Vapor 3.6 beta
js-framework
1×
2.5×
2.2×
1.1×
1.5×
1.0×
1.0×
todomvc
1×
2.4×
2.4×
1.2×
1.2×
0.78×
0.91×
chat-stream
1×
3.8×
2.7×
1.4×
2.0×
1.2×
1.1×
js-framework-reorder
1×
2.9×
6.4×
1.5×
2.2×
1.6×
2.2×
dbmon
1×
1.8×
2.0×
2.8×
1.2×
1.2×
1.1×
effectful-list
1×
2.3×
3.6×
0.59×
0.74×
1.0×
0.66×
memo-wall
1×
6.1×
7.5×
0.39×
1.2×
2.4×
0.35×
recursive-context
1×
1.3×
1.0×
1.0×
1.7×
0.82×
0.90×
signal-favoring
1×
5.9×
3.2×
0.66×
0.78×
0.29×
0.31×
portal-swarm
1×
7.6×
9.6×
0.91×
2.8×
3.2×
1.2×
async-waterfall
1×
11×
8.7×
0.90×
0.90×
0.88×
—
news
1×
3.1×
2.0×
1.8×
1.1×
1.8×
1.3×
streaming-ssr
1×
0.99×
1.1×
3.3×
—
0.93×
—
bundle-size
1×
0.94×
0.57×
0.69×
0.81×
0.77×
0.69×
ssr-throughput
1×
2.4×
2.3×
1.6×
0.97×
1.4×
0.86×
geomean
1×
2.9×
2.7×
1.1×
1.3×
1.1×
0.86×

Each cell is that framework’s score relative to Octane (1×), geometric mean across the suite’s operations. Green is faster, red is slower.

Faster
Slower
Octane = 1× baseline