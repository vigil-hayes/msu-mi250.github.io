---
parent: Week 10
topic: Practicing Functions
git: https://gitlab.msu.edu/mi-250/more-functions
nav_exclude: true
visible: false
---

{% capture _ %}{% increment exercise8 %}{% endcapture %}

## Using Functions with Parameters

Today, we are going to write code to build a checkboard using Turtle and write some of our own functions. Today's lab is focused on learning more about how functions are actually used in real programming. You are always welcome to revisit [the previous functions lab]({% link labs/drawing_with_functions.md %}) to refresh your memory.

### Exercise {% increment exercise8 %}: Squares 

The file `board_1.py` wants to draw a game board, but it is missing the code for its `square` function. The square function takes two parameters -- how big the square should be, and what color the square should be. Fill in the code for this function.

![Board 1]({% link img/board_1.png %})

Test this.  Does it work? It should draw a large black square on the screen.

You can also test this by going down to the line where `square(400, "black")` is called, and change the number to a different size.  Does it draw a different size square?  (It should.)  This is generally a good idea when working with functions. Run the program a couple of different times, putting different values in the parameter to make sure that the function does what it is supposed to do. Don't forget to change the parameters back to the way it started `square(400, "black")` when you are done testing it.

*Hint:* Remember it's good practice to have the Turtle be in the same place AND facing the same direction at the start of the function as at the end.

*Hint 2:* I would recommend using `color()` here to define the color of the square. Remember `fill_color()` only affects the fill color, and `pen_color()` only affects the outline color. `color()` handles both.

### Exercise {% increment exercise8 %}: Red Squares 

The file `board_1.py` draws a large black square. Let's change this to draw a large red square. If you wrote your function well, then all you should need to do is change one line near the bottom to say `'red'` instead of `'black'`. Try that:

```
square(400, "red")
```

Test this. Does it work? It should draw a large red square on the screen.

If it does, then great!  You finished this exercise.  If it doesn't -- if it still draws a black square -- then your function isn't working the way it is supposed to. Go back to your function and modify it so that it draws whatever color square is specified on that line at the bottom of the program.

### Exercise {% increment exercise8 %}: Row of Squares 

The file `board_2.py` continues our work toward building a game board. Copy-and-paste the code for your `square` function into this file. You should see another function, called `row`. It wants to draw a row of squares. Write the code to do this. You should build on your square function; that is, you should repeatedly call your square function to draw a row of squares all the same color.

As you do this, think carefully about *side effects*. When you a call a function, it has side effects. For Turtle, the side effects include moving the turtle and changing the direction the turtle is facing. If your function has side effects, that can cause problems if you call the function multiple times, or if you call other functions after it. To deal with this, it is a good idea to try to make sure our functions are predictable -- they always leave the turtle in the same place it started and facing the same direction it started. So, make sure that all of the `right()` or `left()` turns in the function always turn a total of 360 degrees. If your square function from Exercise 1 has side effects, you might have to modify it to make it work in the row.

*Hint*: You should use a `for` loop with a `range()` parameter to draw the row; `for i in range(number):`

*Hint 2*: You shouldn't need to write turtle code for drawing a square again.  Just call your `square()` function to draw the square!

*Hint 3*: The hard part about this execise is understanding **parameters** of functions. It might help to go back to the readings and look at how they talk about parameters. Remember that parameters are variables; they get filled in with whatever is passed into the function when it is called, and you use them like normal variables, but only inside the function.

*Hint 4*: No hard-coded numbers are needed for the `row()` function.

![Board 2]({% link img/board_2.png %})

## Return Values

In Python, functions can *return* values that they figure out. For example, you've already used the `input()` function, which does 2 things: it prints out a prompt, and then it *returns* whatever the user enters. You then store that returned value into a variable when you say `variable = input("prompt")`.

### Exercise {% increment exercise8 %}: Next Color

Look at the file `color.py`. It contains a function called `next_color` that returns a value -- a string containing the name of a color. Right now, it always returns `"black"` as the next color. Run the program, and you can see what it does. The program has a variable called `col` that stores the current color, and prints out what it thinks the
current color is. Then it calls `next_color`, and it changes the current color from red to black. Then it repeats that again -- calling `next_color` and printing out what the current color is. However, since `next_color` always returns `"black"`, the current color always stays black.

`next_color` takes a parameter of what the current color is. Modify the `next_color` function to use an `if` statement to return different colors. If the current color is "red", return black. If the current color is "black", return red.

What happens when you run this program now?

### Exercise {% increment exercise8 %}: Checkerboard

Let's combine the last 3 exercises to see if we can get Python to draw a checkerboard pattern on the screen. Copy and paste your code from the previous three exercises into the `board_full.py` file. Then you should modify the `row()` function so that after it draws each square, it changes the color to whatever is returned from `next_color`. This should hopefully allow you to draw a checkerboard pattern on the screen.

*Reminder*: If you put `speed(0)` at the top of your file, the turtle will draw much faster.

![Checkerboard]({% link img/checkerboard.png %})

*Hint*: If you are having trouble getting it to work, try reading the code under `draw_board()` that calls `next_color()` to see how it is used.

### Exercise {% increment exercise8 %}: Draw a Rainbow

Let's take a detour from our board game. The program `rainbow.py` is designed to draw a rainbow. However, it currently only draws a weird orange box with a red stripe on top. 

