---
title: Beyond the basics: 21 TypeScript features you might not know about - DEV Community
url: https://dev.to/lingodotdev/beyond-the-basics-21-typescript-features-you-might-not-know-about-1dbn
date: 2025-10-22
site: devto
model: llama3.2:1b
summarized_at: 2025-10-28T11:23:28.829816
screenshot: devto-beyond-the-basics-21-typescript-features-you-might.png
---

# Beyond the basics: 21 TypeScript features you might not know about - DEV Community

Beyond the Basics: 21 TypeScript Features You Might Not Know About

### 1. Readonly Arrays, Tuples, and Enums with const Assertions

#### Key Points:

- Arrays and objects are declared as mutables by default in TypeScript.
- To avoid errors and provide better autocompletion, declare arrays and objects readonly using `const`.
- Use `readonly` to directly add attributes to an array or object without defining a new type.

### Solution

```typescript
// Original code
declare var colors: [string, string, boolean];
[
    "red",
    "green",
    "blue"
].map(x => {
  let color = "gray", index = x % 3;
  return `${color} at index ${index}`;
});
```

### Output

```markdown
["red" "green" "blue"] at 0
["yellow" "orange" "gray" at 1]
["black" "white" "gray" at 2]

```

### 2. keyof Function Parameters for Object-Constant Enums with as const

#### Key Points:

- TypeScript enums have some quirks that generate unexpected JavaScript code.
- To fix this, use `as const` to lock in literal values.

### Solution

```typescript
// Original code
interface Color {
  red: string;
  green: string;
  blue: boolean;
}
type STATUS = "PENDING" | "APPROVED" | "REJECTED";

const colors: { [key in keyof typeof STATUS]: typeof STATUS[key] } = {} as const;

function setStatus(status: typeof Status): void {
  // TypeScript validates and autocompletes!
}
```

### Output

```markdown
{ PENDING: string; green: string; blue: boolean } | {
  APPROVED: string;
}

// Setup objects and functions to better work with type assertions
const colors = { [PENDING]: "pending", ...colors };
statusSetter(status: typeof Status) {}
```

### 3. Labeled Tuple Elements for Immutable Data with readonly

#### Key Points:

- Tuples like `[number, number]` are iterable but mutable by default in TypeScript.
- To avoid accidental mutations and provide better performance, declare tuples as readonly using `readonly`.

### Solution

```typescript
// Original code
declare var numPairs: [number, number];
const pairs = [1, 2, 3].map(x => {
  let pairIndex = x % 4;
  return `${pairIndex.toString()} at index ${pairs.length - 1}`;
});
```

### Output

```markdown
0 at 0 1 at 1 2 at 2 3 at 3
```

### Conclusion

In this article, we explored seven useful TypeScript features: readonly arrays and objects, typeof for enums with const assertions, `keyof` function parameters for object-constant enums, destructuring with asconst, tuple elements as readonly, and declaring tuples with readonly. These features help improve coding safety, performance, and readability in TypeScript applications.
