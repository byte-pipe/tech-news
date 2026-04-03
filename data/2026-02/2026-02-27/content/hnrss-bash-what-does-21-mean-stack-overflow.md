---
title: bash - What does " 2>&1 " mean? - Stack Overflow
url: https://stackoverflow.com/questions/818255/what-does-21-mean
site_name: hnrss
content_file: hnrss-bash-what-does-21-mean-stack-overflow
fetched_at: '2026-02-27T11:16:03.626495'
original_url: https://stackoverflow.com/questions/818255/what-does-21-mean
date: '2026-02-26'
description: What does " 2>&1 " mean?
tags:
- hackernews
- hnrss
---

3293

To combinestderrandstdoutinto thestdoutstream, we append this to a command:

2>&1

For example, the following command shows the first few errors from compilingmain.cpp:

g++ main.cpp 2>&1 | head

But what does2>&1mean?

* bash
* shell
* unix

edited
Aug 6, 2024 at 23:26

Mateen Ulhaq

28k
22
22 gold badges
122
122 silver badges
157
157 bronze badges

 asked
May 3, 2009 at 22:57

Tristan Havelick

70.1k
20
20 gold badges
58
58 silver badges
65
65 bronze badges

10

## 19 Answers19

 Sorted by:


 Reset to default


 Highest score (default)


 Trending (recent votes count more)


 Date modified (newest first)


 Date created (oldest first)


3729

File descriptor 1 is the standard output (stdout).File descriptor 2 is the standard error (stderr).

At first,2>1may look like a good way to redirectstderrtostdout. However, it will actually be interpreted as "redirectstderrto a file named1".

&indicates that what follows and precedes is afile descriptor, and not a filename. Thus, we use2>&1. Consider>&to be a redirect merger operator.

edited
Jul 17, 2022 at 6:18

Mateen Ulhaq

28k
22
22 gold badges
122
122 silver badges
157
157 bronze badges

 answered
May 3, 2009 at 23:04

Ayman Hourieh

139k
23
23 gold badges
149
149 silver badges
116
116 bronze badges

 Sign up to request clarification or add additional context in comments.


## 21 Comments





Add a comment



dokaspar

dokaspar

Over a year ago




but then shouldn't it rather be
&2>&1
?

2013-09-04T06:12:13.6Z+00:00


451


Reply








Adam Rosenfield

Adam Rosenfield

Over a year ago




@Dominik: Nope,
&
 is only interpreted to mean "file descriptor" in the context of redirections. Writing
command &2>&
 is parsed as
command &
 and
2>&1
, i.e. "run
command
 in the background, then run the command
2
 and redirect its stdout into its stdout".

2014-01-28T00:02:30.8Z+00:00


481


Reply








CommaToast

CommaToast

Over a year ago




Why did they pick such arcane stuff as this? Just curious.

2014-05-17T04:00:27.42Z+00:00


103


Reply










Blair

Blair

Oct 9, 2025 at 20:41




I am thinking that they are using & like it is used in c style programming languages. As a pointer address-of operator. Consider the following options:
2>1 would represent 'direct file 2 to file 1'.
,
&2>&1 would represent 'direct the address of file 2 to the address of file 1'
, or
2>&1 would represent 'direct file 2 to the address of file 1'.
 Clearly option 3 does what we want. Directing the output from file 2, to the location that file 1 is using aka its address. Is what we want to do. And it makes sense to a c programmer.

2025-10-09T20:41:17.363Z+00:00


12


Reply










Timmmm

Timmmm

2 hours ago




Whoever designed Bash clearly had no taste at all. It was in the 70s to be fair. Modern shells like Nushell are much less arcane.

2026-02-27T08:40:04.107Z+00:00


0


Reply








Martín Fixman

Martín Fixman

Over a year ago




But how would you redirect stderr to a file named '&1'?

2014-11-04T17:07:08.273Z+00:00


149


Reply








user1247058

user1247058

Over a year ago




@Martin:
2>'&1'

2016-03-14T10:46:22.14Z+00:00


224


Reply









|



1063

To redirect stdout tofile.txt:

echo test > file.txt

This is equivalent to:

echo test 1> file.txt

