# Magic Move Animation Engine for Excalidraw

## Core Concept
Built a dynamic animation system enabling **smooth, logic-driven transitions** between diagram states without manual time-lapse editing. Elements automatically connect and animate based on structural changes.

## Key Components

| Component                 | Function                                                                 |
|---------------------------|--------------------------------------------------------------------------|
| **State Diffing**         | Classifies elements as `stable` (unchanged), `entering` (new), or `exiting` (removed) between frames |
| **Transition Logic**      | Automatically categorizes transitions (e.g., movement, color shift) based on element presence and property changes |
| **Property Interpolation**| Applies precise non-linear interpolation for positions (x/y), colors (strokeColor), and angles using shortest-path calculations |

## Implementation Summary

1. **State Categorization**
   Implemented `CategorizeTransition` function using custom `transition-logic` utility to map elements to intermediate states between two frames.

2. **Precision Interpolation**
   Applied specialized calculations for:
   - Positional movement (x/y coordinates)
   - Color transitions (strokeColor)
   - Angular transformations
   *(All using shortest-path interpolation for natural motion)*

## Technical Stack
| Tool                   | Purpose                                      |
|------------------------|----------------------------------------------|
| **Framer Motion**      | Efficient animation playback                 |
| **Next.js**            | React framework integration for SSR capabilities |
| **Custom Utilities**   | Simplified complex logic-driven operations   |