It needs you to implement the function is `next_color()`. This function is interesting. It takes one parameter -- the current color -- and then figures out what the next color should be. That next color is then returned from the function. This is really similar to the `next_color` function from the previous exercise. Except this time, it needs to needs to handle more than just back-and-forth.

Finish writing this function. Once you finish writing this function, the program should draw a rainbow on the screen.

*Note*: The colors of the rainbow, in order, are usually red, orange, yellow, green, blue, indigo, and violet. Or maybe red, orange, yellow, green, cyan, blue, and violet, if you prefer. The screenshot below uses cyan and blue.

![Rainbow]({% link img/rainbow_output.png %})

### Exercise {% increment exercise8 %}: Rainbow Checkerboard

You've now got a nicer `next_color` function. You should be able to put that into the checkerboard file (replacing the black-and-red one) and produce a rainbow checkerboard!

Start by opening `board_full.py` and doing a File --> Save As and saving a new copy as `rainbow_board.py`.  

You should be able to do this by only replacing the `next_color` function. 

*Hint*: You will need to make it cycle to make it look like the screenshot. Modify your function so that the next color after the last color in the rainbow is the first again.

![Rainbow Checkerboard]({% link img/rainbow.png %})


## How are functions used?

So far, you've written functions that take parameters and do different things based on those parameters, and also functions that return values.

But why do we separate things into functions? What is the point?

In this section of the lab, we will try to understand the idea of *abstraction*: we can use functions to make programming easier by abstracting away the difficulties.

Let's take our checkerboard for example. Say we want to put a checker piece on one of the spots of the board -- how would we do that? Right now, you'd have to do a lot of work to figure out where on the screen it should go, the size it should be, etc. Let's see if we can make that simpler by writing a couple functions.

### Exercise {% increment exercise8 %}: Draw a Circle on a square

Go back to `board_full.py`. When you run it, the turtle stopped at the upper-left square of our checkerboard. Add a new function called `draw_piece` that draws a red circle on that square. It should take no parameters and should draw a piece on whatever square the turtle
currently is on.

*Hint*: The whole checkerboard is `400` pixels across, and there are `8` squares acrosss. So each square is `400/8` pixels. You don't need to do the math; the program can do it for you. Just specify `400/8` to get the right size.

*Reminder*: Turtle has a `circle()` function that draws a circle counterclockwise. It takes one parameter -- the size (radius) of the circle. Use it (along with `color()`, `begin_fill()`, and `end_fill()`) to draw a filled in circle. Note that the radius should be half of the size of a square -- so if `400/8` is the size of a square, the radius of the circle should be `400/8/2`.

*Hint 2*: Don't hard-code locations using `goto()`. That might work for this exercise, but it will make it hard to do the next exercises where we move the pieces to different locations on the board.

*Reminder 2*: Don't forget to call your `draw_piece()` function at the end of the file.

### Exercise {% increment exercise8 %}: Goto a square

In chess, each square is given a number and a letter so that players can describe each move they make - e.g. "queen to e4". We can do something similar here. Since we're using Turtle, though, let's give each square a designation that looks like x/y coordinates, but is a bit easier to use. 

Let's start in the upper left, where the turtle is and where you just drew a piece. Let's call that square (1,1). The one just to the right of it then will be (2,1) (and (3,1), (4,1), etc.). The one just below it will be (1,2). The lower right corner square is (8,8).

I've written a function called `goto_square()`, located in the file `goto_square.py`. It takes two parameters -- the square number coordinates for row and column. It then moves the turtle to the upper left hand corner of that square on the checkerboard.

Copy-and-paste that function into your checkerboard program.

### Exercise {% increment exercise8 %}: Place a piece on square (5,6)

Now combine these two functions. Use the `goto_sqaure()` function to goto square (5,6) on the board. Then use your `draw_piece()` function to draw a circle in the middle of that square.

![Piece on Board]({% link img/piece.png %})

### Exercise {% increment exercise8 %}: Place a piece on a square the user specifies

For the final exercise today, ask the user which square to put a piece on (using `textinput()`, which is very similar to `input()` and we used in the [first Turtle lab]({% link labs/drawing_with_functions.md %})).  You'll have to ask twice -- once for the row, and once for the column. 

Do you see how functions make this easier? Now, instead of having to do that complicated math each time you want to draw something on a square, you just call your `goto_square()` function which does the thinking for you. You just tell it which square to draw on.

This is one way functions are really useful. They provide an *abstraction* -- now that you have the `goto_square()` and `draw_piece()` functions, you don't need to think about circles, lines, and fills. All you need to do to play checkers is to go to a specific checkers square, and draw a piece there. Because of the functions, you can think about checkers pieces and not about Turtle lines and fills.

## Challenges

If you still have time before the end of class after completing all of the exercises, try at least one of the challenges below.

### Challenge 1: Change the size of the board

Take the code that I wrote and put it into its own function that draws a checkerboard. Modify the function to accept a new parameter -- the number of squares across on the board. Right now, it does an 8x8 checkerboard. Use your new function to draw a 10x10 checkerboard.

Note: You don't have to make the piece drawing work for this, but if you want to try, go for it!  

### Challenge 2: Multiple pieces

Use a loop to ask the user for multiple locations, and place a piece at each location they tell you to. 

Bonus: use alternate colors for each piece that is placed - one color for player one, a different color for player 2, and with the assumption that the players are taking turns.

### Challenge 3: Remove a piece

How would you remove a piece from the board?  Write a function to remove a piece from a specific square. 
