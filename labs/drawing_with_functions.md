---
parent: Week 7
topic: Drawing with Functions
git: https://gitlab.msu.edu/mi-250/drawing-functions
nav_exclude: false
visible: true
---

## Using Functions

In your readings, you learned about functions.  Functions are named sections of code, that you can "call" from other
parts of code.  In this section of the lab, we will be using the `cards.py` program.  The top of this program defines 4
functions in it: one that draws a diamond, one that draws a heart, one that draws a club, and one that draws a spade.
You shouldn't need to modify or change these functions; leave them in the program.    If you run the program, it just
draws a spade right now (because, at the end of the file, we call the `spade()` function).

### Exercise 1: Draw a club

For the first exercise, change the program to draw a club instead of a spade.   This should only involve changing one
line of the program.

![club]({% link img/club.png %})

### Exercise 2: Draw a heart

Next, change the program to draw a heart instead of a spade.  Again, this should only involve changing one line.

![heart]({% link img/heart.png %})

### Exercise 3: Draw and spade and a heart next to each other

Next, change the program to draw a spade and a heart next to each other.  You shouldn't need to change the functions at
all.  Instead, you should call the spade function, then move the turtle, and then call the heart function.

![spade and heart]({% link img/spadeheart.png %})

*Hint*: Remember you can use penup() and pendown() so that you don't draw a line in between drawing the two shapes.

### Exercise 4: Draw two clubs and a diamond next to each other

Finally, modify your program to draw two clubs and a diamond next to each other.

![club club and diamond]({% link img/clubclubdiamond.png %})

## Creating your own functions

In `cards.py`, the code I gave you used `def spade():` to define the `spade` function.   All of the indented lines after
that are part of that function.  You can use `def` to create your own functions.  

### Exercise 5: Fill in a function that draws a star

Look at the program `stars.py`.  It has a `def star():` near the top of the program.  That is creating a new function
that is supposed to draw a star.  However, right now, the code for the function (everything indented below it) just says
`pass` -- which is python's way of saying "do nothing".  

Modify the star function to include the code for drawing a star.   When you run the program, it should look like this:

![stars in a cirlce]({% link img/stars.png %})

*Hint*: Remember, it is OK to look at past labs (and the solutions to past labs) for help.

*Hint 2*: You can speed up the turtle by putting the command `speed(0)` near the top of your program.

<!-- Exercise 7: Convert code into a function, so it can be called more than once -->

## Functions with parameters

So far in this lab, we have just used functions as a way of organizing our program.  Basically, we give a section of our
program a name, and then we can "call" that function -- which runs the section with the name.   This is a really useful
feature of functions.  Remember how long and confusing the code was for your flags two weeks ago. If we broke it up into
logical pieces -- the piece that draws a bar, the piece that draws a star, etc. -- then we can give each of those pieces
a name and make them a function.  This would make the code easier to understand.

Functions can do more than just that, though.  They can also have parameters that modify what they do. 

### Exercise 6: Sizes of Stars

Look at the program `sizes.py`.  It has a function called `star` that draws a star.  Except, unlike the star function
you wrote above, it accepts a parameter -- `size`.  The size parameter tells it how big of a star to draw.   

Right now that program draws a single star of size 25.  Modify the program so that it draws 3 stars next to each other,
each one bigger than the other (25, 50, 100).  When complete, it should look like this:

![3 stars]({% link img/sizes.png %})

### Exercise 7: Colored bars on a flag

Next, look at the program `flag.py`.   The goal of this program is to draw the flag of Germany. Unfortunately the
program is incomplete.  Since each of the three bars is the same thing except a different color, I decided to write a
`bar()` function that draws a single bar.  That function takes one parameter -- `bar_color` -- that tells the function
what color to make the bar.

Let's start by writing a simple `bar()` function that just draws a 300x50 rectangle.  If you put the code to draw a
rectange into the `bar()` function, then it should look like then when it works.

![3 bars]({% link img/empty_flag.png %})

### Exercse 8: German Flag

Let's continue to modify the flag program to draw the flag of Germany: three colored bars that are black, red, and
yellow.  The `bar()` function accepts one parameter -- `bar_color`.  When it is used at the bottom of the file, it calls
`bar()` three times, each time asking to draw a different colored bar.   

Modify the code for the bar function to color that rectangle whatever color the parameter says it should be. When you
get the bar function working to correctly draw the colored rectangle, the program should look like this:

![Flag of Germany]({% link img/germanflag.png %})

### Exercise 9: Flag of Ghana

You now have a function that draws horizontal bars, and a function that draws a star of a different size.  As the next exercise in this
lab, copy both of those functions into the same file and write a program that draws the [Flag of Ghana](https://en.wikipedia.org/wiki/Flag_of_Ghana#/media/File:Flag_of_Ghana.svg).

Copy your flag program to a new file. Your code should use the `bar()` function and the `star()` function to draw the
colored bars and the black star.   Other than that, the only code you should need to write is moving the turtle to the
right place.

*Note*: You'll probably need to also color the star black.

## Your own functions

So far in this lab, you have used functions that I wrote, and filled in functions that I created.  Next, you need to
write your own function.

### Exercise 10: Next Suit Function

Go back to the `cards.py` program.   Write a `move_next()` function that moves the turtle to a place to get it ready to
draw the next suit.   Once your function works, it should be able to be used like this:

```
spade()
move_next()
heart()
move_next()
diamond()
```

## Challenges

If you complete all of the exercises, try these challenges:

### Challenge: User Input

Go back to your `cards.py` program and modify it to ask the user which suit it should draw.  Then draw the suit that the
user specifies.

### Extra Challenge: 5 suits

Put this user input into a loop: Ask the user 5 times what suits they want drawn, and then draw those five symbols next
to each other on the screen.

### Challenge: Sized Circle of Stars

Modify the stars program to draw circles of different sized stars.
