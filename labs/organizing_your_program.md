---
parent: Week 14
topic: Organizing Your Program
git: https://gitlab.msu.edu/mi-250/organizing-code
nav_exclude: false
visible: true
---

## Organizing your Code

As you begin to write longer and more complex programs, it becomes more important to stay organized as you work.
Earlier in the semester, you would put all of the code in one file, with no line breaks or other ways of organizing the
code.  Today, we are going to practice a few skills that will make it easier to stay organized.

### Exercise 1: Refactoring -- Red stripes

Run the program `refactor.py` in this week's git repository.  It should draw something that resembles a US flag.  The
program is over 250 lines long!  And there is a LOT of repetition in that program.  We can better organize our code in a
way that will make it easier to read, shorter, and work better.   So let's try to do that.  This is called "refactoring"
-- rewriting code so that it does exactly the same thing, but the code is easier to read, makes more sense, and
hopefully will be easier to use in the future.

Start by reading the code in `refactor.py`.  Think about what it does. As you read it, you'll find yourself mentally
organizing the code in your head -- "OK so this part draws the first red stripe.  Then this part moves the turtle down to
the next stripe." and so on.  Pay attention to that. The logical sections that appear in your head should become sections
or functions in the code.

Let's start with those first two blocks of code.  The first block draws a red stripe.  The second block moves the turtle to
be ready to draw the next stripe.  Your exercise is to create functions for those.

Take the code for the red stripe, and put it into a function called `red_stripe()`.  Now go through the code, and every time
it draws a red stripe, replace the the code with a call to the `red_stripe()` function. That is, delete the extra copies
of the current code that draws a red stripe, and replace it with a call to your `res_stripe()` funtion.  There are 7 red
stripes in the US flag, so there should be 7 calls to `red_stripe()`.

### Exercise 1.5: Move Next

Next, look at the 2nd block of code.  It moves the turtle to be ready to draw the next stripe.   Put that code into a
`move_next()` function.  Go through the code and every time it tries to move the turtle for the next stripe, replace it
with `move_next()`.  Since there are 13 stripes in the flag, there should be 13 calls to `move_next()`.

When you run the program, it should still draw exactly the same flag as it did when you began.  But the program should
be much shorter now.

### Exercise 2: Refactoring -- Generalize to stripe()

The first exercise involved copy-and-pasting code into functions, and then calling those functions. This is a really
common part of refactoring, and it is important.  Just giving sections of code a name can make the code easier to read
and understand.

But once you give it a name, you often realize that it can do more than just one thing. We only replaced the red
stripes.  THe program also draws white stripes, with almost exactly the same code. For this exercise, change the
`red_stripe()` function to just be `stripe()`, and add a parameter that allows you to specify what color you want the
stripe to be.   That is, you should be able to say `stripe("red")` or `stripe("white")` to get either a red stripe or a
white stripe.

Now, see if you can replace more of the code with this `stripe()` function.   You should be able to replace all of the
code that draws all 13 stripes with calls to this function.

When you run the program, it should still draw exactly the same flag as it did when you began.

### Exercise 3: Refactoring -- Generalize to colored_rectangle()

OK, we've done a good job of making our program much, much shorter.  It is also easier to read and understand now.
Let's keep going.   We've got a bunch of code that draws a blue box on top of our red-and-white stripes. We could
copy-and-paste this code into a `blue_box()` function.   But, looking at the code, it looks surprisingly similar to the
code for the stripes we had before, doesn't it?  

Let's see if we can add some more parameters to our `stripe()` function to allow us to draw a blue box.  We already can
specify the color of the box.   But right now, `stripe()` always draws a rectangle that is 300 by 10.   Let's add some
more parameters to our `stripe()` function to specify how far across and how far up the rectangle should be.   

ALso, since we are logically changing what this function does, we should also rename the function to better reflect what
it does.  How does the name `colored_rectangle()` sound?  So, we could call `colored_rectangle("red", 300, 10)` to draw
a red strip, and `colored_rectangle("blue", 100, 70)` to draw the blue box.

Modify the flag code to make this happen.

When you run the program, it should still draw exactly the same flag as it did when you began.

### Exercise 4: Refactoring -- Moving helper functions to a module

If you look at your code now, it is really in two parts.  First, there are a couple of helper functions --
`colored_rectangle()` and `move_next()`.  And second, there is the main code, that calls these functions.

Let's move these helper functions to a separate python file.   Create a new file called `flag.py`, and move these two
functions into that new file.  Since you use turtle commands in this file, you will need `from turtle import *` at the
top of the `flag.py` file.

