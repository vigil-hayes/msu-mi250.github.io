---
parent: Week 10
topic: Tic Tac Toe
nav_exclude: false
visible: true
---

For the studio today, you are going to make a [game of Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe). You should draw an initial board (two vertical lines and two horizontal lines). Then ask the user where they want to move. Draw either an X or an O in the place they say. Let the user(s) continue until the whole board is full, or until the user decides someone has won.

That's all of the instructions. Form a group (of 2 to 4 people) and write a tic-tac-toe program. Have fun with it!

## Advice

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently.

### Work as a team

There are lots of parts of tic-tac-toe.  There's the user input side -- asking for where to move next. There is the drawing side. There is the figuring out of someone has won.

Spread out the work across the team. Have different people do different parts. Use functions to capture the different parts of the program. Use modules to break apart your code among group members. Use git to share code. This project is much easier if you break it into parts, and then do the parts separately, and then put them together. Make sure to leave time towards the end of class to put everything together; its not as easy as it sounds.

### Think about program structure

Think about how you want to structure your program. At a high level, what are the logical things that the program needs to do? How do they fit together in the program? What information needs to be send from one logical thing to the next? As you get started, it can be helpful draw out a diagram that describes what those pieces are, and what information need to move from one to the next.

### Break the program into pieces (functions)

This type of program is MUCH easier if you can write some functions to do it. It really helps if you can think ahead of time about what functions you will want in your program. This is called "organizing" your program.

Once you figure out the logical structure of your program, then use that to break the program into functions. If you try to write one big program that does the whole game, you will find it is really difficult. Each time you find yourself thinking you need the program to do something, write a function for that something. Need it to draw a symbol? Write a function for that. Need it to move the turtle to a new place? Write a function for that. Need to do the same thing more than once? Write a function!

For example, you could write a `draw_board()` function that draws the intiial board. You could write a `draw_x` function and a `draw_o` function that draws either an X or an O at the correct place. And you could write a function to get user input of a location and draw the appropriate symbol on the board.

### Use code you've written before

You've done a lot of programming already in this class.Use that! If you've already written code to draw a smiley face for a previous lab or studio, then go find that code and modify it. If you've already written code to ask for user input, go look it up and use it. There is no reason to write things from scratch when you've already written a lot of code.  

### Test each function as you go

It is MUCH easier to figure out if a single function works than if the whole program works. As you write each function, write some throwaway code to see if it works. WHen you write the draw board function, run it and see if the board looks right. When you write a function to draw an X on the board, run it to see if it works. Run it to draw X's in different places.

### Challenge 1: New Symbols

This is the easier challenge. X's and Os are very boring. Instead of using X's and O's, draw different symbols. Maybe do a game of pizza-and-sandwiches? Or a game of smileys and frowns? Be creative (and/or use your emojis from [the emoji studio]({% link studios/speak_in_emoji.md %}){:target="_blank"}).

In addition to different symbols, can you change the board up to make it more interesting? Create a theme for the board? Use colors?

### Challenge 2: When is the game done?

Your goal for this studio is just to allow users to play tic-tac-toe.  Your program doesn't need to detect when someone has won the game (3 X's or O's in a row) or when the game has ended in a stalemate. This is actually not easy to do.

As a challenge, if you finish your tic-tac-toe game early, try to figure out how you can tell if someone has won the game. To do this, you'll have to figure out how to store moves in a variable (like a list or a dictionary), and then you'll have to figure out how to look through that variable to see if there are 3 in a row.  

Detecting a stalemate (tie) is easy -- if there have been 9 valid moves, but no one has won yet, then the game is a stalemate.

Don't work on this until you get the main tic-tac-toe program working successfully.

