---
parent: Week 2
topic: Control Flow
git: https://gitlab.msu.edu/mi-250/control-flow
nav_order: 3
visible: true
---

The first thing you need to do today is to create a copy of the files you'll need for the lab.   These files are in the
git repository listed above. 

Most of the labs in the class build on the previous labs. Last week, we learned how to download files from a git
repository. Rather than repeat the instructions here (and every week going forward), I'm just reminding you that you can
go to [Lab 0]({% link labs/installing_python.md %}) to find more instructions for downloading files from GitLab.  Note that this weeks files
are in a different repository on GitLab; that is, the link for this week above is different than the link for last week.

Once you get the repository, you should see these files:
* README.md
* hello.py
* mad-libs.py
* mad-libs-input.py
* avengers.py

The goal of these labs is *practice* -- we will be going through a series of challenges and exercises to try to practice
usign the skills you learned during the reading and videos from this week.  We will practice skills over and over

As you finish a couple of exercises, ask the professor or TA to come over and look at your solution.

Also, since today is a lab, remember that we doing pair programming today.  Always work in pairs, with two
people using one computer.  Every 20 minutes or so I will announce that it is time to swap roles.

# Print -- our first program 

The first program that almost everyone writes is called "Hello World".   The idea is to create a program that
communicates with a user by giving them a simple piece of information -- in this case, it says hello.

I've already written a simple version of this program, and its called "hello.py".  The first step is to run this
program using `python` on Windows or `python3` on Mac:

Windows users:
```
python hello.py
```

Mac users:
```
python3 hello.py
```

Now, we are going to practice modifying this program. Last week, we opened program files in a text editor, edited them,
and then ran them on the command line.  We are going to do that again this week; however, this week we are going to be
making more careful edits that do more than we did last week.

### Exercise 1: Say hello to someone

The first challenge is to have the program, when you run it, say hello to a specific person -- the person who is
navigator.  To do this, you want to put the navigator's name into the print statement.  

So, if the navigator's name is Andrea Jones, then the program should print out
```
Hello Andrea Jones
```

### Exercise 2: Add more information

The second challenge is to have this program print out some additional information.  To do this, you'll need to add
additional print statements. Each print statement prints out one line of output.  You want the program to introduce
yourself (the driver) to the navigator, so that when the navigator runs the program, they learn more about the driver.
So, for example, the program could output something like

```
Hello Andrea Jones
I am Rick Wash
and I am a sophomore media and information major.

I enjoy helping people use technology, 
I hope to become a user experience professional when I graduate.
```

To do this, go back to the readings and videos from this week to remind yourself about print statements and how to use
them.  Make sure that all of this information is not on one line, but instead appears on multiple different lines.
Also remember that you can print a blank line using `print("")`.


# Variables -- storing information for later use

Now that we've had a chance to practice printing out information, let's use variables to change up what we are
displaying.  To do this, we need to put information into a variable, and then use the print commands to print out
information that fills in blanks with the contents of a variable.

We will start with the file `mad-libs.py`.   The first thing you should do is to run the program.  What does it print
out?

### Exercise 3: Words

Now open up the file, and notice that at the top of the file, there are some variables.  The name of each variable is a
prompt, like "verb" or "action". Ask the navigator to come up with new words by reading the prompts and filling in the
words the navigator comes up with.  

Run the program again, and notice what changed.  Why did that happen?

Notice what running the program does -- it stores specific words (in `""` quotes) into variables like `body_part` and
`action`.  Then, when it prints out, instead of print out the word `action`, it prints out whatever is stored in the
variable named `action`.  This is how variables work -- you store something in them, and then python will substitute
whatever is stored in them as it runs.

### Exercise 4: New Mad-libs

Pick a new movie quote.  It can be from any movie you want, though if you like the Guardians of the Galaxy theme, here
are some of the [memorable quotes](https://www.cbr.com/guardians-galaxy-mcu-best-quotes/).  Add a new print
statement that prints out the quote.  Then choose a word to replace, and create a variable to hold the word that
replaces it. Try to get it so that you can change the value of the variable at the top of the file, and it will change
what is printed out.


# Getting input from users

So far, the programs that we have created just do one thing.  Every time we run the program, it does the same thing.
That's not a bad thing -- some of the most interesting programs do the same thing every time it is run (like calculate
tomorrows weather, or figure out a prediction, or rendering a 3D movie).  But the most interesting programs are
interactive -- they ask the user for input, and then change what they do based on what the user does.

Up to this point, the way you made the program do something different was to edit the program.  That is, you were both
being the programmer (who edits the program) and the user (who tells the program what to do).  Starting now, we are
going to separate those roles.   You will write a program that asks the user -- which may be you, or it may be other
people -- for input.  Then the program will do interesting things with that user input.  What this means is that,
starting now, we are going to be writing programs that are not just for ourselves, but that can also be used by other
people for their own purposes.  This is one of the most interesting and exciting parts of programming -- that other
people can take your program and do interesting things with it.

Today, we are going to begin with the simplest way to get user input -- through the keyboard using `input()`.

