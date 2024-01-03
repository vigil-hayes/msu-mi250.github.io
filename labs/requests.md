---
parent: Week 13
topic: Requests Data Using APIs
git: https://gitlab.msu.edu/mi-250/using-apis
nav_exclude: False
visible: true
---

So far, we've been creating our own content to use in programs. We've been writing out stories and storing them as strings, or storing structure data in dictionaries, or putting text data in files and bringing it in to Python. For structured data, we've been writing it ourselves. But you may want to write a program that uses large amounts of structured data that already exists out in the world.

A large number of people, organizations, and companies that have their own data make their data available for public use. The U.S. government, for example, makes large amounts of data about the weather and the census and all sorts of things freely available to anyone who wants to use it. Some companies do this as well: Google Maps has a whole lot of map and location data that people can use to build their own map-based programs (though Google charges money in exchange for their data). 

How do people access this data? One way is to use an API, short for "application program interface". An API is a middle man that sits between the data and programs that use the data. People or organizations or companies create the API so that people who want to use their data have a way to access it via a programming language like Python. Today we're going to practice accessing data that's out there in the world by using Python to talk to APIs.

{% capture _ %}{% increment exercise %}{% endcapture %}

## Requests

### Exercise {% increment exercise %}: Install the requests library

We are going to begin by using a simple API that just gives us some current information. To do this, we need to install the `requests` library.  Using the command line, run the command:

