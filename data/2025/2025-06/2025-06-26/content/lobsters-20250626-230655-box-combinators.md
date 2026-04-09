---
title: Box combinators
url: https://mmapped.blog/posts/41-box-combinators
site_name: lobsters
fetched_at: '2025-06-26T23:06:55.953479'
original_url: https://mmapped.blog/posts/41-box-combinators
author: Roman Kashitsyn
date: '2025-06-26'
description: The most visual way to print a table.
tags: programming
---

# Box combinators

✏
2025-06-01

  

✂
2025-06-01

* Text boxes
* ExamplesSierpinski triangleSpiralData table
* Sierpinski triangle
* Spiral
* Data table
* Closing words
* Appendix: the Box module

A combinator is a function which builds program fragments from program fragments.

In functional programming,combinator librariesrefer to a design style that emphasizes bottom-up program construction.
Such libraries define a few core data types
and provideconstructors—functions that create initial objects—andcombinators—functions that build larger objects from smaller pieces.Combinators enable the programmer to use intuitive visual and spatial reasoning
that’s vastly more powerful than linear language processing.
As a result, solving problems with combinators feels like playing withlegopieces.This article describes a combinator library that deals with two-dimensional blocks ofasciicharacters.
I’ll useOCamlto demonstrate the ideaFunctional languages are a perfect medium for combinator libraries.,
but you won’t have trouble translating it to any modern language.
Box combinators are my go-to tool when I need to visualize data programmatically for debugging or exploration.

## Text boxes

I stumbled on the idea of box combinators around 2012 while reading chapter 10 ofProgramming in Scala, 2nd edition.
The chapter demonstrates how to use Scala’s object-oriented features to build a module for rendering rectangular text boxes (the authors called themelements).
This section describes the underlying idea without the object-oriented fluff.The primary type in our library is thebox: a two-dimensional array ofasciicharactersSingle-byte characters aren’t a fundamental restriction;
 we could also arrange Unicode glyphs in a grid..
A box has aheight(the number of rows) and awidth(the number of columns).
There are two primary ways to construct a box:of_stringwraps a string into a unit-height gridHandling multiline strings is an exercise for the reader.andfillfills a box of specified dimensions with a character.
Thespaceandof_charconstructors are special cases offill.
Anemptybox has zero dimensions and acts as a neutral element; combining it with other boxes has no effect.⊕Primitive box constructors.+-------------+of_string"Hello, World!" = |Hello, World!|+-------------++----+|aaaa|fill'a' 3 4 = |aaaa||aaaa|+----++--+| |space3 2 = | || |+--++-+of_char'a' = |a|+-+empty= ++++Things get interesting when we start combining the primitives.
We can compose two boxes in at least two ways:
by stacking them horizontally (placing the first boxbesidethe second)
or vertically (placing the first boxabovethe second).⊕Box combinatorsbesideandabovestack boxes horizontally and vertically.+--+ +--+ +----+|aa| |bb| |aabb||aa|beside|bb| = |aabb||aa| |bb| |aabb|+--+ +--+ +----++--++--+ +--+ |aa||aa| |bb| |aa||aa|above|bb| = |aa||aa| |bb| |bb|+--+ +--+ |bb||bb|+--+For the composite box to have well-defined height and width, the arguments must have compatible dimensions:
vertically stacked boxes must have the same width, and horizontally stacked boxes must have the same height.We solve this issue by padding the smaller box with extra space:
wewidenit for vertical composition
andheightenit for horizontal composition.
We can add the padding before, after, or around the smaller box.
Since none of the options is inherently superior, we provide all three, using central alignment as the default.+---+ +-------+widen7 |aaa| = | aaa |+---+ +-------++-++-+ | |heighten3 |b| = |b|+-+ | |+-++---+ +----+|aaa| +-+ |aaa ||aaa|beside|b| = |aaab||aaa| +-+ |aaa |+---+ +----++---+ +-+ +---+|aaa|above|b| = |aaa|+---+ +-+ | b |+---+Thehconcat(concatenate horizontally) andvconcat(concatenate vertically)
stack an array of boxes (besideandabovecompose exactly two boxes).
Thegridfunction takes a2-darray of boxes,
combines each row horizontally,
and then combines the rows vertically.⊕Box combinators operating on arrays of boxes.+-+ +-+ +-+ +---+hconcat[| |a|; |b|; |c| |] = |abc|+-+ +-+ +-+ +---++-++-+ +-+ +-+ |a|vconcat[| |a|; |b|; |c| |] = |b|+-+ +-+ +-+ |c|+-++-+ +-+ +-+ +-+ +--+grid[| [| |a|; |b| |]; [| |c|; |d| |] |] = |ab|+-+ +-+ +-+ +-+ |cd|+--+

