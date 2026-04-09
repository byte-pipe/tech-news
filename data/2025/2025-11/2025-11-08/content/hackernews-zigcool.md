---
title: ZigCool
url: https://nilostolte.github.io/tech/articles/ZigCool.html
site_name: hackernews
fetched_at: '2025-11-08T11:06:44.493922'
original_url: https://nilostolte.github.io/tech/articles/ZigCool.html
author: vitalnodo
date: '2025-11-08'
---

# Why is Zig so Cool?

by Nilo Stolte

## Foreword

I can’t think of any other language in my 45 years long career that
surprised more thanZig. I can easily say that Zig is
not only a new programming language, but it’s a totally new way to write
programs, in my opinion. To say it’s merely a language to replace C or
C++, it’s a huge understatement.

In this article, I will present the features that I found to be most
seductive in the language, and I will also present a brief overview
about it. The goal is to presentsimplefeatures for
programmers to quick start in the language. Be aware, though, that many
more features are affecting its acceptability in the industry.

## The compiler

### It compiles C and it cross
compiles

Probably the most incredible virtue of Zig compiler is its ability to
compile C code. This associated with the ability to cross-compile code
to be run in another architecture, different than the machine where it
is was originally compiled, is already something quite different and
unique. These features alone, completelyout-of-the-box, are causing an incredible impact in the
industry already.In spite of that what we want to concentrate on is how
to program in Zig and why should one choose Zig instead of any other
language.

### Installing the compiler

Installing the compiler is quite simple. InZinglang’s download pageone
finds the compiler in several formats, depending on the processor or
OS:

OnWindows 10, for example, one chooses thex86_64zip file and copy its decompressed content in
the desired directory. For example, in “Program Files”. I modified the
root directory name to “zig-windows-x86_64” because in this way I can
just copy another version of the compiler with no need to modify the
path inPathenvironment variable.

Next, one adds this root directory path to thePathenvironment variable using Advanced System Properties (clicking on 1-4,
pasting path on 5, and clicking “OK” on 6-8):

Notice that after setting the
path to Zig’s root directory one can already use the compiler in CLI
mode. That’s the recommended way to use it for the sake of
simplicity.

### Building a “Hello World!”
program in Zig

It’s recommended to build a “Hello World!” program using the
instructions in the “Getting Started” section in thissite. An alternative installation
procedure is also presented there, including for MacOS and Linux
(“Installing manually” is highly recommended). It’s also recommended to
check the “Language” Basissection, for a
deeper insight of Zig language.

## Main concepts and commands

The following sections will give a bird’s eye view of Zig language.
Their goal is to instruct the programmer how to quickly start
programming in Zig by just knowing a few basic concepts and
commands.

Then, a compact view on how to build programs and test modules is
given.

Finally, a deeper view on how low level programming can be done in
Zig. A more detailed explanation on the examples used is also given.

### Variable declaration

Normally, variable declarations in Zig have potentially three parts.
The first part contains the accessibility (pubor nothing),
followed by the wordvarorconst, followed by
the variable name. The second part, separated of the first part by a
colon, contains the variable type declaration. The third part is the
initialization of the variable. Only the first and third part are
compulsory in Zig, which is kind of puzzling, coming from Java or C. One
may wonder how the compiler discovers the variable type. The type in
this case isinferredby the initialization.

var sum : usize = 0; // variable declaration with 3 parts

Variables that don’t have their accessibility explicitlypubare local to the module, that is, they aren’t
accessible outside the source file it was declared (just likestaticvariables in C). It’s not recommended to have
variables declaredpuband it’s recommended to have just
few functions declaredpubin a module to discourage
coupling and encourage cohesion. Thepubfunctions behave
as the module’s API.

### Structs, anonymous
structs and test block

In Zig, a.{closed with a}is an“anonymous struct literal”- an anonymous struct mostly used to
initialize the elements of another structure or to create a new
structure with its elements initialized. A.{ }is an an
empty anonymous struct literal. The wordstructfollowed by
a{and closed with a}is a struct
declaration. One can initialize a variable with a type, which functions
as an alias to the type. Notice the“test block”allowing to
compile and execute tests without the need of an executable.

