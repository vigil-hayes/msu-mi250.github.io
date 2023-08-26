---
parent: Week 8
topic: Dictionaries as Data Structures
git: https://gitlab.msu.edu/mi-250/structured-data
nav_exclude: true
visible: false
---

## Working with Dictionaries

Dictionaries are key/value stores.  They are similar to lists, but differently structured.  In a list, values are stored
in order: 0, 1, 2, ....  In a dictionary, values are stored by name.  The name is called the 'key' of the dictionary.

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

*Note*: You can create a blank dictionary with `{}`:
```
my_dictionary = {}
```

*Note 2*: Today's lab is long, but some of the exercises are pretty easy.  If you get through everything, then great!
You've got a good handle on dictionaries.  If you don't, then that's OK too. Dictionaries are really useful, but also a
somewhat weird way to interact with a computer, and they take a bit of time to figure out and get used to.

## Using dictionaries

### Exercise 1: Print out a mascot

Start by looking at the program `mascots.py`. Look at the code.  It created a dictionary at the top of the program.
Each name of a school is associate with its mascot.  If you give the dictionary the name of a school, the dictionary
will spit back out the mascot for that school (much like if you give a real-world dictionary a word, it gives you back
the defintion of that word).

We use this feature in the first print statement.   We give the dictionary the name `"Wisconsin"`.  When we run the
program, it goes into the dictionary and gets the mascot for Wisconsin and prints out "badgers".

Modify this program to print out the mascot for Ohio State.

Note: you should not have to change the dictionary for this exercise, and at no point should you have to type
"Buckeyes".  You should be able to do this by just changing the `print` statement on line 10 to use a different school.

### Exercise 2: Add another mascot

Your next task is to modify the dictionary and add another school's mascot to the dictionary.   Add "Indiana" to the
dictionary.  People from Indiana are called "[Hoosiers](https://en.wikipedia.org/wiki/Hoosier)" (though I have no idea
what a Hoosier is).

Modify the dictionary to include Indiana in the dictionary, and then modify the print statement to print out the mascot
for Indiana.

### Exercise 3: Ask the User

Right now, all the program does is print out a single mascot for a single university.  What if you want to know a
different university's mascot?  Let's modify the program to be a bit more user friendly.

After creating the dictionary, add some code that uses `input()` to ask the user which university they want to know the
mascot for.  Then the program should print out the mascot for whatever university the user entered by looking it up in
the dictionary.   For example:

```
What university do you want to know the mascot for? Penn State
People who go to Penn State are called Nittany Lions
```

Your program should NOT use an `if` statement.   You should be able to do this by inputting a name from the user,
storing in a variable, and then using that variable to look up the answer in your dictionary.

*Hint*: Don't forget to change the school's name in the print statement to whatever the user input, in addition to printing out
the mascot.

## Storing structured data
### Exercise 4: Print out favorite food

Next, look at the file `student.py`.  Run it; it should print out some information about me (your instructor).

Right now, the program prints out my name and major.  But the dictionary stores one more piece of information about me:
my favorite food.  Modify the program to *also* print out my favorite food by adding an additional print line.

### Exercise 5: Change the dictionary to your partner's information

Now that the program is printing out all of my information, change whose information it prints out.  Ask your lab
partner for his or her information, and change the information in the dictionary to his or her information.  To do this
exercise, you should *only* change the information inside the dictionary; you should not need to change the print
statements at all.

### Exercise 6: Add favorite color

Name, major, and favorite food are great, but that isn't much information about a person.  Add to the program the
ability to store the person's favorite color, and also print out that favorite color.  

To do this, you should add an entry to the "student" dictionary called 'favorite_color', where you fill in the favorite
color.  Then you can add a new print statement to print out that favorite color.

### Exercise 7: Swap and add a second student's information

So far, you've got a dictionary that contains a bunch of information about a single person, and then prints out that
information.

Swap driver and navigator, and then have the new driver add the other person's information to the file.  This should be
a second dictionary, stored in a separate variable.   Have the program print out both people's information to the
screen, with a blank line between them.

The output should be something like this:
```
The first student's name is Rick Wash
The first student's major is Information Science
The first student's favorite food is pizza
The first student's favorite color is blue

The second student's name is Jack Waier
The second student's major is Games and Interactive Media
The second student's favorite food is mac and cheese
The second student's favorite color is green
```

## Structured data into functions

One of the advantanges of dictionaries is that you can store complex data -- such as all of the information about a
student -- in a single variable.  That means that you can pass that single variable into a function.

