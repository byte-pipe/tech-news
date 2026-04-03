---
title: Drugwars for the TI-82/83/83+ Calculators · GitHub
url: https://gist.github.com/mattmanning/1002653/b7a1e88479a10eaae3bd5298b8b2c86e16fb4404
site_name: hnrss
content_file: hnrss-drugwars-for-the-ti-828383-calculators-github
fetched_at: '2026-03-20T19:19:44.743882'
original_url: https://gist.github.com/mattmanning/1002653/b7a1e88479a10eaae3bd5298b8b2c86e16fb4404
date: '2026-03-20'
description: 'Drugwars for the TI-82/83/83+ Calculators. GitHub Gist: instantly share code, notes, and snippets.'
tags:
- hackernews
- hnrss
---

Instantly share code, notes, and snippets.

# mattmanning/drugwars.txt

 Created
 
June 1, 2011 16:09

 

Show Gist options

 

* Download ZIP

 

 

* Star60(60)You must be signed in to star a gist
* Fork12(12)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/mattmanning/1002653.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save mattmanning/1002653 to your computer and use it in GitHub Desktop.

 

Embed

# Select an option

 

* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found

 

 
 
Learn more about clone URLs

 

 

 Clone this repository at &lt;script src=&quot;https://gist.github.com/mattmanning/1002653.js&quot;&gt;&lt;/script&gt;

 

 

Save mattmanning/1002653 to your computer and use it in GitHub Desktop.

Download ZIP

 Drugwars for the TI-82/83/83+ Calculators
 

 

Raw

 drugwars.txt
 

Lbl G

ClrHome

Disp " J.M.'S DRUGWAR"," SIMULATION",""," VERSION 2.00",""," JUST SAY NO."

2000→Z

5000→Y

0→V

100→K

1→B

2→N

0→I

0→J

100→T

0→M

0→N

0→O

0→P

0→Q

0→R

Pause 

ClrHome

Disp "","ORIGINAL GAME","FOR IBM BY:"," JOHN E. DELL",""

Disp "INSTRUCTIONS?"

Input "(1=YES,2=NO)",X

If X=1

Then

ClrHome

Disp "THIS IS A GAME","OF BUYING AND","SELLING. YOUR","GOAL IS TO PAY-","OFF YOUR DEBT TO","THE LOAN SHARK,","AND THEN MAKE AS"

Pause 

ClrHome

Disp "MUCH MONEY AS","POSSIBLE IN A 1","MONTH PERIOD.","WATCH-OUT FOR","THE POLICE IF","YOU DEAL TOO","HEAVILY!"

Pause 

ClrHome

Disp "PRICES FOR DRUGS","ARE:","COCAINE:","15000-28000","HEROINE:","5000-12000","ACID: 1000-4200"

Pause 

Disp "WEED: 300-720","SPEED: 70-220","LUDES: 10-50"

Pause 

ClrHome

Disp "GENERALY, TYPE","THE FIRST LETTER","OF WHAT YOU WANT","TO DO, I.E.:","W=WEED, L=LUDES","ETC..."

Pause 

Disp "BUT, 1=YES AND","2=NO"

Pause 

ClrHome

Disp "THE LAST NUMBER","IN THE PRICES","LIST IS YOUR","WALLET. THE LAST","NUMBER IN YOUR","TRENCHCOAT IS","FREE SPACE."

Pause 

End

Lbl θ

round(rand*12000+16000,0)→C

round(rand*7000+5000,0)→H

round(rand*34+10,0)*100→A

round(rand*42+33,0)*10→W

round(rand*15+7,0)*10→S

round(rand*4+1,0)*10→L

round(rand*20,0)→D

If D=1

Then

ClrHome

Disp "RIVAL DEALERS","ARE SELLING","CHEAP LUDES!!!"

Pause 

2→L

End

If D=2

Then

ClrHome

Disp "WEED PRICES HAVE","BOTTOMED-OUT!!!"

Pause 

122→W

End

If D=3

Then

ClrHome

Disp "PIGS ARE SELLING","CHEAP HEROINE","FROM LAST WEEK'S","RAID!!!!"

