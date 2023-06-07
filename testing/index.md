---
layout: home
title: Software Testing
nav_exclude: true
---

Software Testing
================

## Exercise: What is a bug?

Software testing is the process of finding and eliminating bugs in software.  Take a minute and write down your answer
to the question "What is a bug?".  Go ahead; I'll wait.

Computer programs are written with goals in mind; the program is supposed to do something specific.   A bug is anytime
that the program doesn't do that.  That is, a bug is anytime there is a difference between what the program is *supposed
to do* and what the program *actually does*.

As computer programs get more complicated, so do the bugs.   A simple computer program often only does one thing.  If it
does that then, then great; it works.  When you make computer programs more complicated, they have to work in a wider
variety of different settings.  Different people might enter in different inputs.  The program has to work with
different types of data.   The program has to work on different computers (Mac vs. Windows) with different size screens
and other differences.  Bugs may appear only in some circumstances but not others -- it may work fine for you on your
computer, but not for me on my computer.   But still, that's a big problem for me!   (AND, also, a problem for you if
you want me to pay you for the computer program....)

### Fixing Bugs

When people write programs, they often think that they should try to write programs that don't have bugs.  But, that's
impossible!  They also think that programs aren't done until they are bug-free.  That's also impossible!  Microsoft
Windows shipped with millions of known bugs that were not fixed.   People still bought it and use it on a regular basis.
Fixing every bug is hard, and often not worth the time and effort.  

If a bug is any time what the program *actually does* is different than what the program is *supposed to do*, then there
are two ways to fix a bug:
1. Change what the program actually does.  Modify the code so that the program does what it is supposed to do.
2. Change what the program is supposed to do.  Change your idea of what the program is supposed to do and what kinds of
   things it can and can't do.  (and, if applicable, change the written specification)

Both are entirely reasonable ways to fix a bug.   Also, it is reasonable to choose to *not* fix a bug; just acknowledge
that it exists but that it isn't worth fixing.

## Why Test?

Computer programs do not always work as the programmer intends them to.  Often, I write code that I think does one
thing, and then when I run it, I find out that it does something else.  This is a very normal thing to happen, and every
programmer experiences it on a daily basis. Testing is really an attempt to understand what your program *actually*
does. Testing is a way to better understand the program that you've written and what it can and cannot do.

**Testing** is the process of trying to find bugs.   Testing does not necessarily involve fixing bugs.  Instead, you
test your program to try to learn about the bugs that exist. This gives you the information you need to decide whether
it is worth fixing the bugs or not.  

### Automated vs. Manual testing

There are two major ways of doing testing: manually testing the program by running it and entering inputs on your own,
and automated testing by writing a 2nd program that tests your 1st one.

You are already familiar with **manual testing**.  You do it all the time.  You write code, and then you run the code
and see what happens.  You have some idea in your head about what the program *should* do, and then you run the program
and see what the program actually does.  Often, this isn't a very structured or formalized process, but you still do it
all the time.  You run your program over and over, adding code and trying different inputs, to see what happens.  This
is manual testing.  

It is possible, and not uncommon, to do more structured manual testing.  Rather than just ad-hoc running your program,
you could think carefully about what kinds of inputs your program might get, and then write down a list of possible
inputs.  Then you could think about, for each input, what *should* the program do?   Write that down next to the input.
Rather than having some vague notion about what the program should do, you now have explicitly written down the expected
output.  Now you can run the program multiple times, and see if what the program does matches what you wrote down that
it should do.

This structured, manual testing is quite common in the real world.  Large companies pay people to run these structured
manual tests and figure out if the program does what it is supposed to do.  Some things, like user interfaces, are
difficult to test automatically, and mostly are tested this way.

However, running through these tests manually is hard and boring work -- especially if you have to do it frequently.
So, programmers often do what they are good at -- they write a computer program to automatically run tests and check if
the program does what it is supposed to do.  **Automated testing** invovles using one computer program to test another,
and is an extremely common way to do testing.  As programs get bigger and bigger, automated testing becomes more
important.


### Regression bugs: bugs that appear later, breaking previously working code.

As you work on writing computer programs, one thing that you notice is that you change things in one place, and it
affects other parts of the program.  That is, it is possible (and common) that one part of the program works fine NOW,
but later on you change something else and now that part no longer works.  When this happens, it is called a "regression
bug".

Regression bugs are really nasty, because they mean that you tested the program and it worked, but then later on it
stopped working.  The only way to catch regression bugs is to re-run all of your tests again, to make sure that the
program still does everything it is supposed to.  But doing that is a real pain.   That's one of the big reasons that we
automate tests; it is much easier to re-run tests if they are automated and can be run with a single keystroke.


## Test Cases and Automating Tests

In order to think about how to test software, we break our program down into test cases.  Each case tests one specific
feature or function of a program, and a single input to that part of the program.  To test a program you've written, you
will normally have many different test cases that test different parts of the program with different inputs.
Basically, test cases break the job of software testing into discrete, managable parts.

