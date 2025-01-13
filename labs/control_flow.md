---
parent: Week 2
topic: Control Flow
git: https://gitlab.msu.edu/mi-250/control-flow
nav_exclude: true
visible: false
layout: studio
---

The first thing you need to do today is to create a copy of the files you'll need for the lab. These files are in the git repository linked above. Last week, you only downloaded one file. This week, download the full repository. Find the download button (next to the blue "Code" button) on the main repository page and choose the ".zip" option. It will download as a .zip folder on your computer.

Once you get the repository on your computer, you may need to unzip it to be able to work with the files inside. On Windows, right click on the file and choose 'Extract All' - this will create a new folder with the same name. On Mac, double click on the folder and it will do the same thing.

You should have a folder named 'control-flow-master' with 5 files in it:
* README.md
* avengers.py
* hello.py
* mad-libs.py
* mad-libs-input.py

The goal of these labs is to *practice*. Each lab will be a series of exercises and challenge to practice the concepts you were introduced to in the readings/videos for the week. You'll continue practicing the concepts from this lab in the studio this week, and in future labs and studios. Many of the concepts build on each other and can be used in combination with one another. 

As with all labs, this lab will be done in pairs. Remember to switch places every so often! Everyone should spend at least part of the class as the driver, and at least part of the class as the navigator.

## Print - outputting information

You learned a bit about the `print` statement in the readings this week. You'll be using it a lot this semester; we'll start practicing now.

### Exercise 1: Hello world 

The first program that almost everyone writes when they're learning how to program is called "Hello World". The idea is to create a program that communicates with a user by giving them a simple piece of information -- in this case, it says hello.

I've already written a simple version of this program, and its called "hello.py". First, run this program in command line with:
```
python hello.py
```

Remember to use `python3` if you're on a Mac! If you need a refresher on running Python programs, go back to [Lab 1]({% link labs/installing_python.md %}).

Open up the `hello.py` in your text editor. What does it look like? What do you think `print` does?

### Exercise 2: Say hello to someone

Next we will practice modifying this program. Last week, we opened program files in a text editor, edited them, and then ran them on the command line. We are going to do that again this week; however, this week we are going to be making more careful edits that do more than we did last week.

Have the program, when you run it, say hello to a specific person -- use the name of the person who is the driver in your pair today. To do this, you want to put the drvier's name into the print statement.  

So if the driver's name is David Bowie, then the program should print out
```
Hello David Bowie
```

### Exercise 3: Add more information

Next, have `hello.py` print out some additional information. To do this, you'll need to add additional print statements. Each print statement prints out one line of output. 

You want the program to introduce the person who is navigating to the driver, so that when the driver runs the program, they learn more about their partner for the lab. So, for example, the program could output something like:

```
Hello David Bowie
I am Ziggy Stardust
and I am a sophomore media and information major.

I enjoy helping people use technology. 
I hope to become a user experience professional when I graduate.
```

You can always go back to the [readings and videos from this week]({% link readings/variables.md %}) to remind yourself about print statements and how to use them. Make sure that all of this information is not on one line, but instead appears on multiple different lines. Also remember that you can print a blank line using `print("")`.

### Change places

Now is a good time to switch places with your partner. Before you do, remember to take a screenshot of `hello.py` with the changes you made running in command line. 

The new driver will need to download the Git repository for today's lab on their computer now - go to the top of this page if you need a refresher on how to do that.

### Exercise 4: New hello program

Make a *new* program called `hello2.py`. You can do this by going to File -> New File in your text editor (Visual Studio Code or similar) and then doing File -> Save As and giving it a name - make sure you add the `.py` at the end of the name so your computer will know it's a Python program.

The file will start out blank - you'll need to add code to it. Write code to introduce the other person in your pair today - they should be the driver now. When you're done, your code should look similar to your partner's edited version of hello.py - it should be a series of `print()` statements which print out information about you when you run the program. Make sure to run the program to test it!

