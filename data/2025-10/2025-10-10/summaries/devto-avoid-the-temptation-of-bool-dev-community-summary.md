---
title: Avoid the Temptation of bool - DEV Community
url: https://dev.to/pauljlucas/avoid-the-temptation-of-bool-5g31
date: 2025-10-04
site: devto
model: llama3.2:1b
summarized_at: 2025-10-10T11:13:08.100964
screenshot: devto-avoid-the-temptation-of-bool-dev-community.png
---

# Avoid the Temptation of bool - DEV Community

Avoiding bool - DEV Community

## Key Points

- The Boolean type (bool) is fundamental in programming but can be misleading because `true` and `false` do not carry meaning.
- Alternatives to using `bool` for parameters include two functions, an enumeration, or bit flags.
- Using an enumeration improves clarity by providing additional options that can be easily added.

## Structured Output

### Alternatives to bool for Parameters

*   **Two Functions**

    ```cpp
void *
alloc_raw(size_t size) {
  // implementation
}

void *
alloc_zero(size_t size) {
  // implementation
}
```

*   **Enumeration**

    ```c
enum alloc_opts {
  ALLOC_RAW,
  ALLOC_ZEROED
};

typedef enum alloc_opts alloc_opts;

void *
alloc_buf(size_t size, alloc opts opt) {
  switch (opt) {
    case ALLOC_RAW:
      // implementation
      break;
    case ALLOC_ZEROED:
      // implementation
      break;
  }
}
```

*   **Bit Flags**

    ```c
enum alloc_opts {
  ALLOC_RAW = 1,
  ALLOC_ALIGNED = 2 << 0,
  ALLOC_ZEROED = 1 << 1
};

typedef enum alloc_opts alloc_opts;

void *
alloc_buf(size_t size, alloc opts opt) {
  // implementation using bitwise AND operator
}
```

### Additional Advantages

Using an enumeration or bit flags provides several benefits:

*   **Improved Readability**: The code is easier to read and understand when having multiple options.
*   **Increased Clarity**: The meaning of `true` or `false` becomes clear from the function name or option values.
*   **Reduced Error Messages**: With an enumeration, you can avoid printing error messages if allocation fails. With bit flags, you need a separate structure to represent these values.

### Go Example

The provided example demonstrates how using an enum to represent boolean options is more readable and maintainable than using `bool`:

```go
import "fmt"

var allocOptions uint8

func init() {
  allocOptions = uint8(ALLOC_ALIGNED)
}

// allocation function will take in the option value as a uint8
func allocate(bufSize int64, opts uint8) (*uint32, error) {
  switch opts {
  case ALLOC_RAW:
    // implementation
  case ALLOC_ZEROED:
    return nil, fmt.Errorf("allocation failed")
  }
}
```
In this example, `AllocOptions` is an enum defined with three values: `ALLOC_RAW`, `ALLOC_ZEROED`. The function signature uses the first value to represent a RAW allocation. The type of the returned pair is more explicit, allowing developers looking at your code to understand what they're seeing.
