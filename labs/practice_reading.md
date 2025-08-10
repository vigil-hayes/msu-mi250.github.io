---
parent: Week 11
topic: Practice Reading Code
git: https://gitlab.msu.edu/mi-250/reading-code
nav_exclude: true
visible: false
---

You have spent almost all of the lab and studio sessions writing code for this class. Writing code is relatively straightforward -- you enter code into the text editor, you run the code, see if it does what you want it to, and then keep editing it until it does. One aspect of this is that you don't always have to really understand what the code is doing -- sometimes you get lucky and it just works.

The goal for today is to practice *reading* code. Reading code is harder than writing code. Reading code requires you to think more carefully about what each line of a program is doing. It requires you to keep track of what is stored in variables, and what variables contain what information. It requires you to think through options for if statements, to try to understand why they are there. You are going to practice reading today, to try to get better at it. Reading code is one of the best ways to become a better programmer, once you have the basics down. But reading code is a skill that requires practice, just like all other skills.

## Instructions

For each of the following exercises, your goals is not to write code. It is to read the code and write comments describing what the code does. You should not need to modify the code the code itself, you will only need to write comments. 

You will use a timer for these exercises: each exercise will ask you to set a time, and then you have that amount of time to try and figure out what the code does before you actually run the program. Only **after** your timer goes off can you run the code to see what it does. I recommend setting a timer on your phone, or typing "Timer" into Google and use the built-in Google time that comes up.

As you work, **think out loud**. You are working with a partner. Think out loud, and work with your partner to try to figure out what the program is doing. You should be spending a LOT of time talking to each other during this lab. One person (the 'driver') should pull up the code on their computer, and then both of you can talk about what it is doing and how it is doing it.

As you figure out what the code does, you will need to add *comments* to the code that describe what is happening. As a reminder, if you put a `#` symbol in the code, python ignores everything that comes after that symbol (which we call a 'comment'). For each line of code, or each small chunk of code, add a comment to that explains what the code is doing. Do this for every piece of code in the program. 

As an example:

```python
# Purpose: this program keeps asking the user if they want to stop, and stops when they say so

while True:                                    # Keep looping forever, until "break"
    answer = input("Do you want to stop? ")    # Ask the user if they want to stop, and store the result in the variable answer
    if answer == "yes":                        # If the word the user enters is "yes", break out of the loop
        break                                  
                                               
print("Done looping!")                         # Print message AFTER loop is broken out of to let the user know the break was successful
```

## Guidelines for this lab

**Check in with Morgan or Shiyu**: Every two to three exercises, before you move on to the next one, ask Morgan or Shiyu to come over and look at your comments to make sure that they aren't missing anything. This is important; often we will ask you questions that reveal that you might not have fully understood the program. You might understand overall what the program does, but may not understand exactly what each line of code does. The goal of today's exercises is to dig into the code so that you understand exactly how it's working.

**Write a "purpose" comment**: At the top of each program, write a comment that explains, at a high level, what the program is doing.

**Write specific comments about variables and functions**: For every variable in the program, you should have at least one comment explaining what the variable is storing (is it a string? a list? a dictionary?) and what it's being used for (what data is it storing and why?). For every function in the program, you should explain what the function is doing and note where it is being called. For functions, also take note of the inputs (the parameters) of the function and the function's outputs (what does it do / what does it return?).

**Look at the order of how the code is run**: Python executes code in a specific order. In simple programs, it executes code from top to bottom. But not all programs are simple. If a function is called at the bottom of a program, for example, the code of the function, which may be in a different place, will run first. If/else statements will also affect the order by skipping some code (for example, if the if statement isn't true). Keep this in mind as you're trying to understand what the code is doing.

**Use print**: After the timer goes off, if you are still trying to figure out what the program does, a good way to do this is to use `print()`.  Add `print()` statements to the program and run it again to print out the contents of variables (or lists or dictionaries) so you can see what is stored in them. This will help you think about what the program does and how it works.

**Use the tools and resources available to you**: You and your partner should try to use what you remember from the class to figure out what the code is doing on your own first, but if you get stuck, there are a lot of tools and resources available to you. Ask your partner, or another pair sitting at your table. Check the Python documentation, or the Turtle documentation. Google it. Use ChatGPT. Ask Morgan or Shiyu.

### Exercise 1

Set your timer for 2 minutes.

Look at the program in `ex1.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.

After your timer goes off, you are allowed to run the program to see what it does.

### Exercise 2

Set your timer for 2 minutes.

Look at the program in `ex2.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.

After your timer goes off, you are allowed to run the program to see what it does.

### Exercise 3

Set your timer for 5 minutes.

Look at the program in `ex3.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.

After your timer goes off, you are allowed to run the program to see what it does.

## Check in

At this point, ask Morgan or Shiyu to check your comments for exercises 1 through 3 before moving on. Switch drivers if you haven't already.

### Exercise 4 

Set your timer for 5 minutes.

Look at the program in `ex4.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.

After your timer goes off, you are allowed to run the program to see what it does.

### Exercise 5

Set your timer for 5 minutes.

Look at the program in `ex5.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.

After your timer goes off, you are allowed to run the program to see what it does.

### Exercise 6

Set your timer for 8 minutes.

Look at the program in `ex6.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.
this program do?

After your timer goes off, you are allowed to run the program to see what it does.

## Check in

At this point, ask Morgan or Shiyu to check your comments for exercises 4 through 6 before moving on. Now is a good time to switch drivers again.

### Exercise 7

Set your timer for 7 minutes.

Look at the program in `ex7.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.
this program do?

After your timer goes off, you are allowed to run the program to see what it does.

### Exercise 8

Set your timer for 10 minutes.

Look at the program in `ex8.py`. Read the code, and write comments for each line or chunk of code as described above. Remember to describe what the program does at the top when you're done.
this program do?

After your timer goes off, you are allowed to run the program to see what it does.

## Check in

At this point, ask Morgan or Shiyu to check your comments for exercises 7 and 8 before you try a challenge.

---

Don't forget to add, commit, and push all of your comments to your git repository.

## Challenges

Please complete at least one challenge before leaving for the day. It is up to you which one you do. Ask Morgan or Shiyu to come over and see the results of your challenge before you leave.

### Challenge 1: Eliza

Also in the git repository for this week is the Eliza program that you ran the very first week of the semester. Do this same code reading exercise on that program: for each line of the program, put a comment next to it describing what that line does and how it works. Pay particular attention to the `responses` variable. What is stored in that variable? It is a list. But a list of what? How does that work? How does it get used?

### Challenge 2: Revisit an old studio

If you and your partner were in different studio groups last week, have one person bring up the code for their group's studio and have the other person read the code and try to figure out what it's doing. The person who *didn't* work on that group's studio last week should be driving. Figure out as much as you can without running the code first.

If you were in the same studio group, or didn't attend last week, find a studio that only one of you worked on.

As you figure out what each piece of code is doing, add comments to it. If you would like to make improvements to the studio while you're attempting to figure out what the code does, that's fine, too!