---
title: Tree Drawing
nav_exclude: false
visible: true
parent: Extra
nav_order: 1
has_children: false
---

# Turtle Tree Drawing Challenge
In this challenge, you'll create beautiful tree structures using Python's turtle graphics! You'll start by drawing simple branching patterns and work your way up to creating realistic-looking trees with random variations.

**What you'll learn:**
- Recursive functions (functions that call themselves)
- How to break down complex patterns into simple rules
- Working with angles and coordinates
- Using randomness in programming

## Setup
Make sure you have Python installed, then start with this basic template:

```python
import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(800, 600)

# Create a turtle
tree_turtle = turtle.Turtle()
tree_turtle.speed(0)  # Fastest drawing
tree_turtle.color("brown")

# Your code goes here!

# Keep the window open
screen.exitonclick()
```

## Challenge 1: Basic Tree with Variable Depth

### Your Mission
Create a function called `draw_tree()` that draws a tree by following these simple rules:
1. Draw a branch (line) forward
2. Turn left and draw a smaller tree
3. Turn right and draw another smaller tree
4. Stop when the branches get too small

### Function Requirements
```python
def draw_tree(branch_length, depth):
    """
    Draw a tree structure
    branch_length: how long the current branch should be
    depth: how many more levels of branches to draw (stop when depth = 0)
    """
    # Your code here!
```

### Rules to Follow:
- If `depth` is 0, don't draw anything (the tree is done!)
- Draw a branch forward using the `branch_length`
- Turn left 30 degrees, draw a smaller tree (reduce `branch_length` by 20, reduce `depth` by 1)
- Go back to where you started the branch
- Turn right 30 degrees, draw another smaller tree
- Go back to the starting position and reset your angle

### Test Your Function:
Try calling your function with different parameters:
```python
# Start at the bottom of the screen
tree_turtle.penup()
tree_turtle.goto(0, -250)
tree_turtle.setheading(90)  # Point upward
tree_turtle.pendown()

# Draw trees with different depths
draw_tree(100, 3)  # Small tree
# draw_tree(120, 5)  # Medium tree  
# draw_tree(150, 7)  # Large tree
```

### Hints:
- Use `turtle.forward()` to draw branches
- Use `turtle.left()` and `turtle.right()` to turn
- Use `turtle.backward()` to go back, or save your position with `turtle.position()` and `turtle.heading()`
- Remember: the function should call itself with smaller values!

---

## Challenge 2: Random Tree Generator

### Your Mission
Now make your trees look more natural by adding randomness! Modify your tree function to create unique trees every time.

### Enhanced Function:
```python
def draw_random_tree(branch_length, depth):
    """
    Draw a tree with random variations
    branch_length: starting length of branches
    depth: maximum depth (but might stop earlier randomly!)
    """
    # Your code here!
```

### New Random Elements to Add:
1. **Random early stopping**: Sometimes stop growing even when `depth > 0`
   - Use `random.randint(1, 10)` - if you get 1 or 2, stop early
   
2. **Random branch angles**: Instead of always turning 30 degrees
   - Use `random.randint(15, 45)` for turn angles
   
3. **Random branch length reduction**: Instead of always reducing by 20
   - Use `random.randint(15, 25)` for how much to reduce the length
   
4. **Random number of branches**: Instead of always 2 branches
   - Use `random.randint(2, 4)` to decide how many branches to draw
   - For 3+ branches, try different angles like -30°, 0°, +30°

### Bonus Features:
- **Seasonal colors**: Change turtle color based on branch size
  ```python
  if branch_length > 50:
      tree_turtle.color("brown")
  elif branch_length > 20:
      tree_turtle.color("green")
  else:
      tree_turtle.color("lightgreen")
  ```

- **Wind effect**: Add a slight bias to your random angles to make the tree lean

### Test Your Random Trees:
```python
# Draw several random trees
for i in range(3):
    tree_turtle.clear()
    tree_turtle.penup()
    tree_turtle.goto(0, -250)
    tree_turtle.setheading(90)
    tree_turtle.pendown()
    draw_random_tree(100, 6)
    input("Press Enter for next tree...")  # Pause between trees
```

---

## Reflection Questions

After completing both challenges, think about these questions:

1. **Pattern Recognition**: What pattern did you notice in how trees grow? How is this similar to other things in nature?

2. **Recursion**: How did breaking the tree into "smaller trees" make the problem easier to solve?

3. **Randomness**: How did adding randomness change the appearance of your trees? What other ways could you add variety?

4. **Real-world Applications**: Where else might you use this kind of "branching" pattern in programming or real life?

---

## Extension Ideas

Ready for more? Try these advanced features:

- **Leaves**: Add small circles or shapes at the end branches
- **Multiple tree types**: Create functions for pine trees, oak trees, etc.
- **Forest scene**: Draw multiple trees of different sizes
- **Animation**: Make your tree grow slowly by adding `time.sleep()` between branches
- **User interaction**: Let users click where they want trees to grow

Remember: The best way to learn programming is to experiment and have fun with it!