## Examples

### Sierpinski triangle

Box combinators are a powerful tool for playing with fractals.
Rendering aSierpinski trianglerequires only a few lines of code.⊕A program drawing a Sierpinski triangle of ordern.let recsierpinski n =if n == 0 then Box.of_char '*'else let s = sierpinski (n - 1) inBox.above s (Box.hconcat [| s; Box.of_char ' '; s |])⊕A Sierpinski triangle rendered using box combinators.$ sierpinski 5 |> Box.print_box** ** ** * * ** ** * * ** * * ** * * * * * * ** ** * * ** * * ** * * * * * * ** * * ** * * * * * * ** * * * * * * ** * * * * * * * * * * * * * * ** ** * * ** * * ** * * * * * * ** * * ** * * * * * * ** * * * * * * ** * * * * * * * * * * * * * * ** * * ** * * * * * * ** * * * * * * ** * * * * * * * * * * * * * * ** * * * * * * ** * * * * * * * * * * * * * * ** * * * * * * * * * * * * * * ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *### SpiralThe following snippet is a modified version of the spiral renderer from section 10.15 ofProgramming in Scala.⊕A program drawing a spiral withnturns.let recspiral n =let open Box inif n <= 0then of_char '+'else let s = spiral (n - 1) inlet h, w = dimensions s inlet vbar = fill '|' h 1 ingrid [| [| of_string "| +"; fill '-' 1 w; of_char '+' |]; [| vbar; of_char ' '; s; of_char ' '; vbar |]; [| of_char '+'; fill '-' 1 (w+2); of_char '+' |] |]$ spiral 4 |> Box.print_box| +-------------+| | +---------+ || | | +-----+ | || | | | +-+ | | || | | | + | | | || | | +---+ | | || | +-------+ | || +-----------+ |+---------------+### Data tablePlaying with fractals is fun, but it won’t pay our bills.
Business loves tables, and box combinators are a powerful tool for rendering them.
Let’s display an array of book metadata in a human-friendly way.typebook = { title : string;author : string;rating : int;price : float }letbooks = [| { title = "Waiting for Good Dough";author = "Samuel Biscuit";rating = 4;price = 23.86 };{ title = "The Bun Also Rises";author = "Ernest Hemingwaffle";rating = 5;price = 9.86 };{ title = "Yeast of Eden";author = "John Sconebeck";rating = 2;price = 6.00 };{ title = "One Hundred Years of Solid Food";author = "G. Gordita Marquez";rating = 4;price = 17.00 }|]Themake_tablefunction transforms records into a table in three steps:Convert each field into a text box and stack related fields vertically, aligning them according to their data type (lines 6–9).Place a column header above each of the resulting columns (lines 11–15).Put vertical bars around the titled column boxes (line 17).⊕Themake_tablefunction renders a book metadata array as anasciitable.letmake_table t =let open Box inlet make_column f align =Array.map (fun b -> f b |> of_string) t |> vconcat ~align inlet cols = [|("Title", make_column (fun b -> b.title) `Left);("Author", make_column (fun b -> b.author) `Left);("Rating", make_column (fun b -> String.make (b.rating) '*') `Left);("Price", make_column (fun b -> Printf.sprintf "%.2f" b.price) `Right);|] inlet titled = Array.map (fun (h, column) ->let header = of_string h inlet hbar = fill '-' 1 (max (width header) (width column) + 2)in vconcat [| header; hbar; column |]) cols inlet vbar = fill '|' (height titled.(0)) 1 inArray.fold_left (fun acc col -> hconcat [| acc; col; vbar |]) vbar titledRendering the book metadata results in a neatasciitable.⊕Rendered book metadata array.$ make_table books |> Box.print_box| Title | Author | Rating | Price ||---------------------------------|---------------------|--------|-------|| Waiting for Good Dough | Samuel Biscuit | **** | 23.86 || The Bun Also Rises | Ernest Hemingwaffle | ***** | 9.86 || Yeast of Eden | John Sconebeck | ** | 6.00 || One Hundred Years of Solid Food | G. Gordita Marquez | **** | 17.00 |

