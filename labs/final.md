---
parent: Final Week
topic: Adventure Engine
git: None
nav_exclude: false
visible: true
---

For all of this week, we will be going back to the beginning of this class.  Our very first studio assignment was to
make a ["Choose your Own Adventure" story]({% link studios/choose_your_own_adventure.md %}) -- a program that tells an interactive story where the user
gets to make meaningful choices that affect the progression of the story.  This week, we are going to do that again --
but this time, you will be using the skills you've learned in class to make the program more fun and interesting.  This
entire week is a studio; form into teams of 2-4 people; you will be continuing this same project on Wednesday with the
same group.

One thing that many programs do: they separate the "logic" of the program (how it works) from the content (what it
says).  The logic portion is known as an "engine", and it controls all of the interactive parts of the story.   The
content part (usually just called "content") is where the actual story is.  In games, it is also where the art and music
and other aspects of the story are. For this studio, you will be creating both an interactive storytelling engine, and
also creating a set of files that contain a specific, interesting story that is being told.

The engine will be one or more python files.  Those files will have code to display the text-based story, accept input
from users, figure out what the next stage of the story is, and allow the user to quit.   The actual story itself will
be stored in plain text files (`.txt`) that are in the same directory as your python program.  The plain text files
should look like this:

```
It was a dark and stormy night.  You have been walking down this road for what seems like 
forever, and are soaked to the bone from the rain.  You come across a lonely house -- the 
first one you've seen.  It is dark inside.   What do you do?
```

The file contains the story text that should be displayed to the user at this point. Each point should be a separate
text file.  For example, this file might be called `intro.txt`, and if the user chooses to go inside, the next text file
might be called `inside.txt`.  (And if the user choser to stay outside, you would display the contents of `outside.txt`
instead...)

Using this structure, your goal is to create an interesting, interactive story experience. You will write the code that
reads these files, displays them to users, and gives the users interactive options.  And you will also write an
interesting and compelling story.   The Engine + Content structure allows you to separate the work on the two parts of
the story -- the interactivity, and the story text.  Work on both simultaneously, and go back and forth between them as
you work.  I expect that as you work, you will come up with more ideas.

---

That's basically it.  Those are the instructions -- create an engine for telling an interactive, text-based story, and
then use that engine to create a fun and interesting story experience.  I think of this as an interactive art project
that you are creating.

What follows are some suggestions for features and ways to think about doing this.   You have both today's class and
Wednesday's class to do this project.   The final, working project must be stored in a git repository that is shared
with both Dr. Wash and with Jack Waier.  Additionally, please post screenshots to D2L of your finished program
running.

## Engine Features

### Read and display files

The obvious place to start work is with a function that will read in the content of a file and print out that content on
the screen. This is the most basic functionality of your program, and probably the thing you should get working first.
I recommend passing the name of the file in as a parameter -- so you can use the same function every time you need to
read in and display the next file.

### Provide an option to quit

Your user might want to just stop the program in the middle.  You should allow your user to enter "quit" (or some other,
equivalent input) and when you notice that, the program should just stop.

You can use the `sys.exit()` function to just stop the whole program.  So when the user enters "quit", call `sys.exit()`
to stop the program.  Don't forget that you need to `import sys` somewhere for this to work.

### Loop to load the next file

Once you've got the code working that reads and displays the `.txt` files, and also the code that gets inputs from
users, then you can try to loop the code.  Use the input to figure out what the next `.txt` file is that you should
load, and then loop back around to load and display the contents of that file and ask for another user input.

Most engines contain a main loop like this.  This main loop is what controls the whole interactive experience.

### Display the story with turtle graphics

Once you have all of that working using the terminal, you might want to instead change it to display using turtle
graphics.  Using turtle graphics, you can use different fonts to make your story more interesting, and you can draw
other things on the screen around the text.  That is, you can make the interactive story more like a creative art
project.  Think about what you want your screen to look like, and how you want to display your story.

I recommend getting the interactive story working on the terminal before moving to turtle graphics.

---

## Storytelling

This is a computer programming class, and the natural inclination is to focus your time and energy on the programming
part of this assignment. I strongly encourage you to spend at least as much time on the storytelling part of the
assignment!  Telling an interesting, creative, interactive story is important -- it is a different way of expressing
yourself, and a different way of thinking about how you can express yourself.  The programming is not the end goal -- it
never is! Instead, the programming is just a means to tell a story.  If you don't tell an interesting story, it doesn't
matter how good the programming is.   

