# Lesson 01: Basics

<!-- TOC depthFrom:2 orderedList:true -->

1. [Part A: Opening your Terminal:](#part-a-opening-your-terminal)
    1. [Windows](#windows)
    2. [Mac](#mac)
2. [Part B: Terminal Basics, Moving Around](#part-b-terminal-basics-moving-around)
3. [Part C: Terminal Basics, Looking inside](#part-c-terminal-basics-looking-inside)

<!-- /TOC -->

## Part A: Opening your Terminal:

### Windows

1. Press `win`+`R`
2. Type in "Powershell" and press Enter

You should see a blue window with something that looks like this:

```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\jamphan>
```

- The first four lines are just a welcome message, and it may vary. You can ignore all of that.
- The line that has `PS C:\Users\jamphan>` is where you will type in your commands.
- The `PS C:\Users\jamphan>` is called the "prompt". When you see this, powershell is "prompt"-ing you to type in a command.
    - The `PS` means "Powershell"
    - The path `C:\Users\jamphan` is the current folder you are working from. (`jamphan` is my username, so you should see your username instead)
    - The `>` is the prompt to signal where the text you enter will start.

### Mac

1. Open up Spotlight (`cmd`+`Space`)
2. Type in "Terminal" and press Enter

You should see a black or white window with something that looks like this:

```
jamphan-mac:~ jamphan$
```

- The text `jamphan-mac:~ jamphan$` is called the "prompt". When you see this, powershell is "prompt"-ing you to type in a command.
    - The text before the `:` is your computers name (you probably entered this in way back when you first booted your computer). My computer is called `jamphan-mac`
    - The `~` is short-hand for your Home folder, and indicates you are currently working from your Home folder
    - `jamphan` is my username, you should see your own.
    - `$` is the prompt to signal where the text you enter will start.

## Part B: Terminal Basics, Moving Around

**For simplicity, I'm just going to use `$` as shorthand for the prompt, do not enter this character in!**

First, lets make a folder where we will save all of our work. In `File Explorer` (Windows) or `Finder` (Mac) create a folder in your Desktop called "pytutes"

Now in your terminal:

```
$ cd ~/Desktop/pytutes
```

You should see your prompt change:

- For Windows, you should see something like `PS C:\Users\jamphan\Downloads\pytutes>`
- For Mac, you should see `jamphan-mac:pytutes jamphan$`

**Explanation**:
- `cd` is short for "Change Directory", it will move your current working location to a new folder (directory)
- The string of characters following `cd` is the destination you want to change to, in our case `~/Desktop/pytutes` is our destination.
- `~` is shorthand for your Home directory.
    - For Windows, that is `C:\Users\<your username>\`
    - For max, that is `/Users/<your username>/`
- Every home directory has a `Desktop` folder by default, and if you followed the first step, you made a folder on your desktop called `pytutes`.

Now type:

```
$ cd ..
```

- You should now be in `~/Desktop/` (if not, redo the previous command `cd ~/Desktop/pytutes` and retry)
- `..` is short for "one folder up".

Do it again:

```
$ cd ..
```

- You should now be in `~` your Home directory.

## Part C: Terminal Basics, Looking inside
