---
title: GitHub - zeux/meshoptimizer: Mesh optimization library that makes meshes smaller and faster to render · GitHub
url: https://github.com/zeux/meshoptimizer
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:37:46.942207
---

# GitHub - zeux/meshoptimizer: Mesh optimization library that makes meshes smaller and faster to render · GitHub

# meshoptimizer

## Purpose
- Provides algorithms to make triangle meshes smaller and faster to render by optimizing data for GPU pipelines and reducing mesh complexity and storage.
- Offers C and C++ interfaces; usable from other languages via FFI (e.g., Rust `meshopt` crate, JavaScript `meshoptimizer.js`).
- Includes two companion projects:
  - **gltfpack** – command‑line tool that automatically optimizes glTF files.
  - **clusterlod.h** – single‑header library for continuous level‑of‑detail using clustered simplification.

## Installing
- Clone the repository or download the zip archive:  
  `git clone -b v1.2 https://github.com/zeux/meshoptimizer.git`
- Available as packages for many Linux distributions (Arch, Debian, FreeBSD, Nix, Ubuntu) and via Vcpkg or Conan.
- `gltfpack` can be obtained as a pre‑built binary from the Releases page or through the npm package; native binaries are recommended for performance and texture‑compression support.

## Building
- Distributed as a header (`src/meshoptimizer.h`) and a set of C++ source files (`src/*.cpp`).
- Build options:
  - Use CMake to compile the library as a standalone project or integrate it into an existing CMake build.
  - Add the needed source files directly to your own build system; no special compiler flags are required on major compilers.
  - For a single‑file build, concatenate the source files into one `.cpp` file.
- Include the header in code (`#include "meshoptimizer.h"`); the implementation is C++, but the API is C‑compatible.

## Core optimization pipeline
When preparing a mesh for rendering, apply the following steps in order (optional steps are marked):

1. Indexing  
2. Vertex cache optimization  
3. Overdraw optimization (optional)  
4. Vertex fetch optimization  
5. Vertex quantization  
6. Index filtering  
7. Shadow indexing (optional)

### Indexing
- Ensure the mesh has a vertex buffer without redundant vertices and an accompanying index buffer.
- Generate a remap table that maps original vertices to unique ones:
  ```cpp
  size_t index_count = face_count * 3;
  size_t unindexed_vertex_count = face_count * 3;
  std::vector<unsigned int> remap(unindexed_vertex_count);
  size_t vertex_count = meshopt_generateVertexRemap(
      &remap[0], nullptr, index_count,
      &unindexed_vertices[0], unindexed_vertex_count,
      sizeof(Vertex));
  ```
- Use the remap table to create compact buffers:
  ```cpp
  meshopt_remapIndexBuffer(indices, nullptr, index_count, &remap[0]);
  meshopt_remapVertexBuffer(vertices, &unindexed_vertices[0],
                            unindexed_vertex_count, sizeof(Vertex), &remap[0]);
  ```
- The default remap uses binary equivalence of vertex data; for floating‑point drift, either quantize attributes first or use `meshopt_generateVertexRemapCustom` with a custom comparison function.

### Vertex cache optimization
- Reorder triangles to improve vertex shader reuse across the GPU’s post‑transform cache.
- Adaptive algorithm (works well on many GPU architectures):
  ```cpp
  meshopt_optimizeVertexCache(indices, indices, index_count, vertex_count);
  ```
- Faster, fixed‑size FIFO variant (recommended cache size 16):
  ```cpp
  meshopt_optimizeVertexCacheFifo(indices, indices, index_count, vertex_count, 16);
  ```

### Overdraw optimization
- After vertex processing, triangles are rasterized; reducing the number of pixels that pass the depth test lowers pixel‑shader workload.
- The library provides functions to reorder triangles to minimize overdraw (details continue in the full documentation).