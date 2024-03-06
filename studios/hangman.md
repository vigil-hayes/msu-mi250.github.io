---
parent: Week 9
topic: Hangman
nav_exclude: true
visible: false
---

For the studio today, you are going to make a [hangman game](https://en.wikipedia.org/wiki/Hangman_(game)). The game works like this:

The game chooses a secret word, and displays a number of blanks indicating how many letters that word has. The player then has to guess the letters in the word. If the player guesses a letter correctly, the game fills in the letter in all places in that word that it appears.   If the player guesses a letter that is not in the word, then the game draws the next line in a stick figure (drawn with Turtle). The player wins if she or he guesses all of the letters in the word before the stick figure is completed. The player loses if they guess incorrectly so many times that the stick figure is fully drawn.

## Advice

What follows is some advice for building this program. You don't have to follow my advice; do whatever you want.

### Choose a drawing that works in pieces

The traditional hangman game uses a stick figure in a noose. That's pretty morbid, though, and I'd encourage you to choose something else to draw. Look at the Turtle drawings you've done for past studios and labs in this class - could any of them be adapted for use in the game? Keep in mind that a good drawing for this game should do these things:

* *be able to be split up into pieces so that each piece can be drawn separately to make up parts of the whole.* The stick figure traditionally used in hangman has 6-7 pieces that can be drawn separately. Having fewer pieces makes the game harder; more pieces makes the game easier.
* *use color smartly (or sparingly).* Remember if you want to fill a shape with color, you have to draw the entire shape first. That means if you have a drawing you want to use but it uses a color fill, you might not be able to use color when you split up the drawing into pieces. You can either plan to fill the color in at the end, or not use color, or only use an outline color (`pen_color()`).

### Use functions and modules to structure your program



### Work as a team

There are lots of parts of hangman. There's the user input side -- guessing letters, and checking to see if they are in a word. There is the hangman drawing side, that draws the figure incrementally. And there is the game logic, that chooses a word for the game and then connects the user input with the drawing.  

Spread out the work across the team. Have different people do different parts.   Use functions to capture the
different parts of the program.  Use git to share code.  This project is much easier if you break it into parts, and
then do the parts separately, and then put them together.  Make sure to leave time to put them together; its not as easy
as it sounds.

### Think about program structure

In the lab this week, you were reading code.  Almost all of that code had a nice, clear structure -- it had logical
things that it did, and it had a function for each logical thing.  Then, at the bottom, there was a "main" section that
was only a few lines long that connected those functions together.

Think about how you want to structure your program.  At a high level, what are the logical things that the program needs
to do?  How do they fit together in the program?  What information needs to be send from one logical thing to the next?
As you get started, draw a diagram that describes what those pieces are, and what information need to move from one to
the next.

### Break the program into pieces (functions)

Once you figure out the logical structure of your porgram, then use that to break the program into functions.  If you
try to write one big program that does this whole game, you will find it is really difficult.  Each time you find
yourself thinking you need the program to do something, write a function for that something.  Need it to draw a dash
with a letter in it?  Write a function for that.  Need it to draw the next line of the stick figure?  Write a function
for that.  It is pretty much impossible to have too many functions.

### Clone turtles

In almost all of your programs so far, you've only had one turtle.  But there is no reason to limit your program to just
one. You can use the `clone()` function of turtles to create new turtles.  For example:

```
from turtle import *

t2 = clone()

t2.color("red")
t2.left(90)
t2.forward(100)

forward(100)
```

This little program will create a clone of the turtle, which starts right where the old turtle was at the time you
clone it.  The clone (`t2`) will change color to red, turn left, and draw a line stright up.  Then the original turtle,
still black, will draw a line going right starting at the original position (since it hasn't moved yet).

You can create multiple turtles to do different parts of the hangman program.   One turtle might draw the hangman stick
figure.  Another turtle might be responsible for drawing the letters of the word.   Yet a third turtle might write out
the incorrectly guessed letters?   Its up to you how you use this, but be creative.

### Use code you've written before

You've done a lot of programming already in this class.  Use that!   If you've already written code to draw a smiley
face for a previous lab or studio, then go find that code and modify it.  If you've already written code to ask for user
input, go look it up and use it.   There is no reason to write things from scratch when you've already written a lot of
code.  

### Use code you've read before

Likewise, it is also a good thing to use code that you didn't write, but you have read or seen elsewhere.  Also, if you
feel like someone has already written code to do something, they probably have.  Google around and see if you can find
it. 

The only catch with using code you didn't write is that you should read it and try to understand it (like you did in the
lab this week).  If you don't understand how the code works, then it will be difficult to use it correctly and make it
work in your program.

There is a function in [exercise 4](https://gitlab.msu.edu/mi-250/reading-code/blob/master/ex4.py) from this
week's lab that might be very useful in finding where a letter appears in a word.  It is called `letter_places()`.  If
you give it a string, and then a letter, it will return a list of all of the places in the string that letter appears.   

Try it!  Copy-and-paste that function into a new python program, and then add code to call it and see what happens.  if
you say `letter_places("hangman", "a")`, what does it print out?   If you instead ask for `letter_places("hangman",
"q")`, what happens?

### Store the answer

The hardest part of today's studio is having your program keep track of the word as the user makes guesses. The easiest
way to do this is using a list.  What I recommend is creating a list of letters, and as the user guesses letters, then
you can fill in the correct letters in the right spaces.  That is, we will start with a list of blanks (spaces), and
each time the user guesses a letter correctly, we will replace the space with the correct letter.

To do this, we should start out by creating a variable (which I call `in_progress`) and initializing a list with spaces:
```
solution = "hangman"
num_letters = len(solution)
in_progress = list( '_'*num_letters )
print(in_progress)
```

Now, each time the user makes a guess, we can use the letter places function to figure out which spaces to replace with
the guessed letter:
```
places = letter_places(solution, guess)
if len(places) > 0:			# the guessed letter is at least one place in the solution
	for place in places:
		in_progress[place] = guess

print(in_progress)
```

In the lab this week, you practiced reading and understanding code.  This is
code that you can use. It works, but you'll need to end up modifying it to work
in your program and to work with turtle.  I strongly recommend you read it
first like you did in lab, carefully figuring out what each line does and how
it works.  Then you will be better able to integrate it into your program.


