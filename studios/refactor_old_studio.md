---
parent: Week 11
topic: Refactor Old Studio
nav_exclude: true
visible: false
---

Your goal today is *refactoring*. The task for today is to go back to one of the previous studios that you did, read through the code, and then re-write the code. Your goal in re-writing the code is to make it easier to read, easier to understand, more reusable, and to work better. You don't need to change what the program does if you don't want to. Instead, focus on understanding what the code is doing (writing comments can help) and on figuring out how to make the code clearer and more efficient.

If you would like to use this opportunity to finish a previous studio that you didn't get a chance to finish earlier in the semester, that's fine, too. If you have a specific studio in mind that you'd like to refactor, it might be helpful to work with the same group you worked with for that studio - but it's not necessary. You can also work on refactoring someone else's studio. If you're working on a version of a studio that you didn't originally contribute to, make sure to spend extra time reading the code and understanding what it's doing. If you did contribute to the code but someone else in your group did not, make sure to spend some time explaining to your groupmate(s) what the code is doing.

Work in groups of 2-3, as usual.

## Advice

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever makes the most sense to you.

### Pick a studio you enjoyed, or didn't finish, or didn't do

You can pick any past studio you want to work on and refactor. My recommendation would be to pick a studio you remember enjoying; you'll care about it more if you had fun with it. Or if there's a studio you and your group didn't manage to complete, you can use today as an opportunity to get the code working. You can also focus on a studio that at least one person in your group didn't get to do.

### Take time to read and understand the code

Read through the code and make sure you understand what it's doing. Run the program to see if it does what you expect based on how you've understood the code. It will likely be helpful to add comments to the code to note down what data each variable is storing, what each function does, etc. (You might find you wished you'd added comments when you originally wrote the code!)

### Use functions

Code is much easier to read and work with when it is organized into functions. Functions are also really useful for repeating code. A large part of refactoring is figuring out how to write functions so that you aren't repeating yourself, and so the code is easier to read.

Ideally, you will most *most* of your code into functions, and have a relatively short 'main' section that just calls the appropriate functions in the right order. It might also make sense to put all of your functions in a module.

### Look for opportunities to refactor

Look for a couple of things to identify opportunities for refactoring:

* *Look for repeated code*, or places where the exact same code is repeated multiple times. Pull them together into a function.
* *Look for similar code*, or places where code that isn't exactly the same, but is similar, is repeated multiple times. That is a good candidate for putting into a function with one or more parameters.  Small differences can be controlled with the parameter (like the `color` parameter to the rectangle function).
* *Look for opportunities to generalize*. Look for places where you take an existing function and make it more useful by making it slightly more general than it currently is - for example, adding a parameter or two so the function can be more flexible. (Emphasis on *slightly*; if you make things too general, then they become less useful).
* *Remove unneeded code*. As you look at the code, you might find things that aren't needed anymore. Remove them from the file so they don't get in the way of the more important things.
* *Look at how data is stored*. If the program is storing data, what form does the data take? For example, if it's two lists that work with each other, would a dictionary make more sense? Would it make more sense to store data in a module?

It might be helpful to review the [Organizing Your Program]({% link labs/organizing_your_program.md %}) lab from a couple weeks ago, for a refresher on the techniques that were used in that lab.

### Think about the user experience

Refactoring is a gread opportunity to make minor changes to improve the user experience of running your program. Put yourself in the shoes of someone else running your code. What would make it easier to use?  Some things I've seen groups do in class so far include:

* Adding spaces in appropriate places (e.g. at the end of an `input()` prompt) so things don't run together.
* Adding additional text (`print()` statements) to help explain to the user what the program does and how the user is supposed to interact with it.
* Moving the turtle at the beginning of the program up and to the left, so whatever it draws is centered on the screen.
* Changing the font or the color or the line thickness so whatever is being drawn by the turtle is easier to see
* Speeding up the turtle (with the `speed()` function) so you don't have to wait as long for things to draw. (OR have it speed up and slow down at different times as it draws for dramatic effect.)

### How much more can you do?

If you think you've done enough refactoring with a studio, call for help from either Shiyu or Caitlin and talk us through the changes you made. If we don't have additional ideas, then you can move on and work on refactoring another studio.
