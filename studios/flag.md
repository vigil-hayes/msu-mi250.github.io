---
parent: Week 5
topic: Country Flag Studio
nav_exclude: true
visible: false
---

For today, we are going to do a studio instead of the regular Monday lab.

Today we are going to practice [Vexillography](https://en.wikipedia.org/wiki/Vexillography) -- the art of designing flags!

Imagine that you and your teammates are going to go and start your own country.  This isn't so crazy at it sounds; not
too long ago, a family colonized an old weapons platform outside England and created the [Principality of
Sealand](https://en.wikipedia.org/wiki/Principality_of_Sealand); othes have claimed islands in the Pacific Ocean or
tried to create floating countries.

What all countries need is a flag. Your job today is to design a flag for your country, and then write a python
program that draws that flag on the screen using the `turtle` package.  

---

That’s it. That’s the whole of the instructions – form a group, design a flag, and program the computer to draw that
flag on the screen. What the flag looks like or symbolizes is entirely up to you. How you program it is entirely
up to you. How complicated or simple the flag is is up to you. Have fun with it. Be creative.

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### Flag Symbolism

Flags are not easy to design.  Flags have a lot of symbolism in them.  Figure out what you want your flag to symbolize,
and try to make sure that the flag conveys the symbols you want it to convey.

### Flag Design

The flag should follow good flag design.  Here is a pamphlet from the North American Vexillography Association that
describes their 5 principles for good flag design, with examples: <https://nava.org/digital-library/design/GFBF_English.pdf>

### Start Simple

Start simple.  First, design a really simple flag (a 2 or three color striped flag like the [Flag of
Italy](https://en.wikipedia.org/wiki/Flag_of_Italy)?) and write a program to draw that.  Then think about how you can
make the flag more complicated or more interesting.  Change the colors.  Change the orientation.  Change the size of the
flag.

### Think like a Pen

Turtle graphics are designed to be like drawing with a pen.  Draw a line here, lift the pen, move it over here, put it
back down, and draw another line. If you get stuck thinking about your program, figure out how you would draw the same
thing with a pen.  Break down the pen drawing into steps; those steps are the steps for the turtle.

### Start on Paper

Start by drawing your flag on a piece of paper. Get something working.  Then try to figure out what pen movements you
had to make on paper to draw that flag,  Then see if you can make the turtle move like the pen did.


### Turtle Graphics

* [Official Documentation](https://docs.python.org/3/library/turtle.html)

If there is something you would do with a pen, you can probably do it with a turtle.  There are a lot more turtle
commands than what we used in the readings or in the lab.  Look at the official turtle documentation to find more
commands to help you think about how to draw things.  

Push yourself to try new things and new features with the Turtle graphics.  It doesn't hurt to try.  If you aren't sure,
try and see what happens.  For example, in one single program you can have two different turtles drawing different
things at the same time!  You can also have two difference screens being drawn on.    

### Use What You Know

You know a lot about programming already -- `if` statements and `for` loops and getting input from users.   Use all of
that knowledge to help you in you drawing.

### Stay Organized, and use comments

One of the hardest parts of programmming computers to draw on the screen is the sheer number of commands and
instructions it takes.  You will find that your programs are getting long quickly because it takes a lot of instructions
to draw anything.

Think about how to stay organized.  You can always add blank lines; use that to group sets of commmands.  So if you've
got one set of commands that draws a blue square, and another that draws a white star, leave a blank line in between
them.  Also, use comments (lines that start with `#` that don't get read by python) to tell yourself what those lines
do, logically.   Its hard to understand what `fd(10); right(120); fd(10); right(120); fd(10)` does.  It is much easier
if you label this with `# Draw a triangle`:

```
# Draw a Triangle
fd(10)
right(120)
fd(10)
right(120)
fd(10)
```


### Keep Pushing Yourself

Your flag is a computer program.  That means that it can do things that other flags cannot.  Think about how you might
make your flag more interesting because it is a program. For example, could you animate something on the flag, or have a
special way of drawing the flag? Keep pushing yourself to make the flag more interesting.   Maybe you can ask the user
for some input, and then customize the flag around that input?  What can you do to make this flag program more interesting?