### Bitfields

Bitfields are declared fields with types having specific sizes in apacked struct. Pointers can point to a specific bit field
as shown here:

### For loops

Zig syntax is clearer than C’s, except that one would think it should
be[0..8], but in reality it’s an open interval:[0..9).Advantage in Zig: the type
declaration ofi, its initialization, test, and
incrementation are automatic.

### Arrays

A[_]defines an array with unknown size. It must be followed
by the type of its elements (hereu8,unsigned
byte) and its initialization between{and}. In this example below, the initialization is saying that
this is an array of unknown size ([_]) where each element
is of typeu8(unsigned byte) and each element initialized
with zeros ({0} ** 81). Notice that the size is also
inferred by the repetition factor (81) of the
initialization ({0}).

var grid = [_]u8{0} ** 81;

We see in the figure below a test environment with a loop interacting
over the array and adding its elements. Thetry expectstatement verifies thatsumis correct.

The wordbyteis not a type or reserved word in Zig.
Here, it’s a variable to hold each of the array’s elements on each step
of the loop. Notice that a variable declared between two|with an array between the parenthesis of a for loop is always assumed of
the same type as the array elements.

Notice also, thatusizeis the natural unsigned integer
for the platform. That means on 64 bits machines it’s anu64, and in 32 bits machines it’s anu32.

### Many-item pointers in Zig

Pointers to arrays can use pointer arithmetic only if the pointer isexplicitlydeclared as a many-item pointer, here[*]const i32. Notice that the array below isconst, can’t be changed, but that the pointer isvar.

### Dereferencing Pointers

When attributed the address of an individual array position, a
pointer cannot be updated with pointer arithmetic. In this case,constonly prevents its value to be changed with another
direct address attribution. To dereference pointers in Zig one uses theptr.*as shown below:

### Labeled breaks

Zig can do many things in compilation time. Let’s initialize an
array, for example. Here, alabelled breakis used. The block
is labelled with an:after its nameinitand
then a value is returned from the block withbreak.

This syntax may look overwhelming.0..means an infinite
range starting with zero. In thefor, variablesptandiare respectively initialized with the address ofinitial_valuearray and zero. During the loop both are
incremented automatically and the loop stops right after dealing with
the array’s last position. Also notice how to dereference theptpointer:pt.*.

Also interesting it’s how the array is declared in the labelled
block. The array is calledinitial_valueand has 10
positions of the typePoint(declared afterwards).
Variables must be initialized in Zig. The way to explicitly not
initialize is with the reserved wordundefined.

### Functions in Zig

Functions in Zig are declared withfnand are static by
default (cannot be imported in other files) in the file they are
declared, except whenfnis preceded bypub. A
function can be “inlined.” Function pointers are preceded byconstand followed by the function prototype.

### OOP in Zig

Structs can have functions. Here, a simple stack is implemented. This
stack is declared and used only inside the module it is defined, and it
accesses and modifies other data structures in the module that are
irrelevant in this example. The stack can have at maximum 81 elements
(as seen instkdeclaration), each one of typeStkNode. Notice that ++ and –– operators don’t exist in Zig.
The equivalent += and –=should be used instead. The stack pointer is
just an integer used as an index in thestkarray.

Notice that the pointerself(selfis not a
reserved word, but it’s just a convention) is not passed explicitly as a
parameter as one would normally expect. It is indirectly assumed that it
is a pointer to the instance of the stack the function is been called
from. In the example below, a stack pop would be called withstack.pop();. In this case the pointerselfcorresponds to a pointer tostack. This pointer is then
somewhat equivalent tothisin Java or C++.

Functioninit()is the stack constructor.

Notice as well that functionspopandpushare “inlined.”

## Building and executing Zig
programs

### Building an executable

To build an executable program one needs amainfunction, which indicates the program entry point as in Java or C
programs. When this function exists the set of modules can be compiled
to an executable code. A simple program can have amainfunction in the same file as the rest of the program. In many cases one
can also insert a main function at the end of a module to create an
executable in order to debug the module independently. Once debugged
this function can be commented out.

