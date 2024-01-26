---
title: Error messages
nav_exclude: true
visible: false
parent: Reference
nav_order: 5
has_children: false
---

It's helpful to know how to read and understand the different parts of error messages because those messages are meant to help you figure out a) where the error is and b) how to correct it.

## Reading error messages

For Python, error messages usually have 3 parts:

1. What file the error is in and the line number in the file that the error is on (or near)
2. The actual line of code causing the error
3. The type of error and a brief explanation of what the error is

### Example
```
PS C:\Users\geier\Desktop\mi250> python avengers.py"
  File "c:\Users\geier\Desktop\mi250\avengers.py", line 2
    if (person == "Thor") or (person == "thor")
                                               ^
SyntaxError: expected ':'
```

From the first two lines, you can tell that the error is in the file `avengers.py`. You can also tell that the error falls on line 2 in that file.

In the next line of the message, it shows the line of code that caused the error to happen. Notice the arrow pointing up at the blank space at the end of the line of code. There will often be arrows underneath the code like this. Sometimes they can be very helpful: in this case, it's indicating that something is missing.

The last line shows the type of error (SyntaxError) and a brief description of what's wrong. For this error, it says Python is expecting a colon character (:) on that line of code. `if` statements always need to end with a colon. The arrow on the previous line points to where the colon is supposed to be.

## Tips

Sometimes the error message will give an error for a specific line, but the error is actually before or after that line. If you can't figure out what's wrong in the line of code that's in the error message, look at the lines above and below it in your code.

Text editors like Visual Studio Code will highlight issues that will cause errors, usually in red or yellow. That can help you spot and fix issues before you run the program.

It can also be helpful to look at the *syntax highlighting* in your text editor - that is, the different colors text editors use to represent different parts of the code. For examples, VS Code always shows strings in Python files as orange text. If you know a line of text is supposed to be a string but it's not all in orange, that's a sign that there's something wrong that needs fixing - like a missing quote mark (") at the beginning or end of the string.

## Resources

Google (or the search engine of your choise) is one of the best resources for looking up error messages. Here are a couple of other helpful resources:

* [Error types in Python](https://www.tutorialsteacher.com/python/error-types-in-python){:target="_blank"}
* [Common Python runtime errors beginners find](https://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors-beginners-find/){:target="_blank"}



