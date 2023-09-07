---
parent: Week 3
topic: Round Robin
nav_exclude: true
visible: false
---

Today's studio is a creative exercise aimed at get you used to sharing code with other people using Git. You'll be practicing what's called round robin storytelling - this is when one person starts a story, then passes it on to the next person who adds to it, and then to the next person, who adds even more, and so on. 

You'll be using Git to share code this week - and also to write the story. The first person will start writing the story and building the code around it, then will push it up to GitLab so the next person can pull it down and start writing a new part of the story/program. 

## Using Git to share code for the studio

Unlike labs, you will generally start from scratch with studios. That means there's no existing GitLab repository for you to fork. Instead, you'll create your own.

First, nominate one member of your group to create the repository. You only need one repo for the whole group.

1. From your projects page in GitLab (this is the main landing page when you first log into Gitlab), click the blue "New Project" button
2. Choose the "Create blank project" option
3. On the Create blank project page, give your project a name (Studio 3 works fine, but you can name it whatever you want). Keep all the other options on that page as-is and click the blue "Create project" button at the bottom.
4. Add your groupmates to the project as members. Also add Caitlin (geierac) and Jack (waierjac). For a reminder of how to do this, see the [Git reference page]({% link reference/using_git.md %}).

At this point, everyone in the group should check that they have access to the repository, and then use `git clone` to make a copy of it on their computers. The repo will only have a README file in it when it's first created, so when you use `git clone`, it will create a new folder on your computer with just the README file it in.

Choose who will start the story - that person should create a new file in the folder that `git clone` just created. Name it whatever you want, just make sure you add .py to the end of the filename. It's also good practice not to put spaces in the filename for a program and use dashes or underscores instead, like this: `my-new-program.py`. The file you create will be the program that you all will take turns working in.

You'll be using Git to pass control of the code from one person to the next. When it's your turn to write part of the story, here's what you'll do:

1. before you make any edits, use `git pull` to bring changes from GitLab down to your computer.
2. add code to your group's program and test it by running the program to make sure it works. It's good practice to make sure your code works as intended before you push it back up to GitLab; otherwise your teammates will have to fix your code before they can run it!
3. push your changes back up to GitLab using `git add`, `git commit`, and `git push`.

Once you've pushed your code, then it'll be ready for the next person to pull it down.

## Advice

Here's my advice. You don't have to take it; I've included here to give you ideas of what you can do for this project. The main goal is for you to get comfortable using Git and passing code from one person to the next, and to tell a story together while you're practicing.

### Decide how long each person's "turn" will be

Writing a round robin story means you will be taking turns writing pieces of the story. You can figure out together what you want the story to be about in a broad sense, but each individual piece of the story will be written by one person.

Each of you will take turns writing a small bit of the story and code for it and then pass it on to another person in your group using Git. Before you start writing, talk as a group and figure out how much text and code each person will be writing before passing the story on to the next person. Maybe two sentences? Maybe one branch of a story path? Maybe set a timer for 5 minutes? Figure out what makes sense for your group and the story you want to tell. Everyone's turn should last about the same amount of time so that each person can contribute equally to the story.

### Make it interactive

You can just write a story using print statements if you want. But you know how to do a few other things with code. For example, last week you learned how to:
* ask for user input
* give your story branching paths
* replace words with user input
Decide as a group what features you want to include in the story - should it be a choose your own adventure, like last week? Should it be some other kind of interactive story where users can add text to it while running the program? Remember you're not only writing a story, you're writing a program - what other things can you do that can make the story more interactive?

### Work together!

You will each be writing your own chunks of the story, but that doesn't mean you shouldn't be working together. You all have a responsibility to each other to make sure that everyone understands the code that the others are writing. If you get stuck, ask your teammates for help. If your teammate gets stuck, see what you can do to help them. Maybe your code keeps giving you errors, maybe Git isn't working right, maybe you have writer's block - all of these are places where your teammates can help you out. Caitlin and Jack are always around to help you get unstuck, too.

### Include ASCII art

Not everyone loves writing, and that's okay. If you completely run out of ideas or want to leave the writing to your groupmates, you can make your part of the story visual instead. One very easy way to add images is to use ASCII art - that's art made by using letters and symbols. In Python, you can use `print()` statements to print out ASCII art so it shows up in command line. The [ASCII Art Archive](https://www.asciiart.eu/){:target="_blank"} is a great place to find ASCII art that others have made, or you can make your own.

Hint: ASCII art usually takes up multiple lines and it can be a pain to use `print()` for every single line. Another way is to use triple quotes before and after a block of text (or symbols), like this:
```
print("""
stuff
stuff
stuff
""")
```

This method will preserve the line breaks of whatever you put inside. 

Be aware that Python sees the backslash symbol - \ - as something special, even when it's in a string. Your text editor might highlight these as a different color. You can "escape" a backslash by adding a second backslash after the first - doing this means you're telling Python to print the first backslash.