Then, back in your main file, delete these functions.   Instead, you should be able to `import flag`
-- which will import these functions from this "helper" file into your main file for use.   You can then call them by
saying `flag.colored_rectangle()` or `flag.move_next()`. This allows you to separate your code into parts.   The drawing
helper file contains a small set of functions that help out, and then the main file uses those functions, but is much
shorter and easier to read.

When you run the program, it should still draw exactly the same flag as it always did, but now, it should be much easier
to read and modify the program.

*Hint*: If you `import flag`, then you have to say `flag.function()`.   If, instead, you say `from flag import *`, then
you can use the functions directly as `function()`, without having to say `flag.`.  .


## Separating Content and Logic

Next, turn your attention to the program `flashcards.py`.  Run that program.  It should print out a set of questions 
about state capitals, and ask you for the answers.  It will tell you if you get it right, and then at the end tell you
how many you got right.

Let's see if we can refactor this program also.   Read the code in `flashcards.py`.  It is very repetitive, isn't it?
Let's see if we can make it easier to read and understand.

### Exercise 5: Refactoring -- Write a flashcard function

Each of the flashcards has a set of code that displays a prompt and then checks what the user inputs against an answer.
The only thing that varies between flashcards is the prompt, and the correct answer.

Let's refactor this code into a `flashcard()` function.  The function can accept two parameters -- a prompt, and an
expected answer.   Move code for displaying a question, getting the answer from the user, and then checking
to see if it is correct or not into the function.  

Then modify the main part of the program to call the flashcard function 4 times, to ask the same 4 questions as it
currently does.  

When you run the flashcard program, it should look the same to the user as it currently does.

### Exercise 6: Refactoring: Moving the content into a dictionary

Right now, the *content* of the flashcards -- the questions and answers -- is mixed with the *logic* of the
flashcard program.  The logic controls what order the flashcards should be displayed, when the user should be asked for
an answer, what counts as a correct answer, etc.  Mixing the content of the flashcards with the logic of the program
makes it hard to update either.  If you want to add new flashcards, you have to understand how the program works to know
what to change.  If you want to change how the program works, you have to work around all of the content of the
flashcards in doing so.

Let's try to separate the logic of the program from the content in the program.  Let's put all of the content in a
single dictionary, where each key is a prompt for the user, and the value associated with that key is the expected
answer.  This dictionary should be hard-coded at the top of the file, and will contain the same 4 questions as we asked
before. 

Remember that you can hard-code dictionaries:
```
cards = {}
cards['Wyoming'] = 'Cheyenne'
...
```
OR
```
cards = {
	'Wyoming': 'Cheyenne',
	...
	}
```

Once we have the content of the flashcards in a dictionary (which I call `cards`), then we can loop through the
dictionary to display the flashcards -- something like this:
```
for prompt, answer in cards.items():
    flashcard(prompt, answer)
```

When you run the program, it should do the same thing as before. But the content of the flashcards should be in a
dictionary.   If you want to add a new flashcard, you shouldn't have to change the code at all.  Instead, you should
just add a line to the dictionary.  Try this; add one additional flashcard about another state capital to the
dictionary, run the program, and verify that you can add new flashcard content without changing the main code.

*Note*: If a dictionary only contains state names and capitals, then the rest of the prompt needs to be included as part
of the input statement inside `flashcard()`.  Inside an input statement, you can's use comma's like in print, but you
can use `+`:
```
user_entry = input("What is that capital of " + prompt + "? ")
```

*Note 2*: If you want to make it easy for users, make everything lowercase.  You can use `.lower()` on the user's input
to convert it to lowercase.  You'll also want to convert the state names/titles to lowercase with `.lower()`:
```
  if cards['Wyoming'].lower() == user_entry.lower():
```
A good way to remember this is if you are using `.lower()`, then both sides of the equal sign should use `.lower()` so
everything that you are comparing is always lower case.


### Exercise 7: Moving the content into a separate file

The previous exercise talked about separating content and program logic -- but the content is still being specified in a
python dictionary.  That means that to update the list and add new flashcards, whoever is doing that has to understand
the syntax for python dictionaries.   If you are working on a team, some of your teammates (who might be content experts
but not programmers) will find this hard.  Let's make it easier for them.  Let's read in the list of state capitals from
a file, and then generate flashcards from that.  That way, if they want to update it, they can just edit that file and
not have to edit code.

