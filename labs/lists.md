---
parent: Week 6
topic: Using Lists
git: https://gitlab.msu.edu/mi-250/random-lists
nav_exclude: false
visible: true
---

{% capture _ %}{% increment exercise5 %}{% endcapture %}

## Names, names, and more names

### Exercise {% increment exercise5 %}: Add your names to a list

Start by running the program `names.py`.  This prints out a list with the names of the instructor and TA for this class.

Add both your name to the list, and your partner's name to the end of the list.  Run the program and make sure it prints
out all four names correctly.

### Exercise {% increment exercise5 %}: Adding another name

You have hard coded a set of names in the program by explicitly specifying a list.  However, you can also get python to
add things to a list using `.append()`.  So if you have a variables called `stuff` that contains a list, and you want to
add "basketball" to that list you can say:
```
stuff.append("basketball")
```
Of course, you can replace "basketball" with a variable that contains a string also.

Use this to modify your program to ask the user for another name with `input()`.  Then `.append()` that name to your list, and print
out the full list with 5 names on it.

### Exercise {% increment exercise5 %}: Alphabetical order

The function `.sort()` will sort any list you have. By default, it sorts things alphabetically, with all the capital
letters coming before any lowercase letter.  So if you have a variable *stuff* that contains a list, then you can say
`stuff.sort()` to sort that list.

The names program should print out 5 names now.  Modify the program to sort the names, and print out the list of names
in alphabetical order.   Test your program by entering in different names, and seeing if it sorts them differently.

### Exercise {% increment exercise5 %}: Beginning of the Alphabet

In your program, you can retrieve specific items from the list using `[]`.  So, to get the 2nd item from the list
`stuff`, you can say `stuff[1]`.  (Note: Lists in python always start at 0, so 0 is the first item, 1 is the second, and
so on.)

Modify your program to print out only one name: the name that comes *first* in alphabetical order.

### Exercise {% increment exercise5 %}: End of the Alphabet

Having a last name like "Wash" means that I always end up at the end of any list of alphabetical order.  So let's give
some love to the end of the alphabet.  Change your program so it prints out the person's name who appears last in
alphabetical order.

*Hint*: Modify your program so it prints out the name that appears last in the list, after the list has
been sorted into alphabetical order.  OR, first in the list after sorting by reverse alphabetical order.

## Random Number Generator

Next, we are going to use the `random` package to build a couple of useful tools to help us make choices.  As a
reminder, before you can use the random package, you need to `import random` into your program.  I usually put the
import lines at the beginning of my program.

The git repository has a really simple coin flip program called `coin.py`.  Run this program. What happens?  Run it
again.  Does it always print out the same thing? Now, open up the code and look at how it works.

Notice that you had to run the program more than once to see what it was doing.   That is true in general when dealing
with randomness; you have to run the program more than once to verify that the random numbers are working correctly.

### Exercise {% increment exercise5 %}: Random Number Generator

Coin flips are great when you only have 2 options to choose from.  But sometimes you have more than two options to
choose from.  The program `rand_num.py` assumes you need to choose among 5 things, and picks a random one of those 5 things.  

Modify this program to ask the user how many things they are trying to choose between.  It should then
pick a random number between 1 and that number and print it out, to help the user make a choice. For example, if the
user is trying to decide between 6 things, the program will ask how many things, the user will enter "6", and the
program should pick a random number between 1 and 6

Note: Remember the difference between strings and integers.   When a user enters a response to `input()`, it comes as a
string.  If you want to use it as a number, for example in a `range()` command, then you need to convert it to a number
with `int()`.

Note 2: Remember to run the program more than once to make sure it's giving you a random number.

## Combining Loops and Randomness

### Exercise {% increment exercise5 %}: Coin flipper

The `coin.py` program flips a single coin and prints out either heads or tails.  Let's test to see if this program is
biased. Modify the program to flip the coin 20 times and print out the results of each flip.

*Hint*: You will need to use a loop for this.  Look back at the [for loop lab](../4/lab.html) for help.

### Exercise {% increment exercise5 %}: Coin flipper pt. 2

Modify your coin flipping program to count how many heads and tails it gets.  At the end of the program, it should print out the counts
-- how many heads came up, and how many tails came up.

*Hint*: You can use a counter to do this (which is sometimes known as an "accumulator").  You create a variable, and
then set it to zero as a place to start.  Then, each time through a loop, you add one to it.  Something like this:
```
counter = 0
while looping:
	counter = counter + 1
print(counter)
```

*Hint 2*: Sometimes you don't want to count every time in a loop, but only some loops (like the loops where it comes up
heads).  You can use an `if` statement to only add one to the counter when that happens.


### Exercise {% increment exercise5 %}: Coin flipper pt. 3

Modify the program to ask the user how many times it should flip the coin.  Then have the program flip a coin
that many times, and count how many heads and tails it gets.  At the end of the program, it should print out the counts
-- how many heads came up, and how many tails came up.

Note: Remember the difference between strings and integers.   When a user enters a response to `input()`, it comes as a
string.  If you want to use it as a number, for example in a `range()` command, then you need to convert it to a number
with `int()`.

Be sure to commit your changes to the git repository.  Also, if you haven't already, now is a good time to swap driver
and navigator.



<!-- End from lab-3 -->
## Choosing a restaurant

