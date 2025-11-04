---
title: Reddit Data Analysis
nav_exclude: false
visible: true
parent: Extra
nav_order: 1
has_children: false
---

# Reddit Data Analysis Challenge
In this challenge, you will collect, analyze, and tell a "data story" about a subreddit or term from subreddit. This is a non-trivial challenge and exemplifies a real-world task of using authenticated APIs to collect real data. It also exemplifies the real challenge of working with raw data, which can require substantial cleaning prior to analysis.  

**What you'll learn:**
- How to use the Reddit PRAW API to collect data from Reddit
- How to analyze data from Reddit

## Setup

1. Before you start, you will need to have a Reddit account. Click the "Login" button in the top left corner [here](https://www.reddit.com/).

2. Next, you need to go to the [Reddit apps page](https://www.reddit.com/prefs/apps/) to register your app. "App" seems like a misleading word here in the context of how that term is used in everyday language. Registering your "app" just means you are registering that you are creating a Python program that is going to try to talk to Reddit. By registering your app, you connect your program to your account identity which holds you account to rate limits and other terms of service asserted by Reddit. 

When you register, you will be asked to provide the following:

- **Name:** The name of your app. I would do something that is easily legible to you and to your purpose. For example, if you plan to look at r/meshtastic posts, you could name your app "meshtastic_app".

- **Description:** This describes what your app is doing. This is optional.

- **App Type:** You should select "Script" for this exercise.

- **Redirect URI:** You should enter "http://localhost:8080" for this exercise.

3. Add your API keys to the config file.

Once you complete Step 2, you will get API keys that include:

- **Client Secret:** This appears as "secret" on the screen

- **Client ID:** This appears under the words "personal use script" once you have registered.

- **User Agent:** This appears as the name of your app. 

Add these to 

