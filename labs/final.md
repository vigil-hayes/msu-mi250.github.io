---
parent: Final Week
topic: Adventure Engine
git: None
nav_exclude: true
visible: false
---

For all of this week, we will be going back to the beginning of this class. The very first studio assignment was to make a ["Choose Your Own Adventure" story]({% link studios/choose_your_own_adventure.md %}) -- a program that tells an interactive story where the user gets to make meaningful choices that affect the progression of the story. This week, we are going to do that again -- but this time, you will be using all the skills you've learned throughout the semester to make the program more fun and interesting.

You may use any of the code you wrote for that studio, or any other code you've written or used during the semester. But don't use the same story you wrote before: write something new for this studio.

**Important:** This entire week is a studio. You'll be working in groups of 2-3 people as usual, but you will be continuing this same project on Wednesday with the same group. You'll have class today and on Wednesday to work on the project, and can finish it in that time if you wish. You can also choose to work on it during finals week. Your group's project will be due at the end of the final period for this class: **5pm on Wednesday, April 30**. (Reminder: there is no final exam for this class.)

## Grading and Rubric 

In addition to the normal check, check plus, check minus grades for participating in class this week, this project will receive a grade
as the final project for the class. This grade is based on how well the program works and how interesting / creative the program is. This class has not only taught you how to program, but also emphasized how programming is a useful tool for expressing creativity.

The grade for your final project is 10% of your overall grade for the class. Each student in the group will receive the same grade for the project. Here is a rubric will we use to determine your grade for the project:

*Basic necessities* (aka the “Minimum Viable Product”) (70% of grade; 10% each)
* Program runs (with minimal effort)
* Content exists; the program tells a story
* Program is interactive and gives the user multiple paths to follow (those choices matter for the story)
* Logic of program separated from content somehow
* Option to quit the program exists
* Code is stored in Gitlab
* Screenshots of final, working program in D2L (or in Gitlab)

The remaining 30% of the grade is for going beyond the minimum and making an interesting choose-your-own-adventure program. This can be done through creativity, through programming, or through a combination of both:

*Creativity*
* Tells an interesting story
* Story has an interesting setting / millieu
* Turtle interface that looks interesting 
* Turtle interface that adds to the story
* Other, unanticipated creative strengths

*Programming*
* The program is well commented and easy to read
* The code and content is well organized
* Uses interesting programming / logic to tell the story
* Uses complex-but-not-unnecessarily-complex code/logic (e.g. dictionaries / files)
* Other, unanticipated programming strengths

Each of these can be awarded 0-15 percentage points based on how good / interesting it is. Maximum grade is 100%. Generally, if one of these things is there, it is worth 5%. If it is good, then 10%, and if it is really great, then 15%. Plan to incorprate at least 2 things which go beyond the minimum, and play to your group’s strengths.

You will turn your project in the same way as you have been all semester - put the code in Gitlab, and turn in screenshots on D2L. Make sure to add both Shiyu and Caitlin as *maintainers* on your GitLab repo, or else we won't be able to grade your project!

## Advice

There are many ways to approach this project and you have a lot of tools as your disposal to make something really interesting. Remember you can use any of the code you've written all semester; it might be useful to go back to some of the old labs and studios and see if there's anything you might want to use in your program.

In my experience, every group's program for this project is very different. There's no right or wrong way to do things. Write the program in whatever way makes the most sense to you. The advice below is based on my experience, but you can do things differently if you want.

### Refer to previous labs and studios

Forget how to do something? Remember you can look at the code from previous labs and studios to remind yourself. And you can use any code you've written in the past, too. 

### Logic vs content

One of the items on the rubric is that your program should separate the logic from the content somehow. The logic is what the program is doing - how it works, in what order things happen, etc. The content is what you're showing the user - the text of the story, Turtle illustrations, etc.

We've used two techniques in class that separate content from logic: files and modules.

*Files* allow you to store information - like story text - in a different place than the code for the program. Using text files to store your content and then pulling it into the program is one way you'll want to separate the content from the logic. 

One way to set this up is to have a file for each "path" the user can take in the story. For example, "intro.txt" could contain text that introduces the users to the story, and then gives them two options: stay inside or go outside. If they choose to stay inside, the program will pull the text that describes what happens from "inside.txt". What happens if they choose to go outside will be in "outside.txt". 

