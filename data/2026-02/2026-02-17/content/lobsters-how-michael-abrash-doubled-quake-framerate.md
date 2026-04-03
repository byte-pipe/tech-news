---
title: How Michael Abrash doubled Quake framerate
url: https://fabiensanglard.net/quake_asm_optimizations/index.html
site_name: lobsters
content_file: lobsters-how-michael-abrash-doubled-quake-framerate
fetched_at: '2026-02-17T06:00:29.287597'
original_url: https://fabiensanglard.net/quake_asm_optimizations/index.html
date: '2026-02-17'
tags: games, performance
---

FABIEN SANGLARD'S WEBSITE

CONTACT
    
RSS
     
DONATE

Feb 14, 2026

How Michael Abrash doubled Quake framerate

With the 1999 release of the Quake source code, came areadme.txtwritten by John Carmack. There is a particular sentence in that text that piqued my curiosity.

Masm is also required to build the assembly language files. It is possible to
change a #define and build with only C code, but the software rendering versions
lose almost
half its speed
.

Quake would be twice as fast thanks to its hand-crafted assembly? Let's find out if that is true, how it works, and what are the most important optimizations.

Establishing stock fps on my machine

Before doing anything with the source I needed to establish what was the framerate of the released version ofwinquake.exeon my Pentium MMX 233MHz.

C:\winquake> winquake.exe -wavonly +d_subdiv16 0 +timedemo demo1

I disabledd_subdiv16because it has no C implementation (that will make C vs ASM comparison impossible). This makes the engine fallback to D_DrawSpans8 instead of D_DrawSpans16 (perspective sampling every 8 pixels instead of 16).-wavis the fastest audio backend (also known as"fastvid" option in wq.bat).

Stock winquake completedtimedemo demo1at 42.3fps.

Building with ASM

Following the steps inLet's compile like it's 1997!, I builtwinquake.exein release modewiththe ASM optimizations. I really hoped VC++6 compiler did not get significant improvement[1]over VC++4 (the version id software used to ship winquake in 1997).

C:\winquake> WinQuake_ASM.exe -wavonly +d_subdiv16 0 +timedemo demo1

I was relieved to seeWinQuake_ASM.exerun at nearly the same framerate, 42.2 fps. I was on a good track.

Building without ASM

As John Carmack mentioned, building without ASM only requires settingid386to0inquakedef.h.

That broke the linker because a VC6 project meant running on an Intel CPU at the time.

All I had to do was to addnointel.cto the project and I had a working executable.

Quake without ASM optimizations

With a successful release build, it was time to runWinQuake_No_ASM.exe.

C:\winquake> WinQuake_No_ASM.exe -wavonly +d_subdiv16 0 +timedemo demo1

Son of a BLiT! The game indeed runs at22.7fpsinstead of42.2fps! As John Carmack warned, Quake framerate is halved without Michael Abrash's optimizations!.

Diving into the assembly

There is a lot of assembly in Quake. In total, grep found 63 functions spread across 21 files.

$ find . -name "*.s" | wc -l
21

