---
parent: Week 8
topic: Dictionaries as Data Structures
git: https://gitlab.msu.edu/mi-250/structured-data
nav_exclude: true
visible: false
---

## Working with Dictionaries

Dictionaries store data based on key/value pairs. They are similar to lists, but differently structured. In a list, values are stored in order: 0, 1, 2, etc. In a dictionary, values are stored by name. The name is called the 'key' of the dictionary.

To create a dictionary, we use the curly braces: `{}`.  Everything between the curly braces is part of the dictionary. We can create dictionaries in Python like this:

```
my_dictionary = {
    'word': 'definition',
    'word2': 'definition2'
    }
```

Any time you need the definition of a word, you can ask Python for `my_dictionary['word']` and it will provide the definition for that word.

You can also create a blank dictionary and add stuff to it later, like with lists. The process of adding things is slightly different, though.

```
my_dictionary = {}
my_dictionary['word'] = 'definition'
```

The second line adds a single key-value pair to the dictionary called `my_dictionary`.

I've used the terms 'word' and 'definition' - paper dictionaries are structured like this, and that's loosely what Python dictionaries are based on. But Python dictionaries are more flexible than that. You can have them store anything you like.

Today's lab is long, but some of the exercises are pretty easy. If you get through everything, then great! If you don't, that's fine, too. Dictionaries are really useful, but also a somewhat weird way to think. It can take some time to figure out how they work and how to do things with them. Like everything else in this class, we'll be revisiting dictionaries again later. 

## Using dictionaries

### Exercise 1: Print out a mascot

Start by looking at the program `mascots.py`. There is a dictionary full of schools and mascots, where the name of each school is associated with its mascot. If you give the dictionary the name of a school, the dictionary will spit back out the mascot for that school (much like if you look in a real-world dictionary for a word, it gives you back the defintion of that word).

We use this feature inside the print statement. We give the dictionary the name `"Wisconsin"`. When we run the program, it goes into the dictionary and gets the mascot for Wisconsin and prints out "Badgers".

Modify this program to print out the mascot for MSU.

Note: you should not have to change the dictionary for this exercise, and at no point should you have to type "Spartans". You should be able to do this by just changing the `print` statement on line 10 to use a different school.

### Exercise 2: Add another mascot

Your next task is to modify the dictionary and add another school's mascot to the dictionary. The University of Washington was just added to the Big 10 this year. Let's add "Washington" to the dictionary, along with their mascot (UW folks are called "Huskies").

Modify the dictionary to include Washington and its mascot, and then modify the print statement so it prints out the mascot for Washington.

### Exercise 3: Ask the User

Right now, all the program does is print out a single mascot for a single university. What if you want to know a different university's mascot? Let's modify the program to be a bit more interactive.

After creating the dictionary, add some code that uses `input()` to ask the user which university they want to know the mascot for. Then the program should print out the mascot for whatever university the user entered by looking it up in the dictionary. The output of the program should look similar to this:

```
What university do you want to know the mascot for? Wisconsin
People who go to Wisconsin are called Badgers
```

Your program should NOT use any `if` statements. You should be able to do this by collecting input from the user, storing in a variable, and then using that variable to look up the answer in your dictionary.

*Hint*: Don't forget to change the school's name in the print statement to whatever the user typed, in addition to printing out the mascot.

## Storing structured data
### Exercise 4: Print out favorite food

Next, look at the file `student.py`. Run it; it should print out some information about me (your instructor).

Right now, the program prints out my name and major. But the dictionary stores one more piece of information about me: my favorite food. Modify the program to *also* print out my favorite food by adding an additional `print` statement.

### Exercise 5: Change the dictionary to your partner's information

Now that the program is printing out all of my information, change whose information it prints out.  Ask your lab partner for their information, and change the information in the dictionary to their information. To do this exercise, you should *only* change the information inside the dictionary; you should not need to change the print statements at all.

### Exercise 6: Add favorite color

Name, major, and favorite food are great, but that isn't much information about a person. Add to the program the ability to store the person's favorite color, and also print out that favorite color.  

BUT instead of just editing the dictionary directly again, this time we're going to add the information using a separate line of code.

The format `dictionary['key'] = value` will add a new key and value to the dictionary. In this example, `dictionary`, `key`, and `value` are all generic - you'll need to replace them all with information specific to this program. 

Remember the key is the word on the left of the colon (`:`), and is always represented as a string (that is, it needs to be in quotes). The value is the data on the right of the colon. You can think of the key as a variable specific to the dictionary that points to a particular piece of data - the value associated with it.

Make sure to add a new print statement to print out the person's favorite color.

