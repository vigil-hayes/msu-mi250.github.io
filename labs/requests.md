---
parent: Week 12
topic: Requests and Movies
git: https://gitlab.msu.edu/mi-250/using-apis
nav_exclude: false
visible: true
---

There is a limit to what you can do with python alone.  But the Internet has a wide range of additional services, and
you can use python to access them through APIs.  Today we are going to explore how to do this.

{% capture _ %}{% increment exercise %}{% endcapture %}

## Requests

We are going to begin by using a simple API that just gives us some current information.   To do this, we need to
install the *requests* library.  Using the command line, run the command:

```
pip3 install requests
```
(If you use VS Code's built-in python, you'll need to install requests through VS Code.)

Requests is a library that makes it easy to access APIs through web requests.

### Exercise {% increment exercise %}: Who is on the International Space Station?

There is an API available on `http://api.open-notify.org/` that provides information about the people who are currently
in space. One of the things that it can do is tell you who is currently present on the space station.   To get that, we
use the `astros.json` endpoint.

Use the requests library to retrive the list of current astronauts on the International Space Station and print out what
the API returns.

To query the API, you can use the `requests.get()` function, and tell it which endpoint you want to query. If you save
the results of that query into a variable called `people`, then you can print out `people.text` to see what it sent
back. (You will need to `import requests` at the top of your file to load the library.)

Start by looking at the file `iss.py` in the lab repository.  It has the correct URL for the API.   Call the
`requests.get()` function (after `import`ing requests) and pass in the URL for ISS information.  Then save the results
into a variable called `people`..

```
people = requests.get(astronauts)
```

The results is a complex variable with many parts.   You want to print out the `.text` part of that variable to see who
is on the ISS.

```
print(people.text)
```

### Exercise {% increment exercise %}: Parse the JSON response

You will notice that the response is actually quite complex.  It is in a data structure called "JSON".   Fortunately,
python makes it pretty easy to convert something from JSON to normal python dictionaries and lists.  We can use the
`json` library and use the `json.loads()` function to convert from JSON to python:

```
import json

info = json.loads(people.text)
```

Once you have loaded the json into a python dictionary, use `pprint()` (from the `pprint` library) to pretty print out
the whole dictionary.  When working with APIs, I have found that using `pprint()` to pretty print the resulting
dictionary is important for helping me to see the structure of the data that I get from the API.

*Hint*: You will probably need to `from pprint import pprint` for this exercise.

*Hint 2*: We use pretty printing back in the lab where we talked about complex python data structures -- [week 8](../8/lab.html).

### Exercise {% increment exercise %}: Human Readable Output

Once you have converted into a python dictionary, then you can use the normal python tools like for loops and `[]` to
access it.  For example, asking for `info['number']` will return the number of people currently in space, and
`info['people']` will return a *list* of dictionaries about the people currently in space.  Note each person is
represented by a dictionary with multiple keys, include `'name'`.

Convert the response of this API to python dictionaries, and then write code to make the output easier to read;
something like this:

```
Number of people in space: 3
Andrew Morgan
Oleg Skripochka
Jessica Meir
```

*Hint*: It is almost always best to go through a list with a `for` loop:
```
for person in response['people']:
	# The person variable now containts a dictionary for a person
```

*Hint 2*: The people currently in space frequently changes as people launch and land.  You might not get the same number
or same people as it was when I wrote this.  That's one of the coolest parts of APIs; they can be current and up-to-date.

## APIs with Parameters

You can think of an API request like you are calling a function -- except that function is somewhere else across the
internet.  Like functions, you can add parameters to the request to tell it more what you want to do.

You can add parameters to a request by putting the parameters in a dictionary, and passing it to the `requests.get()`
API call.

### Exercise {% increment exercise %}: Find words that rhyme with your name

