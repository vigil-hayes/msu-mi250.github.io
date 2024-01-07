---
title: Turning in work
visible: true
parent: Reference
nav_order: 1
---

This course uses D2L and Gitlab for turning in work. Almost every week, students will be responsible for three turn-ins:
* Homework (individual)
* Code and screenshots for labs (partners)
* Code and screenshots for studios (group)

## Homework

Every week, you will have a small amount of homework. Homework consists of:
1. completing readings (articles and/or videos)
2. responding to what you've read / watched

Readings for each week are located on the [schedule]({% link schedule.md %}) in the 'readings' column. They shouldn't take more than 30 minutes to go through each week.

Responses take the form of a summary+question, to be turned in each week under 'Quizzes' on [D2L](https://d2l.msu.edu/){:target="_blank"}{:rel="noopener noreferrer"}. They have two parts:
* Summary: follow the prompt on the readings page for that week to summarize what you've read
* Question: ask a question about what you've read
See the syllabus[link] for more details.

Make sure to turn this in before the first class of each week.

## Code and screenshots for labs

Every week, usually on Mondays, we'll have a lab. Labs are done in pairs. At least one person in each pair will need to turn in:
* code
* screenshots showing code working

Screenshots are turned in on D2L under 'assignments' - the assignment will be marked as a lab with the appropriate week (like "Week 1 Lab"). Rule of thumb: every time you complete an exercise, take a screenshot of the code you wrote working.

In the first two weeks, everyone (including code files) will be turned in on D2L. Starting in week 3, code is turned in on Gitlab. Both partners should be members of the Gitlab repository for the lab.

### Using Gitlab for labs

Each lab has an associated Gitlab repository. Starting in the 3rd week of class, you'll be using Git to clone (make a copy of) the repository on your own computer, which you can then use to send changes back up to the repository in Gitlab. 

For every lab, follow these steps before you start working:
1. one person will *fork* the lab, which creates new version in Gitlab under their username
2. the person who forked the lab should add their partner and also Caitlin (geierac) and Jack (waierjac) as administrators to the newly forked repository
3. the person who will be driving first clones the repository onto their own computer using git

When trading places between driver and navigator:
1. the driver should push all of the code they changed to the Gitlab repo before the navigator becomes the driver
2. the new driver (who used to be the navigator) either clones the repository onto their computer OR uses `git pull` to bring all of their partner's changes down onto their own computer. Only use `git pull` if there's already a cloned repository on your computer

## Code and screenshots for studios

Most weeks on Wednesdays, we'll have a studio. Studios are done in groups of 2-4. At least one person in the group will need to turn in:
* code
* screenshot(s) showing code working

Screenshots are turned in on D2L under 'assignments' - the assignment will be marked as a studio with the appropriate week (like "Week 3 Studio"). The best time to take screenshots is at the end of the studio when everything is working. If you're not sure you'll be able to get something working, take screenshots as you go.

### Using Gitlab for studios

For every studio, follow these steps before you start working:
1. one person in the group will create a *new* repository in Gitlab, named the same as a the studio
2. the person who created the repository should add everyone in their group and also Caitlin (geierac) and Jack (waierjac) as administrators to the newly forked repository

## Avoiding Git conflicts

If multiple people are making changes to a repository at the same time, sometimes there can be conflicts. This especially happens in studios, where different people might be working on different aspects of the studio at the same time. A few tips for avoiding conflicts:
* Always use `git pull` before you start working on a file to make sure you have the most updated version.
* When you're done working on a file, always add, commit, and push your code to Gitlab.
* For studios, talk at the beginning of class about how you might split up the work. If it makes sense to have multiple people writing code at the same time, try each using different files to work on small pieces and combining your code into one file later. Keep talking with everyone in your group so that everyone knows what the others are working on and in what files.

Don't worry if you run into a conflict; Caitlin and Jack are always around to help you resolve them! 