*Hint:* If you're not sure the information is being added to the dictionary correctly, you can always print out the dictionary's structure in the console to check using `print(student)`. Printing things to the console can be a helpful way to troubleshoot your code.

### Exercise 7: Ask the user for more information

Now let's ask the program's user for additional information using `input()` and add it to the dictionary. Ask them what their favorite movie is, and add that information to the dictionary.

Make sure to add a new print statement to print out the person's favorite movie.

*Hint:* You can use the same structure as in the last exercise, but instead of hard-coding the value, save the user's input to a variable and use the variable as the value instead. The key you use to store this value should probably be something like `'favorite_movie'`.

## Structured data into functions

One of the advantanges of dictionaries is that you can store complex data -- such as all of the information about a student -- in a single variable. That means that you can pass that single variable into a function.

### Exercise 8: Passing a dict into a function

Next, let's order a pizza. Go run the program "pizza.py". It prints out my normal Monday pizza order.

Open of the file and look at it. There is a function called `print_pizza_order` that takes a single variable as a parameter -- the pizza order. This order is a dictionary that contains all of the information needed for the order -- the size of the pizza, the type of crust, and any toppings. The function then uses the information in the dictionary to fill in some print statements.

Modify the program to print out my normal Friday order. You should be able to do this by changing exactly one word in the program.

### Exercise 9: Your pizza!

OK, time for you to order a pizza. Add a new variable to the program under `friday`. That variable should contain a dictionary with *your* pizza order -- whatever type of pizza you like! Then modify the program to have it print out your order instead of mine, by calling `print_pizza_order()` and passing in the dictionary with your order.

*Note:* Your dictionary needs to be set up exactly like the `monday` and `friday` dictionaries for it to work with the `print_pizza_order()` function. That means it needs to have the same keys: `'size'`, `'crust'`, and `'toppings'`. But the values associated with those keys can be different.

*Note 2:* There can be multiple values assigned to a single key in a Python dictionary - which means you can theoretically have multiple toppings. We'll get to this in a later exercise -- for now, only add one topping.

## List of dictionaries

We've learned both lists and dictionaries. You can combine these in interesting ways.

### Exercise 10: Random pizza order

Sometimes I am so hungry I can't decide what I want on my pizza. That's when a random pizza ordering program would be useful.

We know from previous labs that we can use `random.choice()` to pick a random item out of a list. Let's use this with our pizzas.

Modify the pizza program to take the three orders that already exist -- my Monday order, my Friday order, and your favorite pizza -- and put them into a list.  Then have the program use `random.choice()` to pick a random item out of that list, and give that choice to `print_pizza_order()` to print out the full order.

Don't forget to `import random` at the top of your program.

*Hint*: You can make a list of dictionaries. The easiest way is to put each dictionary in a variable, and then put those variables into a list:
```
cheese_pizza = {'crust': 'traditional', 'toppings': "cheese"}
pepperoni_pizza = {'crust': "thin", 'toppings': "pepperoni"}

pizza_list = [cheese_pizza, pepperoni_pizza]
```

### Exercise 11: Lists inside of dictionaries

Dictionary keys can also be paired with lots of different kinds of things, including lists. Look in the file `deluxe.py`. This file contains a pizza order inside a dictionary, but instead of having one topping, it has a list attached to the `toppings` key.

The `print_pizza_order()` function is also in `deluxe.py`, but it doesn't quite work with this dictionary. Run the program to see what it prints out.

Remember how to access items in a dictionary. Just like `pizza['crust']` will give you a string with the type of crust, `pizza['toppings']` will give you a *list* of strings. You can then do the things you would normally do with a list, such as accessing the first item (`pizza['toppings'][0]`) or looping through the list (`for item in pizza['toppings']`) or getting the length of the list using `len(pizza['toppings'])`.

Modify the function so it loops through the toppings list and prints out each topping one by one, like this:

```
I would like a extra large pizza on a thin crust
With 5 toppings on it:
- pepperoni
- black olives
- green peppers
- sausage
- mushrooms
```

*Hint*: When a list is stored inside of a dictionary (e.g. toppings), you can get the whole list at once using the dictionary syntax `pizza['toppings']`. Then you can loop through it like any other list using a `for` loop: 
```
for top in pizza['toppings']:
	print(top)
```

*Hint 2:* Remember you can use `len()` to get the length of a list - that will be helpful for the "With X toppings on it" line.

### Exercise 12: Delivery Address

In the previous exercise, you stored a list inside of a dictionary. The key in the key-value pair is always a string, but the value can be anything you want.

Here is a dictionary that contains a delivery address for the pizza:
```
address = {
    'street': "1278 Spartan Dr",
    'city': "East Lansing",
    'state': "Michigan",
    'zip': 48864
}
```