To redirect stderr tofile.txt:

echo test 2> file.txt

So>&is the syntax toredirectastreamto anotherfile descriptor:

* 0 is stdin
* 1 is stdout
* 2 is stderr

To redirect stdout to stderr:

echo test 1>&2 # equivalently, echo test >&2

To redirect stderr to stdout:

echo test 2>&1

Thus, in2>&1:

* 2>redirects stderr to an (unspecified) file.
* &1redirects stderr to stdout.

edited
Jul 17, 2022 at 6:09

Mateen Ulhaq

28k
22
22 gold badges
122
122 silver badges
157
157 bronze badges

 answered
May 3, 2009 at 22:59

dbr

171k
70
70 gold badges
284
284 silver badges
349
349 bronze badges

## 4 Comments





William Pursell

William Pursell

Over a year ago




@dbr
cmd 2>&1 >>file
 does not redirect stderr to the file, but
cmd >> file 2>&1
 does. Order matters. In the first case, stderr is redirected to the stdout of the shell (possibly a tty if the command is entered interactively), and then stdout is directed to the file. In the second case, stdout is directed to the file, and then stderr is directed to the same place.

2013-07-19T13:15:25.967Z+00:00


124


Reply








Max West

Max West

Over a year ago




I like the answer above, but it could be a touch clearer. "2>&1" redirects stderr to the target of stdout. So if you have something like "ls -l >> directoryContents 2>&1" The result will be a file named directoryContents will have the contents of the working directory appended to it. If there are any errors in execution: the error messages will also be appended to the directoryContents file, as they occur.

2015-04-17T17:36:16.977Z+00:00


6


Reply








Cloud

Cloud

Over a year ago




Is
0(or 1,2)>&0(or 1,2)
 like an option to control the output? Is
echo test >test.log 2>&1
 same as
echo test 2>&1 >test.log
?

2018-06-01T12:58:13.2Z+00:00


1


Reply








Estatistics

Estatistics

Over a year ago




for completeness (as top answer) - "redirect (and append) stdout and stderr to file and terminal and get proper exit status"
command 2>&1 | tee -a file.txt

2022-08-14T11:02:05.033Z+00:00


1


Reply












451

## Some tricks about redirection

Some syntax particularity about this may have important behaviours. There is some little samples about redirections,STDERR,STDOUT, and argumentsordering.

### 1 - Overwriting or appending?

Symbol>meansredirection.

