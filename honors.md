---
title: Honors Option
layout: home
topic: "Honors Option: Contract Programming"
nav_exclude: True
---

# Honors Option: Contract Programming

Most programming work is broken up into different parts, which are usually done by different people.   The first part is
the *specification*: deciding what the program needs to do.  Specifications are hard because they need to provide enough
detail about what the program will need to do that someone else can program.  The second part is the *implementation*,
which is writing the main code that (hopefully) accomplishes what the specification says it should   The third part is
the *testing*, which checks the main code to see what it does and does not do, to make sure that it accomplishes what it
is supposed to do.

We are going to do that -- specification, implementation, and testing -- around a small app.

1. First, you are going to need to write a specification.  Look through the studios for this class, and choose one of
   them that you find interesting.  (You do not need to choose the same studio as your partner.)  You will write a
specificaiton for a program that fulfills that studio.  The specification will need to provide a lot more detail than
the studio does, and get you to make decisions about exactly what you want build. The studios are intended to provide
space for creativity -- but when you are writing a specification, you don't want to let the programmer be too creative
or you will get back something very different than what you intended.  So you will have to be creative yourselve, when
creating the specification, and be very specific about what you want to the programmer to provide.

   For example, if you chose [Studio 3: Flashcards](week/3/studio.html), you would need to decide what topic you want your
flashcards to be about, how many flashcards you want, and write the content for the flashcards compete with prompts and
answers.  Also, decide what you want the program to look like.   What functions should exist?  What interface shoudl it
have?  Should it ask repeatedly until answered correctly, or move on and count wrong answers?  You will not be writing
the code for this; someone else will. You are just specifying what code you want written, and what it should do once it
is finished. Think about how you want someone else to write the code.  As you write the specification, remember that the
programmer will have about 2 hours to implement this.  How much could you get done in 2 hours?  What is reasonable to
ask for in 2 hours?

2. Next, we will swap with partners. Your partner will take your specification and try to
   *implement* it.  They will write code that tries to do what you specified.  And, conversely, you will try to write
the code that they specified.   They will ask you to do things differently than you asked.  Your job will be to do what
they asked, not what you envision.

3. Finally, we will swap back.  You will be given a working version of what you specified.
   Your job now will be to *test* it: did they do what was asked?  What works?  What doesn't? Re-read your specification
and compare the program you were given against it.  Think about whether the code that you were handed actually works the
way you think it should.  If it doesn't, is what the code does reasonable, or would you describe it as a bug or a
failure?

4. After you've gone through all three steps -- specification, implementation, and testing -- please write up a short
   reflection.  What was the process like?  Waas it hard to write a specification that you weren't going to program
yourself?  Did the other person interpret things similarly to you or differently than what you imagined?  Did you get
back something close to what you expected? Did everything work well, or were there bugs in the code?  Was it hard to
write code where someone else decided what the program should do?  Or was it easier because you knew exactly what the
proram was supposed to do?  (Also, think about all the questions and ideas in the "Is this fun?" heading above.)

The reflection doesn't need to be long; a paragraph or two about what its like to ask someone else to write code, and
another paragraph or two about what its like to be the programming doing work for someone else should be enough.  

---

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### Be Detailed and Specific

The specification is your contract; it tells the other team what you want done.  The more specific you can be, the more
likely you are to actually get what you want.  If you are doing flashcards, Don't just say "do some math problems" --
how will they ever know what that means? If you just say "do some math problems", then they might give you back
flashcards for grade school math (2+2=4), or they might give you back calculus problems.  Which one die you want?
Instead, give them exact problems for the flashcards.  Tell them exactly how many flashcards.  Think about how you would
implement it, and give them some structure that they can use to make it work correctly.  Do you want it to count the
number correct?  Do you want it to be serious and boring, or snarky and funny?  Be specific.

### Specify both program and content

The natural impulse is just to write the content (e.g. for the flashcards -- what questions should it ask, and what
should the answers be?)   But that's not enough.  You are asking them to write a computer program.   Be sure to also
specify what that program should do.  Should it be graphical (turtle) or text-based (terminal)?  Should it be case
senstive?  Should it give the user more than one chance to get it right?  Should it count the number correct?  What else
should it do?  Anything it should NOT do?

