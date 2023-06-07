---
parent: Week 10
layout: lab
topic: Counting with Dictionaries
git: https://gitlab.msu.edu/mi-250/dictionaries-and-counting
nav_exclude: true
published: false
---

A [couple of weeks ago](../7/week.html), we started to learn how to use python dictionaries.  In that week, we used
dictionaries as a way to store named, structured data.   We created data structures like "pizza", that had parts inside
of them like "toppings" and "crust".  This is the most common use of python dictionaries: storing structured data.  When
used to store structured data, python dictionaries are like lists, but instead of numbering the contents (like a list
does), we give each item a name.   So, instead of `pizza[1] = "pepperoni"` (which is how we would do it with a list), we
say `pizza['toppings'] = "pepperoni"` (dictionary style). 

Using dictionaries to store named, structured data is the most common use of dictionaries in python, but not the only
way they are used.  This week, we will explore other ways to use dictionaries.

## Working with Dictionaries

As a reminder, dictionaries are key/value stores.  They are similar to lists, but differently structured.  In a list,
values are stored in order: 0, 1, 2, ....  In a dictionary, values are stored by name.  The name is called the 'key' of
the dictionary.

To create a dictionary, we use the curly braces: `{}`.  Everything between the curly braces is a dictionary.  We can
create dictionaries in python like this:

```
my_dictionary = {
    'word': 'definition',
    'word2': 'definition2'
    }
```

Then, any time you need the definition of a word, you can ask python for `my_dictionary['word']` and it will provide the
definition for that word.

I've used the terms 'word' and 'definition', but python dictionaries are more flexible than that.  You can have them
store anything you like.

## Adding to Dictionaries

In earlier  exercises, we worked with a pre-defined dictionary.  We created a dictionary at the beginning of the
program, and then used it in the program to get information out of it.

Dictionaries in python don't have to be pre-defined like this.  It is possible to add things to dictionaries after they
have been created.  In the next couple of exercises, we will be adding things to dictionaries.

Above, we accessed the definition for a word with the code `my_dictionary['word']`. If we treat this like a variable,
then we can add something to the dictionary by assigning to it with equals:

```
my_dictionary["word3"] = "definition3"
```

This code will add a 3rd word to our dictionary above, with its own definition.

### Exercise 1: Add your names

The program `names.py` creates a dictionary that stores people's name.  If you know someone's last name, it can look up
their first name.

Write code to add your name and your partner's name to the dictionary.  Test the program to make sure that if you give
it your last name, it correctly prints out your first name.

*Hint*: You shouldn't need to modify anything inside the while look for this.

### Exercise 2: Unknown Student

What happens if you run `names.py` and ask it for the name of a student that the program doesn't know?  Try it and find
out.

You get a "KeyError" -- which means that it tried to look up something in a dictionary and it wasn't there.  It is the
same as looking up a word in a real dictionary that isn't actually the dictionary.

You can check whether a key is in a dictionary using the `in` keyword.   So, you can say:
```
if "Wash" in names:
	# Do something
```

Likewise you can use `not in` to tell if something isn't in a dictionary:
```
if "notastudent" not in names:
	print("I don't know that student")
```

Modify the names program to check and see if the name that the user enters is known -- if it is in the dictionary.  This
check should happen after the user enters the last name, but before printing out the first name.  If the last name is in
the dictionary, print out the student's first name.  If it isn't, then print out an message saying that the program
doesn't know that student.

So, it should work like this:

```
Enter a student's last name: noone
I don't know that name
Enter a student's last name: Wash
Their first name is Rick
```


### Exercise 3: Allow the user to add a student

Right now, the dictionary of students is hard-coded: it is the same every time you run the program.  However, the user
who runs your program might know about more students than you do.

Modify the names program to first ask the user for one additional student's name -- both their first name and the last
name.  Add that new student to the `names` dictionary.   Then, during the query section where the user can ask the
program for student's first names, check and make sure that it the user can successfully ask the program for that new
students information.

Here is what the output might look like:
```
Enter the last name of a student: Stanley
Enter the first name of that same student: Samuel

Enter a student's last name: Wash
Their first name is Rick
Enter a student's last name: Stanley
Their first name is Samuel
Enter a student's last name: Izzo
I don't know that name
Enter a student's last name:
```

*Hint*: Store the last name and first in separate variables, and then use those variables to add the name to the
dictionary.

## Using dictionaries to count

Dictionaries are useful any time you have key/value information -- you want to associate one thing (the 'key') with
another thing (the 'value').  So far, we have always stored words in a dictionary.  Let's do something new: let's store a
number in the dictionary (as the 'value', or the 'definition').  That number can represent how many times we've seen a
word.

### Exercise 4: Ducks and Sheep

Consider the phrase "duck duck goose".  The word "duck" appears twice, and the word "goose" appears once.   

The program `count.py` specifies a dictionary that stores these counts and prints them out.  It says that there are 2
'ducks' and one 'goose'.   Each word is used as a key for the dictionary, and then the value for that key is the number
of time that word appears.

Once we are done making the dictionary, each key is a word and the value for that key is the count of the number of
times the word appears in "duck duck goose"..

Modify the program to instead report counts for the phrase "Baby, Im just gonna shake, shake, shake, shake, shake".  

*Hint*: `+=` is used to add to an existing number.  So
```
var += 10
```
is the same as saying
```
var = var + 10
```

### Exercise 5: Print out one letter at a time

You can use a `for` loop to pull each letter out of a string and loop through the letters in a string.  So, for example, if you write:
```
for letter in phrase:
	print(letter)
```
Then it will loop through each letter of the string stored in `phrase`, put it in the variable `letter`, and then 
print out the letter. Then it will put the next letter of `phrase` into `letter`, and print out that letter.  And so on.

*Create a new program* to print out each letter of the phrase **"Baby, I’m just gonna shake, shake, shake, shake,
shake”**, one letter per line.

*Hint*: This exercise does NOT use dictionaries at all.

### Exercise 6: Letter Count

The next exercise is to modify the program to automatically count how many times each letter appears in the phrase, by
combining the two previous exercises.

Using the same `for` loop from exercise 5, instead of printing out the letters, count them like we did in Exercise 4.
Use a dictionary to count how many times each letter appears in the phrase.   The keys should be the letters, and the
values should be the counts.

Your goal here is to add each letter that's in the phrase to the dictionary, and as you go through the phrase with the
`for` loop, instead of printing out the letter, you add one to the count for that letter so that the program counts how
many times that letter appears.

When you are successful, your counting program should print out the letter counts for that phrase:
```
{'B': 1, 'a': 7, 'b': 1, 'y': 1, ',': 5, ' ': 8, 'I': 1, '’': 1, 'm': 1, 'j': 1, 'u': 1, 's': 6, 't': 1, 'g': 1, 'o': 1, 'n': 2, 'h': 5, 'k': 5, 'e': 5}
```

Note: You will need to handle what happens if the letter isn't already in the dictionary.  You may want to use the
`setdefault()` function.   To do this, you say:
```
my_dictionary.setdefault('word', 'default_value')
```
The way this works is that it looks in the `my_dict` dictionary.  If `word` already exists in the dictionary, it does
NOTHING.  If it doesn't exist, then it creates an entry in the dictionary for `word` and sets its value to
`default_value`.  That is, it is the same as saying:
```
if 'word' not in my_dictionary:
	dict['word'] = 'default_value'
```

The way we normally use this is in combination with `+=`.   You first `setdefault()`, which makes sure that key exists in the dictionary and set it to a default value (like 0) if needed.  Then you `+=`.  On future loops, the `setdefault()` doesn't do anything because the key already exists, and only the `+=` happens:
```
for i in range(10):
	dict.setdefault('word', 0)
	dict['word'] += 1
```

### Exercise 7: Letter counts for the whole song

Here is the whole refrain to the Taylor Swift song:

```
‘Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I’m just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off
Heartbreakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I’m just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off

I shake it off, I shake it off
I, I shake it off, I shake it off
I, I shake it off, I shake it off
I, I shake it off, I shake it off
```

Modify your program to count how many times each letter appears in this song.

Here is what I got:

```
{'\n': 14, '‘': 1, 'C': 1, 'a': 56, 'u': 3, 's': 29, 'e': 47, ' ': 91, 't': 24, 'h': 31, 'p': 6, 'l': 6, 'y': 8, 'r': 11, 'g': 6, 'o': 18, 'n': 14, ',': 35, 'A': 2, 'd': 2, 'B': 2, 'b': 8, 'I': 17, '’': 2, 'm': 2, 'j': 2, 'k': 34, 'i': 12, 'f': 30, 'H': 1}
```

*Hint*: In python, hard-coded strings normally all appear on one line: `"hello"`.   If you want a string to be more than
one line long (like the lyrics above), you can use triple double-quotes around it.   So something like this:
```
lyrics = """
These are the lyrics to a song
that span more than one line
and don't rhyme
"""
```

### Exercise 8: Word Count 

Python has a really useful function calles `split()`.   The split function takes a string and divides it into a list of
words.   So if I have a string:
```
s = "I shake it off"
```
and I run `s.split()`, then it will split it into a list of words:
```
["I", "shake", "it", "off"]
```

Modiy your program to run `split()` on the full song lyrics above and print out the result.  What does `split()` do?

### Exercise 8.5 Word Count, pt 2

After splitting, you can use the same type of program as exercise 6 to count words.

Modify your count program to count how often each **word** appears in the song from exercise 7, rather than each
letter.  How many times does the word "shake" appear in the refrain of the song?

*Hint*: You can loop through the list of words the same way you looped through letters: `for word in s.split():`

### Exercise 9: Pretty print

You've got a really nice counting program at this point.  However, the way that python prints out dictionaries is really
annoying and hard to read -- its all on one line!

Modify your program to loop through all of the words in the dictionary, and print out the count for each word on a
separate line.

You can do this by calling `dict.keys()` -- which returns a list of all of the keys (words) in the dictionary.  You can
then use a `for` loop to loop through that list.  


### Challenge 1: Most Frequent word (sorting dictionaries)

For this exercise, modify your program to print out the dictionary sorted, so that the most frequent word appears first.

Dictionaries are stored in python in a random order. It is not possible to actually sort a dictionary like you can sort
a list.

However, you can loop through the dictionary in a specific order.  Here are some options (where `dict` is the variable
containing your dictionary):

#### Sort by key

```
for key in sorted(dict):
```

#### Sort by value

```
for key in sorted(dict, key=dict.get):
```

#### Reverse sort (highest first)

```
for key in sorted(dict, reverse=True):
```


What is the most common word in that song?   Have your program explicilty print out the most common word in the song.

### Challenge 2: Stop words and punctuation

It is really annoying when "," is the most common word, or when "the" is the
most common word.  Modify your program to remove common punctuation, and also
to remove really common, uninteresting words like "a", "an", "the", and "is".

### Challenge 3: Case

Look carefully at your output. Did you notice that "shake" and "Shake" are two
different words?   Dictionaries are case sensitive, and so treats those as
separate words.  Modify your program so that case doesn't matter, and even if
words are different cases in the input, it still counts them as the same.

*Hint*: `tolower()` can convert a string to lower case.