* >meanssend to as a whole completed file, overwriting target if exist (seenoclobberbash feature at#3later).
* >>meanssend in addition towould append to target if exist.

In any case, the file would be created if they not exist.

### 2 - Theshell command lineis order dependent!!

For testing this, we needa simple command which will send something on both outputs:

$ ls -ld /tmp /tnt
ls: cannot access /tnt: No such file or directory
drwxrwxrwt 118 root root 196608 Jan 7 11:49 /tmp

$ ls -ld /tmp /tnt >/dev/null
ls: cannot access /tnt: No such file or directory

$ ls -ld /tmp /tnt 2>/dev/null
drwxrwxrwt 118 root root 196608 Jan 7 11:49 /tmp

(Expecting you don't have a directory named/tnt, of course ;). Well, we have it!!

So, let's see:

$ ls -ld /tmp /tnt >/dev/null
ls: cannot access /tnt: No such file or directory

$ ls -ld /tmp /tnt >/dev/null 2>&1

$ ls -ld /tmp /tnt 2>&1 >/dev/null
ls: cannot access /tnt: No such file or directory

The last command line dumpsSTDERRto the console, and it seem not to be the expected behaviour... But...

If you want to make somepost filteringaboutstandardoutput,erroroutput or both:

$ ls -ld /tmp /tnt | sed 's/^.*$/<-- & --->/'
ls: cannot access /tnt: No such file or directory
<-- drwxrwxrwt 118 root root 196608 Jan 7 12:02 /tmp --->

$ ls -ld /tmp /tnt 2>&1 | sed 's/^.*$/<-- & --->/'
<-- ls: cannot access /tnt: No such file or directory --->
<-- drwxrwxrwt 118 root root 196608 Jan 7 12:02 /tmp --->

$ ls -ld /tmp /tnt >/dev/null | sed 's/^.*$/<-- & --->/'
ls: cannot access /tnt: No such file or directory

$ ls -ld /tmp /tnt >/dev/null 2>&1 | sed 's/^.*$/<-- & --->/'

$ ls -ld /tmp /tnt 2>&1 >/dev/null | sed 's/^.*$/<-- & --->/'
<-- ls: cannot access /tnt: No such file or directory --->

Notice that the last command line in this paragraph is exactly same as in previous paragraph, where I wroteseem not to be the expected behaviour(so, this could even be an expected behaviour).

Well, there is a little tricks about redirections, fordoing different operation on both outputs:

$ ( ls -ld /tmp /tnt | sed 's/^/O: /' >&9 ) 9>&2 2>&1 | sed 's/^/E: /'
O: drwxrwxrwt 118 root root 196608 Jan 7 12:13 /tmp
E: ls: cannot access /tnt: No such file or directory

Note:&9descriptor would occur spontaneously because of) 9>&2.

Addendum: nota!With the new version ofbash(>4.0) there is a new feature and more sexy syntax for doing this kind of things:

$ ls -ld /tmp /tnt 2> >(sed 's/^/E: /') > >(sed 's/^/O: /')
O: drwxrwxrwt 17 root root 28672 Nov 5 23:00 /tmp
E: ls: cannot access /tnt: No such file or directory

And finally for such a cascading output formatting:

$ ((ls -ld /tmp /tnt |sed 's/^/O: /' >&9 ) 2>&1 |sed 's/^/E: /') 9>&1| cat -n
 1 O: drwxrwxrwt 118 root root 196608 Jan 7 12:29 /tmp
 2 E: ls: cannot access /tnt: No such file or directory

Addendum: nota!Same new syntax, in both ways:

$ cat -n <(ls -ld /tmp /tnt 2> >(sed 's/^/E: /') > >(sed 's/^/O: /'))
 1 O: drwxrwxrwt 17 root root 28672 Nov 5 23:00 /tmp
 2 E: ls: cannot access /tnt: No such file or directory

WhereSTDOUTgo through a specific filter,STDERRto another and finally both outputs merged go through a third command filter.

### 2b - Using|&instead

Syntaxcommand |& ...could be used as analiasforcommand 2>&1 | .... Same rules about command line order applies. More details atWhat is the meaning of operator |& in bash?

### 3 - A word aboutnoclobberoption and>|syntax

That's aboutoverwriting:

Whileset -o noclobberinstruct bash tonotoverwrite any existing file, the>|syntax let you pass through this limitation:

$ testfile=$(mktemp /tmp/testNoClobberDate-XXXXXX)

$ date > $testfile ; cat $testfile
Mon Jan 7 13:18:15 CET 2013

$ date > $testfile ; cat $testfile
Mon Jan 7 13:18:19 CET 2013

$ date > $testfile ; cat $testfile
Mon Jan 7 13:18:21 CET 2013

The file is overwritten each time, well now:

$ set -o noclobber

$ date > $testfile ; cat $testfile
bash: /tmp/testNoClobberDate-WW1xi9: cannot overwrite existing file
Mon Jan 7 13:18:21 CET 2013

$ date > $testfile ; cat $testfile
bash: /tmp/testNoClobberDate-WW1xi9: cannot overwrite existing file
Mon Jan 7 13:18:21 CET 2013

Pass through with>|:

$ date >| $testfile ; cat $testfile
Mon Jan 7 13:18:58 CET 2013

$ date >| $testfile ; cat $testfile
Mon Jan 7 13:19:01 CET 2013

Unsetting this option and/or inquiring if already set.

$ set -o | grep noclobber
noclobber on

$ set +o noclobber

$ set -o | grep noclobber
noclobber off

$ date > $testfile ; cat $testfile
Mon Jan 7 13:24:27 CET 2013

$ rm $testfile

### 4 - Last trick and more...

For redirectingbothoutput from a given command, we see that a right syntax could be:

$ ls -ld /tmp /tnt >/dev/null 2>&1

for thisspecialcase, there is a shortcut syntax:&>... or>&

$ ls -ld /tmp /tnt &>/dev/null

$ ls -ld /tmp /tnt >&/dev/null

Nota: if2>&1exist,1>&2is a correct syntax too:

$ ls -ld /tmp /tnt 2>/dev/null 1>&2

### 4b- Now, I will let you think about:

$ ls -ld /tmp /tnt 2>&1 1>&2 | sed -e s/^/++/
++/bin/ls: cannot access /tnt: No such file or directory
++drwxrwxrwt 193 root root 196608 Feb 9 11:08 /tmp/

$ ls -ld /tmp /tnt 1>&2 2>&1 | sed -e s/^/++/
/bin/ls: cannot access /tnt: No such file or directory
drwxrwxrwt 193 root root 196608 Feb 9 11:08 /tmp/

### 4c- If you're interested inmoreinformation

You could read the fine manual by hitting:

man -Len -Pless\ +/^REDIRECTION bash

in abashconsole ;-)

