---
parent: Week 7
topic: 2 - Error Messages
nav_exclude: false
visible: true
---

Learning how to read and understand error messages that you get when you are running and testing programs is an important skill to have.

First, it's good to understand the anatomy of an error message. This is different for different programming languages. For Python, error messages usually have 3 parts:

1. What file the error is in and the line number in the file that the error is on (or near)
2. The actual line of code causing the error
3. The type of error and a brief explanation of what the error is

It's helpful to know how to read and understand the different parts of error messages because those messages are meant to help you figure out a) where the error is and b) how to correct it.

Google is a very valuable resource for understanding error messages as well. For the exercises below, you might want to use Google to figure out what each error message means. I recommend trying to figure out what the message is saying on your own first, then use Google as a backup option.

## Instructions

Each of the exercises below includes an error message and the snippet of code that caused the error. In your own words, describe what's happening with each of the error messages below. 

Describe: What do you think caused the error? How would you go about trying to fix it? Try to make your descriptions as human-readable as possible - pretend you're trying to explain it to your partner during a lab or a studio in class. 

### Exercise 1

Code:
```python
person = "Thor"
if (person == "Thor") or (person == "thor")
    print("Thor walks over to the hammer and reaches down to pick it up.")
```

Error message:
```
PS C:\Users\geier\Desktop\mi250> python avengers.py"
  File "c:\Users\geier\Desktop\mi250\avengers.py", line 2
    if (person == "Thor") or (person == "thor")
                                               ^
SyntaxError: expected ':'
```

### Exercise 2

Code:
```python
body_part = "head"
print("Nothing goes over my", body_part, ". My reflexes are excellent and I would",  action, "it.")
```

Error message:
```
Traceback (most recent call last):
  File "C:\Users\geier\Desktop\mi250\mad-libs.py", line 2, in <module>
    print("Nothing goes over my", body_part, ". My reflexes are excellent and I would",  action, "it.")
                                                                                         ^^^^^^
NameError: name 'action' is not defined
```

### Exercise 3

Code:
```python
answer = input("What is my favorite color? ")
if answer.lower() == "green":
    print("Right! Green is my favorite color.")
else:
print("Wrong!")
```

Error message:
```
PS C:\Users\geier\Desktop\mi250> python question.py
  File "C:\Users\geier\Desktop\mi250\question.py", line 5
    print("Wrong!")
    ^
IndentationError: expected an indented block after 'else' statement on line 4
```

### Exercise 4

Code:
```python
count = input("How high do you want the count to go? ")
for num in range(count):
    print(num)
```

Error message:
```
Traceback (most recent call last):
  File "C:\Users\geier\Desktop\mi250\counter.py", line 2, in <module>
    for num in range(count):
               ^^^^^^^^^^^^
TypeError: 'str' object cannot be interpreted as an integer
```

## Turn in

Turn your assignment in as a Word doc or a PDF on D2L under Assignments -> Understanding Error Messages. This assignment is due at the end of the day on Wednesday in Week 7.

Grades will be based on following the instructions and making an honest effort. If you describe your findings for each exercise particularly well, that will earn you a check plus.

## Extra tips and resources

As already mentioned, Google (or the search engine of your choice) is one of the best resources for looking up error messages. Here are a couple of other helpful resources:

* [Common Python runtime errors beginners find](https://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors-beginners-find/){:target="_blank"}
* [Python Errors and Built-in Exceptions](https://www.toppr.com/guides/python-guide/tutorials/python-files/python-errors-and-built-in-exceptions/){:target="_blank"}

Note that text editors like Visual Studio Code will also highlight issues that will cause errors, usually in yellow or red. That can help you spot and fix issues before you run the program.

It can also be helpful to look at the syntax highlighting - that is, the different colors text editors use to represent different parts of the code. For examples, VS Code always shows strings in Python files as orange text. If you know a line of text is supposed to be a string but it's not all in orange, that's a sign that there's something wrong that needs fixing - like a missing quote mark (") at the beginning or end of the string.

VS Code and some other text editors will also sometimes show symbols and other visual indicators that there's an error in the code. Sometimes it will look like a squiggly underline, like how Word shows spelling or grammar errors. Other times it will be a red arrow in front the line numbers. When you encounter an error when running a program, look for these kinds of indicators in your text editor.