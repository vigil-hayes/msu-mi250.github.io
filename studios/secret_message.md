---
title: Studio
parent: Week 8
grand_parent: Schedule
layout: studio
nav_order: 3
topic: Secret Message
nav_exclude: true
visible: false
published: false
---

<!-- TODO: add info about .toupper() and .tolower().  add info about """ -->

For today's studio, I am going to give you a secret message.  The secret message has been scrambled; your goal is to
figure out what the message says.  OR, more accurately, your goal is to write a program to help you figure out what the
message says.

Here is the message:
```
hnronxttfao fi x lrnt rl knbxvfdb bphnbiifra. 
hnronxttfao fi x vrrz, tske zfqb xa xnvfiv unsie rn x vd kxtbnx. 
fv kraivnxfai gexv yrs kxa cr knbxvfdbzy, 
usv xzir knbxvbi txay abg rhhrnvsafvfbi lrn favbnxkvfdb bphnbiifra.
```

In this message, each letter has been replaced with a different letter. So, for example, I might have replaced every `a`
with a `q`, and every `e` with a `z`.  (That's not the actual replacements.)  You need to figure out the *key*: what
letters are replacing what other letters?

You could do this by hand.  You could manually replace one letter with another, and see if it works.  And keep track of
whether it works. OR, you could automate this: you could try to program the computer to guess every combination of
letter replacements to see which one works.  Which will take the computer a long time -- and it'll be tough for the
computer to know whether it got the right answer.

By far, the best way to do this is half-way between these two options: write a program to work with a user (you) to make
*guesses*. 

You should write a guessing program.   The guessing program should ask the user for a letter in the message,
and then a letter to replace it with, and then print out the message with the letters replaced. This way, the user
(who will also be you) can see the message so far, along with your guesses. This way, you can make guesses, and the
computer can do the tedious work of replacing letters and keeping track of old guesses.

I like to have the message printed in lower case letters, and the any guessed letters replaced with upper case.   So,
for example, your output might look something like this:

```
Current Message: abcd cd f ghddfjh
What letter do you want to replace? a
What letter do you want to replace it with? T

Current Message: Tbcd cd f ghddfjh
What letter do you want to replace? b
What letter do you want to replace it with? H

Current Message: THcd cd f ghddfjh
What letter do you want to replace? c
What letter do you want to replace it with? I

Current Message: THId Id f ghddfjh
What letter do you want to replace? d
What letter do you want to replace it with? S

Current Message: THIS IS f ghSSfjh
What letter do you want to replace? f
What letter do you want to replace it with? 
```
    
Your goal today is to write a program so that you can work with the computer to figure out the secret message above.
Work in teams of 2-4 people to figure out the secret message.

---

That’s it. That’s the whole of the instructions – form a group, write the guessing program, and then use the
program to guess the message. Have fun with it. 

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### Start simple, and build

The first thing to do is to get the program written.  Start simple.  Write a program that prints out the message.  Run it to make
sure it works.  Then ask the user for a letter, and a new letter to replace it with.  Store them in variables, and print
them back out.  Run it to make sure it works.   Then add in the replacements, and make sure that works.  Then put it in
a loop so the user can make more than one guess.  

Slowly add features to your program until it has all the things you need it do.  Remember, the goal is to make an
interactive program that will help you figure out the secret message.  The program doesn't figure it out itself;
instead, it should support and help *you* to figure it out.

### Replace

Python has a nice `.replace()` function that enabled you to replace one letter (or substring) with another. It then
*returns* the new string.  So
```
thing = "food for the guest"
print(thing.replace("g", "Q"))
```
prints out
```
food for the Quest
```
The `.replace()` function replaces *all* instances.

### Use Case to your Advantage

The entire message right now is in lowercase letters.  Use that to your advantage.  When you replace a letter, replace
it with a capital letter. That way, you can tell which letters are original, and which have been  guessed.  That's what
I did in the example above; as I guessed letters, I replaced the orignal, lowercase letters with the newly guessed
capital letter.

One way to do this is to manually type in lower case letters and upper case letters when you are a user running the
program.  That will work!   But it is hard to remember, and really really confusing if you don't get it right.

You can make the program a bit easier to use by having the program automatically convert input from the user into
lowercase or uppercase as appropriate.  In python, if you have a string variable, you can convert it to uppercase with
the `.upper()` function, and to lowercase with the `.lower()` function.  (If the letter(s) are already uppercase and you
ask for uppercase, then it doesn't do anything.)


### Count Letters

How do you know what letters to guess?  Well, in the English language, some letters (like `e`) appear much more often
than other letters (like `q`).  

To help you guess, you could write a separate program that counts letters.  Ask the user for a letter, and then count
how many times it appears in the message.  Remember -- you are writing the program.  You can write a second program
easily -- just open up a new file and start writing!  You've done this before.

Once you have a program that counts how many times a letter appears, you can use it to help you.  What letter is most
common?  Print out the frequency of each letter in the message.  Then you can compare that to the [frequency of letters
in the English language](https://en.wikipedia.org/wiki/Caesar_cipher#/media/File:English-slf.png) to try to guess what
letters replaced what other letters.   For example, in English, the letter 'e' is the most common letter.  In the
message, what is most common?  Guess that that is an 'e'...  

*Hint*: You can use a `for` loop to loop through the letters in a string.
```
for letter in message:
	print(letter)
```

*Hint 2*: You can also check if the letter is the one entered by the user:
```
if letter == letter_from_user:
	count = count + 1
```

### Guess

Puzzles like these are called cryptograms.   There is [advice on the Internet](https://grammar.yourdictionary.com/games-puzzles-and-worksheets/how-to-solve-cryptograms.html) to help you solve them.

### Start Over

As a user of the program, sometimes your guesses will be wrong, and you will decide you are going down the wrong path.
When that happens, you'll want to start over.  The easiest way to start over is to stop the program, and then run it
again.   Add some way to exit the program.  For example, if instead of typing in a letter, you type "quit", then it can
exit the program.  OR, if you just hit enter instead of typing in a letter, maybe it will exit the program.

*Hint*:
The command `sys.exit()` allows you to quit the program.   To use that command, you have to put the instruction `import
sys` at the top of your python file.

<!--
### Print out the key

Once the program is finished, have the program print out the key.  Each time there is a substitution, store that in a
dictionary.  So if the user guesses that the letter `f` is really `A`, then store that in a dictionary:
```
solution['f'] = 'A'
```

Then, at the end of the program, print out the key so we know what letter is substituted for what, like this:

```
{'a': 'T', 'b': 'H', 'c': 'I', 'd': 'S', 'f': 'A', 'g': 'M', 'h': 'E', 'j': 'G'}
```

-->
## Challenge: More Messages

Here are a couple of more messages.  Use your program to help you figure out each of these messages.  Note that each
message uses a different key.

### Message #1:
```
ymrov srk, pj ia jmt-vm-edihxk mqpjpmj, mdr imvt pjkcesdvtphxk vmdrwk mf islpw. 
wsqshxk mf hmte pjfxpwtpjl pjbdra, sjo rkikoapjl pt. 
― sxhdv odihxkomrk,
```

### Message #2:
```
pdyn hjqm je ojqjhmi, ed idf'h gsehm jh ojxjfb edqmdfm moem'e ojcm. 
idf'h vm hnsuumi vp idbqs – gljal je ojxjfb gjhl hlm nmeyohe dc dhlmn umduom'e hljfzjfb. 
- ehmxm wdve
```

### Message #3:
```
syk qnyg is qxjk iakd zjj, syk qnyg is bnyp iakd, 
syk qnyg is wqnyg iakd zjj, zyp ny iak pzqrykff wnyp iakd
```

## Extra Challenge
Write a program that will *encode* secret messages.  It should ask the user for
a (possibly multiple line long) message.  Then it should randomly create a key,
encode the message, and print out both the encoded message and the key.

---

The instructor's solution to the studio for today is available here:
<https://gitlab.msu.edu/mi-250/cipher>