edited
Jan 19, 2022 at 7:53

 answered
Apr 29, 2013 at 16:33

F. Hauri - Give Up GitHub

73.2k
19
19 gold badges
137
137 silver badges
154
154 bronze badges

## 2 Comments





F. Hauri - Give Up GitHub

F. Hauri - Give Up GitHub

Over a year ago




Further reading:
 If you liked this, you may apreciate:
How redirection abuse could give strange behaviours

2013-12-10T21:14:04.153Z+00:00


7


Reply








F. Hauri - Give Up GitHub

F. Hauri - Give Up GitHub

Over a year ago




@fabs If you liked this, maybe would you like
Open new window for input/output
 and/or
Redirections from script himself

2021-12-14T07:47:04.07Z+00:00


0


Reply










204

I found this brilliant post on redirection:All about redirections

Redirect both standard output and standard error to a file

$ command &>file

This one-liner uses the&>operator to redirect both output streams - stdout and stderr - from command to file. This is Bash's shortcut for quickly redirecting both streams to the same destination.

Here is how the file descriptor table looks like after Bash has redirected both streams:

As you can see, both stdout and stderr now point tofile. So anything written to stdout and stderr gets written tofile.

There are several ways to redirect both streams to the same destination. You can redirect each stream one after another:

$ command >file 2>&1

This is a much more common way to redirect both streams to a file. First stdout is redirected to file, and then stderr is duplicated to be the same as stdout. So both streams end up pointing tofile.

When Bash sees several redirections it processes them from left to right. Let's go through the steps and see how that happens. Before running any commands, Bash's file descriptor table looks like this:

Now Bash processes the first redirection >file. We've seen this before and it makes stdout point to file:

Next Bash sees the second redirection 2>&1. We haven't seen this redirection before. This one duplicates file descriptor 2 to be a copy of file descriptor 1 and we get:

Both streams have been redirected to file.

However be careful here! Writing

command >file 2>&1

is not the same as writing:

$ command 2>&1 >file

The order of redirects matters in Bash! This command redirects only the standard output to the file. The stderr will still print to the terminal. To understand why that happens, let's go through the steps again. So before running the command, the file descriptor table looks like this:

Now Bash processes redirections left to right. It first sees 2>&1 so it duplicates stderr to stdout. The file descriptor table becomes:

Now Bash sees the second redirect,>file, and it redirects stdout to file:

Do you see what happens here? Stdout now points to file, but the stderr still points to the terminal! Everything that gets written to stderr still gets printed out to the screen! So be very, very careful with the order of redirects!

Also note that in Bash, writing

$ command &>file

is exactly the same as:

$ command >&file

edited
Jul 5, 2018 at 3:43

Peter Mortensen

31.2k
22
22 gold badges
111
111 silver badges
134
134 bronze badges

 answered
Oct 29, 2016 at 13:04

Deen John

3,860
5
5 gold badges
34
34 silver badges
33
33 bronze badges

## 3 Comments





M.M

M.M

Over a year ago




The last two are different if "command" ends in a number, as then that is taken as optional file descriptor for
>&

2017-01-23T12:09:25.51Z+00:00


5


Reply








HCSF

HCSF

Over a year ago




