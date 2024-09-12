---
title: Using Git
nav_exclude: false
visible: true
parent: Reference
nav_order: 4
has_children: false
has_toc: true
---

Working with Git and GitLab allows you to easily share your code with your partner or groupmates in labs and studio. GitLab works as cloud storage for your project, which every member of the project can then pull down onto their own computers using Git. When you've made the edits you want on your own version of the code, you can then push it back up to GitLab so your teammates can access it.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. Table of Contents
{:toc}
</details>

## Forking a repository

For every lab, a repository will already exist with code files in it that you will use for lab exercises. You will need to make a copy of it so you can work with the files inside: only one person per pair needs to do this step.

1. On the GitLab repo for the lab, find the Fork button - it should be on the top right of the page. Click it.
2. It will ask you for a 'namespace': there should be only one option, with your username. If you have multiple options, make sure you choose your username as the name space.
3. Leave everything else on the page as-is and click the blue "Fork project" button at the bottom.
4. Be patient - it might take a few moments. Once the fork is complete, it will take you to the project page for your newly forked project. You'll be able to tell because if you look at the breadcrumbs above the project name, instead of saying "MI 250 > Name of Lab", it should say your username instead of MI 250.
5. Add your groupmates to the project. Also add Caitlin (geierac) and Shiyu (xiangsh2). (For a reminder of how to do this, see [sharing a repository with other people](#sharing-a-repository-with-other-people).)

Note: if you get a 404 error, it's because GitLab tried to load the repository page for your new forked repo before the fork was complete. Wait a few seconds and try reloading the page. If that doesn't work, go to your main projects page by clicking the fox icon in the upper left and see if the project you created is in the list.

## Creating a new repository

For every studio, one member of your group will need to create a new repository. 

1. From your projects page in GitLab (this is the main landing page when you first log into Gitlab), click the blue "New Project" button
2. Choose the "Create blank project" option
3. On the Create blank project page, give your project a name (Studio 3 works fine, but you can name it whatever you want). Keep all the other options on that page as-is and click the blue "Create project" button at the bottom.
4. Add your groupmates to the project. Also add Caitlin (geierac) and Shiyu (xiangsh2). (For a reminder of how to do this, see [sharing a repository with other people](#sharing-a-repository-with-other-people).)

## Sharing a repository with other people

If you want other people to be able to see your code, you need to share the repository with them. This includes your partner or groupmates in class, and Caitlin and Shiyu. To share a repo, you need to add the people you want to share with as members of that repo.

1. Go to the main page for your project in Gitlab
2. In the left hand menu, find Manage (it should be near the top.) Hover over it and you'll see a smaller menu - choose "Members" in that menu.
3. On the Members page, click the blue "Invite Members" button on the top right.
4. In the window that pops up, add each of your partners / groupmates - you can search for them using their MSU NetID (same as their MSU email). Also add Caitlin (geierac) and Shiyu (xiangsh2). Make sure to select the Maintainer role before clicking Invite at the bottom!
5. Everyone you added should show up on the list on the Project Members page - double check that they all have the Maintainer role. Everyone in that list will be able to see and edit your project.

## Git clone: Getting a repository onto your computer for the first time

Cloning a repository is always done in three steps:
1. Fork the repository (you will do this for every lab) or create a new repository (for studios)
2. In command line, use `cd` to navigate to the place on your computer where you want the repository to live
3. Copy the https link for the respository you want to clone
4. Use `git clone` followed by the respository link to clone your repository onto your computer

A clone command might look like this:

```
git clone https://gitlab.msu.edu/geierac/git-and-gitlab.git
```

Make sure the last part of the link matches the name of the repository you want to clone! Also make sure it's your or your partner's username in the middle of the link, and not MI-250.

## Git add, commit, push: Pushing code from your computer to GitLab

There are three steps to getting your code from your computer up to GitLab (or any Git repository in the cloud) - staging (add), committing, and pushing.

1. `git add <filename>` will add a file to the staging area - when it's staged, it means you've decided you want to save those changes to the cloud version of the repository. If you made changes to a lot of files and want to save them all at once, use `git add -A`.
2. `git commit -m "<your commit message>"` is what you run once all the files you want to save have been staged. The commit message should say, very briefly, what changes you made and why.
3. `git push` is the final step - this command takes all of your changes and pushes them up to the cloud version of the repo.

If any issues happen while you're giving these commands, errors usually will show in red text in command line. You can also get an idea of where you are in the process and what you need to do next by using `git status`.

## Git pull: Pulling changes from GitLab onto your computer

Other people might change the code in the repository after you've cloned it. `git clone` captures a snapshot in time and saves that snapshot to your computer - it represents the state of the project at the exact time you cloned it, and it doesn't update automatically when changes are made to GitLab. You have to pull down those changes manually. 

To do that, use this command:

`git pull`

This will pull all of the new stuff from GitLab into the version of the repo on your computer. This should be the first thing you do before you start editing.

## Avoiding Git conflicts

If multiple people are making changes to a repository at the same time, sometimes there can be conflicts. This especially happens in studios, where different people might be working on different aspects of the studio at the same time. A few tips for avoiding conflicts:
* Always use `git pull` before you start working on a file to make sure you have the most updated version.
* When you're done working on a file, always add, commit, and push your code to Gitlab.
* For studios, talk at the beginning of class about how you might split up the work. If it makes sense to have multiple people writing code at the same time, try each using different files to work on small pieces and combining your code into one file later. Keep talking with everyone in your group so that everyone knows what the others are working on and in what files.

### Dealing with conflicts

If two people have edited the same file at the same time, this is where you will likely get a merge conflict when trying to save changes to GitLab. The person experiencing the conflict should follow these steps to merge the changes together:
1. use `git pull` to make sure all of the latest changes are on your computer
2. open up the file with the conflict in your text editor. If it's already open, close it and open it again to make sure you're in the latest version of the file.
3. In the file, you should see conflict markers: these look like `<<<<<<<<< HEAD`, `========`, and `>>>>>>>>`. The code inside the markers is what's in conflict. Edit this code to make sure it's what you and your partner want it to look like. When you're done, *delete the conflict markers* and save the file.
4. Use add, commit, and push like usual on the file. This should complete the merge.

For more details, see [Resolving a merge conflict using the command line](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line){:target="_blank"}.

If you've tried to fix the conflict but it's not working, `git restore` and `git reset` are two options to get your repository back in working order. These options will delete any changes you've made since the last commit. If you want to save those changes, create a new file as a temporary place to keep your code and copy and paste your changes into that file. You can move them back in later, once Git is back in order. 
* `git restore <filename>`: use this if you forgot to pull your partner's changes before starting to make your own changes. This will restore the file to the last time it was committed, which will *undo* any changes made to it.
* `git reset --hard`: use this if you've tried to commit changes already. This command will reset the local version of your repository to the last commit that went through, and will delete any changes you've made since then.

If you do either of these, make sure to use `git pull` immediately after to make sure the respository is up to date. For more details, see [Git restore and Git reset](https://academind.com/tutorials/git-restore-and-git-reset){:target="_blank"}.

Don't worry if you run into a conflict; Caitlin and Shiyu are always around to help you resolve them! 