### What is a test case?

A test case is a well-specified set of inputs and expected outputs.   Above, I talked about how you could write down an
input to your program, and then also specify what the output should be.  That is a single test case.   The trick with
test cases is to be very specific.  You are testing a very specific, logical piece of functionality of your code with a
well-defined input and well-defined expected output.  If your test case is specific enough, then it should be easy for
anyone to tell whether the actual output matches the expected output; that is, you can tell whether the test case
"passes" or "fails".

### Automated test cases: Easy to run over and over

When we are writing automated tests, we usually break our tests into test cases.  One function executes exactly one test
case, and then decides whether that test passes or fails.   

For example, let's pretend we have a really simple function called `add()` that takes two numbers and adds them
together.   If I add `1` and `2` together, I would expect to get `3`, right?   We can make that into a test case -- if I
call `add(1,2)`, then I would expect the result to be `3`.   

To do testing, we use the `assert` command in Python.  Assert means to test and see if the result is what is expected.
So, a really simple automated test case for the `add()` function would be:
```
def test_add():
	result = add(1,2)
	assert result == 3
```

In this case, the code is a test because the function name starts with `test_`.  It runs the `add()` function with `1`
and `2` as parameters, and then stores the actual result that is calculated in a variable called `result`.  Then it
checks (*asserts*) that this result is equal to 3 -- the expected output.  If it is equal, then we say that the test
case "passes", and the result is what we expect.  If it is not equal, then we say that the test "fails" because it is
not what we expected.

This is a single test case.   If I wanted to test a different set of inputs, that would be a separate test case.  So if
I also wanted to check that adding `0` and `0` results in `0`, here is a second test case:

```
def test_add_zero():
	result = add(0,0)
	assert result == 0
```

### Testing harness: runs a collection of test cases and produce output reports

Now we have more than one automated test case.  What if we want to run all of these tests, and collect the results into
a single output that is easy to read? That is the job of a *test harness*: a program that runs automated tests for us
and reports on their results.   In python, a common test harness that is built in is called **UnitTest**.  There are
other ones that are commonly used also, such as **pytest** or **nose**.

## Types of Tests


Most software has a large number of tests associated with it.  It is not uncommon for the test code to be more lines of
code than the code that is being tested.  Now, the next question is what kinds of test cases should we create?  How do
we think about what to test?

What follows is one way to think about what to test.  It is not the best way, and it is certainly not the only way.  But
it is a useful way to organize your thinking.

