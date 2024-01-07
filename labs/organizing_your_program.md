---
parent: Week 9
topic: Organizing Your Program
git: https://gitlab.msu.edu/mi-250/organizing-code
nav_exclude: true
visible: false
---

{% capture _ %}{% increment exercise88 %}{% endcapture %}

## Functions and modules

Modules are a way to separate different parts of code into different files so that the code is more organized and easier to read. We've been using modules all semester - `random` is a module, as is `turtle`. These modules contain functions that you can import into your program so that you can use them.

### Exercise {% increment exercise88 %}: Separating functions from running code

Open up `cards.py`. You may recognize this program - we used it in the [functions lab]({% link labs/drawing_with_functions.md %}) a couple weeks ago.

Right now everything is in one program, and the program is over 100 lines long. Most of the code consists of the functions that create the different playing card symbols; there are only a few lines of code at the bottom of the program that actually run when you run the program.

Modules allow you to separate the code that is actually running from the functions that define how the code will be run. 

Create a new file called `card_functions.py`. Move all four of the functions that define how the card symbols should be drawn into this new file. Make sure to include `from turtle import *` at the top of `card_functions.py`.

Now `cards.py` should only have a few lines of code left it in. We'll need to add one more line of code to `cards.py` - the command that imports the card functions from `card_functions.py`.

There are two ways to import functions from another file: we've been using both methods.

```
import random
random.randint()
```

This method imports functions from the `random` module. In order to use functions like `randint()` and `choice()`, you need to put `random.` in front of them.

The other method is the one we've been using to import Turtle functions:

```
from turtle import *
forward(10)
```

This method imports all of the functions from the `turtle` module so that they can be used 'natively' inside a program. That means you don't have to add `turtle.` in front of every Turtle function you want to use.