$ find . -name "*.s" -exec grep -H ".globl C(" {} \;
./server/worlda.s:.globl C(SV_HullPointContents)
./server/math.s:.globl C(BoxOnPlaneSide)
./client/d_copy.s:.globl C(VGA_UpdatePlanarScreen)
./client/d_copy.s:.globl C(VGA_UpdateLinearScreen)
./client/d_draw.s:.globl C(D_DrawSpans8)
./client/d_draw.s:.globl C(D_DrawZSpans)
./client/surf16.s:.globl C(R_Surf16Start)
./client/surf16.s:.globl C(R_DrawSurfaceBlock16)
./client/surf16.s:.globl C(R_Surf16End)
./client/surf16.s:.globl C(R_Surf16Patch)
./client/d_scana.s:.globl C(D_DrawTurbulent8Span)
./client/r_drawa.s:.globl C(R_ClipEdge)
./client/d_parta.s:.globl C(D_DrawParticle)
./client/d_polysa.s:.globl C(D_PolysetCalcGradients)
./client/d_polysa.s:.globl C(D_PolysetRecursiveTriangle)
./client/d_polysa.s:.globl C(D_PolysetAff8Start)
./client/d_polysa.s:.globl C(D_PolysetDrawSpans8)
./client/d_polysa.s:.globl C(D_PolysetAff8End)
./client/d_polysa.s:.globl C(D_Aff8Patch)
./client/d_polysa.s:.globl C(D_PolysetDraw)
./client/d_polysa.s:.globl C(D_PolysetScanLeftEdge)
./client/d_polysa.s:.globl C(D_PolysetDrawFinalVerts)
./client/d_polysa.s:.globl C(D_DrawNonSubdiv)
./client/sys_wina.s:.globl C(MaskExceptions)
./client/sys_wina.s:.globl C(unmaskexceptions)
./client/sys_wina.s:.globl C(Sys_LowFPPrecision)
./client/sys_wina.s:.globl C(Sys_HighFPPrecision)
./client/sys_wina.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_wina.s:.globl C(Sys_PopFPCW)
./client/sys_wina.s:.globl C(Sys_SetFPCW)
./client/math.s:.globl C(Invert24To16)
./client/math.s:.globl C(TransformVector)
./client/math.s:.globl C(BoxOnPlaneSide)
./client/d_draw16.s:.globl C(D_DrawSpans16)
./client/r_aclipa.s:.globl C(R_Alias_clip_bottom)
./client/r_aclipa.s:.globl C(R_Alias_clip_top)
./client/r_aclipa.s:.globl C(R_Alias_clip_right)
./client/r_aclipa.s:.globl C(R_Alias_clip_left)
./client/snd_mixa.s:.globl C(SND_PaintChannelFrom8)
./client/snd_mixa.s:.globl C(Snd_WriteLinearBlastStereo16)
./client/r_aliasa.s:.globl C(R_AliasTransformAndProjectFinalVerts)
./client/d_spr8.s:.globl C(D_SpriteDrawSpans)
./client/r_edgea.s:.globl C(R_EdgeCodeStart)
./client/r_edgea.s:.globl C(R_InsertNewEdges)
./client/r_edgea.s:.globl C(R_RemoveEdges)
./client/r_edgea.s:.globl C(R_StepActiveU)
./client/r_edgea.s:.globl C(R_GenerateSpans)
./client/r_edgea.s:.globl C(R_EdgeCodeEnd)
./client/r_edgea.s:.globl C(R_SurfacePatch)
./client/surf8.s:.globl C(R_Surf8Start)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip0)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip1)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip2)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip3)
./client/surf8.s:.globl C(R_Surf8End)
./client/surf8.s:.globl C(R_Surf8Patch)
./client/sys_dosa.s:.globl C(MaskExceptions)
./client/sys_dosa.s:.globl C(unmaskexceptions)
./client/sys_dosa.s:.globl C(Sys_LowFPPrecision)
./client/sys_dosa.s:.globl C(Sys_HighFPPrecision)
./client/sys_dosa.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_dosa.s:.globl C(Sys_PopFPCW)
./client/sys_dosa.s:.globl C(Sys_SetFPCW)

As a comparison, DOOM has only two.asmfiles and three functions to speed up the engine.

A lot of these functions can be discarded from this study. Some do things that cannot be done in C like setting the floating-point unit precision or setting up the High-precision counter (). Some are not used (). Some are duplicated (one for server, one for client). Some optimizations use self-modifying code requiring markers so the.textregion can be updated fromrtorwand patched ().

$ find . -name "*.s" -exec grep -H ".globl C(" {} \;
./server/worlda.s:.globl C(SV_HullPointContents)

./server/math.s:.globl C(BoxOnPlaneSide)
 // Duplicate from ./client/math.s

