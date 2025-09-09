---
parent: Week 4
topic: Flashcards
nav_exclude: false
visible: true
---

Research on how people learn has suggested that when learning facts, one of the most important things to do is to periodically "retrieve" the information from your memory. That is, if you occasionally remember those facts and use them in some way, then you are more likely to remember them long-term. One of the keys is to remember the fact, not just recognize it. That is, it has to come from your brain, and not from something else like notes or a book or a web page. Doing this remembering [periodically and over time](https://en.wikipedia.org/wiki/Spaced_repetition){:target="_blank"} helps you remember facts long-term.

A common way to memorize a bunch of facts at once is to use *Flash Cards*. [Flash cards](https://www.wikihow.com/Write-Flash-Cards){:target="_blank"} used to be physical note cards with a prompt on one side ("What is 2 + 3?") and an answer on the other ("5"). You use them by reading the prompt and trying to remember the answer. Once you remember the answer, then you can flip the card over and check if your answer was right. Flash cards are also nice because you can measure progress: you can count the number you get right, and tell whether you are remembering more or less than in the past. Now, instead of physical note cards, most people use flashcard apps on their computer, phone, or tablet to accomplish the same goal.

## Today's studio

Your goal today is to write a flash card program to help someone study a specific topic. The topic is up to you. Your program should do these things:
* Display a prompt (the question), and ask the user to input their response (the answer). 
* Tell the user if the response is correct or not. 
* Keep asking a question until the user gets it right.
* Once a question is answered correctly, move on to the next flashcard. 
* Optional: keep track of how many tries each flashcard took to answer correctly and print that out at the end.

It's okay if it always prints out the flash cards in the same order every time. We will learn how to make things in different orders later in the semester.

## Git

Store your project in a Git repository on the [MSU GitLab](https://gitlab.msu.edu). You'll need to make a new repository for you and your group - it's easiest to do this first, before you start writing any code. Only one person in the group needs to create a repository; once it's shared, everyone else in the group will have access to it. Remember to add Morgan (vigilhay) and Shiyu (xiangsh2) as members along with your groupmates. See the [Using Git in the Reference section]({% link reference/using_git.md %}) for a refresher.

## Advice

What follows is my advice for doing this. You don't have to follow this advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently. That's okay!

### Make it useful

Try to make this program actually useful. The easiest way is if you make the flashcard app for something you are already trying to learn. For example, maybe you have some vocabulary or dates you need to know for one of your other classes. Or it can be something related to a hobby or interest you have, like remembering which player is on which baseball team (Question: What team is Julio Rodriguez on? Answer: Seattle Mariners), or trivia about favorite novels (Question: Who wrote American Gods? Answer: Neil Gaiman).

If you can't think of anything you might want to test yourself on, you can create a flashcard program for someone else; for example, create a program to help a middle school student remember biology facts, or a high school student remember world history, or an elementary school student study multiplication. Or make a program that could be used for playing trivia night at a bar or cafe.

### Do your research

Just because you are making the program doesn't mean that you have to already know everything! Then why would you need the program? Instead, plan on doing some research to figure out what things you need to learn. Spend some time with Google trying to make a list of the things you would need to learn, and then spend some time on paper trying to turn those into flash cards.

Also, remember that flash cards work best for **facts** -- things with a right or wrong answer that you need to memorize. They don't really help much with other types of learning, like learning how to write, or how to pronouce words in foreign languages, or how to develop your own style.  

### Input, if, print

There are many different ways to make flash cards. But at their simplest, they are an `input` statement to ask the user for the response, and an `if`/`else` statement to check if it was correct. Get the basic pieces working before making it more complex. `question.py` from the lab this week might be useful to look at.

### Loop until correct

For each flash card, what happens when the user enters the wrong answer? Make your program tell the user that it was wrong, and then ask them again for the answer. Put this in a loop so that they keep getting asked until they get it right. Some of the exercises you did for [this week's lab]({% link labs/counting_and_loops.md %}) might be helpful.

### Start simple and test often

Don’t try to do everything at once. Start with something really simple, test it until it works, and then build from there. For example, the first thing you should do is probably just have it print one prompt, and then end. Get that working first. Then write your first input, that asks the user for the response and checks if it is correct. Just print out whether it is correct. Once that works correctly when you run it, then you can add a second flash card. But don’t move on add anything new until everything you’ve already written works correctly.

One thing to keep in mind is *testing*. You want to test the program, over and over, to make sure it does the right thing. Run it multiple times. Put in the right answer. Put in a wrong answer. What happens? Have a teammate run it. Does it work right for them? You should be spending a large amount of your time actually running your program over and over to see if it is working the way you expect it to.

This also means that you don’t need to have the whole set of flash cards written before you start writing your program. Get the first one or two written, then try to make it work as a computer program. Once you've got those written, write on or two more and make them work as a computer program.  Alternate between writing flash cards and writing code. If you try to do it all at once, the its easy to get bogged down in unimportant details. By going back and forth between flashcard writing and coding, you make sure that each activity works well with the other activity.

Also, it is best to get a basic flashcard program working, where you only get one try for each card, and then later add in the *retry* feature that asks them over and over until they get it correct.

### Follow pair programming

In the lab, you practiced pair programming, with two people using one computer. One person was the driver, controlling the keyboard and mouse, and the other person was the navigator, helping out and thinking. Do that again here. It really does help get things working easier. 

If your group has more than 2 people, rotate the driver frequently so everyone gets a chance to write some code; the people who aren't driving can help by using Google, coaching, and writing flashcards.

### Take Turns

Take turns doing the different parts of the work. Don't have one person be the "programmer" and the other be the "flash card writer". Instead, take turns. Have one person in front of the computer programming for 10-20 minutes and then swap to another person. The original programmer can then take a turn with Google looking up facts. Taking turns keeps things interesting as you work, and makes it easier to collaborate and produce something more interesting than you could do yourself.

Remember to use Git for this! When you trade places, the old driver should add, commit, and push their code to the GitLab repository for the studio. The new driver should use `git pull` to get the changes onto their computer before starting to write new code.

