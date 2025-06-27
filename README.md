## Basic Structure

The course is divided into "labs" and "studios", and each week students do one lab and one studio. A lab is a set of
pre-written exercises designed to slowly get more complicated, and give students an opportunity to practice a specific
new skill that they are trying to develop for that week.  A studio is a very open-ended, creative project intended to
give the students an opportunity to use their skills for something interesting, and aren't necessarily tied to the
skills from the lab (though often use them).  To help prepare the students for their work, there is an assigned reading
for each week to help give students the conceptual background they need to understand the skills they are working on.

Readings are in the `readings/` folder, and each one has a "topic" that they are reading about.  A reading should always
have the "readings" layout, which is automatically added to all files in the "readings" folder.  They are assigned to
weeks by giving them a "parent" which is the week name (e.g. `"Week 12"`) that they go with. To move one to a different
week, just change its parent.

Labs are in the `labs/` folder, and each one has a name.  Most of the file is the text of the exercises.  In the header,
the lab will have a "topic:", which is how it is listed in the schedule. It can be assigned a "git", which is a link to
the repository for the week.  And, like readings, it should have a "parent" that indicates which week the lab should be
done.  All labs should have `layout: lab`, which is automatically added to all files in the `labs/` folder.

Studios are in the `studios/` folder, and each one has a name.  Most of the file is the text of the studio.  The header
has a "topic:", which is how it is listed in the schedule, and a "parent" that indicates which week it should be done
in. All studios should have `layout: studio`, which is automatically added to all files in the `studios/` folder.

All files are written in [Markdown](https://daringfireball.net/projects/markdown/syntax), in a variant known as 
[GFM](https://github.github.com/gfm/).

### Visibility

By default, all readings are always visible, and all labs and studios are invisible.  This means that they don't appear
in the schedule of classes.

To make a lab or studio visible to the students, edit the file and change the header to say `visible: true`. Once
compiled, this will make the lab or studio visible to students. By default, also, labs and studios do not appear in the
table of contents on the left hand side of the page.  I also change `nav_exclude: false` to false at the same time as I
make them visible, so that they appear on that ToC.

### Compiling As You Work

When you are working on the class and making changes, you usually want to be able to see what it looks like.  To do
that, you can compile the website on your personal computer using the `jekyll` command.

To compile the website, the same way it will look on the final site, I use the this command:

    jekyll serve --watch

That command will compile the website, and create a web server on your computer where you can view the compiled site by
going to <http://localhost:4001>. It will also watch for changes you make to the file, and automatically recompile and
update the website as you make and save changes to the source files.

You can also view a "working" version of the website, where it ignores the visibility rules and just shows you
everything on the website:

    jekyll serve --watch --config _config.yml,_working.yml,_local.yml

(This just specifies additional config files.  the `_config.yml` is the default configuration file for the site, and is
automatically loaded normally.  the `_working.yml` file creates a working version of the website and ignores visibility
rules.  And the `_local.yml` files changes the URL for the working version so that it is easier to use and just serves
cleanly from your local computer.)

## Setting up the Class

As you set up the class for the semester, you'll have to do a few things.

1. Update dates.  Go through all of the files in the `week/` folder, and update the dates for this semester.  
   Each week has a number (e.g. `title: "Week 5"`) and dates associated with it (`week: 5 (Feb 13-15)`).  This controls
   what the weeks look like in the schedule.

2. Enter in any holidays or breaks.  I've created files for mlk day (in `labs/mlk.md`) and spring break
   (`labs/springbreak.md` and `studios/springbreak.md`).  If you need them, edit them so they appear at the right time
   in the schedule. If you don't, change them to `published: false` and they won't be compiled.

3. Go through the syllabus and change/update anything you want to change or update.  Obviously, office hours tend to
   change every semester.


### Moving Things Round

One of the most common things I do when I am planning the class is moving things around -- I'll change the order that
things happen in.  That should be pretty easy in this structure: just open the file for the lab or studio you want to
move, and change the `parent` to a different week number.  When it recompiles, it should automatically move to the right
place.

I do this a lot.  I'll move things around in the semester a lot when planning until I have an order and structure that
I'm happy with.

I also recommend you get familiar with doing this, because I've had to do it in the middle of most semester as I replan
around unexpected cancelled classes due to things like instructor illness, weather, pandemics, or mass shootings.

### Doing a lab on a studio day, or vice versa

Every once in a while, I'll want to do a lab on a studio day, or a studio on a lab day.   That happens, especially if
there is a holiday or a cancelled class day.

This is easy.  To do a lab on a studio day, just open up the lab file and add the line `layout: studio` to the header.
That should move the lab to the studio column in the schedule.   

The same thing works for moving studios to the lab column: just add `layout: lab` to the header, and it'll move the
studio to the lab column for the week.

## Writing Labs and Studios

As you write labs and studios (or update the existing ones), you'll want to link to external things.   Jekyll makes it
pretty easy to create those links.

*To link to an image*: put the image file in the `img/` folder.  Then to link to it, use the jekyll `link` command and
specify the name of the file you are linking to: `![club]({% link img/club.png %})`.  The "Drawing with Functions" lab
has a lot of examples of linking to images.

*To link to another lab/studio*: You can also use the jekyll `link` command, but you specify the name of the source file
you are linking to.  Jekyll will automatically translate that to an appropriate link to the correctly compiled file.
For example, to link to the drawing with functions lab, you would do: 

    A link to the [Drawing with Functions]({% link labs/drawing_with_functions.md %}) lab

## Credit
The resources in this repository were originally developed and designed by Rick Wash (UW-Madison) and Caitlin Geier (MSU). Materials were forked by Morgan Vigil-Hayes in June 2025.