Also, good storytelling will cause you to go back and improve the programming to make it better, and good programming
will enable more interesting storytelling.   The two build on each other.

### Choose a milieu -- a "world" for the story to be in

If you are good at coming up with stories, then you don’t need this advice. If, like me, you aren’t awesome at it, then
the easiest way to start is to start with an existing story and a set of characters. For example, I’d probably start with
the Avengers movies because I like them and they have LOTS of interesting stories (and the Infinity War saga movies feel
sort of like a choose-your-own-adventure movie).

Pick a story that you already know a lot about to start with, and begin there. It could be from a movie, a book, a game,
a TV show, a fairy tale, or real life. It could be a true story, or it can be made up. But pick an existing story.

The easiest place to start is to tell that story. Then think about different places where people in the story could have
made different choices, and things would have turned out differently. Those are great places to ask the user to make a
choice. You’ll also have to write the alternative outcomes / stories.

### Think interactively

Telling an *interactive* story, where the reader gets to make choices, is different than telling a straight story.
This semester, you have not only been learning how to program, but you've been learning how to adjust your thinking
around the opportunities that programming gives you.  Use this; think about dfferent ways you can give the reader of
your story opportunities to be involved, while still telling an interesting story with a plot and characters?

Is this person the "reader" of your story?  Or is the person a "user" of your program?  Because this is an interactive
creative story, they are both!  Use that to your advantage.

### Support your work: Create diagrams

Once you’ve got an idea for a story, I’d recommend creating a diagram. Put major events in circles on a piece of paper,
and then draw a line between them to signify order. Figure out what kinds of choices can be made, and add other outcomes
as additional circles. It will really help to have a diagram that you can refer back to as you work on the programming.

