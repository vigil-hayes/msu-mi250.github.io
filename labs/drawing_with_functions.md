---
parent: Week 7
topic: Drawing with Functions
git: https://gitlab.msu.edu/mi-250/drawing-functions
nav_exclude: true
visible: false
---

## Using Functions

In your readings, you learned about functions. Functions are named sections of code that you can "call" from other parts of the program. Functions let you use the same chunks of code over and over again without having to write it all out each time. 

In the first section of the lab, we will be using the `cards.py` program. The top of this program defines 4 functions in it: one that draws a diamond, one that draws a heart, one that draws a club, and one that draws a spade. You shouldn't need to modify or change these functions; leave them in the program. If you run the program, it just draws a spade right now (because, at the end of the file, we call the `spade()` function).

{% capture _ %}{% increment exercise5 %}{% endcapture %}

### Exercise {% increment exercise5 %}: Draw a club

Change `cards.py` to draw a club instead of a spade. This should only involve changing one line of code in the program.

![club]({% link img/club.png %})

### Exercise {% increment exercise5 %}: Draw a heart

Next, change the program to draw a heart instead of a spade. Again, this should only involve changing one line.

![heart]({% link img/heart.png %})

### Exercise {% increment exercise5 %}: Draw a spade and a heart next to each other

Next, change the program to draw a spade and a heart next to each other. You shouldn't need to change the functions at all. Instead, you should call the spade function, then write some code underneath it to move the turtle, and then call the heart function.

![spade and heart]({% link img/spadeheart.png %})

*Hint*: Remember you can use `penup()` and `pendown()` so that you don't draw a line in between drawing the two shapes.

### Exercise {% increment exercise5 %}: Draw two clubs and a diamond next to each other

Finally, modify your program to draw two clubs and a diamond next to one another.

![club club and diamond]({% link img/clubclubdiamond.png %})

## Creating your own functions

In `cards.py`, the code I gave you used `def spade():` to define the `spade` function. All of the indented lines after that are part of that function. You can use `def` to create your own functions.  

### Exercise {% increment exercise5 %}: Fill in a function that draws a star

Look at the program `stars.py`. It has the line `def star():` near the top of the program. That is creating a new function that is supposed to draw a star. However, right now, the code for the function (everything indented below it) just says `pass`. This is a placehoolder: `pass` is Python's way of saying "do nothing".

Modify the star function to include the code for drawing a star. When you run the program, it should look like this:

![stars in a circle]({% link img/stars.png %})

*Hint*: Remember, it is OK to look at past labs for help. You probably drew some stars in the [Turtle lab]({% link labs/turtle.md %}){:target="_blank"}. 

*Hint 2*: You can speed up the turtle by putting the command `speed(0)` near the top of your program.

## Functions with parameters

So far in this lab, we have just used functions as a way of organizing our program. Remember how long and confusing the code was for your flags two weeks ago. If we broke it up into logical pieces -- the piece that draws a bar, the piece that draws a star, etc. -- then we can give each of those pieces a name and make them a function. This would make the code easier to understand, and also allow you to use each chunk of code multiple times. For example, if your flag had three stripes, you could make a function for a stripe and then call it three times.

Functions can do more than just that, though. They can also have parameters that modify what they do. The parameter is what goes inside of the parentheses for a function name. For example, `forward()` is a function that takes one parameter: a number which specifies the distance in pixels that the turtle should move forward. You can put any number you like into the `forward()` function and it will move the turtle that many pixels forward.

Parameters make functions more flexible. Parameters are like variables that you can put different things into to make the function do different things every time you call it. The `forward()` function in Turtle will move a different distance depending on what number you give it, for example.

### Exercise {% increment exercise5 %}: Sizes of Stars

Look at the program `sizes.py`.  It has a function called `star` that draws a star. Except unlike the star function you wrote above, it accepts a parameter -- `size`.  This parameter tells it how big of a star to draw.   

When you define a function that has parameters, you also define the parameters, like this:
```
def star(size):
```
This defines a function called `star()`, with one parameter, called `size`. The parameter is a variable that is specific to the function: it will be filled in later when you call the function. The code inside the function should say where the parameter is used. Notice where `size` is used inside of the `star()` function.

Right now that program draws a single star of size 25. Modify the program so that it draws 3 stars next to each other, each one bigger than the other (25, 50, 100). When complete, it should look like this:

![3 stars]({% link img/sizes.png %})

*Hint:* because you've added a parameter, when you call the `star()` function now, you have to call it with the parameter filled in or Python will give you an error.

*Hint 2:* remember you'll need to write some code to move the turtle between drawing each star so the stars don't overlap.

### Exercise {% increment exercise5 %}: Fill the stars with color

Let's add another paramater that lets you change the color of the star on the fly. You can add a second parameter to the function by putting a comma after the first one, like this:

```
def star(size,star_color):
```

Note I've called it `star_color` and not just `color` - that's because `color()` is already a reserved word in Turtle.