```
pip3 install requests
```
(Note: if you are using VIsual Studio Code to run your code, you'll need to install `requests` through the terminal in VS Code.)

`requests` is a library that makes it easy to access APIs that are available through the web with Python.

### Exercise {% increment exercise %}: Who is on the International Space Station?

There is an API available on http://api.open-notify.org/ that provides a lot of interesting information from NASA, including things like the current position of the International Space Station (the ISS). We're going to use it today to find out which astronauts are currently on the ISS.

To get that, we will use the `astros.json` endpoint. This endpoint will return a JSON file with the astronauts' names. Endpoints for this API are URLs that contain the data. If you use the full URL (http://api.open-notify.org/astros.json) in a browser, it will show you the information in JSON format.

Use the requests library to retrieve the list of current astronauts on the International Space Station and print out what the API returns.

Start by looking at the file `iss.py` in the lab repository. First, make sure to include `import requests` at the top of your program so you can use the requests functions.

Next, let's query the API. To do this, you can use the `requests.get()` function. The URL for the endpoint you want to query is the parameter for the function. If we want to get a list of astronauts, then we will want to use the `astros.json` endpoint. Let's save the results of the query to a variable called `people`, like this:

```
people = requests.get(astronauts)
```

If you use `print` on the `people` variable, what happens? Nothing useful, because `people` is a complex object that can't be easily printed. We can access the text of the JSON object by using `.text` on the variable, like this:

```
people.text
```

Print out the JSON text showing the astronaut information.

*Hint:* The [Python API tutorial](https://www.dataquest.io/blog/python-api-tutorial/){:target="_blank"} from this week's readings might be useful to refer to for this exercise, and also for the next 2 exercises.

### Exercise {% increment exercise %}: Convert the JSON response to Python

You will notice that the response, which is in JSON, is actually quite complex. JSON is a format using specifically for storing complex data structures. Fortunately, Python makes it pretty easy to convert JSON to Python data structures, like dictionaries and lists. This allows us to use Python to do stuff with the data, like loop through it. 

We can use the `json` library and use the `json.loads()` function to convert from JSON to Python:

```
import json

info = json.loads(people.text)
```

Once you have loaded the JSON text into a Python dictionary, use `pprint()` (from the `pprint` library) to pretty print out the whole dictionary. When working with APIs, I have found that using `pprint()` to pretty print the resulting dictionary is important for helping me to see the structure of the data that I get from the API.

*Hint*: You will probably need to `from pprint import pprint` for this exercise.

### Exercise {% increment exercise %}: Number of people in space

Now we have a variable called `info` that is a dictionary with astronaut data in it. Let's look at the structure of the data the API is giving us. It's a dictionary with 3 keys: `message`, `number`, and `people`. The `people` key contains a list of dictionaries, and each dictionary in that list has two keys: `craft` and `name`.

The key `number` in this structure has a value that is an integer. If you look at the output when you pretty printing `info`, you'll notice that this number matches the number of astronauts.

Let's pull that number from the data and print out the number of astronauts in a human readable format, like this:

```
Number of people in space: 3
```

Remember you can get the value associated with a key in a dictionary with this format:

```
dict['key']
```

*Note*: The people currently in space frequently changes as people launch and land. You might not get the same number that I did when I wrote this. That's one of the coolest parts of APIs; they can be current and up-to-date.

*Hint:* The [Dictionaries as Data Structures]({% link labs/dictionaries_as_data_structures.md %}) lab might be useful to refer to for a refresher on how to access data from complex structures like dictionaries.

### Exercise {% increment exercise %}: Astronaut's names

The number of astronauts is only one level deep in the `info` dictionary, so it was pretty easy to get. How would we print out the names of the astronauts? To do this, you need to go three levels deep. For example, if we wanted to print out the name of the first astronaut that's listed, we'd need to target the key `people`, then the first dictionary in the list of people, and then the key `name` for that dictionary. The code would look like this:

```
info['people'][0]['name']
```

When you use `print()` on that line of code, it should print out the name of one astronaut.

For this exercise, we want to print out the names of all of the astronauts, not just the first one. Remember you can go through a list using a `for` loop. The list you want to loop through is `info['people']`. Remember you also want to target the `name` key once you get into a dictionary inside the list.

When you're done, what your program prints out should look like this:

```
Number of people in space: 3
Andrew Morgan
Oleg Skripochka
Jessica Meir
```

*Hint:* If you set up a `for` loop to go through the list `info['people']` like this:
```
for person in info['people']:
```
then `person` represents each item in the list. In this for loop, `person` represents a dictionary, and you can use dictionary syntax (`dict['key']`) to target the key called `name`.

## API Requests with Parameters

Requests can be more specific than just asking for a URL. You can add parameters to a request by putting the parameters in a dictionary and then passing the dictionary to the `requests.get()` function as a parameter.

### Exercise {% increment exercise %}: Find words that rhyme with your name

[Datamuse](https://www.datamuse.com/api/) has a nice, easy to use API that will give you words that are related to other words in various ways. One thing you can do with this API is request words that *rhyme* (sound like) a word that you provide. To do that, you pass a parameter called `rel_rhy` (for "related" to by "rhyme") to the datamuse words API and set that paramter equal to the word you want to rhyme.

You can add parameters to a `requests.get()` call by putting them into a dictionary and then passing that dictionary as a second parameter:
```
parameter = {"rel_rhy": "stuff"}
rhyming = requests.get(datamuse, parameter)
```

The file `rhyme.py` in the lab has the Datamuse API endpoint. Create a dictionary with one item in it -- `rel_rhy` as the key, and your last name as the value. Then call the API, and print out what it returns.  Printing out the raw JSON is fine; don't convert it to Python or parse it yet.

*Hint*: You'll need to remember to `import requests` to use the requests library.

*Hint 2*: Remember, to get the JSON data out of the result of the API call, you need to use `.text` like you did in the previous exercises.

### Exercise {% increment exercise %}: Pretty print the JSON response

The raw JSON that is returned by DataMuse is complicated and hard to read. This is unfortunately pretty normal for APIs -- they give you a LOT of information, and you need to pick through it to get what you want out.

The first step is understanding what they give you back. For this exercise, your goal is to pretty print the results from the previous exercise. You will need to first convert the results from JSON to a Python dictionary using `json.loads()`, just like in Exercise 3. Then use the `pprint()` function to print it out in a readable form.

What does the structure of this look like? Look for where there are list structures (look for square brackets, `[]`) and dictionary structures (look for curly braces, `{}`). Look at how the different structures are nested within one another by looking for where a bracket or brace begins and ends, and what's inside of it. Understanding how data is structured can help you figure out how to get what you need from the data.

Also look at how the data is organized. In this case, the words are in descending order based on a "score" - the score indicates how closely each word rhymes with the word you gave it.

*Hint*: You will need to `import json` and `from pprint import pprint` for this exercise.

### Exercise {% increment exercise %}: Print out the rhymes

The API returns the a complicated JSON object. You already converted the JSON to a Python data structure using `json.loads()` in the last exercise. Now then print out all of the words that rhyme with your last name. Only print out the words: no brackets or scores or anything else in the dictionary.

For example, if I want to rhyme the word 'time', I could run the program and get:

```
paradigm
sublime
rhyme
prime
crime
...
```

Try it with different words. Notice the list is longer for some words than it is for others.

*Hint:* You should only need 1 `for` loop for this.

### Exercise {% increment exercise %}: Accept user input 

Let's make this rhyme finding program more user-friendly. 

Modify the program to accept user input. Ask the user what word they want to find a rhyme for, and then pass that word into the API. You can do this the same way you have all semester by using the Python `input()` command.

Add some text above the rhyming words so the user knows which word the list of rhymes is for, like this:

```
These words rhyme with "time":
paradigm
sublime
rhyme
prime
crime
...
```

*Hint*: You will need to modify the dictionary you pass to the api to include the word input by the user.

### Exercise {% increment exercise %}: Print only the top 10 rhymes

The list it gives you sure can be long. Modify your program so it only prints the top 10 words by score.

*Hint:* The words are already organized in order by score, so you probably don't have to do any extra work to make sure the order is correct.

*Hint 2:* Remember you can use a counter and increment it to keep track of how many times the loop has run, and then break out of the loop when the counter reaches a certain number. But there are other ways to do this.

<!--
### Exercise  increment exercise : Spelling corrector

[Datamuse](https://www.datamuse.com/api/) can do things other than rhyming.  One of the things that it can do is make
suggestions for correcting your spelling.   To do this, instead of passing in the `rel_rhy` parameter, you pass in an
`sp` parameter.

Write a new `spelling.py` program that asks a user for a (possibly misspelled) word, sends that word to the Datamuse
API, and reports back any possible corrected spellings.  You might want to start with your code from `rhyme.py`, and
"Save as" spelling.py.

### Exercise  increment exercise : Only print out good results

If you look at the JSON that the spelling API returns, it gives a list of words, and a "score" for each word.  The score
is how well the word matches, with higher scored being more likely. 

Modify your spelling program to have a cutoff (that you, as the programmer, decide), and then only print out words that
have a score that is above the cutoff -- that is, only print out words that are highly likely to be the word the user
was thinking.

-->

## APIs with authentication

Both the Astronauts API and the Datamuse API can be used by anyone, without needing an account. Most APIs are not that open, though. Most APIs require you to have an account and to authenticate (prove who you are) before you are allowed to make queries. Some also require you to pay to be able to access data through the API. We're only using free APIs for this class. 

Authentication is more complicated for APIs than it is on normal websites; they don't just use a username and password. Instead, they use more complicated setups like OAuth or APIKey to do the authentication. Authenticating requires that you have a special key that you then put into your code so that every time your program makes a request, it's logged under your username.

For today's lab, we are going to access the free API at The Movie Database (TMDB). TMDB uses an access key for access. You have to create an account on TMDB's website, and ask it to generate an access key for you.

### Exercise {% increment exercise %}: Sign up for TMDB, Create a new app, and retrieve the access key.

In order to be able to access TMDB's API, you need to have a TMDB account. If you do not already have a TMDB account, go to <https://www.themoviedb.org/signup> and sign up for an account now. You will need to verify your email address before you can move forward. Only one member of your pair needs to do this (you can both do it if you want, but you'll only need one key).

To access all of the TMDB developer features, use their developer portal: <https://developers.themoviedb.org/3/getting-started/introduction>.

Once you have signed in to TMDB, you will see a profile icon next to the search icon in the upper right hand corner. Click on that profile icon and it will bring up a menu. Choose "Settings". On the settings page, there is an option on the left called "API". Click that. You will see a list of all "Apps" that you have created. For an API, an App is a
program that you are writing that needs permission to access the API.  As a developer, you can create more than one app (if you want). Most likely, you have no apps there right now. Click on "Create" to create a new "App" for the program we are writing, and then choose "Developer" option.

Accept the terms of service, and then TMDB will then present you with a form about that app that asks you for a lot of information. Fill it the form -- give your app a name, provide a description, etc. You can use this website (<http://mi250.dev>) for the required website. Make it a personal app.  

Once you create the app, you will be taken to the App page that shows the information you just submitted. On that page you should see the API key and the access token. These keys identify which app you are using, so TMDB (the company) can tell which program's API access is being used. Copy and paste the API key into the appropriate place at the top of `movies.py`.

Once you've done this, you have everything ready to start access TMDB's API.

Let's test it. Run the program "movies.py" with your API key. If you get an API key error, then it didn't work. If you get a bunch of information about a movie, then it worked!

Congrats!  You now can access TMDB with a program!

### Exercise {% increment exercise %}: Pull out important movie information

When you run "movies.py", the TMDB API returns a data structure -- a complicated dictionary that contains lots of information about the movie. Right now, all the program does is print out the whole dictionary. While this has some useful information, it also prints out a ton of information that isn't needed.

Let's improve our movie information program by only having it print out the important information. Modify "movies.py" to only print out the title, tagline, and overview (in that order):

```
Spider-Man: Across the Spider-Verse
It's how you wear the mask that matters.
--------------
After reuniting with Gwen Stacy, Brooklyn’s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters the Spider Society, a team of Spider-People charged with protecting the Multiverse’s very existence. But when the heroes clash on how to handle a new threat, Miles finds himself pitted against the other Spiders and must set out on his own to save those he loves most.
```

### Exercise {% increment exercise %}: Print out the genres also

Now modify your movie program to also print out the movie's genres. Notice that a movie can be in more than one genre, and that TMDB gives you the genre in a list. You'll have to use a `for` loop to loop through that list and print out the name of each genre:

```
Spider-Man: Across the Spider-Verse
It's how you wear the mask that matters.
--------------
After reuniting with Gwen Stacy, Brooklyn’s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters the Spider Society, a team of Spider-People charged with protecting the Multiverse’s very existence. But when the heroes clash on how to handle a new threat, Miles finds himself pitted against the other Spiders and must set out on his own to save those he loves most.

Genres:
- Animation
- Action
- Adventure
- Science Fiction
```

### Exercise {% increment exercise %}: Print out the stars also

Next, we are going to modify out movie program to get the list of people who starred in the movie and print out their names.

Notice that the data we get back from TMDB doesn't actually include the names of any of the actors (the 'cast') in the movie. Instead, we are going to need to make a *second* request of the API. Copy and paste the code that makes the API request and change the URL to instead use the `movie_credits` URL. Look closely at that URL; it is the word `movie`
followed by the ID number of the movie (569094) we want, followed by the word `credits`.

This should give you a second set of results. It has two entries: `cast` is a list of actors in the movie and `crew` is a list of the production crew of the movie. We only want to print out the cast for this exercise.

Beneath the rest of the movie info, print the names of the cast members (at least the first 5 or 10):

```
Spider-Man: Across the Spider-Verse
It's how you wear the mask that matters.
--------------
After reuniting with Gwen Stacy, Brooklyn’s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters the Spider Society, a team of Spider-People charged with protecting the Multiverse’s very existence. But when the heroes clash on how to handle a new threat, Miles finds himself pitted against the other Spiders and must set out on his own to save those he loves most.

Genres:
- Animation
- Action
- Adventure
- Science Fiction

Cast:
- Shameik Moore
- Hailee Steinfeld
- Jason Schwartzman
- Oscar Isaac
- Brian Tyree Henry
...
```

*Hint*: You will probably need to change the printing code back to just pretty print the dictionary returned by the credits API so you can see what it looks like.

*Hint 2*: The credits request returns a LOT of information. So much that PowerShell or Terminal might not be able to display it all; when you scroll back you might not get all the way back to the beginning.   To deal with this, you can limit how *deep* into the data structure you pretty print. `pprint(info, depth=1)` only prints the top level dictionary. `pprint(info, depth=2)` prints the top level and one level underneath it. That can help you see parts of the dictionary when the data structure is REALLY big. Note also that PowerShell or Terminal will print more than the terminal inside VS Code will.


### Exercise {% increment exercise %}: Change to a Different Movie

Let's change our program to request information about a different movie. Hopefully this should be pretty easy. Let's get information about the movie with TMDB ID number 438631.

What movie is that?


### Exercise {% increment exercise %}: Searching the Database

For all of the previous exercises, you need to know the exact movie ID number in order to get information about a movie. That isn't all that helpful if you don't already know the ID numbers. So instead, we can search the database by name.   

To do that, we need to use the API slightly different. We need to specify a *search query*. We do that as a parameter to the API call.  We are already passing one parameter -- our `api_key`. We need to add a second parameter called `query` by adding it as an additional item in the parameter dictionary. We can then use it to search for a movie by
name.

```
parameter = {"api_key": api_key, "query": "Spider-Man"}
result_json = requests.get(movie_search, parameter)
```

For this exercise, create a new program -- call it `search.py`. Make your program to search TMDB for movies with the word "Spider-Man" in the title. You can and should copy code from your `movies.py` program as needed.

*Hint*: You will probably need to change the printing code back to just pretty print the resulting dictionary so you can see what it looks like, since the search results dictionary looks different than the movie dictionary or the credits dictionary.


## Challenges

### Challenge 1: Print Information About the Top Search Result 

When you search for a movie by name using the search API, most likely the first result is the movie you were looking for. Let's assume that it is.  

Combine the results of your last two programs / exercises. Search for the movie "Harry Potter". The first movie in the list of results is probably the first Harry Potter movie. In the dictionary that you get back from the API, you should be able to find the ID number of that movie. Then fill that ID number in to the URLs to get the movie name, tagline, and overview, and also into the URL to get the cast. Print out all of that information in a human-readable form like you did in exercise 11.

This program in total should make 3 API queries in total: search, movie, and credits.

### Challenge 2: Movie Search Program (aka user input)

Take the program you wrote for challenge 1, and modify it to accept the search query as an input. That is, your program should ask the user what movie they want to know about. It will then search TMDB for that movie. It will assume that the first result is the movie the user is looking for, and remember the ID number for that movie. Then it will use the API to get inforamtion about the movie such as its full name, tagline, overview, and list of stars, and print out all of that information.

This is creating a movie search tool. You type in the name of a movie, and is prints out a bunch of information about that movie.

### Challenge 3: Better Movie Search Program

This builds on Challenge 2. Modify your program so that it prints out the movie titles for the top (5? 10? 20?) results of the search and allow the user to choose the movie they want. Then print out ,more information about the movie they choose.

