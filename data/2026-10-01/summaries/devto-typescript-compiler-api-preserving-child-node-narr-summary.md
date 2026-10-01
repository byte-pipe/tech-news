---
title: TypeScript Compiler API: Preserving Child Node Narrowing in Reusable Type Guards 🔧 - DEV Community
url: https://dev.to/nyaomaru/typescript-compiler-api-preserving-child-node-narrowing-in-reusable-type-guards-4pgh
date: 2026-09-30
site: devto
model: llama3.2:1b
summarized_at: 2026-10-01T17:29:15.846131
---

# TypeScript Compiler API: Preserving Child Node Narrowing in Reusable Type Guards 🔧 - DEV Community

## TypeScript Compiler API: Preserving Child Node Narrowing in Reusable Type Guards

### Background

The TypeScript Compiler API provides a way to refine the parsing process, allowing developers to write more robust type checks and transformations. One key aspect of this API is the `isCallExpression` and `isIdentifier` functions, which determine whether a node is a call expression or identifier, respectively.

### Original Problem

Suppose we have a broad `ts.Node` and want to implement reusable type guards that preserve not only the AST node type but also a narrowed child property. The challenge is that the code snippet reproduces a similar problem with plain TypeScript objects, but it's the `child` property that's narrowed.

### What We're Looking For

To solve this, we need to identify the property that's narrowed and refine our type guards accordingly. In this case, it's the `expression` property.

### Solution

To preserve the `expression` property, we can refine our type guards to:

```typescript
// Refine the isCallExpression function to preserve expression:
const isCallWithIdentifierExpression = (node: ts.Node): ts.Node => {
  return ts.isCallExpression(node) && ts.isIdentifier(node.expression);
};
```

### Refining the Predicates

We need to refine the predicates to also preserve the `expression` property:

```typescript
// Refine the isIdentifier function to also preserve expression:
const isIdentifierWithIdentifierExpression = (node: ts.Node): ts.Node => {
  return ts.isIdentifier(node.expression) && ts.isCallExpression(node);
};
```

### Example Usage

Here's an example usage of these refined type guards:

```typescript
const nodes = [
  //...
];

const calls = nodes.filter(isCallWithIdentifierExpression);
// calls:

// Array<

//   ts.CallExpression & {
//     expression: ts.Identifier;
//   }

// >
```

By refining our type guards to preserve both the AST node type and the narrowed `expression` property, we've made it possible to reuse them across multiple transformations and lint rules.