# ==================================================================================================
"""
Ex. 04b

Summary:
    - We capture user input from the terminal
    - We want to comment on the user's age

Explaination:
    - The input() function polls the user for input; the optional first-argument
      is a prompt message that will be displayed before polling

    - In line 17 we shorten our code by doing several operations in one-line.
      We perform the int() operation on whatever the input() function will return

    - We have multiple branches in our if-else block; If the first statement does
      not match our criteria, then we specify a second criteria using the 'elif'
      (short for else-if) keyword. We continue to do this until we've exhausted
      all of our criterias we wish to check and provide a final 'catch-all' clause
      with 'else'

Activity:
    - What do you expect the program to print if you enter in '25' for your age?
    - How can you fix this?

"""
# ==================================================================================================

age = int(input("How old are you?"))

if (age > 10):
    print("You're a teenager")
elif (age > 19):
    print("You're a young adult")
elif (age > 25):
    print("You're probably having a mid-life crisis right now")
else:
    print("You're getting old")