First, notice that there is a second mad-libs file, `mad-libs-input.py`.   Run that program using `python
mad-libs-input.py`.  Ask the navigator for words based on the prompts, and enter them into the program as it runs.
Then observe what comes out.  That's a simple interactive program that asks for input (words), and then changes what it
says based on what the user inputs.  

Next, run it again, and type in different things.  What happens?

### Exercise 5: Update the Mad-Lib

The original source of that mad-lib is the song "Down Under" by Men at Work.  Its an old song from the 80's.
Since I'm old, I like that kind of music.  You might too, or you might not, and that's OK.  For this
challenge, change the mad-lib.  Pick a different song that YOU like, and use that song to create the mad-lib.  Feel free
to edit this file; you don't need to create a whole new program.

Your new mad-lib should ask the user for new types of words.  They should be words that fit into the song you choose,
not the types of words that I asked for.  Take what the user enters, and have the program store them into variables.
Then print out the lyrics to your song, replacing key words with words that the user input.

Notice how you store things.  The code says `variable = input(...)`.   You pick a variable and put it on the left side
of the equals. Then you put what you want to put into the variable on the right side.  Previously, we put actual words in
quotation marks -- the quotation marks tell python that we mean those actual words.   In this program, instead of
putting quotation marks, we use the command `input(...)` to get input from the user.  It prints out whatever we tell it
to, and then waits for the user to type in something.  Whatever the user types in, it stores into the variable we put on
the left of the input.

(Question: What happens if you put the `input(...)` command, but don't include `variable =` before it?   Answer: It asks
the user for input, but then the program immediately forgets what the user typed because it didn't have anywhere to put
it.)

*Note*: The code for your program -- the file you edit in your text editor -- should not have the actual words in it like it did in
exercise 4.  Instead, it should just contain instructions to ask the user for words.  That's what programming is --
giving the computer instructions for what to do.


# Not always doing the same thing

Next, we will work on basic conditionals -- using an `if` statement to cause different things to happen in different situations.

To begin, let's run the Avengers program:

```
python avengers.py
```

Now go through and read the source code to the Avengers program. Notice that when you run the program, not every line in
the source code gets printed out; instead, it depends on what the user of the program types in.  Pay particular
attention to how things are indented.  Indentation is really important in python.  Indentation controls which lines are
part of the `if` statement and which ones are not.

### Exercise 6: Try different inputs

Run the avengers program multiple times.  Give different answers to the prompts.  Try out all three avengers as an
answer to the first prompt. What happens?

Now look at the code.  Why is that happening?

Also, as you tried things, did anything not work as you expected?  Make a list of 'bugs' -- problems with the program
where it doesn't work the way you expect it to.


### Exercise 7: What Happens when Captain America tries?

Your next challenge is to modify the code.  What happens when Captain America tries to pick up the hammer?  Put some
print statements in the right place to tell the story of what happens when Captain America tries to pick up the hammer.

### Exercise 8: Lowercase

Right now, if you type in Thor's name or Iron Man's name, it works even if you don't capitalize their names.  But
Captain America's name has to be capitalized.  Modify the code so that you can use lowercase to type in captain
america's name.

### Exercise 9: Nicknames

What happens if you just type in "cap" instead of "captain america"?  It doesn't work right.  Let's fix that.  Make it
so that you can enter in nicknames like "cap" or "tony" and it'll still work.


### Exercise 10: Black Widow

Black Widow was also hanging out with the rest of her team.  Let's add her in to the story.  Create a new branch where
she tries to lift the hammer, and print out what happens when she tries.


# Extras

If you finish all of the exercises and want to continue practicing these programming skills, then here are a couple of
extra exercises you can try:

### Exercise: Two-part Mad-libs

Take the mad-libs program that you worked on, and create a second part of the mad-libs.  So you input a bunch of words,
nad it prints out part of a story / song / something.  Then you get a chance to input more words, and it prints out the
second half. You've already got a first half of the mad-libs program written.  Add a second half to your mad-libs program.

### Exercise: Avengers Mad-Libs

Turn the avengers story into mad-libs.  Replace some of the words with variables, and then fill in the variables at the
beginning of the program with funny words.

### Exercise: Avengers bug-list

As part of challenge 6, you made a list of bugs.  Try this again; run the program over and over and try out different
inputs, and see what happens.  Make a list of each input, what you expect to happen, and what actually happens.
Any time what actually happens is different than what you expect, you've found a bug!   The goal here is just to make a
list of bugs in the program.

### Exercise: Avengers bug-fixing

Don't do this until finishing making the bug list.  Go through your list of avengers bugs, and try to fix them.  How do
you get it to do the right thing in all of those situations?


## Solutions

My solutions to the lab will be posted to the Gitlab page 10 minutes before the end of the class.  Looking at them will
let you see how someone else (your instructor) solved the exercises.   It is OK if you didn't do it exactly the same way
I did; that's normal.  The important part is that it works.  If you weren't able to get something working after spending
the lab period on it, then looking at the solutions will be a good way to expand your knowledge.