In these situations one can use the following command line to compileprogram.zigand to generate an executable program (on
Windows, aprogram.exe):

zig build-exe -O ReleaseFast program.zig

This can be put inside a batch file to prevent typos.

### Executing test blocks in a
module

This is probably the best feature of Zig as a programming language.
This environment is normally used for testing, but it can also be used
for prototyping.

A block in Zig is similar to a block in C or Java, that is, some code
between{and}. Atest blockis a
block that starts withtest "message" {and finishes with}, where"message"is a string containing the
message to be displayed when the test is executed (in this case only the
wordmessage).

Test blocks are executed independently from an executable file. The
final executable file does not execute the tests. The test blocks in a
givenmodule.zigare compiled together with the entire code
in that file and executed by the following command:

zig test module.zig

##### Example

As a real life example, thetest blockfrom moduleexample.zigis shown below:

test " => testing set and print functions" {
 set(
 "800000000003600000070090200" ++
 "050007000000045700000100030" ++
 "001000068008500010090000400"
 );
 std.debug.print("\n" ++
 "===================\n" ++
 "Input Grid\n" ++
 "===================\n",
 .{}
 );
 print();
}

Notice thatexample.zigalone has nomainfunction and, therefore, cannot generate an executable, but its test
block can be executed by using the following command:

zig test example.zig

As the message says, the test block above tests the functionssetandprint. As the code shows,setpasses a string of decimal digits as a parameter,
followed by a print statement (which prints a header saying “Input Grid”
), followed itself by a call of theprintfunction.

The real display in a command tool is the following:

##### Printing in Zig

Let’s focus now on thestd.debug.printstatement. This
statement is in fact a call to the functionprintindebug.zigin the standard Zig librarystd. The
first parameter is a format string, and the second is ananonymous
struct(preceded by a dot) containing a list of variables to be
displayed using the format string. Since there is no formatting in the
format string, the struct is empty. This is how formatted prints are
done. This one will display in thestderrby default, as shown
above.

This all looks just like in C language, but there is a fundamental
difference here. In C, theprintffunction dynamically
interprets the format string in execution time, whereas in Zig it’s
possible to deal with the literal string and the list of variables in
compilation time. This is a difficult principle to grasp at the start.
Many things can beexecutedin compilation time.

### Debugging an executable

Using a debugger is not usually a straightforward task, except in
IDEs that already integrate a debugger (as in Java IDEs such as Eclipse
or Intellij IDEA) or in integrated development kits (such as w64devkit
for C/C++).

A huge inconvenient in using debuggers in this way is that one must
integrate the symbols, which not only bloats the code with information
that is not useful to the program, but also requires compiling in Debug
mode, which generates executable code that’s notoriously less efficient.
Someone with practice in complex systems knows that it can be a very
time consuming task.

Zig offers a quite convenient hack in order to avoid these
headaches.

##### The@breakpointbuilt-in

This built-in stops a program at the point where a@breakpoint();is inserted in the source code when its
executable is run in a debugger. This is actually an useful feature to
debug optimized Zig code without the need of symbols.

All it’s needed is to trace the variables one wants to watch usingstd.debug.printright before@breakpoint();In
this way one can know what are the values of the variables at that exact
moment.

##### Example

As a real life example, one generates an executable for moduledebug_example.zigwhich has the has the followingmainfunction:

pub fn main() !void {
 set(
 "800000000003600000070090200" ++
 "050007000000045700000100030" ++
 "001000068008500010090000400"
 );
}

To be able to double check with the results fromexample.zig,
the parameter passed tosetfunction in thismainis the same string as the one passed tosetin the test block inexample.zig,
but this time one inserts the following code insidesetfunction:

 if (c != 0) {
 print();
 std.debug.print(
 "Current digit {}\nposition in string {}\n" ++
 "line {}\ncolumn {}\ncode {b}\n",
 .{c, k, i, j, code}
 );
 @breakpoint();
 }