### Exercise 8: Passing a dict into a function

Next, let's order a pizza. Go run the program "pizza.py".  It prints out my normal monday pizza order.

Open of the file and look at it.  There is a function called `print_pizza_order` that takes a single variable as a
parameter -- the pizza order.  This order is a dictionary that contains all of the information needed for the order --
the size of the pizza, the type of crust, and any toppings.

Modify the program to print out my normal friday order.  You should be able to do this by changing exactly one word in
the program.

### Exercise 9: Your pizza!

OK, time for you to order a pizza.  Add a new variable to the program. That variable should contain a dictionary with
*your* pizza order -- whatever type of pizza you like!  Then modify the program to have it print out your order instead
of mine, by calling `print_pizza_order()` and passing in the dictionary with your order.

### Exercise 10: Writing a function that handles dictionaries

The pizza program showed you how you can pass a dictionary into a function that you write. This allows you to give it a
bunch of pieces of information -- the crust type, the toppings, the size -- all at once. 

Go back to the "student.py" program that you wrote earlier (for exercises 1-4).  You've got a lot of duplicated code --
you wrote basically the same set of `print()` lines twice, once for each student.

Write a function that prints out a single student's information.  Then call that function twice, passing in the
dictionaries with the student information.  If that function is called `print_student()`, then the main code should look
like this:

```
print_student(student1)
print_student(student2)
```

If you need to remember more about functions, feel free to look back at
the [functions lab]({% link labs/drawing_with_functions.md %}) and the
[functions readings]({% link readings/functions.md %}).

## List of dictionaries

We've learned both lists and dictionaries.  You can combine these in interesting ways.  

### Exercise 11: Random pizza order

Sometimes I am so hungry I can't decide what I want on my pizza.  That's when a random pizza ordering program would be
useful.

We know from previous labs that we can use `random.choice()` to pick a random item out of a list.  Let's use this with
our pizzas.

Modify the pizza program to take the three orders that already exist -- my monday order, my friday order, and your
favorite pizza -- and put them into a list.  Then have the program use `random.choice()` to pick a random item out of
that list, and give that choice to `print_pizza_order()` to print out the full order.

Don't forget to `import random` at the top of your program.

*Hint*: You can make a list of dictionaries.  The easiest way is to put each dictionary in a variable, and then put
those variables into a list:
```
cheese_pizza = {'crust': 'traditional', 'toppings': "cheese"}
pepperoni_pizza = {'crust': "thin", 'toppings': "pepperoni"}

pizza_list = [cheese_pizza, pepperoni_pizza]
```

## Data inside of a dictionary

### Exercise 12: List of pizza toppings

Look in the file `deluxe.py`.  This file contains a pizza order inside a dictionary, but it stores the toppings of the
pizza as a list inside the dictionary.   Like this:

```
deluxe_pizza = {
   'crust': "thin",
   'size': "extra large",
   'toppings': ["pepperoni",
                "black olives",
                "green peppers",
                "sausage",
                "mushrooms"
               ]
    }
```

Remember how to access items in a dictionary.  Just like accessing `pizza['crust']` will give you a string with the type
of crust, acessing `pizza['toppings']` will give you a *list* of strings.  You can then do the things you would normally
jo with a list, such as accessing the first item (`pizza['toppings'][0]`) or looping through the list 
(`for item in pizza['toppings']`) or getting the length of the list using `len(pizza['toppings'])`.

Copy the `print_pizza_order()` function from `pizza.py` into `deluxe.py`, and then modify the function to print out the number of toppings, and then a bullet pointed list of toppings like this:

```
I would like a extra large pizza on a thin crust
With 5 toppings on it:
- pepperoni
- black olives
- green peppers
- sausage
- mushrooms
```

*Hint*: When a list is stored inside of a dictionary (e.g. toppings), you can
get the whole list at once using the dictionary syntax `pizza['toppings']`.
Then you can loop through it like any other list using a `for` loop: 
```
for top in pizza['toppings']:
	print(top)
```

### Exercise 13: Delivery Address

In the previous exercise, you stored a list inside of a dictionary.   That should indicate that you can store more
complicated data inside dictionaries than just numbers and words.  And indeed you can.  You can put lists, dictionaries,
or anything else you want inside of a dictionary.

Here is a dictionary that contains a delivery address for the pizza:
```
address = {
    'street': "1278 Spartan Dr",
	'city': "East Lansing",
	'state': "Michigan",
	'zip': 48864
    }
```