We want to put this address inside of the pizza order, so we know where to deliver this pizza. We can do this by modifying the pizza order:
```
cheese_pizza = {
    'crust': "traditional",
    'size': "large",
    'toppings': ['cheese'],
    'delivery': address
}
```

Notice that I did not put quotes around the `address`. In Python, if you put something in quotes, it's a string. The only information a string stores is the text inside the quotes. But I don't to `delivery` to be linked to the word `"address"`, I want it to link to the dictionary that is stored in the variable `address`. So I use `address` without quotes to point to the variable.

You access this is basically the same way as before. If you access `cheese_pizza['delivery']`, it gives you a *dictionary* of information. And then you can use the same technique to get items out of that. So `cheese_pizza['delivery']['street']` will tell you the street address that you are delivering it to.

Add the address dictionary to `deluxe.py` (you can change the address info if you want) and then reference the address dictionary inside the `deluxe_pizza` dictionary. Modify the `print_pizza_order()` function to print out the address the pizza should be delivered to. Your function should still just accept one parameter -- a dictionary with the pizza order.

### Exercise 13: Pretty print 

Now that we are building more complicated dictionaries, it is sometimes useful to print out the contents of a dictionary to the terminal so we can better see what it looks like.   

Modify your program to just call `print(deluxe_pizza)` -- that is, to use the regular print function and passing it the dictionary. This gives you the information, but it is hard to read.

Another, clearer way to do this is called "pretty printing". This tries to format the dictionary in a way that is easier for humans to read. We can use the `pprint` library to pretty print.

```
import pprint
pprint.pprint(deluxe_pizza)
```

Modify your `deluxe.py` program to pretty print the entire dictionary your pizza using `pprint`.

We don't normally do this in code that is intended for other people to use. But pretty printing a dictionary is a great way for us to see what the dictionary looks like, and is a useful tool for writing (or reading!) code that uses dictionaries.

*Note:* `pprint` only really works well with dictionaries - it's designed to show how a dictionary is formatted. If you try using `pprint` on other things, you might get some unexpected results.

## Thinking about structured data

All of these exercises today are using dictionaries in a very specific way. The dictionaries are storing "structured data" -- complex data that is made up of multiple different pieces of information that are grouped into a logical whole. A student is a logical whole, but the information about that student has multiple different pieces. Same with a pizza order.

In our structured dictionaries, the keys define the structure of the data. So we have keys that look like "crust", "toppings", or "name" -- they are words in quotes. The values associated with those keys are the actual data. Dictionary keys provide a template for the types of data that are associated with them.

It can be helpful to think of a dictionary as a repeatable template that is full of metadata. Think about filling out a form: a form might have a bunch of items like name, birthdate, address, etc. with blank spaces next to them that you fill out with your information. The same form can be used by a lot of different people, who all will fill in the blanks with different data. But the structure of the form -- the items that need to be filled in -- is the same for everyone. 

### Exercise 14: Structuring Data

Now that you have experience working with dictionaries to store structured data, it is time to create a structure yourself. Create a new file called `songs.py`.

Think about apps you use to play music - Spotify, iTunes, etc. A playlist in these apps will have a bunch of songs in them, and each song has different pieces of data associated with it so that you can tell what song is playing at any given time. These pieces of data are often called *metadata* - the song itself is the data, while the data associated with the song is data about the data (that is, metadata). For songs, this is stuff like the artist, the album the song is on, the length of the song, the year it was released, etc. What other metadata can be associated with a song? 

Make a dictionary structure that will store metadata about a song. The structure should be repeatable: that is, you should be able to put the metadata for different kinds of songs into it and the structure will still work. Think of contingencies - for example, what if a song has more than one artist? Create multiple dictionaries to test: each dictionary should have the data for a single song in it.

Print out the data for each song in the console using a function similar to the `print_pizza_order()` function from the previous exercises. Make sure the function works with different songs.

## Challenges

Please complete at least one challenge before leaving for the day. It is up to you which one you do. Have the instructor or TA come over and see the results of your challenge before you leave.

### Challenge 1: Input pizza order

Right now, the pizza orders are hard-coded into your Python program.  Modify your program to instead ask the user what they want to order using `input()`. You'll have to ask multiple questions, and then assemble the results into a dictionary. The dictionary should be able to be printed using your existing `print_pizza_order()` function.

Bonus: put your questions and `input()` commands into a function that `return`s the complete dictionary.

### Challenge 2: Calculate GPA

Modify the student program to store a list of grades in the dictionary for the student. Then write a function that goes through the student's grades and calculates their GPA.

### Challenge 3: Song randomizer

Modify the the `songs.py` program you made for exercise 14 to print out a randomized song playlist. Format the song list nicely (don't just print out the dictionary code).