Here is a very [simple example](https://creately.com/diagram/example/i7nxnlyt/Choose+Your+Own+Adventure+Decision+Tree) of a diagram.

Each circle in the diagram can end up being a file in the story.  You can label the possible paths with choice names.
The diagram will contain a lot of the information that ends up in your text files.

---

## Features for Integrating Storytelling and Engine 

Here are some suggestions for additional features you could add.  They are in no particular order.  You don't have to
add all these features; they are just here to help you think about how you could make your story more interesting.   

I recommend getting the basic program and story working before trying to add these features.

### Control what's next from the content files

First, get the simple version of the engine working.  But if you get that working, one way to improve your engine is to
integrate the story text and the possible options into the same text file.  The text file would then contain the text to
display to the user, the options for what's next, and what file to read next if that option is chosen.  So the
`intro.txt` file could look like this:

```
It was a dark and stormy night.  You have been walking down this road for what seems like 
forever, and are soaked to the bone from the rain.  You come across a lonely house -- the 
first one you've seen.  It is dark inside.   What do you do?
---
Knock on the door: inside.txt
Run away screeming: scream.txt
```

The beginning of the file is the story text that should be displayed to the user.   Then there is a line that is just 3
dashes.   After that, each line contains an option that the user can choose, followed by a colon and then the name of
the next file that the program should read and display, if the user chooses that option.


### Only accept valid inputs

The next hard part of the program is to figure out what options the user has.  If you think back to your adventure
program in week 1, you used `if` statements to check whether the user entered a valid input.  And you hard coded the
possible valid inputs.  In this program, the possible valid inputs are coming from the `.txt` files with the content, so
you will need a way to read the possible valid inputs from the `.txt` file, get input from the user, and then compare
the users input with the possible valid inputs.

You might also want to use a loop for this, so that if the user enters something that isn't valid, you can tell them
that and ask them again.

I recommend putting the code that does this into a function that you can call.  


### Colors

Colors can really help set the mood.  Different points in the story might best be told in different colors.  So let's
have each text file specify what the background color for the screen should be, and what the text color should be.

Modify your program so that the first two lines of each text file can specify a color.  The first line should specify
the background color, and the second line should specify what color the text should be.   When reading in your file, you
should read in these colors and set them appropriately.

Then your content files might look like this:
```
black
white
---
It was a dark and stormy night.  You have been walking down a long road....
```

### Inline Emoji

You've got a graphical system for displaying your story.  That means you can put little graphics in the story, like
emoji.  Create an ability to specify emoji in the text files.

Think about what kinds of emoji or graphics you would want in your stories.  Create a set of functions that draw these
emoji. Then, modify the part of your program that prints out the text to look for inline emoji indicators.  For example,
you could write the text file like this:

```
It was a dark and stormy night *frown*.  You have been walking down a long road...
```

Notice that there are two asterisks with the word `frown` between them; have your program remove them from the text and
replace them with a frowning face emoji.

Think about what kinds of emoji you might want to include in your story.

### Information display

Often, it is valuable to display some kind of information in a panel in the upper right hand corner of the screen. For
example, if you are writing a story about a sports event, you could display the current score there.  If you are writing
a horror story, you could display the main character's current heart rate next to a heart emoji.

Create a small information display in the upper right hand corner that keeps track of some aspect of the story.  If you
are writing a horror story, then it could display the heart rate, and every time the person sees something scary, you
can increase the heart rate.  If the heart rate gets too high, then the story can go to a specific text file?

### Chance

Rather than the user making a direct choice with a direct consequence, there could be an element of chance involved. If
you choose to run away, maybe that would include some code that would pick a random number between 1 and 10, and give you
different options depending on what you roll. 

You can use `random.randint(1, 10)` to pick a random number between 1 and 10.  Then you can check if that random number
is less than something (7 == 70% chance; 2 = 20% chance) 

---

## General Advice

### Break program into parts (functions, modules)

This is the largest and most complicated program you will write this semester.  If you try to make it all one list of
commands, it will get confusing quickly.  Try to stay organized.  You are already separating the logic (programming)
part from the story part (the `.txt` files).  In the programming, stay organized by breaking your code into functions.
Each logical thing that your program does should be a separate function.   Also, you can organize your functions by
putting them into separate python files ("modules").  Each module should contain logically related functions -- for
example, you could put all of the turtle graphics functions in one module, and all of the file reading and input getting
functions in a separate module.   Staying organized will help you make your program more interesting and make it easier
as the program gets more complicated.

### Work as a team

You are working on a team on this project. Use the whole team!  Break up the work into parts, and have different people
do different parts of the project.   Maybe one or two people work on the story for an hour, while the other people on
the team work on the engine.  Then after an hour, you change up the work.  Or have one person work on input and the
other work on output.  Talk with your teammates about how to organize the work to make the project interesting and to
use the creativity and skills of all of the team members.

Think about pair programming -- where one person types while another looks over their shoulder and helps out.  Does pair
programming help you work faster or slower?

### Use past code

You have spent this whole semester writing code.  That code does a lot of valuable, interesting things.   Don't waste
your effort.  Think about what code you've written before, and then go look it up and try to re-use it here.  You can
copy-and-paste your past code if it already does what you need done, or you can copy it and then modify it if it is
close but not quite what you need. Use what you've already written as much as possible; it is much easier to start with
existing code than it is to write code from scratch.

For all of the labs this semester, I have posted solutions -- my working code that solves the lab problems. Go to the
GitLab page for each lab, and choose "solutions" from the dropdown labeled "master".   Feel free to use my solutions
code also -- just make sure you understand what it is doing and how it works.

Likewise, it is a good thing to use existing Python libraries (like `turtle`, `random`, and `sys`).  They can do many
things for you.  Here is a list of [built-in functions](https://docs.python.org/3/library/functions.html) and the full
Python [standard library](https://docs.python.org/3/library/index.html). 

As you work, if you feel like "this has probably already been written", then it probably has.  Try searching Google for
advice.  You might find code that can help you do what you are trying to do.  Often, you will find code that is close,
and then you have to read, understand, and modify that code to do exactly what you are trying to do. But Google can help
you get closer.

### Use git

Git is a good way to share your work with your teammates.  You've been using it all semester to share work.  Do that for
this project.  You will end up with a lot of different files -- both python files and `.txt` story files -- that you
will need to share to get your program to work.  Putting all of those in a cloned git repository is the easiest way to
stay organized and share your work with your team.  Use git and GitLab to help you.

Also, don't just commit to git at the end of the day.  You want to create multiple version, so you can easily go back to
an older version if you need to.  It is better to commit frequently, as soon as you get something working.

### Test pieces separately, and then the whole

As you develop, think about how you can test out your program.   You don't have to do the automated testing that we
learned in class, though you can if you want to.   But we also learned how to *think* about testing.  As you work on
each piece of your program, think about how to test it to make sure that it works the way you think it does.  Then also
think about integration testing -- how do you test that all of the pieces fit together and work together in the way you
hope they do?

### Comment before Wednesday

Be sure to remember to add comments to your code that will help you remember and understand what you did.  You will be
putting this aside for 2 days while you work on other things, and then coming back to it on Wednesday. Comments now will
really help your code make sense for you on Wednesday when you come back to working on it.