Very nice drawing and explanation! Could you elaborate what "duplicate" really means? You mentioned, "This one [2>&1] duplicates file descriptor 2 to be a copy of file descriptor 1". It sounds like stderr gets duplicated to stdout. But if it is the case, should I also see err though
/dev/tty0
?

2019-07-22T02:35:09.057Z+00:00


0


Reply








MaXi32

MaXi32

Over a year ago




This is a very nice explanation with visual. If I became the one who ask this question, I will mark this as accepted answer.

2020-10-18T03:43:18.307Z+00:00


3


Reply












130

The numbers refer to the file descriptors (fd).

* Zero isstdin
* One isstdout
* Two isstderr

2>&1redirects fd 2 to 1.

This works for any number of file descriptors if the program uses them.

You can look at/usr/include/unistd.hif you forget them:

/* Standard file descriptors. */
#define STDIN_FILENO 0 /* Standard input. */
#define STDOUT_FILENO 1 /* Standard output. */
#define STDERR_FILENO 2 /* Standard error output. */

That said I have written C tools that use non-standard file descriptors for custom logging so you don't see it unless you redirect it to a file or something.

edited
Nov 6, 2012 at 1:25

Rob Kielty

8,192
8
8 gold badges
43
43 silver badges
52
52 bronze badges

 answered
May 3, 2009 at 22:58

Colin Burnett

11.6k
6
6 gold badges
34
34 silver badges
40
40 bronze badges

## 1 Comment





gardenapple

gardenapple

Over a year ago




Is it okay to just use your own "non-standard file descriptors"? How do you know there isn't an open file with the same FD?

2021-11-29T10:08:28.797Z+00:00


1


Reply










66

I found this very helpful if you are a beginner readthis

Update:In Linux or Unix System there are two places programs send output to:Standard output (stdout) and Standard Error (stderr).You can redirect these output to any file.Like if you do thisls -a > output.txtNothing will be printed in console all output(stdout)is redirected to output file.

And if you try print the content of any file that does not exits means output will be an error like if you print test.txt that not present in current directorycat test.txt > error.txtOutput will be

cat: test.txt :No such file or directory

But error.txt file will be empty because we redirecting the stdout to a file not stderr.so we need file descriptor( A file descriptor is nothing more than a positive integer that represents an open file. You can say descriptor is unique id of file) to tell shell which type of output we are sending to file .In Unix /Linux system1 is for stdout and 2 for stderr.so now if you do thisls -a 1> output.txtmeans you are sending Standard output (stdout) to output.txt.and if you do thiscat test.txt 2> error.txtmeans you are sending Standard Error (stderr) to error.txt .&1is used to reference the value of the file descriptor 1 (stdout).Now to the point2>&1means “Redirect the stderr to the same place we are redirecting the stdout”Now you can do this<br

cat maybefile.txt > output.txt 2>&1both Standard output (stdout) and Standard Error (stderr) will redirected to output.txt.

Thanks toOndrej K.for pointing out

edited
Jun 13, 2021 at 5:15

 answered
Apr 1, 2020 at 16:32

kundan bora

797
6
6 silver badges
10
10 bronze badges

## 2 Comments





Shiva

Shiva

Over a year ago




+1 for "&1 is used to reference the value of the file descriptor 1 (stdout).". I always wondered why it wasn't just
2>1

2022-02-14T05:03:50.347Z+00:00


1


Reply








FlexMcMurphy

FlexMcMurphy

Over a year ago




In that case why did he not do
&2>&1
 to mean “Redirect the stderr to the same place we are redirecting the stdout”. And likewise
cat test.txt &2> error.txt
 ?

2024-07-29T11:15:33.413Z+00:00


0


Reply










65

That construct sends the standard error stream (stderr) to thecurrentlocation of standard output (stdout) - this currency issue appears to have been neglected by the other answers.

You can redirect any output handle to another by using this method but it's most often used to channelstdoutandstderrstreams into a single stream for processing.

Some examples are:

# Look for ERROR string in both stdout and stderr.
foo 2>&1 | grep ERROR

# Run the less pager without stderr screwing up the output.
foo 2>&1 | less

