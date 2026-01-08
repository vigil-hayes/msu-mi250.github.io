---
parent: Week 10
topic: Word Cloud
nav_exclude: false
visible: true
---

_Project Management Plan (PMP) due BEFORE in-class studio:_ [PMP Resources](https://gitlab.msu.edu/mi-250/mi250-pmp-resources)

A [word cloud](https://en.wikipedia.org/wiki/Tag_cloud) is a way of visualizing text -- it shows how frequently different words are used by varying the size of the text. Words that have a larger font size appear more frequently than words that are smaller. If you have some text -- like a song, a speech, or a document -- you can use the word cloud to see approximately what that text is about and what kinds of things are being talked about.  

Here's an example word cloud:

![State of the Union word cloud](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/State_of_the_union_word_clouds.png/1024px-State_of_the_union_word_clouds.png)

And another showing popular keywords relating to learning analytics:

![Learning analytics word cloud](https://upload.wikimedia.org/wikipedia/commons/2/2a/ELI-LA-Word-Cloud-2-900x600.jpg)

Your goal today is to write a program that reads in a *text* file, calculates how often each word appears in that file, and then finds an intersting way to display the most common words in the file on the screen using Turtle graphics. Try to make sure your program works with different kinds of input files.

As per usual, work in teams of 2-3 people.

## Advice

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently.

### Create *text* files

Most of the text you find online are in Word files or Google docs or web pages or ebook formats. Your program only needs to work with *text* files -- files that contain nothing but plain text. No formatting, no colors, no pages, nothing but text. Your code that you edit in Atom is a text file.  

I recommend you start by finding a couple of things that you want to look at a word cloud for. Copy-and-paste the texts into files in your text editor (like Atom, or Notepad) and save it as a plain text file (`.txt`), in the same directory as your word cloud program. That way, you can easily run your program on these different files to try it out.

A great place to start is song lyrics. Pick a song you like, Google for the lyrics, and then save those lyrics into a text file. Another alternative is to pick an old book or play. You can find plain text copies of Shakespeare's plays on [Project Gutenberg](http://www.gutenberg.org/ebooks/search/?query=shakespeare).

### Read in Whole Files

In this week's lab, you learned how to read in a file one line at a time. You can read in a single line of a file using `f.readline()`, or you can do it in a loop by using `for line in f:`.  

However, sometimes, you don't want to read it in one line at a time.  Instead, you want to read the whole file in at once and store its contents in a string. You can do this with `f.read()`.  `f.read()` reads the whole file in at once, and stores it in a Python string.  

You'll want to remember to save that string to a variable: `str = f.read()`.  

Also, remember that this only works after you've already opened the file with `open()`.

### Count words

We have worked with code that counts letters or words in a string multiple times. You wrote word counting code in [this week's lab]({% link labs/reading_files.md %}). I wrote some code to do this back in [the reading code lab](https://gitlab.msu.edu/mi-250/reading-code/-/blob/master/ex7.py) as well. Basically, you create a dictionary where words are the keys and the count -- the number of times the word
appears -- is the value. You split the string into words using `.split()`, and then you look up each word you find and add 1 to the count as you loop through each word.   

If you didn't finish this week's lab, I recommend going back through with your group and trying to get through as much as you can. OR, alternatively, you can use the code I wrote for the reading code lab, but you'll need to understand how it works to use it.

### Sort words

The first challenge from [this week's lab]({% link labs/reading_files.md %}) describes how to sort dictionaries. Actually, you can't sort a dictionary, but you can loop through the dictionary in sorted order. You can use this to go through the dictionary with the most frequent words first (or last, depending on what you want).

### Just do a word list to start

There are many ways to display your word cloud. A [cloud-like](https://en.wikipedia.org/wiki/Tag_cloud#/media/File:Foundation-l_word_cloud_without_headers_and_quotes.png) representation is pretty normal, but it is hard to know where to put the words. You don't need to get something that complicated working immediately.   

Instead, try something simpler. You could just display [words in order](https://en.wikipedia.org/wiki/Tag_cloud#/media/File:State_of_the_union_word_clouds.png). That visualization just puts common words in alphabetical order, and makes the words bigger that appear more often.

You can even go simpler than that, and start with a single list of words, with more common words bigger:

![word list]({% link img/wordlist.png%})

### A word is as big vertically as you tell it to be

When you use `write()` with turtle graphics, you can tell it a font size. That font size is approximately how big, vertically, the word is. So if you tell it to write the word with a size of 20, then you can go down one line by moving the turtle down 20 steps. This is really handy to know when making the word list, and it is what I did to make that word list above.

Note that you already have a number associated with each word -- the word count! What if you made the font size the same as that number?

### You can tell `write` to move the pen horizontally

By default, when you use `write()` to put some text on the screen, the turtle doesn't move. It stays right where it is, and puts the text there. However, you can tell the turtle to move with the text, so the turtle ends up to the right of the text instead of where it started on the left. To do so, you just say `move=True`:
```
write("Hello", font=("Arial", 20, "normal"), move=True)
```

This is really useful if you want to put the words horizontally next to each other.

## Challenges

If you get a basic word cloud display working, first try it on different texts.  See what works well and what doesn't.

### Remove stopwords

It won't surprise you that the most common words in English are really boring -- "the", "a", "is", etc. It isn't very interesting to have a word cloud where the biggest words are those really common words.  It is much more interesting to see which of the less common words appear frequently in a text.

Make a list of "stopwords" -- common words that aren't interesting that you want to remove. Then modify your program to remove stopwords from your list so they don't get displayed, and it only displays the more interesting words. Note that you can use `not in` with a for loop, if you only want to deal with words that are not in a list: `for word not in stop_list:`

### Layout and functions

Try different ways of laying things out.  You can make things a vertical list. You can move around in a circle. You can put words horizontally, and then wrap when it gets past a certain part of the screen. You can put words in alphabetical order. You can sort the words and put the most common one first. You can put longer words first and shorter words later (`len(word)` will calculate the length of a word). Try making the words different colors.  

Try different layouts and and see which one(s) you like better. There is no right answer; different layouts might be useful in different situations. As you create more than one layout, make each layout a separate function. That way, you can just call a different function to get a different layout, and it is easy to go back to a previous layout.

### Automatic rescaling

As you try your word cloud program on different texts, you will find that some longer texts end up with really big words, and some shorter texts have only small words. Try to add a calculation that figures out what the most common word is, and then figures out how big that word should be.  Then rescale all of the words relative to that, so that what is important is not how many times a word was mentioned, but how much more or less often a word was mentioned.

### Add visual design

A word cloud frequently only has words on it -- but it doesn't have to.  You can put other designs on the word cloud. Circle the biggest word? Underline words with more than 20 mentions? Draw a cloud around the whole thing? Make it look interesting.

### Fonts

You can also vary the fonts. You can use the same font for everything, to make it look nice. Or you can change words into different fonts to emphasize some words over others. [Here]({% link fonts.py %}) is a program that you can run to get a list of all the fonts available on your computer.

### Color

You can also vary the colors used. For example, many word clouds use different shades of the same color to indicate different ranges of frequencies. Instead of using the same color for everything, can you make different words have different colors? What might the colors mean?
