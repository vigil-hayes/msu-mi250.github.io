---
parent: Week 4
topic: Counting and Loops 
git: https://gitlab.msu.edu/mi-250/counting-and-loops
nav_exclude: true
visible: false
---

For this lab, we are going to use a git repository like we did for last week.  The first thing you should do is fork
this week's GitLab project (linked above).  Once forked, add your partner to the project (and Caitlin and me), and then clone the repository
onto your computer.  Refer to last week's lab for instructions on how to do this.

{% capture _ %}{% increment exercise3 %}{% endcapture %}

### Exercise {% increment exercise3 %}: Count

As an example of how to do loops, look at the file `counter.py` in the git repository.  Run the program to see what it
does.  Then open the file and look at the code.  How does it work?   Read the code and see if you can figure out
how this program works.  Then explain how this code works to your partner.


## Singing a song

### Exercise {% increment exercise3 %}: Ain't No Sunshine

Bill Withers is a great songwriter. One of his most famous songs is *Ain't no sunshine*.  However, he needs your help.
Right now, if you run the program `sunshine.py`, it'll print out his current lyrics to the song.

But the song is missing something.

In the middle of the song is the line "I know".  He sings the line slowly, longing for his lost love.  But really, it
would be much better if he just kept repeating that same line over and over, because when you feel that way, that
feeling just doesn't go away.

Modify the program so that it prints out that line 20 times before moving on.

You should use a for loop to do this.

*Hint*: It should look something like this:

![I know!]({% link img/aint no sunshine with i know repeats.png %})

### Exercise {% increment exercise3 %}: Looping whole verses