One can then generate thedebug_example.exeexecutable
with the following build command:

zig build-exe debug_example.zig

Next, one uses a debugger to calldebug_example.exe. In
this case I usedgdb, a debugger for C/C++ included in
w64devkit, but it could be any debugger for executable programs. Once
insidegdb, one needs to run the program using anrcommand and typingEnterright after as
shown below. Notice that the program printed the grid with its contents
so far as well as the variables, stopping
at the point expected. Then, by typingccommand followed
by anEnterone continues tracing the grid contents and
the variables. After that, one can continue by just typingEnter(it repeats the last command -c, in this
case). By continuing typingEnteruntil the program finishes,
the values found in the grid correspond to the values shown by the test
block inexample.zigabove, since both examples have the same
parameter passed toset.

## Low level programming in Zig

With the introduction and the examples given in the previous
sections, one can already start programming Zig for writing generic
applications. For more advanced programmers, what follows is a more
in-depth analysis of some interesting low-level features already used in
the examples, but not yet explicitly commented.

The idea of the examples shown is to construct a module that sets
(initializes) and displays a 9x9 matrix. This matrix will hold a Sudoku
grid, that is, it will only contain elements with decimal digits. The
initialization of the grid should guarantee that the grid satisfies the
rules of Sudoku game, so it will contain no errors.

At the same time it would be also an excellent opportunity to
demonstrate Zig’s low level capabilities, at least the most noticeable
ones, and these examples fit this goal quite well.

The whole hypothesis behind these examples is the representation of a
grid digit as a bit in the position given by its value. This
representation is quite convenient to detect if a digit is already
present in the grid or not (these are basic rules of Sudoku grids). In
spite of that, this is so encrypted it is only used internally in the
module.

### Representing a matrix

With the purpose of having values that are easily understood by
humans, the digits are actually stored in the matrix as standardu8integers. Even though the input grid in the examples is
given in string format, the ASCII characters are internally converted tou8integers. The digits’ storage in the grid is organized
linearly, line by line, in an array with 81 positions, calledgridin the examples:

var grid = [_]u8{0} ** 81; // Sudoku grid stored linearly

To verify grid correctness, one needs to access the elements by its
respective line and column. In other words, one needs to access the
elements as in a matrix. The strategy is to create an array of pointers
with 9 positions, each one pointing to the start of each line. Blocks of
code cannot in principle return a value, but in Zig they can with
labeled breaks:

const matrix = fill9x9: { // matrix array to allow access
 var m : [9][*]u8 = undefined; // to grid element as a matrix,
 var pt : [*]u8 = &grid; // thus: element = matrix[i][j]
 for (0..9) |i| { //
 m[i] = pt; // stores pointers of each line
 pt += 9; // at each position of matrix
 } //
 break :fill9x9 m; // initializes matrix with m
};

At the end of the loop,mis returned outside the block
using abreak :fill9x9 m;command. Notice thatfill9x9corresponds to the name of a label placed right
before the beginning of the block.

Supposingiandj, respectively an
element’s line and column, any element of the grid can be accessed using
this notation:

element = matrix[i][j]

### Representing decimal digits
as bits

The key concept used here is the replacement of an integer decimal
digitiby an integercodesuch as:

 i ∈ [1,9] → code = 2ⁱ⁻¹
 i = 0 → code = 0

In other words, the only bit ofcodethat is set to1is the bit at the positioni-1ifiis between1and9, otherwise
all bits ofcodeare zero.

##### Values ofcodefor
each digit

The table below shows the correspondence between digits and their
binary representation:

##### Calculatingcodein
Zig

The value ofcodeis calculated in the functionsetusing a left shift operator only ifcis
not zero:

code = @as(u9,1) << (c-1);

In Zig, constants must have a proper size in order to allow an
operation to be compiled and to attribute the the result of an operation
to a given variable. In this case,codeis declared of typeu9. That’s another fundamental quality of Zig, to be able
to have variables witharbitrary bit size. As can be
seen in the table above, the maximum value thatcodecan have is 256,
which requires at least 9 bits to represent. The built-in@asallows to cast the1constant to typeu9.

