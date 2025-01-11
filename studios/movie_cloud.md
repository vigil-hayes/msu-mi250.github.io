---
parent: Week 13
topic: Movie Cloud
nav_exclude: true
visible: false
---

For this studio, you should write a program that creates a Movie Cloud. A movie cloud is a word cloud, but about a movie. Your program should ask the user for the name of a movie. Then it should search that movie in The Movie Database, and get the list of actors in the movie. Using Turtle, it should draw the the name of the movie in big letters, and then should draw the actors' names in a word cloud of some sort.

There's also a lot of other kinds of data associated with movies. You don't have to limit yourself to making a word cloud with actors if you don't want to. Be creative!

Work in groups of 2-3, as per usual. 

## Advice

What follows is just advice for doing it. You don’t have to follow my advice. Do whatever you want. This is just my experience in doing this, and you might want to do it differently.

### Finish the Lab 

If you didn't finish this week's lab, you should make sure that at least one person in your group finished through Exercise 11 -- getting TMDB API access working. If not, go back and do Exercise 11, and possibly also all of the exercises after that. Specifically, you should make sure that you can retrieve and print out movie information from TMDB first.

If not everyone in your group finished the lab, ask the student(s) who got the furthest to show the code from the lab to the others in your group and explain how it works. That will help everyone be on the same page as you work on the studio today.

### Reuse Code

For [Studio 12]({% link studios/wordcloud.md %}), you wrote code to create a word cloud from a file. This studio is similar, but instead of pulling text data from a file, you'll be pulling it from a server using an API. Try to see if you can reuse any of the code you wrote for that studio. The studio instructions for Week 12 also have some good examples of what a word cloud can look like.

### How much data do you need? 

Think about how much data do you need to draw your word cloud?  Only getting 1 actor probably isn't enough to be meaningful. Getting 1000 actors seems like a lot. How much data do you want to use? You might want to limit the size of your cloud.

### Visual Size

You can do things to make your visualization more interesting.  For example, TMDB has a "popularity" score for each actor that indicates how popular she/he is. You could sort the list by popularity, and/or draw more popular actors in a larger font.

### Variation: Actor Cloud

Rather than just displaying a word cloud for a movie, can you make a version that takes an actor's name, and displays his/her movies? Each movie has a popularity score also that you could sort by or use to control the font size. Movies also have budget information, so you could make movies with bigger budgets have a larger font?  Be creative.

### Improve the wordcloud and the layout

You made word clouds last week also. You can and should definitely re-use that code for this week's studio. But think about how you can make it better. Can you make the layout of the words on the screen better?

You've got a movie that you are representing visually. Another way of thinking of the "movie cloud" is as a text-based movie poster. Have your program draw a poster-like representation of the movie on the screen with Turtle. Does that shift in mindset give you ideas for how it might look?

### Draw first before adding user input

Make sure your program can draw a nice looking cloud first before adding the feature that allows the user to specify which movie they want the cloud to be drawn for. That is, hard code a movie into your program and make sure it works with that movie before trying it with different movies.

If you're in a group of 3, it might make sense for 1-2 people to work on the user input portion while the others work on drawing the cloud
