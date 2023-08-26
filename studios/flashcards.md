---
parent: Week 4
topic: Flash Cards
nav_exclude: true
visible: false
---

Research on how people learn has suggested that, when learning facts, one of the most important things to do is to
periodically "retrieve" the information from your memory.  That is, if you occasionally remember those facts
and use them in some way, then you are more likely to remember them long-term.  One of the keys is to remember the
fact, but not recognize it.  That is, it has to come from your brain, and not from something else like notes or a book
or a web page.  Doing this remembering [periodically, over time](https://en.wikipedia.org/wiki/Spaced_repetition) helps
you remember those facts long-term.

To help people with this, one of the most common ways of remembering a bunch of facts is *Flash Cards*.  [Flash cards](https://www.wikihow.com/Write-Flash-Cards)
used to be physical note cards with a prompt on one side ("What is 2 + 3?") and an answer on the other ("5").  You use
them by reading the prompt and trying to remember the answer. Once you remember the answer, then you can flip the card
over and check if your answer was right.   Flash cards are also nice because you can measure progress; you can count the
number you get right, and tell whether you are remembering more or less than in the past.  Now, instead of physical note
cards, most people use flashcard apps on their computer, phone, or tablet to accomplish the same goal.

Your goal today is to write a flash card program to help someone study a specific topic.  The topic is up to you. It
should display a prompt, and ask the user to input their response.  It should then tell the user if the response is 
correct or not. Then it should do the next flash card. (Optional) And then, at the end, it should tell the user how many (and what
percent) of the flashcards they got correct.

It is OK if it always prints out the flash cards in the same order every time.  We will learn how to make things in
different orders later in class.

Also, store your project in a git repository on the [MSU GitLab](https://gitlab.msu.edu)

----

That's it.  That's the whole instructions for today: pick a topic, and write a program that does flashcards for that
topic, and then tells the user how many they got right.  What topic you want to help people learn is up to you.  How you
program it is entirely up to you.  Be creative!

What follows is advice for doing this.  You don't have to follow this advice.  Do whatever you want.  This is just my
experience in doing this, and you might want to do it differently. That's ok!

## Advice

### Make it useful

Try to make this program actually useful.  The easiest way is if you make the flashcard app for something you are trying
to learn.  You can put a bunch of facts from one of your classes into the program and use it to help yourself remember
those facts. Or it can be something else you are trying to learn. For example, I am working on learning how to play
guitar in my spare time, and I created a flash card program to help myself learn guitar chords.

OR, you can create a flashcard program for someone else; for example, create a program to help a middle school student
remember biology facts, or a high school student remember world history, or an elementary school study with
multiplication.  Try to pick a specific person -- maybe your brother, sister, cousin, or friend -- and make a flash card
program that will help them learn something that they want to learn.

### Do your research

Just because you are making the program doesn't mean that you have to already know everything!  Then why would you need
the app?  Instead, plan on doing some research to figure out what things you need to learn.  Spend some time with Google
trying to make a list of the things you would need to learn, and then spend some time on paper trying to turn those into
flash cards.

Also, remember that flash cards work best for **facts** -- things with a right or wrong answer that you need to
memorize.  They don't really help much with other types of learning, like learning how to write, or how to pronouce
words in foreign languages, or how to develop your own style.  

### Start with git

It is slightly easier to start with a program in Git than it is to add it later.   Start by going to the [MSU
GitLab](https://gitlab.msu.edu) and creating a new project there. After creating the project, go to "members" and add
your teammates and also your instructor and TA. The best way to use it "initialize it with a README", and then to follow
the instructions for cloning the repository to your personal computer.  Once cloned, then you can create new files that
you add and commit.

Also, please add both the instructor (Rick Wash) and the TA (Caitlin Geier) to your GITLab repository.  This is how you
submit your work for the studios from now on.

### Print and If

There are many different ways to make flash cards.  But at their simplest, they are simply a `print` statement (to
present the prompt), an `input` statement to ask the user for the response, and an `if` statement to check if it was
correct.   Start with this simple structure -- `print` -> `input` -> `if`.  If you want to make things more complicated,
that's OK; start by getting this working and then add complexity.

<!--
### Loop until correct

For each flash card, what happens when the user enters the wrong answer? Make your program tell the user that it was
wrong, and then ask them again for the answer. Put this in a loop so that they keep getting asked until they get it
right.  `while true:` can be used to loop infinitely, and then the `break` command can be used to break out of the loop
once they get it right.

*Hint*: When you don't know how long you will be looping, it is better to use a `while` loop than a `for` loop.  
*Hint 2*: When the user finally answers the right answer, you can `break` out of the loop.  
-->

### Start simple, then expand

Don’t try to do everything at once. Start with something really simple, and then build from there. For example, the
first thing you should do is probably just have it print one prompt, and then end. Get that working first.
Then write your first input, that asks the user for the response and checks if it is correct.  Just print out whether it
is correct.  Once that works correctly when you run it, then you can add a second flash card.  But don’t move on add
anything new until everything you’ve already written works correctly. 

One thing to keep in mind is *testing*.  You want to test the program, over and over, to make sure it does the right
thing.  Run it multiple times.  Put in the right answer.  Put in a wrong answer.  What happens?  Have a teammate run it.
Does it work right for them?  You should be spending a large amount of your time actually running your program over and
over to see if it is working the way you expect it to.

This also means that you don’t need to have the whole set of flash cards written before you start writing your program.
Get the first one or two written, then try to make it work as a computer program. Once you've got those written, write
on or two more and make them work as a computer program.  Alternate between writing flash cards and writing code. If you
try to do it all at once, the its easy to get bogged down in unimportant details. By going back and forth between flash
card writng and coding, you make sure that each activity works well with the other activity.

<!--
Also, it is best to get a basic flashcard program working, where you only get one try for each card, and then later add
in the *retry* feature that asks them over and over until they get it correct.
-->

### Follow pair programming

In the lab, you practiced pair programming, with two people using one computer. One person was the driver, controlling
the keyboard and mouse, and the other person was the navigator, helping out and thinking. Do that again here. It really
does help get things working easier.

### Take Turns

Take turns doing the different parts of the work.  Don't have one person be the "programmer" and the other be the "flash
card writer".  Instead, take turns.  Have one person in front of the computer programming for 10-20 minutes and then
swap to another person.  The original programmer can then take a turn with Google looking up facts.  Taking turns keeps
things interesting as you work, and makes it easier to collaborate and produce something more interesting than you could
do yourself.


