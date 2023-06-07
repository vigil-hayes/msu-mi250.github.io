---
parent: Week 13
topic: Refactor Old Studio
nav_exclude: false
visible: true
---

Your goal today is *refactoring*.  The task for today is to go back to one of the previous studios that you did, read
through the code, and then re-write the code.  Your goal in re-writing the code is to make it easier to read, easier to
understand, more reusable, and to work better.  Much like you did on Monday, you don't need to change what the program
does.  You just should revise and rewrite the code to make it do what it already does better.

For today's studio, it is up to you whether you work by yourself or whether you work in a group.  You do not have to be
working with the same group that you did for the original studio; it is OK to refactor code that others wrote.

---

That’s it. That’s the whole of the instructions – choose a past studio, optionally form a group to work with, and revise
the code to work better. Have fun with it.

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### Pick any studio

Pick any studio to work on and refactor. It is OK if you didn't actually finish and get it working when you were
originally working on it. If so, then this is your opportunity to finish it.  It is also OK if you got it working and
all you want to do is refactor the code so it works better.  It is up to you which studio to refactor.   My
recommendation is to pick the studio you liked the best and spend your time working on that; you always do your best
work (and learn the most) working on something you care about.

### Use Functions

Code is much easier to read and work with when it is organized into functions.  In addition to grouping lines of code
together, functions also give that group of commands a name.   Using that name then makes things easier to read and make
more sense.  Think about what you kinds of things you can group together into functions.  Ideally, you will most *most*
of your code into functions, and have a relatively short 'main' section that just calls the appropriate functions in the
right order.

### Look for opportunities to refactor

Go back to Monday's lab for ideas how to refactor. When we looked at our existing code, we looked for a couple of things
to identify opportunities for refactoring:

* *Add comments*. You are going back and reading code that you wrote weeks or possibly months ago.  Some of it will feel
  pretty obvious what it is doing.  But some of it won't.  Anything that you feel you had to stare at for more than a
  few minutes to figure out what it is doing is probably something that isn't obvious. Once you figure out what it does, 
  add a comment to that describes what it does, so it is easier to remember in the future.
* *Look for comments*.  If you have written a comment to yourself about what this set of lines do, then that is a good
  opportunity to pull those lines into a separate function that has a name.  Giving code a name makes it easier to read.
* *Look for repeated code*, or places where the exact same code is repeated multiple times.   Pull them together into a
  function.
* *Look for similar code* --- places where code that isn't exactly the same, but is similar, is repeated multiple times.
  That is a good candidate for putting into a function with a parameter.  Small differences can be controlled with the
  parameter (like the `color` parameter to the rectangle function).
* *Look for opportunities to generalize*.  Just like we went from `red_strip()` to `stripe(color)` to
  `colored_rectangle(...)`, look for places where you take an existing function, and make it more useful by making it
  slightly more general than it currently is.  (Emphasis on *slightly*; if you make things too general, then they become
  less useful).
* *Remove unneeded code*. As you look at the code, you might find things that aren't needed anymore.  Remove them from the
  file so they don't get in the way of the more important things.

### Think about the User Experience

Refactoring is a gread opportunity to make minor changes to improve the user experience of running your program.   Put
yourself in the shoes of someone else running your code.  What would make it easier to use?  Some things I've seen
groups do in class so far include:

* Adding spaces in appropriate places (e.g. at the end of an `input()` prompt) so things don't run together.
* Adding additional text (`print()` statements) to help explain what the program does and what the user is supposed to
  do.
* Moving the turtle at the beginning of the program up and to the left, so whatever it draws is centered on the screen.
* Changing the font or the color or the line thickness so whatever is being drawn by the turtle is easier to see
* Speeding up the turtle (with the `speed()` function) so you don't have to wait as long for things to draw. (OR have it speed up and slow down at different times as it draws for dramatic effect.)


### Enough with it!

If you think you've done enough refactoring with a studio, call for help from
either Jack or me and talk us through the changes you made.  If we don't
have additional ideas, then you can move on and work on refactoring another
studio.
