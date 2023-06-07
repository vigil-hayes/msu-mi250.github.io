---
topic: Testing 
git: https://gitlab.msu.edu/mi-250/testing
published: false
nav_exclude: true
visible: false
---

## Install PyTest

Today, we will be writing automated software tests.   Python comes built-in with a testing framework called
[unittest](https://docs.python.org/3.7/library/unittest.html), but we aren't going to use that.  We are going to use a
much better and easier to use system called [PyTest](https://docs.pytest.org/en/latest/).  

Before we can use it, we first need to install it.  This only needs to be done once.  On the command line, run the
command
```
pip3 install pytest
```

It should download and install the latest version of pytest.   Once it is finished, you should get your prompt back at
the command line. Next, let's check and make sure it is installed and working correctly.  The [fib.py]({% link fib.py %})
program from the readings is in the git repository for this week.  Run this command; it should run the tests and report
4 passes and 4 failures:
```
pytest fib.py
```
Note: You'll need to make sure that fib.py is in the current directory

If it runs the tests (which may take a few seconds), and then prints out that there are 4 passes and 4 failures, then it
is working.

You can also run `pytest fib_improved.py` to see all of the tests pass.

## Basic Testing

We are going to practice writing test cases for existing code.   I am going to give you pre-written functions, and you
will need to write one or more test cases -- usually automated test cases -- for those.

### Exercise 1: Basic (Level 0) Test for Cleanup

Let's start by looking at the file `cleanup.py`.  It contains a function -- `cleanup()` -- that takes a string and tries
to clean up the langauge by replacing bad words with less bad words.

Let's begin by writing a basic test for this.  There is a test function in the file -- `test_cleanup()` -- that right
now does nothing.  Let's write a test case.  In the test, call the `cleanup()` function, and give it the message "damn
this shit to hell" -- which of course has a lot of bad words in it.  Save the output from the `cleanup()` function into
a variable.  Then use `assert` to check to see if that output has had the bad words replaced -- it should now say "darn
this poop to hades".

Once you get the test written, run `pytest cleanup.py` and see if it passes.  You should make sure that your test passes
correctly before moving on.

### Exercise 2: Basic (Level 0) Test for First Word

If you look at the file `first_word.py`, it contains a function called `first_word()`.  This function takes a sentence
as a string, and it returns the very first word in the sentence.   Let's write a test for this, to see if it works
correctly.

The file contains a single test called `test_first_word()`.  Right now that function does nothing, so the test passes.
Edit that function to test the `first_word()` function.   Call the function, passing in the sentence "This is a test".
Save what the function returns to a variable.  Then check that what the function returns is correct -- it is the word
"This".

Run your test. It should fail, because the `first_word()` function is broken. 

### Exercise 3: Fix the bug in first_word

It is returning the wrong word!  Fix the function so that your test now passes.  Run `pytest` and verify that your test
now passes correctly.

## A Few More Tests

### Exercise 4: Testing how to count letters -- "HI"

Next, turn your attention to the `count_letters.py` file.  This file counts a `count_letters()` function that takes a
message and counts how many times each letter appears, and returns the dictionary with the letter counts.

Write a test for this function that passes in the word "HI" and verifies that the function reports that the word has one
"H" and one "I".  You will have to write our own test function for this.

*Note*: You are allowed to have more than one `assert` in a single test.  All asserts must pass for the test to pass. So
you can separately check the counts for 'H' and 'I' are correct.

### Exercise 5: Test repeats (Level 1 test)

Add a second test to this file that tests repeated letters.  Pass in a string that has at least one letter repeated
more than once.  Then verify that this correctly counts the number of times that letter appears.

### Exercise 6: Test empty (Level 1 test)

What happens if you pass in the empty string -- `""`?  Add a test case that passes the empty string to
`count_letters()` and verifies that it returns a reasonable answer.

### Exercise 7: Test missing (Level 2 test)

Add one more test case to `count_letters.py`.  Pass in a word to `count_letters()`.  Verify that it correctly counts at
least one of the letters.  But also pick a letter that is NOT in that word, and verify that that that letter is NOT
reported in the dictionary that is returned.

By this point, you should have 4 separate tests in `count_letters.py` that all pass when you run it with `pytest`.

*Hint*: You can do `assert key in dict` or `assert key not in dict` -- in general, anything you would use in an `if`
statement, you can also do in an `assert`.


## Testing Output

Much of the code we've written so far in class has been creating output -- for example, the `print()` statements for our
choose-your-own adventure program or our conversational agent program.   We can test this code by "capturing" the output
from the print statements into variables, and then checking whether that output is what we expect it to be.

To capture output, we use the `capsys` functionality of pytest.  We add a parameter to our test called `capsys`, which
will cause pytest to capture all print statements.   Then we can retrieve that output by saying `captured =
capsys.readouterr()`.  THen we can access the actual output with `captured.out`.  He is an example test that just prints
the word hello, and verifies tht it prints correctly:

```
def test_print(capsys):
	print("hello")
	captured = capsys.readouterr()
	assert capured.out == "hello"
```

### Exercise 8: 99 bottles

If you look in the file `bottles.py` you'll see a function that prints out one verse of the song [99 bottles](https://en.wikipedia.org/wiki/99_Bottles_of_Beer).  

Write a function that tests this by picking a verse number (e.g. verse 75), calling the bottles function, capturing the output, and the
verifying that the output looks like what it is supposed to look like.

### Exercise 9: 9 bottles

The bottles function does something different for verses less than 10.  Write another test to verify that a verse less
than 10 (e.g. 9) prints out the alternate version of the song.


## Testing Input

We also write a lot of code that gets inputs from users.   How do you test that?

The easiest way to test that is to replace the `input()` function with another function that returns a pre-specified
string.  This way, when your program calls `input()`, it won't actually ask the user; instead, it will just pretend the
user typed something in and return what you tell it to.  This is called *mocking* the input.

To do that, we use a feature in pytest called monkeypatch.  Put one line at the beginning of your test to replace input
with whatever you want it to be:

```
def test_input(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda x: "Rick Wash")
	name = input("What is your name? ")
	assert name == "Rick Wash"
```

### Exercise 10: Test the Flashcard

The file `flashcard.py` has a function that contains a single flashcard, much like the flashcards you made in week 2
studio.  It asks the user a riddle, waits for the user to respond, and then returns either the word "Correct" or
"Incorrect" based on what the user entered.

Test that this flashcard works correctly.  If the user enters "mountain" (the correct answer), then the function should
return "Correct".  If the user enters anythign else, it should return "Incorrect". 

You will need at least two tests to test this -- one that tests a correct answer, and one that tests an incorrect
answer.

## Testing Your Own Code

It is easier to write tests once you have a program working.  But which comes first, the test or the program?   If you
google this question, you'll get **thousands** of very long, heated discussions online.  This is a subject of much
debate among programmers.

Still, this is something you will need to deal with. So for this next exercise, you will need to write BOTH the main
function code, and the test code.

### Exercise 11: Nth word

Write a function that extracts the nth word from a sentence.  That is, if I give you the sentence "this is a sentence"
and ask for the 4th word, it should return "sentence".   If I ask for the 2nd word, it should return "is".  Look at the
code in `first_word.py` as a good place to start.

Also, then write one or more tests for your nth word function to verify that it works correctly.

It is up to you whether you write the test first, write the main code first, or do them both at the same time.   Think
about which way makes most sense to you.  Do you write the code first, and then test it to make sure it works?  OR, do
you write the test first, so you know what it needs to do, and then write the code so that it matches what the test says
it should do?

*Hint*: Start by making a list of what kinds of things you can test.  Then write your "nth word" function to be easy to
test in that way.  Focus on Level 0 and Level 1 tests.   Try to find ways that the function is supposed to work
correctly, and test that it does.  


## Manual Test Cases for Turtle Graphics

We've now written a lot of automated tests, spread across a bunch of different files.  Run the command
```
pytest bottles.py cleanup.py count_letters.py fib_improved.py first_word.py flashcard.py
```
It will go through all of the files that have tests in them, and then run ALL of the tests you've written.  Very hand
way to check all of your code.

However, there's one thing we've done a lot of in this class that we haven't written tests for: turtle graphics.   It is
actually pretty hard to write tests for turtle graphics, because the output is on the screen.

Instead, we usually do manual tests for turtle graphics programs. So far, you've just run the program over and over and
see if you like what is looks like.  Let's be more rigorous than that.   Let's create some very specific manual tests
where the program draws something, and then we explicitly write down what we expect it to draw.   That way, someone can
look at the expected output and decide, for each drawing, whether it "passes" or "fails".

### Challenge: Stars

In your folder for this week, there is a `star.py` program.  That program contains a function that draws a star of
different sizes and colors.

Create 3 manual tests for this star function.   One test should be a Level 0 test -- give it a reasonable size and
color, and see if it works.   The other two tests should be Level 1 tests -- give it a different size, and a different
color, and see if it draws the star appropriately.

For each test case, explicilty write down what parameters to give the function, and what you *expect* the program to
draw.  They should be paired -- so these parameters should draw this output. It is OK to write this on a piece of paper
-- just take a photo of it with your phone to turn it in.

Then modify the program to draw the 3 test cases on the screen.   Then run your test manually -- look at the output, and
decide for yourself whether what it drew matches what you expected it to draw.   Write down whether each test cases
passes or fails.


### Challenge: Level 2 tests for nth_word

As a second challenge, try to write one or more tests for your `nth_word()` function that tests errors -- aka Level 2
tests. Think about inputs to your `nth_word()` function that might be invalid.  What happens if someone asks for the 5th
word in a sentence that only has 4 words?  What happens if someone asks for the 'a'th word instead of the '1'st word?  
What happens if someone asks for the '-1'st word?   (is that actually an error?)  

In each of those cases, think about what you think *should* happen, and then write the test to test whether that
actually happens or not.  If it doesn't happen, it could be because the function is broken.  Or it could be because your
understanding is incorrect, and the test is helping you to see what is wrong.  

