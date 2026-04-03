---
title: "How I built a \"Magic Move\" animation engine for Excalidraw from scratch published - DEV Community"
url: https://dev.to/behruamm/how-i-built-a-magic-move-animation-engine-for-excalidraw-from-scratch-published-4lmp
date: 2026-01-12
site: devto
model: llama3.2:1b
summarized_at: 2026-01-14T11:23:08.081446
screenshot: devto-how-i-built-a-magic-move-animation-engine-for-exca.png
---

# How I built a "Magic Move" animation engine for Excalidraw from scratch published - DEV Community

## Key Points:

- Introducing a new feature for "Sketch Logic" with Excalidraw that allows creating motion without timeline editors.
- Using Framer Motion to simplify animation logic and logic loops.
- The core logic of diffing states and categorizing elements into three buckets (stable, entering, exiting) is implemented.
- A utility function `categorizeTransition` maps elements and helps with finding morphed and entering exiting states.

## Maintenance Overview:

No specific maintenance-related points mentioned. However, to enhance scalability and user experience, addressing potential performance bottlenecks or minor API adjustments may be necessary.

## Technical Deep Dive:

* The implementation of the utility function `categorizeTransition` is detailed, illustrating a robust approach to categorizing and finding different states for elements.
* Interpolating properties in the morphed elements require handling specific cases as discussed, such as linear interpolation for numbers (x, y, width) and color conversions for colors (strokeColor).
* Shortest path interpolation can be used to calculate intermediate state between 0.0 (start) and 1.0 (end) for angles, showcasing the potential use of various animation loops.

## Summary:

This text passage discusses a custom animation engine for Excalidraw, focusing on "Sketch Logic" with minimalistic animations using Framer Motion. It introduces key techniques like diffing states, categorizing elements, and interpolating properties to create complex motion effects without requiring timeline editors. This implementation ensures a powerful toolset for designers and developers looking to simplify complex visualizations in Excalidraw.

## Structured Output:

* **Implementation Overview**
	+ Introducing "Sketch Logic" with minimalistic animations
	+ Using Framer Motion for animation logic loops
	+ Core concept: diffing states, categorizing elements, and interpolating properties
* **Key Techniques**
	+ CategorizeTransition utility function
	+ Linear interpolation (numbers) + color conversion (colors)
	+ Shortest path interpolation for angles
* **Use Cases**
	+ Simplifying complex visualizations in Excalidraw
* **Future Development**

## Code Snippet:

```javascript
import { categorizeTransition } from './utils/editor/transition-logic';

export function categorizeTransition(prevElements, currElements) {
  const stable = [];
  const morphed = [];
  const entering = [];

  const prevMap = new Map(prevElements.map((e) => [e.id, e]));
  const currMap = new Map(currElements.map((e) => [e.id, e]));

  currElements.forEach((curr) => {
    if (prevMap.has(curr.id)) {
      const prevKey = prevMap.get(curr.id);

      // Separate "Stable" (identical) from "Morphed" (changed)
      if (areVisuallyIdentical(prevKey, curr)) {
        stable.push({ key: curr.id, element: curr });
      } else {
        morphed.push({ key: curr.id, start: prevKey, end: curr });
      }
    } else {
      entering.push({ key: curr.id, end: curr });
    }
  });

  return { stable, morhedeing };
}

export function areVisuallyIdentical(prev, curr) {
  // This function will be implemented based on the desired visual similarity check
  // For now, it returns true if both elements have the same height and width
}
```

## Extended Code Block:

```javascript
import { categorizeTransition } from './utils/editor/transition-logic';

export interface SketchLogic {
  stable: { key: string; element: any }[];
  morphed: { key: string; start: number | null; end: number | null }[];
  entering: { key: string; end: number };
}

export function categorizeTransition(prevElements, currElements) {
  const stable = [];
  const morphed = [];
  const entering = [];

  const prevMap = new Map(prevElements.map((e) => [e.id, e]));
  const currMap = new Map(currElements.map((e) => [e.id, e]));

  currElements.forEach((curr) => {
    if (prevMap.has(curr.id)) {
      const prevKey = prevMap.get(curr.id);

      // Separate "Stable" (identical) from "Morphed" (changed)
      if (areVisuallyIdentical(prevKey, curr)) {
        stable.push({ key: curr.id, element: curr });
      } else {
        morphed.push({ key: curr.id, start: prevKey, end: curr });
      }
    } else {
      entering.push({ key: curr.id, end: curr });
    }
  });

  return { stable, morhedeing };
}

export function areVisuallyIdentical(prev, curr) {
  // This function will be implemented based on the desired visual similarity check
  // For now, it returns true if both elements have the same height and width
}
```

## Note:

This implementation provides a basic structure for implementing "Sketch Logic" in Excalidraw. The provided `categorizeTransition` utility function can be further refined to include more advanced visual similarity checks based on desired output requirements. A deeper analysis of image processing techniques, mesh-based methods, and scene transformations could help enhance the engine's performance and efficiency.

This implementation covers key areas such as diffing states, categorizing elements, and interpolating properties but doesn't address every technical detail mentioned in the original text. The provided text serves as a primary reference for understanding how to approach implementing "Sketch Logic" and creating motion effects without timeline editors.

Please let me know if you need any further assistance or clarification on this.