### Think About Testing While Writing the Specification

Near the end of class, you are going to get back some code.  It almost certainly will not do exactly what you expect it
to -- but your partner will think it does.   Think about how you will test it.  As you are writing the
specification, also jot down some notes about how to test it.  What things will you look for? What does it mean to
"work" correctly?   What are some possible inputs, and what would you expect to happen with those inputs?

### Choose something interesting

I gave an example above using the flashcards studio.  But that is probably the least interesting and least creative studio of
the year.   Try to choose something either that you think would actually be useful to you, or would be interesting for
you to work on and think about.  Then make it more interesting *to you* -- be creative, and come up with an interesting
program that you would want done.   Remember, you want creativity to be part of the specification, not part of the
implementation.

### Ask for clarifications

Despite trying really hard, program specifications are almost always more vague and less detailed than you would like.
As you start writing code, you start to realize all of the things that the specification did NOT specify.  It is OK to
ask for clarifications.  "When you said X, what did you mean?" "If this happens, would it be better if the program does
X or Y?"  Clarifying questions are normal and good.

### Use email to communicate

This isn't a one-time handoff.  You are allowed to communicate with the other team.  You will be implementing their
specification, and they will be implementing yours. Talk to them!  Ask questions! Answer their questions.  Get to know
them.  

You'll need to think about how to do this communication. You'll probably have multiple questions.  Do you send them a
separate email every time something comes up?  Can you figure out any of the answers yourself?  Do you need to wait for
a response, or can you keep working while you wait?

When you need a clarification, communicate via email, and CC both Jack and Rick when you email. 

### Is this fun?

As you work, think about what parts of this you are enjoying, and what parts you don't. Some people really like being
told what to do, and having a specification to work towards is nice and easy.  Other people hate it because it feels
uncreative and like they can't express themselves.  Some people really like testing because it is fun to break things
and think about all the weird ways that programs get used; other people hate testing and find it very tedious.   Some
people like writing specifications because they get to see lots of possibilities, and then get to have other people make
them happen.  Other people hate writing specifications because they feel like writing down all the details that a
specification needs is more work than just writing the code.

Think about what parts of this you like, and what parts you don't like.  This will help you as you move forward in your
career in thinking about what parts of the work you might want to do, or might want to avoid.  (This is a good thing to
mention in your reflection.)

### Limit your commitment

This honors option shouldn't take a ton of time.  For coming up with a specifcation, set a timer and limit yourself to
about 20-30 minutes.   Try to come up with a good specification in that time, but its OK if it isn't perfect.

For the actual programming aspect, expect about 2 hours of work -- about the same amount of time and complexity as a
normal studio in class.   Try to design your specification to be able to be done in that amount of time.  And when you
are programming, limit your time to about 2 hours.  IF you really want to, you can go longer, but think of it like a
contract job -- the client agreed to pay you for 2 hours of work, so if you do more than that, you are doing it for
free!

## Suggested Timeline

These dates are only suggestions.  Please feel free to recommend changes if you would like different deadlnes.

|-------|--------------------|----------|----------------|
| Step  | Time Commitment    | Due Date | How to turn in |
|:------|:-------------------|:---------|:---------------|
| 1. Specification | 20-30 minutes | Friday, April 7 | Email to partner; CC Rick and Jack |
| 2. Programming   | ~2 hours      | Friday, April 21  | Create new Gitlab repo with your program and place a copy of the specs you followed in it. Add partner, as well as Rick and Jack, to repo as maintainers. Email partner, CC Jack and Rick when done. |
| 3. Testing       | 20-30 minutes | Friday, April 28  | (Nothing to turn in, but would be helpful for you to write down a list of what works as you expected and what doesn’t to refer to as you write your reflection) |
| 4. Reflection    | However long it takes you to write 2-4 paragraphs | Wednesday, May. 3, 7:45pm (end of finals timeslot for this class) | See bottom of guidelines for what to write about. To turn it in, email to Jack and Rick as PDF or Word doc. Also include a link to the Gitlab repo you created (with the program you wrote based on your partner's specifications) in the email and/or in the reflection paper. |
|-------|--------------------|----------|----------------|
