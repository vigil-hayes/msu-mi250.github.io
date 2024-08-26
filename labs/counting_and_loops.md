---
parent: Week 4
topic: Counting and Loops 
git: https://gitlab.msu.edu/mi-250/counting-and-loops
nav_exclude: true
visible: false
---

For this lab, we are going to use a Git repository like we did for last week. The first thing you should do is fork this week's GitLab project (linked above). Only one person needs to create a forked project. Once forked, add your partner to the project (and Caitlin and Jack), and then clone the repository onto your computer. Check out the [Git reference]({% link reference/using_git.md %}) for a reminder on how to do this.

{% capture _ %}{% increment exercise3 %}{% endcapture %}

## Counting in a loop

### Exercise {% increment exercise3 %}: Count

As an example of how to do loops, look at the file `counter.py` in the Git repository. The program is supposed to count to 5. 

Run the program to see what it does. Then open the file and look at the code. How does it work? Read the code and see if you can figure out how this program works. Does it do anything you're not expecting?

Edit the program so that it counts to 5 the way a person would count (that is, starting at 1).

*Hint:* When Python counts using numbers, it starts at 0 by default.

*Hint 2:* There are multiple ways to do this. One way is to use an increment, another is to modify the range. `range()` can take more than one value at once! Check out this week's [readings]({% link readings/loops.md %}) for more detail.

### Exercise {% increment exercise3 %}: Print a random number

Right now when you run `counter.py`, it only counts to 5. It counts to 5 every single time. Let's give it a random number to count to instead.

First, let's test out the random module by printing some random numbers outside of the for loop. We have to tell Python we're using the module first, though. Do this by adding `import random` at the top of the `counter.py` program, above the for loop.

Let's generate a random number and print it out (outside of the for loop!) so we know it's working. Try putting `random.random()` inside of a print statement: this will print out a number between 0 and 1. Run the program a few times and you'll notice the number changing. The first number I got when I ran it was `0.4094163341030903`. The numbers you get will be different.

That's cool, but `counter.py` only works well with whole numbers. You can use `random.randint(x,y)` to generate a whole number inside of a range of numbers, where x is the smallest number and y is the biggest. Try generating a number between 1 and 10 and print it out. Run the program a few times to make sure it's giving you different numbers.

*Note:* the for loop will still be running whenever you run the program. The first number that prints out when you run it will be the random number.

### Exercise {% increment exercise3 %}: Count to a random number

The for loop is still running, and still only counts to 5. Let's make it count to a random number instead.

You're already generating a random whole number, but you're only printing it out. Let's add it to the for loop so that instead of running 5 times, it will run a random number of times. You can do this by storing the random number in a variable called `count` and then using the variable inside of `range()` in the for loop.

*Note:* You can get this to work without using a variable at all, but it's good practice to store values in variables before using them in other functions, like `print()` or `range()`. You'll see why in the next exercise!

### Exercise {% increment exercise3 %}: Add some text

The program only spits out a bunch of numbers. Let's make it a little more user friendly by adding some text to tell the person running it what it's doing. Print out a line of text that says `The program is counting to X`, but replace `X` with the random number you're generating.

*Hint:* This should be easy to do if you stored your random number in a variable! Look at `mad-libs.py` from [the Control Flow lab]({% link labs/control_flow.md %}) if you can't remember how to use a variable inside of a print statement that already has other text in it.

*Hint 2:* You'll need to figure out where the best place is to put this print statement. Should it be before the loop, after the loop, or inside of it? Do what you think will make the most sense to a user who is running the program.

## Change places with Git

Now is a good time to save your changes to Git and trade driver positions with your partner. The old driver should add, commit, and push their code, and then make sure their changes show up in GitLab. The new driver should use `git pull` to pull the changes their partner made down to their computer. For a refresher, see [Using Git]({% link reference/using_git.md %}) in the reference section on the course site.

## Singing a song

### Exercise {% increment exercise3 %}: Looping verses

