---
parent: Week 7
topic: Random Pizza Generator
nav_exclude: true
visible: false
published: false
---

<!--
Ideas:
- Specify a quartered coat of arms in a dictionary, and draw it using functions
- Write code that counts words in a string (duplicates later lab)
- Choose-you-own-adventure, with dictionaries.
- Visual choose-your-own-adventure, with screen coordinates in a dictionary
- Walk along a map?
- Guestbook with messages, sorted?
- Import JSON and work with it?
- Random recipe (pizza) generator
-->

Work in teams of 2-4 people to make a random pizza generator.  The program should generate a dictionary containing a
randomly generated pizza, and print out the randomly generated pizza. The program must store the pizza in a single
dictionary.  Once generated, draw the random pizza on the screen using turtle.

Only after you are fully generating a random pizza, then work on the drawing
the pizza on the screen.  Check with the instructor or the TA before moving on
to the drawing portion.

---

That’s it. That’s the whole of the instructions – form a group, generate a random pizza, draw it on the screen, and have
fun with it. 

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### Data structures: What are the parts of a pizza?

Dictionaries are ways of storing *structured* data.  It helps to begin by putting structure on things.  What are the
parts of a pizza that you'll need?  Shape?  Size? Crust?  Sauce?  Toppings?  Sides? Number of slices?  The best way to
start is to figure out the "data structure" of the pizza.  If you want to store a pizza in a dictionary, what should
that dictionary look like?  

Once you think you know what the parts of the pizza are, write it into a python dictionary.  Actually write the code!
Create a dictionary in a python file, and then fill it in with one example pizza.  Have your program print it out.  Then
run your program.  That way, you'll know that you got the basic pizza dictionary data structure right and working.

### Random Generator

Python doesn't have a built-in way of randomly choosing whole pizzas.  Instead, you will probably need to have it
randomly choose each part of the pizza.

If you go back to the [week](../5/week.html) on [lists](../5/lab.html), we learned that you can use `random.choice()` to
randomly choose an item from a list. It works like this:
```
mylist = ['red', 'green', 'blue']
mycolor = random.choice(mylist)
```

For each type of thing (crust, sauce, etc.), you can create a list of the possible options.   Then use `random.choice()`
to pick one of the options.  Then you will need to add whatever was chosen into your pizza dictionary.

### Start simple, and build

Start by hard coding a whole pizza and printing that out.  This simple program should always print out the same pizza.
Then you can add features one by one.  Start by adding a randomly generated crust. See if you can get that working, so
that when you run the program more than once, it gives you the same pizza, but with different crusts.  After that, do
sauce.

Toppings will be more complicated, won't they?  How many toppings do you want?  How do you represent them in the
dictionary?  Do you always put the same number of toppings on the pizza, or do you randomly generate the number of
toppings?   I recommend getting the basic randomized-crust-and-sauce pizza working before you start working on the
toppings.

**Only after you are fully generating a random pizza, then start on the drawing the pizza on the screen.**

### Use "if" to handle randomness

Because the program is randomly generating a pizza, as the programmer, you don't know ahead of time what it will choose.
What that means it that you'll have to write your program to handle all of the possible options that can be generated.
Think about that: each time the program runs, it'll draw only one pizza.  But, the program itself will have to have the
code in it to draw all of the different types of pizzas.

Start by thinking about how you can do this effectively.  For example, if I am randomly chosing between "marinara" and
"alfredo" sauces, the only real difference in drawing might be the fill color; I fill the circle with different colors.
When drawing the pizza, I could use an `if` statement to change the color appropriately:
```
if pizza['sauce'] == "marinara":
	color('red')
elif pizza['sauce'] == "alfredo":
	color('white')
begin_fill()
circle(200)
end_fill()
```

### Use functions for drawing different options

As you work on drawing code, you'll find your code is getting really long and hard to read.  One way to make it easier
is to use functions.   Think about each of the possible options, and write a function to draw that option.  For example,
you could have one topping that is pepperoni (a bunch of red circles), and another topping of pineapple (yellow
squares). Use functions to stay organized!  Write a separate function for each of these!

For example, you could have a function called `draw_pepperoni()` that draws red circles.   And you could have another
function called `draw_pineapple()` that draws yellow squares, or `draw_olives()` that draws black or purple circles..

Then, in your main program, you can just call those functions:
```
if 'pepperoni' in pizza['toppings']:
	draw_pepperoni()
if 'pineapple' in pizza['toppings']:
	draw_pineapple()
```

### Think about testing

This program is supposed to draw a random pizza.  Each time you run it, it will pick different options and draw those on
the screen.  This means each time you run the program, it'll look different.  

This might be really annoying while you are working.  Imagine that you are working on the code to `draw_pepperoni()`.
You run your program, and it randomly picks toppings.  What if it doesn't pick pepperoni?   Then you'll have to stop and
run it again.  Ugh.  Very annoying.

It is worthwhile to think about *temporary* changes you can make to the program while you working on the code.   While
you are working on the `draw_pepperoni()` code, maybe you should temporarily change the code to *always* have pepperoni
toppings.  Then it'll be easier to test and see if your code to draw pepperoni is working correctly.   Once you finish
working on the pepperoni code, then you can change the code back to randomly choose toppings.

This kind of *temporary* change to programs is quite common among programmers.  We will often make temporary changes to
our programs to make it easier to run them and see if they are working right.  Just don't forget to change it back when
you are done!

### For drawing, Start simple, and build

You might have noticed that every studio so far includes the advice to "start simple, and build".   This is really
imporant.  Don't try to do everything at once.  That isn't how computer programs are written.  Instead, we start by
getting something simple working correctly, and then we slowly add more and more features until it all works.

Today's advice includes this twice!  It really is that important!   

When writing your drawing code, be sure to do this also!  Start really simple.  What is the simplest pizza-like-thing
you can do?   Maybe you should always start with square pizzas because squares are easier than circles?   Maybe at
first, you should only allow one topping.  Something like that.  

Figure out what the absolute simplest pizza you can draw it, and do that first.  Then, slowly add complexity.  First,
add the things that are easiest to add.  What is easier to add: different sauces? different toppings?  different pizza
shapes?   Do whichever one is easiest, and try to get that working.  Only *after* that is working should you move on to
the next one.







