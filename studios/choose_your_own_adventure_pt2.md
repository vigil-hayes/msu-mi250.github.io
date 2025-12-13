---
parent: Week 3
topic: Choose Your Own Adventure, Pt 2
nav_exclude: true
visible: false
---

<!-- change "Tuesday" to "last week" for spring semester; reverse for fall semester-->

The goal for today's studio is to build onto someone else's story. By doing this, you will get to practice three things:
1. How to upload and share code via GitLab
2. How to fork code from GitLab
3. How to read someone _else's_ code and make sense on it (SUPER VALUABLE!)

This studio is a bit meta because you are going to be choosing your own choose your own adventure game to modify. 

Again, the goal for today is to take joy in creativity and have fun. You must work with at least one other person. This time, you will be using someone else's core story to drive your work, but you will be focused on either polishing or expanding the story.


### Work together

You should work in small groups on this studio. Groups of 2-3 people. Work together to create the story and to write the code. But don't divide up the work; that's no fun. Everyone should work on all parts. If you need to come up with the next step of the story, then get the whole group together and brainstorm the story. If you need to implement a choice in Python, then get the whole group together and work on it until it looks how you want it to. Have one person on the keyboard sharing their screen, and the rest looking over helping (navigating).

Some groups like to start out by writing the story in Google Docs or by mapping out the story paths on paper. That's fine. When you're writing the code, make sure to switch drivers regularly so everyone gets a chance to work on the program! 

## Create a new Git Project (Repository) on GitLab

