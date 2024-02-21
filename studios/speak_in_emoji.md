---
parent: Week 7
topic: Speak in Emoji
nav_exclude: false
visible: true
---

Emoji are graphical representations of ideas and concepts -- basically, they are pictograms. It is possible to convey complex concepts and ideas using nothing but emoji. Smiley face emoji are particularly interesting because they often convey emotions better than words do. Emoji are especially powerful when you put one after the other to form emoji "sentences".

Your goal for today is to write a set of functions that draw emoji using turtle graphics. Each function should draw one emoji. Then use those functions to draw out an emoji "sentence" on the screen that conveys some complex feeling or idea.

As usual, work in groups of 2-3 people.

## Advice

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently.

### Use functions!

Functions work best when they comprise a logical, coherent thing. You want each function to make sense on its own, and to do one "logical" thing. When functions try to do too much in one function, it gets confusing. So, you can create a function `smiley()` that draws a smiley face emoji. It should do everything that is needed for the smiley face.

Also, you don't want it to do things other than what the name implies. So, a `smiley()` function should only draw a smiley face. It shouldn't also move the turtle around to other places, or draw a second emoji, or anything like that.

### Think about side effects

Side effects happen with Turtle functions when you run a function an the turtle ends up somewhere you don't expect at the end. That makes it hard to draw the next thing. One key tip is to make sure the turtle is the same color, in the same place on the screen, and in the same orientation (the direction it faces) at the end of the function as it is at the beginning.

Following this principle makes it much easier to collaborate, too! If everyone in your group is working on a different emoji, it's easier to put them together into one program at the end if you know that each emoji drawing will end where it started. Then all you need is something like a `move_next()` function, like in the lab on Monday, to be able to draw all of the emojis in a row.

### Create your own emoji

Everyone knows the standard smiley face emoji. People have come up with hundreds of new emoji. I encourage you to create your own emoji that capture ideas or feelings that you have! You can use an existing emoji if you want, but it is much more fun to create your own emoji.

### Keep your emoji simple

Emoji are supposed to be simple pictograms. Work hard to keep them simple. Don't spend hours tweaking your emoji to get it just right. Start simple and get the basic emoji working. You can always make it more complex later. Besides, sometimes simple things can convey ideas more effectively than complex things.

### Divide and conquer

Split up the emoji between team members. One of the nice things about functions is that it is really easy to divide up the work. One person can work on one function, and another person can work on the other. This makes it easy to divide up the work in a reasonable, logical way. Also, if you are each working on different functions, Git can usually merge the changes easily. Just make sure that you are all working in a clone of the same Git repository.

If you want to avoid potential Git conflicts, you can also each create your own file for each emoji and assign one team member to combine the code into a single file towards the end of class.

### Support functions

In addition to having a separate function for each emoji, you might want to create a function or two to help with other things that you need to do. For example, could you create a `move_next()` function that moves the turtle to the right and gets it ready to draw the next emoji?

### Look for common features

As you work on your emoji, you might notice that you have common features. For example, if you are drawing both a smiley face and a frowning face, both of them will have the same circular face. That is an opportunity to create a support function. You could in this case create a function that draws a blank face (a circle of the appropriate color). Then your smiley function could call the blank face, and then draw the eyes and mouth. Your frowning face could also call the blank face function first, and then draw a different eyes and mouth.  

Creating support functions for common features like this is a great way to avoid lots of copy-and-pasting of code. It also makes it easier if you want to change something later on. If you want to change the skin color, for example, you only need to change it in the one place (blank face), rather than find all the places in your code that have a skin color.

## Challenge

If you get the basic emoji sentence working and you have time left in the studio today, try this challenge:

The emoji sentence that your program draws is "hard-coded" -- it always draws the same sentence (the same emoji in the same order) every time. Instead of hard coding a sentence, modify your program to allow the user to specify which emoji should be drawn in which order.

For example, your program could work like this:
```
This program has the following emoji:
1. Smiley face
2. Frowney face
3. Winking face
4. Sticking out tongue
(enter 0 to stop)
Which emoji should be first? 1
Which emoji should be next? 1
Which emoji should be next? 2
Which emoji should be next? 4
Which emoji should be next? 3
Which emoji should be next? 0
```
And then it prints out the emoji sentence specified by the user.



