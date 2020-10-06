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

age, gender = 25, "M"

if (age > 30 and gender == 'F'):
    print("Ma'am")
elif (age > 30 and gender == 'M'):
    print("Sir")
elif (age > 19):
    print("Dude")
elif (age > 10 and gender == 'F'):
    print("Girl")
elif (age > 10 and gender == 'M'):
    print("Boy")
else:
    print("Child")