# Send stdout/err to file (with append) and terminal.
foo 2>&1 |tee /dev/tty >>outfile

# Send stderr to normal location and stdout to file.
foo >outfile1 2>&1 >outfile2

Note that that last one willnotdirectstderrtooutfile2- it redirects it to whatstdoutwas when the argument was encountered (outfile1) andthenredirectsstdouttooutfile2.

This allows some pretty sophisticated trickery.

edited
Jun 26, 2009 at 8:39

 answered
May 3, 2009 at 23:54

paxdiablo

890k
243
243 gold badges
1.6k
1.6k silver badges
2k
2k bronze badges

## 4 Comments





Michael Cramer

Michael Cramer

Over a year ago




Although that last example would be much clearer as: foo >outfile2 2>outfile1

2009-05-04T00:15:20.33Z+00:00


5


Reply








paxdiablo

paxdiablo

Over a year ago




Clearer, yes, but that wouldn't show the "positional" nature of redirection. The example is contrived since it's not usually useful to do this in a single line - the method becomes really useful when different parties are responsible for the different parts of the redirection. For example, when a script does one bit of redirection and you run it with another bit.

2009-05-04T00:19:52.88Z+00:00


5


Reply








snapfractalpop

snapfractalpop

Over a year ago




I just realized that the last example also resolves a long standing confusion I had regarding why this:
some_program 2>&1 > /dev/null
 does not work like this:
some_program > /dev/null 2>&1
.

2012-12-20T13:58:24.013Z+00:00


6


Reply








Nils-o-mat

Nils-o-mat

Over a year ago




Your comment about the last example is worth its letters in gold :-) I never thought that these redirectional arguments are positional... I think this is pretty important to know.

2018-04-18T09:04:34.583Z+00:00


0


Reply












28

2 is the console standard error.

1 is the console standard output.

This is the standard Unix, and Windows also follows the POSIX.

E.g. when you run

perl test.pl 2>&1

the standard error is redirected to standard output, so you can see both outputs together:

perl test.pl > debug.log 2>&1

After execution, you can see all the output, including errors, in the debug.log.

perl test.pl 1>out.log 2>err.log

Then standard output goes to out.log, and standard error to err.log.

I suggest you to try to understand these.

edited
Jul 5, 2018 at 3:14

Peter Mortensen

31.2k
22
22 gold badges
111
111 silver badges
134
134 bronze badges

 answered
Jul 19, 2013 at 3:23

Marcus Thornton

6,293
8
8 gold badges
52
52 silver badges
54
54 bronze badges

## 1 Comment





F. Hauri - Give Up GitHub

F. Hauri - Give Up GitHub

Over a year ago




The second sample is wrong: as order precedence
STDERR
 is redirected to
STDOUT
, only default
STDOUT
 will be written to