To help illustrate, I will be writing tests for a function that generate [Fibonacci
numbers](https://en.wikipedia.org/wiki/Fibonacci_number) -- a sequence of numbers that goes 1, 1, 2, 3, 5, 8, 13, 21,
34...  Each number in the sequence is the sum of the two previous numbers.   The function takes as a parameter which
number in the sequence it should generate (the 1st number, or 3rd number, or what), and it returns that number.  Here is
an implementation of that function:
```
def fib(n):
	if n <= 2:
		return 1
	return (fib(n-1) + fib(n-2))
```
For the first two numbers (n=1 and n=2), it returns a hard coded 1.  For each number after that, it calculates the 
two previous numbers and adds them together.

This is just an example function.  We could write tests for almost any function we create.

### Level 0: Basic Functionality

The first types of test cases that I write are called "Level 0" tests.  These test the most basic functionality; if
these fail then the function is hopelessly broken and needs to be fixed.  Level 0 tests should test the one or two most
common use cases of a function to make sure that it works correctly with completely normal input.

For the Fibonacci function, a very normal use is to ask it for the 3rd or 4th number.  Let's pick one -- the 4th number.
Looking at the Wikipedia page for Fibonacci nunbers, it looks like 4th number is `3`.  So we would expect `fib(4)` to
result in 3.   We can write this as a test case:

```
### Level 0 tests
def test_fib_3():
	assert fib(4) == 3
```

Usually we don't have many level 0 tests.  We write level 0 tests just to check and make sure that the most basic
funcationality works.  If there is a syntax error, or if `fib()` does something unrelated to Fibonacci numbers, or if I
forgot to write the code for `fib()`, then this test will catch that.  All it does it make sure that the most normal,
basic way of using the function works.

### Level 1: Full Range of Functionality and Edge Cases

Once the Level 0 tests are passing, we know that the basic function works.  The next thing I do is write Level 1 tests.
These tests look at the full range of functionality to try to identify what are the edge cases and different types of
inputs that the function should handle.  We should use our knowledge of the function to try to identify tricky cases,
and test those to make sure they work.   However, all of the Level 1 test cases should be *valid* cases, in that they
ask the function to do things that it normally would be expected to do.

For the `fib()` function, what are some tricky cases that it needs to handle?  Well, the first two Fibonacci numbers are
always tricky, because they are different than the others.  The first number should be `1`, and the second number should
also be `1`.  Let's write a couple of tests for those:

```
# Level 1 tests
def test_fib_1:
	assert fib(1) == 1

def test_fib_2:
	assert fib(2) == 1
```

Are there any other trick cases?   Let's pick a higher nunber, and make sure that it does calculations accurately.
Looking at the Wikipedia page for [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number), the 10th number
is `55`.  So let's check that to make sure it calculates larger and more complicated numbers correctly:

```
def test_fib_10():
	assert fib(10) == 55
```

Ideally, you want to keep writing Level 1 tests until you've tests the full range of valid inputs -- long inputs, short
inputs, big numbers, small numbers, blanks, etc.  Everything that is valid, you should write a test for to make sure
that it works.

### Level 2: Error conditions

Almost all programs have invalid inputs -- inputs that are considered to not be legitimate.  However, sometimes the user
ends up providing an invalid input.  Good programs detect that the input is invalid, and handle it appropriately (for
example, by displaying an error message).  

Level 2 tests test these invalid inputs.  They intentionally provide invalid inputs to the program, and then check to
make sure that the program does something reasonable with that input. 

For example, the `fib()` function only really produces sensible outputs for positve, whole numbers. If you enter a
negative number, or if you give it a fraction, it doesn't know what to do.  

What should it do?  Often, when writing test cases, you realize that you don't know what a program *should* do.  If a
bug is when what the program *actually* does is different than what the program *should* do, then it is a problem if you
don't know what the program should do!

This is surprisingly common, to not know what the program should do.  This is another benefit of testing -- it forces us
to think through all of the things that can happen, and try to figure out what we want to the program to do in each of
these situations.  For the Fibonacci function, what do we want the program to do if it gets an invalid input?  Let's say
that is *should* throw an `IndexError` any time it gets an invalid input.

Now that we know what it should do, we can write some tests for some invalid inputs.  We can use `pytest.raises()` to
check and make sure that that error is raised.  The test fails if it does NOT raise that error, and it passes if it does
create that error:

```
# Level 2 tests
def test_fib_negative():
	with pytest.raises(IndexError):
		fib(-1)

def test_fib_fraction():
	with pytest.raises(IndexError):
		fib(2.5)

def test_fib_string():
	with pytest.raises(IndexError):
		fib("hi")
```

If you run these tests with our `fib()` code above, you'll see that these Level 2 tests fail!  Uh oh!  We have found
some bugs in our code -- it doesn't handle error conditions very well.  First, we need to decide if we care -- is this a
bug that is worth our time fixing?  If it is, then we need to change our `fib()` code to make it do the right thing.

### Level 3: Performance and Scalability

Once all of the tests for Levels 0, 1 and 2 are passing, then the program mostly works correctly -- it does what it is
supposed to do.  However, that's not quite enough.  There are usually other goals that programs have -- for example,
running fast enough that the user doesn't get bored.  Level 3 tests test these other, non-correctness features of
programs.

For example, it is a problem if it takes minutes to calculate our Fibonacci number.  That's not good.  The computer
should be able to calculate it in less than 10 seconds.  So let's write a test to check this:

```
# Level 3 tests
def test_fib_speed():
    start = datetime.datetime.now()
    out = fib(40)
    end = datetime.datetime.now()
    assert (end-start).total_seconds() < 10  # It should take less than 10 seconds to compute
```	

### Example

You can download these examples [here](fib.py).  This file contains the basic `fib()` function, and all of the tests
listed above.  To run it, use the command:
```
pytest fib.py
```

OR, alternatively, you can run it with
```
python3 -m pytest fib.py
```

When you run it, you should see that four of the test fail!   Our `fib()` function only passes half of the tests. As an
exercise, can you fix it so that all the tests pass?   ([Solution](fib_improved.py))

## Testing an Application

When testing a whole program or large application, there are some additional considerations.  Specifically, it is really
valuable to distinguish between *unit tests* and *integration tests*.

### Unit tests
Most programs are split up into smaller, logical units of functionality. A unit test tests a single, small unit of
functionality.  Often, we do this with functions; a unit test can test that a function works correctly.   All of the
tests we wrote above for the `fib()` function are unit tests -- they test a small unit of functionality that is (most
likely) part of a larger program.

Unit tests are very common, and the majority of automated tests that are written are unit tests.  Unit tests are great
for catching regression bugs and for helping us to think through program and make sure that we cover everything it is
supposed to be able to do.

### Integration tests

However, it is possible that all of the individual pieces work correctly on their own, but that they don't fit together
properly.   That is where integration tests come in.  Integration tests look at the program as a whole, and make sure
that the pieces all fit together properly in a way that works.  

The most common way to create an integration test is a *user script* -- write a script of what the user would do when
using the application as a whole, and then annotate the script with what is expected to happen at each stage. User
scripts can capture the overall functionality of a program in a way that unit tests don't.

Integration tests can be automated, and many good integration tests are.  But often, we also do integration tests as
manual tests, running through the application and making sure that it works as a whole.

#### Exercise

You can try to complete the [testing lab](lab.html).

