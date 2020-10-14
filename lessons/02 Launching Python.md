# Lesson 02: Launching Python

<!-- TOC depthFrom:2 orderedList:true -->

1. [Part A: Checking Python's Version](#part-a-checking-pythons-version)
2. [Part B: Running Python](#part-b-running-python)
3. [Part C: Your First Python commands](#part-c-your-first-python-commands)
4. [Part D: Leaving Python](#part-d-leaving-python)
5. [Part E: Your First Python Script](#part-e-your-first-python-script)
6. [Part F: `print()`, Hello World!](#part-f-print-hello-world)

<!-- /TOC -->

## Part A: Checking Python's Version
**Remember, the `$` is the Prompt, don't type it in!**

In your terminal, type:

```
$ python --version
```

You should see text written in the next line like `Python 3.9.0`.

- We told the terminal to run the `python` program.
- The words following `python` are sent to the `python` program, in this case `--version` tells Python to check the python version.
- Python then completed the requested task by returning its version.

## Part B: Running Python
**Remember, the `$` is the Prompt, don't type it in!**

In your terminal, type:

```
$ python
```

You should see something like:

```
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- The first line will vary depending on your OS.
- The `>>>` is **Python's Prompt** (not your terminal's prompt!), Python is waiting for you to enter in a *python* command for it to run.

Now try enter in `ls`:

```
>>> ls
```

You should see something like

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined
```

Python is complaining that you entered a command it does not recognise. Remember! Python is prompting you (`>>>`). You have to type in Python commands

## Part C: Your First Python commands

**Remember, the `>>>` is the Python Prompt, don't type it in!**


Type in:

```
>>> 2*3
```

You should see Python return `6`

Now try:

- ```>>> 1/2```
- ```>>> 1+1```
- ```>>> 1+1.0```

Here you can see Python accepts commands one at a time, and returns the result everytime.

## Part D: Leaving Python

To leave python, type:

```
>>> quit()
```

## Part E: Your First Python Script

In your `~/Desktop/pytutes` folder, create a file called `02e.py`.

In your text-editor, type in the following and save the file.

``` py
2*3
print(1/2)
```

Now in your terminal, type in the two commands:

```
$ cd ~/Desktop/pytutes
$ python 02e.py
```

You should see:
```
$ python 02e.py
0.5
```

**Explanation**:

- We've created a Python script, and told Python to run the commands in the script.
- When we typed in `python 02e.py`;
    - We told the terminal to launch the `python` program
    - We then "passed" the value `02e.py` to Python (similar to how we passed `--version`)
    - Python then attempts to read the contents of the file, and if the commands in them are valid Python commands, then Python will run them.
- In our Python script;
    - We entered commands similar to in the commands in [Part C](#part-c-your-first-python-command).
    - Each command has its own line in the file
    - However, unlike Part C, Python only displayed the result of one command. That is because when we are writing scripts, we must explicity tell Python when to display information using the `print()` function.

## Part F: `print()`, Hello World!

In your `~/Desktop/pytutes` folder, create a file called `02f.py`.

In your text-edit, type in the following into your new file and save the file.

``` py
print("Hello, World!")
```

Now in your terminal:

```
$ python 02f.py
```

**Explaination**:

- You should see `Hello, World!` without any quotation marks.
- When we want to handle actual displayable words, we have to wrap them in quotations `"`. This is how we signal to python that we are dealing with the literal word, and not some fancy Python command. In Python's eyes:
    - `print` is the function to display text
    - `"print"` is the literal word "print".
- If you were to try printing text without the qutotation marks, Python will get confused, and think you are trying to run a command called `Hello`.



