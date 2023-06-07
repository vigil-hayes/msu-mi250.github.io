---
parent: Week 6
topic: Guestbook
nav_exclude: true
visible: false
---

For this week, your goal is to make a digital guestbook. Traditionally, a
[guestbook](https://en.wikipedia.org/wiki/Guestbook) is a physical book left near the entrance of some event (like a
wedding, funeral, or museum) where guests can sign their name, and possibly leave a message.

Your goal is to create a digital guestbook.  Imagine it being left running so people can enter their names and possibly
leave a message. There should be a way to view all of the previous guests, as well as a way for the user to add herself
or himself as a guest. Whether people can leave a message with their name is up to you, as is whether they can add
additional information. The guest list should be displayed in alphabetical order.

Work in teams of 2-4.

---

That’s it. That’s the whole of the instructions – form a group, create a digital guestbook. What the guest book looks
like is entirely up to you. How you program it is entirely up to you. Have fun with it. Be creative.

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### Use Graphics

You spent last week learning turtle graphics.  Use those to make a visual guestbook that looks nice.  Be creative in how
it looks, and get the guestbook to look interesting.

### Start Simple, then Expand

Start with something simple.  For example, you could start by getting a really simple guestbook working that just does
text: it asks for `input()` from the user, and then prints out the whole list of guests every time.  Then modify that so
that it puts them in alphabetical order before printing.  Then modify it so that it uses turtle graphics to print them
out in a way that looks nice.  Then change the input to a `textinput()` that pops up a window asking for the name.

Or something like that.  Think about how to build up capabilities.   Wait for fancy capabilities like visual design or
messages along with names until you've got the basics working well.

### Write in Fonts

The `write()` function in Turtle graphics allows you to specify the font and size.  So, for example, you can write:
```
write("Welcome to my Guestbook", font=("Arial", 30, "normal"))
```
Or
```
write("Please enter your full name", font=("Helvetica", 12, "italic"))
```

There is a python program [here](https://gitlab.msu.edu/mi-250/random-lists/-/snippets/143) that will give
you a list of all the fonts on your computer.

### Test your program

Test your program.  Try inputing different types names.  Type names in in weird or funny ways. Use upper case, or lower
case.  Use names with characters not found in English.  See if it works correctly.

### Add design elements

A simple list of names is pretty boring.  Once you get your names printed, add some stylish visual flair to customize
your guestbook and make it more interesting and appealing.

### Store names in a list

This week, we worked on storing information in lists.  Could you store the names that people enter in a list, and then
display that list on the screen?  If you have everything in a list, does that make it easier or harder to display?  What
more can you do once you have it in a list?  Could you display the names in alphabetical order?  Be creative here.

I recommend that you get your basic guestbook working first, and then try to add lists or sorting.  Build incrementally,
getting something simple working first and then add features.

### Take advantage of randomness

This week, we also learned about using randomness. Is there any way this can be made more interesting if you use
randomness?  Could you make names randomly different sizes?  Or random colors?  Could you make some of the decorations
around the side random?  Be creative.