## Closing words

If you found box combinators interesting and want to play with them:Implement them in your preferred language.Use them to visualize complex data.
If you have no good ideas,formatting a calendarwill stretch your box-welding skills.Study their graphical counterparts that appear in bothStructure and Interpretation of Computer Programs(section 2.2.4)
andAlgebra-Driven Designby Sandy Maguire
(chapter 2).

## Appendix: the Box module

This text box implementation is not the most efficient since combining boxes in a loop has quadratic complexity.
A more sophisticated design would combine boxes lazily, delaying concatenations until the last moment or avoiding them entirely.
However, the simple approach is good enough for data that fits on a screen.⊕A simple implementation of the box combinator library.
This code belongs in thebox.mlfile.type t = string arraylet height b = Array.length blet width b = if Array.length b == 0 then 0 else String.length b.(0)(** Returns the box height and width. *)let dimensions b = height b, width b(** Prints box b to the standard output. *)let print_box b = Array.iter print_endline b(** Creates a box large enough to hold string s. *)let of_string s = [| s |](** Creates an h×w box filled with character c. *)let fill c h w = Array.make h (String.make w c)(** Creates a 1×1 box containing character c. *)let of_char c = fill c 1 1(** Creates an h×w box filled with spaces. *)let space h w = fill ' ' h w(** An empty box. *)let empty = space 0 0(** The vertical alignment type. *)type vertical = [ `Top | `Center | `Bottom ](** The horizontal alignment type. *)type horizontal = [ `Left | `Center | `Right ](** Stack box l to the left of box r. *)let recbeside ?(align:vertical = `Center) l r =if width l == 0 then r else if width r == 0 then lelse let hl = heighten ~align (height r) l inlet hr = heighten ~align (height l) r inArray.map2 String.cat hl hr(** Stack box t above of box b. *)andabove ?(align:horizontal = `Center) t b =if height t == 0 then b else if height b == 0 then telse let wt = widen ~align (width b) t inlet wb = widen ~align (width t) b inArray.append wt wb(** Makes box b at least w units wide. *)andwiden ?(align:horizontal = `Center) w b =if width b >= w then belse let bh, bw = height b, width b inlet pw = w - bw inmatch align with| `Left -> beside b (space bh pw)| `Right -> beside (space bh pw) b| `Center -> hconcat[| space bh (pw/2); b; space bh (pw - pw/2) |](** Makes box b at least h units high. *)andheighten ?(align:vertical = `Center) b h =if height b >= h then belse let bh, bw = height b, width b inlet ph = h - bh inmatch align with| `Top -> above b (space ph bw)| `Bottom -> above (space ph bw) b| `Center -> vconcat [| space (ph/2) bw; b; space (ph - ph/2) bw |](** Stacks an array of boxes horizontally. *)andhconcat ?(align:vertical = `Center) boxes =Array.fold_left (beside ~align) empty boxes(** Stacks an array of boxes vertically. *)andvconcat ?(align:horizontal = `Center) boxes =Array.fold_left (above ~align) empty boxes(** Arranges a 2-D array of boxes. *)letgrid g = Array.map hconcat g |> vconcat(** Draws an ASCII art frame around box b. *)letframed b =let h, w = dimensions b inlet vbar = fill '|' h 1 inlet hbar = fill '-' 1 w inlet corner = of_char '+' ingrid [| [| corner; hbar; corner |]; [| vbar; b; vbar |]; [| corner; hbar; corner |] |]

## Similar articles

* ONNX introduction
* Effective design docs
* Static types are for perfectionists
* Transposing tensor files
* The plan-execute pattern

Three degrees of validity→