[Datamuse](https://www.datamuse.com/api/) has a nice, easy to use API that will give you words that are related to other
words in various ways.   One thing you can do with this API is request words that *rhyme* (sound like) a word that you
provide.   To do that, you pass a parameter called `rel_rhy` (for "related" to by "rhyme") to the datamuse words API,
and set that paramter equal to the word you want to rhyme.

You can add parameters to a `requests.get()` call by putting them into a dictionary and then passing that
dictionary as a second parameter:
```
parameter = {"rel_rhy": "stuff"}
rhyming = requests.get(datamuse, parameter)
```

The file `rhyme.py` in the lab has the Datamuse API endpoint.   Create a dictionary with one item in it -- `rel_rhy` as
the key, and your last name as the value.  Then call the API, and print out what it returns.  Printing out the raw JSON
is fine; don't convert it or parse it yet.

*Hint*: You'll need to remember to `import requests` to use the requests library.

*Hint 2*: Remember, to get the JSON data out of the result of the API call, you need to use `.text` like you did in the previous exercises.

### Exercise {% increment exercise %}: Pretty print the JSON response

The raw JSON that is returned by DataMuse is complicated and hard to read.  This is unfortunately pretty normal for APIs
-- they give you a LOT of information, and you need to pick through it to get what you want out.

The first step is understanding what they give you back.  For this exercise, your goal is to pretty print the results
from the previous exercise.   You will need to first convert the results from JSON to a python dictionary using
`json.loads()`.  Then you can use the [`pprint()`](https://docs.python.org/3/library/pprint.html) function to print it
out in a readable form.

*Hint*: You will probably need to `import json` and `from pprint import pprint` for this exercise.

*Hint 2*: We use pretty printing back in the lab where we talked about complex python data structures -- [week 7](../7/lab.html).

### Exercise {% increment exercise %}: Accept user input, 

Let's make this rhyme finding program more user-friendly. 

Modify the program to accept user input.  Ask the user what word they want to find a rhyme for, and then pass
that word into the API.  You can do this the same way you have all semester by using the python `input()` command.

*Hint*: You will need to modify the dictionary you pass to the api to include the word input by the user.


### Exercise {% increment exercise %}: Print out the top 5 rhymes

The API returns the a complicated JSON thing.  You already converted the JSON to a python dictionary using
`json.loads()`. Now then print out the top 5 rhyming words (and only 5) that match.  Only print out 5 words, no more and
only print out the words (no scores or anything else in the dictionary).

For example, if I want to rhyme the word 'time', I could run the program and get:
```
What word do you want to rhyme? time
paradigm
sublime
rhyme
prime
crime
```

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

Both the Astronauts API and the Datamuse API can be used by anyone, without needing an account.  Most APIs are not that
open, though.  Most APIs require you to have an account and to authenticate (prove who you are) before you are allowed
to make queries.  This is more complicated for APIs than it is on normal websites; they don't just use a username and
password.  Instead, they use more complicated setups like OAuth or APIKey to do the authentication.

For today's lab, we are going to access the API at The Movie Database (TMDB). TMDB uses an access key for access.  You
have to create an account on TMDB's website, and ask it to generate an access key for you.  Then you need to include
that access key with every request you make, so they know it is you.

### Exercise {% increment exercise %}: Sign up for TMDB, Create a new app, and retrieve the access key.

In order to be able to access TMDB's API, you need to have a TMDB account.  If you do not already have a TMDB
account, go to <https://www.themoviedb.org/signup> and sign up for an account now.  You will need to verify your email
address before you can move forward.  Only one member of your pair needs to do this.


To access all of the TMDB developer features, use their developer portal: <https://developers.themoviedb.org/3/getting-started/introduction>.

Once you have signed in, you will see a profile icon next to the search icon in the upper right hand corner. Click on
that profile icon and it will bring up a menu. Choose choose "Settings".  On the settings page, there is an option on
the left called "API".  Click that.  You will see a list of all "Apps" that you have created.  For an API, an App is a
program that you are writing that needs permission to access the API.  As a developer, you can create more than one app
(if you want).  Most likely, you have no apps there right now.   Click on "Create" to create a new "App" for the program
we are writing, and then choose "Developer" option..

Accept the terms of service, and then TMDB will then present you with a form about that app that asks you for a lot of
information.  Fill it the form -- give your app a name, provide a description, etc.   You can use this website
(<http://mi250.cas.msu.edu>) for the required website.  Make it a personal app.  

Once you create the app, you will be taken to the App page that shows the information you just submitted.  On that page you should see the API key and the
access token.  These keys identify which app you are using, so TMDB (the company) can tell which program's API
access is being used.   Copy-and-paste those into the appropriate places in the file "movies.py" in our lab.

Once you've done this, you have everything ready to start access TMDB's API.

Let's test it.  Run the program "movies.py" with your API key.  If you get an API key error, then it didn't work.   If
you get a bunch of information about a movie, then it worked!


Congrats!  You now can access TMDB with a program!

### Exercise {% increment exercise %}: Pull out important movie information

When you run "movies.py", the TMDB API returns a data structure -- a complicated dictionary that contains lots of
information about the movie.   Right now, all the program does is print out the whole dictionary.  While this has some
useful information, it also prints out a ton of information that isn't needed.

Let's improve our movie information program by only having it print out the important information.   Modify "movies.py"
to only print out the title, tagline, and overview (in that order):

```
Black Panther: Wakanda Forever
Forever.
--------------
Queen Ramonda, Shuri, M’Baku, Okoye and the Dora Milaje fight to protect their
nation from intervening world powers in the wake of King T’Challa’s death. As
the Wakandans strive to embrace their next chapter, the heroes must band
together with the help of War Dog Nakia and Everett Ross and forge a new path
for the kingdom of Wakanda.
```

### Exercise {% increment exercise %}: Print out the genres also

Modify your movie program to print out the movie's genres also.  Notice that a movie can be in more than one genre, and
that TMDB gives you the genre in a list.  You'll have to use a for loop to loop through that list and print out the name
of each genre:

```
Black Panther: Wakanda Forever
Forever.
--------------
Queen Ramonda, Shuri, M’Baku, Okoye and the Dora Milaje fight to protect their
nation from intervening world powers in the wake of King T’Challa’s death. As
the Wakandans strive to embrace their next chapter, the heroes must band
together with the help of War Dog Nakia and Everett Ross and forge a new path
for the kingdom of Wakanda.
- Action
- Adventure
- Science Fiction
```

### Exercise {% increment exercise %}: Print out the stars also

Next, we are going to modify out movie program to get the list of people who starred in the movie, and print out their
names.

Notice that the data we get back from TMDB doesn't actually include the names of any of the actors (the 'cast') in the
movie.  Instead, we are going to need to make a *second* request of the API.  Copy and paste the code that makes the API
request, and change the URL to instead use the `movie_credits` URL.  Look closely at that URL; it is the word `movie`
followed by the ID number of the movie (24426) we want, followed by the word `credits`.

This should give you a second set of results.  It has two entries: `cast` is a list of actors in the movie, and `crew`
is a list of the production crew of the movie.  We only want to print out the cast for this exercise.

Once done, you should print the names of the cast members (at least the top 5 or 10):
```
Black Panther: Wakanda Forever
Forever.
--------------
Queen Ramonda, Shuri, M’Baku, Okoye and the Dora Milaje fight to protect their
nation from intervening world powers in the wake of King T’Challa’s death. As
the Wakandans strive to embrace their next chapter, the heroes must band
together with the help of War Dog Nakia and Everett Ross and forge a new path
for the kingdom of Wakanda.
- Action
- Adventure
- Science Fiction
Starring:
* Letitia Wright
* Lupita Nyong'o
* Danai Gurira
* Winston Duke
* Dominique Thorne
* Tenoch Huerta
* Angela Bassett
* Florence Kasumba
* Michaela Coel
* Mabel Cadena
```

*Hint*: You will probably need to change the printing code back to just pretty print the dictionary returned by the
credits API so you can see what it looks like.

*Hint 2*: The credits request returns a LOT of information.  So much that powershell or terminal might not be able to
display it all; when you scroll back you might not get all the way back to the beginning.   To deal with this, you can
limit how *deep* into the data structure you pretty print.  `pprint(info, depth=1)` only prints the top level
dictionary.  `pprint(info, depth=2)` prints the top level and one level underneath it.  That can help you see parts of
the dictionary when the data structure is REALLY big.


### Exercise {% increment exercise %}: Change to a Different Movie

Let's change our program to request information about a different movie.   Hopefully this should be pretty easy.  Let's
get information about the movie with TMDB ID number 600583.

What movie is that?


### Exercise {% increment exercise %}: Searching the Database

For all of the previous exercises, you need to know the exact movie ID number in order to get information about a
movie.  That isn't all that helpful if you don't already know the ID numbers.  So instead, we can search the database by
name.   

To do that, we need to use the API slightly different.  We need to specify a *search query*.  We do that as a parameter
to the API call.  We are already passing one parameter -- our `api_key`.  We need to add a second parameter called
`query` by adding it as an additional item in the parameter dictionary.  We can then use it to search for a movie by
name.

```
parameter = {"api_key": api_key, "query": "Avengers"}
result_json = requests.get(movie_search, parameter)
```

For this exercise, create a new program -- call it `search.py`.  Make your program to search TMDB for movies with the
word "Avengers" in the title.  You can and should copy code from your `movies.py` program as needed.

*Hint*: You will probably need to change the printing code back to just pretty print the resulting dictionary so you can
see what it looks like, since the search results dictionary looks different than the movie dictionary or the credits
dictionary.



## Challenges

### Challenge 1: Print Information About the Top Search Result 

When you search for a movie by name using the search API, most likely the first result is the movie you were looking
for.  Let's assume that it is.  

Combine the results of your last two programs / exercises.   Search for the movie "Harry Potter".  The first movie in the list of
results is probably the first Harry Potter movie.  In the dictionary that you get back from the API, you should be able
to find the ID number of that movie.   Then fill that ID number in to the URLs to get the movie name, tagline, and
overview, and also into the URL to get the cast.  Print out all of that information in a human-readable form like you
did in exercise 11.

This program in total should make 3 API queries in total: search, movie, and credits.

### Challenge 2: Movie Search Progarm (aka user input)

Take the program you wrote for challenge 1, and modify it to accept the search query as an input.  That is, your program
should ask the user what movie they want to know about. It will then search TMDB for that movie.   It will assume that
the first result is the movie the user is looking for, and remember the ID number for that movie.  Then it will use the
API to get inforamtion about the movie such as its full name, tagline, overview, and list of stars, and print out all of
that information.

This is creating a movie search tool.  You type in the name of a movie, and is prints out a bunch of information about
that movie.