./client/d_copy.s:.globl C(VGA_UpdatePlanarScreen)
 // DOS

./client/d_copy.s:.globl C(VGA_UpdateLinearScreen)
 // DOS
./client/d_draw.s:.globl C(D_DrawSpans8)
./client/d_draw.s:.globl C(D_DrawZSpans)

./client/surf16.s:.globl C(R_Surf16Start)

./client/surf16.s:.globl C(R_DrawSurfaceBlock16)
 // Experimental 16-bit rendering

./client/surf16.s:.globl C(R_Surf16End)

./client/surf16.s:.globl C(R_Surf16Patch)

./client/d_scana.s:.globl C(D_DrawTurbulent8Span)
./client/r_drawa.s:.globl C(R_ClipEdge)
./client/d_parta.s:.globl C(D_DrawParticle)
./client/d_polysa.s:.globl C(D_PolysetCalcGradients)
./client/d_polysa.s:.globl C(D_PolysetRecursiveTriangle)

./client/d_polysa.s:.globl C(D_PolysetAff8Start)

./client/d_polysa.s:.globl C(D_PolysetDrawSpans8)

./client/d_polysa.s:.globl C(D_PolysetAff8End)

../client/d_polysa.s:.globl C(D_Aff8Patch)

./client/d_polysa.s:.globl C(D_PolysetDraw)
./client/d_polysa.s:.globl C(D_PolysetScanLeftEdge)
./client/d_polysa.s:.globl C(D_PolysetDrawFinalVerts)
./client/d_polysa.s:.globl C(D_DrawNonSubdiv)

./client/sys_wina.s:.globl C(MaskExceptions)
./client/sys_wina.s:.globl C(unmaskexceptions)
./client/sys_wina.s:.globl C(Sys_LowFPPrecision)
./client/sys_wina.s:.globl C(Sys_HighFPPrecision)
./client/sys_wina.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_wina.s:.globl C(Sys_PopFPCW)
./client/sys_wina.s:.globl C(Sys_SetFPCW)

./client/math.s:.globl C(Invert24To16)

./client/math.s:.globl C(TransformVector)
./client/math.s:.globl C(BoxOnPlaneSide)
./client/d_draw16.s:.globl C(D_DrawSpans16)
./client/r_aclipa.s:.globl C(R_Alias_clip_bottom)
./client/r_aclipa.s:.globl C(R_Alias_clip_top)
./client/r_aclipa.s:.globl C(R_Alias_clip_right)
./client/r_aclipa.s:.globl C(R_Alias_clip_left)
./client/snd_mixa.s:.globl C(SND_PaintChannelFrom8)
./client/snd_mixa.s:.globl C(Snd_WriteLinearBlastStereo16)
./client/r_aliasa.s:.globl C(R_AliasTransformAndProjectFinalVerts)
./client/d_spr8.s:.globl C(D_SpriteDrawSpans)

./client/r_edgea.s:.globl C(R_EdgeCodeStart)

./client/r_edgea.s:.globl C(R_InsertNewEdges)
./client/r_edgea.s:.globl C(R_RemoveEdges)
./client/r_edgea.s:.globl C(R_StepActiveU)
./client/r_edgea.s:.globl C(R_GenerateSpans)

./client/r_edgea.s:.globl C(R_EdgeCodeEnd)

./client/r_edgea.s:.globl C(R_SurfacePatch)

./client/surf8.s:.globl C(R_Surf8Start)

./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip0)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip1)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip2)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip3)

./client/surf8.s:.globl C(R_Surf8End)

./client/surf8.s:.globl C(R_Surf8Patch)

./client/sys_dosa.s:.globl C(MaskExceptions)
./client/sys_dosa.s:.globl C(unmaskexceptions)
./client/sys_dosa.s:.globl C(Sys_LowFPPrecision)
./client/sys_dosa.s:.globl C(Sys_HighFPPrecision)
./client/sys_dosa.s:.globl C(Sys_PushFPCW_SetHigh)
./client/sys_dosa.s:.globl C(Sys_PopFPCW)
./client/sys_dosa.s:.globl C(Sys_SetFPCW)

