---
title: 'Phrase origin: Why do we "call" functions? – Arthur O''Dwyer – Stuff mostly about C++'
url: https://quuxplusone.github.io/blog/2025/04/04/etymology-of-call/
site_name: lobsters
fetched_at: '2025-07-09T23:06:51.704675'
original_url: https://quuxplusone.github.io/blog/2025/04/04/etymology-of-call/
author: Arthur O’Dwyer
date: '2025-07-09'
description: 'On StackExchange, someone asks why programmers talk about “calling” a function. Several possible allusions spring to mind: Calling a function is like calling on a friend — we go, we stay a while, we come back. Calling a function is like calling for a servant — a summoning to perform a task. Calling a function is like making a phone call — we ask a question and get an answer from outside ourselves. The true answer seems to be the middle one — “calling” as in “calling up, summoning” — but indirectly, originating in the notion of “calling for” a subroutine out of a library of subroutines in the same way that we’d “call for” a book out of a closed-stack library of books.'
tags: historical, plt
---

# Phrase origin: Why do we “call” functions?

OnStackExchange,
someone asks why programmers talk about “calling” a function. Several possible allusions spring to mind:

* Calling a function is like calling on a friend — we go, we stay a while, we come back.
* Calling a function is like calling for a servant — a summoning to perform a task.
* Calling a function is like making a phone call — we ask a question and get an answer from outside ourselves.

The true answer seems to be the middle one — “calling” as in “calling up, summoning” —
but indirectly, originating in the notion of “calling for” a subroutine out of a library of subroutines
in the same way that we’d “call for” a book out of a closed-stack library of books.

The OED’s first citation forcall numberin the library-science sense comes fromMelvil Dewey(yes,that Dewey)
in 1876. The OED defines it as:

A mark, esp. a number, on a library book, or listed in a library’s catalogue,
indicating the book’s location in the library; a book’s press mark orshelf mark.

I see librarians using the term “call-number” inThe Library Journal13.9(1888) as if it was very well established already by that point:

Mr. Davidson read a letter from Mr. A.W. Tyler […] enclosing sample of the newcall blankused at the
Plainfield (N.J.) P. L., giving more room for the signature and address of the applicant. […]
“In connection with Mr. Tyler’s newcall slip[…] I always feel outraged when I make up a long list
ofcall numbersin order to make sure of a book, and then the librarian keeps the list, and the next
time I have it all to do over again.”

According toThe Organization of Information4th ed. (Joudrey & Taylor, 2017):

Call number.A notation on a resource that matches the same notation in the metadata description and
is used to identify and locate the item; it often consists of a classification notation and a cutter number,
and it may also include a workmark and/or a date. It is the number used to “call” for an item in a closed-stack
library; thus the source of the name “call number.”

Cutter number.A designation with the purpose of alphabetizing all works that have exactly the same classification notation.
Named forCharles Ammi Cutter, who devised such a scheme, but spelled
with a smallcwhen referring to another such table that is not Cutter’s own.

John W. Mauchly’s article“Preparation of problems for EDVAC-type machines”(1947)
uses the English word “call” only twice, yet this seems to be an important early attestation of the word
in the context of a “library” of computer subroutines:

Important questions for the users of a machine are: How easily can reference be made to any of the subroutines?
How hard is it to initiate a subroutine? What conditions can be used to terminate a subroutine? And with what
facility can control revert to any part of the original sequence or some further sequence […] Facilities
for conditional and other transfers to subroutines, transfers to still further subroutines, and transfers
back again, are certain to be used frequently.

[…] the position in the memory at which arguments are placed can be standardized, so that whenever a subroutine
iscalled into perform a calculation, the subroutine will automatically know that the argument which is to
be used is at a specified place.

[…] Some of them might be written out in a handbook and transferred to the coding of the problem as needed,
but those of any complexity presumably ought to be in alibrary— that is, a set of magnetic tapes in which
previously coded problems of permanent value are stored.

[…] One of the problems which must be met in this case is the method of withdrawal from the library
and of compilation in the proper sequence for the particular problem. […] It is possible […] to evolve
a coding instruction for placing the subroutines in the memory at places known to the machine, and in such
a way that they may easily becalled into use[…] all one needs to do is make brief reference to them
by number, as they are indicated in the coding.

The manual for the“MANIAC II assembly routine”(January 1956)
follows Mauchly’s sketch pretty closely. MANIAC II has a paper-tape “library” of subroutines which
can be summoned up (by the assembler) to become part of a fully assembled program, and in fact each item
in the “library” has an identifying “call number,” just like every book in a real library has a call number:

The assembly routine for Maniac II is designed to translate descriptive code into absolute code. […]
The bulk of the descriptive tape consists of a series of instructions, separated, by control words,
into numbered groups calledboxes[because flowcharts: today we’d say “basic blocks”]. The allowed
box numbers are01throughEF[. …] If the address [in an instruction’s address field] isFXXX,
then the instruction must be a transfer, and the transfer is to the subroutine whosecall numberisXXX. The most common subroutines are on the same magnetic tape as the assembly routine, and are
brought in automatically. For other subroutines, the assembly routine stops to allow the appropriate
paper tapes to be put into the photoreader.

Notice that the actual instruction (or “order”) in MANIAC II is still known as “TC,” “transfer control,”
and the program’s runtime behavior is known as atransfer of control, not yet as acall.
Thecallinghere not the runtime behavior but rather the calling-up of the coded subroutine (at assembly time)
to become part of the fully assembled program.

