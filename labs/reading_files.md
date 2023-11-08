---
parent: Week 12
topic: Working with Text and Files
git: https://gitlab.msu.edu/mi-250/working-with-files
nav_exclude: true
visible: false

---

{% capture _ %}{% increment exercise11 %}{% endcapture %}
## Using dictionaries for analysis

For this series of exercises, we are going to build up a program that counts words in a file (how many times each word appears) and prints the results.

Dictionaries are useful any time you have key/value information -- you want to associate one thing (the 'key') with another thing (the 'value'). The key is always a word, but the value can be anything. We've mainly used dictionaries as a way to provide structure for sets of data, but dictionaries can also be useful for analyzing text. Today we'll use dictionaries to do some very basic text analysis.

### Exercise {% increment exercise11 %}: Ducks and Sheep

Consider the phrase "duck duck goose". The word "duck" appears twice, and the word "goose" appears once.   

The program `count.py` specifies a dictionary that stores these counts and prints them out. It says that there are 2 'ducks' and one 'goose'. Each word is used as a key in the dictionary, and the value for that each is the number of time that word appears.

Once we are done making the dictionary, each key is a word and the value for that key is the count of the number of times the word appears in "duck duck goose".

Modify the program to instead report counts for the phrase "Baby, I'm just gonna shake, shake, shake, shake, shake". You should use the same program structure: use `setdefault()` on each unique word in the phrase to set the value associated with each word to 0 at the top, and then use a single line to increment the counter for each word of the phrase.

*Hint*: `+=` is used to add to an existing number.  So
```
var += 10
```
is the same as saying
```
var = var + 10
```

### Exercise {% increment exercise11 %}: Split the string

It's a pain to add each word to the dictionary one by one. Luckily, we're using Python, and Python has lots of tools to make that kind of work faster.

Right now, the phrase "Baby, I'm just gonna shake, shake, shake, shake, shake" is a string, and we've been breaking it up into individual words and adding them to the dictionary manually. Python has a function for breaking up strings into a list of words. We can then use a `for` loop to add each word to the dictionary. 

Create a **new program** called `word_count.py`. Paste the phrase "Baby, I'm just gonna shake, shake, shake, shake, shake" into the new program and save it to a variable.

Now let's break up this phrase -- which is a string -- into individual words. In Python, we can do this with the `split()` function, which separates out each word and returns a list of words. So if I have a string called `s`:
```
s = "I shake it off"
```
and I run `s.split()`, then the list it returns will look ike this:
```
["I", "shake", "it", "off"]
```

Do this on the phrase in your program, and print out the resulting list.

*Hint:* You'll want to save the results of the `split()` function - the list - into a new variable, otherwise you'll have a hard time with the next exercise.

### Exercise {% increment exercise11 %}: Count words using a dictionary

Now we have a list of words. Remember you can use a `for` loop to go through a list item by item like this:
```
for item in my_list:
```
Every time this loop runs, the variable `item` represents the next word in the list. You can use that variable inside of the loop to do things with each word.

Now create a blank dictionary called `words`. We'll use the `for` loop to add each word in the list to this dictionary along with a value representing how many times that word has been encountered. 

First, you will want to set the default value associated with each word to 0 using a phrase like this:
```
my_dictionary.setdefault('word','default_value')
``` 
In this example, 'word' is the key and 'default_value' is the value -- both of these are hardcoded. But we want the word - the key - to be different each time the loop is run, so that each individual word will be added to the dictionary. Remember there's a variable in the `for` loop statement that represents each word in the list of words. 

We also want the default value to start at 0 so that we can add to that count every time we encounter the word. After you set the default value, you'll want to increment the count for the value every time the word shows up. You already did this in the first exercise. 

Your `for` loop should now set the default value for each word and then increment the count associated with that word each time it sees it in the list. Print out the `words` dictionary when you're done. It should look like this:

```
{'Baby,': 1, "I'm": 1, 'just': 1, 'gonna': 1, 'shake,': 4, 'shake': 1}
```

### Exercise {% increment exercise11 %}: Clean up text, part 1

Notice the work 'shake' is in the dictionary twice. The fist time it appears, there's a comma next to it. We can use Python to strip out the punctuation. 

Python has another useful function that works on strings called `replace()`. This function will replace a given character or word in a string with something else. `replace()` takes two arguments: the character/word to find in the string, and the thing you want to replace that character or word with. For example,

```
my_string.replace("w","x")
```
would look for every time the character 'w' shows up in a string and replace it with the character 'x'.

For this exercise, what we're going to do is replace all of the punctuation characters in the string with nothing, like this:

```python
punc = ''',.?!:;-'''    # common punctuation marks, saved into a string
for char in phrase:  	# go through each character in the "phrase" string
	if char in punc: 	# for each character in the string, checks if the character is also in the string called 'punc'
		phrase = phrase.replace(char, "") 	# replaces the character with nothing and resaves the string
```

Integrate the code above into your program. If you've done it correctly, the dictionary that prints out should now look like this:

```
{'Baby': 1, "I'm": 1, 'just': 1, 'gonna': 1, 'shake': 5}
```

*Hint:* You'll need to think about where best to put this code. Think about the order that things are happening in: should this code go before or after the phrase is split up into a list of words?

### Exercise {% increment exercise11 %}: Clean up text, part 2

That looks better. But note that some words are capitalized and some words aren't. If the word "Baby" were to show up more than once and some instances were capitalized and some were not, it would end up as two different entries in our word count dictionary.

Let's fix that. Python has yet another function that can be used on strings to make all of the characters lower case called `lower()`. We used it all the way back in Week 2 and a few times since then. Use it here to convert the whole song to lower case before you split it up into words.

Now your dictionary should look like this:

```
{'baby': 1, "i'm": 1, 'just': 1, 'gonna': 1, 'shake': 5}
```

*Hint:* Remember if you want the string to be saved as all lower case, you have to overwrite the variable the string is saved into when you apply `lower()` to it.

### Exercise {% increment exercise11 %}: Use different text

This program is working pretty well with a short phrase. What about something longer? We're only running it on one line of the Taylor Swift song. Let's use the full refrain instead:

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

*Note:* In Python, hard-coded strings normally all appear on one line: `"hello"`. If you want a string to be more than one line long (like the lyrics above), you can use triple double-quotes around it. So something like this:
```
lyrics = """
These are the lyrics to a song
that span more than one line
and don't rhyme
"""
```

The dictionary that prints out should now look like this:

```
{'‘cause': 1, 'the': 3, 'players': 1, 'gonna': 6, 'play': 5, 'and': 2, 'haters': 1, 'hate': 5, 'baby': 2, 'i’m': 2, 'just': 2, 'shake': 22, 'i': 15, 'it': 12, 'off': 12, 'heartbreakers': 1, 'break': 5, 'fakers': 1, 'fake': 5}
```

### Exercise {% increment exercise11 %}: Print the results nicely

You've got a really program for cleaning text and counting words at this point. However, the way that Python prints out dictionaries is really annoying and hard to read.

Modify your program to loop through all of the words in the dictionary and print out the count for each word on a separate line, like this:

```
‘cause: 1
the: 3
players: 1
gonna: 6
play: 5
...
```

You can do this by calling `dict.keys()` -- which returns a list of all of the keys (words) in the dictionary. You can then use a `for` loop to loop through that list.  

## Working with Files

We can do a lot with strings in Python. But if you have a lot of text -- like a book's worth of text -- it becomes very annoying to store the text inside the program itself.

Instead, you can store the text in text files (files that end in `.txt`) and have Python read text from the file and into the program. 

### Exercise {% increment exercise11 %}: Print out a file's contents

If you look in the repository, there is a file there called `filecount.py`. It contains the beginning of a program. Right now it just opens a file, reads the first line, and prints it out.

Notice that it uses the `with()` command. `with()` allows you to open a file, and then everything in the with block -- everything indented below the `with` command -- has access to the file. As soon as a line runs that isn't indented, then Python closes the file, and the program no longer have access to it. Also, remember that `with` is NOT a loop; it only runs once (like `if`).

Run this program. What does it print out? Look at the other files in the git repository -- where is this program getting the text from?

### Exercise {% increment exercise11 %}: Print out the full file

Modify `filecount.py` to read in the *whole file*, one line at a time, and then print out the text from the file one line at a time. You will need to add a loop to the program to do this.

There are two ways to read in a file. Choose one, and try to get it working:

1. One way is to put the [`f.readline()`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) function inside a `while` loop.  It returns `""` (an empty string) when it gets to the end of the file, so you can break out of the loop when you see an empty string (e.g. `while line != ""`).

2. The other way is to use a for loop -- `for line in f:`.  If you use this, then the for loop implicitly does a `readline()` behind the scenes, saves each line in the variable `line`, and automatically stops at the end of the file. (You do NOT need `readline()` if you use a for loop; you should remove that line if you choose to use a for loop.)

Either way will work. Pick one, and modify the program to print out the whole file.

### Exercise {% increment exercise11 %}: Print line numbers

Right now, the program is really basic; all it does is print out the contents of the file. But once you have the contents of the line in a variable, you can have your program do more interesting things. We will start with something simple: adding line numbers. Modify your program to print out the line number, and then the contents of the line. The output should look something like this:

```
1 All the world‘s a stage, 
2 and all the men and women merely players.
3 They have their exits and their entrances; 
4 And one man in his time plays many parts
```

*Hint*: To do this, you'll have to keep track of which line you are on with a counter variable, which you can increment (add 1 to it) every time you read a new line in.

### Exercise {% increment exercise11 %}: Print out the total number of lines in the file

Modify the program to print out how many lines are in the file at the very end. This should be pretty easy if you finished the previous exercise. The total number of lines is the line number for the last line, right?

```
There are a total of 4 lines in this file
```

### Exercise {% increment exercise11 %}: Count the total number of words in the file

Modify the program to count the total number of words in the file. Your program should take each line, split it into separate words, and count the words in the file. Your program should print out the total count after it is finished reading the whole file in.

Remember, we used `split()` in our word counter program to convert a string into a list of words. You can use it in a similar way here.

Once you have them in a list, you can then count them: `len(list)` returns the length of list (the number of items in that list).

```
number_of_words_in_line = len(words_list)
```

### Exercise {% increment exercise11 %}: Change the file you read from

Right now, the program always reads the same file -- 'short.txt'.   Modify the program so that when you run it, it instead reads in the file 'medium.txt', prints it out with line numbers, and calculates information for that file instead.

## Count words from files

Right now this program is just telling you very basic things about the file you give it. But we can do more interesting things -- we've already done more interesting things with strings. We can do the same things with text from a file.

### Exercise {% increment exercise11 %}: Count how many of each word

For this exercise, modify your program to instead count how many times each word appears. You should have a separate count for each word.

Sound familiar? You've already done in your `word_count.py` program. Bring the code from that program into this one, but modify it to use the text from the file instead.

Your program should print out a dictionary that has the count of the number of times each word appears in the file.

When I run mine on "short.txt", these are the counts I get:
```
{'All': 1, 'the': 2, "world's": 1, 'a': 1, 'stage,': 1, 'and': 3, 'all': 1, 'men': 1, 'women': 1, 'merely': 1, 'players.': 1, 'They': 1, 'have': 1, 'their': 2, 'exits': 1, 'entrances;': 1, 'And': 1, 'one': 1, 'man': 1, 'in': 1, 'his': 1, 'time': 1, 'plays': 1, 'many': 1, 'parts': 1}
```

### Exercise {% increment exercise11 %}: Clean up the text

You also have code in `word_count.py` that removes extra punctuation makes and puts all the words into lower case. Let's use that code here, too -- that is, if you haven't already done so.

Now your dictionary should look like this for "short.txt":
```
{'all': 2, 'the': 2, 'world‘s': 1, 'a': 1, 'stage': 1, 'and': 4, 'men': 1, 'women': 1, 'merely': 1, 'players': 1, 'they': 1, 'have': 1, 'their': 2, 'exits': 1, 'entrances': 1, 'one': 1, 'man': 1, 'in': 1, 'his': 1, 'time': 1, 'plays': 1, 'many': 1, 'parts': 1}
```

Remember that all of the code that acts on text from a file must be *inside* the `with` block.

### Exercise {% increment exercise11 %}: Print the results nicely

The bigger a dictionary gets, the harder it is to read. Modify your program to loop through all of the words in the dictionary and print out the count for each word on a separate line. Remember you've already done this in a previous exercise.

Make sure to test it with both `short.txt` and `medium.txt`.

### Exercise {% increment exercise11 %}: Move to Long

Look at the file `long.txt` in the repository. It is the play "Twelfth Night" by William Shakespeare. Yes, the entire play.

Modify your program to count how many of each word is present in that play and print out the results. This should be easy, but the results will be much, much longer!

## Challenges

If you've finished all of the exercises above and still have time left in class, try at least one of the challenges below. Note: most of these challenges will be helpful for the studio this week.

### Challenge 1: Sort the words by frequency

Modify your program to only print out most common words that appear in the input file, with the most common words first. Make sure it works with all three text files: `short.txt`, `medium.txt`, and `long.txt`. Note it's easiest to test code on `short.txt` because it's the output is so much smaller.

You can do this by sorting the dictionary and looping through your sorted dictionary, and then print out the word and the count. Make sure the output looks nice and is easily readable by humans.

Dictionaries are stored in Python in a random order. It is not possible to actually sort a dictionary like you can sort a list.

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

Choose one of these options and use it to sort your dictionary and print out the the words in order by how common they are.

When I print out most common words in `medium.txt`, this is what I get:
```
and 5
thou 4
shall 3
to 3
of 3
fair 3
thee 2
a 2
summer’s 2
more 2
the 2
...
```

### Challenge 2: Top 10 most common words

Modify your program to only print out the 10 most common words that appear in the input file. Try it out with both `medium.txt` and `long.txt`.

You should be able to do this by keeping a separate counter, and then using `break` to stop the loop after you've printed out 10 words.

### Challenge 3:  Stop List

When you run your program, particularly on `medium.txt` and on `long.txt` and look at your top 10 list, you'll notice that many of the top words are obvious -- and, of, the, a, etc. Let's try removing the really common, obvious English words to see if we can get a list of the more unique words in the files.

This is called making a **stop list**. Create a list at the top of your file that contains common English words. Then, when you are reading in the file, if you see a word in that list, skip that word.

Once you have the stop list working, run your word counting program on `long.txt`. What are the 10 most common words in Shakespeare's Twelfth Night, not counting really common boring words?

*Hint*: Python supports `not in` a list. If you have a list of `stop_words`, you can say
```
if word not in stop_words:
	...
```

### Challenge 4: Top 10 words in a different Shakespeare play

Pick a different Shakespeare play that you like, and use your program to figure out the most common words in that play.   

You can find plain text copies of Shakespeare's plays on [Project Gutenberg](http://www.gutenberg.org/ebooks/search/?query=shakespeare).

Pick a play, download the "plain text" version of the play, and then run your program on that file. Make sure the file is in the same folder as the program on your computer. If you do it right, you should only have to change one line in your program.