This still leaves 32 methods pertaining to math, sound, render, and draw. The distinction between R_ and D_ is not obvious. The R_ code is in charge of *what* to draw. The D_ code is in charge of *how* to draw it.

//******* DRAW *******

./client/d_spr8.s:.globl C(D_SpriteDrawSpans) // Draw sprite facing camera
./client/d_draw.s:.globl C(D_DrawSpans8) // World draw 8 pixels persp
./client/d_draw.s:.globl C(D_DrawZSpans) // World write to Z-Buffer
./client/d_draw16.s:.globl C(D_DrawSpans16) // World draw 16 pixels persp
./client/d_scana.s:.globl C(D_DrawTurbulent8Span)
./client/d_parta.s:.globl C(D_DrawParticle)
./client/d_polysa.s:.globl C(D_PolysetCalcGradients) // All the polysets are for
./client/d_polysa.s:.globl C(D_PolysetRecursiveTriangle) // alias models rendering.
./client/d_polysa.s:.globl C(D_PolysetDrawSpans8)
./client/d_polysa.s:.globl C(D_PolysetDraw)
./client/d_polysa.s:.globl C(D_PolysetScanLeftEdge)
./client/d_polysa.s:.globl C(D_PolysetDrawFinalVerts)
./client/d_polysa.s:.globl C(D_DrawNonSubdiv) // Also model drawing

//******* MATH *******

./client/math.s:.globl C(TransformVector)
./client/math.s:.globl C(BoxOnPlaneSide)
./server/worlda.s:.globl C(SV_HullPointContents)

//******* SOUND *******

./client/snd_mixa.s:.globl C(SND_PaintChannelFrom8)
./client/snd_mixa.s:.globl C(Snd_WriteLinearBlastStereo16)

//******* RENDER *******

./client/r_drawa.s:.globl C(R_ClipEdge)
./client/r_aclipa.s:.globl C(R_Alias_clip_bottom)
./client/r_aclipa.s:.globl C(R_Alias_clip_top)
./client/r_aclipa.s:.globl C(R_Alias_clip_right)
./client/r_aclipa.s:.globl C(R_Alias_clip_left)
./client/r_aliasa.s:.globl C(R_AliasTransformAndProjectFinalVerts)
./client/r_edgea.s:.globl C(R_InsertNewEdges)
./client/r_edgea.s:.globl C(R_RemoveEdges)
./client/r_edgea.s:.globl C(R_StepActiveU)
./client/r_edgea.s:.globl C(R_GenerateSpans)
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip0) // Surface caching generation
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip1) // Surface caching generation
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip2) // Surface caching generation
./client/surf8.s:.globl C(R_DrawSurfaceBlock8_mip3) // Surface caching generation

The next thing to do, before going deeper was to quantify how much each function contributes to improving the framerate from 22.7fps to 42.2fps. To find out, I modified the engine to enable one ASM function at a time and ran the same timedemo over and over again.

Function Name

Frames per Second (fps) gain

D_DrawSpans8

12.6

R_DrawSurfaceBlock8_mip*

 4.2

D_Polyset*

 2.2

D_DrawZSpans

 0.2

D_DrawParticle

 0.1

Others

 0.6

Total: 19.5

Without surprise, the most important optimizations are in the low-level drawing routines withD_DrawSpans8to render the walls,R_DrawSurfaceBlock8Xto combine texture and lightmap into a surface, andD_Polyset*to draw the models. The rest barely registered on my (rather crude) benchmark.

How much each ASM function improves framerate from 22.7fps to 42.2fps.

The Polyset* functions are intertwined in such a way they cannot be individually switched to C/ASM. They have to be all C or all ASM.