One person in your group will need to create a **new** Git repository on GitLab and make it internally visible. [Follow the instructions here.](https://docs.gitlab.com/user/project/repository/)

Note that Git is easiest to use when only one person is writing code at any given time; if multiple people are working on the same file, you will run into Git conflicts, which are sometimes hard to resolve. 

## Add your story from Week 2 to the Git Project you just made
For this next step, I recommend using the GitLab Web Editor to support adding new files. The way you can do this is by following Steps 1-5 [in these instructions](https://docs.gitlab.com/user/project/repository/web_editor/#upload-a-file). For Step 6, I suggest following the option outlined in the first bullet point, e.g., committing your changes (new file) to the **main** branch. 

Note that I will talk a bit about the concept of branches in class this week, but probably will not expect you to do too much branching in this class. As someone who has used Git for well-over a decade, branching logic still can give me a headache.

## Update your README for your project
Use the GitLab Web Editor to make changes to your README file using [the instructions for Steps 1-6 here.](https://docs.gitlab.com/user/project/repository/web_editor/#edit-a-file)


You want your README to really sell what is awesome about your adventure. Your README should include:
* A pitch for why someone should want to play your adventure
* A brief description of your adventure
* An overview of the setting of where your adventure takes place
* An overview of the characters in your adventure
* Quick list of themes in your adventure, e.g. "quest" or "comedy" or "romantic" or "spooky"

For Step 7, follow the first bullet point. You will commit to the **main** branch again.

## Share your project
Link your project onto [this shared Google Doc](https://docs.google.com/document/d/1KrOXSCqaPbLw1ZzQZqDZNwvqoC0gtLg3sNIIMKkfQ1o/edit?usp=sharing). Be sure to be logged into your MSU account in order to edit the document.

## Pick a project and clone it
Browse through your classmates' projects and pick one that you think would be fun to add to, embellish, or expand on in some way. When you click the link, you should be taken to the GitLab page for the project.

### Set up GitLab password for HTTPS
On GitLab, you might be prompted by a yellow banner that if you are using SSO (Okta) you need to set a password. I suggest setting a password that you can remember or copy easily from a key ring. You need to have this set up before you can proceed to cloning the repository.

### Fork the repository on GitLab
On GitLab, you will fork the project you chose because your intent is to contribute your changes back to it AND you probably are not a collaborator on the repository. This will allow you to create a fork of the project that you are a collaborator on and then you can make a pull request in the future if you wish to contribute your changes.

### Clone the repository with `git`
Some of you may already have `git` installed. Git is the underlying open source software utility that GitLab (and GitHub) uses to manage software version control. It is a powerful tool for collaboration and developing software. 

You can check to see if `git` is already installed by running in Terminal (Mac OS X or Linux) or PowerShell (Windows) run:
```
git --version
```

You will either see information about the version of `git` that is installed or an error message indicating that your computer has no idea where/what `git` is.

#### If you need to install `git`

**Mac OS X** users should follow [these instructions](https://git-scm.com/downloads/mac) for installing git on their local machine.

**Debian Linux** users should open the Terminal and run `sudo apt install git-all`.

**Windows** users should follow [these instructions](https://git-scm.com/downloads/win) for installing `git` on their local machine.

#### Navigate to the directory where you want to store the project
On my computer, I have a folder at ~/Desktop/MSU/MI250/Repos where I keep my project files. You will need to change directory (cd) in your Terminal (Mac OS X/Linux) or PowerShell to navigate to whatever directory you would like to use.

#### Run `git clone`
Once you have navigated to the correct directory, you should follow the web link to the GitLab Project you decided you wanted to contribute to. At the top right underneath the Project Title, there is a blue button that says "Code". When you click that button, you will be given two options to clone: "Clone with SSH" and "Clone with HTTPS". In this class, we will use HTTPS. Copy the link below "Clone with HTTPS"--it should start with https://gitlab.msu.edu/.

Next, you will run the following on Terminal or PowerShell:

```
git clone [paste_copied_project_URL]
```
where you will replace `[paste_copied_project_URL]` with the URL you just copied from GitLab.

When you hit enter, you will be prompted for your Username. You should use your MSU user name. You will then be prompted for your Password. You should use the Password you set up at the beginning of this lab. 

Once you have entered that information, you will see something like this (though the details will be different):
```
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 9 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (9/9), 4.28 KiB | 1.43 MiB/s, done.
```
Now you have the project cloned! This means that not only do you have a local copy of the project from the GitLab repository, but you also have all the metadata necessary to contribute your changes back to the project on GitLab.

### Modify the Adventure
Now that the Driver has the project cloned, go ahead and start thinking about how you want to modify it. Do you want to add branches? Add a new character? Something else? **DO NOT START CODING YET!***

My suggestion is to first run and play the adventure and then walk through the code to understand how it works. Then spend some time brainstorming how you want to change it. 

Only have the Driver making changes on their laptop. 

#### Create a new branch
Once your Driver has made the changes you wanted to, you will create a new branch for your modifications to live on:

```
git checkout -b <new-branch-name>
```

Where `<new-branch-name>` is the name of your modified version of the adventure. I suggest making this something related to how you have modified the advanture and keeping it pretty short--one word--as a matter of professional best practice.

#### Commit changes to the new branch
Now you will commit your changes to the new branch with a `git add` and `git commit`. This combo stages modified files to be committed for version control (`add`) and then commits them for version control (`commit`). 

```
git add .
git commit -m "<commit-message>"
```

Where `<commit-message>` is a note about what you modified at a high level. Usually 1-2 sentences are sufficient. 

#### Push your changes to GitLab
Right now, your changes are only being tracked on your laptop and nowhere else. Let's make those modifications visible to the rest of the world.

Run:

```
git push -u origin <new-branch-name>
```
Where `<new-branch-name>` is the same name you gave to the branch you created in the checkout stage.

When I run it, I see something like the following:

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 390 bytes | 390.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: 
remote: To create a merge request for annoying, visit:
remote:   https://gitlab.msu.edu/mi-250/dragonslayer/-/merge_requests/new?merge_request%5Bsource_branch%5D=annoying
remote: 
To https://gitlab.msu.edu/mi-250/dragonslayer.git
 * [new branch]      annoying -> annoying
branch 'annoying' set up to track 'origin/annoying'
```

Now, if you go to the web browser to look for the project you modified on GitLab you should notice a couple of things:

1. There is a green banner that notes that you made branch. It also prompts you to make a merge request. This is a request that asks the original owner of the project if they want to integrate your modifications into the main branch of the project.

2. Under the title of the project, you will see a button that has three circles connected by lines and it will say `main`.If you click on that button, you should see a list of branches for the project--including the one you just created and pushed!

### Challenge 1
Add your teamm members as collaborators to your project.
Have other members on your team serve as Driver and clone the project you just created a branch for. Have them create their own branch from main by following the previous steps in the lab OR have them continue contributing to your modified branch by running the following command after running `git clone`:

```
git checkout <branch-name>
```

Where `<branch-name>` is the name of the branch your group just modified. 

When it comes time to commit your updated modifications, run:

```
git add .
git commit -m "<commit-message>"
git push origin <branch-name>
```

### Submit on D2L and Gitlab
Your studio is finished when the class is over - no sooner! You can always continue to add to the story or improve your code.

When you are done, please submit screenshots of your code working (that is, of the program running in Powershell or Terminal) on D2L under Assignments. Every person in the group needs to submit a screenshot. 

Also, include a link to the GitLab for the project you modified (Shiyu and Morgan should be able to access as it is in MSU/studio2).

<!--Also submit your Python program (your .py file that contains your code) on D2L. Again, only one person in the group needs to submit this.-->

<!--See the [Git reference]({% link reference/using_git.md %}) if you need pointers on using Git for studios.>

