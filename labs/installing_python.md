---
parent: Week 1
topic: Getting Started
git: https://gitlab.msu.edu/mi-250/getting-started
layout: studio
title: Studio
nav_order: 3
visible: true
---

Today we will start with our first lab.  Since we haven't yet done any
programming, we cannot yet do a studio, so our first two weeks will be labs.

# Pair Programming

In this class, all of the labs will be done through pair programming.  You will be assigned to work with one other
person as a "pair". Pairs work following the mantra of "2 people, 1 computer"; that is, both people work together on a
single computer to get the lab exercises done.  You must do all of the lab exercises together, and both members of the
pair will receive the same grade for the lab.  

At any given time, each of you will have different roles.  One person will be the "driver", and the other person the
"navigator".

#### Driver

The driver controls the computer.  They are physically in front of their computer using the keyboard and mouse.  The job
of the driver is to get the computer to do the tasks assigned in the lab. The driver is ultimately responsible for what
happens with the computer. 

#### Navigator

The navigator watches the driver's activities.  They make suggestions, point out error and problems, ask questions, and
thinks more carefully about what is being done. Being a navigator does not mean being passive; you should be actively
watching and trying to help out.  Navigators should not use any devices of their own -- no computers, tablets, or
phones. If the navigator needs some information, they need to talk with the driver and ask them to look it up (so it is
done together).  

It is very important that both members of the pair communicate regularly.   The driver can ask questions and discuss
issues, the navigator can ask that specific changes be made or specific code by typed in, and both members can stop what
is going on to discuss anything they feel needs to be discussed.

Periodically, both of you will switch roles.  In some labs, we will switch roles when you complete specific parts of the
lab (like today).  In other labs, we will set times, and we will switch roles every 20 minutes or so.

When you get into your breakout, begin by deciding who will first be the driver, and who will first be the navigator.
The driver should then share his or her screen.  It is really important that only one person do the lab at a time.

# Run your first Python program

The goal of this lab is to get everything set up to run your first python program on both your own computer and your
partner's computer.  I will give you a program, and you can both run it on your computers. 

## Install Python

Python is a programming language, but is interpreted, which means that there is a separate program that reads the
program that you write, and "runs" it by interpreting it as instructions. That is, it is a program that runs other
programs.

The first thing we need to do is go install it.  Go to the main python website at <https://www.python.org> (or just
Google for "python").  On that page, hover over the "Download" menu and you should see a yellow download link.  Go and
download the program, and run the installer program.  That will install the current version of the python interpreter.
While running the installer, be sure to click the "Add python to the PATH" checkbox.

If you already have python installed on your computer, make sure you have the current version (3.11.something).  If the
version of Python you have installed is not the current version, then run the installer and it should replace your old
python with the current version.


## Use the Command Line

Next, we want to verify that python is installed, and that it is installed correctly.  To do that, we are going to use
a command line to do this.  A lot of our interactions will be using the command line, so it is good to practice doing
that right now.

#### If you have Windows

In windows, we are going to use the "Powershell" command line interface.  This comes built in to all recent versions of
windows.  To access this, click on the search bar and type in "powershell", and that should find it.  Run that.

It should open up a window with a bunch of white text at the top on a blue or black background.  It will stay open with
a prompt.  If you type, text appears after the prompt.

The first thing we are going to do is to verify that we have python installed correctly.   To do that, simply type
`python` in the window and hit enter.  If it works, you should see something like this:

```
Python 3.11.1 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If it doesn't work, you'll get an error message (on older versions of windows), or it will open python in the Microsoft
store (on newer Windows 10).  Either of these outcomes means that python isn't properly installed.

If you get either of these outcomes, go back to the python homepage and re-install python.  If it is already installed,
if will give you an opportunity to "modify" the python install.  Do that.  Click through the optional features, and then
you should see a page of "Advanced Options".  On that page, click the checkbox next to "Add python to environment
variables".  Then click install to actually do it.  After this, close powershell and run it again, and try the python
command again.

To close python once it is in interactive mode, type `quit()` to leave python and go back to the command line.  (Or you
can hit Control-D (Mac OS) or Control-Z then Enter (Windows).)

#### If you have Mac OS

On a Mac, we will use the Terminal app.  Terminal gives us a command line that we can use to run things. On the
launchpad or in the applications list, it is usually in the "Other" folder.   Or you can click the spotlight search icon
(the magnifying glass in the upper right) and type in `terminal`.

Terminal should open up a window with a bunch of text in it, and a prompt.  If you type, it should appear in that
window.  Type the command `python3` and hit enter.   If it works, then you should see something like this appear:

```
Python 3.11.1 (default, Jan 13 2021, 11:08:38)
[Clang 12.0.0 (clang-1200.0.26.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If you get an error message, that means python wasn't installed properly.  Go back to the installer and try again.

Macs come pre-installed with a REALLY old version of python (2.7).  You don't want to use this.  If you just type
`python`, it'll run that really old version.   If you are using a Mac, you should always type `python3` instead of
`python` to run python. That way, you'll use the current version.   Be sure to check the version number that is
printed out to make sure it is correct.

To close python once it is in interactive mode, type `quit()` to leave python and go back to the command line.  (Or you
can hit Control-D (Mac OS) or Control-Z then Enter (Windows).)

## Run your first program

Next, we are going to try to run our first python program.  Near the top of this webpage is a link to a Git repository.
That repository contains the code for this week's lab.  Each week's lab will contain a similar link.

If you click on that link, you should see a list of files.  Clicking on one of the files will show you the contents of
tha file -- a python program.  You will probably have to log in to Gitlab using your MSU NetID first.  Gitlab is a
useful service that MSU provides to all students and faculty; we will use it a little today, and explore it more in
future weeks.

We want to download the `eliza.py` file.  Click on the name of the file, and it should take you to a webpage where you
can view the file.  Near the top of the contents, there is a download link that looks like a cloud with a down arrow.
Click that, and download the file.

Next, we want to run the file from the command line.  Open up Powershell (in Windows) or Terminal (in Mac OS).  More
information about these shell commands can be found
[here](http://swcarpentry.github.io/shell-novice/reference)..

The most important think to remember about the command line is that it is *modal*, which means that it remembers
something about where it is, and everything you do depends on that, but it doesn't really tell you that it is
remembering.  In this case, the command line is always has a *current directory* (or folder), and all commands are
relative to that directory.  You can see the current directory with the `pwd` command, which prints the working
directory.

The first thing we need to do is to change the current directory to the one where the file was downloaded.  This can
most likely be achieved with the command `cd Downloads`. If that command words, it won't print anything out; instead it
will just give you another prompt.  That's good!  If it does print something out, that is probably an error message.  To
learn more about this, you can read about [Navigating the Command Line](http://swcarpentry.github.io/shell-novice/02-filedir/index.html) 
(which I recommend if you haven't worked with the command line before).

If that doesn't work, then there is a neat trick that works in both Windows and Mac OS: Open up the folder you want in
File Explorer (Windows) or Finder (Mac OS) -- the normal way of viewing folders.   Then drag the folder over to the
terminal.  That should put the full directory name into the terminal.  However, it is just the directory name, but it
doesn't have the command `cd` in front of it.  So add `cd` in front of it so it looks like this: 
`cd /Users/rickwash/Downloads`. 

A couple of other useful command line commands:
* You can get a list of the files in the current directory with the `ls` command
* You can move up one directory (to the parent directory) with the command `cd ..`
* If you start typing the name of a file or directory, you can it the Tab key and it will try to automatically finish
  typing the name of that file/directory for you.

Once you are in the right directory, try to run the Eliza program you downloaded:
```
python3 eliza.py
```

The program should begin talking to you, and ask you for information about yourself.  Play around with it, and answer
some questions.  Notice how it responds, and when it says the same things and when it says different things.  When you
are done, say "goodbye".

Congrats!  You have run your first python program by hand on the command line!  Good work. We will be doing this
many times over the course of the semester, but in the future it will mostly be programs that YOU write that you will be
running.

## Repeat

**Change Drivers**:  At this point, the driver should have python installed and running on their computer.  Now the
driver and navigator should swap; the navigator becomes the new driver (driving his or her own computer), and the driver
becomes the new navigator. The first driver should close their laptop, and the new driver should open theirs.

Re-do these all of the above steps on the new driver's computer.  Make sure that you've got python installed correctly
on both computers, and that both computers can run the python program.  Some things will be easier the second time
around, and sometimes you will encounter new problems.  Work together with your partner to figure out how to get it
working.

# Edit the program

Congratulations on getting a python program running  on you computer.  That is a big accomplishment, and is probably one
of the hardest parts of this class.  Command lines, python, downloading .py programs -- this is all very weird and not
the normal way we install or run programs on computers.  There is a reason we do it this way -- it turns out it will be
easier in the future if we do it this way -- but it is very weird and takes a while to get used to.  That's OK if it
feels weird! It should.

For the next step, we are going to edit the program.  We are going to add some new features to the program, and then run
it again.

## Install a Plain Text Editor

To edit the program, the first thing we need it is a text editor.  Computer programs are written as plain text files.
This means we can't open them up in Word or Google docs or anything like that.  We have to open them in a plain text
editor.  There are lots of plain text editors out there that you can use, and they can get really complicated.  You are
allowed to use whatever plain text editor you want to; if you know of one you like already, then its OK to use it.  Most
people who take this class, though, probably aren't familiar with text editors, and that's OK.  Here are my suggestions:

The text editor I use is recommend for this course is [BBEdit](https://www.barebones.com/products/bbedit/download.html) 
(Mac only, free version works fine) and  [Notepad++](https://notepad-plus-plus.org) (Windows only). But you are 
welcome to install any other text editor you ilke.  I also sometimes use 
[Visual Studio Code](https://code.visualstudio.com) (both Windows and Mac).  All of those are free.  There are many 
others, and I encourage you to experiment and find one that YOU like.  Programming is a form of art, and each artist 
has their own preferences for tools; its OK if you like something different than other people like.

## Make changes to eliza

You downloaded the `eliza.py` program earlier in this lab.  Our next goal is to edit this file.   Go to the text editor
that you choose, and open the eliza.py file from your downloads folder.

First, look over the file.  Read what it says.  It is weird, and hard to read.  The file roughly has three sections. 

The first section is only 2 lines.  It looks like a header (basically, it is).  Both lines start with the word import.
We'll learn more about imports later, but they allow the program to access specific functionality.

The second section is labeled "List of inputs and possible responses", and has a bunch of text in quotes.  This contains
the logic and intelligence for Eliza, our fictional person.  

And then the last section calls itself the "code tha aks for user input and prints out a response".  This is a series of
commands -- think of them like the instructions we wrote in How-Tos last week.  It prints out information, then asks the
user to type something in, and chooses a response based on what was typed.

Right now, the way Eliza works is that the computer looks for specific words in what the user types; words like "hello",
"mother", or "I feel", which the program calls prompts.  Then, when it sees one of these prompts, it looks at the list
of possible responses below the prompt, and picks one randomly to print out.  So if the user enters "hello", then it
will randomly pick one of the 3 responses below it and print it out.

### Make a change

We are going to make a change.  We are going to allow Eliza to respond to questions.

First, we should check whether she already does that.   Run the eliza.py program with the command `python eliza.py` at
the command line.  Enter a question, complete with a question mark at the end.  What happens?   She responds, but she
doesn't seem to acknowledge that it was a question.

Now, let's add an ability for her to respond to questions.   If you look in the file, you should see code that looks
like this:
```
 ("",
     ["Please tell me more",
      "Can you elaborate on that?",
      "I see",
      "How does that make you feel?",
      "How do you feel when you say that?"
      ]),
```
That is the 'default' response; if she doesn't know what else to say, she says that.  Let's put the question responses
just above that.   Add a new, blank line right **above** that.   Then paste in this code:

```
  ("?",
     ["Why do you ask that?",
      "Why don't you tell me?"
       ]),
```

Great!  You've just made your first changes to a python program.  Good work.

### Run again, and see if the changes appear

Now let's see if those changes work.  Go to the command line again, and run eliza.py using the command `python
eliza.py`.   Notice that this is how we always run a python program; we go to the command line, type the word python
followed by the name of the program file we've been editing.

Eliza should appear again.  Start interacting with her.  Does she still behave normally?  What happens now if you ask
her a question?  Does she do somethig different than she did before?

If she does, then you changes have worked!  If she doesn't, then go back to the file and try again.  Don't forget to
save; not saving the file is one of the biggest reasons why programs don't work the way you expect them to.
Unfortunately, when programming, it is important to remember to save the file frequently.

Don't worry (yet) about how that code works, or what exactly it does.  We will learn that throughout the semester.  By
the end of the semester -- actually, about half way through the semester -- you should be able to read and understand
(and possibly write) this program yourself.  But for now, if you don't understand it, that's normal and OK.  The
important part is figuring out how to edit files in a text editor, and then run them on the command line.

In the interest of practicing that skill, the next thing to do is repeat.

## Repeat

In normal labs after this week, we won't be repeating steps on both people's computers. But for now, we want to make
sure that both people's computers are set up and working with python correctly.  So **change drivers** again, and make
sure a text editor is installed and working correctly on both computers by editing the program on both computers.
Hopefully it will be easier the second time.



<!-- # Git? -->

# Extra Challenges

## Challenge: Other Python programs 

Now that you've gotten your first python program running, try to download a few more python programs and get them
running. Be sure to run them using the command line:

* [Snowflake](https://github.com/raspberrypilearning/turtle-snowflakes/blob/master/code/snowflake.py) -- draws a
  snowflake on the screen.  (the "raw" button downloads the file)
* [Uno](http://code.activestate.com/recipes/580811-uno-text-based/?in=lang-python) -- play the card game uno


## Challenge: Add more responses to Eliza

You don't necessarily understand how Eliza works, yet.  You will later in the semester. But still, it is a good exercise
to try to add additional responses to Eliza.  Try to figure out how she works, and see if you can get her to respond in
different ways than she does now. 


# Submit

At the end of the class period, please take a screen shot of Eliza working on your computer -- preferably showing some
of the new responses you've added -- and submit it on D2L. 

### Other

If for some reason, you cannot download the Eliza program from the gitlab link at the top of the page, you can download
it here: 

* [eliza.py]({% link eliza.py %})