The ASM optimizations I found often involve loop unrolling, self-modifying code, avoiding mis-predictions, leveraging the Pentium FPU pipeline to hide latency, and creating "overlap" where both Pentium U/V pipelines and the FPU pipeline are executing instructions in parallel.

Here are a few detailed functions. For those willing to go ever deeper in that rabbit hole, I suggest readingOptimizations for Intel's
32-Bit Processors (Feb 94)[2]which covers Pentium extensively. Be warned it is more powerful than 20g of melatonin.

TransformVector

The functionTransformVectoris a good introduction to the P5 FPU. It is a simple matrix-vector multiplication., used extensively to project everything in screen space, from world polygons, model/alias polygons, and sprites.

typedef float vec_t;
typedef vec_t vec3_t[3];

vec3_t vpn, vright, vup;

#define DotProduct(x,y) (x[0]*y[0]+x[1]*y[1]+x[2]*y[2])

void TransformVector (vec3_t in, vec3_t out) {
 out[0] = DotProduct(in,vright);
 out[1] = DotProduct(in,vup);
 out[2] = DotProduct(in,vpn);
}

Let's look at the assembly. I kept mabrash's asm in AT&T notation[3]on the left. On the right is what VC6 generated, in Intel notation, decompiled by Ninja.

// Abrash version

.globl C(TransformVector)

movl in(%esp),%eax
movl out(%esp),%edx

flds (%eax)
fmuls C(vright)
flds (%eax)
fmuls C(vup)
flds (%eax)
fmuls C(vpn)

flds 4(%eax)
fmuls C(vright)+4
flds 4(%eax)
fmuls C(vup)+4
flds 4(%eax)
fmuls C(vpn)+4
fxch %st(2)

faddp %st(0),%st(5)
faddp %st(0),%st(3)
faddp %st(0),%st(1)

flds 8(%eax)
fmuls C(vright)+8
flds 8(%eax)
fmuls C(vup)+8
flds 8(%eax)
fmuls C(vpn)+8
fxch %st(2)

faddp %st(0),%st(5)
faddp %st(0),%st(3)
faddp %st(0),%st(1)

fstps 8(%edx)
fstps 4(%edx)
fstps (%edx)

ret

// VC6 output

float* TransformVector(float* a1, float* a2)

mov eax, dword [esp+0x4 {a1}]
mov ecx, dword [esp+0x8 {a2}]

fld st0, dword [0x2970]
// vright.x

fmul st0, dword [eax]
fld st0, dword [0x2978]
// vright.y

fmul st0, dword [eax+0x8]
faddp st1, st0
fld st0, dword [0x2974]
// vright.z

fmul st0, dword [eax+0x4]
faddp st1, st0
fstp dword [ecx], st0

fld st0, dword [0x2974]
// vup.x

fmul st0, dword [eax]
fld st0, dword [0x297c]
// vup.y

fmul st0, dword [eax+0x8]
faddp st1, st0
fld st0, dword [0x2978]
// vup.z

fmul st0, dword [eax+0x4]
faddp st1, st0
fstp dword [ecx+0x4], st0

fld st0, dword [0x296c]
// vpn.x

fmul st0, dword [eax]
fld st0, dword [0x2974]
// vpn.y

fmul st0, dword [eax+0x8]
faddp st1, st0
fld st0, dword [0x2970]
// vpn.z

fmul st0, dword [eax+0x4]
faddp st1, st0
fstp dword [ecx+0x8], st0

retn {__return_addr}

VC6 output:The FPU is used like a 487 FPU. Namely an un-pipelined stack where operands are picked up from the top of the stack and results are pushed back on the top of the stack (if you know how a JVM works, that is the same principle). Instructions are found in the same order as on the code, one dot-product after another. And each dot product is *, *, +, *, +. The whole sequence looks as follows.

*, *, +, *, +, store
*, *, +, *, +, store
*, *, +, *, +, store

This approach incurs stalls. Afmultakes three cycles[4]to return a result. This means that eachfaddstalls for two cycles while waiting forfmulresult to be available.

