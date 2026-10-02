---
title: "Structs Aren't on the Stack. How C# Actually Manages Memory. - DEV Community"
url: https://dev.to/smtahosin/structs-arent-on-the-stack-how-c-actually-manages-memory-128p
date: 2026-10-01
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-03T03:07:46.020591
---

# Structs Aren't on the Stack. How C# Actually Manages Memory. - DEV Community

# Summary of “Structs Aren’t on the Stack. How C# Actually Manages Memory.”

## The Persistent Myth  
- Many tutorials and interview questions claim **“classes live on the heap, structs live on the stack.”**  
- This statement is a simplification that misleads developers and causes performance‑related bugs.

## The Real CLR Rule  
- **Value types live wherever their declaring container is allocated.**  
- The stack is only the execution context for method frames; a struct does not require stack storage, it only requires that its raw data be stored directly, without an extra reference indirection.

## Where Structs Actually Live  

### 1. Local variables inside a method  
- Example: `int count = 42; Point origin = new Point(0,0);`  
- These locals are stored in the thread’s stack frame and reclaimed when the method returns.  
- This is the sole case where the “stack” description happens to be true.

### 2. Struct as a field of a class  
- Example: `class Player { public Health PlayerHealth; }` where `Health` is a struct.  
- `new Player()` allocates the entire object on the managed heap; the `Health` field is embedded directly inside that heap block.  
- No part of the struct “floats” to the stack.

### 3. Struct inside an array  
- Example: `Point[] points = new Point[1000];`  
- All arrays are reference types, so the array object resides on the heap.  
- The CLR allocates one contiguous heap block large enough for all 1,000 structs; none are on the stack.

### 4. Variables captured by lambdas or async methods  
- Example: an `async` method with a local `int retryCount`.  
- The compiler generates a hidden state‑machine class; captured locals become fields of that heap‑allocated class.  
- Thus the value type lives on the managed heap for the duration of the async operation or lambda execution.

## Memory Layout Comparison (64‑bit CLR)

| Type | Overhead | Payload | Total Size |
|------|----------|---------|------------|
| `class ClassPoint` | Reference pointer (8 B) + SyncBlockIndex (8 B) + MethodTable pointer (8 B) | X (4 B) + Y (4 B) | 32 B |
| `struct StructPoint` | None | X (4 B) + Y (4 B) | 8 B |

- Classes incur a ~300 % overhead due to object header and indirection.  
- Structs have zero header, no pointer chasing, and no GC tracking.

## The Boxing Trap – Silent GC Pressure  
- Assigning a value type to `object` or an interface causes **boxing**: a new heap object (≈24 B) is allocated, the value’s bits are copied into it, and a method‑table pointer is added.  
- Repeated boxing in hot paths (e.g., adding ints to a non‑generic `ArrayList`) creates massive heap churn and frequent Gen‑0 collections.  
- Generics (`List<T>`) avoid boxing by storing raw values in a contiguous buffer.

## Practical Takeaways  
- Do not rely on “structs are on the stack” when reasoning about performance or memory usage.  
- Understand where a value type is stored based on its containing context.  
- Prefer structs for small, immutable data that benefits from reduced allocation overhead, but be aware of boxing and capture scenarios that push them onto the heap.  
- Use generics to eliminate unnecessary boxing and improve cache locality.