*Modules* are similar to files in that they allow you to store things separately from the logic of the program. We've mostly used them to store functions. And we've made a lot of functions that draw things out in Turtle. For this project, you might want to illustrate things that happen in Turtle or as ASCII art - those illustrations are also content. You can create a function for each illustration you want to use, store those functions in their own module, and then call them in the main body of the program.

### Providing an option to quit

The rubric also asked you to provide the user with the option to quit the program while it's running. You should allow your user to enter "quit" (or some other, equivalent input) and when the program notices that, it should just stop.

You can use the function `sys.exit()` to just stop the whole program.  So when the user enters "quit", call `sys.exit()`. You will need to `import sys` at the top of your program so you can use the `exit()` function.

### Loop to load the next file

You could write the program similarly to how you did in the first studio, with a bunch of if / else statements. But if you wanted to allow the user to quit the program at any point while it's running, you'll likely want to use a loop.

One way you might want to use a loop is to have a basic while loop (`while True:`) with all of the main logic for the program inside it. You can use an `if` statement to catch if the user wants to quit.

You can also use loops to serve up the next piece of content depending on what choice the user makes at each juncture. A basic structure for this kind of loop would be to serve up content, then ask the user what their choice is, then loop again to serve up more content. You'd all have to have some code somewhere that would tell the program which content to serve up and when.

### Check for valid input

You can also use loops to make sure the user is entering what the program is expecting by catching errors and giving feedback to the user. For example, say your program is expecting the user to enter A or B, and they enter Q - your program can't do anything but that. But you can use an `else:` statement to catch bad input, give them a message (like "that's not one of the choices") and then loop to give them the same prompt again.

### Use Turtle to illustrate the story

You can use Turtle in lots of ways for this program. You could have the entire story - all of the text, any illustrations, all of the user input - take place in Turtle. You could also display the text and ask for user input in terimal, but show Turtle illustrations at different points in the story.

It's up to you how much or how little Turtle code you want to write for this project. But creating illustrations in Turtle can go a long way towards making your story more interesting and immersive.

### Coordinate your work as a group

Everyone in the group should be working on something, but you don't all have to be working on the same thing. Maybe one person is workong on Turtle illustrations, while another is writing the story and another is working on the engine (the logic of the program.) Or maybe you all write the story together in Google docs, and then split up the coding tasks after the story is written. It's up to you how you want to do this, but try to split it out so that each person is contributing something at all times, and check in with your groupmates frequently.

### Comment your code

Remember you'll be coming back to this project on Wednesday. Add comments to your code to explain what it's doing and how - this will help you pick up the project much faster when you continue working on it later.

## Ideas for being creative

These are all ideas that can help you make your story creative and interactive. You don't have to use any of them if you don't want to: they're here to help you think about what you might be able to do.

*Choose an interesting setting:* Maybe your story takes place in a haunted house, or on Mars. Deciding on a setting first can help provide focus when you go to write and illustrate your story.

*Diagram the story:* Make a decision tree diagram to plot out the different paths the user can take before you write and illustrate it. This can help you to figure out how to code the logic, and where you might want to include illustrations. Here is a very [simple example](https://creately.com/diagram/example/i7nxnlyt/Choose+Your+Own+Adventure+Decision+Tree) of a diagram.

*Collect information from the user:* You can make your program more interactive by asking the user for information about themselves and using it somewhere in the program. For example, you could ask them their name, store it in a variable, and then use it throughout the program. What other things could you do?

*Use randomness:* A lot of role playing games (video or otherwise) use a choose your own adventure type logic - what happens next in the game is determined by what you choose to do. A lot of RPGs also include some element of randomness: if you choose to attack, you roll a 20-sided die and anything you roll that's above a 5 will be a hit. And then another random number might be used to determine how much damage your hit did.

*Draw an info panel:* Sometimes it can be nice for the user to see what paths they've chosen, or what their status is in the came. You could draw an info panel in Turtle that keeps track of the user's previous choices and displays them. Or maybe the info panel shows what items are in the user's inventory, or the amount of health they have. 