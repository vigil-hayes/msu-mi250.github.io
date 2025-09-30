---
title: Turtle Loops
nav_exclude: false
visible: true
parent: Extra
nav_order: 1
has_children: false
---

# Python Turtle Loops Challenge - Patterns and Performance

## Introduction
In this challenge, you'll create mesmerizing patterns and art using Python's turtle graphics while discovering the power and pitfalls of different types of loops! You'll learn when to use different loop types, how to combine them, and why some approaches are faster than others.

**What you'll learn:**
- When loops are the right tool for the job
- The difference between `for` loops and `while` loops
- How to combine loops (nested loops)
- Why some code runs faster than others (time complexity)
- How to measure and improve your code's performance

## Setup
```python
import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)

# Create a turtle
artist = turtle.Turtle()
artist.speed(0)
artist.pensize(2)

# For timing our code
start_time = 0

def start_timer():
    global start_time
    start_time = time.time()

def end_timer(description):
    elapsed = time.time() - start_time
    print(f"{description}: {elapsed:.2f} seconds")

# Your code goes here!

screen.exitonclick()
```

---

## Challenge 1: When to Use Loops vs. When NOT to Use Loops

### Part A: The Repetitive Way (No Loops)
First, let's see what happens when we DON'T use loops:

```python
def draw_square_no_loop():
    """Draw a square without using any loops - the hard way!"""
    artist.forward(100)
    artist.right(90)
    artist.forward(100)
    artist.right(90)
    artist.forward(100)
    artist.right(90)
    artist.forward(100)
    artist.right(90)

def draw_spiral_no_loop():
    """Try to draw a spiral without loops - good luck!"""
    artist.forward(10)
    artist.right(90)
    artist.forward(20)
    artist.right(90)
    artist.forward(30)
    artist.right(90)
    # ... this would take forever!
```

### Part B: The Smart Way (With Loops)
Your mission: Rewrite these functions using loops!

```python
def draw_square_with_loop():
    """Draw a square using a loop - much better!"""
    # Your code here!
    pass

def draw_spiral_with_loop(num_sides):
    """Draw a spiral with any number of sides"""
    # Your code here!
    # Hint: make each side a bit longer than the last
    pass

def draw_polygon(sides, size):
    """Draw any regular polygon"""
    # Your code here!
    # Hint: the angle to turn = 360 / sides
    pass
```

### Test Your Functions:
```python
start_timer()
draw_square_with_loop()
end_timer("Square with loop")

artist.clear()
draw_spiral_with_loop(50)

artist.clear()
draw_polygon(8, 100)  # Octagon
```

### Reflection:
- When did loops make the code easier to write?
- When did loops make the code easier to read?
- What would happen if you needed to draw a 100-sided polygon without loops?

---

## Challenge 2: For-Loop vs While-Loop - When to Use Which?

### The Great Loop Showdown!

#### Scenario 1: You Know Exactly How Many Times
```python
def draw_flower_petals_for():
    """Draw 8 flower petals - we know exactly how many!"""
    # Use a for-loop here!
    # Your code here!
    pass

def draw_flower_petals_while():
    """Draw 8 flower petals using while-loop"""
    # Try using while-loop - is it easier or harder?
    # Your code here!
    pass
```

#### Scenario 2: You Don't Know How Many Times
```python
def draw_until_edge():
    """Draw forward until you're close to the screen edge"""
    # Use while-loop here! Keep going until x-coordinate > 300
    # Your code here!
    # Hint: artist.xcor() gives current x position
    pass

def random_walk():
    """Keep drawing until you've moved more than 500 total pixels"""
    # Use while-loop! Keep track of total distance moved
    total_distance = 0
    # Your code here!
    # Hint: add random.randint(10, 50) to total_distance each step
    pass
```

### Your Mission:
Complete all four functions above, then test them:

```python
# Test known repetitions
artist.color("red")
draw_flower_petals_for()
artist.clear()

# Test unknown repetitions  
artist.color("blue")
draw_until_edge()
artist.clear()

artist.color("green")
random_walk()
```

### Loop Choice Rules:
After testing, write down:
1. When should you use `for` loops?
2. When should you use `while` loops?
3. Which one felt more natural for each scenario?

---

## Challenge 3: Nested Loops - Patterns Within Patterns

### Part A: Simple Grid Pattern
```python
def draw_dot_grid(rows, cols):
    """Draw a grid of dots using nested loops"""
    start_timer()
    
    # Your code here!
    # Outer loop: move down for each row
    # Inner loop: draw dots across each row
    # Hint: use artist.goto(x, y) to position dots
    
    end_timer(f"Grid {rows}x{cols}")

def draw_square_grid(rows, cols, square_size):
    """Draw a grid of squares"""
    start_timer()
    
    # Your code here!
    # This will be slower - why do you think that is?
    
    end_timer(f"Square grid {rows}x{cols}")
```

### Part B: Fancy Nested Patterns
```python
def draw_spiral_of_polygons(num_polygons, sides):
    """Draw polygons arranged in a spiral pattern"""
    # Outer loop: position for each polygon
    # Inner loop: draw each polygon
    # Your code here!
    pass

def draw_rainbow_circles():
    """Draw concentric circles in different colors"""
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    # Outer loop: each color
    # Inner loop: draw circle with that color
    # Your code here!
    pass
```

### Performance Testing:
```python
# Test different grid sizes - watch the timing!
draw_dot_grid(5, 5)      # 25 operations
artist.clear()

draw_dot_grid(10, 10)    # 100 operations  
artist.clear()

draw_dot_grid(20, 20)    # 400 operations
artist.clear()

# What pattern do you notice in the timing?
```

---

## Challenge 4: The Time Complexity Detective

### Part A: Linear vs Quadratic Growth
Create these functions and time them:

```python
def draw_line_of_circles(n):
    """Draw n circles in a line - O(n) complexity"""
    start_timer()
    
    # Single loop: draw n circles
    # Your code here!
    
    end_timer(f"Line of {n} circles")

def draw_circle_filled_with_circles(n):
    """Draw n circles, each filled with n smaller circles - O(n²) complexity"""
    start_timer()
    
    # Nested loops: n * n total circles
    # Your code here!
    
    end_timer(f"Circle grid {n}x{n}")

def draw_triangle_pattern(n):
    """Draw a triangle made
