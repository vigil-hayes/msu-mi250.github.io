---
parent: Week 6
topic: Using Lists
git: https://gitlab.msu.edu/mi-250/random-lists
nav_exclude: true
visible: false
---

{% capture _ %}{% increment exercise55 %}{% endcapture %}

## Names, names, and more names

Lists are the simplist possible form of what's known as an array. An array is a data structure that allows you to store lots of different pieces of related data in a single variable. A "list" in Python is exactly like it sounds: a list of different, but related, pieces of data. For example:

```
groceries = ["apples", "cheese", "crackers"]
```

The variable `groceries` is storing a list of different things you might buy at a grocery store. You can have as many (or as few) items in a list as you want. Lists are also *mutable*, which means you can change the contents on the fly. 

Lists are always identified by the square brackets (`[]`) around the contents of the list. Whenever you see square brackets in Python, you can be sure it's a list (or, more broadly, an array) of some sort.

### Exercise {% increment exercise55 %}: Add your names to a list

Start by running the program `names.py`. This prints out a list with the names of the instructor and the course assistant for this class.

Add both your (the driver's) name as a separate to the end of the list. Run the program and make sure it prints out all 3 names correctly.

### Exercise {% increment exercise55 %}: Adding another name

You have hard coded another name into the list. However, you can also get Python to add more things to a list that already exists using `.append()`. For example, look at the `groceries` list at the very beginning of today's instructions. Say you want to add "jam" to that list. You can do that like this:

```
groceries.append("jam")
```

In `names.py`, use `.append()` to add your partner's (the navigator's) name to the list. The `names` list that prints out should have 4 names in it now.

### Exercise {% increment exercise55 %}: Add name with input

Now, go back to `names.py`. Modify your program to ask the user for another name with `input()`. Then `.append()` that name to your list, and print out the full list. It should have 5 names in it when you're done.

*Hint:* You'll want to store the user input into a variable first before you append it to the list. As an example, if "jam" were stored in a variable called `new_grocery_item`, you could also append it to the `groceries` list using the variable:

```
new_grocery_item = "jam"
groceries.append(new_grocery_item)
```

### Exercise {% increment exercise55 %}: Alphabetical order

The function `.sort()` will sort any list you have. If the list is made up of numbers, it will sort from lowest to highest. If the list is made up of words, it will sorts things alphabetically, with words that are capitalized coming before words that are lowercase. So if you have a variable `groceries` that contains a list, then you can say `groceries.sort()` to sort that list into alphabetical order.

Modify `names.py` to sort the names, and print out the list of names in alphabetical order by first name. Test your program by entering in different names, and seeing if it sorts them differently.

### Exercise {% increment exercise55 %}: Beginning of the Alphabet

With lists, you can also retrieve specific items using square brackets (`[]`) next to the name of the list.  So, to get the 2nd item from the list `stuff`, you can say `stuff[1]`. The number in the square brackets is called the *list index*. 

Modify your program to print out only one name: the name that comes *first* in alphabetical order.

*Hint:* the list index in Python *always* start at 0, so 0 is the index for the first item, 1 is the second, and so on.

### Exercise {% increment exercise55 %}: End of the Alphabet

The folks who have last names that start near the end of the alphabet always end up waiting longer. So let's show some love to the end of the alphabet. Change your program so it prints out the person's name who appears last in alphabetical order.

