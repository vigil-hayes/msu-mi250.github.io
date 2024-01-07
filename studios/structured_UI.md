---
parent: Week 8
topic: Structured User Interface
nav_exclude: true
visible: false
---

Imagine a post on social media, such as a Twitter (now X) post or an Instagram post. The post itself is actually a complex object that has a lot of information -- who posted it, the text content of the post, an optional picture, hashtags, the date and time when it was posted, etc. Each post on a given platform has the same structure, and is displayed the same way. But the content of each post -- the data that makes up the post -- is different.

Dictionaries work really well for structured objects like social media posts. For today's studio, you'll be designing your own social media post format with a UI (user interface) for displaying the post.

Your program should:
* have a dictionary structure for a post that stores all of the data and metadata associated with that post. 
* use Turtle to visually display all of the information in a post in a nicely formatted way. (You only have to display one post.)

It is up to you how you want the post to be structured, and what kinds of data it will have in it or associated with it. You can base your post design off of an existing social media platform, or you can create your own. Be creative! The only rule is that all of the data associated with a single post has to be stored in a single variable -- which means in a dictionary.

As per usual, work in groups of 2-4.

## Advice

Here's some advice that might help you out. But you don't have to take my advice; do whatever you want. 

### Take inspiration from existing designs

There are lots of social media platforms out there, and nearly all of them have the concept of a 'post'. But posts on each platform have different kinds of data associated with them. Look at what posts look like and what kinds of data are displayed for each post on the platforms you use to get an idea of what kinds of data you might want to include. Also look at *how* posts are displayed -- what size fonts are used for different things? Where is the post image displayed in relation to the text around it? How big is an average post in terms of width or height?

### Design the UI on paper first

[Wireframing](https://www.interaction-design.org/literature/topics/wireframing){:target="_blank"} is common technique in UX design to quickly sketch out how a webpage or app should look, or how a piece of it could look. On paper (or a whiteboard), wireframing is a quick and dirty way to figure out where elements should be placed relative to one another. 

It will probably be easier and faster to code the layout of your post in Turtle if you already have a visual guide for what the post should look like to refer to. Wireframes can also include information like how many pixels high or wide something should be - remember `forward()` using pixels to measure how far the Turtle should move. Font size also relates directly to pixels - a 12 point font is 12 pixels tall.

### Split up the work

There are two parts to this project: putting together a dictionary structure that works with different kinds of data, and drawing that data using Turtle. It might make sense to split your group up so that 1-2 people work on the data part and 1-2 people work on the Turtle part. The people working on the Turtle part can hard-code data that can then be replaced with data from the dictionary later on.

### Test with different data

Make sure that the structure you've created works with different sets of data. You'll probably want to create multiple dictionaries for the purposes of testing. Each dictionary should have the same structure (the same keys), but different data (different keys). This can help you determine the data types you need associated with each key -- for example, there can only be one post title, so you can use a string for the value. But there might be multiple hashtags associated with a post, which means you'd need a list to store them.

It can help to write out a template of what the dictionary structure should look like so that when you create new dictionaries to store different sets of data, they'll all have the same structure. For example:

```
post_title: string
hashtags: list
post_date: integer
num_likes: integer
```

### Use functions

Just like you used a function to print out pizza data in the lab, you could write a function that draws out post data using Turtle for this. Putting all of the Turtle code into a function can make it much easier to test your drawing with different sets of data -- you can just replace the dictionary variable when you use the function with one that contains different data.

For example, you could write a function called `display_post()` that does the work of drawing out the data using Turtle and takes one parameter, a dictionary. `post_1` could be a dictionary containing the data for a post. `post_2` could be a dictionary with the exact same structure, but with different data. To test your function with different sets of data, all you'd have to do is plug different dictionaries into the function -- `display_post(post_1)` would display a post using the data in the `post_1` dictionary. `display_post(post_2)` would do the same thing, but with the data in the `post_2` dictionary. 

It's very common to have different sets of data that you use to test to make sure a program works the way you expect; it's good to have an easy way to do this. Functions can be very useful for testing purposes.

### Import images into Turtle

Turtle allows you to import existing images into the Turtle drawing window, so long as those images are in .gif format. You can convert most images to .gif using Paint (Windows) or Preview (Mac). Open the image, and then go to File > Save As and choose GIF under Format. Note that Turtle won't display the animation in animated gifs.

Social media platforms do work behind the scenes to make sure all of the images that display in posts display at the same size. You might want to change the size of the images you use to specific pixel dimensions -- like make all images 150x150 pixels -- so that you can plan your post design around those specific dimensions. It's harder to plan consistent designs when the design elements aren't consistent.

To display an image in Turtle, you need to add it as a shape first, and then call the shape.

```
addshape("ship.gif")
shape("ship.gif")
```

Make sure the image file is in the same folder as the Python program that's trying to use it. *Note:* if you're running the Python program directly through VS Code, you'll need to navigate to the right folder in VS Code's terminal first or the program won't be able to find the image and will give you an error.

### What happens if data is missing?

For most types of social media posts, certain kinds of data are optional. For example, you can post on the platform formerly known as Twitter without including any images. The user interface adjusts the positioning of all of the elements of the post depending on whether there's an image or not. 

You can use if statements to test for whether data exists. A very basic version might look like this:

```
if dict['image'] == "":
    <don't move the turtle>
else:
    <insert image>
    <move turtle so it's below the image>
```

This code assumes that if there is no image associated with the `image` key in the dictionary, there will be an empty string (`""`) in its place.

## Challenge

If you've created a good structure and can use Turtle to print out a nicely formatted user interface for the post each time, great! Next step: make it interactive.

Instead of hard-coding the data for the post, collect it from the user. Exercises 6 and 7 from [the dictionary lab]({% link labs/dictionaries_as_data_structures.md %}){:target="_blank"} might be useful. Also remember you can use `textinput()` in order to collect user input through the Turtle window rather than through command line.

Remember when you collect user input, it all comes into Python as strings. You may need to convert the strings into other things so that they work with your dictionary structure. If you want the user to be able to enter multiple hashtags to associate with their post, for example, you could use a loop that keeps asking the user to enter a hashtag until the user tells it to stop and then put all of the hashtags then enter into a list with `.append()`

If your post structure uses images, there's no easy way to upload images to Turtle like there is on a real social media platform. But you can ask the user to input the name of the image file they want to use for the post.
 