Abrash version:That is a radically different approach. It enqueue as many independent (result not depending on previous operation) instructions as possible in the pipeline. On a 487 that would be a problem because the operands would have to be re-organized with costlyfxch(4 cycles!) to swap their location on the stack.

Butfxchis free (0 cycle) on Pentium. This instruction allows developers to use nearly all the registers (s) in the FPU stack. It turns the cumbersome legacy FPU stack into a convenient register array.

This allows to calculate three dot products in parallel, with three partial sums on the x87 stack at all times. And the computation looks as follows.

* * * * * *
+ + +
* * *
+ + +
store, store, store

By the time it does the additions, the results of the multiplication are already available. This hidesfmullatency and lets the P5 avoid stalls completely.

Store optimization:Another optimization in Abrash's version, are the stores (fstps) located at the end instead of being mixed with other operations like in the VC6 output. Storing a value (fstp) immediately after calculating results in a 1-cycle stall because the write-back stage of the pipeline cannot be bypassed[5]. Having the stores at the end ensures that the last faddp has enough cycles to complete before the fstp tries to move that data into memory.

Invert24To16

This function is not actually used in Quake. It is likely one of these optimizations that Michael Abrash wrote and had to be abandoned because John Carmack rewrote the engine completely.

Michael Abrash focused on the x86 assembly optimizations. There were some times where he had spent a lot of effort on a low level routine, then I changed the architecture and he had to start over, which I felt a little bad about, even though it was net-positive.

He did use a NeXT for some things (he managed the code merges between us), but he had to do his assembly timings on DOS.

- Conversation with John Carmack

fixed16_t Invert24To16(fixed16_t val) {
 if (val < 256)
 return (0xFFFFFFFF);

 return (fixed16_t)
 (((double)0x10000 * (double)0x1000000 / (double)val) + 0.5);
}

What is cool to see is that no stone were left unturned. Here the main goal of the rewrite is to avoid a call to Microsoft costly CRT__ftolfunction.

.globl C(Invert24To16)

 movl val(%esp),%ecx
 movl $0x100,%edx // 0x10000000000 dividend
 cmpl %edx,%ecx
 jle LOutOfRange

 subl %eax,%eax
 divl %ecx

 ret

LOutOfRange:
 movl $0xFFFFFFFF,%eax
 ret

int32_t _Invert24To16(int32_t arg1)

cmp dword [esp+0x4 {arg1}], 0x100
jge 0xf04

or eax, 0xffffffff {0xffffffff}
retn {__return_addr}

fild st0, dword [esp+0x4 {arg1}]
fdivr st0, qword [__real@4270000]
fadd st0, qword [__real@3fe0000]
jmp __ftol

R_DrawSurfaceBlock8_mipX

By the time the engine reaches R_DrawSurfaceBlock8, it has determined which part of a wall is visible. Now theR_enderer needs to "bake" the lightmap into the texture. The result is called a "Surface" (that is later handed to theD_rawer which rasterizes to the framebuffer). Michael Abrash describes this part extensively inChapter 68: Quake’s Lighting Modelso I won't elaborate more on it.

There are four R_DrawSurfaceBlock8_mip functions. One for each level of mipmap. Here is a clickable image modified engine to show where each level triggers.

Click me to see the four mipmap distances.

The C version of all four functions ishere. The ASM versions arehere. And the VC6 output forR_DrawSurfaceBlock8_mip0ishere.

The most obvious optimization is the self-modifying code. Several memory locations arehard-coded to 0x12345678and patched inR_Surf8Patchjust before R_DrawSurfaceBlock8 is called. The patching bakes the colormap base into the instruction stream which avoids using a register to keep the base. Moreover, this avoids an extra ADD to lookup the colormap.

The inner "b" loop is fully unrolled. This further saves a register by avoiding a loop counter. And one misprediction is avoided on the last iteration (the P5 always picks the backward jmp destination in order to excel at loops).

