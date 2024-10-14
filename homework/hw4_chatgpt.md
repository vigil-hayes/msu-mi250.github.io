---
parent: Week 11
topic: 4 - ChapGPT
nav_exclude: true
visible: false
---

Chat-based AI systems such as ChatGPT can be very useful for programming. But like any tool, it helps to understand how it works and what is or isn't useful about using it first. This assignment will have you do a couple of programming-related exercises with ChapGPT so you can learn a bit more about how it can / can't help you with programming tasks.

If you do not already have a ChatGPT account, you can [create a free one here](https://chat.openai.com/auth/login). You will not need a paid account to do this assignment. 

If you would prefer to use a different AI system to complete this assignment, that's fine! Make sure to say which system you used at the top of your assignment. 

## Instructions

Each of the exercises below will involve giving ChatGPT a prompt and then documenting how ChatGPT responds to that prompt. Your response for each exercise should include:
1. the prompt you used in ChatGPT
2. a screenshot of a relevant part of the ChatGPT results OR a screenshot of what happens when you run the code ChatGPT gives you
3. a short response (1-3 sentences) to the question(s) in the exercise

I encourage you to play around with ChatGPT - try different prompts, or try the same prompt multiple times, and see if it comes up with different results. Try to make your prompts more specific or less specific and see what works better. You only need to include 1 prompt and the results of that 1 prompt for each exercise.

*Note:* if ChatGPT responds to your prompt with code, you will need to copy+paste the code it gives you into your text editor (e.g. Visual Studio Code, BBEdit, Notepad++, etc.) and run it on your computer to see what it does - ChatGPT can't run the code for you.

### Exercise 1

Ask Chat GPT to tell you what this code does:

```python
guess = input("What letter do you guess? ")
index_counter = 0  
if guess in word:           
	for letter in word:             
		if guess == word[index_counter]:        
			guess_list[index_counter] = guess   
		index_counter += 1
```

Is the response helpful, or not? How would you describe what this code does in 1-2 sentences based on ChatGPT's response? Based on what ChatGPT says, would you be able to run this code without getting any errors?

Include the prompt you used (everything you typed except for the code) and ChatGPT's response to it in your assignment.

### Exercise 2

Ask ChatGPT to tell you more about the error below:

```
Traceback (most recent call last):
  File "c:\Users\geier\Documents\MI250\structured-data\pizza.py", line 11, in <module>
    print_pizza_order(saturday)
  File "c:\Users\geier\Documents\MI250\structured-data\pizza.py", line 4, in print_pizza_order
    print("I would like a", pizza['size'], "pizza on a", pizza['crust'], "crust")
                            ~~~~~^^^^^^^^
TypeError: list indices must be integers or slices, not str
```
Based on ChatGPT's response, how do you think you would go about fixing the error, in your own words? 

Include the prompt you used (everything you typed except for the error message) and ChatGPT's response to it in your assignment.

### Exercise 3

Ask ChatGPT to create a choose your own adventure program using Python.

Remember, we made choose your own adventure programs for our first studio near the beginning of the semester. Find the code you wrote then (if you were in class that day) and look at it. How is the code ChatGPT gave you different from what you and your group wrote for the studio? Does the code it gave you make sense to you? Would you rather use ChatGPT's code or write your own for a program like this?

If you were not in class that day (for Studio 3), you only need to answer the last two questions. 

Include the prompt you used and a screenshot of ChatGPT's results (as much as you can fit into 1 screenshot) in your assignment.

### Exercise 4

Ask ChatGPT to draw an MSU Spartan logo using Python's Turtle library. You may phrase the prompt however you wish. 

Are the results what you expected? Why or why not? What kinds of things do you think you could reasonably ask ChatGPT to use Turtle for? Would you personally want to use ChatGPT to create Turtle drawings for you?

Include the prompt you used and a screenshot of the resulting Turtle drawing in your assignment. 

## Using ChatGPT in class

You've already been using resources like Google, Reddit, StackOverflow, etc. in class to help you with your code. A few of you have already been using ChatGPT as well. ChatGPT is another tool in your toolbox - you will not be marked down in this class for using it.

BUT. Like with any code you get off the Internet, you'll need to try and understand what ChatGPT is giving you before you can incorporate it into the code you are writing. For any code you use from any source, whether it be Google or StackOverflow or ChatGPT, I highly recommend taking the time to add comments to the code. Writing down what the code is doing (or what you think it's doing) in human-readable terms can help you to understand better how it's working.

## Turn in

Turn in your reflection in on D2L either as a Word doc or a PDF under Assignments -> Jobs and Programming. This assignment is due before the start of the studio in Week 11.