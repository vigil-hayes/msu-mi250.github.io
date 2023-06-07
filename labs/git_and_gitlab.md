---
parent: Week 2
topic: Git and GitLab
git: https://gitlab.msu.edu/mi-250/git-and-gitlab
nav_exclude: false
visible: true
---

# Your own git repository

In the readings, you read about version control and git.  A repository is a specific, named collection of files that
usually make up a single program.  You've already used a git repository without really knowing it; all of the files for
last week's lab were stored in a git repository, which you accessed through a webpage (GitLab).

Today, the first thing you are going to do is to get your OWN copy of the repository on your computer. 

## Make a copy for your pair (only do once)

At the top of this page, there is a link to this week's GitLab project. Click on that link and open it in a new
window. What opens is a web interface to MY project on GitLab.  GitLab is a system hosted by MSU that allows you to
create new projects. Each project in GitLab has a git repostoriy in it.  GitLab allows you to share them with other
people as much as you want, for free.  One of you will have to log into GitLab with your NetID and password in order to
be able to see the project and repository.

The webpage you see represents a GitLab project.  If you look around, you can see that there are files in that project.
Those files are in the repository that is inside the project.  Each project has one repository that contains the files
for the project.  There are also a lot of controls along the left side of the web page that allow you to do things like
see the activity on the project, report bugs ("issues") in the code, or change settings.  There is a "history" button on
the top right that allows you to see every change I've ever made to that project.  (Click it!)

This first thing we are going to do is to **fork** the project.   Forking a project means making a wholely new
project that is a copy of this project.  It creates its own copy of the repository/files and also copies its own
settings and everything about it.

To do this, look for the "fork" button along the top of the webpage, and click that.  It will ask you for a 'namespace';
there should be only one option, with your name.  Click on that to start the forking. Forking will take a moment.  Once
it finishes, then it will take you to the new project.  The new project should look almost the same as the original --
it is a copy, after all!  The main difference is if you look at the top, instead of saying "MI-250 / Git and Gitlab", it
should say your name now.  If it does, then great! It worked!  If not, then ask the instructor or TA for some
assistance.   (Sometimes you may get a 404 Error page. That happens when forking is slow.  Just wait a minute and hit
"refresh" and it usually fixes itself.)

The first thing you should do after forking a project is to give your pair partner access to the project.  To do this,
click on settings on the left, and then go to "members".  This is the page where you can give other people access.  Find
your partner's name in the search bar.  Then change the "role permission" to "Maintainer" -- the highest level of
permissions.  Then click "add to project"  This will add them to the project.

