---
parent: Week 12
topic: Movie Cloud
nav_exclude: false
visible: true
---

For this studio, you should write a program that creates a Movie Cloud.  A movie cloud is a word cloud, but about a
movie.   Your program should ask the user for the name of a movie.  Then it should search that movie in The Movie
Database, and get the list of actors in the movie.  Using turtle, it should draw the the name of the movie in big
letters, and then the list of the top actors in the movie.

---

That's it.   Get a movie name, query TMDB, draw a word cloud of actors . Have fun with it. Be creative.

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my
experience in doing this, and you might want to do it differently.

## Advice

### Reuse Code

Last week in [Studio 11]({% link studios/wordcloud.md %}) you wrote code to create a word cloud from a file.  This studio is similar.
Try to see if you can reuse any of the code you wrote last week to help with this week's studio.  Last's weeks
instructions also include examples of word clouds to help you with inspiration.

### Finish the Lab 

If you didn't finish this week's lab, you should make sure that at least one person in your group finished through
Exercise 8 -- getting TMDB API access working.  If not, go back and do Exercise 8, and possibly all of the exercises.
Specifically, you should make sure that you can retrieve and print out movie information from TMDB first.

If not everyone in your group finished the lab, ask the student(s) who got the furthest to show the code from the lab to
the others in your group and explain how it works.  That will help everyone be on the same page as you work on the
studio today.

### How much data do you need? 

Think about how much data do you need to draw your word cloud?  Only getting 1 actor probably isn't enough to be
meaningful.   Getting 1000 actors seems like a lot.  How much data do you want to use?  You might want to limit the size
of your cloud.

### Visual Size

You can do things to make your visualization more interesting.  For example, TMDB has a "popularity" score for each
actor that indicates how popular she/he is.  You could sort the list by popularity, and/or draw more popular actors in a
larger font.

### Expand to Actor Cloud

Rather than just displaying a word cloud for a movie, can you make a version that takes an actor's name, and displays
his/her movies?  Each movie has a popularity score also that you could sort by or use to control the font size.  Movies
also have budget information, so you could make movies with bigger budgets have a larger font?  Be creative.


### Improve the wordcloud and the layout

You made word clouds last week also.   You can and should definitely re-use that code for this week's studio.  But think
about how you can make it better. Can you make the layout of the words on the screen better?

You've got a movie that you are representing visually.  Another way of thinking of the "movie cloud" is as a text-based
movie poster.  Have your program draw a poster-like representation of the movie on the screen with turtle.  Does that
shift in mindset give you ideas for how it might look?


### Challenge: User Input

Once you get a movie cloud drawn, try to accept user input.   Allow the user to
type in the name of a movie.  Get the list of actors for that movie, and draw
them on the screen in a movie cloud.   Try it out; can you make it work for multiple different movies?

