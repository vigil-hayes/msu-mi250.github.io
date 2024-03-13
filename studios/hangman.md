---
parent: Week 9
topic: Hangman
nav_exclude: false
visible: true
---

For the studio today, you are going to make a [hangman game](https://en.wikipedia.org/wiki/Hangman_(game)). The game works like this:

The game chooses a secret word, and displays a number of blanks indicating how many letters that word has. The player then has to guess the letters in the word. If the player guesses a letter correctly, the game fills in the letter in all places in that word that it appears.   If the player guesses a letter that is not in the word, then the game draws the next line in a stick figure (drawn with Turtle). The player wins if she or he guesses all of the letters in the word before the stick figure is completed. The player loses if they guess incorrectly so many times that the stick figure is fully drawn.

As per usual, work in groups of 2-3 and store your code in Gitlab.

## Advice

What follows is some advice for building this program. You don't have to follow my advice; do whatever you want.

### Choose a drawing that works in pieces

The traditional hangman game uses a stick figure in a noose. That's pretty morbid, though, and I'd encourage you to choose something else to draw. Look at the Turtle drawings you've done for past studios and labs in this class - could any of them be adapted for use in the game? Keep in mind that a good drawing for this game should do these things:

* *can be split up into pieces so that each piece can be drawn separately to make up parts of the whole.* The stick figure traditionally used in hangman has 6-7 pieces that can each be drawn separately. Having fewer pieces makes the game harder; more pieces makes the game easier.
* *uses color smartly (or sparingly).* Remember if you want to fill a shape with color, you have to draw the entire shape first. That means if you have a drawing you want to use but it uses a color fill, you might not be able to use color when you split up the drawing into pieces. You can either plan to fill the color in at the end, or not use color, or only use an outline color (`pen_color()`).

### Use functions structure your program

The program you write for this will likely have many pieces: the piece that takes user input and checks if a letter is in the word or not and the various pieces that draw different things in Turtle at different times. 

It might make sense to use a function for each "piece" of the Turtle drawing you need to make for the game. The piece of the drawing that happens after the first wrong guess could be one function, and the second piece could be the next function. The piece that draws a correct letter in a specific place on the Turtle screen could be another function. There are lots of ways to do it. But thinking of what all of the different "pieces" of the program are can help you figure out what functions you might want to have.

### Use modules to make teamwork easier

Modules allow you to more easily spread out the work amongst team members and combine code. For this studio, for example, it might make sense for 1-2 people to work on the drawings, and another 1-2 people work on the code that runs the guessing game. Each function you use in Turtle can be stored in one or more helper files and then imported into the main file that runs the code. 

You don't have to use modules for this, but it would be a good chance to practice. Note that if everyone is working in different files, you'll be less likely to run into Git conflicts. Remember to push your code to the Git repo frequently so your teammates can make use of your code. And remember to use `git pull` before you push so you always have the latest code on your computer first.

### Use multiple turtles

In [last week's studio]({% link studios/structured_UI.md %}), there were instructions for making a second turtle. This feature of turtle might be helpful here, too! You could, for example, use one turtle to draw the image and another to write out the correctly guessed letters. Note you can make as many turtles as you want. 

## If you get stuck

The hardest part of today's studio is having your program keep track of the user's progress in the game. Below is a brief solution for the code that will keep track of whether the user's guess is in the word they're trying to guess. I'd recommend trying to figure it out with your group first, and only looking at this solution if you get stuck. There are lots of ways to do this piece of the game using Python; my solution is only one possible way. You might have a better solution, or a solution that makes more sense to you.

### Storing the user's guesses

The easiest way to do this is using a list. What I recommend is creating a list of placeholders that's as long as the word the user is trying to guess, and as the user guesses letters, then you can fill in the correct letters in the right places in the list. So the list would start out looking like this:

```
['_', '_', '_', '_', '_', '_', '_']
```
Then say the second letter in the word is e. When the users guesses e, the list would change to look like this:

```
['_', 'e', '_', '_', '_', '_', '_']
```

To do this, we can start out by creating a variable to store the word the user will try to guess, and then creating a list of placeholders that's the same length as the word:

```python
word = "decorum"   
guess_list = list('_'*len(word)) 
```   

Now, we can write some code that collects user input, checks if the letter the user guessed is in the word, and if it is, then replace the placeholder in `guess_list` with the letter.

```python
guess = input("What letter do you guess? ")
index_counter = 0  
if guess in word:           
	for letter in word:             # iterates through each letter in the word
		if guess == word[index_counter]:        # if the letter matches the user's guess, finds the corresponding index number
			guess_list[index_counter] = guess   # replaces the blank with the guessed letter in guess_list by finding the matching index number
		index_counter += 1
```

You'll want to add some more code to this, of course - code that will write out the correctly guessed letter in Turtle, code that will draw part of the image if the guess is incorrect, a loop so that the user can keep entering guesses, something that breaks the loop if the user has correctly guessed all the letters OR the full picture is drawn, etc.
