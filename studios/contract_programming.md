---
parent: Week 10
topic: Contract Programming
published: false
nav_exclude: true
visible: false
---

Most programming work is broken up into different parts, which are usually done by different people.   The first part is
the *specification*: deciding what the program needs to do.  Specifications are hard because they need to provide enough
detail about what the program will need to do that someone else can program.  The second part is the *implementation*,
which is writing the main code that (hopefully) accomplishes what the specification says it should   The third part is
the *testing*, which checks the main code to see what it does and does not do, to make sure that it accomplishes what it
is supposed to do.

We are going to do that today -- specification, implementation, and testing -- around a small [flashcards
app](../2/studio.html).  

Today's studio is going to be organized a little bit differently than normal.  First, form groups of 2-3 people (no
groups of 4).    Second, once you have a group, find another group to be your partner.   Each group should have one
partner group -- so you'll be working directly with the 1-2 other members of your group, and indirectly with the 2-3
people in the partner group.

1. For the first 20-30 minutes of class, your group should work on a *specification*.   Decide what topic you want your
   flashcards to be about.  Write the content for a few flashcards (5? 10?) compete with prompts and answers.  Also,
decide what you want the program to look like.   What functions should exist? You will not be writing the code for this;
someone else will. You are just specifying what code you want written, and what it should do once it is finished. Think
about how you want someone else to write the code.  

2. For the next 45-60 minutes, we will swap with partners. Your partner group will take your specification and try to
   *implement* it.  They will write code that tries to do what you specified.  And, conversely, you will try to write
the code that they specified.   They will ask you to do things differently than you asked.  Your job will be to do what
they asked, not what you envisioned.

3. Finally, for the last 20-30 minutes, we will swap back.  You will be given a working version of what you specified.
   Your job now will be to *test* it: did they do what was asked?  What works?  What doesn't?   Think about both manual
and automated testing as a way to figure out whether the code that you were handed actually works the way you think it
should.

---

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

The specification is your contract; it tells the other team what you want done.  The more specific you can be, the more
likely you are to actually get what you want.  Don't just say "do some math problems" -- how will they ever know what
that means? Give them exact problems for the flashcards.  Tell them exactly how many flashcards.  Think about how you
would implement it, and give them some structure that they can use to make it work correctly.  Do you want it to count
the number correct?  Do you want it to be snarky?  Be specific.

### Specify both program and content

The natural impulse is just to write the content of the flashcards -- what questions should it ask, and what should the
answers be?   But that's not enough.  You are asking them to write a computer program.   Be sure to also specify what
that program should do.  Should it be graphical (turtle) or text-based (terminal)?  Should it be case senstive?  Should
it give the user more than one chance to get it right?  Should it count the number correct?  What else should it do?
Anything it should NOT do?

### Think About Testing While Writing the Specification

Near the end of class, you are going to get back some code.  It almost certainly will not do exactly what you expect it
to -- but your partner team will think it does.   Think about how you will test it.  As you are writing the
specification, also jot down some notes about how to test it.  What things will you look for? What does it mean to
"work" correctly?   What are some possible inputs, and what would you expect to happen with those inputs?

### Use Slack to communicate

This isn't a one-time handoff.  You are allowed to communicate with the other team.  You will be implementing their
specification, and they will be implementing yours. Talk to them!  Ask questions! Answer their questions.  Get to know
them.  

Zoom isn't very good for this.  You can all agree to meet in a breakout room for in-person chats.  But a lot of
questions are too small for this.  Use Slack for this.  Type questions into the slack, messaging the other team. Watch
the Slack, and answer questions from the other team. Use this for quick, lightweight conversations.  Or to coordinate
when you want to meet in a breakout room to talk in person.

### Ask for clarifications

Despite trying really hard, program specifications are almost always more vague and less detailed than you would like.
As you start writing code, you start to realize all of the things that the specification did NOT specify.  It is OK to
ask for clarifications.  "When you said X, what did you mean?" "If this happens, would it be better if the program does
X or Y?"  Clarifying questions are normal and good.

### Is this fun?

As you work, think about what parts of this you are enjoying, and what parts you don't. Some people really like being
told what to do, and having a specification to work towards is nice and easy.  Other people hate it because it feels
uncreative and like they can't express themselves.  Some people really like testing because it is fun to break things
and think about all the weird ways that programs get used; other people hate testing and find it very tedious.   Some
people like writing specifications because they get to see lots of possibilities, and then get to have other people make
them happen.  Other people hate writing specifications because they feel like writing down all the details that a
specification needs is more work than just writing the code.

Think about what parts of this you like, and what parts you don't like.  This will help you as you move forward in your
career in thinking about what parts of the work you might want to do, or might want to avoid.