*Hint*: There are two ways to do this: the first is to find out how long the list is and call the last item in it, and the second is to sort the list in reverse alphabetical order to call the first item. Refer to [this week's readings]({% link readings/lists_and_randomness.md %}){:target="_blank"} for help with the second option. Google will likely be helpful, too!

## Flipping Coins

Next, we are going to use the `random` package to build a couple of useful tools to help us make choices. As a reminder, before you can use the random package, you need to add `import random` at the beginning of your program.

### Exercise {% increment exercise55 %}: Heads or tails

Open up `coin.py`. This program is supposed to flip a coin - but the program isn't finished yet. Right now it just generates a random number between 1 and 2, stores it in the variable `num`, and prints out the number it generates. Run it to see how it works - the number it prints should change if you run it enough times.

Edit the program so it prints out "Heads" if `num` is 1, and "Tails" if `num` is 2 (or if it isn't 1). 

### Exercise {% increment exercise55 %}: Coin flipper bias

The `coin.py` program flips a single coin and prints out either heads or tails. Let's test to see if this program is biased. Modify the program to flip the coin 20 times and print out the results of each flip.

*Hint*: You will need to use a loop for this. Look back at the [lab on loops]({% link labs/counting_and_loops.md %}) for help.

### Exercise {% increment exercise55 %}: Coin flipper counter

Modify your coin flipping program to count how many heads and tails it gets. At the end of the program, it should print out the counts -- how many heads came up, and how many tails came up.

*Hint*: You can use a counter to do this (which is sometimes known as an "accumulator"). You create a variable, and then set it to zero as a place to start. Then, each time through a loop, you add 1 to it. It looks something like this:
```
counter = 0
while looping:
	counter = counter + 1
print(counter)
```

*Hint 2*: you'll likely need two counters: one for heads, and one for tails. Where should the counter for tails go in the code if you only want it to go up whenever the coin is tails?

### Exercise {% increment exercise55 %}: Coin flipper user input

Modify the program to ask the user how many times it should flip the coin. Then have the program flip a coin that many times, and count how many heads and tails it gets. At the end of the program, it should print out the counts -- how many heads came up, and how many tails came up.

*Hint:* Remember the difference between strings and integers. When a user enters a response to `input()`, it is stored as a string. If you want to use it as a number, you need to convert it to one using `int()`.

## Choosing a restaurant

It is always difficult to choose where to go for lunch when you are with a bunch of friends. We are going to build a restaurant choosing program to help with the choice. Let's start by looking at `restaurant.py` and running it. It should ask the user for 3 restaurants, and then print out the list of restaurants.

### Exercise {% increment exercise55 %}: User experience of counting

Python counts starting a zero: 0, 1, 2, 3, etc. Regular human beings, on the other hand, start counting at 1: 1, 2, 3, 4, etc.

Right now, the program asks for "restaurant 0" first.  Modify the program so that it looks like human beings would expect, starting with 1.

*Hint:* the program should still ask for 3 restaurants.

*Hint 2:* In `for i in range(3)`, `i` is a variable that changes value each time the loop is run. Where is that value showing up in what prints out as the program runs? Note where `i` is being used *inside* the for loop.

### Exercise {% increment exercise55 %}: Random Choice

The function `random.choice()` will pick a random item out of a list, and return that item. So if you have a list of `stuff`, you can say `random.choice(stuff)` to get a random thing out of that list.

Modify the restaurant program to use this to randomly choose a restaurant for lunch, and print out which restaurant the computer chose.

*Note:* Remember to import the random library (`import random`) at the beginning of your program.

### Exercise {% increment exercise55 %}: More (or less) than 3

This is where lists really shine. Lists are great because you don't have to know ahead of time how many items are going to be in the list. They get bigger or smaller as needed.

Right now, the `restaurant.py` program always asks for exactly 3 restaurants. In programmer terminology, we say that "3" is "hard-coded" into the program.

Modify the program to ask the user how many restaurants they are thinking about for lunch, and then have it ask them for that many restaurant names, and then pick a random restaurant from that list. So if they say they are thinking about `5` restaurants, your program should ask them for 5 names of restaurants, and then pick from among those 5. If they say `2`, it should only ask them for 2 restaurant names. 

Here is a potential use of the program:
```
How many places are you thinking about for lunch? 4
Enter the name of restuarant 1: Jimmy Johns
Enter the name of restuarant 2: Chipotle
Enter the name of restuarant 3: Five Guys
Enter the name of restuarant 4: Noodles and co.
You should go to Noodles and co.
```

*Hint:* Remember the difference between strings and integers. When a user enters a response to `input()`, it is stored as a string. If you want to use it as a number, you need to convert it to one using `int()`.

*Hint 2:* Notice that I made the program a little more user friendly by printing out the words "You should go to" in addition to the final choice.  It is always a good idea to try to make things easier for your users to use and understand.

## Challenges

If you finish with the exercises above, try at least one of the challenges below. The challenges are starting to give a little less direction - as you get further into programming, you get fewer and fewer directions for how to do things, and have to do more work to figure it out yourself.


{% capture _ %}{% increment challenge55 %}{% endcapture %}
### Challenge {% increment challenge55 %}: Unlimited Restaurant Options

Modify your program so that it doesn't need to ask ahead-of-time for the number of restaurants. The user should be able to just keep entering restaurants until they type "done" or just hit enter or something. Then it will randomly choose one of the ones they entered and print it. The program should still accept as many restaurants as they want.

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

*Hint*: `while True:` will loop forever. You can break out of a loop with the `break` command. An elegant way to break out of a loop with user input is to only have the `break` command run if the user enters a specific word, like "quit".

### Challenge {% increment challenge55 %}: Infinite coin flipper

Make a copy of your coin program and call it `infinite.py`. Modify the program so that it keeps flipping coins as long as the user wants it to. It should flip a coin, and then ask the user if it should continue. If the user says "yes", it should go and flip another coin, and then ask the user again. It should keep doing that until the user says "no".

As a bonus, have the program print out the percent of coin flips that have come up "heads". To get this, you can divide the number of "heads" by the total number of coin flips (heads + tails), then multiply the result by 100.

Don't forget to add this program to your git repository.

*Hint*: `while True:` will loop forever. You can break out of a loop with the `break` command. An elegant way to break out of a loop with user input is to only have the `break` command run if the user enters a specific word, like "quit".

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
### Challenge {% increment challenge55 %}: Song list randomizer

Start a new program called `songs.py` that asks the user for several songs they want to listen to, then present the list of songs in a random order.

Don't forget to add this program to your git repository.

*Hint*: `random.shuffle(list)` will randomly re-order a list. Picture in your head putting each item in your list on a separate index card, and then shuffling the deck of index cards.

*Hint 2:* you can ask the user how many songs they want in the list ahead of time, OR you can let them keep adding songs until their song list is complete. If you do the second option, you could use a while loop.