Pause 

rand→H

(850+(H*1150))→H

(int(H)→H

End

If D=4 or D=5

Then

ClrHome

Disp "ADDICTS ARE","BUYING HEROINE","AT OUTRAGEOUS","PRICES!!!"

Pause 

rand→H

(18000+(H*25000))→H

(int(H)→H

End

If D=6 or D=7

Then

ClrHome

Disp "PIGS MADE A BIG","COKE BUST!","PRICES ARE","OUTRAGEOUS!!!!"

Pause 

rand→C

(80000+(C*60000))→C

(int(C)→C

End

If D=8

Then

ClrHome

Disp "YOU WERE MUGGED","IN THE SUBWAY!"

Pause 

(Z/3)→Z

(int(Z)→Z

(Z*2)→Z

End

If D=15 and Zù300

Then

ClrHome

Disp "WILL YOU BUY A","NEW TRENCHCOAT","WITH MORE","POCKETS FOR 200","BUCKS?"

Input X

If X=1

Then

(T+10)→T

(T-M-N-O-P-Q-R)→K

(Z-200)→Z

End

End

If D=14

Then

ClrHome

Disp "THERE'S SOME","WEED HERE THAT","SMELLS LIKE GOOD","STUFF!!"

Pause 

Disp "WILL YOU SMOKE"

Input "IT?",X

If X=1

Then

ClrHome

Disp "YOU HALLUCINATE","ON THE WILDEST","TRIP OF YOUR","LIFE,"

Pause 

Disp "STUMBLE ON TO","THE SUBWAY","TRACKS AND GET","CREAMED BY A","TRAIN."

Pause 

ClrHome

Disp "JUST SAY NO TO","DRUGS."

Pause 

Goto C

End

End

If Zù500 and Kù5

Then

If D=12 or D=13

Then

ClrHome

Disp "WILL YOU BUY A"

round(rand*2,0)→X

If X=0

Disp "BARRETTA"

If X=1

Disp "SATURDAY NIGHT","SPECIAL"

If X=2

Disp ".44 MAGNUM"

Disp "FOR 400 DOLLARS?"

Input X

If X=1

Then

(I+1)→I

(Z-400)→Z

(T-5)→T

(T-M-N-O-P-Q-R)→K

End

End

End

If D=16 and Kù8

Then

int((rand*7+1)→F

ClrHome

Disp "YOU FOUND:",F,"UNITS OF:"

int((rand*5)→X

If X=0

Then

Disp " LUDES"

(R+F)→R

End

If X=1

Then

Disp " SPEED"

(Q+F)→Q

End

If X=2

Then

Disp " WEED"

(P+F)→P

End

If X=3

Then

Disp " ACID"

(O+F)→O

End

If X=4

Then

Disp " HEROINE"

(N+F)→N

End

If X=5

Then

Disp " COCAINE"

(M+F)→M

End

Disp "ON A DEAD DUDE","IN THE SUBWAY!!!"

(T-M-N-O-P-Q-R)→K

Pause 

Goto A

End

If D=17

Then

ClrHome

Disp "THE MARKET HAS","BEEN FLOODED","WITH CHEAP HOME-","MADE ACID!!!!"

int((250+(rand*550))→A

Pause 

Goto A

End

If D=9 or D=10 or D=11

Then

If (M+N+O+P+Q+R)ù50

Then

ClrHome

If D=9

1→D

If D=10

3→D

If D=11

4→D

Disp "OFFICER HARDASS","AND",D,"OF HIS DEPPUTIES","ARE AFTER YOU!"

Pause 

ClrHome

Lbl M

Menu("BEING CHASED!!","VIEW GUNS",H,"VIEW DAMMAGE",I,"NUMBER OF PIGS",J,"RUN",K,"FIGHT",L)

Lbl H

ClrHome

Disp "NUMBER OF GUNS","YOU HAVE:"

Disp I

Pause 

Goto M

Lbl I

ClrHome

Disp "YOUR DAMMAGE="

Disp J

Disp "(50 DAMMAGE AND","YOU DIE!)"

Pause 

Goto M

Lbl J

ClrHome

Disp "THERE ARE:"

(D+1)→D

Disp D

(D-1)→D

Disp "PIGS STILL","CHASING YOU!"

Pause 

Goto M

Lbl K

ClrHome

Disp "","","",""," RUNNING"

round(rand*1,0)→X

If X=0

Then

ClrHome

Disp "YOU LOST THEM IN","AN ALLEY!!"

Pause 

If B=31

Then

Goto A

Else

Goto θ

End

End

If X=1

Then

ClrHome

Disp "YOU CAN'T SHAKE","THEM!"

Pause 

Goto O

End

Lbl L

If I=0

Then

ClrHome

Disp "YOU DON'T HAVE","ANY GUNS!"

Pause 

Disp "YOU HAVE TO RUN!"

Pause 

Goto M

Else

round(rand*1,0)→X

If X=0

Then

ClrHome

Disp "YOU MISSED!!!"

Pause 

Else

ClrHome

Disp "YOU KILLED ONE!!"

Pause 

(D-1)→D

If D=(ú1)

Goto N

End

Lbl O

round(rand*1,0)→X

ClrHome

Disp "THEY'RE FIRING","AT YOU!!"

If X=0

Then

Disp "THEY MISSED!!"

Pause 

Goto M

Else

Disp "YOU'VE BEEN HIT!"

(J+3)→J

Pause 

If Jù50

Then

Disp "YOU'VE BEEN ","KILLED!!"

Pause 

Goto C

End

Goto M

End

Lbl N

ClrHome

Disp "YOU KILLED ALL","OF THEM!"

int((rand*1250+750)→X

(Z+X)→Z

Pause 

Disp "YOU FOUND"

Disp X

Disp "DOLLARS ON","OFFICER HARDASS'","CARCASS!!"

Pause 

If Zù1200

Then

ClrHome

Disp "WILL YOU PAY","1000 DOLLARS FOR","A DOCTOR TO SEW","YOU UP?"

Input X

If X=1

Then

(Z-1000)→Z

0→J

End

End

End

End

End

Lbl A

ClrHome

Menu("DRUGWAR!","SEE PRICES",1,"TRENCHCOAT",2,"BUY",3,"SELL",4,"JET",5,"SEE LOAN SHARK",6,"VISIT BANK",7)

Lbl 1

ClrHome

Disp C,H,A,W,S,L,Z

Output(1,1,"COCAINE")

Output(2,1,"HEROINE")

Output(3,1,"ACID")

Output(4,1,"WEED")

Output(5,1,"SPEED")

Output(6,1,"LUDES")

Output(7,1,"WALLET")

Pause 

Goto A

Lbl 2

ClrHome

Disp M,N,O,P,Q,R,K

Output(1,1,"COCAINE")

Output(2,1,"HEROINE")

Output(3,1,"ACID")

Output(4,1,"WEED")

Output(5,1,"SPEED")

Output(6,1,"LUDES")

Output(7,1,"FREE SPACE")

Pause 

Goto A

Lbl 3

ClrHome

Disp "DAY NUMBER:",B

Input "WHAT TO BUY?",F

If FøC and FøH and FøA and FøW and FøS and FøL

Goto 3

int((Z/F)→E

Disp "HOW MUCH?","YOU CAN AFFORD:",E,"YOU CAN HOLD:",K

Input G

If G>K or G<0 or G>E

Goto 3

(Z-(FG))→Z

If F=C

(M+G)→M

If F=H

(N+G)→N

If F=A

(O+G)→O

If F=W

(P+G)→P

If F=S

(Q+G)→Q

If F=L

(R+G)→R

(T-M-N-O-P-Q-R)→K

Goto A

Lbl 4

ClrHome

Disp "DAY NUMBER:",B

Input "WHAT TO SELL?",F

If FøC and FøH and FøA and FøW and FøS and FøL

Goto 4

If F=C

M→E

If F=H

N→E

If F=A

O→E

If F=W

P→E

If F=S

Q→E

If F=L

R→E

Disp "HOW MUCH?","YOU HAVE:",E

Input G

If G>E or G<0

Goto 4

If F=C

(M-G)→M

If F=H

(N-G)→N

If F=A

(O-G)→O

If F=W

(P-G)→P

If F=S

(Q-G)→Q

If F=L

(R-G)→R

(Z+FG)→Z

(T-M-N-O-P-Q-R)→K

Goto A

Lbl 5

ClrHome

Menu("WHERE TO, DUDE?","BRONX",R,"GHETTO",B,"CENTRAL PARK",B,"MANHATTEN",B,"CONEY ISLAND",B,"BROOKLYN",B,"OOPS... STAY!",A)

Lbl R

If N=2

Then

ClrHome

Disp "YOU'RE ALREADY","IN THE BRONX!"

Pause 

Goto 5

End

2→N

Goto S

Lbl B

1→N

Lbl S

ClrHome

Disp "","","",""," SUBWAY"

(B+1)→B

int((Y*1.1)→Y

int((V*1.06)→V

If B=31

Goto C

Goto θ

Lbl 6

If N=1

Then

ClrHome

Disp "THE LOAN SHARK","ONLY DEALS IN","THE BRONX."

Pause 

Goto A

End

ClrHome

Menu("LOAN SHARK...","REPAY",P,"BORROW",Q)

Lbl P

ClrHome

Disp "YOU'RE DEBT IS:",Y,"YOUR WALLET=",Z,"REPAY HOW MUCH?"

Input F

If F>Z or F<0 or F>Y

Goto 6

(Y-F)→Y

(Z-F)→Z

Goto A

Lbl Q

ClrHome

Disp "YOUR DEBT=",Y,"YOUR WALLET=",Z,"BORROW HOW MUCH"

Input "MORE?",F

If F>5000

Then

ClrHome

Disp "YOU THINK HE'S","CRAZY, MAN?!"

Pause 

Goto Q

End

If F<0

Goto 6

(Y+F)→Y

(Z+F)→Z

Goto A

Lbl 7

If N=1

Then

ClrHome

Disp "THE BANK IS IN","THE BRONX."

Pause 

Goto A

End

Menu(" BANK ","VIEW ACCOUNT",D,"DEPOSIT",E,"WITHDRAW",F,"GOODBYE",A)

Lbl D

ClrHome

Disp "YOUR ACCOUNT=",V

Pause 

Goto 7

Lbl E

ClrHome

Disp "HOW MUCH TO","DEPOSIT?","YOU HAVE:",Z

Input G

If G>Z or G<0

Goto E

(V+G)→V

(Z-G)→Z

Goto 7

Lbl F

ClrHome

Disp "HOW MUCH TO","WITHDRAW?","ACCOUNT=",V

Input X

If X>V or X<0

Goto F

(V-X)→V

(Z+X)→Z

Goto 7

Lbl C

ClrHome

Disp " GAME OVER!"

(V+Z-Y)→V

If V<0

Then

0→V

Else

(√(V/31.5)→V

If V>100

100→V

End

round(V,0)→V

Disp "YOUR SCORE (ON A","SCALE OF 1 TO","100)=",V,""

Pause 

Input "PLAY AGAIN?",V

If V=1

Goto G

ClrHome

Disp " THANKS FOR"," PLAYING!"

Pause 

ClrHome

Disp "","","REMEMBER:","","WATCH YOUR BACK."

Pause 

Disp "","HAVE A NICE DAY!"

Load earlier comments...

 

### ileathancommentedSep 26, 2021•edited

https://drive.google.com/file/d/1O7Bc826GCLZusbUgD1T-lwTG10PNbZ7X/view?usp=sharing

Please let me know if it doesn't work, should work fine.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### spitemimcommentedSep 27, 2021

This doesn't work on my TI-84+. I've tried using the .8xp and copying it into SourceCoder. Is it not compatible with the 84+, or am I doing something wrong?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### ileathancommentedSep 27, 2021•edited

I got it to run on the TI-83+ didn't try on 84 but figured it would also work, did you get any errors?

Edit: I got it to work on a TI-84+ emulator just fine as well. hmm. You should be able to just transfer the file over and run it with the prgm command, or if its an emulator just File -> open it. (or hit prgm) I wont not appear in Mirage unless you add::as the first line of code.

Worst case you could just write the code from here directly in the calculator's basic interpreter via prgm -> new.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### DaSovietPotatocommentedMar 14, 2022

I found a problem with the TI-84 conversion, however low and behold I have only needed to do some bug fixing. The new file should work just fine.https://github.com/DaSovietPotato/Drugwars-TI-84

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### gammalogiccommentedJul 21, 2023

Is this version based on the IBM Basic source code from the original 1984 game or has the game functionality been determined by playing/testing? I'm trying to port the original DOS game to a different platform (Sega Master System) and want it to be authentic as possible but this will require disassembling the DOS executable which (I think) would have been generated using the IBM Basic compiler and so probably has a lot of IBM Basic environment code in there that I don't understand.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### ileathancommentedJul 21, 2023

Do keep us informed@gammalogic. I think it is based on the original but thats just my guess as I could not find the original source aside from reverse engineering it.

Maybe it is out there somewhere in the wild though.

I found many sites with the code to older versions starting with the dope wars from 2000 or so. but they are different and improved

Good luck

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Author

### mattmanningcommentedJul 21, 2023via email

Hey y'all. This gist shows how to program the game on a TI-82 graphing
calculator.

I believe the TI game is based on the IBM game, but you wouldn't be able to
compile this for other platforms. You could use it to give you an idea of
the game's rules and logic though.

I found this somewhere on the Internet many years ago and cleaned up some
of the character formatting to make it more readable, but that's about the
extent of my knowledge.

…

On Fri, Jul 21, 2023, 1:07 PM Spinelli Valentinuzzi < ***@***.***> wrote:
 ***@***.**** commented on this gist.
 ------------------------------

 Do keep us informed 
@gammalogic
 <
https://github.com/gammalogic
>. I think
 it is based on the original but thats just my guess as I could not find the
 original source aside from reverse engineering it.

 Maybe it is out there somewhere in the wild though.

 I found many sites with the code to older versions starting with the dope
 wars from 2000 or so. but they are different and improved

 Good luck

 —
 Reply to this email directly, view it on GitHub
 <
https://gist.github.com/mattmanning/1002653#gistcomment-4636818
> or
 unsubscribe
 <
https://github.com/notifications/unsubscribe-auth/AAAK4R7MV24YQZAZ7QKGLETXRKZL5BFKMF2HI4TJMJ2XIZLTSKBKK5TBNR2WLJDHNFZXJJDOMFWWLK3UNBZGKYLEL52HS4DFQKSXMYLMOVS2I5DSOVS2I3TBNVS3W5DIOJSWCZC7OBQXE5DJMNUXAYLOORPWCY3UNF3GS5DZVRZXKYTKMVRXIX3UPFYGLK2HNFZXIQ3PNVWWK3TUUZ2G64DJMNZZDAVEOR4XAZNEM5UXG5FFOZQWY5LFU4YTAMBSGY2THJ3UOJUWOZ3FOKTGG4TFMF2GK
>
 .
 You are receiving this email because you authored the thread.

 Triage notifications on the go with GitHub Mobile for iOS
 <
https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675
>
 or Android
 <
https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub
>
 .

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### ileathancommentedJul 21, 2023

Thanks for that Matt. I am pretty sure you are right about it being based on the original code as well just based off gameplay.

I still have this on my calculator and my phone and while I don't really play it I enjoy quite thoroughly having it, so again, ty.

@gammalogicI think your best bet is to just go line by line (having fun with the gotos/labels) and port the code to whatever language you want. You are going to want to know BASIC but its actually very easy and basic in many ways just look for a TI-83 manual and check what each line of code does and learn as you go and you will be done by the end of the day.

For example just using a search engine for

"ti-83 manual goto meaning"

I get

"The Goto command is used together with the Lbl command to jump (or branch) to another place in a program. When the calculator executes a Goto command, ."

Simple enough! Good luck!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### gammalogiccommentedJul 22, 2023

Thank you@mattmanningand@ileathanfor your comments. The TI-82 code is a great starting point even if it isn't 100% accurate to the original code (which it might be). I have done some C and SDL programming so I would like to re-implement the game in that first, then look at the Z80 version next. I had also considered running the original Drug Wars in a DOS emulator with debugging enabled, so that I could check to see what values are in the registers/memory when the game is running. This game seems perfect for a retro console (i.e. Master System, Game Gear or NES) hence my idea to try and port it to the Z80. I do have some ideas for extending the game but the original version is priority with a "2.0" version as a bonus i.e. let players choose which one they want. This isn't necessarily vaporware as I got as far as putting together a basic C/SDL tech demo about two years ago running at NES screen resolution with memory mapped video emulation to display the stash and trench coat totals in nice bordered windows and let you change amount of drugs and current location. There was also an option to change the location from New York to Los Angeles and have different types of drugs for sale e.g. crystal, all fairly obvious but with different colour schemes and graphics to keep things interesting.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### gammalogiccommentedJul 22, 2023

Just as a point of interest, John Dell said that he was inspired to create Drug Wars after playing the TRS-80 game "Taipan". The author of that game also co-authored a book of the same name explaining how the game was designed, and the book includes code listings for the Apple II version. The Applesoft BASIC code can be found attaipangame.com/BASIC.txt.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### trav29commentedDec 28, 2023

This was my era during high school and loved playing this game. I have found a TI-83 and a unit-to-unit cable. Is there an easy way to download this game as i would love it for the mancave. Help would be appreciated

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### ileathancommentedDec 28, 2023•edited

This was my era during high school and loved playing this game. I have found a TI-83 and a unit-to-unit cable. Is there an easy way to download this game as i would love it for the mancave. Help would be appreciated

You can add the game using only your calculator by entering the BASIC interpreter (PRGM -> New) and then enter the source code you see here [If you add::as a first line and move the rest of the code down one line it will appear inMirageOS's games list].

Or much quicker you can use a Computer and a program like TI-Coder to turn this into .8xp and transfer it to the calculator (I had to replace ≥ with >= and (the arrow) with -> and ≥ with >= and θ with 0 before making the .8xp file). There may be other programs like TI CONNECT that you can use to move the files over from the pc to your calculator as well.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### gammalogiccommentedDec 28, 2023

@trav29Just to add to what@ileathanhas said, your options are (I think) to either buy a TI-83 to USB adaptor and download the game from your PC, or to type in the game code directly if you have the source code (which you do). I would look on eBay first for the cable/adaptor - they should come with Windows software on a CD. Some of the adaptors were probably sold around the time that Windows XP was still current, so might not work for current Windows versions (unless you can run Windows XP in virtualisation software, which is probably too much effort). I'm sure there must also be some kind of free (i.e. Linux or Un*x based) software, working on the basis that free software fanatics like the TI-83 and would almost certainly have written a driver for it.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### ileathancommentedDec 28, 2023•edited

This was my era during high school and loved playing this game. I have found a TI-83 and a unit-to-unit cable. Is there an easy way to download this game as i would love it for the mancave. Help would be appreciated

Here is a .8xp file that I made using TI-Coder with the above codehttps://t7.vc/dl/DRUGWARS.8xp

You could use "TI CONNECT" (need TI-83 to USB adaptor) to push it onto your calculator.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### darth-crunchuscommentedJan 6, 2024•edited

This was my era during high school and loved playing this game. I have found a TI-83 and a unit-to-unit cable. Is there an easy way to download this game as i would love it for the mancave. Help would be appreciated

Here is a .8xp file that I made using TI-Coder with the above codehttps://t7.vc/dl/DRUGWARS.8xp

You could use "TI CONNECT" (need TI-83 to USB adaptor) to push it onto your calculator.

The only thing you have to watch out for is, after you get it on your calculator, you need to go into the BASIC editor and modify the conditional blocks in Lbl 3 and Lbl 4; TI-Coder apparently doesn't like inequality symbols, as they appear as like weird floating commas? instead of =/=, and some of the "F"s in those Lbls are displayed as "f"s, which is also going to cause errors. Everything else seems fine, though I haven't enountered many of the game's random encounters yet. Also, in the 23 years I've been messing around with TI-BASIC, I never knew you could pass alphanumeric characters to normal variables using Input commands. I was under the impression they HAD to contain numbers and numbers only. Or is it that when you answer a numeric input with a letter, what you're actually doing is transferring the value contained in that variable to the receiving variable?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### ileathancommentedJan 6, 2024•edited

Maybe I misunderstood but the code never passes alphanumeric characters as input but youcan, it treats them as a variable length string I would use them to store usernames or even entire phonebook program with 1 variable lol.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### darth-crunchuscommentedJan 29, 2024

Yeah, it appears that it just dumps the values stored in C, H, A, W, S, and L into the prompt behind the scenes. Still a neat feature. I've been messing with this for the past couple of weeks, and I've gotten it working completely on my TI-84 Plus CE, even adding a couple random encounters back in, namely the police dogs encounter and the brownies encounter, and restored a few things like random pricing to guns and trench coat upgrades, and even the random size to how much extra storage each trench coat gives you, and added the fourth gun back in. It's up to 6310B, but hey, still not as big as Pimp Quest lol That's still got a good half KB over this.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### DenverGamercommentedMar 22, 2024

Hello, I have no idea what I am doing. Can someone help me play this on TI-82? Trying to create the file

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### DrChorizasocommentedMay 1, 2024

Can some one please help i got the game to show up it runs and all but every time to go to buy or sell i type W and as soon as i hit enter it kicks me back to mirage

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### SmarterJokercommentedJul 22, 2024

Yeah, it appears that it just dumps the values stored in C, H, A, W, S, and L into the prompt behind the scenes. Still a neat feature. I've been messing with this for the past couple of weeks, and I've gotten it working completely on my TI-84 Plus CE, even adding a couple random encounters back in, namely the police dogs encounter and the brownies encounter, and restored a few things like random pricing to guns and trench coat upgrades, and even the random size to how much extra storage each trench coat gives you, and added the fourth gun back in. It's up to 6310B, but hey, still not as big as Pimp Quest lol That's still got a good half KB over this.

I know this is a while back, but do you still have the 8x file of this? Please let me know, thanks.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### darth-crunchuscommentedNov 22, 2024

Yeah, it appears that it just dumps the values stored in C, H, A, W, S, and L into the prompt behind the scenes. Still a neat feature. I've been messing with this for the past couple of weeks, and I've gotten it working completely on my TI-84 Plus CE, even adding a couple random encounters back in, namely the police dogs encounter and the brownies encounter, and restored a few things like random pricing to guns and trench coat upgrades, and even the random size to how much extra storage each trench coat gives you, and added the fourth gun back in. It's up to 6310B, but hey, still not as big as Pimp Quest lol That's still got a good half KB over this.

I know this is a while back, but do you still have the 8x file of this? Please let me know, thanks.

Sorry it's taken so long to reply, but yes! I do I actual;ly just updated it today. I kinda went a little overboard...it's now up to 11429B. I've been busy, trying to get it as close to the DOS original as I can, including random seeding of the rand( function. Here's a plain-text version:https://pastebin.com/4dUuw0BR. It may or may not preserve the signing for the negative ints

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### JonesWebConsultingcommentedApr 3, 2025

If it hasn't already been done. I want to rewrite this as a C# console app.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### EnderBeastytcommentedNov 25, 2025

anyone have a version for the ti 84 plus ce or ce py?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### darth-crunchuscommentedNov 26, 2025

anyone have a version for the ti 84 plus ce or ce py?

It runs on the 84 Plus CE/ CE Python as is.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### DrChorizasocommentedNov 26, 2025via email

Do you have the file Sent from my iPhoneOn Nov 26, 2025, at 8:17 AM, darth-crunchus ***@***.***> wrote:﻿Re: ***@***.*** commented on this gist.anyone have a version for the ti 84 plus ce or ce py?It runs on the 84 Plus CE/ CE Python as is.—Reply to this email directly, view it on GitHub or unsubscribe.You are receiving this email because you commented on the thread.Triage notifications on the go with GitHub Mobile for iOS or Android.                                                           

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### darth-crunchuscommentedNov 26, 2025

Do you have the file Sent from my iPhoneOn Nov 26, 2025, at 8:17 AM, darth-crunchus@.> wrote:﻿Re:@.commented on this gist.anyone have a version for the ti 84 plus ce or ce py?It runs on the 84 Plus CE/ CE Python as is.—Reply to this email directly, view it on GitHub or unsubscribe.You are receiving this email because you commented on the thread.Triage notifications on the go with GitHub Mobile for iOS or Android.

Look for the pastebin link on here; just copy the source into TI Connect, and you can save it as a .8xp file.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### SmarterJokercommentedNov 29, 2025via email

Keep me posted, I am looking forward to put this on my calculator, heck
even on a few devices if you plan to make this Android or PC.

…

On Thu, Apr 3, 2025, 3:38 PM Kenneth R. Jones ***@***.***> wrote:
 ***@***.**** commented on this gist.
 ------------------------------

 If it hasn't already been done. I want to rewrite this as a C# console app.

 —
 Reply to this email directly, view it on GitHub
 <
https://gist.github.com/mattmanning/1002653#gistcomment-5526488
> or
 unsubscribe
 <
https://github.com/notifications/unsubscribe-auth/AJP6WSNWIRDC6ERSQVIRYVD2XWL3JBFKMF2HI4TJMJ2XIZLTSKBKK5TBNR2WLJDUOJ2WLJDOMFWWLO3UNBZGKYLEL5YGC4TUNFRWS4DBNZ2F6YLDORUXM2LUPGBKK5TBNR2WLJDHNFZXJJDOMFWWLK3UNBZGKYLEL52HS4DFVRZXKYTKMVRXIX3UPFYGLK2HNFZXIQ3PNVWWK3TUUZ2G64DJMNZZDAVEOR4XAZNEM5UXG5FFOZQWY5LFU4YTAMBSGY2THJ3UOJUWOZ3FOKTGG4TFMF2GK
>
 .
 You are receiving this email because you commented on the thread.

 Triage notifications on the go with GitHub Mobile for iOS
 <
https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675
>
 or Android
 <
https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub
>
 .

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### vladimir1909commentedDec 18, 2025

anyone have a version for pico 8 ?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### vladimir1909commentedDec 19, 2025

anyone have a version for pico 8 ?

nevermind, I wrote it by myself

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### tibboncommentedMar 20, 2026

In TI-83 BASIC, variables are single letters, and the original code reuses N for two completely different purposes:

1. Heroine inventory — 0→N (initialization), (N+G)→N (buying), (N-G)→N (selling)
2. Location tracker — 2→N (Bronx), 1→N (everywhere else)

What happens

- Traveling changes your heroine count. Jetting to the Bronx sets N=2, meaning you now "have" 2 heroine. Jetting anywhere else sets
N=1.
- Buying/selling heroine changes your location. If you buy 2+ heroine (making N≥2), the game thinks you're in the Bronx, giving you
access to the loan shark and bank from anywhere. If you sell all your heroine (N=0), neither the Bronx check (N=2) nor the not-Bronx
check (N=1) triggers, so you can still access the bank and loan shark.

How to exploit it

1. Unlimited bank/loan shark access: Buy exactly 0 heroine or sell it all so N=0. The guard clauses check If N=1 (not Bronx) to block
you — but 0≠1, so you bypass the restriction and can use the bank and loan shark from any location.
2. Free heroine: Travel to the Bronx at any time and you instantly "have" 2 heroine in your trenchcoat, conjured from nothing. Travel
away, sell the 2 heroine for profit, repeat.
3. Inventory/capacity desync: Since traveling overwrites N, your trenchcoat free space calculation (T-M-N-O-P-Q-R)→K uses the location value instead of actual heroine count, potentially letting you carry more than your coat allows.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment