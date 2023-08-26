---
parent: Week 12
topic: Reading and Writing Files
git: https://gitlab.msu.edu/mi-250/working-with-files
nav_exclude: true
visible: false
published: false
---

## Word Counter

For this series of exercises, we are going to build up a program that counts words in a file and saves the results to
another file.

### Exercise 1: Print out a file's contents

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

### Exercise 2: Print line numbers

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

### Exercise 3: Print out the total number of lines in the file

Modify the program to print out how many lines are in the file at the very end.  This should be pretty easy if you
finished the previous exercise.  The total number of lines is the line number for the last line, right?

```
There are a total of 4 lines in this file
```

### Exercise 4: Count the total number of words in the file

Modify the program to count the total number of words in the file.  Your program should take each line, split it into separate
words, and count the words in the file.  Your program should print out the total count after it is finished reading the whole
file in.

If you have a variable that contains a string, you can split that into separate words using the
[`.split()`](https://docs.python.org/3.8/library/stdtypes.html#str.split) function.   

```
words_list = line.split()
```

Once you have them in a list, you can then count them: `len(list)` returns the length of list (the number of items in
that list).

```
number_of_words_in_line = len(words_list)
```

### Exercise 5: Change the file you read from

Right now, the program always reads the same file -- 'short.txt'.   Modify the program so that when you run it, it
instead reads in the file 'medium.txt', prints it out with line numbers, and calculates information for that file
instead.


## Make the program do more interesting things

### Exercise 6: Count how many of each word

In all of the exercises you have done so far, you should just be counting the *total* number of words.

Back in [week 9](../9/lab.html), you wrote some code that would count how frequently a word appears in a string.  And in
week 10 during [Exercise 7](https://gitlab.msu.edu/mi-250/reading-code/-/blob/master/ex7.py), you read code that
includes the `count_words()` function that takes a string, and returns a dictionary of all the words with the number of
times that word appears.

For this exercise, modify your program to instead count how many times each word appears.  You should have a separate
count for each word.  You are welcome to use the `count_words()` function to do the counting, or write your own.

Your program should print out a dictionary that has the count of the number of times each word appears in the file, and
print out that dictionary.

When I run mine on "short.txt", these are the counts I get:
```
{'All': 1, 'the': 2, "world's": 1, 'a': 1, 'stage,': 1, 'and': 3, 'all': 1, 'men': 1, 'women': 1, 'merely': 1, 'players.': 1, 'They': 1, 'have': 1, 'their': 2, 'exits': 1, 'entrances;': 1, 'And': 1, 'one': 1, 'man': 1, 'in': 1, 'his': 1, 'time': 1, 'plays': 1, 'many': 1, 'parts': 1}
```

### Exercise 7: Sort the words by frequency

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

### Exercise 8: Top 10 most common words

Modify your program to only print out the 10 most common words that appear in the input file, and write out those 10
words to the output file.   

You should be able to do this by keeping a separate counter, and then using `break` to stop the loop after you've
printed out 10 words.

### Exercise 9: Stop List

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

## Command Line Parameters

### Exercise 10: Change the file you read from, pt 2

Right now, every time you run the program, it always reads the same file -- 'medium.txt'.  And to change this, you have to
edit python code.   Modify the program so that when you run it from the command line, you can tell it which file to read
and measure.  It should work like this:  

```
python3 wordcount.py medium.txt
```

You should be able to tell it to calculate word counts for either the short or the medium files, and it should count the
number of words correctly.

Be sure that your programe will change which file it reads based on the command line. Everything on the command line is
in a list called `sys.argv`, which you can access after you `import sys`. This is a list, so the first item in the list
is probably "python3", the second item is "wordcount.py", and the 3rd item is probably the name of the file you want to
read.

Your program should not contain the actual name of the file.  Instead, it should always get the name of the file from
the command line, and once your program is finished, the same program can be used to measure different files without
having to edit python code.

*Hint*: You should refer back to the reading this week about using command-line parameters.  You will need to include a line
like `input_filename = sys.argv[1]` to get the filename from the command line.

### Exercise 11: Write the results to a file

In the previous exercise, you calculated the number of words in a file, and printed out the results to the screen.  For
this exercise, instead of printing it out to the screen, you should have your program write that out to a second file
called `output.txt`.

You will need to open that file for writing before writing the results.  Look at how we opened a file before for
reading.  You will need to open a new file, and change it so that it is opened for writing.

Once you have a file open for writing, the easiest way is to use the normal `print()` function, but to add a
file parameter.  So:
```
print("this will be written to the file", file=f)
```

### Challenge 1: Change the file you write to

Add a second command line parameter -- the filename to store the output to.  This way, you can run your program and tell
it which file to read and which file to write.

Once you get this working, run this on the file `long.txt` and save the word counts to `long-output.txt`:
```
python3 wordcount.py long.txt long-output.txt
```

Don't forget to save your output.txt and long-output.txt to your git repository.  Also, always close your output file
before running your program, and then open it up to look at it after running to make sure it contains what you think is
the correct output.

---

### Challenge 2: Top 10 words in a different Shakespeare play

Pick a different Shakespeare play that you like, and use your program to figure out the most common words in that play.   

You can find plain text copies of Shakespeare's plays on [Project Gutenberg](http://www.gutenberg.org/ebooks/search/?query=shakespeare).

Pick a play, download the "plain text" version of the play, and then run your program on that file.  If you do this
right, you shouldn't have to change your code at all; you should just be able to specify the filename on the command
line.

### Challenge 3: Append to the output

Modify your program so that when you run it, instead of overwriting the output file, it appends to the output file.
That is, it takes what is already in the file and writes  your new top-10 list to the end of the file, keeping the old
outputs there.   This can be done by only changing one or two characters in your program.

### Challenge 4: Zip

Write a program that takes the names of three different files on the command line. It should then read a line from the
first file, and write it out to the 3rd.  Then read a line from the second file, and write it to the third.  Then read
another line from the first file, and then from the second file.  Back and forth.  Basically, it reads in the first two
files, and write out to the third file alternating lines, like a zipper.  So the third file should look like this:

```
First file, line 1
Second file, line 1
First file, line 2
Second file, line 2
First file, line 3
Second file, line 4
```

Think about what happens when one file is longer or shorter than the other file.