We want to put this address inside of the pizza order, so we know where to deliver this pizza.  We can do this by
modifying the pizza order:
```
cheese_pizza = {
	'crust': "traditional",
	'size': "large",
	'toppings': ['cheese'],
	'delivery': address
}
```

Notice that I did not put quotes around the `address`. In python, if you put something in quotes, it means that
exact word -- so `"delivery"` means the exact word delivery.  But i don't want the word `"address"`, I want the
dictionary that is stored in the variable `address`.  So I put it there without quotes.

You access this is basically the same way as before.   If you access `cheese_pizza['delivery']`, it gives you a
*dictionary* of information.  And then you can use the same technique to get items out of that.  So 
`cheese_pizza['delivery']['street']` will tell you the street address that you are delivering it to.

Add the address dictionary to deluxe.py (you can change the address info if you want) and then reference the address dictionary inside the deluxe_pizza dictionary.
Modify your print function to print out the address the pizza should be delivered to.   Your function should still just
accept one parameter -- a dictionary with the pizza order.  

### Exercise 14: Pretty print 

Now that we are getting more and more complicated dictionaries, it is sometimes useful to print out the contents of a
dictionary to the terminal so we can better see what it looks like.   

Modify your program to just call `print(pizza)` -- that is, to use the regular print function and passing it the
dictionary.  This gives you the information, but it is hard to read.

A better way to do this is called "pretty printing".  This tries to format the dictionary in a way that is easier to
read.  We can use the ``pprint` library to pretty print.

```
import pprint
pprint.pprint(deluxe_pizza)
```

Modify your `deluxe.py` program to pretty print the entire dictionary your pizza. 

We don't normally do this in code that is intended for other people to use.  But pretty printing a dictionary is a great
way for us to see what the dictionary looks like, and is a useful tool for writing code that uses dictionaries.


## Thinking about structured data

All of these exercises today are using dictionaries in a very specific way, and in a way that is different than we used
them before. All of these exercises are using dictionaries to store "structured data" -- complex data that is made up of
multiple different pieces of information that are grouped into a logical whole.  A student is a logical whole, but the
information about that student has multiple different pieces.  Same with a pizza order.

When we put this information into a dictionary, we do so in a specific way.  Dictionarys store "key/value" information
that associates some value (e.g. definition) with a key (e.g. word). 

In our structured dictionaries, the key is always the structure.  So we have keys that look like "crust", "toppings", or
"name" -- they are words in quotes.   And then the value in the dictionary is our actual data.  We can have multiple
different dictionaries with the same key names, but different values.   The key names represent the structure of the
data, and the values are the actual data.

This is a really common and valuable way to think about and use dictionaries in python.  

Working with dictionaries this way is hard because you have to keep in mind what the dictionary looks like.   I find it
helpful to draw out the dictionary on a piece of paper to help me see what the parts of it are.

### Exercise 15: Structuring Data

Now that you have experience working with dictionaries to store structured data, it is time to create the structures
yourself.

Imagine a post on social media, such as a Facebook post or an Instagram post.  The post is actually a complex object
that has a lot of information -- who posted it, the text content of the post, an optional picture, hashtags, the date
and time when it was posted, etc.

Write a program that stores a post on an imaginary social media system that you are creating in a dictionary, and then
prints out that post on the terminal.

Create multiple different posts as separate dictionaries.  Make sure that the code you use to print out the post is a
function, and test that it works correctly with multiple different posts.

It is up to you how you want to structure / organize your dictionary.  The only rule is that the entire post has to be
stored in a single variable -- which means in a dictionary.


## Challenges

Please complete at least one challenge before leaving for the day.  It is up to you which one you do. Have the
instructor or TA come over and see the results of your challenge before you leave.

### Challenge 1: Input pizza order

Right now, the pizza orders are hard-coded into your python program.   Modify your program to instead ask the user what
they want to order using `input()`.  You'll have to ask multiple questions, and then assemble the results into a
dictionary.

Put your questions and `input()` commands into a function that `return`s the complete dictionary. The dictionary it
returns should be able to be printed using your exisitng `print_pizza_order()` function.

### Challenge 2: Calculate GPA

Modify the student program to store a list of grades in the dictionary for the student.   Then write a function that
goes through the student's grades and calculates their GPA.

### Challenge 3: Display your social media post

Modify the program from Exercise 15 (the social media post) to use turtle to display all of the information in the post
visually.  
