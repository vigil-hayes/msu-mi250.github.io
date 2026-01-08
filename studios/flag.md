---
parent: Week 5
topic: Country Flag
nav_exclude: false
visible: true
---

_Project Management Plan (PMP) due BEFORE in-class studio:_ [PMP Resources](https://gitlab.msu.edu/mi-250/mi250-pmp-resources)

Today we are going to practice [Vexillography](https://en.wikipedia.org/wiki/Vexillography) -- the art of designing flags!

Imagine that you and your teammates are going to go and start your own country. This isn't so crazy at it sounds; not too long ago, a family colonized an old weapons platform outside England and created the [Principality of Sealand](https://en.wikipedia.org/wiki/Principality_of_Sealand). Others have claimed islands in the Pacific Ocean or tried to create floating countries.

What all countries need is a flag. Your job today is to design a flag for your group's new country, and then write a Python program that draws that flag on the screen using the `turtle` package. Remember to add `from turtle import *` at the top of your program and `done()` at the end! 

## Advice

What follows is just advice for doing it. You don’t have to follow my advice, but some of it might help.

### Define Your Country

Talk with your group - if you were to create a new country, what would its values be? Who would live there? What kind of climate might it have? Coming up with a backstory for your country will help you design a good flag to represent it.

### Flag Symbolism

Flags are not easy to design. Flags have a lot of symbolism in them.  Figure out what you want your flag to symbolize, and try to make sure that the flag conveys the symbols you want it to convey. It may help to talk with your group to decide what all is important to you and think about how you might represent those things using symbols.

### Flag Design

Try to design your flag based on good flag design principles. Here is a pamphlet from the North American Vexillography Association that describes their 5 principles for good flag design, with examples: <https://nava.org/digital-library/design/GFBF_English.pdf>

Also think about what's easy and hard about using Turtle to draw things, based on your experience with this week's lab. It's harder to draw a flower with Turtle than to draw a circle or a square. 

It might help to draw out ideas on paper or using the whiteboard first.

### Start Simple

Start simple.  First, design a really simple flag (a 2 or three color striped flag like the [Flag of Italy](https://en.wikipedia.org/wiki/Flag_of_Italy)?) and write a program to draw that. Then think about how you can make the flag more complicated or more interesting. Change the colors. Change the orientation. Change the size of the flag.

If you have specific symbols you want to incorporate, think about how to make them as simple as possible while still conveying meaning. You can also think about how you might make a more complex shape using simple shapes (like squares and circles) that are drawn on top of each other.

### Test frequently

Test your code often. Write a couple lines and test. Fix any errors that come up. Write another couple of lines and test again. The more code you write at once without testing it, the more likely you'll have trouble figuring out what isn't working and why! 

### Think like a Pen

Turtle graphics are designed to be like drawing with a pen.  Draw a line here, lift the pen, move it over here, put it back down, and draw another line. If you get stuck thinking about your program, figure out how you would draw the same thing with a pen. Break down the pen drawing into steps; those steps are the steps for the turtle. Again, using paper and pencil or using the whiteboard might help with this.

### Turtle Graphics

* [Official Turtle Documentation](https://docs.python.org/3/library/turtle.html)

If there is something you would do with a pen, you can probably do it with a turtle. There are a lot more turtle commands than what we used in the readings or in the lab. Look at the official Turtle documentation to find more commands to help you think about how to draw things.  

There are also loads of colors you can use in Turtle. See exercise 11 in [the Turtle lab]({% link labs/turtle.md %}) for a couple of ways to find colors.

Push yourself to try new things and new features with the Turtle graphics. It doesn't hurt to try. If you aren't sure, try and see what happens. For example, in one single program you can have two different turtles drawing different things at the same time!

### Use What You Know

You know a lot about programming already -- `if` statements and `for` loops and using variables to store information and getting input from users. Use all of that knowledge to help you in you drawing. Remember you can always refer to old labs for reminders on how to do things.

The lab on Monday had you drawing stars using Turtle. If you want to use star(s) on your flag, you can use the code you wrote for Monday. But note if you try to fill the star with color, the middle of it will still be empty. I've written a [different version of the code to make a star](https://gitlab.msu.edu/mi-250/turtles/-/blob/solutions/star_alt.py?ref_type=heads){:target="_blank"} that does fill in the center with color, which you can use if you want.

### Stay Organized, and Use Comments

One of the hardest parts of programmming computers to draw on the screen is the sheer number of commands and instructions it takes. You will find that your programs are getting long quickly because it takes a lot of instructions to draw anything.

Think about how to stay organized. You can always add blank lines; use that to group sets of commmands. So if you've got one set of commands that draws a blue square, and another that draws a white star, leave a blank line in between them.  

Also, use comments (lines that start with `#` that don't get read by Python) to tell yourself what those chunks of code do, logically. Its hard to understand what `fd(10); right(120); fd(10); right(120); fd(10)` does. It is much easier if you label this with `# Draw a triangle`:

```
# Draw a Triangle
fd(10)
right(120)
fd(10)
right(120)
fd(10)
```

Adding comments to your code is a really good way to remind yourself (and your group mates!) what the code is doing as your program gets longer.

### Use Programming's Strengths

Your flag is a computer program. That means that it can do things that other flags cannot. Think about how you can use programming to make your flag more interesting than just a flat drawing. For example, could you animate something on the flag, or have a special way of drawing the flag? Or maybe you can ask the user for some input, and then customize the flag around that input. Maybe you can use the `random` library to make the flag have different dimensions every time the program is run.

Programming can be an artistic tool. And unlike other artistic tools, like paintbrushes or clay, programming can be very dynamic and interactive - it can produce things that are different each time the program runs. How can you harness this strength of programming to make your flag unique?