## Variables -- storing information for later use

Now that we've had a chance to practice printing out information, let's use variables to change up what we are displaying. To do this, we will first put pieces of information into variables. Then we'll use the print command to print out information that fills in blanks with the contents of a variable.

We will start with the file `mad-libs.py`. The first thing you should do is to run the program. What does it print out? 

### Exercise 5: Words

Now open up the file, and notice that at the top of the file, there are some variables. The name of each variable is a prompt, like "body_part" or "action". Ask the navigator to come up with new words to respond to the prompts by reading the variable names to them. Replace what's in there now with the new words.

Run the program again, and notice what changed. Why did that happen?

Notice what running the program does -- it stores specific words (in `""` quotes) into variables like `body_part` and `action`.  Then, when it prints out, instead of printing out the word `action`, it prints out whatever is stored in the variable named `action`. This is how variables work -- you store something in them, and then Python will substitute whatever is stored in them as it runs.

### Exercise 6: New Mad-libs

Pick a new movie quote. It can be from any movie you want, though if you like the Guardians of the Galaxy theme, here are some of the [memorable quotes](https://www.imdb.com/title/tt2015381/quotes/){:target="_blank"}. Add a new print statement that prints out the quote. Then choose a word to replace, and create a variable to hold the word that replaces it. Try to get it so that you can change the value of the variable at the top of the file, and it will change what is printed out.

### Change places

This is another good place to switch from driver to navigator, and vice versa. When the next exercise uses a different file, that's often a good time to trade places.

## Getting input from users

So far, every time we run the programs we've worked on, they do the same thing. That's not a bad thing -- some of the most interesting programs do the same thing every time they are run (like display tomorrow's weather, or figure out a prediction, or render a 3D movie). But the most interesting programs are interactive -- they ask the user for input, and then change what they do based on what the user does.

Up to this point, the way you made the program do something different was to edit the program. That is, you were both being the programmer (who edits the program) and the user (who tells the program what to do). Starting now, we are going to separate those roles. You will write a program that asks the user -- which may be you, or it may be other people -- for input. Then the program will do interesting things with that user input. What this means is that, starting now, we are going to be writing programs that are not just for ourselves, but that can also be used by other people for their own purposes. This is one of the most interesting and exciting parts of programming -- that other people can take your program and do interesting things with it.

Today, we are going to begin with the simplest way to get user input -- through the keyboard using `input()`.

First, notice that there is a second mad-libs file, `mad-libs-input.py`. Run that program using `python mad-libs-input.py`. Ask the navigator for words based on the prompts, and enter them into the program as it runs. Then observe what comes out. This is a simple interactive program that asks for input (words) and then changes what it says based on what the user inputs.  

Next, run it again, and type in different things. What happens?

### Exercise 7: Update the Mad-Lib

The original source of that mad-lib is the song "Space Oddity" by David Bowie. It's an old song from the late 60s, written during the space race. For this challenge, change the mad-lib. Pick a different song that YOU like, and use that song to create the mad-lib. Feel free to edit this file; you don't need to create a whole new program.

Your new mad-lib should ask the user for new types of words. They should be words that fit into the song you choose, not the types of words that I asked for. Take what the user enters and have the program store them into variables. Then print out the lyrics to your song, replacing key words with words that the user inputs.

Notice how you store things. The code says `variable = input("...")`. You pick a variable and put it on the left side of the equals sign. Then you put what you want to put into the variable on the right side. Previously, we put actual words in quotation marks -- the quotation marks tell Python that we want the words inside to be reproduced as-is. In this program, instead of putting quotation marks, we use the command `input("...")` to get input from the user. The text inside the parentheses () is the prompt that the user gets when they run the program. Whatever the user types in, it stores into the variable on the left side of the equals sign.

(Question: What happens if you put the `input("...")` command, but don't include `variable =` before it? Answer: It asks the user for input, but then the program immediately forgets what the user typed because it didn't have anywhere to store it.)

*Note*: The code for your program -- the file you edit in your text editor -- should not have the actual words in it like it did in exercise 4. Instead, it should just contain instructions to ask the user for words. 

### Change places

This is another good time to change places with your partner. 

## Not always doing the same thing

Next, we will work with basic conditionals. There are three kinds of conditional statements: `if`, `elif`, and `else`. They all cause things to to cause different things to happen in different situations. 

To begin, let's run the Avengers program:

```
python avengers.py
```

Now go through and read the source code for the Avengers program -- open up `avengers.py` in your text editor. Notice that when you run the program, not every line in the source code gets printed out; instead, it depends on what the user of the program types in. 

Pay particular attention to how things are indented. Indentation is really important in Python. Indentation controls which lines are part of the `if` statement and which ones are not. When `if`, `elif`, and `else` statements are all indented at the same level, this connects them together as one big statement with multiple branches of possibility.

### Exercise 8: Try different inputs

Run the avengers program multiple times. Give different answers to the prompts. Try out all three avengers as an answer to the first prompt. What happens?

Now look at the code. Why is that happening? What is each part of the statement doing? What are the differences between `if`, `elif`, and `else`? (Hint: `elif` is short for "else if".)

Also, as you tried things, did anything not work as you expected?  Make a list of 'bugs' -- problems with the program where it doesn't work the way you expect it to. What you're doing here is testing the program to understand how it works and thinking about how you could improve it. 

### Exercise 9: What Happens when Captain America tries?

Next, modify the code. What happens when Captain America tries to pick up the hammer? Put some print statements in the right place to tell the story of what happens when Captain America tries to pick up the hammer.

### Exercise 10: Lowercase

Right now, if you type in Thor's name or Iron Man's name, it works even if you don't capitalize their names. But Captain America's name has to be capitalized. Modify the code so that you can use lowercase to type in captain america's name.

### Exercise 11: Nicknames

What happens if you just type in "cap" instead of "captain america"? It doesn't work right. Let's fix that. Make it so that you can enter in nicknames like "cap" or "tony" and it'll still work.

### Exercise 12: Black Widow

Black Widow was also hanging out with the rest of her team. Let's add her in to the story. Create a new branch where she tries to lift the hammer, and print out what happens when she tries.

## Challenges

If you and your partner finish all of the exercises before the end of class, try at least one of the challenges below. Check in with Caitlin or Shiyu once you've attempted at least one. If you've completed at least one challenge and there's still time left in class, you can leave early (for labs only). Remember to turn in your work on D2L first!

### Challenge 1: Two-part Mad-libs

Take the mad-libs program that you worked on, and create a second part of the mad-libs. So you input a bunch of words, and it prints out part of a story / song / something. Then you get a chance to input more words, and it prints out the second half. You've already got a first half of the mad-libs program written. Add a second half to your mad-libs program.

### Challenge 2: Avengers Mad-Libs

Turn the Avengers story into mad-libs. Replace some of the words with variables, and then fill in the variables at the
beginning of the program with funny words.

### Challenge 3: Chat bot

Make a new program called `chat.py`. Revisit exercise 4 if you need a reminder on how to do this. Your program should ask the user a question, collect input from the user, then give a different answer in response depending on what the user says. 

For example, `if` the user says "no", respond with one phrase. Else if (`elif`) they say "yes", respond with a different phrase. You can use as many `elif`s as you want to catch different types of user input. You can also use `else` at the end to catch any user response that doesn't match with your `if` or `elif` cases.

## Turn in your work

Today, you'll turn in screenshots of your code working (programs running in PowerShell or Terminal) and the .py files you edited for today's exercises. Turn everything in on D2L, under Assignments -> Lab 2 Screenshots and Code.

For a refresher on taking screenshots, see the [screenshot reference]({% link reference/screenshots.md %}) page.