Next, the navigator (who was just added to the project) should try to log into Gitlab
[https://gitlab.msu.edu](https://gitlab.msu.edu) and click on "Projects" -> "Your Projects".  She or he should see the
"Git and Gitlab" project on the list, and be able to click on it and view it.

Congrats!  You've now got your first GitLab project!  Good work!


## Set up your computer to use the new git repository

You've now got your own project, but right now it only exists on GitLab.  That's great -- it is on a webpage where
others can see it also.  But it is hard to work with it on a webpage.  All of the programming work you've done in this
class is on your personal computer.  It is difficult to do programming on a webpage.

To work with on your computer, we need to get a copy of the *repository* -- the files stored inside the project.   To do
that, we will use git.

### Install Git

The first thing you'll need to do is download and install Git onto your computer.  You can do that from the [Git
Downloads Page](https://git-scm.com/downloads).  Do that now. If you are on a Mac, choose the "Binary Installer"

On Windows, it will ask you a lot of questions.  Just click next on ALMOST all of them.  There is one question -- What
do you want your default editor to be? -- that you need to answer.  Click on the dropdown and choose the text editor
that you use for editing in this class.  On Mac, it won't ask this.

Once you've got that installed, open up a command line window (either Powershell or Terminal). If you just type the
command `git`, it should print out a bunch of help information about the different git commands.  If it does that, then
you've got git installed correctly!  If you get an error message, then you didn't install git correctly yet.

The first thing we need to do is to set up git by telling it who we are and what editor we use.  Use the following two
commands to tell it who you are, substituting your name and email address for mine:

```
git config --global user.name "Rick Wash"
git config --global user.email "wash@msu.edu"
```
Be sure to keep the quotation marks.   You should only need to do this once on your computer; after that, it will
remember who you are.

#### Mac OS

Next, only for Mac OS, we need to tell git what text editor we use.   This is harder on Macs than on Windows.  On
Windows, you already told it what editor to use when you installed it.  So skip this section; you only have to do this
if you didn't tell git what editor to use.

On Mac, there isn't a good text editor built in, so we need to tell it to use the one you installed during Week 0.

If you use BBedit, then click on the BBEdit menu in the upper left corner, and choose "Install Command Line Tools".
After that is done, then run this command to tell git to use BBedit:

```
git config --global core.editor "bbedit -w"
```

If you use VS Code, then goto the menu and find "Install 'Code' command in path".  Once you choose that, then run this
command on the command line to tell git to use VS Code:

```
git config --global core.editor "code --wait"
```

### Create a GitLab Access Token

Gitlab recently changed to not allow passwords.  Instead, you need to use something called an "Access
Token" instead of your NetID and password.  To create an access token, go back to the GitLab webpage and click on the
image in the upper right hand corner of the page and choose "Preferences" for your user.  Then, on the page that
appears, in the menu on the left, choose "Access Tokens".  On this page, you can create an access token, which is
basically a temporary password for you to use.  

Type in your NetID in the "Token Name" field.  Then choose an expiration date that is sometime after May 2023.  It is
important that you click the "write_repository" checkbox, because that allows this password to access your repositories.
Then click the "Create personal access token" button. The webapge will reload, and near the top, it will print out a new
"access token" which is basically a randomly generated password for you to use.

**Write down this access token**.  (Or copy-and-paste it somewhere you can find it.)

You should only need to do the access token thing today; after completing this lab, git should remember it and never ask
you again.


### Fork and Clone the Repository

On your computer, you should make a place to keep your work for this class -- all of the labs and studios that you work
on. Me, personally, I created a folder on my desktop called "MI 250" and keep everything in there.  But its your
computer, and you can put it whereever you want.

To work with a repository on your computer, you need to "clone" the repository -- which means that we need to download
the repository onto your personal computer so you can work with it.   First, let's set up your computer to be ready to
clone.   Open up a command line (using either Terminal (Mac OS) or PowerShell (Windows), as we did last week).  Then
change directories to the directory where you want to keep your files using the `cd` command.  Remember, like last week,
you can drag a directory from Explorer/Finder onto the command line, and it will type in that directory name for you
onto the command line.

If you are using an MI 250 folder on your desktop like I do, then the command to change directories is
```
cd Desktop/MI\ 250
```

If you look at *your* project page on GitLab, in the upper right hand corner there is a blue button labled "Clone".  If you
click on that, you get two options: "Clone with SSH" and "Clone with HTTPS". Those are just two different ways of
accomplishing the same thing.   In this class, we are going to use the 2nd option: "Clone with HTTPS".  Click the button
next to that option, and it will copy a link to the repository onto your clipboard.

Next, we want to use the command line to actually clone the project.  By default, this command will clone the project
into whatever directory you are currently in on the command line.  That's why it was important that we `cd` into our
folder for this class before running this command.  

Use the command `git clone` to clone the project.  On the command line, type in `git clone ` and then paste in the link
that you copied from the Gitlab website.  It should look something like this:

```
git clone https://gitlab.msu.edu/wash/git-and-gitlab.git
```

When you do this, it will ask you for your username and password. Don't enter your real password!  Instead, Log in with
your NetID (don't include `@msu.edu`) and then use your newly created "access token" as the password.  If this works,
then it should print out information telling you it is "receiving objects", which means it is downloading the files for
the repository for you.

Once it has downloaded, you will get a prompt on the command line again.  If you use the command `ls`, you should see a
new directory called "git-and-gitlab". Change directories into that using the command `cd git-and-gitlab`.  If you do an
`ls` again, you'll see that all of the files from the repository have now been downloaded onto your computer and are
there for you to work with.  If you look at the folder in Exporer/Finder, then you should also see the files.

## Make a change

Next, let's make a change.  Open up the file `README.md` in your text editor.  Right now, it has my name (Rick Wash) in
there as the author.   That's not longer true -- this is YOUR repository now!  Change the name to your name.

## Commit and Push the change

Now, you've change the file on your local computer.  But if you go look at the file in the repository on GitLab, it
still has my name in it. That is because you haven't committed or pushed your change; that is, you haven't made the
change official.   Git has this idea that you can edit lots of files, and try lots of things out, but it is only when
you make something official that it actually gets recorded and put into the repository.  And this process of making
things official is something you have to do by hand, intentionally.

Doing this has three steps: add, commit, and push.  Each of these steps is important, so let's walk through them.

#### Add

Start by running the status command on the command line:
```
git status
```

This command will show you the current status of the local clone of your git repository that is on your computer.  It
will let you know if any files have been modified since the last version you got, and if any files have been added or
deleted.  You should see that you've modified the `README.md` file.

The first step is to let git know what changes go together.  Sometimes you make changes in multiple different files, and
you want all of those changes to logically go together as one commit.   To do this, git has what it calls a "staging
area" -- a place you put changes until you've got the whole set of them together.   You use the command `git add` to add
things to this staging area.  You can run this command multiple times if you want to add changes from more than one file
to the same commit.  

We only have one file with changes -- `README.md` -- so we only need to add one file to the staging area.  Let's do so
with the `git add` command:
```
git add README.md
```

If this works correctly, then it won't print anything out.  It will just give you a new prompt.  If it doesn't work,
then you'll get an error message.

Note: On many systems, the filename is case sensitive; so if you get an error message, try to make sure the case is
correct.

#### Commit

Once you've got all the changes together in the staging area, the next step is to "commit" those changes.  Committing
the changes takes all those changes, and creates a new version of your program that has those changes.  That is, it
formally records that these changes compromise a new version of your program.

To do this, we use the command `git commit`.

```
git commit
```

When you type "git commit" and hit enter, your default text editor should open up.
A new file will open up in your text editor. Type the commit message on the first line of the file.
SAVE and CLOSE the file! Once you do this, the commit should go through in PowerShell/Terminal.

When you run that command, then git will ask you for a message.  This is a description what changes you are making.  This
description becomes an official part of the record -- you can sit it in GitLab by looking at the History of the
repository. It is important to put a good, descriptive message here so that you -- future you -- can remember what
changes you made and why you made them.

When you close the window with the commit message, git should complete the commit.

If a file doesn't open when you `git commit`, then look at the Troubleshooting section at the bottom of this page.

#### Push

Committing the changes only records the changes in the clone of the repository that is on your computer.  If you look at
Gitlab, your changes haven't made it to the main repository yet.  That's what `git push` does -- it takes any changes
that are on your current computer that you've committed, and it pushes them up to the main repository on Gitlab.   Run
that command now:
```
git push
```

Now go check the main Gitlab page.  Don't forget to refresh the page.   When you look at the README.md file, it should
have your name in it now instead of my name.  That means that you have successfully commited your first change to a git
repository!  Good work!


## Swap and Repeat

The biggest benefit of git is collaboration -- it makes it easier to work with other people on the same program.  The
next step of today's lab is to learn how that works by swapping roles.  The current driver (the person at the keyboard)
will become the navigator, and the navigator will become the driver.  And you should now use the navigator's computer.

Go through all of the same steps, starting with "[Set up your computer to use the new git repository](#set-up-your-computer-to-use-the-new-git-repository)"
on the navigator's computer.  When you edit the file, *add* your name to the file, so that it says "By: Driver Name and
Navigator Name".  Be sure to add, commit, and push the changes, and then check on the GitLab to make sure that the
changes appear there.

Once you've done this, then there should be a single git repository in the GitLab, and both members of the pair should
have a clone of that git repository on their personal computer.  Either person can work on the program, and then commit
and push changes back to the repository at any time.  This makes collaboration easier, because both people have a copy,
and both people can work on it.

### Git Pull

Swap roles again, so that the original driver is now driving again using their own computer.

If you look at the files on your computer, then you'll notice that the newest change -- the one that adds the
navigator's name to `README.md` -- aren't there.  What is happening is that there are changes in the main GitLab
repository, but they haven't been copied down to your computer yet.

To do that, we can use the command `git pull`.  This command will take all of the changes that are in the main
repository, and pull them down to your computer.  Run that now:
```
git pull
```

Now open the README.md file in the text editor on your computer, and you should see the changes, including both people's
names.

You want to run this command any time that your partner makes any changes and then commits and pushes those changes to
the repository.   

Git can be used by as many people as you want; there are git repositories with millions of people using them.  Always
remember to `git pull` to make sure you have all the latest changes before you start working.


# Programming

Now that you've got the git repository, we can start working on programming in the files in that repository.

We are going to begin with the program `bottles.py`, which is a simple program that prints out lyrics to a song -- the
song [99 bottles of beer](https://en.wikipedia.org/wiki/99_Bottles_of_Beer).  

The first thing to do is to run the program on the command line:
```
python bottles.py
```

You should see it print out two verses of the song.

### Exercise 1: Change the beverage

Right now, the song is being sung about water.   The original song was about beer.  What is your favorite beverage?
Pick a new beverage, and change the song so that it is being sung about your favorite beverage.

### Exercise 2: Last verse

The last verse gets down to zero bottles.   No one likes singing about "zero" bottles.   Most of the time, that last
verse gets modified; for example, the Wikipedia article lists "No more bottles of beer on the wall, no more bottles of
beer." as the last verse.  

Create a last verse that is more interesting for the song; one that doesn't use the word or number "zero".


### Exercise 3: Git Commit

OK, now you've made some changes to your bottles program.   The next thing you should do it commit that code to your git
repository.  Use the same sets that you used above -- `git add`, `git commit`, and `git push` -- to commit those changes
and push them back to the main repository on Gitlab.

### Exercise 4: Swap driver and navigator

Now, swap driver and navigator.  On the 2nd computer, you should then `git pull`.  Run the program again with `python
bottles.py` and make sure that the 2nd computer has all of the changes that you made.

### Exercise 5: 5 bottles

The song right now starts with only 2 bottles.  That's not very many.  Expand the song to start with 5 bottles of your
favorite beverage, and then count down until there are none left.

### Exercise 6: Git Commit

OK, now you've made some more changes to your bottles program.  You should commit that code to your git repository.  Use
the same sets that you used above -- `git add`, `git commit`, and `git push` -- to commit those changes and push them
back to the main repository on Gitlab.

Then, swap again, and have the other person `git pull` on their computer, and see if all features added by both people
are on both computers.




## Troubleshooting git clone

Sometimes, you get an error message when you try to download the repository using `git clone`.

#### NetID

When you run `git clone` the first time, it asks you for your username and password.   The most common problem is that
students put `user@msu.edu` in the box.  Do NOT do that.  Just put your username in the box -- do NOT put the `@msu.edu`
part.

If you did that, then try running `git clone` again, and use the correct username.   IF it doesn't ask you for your
username, then Windows is trying to remember your (incorrect) username.

#### Windows remembering your password

When you first run `git clone`, git will ask you for your username and password. both MacOS and Windows will remember
these -- it won't ask you for them again after the first time.   However, sometimes you get something wrong the first
time.  Generally Mac handles this well -- if it didn't work, then Mac will prompt you again next time.

However, Windows sometimes remembers this wrong username/password, and then `git` commands don't work.  To fix this, go
down to the start bar and search for "Windows Credential Manager".  On the page that comes up, look through the list for
the git/Gitlab credential.  I usually just delete the entry for git/Gitlab.  Then try running `git clone` again, and it
should prompt you.


## Troubleshooting git commit

This section contains extra instructions for troubleshooting problems with `git commit`. Specifically, do this if no
file opens when you `git commit` and you immediately get an error message.

#### VS Code

The most common problem with VS Code is the need to install the shell utilities.
Open VS Code, go to the menu, and then choose "Install 'code' command in path".  That will
hopefully help git to open vs code properly.  

#### Windows

If you can't get Notepad++ or VS Code  working, then on Windows, just run this command:
```
git config --global core.editor notepad
```

That will tell git to use the built-in notepad when it needs information from you, which works fine.

#### Another Alternative

If you can't get an editor to work for `git commit`, there is another option.  You can specify your commit message on
the command line.  You MUST have a commit message, but it can be short.

To do so, use the `-m` option to `git commit`:

```
git commit -m "Message goes here, in quotes"
```