### Representing the grid
using bitfields

By representing digits as bits one can mirror the entire grid in much
simpler ways.

##### Line by line bitfield grid

The arraylinesmirrors the entire grid by representing
each line with a9bits integer, each bit representing a
decimal digit that might be present in the a line:

var lines = [_]u9{0} ** 9;

In this way, by just accessing this array with the lineiof an element in the 9x9 grid one can know if a given
digit is already present in that line, by just performing a bitwiseand(&) with the digit’scode, in this way:

lines[i] & code

If the result of the operation above is zero, this means the digit is
not yet present in the linei. Otherwise we have a
duplicate.

##### Column by column bitfield
grid

The arraycolumnsmirrors the entire grid by
representing each column with a9bits integer:

var columns = [_]u9{0} ** 9;

In this way, by just accessing this array with the columnjof an element in the 9x9 grid one can know if a given
digit is already present in that column, by just performing a bitwiseand(&) with the digit’scode, in this way:

columns[i] & code

If the result of the operation above is zero, this means the digit is
not yet present in the columnj. Otherwise it’s a
duplicate.

##### Sudoku rules

Let’s suppose an empty Sudoku grid, as it is the case when one is
populating the grid with the input string as done in the examples. A new
digit inserted at any empty element, must not already exist in the
entire line, column or cell containing the new element.

Let’s suppose now this grid, already initialized:

Acellis each one of the nine 3x3 grids delimited by the
thick lines. The key knowledge to understand at this point is that each
specific element in the 9x9 grid has a unique line, column and cell that
contains this element.

For example, the first cell of the grid contains the values: 3, 5, 6,
8, and 9. Therefore, the values: 1, 2, 4 and 7 are missing. Let’s suppose
one is willing to place the value 7 in one of the empty places in the
first cell. Obviously, one cannot place it in the only empty element of
the first line, because 7 is already present in that line. One cannot
place it in the only empty place in the first column either since 7 is
already in that column. One can only place the 7 in one of the two empty
elements of the second line. But one can’t know for sure which one is
the good one.

Let’s examine now the second cell, which contains the values: 1, 5,
7, and 9. One can see that the only possible element in this cell where an 8
can be placed is in the first line at the empty position on the right of
the value 7.

Arrayslinesandcolumnstake care of
checking duplicates in lines and in columns. A new array is then needed
to check duplicates in cells.

##### Cell by cell bitfield grid

The arraycellsmirrors the entire grid by representing
each cell with a9bits integer:

var cells = [_]u9{0} ** 9; // all elements at each cell

Here is where things get more complicated. One cannot accesscellsdirectly using the line or the column. It would be
easier if one could accesscellsas a 3x3 matrix. This can
be done mimicking what has been done for the 9x9 matrix, that is,
filling the arraycellas follows:

const cell = fill3x3: { // cell array to allows access
 var m : [3][*]u9 = undefined; // cell elements as a matrix,
 var pt : [*]u9 = &cells; // cell[cindx[i]][cindx[j]]
 for (0..3) |i| { //
 m[i] = pt; // stores pointers of each line
 pt += 3; // at each position of cell
 } //
 break :fill3x3 m; // initializes cell with m
}; //

But now one needs to determine the line and column incellmatrix from the line and column of the element in the
original 9x9 grid. One could use integer divisions to divide the line
and column by 3 to obtain the proper indexes, but a division operation
is notoriously slow. Two divisions makes it even worse. One can use the
following array to give the result of the division as follows:

const cindx = [_]usize{ 0,0,0, 1,1,1, 2,2,2 };

In this way, by just accessing this matrix with the lineiand columnjof an element in the 9x9 grid,
one can know if a given digit is already present in this element’s cell
by just performing a bitwiseand(&)
with the digit’scode, in this way:

cell[cindx[i]][cindx[j]] & code

If the result of the operation above is zero, this means the digit is
not yet present in the cell. Otherwise it’s a duplicate.

### Testing if an element is
duplicated

