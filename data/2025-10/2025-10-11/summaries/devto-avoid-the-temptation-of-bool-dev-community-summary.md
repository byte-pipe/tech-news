---
title: Avoid the Temptation of bool - DEV Community
url: https://dev.to/pauljlucas/avoid-the-temptation-of-bool-5g31
date: 2025-10-04
site: devto
model: llama3.2:1b
summarized_at: 2025-10-11T11:10:34.641996
screenshot: devto-avoid-the-temptation-of-bool-dev-community.png
---

# Avoid the Temptation of bool - DEV Community

## Avoid the Temptation of bool - DEV Community

Avoiding using `bool` as a parameter in public APIs is essential for clarity. Instead, explore other alternatives.

### Using Two Functions

Declaring two separate functions for raw allocation and zeroing can help clarify code.

*   `alloc_raw(size_t size)`
*   `alloc_zero(size_t size)`

These functions can be combined into one API with an enum type to specify the allocation option.

```plain
enum alloc_opts {
    ALLOC_RAW,
    ALLOC_ZEROED
};

typedef alloc_opts alloc_opts;

void alloc_buf(size_t size, alloc_opts opt) {
    switch (opt) {
        case ALLOC RAW:
            // implementation for raw allocation
            break;
        case ALLOC ZEROED:
            // implementation for zeroing buffer
            break;
        default:
            // handle unknown option
            break;
    }
}
```

### Using an Enumeration

Defining a custom enum type with specific values provides better clarity than using `bool`.

```cpp
enum alloc opts {
    ALLOC_RAW,
    ALLOC_ZEROED
};

void alloc_buf(size_t size, alloc opts opt) {
    switch (opt) {
        case ALLOC RAW:
            // implementation for raw allocation
            break;
        case ALLOC ZEROED:
            // implementation for zeroing buffer
            break;
        default:
            // handle unknown option
            break;
    }
}
```

### Alternative Solution

In languages like C and Go, define a custom struct with booleans to represent the allocation option.

```cpp
struct AllocatedState {
    bool raw: 1;
    bool zeroed: 1;
} opts;

void alloc_buf(size_t size, allocated_state state) {
    switch (state.raw) { // assuming this is where you decide which function to call
        case true:
            // implementation for raw allocation
            break;
        default: // no-op on no-zero allocations
           break;
    }
}
```

This approach allows for more control over the code and ensures better readability.

### Conclusion

Choosing the right data type can significantly impact your programming experience. By exploring alternatives to `bool`, you can create more readable, maintainable, and efficient code. Remember to consider the benefits of each approach and choose the one that best suits your project's requirements.