I've put the list of 4 state capitals in a text file called `capitals.txt` in the lab repository.  

You'll also need a function that reads in the state capitals and puts them into a dictionary.  Try to write that code.
But, if you want, you can also look in the file `read_cards.py`.  In it is a function that reads in the state
capitals and returns a dictionary that looks exactly like the one in Exercise 6 -- they key of the dictionary is the
prompt, and the value is the answer.  Copy-and-paste the function into your program.  

Instead of manually specifying the states and capitals in your code, call this function to read in the cards from a
file:
```
cards = read_cards("capitals.txt")
```

This dictionary should basically look exactly the same as the dictionary from Exercise 6.  Except this time, it is being
read in from a file instead of being hard-coded in the python file.

This way, instead of manually specifying flashcards in your program, you fully separate the content and the program
logic.   The program logic is in the `flashcards.py` file, and the content of the flashcards is in the `capitals.txt`
file.  The `flashcards.py` program should still do *exactly* the same thing that it always did, but now, the python file
doesn't actually contain any actual content.

### Exercise 8: Put helper functions in a separate file

The `flashcards.py` program should basically contain two parts -- a couple of helper functions to display a flashcard
and read information from a file, and the main part that loops through the dictionary displaying flashcards and counting
results.  This is a very similar structure to what we had for the `flag.py` program above -- a couple of helper
functions and a main program.   

Let's organize the code the same way we did above.  Put all of the helper functions into a separate file.  Then, in the
main `flashcards.py` file, `import` that other code and use it.


### Exercise 9: Create 50 flashcards for all 50 states

The file `capitals-all.txt` contains the capital cities of all 50 US states, one per line.   Modify your program to test
the user's knowledge of all 50 capital cities, and report whether they get each one right.

If you did this right, this should be REALLY easy -- you should just change the filename that is being read in, and the
program should automatically adjust and handle it correctly.  See how easy it is to add new flashcards once you've
separate content and program logic?

### Exercise 10: Change the flashcards to sports

For the next exercise, let's really push and see how easy it is to add new flashcards. Modify your program to ask the
user which team certain players play for.   Create a new text file that contains a list of player names and the name of
the team that they play for.  Have your flashcard program load in that file instead of the state capitals file.

Hopefully, this should be pretty easy.  You just put the names in a text file, and your same `flashcards.py` program
should work with minimal modifications.   

*Hint*: The file currently contains information in the form `capital, state`.  That is, the answer is first, followed by
a comma, then the question.   If you want to change that to something else, then it is a good idea to maintain the same
`answer, question` format.

### Challenge 1: More Refactoring of the flag

The code in the first two files (`flag.py`) still seems to contain a bunch of redundancy and repetition.  Are there
other ways that you can continue to refactor the code?  Can you create additional helper functions in `flag.py`?   Can
you move things to `for` loops to make it clearer and easier?   Should `move_next()` be called at the end of
`colored_rectangle()`?  Or maybe, we should create a `stripe()` function that calls both `colored_rectangle()` and
`move_next()`?  What do you think would be the easiest-to-understand way of organizing the code?

### Challenge 2: Randomize the order of the flashcards

Now that we've separated the content from the program logic, it is also easier to make changes to the program logic.
Modify your program to randomize the order that it asks users the flashcards.

Verify that it works by using it with the 50 state capitals, and with your sports players file.

*Hint*: `cards.keys()` will give you a list of all of the prompts. Once you have a list, you can use `random.shuffle()`
on that list to reorder that list into a random order.   You can then use a `for` loop to loop through that new order of prompts.
Given a prompt, you can use `cards[prompt]` to figure out the expected answer.

### Challenge 3: Refactoring -- Handling the count correctly

Now that we have moved the question-and-answer code into a `flashcard()` function, we need to create a way for the
function to tell the main code whether the person got it right.   Really, though, all the main code cares about is *how
many* the user got right.  And since the `flashcard()` function only asks one question, for that function, the answer is
either `0` or `1`.  Let's have the `flashcard()` function return either a 0 or a 1 to indicate whether the user got it
right.  Then the main code can add up the number of 1's to figure out the total, like this:

```
count_right = 0
count_right += flashcard("What is the capital of North Dakota? ", "Bismark")
count_right += flashcard("What is the capital of Wyoming? ", "Cheyenne")
...
```

See if you can use this to add functionality that counts how many the user gets right. And it should also print out the
number correct at the end of the flashcards. 

*Hint*: You can use `len(cards)` to get the total number of entries in a dictionary.