Use one of the above methods to import the card functions in `card_functions.py` into `card.py`. The name of the module you import is the same as the name of the file (for this exercise, you'll be importing `card_functions`).

*Note:* It's best practice in Python (and many other programming languages) to separate words in the names of variables, functions, files, or anything else you're naming with underscores: `_`. Python sometimes has trouble with hyphens (`-`) because they're used for math (minus sign), but never has trouble with underscores.

### Exercise {% increment exercise88 %}: Add another function

Right now the program draws a spade, then moves, then draws a heart, then moves, etc. The code that moves the turtle in between each symbol is repetitive, though.

Make a new function called `move_next()` that moves the turtle in between each symbol and replace the repetitive code with calls to the function. Put this function in the `card_functions.py` file.

The program should run in exactly the same way as it did before, but `cards.py` should be shorter.

## Organizing and Refactoring Code

As you begin to write longer and more complex programs, it becomes more important to stay organized as you work. Earlier in the semester, you would put all of the code in one file, with no line breaks or other ways of organizing the code. Today, we are going to practice a few skills that will make it easier to stay organized.

One method is called refactoring - this is when you edit code you've already written to make work better, make it cleaner, or make it more efficient. In professional programming, it's very, very common to spend time refactoring code on a regular basis.

### Exercise {% increment exercise88 %}: Read and comment

Run the program `flag.py` in this week's git repository. It should draw something that resembles a US flag. The program is over 250 lines long! And there is a LOT of repetition in that program. We can better organize our code in a way that will make it easier to read, shorter, and work better.

The first step is to figure out what the code is doing. Start by reading the code in `flag.py`. Think about what it does. As you read it, you'll find yourself mentally organizing the code in your head -- "OK so this part draws the first red stripe. Then this part moves the turtle down to
the next stripe." and so on. Pay attention to that. The logical sections that appear in your head should become sections or functions in the code.

As you read through the code and figure out what each section of it does, write comments describing each code section. In Python, commented lines start with `#`. I've added a few comments at the beginning of the program as an example.

### Exercise {% increment exercise88 %}: Red stripes

Now that you've commented the code, you'll notice that you probably used the same comments multiple times. When a chunk of code does the same thing as another chunk of code, that's a good time to use a function.

Take the code for the red stripe, and put it into a function called `red_stripe()`. Now go through the code, and every time it draws a red stripe, replace the the code with a call to the `red_stripe()` function. That is, delete the extra copies of the current code that draws a red stripe, and replace it with a call to your `res_stripe()` funtion.  There are 7 red stripes in the US flag, so there should be 7 calls to `red_stripe()` in the program when you're done.

### Exercise {% increment exercise88 %}: Move Next

Next, look at the 2nd block of code. It moves the turtle to be ready to draw the next stripe. Put that code into a `move_next()` function. Go through the code and every time it tries to move the turtle for the next stripe, replace it with `move_next()`. Since there are 13 stripes in the flag, there should be 13 calls to `move_next()`.

When you run the program, it should still draw exactly the same flag as it did when you began. But the program should be much shorter now.

### Exercise {% increment exercise88 %}: Generalize to stripe()

The first exercise involved copy-and-pasting code into functions, and then calling those functions. This is a really common part of refactoring, and it is important.  Just giving sections of code a name can make the code easier to read and understand.

But once you give it a name, you often realize that it can do more than just one thing. We only replaced the red stripes. The program also draws white stripes, with almost exactly the same code. For this exercise, change the `red_stripe()` function to just be `stripe()`, and add a parameter called `bar_color` that allows you to specify what color you want the stripe to be. That is, you should be able to say `stripe("red")` or `stripe("white")` to get either a red stripe or a white stripe.

Now, see if you can replace more of the code with this `stripe()` function. You should be able to replace all of the code that draws all 13 stripes with calls to the `stripe()`.

When you run the program, it should still draw exactly the same flag as it did when you began.

*Hint:* Remember parameters are variables specific a function that act as placeholders, and then are filled in with whatever is in the paratheses when the function is called. So `bar_color` in the function's code would be replaced with `"white"` or `"red"` when the function is called. If you need a refresher on parameters, go back to the [drawing with functions lab]({% link labs/drawing_with_functions.md %}). 

### Exercise {% increment exercise88 %}: Generalize to colored_rectangle()

OK, we've done a good job of making our program much, much shorter. It is also easier to read and understand now. Let's keep going. We've got a bunch of code that draws a blue box on top of our red-and-white stripes. We could copy-and-paste this code into a `blue_box()` function. But, looking at the code, it looks surprisingly similar to the code for the stripes we had before, doesn't it?  

Let's see if we can add some more parameters to our `stripe()` function to allow us to draw a blue box. We already can specify the color of the box. But right now, `stripe()` always draws a rectangle that is 300 by 10. Let's add some more parameters to our `stripe()` function to specify how wide and how tall the rectangle should be.   

ALso, since we are logically changing what this function does, we should also rename the function to better reflect what it does. How does the name `colored_rectangle()` sound?  So, we could call `colored_rectangle("red", 300, 10)` to draw a red stripe, and `colored_rectangle("blue", 100, 70)` to draw the blue box.

Modify the flag code to make this happen. You'll need to change all of the calls to `stripe()` so that they call the new function instead and use the extra parameters for width and height.

When you run the program, it should still draw exactly the same flag as it did when you began.

### Exercise {% increment exercise88 %}: Moving functions to a module

If you look at your code now, it is really in two parts. First, there are a couple of helper functions -- `colored_rectangle()` and `move_next()`. And second, there is the main code that calls these functions and creates the actual drawing.

Create a new file called `flag_functions.py` and move these two functions into that new file. Remember to add `from turtle import *` at the top of the `flag_functions.py` file. Then add a new import statement at the top of `flag.py` to import `flag_functions`.

When you run the program, it should still draw exactly the same flag as it always did, but now it should be much easier to read and modify the program.

*Hint*: Remember if you decide to use `import functions` instead of `from functions import *` you'll need to refer to the module when you call each function in it, like `functions.move_next()`.

### Exercise {% increment exercise88 %}: Add a star

Write a function to draw a single white star, and draw it on top of the blue box in the flag. But keep your code organized! The function that draws the star shoud go into your functions file (`flag_functions.py`), and the code that actually moves the turtle and creates the star should go in the main program file (`flag.py`).

*Hint:* if you can't remember how to draw a star, go back to the code you wrote for the [functions lab]({% link labs/drawing_with_functions.md %}).

## Separating Logic and Content

Next, turn your attention to the program `flashcards.py`. Run that program. It should prompt you to name the capitols for a series of U.S. states. After each prompt, it will tell you if you got it right or not.

Let's refactor this program. Note that not only is it repetitive, but it also has a lot of hardcoded content - that is, it only tests you on the same four state capitols every time you run it. We'll try to make the program not only more effecient, but also easier to use with different types of content.

### Exercise {% increment exercise88 %}: Write a flashcard function

Each of the flashcards has a set of code that displays a prompt and then checks what the user inputs against a correct answer. The only thing that varies for each flashcard is the prompt and the expected answer. This is the *content* of the program; everything else is the *logic*.

Let's refactor this code into a `flashcard()` function. The function can accept two parameters -- the prompt and an expected answer. Move code for displaying a question, getting the answer from the user, and then checking to see if it is correct or not into the function.  

Then modify the main part of the program to call the flashcard function 4 times and to ask the same 4 questions as it currently does.  

When you run the flashcard program, it should look the same to the user as it currently does.

### Exercise {% increment exercise88 %}: Moving the content into a dictionary

Right now, the *content* of the flashcards -- the prompts and answers -- is hardcoded and is mixed with the *logic* of the flashcard program. The logic controls what order the flashcards should be displayed, when the user should be asked for an answer, what counts as a correct answer, etc. Mixing the content of the flashcards with the logic of the program makes it hard to update either. If you want to add new flashcards, you have to understand how the program works to know what to change. If you want to change how the program works, you have to work around all of the content of the flashcards in doing so.

Let's try to separate the logic of the program from the content in the program. Let's put all of the content in a single dictionary, where each key is a prompt for the user, and the value associated with that key is the expected answer. This dictionary should be hard-coded at the top of the file, and will contain the same 4 prompts and answers that we asked before. 

Remember that you can hard-code dictionaries in two different ways:
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

Once we have the content of the flashcards in a dictionary (which I called `cards`), then we can use a `for` loop to go through the dictionary to display the flashcards using a structure like this:

```
for prompt, answer in cards.items():
    flashcard(prompt, answer)
```

Run the program to make sure it's pulling content from the dictionary. Your program should no longer have any repetitive code in it at this point.

### Exercise {% increment exercise88 %}: Fix the formatting

When you run the program, it should do basically the same thing as before -- give you instructions, then start naming states and expecting the user to type in each state's capitol. Except you may notice that what prints out in the terminal is not as nicely formatted as it was before. It looks like `Montanahelena` once the user types in an answer instead of `Montana: Helena` like it did before.

Let's add back the colon (:) and extra space to the prompt so it looks more user friendly. 

*Hint:* Inside an `input()` statement you can't use commas like in `print()`, but you can use `+` to combine strings together. Using `+` means you need to add spaces into the string manually, though. `user_entry = input(answer + " is correct")` prints out in the terminal as `Helena is correct`, where answer = Helena.

### Exercise {% increment exercise88 %}: Add more content

Now if you want to add a new flashcard, you shouldn't have to change anything except the dictionary. Try this: add two additional flashcards about states and capitols to the dictionary, run the program, and verify that you can add new flashcard content without changing the main code.

There's a text file in the Gitlab repo called `capitols-all.txt` with all of the U.S. states and their capitols in it, for reference.

### Exercise {% increment exercise88 %}: Moving the content into a separate file

So far we've only used modules with functions. But modules can also be used to store content. Create a new file called `capitols.py` and move the dictionary into it. The `instructions` variable also contains content that is specific to this set of flashcards: move that variable into `capitols.py` as well.

Then import `capitols` into `flashcards.py` so that you can continue to use the content.

*Hint:* We've covered two ways to import things from another file: `from filename import *` imports everything from that file so it can be used natively, and `import filename` expects that you refer to the module whenever you call a function from it (like `filename.function()`). Use whichever method makes the most sense to you.

### Exercise {% increment exercise88 %}: Put helper functions in a separate file

Now that we've taken the content out, the `flashcards.py` program should contain two parts: a helper function that makes the flashcard work and the main part that loops through the dictionary to display flashcards.  

Let's organize the code the same way we did above. Put the helper function into a separate file called `flashcard_functions.py`. Then import the functions into the main `flashcards.py` file.

Your flashcard program should now have two import statements, and should only contain a few lines of code: a print statement that prints out the instructions, and the loop that goes through the dictionary.

### Exercise {% increment exercise88 %}: Create a new set of sports flashcards

For the next exercise, let's see how easy it is to use a different set of flashcards with the program. Create a new file called `players.py` and add instructions and a dictionary with the same `prompt: answer` format as the dictionary you created to store states and capitols. This set of flashcards should give the user a player's name and prompt them to say what team the player plays for.

The format of this new file should look very similar to `capitols.py`. I'd even recommend using the same variable names for the instructions and the dictionary. Only the content -- the actual text of the instructions and the contents of the dictionary -- should be different.

Now instead of importing capitols into `flashcards.py`, import `players` instead. If you've set it up correctly, when you run `flashcards.py` it should now be asking sports questions instead of questions about state capitols.

## Challenges

If you finish all of the exercises above before the end of class, try at least one of the challenges below.

### Challenge 1: Draw a different flag with the flag functions

Your flag functions file contains a generalized functions for making a stripe, and more specific functions for making a star and moving the turtle to the next stripe. Create a new program and import the flag functions into it, then use those functions to draw the [flag for Myanmar](https://en.wikipedia.org/wiki/Flag_of_Myanmar){:target="_blank"}. You'll likely need to generalize both your `move_next()` function (perhaps add a parameter to specify how far the turtle should move between stripes) and the `star()` function (add a parameter for size).

### Challenge 2: Randomize the order of the flashcards

Now that we've separated the content from the program logic, it is also easier to make changes to the program logic. Modify your program to randomize the order that it asks users the flashcards.

Verify that it works with both the capitols and the sports content.

*Hint*: `cards.keys()` will give you a list of all of the prompts -- that is, it will convert all of the keys in the dictionary into a list. Once you have a list, you can use `random.shuffle()` on that list to reorder that list into a random order. You can then use a `for` loop to loop through that new order of prompts. Given a prompt, you can use `cards[prompt]` to figure out the expected answer.

### Challenge 3: Count the number of correct flashcards

Add functionality to `flashcards.py` so that it prints out how many flashcards the user got correct at the end of the program. You'll need to modify the `flashcard()` function so that it uses `return` to return information about whether the answer was correct or not. One way to do this is to have the function return 1 for every correct answer and 0 for every incorrect answer, and then add the number it returns to an incrementing counter.

As a very simple example, if `flashcard()` returns 1, then:

```
count_correct = 0
count_correct += flashcard()  # first flashcard
count_correct += flashcard()  # second flashcard
print(count_correct)
```

If the user answer both flashcards correctly, and `flashcard()` returns 1 each time, the print statement will print 2.

*Hint:* you can use `len(cards)` to get the total number of entries in a dictionary.