If you run the program `bottles.py` in the git repository, it will print out the first verse of the song [99 bottles](https://en.wikipedia.org/wiki/99_Bottles_of_Beer).  

Modify the program to print out all 100 verses of that song.   Use a `for` loop to do this.   

The final code for this program should contain less than 100 lines of code.

*Hint*: Start by looping a small number of times (5?).  Then once that works, increase the number so it loops 100 times.

*Hint 2*: `range(5)` will count from 0 to 4. It always stops just before it
gets to the end number.  `range(1, 5)` will count starting at 1, so will caount
from 1 to 4.   `range(5, 1, -1)` will count by `-1`, so it will count backwards
from 5 down to 2.

*Hint 3*: A `for` loop uses a variable.  `for i in range(10)`.  That `i` is a variable.
You can use that variable inside the loop.  Each time through the loop, the `for` loop 
fills in that variable with the current number.  So the first time through the loop,
`i` is 0; the second time, it is 1, the third time is 2, and so on.

### Exercise {% increment exercise3 %}: Change the final verse

Modify your program to change the final verse of the song.  Rather than singing zero, have it sing a different ending.
For example, here is one alternative ending to the song:
```
No more bottles of beer on the wall, no more bottles of beer. 
We've taken them down and passed them around; now we're drunk and passed out!
```

*Hint*: The easiest way to do this is to do one fewer loops, and then copy-and-paste your print statements to happen
*after* the loop (not indented) and modify them so they look different.

### Exercise {% increment exercise3 %}: Change the 6th-to-last verse

There is an alternative way to sing the 99 bottles song, where the 3rd line is replaced with:
```
If one of those bottles should happen to fall, 98 bottles of beer on the wall...
```

Modify your program such that the 6th-to-last verse ("5 bottles") uses this alternative line instead of the normal line. 

*Hint*: You can use an `if` statement to check which loop you are on, and print out something different if you are on a
specific loop.


### Git

Don't forget to commit your changes to the git repository. Check the repository
on Gitlab to make sure that all of the programs are correctly in your git
repository.

If you haven't already, now would be a good time to swap driver and navigator.


## Text-based Drawing, with for loops

The first things we are going to do today is use for loops to do some basic text-based drawing.  We are going to write
programs that draw lines, squares, rectangles, triangles, and pyramids.

In the lab, there is a program called "line.py".   Run it with the command
```
python line.py
```

It should print out a horizontal line of eight `*` characters.

### Exercise {% increment exercise3 %}: User-input length line

Combine this with the counter in exercise 1.  Modify the line program to ask the user how long of a line they want (much
like exercise 1's counter asked for how high to count), and then use a `for` loop to print out a line of the length
requested by the user.

*Hint*: Remember the `range()` function, which is commonly used in `for` loops.

*Hint 2*: When the user types in a number, python stores it as a string.  You might need to convert it to an integer
with the `int()` function.

### Exercise {% increment exercise3 %}: Square

OK, now you've got a program that prints out a line of different lengths.  Create a copy of this program and call it
`square.py`.  Modify the program so that it prints out a square instead of a line --- it should print out multiple lines
that are all the same length.  So a square of size 3 looks like this:

```
***
***
***
```

Be sure to test this program with different sizes.


*Hint*: You can have `for` loops inside `for` loops.  Remember that python uses indentation to show what is inside the loop.

*Hint 2*: Don't forget to add a new line character at the end (by running `print("")` without the `end=` parameter).  Should this be inside the inner for loop, or the outer for loop?

Add the square program to git.  Don't forget to commit and push.

### Exercise {% increment exercise3 %}: Triangle

Create a copy of the square program and call it `triangle.py`.  Modify the program so that it prints out a triangle.  A
right triangle of size 4 should look like this:

```
*
**
***
****
```

Be sure to test this program with different sizes.

Add the triangle program to git.  Don't forget to commit and push.

### Exercise {% increment exercise3 %}: Rectangle

Create a copy of the square program and call it `rectangle.py`.  Modity the program so that it asks the user separately
for a length and a width, and prints out a rectangle.

Be sure to test this program with different sizes.

Add the rectangle program to git.  Don't forget to commit and push.

### Git

At this point, you should have at least six different programs in your git repository.   Check the repository on Gitlab
to make sure that all of the programs are correctly in your git repository.



## Challenges

If you finish the lab, please try to do at least one of the challenges.  If you
can get two or more of the challenges working correctly, then you can leave
class early.

{% capture _ %}{% increment challenge3 %}{% endcapture %}

### Challenge {% increment challenge3 %}: Alternate lines

Modify your bottles program so that every other line uses the alternative version.  So the first verse should say `take
one down, pass it around`, the second verse should say `if one of those bottles should happen to fall`; the third verse
should say `take one down, pass it around`, and so on.

*Hint*: Python has a modulus operator: `%`.   Modulus finds the remainder after division.  So `13 % 5` is equal to 3,
since when you divide 13 by 5 ,you get 2 with a remainder of 3.   You can use this to figure out if a number is even or
odd: if the line number divided by 2 has a remainder of 0, then it is an even number.  If the line number divided by 2
has a remainder of 1, then it is an odd number.


### Challenge {% increment challenge3 %}: Backwards Triangle

The triangle program you just created is up against the left side of the window.   Create a copy of the triangle
program and call it `backwards.py`.  Modify that program so that the vertical edge of the triangle is on the right side
of the triangle, like this:
```
   *
  **
 ***
****
```

Be sure to test this program with different sizes.

*Hint*: You will probably need to add a second for loop to print out the leading spaces.

*Hint 2*: Think about indentation.   If code is indented, then it happens *inside* that for loop -- it happens over and
over in the loop.  If it isn't indented, then it happens *after* the loop, only once.

Add the backward triangle progrm to git.  Don't forget to commit and push.

### Challenge {% increment challenge3 %}: Pyramid

Create a copy of your backwards triangle program and call it `pyramid.py`.  Modify the program to print out a pyramid
structure where the height of the pyramid is what the user asks for, and the base is twice that size.  So a pyramid of
size 5 should look like:

```
    **
   ****
  ******
 ********
**********
```

*Hint*: A pyramid is a backwards triangle next to a forwards triangle

Be sure to test this program with different sizes.

Add the pyramid progrm to git.  Don't forget to commit and push.

### Extra Challenge {% increment challenge3 %}:  Pointy Pyramid

Can you write a program that creates a pointy pyramid? Note the odd number of stars in each row.

```
    *
   ***
  *****
 *******
*********
```


