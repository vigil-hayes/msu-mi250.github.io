---
parent: Week 13
topic: Refactor Old Studio
nav_exclude: true
visible: false
layout: lab
---

Your goal today is *refactoring*. The task for today is to go back to one of the previous studios that you did, read through the code, and then re-write the code. Your goal in re-writing the code is to make it easier to read, easier to understand, more reusable, and to work better. Much like you did on Monday, you don't need to change what the program does. You just should revise and rewrite the code to make it do what it already does better.

For today's studio, it is up to you whether you work by yourself or whether you work in a group. You do not have to be working with the same group that you did for the original studio; it is OK to refactor code that others wrote.

---

That’s it. That’s the whole of the instructions – choose a past studio, *optionally* form a group to work with, and revise the code to work better. Have fun with it.

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently.

## Advice

### Pick a studio you enjoyed, or didn't finish

You can pick any past studio you want to work on and refactor. My recommendation would be to pick a studio you remember enjoying; you'll care about it more if you had fun with it. Or if there's a studio you and your group didn't manage to complete, you can use today as an opportunity to get the code working.

### Take time to read and understand the code

Read through the code and make sure you understand what it's doing. Run the program to see if it does what you expect based on how you've understood the code. It will likely be helpful to add comments to the code to note down what data each variable is storing, what each function does, etc.

### Use Functions

Code is much easier to read and work with when it is organized into functions. Functions are also really useful for repeating code. A large part of refactoring is figuring out how to write functions so that you aren't repeating yourself, and so the code is easier to read.

Ideally, you will most *most* of your code into functions, and have a relatively short 'main' section that just calls the appropriate functions in the right order.

### Use files to store data

One way to approach refactoring is to think about the data you're working with in the program and where the most efficient way to store that data would be. If you're working on a studio that uses *content* - like text-based data that comprises a story - it might make sense to save that data into files and then use Python to read the files in order to make use of the data. You can also [write text to a file](https://www.geeksforgeeks.org/writing-to-file-in-python/#), which might be useful for storing user input, for example.

### Look for opportunities to refactor

Go back to Monday's lab for ideas how to refactor. When we looked at our existing code, we looked for a couple of things to identify opportunities for refactoring:

* *Look for repeated code*, or places where the exact same code is repeated multiple times. Pull them together into a function.
* *Look for similar code*, or places where code that isn't exactly the same, but is similar, is repeated multiple times. That is a good candidate for putting into a function with one or more parameters.  Small differences can be controlled with the parameter (like the `color` parameter to the rectangle function).
* *Look for opportunities to generalize*. Just like we went from `red_strip()` to `stripe(color)` to `colored_rectangle(...)`, look for places where you take an existing function, and make it more useful by making it slightly more general than it currently is. (Emphasis on *slightly*; if you make things too general, then they become less useful).
* *Remove unneeded code*. As you look at the code, you might find things that aren't needed anymore. Remove them from the file so they don't get in the way of the more important things.
* *Look at how data is stored*. If the program is storing data, what form does the data take? For example, if it's two lists that work with each other, would a dictionary make more sense? Or if it's all text data in strings, would it make more sense to store everything in a text file?

### Think about the User Experience

Refactoring is a gread opportunity to make minor changes to improve the user experience of running your program. Put yourself in the shoes of someone else running your code. What would make it easier to use?  Some things I've seen groups do in class so far include:

* Adding spaces in appropriate places (e.g. at the end of an `input()` prompt) so things don't run together.
* Adding additional text (`print()` statements) to help explain what the program does and what the user is supposed to do.
* Moving the turtle at the beginning of the program up and to the left, so whatever it draws is centered on the screen.
* Changing the font or the color or the line thickness so whatever is being drawn by the turtle is easier to see
* Speeding up the turtle (with the `speed()` function) so you don't have to wait as long for things to draw. (OR have it speed up and slow down at different times as it draws for dramatic effect.)

### How much more can you do?

If you think you've done enough refactoring with a studio, call for help from either Jack or me and talk us through the changes you made.  If we don't have additional ideas, then you can move on and work on refactoring another studio.