Given the importance of this function, I understand better now why Michael Abrash mentioned it in his book.

As it turns out, the raw speed of surface-based lighting is pretty good. Although an extra step is required to build the surface, moving lighting and tiling into a separate loop from texture mapping allows each of the two loops to be optimized very effectively, with almost all variables kept in registers.
The surface-building inner loop is particularly efficient, because it consists of nothing more than interpolating intensity, combining it with a texel and using the result to look up a lit texel color, and storing the results with a dword write every four texels.
In assembly language, we got this code down to 2.25 cycles per lit texel in Quake.

- Michael Abrash, Chapter 68: Quake’s Lighting Model

D_DrawSpans8

Quake uses an Active Edge Table to render polygons as horizontal spans (I wrote about that15 years agoif you want to see it in action). TheC versionis a pretty big function which spans over 218 lines of code. VC6generated256 lines of ASM. And thehand-optimized versionis a 650 lines juggernaut.

D_DrawSpans8 receives a list of spans (a portion of a surface) to be rasterized to the framebuffer. The goal is to be perspective correct every 8 pixels (vs D_DrawSpans16 which does it every 16 pixels) and interpolate the rest.

The biggest challenge of this function is that interpolating Z in screenspace does not work. In order to be perspective-correct, the interpolation must be done on 1/z. A division is the worst thing you can ask from the P5 FPU since it can take up to 39 cycles on a P5.

The main optimization here is a huge "overlap" where anFDIVis issued for the next 8-pixel span at the very beginning of the current span. While the FPU is doing that division for 30+ cycles, the CPU's integer U and V pipelines draw the current 8 pixels. Many comments mention how the divide is "in-flight". A funny comment from Michael Abrash assesses of the extensive care he put to do other things in the integer pipelines while fdiv is running in the floating-point pipeline.

 fdiv %st(1),%st(0)
// this is what we've gone to all this trouble to


// overlap

To avoid a mis-prediction on the last part of a span (which may feature less than 8 pixels, a Jump table is used. The code calculates the number of pixels to draw in the span, looks up a memory address in a table, and jumps directly to a label like Entry3_8. Zero mis-prediction possible here.

There are other tiny optimizations but given how white hot this function is, everything counts. This is the case of clamp. In the C version, it performs two tests, one for "too high" and another one for "below zero" which is two branches that can result in mis-predictions. By usingja(Jump if Above), an unsigned comparison on signed integers, both high and low conditions are tested at once (if the value is negative, it turns into a very big integer that is above "too high"). This is super neat.

Throughout the ASM code of Quake, there are several mentions where Michael was looking for "overlap". This seems to indicate an obsession to find places where the FPU and the integer pipeline could process instructions in parallel.


 // TODO: any overlap from rearranging?

Like it was the case for R_DrawSurfaceBlock8_mip, Michael Abrash brought up D_DrawSpans in hisGraphic Programming Black Bookwhich underlines further how paramount this optimization was at the time.

The texture-mapping inner loop, which overlaps an FDIV for floating-point perspective correction with integer pixel drawing in 16-pixel bursts, has been squeezed down to 7.5 cycles per pixel on a Pentium, so the combined inner loop times for building and drawing a surface is roughly in the neighborhood of 10 cycles per pixel which is fast enough to do 40 frames/second at 640×400 on a Pentium/100.

- Michael Abrash, Chapter 68: Quake’s Lighting Model

Going deeper

If you want to dig deeper,hereare the objs resulting from a compilation of Quake with assembly optimizations disabled. The disassembly can easily be extracted with Binary Ninja.

References

^[1]A visual history of Visual C++^[2]Optimizations for Intel's 32-Bit Processors^[3]GMU assembler uses AT&T. This notation was used so it would compile on Linux as well.^[4]Architecture of the Pentium Microprocessor^[5]A floating-point store must wait an extra cycle for its floating-point operand



*
