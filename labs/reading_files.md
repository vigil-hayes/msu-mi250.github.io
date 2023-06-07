---
parent: Week 11
topic: Reading Files
git: https://gitlab.msu.edu/mi-250/working-with-files
published: true
nav_exclude: false
visible: true
---

{% capture _ %}{% increment exercise11 %}{% endcapture %}
## Word Counter

For this series of exercises, we are going to build up a program that counts words in a file (how many times each word
appears) and prints the results.

## Using dictionaries to count

Dictionaries are useful any time you have key/value information -- you want to associate one thing (the 'key') with
another thing (the 'value').  So far, we have always stored words in a dictionary.  Let's do something new: let's store a
number in the dictionary (as the 'value', or the 'definition').  That number can represent how many times we've seen a
word.

### Exercise {% increment exercise11 %}: Ducks and Sheep

Consider the phrase "duck duck goose".  The word "duck" appears twice, and the word "goose" appears once.   

The program `count.py` specifies a dictionary that stores these counts and prints them out.  It says that there are 2
'ducks' and one 'goose'.   Each word is used as a key for the dictionary, and then the value for that key is the number
of time that word appears.

Once we are done making the dictionary, each key is a word and the value for that key is the count of the number of
times the word appears in "duck duck goose"..

Modify the program to instead report counts for the phrase "Baby, Im just gonna shake, shake, shake, shake, shake".  You
should use the same program structure: `setdefault()` each possible word to 0 at the top, and then use a single line to
increment the counter for each word of the phrase.

*Hint*: `+=` is used to add to an existing number.  So
```
var += 10
```
is the same as saying
```
var = var + 10
```

### Exercise {% increment exercise11 %}: Print out one letter at a time

You can use a `for` loop to pull each letter out of a string and loop through the letters in a string.  So, for example, if you write:
```
for letter in "Hello":
	print(letter)
```
Then it will loop through each letter of the string "Hello", put it in the variable `letter`, and then 
print out the letter. Then it will put the next letter of "Hello" into `letter`, and print out that letter.  And so on.

*Create a new program* to print out each letter of the phrase **"Baby, I’m just gonna shake, shake, shake, shake,
shake”**, one letter per line.

*Hint*: This exercise does NOT use dictionaries at all.

### Exercise {% increment exercise11 %}: Letter Count

The next exercise is to modify the program to automatically count how many times each letter appears in the phrase, by
combining the two previous exercises.

Using the same `for` loop from exercise 2, instead of printing out the letters, count them like we did in Exercise 1.
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

Using `setdefault()` is safe.  If there isn't anything in the dictionary, then `setdefault()` will make sure there is
soemthing in the dictionary.  But if there already is something in the dictionary for that keyword, then it doesn't
touch the dictionary.   If you don't do this, then the increment line will cause an error if the word isn't already in
the dictionary.   

### Exercise {% increment exercise11 %}: Letter counts for the whole song

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

### Exercise {% increment exercise11 %}: Word Count 

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

### Exercise  {% increment exercise11 %}: Word Count, pt 2

After splitting, you can use the same type of program as exercise 4 to count words.

Modify your count program to count how often each **word** appears in the song from exercise 6, rather than each
letter.  How many times does the word "shake" appear in the refrain of the song?

*Hint*: You can loop through the list of words the same way you looped through letters: `for word in s.split():`

### Exercise {% increment exercise11 %}: Pretty print

You've got a really nice counting program at this point.  However, the way that python prints out dictionaries is really
annoying and hard to read -- its all on one line!

Modify your program to loop through all of the words in the dictionary, and print out the count for each word on a
separate line.

You can do this by calling `dict.keys()` -- which returns a list of all of the keys (words) in the dictionary.  You can
then use a `for` loop to loop through that list.  


## Working with Files

### Exercise {% increment exercise11 %}: Print out a file's contents

If you look in the repository, there is a file there called "wordcount.py". It contains the beginning of a program.
Right now it just opens a file and reads it one line and prints it out.

Notice that it uses the `with()` command.   With allows you to open a file, and then everything in the with block --
everything indented below the `with` command -- has access to the file.  As soon as a line runs that isn't indented,
then python closes the file, and you no longer have access to it.  Also, remember that `with` is NOT a loop; it only
runs once (like `if`).

Modify this program to read in the *whole file*, one line at a time, and then print out that file one line at a time.
You will need to ADD a loop to the program.

There are two ways to read in a file. Choose one, and try to get it working:

1. One way is to put the [`f.readline()`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects)
   function inside a `while` loop.  It returns `""` (the blank string) when it gets to the end of the file, so you can
   break out of the loop when you see a blank string (e.g. `while line != ""`).

2. The other way is to use a for loop -- `for line in f:`.  If you use this, then the for loop implicitly does a
   `readline()` behind the scenes, saves each line in the variable `line`, and automatically stops at the end of the
   file.   (You do NOT need `readline()` if you use a for loop; you should remove that line if you choose to use a for
   loop.)

Either way will work.  Pick one, and modify the program to print out the whole file.

*Hint*:
When you open files, you might end up with some weird looking characters.   That happens sometimes (especially on
Windows).  This is called an "encoding" problem.  You can solve that by including `encoding = 'utf-8'` in your open
command:
```
with open(filename, "r", encoding = 'utf-8') as f:
	...
```

### Exercise {% increment exercise11 %}: Print line numbers

Right now, the program is really basic; all it does is print out the contents of the file.  But once you have the
contents of the line in a variable, you can have your program do more interesting things.  We will start with something
simple: adding line numbers.   Modify your program to print out the line number, and then the
contents of the line.  So the output should look something like this:

```
1 All the world‘s a stage, 
2 and all the men and women merely players.
3 They have their exits and their entrances; 
4 And one man in his time plays many parts
```

*Hint*: To do this, you'll have to keep track of which line you are on in a variable, and then add one to it ever time
you read a new line in.

### Exercise {% increment exercise11 %}: Print out the total number of lines in the file

Modify the program to print out how many lines are in the file at the very end.  This should be pretty easy if you
finished the previous exercise.  The total number of lines is the line number for the last line, right?

```
There are a total of 4 lines in this file
```

### Exercise {% increment exercise11 %}: Count the total number of words in the file

Modify the program to count the total number of words in the file.  Your program should take each line, split it into separate
words, and count the words in the file.  Your program should print out the total count after it is finished reading the whole
file in.

Remember, if you have a variable that contains a string, you can split that into separate words using the
[`.split()`](https://docs.python.org/3.8/library/stdtypes.html#str.split) function.   

```
words_list = line.split()
```

Once you have them in a list, you can then count them: `len(list)` returns the length of list (the number of items in
that list).

```
number_of_words_in_line = len(words_list)
```

### Exercise {% increment exercise11 %}: Change the file you read from

Right now, the program always reads the same file -- 'short.txt'.   Modify the program so that when you run it, it
instead reads in the file 'medium.txt', prints it out with line numbers, and calculates information for that file
instead.


## Make the program do more interesting things

### Exercise {% increment exercise11 %}: Count how many of each word

In all of the exercises you have done so far, you should just be counting the *total* number of words.

For this exercise, modify your program to instead count how many times each word appears.  You should have a separate
count for each word.  You already wrote code to count words in a string in Exercise 6.  Use that here to count how
frequently each word appears in a file.

Your program should print out a dictionary that has the count of the number of times each word appears in the file, and
print out that dictionary.

When I run mine on "short.txt", these are the counts I get:
```
{'All': 1, 'the': 2, "world's": 1, 'a': 1, 'stage,': 1, 'and': 3, 'all': 1, 'men': 1, 'women': 1, 'merely': 1, 'players.': 1, 'They': 1, 'have': 1, 'their': 2, 'exits': 1, 'entrances;': 1, 'And': 1, 'one': 1, 'man': 1, 'in': 1, 'his': 1, 'time': 1, 'plays': 1, 'many': 1, 'parts': 1}
```

### Exercise {% increment exercise11 %}: Move to Long

Look at the file `long.txt` in the repository.  It is the play "Twelfth Night" by William Shakespeare.  Yes, the entire
play.

Modify your program to count how many of each word is present in that play.   Also, modify your program to "pretty
print" the results, so it is easier to read.  You can use `pprint()` for this.

---

## Challenges

### Challenge 1: Sort the words by frequency

Modify your program to only print out most common words that appear in the input file, with the most common words first.

You can do this by sorting the dictionary and looping through your sorted dictionary, and then print out the word and the
count. Make sure the output looks nice and is easily readable by humans.

Dictionaries are stored in python in a random order. It is not possible to actually sort a dictionary like you can sort
a list.

However, you can loop through the dictionary in a specific order.  Here are some options:

#### Sort by key

```
for key in sorted(dict):
	print(key, dict[key])
```

#### Sort by value

```
for key in sorted(dict, key=dict.get):
	print(key, dict[key])
```

#### Reverse sort (highest first)

```
for key in sorted(dict, reverse=True):
	print(key, dict[key])
```

#### Combined (reverse sort by value)
```
for key in sorted(dict, key=dict.get, reverse=True):
	print(key, dict[key])
```

Choose one of these options and use it to sort your dictionary and print out the the words in order by how common they
are.

When I print out most common words in "medium.txt", this is what I get:
```
and: 5
thou: 4
shall: 3
to: 3
of: 3
fair: 3
a: 2
summer’s: 2
more: 2
the: 2
...
```

*Hint* To get the same counts as I did, you will need to get the program to ignore capitals / lowercase issues.  The way
I did that is I converted all the words to lowercase using [`.lower()`](https://docs.python.org/3.8/library/stdtypes.html#str.lower)

### Challenge 2: Top 10 most common words

Modify your program to only print out the 10 most common words that appear in the input file.

You should be able to do this by keeping a separate counter, and then using `break` to stop the loop after you've
printed out 10 words.

### Challenge 3:  Stop List

Modify your program to run on "long.txt".

When you run your program on "long.txt" and look at your top 10 list, you'll notice that many of the top words are obvious
-- I, of, to, a, etc.  Let's try removing the really common, obvious English words to see if we can get a list of the
more unique words in the files.

This is called making a **stop list**.  Create a list at the top of your file that contains common English words.  Then,
when you are reading in the file, if you see a word in that list, skip that word.

Once you have the stop list working, run your word counting program on "long.txt".  What are the 10 most common
words in Shakespeare's Twelfth Night, not counting really common boring words?

*Hint*: Python supports `not in` a list.  If you have a list of `stop_words`, you can say
```
if word not in stop_words:
	...
```

### Challenge 4: Top 10 words in a different Shakespeare play

Pick a different Shakespeare play that you like, and use your program to figure out the most common words in that play.   

You can find plain text copies of Shakespeare's plays on [Project Gutenberg](http://www.gutenberg.org/ebooks/search/?query=shakespeare).

Pick a play, download the "plain text" version of the play, and then run your program on that file.  If you do this
right, you shouldn't have to change your code at all; you should just be able to specify the filename on the command
line.
