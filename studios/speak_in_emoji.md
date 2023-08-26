---
parent: Week 7
topic: Speak in Emoji
nav_exclude: true
visible: false
---

Emoji are graphical representations of ideas and concepts -- basically, they are pictograms.  It is possible to convey
complex concepts and ideas using nothing but emoji. Smiley face emoji are particularly interesting because they often
convey emotions better than words do.  Emoji are especially powerful when you put one after the other to form emoji
"sentences".

Your goal for today is to write a set of functions that draw emoji using turtle graphics.  Each function should draw one
emoji.  Then use those functions to draw out an emoji "sentence" on the screen that conveys some complex feeling and
idea.

Work in groups of 2-4 people.

---

That’s it. That’s the whole of the instructions – form a group, write functions that create emoji, and then form those
emoji into sentences. What the emoji look like is entirely up to you. How you program it is entirely up to you. What
sentence you convey is up to you. Have fun with it. Be creative.

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### One function per emoji

Functions work best when they comprise a logical, coherent thing.  You want each function to make sense on its own, and
to do one "logical" thing. When functions try to do too much in one function, it gets confusing.   So, you can create a
function `smiley()` that draws a smiley face emoji.  It should do everything that is needed for the smiley face.  It is
better that it do everything for the smiley face.

Also, you don't want it to do things other than what the name implies.  So, a `smiley()` function should only draw a
smiley face.  It shouldn't also move the turtle around to other places, or change the turtle colors, or anything like
that.  If the function has side effects, then it gets confusing when you should use the function and when you
shouldn't.  Try to avoid your functions having side effects.

### Create your Own Emoji

Everyone knows the standard smiley face emoji.  People have come up with hundreds of new emoji. I encourage you to
create your own emoji that capture ideas or feelings that you have! You can use an existing emoji if you want, but it is
much more fun to create your own emoji!

### Keep your Emoji simple

Emoji are supposed to be simple pictograms.  Work hard to keep them simple.  Don't spend hours tweaking your emoji to
get it just right.  Start simple and get the basic emoji working.  You can always make it more complex later.

### Divide and Conquer

Split up the emoji between team members.  One of the nice things about functions is that it is really easy to divide up
the work.  One person can work on one function, and another person can work on the other.  This makes it easy to divide
up the work in a reasonable, logical way.  Also, if you are each working on different functions, git can usually merge
the changes easily.  Just make sure that you are all working in a clone of the same git repository.

### Support functions

In addition to having a separate function for each emoji, you might want to create a function or two to help with other
things that you need to do.  For example, could you create a `next()` function that moves the turtle to the right and
gets it ready to draw the next emoji?

### Look for common features

As you work on your emoji, you might notice that you have common features.  For example, if you are drawing both a
smiley face and a frowning face, both of them will have the same circular face.  That is an opportunity to create a
support function.   You could in this case create a function that draws a blank face (a circle of the appropriate
color).  Then your smiley function could call the blank face, and then draw the eyes and mouth.  Your frowning face
could also call the blank face function first, and then draw a different eyes and mouth.  

Creating support functions for common features like this is a great way to avoid lots of copy-and-pasting of code.  It
also makes it easier if you want to change something later on.  If you want to change the skin color, for example, you
only need to change it in the one place (blank face), rather than find all the places in your code that have a skin
color.


## Challenge

If you get the basic emoji sentence working and you have time left in the studio today, try this challenge:

The emoji sentence that your program draws is "hard-coded" -- it always draws the same sentence (the same emoji in the
same order) every time.  Instead of hard coding a sentence, modify your program to allow the user specify which emoji
should be drawn in which order.

For example, your program could work like this:
```
This program has the following emoji:
1. Smiley face
2. Frowney face
3. Winking face
4. Sticking out tongue
(enter 0 to stop)
Which emoji should be first? 1
Which emoji should be next? 1
Which emoji should be next? 2
Which emoji should be next? 4
Which emoji should be next? 3
Which emoji should be next? 0
```
And then it prints out the emoji sentence specified by the user.