Fortran II(1958; alsohere)
introducedCALLandRETURNstatements, with this description:

The additional facilities of FORTRAN II effectively enable the programmer to expand the language
of the system indefinitely. […] Each [CALL statement] will constitutea call forthe defining subprogram,
which may carry out a procedure of any length or complexity […]

[The CALL] statement causes transfer of control to the subroutine NAME and presents the subroutine
with the arguments, if any, enclosed in parentheses. […] A subroutine introduced by a SUBROUTINE
statement iscalled intothe main program by a CALL statement specifying the name of the subroutine.
For example, the subroutine introduced by

SUBROUTINE MATMPY (A, N, M, B, L, C)



could becalled intothe main program by the statement

CALL MATMPY (X, 5, 10, Y, 7, Z).



Notice that Fortran II still describes the runtime behavior as “transfer of control,”
but as the computer language becomes higher-level the English starts to blur and conflate
the runtime transfer-of-control behavior with the assembly- or link-time “calling-in” behavior.

In Robert I. Sarbacher’sEncyclopedic dictionary of electronics and nuclear engineering(1959),
the entry forSubroutinedoesn’t use the word “call,” but Sarbacher does seem to be reflecting
a mental model somewhere inside the union of Mauchly’s definition and Fortran II’s.

Call in.In computer programming, the transfer of control of a computer from a
main routine to a subroutine that has been inserted into the sequence of calculating
operations to perform a subsidiary operation.

Call number.In computer programming, a set of characters used to identify
a subroutine. They may include information related to the operands, or may be used
to generate the subroutine.

Call word.In computer programming, a call number exactly the length of one word.

Notice that Sarbacher defines “call in” as the runtime transfer of control itself;
that’s different from how the Fortran II manual used the term.MaybeSarbacher was
accurately reflecting an actual shift in colloquial meaning that had already taken place
between 1958 and 1959 — but personally I think he might simply have goofed it.
(Sarbacher was a highly trained physicist, but not a computer guy, as far as I can tell.)

“JOVIAL: A Description of the Language”(February 1960) says:

Aprocedure call[today we’d say “call site”] is the link from the main program
to a procedure. It is the only place from which a procedure may be entered.

Aninput parameter[today we’d say “argument”] is an arithmetic expression specified in theprocedure callwhich represents a value on which the procedure is to operate[.] Adummy input parameteris an item specified in
the procedure declaration which represents a value to be used by the procedure as an input parameter.

One or moreProcedure Calls(ofother procedures) may appear within a procedure.
At present, only four “levels” ofcallsmay exist.

That JOVIAL manual mentions not only the “procedure call” (the syntax for transferring control to a procedure declaration)
but also the “SWITCHcall” (the syntax for transferring control to a switch-case label). That is, JOVIAL (1960) has
fully adopted thenoun“call” to mean “the syntactic indicator of a runtime transfer of control.”
However, JOVIAL never uses “to call” as a verb.

Backtracking a few months, here’s Perlis & Samelson’s“Preliminary Report—International Algebraic Language”(CACM2(6), June 1959):

Aprocedurestatement serves to initiate (call for) the execution of aprocedure,
which is a closed and self-contained process […] The procedure declaration defining thecalledprocedure contains,
in its heading, a string of symbols identical in form to the procedure statement, and the formal parameters […]
give complete information concerning the admissibility of parameters used in anyprocedure call[.]

Peter Naur’s“Algol 60 Report”(May 1960) avoids the verb “call,”
but in a new development casually uses the noun “call” to mean “the period during which the procedure itself is working” —
not the transfer of control but the periodbetweenthe transfers in and out:

A procedure statement serves to invoke (call for) the execution of a procedure body. […]
[When passing an array parameter, if] the formal parameter is called by value the local array createdduring the callwill have the same subscript bounds as the actual array.

Finally,“Burroughs Algebraic Compiler: A representation of ALGOL for use with the Burroughs 220 data-processing system”(1961)
attests a single (definitionary) instance of the preposition-less verb “call”:

TheENTERstatement is used to initiate the execution of a subroutine (tocalla subroutine).

The usage in“Advanced Computer Programming: A case study of a classroom assembly program”(Corbató, Poduska, & Saltzer, 1963)
is entirely modern: “It is still convenient for pass one tocalla subroutine to store the cards”; “In order tocallEVAL,
it is necessary to save away temporary results”; “the subroutine whichcallsPASS1andPASS2”; etc.

Therefore my guesses at the moment are:

* Fortran II (1958) rapidly popularized the phrasing “to call X” for the temporary transfer of control to X,
 because “CALL X” is literally what you write in a Fortran II program when you want to transfer control
 to the procedure namedX.
* Fortran’s own choice of the “CALL” mnemonic wasan original neologism,inspired by the pre-existing use
 of “call (in/up)” as seen in the Mauchly and MANIAC II quotations but introducing wrinkles that had never been
 seen anywhere before Fortran.
* By 1959, Algol had picked up “call” from Fortran. Algol’s “procedure statements” producedcallsat runtime;
 a procedure couldbe called; duringthe callthe procedure would perform its work.
* By 1961,we see the first uses of the exact phrase “to call X.”

 Posted 2025-04-04


digital-antiquaria

etymology
