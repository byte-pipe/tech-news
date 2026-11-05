---
title: A new Go API for JSON - The Go Programming Language
url: https://go.dev/blog/jsonv2
date: 2026-11-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:25:01.217798
---

# A new Go API for JSON - The Go Programming Language

# A new Go API for JSON

## Introduction
- JSON is the dominant data‑interchange format and has been supported by Go since before Go 1.0.  
- After years of use, the original `encoding/json` package shows several shortcomings.  
- An experimental API (`encoding/json/v2` and `encoding/json/jsontext`) has been stabilized and is available in Go 1.27.

## Problems with `encoding/json`

### Behavior flaws
- Accepts invalid UTF‑8 despite RFC 8259 requiring valid UTF‑8; should error instead of corrupting data.  
- Allows objects with duplicate member names; RFC 8259 leaves handling unspecified, leading to ambiguous semantics and security risks (e.g., CVE‑2017‑12635).  
- Marshals nil slices/maps as `null`; most users prefer empty arrays/objects.  
- Performs case‑insensitive matching of JSON keys to struct fields, which is surprising, may be a security issue, and hurts performance.  
- Inconsistent invocation of `MarshalJSON` on pointer receivers; cannot be changed without breaking existing code.

### API deficiencies
- Unmarshalling from an `io.Reader` via `json.NewDecoder(r).Decode(v)` does not reject trailing junk.  
- Options set on `Encoder`/`Decoder` cannot be applied when using the top‑level `Marshal`/`Unmarshal` functions or custom `Marshaler`/`Unmarshaler` implementations.  
- Helper functions (`Compact`, `Indent`, `HTMLEscape`) only write to a `bytes.Buffer`, limiting flexibility.

### Performance limitations
- `MarshalJSON` forces allocation of a `[]byte` and requires re‑validation/re‑formatting of the result.  
- `UnmarshalJSON` must first parse the whole JSON value to locate its end, then parse it again inside the method.  
- No true streaming support: `Encoder`/`Decoder` buffer the entire JSON value; token‑level APIs are allocation‑heavy and lack a corresponding writer.  
- Recursive calls to `Marshal`/`Unmarshal` inside custom methods can cause quadratic performance.

## Trying to fix `encoding/json` directly
- Changing existing behavior would break Go 1 compatibility; many issues stem from the current API design.  
- Adding parallel functions like `MarshalV2` would create a confusing namespace within the same package.  
- Therefore a separate module (`encoding/json/v2`) is introduced to allow breaking changes without violating compatibility guarantees.

## Building on `encoding/json/jsontext`
- The `jsontext` package separates **syntactic** processing (encode/decode) from **semantic** processing (marshal/unmarshal).  
- This clear division enables more flexible implementations, better streaming support, and resolves many of the limitations of the original package.  
- Types are represented in purple blocks, functions/methods in blue blocks, illustrating the flow from raw JSON text to Go values and back.