---
title: Using command line
nav_exclude: true
visible: false
parent: Reference
nav_order: 3
has_children: false
---

You'll be using command line a lot in this class to run Python programs. Here are some tips and tricks to help you out.

## Command line applications

Both MacOS and Windows come with command line applications preinstalled. In this class we'll be using:

**Windows:** PowerShell  
**MacOS:** Terminal

## Navigating through folders

The most important thing to remember about command line is that it only will let you do things with files if it thinks it's in the same location the file is. That means if the file you want to work with is in the Downloads folder, then command line also needs to be pointed at the Downloads folder before you can do anything with that file. 

Folder structures on computers are nested on multiple levels. It might look like this:

```
geier  
- Desktop  
- Documents  
- - Photos  
- - School  
- - - MI 250  
- Downloads  
```

In this example, the MI 250 folder is inside the School folder, which is inside Documents, which is inside the top level 'geier' folder. To navigate to the MI 250 folder, you have to go through all of its 'parent' folders first.

By default, both PowerShell and Terminal start at a folder named after the computer's user. Desktop, Downloads, and Documents as well as a few other folders are there by default. When you make a new folder, you need to pay attention to where you're putting it in this structure so you can find it again.

In command line, to navigate to a folder, you use `cd`, which stands for 'change directory'. `cd` is not case sensitive (you don't have to use capital letters). To get to the MI 250 folder, I would give this command:
```
cd documents/school/"mi 250"
```

### Getting to a folder fast

There's a neat trick that works in both Windows and Mac OS to get to the folder you want to go to within typing in the full path to get there. 
1. Type `cd` in command line - make sure there is a space after `cd`.
2. Open up the folder you want in File Explorer (Windows) or Finder (Mac OS) -- the normal way of viewing folders. 
3. Drag the folder over to the command line window. When you release your mouse on top of the command line window, that should put the full directory name after `cd`.

### Other useful commands for navigation

A couple of other useful command line commands:
* You can get a list of the files in the current directory with the `ls` command
* You can move up one directory (to the parent directory) with the command `cd ..`
* If you start typing the name of a file or directory, you can hit the Tab key and it will try to automatically finish typing the name of that file/directory for you.

To learn more about navigating through folders with command line, you can read [Navigating the Command Line](http://swcarpentry.github.io/shell-novice/02-filedir/index.html) 
(which I recommend if you haven't worked with the command line before).

## Python's interactive mode (and getting out of it)

To run Python programs in command line, you type `python` (Windows) or `python3` (MacOS) followed by the name of the program. So to run eliza.py, you'd type `python eliza.py` and that will run the program. 

If you only type `python` without giving it a program to run, it will go into interactive mode. You can use this mode to try out short snippets of code to see if it works. We won't be using it much in this class, though. You'll know you're in this mode if you see three arrows (`>>>`) on the last line. 

To get out of this mode, type `quit()` and hit Enter. On Windows, you can also hit Control+Z and then Enter. On MacOS, you can use Control+D.

## More tips

### Saving time

When the space next to the prompt in command line is empty (you haven't typed anything yet), you can hit the "up" arrow on your keyboard - this will autopopulate the last command that was given. If you hit the up arrow multiple times, it will cycle through all of the previous commands you've given it. The down arrow goes the opposite direction through the commands.

## More resources

More information about command line (or 'shell') commands can be found
[here](http://swcarpentry.github.io/shell-novice/reference).