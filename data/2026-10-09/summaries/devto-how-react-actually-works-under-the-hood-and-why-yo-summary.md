---
title: How React Actually Works Under the Hood (And Why Your Mental Model Might Be Wrong) - DEV Community
url: https://dev.to/smtahosin/how-react-actually-works-under-the-hood-and-why-your-mental-model-might-be-wrong-12b8
date: 2026-10-08
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-09T10:16:45.977870
---

# How React Actually Works Under the Hood (And Why Your Mental Model Might Be Wrong) - DEV Community

# How React Actually Works Under the Hood (and Why the Rookie State‑Logging Mistake Happens)

## The Classic Rookie Mistake
- A common pattern: call `setCount(count + 1)` then `console.log(count)` inside the same handler.  
- The console logs the previous value (e.g., logs `0` when the UI shows `1`).  
- The cause is not simply “state is asynchronous”; it’s a misunderstanding of React’s update cycle.

## The Mental Model Trap
- Beginners often think:
  1. `setState` runs immediately.  
  2. React directly mutates the DOM.  
  3. The change is instantly visible.  
- Direct DOM mutation on every state change would be slow because the browser would need to recalculate styles, layout, and repaint each time.

## React’s Real Workflow: Three Distinct Phases
### 1. Trigger Phase
- `setCount` creates an **Update** object and pushes it onto an internal queue attached to the component’s Fiber node.  
- The component is marked “dirty” and work is scheduled with the React Scheduler.  
- Multiple updates in the same event are **batched** together, so React processes them in one go.

### 2. Render Phase (Pure JavaScript)
- “Render” means **calling the component function**, not drawing pixels.  
- JSX is compiled to `React.createElement` calls, which return plain JavaScript objects (the Virtual DOM nodes).  
- React builds a new object tree, then **reconciles** it with the previous tree to compute a minimal set of changes (patch instructions).

### 3. Commit Phase
- The computed patches are applied **synchronously** to the real browser DOM using native APIs (`textContent = '1'`, etc.).  
- Only the nodes that actually changed are touched; the rest of the DOM remains untouched.  
- After the commit, the browser paints the updated pixels.

## Why Hook Order Matters: The Fiber Linked List
- Hooks cannot be called inside loops, conditions, or nested functions because React relies on **call order**, not variable names.  
- Each component’s Fiber node holds a `memoizedState` property that is a **singly‑linked list** of hook objects.  
- During each render, React walks this list with an internal pointer (`workInProgressHook`):
  1. `useState` reads Hook 0, moves pointer to Hook 1.  
  2. `useEffect` reads Hook 1, moves pointer to Hook 2.  
  3. Subsequent `useState` reads Hook 2, etc.  
- Placing a hook inside a conditional changes the order of the list, causing mismatches and the error “Rendered fewer hooks than expected.”

## Takeaway
- State updates are **scheduled**, not applied instantly; the UI reflects the new state only after the commit phase finishes.  
- Understanding the three‑phase cycle and the Fiber‑based hook list prevents the off‑by‑one logging bug and many other subtle issues in React applications.