If you run the program `bottles.py` in the git repository, it will print out the first verse of the song [99 bottles](https://en.wikipedia.org/wiki/99_Bottles_of_Beer){:target="_blank"}. 

Let's start small! Modify the program so it repeats the verse 5 times. Don't worry about number of bottles in each verse just yet; just get the loop working. Your code should only be 5 lines in total.

*Hint:* `range(5)` will count from 0 to 4. It always stops just before it gets to the end number. `range(1, 5)` will count starting at 1, so will count from 1 to 4. `range(5, 1, -1)` will count by `-1`, so it will count backwards from 5 down to 1.

*Hint 2:* Python using indentation to figure out which blocks of code belong together. Code that runs inside a loop in Python means the code that will loop will start on the line underneath the loop statement *and* will be indented.

```python
for i in range(x):  # this is the loop statement
    print(i) # code here will repeat with each loop - notice how it's indented
print("This is outside of the loop") # this code will NOT repeat because it's not indented
```

### Exercise {% increment exercise3 %}: Make the number of bottles go down

Now modify the code so that the number of bottles counts down with each verse, like in the song.

*Hint*: A `for` loop uses a variable. In `for i in range(10)`, the `i` is a variable. You can use that variable inside the loop. Each time through the loop, the `for` loop fills in that variable with the current number.  So the first time through the loop, `i` is 0; the second time, it is 1, the third time is 2, and so on. `i` will have different start and end points depending on what you include in `range()`.

### Exercise {% increment exercise3 %}: All the verses

Now modify the program to print out all 100 verses of the song. The last verse should have 0 bottles in the last line.  

At this point, your program should still only have 5 lines of code!

### Exercise {% increment exercise3 %}: Change the final verse

Modify your program to change the final verse of the song. Rather than singing zero, have it sing a different ending. For example, here is one alternative ending to the song:
```
No more bottles of beer on the wall,  
no more bottles of beer.  
We've taken them down and passed them around;  
now we're drunk and passed out!
```
Feel free to write your own lyrics for the last verse!

*Hint*: There are multiple ways to do this, and none of them is wrong. A question to ask: should the new verse be inside of the loop or outside?

### Exercise {% increment exercise3 %}: Change the 6th-to-last verse

There is an alternative way to sing the 99 bottles song, where the 3rd line is replaced with:
```
If one of those bottles should happen to fall,  
98 bottles of beer on the wall...
```

Modify your program so that the 6th-to-last verse ("5 bottles") uses this alternative line instead of the normal line. 

*Hint*: You can use an `if` statement inside the loop to check which loop you are on, and print out something different if you are on a specific loop.

## Change places with Git

This is another good time to save your changes to Git and trade driver positions with your partner. The old driver should add, commit, and push their code, and then make sure their changes show up in GitLab. The new driver should use `git pull` to pull the changes their partner made down to their computer. For a refresher, see [Using Git]({% link reference/using_git.md %}) in the reference section on the course site.

## Guessing game

For loops are great if you want a loop to run a set number of times, and to stop once that number is reached. They're not so great if you want a loop to keep running for some undefined amount of time -- usually until something specific happens. That's where while loops come in.

### Exercise {% increment exercise3 %}: Play a guessing game

Run `question.py`. Right now, it asks one question, then tells you if you're right or wrong. Let's change the program so it keeps asking the question until the user gets it right. You can do this with a while loop.

There are two parts to a while loop: the condition that makes the loop run, and the condition that causes the loop to end.

The most basic while loop starts with `while True:` -- everything inside of it will keep running until it reaches a condition which causes the loop to end. The `True` part of it means everything in the loop is true, until proven false (that is, until it breaks!). Remember: Python sees code as being *inside* of other code by looking at how the code is indented.

The other piece the loop needs to have is a condition in it that causes it to end. **Important:** The keyword `break` is used to signal that the loop should end. If you don't break a while loop somewhere, it will keep running forever!

A basic while loop looks something like this:
```
while True:
    stuff to repeat
    if <condition to be met>:
        break
```

Set up `question.py` so it keeps asking the question, and then end the loop with `break` when the question is answered correctly.

### Exercise {% increment exercise3 %}: Ask a different question

Change the question and the answer to something interesting about yourself. My example of my favorite color is very boring. I'm sure you can come up with a more interesting fact about yourself than that.

### Exercise {% increment exercise3 %}: Ask another question

Ask a second question. Once the user has succesfully answered the first question, the program should start asking the second question.

*Hint:* You'll need a second loop for this!

### Git

At this point, you should have modified versions of all 3 programs for this lab. Make sure all of the modifications you've made on your own computers are pushed to your Gitlab repository! This is how you're turning your code in for this lab, and for all future labs.

## Challenges

If you finish the lab before the end of class, please try to do at least one of the challenges. If you can get one or more of the challenges working correctly, then you can leave class early. Check in with Caitlin or Jack first before you leave.

{% capture _ %}{% increment challenge3 %}{% endcapture %}

### Challenge {% increment challenge3 %}: Alternate lines

Modify your bottles program so that every other line uses the alternative version. So the first verse should say `take one down, pass it around`, the second verse should say `if one of those bottles should happen to fall`; the third verse should say `take one down, pass it around`, and so on.

*Hint*: Python has a modulus operator: `%`. Modulus finds the remainder after division. So `13 % 5` is equal to 3, since when you divide 13 by 5 ,you get 2 with a remainder of 3. You can use this to figure out if a number is even or odd: if the line number divided by 2 has a remainder of 0, then it is an even number. If the line number divided by 2 has a remainder of 1, then it is an odd number.

### Challenge {% increment challenge3 %}: Random number of bottles

Use the `random` module to make the song start at a random number of bottles rather than at 100. When you do this, think about practicalities - you need the number it generates to be a whole number, but don't want it to be too many digits or else your program will take forever to run. Remember to include `import random` at the top of the program!

### Challenge {% increment challenge3 %}: Limited tries

In `question.py`, change the code so it only lets the user try to answer the first question 3 times before it moves onto the next question. 

How would you do this with a while loop? (hint: there are examples in this week's reading on loops.) How would you do it with a for loop? Bonus: use a while loop for the first question, and a for loop for the second question.

Remember the loop still needs to end immediately if the user guesses the answer correctly.

### Challenge {% increment challenge3 %}: Random guessing game

Make a guessing game that generates a random number and then asks the user to guess the number. It should work similarly to `question.py` in that it keeps asking the user to guess until the user gives the correct answer. Make it user friendly, too - print out some introductory text to introduce the user to the game and describe how to play. Remember to include `import random` at the top of the program!

I recommend making a new file and calling it `random-guess.py` for this challenge. Make sure to save the file in the same folder as your other code for this lab. Some of the code you wrote in `question.py` and `counter.py` might be helpful to copy+paste into the new file as you write the program. 





