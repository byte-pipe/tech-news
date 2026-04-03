---
title: Inigo Quilez :: computer graphics, maths, shaders, fractals, demoscene
url: https://iquilezles.org/articles/noacos/
date: 2026-03-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:15:04.132552
---

# Inigo Quilez :: computer graphics, maths, shaders, fractals, demoscene

# Inigo Quilez – Computer Graphics, Maths, Shaders, Fractals, Demoscene  

## Main Argument  
- Trigonometric functions (sin, cos, atan, etc.) should be avoided inside core 3D algorithms; their presence often indicates unnecessary complexity.  
- Angles are abstract, while vectors and geometric operations (dot and cross products) directly encode the needed information.  

## Why Trigonometry Is Problematic  
- Using `acos` to obtain an angle and then `cos` on that angle is redundant: `cos(acos(x))` equals `x`.  
- The `acos`/`cos` chain introduces floating‑point errors, extra computation, and the need for clamping.  
- Normalizing vectors and computing square roots for lengths adds further cost and potential instability.  

## Dot and Cross Products as Alternatives  
- The dot product gives the cosine of the angle between two vectors (scaled by their lengths).  
- The cross product’s magnitude gives the sine of the angle (scaled by the vectors’ lengths).  
- Together, they provide a complete description of relative orientation without converting to angles.  

## Example: Rotating an Object to Align with a Direction  

### Suboptimal Approach (uses trigonometry)  
```cpp
vec3 axi = normalize(cross(z, d));
float ang = acosf(clamp(dot(z, d), -1.0f, 1.0f));
mat3x3 rot = rotationAxisAngle(axi, ang);
```  
- Computes `acos`, then `cos` and `sin` inside `rotationAxisAngle`.  
- Performs unnecessary normalization and clamping.  

### Proper Approach (uses only dot and cross)  
```cpp
mat3x3 rotationAlign(const vec3& d, const vec3& z) {
    vec3 ax = cross(z, d);
    float co = dot(z, d);
    float si = length(ax);          // = sin(theta) for unit vectors
    vec3 v = ax / si;                // normalized rotation axis
    float ic = 1.0f - co;
    return mat3x3( v.x*v.x*ic + co, v.y*v.x*ic - si*v.z, v.z*v.x*ic + si*v.y,
                  v.x*v.y*ic + si*v.z, v.y*v.y*ic + co, v.z*v.y*ic - si*v.x,
                  v.x*v.z*ic - si*v.y, v.y*v.z*ic + si*v.x, v.z*v.z*ic + co );
}
```  
- No `acos`, `cos`, `normalize`, or `clamp`.  
- Uses `dot` for cosine, `cross` length for sine, and avoids extra square‑root by noting `si² = 1 - co²`.  

## Deeper Insight  
- Replacing angle‑based formulas with vector‑based ones often reveals underlying geometric relationships and leads to more robust, efficient code.  
- The pattern “dot → cosine, cross → sine” can be applied broadly to eliminate trigonometry from many graphics algorithms.  

## Takeaway  
- Prefer dot and cross products over explicit trigonometric functions when working with vectors and orientations in computer graphics.  
- This practice reduces computational cost, improves numerical stability, and aligns code more closely with the geometric nature of the problem.