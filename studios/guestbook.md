---
parent: Week 6
topic: Guestbook
nav_exclude: false
visible: true
---

For this week, your goal is to make a digital guestbook. Traditionally, a [guestbook](https://en.wikipedia.org/wiki/Guestbook) is a physical book left near the entrance for an event (like a wedding or funeral) or a place (like a museum). Guests can sign their name and maybe leave a message, and the guestbook acts as a record of who was there.

Your goal is to create a digital guestbook. Imagine it being left running so people can enter their names and possibly leave a message. There should be a way to view all of the previous guests, as well as a way for the user to add themself as a guest. Whether people can leave a message along with their name is up to you, as is whether they can add additional information.

Use Turtle as the interface for the guestbook - the names and any additional information people enter into the guestbook should be displayed using Turtle.

Work in teams of 2-4. One person should start a new repository in GitLab so your team can share code.

## Advice

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently. Be creative!

### Use Turtle

You spent last week learning Turtle graphics. Use Turtle to make a visual guestbook that looks nice. Be creative in how it looks, and get the guestbook to look interesting. Remember you can more than just writing out names - you can draw shapes and use different colors and fonts, too. Refer to the [Turtle lab]({% link labs/turtle.md %}){:target="_blank"} if you need a reminder on how to do certain things with Turtle. The [Turtle documentation](https://docs.python.org/3/library/turtle.html){:target="_blank"} is also a very helpful resource.

### Use lists

We learned how to use lists this week. Think about how you can approach this using lists. You can add things (like user input) to a list, or sort the list (for example, alphabetically).

You can also use a for loop to iterate through a list, item by item. For example, this structure
```
for item in stuff:
    print(item)
```
will go through the list called `stuff` and will print out each item in the list one by one.

Think about how you might want to use lists. Do you want to have everyone add their names to the guestbook first and print it out at the end? Or have it draw out new names using Turtle as they're added? How would you use a list to store and retrieve the names in each case?

### Start simple, then expand

Start with something simple. For example, you could start by getting a really simple guestbook working for just one guest: ask for user input, then draw the user input using Turtle. Then modify it so the name looks nice. Then add a loop so it asks for user input over and over and prints out each name. Then store the names in a list, and print out the list.

Or something like that. There are lots of different ways to do this. Think about how to build up features. Wait to do the fancier, more complex features until you have the basic features working well.

### Use interesting fonts

The `write()` function in Turtle graphics allows you to specify the font and size.  So, for example, you can write:
```
write("Welcome to my Guestbook", font=("Arial", 30, "normal"))
```
Or
```
write("Please enter your full name", font=("Helvetica", 12, "italic"))
```

There is a python program [here](https://gitlab.msu.edu/mi-250/random-lists/-/snippets/143) that will give you a list of all the fonts on your computer. Another trick is to open up Microsoft Word and look at the fonts Word lets you use - if there is no cloud icon next to the name of the font in Word's font list, that means it's already installed on your computer.

### Use randomness

Remember you can pull random items out of a list! If you have, for a example, a list of fonts or a list of colors, you can use `random.choice()` on the list to pull a random item from it. That might be an interesting way to make your guestbook look unique. What other parts of your geustbook design can you apply random features to?

### Test your program

Test your program frequently. Every time you add a few lines of code, test it to make sure it works. It's easier to debug programs if you know the bug is somewhere in the last 2 lines you typed out, rather than having to go through the entire program to figure out what went wrong.