debug.log
 (not
STDERR
) see
my answer
 (the paragraph #2)! To ensure
both
 to be redirected to same file, you have to invert redirections directives:
perl test.pl > debug.log 2>&1

2015-02-10T16:04:52.743Z+00:00


0


Reply










25

2>&1is a POSIX shell construct. Here is a breakdown, token by token:

2: "Standard error" output file descriptor.

>&:Duplicate an Output File Descriptoroperator (a variant ofOutput Redirectionoperator>). Given[x]>&[y], the file descriptor denoted byxis made to be a copy of the output file descriptory.

1"Standard output" output file descriptor.

The expression2>&1copies file descriptor1to location2, so any output written to2("standard error") in the execution environment goes to the same file originally described by1("standard output").

Further explanation:

File Descriptor: "A per-process unique, non-negative integer used to identify an open file for the purpose of file access."

Standard output/error: Refer to the following note in theRedirectionsection of the shell documentation:

Open files are represented by decimal numbers starting with zero. The largest possible value is implementation-defined; however, all implementations shall support at least 0 to 9, inclusive, for use by the application. These numbers are called "file descriptors". The values 0, 1, and 2 have special meaning and conventional uses and are implied by certain redirection operations; they are referred to as standard input, standard output, and standard error, respectively. Programs usually take their input from standard input, and write output on standard output. Error messages are usually written on standard error. The redirection operators can be preceded by one or more digits (with no intervening characters allowed) to designate the file descriptor number.

 answered
Dec 25, 2016 at 6:43

wjordan

20.6k
3
3 gold badges
92
92 silver badges
101
101 bronze badges

## Comments







20

To answer your question: It takes any error output (normally sent to stderr) and writes it to standard output (stdout).

This is helpful with, for example 'more' when you need paging for all output. Some programs like printing usage information into stderr.

To help you remember

* 1 = standard output (where programs print normal output)
* 2 = standard error (where programs print errors)

"2>&1" simply points everything sent to stderr, to stdout instead.

I also recommend readingthis post on error redirectingwhere this subject is covered in full detail.

 answered
May 3, 2009 at 23:24

Andrioid

3,420
4
4 gold badges
29
29 silver badges
32
32 bronze badges

## Comments







13

Provided that/foodoes not exist on your system and/tmpdoes…

$ ls -l /tmp /foo

will print the contents of/tmpand print an error message for/foo

$ ls -l /tmp /foo >/dev/null

will send the contents of/tmpto/dev/nulland print an error message for/foo

$ ls -l /tmp /foo 1>/dev/null

will do exactly the same (note the1)

$ ls -l /tmp /foo 2>/dev/null

will print the contents of/tmpand send the error message to/dev/null

$ ls -l /tmp /foo 1>/dev/null 2>/dev/null

will send both the listing as well as the error message to/dev/null

$ ls -l /tmp /foo >/dev/null 2>&1

is shorthand

edited
Mar 11, 2024 at 10:09

 answered
Sep 1, 2016 at 20:58

Matijs

3,208
2
2 gold badges
32
32 silver badges
43
43 bronze badges

## 1 Comment





Blacklight MG

Blacklight MG

Over a year ago




For anyone reading, I have to point out that
/tmp
 doesn't go to
/dev/null
 because it is the first argument and
/foo
 is the second. It does so because
ls /tmp
 is valid (prints to
stdout
), while
ls /foo
 is an error (prints to
stderr
).

2024-05-26T08:14:46.833Z+00:00


0


Reply










11

From a programmer's point of view, it means precisely this:

dup2(1, 2);

See theman page.

Understanding that2>&1is acopyalso explains why ...

command >file 2>&1

... is not the same as ...

command 2>&1 >file

The first will send both streams tofile, whereas the second will send errors tostdout, and ordinary output intofile.

 answered
Dec 3, 2015 at 10:20

ams

25.8k
4
4 gold badges
62
62 silver badges
79
79 bronze badges

## Comments







10

People, always rememberpaxdiablo's hint about thecurrentlocation of the redirection target... Itisimportant.

My personal mnemonic for the2>&1operator is this:

* Think of&as meaning'and'or'add'(the character is anampers-and, isn't it?)
* So it becomes:'redirect2(stderr) to where1(stdout) already/currently is andaddboth streams'.

The same mnemonic works for the other frequently used redirection too,1>&2:

* Think of&meaningandoradd... (you get the idea about the ampersand, yes?)
* So it becomes:'redirect1(stdout) to where2(stderr) already/currently is andaddboth streams'.

And always remember: you have to read chains of redirections 'from the end', from right to left (notfrom left to right).

 answered
Jul 1, 2012 at 10:47

Kurt Pfeifle

91.6k
24
24 gold badges
271
271 silver badges
358
358 bronze badges

## Comments







10

## Redirecting Input

Redirection of input causes the file whose name
 results from the expansion of word to be opened for reading on file
 descriptor n, or the standard input (file descriptor 0) if n is
 not specified.

The general format for redirecting input is:

[n]<word

## Redirecting Output

Redirection of output causes the file whose
 name results from the expansion of word to be opened for writing on
 file descriptor n, or the standard output (file descriptor 1) if n
 is not specified. If the file does not exist it is created; if it
 does exist it is truncated to zero size.

The general format for redirecting output is:

[n]>word

## Moving File Descriptors

The redirection operator,

[n]<&digit-

moves the file descriptor digit to file descriptor n, or the
 standard input (file descriptor 0) if n is not specified.
 digit is closed after being duplicated to n.

Similarly, the redirection operator

[n]>&digit-

moves the file descriptor digit to file descriptor n, or the
 standard output (file descriptor 1) if n is not specified.

## Ref:

man bash

Type/^REDIRECTto locate to theredirectionsection, and learn more...

An online version is here:3.6 Redirections

### PS:

Lots of the time,manwas the powerful tool to learn Linux.

edited
Jul 5, 2018 at 3:25

Peter Mortensen

31.2k
22
22 gold badges
111
111 silver badges
134
134 bronze badges

 answered
Jun 6, 2015 at 11:07

yurenchen

2,784
30
30 silver badges
24
24 bronze badges

## Comments







10

unix_commands 2>&1

This is used to print errors to the terminal.

* Whenerrorsare produced, they are written to the "standard error" buffer at memory address&2, and2references and streams from that buffer.
* Whenoutputsare produced, they are written to the "standard output" buffer at memory address&1, and1references and streams from that buffer.

So going back to the command. Anytime the programunix_commandsproduces an error, it writes that into theerrorsbuffer. So we create a pointer to that buffer2, and redirect>the errors into theoutputsbuffer&1. At this point we're done, because anything in the outputs buffer is read and printed by the terminal.

edited
Jul 11, 2022 at 7:16

 answered
Jan 25, 2020 at 20:50

tim-montague

17.7k
6
6 gold badges
68
68 silver badges
62
62 bronze badges

## Comments







5

This is just like passing the error to the stdout or the terminal.

That is,cmdis not a command:

$cmd 2>filename
cat filename

command not found

The error is sent to the file like this:

2>&1

Standard error is sent to the terminal.

edited
Jul 5, 2018 at 3:17

Peter Mortensen

31.2k
22
22 gold badges
111
111 silver badges
134
134 bronze badges

 answered
Oct 11, 2013 at 6:16

Kalanidhi

5,107
30
30 silver badges
42
42 bronze badges

## Comments







2

0 for input, 1 for stdout and 2 for stderr.

One Tip:somecmd >1.txt 2>&1is correct, whilesomecmd 2>&1 >1.txtis totallywrongwith no effect!

 answered
Jul 25, 2016 at 9:46

ch271828n

17.9k
5
5 gold badges
71
71 silver badges
108
108 bronze badges

## 1 Comment





jhnc

jhnc

Over a year ago




actually, it does have an effect. compare
rm /x | wc -l
 to
rm /x 2>&1 >/dev/null | wc -l

2024-08-02T10:16:31.627Z+00:00


0


Reply










1

You need to understand this in terms of pipe.

$ (whoami;ZZZ) 2>&1 | cat
logan
ZZZ: command not found

As you can see both stdout and stderr of LHS of pipe is fed into the RHS (of pipe).

This is the same as

$ (whoami;ZZZ) |& cat
logan
ZZZ: command not found

 answered
May 23, 2022 at 2:43

Logan Lee

1,045
1
1 gold badge
12
12 silver badges
27
27 bronze badges

## Comments







0

Note that1>&2cannot be used interchangeably with2>&1.

Imagine your command depends on piping, for example:docker logs 1b3e97c49e39 2>&1 | grep "some log"grepping will happen across bothstderrandstdoutsincestderris basically merged intostdout.

However, if you try:docker logs 1b3e97c49e39 1>&2 | grep "some log",grepping will not really search anywhere at all because Unix pipe is connecting processes via connectingstdout | stdin, andstdoutin the second case was redirected tostderrin which Unix pipe has no interest.

 answered
Jul 22, 2020 at 13:39

yuranos

9,915
9
9 gold badges
65
65 silver badges
71
71 bronze badges

## 1 Comment





Akira Taguchi

Akira Taguchi

Over a year ago




Your grep example only demonstrates how grep does not get stderr as input in Unix pipe. This does not however show that
1>&2
 and
2>&1
 cannot be used in an interchangable way. Do you have any other examples that would clarify your initial thesis?

2022-11-24T07:54:33.257Z+00:00


0


Reply










Start asking to get answers

Find the answer to your question by asking.

Ask question

Explore related questions

* bash
* shell
* unix

See similar questions with these tags.