Now we've defined the parameter, but it won't do anything unless we call it inside of the function as well. Notice how the parameter `size` is used: it's a placeholder for a number that get put into the function when you call it later. We can do the same with color. Normally you'd define the color like this:

```
fillcolor("black")
begin_fill
<draw shape>
end_fill
```

The code above hardcodes the color black: that means if you put it in the function as-is, every time you call it, it will only draw a black star. Instead, we want to use the parameter `star_color` in place of `"black"`. That way the parameter can be replaced with whatever color you want when the function is called.

When you call the star function at the bottom of the program now, make each of the three stars a different color.

### Exercise {% increment exercise5 %}: Use new star function in circle

Your star() function is a bit more flexible now - let's use it in `stars.py`. Replace the star() function you wrote for `stars.py` with the updated function from `sizes.py`. What happens? Aside from the function itself, what other code do you have to change to get it to work correctly?

*Hint:* You should only have to change one line of code inside the for loop in the main code section.

## Write Your Own Functions

### Exercise {% increment exercise5 %}: Bars for a flag

Next, look at the program `flag.py`. The goal of this program is to draw the flag of Germany, but the program isn't done yet. Right now it's also very inefficient - there's a lot of repeated code. When you run the program, it should look like this: 

![3 bars]({% link img/empty_flag.png %})

The code right now makes three rectangles, one on top of the other, like a flag but without color. Notice the code for each of the three rectangles is exactly the same. This is a good use case for using a function instead!

Write a function called `bar()` and replace the code that draws each bar with calls to that function. Remember a function is defined like this:

```
def my_function():
    <stuff>
```

The code inside your function should only draw one bar of the flag. To make three bars, you'll need to call the function three times in the code below. When you run the program after you've made your changes, it should look exactly the same as it did before, but have far fewer lines of code.

### Exercise {% increment exercise5 %}: Move Function

There's also some repeated code in between each bar that draws which moves the turtle in preparation for drawing the next bar. Make a function called `move_next()` that moves the turtle and call it in place of the repeated code.

### Exercse {% increment exercise5 %}: German Flag

Let's continue to modify the flag program to draw the flag of Germany: three colored bars that are black, red, and yellow. Your `bar()` function currently doesn't account for color, and doesn't accept any parameters. Modify it so it has one paramater called `bar_color` and then use the parameter inside the function to define the color. Remember the parameter is like a variable inside of the function; it will be filled in with a 'real' value when the function is called. 

You will need to modify your function calls at the bottom of the program so that they use the new parameter. So the first bar should be drawn using `bar("black")` instead of `bar()`. The colors in the German flag are "black", then "red", then "yellow".

Your program should look like this:

![Flag of Germany]({% link img/germanflag.png %})

*Hint:* `pencolor()` changes the color of the outline, `fillcolor()` changes the fill color. `color()` changes the color of both the outline and the fill. Which should you use to get it to look like the screenshot above? Also remember to use `begin_fill()` and `end_fill()`.

### Exercise {% increment exercise5 %}: Flag of Ghana

You now have a function that draws a horizontal bar, a function that moves the turtle between drawing bars, and a function in a different program that draws a star with a `size` parameter. Let's use them all together. 

Create a new program called `ghana.py` and copy all three of those functions into it. Use those functions to write a program that draws the [Flag of Ghana](https://en.wikipedia.org/wiki/Flag_of_Ghana#/media/File:Flag_of_Ghana.svg).

## Challenges

{% capture _ %}{% increment challenge5 %}{% endcapture %}

If you complete all of the exercises before the end of class, try at least one of these challenges:

### Challenge {% increment challenge5 %}: 5 suits

Modify your `cards.py` program to ask the user which suit it should draw. Then draw the suit that the user specifies.

Put this user input into a loop: Ask the user 5 times what suits they want drawn, and then draw those five symbols next to each other on the screen. Bonus: keep drawing suit symbols until the user says to stop.

### Challenge {% increment challenge5 %}: Random color stars

Modify `stars.py` to draw each star in a random color. Use the list of colors below and `random.choice()` so that when each star in the circle is drawn, it draws as a random color from the list. You'll need to modify how the `star_color` parameter in your function works to get this to work.

```
colors = ["red","orange","green","blue","yellow","light blue","purple"]
```

You can put more colors into the list if you want to.

Note: remember to add `import random` to the top of your program.

### Challenge {% increment challenge5 %}: Draw the original U.S. flag

The [Betsy Ross variant of the original U.S. flag](https://en.wikipedia.org/wiki/Flag_of_the_United_States#/media/File:Betsy_Ross_flag.svg){:target="_blank"} had 13 stars in a circle on the blue part of the flag. The code in `stars.py` draws a circle of 13 stars. Use the `star()` function, the loop that draws the circle of stars, and the `bar()` function to draw the original U.S. flag. You'll probably need to modify the `bar()` function so it draws skinnier bars.
