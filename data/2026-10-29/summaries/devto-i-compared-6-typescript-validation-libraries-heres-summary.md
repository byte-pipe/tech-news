---
title: "I Compared 6 TypeScript Validation Libraries. Here's What Surprised Me 🤔 - DEV Community"
url: https://dev.to/nyaomaru/i-compared-6-typescript-validation-libraries-heres-what-surprised-me-325g
date: 2026-10-28
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:09.669273
---

# I Compared 6 TypeScript Validation Libraries. Here's What Surprised Me 🤔 - DEV Community

# The hidden danger of mismatched runtime contracts

## Introduction  
- The author, a frontend engineer who works with TypeScript, questions whether the common “Which validation library should I use?” discussion actually compares tools that solve the same problem.  
- The focus is on the gap between compile‑time types and runtime validation (the “runtime contract”).  
- To explore this, the same `User` validation logic is implemented with seven approaches and then measured for correctness, bundle size, and runtime performance.

## Validation scenario  
- **Type definition**  

```ts
type User = {
  id: string;
  name: string;
  age: number;
  role: "admin" | "user";
  tags: string[];
  profile: {
    bio: string;
    active: boolean;
  };
};
```  

- **Runtime rules**  
  - `id` – string  
  - `name` – 1 to 100 UTF‑16 code units  
  - `age` – integer between 18 and 120  
  - `role` – exactly `"admin"` or `"user"`  
  - `tags` – array of strings  
  - `profile.bio` – string  
  - `profile.active` – boolean  
  - No extra keys allowed at any level  
  - No coercion of values  

The input domain is ordinary JSON‑decoded data, which means the validators must also handle edge cases such as inherited properties, sparse arrays, symbols, getters, and non‑enumerable keys.

## 1. Handwritten guard (type predicate)  
- Implements the contract directly with JavaScript checks and a TypeScript predicate (`value is User`).  
- **Pros**  
  - No extra dependency or learning curve.  
  - Very small bundle size; the code is exactly what runs at runtime.  
- **Cons**  
  - Becomes unwieldy as the number of guards grows (e.g., `isUser`, `isProfile`, `isRole`, …).  
  - Lacks reusable building blocks, error‑reporting, transformation, and integration features that larger libraries provide.  

## 2. is‑kit (small composable guards)  
- Provides tiny, composable guard primitives (`and`, `arrayOf`, `oneOfValues`, `struct`, …) and a `safeParse` helper that returns a success/failure result.  
- **Pros**  
  - Keeps guards small and composable while staying in the predicate world.  
  - Type inference highlights subtle differences (e.g., readonly vs mutable arrays).  
- **Cons**  
  - Does not offer field‑level error objects, transformation pipelines, schema metadata, OpenAPI generation, or form‑library integrations.  
  - When those higher‑level features are needed, a full schema library is a better fit.  

## 3. Runtypes (validator objects)  
- Uses a runtime validator object rather than a plain boolean predicate.  
- Example pattern:  

```ts
import { String as RtString, Number as RtNumber, Literal, Union, Object as RtObject } from "runtypes";

const Name = RtString.withConstraint(v =>
  (v.length >= 1 && v.length <= 100) || "name length must be 1..100"
);

const Age = RtNumber.withConstraint(v =>
  (Number.isInteger(v) && v >= 18 && v <= 120) || "age must be an integer in 18..120"
);

export const UserSchema = RtObject({
  id: RtString,
  name: Name,
  age: Age,
  role: Union(Literal("admin"), Literal("user")),
  tags: RtArray(RtString),
  profile: RtObject({
    bio: RtString,
    active: RtBoolean,
  }),
}).asReadonly(); // optional exactness can be enforced with .asReadonly()
```

- **Pros**  
  - Provides a rich API: `validate`, `check`, `guard`, `decode`, and detailed error trees.  
  - Supports exact object shape checking and can be extended with custom constraints.  
- **Cons**  
  - Larger runtime footprint compared with pure guards.  
  - The API is more opinionated; developers must adopt the Runtypes object model.  

## 4. Valibot, Zod, ArkType, typia (brief overview)  
| Library | Core idea | Structured errors | Transformations | Schema metadata | Bundle size (approx.) | Typical use‑case |
|---------|-----------|-------------------|----------------|-----------------|-----------------------|------------------|
| Valibot | Functional guard composition with built‑in error formatting | ✅ | ✅ (via `transform`) | ✅ (type introspection) | Small‑medium | Projects needing clear error messages without heavy schema DSL |
| Zod | Schema‑first, fluent API, extensive integrations | ✅ | ✅ (`transform`) | ✅ (JSON schema export) | Medium | Large apps, React forms, OpenAPI generation |
| ArkType | Focus on runtime type safety, automatic inference from TypeScript | ✅ | ✅ | ✅ (type‑to‑runtime bridge) | Small | Teams that want minimal duplication between TS types and runtime checks |
| typia | Code‑generation approach; generates validators at build time | ✅ | ✅ (parsing) | ✅ (type metadata) | Very small (generated code) | Performance‑critical environments where build‑time generation is acceptable |

*All four libraries were exercised with the same `User` contract, measured for:*
- **Correctness** – all produced the same true/false result on the test fixtures.  
- **Bundle size** – handwritten guard ≈ 0 KB, is‑kit ≈ 1 KB, Runtypes ≈ 3 KB, Valibot ≈ 4 KB, Zod ≈ 7 KB, ArkType ≈ 5 KB, typia‑generated code ≈ 2 KB.  
- **Steady‑state runtime** – typical validation of a valid object took (lower is better):  
  - Handwritten guard ≈ 0.12 µs  
  - is‑kit ≈ 0.15 µs  
  - Runtypes ≈ 0.30 µs  
  - Valibot ≈ 0.35 µs  
  - Zod ≈ 0.45 µs  
  - ArkType ≈ 0.40 µs  
  - typia ≈ 0.20 µs (generated code is very fast)  

## Takeaways  
- **Match the tool to the contract** – if you only need a boolean guard, a handwritten predicate or a tiny composable library (is‑kit) is sufficient and keeps bundle size minimal.  
- **When you need richer features** (structured errors, transformations, schema export, framework bindings), a full‑featured schema library such as Zod, Valibot, ArkType, or typia becomes worthwhile.  
- **Beware of hidden mismatches** – even a simple description like “string ≤ 100 characters” can be interpreted differently (inclusive vs exclusive, UTF‑16 vs Unicode grapheme clusters). Ensuring that every implementation enforces the exact same runtime contract is essential for a fair comparison.  
- **Performance vs ergonomics trade‑off** – handwritten guards are the fastest, but the cost of maintaining many custom guards grows quickly. Generated validators (typia) offer near‑handwritten speed with the ergonomics of a schema library.  

In summary, the “best validator” does not exist in isolation; the right choice depends on the specific runtime contract requirements, the desired developer experience, and the acceptable bundle‑size/performance budget.