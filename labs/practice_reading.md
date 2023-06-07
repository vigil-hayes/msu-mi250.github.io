---
parent: Week 10
topic: Practice Reading
git: https://gitlab.msu.edu/mi-250/reading-code
nav_exclude: false
visible: true
---

You have spend almost all of the lab and studio sessions writing code for this class.   Writing code is relatively
straightforward -- you enter code into the text editor, you run the code, see if it does what you want it to, and then
change it until it does.  One aspect of this is that you don't always have to really understand what the code it doing
-- sometimes you get lucky and it just works.

The goal for today is to practice reading code.  Reading code is harder than writing code.  Reading code requires you to
think more carefully about what each line of a program is doing.  It requires you to keep track of what is stored in
variables, and what variables contain what information.  It requires you to think through options for if statements, to
try to understand why they are there.  You are going to practice reading today, to try to get better at doing so.
Reading code is one of the best ways to become a better programmer, once you have the basics down.  But reading code is
a skill that requires practice, just like all other skills.

### Exercise 1: Timer

Start by looking at the file `timer_seconds.py`.  Run it.  What does it do?

Open up the code for `timer_seconds.py` and see how it works.

`time.sleep()` waits a specified number of seconds. So if you say `time.sleep(10)`, it will wait 10 seconds.  If you say
`time.sleep(20)`, it will wait 20 seconds.

If you wanted to wait for minutes instead of seconds, how would you do that?  Think about how you might want to modify
this program if you wanted to ask the user for how many *minutes* the user wants to wait.  Then have the program wait
that many minutes.   Remember, if you have a number of minutes, you can calculate how many seconds that is by
multiplying by 60 (since there are 60 seconds in a minute).

Now look at the program `timer.py`.   Is that how you would have done it?

Check and make sure the timer program works; run it, ask it for a 2 minute timer, wait two minutes, and see if it tells you to
stop at the end of that minute.

## Code Reading

For each of the following exercises, your goals is not to write code.  It is to read the code and write comments.   You
should not need to modify the code at all.  Instead, you will need to read through the code and figure out what it does.  

You are going to use the python timer program on the command line.   For each exercise, I will give you an amount of
time.   Set your timer for that amount of time, and then work on reading the code.  Only **after** your timer goes off
can you run the code to see what it does.   Your first job is to figure out what the code does without running it.
After the timer goes off, run the code, and then go back to the code and use what you now know about the program to try
to figure out how it does it.   

As you work, think out loud.  You are working with a partner.  Think out loud, and work with your partner to try to
figure out what the program is doing.  You should be spending a LOT of time talking to each other during this lab.  One
person (the 'driver') should pull up the code on their computer, and then both of you can talk
about what it is doing and how it is doing it.

As you figure out what the code does, you will need to add *comments* to the code that describe what is happening.  As a
reminder, if you put a `#` symbol in the code, python ignores everything that comes after that symbol (which we call a
'comment').   For each line of code, add a comment to the code that explains what that line is doing. Do this for each
line of code in the program.  You are done with the exercise when you have a comment for every line of code, and also an
comment at the top describing the program as a whole.  Like this:

```python
# Purpose: this program keeps asking the user if they want to stop, and stops when they say so

while True:                                    # Keep looping forever, until "break"
    answer = input("Do you want to stop? ")    # Ask the user if they want to stop, and store the result in answer
    if answer == "yes":                        # Check if what the user typed in is the word "yes", all lowercase
        break                                  # if it is "yes", then break out of the while loop
                                               # End of the loop, go back to the top of the while loop
print("Done looping!")                         # Print message AFTER loop is broken out of to let the user know the break was successful
```

**Important**: As you finish two to three exercises, before you move on to the next one, ask the instructor or TA to come over
and look at your comments to make sure that they aren't missing anything.  This is important; often we will ask you
questions that reveal that you might not have fully understood the program. 

#### Hint: Use print

After the timer goes off, if you are still trying to figure out what the program does, you should use `print()`.  Add
`print()` statements to the program and run it again to print out the contents of variables (or lists or dictionaries)
so you can see what is stored in them.  This will help you think about what the program does and how it works.

### Exercise 2

Set your timer for 2 minutes.

Look at the program in `ex2.py`.   Read the code, and write comments for each line of code as described above.  What
does this program do?

After your timer goes off, you are allowed to run the program to see and help you.  But don't run it before the timer
goes off. Try to read the code and figure out what it does before the timer goes off.

### Exercise 3

Set your timer for 5 minutes

Look at the program in `ex3.py`.  Read the code, and write comments for each line of code as described above.  What does
this program do?

After your timer goes off, you are allowed to run the program to see and help you.  But don't run it before the timer
goes off. Try to read the code and figure out what it does before the timer goes off.

As a reminder, *every* non-blank line of code should have a comment describing what it is doing, and also why that line
is needed as part of the program.

*Once you are finished with exercises 2 and 3, ask the instructor or TA to check your comments before moving on.*

### Exercise 4: 

Set your timer for 5 minutes

Look at the program in `ex4.py`.  Read the code, and write comments for each line of code as described above.  What does
this program do?

After your timer goes off, you are allowed to run the program to see and help you.  But don't run it before the timer
goes off. Try to read the code and figure out what it does before the timer goes off.


### Exercise 5:

Set your timer for 5 minutes

Look at the program in `ex5.py`.  Read the code, and write comments for each line of code as described above.  What does
this program do?

After your timer goes off, you are allowed to run the program to see and help you.  But don't run it before the timer
goes off. Try to read the code and figure out what it does before the timer goes off.

*Once you are finished with exercises 4 and 5, ask the instructor or TA to check your comments before moving on.*

### Exercise 6:

Set your timer for 8 minutes

Look at the program in `ex6.py`.  Read the code, and write comments for each line of code as described above.  What does
this program do?

After your timer goes off, you are allowed to run the program to see and help you.  But don't run it before the timer
goes off. Try to read the code and figure out what it does before the timer goes off.

*Once you are finished, ask the instructor or TA to check your comments before moving on.*

### Exercise 7:

Set your timer for 7 minutes

Look at the program in `ex7.py`.  Read the code, and write comments for each line of code as described above.  What does
this program do?

After your timer goes off, you are allowed to run the program to see and help you.  But don't run it before the timer
goes off. Try to read the code and figure out what it does before the timer goes off.

*Once you are finished, ask the instructor or TA to check your comments before moving on.*

### Exercise 8:

Set your timer for 10 minutes

Look at the program in `ex8.py`.  Read the code, and write comments for each line of code as described above.  What does
this program do?

After your timer goes off, you are allowed to run the program to see and help you.  But don't run it before the timer
goes off. Try to read the code and figure out what it does before the timer goes off.

*Once you are finished, ask the instructor or TA to check your comments before moving on.*

---

Don't forget to add, commit, and push all of your comments to your git repository.

### Challenge: Eliza

Also in the git repository for this week is the Eliza program that you ran the very first week of the semester.  Do this
same code reading exercise on that program: for each line of the program, put a comment next to it describing what that
line does and how it works.   Pay particular attention to the `responses` variable.   What is stored in that variable?
It is a list.  But a list of what?  How does that work?  How does it get used?




