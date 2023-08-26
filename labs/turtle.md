---
parent: Week 5
topic: Turtles
git: https://gitlab.msu.edu/mi-250/turtles
nav_exclude: true
visible: false
---

For this lab, we are going to use a git repository like we did for last week. The first thing you should do is fork the
turtles repository, add your partner, the instructor, and the TA to the repository, and then clone the repository onto
your computer. Refer to last week’s lab for instructions on how to do this.

For this lab, we will be working with turtle graphics all day.  There are a LOT of commands that can get the turtle to
do things.  You will need to refer back to the documentation frequently to figure out what commands exist, and how to do
what you need to do.  For reference, here are links to the documentation; I suggest you keep one or more of these open
as you work:

* [Turtle Documentation](https://docs.python.org/3/library/turtle.html)

I also *strongly* advise you to work incrementally.   Add one or two lines of
code, and then run it to see what happens.  Add one or two more lines, run it
again.  And so on.  The more often you run it, the more you'll understand what
it is doing and the easier it will be to get it to do what you want it to.

## Draw some things

### Exercise 1: Finish the square

In the git repository, you should see a program called `square,py`.  This program is supposed to draw a square on the
screen that looks like this:

![square]({% link img/square.png %})

However, the program isn't finished!   Run the program with `python square.py` (or `python3 square.py` on Mac) and see
what happens.

Edit the program to finish drawing the square.  Remember that the `right()` and `left()` commands turn the turtle in
*degrees* -- 360 degrees turns the turtle all the way around so it is facing the same way it started.  90 degrees is a
right turn.  180 degrees turns the turtle around to face the opposite direction is started.

### Exercise 2: Finish the stick figure

In the git repository you should see a program called `person.py`.  This program begins to draw a stick figure using
turtle graphics.  Run this program using
```
python person.py
```
(On MacOS, you probably need to run it with `python3`)

It should start to draw a stick figure, and then wait for you to close the window.   Notice that python keeps running
(but doesn't do anything) until you close the window.

Write the code to finish drawing the stick figure.  The `person.py` file contains some comments for what you'll need to
write to finish it.

Don't try to do this all at once.  Start by drawing on a piece of paper without lifting up your pen: what do you need to
do with the pen?  Next, write one or two commands, and then run the program to see what happens.  Write more
commands, and see what happens.  

Once it is finished the person should look like this:

![person]({% link img/person.png %})

*Note*: Pay attention to the direction the arrow is facing. After drawing the
code that I wrote, it is facing down.  That means if you turn right, it will
end up facing left (because if you facing down and turn right, that's where you
end up).

### Exercise 3: Pen Up and Down

Next, we are going to do a bit of writing with our turtle.   Create a new program, called `MI.py`, that writes the two
capital letters "MI" next to each other.  The two letters should not be touching each other.  It should probably look
something like this:

![mi]({% link img/mi.png %})

To do this, you can use the `penup()` and `pendown()` functions to lift up the pen and put it back down.

Before you can use any of the turtle commands, you need to remember to *import* the turtle library.  Importing brings in
additional functionality into python that it normally doesn't have.  To import the turtle library, use the command
```
from turtle import *
```
at the beginning of your program.  Notice, both of the previous programs do that.

Also, for turtle programs, it helps to end the program with `done()`.  This causes the program to wait until the user
clicks on the image before finishing and closing the window..

Don't forget to add, commit, and push this file to your git repository.


### Exercise 4: Names, squared

For the next exercise, create a new program called `names.py`.  This program should use the `write()` function to print
out both your name and the name of your partner for the lab.  It should also draw a red box around those names.  

Here is mine:

![rick]({% link img/rick.png %})

Note: you can change the color of the pen with `pencolor("red")`



## Interactive Drawing!

The program `guestbook.py` is a simple guest book app that prints out a name on the screen.  If you run it, it should
print my name, and move the turtle a bit.

### Exercise 5: Input name from user

The turtle has a function called `textinput()` that allows you to ask the user for a text input, and then saves it to a
variable. Modify the guestbook program to ask the user for their name, and then print out the user's name on the screen.

`textinput()` causes a window to pop up asking the user for information.  It needs two pieces of information -- the
title of the window, and the prompt that is displayed to the user.  So, for example, the code:
```
name = textinput("Name", "Please enter your name")
```
would pop up a window titled "Name" and ask the user to "Please enter your name" and then save whatever they enter into
the `name` variable.


### Exercise 6: Second Name

Now modify the guest book to ask the user for a second name, and display that second name below the first one.  You'll
have to move the pen down before writing that second name to make sure the names aren't on top of each other.


## Seeing Stars

### Exercise 7: Star

Create a new program called `stars.py`.   For this program, write a program that draws a 5 pointed start.  Here's the
catch:  You must you a `for` loop do draw the star.  If you do it right, the star can be drawn using only 3 lines of
python code.

Note: The angle at a point of a star is 144 degrees.

Note 2: Drawing a star should just involve moving forward, turning 144 degrees, moving forward, turning again, and so on
until the star is finished.

One finished, it should look like this:

![star]({% link img/star.png %})


### Exercise 8: Row of stars

Next, modify your program to use a `for` loop to create a row of 5 stars next to each other.  You should use the same
code you wrote above to draw a single star, but put it in a loop with some additional code between the stars to move the
turtle to get ready to draw the next star.


### Exercise 9: Colored Stars

Modify your program to fill in the stars with a color.  You can specify the color using the `color()` command.  Use
`begin_fill()` when you start drawing to begin filling in the stars, and `end_fill()` when you are done with what you
want filled.  Make the stars brightly colored.   Can you make the stars different colors?

*Note*: For some reason, on Macs, it doesn't actually fill in the center of the
star.  That's OK for now.  Just get it to fill in as much as you can.   If you
want to know why or how to fix it, ask Caitlin or me.

![Hollow star, on a Mac]({% link img/star-mac.png %})
Hollow star, on a Mac

![Filled star, on Windows]({% link img/star-win.png %})
Filled star, on Windows

### Exercise 10: Looped Guestbook

Go back to your guestbook code.  Right now, it should ask for one name, draw it on the screen, then ask for a second
name, and draw it.

Put the code for the guestbook into a loop so that multiple people can enter their names, and those names are displayed
on the screen for everyone to see.

*Note*: You will need to make sure the turtle moves between names so that they aren't all on top of each other.


### Challenge 1: Lots of Stars

Now that you have the commands to draw a star, let's draw lots of stars.  Using for loops, modify your previous program
to draw 100 stars in a 10 by 10 grid.

Hint: the command `speed(0)` will speed up the turtle drawing so you don't have to wait as long.

### Challenge 2: White stars on a Blue Background

Modify the program to create a blue background, and change the stars to be solid white.  You can set the background
color using `bgcolor()`, or by drawing a large square and filling it in with the color you want before you draw the
stars.

### Extra Challenge: The US stars

Draw the 50 stars in the pattern they appear on the [US Flag](https://en.wikipedia.org/wiki/Flag_of_the_United_States#/media/File:Flag_of_the_United_States.svg)

### Extra Challenge: The US Flag

Now that you've got the blue and white stars from the US flag, it shouldn't be too hard to add the red and white
stripes.   Modify your program to finish drawing the US flag.

### Extra Challenge: Fancy Guestbook

Modify the guestbook to make it look nicer than just having a list of names.  For example, draw a symbol (a star?) next
to each name, and/or put the names in a colored box.  Or add a way for the user to type "quit" and have the guestbook
quit.