It is always difficult to choose where to go for lunch when you are with a bunch of friends.  We are going to build a
restaurant choosing program to help with the choice.  Let's start by looking at `restaurant.py` and running it.  It
should ask the user for 3 restaurants, and then just print out that list.

### Exercise {% increment exercise5 %}: User experience of counting

Python counts starting a zero: 0, 1, 2, 3, ...  Regular human beings, on the other hand, start counting at 1: 1, 2, 3,
4, ...

Right now, the program asks for "restaurant 0" first.  Modify the program so that it looks like human beings would
expect, starting with 1.

Note: the program should still ask for 3 restaurants.

### Exercise {% increment exercise5 %}: Random Choice

The function `random.choice()` will pick a random item out of a list, and return that item.   So if you have a list of
`stuff`, you can say `random.choice(stuff)` to get a random thing out of that list.

Modify the restaurant program to use this to randomly choose a restaurant for lunch, and print out which restaurant the
computer chose.

Note: Remember to import the random library (`import random`) at the beginning of your program.

### Exercise {% increment exercise5 %}: More (or less) than 3

This is where lists really shine. Lists are great because you don't have to know ahead of time how many items are going
to be in the list.  They get bigger or smaller as needed.

Right now, the `restaurant.py` program always asks for exactly three restaurants.  In programmer terminology, we say
that "three" is "hard-coded" into the program.

Modify the program to ask the user how many restaurants they are thinking about for lunch, and then have it ask them for
that many restaurant names, and then pick a random restaurant from that list.    So if they say they are thinking about
`5` restaurants, your program should ask them for five names of restaurants, and then pick from among those five.  If
they say `2`, it should only ask them for 2 names. 

Here is a potential use of the program:
```
How many places are you thinking about for lunch? 4
Enter the name of restuarant 1: Jimmy Johns
Enter the name of restuarant 2: Chipotle
Enter the name of restuarant 3: Five Guys
Enter the name of restuarant 4: Noodles and co.
You should go to Noodles and co.
```

Note: Remember the difference between strings and integers.   When a user enters a response to `input()`, it comes as a
string.  If you want to use it as a number, for example in a `range()` command, then you need to convert it to a number
with `int()`.

Note 2: Notice that I made the program a little more user friendly by printing out the words "You should go to" in
addition to the final choice.  It is always a good idea to try to make things easier for your users to use and
understand.

## Challenges

The following exercises are related to the ones above, but a little more uncertain.  As you get further into
programming, you get fewer and fewer directions for how to do things, and have to do more work to figure it out
yourself.  Try these exercises, and feel free to talk to your peers or your instructors as you think through how you
want to make these work.


{% capture _ %}{% increment challenge5 %}{% endcapture %}
### Challenge {% increment challenge5 %}: Homework Chooser

A problem that many students have is choosing which class's homework to do next.   Write a homework chooser that asks
the student which classes they currently need to do homework for, and then randomly chooses which order the student
should do homework.

*Hint*: `random.shuffle(list)` will randomly re-order a list.  Picture in your head putting each item in your list on a
separate index card, and then shuffling the deck of index cards.

### Challenge {% increment challenge5 %}: Infinite coin flipper

Make a copy of your coin program and call it `infinite.py`.  Modify the program so that it keeps flipping coins as long
as the user wants it to.  It should flip a coin, and then ask the user if it should continue.  Unless the user says no,
it should go and flip another coin.  Then ask the user again.  It should keep doing that until the user says "no".

As a bonus, get the infinite coin flipper to print out counts of how many heads and tails it flipped so far.

Don't forget to add this program to your git repository.

*Hint*: `while true:` will loop forever.  You can break out of a loop with the `break` command.

```
Heads
Should I continue? yes
You have flipped 1 coins
1 have come up Heads
Which is 100%
Tails
Should I continue? yes
You have flipped 2 coins
1 have come up Heads
Which is 50%
Heads
Should I continue? yes
You have flipped 3 coins
2 have come up Heads
Which is 66.66666666666666%
Heads
Should I continue? yes
You have flipped 4 coins
3 have come up Heads
Which is 75%
Tails
Should I continue? no
```

### Challenge {% increment challenge5 %}: Unlimited Restaurant Options

Your restaurant choosing program asks the user to pre-specify how many options there are.  I don't know about you, but
when I'm hungry and trying to decide where to go, I can't figure out how many options there are.  That's just too much
advance thinking.  

Modify your program so that it doesn't need to ask ahead-of-time for the number of restaurants.  The user should be able
to just keep entering restaurants until they type "done" or just hit enter or something.  Then it will randomly choose
one of the ones they entered and print it.  The program should still accept as many restaurants as they want.

Here is an example output:
```
Enter the name of a restuarant: Culvers
Enter the name of a restuarant: Chipotle
Enter the name of a restuarant: Jimmy Johns
Enter the name of a restuarant: No Thai!
Enter the name of a restuarant: Potbellys
Enter the name of a restuarant:
You should go to No Thai!
```

### Challenge {% increment challenge5 %}: Random 99 bottles

Two weeks ago in Lab 4, we wrote a program that sings the song "99 bottles". The last exercise introduced a new way to
sing the song -- a change to the 3rd line.

Modify the 99 bottles program to randomly choose which version of the verse is sung, for all verses.  When
you do this, store the possible verses in a list, and then use `random.choice()` to choose which one to sing.