The complete test to verify if an element is duplicated can be done
by composing with a bitwiseor(|)
all the previous elements in the same line, column and cell, and then
performing a bitwiseand(&) with
the element’scode, in this way:

if (((lines[i]|columns[j]|cell[cindx[i]][cindx[j]])&code) != 0) {
 unreachable;
}

If the result is zero it’s because the element doesn’t exist yet in
its line, column or cell. If the result is not zero the program stops
because it tries to run the instructionunreacheable. This
is the simplest way to explicitly indicate an execution error in Zig.
Notice that the actual code insetfunction also prints the
details where the error occurs.

For example, replacing the'0'right after the first'8'by a'5'in the string passed tosetgives the following error while testingexample.zig:

This is because in column 1 there was already a 5 in line 3 as the
error message says. The error is due to a panic caused by reaching an
unreachable code at functionsetas indicated.

### Updating the data structures

In functionset, a doubleforloop
interacts line by line to copy each new element from the input stringsinto the grid as indicated below (variablekkeeps the index of the new input character in the strings):

 for ( 0..9 ) |i| {
 line = matrix[i];
 for ( 0..9 ) |j| {
 c = @intCast(s[k]-'0');
 if (c != 0) {
 code = @as(u9,1) << (c-1);
 ⋮ // rest of the code
 }
 line[j] = c;
 k+= 1;
 }
 }

The character is converted to anu4(variablec) by subtracting'0'from it. If the new
element to be inserted in the grid is not equal to zero (c != 0),code(calculated with a left shift
instruction as indicated) is copied in each of the mirror grids, by
doing a bitwiseor(|=) with the
corresponding mirror grid, that is:

 lines[i] |= code;
 columns[j] |= code;
 cell[cindx[i]][cindx[j]] |= code;

No test is required to explicitly test if the value ofcis between1and9because an overflow will
occur at execution time when the shift operation is executed. For
example, replacing the'0'right after the first'8'of the input string by a':'in the string
passed tosetgives the following error while testingexample.zig:

By substituting the same'0'by a'/'a
similar execution error will issued. The program will work only if the
values are between1and9, that is, if the
input grid contains only decimal digits.

Many Sudoku grids on the web also represent'0'as a'.'. That’s the reason the following line exists insetfunction:

if (s[k] == '.') c = 0;

This will conveniently bypass the shift operation because the value ofcis zero.

### Prototyping and robustness

The forced errors shown in the two sections above demonstrate
important features of Zig that might have passed inconspicuously. One is
Zig’srobustness. In the case of the shift operation no
wrong behavior is allowed and the situation is caught at execution time,
as has been shown.

One might think that all the efforts in Zig are towards efficiency,
but here it’s a typical case where performance was traded for
robustness. One can have mixed feelings about this decision, when
performance was the ultimate goal. In C, for example, it’s the
programmer’s problem if a shift operation loses a bit and this
translates in better performance for this specific Assembler
instruction.

Another feature demonstrated in the two sections above is the
possibility of using the test blocks forprototypingas
suggested at the beginning of the article. The possibilities are
numerous, even though the application shown was only to debug certain
situations in cases of error.

These features alone demonstrate an awesome power, very rare in
programming languages, particularly in compiled programing
languages.

## Conclusion

This is all quite surprising and let one think that many advantages
previously found only in interpreted languages are gradually migrating
to compiled languages in order to offer more performance. [A reference
to Mojo here looks appropriate].

Zig resemblance to interpreted languages is quite striking,
particularly with its concept ofcompile time
execution, unfortunately not stressed enough in this article.
This is an aspect of Zig that on one hand makes it particularly
different and powerful but on the other hand difficult to grasp.

I concentrated more in instructing how to have a quick and easy start
with the language, and insimpleaspects that make Zig
language cool, although there are many other aspects not mentioned here
that are also quite impressive.

The examples shown here are simplified versions of a more involved
program tosolve
Sudoku grids, which was also developed in Java and in C. The
documentation in this repository explains in detail most of the
structures and algorithms used to accomplish that.
