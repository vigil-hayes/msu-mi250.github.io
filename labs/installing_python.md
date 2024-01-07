---
parent: Week 1
topic: Getting Started with Python
git: https://gitlab.msu.edu/mi-250/getting-started
layout: studio
nav_exclude: true
visible: false
---

Today we will start with our first programming lab. We'll be getting Python set up and getting your computer ready for writing code, then we'll practice working with code a bit.

## Pair Programming

In this class, all of the labs will be done through pair programming.  You will be assigned to work with one other person as a "pair". Pairs work following the mantra of "2 people, 1 computer"; that is, both people work together on a single computer to get the lab exercises done. You must do all of the lab exercises together. 

You'll be randomly assigned into a pair for each lab. At any given time, each of you will have different roles. One person will be the "driver", and the other person the "navigator". Once you're paired up, begin by deciding who will be the driver and who will be the navigator.

### Driver

The driver controls the computer. They are physically in front of their computer using the keyboard and mouse. The job of the driver is to get the computer to do the tasks assigned in the lab. The driver is ultimately responsible for what happens on the computer. 

### Navigator

The navigator (also called the observer) watches the driver's activities. They make suggestions, point out errors and problems, ask questions, and think more carefully about what is being done. Being a navigator does not mean being passive; you should be actively watching and trying to help out. Since laptop screens are small, it may be helpful if the navigator uses their laptop or another device to keep the lab instructions up or to look things up. 

It is very important that both members of the pair communicate regularly. The driver can ask questions and discuss issues, the navigator can ask that specific changes be made or specific code by typed in, and both members can stop what is going on to discuss anything they feel needs to be discussed.

Periodically, both of you will switch roles.  In some labs, we will switch roles when you complete specific parts of the lab (like today). In other labs, we will set times, and we will switch roles every 20 minutes or so. Everyone should be both a driver and a navigator at some point during the lab.

## Get ready to work with Python

The goal of this lab is to get everything set up to run your first python program on both your own computer and your partner's computer.  I will give you a program, and you can both run it on your computers.

For this section, the driver will do everything on their computer first with the other person acting as navigator. Later on in the lab you'll switch places. Remember you'll learn faster by working together!

### Install Python

Python is a programming language, but is interpreted, which means that there is a separate program that reads the program that you write and "runs" it by interpreting it as instructions. That is, it is a program that runs other programs.

The first thing we need to do is go install Python. Go to the main Python website at <https://www.python.org>. On that page, hover over the "Download" menu and you should see a button with Python 3.12.X on it. Click the button to download the program, and run the installer program. That will install the current version of the python interpreter on your computer. 

**Important:** While running the installer, be sure to click the "Add python to the PATH" checkbox.

If you already have python installed on your computer, make sure you have the current version (3.11.X). If the version of Python you have installed is not the current version, then run the installer and it should replace the old version of Python with the current version.

### Use Command Line

Next, we want to make sure that Python is installed, and that it is installed correctly. To do this, we are going to use command line. We will be using command line for a lot of things in this class, including running code and saving code to the cloud.

#### If you have Windows

In Windows, we are going to use the "PowerShell" command line interface. This comes built in to all recent versions of
Windows. To access this, click on the search bar and type in "powershell", and that should find it. Run it.

It should open up a window with a bunch of white text at the top on a blue or black background. You'll see a prompt with a blinking cursor in front of it, like this:

```
PS C:\Users\geier>
```

The first thing we are going to do is to verify that we have python installed correctly. To do that, simply type `python` where the cursor is and hit enter. If it works, you should see something like this:

```
Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 19:29:22) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The three arrows `>>>` mean Python is in interactive mode. Try typing `2+2` and hitting enter. It should add the numbers for you. You can use this mode to try out short snippets of code to see if it works. We won't be using it much in this class, though.

To get out of Python's interactive mode, type `quit()` and hit Enter. On Windows, you can also hit Control-Z and then Enter.

##### Troubleshooting

If the Python install doesn't work, you'll get an error message (on older versions of windows), or it will open Python in the Microsoft store (on Windows 10 or 11). Try closing PowerShell and opening it again. If it still doesn't work, it means Python isn't properly installed. 

Run the Python installer again. If it is already installed, if will give you an opportunity to "modify" the python install. Do that. Click through the optional features, and then you should see a page of "Advanced Options". On that page, click the checkbox next to "Add python to environment variables". Then click install to finish it. After this, close PowerShell and open it again, then try the `python` command again.

#### If you have Mac OS

On a Mac, we will use the Terminal app. Terminal gives us a command line that we can use to run things. On the launchpad or in the applications list, it is usually in the "Other" folder.  Or you can click the spotlight search icon (the magnifying glass in the upper right) and type in "terminal".

Terminal should open up a window with a bunch of text in it, and a prompt with a blinking cursor next to it. It might look like this:

```
Last login: Mon Aug 28 23 16:57:43 on ttys000
geier-Macbook-Pro:~ geier$
```

If you type, it should appear next to the prompt. Type the command `python3` and hit enter.   If it works, then you should see something like this appear:

```
Python 3.11.1 (default, Jan 13 2021, 11:08:38)
[Clang 12.0.0 (clang-1200.0.26.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The three arrows `>>>` mean Python is in interactive mode. Try typing `2+2` and hitting enter. It should add the numbers for you. You can use this mode to try out short snippets of code to see if it works. We won't be using it much in this class, though.

To get out of Python's interactive mode, type `quit()` and hit Enter. On Mac, you can also hit Control-D.

**Important:** Macs come pre-installed with a REALLY old version of Python (2.7). Many of the things we do in this class won't run on that version of Python. If you just type `python`, it'll run that really old version. If you are using a Mac, you should always type `python3` instead of `python` to run python. That way, you'll use the current version. Be sure to check the version number that is printed out to make sure it is correct.

##### Troubleshooting

If you get an error message, that means python wasn't installed properly. Try closing Terminal, opening it again, and then trying the `python` command again. If it still doesn't work, try running the Python installer again.

## Run your first program

Next, we are going to try to run our first python program. The program is called `eliza.py` - eliza is the name of the program, and the `.py` at the end means it's a Python program. All python programs end with `.py`.

### Download eliza.py from Gitlab

Near the top of this webpage is a link to a Git repository on Gitlab (which is similar to Github, except administered by MSU). The repository contains the code for this week's lab. Each week's lab will have a Gitlab link at the top.

When you go to Gitlab for the first time, you'll need to log in. Click the "Okta" button (and check the "Remember me" box down below so you won't have to log in everytime.) If you're logged into an MSU system already, the site should load. Otherwise, it'll ask you for the MSU netid and password.

Once you're in Gitlab, you should see a short list of files. Clicking on a file will show you the contents of the file. This repository only has two files in it: `eliza.py` and a file called README.md which says a bit about what's in the repository.  

We want to download the `eliza.py` file. Click on the name of the file, and it should take you to a page where you can view the file.  Near the top of the contents, there is a download link that looks like the bottom half of a box with a down arrow going into it. Click that, and download the file. It will either automatically go to the Downloads folder on your computer, or it will ask you where you want to download it to.

### Find the program using command line

Next, we want to run the file from the command line. Open up PowerShell (in Windows) or Terminal (in Mac OS).

The most important thing to remember about command line is that it only will let you do things with files if it thinks it's in the same location the file is. That means it has to be in the Downloads folder to interact with any of the files in Downloads. PowerShell will show you the directory tree you're in, while Terminal will only show you your current folder.

By default, both PowerShell and Terminal start in the top level Users/username directory when you open it up. Other directories like Desktop and Downloads are nested directly under the Users directory.

The first thing we need to do is to change the current directory to the one where the file was downloaded. If you sent `eliza.py` to the Downloads folder, use the command `cd downloads`. `cd` is short for "change directory". If that command works, it won't print anything out; instead it will just give you a new prompt which will show you you've moved into that folder.  

On Windows, this looks like:

```
PS C:\Users\geier\downloads>
```

On Mac, it looks like:

```
geier-Macbook-Pro:Downloads geier$
```

See how "downloads" is now in the prompt? You can always see where you are in the folder structure on your computer by looking at the command line prompt.

You can go to different places on your computer, too. For example, if you created an "MI 250" folder on your desktop and saved `eliza.py` in there, you can get to your MI 250 folder in command line with this command:

```
cd desktop/"MI 250"
```

Note that whenever you have spaces in the name of a folder, you need to put quote marks ("") around it when you navigate to it in command line.

Once you think you're in the right folder on command line, run the command `ls`. This will give you a list of files in that folder. Make sure `eliza.py` is in that list. If it is, you can run it!

#### Command line reference

There's also a neat trick that works in both Windows and Mac OS to get to the folder you want to go to. 
1. Type `cd` in command line - make sure there is a space after `cd`.
2. Open up the folder you want in File Explorer (Windows) or Finder (Mac OS) -- the normal way of viewing folders. 
3. Drag the folder over to the command line window. When you release your mouse on top of the command line window, that should put the full directory name after `cd`.

A couple of other useful command line commands:
* You can get a list of the files in the current directory with the `ls` command
* You can move up one directory (to the parent directory) with the command `cd ..`
* If you start typing the name of a file or directory, you can it the Tab key and it will try to automatically finish typing the name of that file/directory for you.
* When the space next to the prompt is empty (you haven't typed anything yet), you can hit the "up" arrow on your keyboard - this will autopopulate the last command that was given. 

There's more [useful command line stuff]({% link reference/command_line.md %}) in the Reference section on this site.

### Run the program

Once you are in the right directory, try to run the Eliza program you downloaded:
```
python eliza.py
```
If you're on a Mac, remember to use `python3`!

The program should begin talking to you, and ask you for information about yourself. Play around with it, and answer some questions.  Notice how it responds, and when it says the same things and when it says different things. When you are done, type "goodbye" to exit the program.

Congrats!  You have run your first python program by hand on the command line!  Good work. We will be doing this many times over the course of the semester, but in the future it will mostly be programs that YOU write that you will be running.

## Trade places and repeat

**Change Drivers**: At this point, the driver should have Python installed and running on their computer, and should have been able to run `eliza.py`. Now the driver and navigator should swap.

Go back to the beginning of the [Install Python section]( #install-python) on this page and re-do these all of the above steps on the new driver's computer. Make sure that you've got python installed correctly on both computers, and that both computers can run `eliza.py`. Some things will be easier the second time around, and sometimes you will encounter new problems. Work together with your partner to figure out how to get it working.

## Edit the program

Congratulations on getting a Python program running on your computer.  That is a big accomplishment, and is probably one of the hardest parts of this class. Command line, Python, downloading .py programs -- this is all very weird and not the normal way we install or run programs on computers. There is a reason we do it this way -- it turns out it will be easier in the future if we do it this way -- but it is very weird and takes a while to get used to. That's OK if it feels weird! It should.

For the next step, we are going to edit the program.  We are going to add some new features to the program, and then run it again.

### Install a text editor

To edit the program, the first thing we need it is a text editor.  Computer programs are written as plain text files. This means we can't open them up in Word or Google docs or similar programs. We have to open them in a text editor. There are lots of text editors out there that you can use, and they can get really complicated.

The text editors I recommend for this course are:
* For Mac: [BBEdit](https://www.barebones.com/products/bbedit/download.html) (free version works fine)
* For Windows: [Notepad++](https://notepad-plus-plus.org). 

But you are welcome to install any other text editor you like. If you have a text editor that you already use and like, that's fine, too. I also sometimes use [Visual Studio Code](https://code.visualstudio.com) (both Windows and Mac). 

All of the options above are free to use. There are many others, including some specifically for Python, but not all of them are free and some get very complicated. I encourage you to experiment and find one that YOU like. Programming is a form of art, and each artist has their own preferences for tools.

### Look at the eliza program's code

You downloaded the `eliza.py` program earlier in this lab.  Our next goal is to edit this file. Go to the text editor that you choose, and open the eliza.py file from whatever folder you downloaded it to (probably downloads).

First, look over the file. Read what it says. It is weird, and hard to read. The file roughly has three sections. 

The first section is only 2 lines. It looks like a header (basically, it is). Both lines start with the word `import`. We'll learn more about imports later, but they allow the program to access specific functionality.

The second section is labeled "list of inputs and possible responses", and has a bunch of text in quotes. This contains the logic and intelligence for Eliza, our fictional person.  

The last section calls itself the "code that asks for user input and prints out a response". This is a series of commands -- think of them like the instructions you wrote to make pizzas earlier this week. It prints out information, then asks the user to type something in, and then chooses a response based on what was typed.

Right now, the way Eliza works is that the computer looks for specific words in what the user types; words like "hello", "mother", or "I feel", which the program calls prompts. Then, when it sees one of these prompts, it looks at the list of possible responses below the prompt, and picks one randomly to print out. So if the user enters "hello", then it will randomly pick one of the 3 responses below it and print it out.

### Make a change to the code

We are going to make a change. We are going to allow Eliza to respond to questions.

First, we should check whether she already does that. Run the eliza.py program with the command `python eliza.py` in command line. Enter a question, complete with a question mark at the end. What happens?   She responds, but she doesn't seem to acknowledge that it was a question.

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
That is the 'default' response; if she doesn't know what else to say, she says that. Let's put the question responses just above that. Add a new, blank line right **above** that. Then paste in this code:

```
  ("?",
     ["Why do you ask that?",
      "Why don't you tell me?"
     ]),
```

Make sure not to leave out any parentheses (), square brackets [], or commas. Also make sure the indents look like how the next chunk of code is indented. Indents are important in Python.

Great! You've just made your first changes to a python program. Good work.

When you're done, save the file by going to File -> Save in your text editor. A quicker way to do this is Ctrl+S on Windows or Cmd+S on Macs. Files never save automatically; you have to remember to do it yourself every time. If your changes aren't saved and you try to run the program, it will run the last saved version.

### Run again, and see if the changes appear

Now let's see if your changes work. Go to the command line again, and run eliza.py using the command `python eliza.py`. Notice that this is how we always run a python program: we go to the command line, type the word python followed by the name of the program file we've been editing. (And again, remember to use `python3` if you're on a Mac!)

Eliza should appear again. Start interacting with her. Does she still behave normally?  What happens now if you ask her a question? Does she do somethig different than she did before?

If she does, then your changes have worked! If she doesn't, then go back to the file and try again. Make sure you saved the latest version, and take a look at the punctuation and indents in the code you added.

Don't worry (yet) about how that code works, or what exactly it does.  We will learn that throughout the semester. By the end of the semester -- actually, about half way through the semester -- you should be able to read and understand (and possibly write) this program yourself.  But for now, if you don't understand it, that's normal and OK. The important part is figuring out how to edit files in a text editor, and then run them on the command line.

### Take a screenshot

Once you've got the changes you made to `eliza.py` working, take a take a screen shot of Eliza working on your computer -- preferably showing some of the new responses you've added -- and submit it on D2L. The easiest way to do this is to put the window with your code editor and the window for Terminal or PowerShell side by side and take one big screenshot of both windows.

## Trade places and repeat

In normal labs after this week, we won't be repeating steps on both people's computers. But for now, we want to make sure that both people's computers are set up and working with Python correctly. So **change drivers** again, and go through the steps starting at [Install a Text Editor](#install-a-text-editor) again. Hopefully it will be easier the second time around.

## Extra Challenges

At this point, both you and your partner should have Eliza.py with changes working on both of your computers. Labs every week will have one or more challenges at the end. If you finish all of the main exercises, start working on one of the challenges. If you finish one (or both!) challenges before class ends, let Caitlin or Jack know so we can check your work and answer any questions.

### Challenge: Other Python programs 

Now that you've gotten your first Python program running, try to download a few more Python programs and get them running. Be sure to run them using the command line:

* [Snowflake](https://github.com/raspberrypilearning/turtle-snowflakes/blob/master/code/snowflake.py){:target="_blank"} -- draws a snowflake on the screen.  (the "raw" button downloads the file)
* [Uno](http://code.activestate.com/recipes/580811-uno-text-based/?in=lang-python){:target="_blank"} -- play the card game uno

### Challenge: Add more responses to Eliza

You don't necessarily understand how Eliza works, yet. You will later in the semester. But still, it is a good exercise to try to add additional responses to Eliza. Try to figure out how she works, and see if you can get her to respond in different ways than she does now. 

## Submit your work

When you and your partner are done for the day, submit your work! Today you'll just need to turn in screenshots of Eliza working in command line and of the changes you made to the code. If you got to the challenges, take screenshots of those working, too. Next week you'll start turning in your code as well.

If you and your partner both finished everything and submitted your work before the end of class, you can leave early! **Make sure you check in with Caitlin or Jack first.**

If you didn't get everything done today, that's OK. Sometimes you won't be able to finish the entire lab, and that's fine. For today, since we were installing stuff you'll be using for the rest of the semester, let Caitlin and Jack know if you couldn't finish the main part of the lab and how far you got. We'll work with you after class on Thursday to make sure you have everything working.