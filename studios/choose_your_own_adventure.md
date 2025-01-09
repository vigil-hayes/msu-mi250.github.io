---
parent: Week 3
topic: Choose Your Own Adventure
nav_exclude: false
visible: true
---

<!-- change "Tuesday" to "last week" for spring semester; reverse for fall semester-->

The goal for today's studio is to write an interactive Choose Your Own Adventure story. In these types of stories, the reader gets to choose what happens next in the story based on a set series of choices. When you run the program, it should show the beginning of the story, ask the user to make a choice from a few choices that you give them, and then continue the story based on that choice. And so on. If I run the program again, it will start in the same place, but if I make different choices, the story should go in a different direction. 

Be creative! There's a small choose your own adventure program in the code from last week's lab using the Avengers. You don't have to write a story about the Avengers; your story can be about anything. But the code from Tuesday might be useful to start with.

You must work in a small group on this project. Form a group of 2-3 people and work together on this project. Who you work with is up to you, but you can't work alone.

## Advice

What follows is just advice for doing it. You don't have to follow my advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently.

### Work together

You should work in small groups on this studio. Groups of 2-3 people. Work together to create the story and to write the code. But don't divide up the work; that's no fun. Everyone should work on all parts. If you need to come up with the next step of the story, then get the whole group together and brainstorm the story. If you need to implement a choice in Python, then get the whole group together and work on it until it looks how you want it to. Have one person on the keyboard sharing their screen, and the rest looking over helping (navigating).

Some groups like to start out by writing the story in Google Docs or by mapping out the story paths on paper. That's fine. When you're writing the code, make sure to switch drivers regularly so everyone gets a chance to work on the program! 

### Use Git

For studios, one person in your group will need to create a **new** Git repository and share it with the rest of the group (and Caitlin and Shiyu).

Note that Git is easiest to use when only one person is writing code at any given time; if multiple people are working on the same file, you will run into Git conflicts, which are sometimes hard to resolve. 

I would recommend approaching it by having one person drive (write code) at a time, and switching off every so often.

First driver:
1. use `git clone` (first time) or `git pull` (every time after the first time) to get the most up to date project onto their computer
2. write code
3. use `git add`, `git commit`, and `git push` to save code to the group's Gitlab repository

Switch drivers, second driver does the same as above, and so on.

If you get stuck with Git, here's a [Git reference]({% link reference/using_git.md %}) that may be helpful. We can also help you anytime. Remember all of your code needs to be in Gitlab at the end of class - that's how you will turn your code in from now on! -->

### Choosing a story

If you are good at coming up with stories, then you don't need this advice. If you aren't awesome at it, then the easiest way to start is to start with an existing story and set of characters.  Pick a story that you already know a lot about to start with, and begin there. It could be from a movie, a book, a game, a TV show, a fairy tale, or real life. It could be a true story, or it could be made up.

The easiest place to start is to tell that story. Then think about different places where people in the story could have made different choices, and things would have turned out differently.  Those are great places to ask the user to make a choice. You'll also have to write the alternative outcomes / stories.

### Diagram

Once you've got an idea for a story, I'd recommend creating a diagram. Put major events in circles on a piece of paper,
and then draw a line between them to signify order. Figure out what kinds of choices can be made, and add other outcomes as additional circles. It will really help to have a diagram that you can refer back to as you work on the programming.

Here is a very [simple example](https://creately.com/diagram/example/i7nxnlyt/Choose+Your+Own+Adventure+Decision+Tree) of a diagram.

It is perfectly OK to use pencil and paper. It is also OK to find a computer program to draw the diagram, and then share your screen as you do that. It is up to you what tools you want to use, and how you use them. I think you will find that using external tools (like pencil and paper) is a very important part of computer programming.

### Start simple, then expand

Don't try to do everything at once. Start with as simple of a story as you can, and then build from there. For example, the first thing you should do is probably just have it print out a single story block, and then end. Get that working first. Then write your first choice -- get the coding working for a single choice, that prints out something silly, but different based on the choice the user made. Once that works correctly when you run it, then you can replace the silly text with the actual story you want to be telling. And then you can add more choices. But don't move on add anything new until everything you've already written works correctly. Keep testing small bits of the program as you go!

This also means that you don't need to have the whole story written before you start writing your program. Get the first bit of it written, then try to make it work as a computer program. Alternate between writing story and writing code. If you try to do it all at once, it's easy to get bogged down in unimportant details. By going back and forth between story writing and coding, you make sure that each piece works well before you move on.

### Use code you've already worked with

You already did a bit with conditionals (if, else, and elif) in last week's lab. You can always use code from labs as a model to build your own code. For today's studio, the `avengers.py` program will be particularly helpful for you to look at.

### Submit on D2L and Gitlab

Your studio is finished when the class is over - no sooner! You can always continue to add to the story or improve your code.

When you are done, please submit screenshots of your code working (that is, of the program running in Powershell or Terminal) on D2L under Assignments. At least one person in the group needs to submit a screenshot. 

Also submit your Python program (your .py file that contains your code) on D2L. Again, only one person in the group needs to submit this.

Also make sure all of your most recent code is in Gitlab, and that your Gitlab repository is shared with Caitlin and Shiyu. This is how you will turn in your code for every studio. See the [Git reference]({% link reference/using_git.md %}) if you need pointers on using Git for studios.